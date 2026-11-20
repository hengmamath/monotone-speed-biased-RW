"""Exact finite identities for the complete joint curvature upper polynomial.
Pays highest coefficients only; four middle coefficient bounds remain OPEN.
"""
import sympy as s
from fractions import Fraction as F
y,D,e,z,delta,p0,p1,p2,p3,n30,n31,n32,n40,n41,n42,t0,t1,q3,q4,q5,ck,l= \
 s.symbols("y D e z delta p0 p1 p2 p3 n30 n31 n32 n40 n41 n42 t0 t1 q3 q4 q5 ck l")
Pa=p0+p1*y+p2*y*y+p3*y**3
N3=n30+n31*y+n32*y*y
N4=n40+n41*y+n42*y*y
N5=t0+t1*y
Ra=1-5*D*y+10*D*D*y*y-5*D**3*y**3
U=1-5*e*y+y*y/20
Rold=(1-D*y)*(1+4*z*y+(4*z*delta+6*z*z)*y*y
 +(4*z*delta*delta+12*z*z*delta+4*z**3)*y**3)
R=1+(4*z-D)*y+10*z*z*y*y+10*z*z*(D+2*z)*y**3 \
 -4*D*z*(D*D+5*D*z+5*z*z)*y**4
assert s.expand(Rold.subs(delta,D+z)-R)==0
v=s.symbols('v')
assert s.expand((1-v)**5-(1-5*v+10*v*v-5*v**3)+v**3*(5-5*v+v*v))==0
P=s.Poly(s.expand(Pa*Ra+q3*q3*(N3*U+s.Rational(63,100)*y*y)
 +q4*q4*N4+q5*q5*N5*R+5*ck*l*l-s.Rational(3,4)),y)
assert P.degree()==6
assert s.expand(P.nth(5)-(-5*D**3*p2+10*D*D*p3
 -4*q5*q5*t1*D*z*(D*D+5*D*z+5*z*z)))==0
assert P.nth(6)==-5*D**3*p3
S2=1+l;S4=S2*(1+l*l)
a=s.cancel(P.nth(6).subs({p3:-80*l**4/S2**8,D:l*l/S4}))
assert s.cancel(a-400*l**10/(S2**11*(1+l*l)**3))==0
assert s.expand(S2*S2-4*l-(l-1)**2)==0
assert s.expand(1+l*l-2*l-(l-1)**2)==0
assert s.cancel(s.diff(l*l/S2,l)-l*(l+2)/S2**2)==0
assert F(25,512)*F(100,119)==F(625,15232)
assert F(1,20)-F(625,15232)==F(683,76160)>0
Y=F(71,100)
Q=-F(59,10)+F(19,2)*Y-9*Y*Y+F(13,2)*Y**3+F(9,2)*Y**4+F(1,20)*Y**6
assert Q==-F(4310956816079,20000000000000)<0
assert F(19,2)-F(18*18,4)/F(39,2)==F(139,26)>0
print('PASS exact common-parameter R45 simplification and complete P degree6')
print('PASS b5 three-negative-term identity and exact b6 identity')
print('PASS b6 short positive gap 683/76160; no critical-point sampling')
print('PASS conditional reduction Q(71/100)<0 and Q monotonicity')
print('SCOPED: b1,b2,b3,b4 payments and full Fuu<0 are NOT asserted')

