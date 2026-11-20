"""NEW complete s4 payment candidate; corrected calibration from ORIGINAL.

No new speed theorem. The old s2+s3 certificate was INVALID and its
corrected whole-box sign is disproved. This adds the entire positive
s4 term and checks original rational expressions independently of AN.
"""
import sympy as S
from fractions import Fraction as F
from math import comb
from itertools import product
import sys
last=int(sys.argv[1]) if len(sys.argv)>1 else 4
assert 3<=last<=6
l,u,T=S.symbols('l u T')
c=l-1;g=c/(l+1)
ellL=2*(g+g**3/3+g**5/5)
ellU=ellL+2*g**7/(7*(1-g*g))
K=S.cancel(c/(l*ellL)+(1-u)/2+ellU*(l+1-2*l*u)*(1-u)/(12*c))
kn,kd=S.fraction(K)
pp=lambda e:S.Poly(e,l,u,T,domain=S.QQ)
L,U,X=pp(l),pp(u),pp(T);ONE=pp(1);C=L-ONE
KN,KD=pp(kn),pp(kd)
rho=X*(2-X)
# Z_s=N_s/c, eliminating positive c factors before expansion.
Z={s:sum((L**j for j in range(s)),pp(0))
          -U*sum((L**j for j in range(1,s)),pp(0)) for s in range(1,last+2)}
A1=Z[2]
RN=(ONE-U)*KD+rho**2*(KN-(ONE-U)*KD)
QN=A1*(ONE-U)*KD+L*U*rho*(ONE-U)*KD+U*rho**2*KD
VD=2*QN-(L+ONE)*U*A1*RN
VN=C*A1*RN
A0N=(ONE-(L+ONE)*U)*A1+L*U*rho
AN=A1*(VD-RN*A0N) # CORRECT: NO extra U
# Root denominator A1^2 is already covered by Z2^3.
D=Z[last+1]**2
for s in range(2,last+1):D*=Z[s]**3
epN=A1-L*rho
root=rho*(VD+U*VN)*epN**2-2*(rho*VD-AN)*epN*A1
P=root*D.exquo(A1**2)
for s in range(2,last+1):
 Ns,Nm,Np=Z[s],Z[s-1],Z[s+1]
 fs=X**(s-1)*(s-(s-1)*X)
 ds=Ns**3*Np**2*Nm
 tail=rho*(VD+U*VN)*fs**2*(Np-L*Ns)**2*Ns*Nm
 tail+=2*L*(rho*VD-AN)*(Ns**2-Nm*Np)*fs**2*Np*Nm
 tail+=2*(Ns-L*Nm)*AN*(Np-Ns)*fs**2*Np*Nm
 tail+=2*(Ns-L*Nm)*rho*U*A1*RN*fs*((L+ONE)*Np*Nm*fs-L*Ns*Nm*fs-Ns*Np)*Np
 P+=s*L**(s-1)*tail*D.exquo(ds)
# EXACT S_last/u^2=P/[lambda*rho*VD*D].

def original_value(ll,uu,tt):
 cc=ll-1;rr=tt*(2-tt);aa1=ll+1-ll*uu
 zz=rr/aa1;bb=uu*zz
 KK=K.subs({l:ll,u:uu})
 TT2=uu*uu*(1+rr*rr*(KK-1+uu)/(1-uu))
 QQ2=uu+ll*uu*uu*zz+aa1*uu*uu*zz*zz/(1-uu)
 vv=cc*TT2/(2*QQ2-(ll+1)*TT2)
 aa=(uu-vv*(1-(ll+1)*uu+ll*bb)/cc)/bb # ORIGINAL calibration
 ep=(uu-ll*bb)/uu
 value=((1+vv)*ep*ep-2*(1-aa)*ep)/ll
 hh=cc*uu/(1-uu);dd=1-hh
 beta=lambda s:hh/(ll**s-dd)
 for s in range(2,last+1):
  rs=beta(s+1)/beta(s);rm=beta(s)/beta(s-1)
  fs=tt**(s-1)*(s-(s-1)*tt)
  AA=beta(s)*fs/uu
  BB=(1+vv)*(1-ll*rs)**2/ll+2*(1-aa)*(rs-rm)
  MM=aa*(1-rs)+vv/cc*(ll+1-ll*rs-beta(s-1)/(beta(s)*fs))
  value+=s*ll**(s-1)*AA*AA*(BB+2*(1/ll-rm)*MM)
 return S.cancel(value),S.cancel(vv),S.cancel(aa)

# These checks start from ORIGINAL v=cT2/[2Q2-(lambda+1)T2] and
# ORIGINAL a=[u-vA0/c]/b; they do not reuse normalized AN identities.
for point in [(S.Rational(231,200),S.Rational(22869,595610),S.Rational(9,10)),
              (S.Rational(6,5),S.Rational(1,200),S.Rational(3,4))]:
 ll,uu,tt=point;vals={l:ll,u:uu,T:tt}
 value,vv,aa=original_value(*point)
 ev=lambda poly:poly.eval(vals)
 assert S.cancel(vv-uu*ev(VN)/ev(VD))==0
 assert S.cancel(aa-ev(AN)/(tt*(2-tt)*ev(VD)))==0
 assert S.cancel(value-ev(P)/(ll*tt*(2-tt)*ev(VD)*ev(D)))==0
 print('Original v,a,whole S'+str(last)+' clearing checked at exact point:',point,flush=True)

print('New numerator degree',P.degree_list(),'terms',len(P.terms()),flush=True)
du=P.degree(u);H=L**2+L-ONE
transformed=pp(0)
for (i,j,k),v in P.terms():
 transformed+=v*L**(i+j)*U**j*X**k*rho**j*H**(du-j)
raw=dict(transformed.terms())
min_l=min(idx[0] for idx in raw)
raw={(i-min_l,j,k):v for (i,j,k),v in raw.items()}
deg=tuple(max(idx[a] for idx in raw) for a in range(3))
print('Physical transform degree',deg,'min lambda power',min_l,flush=True)
cf={}
for (i,j,k),v in raw.items():
 vv=F(int(v.p),int(v.q))
 for a in range(i+1):
  idx=(a,j,k)
  cf[idx]=cf.get(idx,F(0))+vv*comb(i,a)*F(23,20)**(i-a)*F(7,20)**a
for axis in range(3):
 out={}
 for idx,v in cf.items():
  for a in range(idx[axis],deg[axis]+1):
   ii=list(idx);ii[axis]=a;ii=tuple(ii)
   out[ii]=out.get(ii,F(0))+v*F(comb(a,idx[axis]),comb(deg[axis],idx[axis]))
 cf=out
full=[cf.get(idx,F(0)) for idx in product(*(range(n+1) for n in deg))]
print('CORRECTED S'+str(last)+' whole physical box:',
      sum(v<0 for v in full),'negative;',sum(v>0 for v in full),'positive;',len(full),'total',flush=True)
negative=[idx for idx,v in cf.items() if v<0]
if negative:
 print('Negative support ranges:',[(min(idx[a] for idx in negative),max(idx[a] for idx in negative)) for a in range(3)],flush=True)
 # NEW exact full-domain test: split only T at1/2. No sample scan.
 axis=2;n=deg[axis];left={};right={}
 for i,j in product(range(deg[0]+1),range(deg[1]+1)):
  line=[cf.get((i,j,k),F(0)) for k in range(n+1)]
  ll=[line[0]];rr=[line[-1]]
  while len(line)>1:
   line=[(line[k]+line[k+1])/2 for k in range(len(line)-1)]
   ll.append(line[0]);rr.append(line[-1])
  rr.reverse()
  for k in range(n+1):left[i,j,k]=ll[k];right[i,j,k]=rr[k]
 for name,leaf in [('T<=1/2',left),('T>=1/2',right)]:
  print('NEW S'+str(last),name,'negative',sum(v<0 for v in leaf.values()),
        'positive',sum(v>0 for v in leaf.values()),'total',len(leaf),flush=True)
print('This tests a NEW payment; accepted speed threshold stays707/500.',flush=True)
