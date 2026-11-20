#!/usr/bin/env python3
"""Independently unpack and validate the complete lossless table inventory."""
from pathlib import Path
from fractions import Fraction
import argparse
import gzip
import hashlib
import json


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--index",type=Path,default=Path(__file__).resolve().parent/"data/index_all.json")
    args=ap.parse_args()
    manifest=json.loads(args.index.read_text())
    filenames=[table["file"] for table in manifest["tables"]]
    if len(set(filenames))!=len(filenames):
        raise RuntimeError("Duplicate table in the aggregate index")
    if manifest.get("group")=="all":
        actual={path.name for path in args.index.parent.glob("*.jsonl.gz")}
        if actual!=set(filenames):
            raise RuntimeError("Aggregate index does not cover exactly the exported tables: "+
                               repr(sorted(actual.symmetric_difference(filenames))))
        individual={}
        for path in args.index.parent.glob("*_index.json"):
            for table in json.loads(path.read_text()):
                if table["file"] in individual:
                    raise RuntimeError("Duplicate table across program indices")
                individual[table["file"]]=table
        if individual!={table["file"]:table for table in manifest["tables"]}:
            raise RuntimeError("Aggregate and program indices disagree")
    total=0
    compressed_bytes=0
    for table in manifest["tables"]:
        path=args.index.parent/table["file"]
        data=path.read_bytes()
        if len(data)!=table["bytes"] or hashlib.sha256(data).hexdigest()!=table["sha256"]:
            raise RuntimeError("Table identity mismatch: "+path.name)
        compressed_bytes+=len(data)
        with gzip.open(path,"rt",encoding="utf-8") as stream:
            header=json.loads(next(stream))
            if header["schema"]!="exact-rational-sparse-v1" or header["kind"]!=table["kind"]:
                raise RuntimeError("Table schema or basis mismatch: "+path.name)
            if header["metadata"]!=table["metadata"]:
                raise RuntimeError("Table metadata mismatch: "+path.name)
            indices=set()
            for line in stream:
                index,numerator,denominator=json.loads(line)
                index=tuple(index)
                if index in indices:
                    raise RuntimeError("Duplicate coefficient: "+path.name)
                indices.add(index)
                if any(k<0 for k in index):
                    raise RuntimeError("Negative polynomial power: "+path.name)
                if header["degrees"] is not None and len(index)!=len(header["degrees"]):
                    raise RuntimeError("Coefficient dimension mismatch: "+path.name)
                if header["degrees"] is not None and any(k>d for k,d in zip(index,header["degrees"])):
                    raise RuntimeError("Coefficient outside declared degree: "+path.name)
                n,d=int(numerator),int(denominator)
                if d<=0 or Fraction(n,d).denominator!=d:
                    raise RuntimeError("Noncanonical exact rational: "+path.name)
        if len(indices)!=header["entries"] or len(indices)!=table["entries"]:
            raise RuntimeError("Coefficient count mismatch: "+path.name)
        total+=len(indices)
    if total!=manifest["stored_rational_entries"]:
        raise RuntimeError("Total rational-entry count mismatch")
    if len(manifest["tables"])!=manifest["table_count"] or compressed_bytes!=manifest["compressed_bytes"]:
        raise RuntimeError("Total table count or compressed size mismatch")
    print("PASS: unpacked",len(manifest["tables"]),"exact tables with",total,"rational entries.")
    print("Compressed table bytes:",manifest["compressed_bytes"])


if __name__=="__main__":
    main()
