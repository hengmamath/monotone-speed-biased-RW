"""238--243 complete local exact certificates; independent audit pending."""
import sympy as S
from fractions import Fraction as F
from math import comb
from collections import defaultdict
x,h,t,w,g,M,a=S.symbols('x h t w g M a')
ell=1+h*x;c=h*x;b=x*w;i=t/x;R=1/x-g;d=1-h
alpha=(ell*ell+g*d*(ell+1)*x*x)/(1+x);z=w/(h+w)
r=1/(ell+b);rp=(1-b)/ell;k=2/(ell+1)
A=1-b+(c*b+b*b)/2
P=c+2*b-4*c*b-5*b*b+S.Rational(9,2)*c*c*b+S.Rational(25,2)*c*b*b+8*b**3
C=S.Rational(5,3)*b+c*z/3
U=(i*(A+R*P)+z/2+R*C)/ell
tau=1-(alpha+ell*R)*r+(ell+1)*R-R/rp
B=2*i*(alpha+c*R)/ell+2*i*R*r*b/ell+2*(i+1)*R*r*r*b+k*(2*i-1)*tau
shape=2*h*t+4*(t-S.Rational(1,3))*w-(2*h+3)*z/3
num,den=S.fraction(S.factor(S.cancel((B-2*U-shape)/x+M*(1+h*t))))
assert S.cancel(den+3*(h+w)*(x+1)*(h*x+1)*(h*x+2)*(1-w*x)*(h*x+w*x+1)**2)==0
pp=S.Poly(-num,x,h,t,w,g,M);D=pp.degree(w);v=S.symbols('v')
assert D==7 and pp.degree(g)==1 and pp.degree(M)==1
ee=S.expand(sum(co*x**mo[0]*h**mo[1]*t**mo[2]*(1-h)**mo[3]*v**mo[3]*(1+t)**(D-mo[3])*g**mo[4]*M**mo[5] for mo,co in pp.terms()))
def bern(poly):
    degrees=(6,8,8,7)
    assert poly.degree_list()==degrees
    coefs={mo:F(co)/10**mo[0]/2**mo[1] for mo,co in poly.terms()}
    for axis in (0,1,3):
        groups=defaultdict(dict)
        for mo,co in coefs.items(): groups[mo[:axis]+mo[axis+1:]][mo[axis]]=co
        out={}
        for key,aa in groups.items():
            for j in range(degrees[axis]+1):
                cc=sum((co*F(comb(j,k),comb(degrees[axis],k)) for k,co in aa.items() if k<=j),F())
                if cc: out[key[:axis]+(j,)+key[axis:]]=cc
        coefs=out
    return coefs
for endpoint in (0,1):
    co=bern(S.Poly(ee.subs({g:endpoint,M:S.Rational(28,5)}),x,h,t,v))
    assert len(co)==4319 and all(a>0 for a in co.values()) and min(co.values())==F(69,280)
    print('239 ALL-age q>=10 g',endpoint,'4319 coefficients/min69/280 PASS')
f=d*(2*h+1)/6;ss=a-x/2+x*x*(2-h)/(12*a);J=24-36*h+14*h*h-h**3
source=2*(ss*ss-(ell+1)*ss+a*a-x*x*(2-h)/12)-(f-S.Rational(2,5)*x)*x*ell*(2*ell-(ell+1)*(ss-x**4*J/(720*a**3)))
sn,sd=S.fraction(S.factor(source.subs(a,1+h*x/2-h*h*x*x/12)))
assert S.expand(sd-1800*(h*h*x*x-6*h*x-12)**3)==0
poly=S.Poly(S.cancel(-sn/x**3),h,x)
assert poly.coeff_monomial(1)==380160 and len(poly.terms())==60
negative=sum((-F(co)/2**mo[0]/10**mo[1] for mo,co in poly.terms() if co<0),F())
assert negative==F(65345524702337817,204800000000) and negative<320000
print('238 full source negative monomials',negative,'<320000; constant380160 PASS')
n=S.symbols('n')
assert S.expand(720-360*n+60*n*(n-1)-n*(n-1)*(n-2)*(n-3)+(n-6)*(n-5)*(n-3)*(n+8))==0
y=S.symbols('y');env=(9*t-7)/(3*(1+t))
L=2*h*t+4*(t-S.Rational(1,3))*d*(1-h*t/3)/(1+t-h*t/3+h*t*t/6)-(2*h+3)*d/(3*(1+h*t))
Q=t**3*(15*y*y-27*y+18)+t*t*(81*y*y+13*y+108)+t*(42*y*y-48*y+18)+120+152*y-40*y*y+(48*y-16*y*y)/t
assert S.cancel(L-env-S.Rational(3,4)*h*t-h*Q.subs(y,h*t)/(12*(t+1)*(h*t+1)*(h*t*t-2*h*t+6*t+6)))==0
print('240 ALL-age strengthened shape identity PASS')
eta=S.Rational(4,15);AA=7+3*eta;BB=9-3*eta
G=t*(AA-BB*t)/(3*(1+t)**3)
assert AA==S.Rational(39,5) and BB==S.Rational(41,5)
assert S.cancel(S.diff(G,t)-(AA-32*t+BB*t*t)/(3*(1+t)**4))==0
assert S.cancel(S.diff(G,t,2)-(-32-4*AA+(96+2*BB)*t-2*BB*t*t)/(3*(1+t)**5))==0
assert 52**2-4*17*40==-16
I=S.Rational(175,96)+S.Rational(9,16)*eta-S.Rational(3,32)*eta*eta-(3-eta)*S.log(16/BB)
assert S.simplify(S.integrate(G,(t,0,AA/BB))-I)==0
s=F(39,121);loglo=2*(s+s**3/3+s**5/5+s**7/7)
Iup=F(175,96)+F(9,16)*F(4,15)-F(3,32)*F(4,15)**2-(3-F(4,15))*loglo
q0=21;omega=F(17,7)
Jup=(F(22,21)**4/(12*omega**3))+(F(22,21)**2/(12*omega*q0**2))
assert Jup==F(2904605,409493637)
margin=F(1,6)-F(2,5*q0)-F(1,2*q0**2)-Iup-Jup
assert margin==F(28155382207511429143103,124404112403316879470013600) and margin>F(1,5000)
print('243 ENTIRE q>=21 coupled margin',margin,'>1/5000 PASS')
print('Complete local proofs/exact checks PASS; independent audit pending, q<21 OPEN.')
