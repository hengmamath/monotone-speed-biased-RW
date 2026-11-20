"""Exact local identities and one all-index absorption certificate.

Complete local proof in root_canonical_profile_payment.md; independent
audit pending. The complete root SIZE certificate is a separate file;
the original theorem below2/sqrt3 remains OPEN.
"""
import sympy as S
from math import comb
l,u,t,L=S.symbols('l u t L')
c=l-1
total=positive=0
for s in range(2,8):
 N=l**s*(1-u)-1+l*u
 D=l**(s+1)*(1-u)-1+l*u
 P=s*(l+1)*N*(D-l*N)+(1-l*l*u)*((2*s-1)*D**2-s*(l+1)*N*D)
 raw=S.Poly(S.expand(l**4*P.subs(u,t/l**2)),l,t)
 H=raw.exquo(S.Poly(l**2*c**2,l,t))
 assert H.degree_list()==(2*s+2,3)
 shifted=S.Poly(H.as_expr().subs(l,L+S.Rational(23,20)),L,t)
 cf={}
 for (i,j),v in shifted.terms():
  for a in range(j,4):
   cf[i,a]=cf.get((i,a),S.Rational(0))+v*S.Rational(comb(a,j),comb(3,j))
 full=[cf.get((i,j),S.Rational(0)) for i in range(H.degree(l)+1) for j in range(4)]
 assert all(bool(v>=0) for v in full)
 assert all(bool(cf.get((0,j),0)>0) for j in range(4))
 total+=len(full);positive+=sum(bool(v>0) for v in full)
 print('s',s,'degree',H.degree_list(),'all nonnegative;',sum(bool(v>0) for v in full),'positive')
assert (total,positive)==(288,261)
assert S.Rational(15)*S.Rational(23,20)/(8*(S.Rational(23,20)+1))==S.Rational(345,344)

a,v,A,x,r,rp,th,dd,cs=S.symbols('a v A x r rp th dd cs')
ep=x*(1-l*r)+l*dd
gamma=x*(r-rp)-dd+th
LC=1/l-rp
Bs=(1+v)*(1-l*r)**2/l+2*(1-a)*(r-rp)
absorption=x*x*Bs+2*x*dd*((1+v)*(1-l*r)+(1-a)*(cs-1))+(1+v)*l*dd*dd+2*(1-a)*x*(th-cs*dd)
assert S.expand((1+v)*ep*ep/l+2*(1-a)*x*gamma-absorption)==0
assert S.expand(gamma+ep/l-(x*LC+th))==0

h=c*u/(1-u);b=S.symbols('b');A0=1-(l+1)*u+l*b
assert S.cancel((u-h*A0/c)/b-l*h/c*(u/b-1))==0
k0=(l*l+13*l+6-l*(3*l+7)*u+2*l*l*u*u)/(12*l)
pol=S.Poly(S.cancel(l**3*12*l*(2-(1+l*u)*k0)).subs(u,t/l**2).expand(),t)
expected=[-l**3*(l*l-11*l+6),
 -l*l*(3*l**3-32*l*l+28*l-1)/3,
 -l*(l-1)*(3*l**3-28*l*l+10*l+5)/3,
 -(l-1)**2*(l**3-8*l*l-l+2)]
for j in range(4):
 bb=sum(pol.nth(i)*S.Rational(comb(j,i),comb(3,i)) for i in range(j+1))
 assert S.expand(bb-expected[j])==0
for pp in [3*l**3-32*l*l+28*l-1,3*l**3-28*l*l+10*l+5,l**3-8*l*l-l+2]:
 assert pp.subs(l,S.Rational(23,20))<0
 # The respective derivative's positive term is <=9*(3/2)^2;
 # its negative linear term uses l>=23/20.
 dp=S.Poly(S.diff(pp,l),l)
 assert dp.nth(2)*S.Rational(3,2)**2+dp.nth(1)*S.Rational(23,20)+dp.nth(0)<0
assert -S.Rational(3,2)**2+11*S.Rational(23,20)-6>0
print('All-index absorption, 3 rational identities and 4 cap coefficients PASS locally; root certificate is separate.')
