"""Independently PASSED high-u ORIGINAL root plus COMPLETE s2 payment.

Sign is tested, never assumed. Correct original a calibration; actual proof
still requires 0<a_bar<1, assigned Delta>=0 and canonical moments.
This script concerns only an explicit sufficient scalar payment.
"""
import sympy as S
from fractions import Fraction as F
from math import comb
from itertools import product
l,u,R=S.symbols('l u R')
c=l-1;g=c/(l+1)
lo=2*(g+g**3/3+g**5/5)
up=lo+2*g**7/(7*(1-g*g))
K=S.cancel(c/(l*lo)+(1-u)/2+up*(l+1-2*l*u)*(1-u)/(12*c))
kn,kd=S.fraction(K)
pp=lambda x:S.Poly(x,l,u,R,domain=S.QQ)
L,U,X=pp(l),pp(u),pp(R);ONE=pp(1);C=L-ONE
KN,KD=pp(kn),pp(kd)
A1=L+ONE-L*U
A2=L**2+L+ONE-(L**2+L)*U
RN=(ONE-U)*KD+X**2*(KN-(ONE-U)*KD)
QN=A1*(ONE-U)*KD+L*U*X*(ONE-U)*KD+U*X**2*KD
VD=2*QN-(L+ONE)*U*A1*RN
VN=C*A1*RN
A0N=(ONE-(L+ONE)*U)*A1+L*U*X
AN=A1*(VD-RN*A0N)  # CORRECT original calibration, no extra u.
epN=A1-L*X
root=X*(VD+U*VN)*epN**2-2*(X*VD-AN)*epN*A1
tail=X*(VD+U*VN)*X**2*(A2-L*A1)**2*A1
tail+=2*L*(X*VD-AN)*(A1**2-A2)*X**2*A2
tail+=2*(A1-L)*AN*(A2-A1)*X**2*A2
tail+=2*(A1-L)*X*U*A1*RN*X*((L+ONE)*A2*X-L*A1*X-A1*A2)*A2
P=root*A1*A2**2+2*L*tail
D=L*X*VD*A1**3*A2**2

def original(ll,uu,rr):
 cc=ll-1;aa1=ll+1-ll*uu;zz=rr/aa1;bb=uu*zz
 kk=K.subs({l:ll,u:uu})
 tt=uu*uu*(1+rr*rr*(kk-1+uu)/(1-uu))
 qq=uu+ll*uu*uu*zz+aa1*uu*uu*zz*zz/(1-uu)
 vv=cc*tt/(2*qq-(ll+1)*tt)
 aa=(uu-vv*(1-(ll+1)*uu+ll*bb)/cc)/bb
 r1=1/aa1;r2=aa1/(ll*ll+ll+1-(ll*ll+ll)*uu)
 ee=1-ll*zz
 mm=aa*(1-r2)+vv/cc*(ll+1-ll*r2-1/zz)
 val=((1+vv)*ee**2-2*(1-aa)*ee)/ll
 val+=2*ll*zz**2*((1+vv)*(1-ll*r2)**2/ll
              +2*(1-aa)*(r2-r1)+2*(1/ll-r1)*mm)
 return S.cancel(val),S.cancel(vv),S.cancel(aa)

for point in [(S.Rational(231,200),S.Rational(3,5),S.Rational(19,20)),
              (S.Rational(6,5),S.Rational(1,2),S.Rational(9,10))]:
 ll,uu,rr=point;vs={l:ll,u:uu,R:rr};value,vv,aa=original(*point)
 ev=lambda p:p.eval(vs)
 assert S.cancel(vv-uu*ev(VN)/ev(VD))==0
 assert S.cancel(aa-ev(AN)/(rr*ev(VD)))==0
 assert S.cancel(value-ev(P)/ev(D))==0
 print('ORIGINAL independent whole S2 check',point,flush=True)
print('P degree/terms',P.degree_list(),len(P.terms()),flush=True)

# Preserve actual variance and canonical rho<=1 exactly:
# rho=u A1+(1-u A1)t, 0<=t<=1.  This is only a polynomial sign cover;
# the actual lower-bound argument always retains a_bar<1.
phys=U*A1+(ONE-U*A1)*X
powphys=[ONE]
for j in range(P.degree(R)):powphys.append(powphys[-1]*phys)
fibers={}
for (i,j,k),v in P.terms():
 fibers[k]=fibers.get(k,pp(0))+v*L**i*U**j
Pphys=sum((fibers[k]*powphys[k] for k in fibers),pp(0))
print('Variance cover degree/terms',Pphys.degree_list(),len(Pphys.terms()),flush=True)

# Exact high-u cap: u=1/2+(1/lambda^2-1/2)w.
# lambda<=707/500<sqrt2 ensures this oriented interval is nonempty.
du=Pphys.degree(u);un=L**2+(2-L**2)*U;ud=2*L**2
unpow=[ONE];udpow=[ONE]
for j in range(du):unpow.append(unpow[-1]*un);udpow.append(udpow[-1]*ud)
fibers={}
for (i,j,k),v in Pphys.terms():
 fibers[j]=fibers.get(j,pp(0))+v*L**i*X**k
Q=sum((fibers[j]*unpow[j]*udpow[du-j] for j in fibers),pp(0))
# Remove common positive lambda power, not a numerical simplification.
ml=min(idx[0] for idx,v in Q.terms());Q=Q.exquo(L**ml)
deg=Q.degree_list();print('Exact whole high-u cube degree/terms',deg,len(Q.terms()),flush=True)
cf={}
for (i,j,k),v in Q.terms():
 vv=F(int(v.p),int(v.q))
 for a in range(i+1):
  idx=(a,j,k)
  cf[idx]=cf.get(idx,F(0))+vv*comb(i,a)*F(23,20)**(i-a)*F(33,125)**a
for axis in range(3):
 out={}
 for idx,v in cf.items():
  for a in range(idx[axis],deg[axis]+1):
   ii=list(idx);ii[axis]=a;ii=tuple(ii)
   out[ii]=out.get(ii,F(0))+v*F(comb(a,idx[axis]),comb(deg[axis],idx[axis]))
 cf=out
full=[cf.get(idx,F(0)) for idx in product(*(range(n+1) for n in deg))]
print('High-u ORIGINAL root+s2:',sum(v<0 for v in full),'negative;',
      sum(v>0 for v in full),'positive;',len(full),'total',flush=True)
assert deg==(46,17,5) and len(full)==5076
assert all(v>0 for v in full)
print('COMPLETE SCALAR SIGN independently PASSED SAME-reviewer audit.',flush=True)
