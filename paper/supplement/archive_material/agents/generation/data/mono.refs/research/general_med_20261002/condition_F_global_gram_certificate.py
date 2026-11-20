"""Full exact sign certificate for joint SECOND-prefix Gram payment.

Complete independent audit PASSED the SAME sole reviewer. This is not a certificate
for overall speed monotonicity or payment of the six remaining low blocks.
"""
import sympy as S
from fractions import Fraction as F
from math import comb
from itertools import product
from exact_qsqrt3 import Q3
l,u,s=S.symbols('l u s')
c=l-1;g=c/(l+1)
ellL=2*(g+g**3/3+g**5/5)
ellU=ellL+2*g**7/(7*(1-g*g))
K=c/(l*ellL)+(1-u)/2+ellU/(12*c)*(l+1-2*l*u)*(1-u)
kn,kd=S.fraction(S.cancel(K))
expected_den=2520*l*(l+1)**5*(23*l**4+48*l**3+98*l**2+48*l+23)
assert S.expand(kd-expected_den)==0
pp=lambda e:S.Poly(e,l,u,s,domain=S.QQ)
L,U,V=pp(l),pp(u),pp(s);ONE=pp(1)
KN,KD=pp(kn),pp(kd)
A1=L+ONE-L*U
A2=L**2+L+ONE-L*(L+ONE)*U
A3=L**3+L**2+L+ONE-L*(L**2+L+ONE)*U
ZN=U*A1+V*(ONE-U)*(ONE-L*U)
RN=(ONE-U)*KD+(KN-(ONE-U)*KD)*ZN**2
DN=A1*(ONE-U)*KD+2*L*U*ZN*(ONE-U)*KD+2*U*ZN**2*KD-A1*(KN-(ONE-U)*KD)*ZN**2
TN=DN-U*RN*(A1-ZN)
N=A3*ZN*A1*TN**2-(2*U*A3+A2)*ZN*A1*TN*DN+A2*U*A1**2*TN*DN+A3*U*ZN**2*DN**2
# N/(A3*A1^2*DN^2)=z*Gram(tcrit2), positive denominator.
removed=0
while N.eval(u,1).is_zero:
 N=N.exquo(pp(1-u));removed+=1
assert removed==2
du=N.degree(u)
# u=t/l^2; multiply by l^(2du), a positive factor.
raw={(i+2*(du-j),j,k):v for (i,j,k),v in N.terms()}
minl=min(idx[0] for idx in raw)
assert minl==11
raw={(i-minl,j,k):v for (i,j,k),v in raw.items()}
degree=tuple(max(idx[a] for idx in raw) for a in range(3))
assert degree==(57,20,7)
# Affine l on the EXACT interval [2/sqrt3,707/500].
lo=Q3(0,F(2,3));delta=Q3(F(707,500))-lo
assert lo*lo==Q3(F(4,3)) and delta>0
lp=[lo**i for i in range(degree[0]+1)]
dp=[delta**i for i in range(degree[0]+1)]
coeff={}
for (i,j,k),v in raw.items():
 vv=F(int(v.p),int(v.q))
 for a in range(i+1):
  idx=(a,j,k)
  coeff[idx]=coeff.get(idx,Q3(0))+vv*comb(i,a)*lp[i-a]*dp[a]
# Convert every variable from powers to Bernstein coefficients on [0,1].
for axis in range(3):
 out={}
 for idx,v in coeff.items():
  i=idx[axis]
  for a in range(i,degree[axis]+1):
   ii=list(idx);ii[axis]=a;ii=tuple(ii)
   out[ii]=out.get(ii,Q3(0))+v*F(comb(a,i),comb(degree[axis],i))
 coeff=out
indices=list(product(*(range(n+1) for n in degree)))
coeff={idx:coeff.get(idx,Q3(0)) for idx in indices}
neg=[idx for idx,v in coeff.items() if v<0]
assert len(neg)==3
print('Root degree:',degree,'negative coefficient indices:',neg,flush=True)
# ONE de Casteljau split of t=l^2*u at1/2: certify both whole boxes.
left={};right={};n=degree[1]
for i,k in product(range(degree[0]+1),range(degree[2]+1)):
 line=[coeff[i,j,k] for j in range(n+1)]
 ll=[line[0]];rr=[line[-1]]
 while len(line)>1:
  line=[(line[j]+line[j+1])/2 for j in range(len(line)-1)]
  ll.append(line[0]);rr.append(line[-1])
 rr.reverse()
 for j in range(n+1):left[i,j,k]=ll[j];right[i,j,k]=rr[j]
for name,leaf in [('t<=1/2',left),('t>=1/2',right)]:
 assert len(leaf)==9744 and all(v>=0 for v in leaf.values()),name
 print(name,': all9744 exact coefficients NONNEGATIVE;',
       sum(v>0 for v in leaf.values()),'strictly positive',flush=True)
print('FULL GLOBAL SECOND-PREFIX GRAM CERTIFICATE PASSED locally.')
