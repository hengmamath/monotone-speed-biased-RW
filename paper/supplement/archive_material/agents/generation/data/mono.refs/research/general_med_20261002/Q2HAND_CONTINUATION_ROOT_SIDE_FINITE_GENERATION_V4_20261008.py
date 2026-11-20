"""Q2 S7--10 original root finite identities, stdlib Fraction only.
Source coordinates x=1/q,h; no old model imports or coefficient input.
Author LOCAL. Full source arrays printed after generation, not definitions.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import comb
import json
P=Path(__file__).resolve().parent
def clean(a):return {m:v for m,v in a.items() if v}
def con(v):return {(0,0):F(v)} if v else {}
def add(a,b):
 d=defaultdict(F,a)
 for m,v in b.items():d[m]+=v
 return clean(d)
def sc(a,v):return clean({m:x*F(v) for m,x in a.items()})
def mul(a,b):
 d=defaultdict(F)
 for (i,j),v in a.items():
  for (k,l),w in b.items():d[i+k,j+l]+=v*w
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
def df(a,j):return {tuple(m[k]-(k==j) for k in range(2)):v*m[j] for m,v in a.items() if m[j]}
def divide(a,b):
 r=dict(a);out={};bm=max(b);bc=b[bm]
 while r:
  rm=max(r);dm=tuple(rm[i]-bm[i] for i in range(2));assert min(dm)>=0,('not polynomial',rm,bm)
  z={dm:r[rm]/bc};out=add(out,z);r=add(r,sc(mul(z,b),-1))
 return out
def remove(a,k,j=0):
 assert all(m[j]>=k for m in a),('monomial removal',j,k)
 return {tuple(m[i]-(k if i==j else 0) for i in range(2)):v for m,v in a.items()}
def subst(a,j,v):
 d=defaultdict(F)
 for m,w in a.items():d[tuple(m[i] if i!=j else 0 for i in range(2))]+=w*F(v)**m[j]
 return clean(d)
def shift(a,j,v):
 out={}
 for m,w in a.items():
  for k in range(m[j]+1):out=add(out,{tuple(m[i] if i!=j else k for i in range(2)):w*comb(m[j],k)*F(v)**(m[j]-k)})
 return out
def reversex(a,n):
 assert deg(a)[0]<=n
 return {(n-i,j):v for (i,j),v in a.items()}
def vec(a,j=0,n=None):
 if n is None:n=deg(a)[j]
 assert all(not m[1-j] for m in a)
 return [a.get(tuple(k if i==j else 0 for i in range(2)),F(0)) for k in range(n+1)]
def txt(v):return '['+', '.join(str(x) for x in v)+']'
one=con(1);x={(1,0):F(1)};h={(0,1):F(1)}
U=add(one,x);L=add(one,mul(h,x));D=sm([one,sc(x,2),prod(h,pw(x,2))]);d=add(one,sc(h,-1));c=prod(h,x)
AL=sm([con(12),sc(c,6),sc(pw(c,2),-1)])
AU=sm([con(24),sc(c,12),sc(pw(c,2),-2),pw(c,3)])
TG=sm([con(12),sc(x,16),sc(pw(x,2),6),sc(c,6),sc(prod(h,pw(x,2)),5)])
D2=sm([con(2),sc(x,3),prod(h,pw(x,2))])
fac={'X':x,'U':U,'L':L,'D':D,'AL':AL,'AU':AU,'TG':TG,'D2':D2}
class Ex:
 def __init__(self,ts=()):self.ts=[(n,d) for n,d in ts if n]
 def __add__(self,o):return Ex(self.ts+o.ts)
 def __sub__(self,o):return self+o.sc(-1)
 def sc(self,v):return Ex([(sc(n,v),d) for n,d in self.ts])
 def __mul__(self,o):
  out=[]
  for n,d in self.ts:
   for m,e in o.ts:
    ds=dict(d)
    for k,v in e.items():ds[k]=ds.get(k,0)+v
    out.append((mul(n,m),ds))
  return Ex(out)
 def __pow__(self,n):
  out=ex()
  for _ in range(n):out=out*self
  return out
def ex(n=one,v=1,**ds):return Ex([(sc(n,v),ds)])
def cl(e,v=1,**ds):
 out={};bounds=[]
 for n,nd in e.ts:
  p=sc(n,v);bd=list(deg(n));assert all(k in ds for k in nd)
  for k,ee in ds.items():
   rem=ee-nd.get(k,0);assert rem>=0,(k,ee,nd)
   bd=[bd[j]+rem*deg(fac[k])[j] for j in range(2)]
   p=mul(p,pw(fac[k],rem))
  bounds.append(bd);out=add(out,p)
 return out,[max(b[j] for b in bounds) for j in range(2)]
t=ex(pw(U,2),X=1,L=1,D=1);r=ex(U,D=1)
A=ex(prod(pw(L,2),x),D=1);B=ex(prod(d,x),D=1)
P2=A*(A+B);P3=A*(A*A+(A*B).sc(4)+B*B)
P5=A*(A**4+(B*A**3).sc(26)+(B**2*A**2).sc(66)+(B**3*A).sc(26)+B**4)
ae=ex(add(one,sc(c,F(1,2))));al=ex(AL,F(1,12));au=ex(AU,F(1,24))
TU=t*(au+A.sc(F(1,2))+P2*ex(v=2,AU=1))
# The P5 coefficient is -12^3/360=-24/5, not a new price.
PL=t*ex(L=1)*(al*al+(al*A).sc(2)+P2.sc(F(11,12))+P3*ex(v=2,AL=1)-P5*ex(v=F(24,5),AL=3))
theta=ex(add(con(6),sc(x,5)),F(1,6),U=1);R=theta*ex(X=1)
b=ex(prod(d,x),U=1)
al0=ex(add(pw(L,2),prod(d,add(L,one),x)),U=1)
al1=ex(prod(d,add(L,one),x),-1,U=1)
W0=ex(c,L=1)-ex()+b*ex(v=2,L=1)
Wp=ex(c)*W0+b*ex(v=4,L=1)-(r*(b*ex(L=1)+ex(prod(d,x),2,D=1))).sc(2)
Bi0=al0*ex(v=2,L=1)
Bi1=(al1+ex(h))*ex(v=2,L=1)+(r*b)*ex(v=2,X=1,L=1)+(r*r*b)*ex(v=4,X=1)
E=ex(prod(pw(d,2),pw(x,2)),U=2)
Uhi=t*(ae+A.sc(F(1,2))+P2.sc(F(1,12)))
Plo=t*ex(L=1)*(ex(sm([one,c,sc(pw(c,2),F(1,12)),sc(pw(c,3),F(-1,12))]))+(al*A).sc(2)+P2.sc(F(11,12))+(ex(add(one,sc(c,F(-1,2))))*P3).sc(F(1,6))-P5.sc(F(1,360)))
Vhat=(ex()+ex(c)*R).sc(-1)
Vhat=Vhat*Uhi+(ex()+ex(add(L,one))*R)*Plo-(R*ex(L)*r*r).sc(4)-(R*t).sc(2)
Ws=W0+R*Wp;Bi=Bi0+theta*Bi1;Cal=al0+theta*(al1+ex(L,X=1))
Fhat=Vhat+Ws-theta*ex(d,2,L=1)
Ghat=Bi-Vhat.sc(2);Khat=Vhat+Cal*ex(v=2,L=1)-(ae*R*r).sc(F(3,2))
g0=Fhat-ex(v=F(2,15));gs=[g0,g0+(E*Ghat).sc(F(1,2)),g0+E*Ghat+E*E*Khat]
Ns=[];source_bounds=[];divisions=[]
for j,g in enumerate(gs):
 n,bd=cl(g,2160,X=2,U=2+2*j,L=2,D=6)
 z=remove(n,2);divs=['X^2']
 if j:z=divide(z,L);divs.append('L')
 Ns.append(z);source_bounds.append(bd);divisions.append(divs)
 print('S10 original g numerator',j,'structural clear',bd,'post division actual',deg(z),'nonzero',len(z),flush=True)
prefixes=[];tails=[];curvmargins=[];hzero=[]
for j,N in enumerate(Ns):
 M={}
 for (k,l),v in N.items():
  if l==2:M=add(M,{(k,0):2*v})
  elif l>=3 and v>0:M=add(M,{(k,0):v*l*(l-1)/2**(l-2)})
 mv=vec(M);kk=[6,8,7][j];pre=[-v for v in mv[:kk]];tail=mv[kk:]
 cap=[4400000,14600000,42000000][j]
 assert min(pre)>0 and min(tail)>0 and max(tail)<=cap
 margin=pre[2]-F(3,2)*cap/F(3)**(kk-2);assert margin>0
 prefixes.append(pre);tails.append(tail);curvmargins.append(margin)
 n0=subst(N,1,0)
 # Match positive q denominators by reversal then exact factors:
 # Nj(x,0)=2? x^(dj−n) Hnj(q); Dj powers yield deg 8,9,10.
 qnum=reversex(n0,[8,10,12][j]);qnum=sc(qnum,F([90,90,180][j],2160))
 if j:qnum=divide(qnum,add(con(2),x)) if j==1 else divide(divide(qnum,add(con(2),x)),add(con(2),x))
 hz=vec(shift(qnum,0,3));assert min(hz)>0;hzero.append(hz)
 print('S10 curvature source and h0',j,'margin',margin,'q3 slots',len(hz),flush=True)
# Half endpoint from original Fhat,Ghat, after h substitution and q reversal.
FN,fb=cl(Fhat-ex(v=F(3,20)),17280,X=2,U=2,L=2,D=6)
GN,gb=cl(Ghat+ex(),8640,X=2,U=2,L=2,D=6)
NF=reversex(subst(remove(FN,2),1,F(1,2)),18)
NG=reversex(subst(remove(GN,2),1,F(1,2)),18)
# x-form positive denominator gives factor 1/256 from L²D6 at hhalf.
NF=sc(NF,256);NG=sc(NG,256)
nf=vec(NF,0,18);ng=vec(NG,0,18)
RF=[-v for v in nf[:11]];PG=ng[:15]
assert nf[11:]==list(map(F,[-684364272,-328291360,-72321344,18298240,19749120,6739968,1121280,73728]))
assert ng[15:]==list(map(F,[735373056,109363200,3671040,-737280]))
assert min(RF)>0 and max(RF)<=912655344 and min(PG)>0
CF=F(6739968)*27+19749120*9+18298240*3-72321344-F(328291360,3)-F(684364272,9)-F(912655344,18)
assert CF==F(318361768,3)>0
wh=Wp-(ex(v=F(3,2))-r)*ex(x,L=1,U=1)+(r*r)*ex(x,v=2,U=1)
wn,wb=cl(wh,X=1,U=2,L=1,D=2)
assert not subst(wn,1,F(1,2))
print('S10 original two hhalf endpoints 19+19 slots, Wp source identity PASS',flush=True)
# S8 exact original root theta upper: TU and Tg, not Uhi.
Tg=ex(add(con(6),sc(x,5)),2,X=1,TG=1)
SN,sb=cl(Tg-ex(U=2)*(ex()+TU),24,X=1,U=2,L=1,D=3,AU=1,TG=1)
SN=remove(SN,1)
print('S8 original theta numerator',deg(SN),'source',sb,flush=True)
# S9 original upper VR using complete upper PL and lower TU.
Pup=t*ex(L=1)*(ae*ae+(ae*A).sc(2)+P2.sc(F(11,12))+P3.sc(F(1,6)))
Ulo=t*(al+A.sc(F(1,2)))
Vbar=ex(c,-1)*Ulo+ex(add(L,one))*Pup-(ex(L)*r*r).sc(4)-t.sc(2)
Sbar=Vbar*ex(X=1)+Wp*ex(X=1)-ex(d,2,L=1)
S9,s9b=cl(Sbar.sc(-1),12,X=2,U=1,L=2,D=4);S9=remove(S9,2)
Pup0=Pup-(t*ex(L=1)*P3).sc(F(1,6))
Vbar0=ex(c,-1)*Ulo+ex(add(L,one))*Pup0-(ex(L)*r*r).sc(4)-t.sc(2)
D0=Bi1-(Vbar0*ex(X=1)).sc(2)
DS,dsb=cl(D0.sc(-1)-ex(v=F(33,64)),192,X=2,U=1,L=2,D=4);DS=divide(remove(DS,2),D)
DSq=reversex(DS,9);DSq3=shift(DSq,0,3)
# g=1/2−h ordinary h blocks in q−3
DSqg={}
for (k,l),v in DSq3.items():
 for a in range(l+1):DSqg=add(DSqg,{(k,a):v*comb(l,a)*F(1,2)**(l-a)*(-1)**a})
print('S9 original two numerators',deg(S9),deg(DS),'clear bounds',s9b,dsb,flush=True)

# Original short Vbar collection: full finite zero identity.
VBt=t*ex(v=F(1,12),L=1)*(ex(prod(pw(c,3),add(con(2),sc(c,-1))),-1)+(ex(prod(c,add(one,sc(c,-1))))*A).sc(-6)+(ex(add(L,one))*P2).sc(11)+(ex(add(L,one))*P3).sc(2))
vbz,vbb=cl(Vbar-VBt,12,X=1,L=2,D=4);assert not vbz
# S8 fold every and only negative higher-h coefficient to h.
L0={m:F(v) for m,v in SN.items() if m[1]==1}
L0={(k,0):v for (k,j),v in L0.items()}
for (k,j),v in SN.items():
 if j>=2 and v<0:L0=add(L0,{(k,0):v/F(2)**(j-1)})
lv=vec(L0)
assert not lv[0] and not lv[1] and all(v>0 for v in lv[2:6]) and all(v<0 for v in lv[6:])
theta_credit=lv[3]+sum(lv[k]/F(3)**(k-3) for k in range(6,len(lv)))
assert theta_credit==F(157993241,118098)>0
# S9 coefficient lower envelopes, full n0..n7.
slope_low=[]
for k in range(8):
 row=[S9.get((k,j),F(0)) for j in range(8)]
 extract=0 if k<=5 else k-5
 assert not any(row[:extract]);row=row[extract:]
 a0=row[0];a1=row[1] if len(row)>1 else F(0)
 a1+=sum(v/F(2)**(j-1) for j,v in enumerate(row) if j>=2 and v<0)
 lower=a0+min(a1,F(0))/2
 slope_low.append(lower)
assert slope_low==list(map(F,[0,F(1,4),F(43,16),F(55,8),F(1587,32),F(331,4),F(1215,16),F(579,8)]))
slopetail=F(381,16)-F(101,48)-F(35,144)-F(1,144)
assert slopetail==F(515,24)>0
# All ten source-gap g lower envelopes after q3 reversal.
gap_lowers=[]
for k in range(10):
 row=[DSqg.get((k,j),F(0)) for j in range(7)]
 ss=row[1]+sum(v/F(2)**(j-1) for j,v in enumerate(row) if j>=2 and v<0)
 assert row[0]>0 and ss>0;gap_lowers.append([row[0],ss])
# Three ordinary polynomial physical checks used for Ktheta and speed gamma.
qphysical=add(con(3),x)
kq=sm([con(20),sc(x,48),sc(pw(x,2),9)])
assert sm([sc(pw(qphysical,2),9),sc(qphysical,-6),con(-43)])==kq
assert F(1,60)-F(1,128)==F(17,1920)>0 and F(1,60)-F(1,64)==F(1,960)>0
print('S8 complete negative fold/eight payment; S9 all 8+10 envelopes and exact Vbar zero collection PASS',flush=True)

data={'status':'AUTHOR LOCAL original finite root identities, independent audit pending','source':'new stdlib Fraction, all original physical coordinates fixed',
 'g_clear_structural_bounds':source_bounds,'g_exact_divisions':divisions,'N_degrees':[deg(n) for n in Ns],
 'N_arrays':[{f'{k},{l}':str(v) for (k,l),v in sorted(n.items())} for n in Ns],
 'curvature_prefixes':[[str(v) for v in a] for a in prefixes],'curvature_tails':[[str(v) for v in a] for a in tails],'curvature_margins':[str(v) for v in curvmargins],
 'h0_q3':[[str(v) for v in a] for a in hzero],'NF_half':[str(v) for v in nf],'NG_half':[str(v) for v in ng],
 'S8_theta_array':{f'{k},{l}':str(v) for (k,l),v in sorted(SN.items())},'S8_structural_clear_bound':sb,
 'S9_slope_array':{f'{k},{l}':str(v) for (k,l),v in sorted(S9.items())},'S9_slope_structural_clear_bound':s9b,
 'S9_D0_q3_g_array':{f'{k},{l}':str(v) for (k,l),v in sorted(DSqg.items())},'S9_D0_structural_clear_bound':dsb,
 'S8_lower_fold':[str(v) for v in lv],'S8_eight_debt_credit':str(theta_credit),'S9_n0_n7_lower':[str(v) for v in slope_low],'S9_last4_credit':str(slopetail),'S9_D0_linear_envelopes':[[str(v) for v in a] for a in gap_lowers],'Vbar_collection_structural_zero_bound':vbb,'RF_half_credit':str(CF),'scope':'S8--10 identities only; continuous inequalities and all original-kernel/theta interfaces still paper obligations.'}
stem=Path(__file__).with_suffix('')
Path(str(stem)+'.exact.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
lines=['## 根侧全部有限来源附录','', '普通乘法为二维卷积；所有列表低次到高次。正文的每个命名分母仅乘非负次幂，随后显示精确X²和L除法。原物理A=L²x/D，B=dx/D，t=U²/(xLD)，r=U/D，theta=(6+5x)/(6U)，所有零槽与次数由本来源排除。']
for j,N in enumerate(Ns):
 lines+=['',f'### N{j}完整h行，x普通系数；实际次数{deg(N)}，原清分子次数界{source_bounds[j]}，除项{divisions[j]}']
 for l in range(deg(N)[1]+1):lines.append(f'h^{l}: `'+txt([N.get((k,l),F(0)) for k in range(deg(N)[0]+1)])+'`')
 lines+=['','曲率前缀：`'+txt(prefixes[j])+'`；尾：`'+txt(tails[j])+'`；严格付款：`'+str(curvmargins[j])+'`。','h0的完整q−3向量：`'+txt(hzero[j])+'`。']
lines+=['','NF_half完整19槽：`'+txt(nf)+'`；NG_half完整19槽：`'+txt(ng)+'`。']
for name,n in [('S8 theta',SN),('S9 slope',S9),('S9 D0(q−3,g)',DSqg)]:
 lines+=['',f'### {name} 完整行，次数{deg(n)}']
 if name.startswith('S9 D0'):
  for k in range(deg(n)[0]+1):lines.append(f'y^{k}: `'+txt([n.get((k,l),F(0)) for l in range(deg(n)[1]+1)])+'`')
 else:
  for l in range(deg(n)[1]+1):lines.append(f'h^{l}: `'+txt([n.get((k,l),F(0)) for k in range(deg(n)[0]+1)])+'`')
lines+=['','S8完整L0系数：`'+txt(lv)+'`；八债余量：`'+str(theta_credit)+'`。','S9 n0…n7提取后的完整下界：`'+txt(slope_low)+'`；末4项余量：`'+str(slopetail)+'`。','S9 10个D0线性下界(常数,斜率)：`'+str([[str(v) for v in a] for a in gap_lowers])+'`。','原Vbar短收集完整零身份的结构界：`'+str(vbb)+'`；每个槽均为零，须按正文乘因子有限核验。']
Path(str(stem)+'.generated.md').write_text('\n'.join(lines)+'\n')
print('Original root finite source LOCAL PASS; all continuous proof obligations remain explicit',flush=True)
