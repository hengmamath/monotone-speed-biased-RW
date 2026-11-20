"""Lossless tables for the exact arithmetic currently being checked."""
from pathlib import Path
from fractions import Fraction
from math import comb
import gzip
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parents[1]/"data"
ROOT.mkdir(parents=True,exist_ok=True)
PREFIX=Path(sys.argv[0]).stem
INDEX=[]
COUNTER=0


def rational(value):
    try:
        return Fraction(value)
    except TypeError:
        if hasattr(value,"numerator") and hasattr(value,"denominator"):
            n,d=value.numerator,value.denominator
        else:
            n,d=value.as_numer_denom()
        return Fraction(int(n),int(d))


def emit(kind,entries,variables=(),degrees=None,metadata=None):
    """Sparse exact table; all omitted slots within degrees are zero."""
    global COUNTER
    COUNTER+=1
    path=ROOT/(PREFIX+"_"+str(COUNTER).zfill(3)+"_"+kind+".jsonl.gz")
    if hasattr(entries,"items"):
        entries=entries.items()
    entries=list(entries)
    header={"schema":"exact-rational-sparse-v1","kind":kind,
            "variables":list(map(str,variables)),
            "degrees":None if degrees is None else list(map(int,degrees)),
            "entries":len(entries),"implicit_zero":True,
            "metadata":metadata or {}}
    with gzip.open(path,"wt",encoding="utf-8",compresslevel=6) as out:
        out.write(json.dumps(header,separators=(",",":"))+"\n")
        for indices,value in entries:
            if not isinstance(indices,(tuple,list)):
                indices=[indices]
            value=rational(value)
            out.write(json.dumps([list(map(int,indices)),str(value.numerator),str(value.denominator)],separators=(",",":"))+"\n")
    record={"file":path.name,"kind":kind,"entries":len(entries),
            "bytes":path.stat().st_size,"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
            "metadata":metadata or {}}
    INDEX.append(record)
    (ROOT/(PREFIX+"_index.json")).write_text(json.dumps(INDEX,indent=2)+"\n")
    return record


def polynomial(poly,kind="power",metadata=None):
    return emit(kind,poly.terms(),poly.gens,poly.degree_list(),metadata)


def bernstein_from_mixed(co,de,axis,metadata=None):
    groups={}
    for mo,value in co.items():
        groups.setdefault(mo[:axis]+mo[axis+1:],{})[mo[axis]]=rational(value)
    result={}
    for key,bb in groups.items():
        for j in range(de[axis]+1):
            value=sum((v*Fraction(comb(j,k),comb(de[axis],k)) for k,v in bb.items() if k<=j),Fraction())
            if value:
                result[key[:axis]+(j,)+key[axis:]]=value
    return emit("bernstein",result,("coordinate_0","coordinate_1","coordinate_2"),de,metadata)


def sturm(poly,sequence,metadata=None):
    polynomial(poly,"sturm_input",metadata)
    entries=[]
    for j,term in enumerate(sequence):
        for (power,),value in term.terms():
            entries.append(((j,power),value))
    return emit("sturm_sequence",entries,("sequence_index","power"),
                (len(sequence)-1,max(p.degree() for p in sequence)),metadata)
