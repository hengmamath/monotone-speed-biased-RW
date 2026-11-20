"""New original Je endpoint source: stdlib finite Fraction products only.
Derive compact collection from COMPLETE TU/PL before endpoint substitution.
Seven named denominator clears, explicit synthetic linear division and
direct derivative product avoid CAS division. Full W and corner payments.
Author source only; not independent audit or a claim of short proof.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import comb
import json
P=Path(__file__).resolve().parent
def clean(a):return {m:x for m,x in a.items() if x}
def con(x):return {(0,0):F(x)} if x else {}
def add(a,b):
 d=defaultdict(F,a)
 for m,x in b.items():d[m]+=x
 return clean(d)
def scale(a,x):return clean({m:z*F(x) for m,z in a.items()})
def mul(a,b):
 d=defaultdict(F)
 for (u,j),x in a.items():
  for (a,k),y in b.items():d[u+a,j+k]+=x*y
 return clean(d)
def power(a,n):
 out=con(1)
 for _ in range(n):out=mul(out,a)
 return out
def prod(*aa):
 out=con(1)
 for a in aa:out=mul(out,a)
 return out
def summ(aa):
 out={}
 for a in aa:out=add(out,a)
 return out
def deg(a):return tuple(max((m[j] for m in a),default=-1) for j in range(2))
def diff(a,j):
 return {tuple(m[k]-(k==j) for k in range(2)):x*m[j] for m,x in a.items() if m[j]}
c={(1,0):F(1)};z={(0,1):F(1)};one=con(1);L=add(one,c);A=add(c,z);C=add(one,scale(mul(add(c,con(2)),z),-1));mz=add(one,scale(z,-1))
a=add(one,scale(c,F(1,2)));al=add(a,scale(power(c,2),F(-1,12)))
P2=prod(A,add(A,z));P3=prod(A,summ([power(A,2),scale(mul(A,z),4),power(z,2)]))
P5=prod(A,summ([power(A,4),scale(prod(z,power(A,3)),26),scale(prod(power(z,2),power(A,2)),66),scale(prod(power(z,3),A),26),power(z,4)]))
Q4=summ([power(c,4),scale(prod(power(c,3),z),30),scale(prod(power(c,2),power(z,2)),150),scale(prod(c,power(z,3)),240),scale(power(z,4),120)])
H=summ([one,c,z,scale(prod(c,z),F(1,2)),scale(power(z,2),F(1,2)),scale(power(c,3),F(-1,24)),scale(prod(power(c,2),z),F(-1,4)),scale(prod(c,power(z,2)),F(-1,4)),scale(Q4,F(-1,720))])
B0=summ([con(F(1,2)),scale(c,F(1,3)),scale(power(c,2),F(-1,12)),scale(power(c,3),F(-1,24)),
 prod(z,summ([con(F(2,3)),scale(c,F(1,3)),scale(power(c,2),F(-1,4))])),prod(power(z,2),add(con(F(1,2)),scale(c,F(-1,4)))),scale(Q4,F(-1,720))])
BR=summ([scale(c,F(1,3)),scale(power(c,2),F(1,3)),scale(power(c,3),F(-1,6)),scale(power(c,4),F(-1,24)),
 prod(z,summ([scale(add(one,c),F(5,3)),scale(power(c,2),F(-1,6)),scale(power(c,3),F(-1,4))])),prod(power(z,2),add(one,scale(power(c,2),F(-1,4)))),scale(prod(add(c,con(2)),Q4),F(-1,720))])
f0=summ([con(72),scale(c,60),scale(power(c,2),12),scale(power(c,3),-1)])
f1=summ([con(48),scale(c,84),scale(power(c,2),10),scale(power(c,3),-1)])
rows=[[3600,-720,-1200,-720,480],[3600,4320,-3120,-2040,360,480],[360,4680,-240,-2640,-240,840,120],
 [420,1140,-1170,-450,540,240],[32,-126,-206,150,150],[1,-35,4,30],[0,-1,1]]
PJS={}
for j,row in enumerate(rows):
 for k,x in enumerate(row):PJS=add(PJS,{(j,k+(2 if j==0 else 1 if j==1 else 0)):F(x)} if x else {})
# Named rational expressions in original c,z. Denominators only L,A,C.
fac={'L':L,'A':A,'C':C}
class Ex:
 def __init__(self,ts=()):self.ts=[(n,d) for n,d in ts if n]
 def __add__(self,o):return Ex(self.ts+o.ts)
 def __sub__(self,o):return self+o.sc(-1)
 def sc(self,x):return Ex([(scale(n,x),d) for n,d in self.ts])
 def __mul__(self,o):
  out=[]
  for n,d in self.ts:
   for m,e in o.ts:
    ds=dict(d)
    for k,x in e.items():ds[k]=ds.get(k,0)+x
    out.append((mul(n,m),ds))
  return Ex(out)
def ex(n=one,x=1,**ds):return Ex([(scale(n,x),ds)])
def cl(e,x=720,**ds):
 out={}
 for n,d in e.ts:
  pp=scale(n,x)
  for k,vv in ds.items():
   rem=vv-d.get(k,0);assert rem>=0
   pp=mul(pp,power(fac[k],rem))
  assert all(k in ds for k in d)
  out=add(out,pp)
 return out
r=ex(mz,L=1);tt=ex(power(mz,2),L=1,A=1)
TU=tt*ex(summ([a,scale(A,F(1,2)),scale(P2,F(1,12))]))
PLi=tt*ex(summ([prod(al,A),scale(P2,F(1,2)),scale(prod(add(one,scale(c,F(-1,2))),P3),F(1,12)),scale(P5,F(-1,720))]),L=1)
PL0=PLi+tt*ex(add(power(al,2),scale(P2,F(-1,12))),L=1)
rr=r*r;lr=ex(mz);ir=ex(prod(L,mz),C=1)
orig=[PLi,PL0-TU,ex(add(L,one))*PLi-ex(L,2)*rr-ex(a,L=1)*(ir-lr),
 ex(c,-1)*TU+ex(add(L,one))*PL0-ex(L,2)*rr-tt.sc(2)+ex(a,F(1,2),L=1)*(ir-lr)-ex(a)*r]
targ=[rr*ex(H),rr*(ex(B0)-ex(prod(c,f0),F(1,144),A=1)),
 ex(prod(mz,PJS),F(-1,720),L=2,C=1),rr*(ex(BR)-ex(prod(power(c,2),f1),F(1,144),A=1))+ex(prod(a,mz),F(1,2),C=1)-(ex(a)*r).sc(F(3,2))]
collection_bounds=[]
for k,(x,y) in enumerate(zip(orig,targ)):
 bb=[]
 for nn,ds in (x-y).ts:
  bd=list(deg(nn))
  for ff,ee in {'L':2,'A':1,'C':1}.items():
   df=deg(fac[ff]);bd=[bd[j]+(ee-ds.get(ff,0))*df[j] for j in range(2)]
  bb.append(bd)
 collection_bounds.append([max(t[j] for t in bb) for j in range(2)])
 assert not cl(x-y,L=2,A=1,C=1),k
print('Four COMPLETE TU/PL zero/age and R collections by finite named clears PASS',flush=True)
# Endpoint q,h finite map, no rational model import or old certificate arrays.
q={(1,0):F(1)};h={(0,1):F(1)};Q=add(q,one);B=add(q,con(2));u=add(q,h);u1=add(u,one);t2=add(q,scale(h,2));T=summ([power(q,2),scale(q,3),scale(h,2)]);d=add(one,scale(h,-1))
def en(poly,dc,dz):
 assert all(j<=dc and k<=dz for j,k in poly)
 return summ([scale(prod(power(h,j),power(q,dc-j+k),power(d,k),power(T,dz-k)),x) for (j,k),x in poly.items()])
HN=en(H,4,4);B0N=en(B0,4,4);BRN=en(BR,5,4);PJN=en(PJS,6,6)
assert all(a>=1 for a,j in PJN)
PX={(a-1,j):x for (a,j),x in PJN.items()}
# Synthetic division in h by h+q, visible finite recurrence.
def divide_h_linear(pp,qq):
 mm=max(j for a,j in pp);rows=[{(a,0):x for (a,j),x in pp.items() if j==k} for k in range(mm+1)]
 bs=[{} for _ in range(mm)];bs[-1]=rows[-1]
 for k in range(mm-1,0,-1):bs[k-1]=add(rows[k],scale(mul(qq,bs[k]),-1))
 assert not add(rows[0],scale(mul(qq,bs[0]),-1))
 out={(a,j):x for j,row in enumerate(bs) for (a,k),x in row.items()}
 assert mul(add(h,qq),out)==pp
 return out
PJQ=divide_h_linear(PX,q)
AN=add(scale(prod(power(u,2),Q),6),prod(d,add(scale(q,2),h)))
AL=summ([scale(power(q,2),12),scale(mul(q,h),6),scale(power(h,2),-1)])
F0=summ([scale(power(q,3),72),scale(prod(h,power(q,2)),60),scale(prod(power(h,2),q),12),scale(power(h,3),-1)])
F1=summ([scale(power(q,3),48),scale(prod(h,power(q,2)),84),scale(prod(power(h,2),q),10),scale(power(h,3),-1)])
nkparts=[scale(prod(u,power(Q,2),u1,t2,power(B,2),add(scale(mul(q,HN),2),mul(u,B0N))),4320),
 scale(prod(q,u,power(Q,2),u1,power(T,5),power(B,2),h,F0),-30),
 scale(prod(q,u1,t2,power(T,5),AN,AL,B,add(scale(q,3),scale(h,-1))),60),
 scale(prod(q,Q,t2,add(scale(q,6),con(5)),B,PJQ),-2),
 scale(prod(power(u,2),Q,u1,t2,power(B,2),add(scale(q,6),con(5)),BRN),720),
 scale(prod(q,u,Q,u1,power(T,5),power(B,2),add(scale(q,6),con(5)),power(h,2),F1),-5),
 scale(prod(power(q,2),power(u,2),Q,t2,power(T,5),add(scale(q,6),con(5)),add(scale(q,2),h),B,add(T,scale(prod(q,u1),-3))),180)]
NK=summ(nkparts);DK=scale(prod(power(q,2),power(u,2),power(Q,2),u1,t2,power(T,6)),4320)
assert deg(NK)==(21,13) and len(NK)==147
cg=summ([scale(prod(u1,t2,T),2),prod(u,t2,T),scale(prod(u,u1,T),2),scale(prod(u,u1,t2),12)])
eg=prod(u,u1,t2,T)
W=scale(add(mul(cg,NK),scale(mul(eg,diff(NK,1)),-1)),4320)
G=prod(power(q,2),u,power(Q,2),power(T,5))
assert mul(G,W)==add(mul(NK,diff(DK,1)),scale(mul(diff(NK,1),DK),-1))
assert deg(W)==(25,16) and len(W)==209
P10={ (a,0):F(x) for a,x in enumerate([177534,834705,1639685,1768778,1176703,524220,173278,47463,10562,1546,102])}
W0={(a,0):x for (a,j),x in W.items() if not j}
assert W0==scale(prod(power(q,13),Q,B,P10),518400)
neg=[{'q':a,'h':j,'value':str(x),'debt':str(-x/F(2**j*3**(25-a)))} for (a,j),x in sorted(W.items()) if x<0]
assert len(neg)==17 and all(r['q']<25 and r['h']>=9 for r in neg)
debt=sum((F(r['debt']) for r in neg),F())
assert debt==F(182857794565,2066242608)<89
print('Seven Je clears NK (21,13)/147; direct derivative W (25,16)/209, exact17 negative debts <89 PASS',flush=True)
# Corner from the SAME NK, not imported old25 coefficients.
NKhalf=defaultdict(F)
for (a,j),x in NK.items():NKhalf[a,0]+=x/2**j
NKhalf=clean(NKhalf)
def divide_q_linear(pp,const):
 n=max(a for a,j in pp);bs=[F() for _ in range(n)];bs[-1]=pp.get((n,0),F())
 for a in range(n-1,0,-1):bs[a-1]=pp.get((a,0),F())-const*bs[a]
 assert pp.get((0,0),F())-const*bs[0]==0
 out={(a,0):x for a,x in enumerate(bs) if x};assert mul(add(q,con(const)),out)==pp
 return out
NCbase=divide_q_linear(NKhalf,1)
DCbase=scale(prod(power(q,2),power(Q,2),power(add(scale(q,2),one),2),add(scale(q,2),con(3)),power(add(add(power(q,2),scale(q,3)),one),6)),138240)
DC=mul(DCbase,power(B,4));NC=add(scale(mul(power(B,4),NCbase),256),scale(mul(power(q,4),DCbase),8))
assert deg(NC)==(24,0) and all(x.denominator==1 for x in NC.values())
cy={}
for (a,j),x in NC.items():
 for k in range(a+1):cy[k,0]=cy.get((k,0),F())+x*comb(a,k)*3**(a-k)
assert all((x>0 if k<=15 else x<0) for (k,j),x in cy.items()) and len(cy)==25
at7=sum(x*7**k for (k,j),x in cy.items());assert at7==15126063553311229299068153856
norm=sum(x*10**k for (k,j),x in NC.items())/sum(x*10**k for (k,j),x in DC.items())
assert norm==F(15197064237428495228777,1786372635950065193184000)
print('Shared original Je corner: degree24/25slots, finite q-3 shift, q10 exact price PASS',flush=True)
def vector(a,nd):return [[str(a.get((u,j),F())) for u in range(nd[0]+1)] for j in range(nd[1]+1)]
data={'status':'author original finite source LOCAL, independent proof pending','original_collection_cleared_degree_bounds':collection_bounds,'compact_source_polynomials':{name:{'degree':deg(pp),'rows_c_power_z_vectors':[[str(pp.get((j,k),F())) for k in range(deg(pp)[1]+1)] for j in range(deg(pp)[0]+1)]} for name,pp in [('H',H),('B0',B0),('BR',BR),('PJS',PJS)]},
 'endpoint_map_degrees':{name:deg(pp) for name,pp in [('HN',HN),('B0N',B0N),('BRN',BRN),('PJN',PJN),('PJQ',PJQ)]},
 'NK_seven_part_degrees':[deg(pp) for pp in nkparts],'NK_degree':deg(NK),'NK_nonzero':len(NK),'NK_h_rows_q_vectors':vector(NK,(21,13)),
 'W_degree':deg(W),'W_nonzero':len(W),'W_h_rows_q_vectors':vector(W,(25,16)), 'W_negative_terms':neg,'W_debt':str(debt),
 'NKhalf_Q_quotient_q_vector':[str(NCbase.get((a,0),F())) for a in range(21)],
 'corner_ordinary_q_vector':[str(NC.get((a,0),F())) for a in range(25)],'corner_shifted_qminus3_vector':[str(cy.get((a,0),F())) for a in range(25)],'corner_at_q10_numerator':str(at7),'corner_at_q10_price':str(norm)}
out=Path(__file__).with_suffix('.exact.json');assert not out.exists();out.write_text(json.dumps(data,indent=2)+'\n')
md=['# S14 与 S12b 原完整Je有限来源附录（作者 LOCAL）','','全部向量按低幂到高幂；完整零槽保留。此附录尚不是独立审计回执。','','## A. 原小多项式与端点次数','']
md.append('四原集合清720L²AC的有限次数界='+str(collection_bounds))
for name,row in data['compact_source_polynomials'].items():
 md.append(name+' degree='+str(row['degree']))
 for j,rr in enumerate(row['rows_c_power_z_vectors']):md.append(f'c^{j}: ['+', '.join(rr)+']')
md+=['','端点映射完整次数='+str(data['endpoint_map_degrees']),'七清分母项完整次数='+str(data['NK_seven_part_degrees']),'','## B. 全部 NK，14行×22槽=308槽，147非零','']
for j,rr in enumerate(data['NK_h_rows_q_vectors']):md.append(f'h^{j}: ['+', '.join(rr)+']')
md+=['','## C. 全部 W，17行×26槽=442槽，209非零','']
for j,rr in enumerate(data['W_h_rows_q_vectors']):md.append(f'h^{j}: ['+', '.join(rr)+']')
md+=['','## D. 全部17负项及逐项准确债务','']
for r in neg:md.append(str(r))
md+=['完整债务='+str(debt)+'<89','','## E. h=1/2的Q商、角点普通q与q−3完整向量','', 'NKhalf/Q=['+', '.join(data['NKhalf_Q_quotient_q_vector'])+']','Ncorner(q)=['+', '.join(data['corner_ordinary_q_vector'])+']','Ncorner(3+y)=['+', '.join(data['corner_shifted_qminus3_vector'])+']','Ncorner(10)='+str(at7),'原归一化q10价格='+str(norm),'']
gen=Path(__file__).with_suffix('.generated.md');assert not gen.exists();gen.write_text('\n'.join(md)+'\n')
print('Full308 NK slots,442 W slots,17 debt rows and25 shiftedcorner slots saved; author LOCAL only',flush=True)
