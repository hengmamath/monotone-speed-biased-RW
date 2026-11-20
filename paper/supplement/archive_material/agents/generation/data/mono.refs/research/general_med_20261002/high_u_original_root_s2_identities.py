"""Complete original identities for the NEW high-u root+s2 payment.

No sampled identity or shared incorrect calibration. First keep K FREE,
and separately start from original speed, original a, free-a/free-v floor.
"""
import sympy as S
from pathlib import Path
src=Path(__file__).with_name('high_u_original_root_s2.py').read_text()
exec(compile(src.split('for point in')[0], 'correct_builder', 'exec'))
k=S.symbols('k');a1=l+1-l*u;a2=l*l+l+1-(l*l+l)*u
z=R/a1;b=u*z
t2=u*u*(1+R*R*(k-1+u)/(1-u))
q2=u+l*u*u*z+a1*u*u*z*z/(1-u)
v=c*t2/(2*q2-(l+1)*t2)
a=(u-v*(1-(l+1)*u+l*b)/c)/b
rn=1-u+R*R*(k-1+u)
qn=a1*(1-u)+l*u*R*(1-u)+u*R*R
vd=2*qn-(l+1)*u*a1*rn;vn=c*a1*rn
a0n=(1-(l+1)*u)*a1+l*u*R
an=a1*(vd-rn*a0n)
assert S.cancel(v-u*vn/vd)==0
assert S.cancel(a-an/(R*vd))==0
av,vv=S.symbols('a v');r1=1/a1;r2=a1/a2;ep=1-l*z
m=av*(1-r2)+vv/c*(l+1-l*r2-1/z)
h=((1+vv)*ep*ep-2*(1-av)*ep)/l
h+=2*l*z*z*((1+vv)*(1-l*r2)**2/l
          +2*(1-av)*(r2-r1)+2*(1/l-r1)*m)
rr=R*(vd+u*vn)*(a1-l*R)**2-2*(R*vd-an)*(a1-l*R)*a1
tr=R*(vd+u*vn)*R**2*(a2-l*a1)**2*a1
tr+=2*l*(R*vd-an)*(a1*a1-a2)*R**2*a2
tr+=2*(a1-l)*an*(a2-a1)*R**2*a2
tr+=2*(a1-l)*R*u*a1*rn*R*((l+1)*a2*R-l*a1*R-a1*a2)*a2
pn=rr*a1*a2*a2+2*l*tr
dd=l*R*vd*a1**3*a2*a2
# Normalize the FREE affine expression before substituting; exact polynomial
# cross-multiplication avoids expanding deeply nested original fractions.
hn,hd=S.fraction(S.cancel(h))
hh=S.Poly(hn,av,vv)
assert hh.total_degree()==1
cleared=hh.coeff_monomial(1)*R*vd
cleared+=hh.coeff_monomial(av)*an+hh.coeff_monomial(vv)*u*vn*R
assert S.Poly(S.expand(cleared*dd-pn*hd*R*vd),l,u,R,k).is_zero
pk=S.Poly(S.expand(pn),k);dk=S.Poly(S.expand(dd),k)
assert pk.degree()==1 and dk.degree()==1
assert S.Poly(P.as_expr()-pk.coeff_monomial(1)*kd-pk.coeff_monomial(k)*kn,l,u,R).is_zero
assert S.Poly(D.as_expr()-dk.coeff_monomial(1)*kd-dk.coeff_monomial(k)*kn,l,u,R).is_zero
print('5 COMPLETE ORIGINAL identities PASSED; K denominator:',S.factor(kd),flush=True)
