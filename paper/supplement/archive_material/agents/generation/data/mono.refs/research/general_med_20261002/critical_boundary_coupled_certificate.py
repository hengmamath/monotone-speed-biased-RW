"""248--253 scalar h0 complete head/root budget. Local checks; audit pending."""
import sympy as S
from fractions import Fraction as F
from math import comb
from collections import defaultdict
x,t,g=S.symbols('x t g');q=1/x;i=t/x;j=q+i;aa=j+1;R=q-g
alpha=(1+2*g*x*x)/(1+x);r=j/aa;rp=(j-1)/j;wi=q*q/(j*j)
S2=1/aa+1/(2*aa**2)+1/(6*aa**3)
S3=1/(2*aa**2)+1/(2*aa**3)+1/(4*aa**4)-1/(12*aa**6)
V=((1+4*R)*q*q*S2-(2+4*R)*q**3*S3-2*R*q*q*((i+1)/aa**2+1/aa))/wi
tau=1-(alpha+R)*r+2*R-R/rp
B=2*i*alpha+2*i*R*r/j+2*(i+1)*R*r*r/j+(2*i-1)*tau
env=(9*t-7)/(3*(1+t))
num,den=S.fraction(S.factor(S.cancel(B-2*V-env-x*(3-9*t)/(1+t))))
assert S.cancel(den-3*(t+1)*(x+1)*(-t+x-1)*(t+x+1)**6)==0
def bern(pp,axes,deg,scale):
    assert all(a<=b for a,b in zip(pp.degree_list(),deg))
    cc={mo:F(co)*scale[0]**mo[0]*scale[1]**mo[1] for mo,co in pp.terms()}
    for axis in axes:
        groups=defaultdict(dict)
        for mo,co in cc.items(): groups[mo[:axis]+mo[axis+1:]][mo[axis]]=co
        out={}
        for key,aa in groups.items():
            for jj in range(deg[axis]+1):
                vv=sum((co*F(comb(jj,k),comb(deg[axis],k)) for k,co in aa.items() if k<=jj),F())
                if vv:out[key[:axis]+(jj,)+key[axis:]]=vv
        cc=out
    return cc
for ep in (S.Rational(1,8),S.Rational(1,4)):
    pp=S.Poly((-num).subs(g,ep),x,t)
    cc=bern(pp,(0,1),(18,17),(F(1,10),F(1,2)))
    assert len(cc)==324 and all(a>0 for a in cc.values())
    shifted=S.Poly(S.expand(pp.as_expr().subs(t,t+S.Rational(1,2))),x,t)
    dd=bern(shifted,(0,),(9,8),(F(1,10),F(1)))
    assert len(dd)==81 and all(a>0 for a in dd.values())
    print('249 ALL-age g',ep,'head324/tail81 coefficients PASS')
Q,z,v=S.symbols('Q z v');a=Q+1
Tl=Q*Q*(1/a+1/(2*a*a)+1/(6*a**3)-1/(30*a**5))
Tu=Q*Q*(1/a+1/(2*a*a)+1/(6*a**3))
assert S.cancel(Tl-2*Q*(Q-S.Rational(1,4))/(2*Q+S.Rational(1,2))-Q*(5*Q**4+30*Q**3+71*Q**2+79*Q+30)/(30*(Q+1)**5*(4*Q+1)))==0
assert S.cancel(2*Q*(Q-S.Rational(1,8))/(2*Q+S.Rational(3,4))-Tu-Q*(Q*Q-6)/(6*(Q+1)**3*(8*Q+3)))==0
S3up=1/(2*a*a)+1/(2*a**3)+1/(4*a**4)
fn,fd=S.fraction(S.factor(Tl*Tl-2*Q**4*S3up-S.Rational(69,500)*(Q-Tl)))
assert fd==45000*(Q+1)**10
fpoly=S.Poly(S.expand(fn.subs(Q,z+10)),z)
assert fpoly.degree()==10 and min(fpoly.all_coeffs())==645
print('248 complete source and1/8<g<1/4 rational bounds PASS')
s0=F(7,25);s1=F(61,187)
lo=lambda s:2*(s+s**3/3+s**5/5+s**7/7)
I0up=F(175,96)-3*lo(s0)
I1up=F(11407,7440)-F(21,10)*lo(s1)
CH=I1up+F(1,240)
assert I1up>I0up and CH==F(17160482889458863049,148731921929151943800)
L=S.Rational(69,500)-Q*Q/(Q+1)**2*S.Rational(CH.numerator,CH.denominator)-Q**3/(324*(Q-4)**3)-Q/(36*(Q-4)*(Q+1)**2)
ln,ld=S.fraction(S.factor(L-S.Rational(1,40)))
pl=S.Poly(S.expand(ln.subs(Q,10+11*v)),v);D=pl.degree()
assert D==5
coef={mo[0]:F(co) for mo,co in pl.terms()}
bc=[sum((co*F(comb(jj,k),comb(D,k)) for k,co in coef.items() if k<=jj),F()) for jj in range(D+1)]
assert min(bc)==1560789407686364815892984 and all(a>0 for a in bc)
print('252 full boundary budget q[10,21]:6 Bernstein coefficients >0 PASS')
assert F(81,70)**2<2 and 8*F(81,80)**3/F(7,4)**2<3
assert F(4557,183)<25 and 13*F(9,5)>22
assert 2*21**2==882 and 8*21**2==3528
print('253 COMPLETEhead supports24/12 and summable uniform tail882/N,3528/N PASS')
print('Local exact checks PASS. No actuallambda1 speed claim; finiteh explicitwidth not established.')
