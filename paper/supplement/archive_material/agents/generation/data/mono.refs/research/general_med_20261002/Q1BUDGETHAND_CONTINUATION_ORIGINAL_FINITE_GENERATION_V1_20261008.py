from pathlib import Path
from fractions import Fraction as F
from math import comb
from collections import defaultdict
import json
p=Path(__file__).resolve().parent
def clean(a):return {m:v for m,v in a.items() if v}
def con(n):return {(0,0,0):F(n)} if n else {}
def add(a,b):
 d=defaultdict(F,a)
 for m,v in b.items():d[m]+=v
 return clean(d)
def scale(a,t):return clean({m:v*F(t) for m,v in a.items()})
def mul(a,b):
 d=defaultdict(F)
 for x,v in a.items():
  for y,w in b.items():d[tuple(i+j for i,j in zip(x,y))]+=v*w
 return clean(d)
def power(a,n):
 d=con(1)
 for _ in range(n):d=mul(d,a)
 return d
q={(1,0,0):F(1)};c={(0,1,0):F(1)};z={(0,0,1):F(1)}
one=con(1);L=add(one,c);Q=add(q,one);B=add(q,con(2));H=add(B,c);J=add(add(scale(q,2),c),con(3))
d=add(one,scale(mul(c,q),-1));dz=mul(d,z);tt=power(dz,2);ET=add(power(Q,2),scale(tt,-1))
AL=add(add(con(12),scale(c,6)),scale(power(c,2),-1))
AU=add(add(add(con(24),scale(c,12)),scale(power(c,2),-2)),power(c,3))
Z2=add(power(L,2),d)
Y3=add(add(power(L,4),scale(mul(d,power(L,2)),4)),power(d,2))
Z4=add(add(power(L,6),scale(mul(d,power(L,4)),11)),add(scale(mul(power(d,2),power(L,2)),11),power(d,3)))
Y5=add(add(power(L,8),scale(mul(d,power(L,6)),26)),add(scale(mul(power(d,2),power(L,4)),66),add(scale(mul(power(d,3),power(L,2)),26),power(d,4))))
factors={'L':L,'Q':Q,'B':B,'H':H,'J':J,'A':AL,'U':AU,'E':ET}
class Expr:
 def __init__(self,terms=()):self.terms=[(n,ds) for n,ds in terms if n]
 def __add__(self,o):return Expr(self.terms+o.terms)
 def __sub__(self,o):return self+o.scal(-1)
 def scal(self,t):return Expr([(scale(n,t),ds) for n,ds in self.terms])
 def __mul__(self,o):
  out=[]
  for n,ds in self.terms:
   for m,es in o.terms:
    fs=dict(ds)
    for k,z in es.items():fs[k]=fs.get(k,0)+z
    out.append((mul(n,m),fs))
  return Expr(out)
def ex(n=one,co=F(1),**ds):return Expr([(scale(n,co),ds)])
def cleared(x,co,**ds):
 out={}
 for n,den in x.terms:
  assert all(den.get(k,0)<=ds.get(k,0) for k in den),den
  pp=scale(n,co)
  for k,z in ds.items():pp=mul(pp,power(factors[k],z-den.get(k,0)))
  out=add(out,pp)
 return out
def degrees(poly):return tuple(max(m[j] for m in poly) for j in range(3))
def prod(*ps):
 out=one
 for pp in ps:out=mul(out,pp)
 return out
# All expressions below are the original finite rational sums, not imported data.
TU=ex(prod(power(Q,2),AU),F(1,24),L=1,H=1)+ex(prod(power(Q,2),L),F(1,2),H=2)+ex(prod(power(Q,2),L,Z2),2,U=1,H=3)
W0=ex(add(scale(d,2),scale(Q,-1)),L=1,Q=1)
Wp=ex(prod(c,add(scale(d,2),scale(Q,-1))),L=1,Q=1)+ex(d,4,L=1,Q=1)-ex(d,2,L=1,H=1)-ex(prod(d,Q),4,H=2)
B10=ex(H,2,L=1,Q=1)
B11=ex(add(scale(prod(d,add(L,one)),-1),prod(c,q,Q)),2,L=1,Q=1)+ex(prod(q,d),2,L=1,H=1)+ex(prod(q,d,Q),4,H=2)
Kinside=Expr()
for co,num,degree in [(F(1,2),one,2),(F(1,2),one,3),(F(1,4),one,4),
 (-F(1,3),q,3),(-F(1,2),q,4),(-F(1,3),q,5),(F(1,6),q,7),
 (F(1),c,1),(F(1,2),c,2),(F(1,6),c,3),
 (-F(1),prod(c,q),2),(-F(1),prod(c,q),3),(-F(1,2),prod(c,q),4),(F(1,6),prod(c,q),6),
 (F(1,3),prod(c,power(q,2)),3),(F(1,2),prod(c,power(q,2)),4),(F(1,3),prod(c,power(q,2)),5)]:
 Kinside+=ex(num,co,L=1,B=degree)
Kn=Kinside*ex(prod(power(q,2),power(Q,2)))
Cq=ex(prod(d,add(scale(power(Q,2),2),scale(d,-1)),add(d,scale(prod(power(c,2),H),-F(1,6)))),Q=4,H=1,J=1)+ex(prod(power(d,2),add(scale(power(Q,2),2),scale(d,-1)),add(con(2),scale(prod(c,q),-1))),F(1,2),Q=4,H=1,L=1)
new={};ledger={}
for name in ['Tlo','Tup']:
 if name=='Tlo':
  DT=scale(prod(L,power(Q,2),power(H,5),power(AL,3)),F(5,12))
  W=add(scale(prod(L,power(H,5),power(AL,3)),F(5,12)),
        mul(power(Q,2),add(add(scale(prod(power(H,4),power(AL,4)),F(5,144)),scale(prod(power(L,2),power(H,3),power(AL,3)),F(5,24))),add(scale(prod(power(L,2),Z2,power(H,2),power(AL,2)),F(5,12)),scale(prod(power(L,2),Z4),-1)))))
  DTQ=scale(prod(L,Q,power(H,5),power(AL,3)),F(5,12))
  DP=ex(prod(L,power(Q,4),power(H,3),power(AL,4)),F(5,72))+ex(prod(L,power(Q,4),power(H,2),power(AL,3),Z2),F(55,144))+ex(prod(L,power(Q,4),H,power(AL,2),Y3),F(5,6))-ex(prod(L,power(Q,4),Y5),2,H=1)+ex(prod(power(Q,4),power(H,4),power(AL,5)),F(5,1728),L=1)
  const=6912;den={'L':1,'Q':6,'B':7,'H':3,'J':1,'U':1,'E':1}
 else:
  DT=scale(prod(L,power(Q,2),power(H,3),AU),F(1,2))
  W=add(scale(prod(L,power(H,3),AU),F(1,2)),mul(power(Q,2),add(add(scale(prod(power(H,2),power(AU,2)),F(1,48)),scale(prod(power(L,2),H,AU),F(1,4))),prod(power(L,2),Z2))))
  DTQ=scale(prod(L,Q,power(H,3),AU),F(1,2))
  DP=ex(prod(AU,L,power(Q,4),H,AL),F(1,12))+ex(prod(AU,L,power(Q,4),Z2),F(11,24))+ex(prod(AU,L,power(Q,4),Y3),A=1,H=1)-ex(prod(AU,L,power(Q,4),Y5),F(12,5),A=3,H=3)+ex(prod(AU,power(Q,4),power(H,2),power(AL,2)),F(1,288),L=1)
  const=11520;den={'L':1,'Q':6,'B':7,'H':3,'J':1,'U':1,'E':1,'A':3}
 Z=add(scale(DT,2),scale(prod(add(L,one),q,W),-1))
 gam=add(Z,prod(c,q,W));cred=add(W,scale(DTQ,-1))
 V=(DP.scal(2)-ex(gam)*TU-ex(prod(q,W,L,power(Q,2)),4,H=2)-ex(prod(q,W,power(Q,2)),2,L=1,H=1))*ex(power(ET,2),Q=4)
 value=V+ex(Z)*W0+ex(W)*(Wp*ex(q)-ex(d,2,L=1))
 value+=ex(tt,Q=2)*(ex(Z)*B10+ex(W)*B11)
 value+=ex(prod(power(tt,2),add(prod(Z,H),prod(W,add(scale(prod(d,add(L,one)),-1),prod(L,q,Q))))),2,L=1,Q=3,E=1)
 value-=ex(prod(power(tt,2),AU,q,W),F(1,16),Q=3,H=1)
 value-=ex(prod(Z,tt,ET,add(Q,scale(dz,-1))),F(3,2),Q=5)*Kn
 value+=ex(prod(tt,cred),2,Q=2)*Cq
 rows=[]
 for n,ds in value.terms:
  assert all(ds.get(k,0)<=den.get(k,0) for k in ds),ds
  bound=list(degrees(n))
  for k,v in den.items():
   fd=degrees(factors[k]);bound=[x+(v-ds.get(k,0))*y for x,y in zip(bound,fd)]
  rows.append({'term_denominators':ds,'term_numerator_degree':degrees(n),'cleared_degree_bound':bound})
 poly=cleared(value,const,**den)
 new[name]=poly;ledger[name]={'W_coefficients':[{'q':m[0],'c':m[1],'z':m[2],'value':str(v)} for m,v in sorted(W.items())], 'Z_coefficients':[{'q':m[0],'c':m[1],'z':m[2],'value':str(v)} for m,v in sorted(Z.items())], 'rows':rows,'factor_bound':tuple(max(r['cleared_degree_bound'][j] for r in rows) for j in range(3))}
 print('Original uncancelled finite budget source',name,degrees(poly),len(poly),'term count',len(rows),'factor degree bound',ledger[name]['factor_bound'],flush=True)
# Compare only after reconstruction; comparison data did not create a coefficient.
cand=json.loads((p/'Q1BUDGETHAND_CONTINUATION_FIRST_AGE_AND_MARKER_SOURCE_V2_20261008.exact.json').read_text())
for name,poly in new.items():
 row=next(r for r in cand['records'] if r['marker']=='old_full_z' and r['endpoint']==name)
 expected={(m['q'],m['c'],m['y']):F(m['value']) for m in row['coefficients']}
 assert poly==expected,name
 print('Independent algorithm agrees with local QQ',name,'PASS',flush=True)
out=Path(__file__).with_suffix('.exact.json');assert not out.exists()
out.write_text(json.dumps({'state':'author original finite convolution and complete degree ledger; not independent AI nor whole theorem','polynomials':{k:{'degree':degrees(v),'coefficients':[{'q':m[0],'c':m[1],'z':m[2],'value':str(a)} for m,a in sorted(v.items())]} for k,v in new.items()},'ledgers':ledger},indent=2)+'\n')
