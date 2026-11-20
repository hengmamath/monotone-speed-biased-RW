"""Q2 S11 full elementary age/theta interface, new stdlib finite source.
Only original Eulerian tails and complete R/alpha/age collections are inputs.
No old certificate/model import; no free escape law or sampling. AUTHOR LOCAL.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json
def clean(a):return {m:v for m,v in a.items() if v}
def con(v):return {(0,0):F(v)} if v else {}
def add(a,b):
 d=defaultdict(F,a)
 for m,v in b.items():d[m]+=v
 return clean(d)
def sc(a,v):return clean({m:x*F(v) for m,x in a.items()})
def mul(a,b):
 d=defaultdict(F)
 for (j,k),v in a.items():
  for (l,n),w in b.items():d[j+l,k+n]+=v*w
 return clean(d)
def pw(a,n):
 r=con(1)
 for _ in range(n):r=mul(r,a)
 return r
def prod(*aa):
 r=con(1)
 for a in aa:r=mul(r,a)
 return r
def sm(aa):
 r={}
 for a in aa:r=add(r,a)
 return r
def deg(a):return tuple(max((m[i] for m in a),default=-1) for i in range(2))
def divide(a,b):
 r=dict(a);out={};bm=max(b);bc=b[bm]
 while r:
  rm=max(r);dm=tuple(rm[i]-bm[i] for i in range(2));assert min(dm)>=0,('exact divide',rm,bm)
  pp={dm:r[rm]/bc};out=add(out,pp);r=add(r,sc(mul(pp,b),-1))
 return out
def row(a,j):return [a.get((j,k),F(0)) for k in range(deg(a)[1]+1)]
def txt(a):return '['+', '.join(str(v) for v in a)+']'
one=con(1);c={(1,0):F(1)};z={(0,1):F(1)};L=add(one,c);A=add(c,z);mz=add(one,sc(z,-1));C=add(one,sc(mul(add(c,con(2)),z),-1))
a=add(one,sc(c,F(1,2)));al=add(a,sc(pw(c,2),F(-1,12)))
P2=prod(A,add(A,z));P3=prod(A,sm([pw(A,2),sc(mul(A,z),4),pw(z,2)]))
P4=prod(A,sm([pw(A,3),sc(prod(z,pw(A,2)),11),sc(prod(pw(z,2),A),11),pw(z,3)]))
P5=prod(A,sm([pw(A,4),sc(prod(z,pw(A,3)),26),sc(prod(pw(z,2),pw(A,2)),66),sc(prod(pw(z,3),A),26),pw(z,4)]))
fac={'L':L,'A':A,'C':C}
class Ex:
 def __init__(self,ts=()):self.ts=[(n,d) for n,d in ts if n]
 def __add__(self,o):return Ex(self.ts+o.ts)
 def __sub__(self,o):return self+o.sc(-1)
 def sc(self,v):return Ex([(sc(n,v),d) for n,d in self.ts])
 def __mul__(self,o):
  ts=[]
  for n,d in self.ts:
   for m,e in o.ts:
    dd=dict(d)
    for k,v in e.items():dd[k]=dd.get(k,0)+v
    ts.append((mul(n,m),dd))
  return Ex(ts)
def ex(n=one,v=1,**ds):return Ex([(sc(n,v),ds)])
def cl(e,v=1,**ds):
 out={};bb=[]
 for n,d in e.ts:
  pp=sc(n,v);bd=list(deg(n));assert all(k in ds for k in d)
  for k,ee in ds.items():
   rem=ee-d.get(k,0);assert rem>=0
   bd=[bd[j]+rem*deg(fac[k])[j] for j in range(2)];pp=mul(pp,pw(fac[k],rem))
  bb.append(bd);out=add(out,pp)
 return out,[max(t[j] for t in bb) for j in range(2)]
r=ex(mz,L=1);lr=ex(mz);ir=ex(prod(L,mz),C=1);rr=r*r;t=ex(pw(mz,2),L=1,A=1)
TLe=t*ex(sm([al,sc(A,F(1,2)),sc(prod(add(one,sc(c,F(-1,2))),P2),F(1,12)),sc(P4,F(-1,720))]))
TUe=t*ex(sm([a,sc(A,F(1,2)),sc(P2,F(1,12))]))
PUi=t*ex(sm([prod(a,A),sc(P2,F(1,2)),sc(P3,F(1,12))]),L=1)
PUzero=PUi+t*ex(sm([pw(a,2),sc(P2,F(-1,12)),sc(P4,F(1,240))]),L=1)
PLi=t*ex(sm([prod(al,A),sc(P2,F(1,2)),sc(prod(add(one,sc(c,F(-1,2))),P3),F(1,12)),sc(P5,F(-1,720))]),L=1)
PLzero=PLi+t*ex(add(pw(al,2),sc(P2,F(-1,12))),L=1)
PUone=PUzero+PUi;PLone=PLzero+PLi
tauR=ex(add(L,one))-lr-ir
# These are coefficients from full BB−2VUe and full Je, preserving i+1.
HRs=ex(c,2,L=1)+ex(z,2,L=1)+(r*ex(z)).sc(2)+ex(al,2,L=1)*tauR-(ex(add(L,one))*PUi-ex(L,2)*rr).sc(2)
HRone=ex(c,2,L=1)+ex(z,2,L=1)+(r*ex(z)).sc(4)+ex(al,L=1)*tauR-(ex(c,-1)*TLe+ex(add(L,one))*PUone-ex(L,4)*rr-t.sc(2)).sc(2)
JRs=ex(add(L,one))*PLi-ex(L,2)*rr-ex(a,L=1)*(ir-lr)
JRone=ex(c,-1)*TUe+ex(add(L,one))*PLone-ex(L,4)*rr-t.sc(2)-ex(a,F(1,2),L=1)*(ir+lr)
HH,bhs=cl(HRs,-6,L=2,A=1,C=1);HS=divide(HH,A)
JJ,bjs=cl(JRs,-720,L=2,A=1,C=1);JS=divide(divide(JJ,A),mz)
H1,bh1=cl(HRone,-360,L=2,A=1,C=1)
J1,bj1=cl(JRone,-720,L=2,A=1,C=1);J1=divide(J1,pw(mz,2))
polys={'HS':HS,'JS':JS,'H1':H1,'J1':J1};sourcebounds={'HS':bhs,'JS':bjs,'H1':bh1,'J1':bj1}
# Alpha coefficients are full affine ones; their age slopes are nonnegative.
Has=ex(v=2,L=1)-(ex(al,L=1)*r).sc(2);Jas=(ex(al,L=1)*r).sc(2)
H0s=ex(al,2,L=1)-PUi.sc(2);J0s=PLi
hc0,b0=cl(H0s,6,L=2,A=1,C=1);hc0=divide(hc0,A)
ha,bha=cl(ex(pw(L,2))*Has,6,L=2,A=1,C=1);ha=divide(ha,A)
hc=[hc0,sm([hc0,ha,sc(HS,-1)]),sc(HS,-1)]
jc0,bj0=cl(J0s,720,L=2,A=1,C=1);jc0=divide(jc0,A)
ja,bja=cl(ex(pw(L,2))*Jas,720,L=2,A=1,C=1);ja=divide(ja,A)
jc=[jc0,sm([jc0,ja,sc(mul(mz,JS),-1)]),sc(mul(mz,JS),-1)]
# Evaluate original cleared q quadratics at q=3 and qmax, no old arrays.
H3=sm([hc[0],sc(hc[1],3),sc(hc[2],9)])
J3=divide(sm([jc[0],sc(jc[1],3),sc(jc[2],9)]),sc(mz,4))
qm=add(one,sc(prod(add(con(3),sc(c,2)),z),-1))
HN=sm([prod(hc[0],pw(A,2)),prod(hc[1],qm,A),prod(hc[2],pw(qm,2))])
JN=sm([prod(jc[0],pw(A,2)),prod(jc[1],qm,A),prod(jc[2],pw(qm,2))])
HM=divide(HN,pw(L,2));JM=divide(JN,prod(pw(L,2),mz))
polys.update({'H3':H3,'HM':HM,'J3':J3,'JM':JM})
print('All four original R/age collections and complete four endpoints from exact q quadratics PASS',flush=True)
# Sign lower envelopes: no row lists used to define any polynomial.
tt=F(1,6);margins={}
for name in ['HS','JS','H1','J1']:
 n=polys[name];v=[]
 for j in range(4):
  rw=row(n,j);kk=next(k for k,w in enumerate(rw) if w);rw=rw[kk:]
  v.append(rw[0]+sum(w*tt**k for k,w in enumerate(rw) if k and w<0))
 rw=row(n,4);kk=next(k for k,w in enumerate(rw) if w)
 value=rw[kk]+sum(w*tt**(k-kk) for k,w in enumerate(rw) if k>kk and w<0)
 for j in range(5,deg(n)[0]+1):
  for k,w in enumerate(row(n,j)):
   if w<0:assert k>=kk;value+=w*tt**(j-4+k-kk)
 v.append(value);assert min(v)>0;margins[name]=v
assert margins['JS']==list(map(F,[F(10330,3),F(31535,9),F(9205,27),F(4625,12),F(929,216)]))
print('Complete 20 theta row margins from original 4 kernels PASS',flush=True)
def negative_pay(n,filterer,weight):return sum(v*weight(j,k) for (j,k),v in n.items() if v<0 and filterer(j,k))
h3a=H3[(0,1)]+negative_pay(H3,lambda j,k:j==0 and k>1,lambda j,k:tt**(k-1))
h3b=H3[(1,0)]+negative_pay(H3,lambda j,k:j==1,lambda j,k:tt**k)
h3c=h3a+negative_pay(H3,lambda j,k:2<=j<=4,lambda j,k:tt**(j+k-1))
assert (h3a,h3b,h3c)==(F(377,9),F(4,9),F(30277,1296))
hml0=F(8)+negative_pay(HM,lambda j,k:j==0 and k>=5,lambda j,k:tt**(k-2))
hml1=F(21,2)+negative_pay(HM,lambda j,k:j==1 and k>=4,lambda j,k:tt**(k-1))
hml2=HM[(2,0)]+negative_pay(HM,lambda j,k:j==2,lambda j,k:tt**k)
debt3=-(HM.get((3,1),F(0))+HM.get((3,4),F(0))*tt**3)/64
debt4=-(HM.get((4,1),F(0))+HM.get((4,4),F(0))*tt**3)/384
hmlc=hml2-debt3-debt4
assert (hml0,hml1,hml2,hmlc)==(F(757,108),F(1087,108),F(2131,3888),F(8071,62208))
j3c=J3[(0,0)]+negative_pay(J3,lambda j,k:True,lambda j,k:tt**(j+k))
assert j3c==F(10619717,62208)>0
jml0=F(710)+negative_pay(JM,lambda j,k:j==0 and k>=4,lambda j,k:tt**(k-1))
jml1=F(540)+negative_pay(JM,lambda j,k:j==1 and k>=3,lambda j,k:tt**k)+negative_pay(JM,lambda j,k:j>=2,lambda j,k:tt**(j-1+k))
assert (jml0,jml1)==(F(1758485,2916),F(655917461,2519424))
print('All endpoint full row debts and exact positive credits PASS',flush=True)

# Generic all-N geometric moments: E_(j+1)=(1+jz)E_j+z(1-z)E_j'.
def df(a,k):return {tuple(m[i]-(i==k) for i in range(2)):v*m[k] for m,v in a.items() if m[k]}
es=[one]
for j in range(5):es.append(add(mul(add(one,sc(z,j)),es[-1]),prod(z,mz,df(es[-1],1))))
evs=[[n.get((0,k),F(0)) for k in range(j if j else 1)] for j,n in enumerate(es)]
assert evs==[[F(1)],[F(1)],[F(1),F(1)],[F(1),F(4),F(1)],[F(1),F(11),F(11),F(1)],[F(1),F(26),F(66),F(26),F(1)]]
# Global C upper even-n coefficient factorization, from cosh multiplication.
n=c
fall2=prod(n,add(n,con(-1)));fall4=prod(fall2,add(n,con(-2)),add(n,con(-3)))
cu=sm([con(2),sc(fall2,F(-1,6)),sc(fall4,F(1,120))])
cuf=sc(prod(add(n,con(-6)),sm([pw(n,3),sc(n,-9),con(-40)])),F(1,120))
assert cu==cuf
print('ALL-N Eulerian moment recurrence and global C coefficient factorization PASS',flush=True)

data={'status':'AUTHOR LOCAL, full continuous interface proof and formal audit required',
 'full_original_collection_structural_bounds':sourcebounds,'quad_h_bounds':[b0,bha],'quad_j_bounds':[bj0,bja],
 'polynomials':{name:{f'{j},{k}':str(v) for (j,k),v in sorted(n.items())} for name,n in polys.items()},
 'actual_degrees':{name:deg(n) for name,n in polys.items()},'full_slots':sum((deg(n)[0]+1)*(deg(n)[1]+1) for n in polys.values()),
 'q_quadratic_full_coefficients':{'H':[{f'{j},{k}':str(v) for (j,k),v in sorted(n.items())} for n in hc],'J':[{f'{j},{k}':str(v) for (j,k),v in sorted(n.items())} for n in jc]},
 'theta_margins':{name:[str(v) for v in a] for name,a in margins.items()},
 'endpoint_credits':{'H3':[str(h3a),str(h3b),str(h3c)],'HM':[str(hml0),str(hml1),str(hml2),str(hmlc)],'J3':str(j3c),'JM':[str(jml0),str(jml1)]},
 'Eulerian_complete_vectors':[[str(v) for v in a] for a in evs],'global_C_even_n_coefficients':[str(cu.get((k,0),F(0))) for k in range(5)],'scope':'S11 elementary full finite identities only; actual KH/KJ enclosure, original theta/age bounds and finite-mean response retained as separate paper interfaces.'}
stem=Path(__file__).with_suffix('')
Path(str(stem)+'.exact.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
lines=['## S11原来源全部有限槽附录','', '二维卷积 (ab)_(j,k)=Σa_(r,s)b_(j−r,k−s)。每个分母只乘正的命名L,A,C的非负次幂；随后显示的A、1−z或L整除可通过反乘逐槽手核。列表低z次至高z次。',
 '','原4清项结构界：`'+str(sourcebounds)+'`。']
for name,n in polys.items():
 lines+=['',f'### {name}完整普通槽，次数{deg(n)}']
 for j in range(deg(n)[0]+1):lines.append(f'c^{j}: `'+txt(row(n,j))+'`')
 if name in margins:lines+=['','五项符号付款：`'+txt(margins[name])+'`。']
for name,qs in [('H',hc),('J',jc)]:
 lines+=['',f'### 原q二次{name}完整系数来源（乘D0(q+1)后）']
 for i,n in enumerate(qs):
  lines.append(f'q^{i}，次数{deg(n)}：')
  for j in range(deg(n)[0]+1):lines.append(f'c^{j}: `'+txt(row(n,j))+'`')
lines+=['','全部端点付款：`'+str(data['endpoint_credits'])+'`。','全部8多项式普通槽数：'+str(data['full_slots'])+'；另含两q二次的完整原系数、精确整除、20符号付款、端点债务。程序输出不是连续证明。']
lines+=['','全部六几何Eulerian向量（按d/p低次到高次）：`'+str([[str(v) for v in a] for a in evs])+'`，共16槽。','全局C上界cosh乘法偶数n系数（乘n!）完整5槽：`'+txt([cu.get((k,0),F(0)) for k in range(5)])+'`；准确因子(n−6)(n³−9n−40)/120。']
Path(str(stem)+'.generated.md').write_text('\n'.join(lines)+'\n')
print('S11 new original finite source COMPLETE LOCAL PASS',flush=True)
