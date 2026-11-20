"""Exact new identities and three finite arithmetic payments for N3>-9.
Not a full-rectangle curvature certificate. No samples or old imports.
"""
import sympy as s
from fractions import Fraction as Q
l,u,y=s.symbols("l u y")
S2=1+l;S3=1+l+l*l;S4=S2*(1+l*l);p3=S3-1
rho=l/S2;q3=p3/S3;alpha=q3-rho;t=1-u;A=1+l*t
K=(l+1)/(2*l)+t/2+(l+1)*(2*l*t-l+1)*t/(24*l);h=K-t
Z={j:1+t*sum(l**i for i in range(1,j)) for j in range(1,6)}
P=lambda n:24-2*n-u*(A+1)/A
upole=S3/p3
# Independently expandable formal age identity before substituting Z_j.
z,w,zm,pp,kk,hh,nn=s.symbols("z w zm pp kk hh nn")
original=((2-z/w-l*z*z/w**2)*pp+u*z/zm*
 (-(24-nn)*kk+2*hh+l*z*zm/w**2*((24-2*nn)*kk-2*hh)))/z**3
expanded=2*pp/z**3-pp/(z*z*w)+l*(u*((24-2*nn)*kk-2*hh)-pp)/(z*w*w) \
 +u*(-(24-nn)*kk+2*hh)/(z*z*zm)
assert s.cancel(original-expanded)==0
L33=12*l*P(3)
L32=6*l*(-P(3)/Z[4]+u*(-21*K+2*h)/A)
L31=6*l*l*(u*(18*K-2*h)-P(3))/Z[4]**2
L22=4*l*(u*(22*K-2*h)-P(1))/A
L21=-4*P(1)/A**2
L41=8*l*l*u*(-18*K+2*h)/Z[4]**2
def at(expr): return s.factor(s.cancel(expr.subs(u,upole)))
c33=at(L33)/S3**3
c32=at(L32+L22)/S3**2-at(s.diff(L33,u))/(S3**3*q3)
c31=at(L31+L21+L41)/S3-at(s.diff(L32+L22,u))/(S3**2*q3) \
 +at(s.diff(L33,u,2))/(2*S3**3*q3**2)
N=c31*(1-alpha*y)**2+3*c32*(1-alpha*y)*(1+rho*y)+6*c33*(1+rho*y)**2
pn0=19*l**10+4988*l**9+11522*l**8-4375*l**7-11750*l**6-3832*l**5 \
 -3869*l**4-1240*l**3-52*l*l+311*l+88
pn1=3454*l**8+661*l**7-34371*l**6-30233*l**5+978*l**4+1303*l**3 \
 +1455*l*l-179*l-176
pn2=3473*l**6+15981*l**5+7141*l**4-5297*l**3+184*l*l+132*l-88
a0=-pn0/(12*l**5*S2*S3**3)
a1=-pn1/(12*l**3*S2**2*S3**3)
a2=pn2/(12*l*S2**3*S3**3)
assert s.cancel(N-a0-a1*y-a2*y*y)==0
c=l-1
W=-202797-1422486*c-4135131*c*c-6011031*c**3-2893758*c**4 \
 +c**5*(5158369+11938400*c+12261059*c*c+7731101*c**3+3149207*c**4 \
 +809054*c**5+119241*c**6+7729*c**7+19*c**8)
assert s.cancel(s.diff(a0,l)-W/(6*l**6*S2**2*S3**4))==0
b=Q(10,7)
assert 3454*b**3+661*b*b+978+1303+1455-34371-30233==-Q(16961024,343)<0
cp=Q(3,7)
positive=sum((v*cp**(j+5) for j,v in enumerate(
 (5158369,11938400,12261059,7731101,3149207,809054,119241,7729,19))),Q(0))
assert positive==Q(18566998494411753,96889010407)
assert 202797-positive==Q(1081802149096626,96889010407)>0
gap=s.cancel(9+a0.subs(l,s.Rational(707,500)))
assert gap==s.Rational(86846158517756652247422093279585703,
 95460081663326673010814336960641467)>0
print("PASS complete formal age/Laurent/N3 identities and derivative identity")
print("PASS three explicit exact payments; N3(y)>-9 continuously by written proof")
print("SCOPED: Pa/N5/full-F curvature/final coupled payment are not asserted")

