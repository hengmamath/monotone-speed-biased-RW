"""New Q1 theta leaf from its full Lambert upper bound, finite convolutions.
No old code, Bernstein transform, Sturm chain, grid or saved coefficient input.
Author validation only; independent AI audit is separate.
"""
from fractions import Fraction as F
from pathlib import Path
import json
def add(*ps):
    out={}
    for p in ps:
        for k,v in p.items(): out[k]=out.get(k,F())+v
    return {k:v for k,v in out.items() if v}
def sc(p,c): return {k:F(c)*v for k,v in p.items() if c*v}
def mul(*ps):
    out={(0,0):F(1)}
    for p in ps:
        nxt={}
        for (i,j),a in out.items():
            for (k,l),b in p.items():
                ix=(i+k,j+l);nxt[ix]=nxt.get(ix,F())+a*b
        out={k:v for k,v in nxt.items() if v}
    return out
def pw(p,n):return mul(*([p]*n))
def K(c):return {(0,0):F(c)} if c else {}
q,c={(1,0):F(1)},{(0,1):F(1)}
L=add(K(1),c);qm=add(q,K(1));B=add(q,K(2),c)
C=add(K(24),sc(c,12),sc(pw(c,2),-2),pw(c,3))
Dt=add(sc(q,16),K(6),sc(pw(q,2),12),sc(mul(c,q),5),sc(mul(c,pw(q,2)),6))
d=add(K(1),sc(mul(c,q),-1))
# Positive denominator 24*L*(q+1)^2*B^3*C*Dt.
terms=[sc(mul(L,pw(qm,2),pw(B,3),C,add(sc(q,6),K(5))),48),
       sc(mul(L,pw(B,3),C,Dt),-24),
       sc(mul(pw(C,2),pw(qm,2),pw(B,2),Dt),-1),
       sc(mul(pw(L,2),pw(qm,2),B,C,Dt),-12),
       sc(mul(pw(L,2),add(pw(L,2),d),pw(qm,2),Dt),-48)]
N=add(*terms)
assert max(i for i,j in N)==6 and max(j for i,j in N)==9
rows=[]
lines=['# Q1 θ：七个 q 次分组的准确有限卷积输出','',
       '系数向量按 c^0..c^9 升序，全部零槽保留。', '',
       '|q次数|完整 c 系数向量|舍去正项、c≤1/6 的常数下界|保留线性正项的系数下界|',
       '|---|---|---|---|']
for i in range(7):
    cs=[N.get((i,j),F()) for j in range(10)]
    lower=cs[0]+sum(min(v,F())/F(6)**j for j,v in enumerate(cs) if j)
    linear=cs[1]+sum(min(cs[j],F())/F(6)**(j-1) for j in range(2,10))
    rows.append({'q_degree':i,'c_coefficients':[str(v) for v in cs],
                 'constant_lower':str(lower),'linear_coefficient_lower':str(linear)})
    lines.append('|'+str(i)+'|'+','.join(map(str,cs))+'|'+str(lower)+'|'+str(linear)+'|')
    assert lower>0 or (cs[0]>0 and linear>=0), 'candidate elementary bound failed'
lines += ['','AUTHOR PASS: all seven complete q groups positive from the displayed elementary bounds.']
base=Path(__file__).with_suffix('')
for suf,payload in (('.generated.md','\n'.join(lines)+'\n'),('.exact.json',json.dumps({'method':'original numerator finite convolution; seven grouped scalar bounds','groups':rows},indent=2)+'\n')):
    out=base.with_name(base.name+suf);assert not out.exists();out.write_text(payload)
print('AUTHOR PASS: complete original theta difference, seven q groups, each positive.')
print('Finite convolution identity/degree<=6,9 and rational bound verified; no old 70-entry certificate executed.')
