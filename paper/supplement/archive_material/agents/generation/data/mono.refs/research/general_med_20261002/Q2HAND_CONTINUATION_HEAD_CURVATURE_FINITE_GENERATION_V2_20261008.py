"""Self-contained original Q2 eight-product head source, Fraction only.
Actual projective t, complete alpha component, exact derivative K, hzero8,
hhalf9 and21 controls. No old factory/arrays/imports/certificate execution.
Author finite arithmetic LOCAL, not a short proof or independent verdict.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import comb
import json
P=Path(__file__).resolve().parent
def clean(a):return {m:x for m,x in a.items() if x}
def con(x):return {(0,0,0):F(x)} if x else {}
def add(a,b):
 d=defaultdict(F,a)
 for m,x in b.items():d[m]+=x
 return clean(d)
def scale(a,x):return clean({m:z*F(x) for m,z in a.items()})
def mul(a,b):
 d=defaultdict(F)
 for m,x in a.items():
  for n,y in b.items():d[tuple(j+k for j,k in zip(m,n))]+=x*y
 return clean(d)
def power(a,n):
 d=con(1)
 for _ in range(n):d=mul(d,a)
 return d
def prod(*aa):
 d=con(1)
 for a in aa:d=mul(d,a)
 return d
def summ(aa):
 d={}
 for a in aa:d=add(d,a)
 return d
def deg(a):return tuple(max((m[j] for m in a),default=-1) for j in range(3))
def diff(a,j):return {tuple(m[k]-(k==j) for k in range(3)):x*m[j] for m,x in a.items() if m[j]}
q={(1,0,0):F(1)};h={(0,1,0):F(1)};t={(0,0,1):F(1)};one=con(1)
Q=add(q,one);u=add(q,h);d=add(one,scale(h,-1));RN=add(scale(q,6),con(5));Wh=add(one,t)
Ph=add(q,prod(add(add(q,con(-1)),h),t));Fh=add(h,t);F2h=add(h,scale(t,2));Mh=add(u,mul(Q,t))
Ih=add(scale(q,2),F2h);Jh=add(scale(q,4),scale(F2h,-1))
AN=add(scale(prod(power(u,2),Q),6),prod(d,add(scale(q,2),h)));AL=summ([scale(power(q,2),12),scale(prod(q,h),6),scale(power(h,2),-1)])
CT=add(scale(Q,6),prod(h,RN));CP=add(scale(Q,6),prod(add(scale(q,2),h),RN));CN=add(AN,prod(q,h,RN,Q))
Th=summ([scale(prod(power(Q,2),Mh,Ph),6),scale(prod(AN,Wh,Ph),-1),scale(prod(q,u,RN,Q,Wh,Ph),-1),
 prod(add(scale(q,2),h),RN,Q,Mh,Ph),scale(prod(q,RN,Q,Wh,u,Mh),-1)])
Bh=prod(u,Fh);Zh=prod(q,d,t)
R2=prod(Bh,add(Bh,Zh));R3=prod(Bh,summ([power(Bh,2),scale(prod(Bh,Zh),4),power(Zh,2)]))
f0q=summ([scale(prod(q,power(Mh,4),AL),F(1,12)),scale(prod(power(q,2),power(Mh,3),Bh),F(1,2)),scale(prod(power(Mh,2),add(scale(q,2),scale(h,-1)),R2),F(1,24))])
gg=summ([scale(prod(q,power(Mh,2),add(scale(q,2),h),Bh),F(1,2)),scale(prod(q,Mh,R2),F(1,2)),scale(R3,F(1,12))])
j0=add(scale(prod(power(q,2),power(Mh,4),power(add(scale(q,2),h),2)),F(1,4)),scale(prod(power(q,2),power(Mh,2),R2),F(-1,12)))
terms=[scale(prod(power(q,2),CN,Ph,Fh,power(Mh,5)),1440),scale(prod(power(q,4),RN,d,t,Q,Ph,Fh,power(Mh,4)),1440),
 scale(prod(power(q,3),u,Q,RN,Wh,d,t,Ih,Ph,Fh,power(Mh,3)),720),scale(prod(Fh,power(Mh,4),AL,Jh,Th),30),
 scale(prod(u,Q,power(Wh,2),Ph,F2h,CT,f0q),720),scale(prod(Q,power(Wh,2),Ph,CP,add(prod(q,Mh,Ih,gg),prod(F2h,j0))),-720),
 scale(prod(power(q,3),power(u,2),Q,RN,power(Wh,2),Ph,Fh,Ih,power(Mh,3)),1440),scale(prod(power(q,4),u,Q,RN,power(Wh,2),Ph,F2h,power(Mh,4)),1440)]
# Exact finite proofs of the two highest-q cancellations; factor suggestions
# were exploratory, but these products are verified solely by Fraction.
q11p=summ([scale(prod(power(h,2),power(t,2)),15),scale(prod(power(h,2),t),84),scale(power(h,2),105),
 scale(prod(h,power(t,3)),30),scale(prod(h,power(t,2)),176),scale(prod(h,t),260),scale(h,42),scale(power(t,3),76),scale(power(t,2),168),scale(t,56)])
high11=[scale(prod(add(h,one),Fh,power(Wh,6)),8640),scale(prod(t,d,Fh,power(Wh,5)),8640),scale(prod(t,d,Fh,power(Wh,5)),8640),{},
 scale(prod(add(h,one),F2h,power(Wh,7)),4320),scale(prod(power(Wh,5),q11p),-1440),
 scale(prod(Fh,power(Wh,5),summ([scale(prod(h,t),21),scale(h,33),scale(power(t,2),6),scale(t,29),con(11)])),2880),
 scale(prod(F2h,power(Wh,6),summ([scale(prod(h,t),12),scale(h,30),scale(t,29),con(11)])),1440)]
high12=[{},{},{},{},{},scale(prod(power(Wh,6),summ([prod(h,t),scale(h,3),scale(power(t,2),2),scale(t,4)])),-8640),
 scale(prod(Fh,power(Wh,6)),17280),scale(prod(F2h,power(Wh,7)),8640)]
for j,pp in enumerate(terms):
 for degree,expected in [(11,high11[j]),(12,high12[j])]:
  assert {(0,b,c):x for (a,b,c),x in pp.items() if a==degree}==expected
assert not summ(high11) and not summ(high12)
N0h=summ(terms)
BAh=add(scale(prod(q,add(prod(h,Wh,add(scale(q,6),h)),scale(prod(q,d,t),12))),4),prod(Wh,AL,F2h))
Nah=scale(prod(Ph,Fh,power(Mh,4),AN,BAh),30)
A20h=add(scale(diff(N0h,1),20),scale(diff(Nah,1),-1))
Pi=diff(A20h,1);K=add(scale(prod(add(t,scale(h,2)),diff(Pi,1)),-1),scale(Pi,3))
assert deg(Pi)[2]==8 and deg(K)==(10,9,9) and len(K)==499
def qp(cs):return {(i,0,0):F(x) for i,x in enumerate(cs) if x}
c0=qp([39,215,383,-7905,-3094,12258,3160,480]);c1=qp([1184,3404,-4256,11772,27208,3200,960]);d2=qp([1150,10040,11430,8140,10400,2400]);c3=scale(prod(RN,add(power(q,2),con(-1))),400)
last={(i,j,0):x for (i,j,k),x in K.items() if k==9}
assert scale(last,-1)==scale(prod(power(Q,2),summ([c0,prod(h,c1),scale(prod(power(h,2),d2),-1),prod(power(h,3),c3)])),360)
assert add(c1,scale(d2,F(-1,2)))==qp([609,-1616,-9971,7702,22008,2000,960])
assert F(12258)-F(3094,3)-F(7905,9)>10000 and F(7702)-F(9971,3)-F(1616,9)>4000
print('Original eight projective products',deg(N0h),len(N0h),'alpha',deg(Nah),'Pi',deg(Pi),'K',deg(K),len(K),'PASS',flush=True)
def fixvar(pp,j,x):
 out=defaultdict(F)
 for m,z in pp.items():
  n=list(m);n[j]=0;out[tuple(n)]+=z*F(x)**m[j]
 return clean(out)
def pick(pp,j,x):return {tuple(m[k] if k!=j else 0 for k in range(3)):z for m,z in pp.items() if m[j]==x}
def qvec(pp):return [str(pp.get((i,0,0),F())) for i in range(deg(pp)[0]+1)]
def atq(pp,x):return sum(z*F(x)**i for (i,j,k),z in pp.items())
def fold(pp,r):
 aa=[pick(pp,1,j) for j in range(r+1)]
 tail={}
 for (i,j,k),z in pp.items():
  if j>r and z<0:tail=add(tail,{(i,0,k):z/2**(j-r)})
 aa[r]=add(aa[r],tail)
 return [summ([scale(aa[j],F(comb(l,j),comb(r,j)*2**j)) for j in range(l+1)]) for l in range(r+1)]
def debt(pp,dg):return sum(-z/3**(dg-i) for (i,j,k),z in pp.items() if i<dg and z<0)
fr=[1,1,1,2,2,1,1,1];caps=[9,9,9,8,8,8,9,9];bounds=[2000000,17000000,17000000,67000000,31000000,31000000,5000000,3000000]
controls=[]
for j,(r,dg,lo) in enumerate(zip(fr,caps,bounds)):
 for l,pp in enumerate(fold(pick(K,2,j),r)):
  assert deg(pp)==(10,0,0)
  main={ (i-dg,0,0):z for (i,h,k),z in pp.items() if i>=dg}
  if dg==9:
   assert main[1,0,0]>0;primary=atq(main,3)
  else:
   assert main[2,0,0]<0;primary=min(atq(main,3),atq(main,10))
  dd=debt(pp,dg);margin=primary-dd;assert margin>=lo
  controls.append({'t_degree':j,'fold_r':r,'control':l,'q_cap':dg,'full_q_vector':qvec(pp),'debt':str(dd),'primary':str(primary),'margin':str(margin),'lower':lo})
E={}
for (i,j,k),z in K.items():E=add(E,{(i+k-1,j,0):z*F(512,360*2**k)})
assert deg(E)==(17,9,0)
ec=[]
for l,(pp,dg,lo) in enumerate(zip(fold(E,2),[12,12,11],[5000000,8000000,36000000])):
 main={(i-dg,0,0):z for (i,j,k),z in pp.items() if i>=dg};dd=debt(pp,dg);dd2=diff(diff(main,0),0)
 n=deg(main)[0];cs=[main.get((i,0,0),F()) for i in range(n,-1,-1)]
 if dg==12:
  a,b,c0,di,ei,fi=cs;assert a<0 and b<0 and di>0 and ei>0
  low=di+125*a+25*b+min(F(),5*c0)
 else:
  a,b,c0,di,ei,fi,gi=cs;assert a<0 and b<0 and c0<0 and di>0 and ei>0 and fi>0
  low=di+125*a+25*b+5*c0
 lowconst=main.get((0,0,0),F())-dd;high=min(atq(main,5),atq(main,10))-dd
 assert low>0 and lowconst>=lo and atq(dd2,5)<0 and high>=lo
 ec.append({'control':l,'q_cap':dg,'full_q_vector':qvec(pp),'debt':str(dd),'low_coefficient':str(low),'low_constant':str(lowconst),'Rdd_at5':str(atq(dd2,5)),'high_margin':str(high),'lower':lo})
assert len(controls)==18 and len(ec)==3
print('All18 prefix+3 real endpoint full q profiles and payments PASS',flush=True)
# Undo t=qv/U, U=W-qv using homogeneous degree8; third coordinate becomes v.
W=add(q,con(2));v=t;U=add(W,scale(prod(q,v),-1))
def undo(pp):
 out={}
 for (i,j,k),z in pp.items():
  assert j==0 and k<=8
  out=add(out,scale(prod(power(q,i+k),power(v,k),power(U,8-k)),z))
 return out
Tzero=undo(fixvar(A20h,1,0))
assert all(i>=9 and k>=1 for i,j,k in Tzero)
Ft={(i-9,0,k-1):z/240 for (i,j,k),z in Tzero.items()};assert deg(Ft)==(9,0,7)
def divide_q(pp,cc):
 n=deg(pp)[0];bs=[F() for _ in range(n)];bs[-1]=pp.get((n,0,0),F())
 for i in range(n-1,0,-1):bs[i-1]=pp.get((i,0,0),F())-cc*bs[i]
 assert pp.get((0,0,0),F())-cc*bs[0]==0
 out={(i,0,0):z for i,z in enumerate(bs) if z};assert mul(add(q,con(cc)),out)==pp
 return out
pih0=[]
for j in range(8):
 aj=summ([scale(pick(Ft,2,k),comb(7-k,j-k)) for k in range(j+1)])
 pp=aj
 for _ in range(7-j):pp=divide_q(pp,2)
 assert deg(pp)==(j+2,0,0)
 pih0.append(pp)
# Physical half face, source G not old nine residual arrays.
Gface=add(undo(fixvar(Pi,1,F(1,2))),scale(prod(power(q,18),v),144000))
assert deg(Gface)==(18,0,8)
Lj=[15552,248832,870912,870912,108864,108864,54432,7776,486];sj=[5,5,5,5,1,5,5,5,5];q4=add(q,con(4))
cc=F(1680000*5**6,6**6);faces=[]
def shiftq(pp,a):
 out={}
 for (i,j,k),z in pp.items():
  assert j==k==0
  for l in range(i+1):out[l,0,0]=out.get((l,0,0),F())+z*comb(i,l)*a**(i-l)
 return clean(out)
for j in range(9):
 bj=summ([scale(pick(Gface,2,k),F(comb(8-k,j-k),comb(8,j))) for k in range(j+1)])
 dc=summ([scale(power(q4,2),F(j*(j-1),56)),scale(q4,-2*j),con(64)])
 rn=add(mul(power(q4,2),bj),scale(prod(power(W,6),power(q,12),dc),-cc))
 assert all(i>=1 for i,h,k in rn)
 pp={(i-1,0,0):z*F(Lj[j],sj[j]) for (i,h,k),z in rn.items()}
 if j==0:
  for _ in range(6):pp=divide_q(pp,2)
 assert deg(pp)==((13 if j==0 else 19),0,0) and all(z.denominator==1 for z in pp.values())
 rho10=atq(rn,10)/F(10**18*14**2);assert rho10>300
 faces.append({'j':j,'full_ordinary_q_vector':qvec(pp),'f_at10':str(atq(pp,10)),'rho_at10':str(rho10)})
 pp0=pp
 a=8 if j==5 else 4 if j==6 else 3;cut={0:14,1:20,2:19,3:17,4:10,5:7,6:14,7:14,8:13}[j]
 sh=shiftq(pp,a);assert all((z>0 if i<cut else z<0) for (i,h,k),z in sh.items()) and len(sh)==deg(pp)[0]+1
 faces[-1].update({'main_shift':a,'main_cut':cut,'full_main_shift_q_vector':qvec(sh)})
 if j in [5,6]:
  fextra=[]
  for a,length,e in ([(3,3,4),(6,2,1)] if j==5 else [(3,1,0)]):
   sh=shiftq(pp0,a);assert all(sh.get((i,0,0),F())>0 for i in range(e+1))
   assert all(i>e for (i,h,k),z in sh.items() if z<0)
   gap=sh[e,0,0]+sum(z*length**(i-e) for (i,h,k),z in sh.items() if z<0);assert gap>0
   fextra.append({'shift':a,'length':length,'power':e,'full_shift_q_vector':qvec(sh),'gap':str(gap)})
  faces[-1]['extra_payments']=fextra
print('Original hzero8 and half moving-square9 fully generated from same source PASS',flush=True)
data={'status':'author original head source/finite controls LOCAL; full proof and independent audit pending','eight_terms_degrees':[deg(x) for x in terms],'N0hat_degree':deg(N0h),'Nalpha_hat_degree':deg(Nah),'Pi_hat_degree':deg(Pi),'K_degree':deg(K),'K_nonzero':len(K),
 'K_full_t_rows_h_rows_q_vectors':[[[str(K.get((i,j,k),F())) for i in range(11)] for j in range(10)] for k in range(10)],
 'prefix18_controls':controls,'endpoint3_controls':ec,'hzero8_Pi_vectors':[qvec(x) for x in pih0],'half9_residuals':faces,
 'N0hat_high_q_rows':{str(i):[[str(N0h.get((i,j,k),F())) for j in range(12)] for k in range(9)] for i in [11,12]},
 'head_finite_origin':'original eight noP4 products with common U8; h derivative fixed q,v equivalent fixed q,t'}
out=Path(__file__).with_suffix('.exact.json');assert not out.exists();out.write_text(json.dumps(data,indent=2)+'\n')
print('499 K source terms/1100 displayedslots plus21 full q controls and9 residual vectors stored; author LOCAL only',flush=True)
md=['# S22/S24/S27/S33完整原头价曲率的有限来源与全部向量（作者LOCAL）','','原八乘积及q11/q12两条有限取消由正文定义；不是从旧499符号表或工厂加载。所有向量低幂到高幂，零槽保留。','','## A. 全部K：10个t行×10个h行×11个q槽=1100槽，499非零','']
for k,rows in enumerate(data['K_full_t_rows_h_rows_q_vectors']):
 md.append('### t^'+str(k))
 for j,row in enumerate(rows):md.append(f'h^{j}: ['+', '.join(row)+']')
 md.append('')
md+=['## B. 全部18前缀控制：各11个q槽','']
for row in controls:md.append(str(row))
md+=['','## C. 全部3真实端点控制：各18个q槽','']
for row in ec:md.append(str(row))
md+=['','## D. h=0八个Pi完整普通q向量','']
for j,row in enumerate(data['hzero8_Pi_vectors']):md.append(f'j={j}: ['+', '.join(row)+']')
md+=['','## E. 半面9个残余量：174普通q槽、174主平移槽、60附加平移槽','']
for row in faces:
 md.append('j='+str(row['j']))
 for key in ['full_ordinary_q_vector','full_main_shift_q_vector']:md.append(key+'=['+', '.join(row[key])+']')
 md.append(str({k:v for k,v in row.items() if k not in ['full_ordinary_q_vector','full_main_shift_q_vector','extra_payments']}))
 for ext in row.get('extra_payments',[]):md.append('附加低区付款='+str(ext))
 md.append('')
md+=['## F. 原式无尾次数台账','',str({k:data[k] for k in ['eight_terms_degrees','N0hat_degree','Nalpha_hat_degree','Pi_hat_degree','K_degree','K_nonzero']}),'']
gen=Path(__file__).with_suffix('.generated.md');assert not gen.exists();gen.write_text('\n'.join(md)+'\n')
print('Complete K/21controls/hzero8/half9 standalone appendix stored',flush=True)
