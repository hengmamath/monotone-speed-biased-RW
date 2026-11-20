"""Authorship exact check of a fully written manual derivation from two original poles.

No old files, coefficient vectors, CAS apart call, grid or previous proof runner.
The human proof uses only pole constant/linear terms, reciprocal recurrences,
and explicitly displayed low-degree divisions; these checks are supplementary.
"""
import sympy as s
from fractions import Fraction as F
l,x,eps=s.symbols('l x eps')
S={j:sum(l**k for k in range(j)) for j in range(1,6)}
rho=l/S[2];q4=1-1/S[4];q5=1-1/S[5];D=q4-rho;z=q5-q4
X=l+1/l;Q=x*x+x-1;a=(x+1)*Q;I=(x+2)*x*x
u0=S[5]/(l*S[4]);t0=-1/(l*S[4]);u=u0*(1-eps);t=1-u
K=lambda tt:(l+1)/(2*l)+(s.Rational(1,2)+(1/l-l)/24)*tt+(l+1)*tt*tt/12
P=12-u-u/(1+l*t)
Z4=1+t*(S[4]-1)
M2=8*l**3*(u*(10*K(t)+2*t)-P)/Z4
M1=-8*l*l*P/Z4**2
orig_c2=s.cancel(M2.subs(eps,0)/S[5]**2)
orig_c1=s.cancel(M1.subs(eps,0)/S[5]+s.diff(M2,eps).subs(eps,0)/S[5]**2)
L0=10*K(t0)+2*t0
L1=u0*(10*s.diff(K(s.Symbol('tt')),s.Symbol('tt')).subs(s.Symbol('tt'),t0)+2)
P0=P.subs(eps,0);P1=s.diff(P,eps).subs(eps,0)
assert s.cancel(u0-Q.subs(x,X)/((l+1)*X))==0
assert s.cancel(t0+1/(l*l*(l+1)*X))==0
assert s.cancel(Z4-(l**3/S[4])*(1+a.subs(x,X)*eps))==0
assert s.cancel(P0-(12-Q.subs(x,X)/((l+1)*X)-Q.subs(x,X)/(l*(X+1))))==0
assert s.cancel(P1-(u0+Q.subs(x,X)*X*(X+2)/(l*(X+1)**2)))==0
cl2=8*(L0-q5*P0)/(l*S[5])
cl1=8*(L1-(1+a.subs(x,X))*L0+(a.subs(x,X)*q5-I.subs(x,X))*P0-q5*P1)/(l*S[5])
assert s.cancel(orig_c2-cl2)==0 and s.cancel(orig_c1-cl1)==0
print('PASS original complete M52/M51 -> epsilon constant/linear extraction, including -P and correct epsilon sign')

def even(ff):return s.cancel((ff+ff.subs(l,1/l))/2)
R=[s.Integer(1),x-1];M=[s.Integer(2),x]
for n in range(2,6):R.append(s.expand(x*R[-1]-R[-2]));M.append(s.expand(x*M[-1]-M[-2]))
for n in range(6):
 assert s.cancel(even(l**(-n)/(l+1))-R[n].subs(x,X)/2)==0
 assert s.cancel(even(l**(-n))-M[n].subs(x,X)/2)==0
print('PASS reciprocal mean recurrences R0..5/M0..5, seeds and induction identities')
F0=5*(M[1]+M[2])/2-7*R[3]/(2*x)-5*(R[4]-R[2])/(24*x)+5*R[5]/(12*x*x)
F1=Q/x*(7*R[1]/2+5*(R[2]-R[0])/24-5*R[3]/(6*x))
C0=6*x-Q*(x-1)/(2*x)-Q*(x*x-2)/(2*(x+1))
B0=6*x*(x+2)/Q-x/2-x*(x*x+x-2)/(2*(x+1))
B1=x/2+x*x*(x+2)*(x*x+x-2)/(2*(x+1)**2)
for name,ff,expected in [('F0',L0/l,F0),('F1',L1/l,F1),('C0',P0/l,C0),('B0',q5*P0/l,B0),('B1',q5*P1/l,B1)]:
 assert s.cancel(even(ff)-expected.subs(x,X))==0
 print('PASS original reciprocal block',name)
h=5*x**5-29*x**4+124*x**3+63*x*x-64*x-10
p=-15*x**3+99*x*x-54*x-20
assert s.cancel(F0-h/(24*x*x))==0 and s.cancel(F1-Q*p/(24*x*x))==0
V=8*(F0-B0)/Q
U=8*(F1-(1+a)*F0+a*B0-I*C0-B1)/Q
assert s.cancel(even(l*l*orig_c2)-V.subs(x,X))==0
assert s.cancel(even(l*l*orig_c1)-U.subs(x,X))==0
print('PASS five-block U,V forms; h degree5 and p degree3 obtained from recurrence')

# Explicit manual quotient identities, not an apart call or a numerator table.
identities=[1/(x*Q)+1/x-(x+1)/Q,
            1/(x*x*Q)+1/(x*x)+1/x-(x+2)/Q,
            x/((x+1)*Q)-1/(x+1)-(1-x)/Q,
            (x+2)*(x*x-2)/(x+1)-(x*x+x-3)+1/(x+1),
            (x+2)**2*(x-1)/(x+1)**2-(x+1)+(3*x+5)/(x+1)**2,
            x*x*(3*x+5)/(x+1)**2-(3*x-1)-(1-x)/(x+1)**2,
            -4/(x+1)+4*(1-x)/((x+1)**2*Q)-8*x/(x+1)**2-(8-12*x)/Q]
assert all(s.cancel(q)==0 for q in identities)
assert s.expand(5*x**3-17*x*x+136*x+63-(5*x-22)*Q-(163*x+41))==0
assert s.expand(271*x**3+593*x*x-100*x-75-(271*x+322)*Q-(-151*x+247))==0
Upoly=s.Rational(7,3)*x**4+12*x**3-s.Rational(287,3)*x*x-s.Rational(514,3)*x+s.Rational(112,3)
Uinter=Upoly+s.Rational(20,3)/x-s.Rational(10,3)/x**2-4/(x+1)
Uinter+=((271*x**3+593*x*x-100*x-75+64/x+10/x**2)/3+4*(1-x)/(x+1)**2)/Q
assert s.cancel(U-Uinter)==0
Uderived=(7*x**4+36*x**3-287*x*x-243*x+434)/3+(355-113*x)/(3*Q)+8*x/(x+1)**2-18/x-s.Rational(20,3)/x**2
Vderived=(5*x-22)/3-48*(x+1)/Q**2+(113*x-211)/(3*Q)-8/(x+1)+s.Rational(74,3)/x+s.Rational(10,3)/x**2
assert s.cancel(Uinter-Uderived)==0 and s.cancel(V-Vderived)==0
print('PASS every displayed manual division and collection; derived compact U,V identities are consequences, not external identity data')

qp=2*x+1;aa=355-113*x;bb=113*x-211
Upp=28*x*x+72*x-s.Rational(574,3)+(226*qp*Q+2*aa*(qp*qp-Q))/(3*Q**3)+16*(x-2)/(x+1)**4-36/x**3-40/x**4
Vpp=-48*((x+1)*(6*qp*qp-4*Q)-4*qp*Q)/Q**4+(2*bb*(qp*qp-Q)-226*qp*Q)/(3*Q**3)-16/(x+1)**3+s.Rational(148,3)/x**3+20/x**4
assert s.cancel(s.diff(U,x,2)-Upp)==0 and s.cancel(s.diff(V,x,2)-Vpp)==0
assert 355-113*F(17,8)==F(919,8)>0
assert F(28)*4+F(72)*2-F(574,3)-F(36,8)-F(40,16)==F(173,3)>0
assert 2*30*F(11,2)**2-226*5*5==-3835<0
assert -F(48)*246/6**4+F(148,24)+F(20,16)==-F(61,36)<0
endpoints=[F(ff.subs(x,2)) for ff in [U,s.diff(U,x),V,s.diff(V,x)]]
assert endpoints==[F(-12013,45),F(-68921,270),F(87,50),F(526,45)]
print('PASS complete continuous U convex and V concave with margins173/3 and -61/36; four endpoint values',endpoints)

T=x**4+4*x**3+3*x*x+5
q=s.symbols('q');f=s.Rational(16,625)*q**4-q*q+3*q-6
assert f.subs(q,5)==0 and s.diff(f,q).subs(q,5)==s.Rational(29,5)
assert s.diff(f,q,2).subs(q,5)==s.Rational(142,25)>0
assert s.diff(f,q,3)==s.Rational(384,625)*q
assert T.subs(x,s.Rational(9,4))==s.Rational(23393,256)<100
assert 267*29-(256*24+3*F(13,4)*100)==624>0
assert F(7)-F(4272,625)==F(103,625)>0
print('LOCAL complete generator-origin manual proof Jbar5>=-4272/625>-7; independent audit pending')
print('No E17/R6/N30, no natural U/V full numerator coefficient table or apart algorithm; all compact coefficients derived visibly')
print('Not a claim of fewer integer occurrences or shorter than every prior proof; direct five-block convexity without compact collection remains optional OPEN simplification')
