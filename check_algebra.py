"""Exact algebra checks for both Galton--Watson speed comparison arguments.

This script checks algebraic identities only. It does not independently
verify the probabilistic comparison, continuity, or the complete proof.
The positivity certificates use exact polynomial coefficients, not sampling.
Run with Python 3 and SymPy installed.
"""
from __future__ import annotations
import sympy as s

x, y, v, lam, c, k, d, S = s.symbols('x y v lam c k d S')
checks: list[str] = []


def check(name: str, left: s.Expr, right: s.Expr) -> None:
    difference = s.factor(s.together(left - right))
    if difference != 0:
        raise AssertionError(f'{name}: residual = {difference}')
    checks.append(name)


def check_positive_coefficients(name: str, expression: s.Expr,
                                *variables: s.Symbol) -> None:
    """Certify strict positivity for nonnegative variables exactly.

    Nonnegative coefficients and a positive constant certify that both the
    numerator and denominator of this rational expression are positive.
    """
    numerator, denominator = s.fraction(s.together(expression))
    for part_name, part in (('numerator', numerator),
                            ('denominator', denominator)):
        polynomial = s.Poly(s.expand(part), *variables)
        if not all(coefficient >= 0 for coefficient in polynomial.coeffs()):
            raise AssertionError(f'{name}: {part_name} coefficient failed')
        constant = polynomial.coeff_monomial(1)
        if constant <= 0:
            raise AssertionError(f'{name}: {part_name} strictness failed')
    checks.append(name)


# Manuscript notation: q(x,y), D(x,y), h_v(y), and f_lambda(S).
# The shorter moment symbols k,j below mean hat{mu}_1,hat{mu}_2;
# d means the feasibility quantity Delta = c + 2 hat{mu}_1 - 1,
# never the root-response constant kappa_root.
q = x + y - x*y
D = lam - 1 + q
h = lambda z: (1+v)*z - v
jmax = k*(c-1+4*k)/(c+1+2*k)
P = c**3-c**2+c+1+(6*c**2-2*c-6)*k+8*(c+1)*k**2

# The original ten checks, in their original order.
check('Transport derivative of the speed numerator',
      s.diff((x*y-v*q)/D, x), (y*y+(lam-1)*h(y))/D**2)
check('RDE denominator transformation',
      (c + lam*x/(1-x)).subs(lam,c+1), (c+x)/(1-x))
check('Feasibility of the tilted second moment',
      jmax-k*k, k*(1-k)*(c+2*k-1)/(c+1+2*k))
check('Moment gap numerator',
      c*c*k+4*c*k*k+(2*k-2*c-1)*jmax,
      k*P/(c+1+2*k))
check('Positive expansion in d = c + 2k - 1',
      P.subs(c, d+1-2*k),
      d**3+2*d**2+(2+2*k*(1-2*k))*d+2*(1-k)*(1-2*k))
f_lam = S/(lam+S)
check('Denominator identity used in L r0',
      D.subs(x, f_lam), lam*(lam-1+S+y)/(lam+S))
check('Cancellation in the dual-RDE kernel',
      lam/(lam+S)**2 / D.subs(x,f_lam)**2,
      1/(lam*(lam-1+S+y)**2))
check('Residual parameter sign identity',
      (1-x)*(1-y)*(x*y-v*q)+x*y*(2-x-y),
      x*(1-x)*h(y)+y*(1-y)*h(x)+(1+v)*x*y*(1-x)*(1-y))
check('Monotone tilt ratio derivative',
      s.diff((lam-1+y)/D, y), lam*x/D**2)

check('Explicit primitive of the corrector',
      s.diff(x*y/((lam-1+y)*D), x), y/D**2)

# Strengthened scalar kernel for the direct root comparison. Unlike
# f_gamma(S), this is a polynomial in an escape probability.
mu, j, z = s.symbols('mu j z')
root_kernel = lambda a: h(a) - (1-v)*a*(1-a)/(2*lam)
psi_numerator = lambda a: a*a + (lam-1)*h(a)

check('Scalar root kernel derivative in the escape probability',
      s.diff(root_kernel(y), y),
      1+v-(1-v)*(1-2*y)/(2*lam))
check('Scalar root kernel derivative in the speed',
      s.diff(root_kernel(y), v), -(1-y)*(1-y/(2*lam)))
check('Decomposition of the positive law-variation kernel',
      psi_numerator(y),
      y*y+(lam-1)*root_kernel(y)
      +(lam-1)*(1-v)*y*(1-y)/(2*lam))

# Gamma uses c+1 for lambda, as in the moment-polynomial argument.
Gamma = (c+1)*(2*k-mu)-(1-mu)*(k-j)
speed_upper = mu/(2-mu)
tilted_root_kernel = ((1+speed_upper)*k-speed_upper
                      -(1-speed_upper)*(k-j)/(2*(c+1)))
check('Gamma threshold for the tilted scalar kernel',
      tilted_root_kernel, Gamma/((c+1)*(2-mu)))
check('Large weighted-mean rearrangement of Gamma',
      Gamma, (c+1)*(2*k-1)+(1-mu)*(c+1-k+j))

# F(j) is the denominator-cleared lower bound for Gamma after replacing
# mu by its upper bound obtained from hat{mu}_3 <= hat{mu}_2.
moment_denominator = c*c+2*c*k+j
mu_upper = (c*c*k+(2*c+1)*j)/moment_denominator
moment_F = s.cancel(moment_denominator*Gamma.subs(mu, mu_upper))
check('Concavity of the strengthened moment polynomial',
      s.diff(moment_F, j, 2), -4*c)

P3 = (d**3+(1-k)*(k+3)*d**2
      +(1-k)*(3-2*k-2*k*k)*d+(1-k)**2*(1-2*k))
P5 = (d**5+2*(3-k)*d**4+2*(6-k-3*k*k)*d**3
      +2*(1-k)*(5+12*k-8*k*k)*d**2
      +2*(1-k)*(3+7*k-16*k*k+4*k**3)*d
      +4*(1-k)**2*(1-2*k))
check('Lower endpoint of the strengthened moment interval',
      moment_F.subs(j, k*k).subs(c, d+1-2*k), k*P3)
check('Upper endpoint of the strengthened moment interval',
      moment_F.subs(j, jmax).subs(c, d+1-2*k), k*P5/(d+2)**2)
check('Positive factorization of the cubic endpoint coefficient',
      3+7*k-16*k*k+4*k**3, 3+k*(1-2*k)*(7-2*k))

# k = z/(2(1+z)) parametrizes 0 < hat{mu}_1 < 1/2 for z > 0.
# z is only an auxiliary certificate variable, not the corrector u.
for name, polynomial in (('P3', P3), ('P5', P5)):
    check_positive_coefficients(
        f'{name}: exact positive-coefficient certificate',
        polynomial.subs(k, z/(2*(1+z))), d, z)

# Pointwise identity for kappa_root. After division by lambda D^2 and
# integration, the last term vanishes by N-vZ=0; no RDE assumption enters.
check('Root-response pointwise cancellation',
      x*(1-x)*psi_numerator(y)+y*(1-y)*psi_numerator(x)
      +lam*(x*y-v*q),
      lam*(x*(1-x)*root_kernel(y)+y*(1-y)*root_kernel(x))
      +D*(x*y-v*q))

# T_{lambda,h}(x) = f_{lambda+h}(lambda*x/(1-x)).
step = s.symbols('step')
T = lam*x/(lam+step*(1-x))
check('Root-map infinitesimal velocity',
      s.diff(T, step).subs(step, 0), -x*(1-x)/lam)
check('Root-map finite transform of the RDE',
      T.subs(x, f_lam), S/(lam+step+S))
check('Root-map finite displacement',
      x-T, step*x*(1-x)/(lam+step*(1-x)))

# A deterministic regular_degree-ary tree has beta=(regular_degree-lam)
# /regular_degree. This degree is distinct from the feasibility variable d.
regular_degree = s.symbols('regular_degree')
beta = (regular_degree-lam)/regular_degree
root_speed = T/(2-T)  # V_{lambda+h}(delta_T) has no explicit bias dependence.
check('Regular-tree root-only speed derivative',
      s.diff(root_speed, step).subs(step, 0).subs(x, beta),
      -2*(regular_degree-lam)/(regular_degree+lam)**2)
check('Regular-tree full speed derivative',
      s.diff((regular_degree-lam)/(regular_degree+lam), lam),
      -2*regular_degree/(regular_degree+lam)**2)

for number, name in enumerate(checks, 1):
    print(f'{number}. OK: {name}')
print(f'All {len(checks)} algebra checks verified exactly.')
