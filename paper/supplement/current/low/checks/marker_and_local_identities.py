"""Reconstruct the displayed marker/floor rational identities from kernels.

No canonical law is sampled or substituted. All variables are independent
formal symbols until an explicitly displayed calibration is imposed.
"""
import sys
import sympy as S
from fractions import Fraction as F

if sys.flags.optimize or not __debug__:
    raise RuntimeError("Assertions must remain enabled.")

count = 0


def equal(name, lhs, rhs):
    global count
    if S.cancel(lhs - rhs) != 0:
        raise AssertionError(name)
    count += 1
    print("identity:", name, flush=True)


l, U, V, w, alpha = S.symbols("l U V w alpha")
c = l - 1
X, Y = c * U / (1-U), c * V / (1-V)
A = c + X + Y - X*Y
bt = X*(1-X)/l
Pc = (1-Y)*(2*w-(1+w)*Y)
Qa = -w/c+(1+(l+1)*w/c)*V-(alpha+l*w/c)*V**2
equal("transformed b(X)Y/A^2", bt*Y/A**2,
      U*V*(1-l*U)*(1-V)/(l*(1-l*U*V)**2))
equal("transformed b(X)Pc(w;Y)/A^2", bt*Pc/A**2,
      U*(1-l*U)*(1-l*V)*(2*w-(c+(l+1)*w)*V)
      /(l*c*(1-l*U*V)**2))
equal("transformed calibrated entropy kernel",
      ((1-alpha)*Y**2+c*((1+w)*Y-w))/A**2,
      (1-U)**2*Qa/(1-l*U*V)**2)
x, y = S.symbols("x y")
t = x+y-x*y
equal("off-speed symmetrization",
      (x*(1-x)*(1-y)*(2*w-(1+w)*y)
       +y*(1-y)*(1-x)*(2*w-(1+w)*x))/(2*l),
      (1-t)*(w*t-x*y)/l)
am, a0, ap = S.symbols("a_sm1 a_s a_sp1")
J = -2*w*am+(c*(1+2*alpha)+(3*l+1)*w)*a0 \
    -(c*(l+2*alpha)+l*(l+1)*w)*ap
tn = -w/c*am+(1+(l+1)*w/c)*a0-(alpha+l*w/c)*ap
equal("correct Mellin first factor, exact bare K coefficient",
      2*alpha*(a0-l*ap)*(a0-ap)/l
      -(a0-l*ap)*(2*w*(am-l*a0)-(c+(l+1)*w)*(a0-l*ap))/(l*c),
      (a0-l*ap)*J/(l*c))
equal("J versus t, with free assigned speed",
      J, 2*c*tn+c*((1+w)*(a0-l*ap)-2*(1-alpha)*a0))
u, a2, R = S.symbols("u a2 R")
A0 = 1-(l+1)*u+l*a2
acal = (u-R*A0)/a2
equal("calibration t0",
      -R+(1+(l+1)*R)*u-(acal+l*R)*a2, 0)
equal("calibrated endpoint quadratic",
      (-R+(1+(l+1)*R)*V-(acal+l*R)*V**2).subs(V,1/l),
      (l-acal)/l**2)
rho, rp, ri, delta, theta = S.symbols("rho rp ri delta theta")
equal("Mellin gamma reorganization",
      a0*(1-rp)+theta-a0+(a0*ri-delta),
      a0*(ri-rp)-delta+theta)

# The continuous quadrature and endpoint budget: direct differentiation
# and full exact rational margins from the displayed expressions.
q = S.symbols("q", positive=True)
lo = lambda s: 2*(s+s**3/3+s**5/5+s**7/7)
CH = F(11407,7440)-F(21,10)*lo(F(61,187))+F(1,240)
assert CH == F(17160482889458863049,148731921929151943800)
assert F(11407,7440)-F(21,10)*lo(F(61,187)) \
       > F(175,96)-3*lo(F(7,25))
Jq = (q+1)**4/(324*q*(q-4)**3)+(q+1)**2/(36*q**3*(q-4))
budget = S.Rational(69,500)-q**2/(q+1)**2*S.Rational(CH.numerator,CH.denominator) \
         -q**4/(q+1)**4*Jq
equal("final continuous budget derivative",
      (q+1)**3/q*S.diff(budget,q),
      -2*S.Rational(CH.numerator,CH.denominator)
      +q*(q+1)**3/(27*(q-4)**4)+(q*q-2*q+2)/(18*q*(q-4)**2))
equal("decreasing final rational derivative term",
      S.diff((q*q-2*q+2)/(18*q*(q-4)**2),q),
      (-q**3-6*q+8)/(18*q*q*(q-4)**3))
assert budget.subs(q,10)-S.Rational(1,40) \
       == S.Rational(195098675960795601986623,65597470507242819053271000)>0
assert budget.subs(q,21)-S.Rational(1,40) \
       == S.Rational(713805528405149594753,359931251068547703996000)>0

# Six Q0 rational tests, directly on the stated finite expressions.
def f(lam,n):
    return lam**(n-1)*(lam-1)**2/(lam**n-1)**2

def tail(lam):
    cc=lam-1
    return cc*cc/(lam*(cc-cc*cc/2+cc**3/3)*(lam**9-1))+f(lam,9)/2

for lam, threshold in [(F(6,5),F(1559,1000)),(F(23,20),F(63,40)),(F(11,10),F(19,12))]:
    assert sum(f(lam,n) for n in range(1,9))+tail(lam)>threshold
lam=F(6,5)
assert sum(f(lam,n)*(1-F(1,n)) for n in range(1,9))+F(8,9)*tail(lam)>F(9,25)
assert sum(F(1,n**3)*(1-(lam-1)/(lam**n-1)) for n in range(1,9))+F(1,128)<F(2,15)
lam=F(23,20);cc=lam-1;z=lam**-8;al=2*cc/(lam+1)
upper=cc**4*z*z/(6*lam*lam)*(8/al*(3-z)/(1-z)**3+(1/al**2)*((2-z)/(1-z)**2-F(1,2)))
assert sum(n*f(lam,n)**2 for n in range(1,9))+upper<F(239,200)
print("PASS",count,"generic identities, exact Q0 and final Q3c rational checks.",flush=True)
