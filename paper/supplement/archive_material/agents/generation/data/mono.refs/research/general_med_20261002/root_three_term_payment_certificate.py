"""CORRECTED assigned calibration; original38998 certificate INVALID.

The sum includes the root and indices2,3. The assigned pair uses the
audited second-prefix K bound. The total speed theorem remains OPEN.
"""
import sympy as S
from fractions import Fraction as F
from math import comb
from itertools import product
import sys
mode=sys.argv[1] if len(sys.argv)>1 else 'physical'
physical=mode=='physical'
coupled=physical or (len(sys.argv)>1 and sys.argv[1]=='canonical')
u_max=F(1) if coupled else (F(sys.argv[1]) if len(sys.argv)>1 else F(1,100))
l,u,T=S.symbols('l u T')
c=l-1;g=c/(l+1)
ellL=2*(g+g**3/3+g**5/5)
ellU=ellL+2*g**7/(7*(1-g*g))
K=S.cancel(c/(l*ellL)+(1-u)/2+ellU*(l+1-2*l*u)*(1-u)/(12*c))
kn,kd=S.fraction(K)
assert S.expand(kd-2520*l*(l+1)**5*(23*l**4+48*l**3+98*l**2+48*l+23))==0
pp=lambda e:S.Poly(e,l,u,T,domain=S.QQ)
L,U,X=pp(l),pp(u),pp(T);ONE=pp(1);C=L-ONE
KN,KD=pp(kn),pp(kd)
rho=X*(2-X);A1=L+ONE-L*U
Rnum=(ONE-U)*KD+rho**2*(KN-(ONE-U)*KD)
Qnum=A1*(ONE-U)*KD+L*U*rho*(ONE-U)*KD+U*rho**2*KD
VD=2*Qnum-(L+ONE)*U*A1*Rnum
VN=C*A1*Rnum
A0num=(ONE-(L+ONE)*U)*A1+L*U*rho
AN=A1*(VD-Rnum*A0num)
# V=VN/VD, a=AN/(rho*VD). All these raw denominators are positive
# on the intended actual domain; no symbolic global GCD is necessary.
Ns={s:L**s*(ONE-U)-ONE+L*U for s in range(1,5)}
D=A1**2*C*Ns[2]**3*Ns[3]**3*Ns[4]**2
epN=A1-L*rho
root=rho*(VD+U*VN)*epN**2-2*(rho*VD-AN)*epN*A1
P=root*D.exquo(A1**2)
for s in (2,3):
 N,Nm,Np=Ns[s],Ns[s-1],Ns[s+1]
 fs=X**(s-1)*(s-(s-1)*X)
 ds=N**3*Np**2*Nm
 tail=C**2*rho*(VD+U*VN)*fs**2*(Np-L*N)**2*N*Nm
 tail+=2*L*C**2*(rho*VD-AN)*(N**2-Nm*Np)*fs**2*Np*Nm
 tail+=2*C**2*(N-L*Nm)*AN*(Np-N)*fs**2*Np*Nm
 tail+=2*C*(N-L*Nm)*rho*U*VN*fs*((L+ONE)*Np*Nm*fs-L*N*Nm*fs-N*Np)*Np
 P+=s*L**(s-1)*tail*D.exquo(ds)
# P/[lambda*rho*VD*D] is EXACTLY the normalized root+2+3 floor.
removed_c=removed_l=0
while P.eval(l,1).is_zero:
 P=P.exquo(C);removed_c+=1
while P.eval(l,0).is_zero:
 P=P.exquo(L);removed_l+=1
p=P
print('Cleared exact full root+2+3; removed positive c,lambda powers:',removed_c,removed_l,flush=True)
print('Numerator degree',p.degree_list(),'terms',len(p.terms()),flush=True)
raw=dict(p.terms())
if physical:
 du=p.degree(u);H=L**2+L-ONE
 transformed=pp(0)
 for (i,j,k),v in raw.items():
  transformed+=v*L**(i+j)*U**j*X**k*rho**j*H**(du-j)
 raw=dict(transformed.terms())
 min_l=min(idx[0] for idx in raw)
 raw={(i-min_l,j,k):v for (i,j,k),v in raw.items()}
 print('u=lambda*rho2*tau/(lambda^2+lambda-1); cleared H^',du,'and removed lambda^',min_l,flush=True)
elif coupled:
 du=p.degree(u)
 raw={(i+2*(du-j),j,k):v for (i,j,k),v in raw.items()}
 min_l=min(idx[0] for idx in raw)
 raw={(i-min_l,j,k):v for (i,j,k),v in raw.items()}
 print('u=tau/lambda^2; cleared positive lambda power',2*du-min_l,flush=True)
deg=tuple(max(idx[axis] for idx in raw) for axis in range(3));cf={}
for (i,j,k),v in raw.items():
 vv=F(int(v.p),int(v.q))
 for a in range(i+1):
  idx=(a,j,k)
  cf[idx]=cf.get(idx,F(0))+vv*comb(i,a)*F(23,20)**(i-a)*F(7,20)**a*u_max**j
for axis in range(3):
 out={}
 for idx,v in cf.items():
  for a in range(idx[axis],deg[axis]+1):
   ii=list(idx);ii[axis]=a;ii=tuple(ii)
   out[ii]=out.get(ii,F(0))+v*F(comb(a,idx[axis]),comb(deg[axis],idx[axis]))
 cf=out
full=[cf.get(idx,F(0)) for idx in product(*(range(n+1) for n in deg))]
print('Certificate degree',deg,flush=True)
print('Whole box lambda23/20..3/2,'+('physical relaxed tau0..1' if physical else ('lambda^2*u0..1' if coupled else 'u0..'+str(u_max)))+',T0..1:',
      sum(v<0 for v in full),'negative;',sum(v>0 for v in full),'positive;',len(full),'total',flush=True)
if physical:
 print('CORRECTED whole-box sign:',all(v>=0 for v in full),flush=True)
if coupled and any(v<0 for v in full):
 print('Negative indices:',[idx for idx,v in cf.items() if v<0],flush=True)
 left={};right={};n=deg[1]
 for i,k in product(range(deg[0]+1),range(deg[2]+1)):
  line=[cf.get((i,j,k),F(0)) for j in range(n+1)]
  ll=[line[0]];rr=[line[-1]]
  while len(line)>1:
   line=[(line[j]+line[j+1])/2 for j in range(len(line)-1)]
   ll.append(line[0]);rr.append(line[-1])
  rr.reverse()
  for j in range(n+1):left[i,j,k]=ll[j];right[i,j,k]=rr[j]
 for name,leaf in [('tau<=1/2',left),('tau>=1/2',right)]:
  print(name,'negative',sum(v<0 for v in leaf.values()),'positive',sum(v>0 for v in leaf.values()),flush=True)
