"""Q2 S13/S36/S37 new self-contained original finite source, stdlib only.
Full compact Je collection repeated explicitly, no source imports/execution.
Finite age/Euler/envelope and two-product remainder payments, author LOCAL.
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
# Small S13 finite derivative and Euler payments in c,z.
cap=F(1,6)
def eval_z(pp):return sum(x*cap**k for (j,k),x in pp.items())
dn=[{(0,k):x for (j,k),x in diff(PJS,1).items() if j==a} for a in range(7)]
low=[]
for j,pp in enumerate(dn):
 if j==0:
  assert all(k>=1 for a,k in pp)
  zz={(0,k-1):x for (a,k),x in pp.items()}
  lo=zz.get((0,0),F())+sum(x*cap**k for (a,k),x in zz.items() if k and x<0)
 else:lo=pp.get((0,0),F())+sum(x*cap**k for (a,k),x in pp.items() if k and x<0)
 low.append(lo)
assert low[0]==6690 and low[1]==F(29720,9) and low[3]==F(1425,2)
dfold=low[2]+sum(low[k]*cap**(k-2) for k in [4,5,6])
assert dfold==F(5663501,1296)>0
pairN=add(scale(prod(L,power(C,2),summ([con(4),scale(c,-3),scale(z,-3)])),4),
 scale(prod(a,mz,summ([scale(prod(z,power(L,2)),2),scale(prod(L,C),-8),scale(prod(add(con(4),z),power(C,2)),6)])),-1))
assert len(pairN)==18 and deg(pairN)==(4,4)
gamma_c=4-sum(-x*cap**(j-1+k) for (j,k),x in pairN.items() if x<0 and j>0)
gamma_z=12-32*cap
assert gamma_c==F(2485,2592)>0 and gamma_z==F(20,3)>0
euler0=F(13,3)*(F(1,72)+F(1,216)+F(5,31104)+F(1,1536))+F(4,27)
BRm=[F(4,3)-F(13,3)*(F(25,5184)+F(13,2304)),5-F(13,3)*(F(5,864)+F(13,2304)),2-F(13,3)*F(1,144)]
assert euler0==F(86561,373248)<F(1,4) and all(x>0 for x in BRm)
assert F(13,3)*F(1121,18)/144==F(14573,7776)<3
# S36 small envelope products and seven complete row payments.
cz=add(c,z);HL=summ([one,c,z,scale(power(z,2),F(1,2)),scale(power(cz,3),F(-7,24))])
U3=summ([scale(power(z,2),3600),scale(prod(c,z),3600),scale(power(c,2),360),scale(prod(c,power(z,2)),4320),scale(prod(power(c,2),z),4870),scale(power(c,3),426)])
hgap=summ([scale(prod(c,z),F(1,2)),add(scale(power(cz,3),F(1,4)),scale(summ([scale(power(c,3),F(1,24)),scale(prod(power(c,2),z),F(1,4)),scale(prod(c,power(z,2)),F(1,4))]),-1)),
 scale(prod(power(cz,3),add(con(F(1,4)),scale(cz,-1))),F(1,6)),scale(add(scale(power(cz,4),120),scale(Q4,-1)),F(1,720))])
assert add(H,scale(HL,-1))==hgap
topvec=[[3600],[3600,4320],[360,4680],[420,1140],[32],[1],[]]
cuts=[2,2,2,2,2,1,1];emarg=[];Uref={}
for j,(raw,top,k) in enumerate(zip(rows,topvec,cuts)):
 pp={i:F((top[i] if i<len(top) else 0)-raw[i]) for i in range(len(raw))}
 assert all(x>=0 for i,x in pp.items() if i<k) and all(i>k for i,x in pp.items() if x<0)
 margin=pp.get(k,F())+sum(x*cap**(i-k) for i,x in pp.items() if x<0)
 assert margin>0;emarg.append(margin)
 Uref=add(Uref,{(j,i+(2 if j==0 else 1 if j==1 else 0)):F(x) for i,x in enumerate(top) if x})
ugap=add(scale(prod(power(c,2),z,add(con(cap),scale(c,-1))),1140),
 prod(power(c,3),add(con(F(23,36)),prod(add(con(cap),scale(c,-1)),add(add(con(32),c),con(cap))))))
assert add(U3,scale(Uref,-1))==ugap
print('S13 derivative7/Euler pair18 and S36 envelope7 finite sources/payments PASS',flush=True)
# Actual q,h endpoint products for S36/S37.
q={(1,0):F(1)};h={(0,1):F(1)};Q=add(q,one);B=add(q,con(2));u=add(q,h);u1=add(u,one);t2=add(q,scale(h,2));T=summ([power(q,2),scale(q,3),scale(h,2)]);d=add(one,scale(h,-1));q3=add(q,con(3))
AN=add(scale(prod(power(u,2),Q),6),prod(d,add(scale(q,2),h)));AL=summ([scale(power(q,2),12),scale(prod(q,h),6),scale(power(h,2),-1)])
HNe=summ([scale(prod(power(q,3),power(T,3)),24),scale(prod(h,power(q,2),power(T,3)),24),scale(prod(power(q,4),d,power(T,2)),24),scale(prod(power(q,5),power(d,2),T),12),scale(prod(power(u,3),power(t2,3)),-7)])
UN=summ([scale(prod(power(q,5),power(d,2)),3600),scale(prod(power(q,3),h,d,T),3600),scale(prod(q,power(h,2),power(T,2)),360),scale(prod(power(q,4),h,power(d,2)),4320),scale(prod(power(q,2),power(h,2),d,T),4870),scale(prod(power(h,3),power(T,2)),426)])
def en(poly,dc,dz):return summ([scale(prod(power(h,j),power(q,dc-j+k),power(d,k),power(T,dz-k)),x) for (j,k),x in poly.items()])
assert HNe==scale(en(HL,3,3),24) and UN==en(U3,3,2)
parts=[scale(prod(power(Q,2),power(u,2),u1,q3,power(B,2),HNe),180),scale(prod(u,u1,q3,power(T,4),AN,AL,B),120),
 scale(prod(q,Q,q3,power(T,3),add(scale(q,6),con(5)),B,UN),-1),
 scale(prod(q,power(Q,2),power(u,2),u1,power(T,5),add(scale(add(scale(q,3),con(-1)),2),prod(h,q3))),-2160)]
N=summ(parts)
A37=scale(prod(u,u1,power(T,4)),120)
B37=add(prod(q3,AN,AL,B),scale(prod(q,power(Q,2),u,T,add(scale(add(scale(q,3),con(-1)),2),prod(h,q3))),-18))
C37=add(scale(prod(Q,power(u,2),u1,B,HNe),180),scale(prod(q,power(T,3),add(scale(q,6),con(5)),UN),-1));FF=prod(Q,q3,B)
assert N==add(mul(A37,B37),mul(FF,C37)) and deg(A37)[1]==6 and deg(B37)[1]==4 and deg(C37)[1]==9
assert all(x>0 for x in A37.values())
def hc(poly,j):return {(a,0):x for (a,k),x in poly.items() if k==j}
def qp(cs):return {(a,0):F(x) for a,x in enumerate(cs) if x}
def qshift(pp,at):
 out={}
 for (a,j),x in pp.items():
  assert j==0
  for k in range(a+1):out[k,0]=out.get((k,0),F())+x*comb(a,k)*at**(a-k)
 return clean(out)
def qvec(pp):return [str(pp.get((a,0),F())) for a in range(deg(pp)[0]+1)]
bpolys=[qp([-7,-11,-3,3]),qp([-54,-125,-86,10,12,3]),qp([-48,-181,-179,-6,21,9]),qp([2,-3,4,12]),one]
bmuls=[scale(prod(power(q,3),q3),12),scale(power(q,2),6),scale(q,2),q3,prod(B,q3,add(scale(q,6),con(5)))]
for j in range(5):assert hc(B37,j)==scale(mul(bmuls[j],bpolys[j]),-1)
assert all(x>0 for j in range(3) for x in qshift(bpolys[j],3).values())
assert bpolys[3]==add(prod(add(q,con(-1)),qp([13,16,12])),con(15))
N0=scale(prod(power(q,8),Q,q3,qp([8108,21708,22109,10638,2441,216])),180)
N1=scale(prod(power(q,7),q3,qp([38380,136080,192283,143182,65471,21952,5568,732,-24,-12])),180)
assert hc(N,0)==N0 and hc(N,1)==N1
assert F(180)*(216+F(2441,10))==82818
assert 732+F(5568,10)+F(21952,100)-1440==F(1708,25)>0
# Record ALL C2..9 ordinary vectors after explicit monomial clears.
cmults=[(2,10,6),(3,2,5),(4,20,4),(5,20,3),(6,20,2),(7,40,1),(8,-48,0)]
cv={}
for j,s,rq in cmults:
 pp=hc(C37,j);assert all(a>=rq for a,k in pp)
 cv[j]={(a-rq,0):x/s for (a,k),x in pp.items()}
 assert all(x.denominator==1 for x in cv[j].values())
assert hc(C37,9)==scale(prod(Q,B),-10080)
cpay=[cv[3][3,0]+cv[3][2,0]+cv[3][1,0],cv[4][3,0]+cv[4][2,0]+cv[4][1,0],cv[5][3,0]+cv[5][2,0]+cv[5][1,0]+cv[5][0,0],cv[6][3,0]+cv[6][2,0]/3+cv[6][1,0]/9+cv[6][0,0]/27]
assert all(x>0 for x in cpay)
for j in [3,4]:assert {a for a,k in cv[j] if cv[j][a,k]<0}=={1,2}
assert {a for (a,k),x in cv[5].items() if x<0}=={0,1,2} and {a for (a,k),x in cv[6].items() if x<0}=={0,1,2}
assert cv[7][3,0]==1203 and cv[7][2,0]==-29341 and 1203*10<29341 and all(cv[8][a,0]>0 for a in range(4))
def athalf(pp):
 out=defaultdict(F)
 for (a,j),x in pp.items():out[a,0]+=x/2**j
 return clean(out)
AB=mul(A37,B37)
ABdelta=scale(add(add(athalf(AB),scale(hc(AB,0),-1)),scale(hc(AB,1),F(-1,2))),4)
Cb=summ([hc(C37,2),scale(hc(C37,7),F(1,32)),scale(hc(C37,8),F(1,64)),scale(hc(C37,9),F(1,128))])
R4=scale(summ([scale(power(q,15),216000),ABdelta,mul(FF,Cb)]),4)
assert deg(R4)==(16,0) and len(R4)==17
assert R4[15,0]+R4[16,0]*10==222960>0
assert R4[3,0]+R4[2,0]/3+R4[1,0]/9+R4[0,0]/27==4555019>0
assert all(R4[a,0]>0 for a in range(4,15))
# Req chord from original rational target: no division beyond constants.
V=summ([power(q,2),scale(q,10),scale(h,8)])
Ftarget=add(prod(q,V,add(add(scale(q,3),con(-1)),scale(prod(h,q3),F(1,2)))),scale(prod(Q,power(u,2),q3),-4))
Fzero=prod(power(q,2),add(q,con(-2)),add(con(11),scale(q,-1)))
Fhalf=athalf(Ftarget)
chord=summ([prod(add(one,scale(h,-2)),Fzero),scale(prod(h,Fhalf),2),scale(prod(q3,h,add(con(F(1,2)),scale(h,-1))),4)])
assert Ftarget==chord
fshift=qshift(scale(Fhalf,4),3)
assert fshift==add(qp([198,487,205,13,-3]),{})
physical=add(prod(q,T),scale(prod(u,t2),-4))
physical_rhs=summ([qp([-2,-5,-1,1]),prod(add(con(F(1,2)),scale(h,-1)),add(add(scale(q,10),con(4)),scale(h,8)))])
# q-shift presentation is (q-3)^3+8(q-3)^2+16(q-3)+1.
assert physical==physical_rhs
print('S36 four clears/two jets; S37 original AB+FC, B5/C8/R17 finite sources and all payments PASS',flush=True)
data={'status':'author full finite sources LOCAL, independent audit pending','compact_collection_degree_bounds':collection_bounds,'PJS_derivative7_lower_bounds':[str(x) for x in low],'PJS_derivative_c2_fold':str(dfold),
 'Euler_pair_18_coefficients':[{'c':j,'z':k,'value':str(x)} for (j,k),x in sorted(pairN.items())],'Euler_pair_margins':[str(gamma_c),str(gamma_z)],'Euler_C0_bound':str(euler0),'Euler_BR_margins':[str(x) for x in BRm],
 'H_envelope_degree':deg(HL),'U3_degree':deg(U3),'PJS_envelope_row7_margins':[str(x) for x in emarg],
 'HNe_degree':deg(HNe),'UN_degree':deg(UN),'four_cleared_part_degrees':[deg(x) for x in parts],
 'components_degrees':{nm:deg(x) for nm,x in [('A37',A37),('B37',B37),('C37',C37),('N',N)]},
 'B_five_positive_kernels':{str(j):{'multiplier_description':['12q3(q+3)','6q2','2q','q+3','(q+2)(q+3)(6q+5)'][j],'ordinary_q_vector':qvec(pp),'qminus3_vector':qvec(qshift(pp,3)) if j<3 else None} for j,pp in enumerate(bpolys)},
 'C_2_to_8_kernels':{str(j):{'multiplier_scalar':s,'q_factor':rq,'ordinary_q_vector':qvec(cv[j])} for j,s,rq in cmults},'C9':'-10080(q+1)(q+2)','C_3_to_6_payments':[str(x) for x in cpay],
 'R4_17_q_coefficients':qvec(R4),'R4_two_payments':['222960','4555019'],'N0_factor_q_vector':['8108','21708','22109','10638','2441','216'],'N1_factor_q_vector':['38380','136080','192283','143182','65471','21952','5568','732','-24','-12']}
out=Path(__file__).with_suffix('.exact.json');assert not out.exists();out.write_text(json.dumps(data,indent=2)+'\n')
md=['# S13/S36/S37 全部小有限来源与准确付款（作者 LOCAL）','','公开乘式和正文有限卷积为来源；未用旧136/209/全N九分组。','','## A. 原斜率与Euler小账','',str({k:data[k] for k in ['compact_collection_degree_bounds','PJS_derivative7_lower_bounds','PJS_derivative_c2_fold','Euler_pair_margins','Euler_C0_bound','Euler_BR_margins']}),'']
for row in data['Euler_pair_18_coefficients']:md.append(str(row))
md+=['','## B. 三次包络和四项的无尾次数','',str({k:data[k] for k in ['H_envelope_degree','U3_degree','PJS_envelope_row7_margins','HNe_degree','UN_degree','four_cleared_part_degrees','components_degrees']}),'','## C. 全部五个B核与三个平移','']
for j,row in data['B_five_positive_kernels'].items():md.append(j+': '+str(row))
md+=['','## D. 全部C2…9核：普通q幂从低到高','']
for j,row in data['C_2_to_8_kernels'].items():md.append(j+': '+str(row))
md+=['9: '+data['C9'],'四准确付款='+str(data['C_3_to_6_payments']),'','## E. 保留实际零次与一次h信用；全部17项R','', 'N0核=['+', '.join(data['N0_factor_q_vector'])+']','N1核=['+', '.join(data['N1_factor_q_vector'])+']','4R=['+', '.join(data['R4_17_q_coefficients'])+']','两准确付款='+str(data['R4_two_payments']),'']
gen=Path(__file__).with_suffix('.generated.md');assert not gen.exists();gen.write_text('\n'.join(md)+'\n')
print('Complete tiny vectors and finite product degree ledger saved, author LOCAL only',flush=True)
