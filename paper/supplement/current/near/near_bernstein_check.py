"""Exact integer Bernstein certificates for explicitly generated near targets."""
import argparse
import json
import math
import pickle
import time
from fractions import Fraction
from pathlib import Path
import sympy as sp

DATA=Path(__file__).with_name('near_arithmetic_data')
L,u=sp.symbols('lambda u')

def scale_for(poly,box):
    n,m=poly.degree_list();a,b,c,d=map(Fraction,box)
    dl=math.lcm(a.denominator,b.denominator);du=math.lcm(c.denominator,d.denominator)
    sl=math.lcm(*(math.comb(n,i) for i in range(n+1)))
    su=math.lcm(*(math.comb(m,j) for j in range(m+1)))
    return dl**n*du**m*sl*su

def mapped_power(poly, box):
    n,m=poly.degree_list()
    a,b,c,d=map(Fraction,box)
    dl=math.lcm(a.denominator,b.denominator)
    du=math.lcm(c.denominator,d.denominator)
    al=int(a*dl); wl=int((b-a)*dl)
    au=int(c*du); wu=int((d-c)*du)
    vals=[[0]*(m+1) for _ in range(n+1)]
    for (i,j),v in poly.terms():
        assert sp.denom(v)==1,('noninteger numerator coefficient',i,j,v)
        v=int(v)*dl**(n-i)*du**(m-j)
        for k in range(i+1):
            left=v*math.comb(i,k)*al**(i-k)*wl**k
            for q in range(j+1):
                vals[k][q]+=left*math.comb(j,q)*au**(j-q)*wu**q
    return vals

def bernstein(vals):
    n=len(vals)-1;m=len(vals[0])-1
    sl=math.lcm(*(math.comb(n,i) for i in range(n+1)))
    su=math.lcm(*(math.comb(m,j) for j in range(m+1)))
    temp=[[sum(vals[k][j]*math.comb(i,k)*(sl//math.comb(n,k)) for k in range(i+1)) for j in range(m+1)] for i in range(n+1)]
    return [[sum(temp[i][q]*math.comb(j,q)*(su//math.comb(m,q)) for q in range(j+1)) for j in range(m+1)] for i in range(n+1)]

def split_line(vals):
    n=len(vals)-1
    row=vals[:]; left=[row[0]*2**n];right=[row[-1]*2**n]
    for j in range(1,n+1):
        row=[row[i]+row[i+1] for i in range(len(row)-1)]
        left.append(row[0]*2**(n-j));right.append(row[-1]*2**(n-j))
    return left,list(reversed(right))

def split_grid(vals,axis):
    if axis==1:
        pairs=[split_line(row) for row in vals]
        return [p[0] for p in pairs],[p[1] for p in pairs]
    pair=split_grid([list(row) for row in zip(*vals)],1)
    return [list(row) for row in zip(*pair[0])],[list(row) for row in zip(*pair[1])]

def certify(name,maxdepth=20):
    start=time.time()
    with (DATA/(name+'.pickle')).open('rb') as f: item=pickle.load(f)
    num=sp.Poly(item['num'],L,u)
    denpoly=sp.Poly(item['den'],L,u)
    denominator_coefficients=bernstein(mapped_power(denpoly,item['box']))
    assert min(v for row in denominator_coefficients for v in row)>0,(name,'denominator sign')
    initial=bernstein(mapped_power(num,item['box']))
    queue=[('',initial)];leaves=[];largest=0
    while queue:
        path,vals=queue.pop()
        flat=[v for row in vals for v in row]
        if min(flat)>0:
            n,m=num.degree_list()
            scale=scale_for(num,item['box'])*2**(n*path.count('0')+m*path.count('1'))
            leaves.append({'path':path,'positive_scale':str(scale),'minimum':str(min(flat)),'maximum':str(max(flat)),'coefficients':[[str(v) for v in row] for row in vals]})
            largest=max(largest,len(path))
            continue
        if max(flat)<0:
            raise AssertionError((name,'negative box',path))
        depth=len(path)//2
        if depth>=maxdepth:
            print(name,'UNRESOLVED',path,'positive leaves',len(leaves),flush=True)
            return False
        n=len(vals)-1;m=len(vals[0])-1
        axis=(depth%2) if n and m else (0 if n else 1)
        first,second=split_grid(vals,axis)
        queue.append((path+str(axis)+'r',second))
        queue.append((path+str(axis)+'l',first))
    out={'name':name,'box':item['box'],'second_variable':item.get('second_variable','u'),'degrees':num.degree_list(),'numerator':str(item['num']),'denominator':str(item['den']),'denominator_positive_scale':str(scale_for(denpoly,item['box'])),'denominator_coefficients':[[str(v) for v in row] for row in denominator_coefficients],'leaves':leaves}
    (DATA/(name+'.certificate.json')).write_text(json.dumps(out))
    print(name,'PASS','leaves',len(leaves),'max path characters',largest,'seconds',round(time.time()-start,2),flush=True)
    return True

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('names',nargs='*');ap.add_argument('--maxdepth',type=int,default=24);args=ap.parse_args()
    names=args.names or ['j1_curvature','j1_left_derivative','j1_right_derivative','j2','j3','t1']
    ok=True
    for name in names:ok=certify(name,args.maxdepth) and ok
    raise SystemExit(0 if ok else 1)
