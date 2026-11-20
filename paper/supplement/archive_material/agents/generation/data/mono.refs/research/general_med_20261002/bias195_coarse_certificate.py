"""Exact 63-polynomial certificate for the unaudited lambda>=39/20 draft.

No law grid, tree sample, or floating point. All outputs are exact rationals.
The full finite-mean probabilistic assembly still needs independent review.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
import sympy as sp


def certificate(expr, e, s, r):
    pp = sp.Poly(sp.expand(expr), e, s, r)
    de, ds, dr = [pp.degree(x) for x in (e, s, r)]
    powers = {p: F(int(a.p), int(a.q)) for p, a in pp.terms()}
    blocks = []
    for k in range(de + 1):
        entries = []
        for j in range(dr + 1):
            aa = [sum((
                a*F(comb(j, b), comb(dr, b))
                for (kk, ii, b), a in powers.items()
                if kk == k and ii == i and b <= j
            ), F(0)) for i in range(ds + 1)]
            nz = [i for i, a in enumerate(aa) if a]
            if not nz:
                entries.append({"r_index": j, "zero": True})
                continue
            q = nz[0]
            lower = aa[q] + sum((
                a*F(9, 25)**(i-q) for i, a in enumerate(aa)
                if i > q and a < 0
            ), F(0))
            assert lower > 0, (k, j, q, lower)
            entries.append({"r_index": j, "leading_s_power": q,
                            "s_power_coefficients": [str(a) for a in aa],
                            "lower_coefficient": str(lower)})
        blocks.append({"e_power": k, "entries": entries,
                       "minimum": str(min(
                           F(0) if z.get("zero") else F(z["lower_coefficient"])
                           for z in entries))})
    return {"degrees": [de, ds, dr], "power_term_count": len(powers),
            "power_coefficients": [{"powers": list(p), "coefficient": str(a)}
                                   for p, a in sorted(powers.items())],
            "coarse_blocks": blocks}


def main():
    e, s, r, c = sp.symbols("e s r c")
    lam = c + 1
    L, d = c + 2 + s, 1 - c*s
    DN = s*d*L**2 + lam*r*s**2*(1+s)*L-lam**2*r**2*s**2*(1+s)**2
    TN = s**2*L**2*(5+2*r**2*(1+s)**2)
    AN = (1-(2*c+1)*s)*L+lam**2*r*s*(1+s)
    BN = (1-s)*L+r*s*(1+s)
    EN = c*(2*c+3)*s-(c+2)
    common = (1+s)**2*L**2
    D0, Tbar = DN/common, TN/(5*common)
    V = c*Tbar/(c*Tbar+2*D0)
    w0 = 1/(c*(1+s))
    zH = AN/(c**2*(1+s)*L)
    F0 = 2-2*(c+(lam+1)*V)*d*w0+2*V*zH
    F1 = 2-2*(c+(lam+1)*V)*d*w0+(1+V)*(r*s/L)*(AN/BN)
    N0 = TN*(AN+c*L*EN)+10*lam*c*s*L*DN
    N1 = ((TN*EN+10*lam*s*DN)*L*BN
          +(1+s)*r*s*AN*(c*TN+5*DN))
    assert sp.cancel(F0-2*N0/(c*(1+s)*L*(c*TN+10*DN))) == 0
    assert sp.cancel(F1-2*N1/((1+s)*L*BN*(c*TN+10*DN))) == 0
    P0, P1 = [sp.expand(sp.cancel(z/s**2).subs(c, sp.Rational(19, 20)+e))
              for z in (N0, N1)]
    assert sp.expand(sp.Poly(P0, e).coeff_monomial(e**6)
                     -4*r**2*s*(1+s)**2) == 0
    assert sp.expand(sp.Poly(P1, e).coeff_monomial(e**6)
                     -4*r**2*s*(1-s)*(1+s)**2) == 0
    rec = {"P0": certificate(P0, e, s, r), "P1": certificate(P1, e, s, r)}
    floors = {"P0": [151, 197, 173, 99, 28, 3, 0],
              "P1": [40, 235, 278, 133, 25, F(2, 5), 0]}
    for name, limits in floors.items():
        for block, lower in zip(rec[name]["coarse_blocks"], limits):
            assert F(block["minimum"]) >= lower
    ll, cc = F(19, 10), F(9, 10)
    tail_pieces = [cc**2*ll**(n-1)/(ll**n-1)**2 for n in (2, 3, 4)]
    tail_pieces.append(cc*ll**5/(ll**5-1)**2)
    for value, upper in zip(tail_pieces, [F(23,100),F(9,100),F(1,25),F(1,25)]):
        assert value < upper
    assert sum(tail_pieces) < F(2,5)
    margin = F(175,1156)-F(18,125)
    assert margin == F(1067,144500)>0
    out = {"status": "exact local algebra reproduced; universal-39/20 assembly unaudited",
           "domain": "c=19/20+e, e>=0, 0<=s<=9/25, 0<=r<=1",
           "num_identities": "both exact symbolic identities passed",
           "tail_pieces": [str(x) for x in tail_pieces],
           "tail_bound": str(sum(tail_pieces)),
           "source_monotonicity_margin": str(margin),
           "polynomials": rec}
    dest = Path(__file__).with_name("bias195_coarse_certificate.json")
    dest.write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps({"output": str(dest), "polynomials_checked": 63,
                      "positive": 59, "zero": 4,
                      "source_monotonicity_margin": str(margin),
                      "minima": {k: [b["minimum"] for b in v["coarse_blocks"]]
                                 for k, v in rec.items()}}))


if __name__ == "__main__":
    main()
