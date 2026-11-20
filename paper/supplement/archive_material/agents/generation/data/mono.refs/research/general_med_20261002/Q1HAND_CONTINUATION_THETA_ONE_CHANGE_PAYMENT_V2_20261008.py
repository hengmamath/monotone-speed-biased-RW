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
lines=['# Q1 theta: complete finite convolution and one-change payment','',
       'Coefficient vector order: c^0..c^9; all internal zero slots included.', '',
       '|q degree|complete c coefficient vector|V_i exact|coarse W_i|V_i-W_i positive gap|',
       '|---|---|---|---|---|']
coarse=[15000,42000,31600,10300,-1100,-1280,-210]
vs=[]
for i in range(7):
    cs=[N.get((i,j),F()) for j in range(10)]
    vi=cs[1]+sum(min(cs[j],F())/F(6)**(j-1) for j in range(2,10))
    gap=vi-coarse[i]
    assert gap>0
    assert cs[0]>=0
    rows.append({'q_degree':i,'c_coefficients':[str(v) for v in cs],
                 'V_i':str(vi),'W_i':str(coarse[i]),'positive_gap':str(gap)})
    vs.append(vi)
    lines.append('|'+str(i)+'|'+','.join(map(str,cs))+'|'+str(vi)+'|'+str(coarse[i])+'|'+str(gap)+'|')
assert [N.get((i,0),F()) for i in range(7)]==[576,2496,960,192,0,0,0]
assert all(x>0 for x in coarse[:4]) and all(x<0 for x in coarse[4:])
wp=sum(F(a)*3**i for i,a in enumerate(coarse))
vp=sum(a*3**i for i,a in enumerate(vs))
assert wp==150270 and vp==F(1381263247,8748)>wp
lines += ['', 'N >= 576+2496q+960q^2+192q^3+c*V(q) >= 576+2496q+960q^2+192q^3+c*W(q).',
          'W coefficients have one sign change. For 0<q<=3: W(q)/q^3 >= W(3)/27=5565.666..., because positive lower powers decrease and negative higher powers decrease as q increases.',
          'Exact W(3)=150270, V(3)=1381263247/8748. q=0 has W(0)=15000>0.',
          'AUTHOR PASS: complete theta leaf via seven rational bounds and one endpoint sum. No claim that all seven original q groups are positive.']
base=Path(__file__).with_suffix('')
for suf,payload in (('.generated.md','\n'.join(lines)+'\n'),('.exact.json',json.dumps({'method':'original finite convolution, negative c tails to linear c, one-change q endpoint payment','groups':rows,'W3':str(wp),'V3':str(vp)},indent=2)+'\n')):
    out=base.with_name(base.name+suf);assert not out.exists();out.write_text(payload)
print('AUTHOR PASS: complete original theta difference and seven coefficient payment gaps.')
print('AUTHOR PASS: W(3)=150270>0 and one-change endpoint argument covers q in [0,3].')
print('Original failed per-q positive-group candidate preserved; no old certificate executed.')
