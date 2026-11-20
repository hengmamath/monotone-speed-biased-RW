import export_exact as EX
"""ALL-N Lambert coefficients, normalized hard gap and complete Jminus cost."""
import sympy as S
from fractions import Fraction as F
l,x,N,i,j,z,k,R=S.symbols('l x N i j z k R')
c=l-1;A=c*N/(x-1);B=c*N*x/(x-1)**2-l/(x-1)
P=(l+1)*A-2*l/x;C=(l+1)*B-2*l/(c*N*x)*(1-A)
cnt=0
def eq(name,a,b):
 global cnt
 assert S.cancel(a-b)==0,name
 cnt+=1
 print('PASS',name)
GG=lambda jj:N*x/(x-1)*(c*N*(jj+1/(x-1))-l)
HH=lambda jj:c*N*((l+1)*N*x*(jj*x-jj+1)/(x-1)**2-l*x/(x-1))-2*l/c-2*l*jj*N
eq('full static coefficient',GG(i+1)/x,N*(A*i+B))
eq('full affine coefficient',HH(i+1)/x,N*(P*i+C))
n,t=S.symbols('n t',integer=True,positive=True)
aa=S.symbols('aa')
ql=lambda v:(v+1)*(v+2)*(n-1-v/S.Integer(3))
qu=lambda v:n*n*(2*(2*n-2-v)+1)-n*(3*(2*n-2-v)+1)-(2*n-2-v)*(2*n-3-v)*(n+(2*n-1-v)/S.Integer(3))
r=S.symbols('r')
eq('positive upper coefficient decomposition',qu(2*n-2-r),
 (n-r-1)*((2*r+1)*n+r*(r+1))+2*r*(r+1)*(r+2)/3)
eq('lower second difference',ql(j)-2*ql(j-1)+ql(j-2),2*(n-1-j))
eq('upper second difference',qu(j)-2*qu(j-1)+qu(j-2),2*(j-3*n+1))
eq('boundary n-1',qu(n-1)-2*ql(n-2)+ql(n-3),0)
eq('boundary n',qu(n)-2*qu(n-1)+ql(n-2),2-3*n)
eq('boundary top-1',-2*qu(2*n-2)+qu(2*n-3),n*(n-2))
eq('boundary top',qu(2*n-2),n*(n-1))
qsum=S.summation(ql(j),(j,0,n-2))+S.summation(qu(j),(j,n-1,2*n-2))
eq('ALL-N positive coefficient sum',qsum,n*n*(n-1)*(5*n+2)/6)
for nn in (1,2):
 Q=sum(l**a for a in range(nn))
 poly=(l+1)*nn**2*l**(2*nn-1)-c*nn*l**nn*Q-(2+2*nn*c)*Q*Q
 qs=0 if nn==1 else sum(ql(v).subs(n,nn)*l**v for v in range(nn-1))+sum(qu(v).subs(n,nn)*l**v for v in range(nn-1,2*nn-1))
 eq('smallN C polynomial '+str(nn),poly,c*c*qs)
# ALL-N slope upper polynomial: coefficients k(k+1) below n,
# n(2n-1-k) above it, degree2n-2. n1/2 handled explicitly.
rl=lambda v:v*(v+1)
ru=lambda v:n*(2*n-1-v)
eq('slope upper lower second difference',rl(j)-2*rl(j-1)+rl(j-2),2)
eq('slope upper interior second difference',ru(j)-2*ru(j-1)+ru(j-2),0)
eq('slope upper boundary n',ru(n)-2*rl(n-1)+rl(n-2),2-2*n)
eq('slope upper boundary n+1',ru(n+1)-2*ru(n)+rl(n-1),-n)
eq('slope upper top-1',-2*ru(2*n-2)+ru(2*n-3),0)
eq('slope upper top',ru(2*n-2),n)
for nn in (1,2):
 Q=sum(l**a for a in range(nn))
 poly=nn*l**(2*nn)-nn*l**(nn+1)-2*nn*l**nn+2*l*Q
 qs=0 if nn==1 else sum(rl(v)*l**v for v in range(nn))+sum(ru(v).subs(n,nn)*l**v for v in range(nn,2*nn-1))
 eq('smallN slope polynomial '+str(nn),poly,c*c*qs)
# B_N exact positive expression and derivative-at-one for its sharp bound.
eq('sharp B derivative-at-one',n*n*(n-1)**2-2*n*S.summation(j*j,(j,1,n-1)),
 n*n*(n-1)*(n-2)/3)
Li=c*z/(l*(1-z));Ln=c*z/(l*(l-z));ri=(1-z)/(l-z)
lower=i/l*((1-z)/(1-z/l))**2*(1+R*c/l*(1+z/l)/(1-z/l))
eq('complete full-mixture lower',lower,i*l*ri*ri*(1+R*(c/l+2*Ln)))
upper=i/l*(1+R*c*(1+z)/(1-z))+z/(2*l)+R*c/l*2*z/(1-z)
eq('complete full-mixture upper',upper,i*(1+c*R)/l+2*R*(i+1)*Li+z/(2*l))
T,Tp0,Qp,u,M1,ML=S.symbols('T Tp0 Qp u M1 ML')
F0=c*M1/l-T+2*ML
Es=-c*M1/l+u*u+(Qp-u)/l
eq('whole affine cap cancellation',c*F0+4*ML-2*Es,(l+1)*F0+2*T-2*u*u-2*(Qp-u)/l)
Z=2*Qp-(l+1)*T
Fp=F0+T/Z*((l+1)*F0+2*T-2*Qp/l)
eq('whole cap quotient source',Fp,2*Qp/Z*(F0+T*T/Qp-T/l))
q,h,th=S.symbols('q h th',positive=True);ll=1+h/q;dd=1-h;uu=q/(1+q);RR=th*q
bb=uu/(ll+1-ll*uu);ap=(uu-RR*(1-(ll+1)*uu+ll*bb))/bb
gap=th*dd*(ll+1)-ll
eq('complete hard calibration normal form',ap,1-gap/(1+q))
EH=gap/((1+q)*(1+ll*th*q))
eq('complete Ehard normalization',(1-ap)/(1+ll*RR),EH)
eq('normalized hard-gap maximum',EH.subs(th,1)*q*q,
 (1-(ll+1)*h)*uu*uu/(1+(ll-1)*uu))
eq('hard-gap monotonicity',S.diff(EH,th),
 (dd*(ll+1)+ll*ll*q)/((1+q)*(1+ll*th*q)**2))
# Full J coefficient coercivity, no sampling.
a=S.symbols('a');rr=1/(l*(1+a));rprev=(1-l*a)/l
BK=(l-1)*rr*rr+2*l*rr**3*a+l*rr-1/rprev
NK=(l*a+l-1)*(2*a*a*l*l+3*a*l*l+2*a*l+a+l*l-1)/(l*l*(1+a)**3*(1-l*a))
eq('exact negative J factor',BK,-NK)
am=dd/(ll*(q+2));rm=1/(ll+dd/(q+2))
Nm=(ll*am+ll-1)*(2*ll*ll*am*am+(3*ll*ll+2*ll+1)*am+ll*ll-1)/(ll*ll*(1-ll*am))
AJlo=ll*rm*rm+4*ll*ll*uu*rm/(ll+1)-q*Nm
num,den=S.fraction(S.factor(AJlo-(3-12/q)))
expect=q*(h+q)**3*(h+2*q)*(q+1)*(q+2)**2*(h+q+1)*(2*h+q*q+3*q)**2
eq('global J coefficient positive denominator',den,expect)
pol=S.Poly(num,h,q)
assert all(v>=0 for v in pol.coeffs())
assert pol.coeff_monomial(q**11)==66
EX.polynomial(pol,metadata={"check":"A_J lower numerator","domain":"q,h>0; positive denominator displayed in manuscript"})
cnt+=1;print('PASS ALL',len(pol.terms()),'nonnegative numerator coefficients; strict global J coercivity')
tt,ff=S.symbols('tt ff')
nn=tt-ff
triangle=(nn+ff)*nn*(nn+1)*(2*nn+1)/6-nn*nn*(nn+1)*(nn+1)/4
eq('ALL-age fractional Faulhaber',triangle,tt**4/12+tt*tt*(-ff*ff/2+ff/2-S.Rational(1,12))+
 tt*(2*ff**3/3-ff*ff+ff/3)-ff*ff*(1-ff)**2/4)
AA=F(11,4)
const=F(51,50)**4/(12*AA**3)+F(51,50)**2/(12*AA*2500)
assert const<F(1,200)
cnt+=1;print('PASS complete q>=50 Jminus cost; exact constant',const,'<1/200')
print(cnt,'NEW exact algebra/certificates PASS; whole head SIZE still OPEN.')
# Optional whole Hpi upper: global Bernoulli remainder, not asymptotic use.
nn,delta=S.symbols('nn delta');z=S.symbols('z')
eq('ALL exponential upper coefficients',1-nn/2+nn*(nn-1)/12,(nn-3)*(nn-4)/12)
f=1/(1-z)
moment=lambda power:S.diff(f,z) if power==1 else None
v=f
for power,answer in [(1,1),(2,(1+z)/(1-z)),(3,(1+4*z+z*z)/(1-z)**2),(4,(1+11*z+11*z*z+z**3)/(1-z)**3)]:
 v=z*S.diff(v,z)
 eq('ALL mixture moment '+str(power-1),(1-z)**2*v/z,answer)
eq('ALL reciprocal-N mixture moment',(1-z)**2*f,1-z)
EN=S.symbols('EN')
eq('ALL affine constant sharper expectation',c*(5*EN/6-S.Rational(1,2)-(1-z)/3),
 c*(5*(EN-1)/6+z/3))
Pupper=(l+1)*(c/delta-c*nn/2+c*delta*nn*nn/12)-2*l*(1-nn*delta+nn*nn*delta**2/2-nn**3*delta**3/6)
eq('complete cubic P upper',Pupper,(l+1)*c/delta-2*l+
 (2*l*delta-(l+1)*c/2)*nn+((l+1)*c*delta/12-l*delta**2)*nn*nn+l*delta**3*nn**3/3)
print(cnt,'total NEW exact checks PASS; 231 whole-H bound is a sufficient upper only.')
