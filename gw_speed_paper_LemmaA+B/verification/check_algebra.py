#!/usr/bin/env python3
"""Exact algebra checks accompanying the Galton--Watson speed manuscript.

These are symbolic identity checks, not simulations or a formal verification
of the probabilistic proof. No floating-point assertions are used.

Run: python verification/check_algebra.py
Dependency: sympy
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    checks: list[str] = []

    def equal(name: str, expression: sp.Expr) -> None:
        residual = sp.factor(sp.together(expression))
        if residual != 0:
            raise AssertionError(f"{name}: nonzero residual {residual}")
        checks.append(name)

    x, y, lam, v = sp.symbols("x y lam v")
    c = lam - 1
    t = x + y - x*y
    A = c + t
    hv = lambda z: (1 + v)*z - v
    kap = lambda z: z*z + c*hv(z)
    fv = lambda z: hv(z) - (1-v)*z*(1-z)/(2*lam)

    equal("Gateaux kernel", sp.diff((x*y-v*t)/A, x) - kap(y)/A**2)
    equal("f derivative in y", sp.diff(fv(y),y) - (1+v-(1-v)*(1-2*y)/(2*lam)))
    equal("f derivative in v", sp.diff(fv(y),v) + (1-y)*(1-y/(2*lam)))

    L = x*(1-x)*kap(y)+y*(1-y)*kap(x)+lam*(x*y-v*t)
    R = lam*(x*(1-x)*fv(y)+y*(1-y)*fv(x)) + A*(x*y-v*t)
    equal("Root-response cancellation", L-R)

    h = sp.symbols('h')
    T = lam*x/(lam+h*(1-x))
    equal("Root-map infinitesimal velocity", sp.diff(T,h).subs(h,0)+x*(1-x)/lam)
    S = sp.symbols('S')
    bx = S/(lam+S)
    equal("Root-map finite difference", T.subs(x,bx) - S/(lam+h+S))
    equal("Inverse RDE transform", c+lam*x/(1-x) - (c+x)/(1-x))

    mu,k,j,cc,d,u = sp.symbols('mu k j c d u')
    Gamma = (cc+1)*(2*k-mu)-(1-mu)*(k-j)
    etilt_f = (1+mu/(2-mu))*k - mu/(2-mu) - (1-mu/(2-mu))*(k-j)/(2*(cc+1))
    equal("Scalar sufficient condition", etilt_f-Gamma/((cc+1)*(2-mu)))
    equal("Large-k rearrangement", Gamma-((cc+1)*(2*k-1)+(1-mu)*(cc+1-k+j)))

    jub = k*(cc-1+4*k)/(cc+1+2*k)
    equal("Feasibility of moment interval", jub-k*k-k*(1-k)*(cc+2*k-1)/(cc+1+2*k))
    den = cc*cc+2*cc*k+j
    muplus = (cc*cc*k+(2*cc+1)*j)/den
    F = sp.cancel(((cc+1)*(2*k-muplus)-(1-muplus)*(k-j))*den)
    equal("Concavity coefficient", sp.diff(F,j,2)+4*cc)

    P3 = (d**3+(1-k)*(k+3)*d**2+(1-k)*(3-2*k-2*k*k)*d
          +(1-k)**2*(1-2*k))
    P5 = (d**5+2*(3-k)*d**4+2*(6-k-3*k*k)*d**3
          +2*(1-k)*(5+12*k-8*k*k)*d**2
          +2*(1-k)*(3+7*k-16*k*k+4*k**3)*d
          +4*(1-k)**2*(1-2*k))
    equal("Lower moment endpoint", F.subs(j,k*k).subs(cc,d+1-2*k)-k*P3)
    equal("Upper moment endpoint", F.subs(j,jub).subs(cc,d+1-2*k)-k*P5/(d+2)**2)
    equal("Last nontrivial coefficient", 3+7*k-16*k*k+4*k**3-(3+k*(1-2*k)*(7-2*k)))

    # An additional exact coefficient check for positivity on 0<k<1/2, d>=0.
    # k=u/(2(1+u)) parametrizes that interval; the cleared denominators are positive.
    certificates = {}
    for name, expr in (("P3",P3),("P5",P5)):
        rational = sp.factor(expr.subs(k,u/(2*(1+u))))
        numerator, denominator = sp.fraction(rational)
        polynomial = sp.Poly(sp.expand(numerator),d,u)
        if not all(coefficient >= 0 for coefficient in polynomial.coeffs()):
            raise AssertionError(f"{name}: coefficient certificate failed")
        if polynomial.eval({d:0,u:0}) <= 0:
            raise AssertionError(f"{name}: strictness certificate failed")
        checks.append(f"{name}: nonnegative-coefficient positivity certificate")
        certificates[name] = {"terms": len(polynomial.terms()), "denominator": str(denominator)}

    # Deterministic d-ary-tree sanity check for the root-only derivative.
    dd = sp.symbols('d_regular',positive=True)
    beta = (dd-lam)/dd
    # For a point mass at x, V=x/(2-x), with no explicit lambda dependence.
    equal("Regular-tree root response", (2*sp.diff(T,h)/(2-T)**2).subs(h,0).subs(x,beta)
          +2*(dd-lam)/(dd+lam)**2)
    equal("Regular-tree full speed derivative", sp.diff((dd-lam)/(dd+lam),lam)+2*dd/(dd+lam)**2)

    report = {
        "status": "all checks passed",
        "number_of_checks": len(checks),
        "checks": checks,
        "coefficient_certificates": certificates,
        "scope": "Exact algebra only; the manuscript separately proves the probability and limit arguments.",
    }
    target = Path(__file__).resolve().with_name('verification_results.json')
    target.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
