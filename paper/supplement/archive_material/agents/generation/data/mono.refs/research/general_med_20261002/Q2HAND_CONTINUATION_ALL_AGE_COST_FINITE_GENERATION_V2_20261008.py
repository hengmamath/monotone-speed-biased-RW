"""S6 whole infinite-age cost: new finite source, stdlib Fraction only.
No old source/certificate import, no CAS, no samples. Author LOCAL evidence.
All rational identities start at the displayed complete-sum enclosures.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json
P=Path(__file__).resolve().parent
def trim(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a
def sc(a,v):return trim([F(v)*x for x in a])
def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def mul(a,b):
 c=[F(0)]*max(0,len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def pw(a,n):
 r=[F(1)]
 for _ in range(n):r=mul(r,a)
 return r
def df(a):return trim([i*a[i] for i in range(1,len(a))])
def shift(a,v):
 out=[]
 for i,x in enumerate(a):out=add(out,sc(pw([F(v),F(1)],i),x))
 return out
def at(a,v):
 r=F(0)
 for x in reversed(a):r=r*v+x
 return r
def txt(a):return '['+', '.join(str(x) for x in a)+']'
q=[F(0),F(1)];one=[F(1)];A=[F(2),F(1)];U=[F(1),F(1)]
fac={'A':A,'U':U}
class Ex:
 def __init__(self,terms=()):self.ts=[(n,d) for n,d in terms if n]
 def __add__(self,o):return Ex(self.ts+o.ts)
 def __sub__(self,o):return self+o.scale(-1)
 def scale(self,v):return Ex([(sc(n,v),d) for n,d in self.ts])
 def __mul__(self,o):
  out=[]
  for n,d in self.ts:
   for m,e in o.ts:
    z=dict(d)
    for k,v in e.items():z[k]=z.get(k,0)+v
    out.append((mul(n,m),z))
  return Ex(out)
def ex(n=one,v=1,**d):return Ex([(sc(n,v),d)])
def clear(e,v=1,**d):
 out=[];bound=-1
 for n,nd in e.ts:
  z=sc(n,v);b=len(n)-1
  assert all(k in d for k in nd)
  for k,m in d.items():
   assert m>=nd.get(k,0)
   b+=m-nd.get(k,0);z=mul(z,pw(fac[k],m-nd.get(k,0)))
  bound=max(bound,b);out=add(out,z)
 return out,bound
def Uj(j):return ex(v=F(1,j-1),A=j-1)+ex(v=F(1,2),A=j)+ex(v=F(j,12),A=j+1)
def Lj(j):return Uj(j)-ex(v=F(j*(j+1)*(j+2),720),A=j+3)
def Pj(j):return Lj(j)+ex(v=F(j*(j+1)*(j+2)*(j+3)*(j+4),30240),A=j+5)
# Universal n-coefficient identities from multiplication by exp(t)-1.
n=q
def fall(k):
 out=one
 for j in range(k):out=mul(out,[F(-j),F(1)])
 return out
lower=add(add(one,sc(n,F(-1,2))),add(sc(fall(2),F(1,12)),sc(fall(4),F(-1,720))))
lp=sc(mul(mul(mul([F(-6),F(1)],[F(-5),F(1)]),[F(-3),F(1)]),[F(8),F(1)]),F(-1,720))
upper=add(lower,sc(fall(6),F(1,30240)))
up=sc(mul(mul(mul(mul([F(-8),F(1)],[F(-7),F(1)]),[F(-5),F(1)]),[F(-3),F(1)]),[F(36),F(8),F(1)]),F(1,30240))
assert lower==lp and upper==up
def early(poly,N):
 vals=[]
 for m in range(N):
  from math import factorial
  v=sum(F(a,factorial(m-k)) for k,a in enumerate(poly) if 0<=m-k and m-k>=1)
  if m>=1:v-=F(1,factorial(m-1))
  vals.append(v)
 return vals
lowearly=early([F(1),F(1,2),F(1,12),F(0),F(-1,720)],7)
upearly=early([F(1),F(1,2),F(1,12),F(0),F(-1,720),F(0),F(1,30240)],9)
assert not any(lowearly) and not any(upearly)
print('Universal coefficient factorizations, all early coefficients PASS',flush=True)
H=Pj(4).scale(-1)
H=H+ex([F(1,2),F(3)])*Lj(5)-ex(mul(q,[F(1,2),F(2)]))*Pj(6)
Q=Pj(3).scale(-1)+ex([F(1),F(9,2)])*Lj(4)-ex([F(0),F(2),F(6)])*Pj(5)+ex([F(0),F(0),F(1),F(5,2)])*Lj(6)
NH,bh=clear(H,720,A=11);NQ,bq=clear(Q,60,A=10)
hshift=shift(NH,3);qshift=shift(NQ,3)
assert hshift==list(map(F,[83885,4956545,5682827,2782725,749142,119340,11202,570,12]))
assert qshift==list(map(F,[26115,176003,154042,58757,11995,1368,82,2]))
assert min(hshift)>0 and min(qshift)>0 and bh==8 and bq==8 and len(NQ)==8
print('All-age mean gaps: original enclosure clearing and 17 full shifted coefficients PASS',flush=True)
head=ex(mul(pw(q,4),add(pw(U,2),[-F(1)])),4,U=1)*(Pj(6)-ex(q)*Lj(7))
quad=ex(pw(q,4),8)*(Pj(6)-ex(q,2)*Lj(7)+ex(pw(q,2))*Pj(8))
BN,bb=clear(head+quad,105,U=1,A=13)
assert not any(BN[:4]);BP=BN[4:]
assert BP==list(map(F,[120736,561568,1110216,1252256,906540,444648,149222,33672,4857,400,14]))
assert bb==14 and len(BN)==15
# Derivative of q^4 P/[105 U A^13] by quotient rule, then remove q^3.
DN=add(mul(add(sc(BP,4),mul(q,df(BP))),mul(U,A)),sc(mul(mul(q,BP),add(A,sc(U,13))),-1))
assert DN==list(map(F,[965888,5253472,12115232,15808120,13136448,7396732,2880976,755874,125776,11381,278,-22]))
assert min(DN[:-1])>0 and 278-22*10==58
B10=10**4*at(BP,10)/F(105*11*12**13)
gap=F(13,100)-B10
assert B10==F(1019883602875,8045387513856) and gap==F(650419348157,201134687846400)>0
# Endpoint of 1-(q-1/2)s-(q+5/2)s^2 at s=1/U.
derivendpoint=add(add(pw(U,2),sc(mul([F(-1,2),F(1)],U),-1)),sc([F(5,2),F(1)],-1))
assert derivendpoint==[F(-1),F(1,2)]
print('Whole-cost endpoint, original rational majorant and full derivative, exact B(10) PASS',flush=True)
data={'status':'AUTHOR LOCAL exact finite generation, not an independent audit','actual_source':'new stdlib Fraction; no imports from historical research code',
 'lower_universal_n_polynomial':[str(x) for x in lower],'upper_universal_n_polynomial':[str(x) for x in upper],
 'lower_early':[str(x) for x in lowearly],'upper_early':[str(x) for x in upearly],
 'H_gap_ordinary':[str(x) for x in NH],'H_gap_q3':[str(x) for x in hshift],'H_source_degree_bound':bh,
 'Q_gap_ordinary':[str(x) for x in NQ],'Q_gap_q3':[str(x) for x in qshift],'Q_source_degree_bound':bq,
 'B_P_ordinary':[str(x) for x in BP],'B_source_degree_bound':bb,'B_derivative_D':[str(x) for x in DN],
 'whole_cost_derivative_endpoint_U2':[str(x) for x in derivendpoint], 'B10':str(B10),'13_over_100_minus_B10':str(gap),
 'displayed_arithmetic_slots':{'universal':5+7,'early_zero':7+9,'two_gap_ordinary_and_shift':34,'P_and_D':11+12,'derivative_endpoint':2,'Q_degree8_zero':1},
 'scope':'S6 scalar complete infinite-age cost only; actual S5 moment interface must also be proved.'}
stem=Path(__file__).with_suffix('')
Path(str(stem)+'.exact.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
lines=['## 完整有限来源与槽位附录','',
 '乘法系数规则为 (ab)_k=Σ_(i+j=k)a_i b_j；q=3+y的完整移位为 Σ_(k≥j) binom(k,j)3^(k−j)a_k。以下系数均按低次到高次排列，未显示之外的槽由原因子次数界排除。',
 '','通用下界n多项式：`'+txt(lower)+'`；上界：`'+txt(upper)+'`。',
 '','下界0…6的完整零槽：`'+txt(lowearly)+'`；上界0…8：`'+txt(upearly)+'`。',
 '','N_H普通9槽：`'+txt(NH)+'`；q−3移位9槽：`'+txt(hshift)+'`。',
 '','N_Q普通8槽：`'+txt(NQ)+'`；q−3移位8槽：`'+txt(qshift)+'`。',
 '','P普通11槽：`'+txt(BP)+'`；D普通12槽：`'+txt(DN)+'`。',
 '','全成本首方向端点乘U²的2槽：`'+txt(derivendpoint)+'`。',
 '','源次数界：N_H≤8，N_Q结构≤8，而最高q8槽是−1/2+3/2−3/2+1/2=0，故N_Q≤7；B的105UA13清分子≤14且其q0…3为零，除q4的P≤10，导数D≤11。',
 '','本附录共88个算术槽（含16早期零槽、两个gap普通及移位的34槽）；不用有限网格，不把成本的全龄求和改成截断。']
Path(str(stem)+'.generated.md').write_text('\n'.join(lines)+'\n')
print('S6 new original finite source COMPLETE LOCAL PASS; continuous series/tilt proof remains in paper',flush=True)
