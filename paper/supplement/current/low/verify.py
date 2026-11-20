#!/usr/bin/env python3
"""Reconstruct and verify the finite arithmetic used by the low-bias proof.

Requires Python 3 and SymPy. No network access, numerical sampling,
historical status records, or generated coefficient cache is used.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

BASE = Path(__file__).resolve().parent
GROUPS = {
    "common": [
        "marker_and_local_identities.py",
        "master_local_identity.py",
        "calibrated_cumulative_head_identities.py",
        "lambert_head_scale_identities.py",
    ],
    "q0": ["low_u_selfcontained_fixed_arithmetic_20261006.py"],
    "q1": ["low_q_full_coupled_certificate.py"],
    "q2": ["mid_q_full_same_e_certificate.py"],
    "q3": [
        "middle_q_coupled_certificate.py",
        "hard_d_coupled_certificate.py",
        "finite_h_quarter_certificate.py",
    ],
}


def main():
    if sys.flags.optimize or not __debug__ or os.environ.get("PYTHONOPTIMIZE") not in (None,"","0"):
        raise RuntimeError("Exact verification requires assertions; unset PYTHONOPTIMIZE and do not use -O.")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--group", choices=["all"]+list(GROUPS), default="all")
    ap.add_argument("--log-dir", type=Path, default=BASE/"verification_logs")
    args = ap.parse_args()
    records = json.loads((BASE/"sources.json").read_text())
    byname = {Path(r["script"]).name:r for r in records}
    names = [n for g,nn in GROUPS.items() if args.group in ("all",g) for n in nn]
    for record in records:
        path=BASE/record["script"]
        if hashlib.sha256(path.read_bytes()).hexdigest()!=record["sha256"]:
            raise RuntimeError("Arithmetic source hash mismatch: "+record["script"])
    args.log_dir.mkdir(parents=True,exist_ok=True)
    env=os.environ.copy()
    env.pop("PYTHONOPTIMIZE",None)
    env["PYTHONDONTWRITEBYTECODE"]="1"
    results=[]
    started=time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="gw-low-exact-") as work:
        for name in names:
            begin=time.perf_counter()
            print("Reconstructing "+name,flush=True)
            log=args.log_dir/(Path(name).stem+".log")
            with log.open("w",encoding="utf-8") as stream:
                cp=subprocess.run([sys.executable,"-B",str(BASE/"checks"/name)],
                                  cwd=work,env=env,stdout=stream,stderr=subprocess.STDOUT)
            result={"script":name,"returncode":cp.returncode,
                    "seconds":round(time.perf_counter()-begin,3),
                    "log":str(log.resolve()),
                    "sha256":byname[name]["sha256"]}
            results.append(result)
            if cp.returncode:
                print(log.read_text()[-12000:],file=sys.stderr)
                raise SystemExit("FAILED: "+name)
            print("PASS "+name+" ("+str(result["seconds"])+" s)",flush=True)
    datasets=[]
    for name in names:
        index=BASE/"data"/(Path(name).stem+"_index.json")
        if index.exists():
            datasets.extend(json.loads(index.read_text()))
    data_report={"status":"PASS","group":args.group,"tables":datasets,
                 "table_count":len(datasets),"compressed_bytes":sum(d["bytes"] for d in datasets),
                 "stored_rational_entries":sum(d["entries"] for d in datasets)}
    (BASE/"data"/("index_"+args.group+".json")).write_text(json.dumps(data_report,indent=2)+"\n")
    report={"status":"PASS","group":args.group,"arithmetic_only":True,
            "seconds":round(time.perf_counter()-started,3),"checks":results,"data":data_report,
            "scope":"Finite rational identities, complete coefficient reconstructions, Bernstein signs and exceptional exact Sturm chains. Analytic proof is in the manuscript."}
    (args.log_dir/("result_"+args.group+".json")).write_text(json.dumps(report,indent=2)+"\n")
    print("PASS all requested low-region arithmetic checks; "+str(len(results))+" programs.",flush=True)
    print("The analytic law/response, infinite-tail, and domain arguments are proved in the manuscript.",flush=True)


if __name__=="__main__":
    main()
