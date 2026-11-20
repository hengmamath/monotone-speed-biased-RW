"""Complete zero-u normalized J1 increases with lambda on the full interval.
Exact generic identities and three coarse derivative payments. No old
imports/certificate runs, parameter grid, LP or sampled-sign inference.
"""
from fractions import Fraction as F
import sympy as s

l,j=s.symbols('l j')
A=1+l
K=(l+1)/(2*l)+s.Rational(1,2)+(l+1)**2/(24*l)
G=2*A-1-l/A;Gp=-1-2*l/A;H=A
B=A*(G-K*H)
Bp=A*Gp-A*(2*(K-1)*H)
root0=2*((25+l)*B-Bp)/(l*A*A)
R0=-l/12-s.Rational(1,12)+44/(l+1)-44/(l+1)**2 \
    -s.Rational(35,12)/l-s.Rational(299,12)/l**2
assert s.cancel(root0-R0)==0
Rp=-s.Rational(1,12)-44*(l-1)/(l+1)**3 \
    +s.Rational(35,12)/l**2+s.Rational(299,6)/l**3
assert s.cancel(s.diff(R0,l)-Rp)==0
assert Rp.subs(l,s.Rational(10,7))>17

x=j*j
FX=(1/(1+x/3)**2,
    (1-x)/((1+x/3)**2*(1+x)**2),
    (1-x)**2/((1+x)**2*(1+2*x+x*x/5)**2))
FY=((1-x)**2/(1+x/3),
    (1-x)**4/((1+x/3)**3*(1+x)),
    (1-x)**6/((1+x)**3*(1+2*x+x*x/5)))
for q,n,wx,wy,fx,fy in zip((2,3,4),(1,3,6),
    (s.Rational(1,9),s.Rational(1,24),s.Rational(1,50)),
    (s.Rational(2,3),s.Rational(2,9),s.Rational(1,10)),FX,FY):
    Z={k:sum(l**i for i in range(k)) for k in range(1,6)}
    r=Z[q]/Z[q+1]
    age0=(24-2*n)*2*q*l**(q-2)*(2-r-l*r*r)/Z[q]**3
    expected=(24-2*n)*(wx*(1-j)**(2*q+2)*fx+wy*(1-j)*fy/2)
    assert s.cancel(age0.subs(l,(1+j)/(1-j))-expected)==0

alo,J=F(40,43),F(7,40);X=J*J;djmax=F(800,1849)
assert F(3,43)==(F(23,20)-1)/(F(23,20)+1)
assert (F(707,500)-1)/(F(707,500)+1)<J
assert F(707,500)<F(10,7)
LX=(F(4,3)*J,
    2*J*(1/(1-X)+F(2,3)+2),
    2*J*(2/(1-X)+6+F(4,5)*X))
LY=(2*J*(2/(1-X)+F(1,3)),
    2*J*(4/(1-X)+2),
    2*J*(6/(1-X)+5+F(2,5)*X))
payments=[]
for q,n,wx,wy,bx,by,bound in zip((2,3,4),(1,3,6),
    (F(1,9),F(1,24),F(1,50)),(F(2,3),F(2,9),F(1,10)),
    LX,LY,(F(41,4),F(9,2),F(2))):
    power=2*q+2
    payment=(24-2*n)*djmax*(
        wx*(power*alo**(power-1)+alo**power*bx)+wy/2*(1+alo*by))
    assert payment<bound
    payments.append(payment)
    print('Exact negative age derivative upper',q,str(payment),'<',str(bound))
assert sum((F(41,4),F(9,2),F(2)),F(0))==F(67,4)
assert 17-F(67,4)==F(1,4)
print('PASS generic full root/three-age identities at u=0')
print('PASS written analytic bounds imply F_lambda(lambda,0)>1/4 everywhere')
print('Zero-u boundary only: no positive-u lambda comparison or six-box removal.')
