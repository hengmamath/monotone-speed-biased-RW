"""Exact checks for the written uniform signed-pole ratio lemma only.
Not a full-J1 curvature or speed theorem certificate; no samples/grid.
"""
from fractions import Fraction as Q
import sympy as s

l,y=s.symbols("l y")
S2=1+l;S3=1+l+l*l;S4=S2*(1+l*l)
alpha=l*l/(S2*S3);e=l**3/(S3*S4);D=l*l/S4;dkdelta=l*l/S2
def eq(a,b):
    assert s.cancel(a-b)==0
eq(D,alpha+e)
eq(alpha-2*e,l*l*(l-1)**2/(S3*S4))
eq(s.diff(alpha,l),l*(2+2*l-l**3)/(S2*S3)**2)
eq(s.diff(l*l/S3,l),l*(2+l)/S3**2)
eq(s.diff((l-1)**2/S4,l),(l-1)*(3+3*l+3*l*l-l**3)/S4**2)
c=s.symbols("c")
eq((9*S3*S4-100*l**3).subs(l,c+1),
   8-30*c+6*c*c+89*c**3+63*c**4+9*c**5)
r=((1-D*y)/(1-alpha*y))**5
eq(s.diff(r,y,2),10*e*(1-D*y)**3/(1-alpha*y)**7*
   (2*e-alpha+alpha*D*y))
eq(3*dkdelta-5*D,l*l*(3*l*l-2)/S4)
Y=S2/(l+2)
Phi=S2**2*(S4+1)**5/((l+2)**2*S4**5*(2-l)**3)
eq((1-D*Y)**5/(1-dkdelta*Y)**3,Phi)
eq(s.diff(Phi,l)/Phi,2/S2-2/(l+2)-5*s.diff(S4,l)/(S4*(S4+1))+3/(2-l))
assert Q(10,7)<Q(3,2) and Q(707,500)<Q(10,7)
assert Q(17,24)<Q(71,100)
assert Q(700,3723)<Q(19,100)
assert 4000<4361
H=Q(707,500);S2h=1+H;S3h=1+H+H*H;S4h=S2h*(1+H*H)
gap=Q(11,1000)-H*H*(H-1)**2/(S3h*S4h)
assert gap==Q(91882193461459,332868529723769000)>0
assert 1-Q(19,100)*Q(71,100)>Q(43,50)
assert 1-Q(28,100)*Q(71,100)>Q(4,5)
g1=Q(1,50)-5*Q(9,100)*Q(11,1000)*Q(50,43)**7
g2=Q(1,20)-5*Q(9,100)*Q(19,100)*Q(28,100)*Q(71,100)*Q(50,43)**7
assert g1==Q(78459236107,13590930555350)>0
assert g2==Q(6234236107,5436372222140)>0
phih=S2h**2*(S4h+1)**5/((H+2)**2*S4h**5*(2-H)**3)
g3=5-phih
assert g3==Q(7810521133897555222894719434215789155174968196289255,
             30553488005938652603121311614689577421321167214257851)>0
g4=Q(391,60)*Q(12,17)**3*Q(4,5)**5-Q(3,4)
assert g4==Q(19077,18062500)>0
print("PASS generic small geometric and derivative identities")
print("PASS four explicit positive rational gaps:",g1,g2,g3,g4)
print("SCOPED: N3 sign/coefficients and complete F curvature are NOT asserted")
