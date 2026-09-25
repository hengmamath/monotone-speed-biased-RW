"""Exact algebra checks for the full-RDE correction argument.

This script checks algebraic identities only. It does not independently
verify the probabilistic comparison, continuity, or the complete proof.
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

t = x + y - x*y
A = lam - 1 + t
h = lambda z: (1+v)*z - v
jmax = k*(c-1+4*k)/(c+1+2*k)
P = c**3-c**2+c+1+(6*c**2-2*c-6)*k+8*(c+1)*k**2

check('Transport derivative of the speed numerator',
      s.diff((x*y-v*t)/A, x), (y*y+(lam-1)*h(y))/A**2)
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
F = S/(lam+S)
check('Denominator identity used in L r0',
      A.subs(x, F), lam*(lam-1+S+y)/(lam+S))
check('Cancellation in the dual-RDE kernel',
      lam/(lam+S)**2 / A.subs(x,F)**2,
      1/(lam*(lam-1+S+y)**2))
check('Residual parameter sign identity',
      (1-x)*(1-y)*(x*y-v*t)+x*y*(2-x-y),
      x*(1-x)*h(y)+y*(1-y)*h(x)+(1+v)*x*y*(1-x)*(1-y))
check('Monotone tilt ratio derivative',
      s.diff((lam-1+y)/A, y), lam*x/A**2)

check('Explicit primitive of the corrector',
      s.diff(x*y/((lam-1+y)*A), x), y/A**2)

for number, name in enumerate(checks, 1):
    print(f'{number}. OK: {name}')
print(f'All {len(checks)} algebraic identities verified exactly.')
