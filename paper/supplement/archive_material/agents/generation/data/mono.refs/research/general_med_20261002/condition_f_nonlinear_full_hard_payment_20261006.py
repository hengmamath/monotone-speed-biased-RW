#!/usr/bin/env python3
"""Fixed identities only; all inequalities have manual proofs in the note."""
import sympy as s

l, u, z, K, v = s.symbols('l u z K v')
c, d = l - 1, 1 - u
A, B = 1 + l*d, 1 + l*(l + 1)*d
Q = 2 + 2*l*u*z + 2*A*u*z*z/d
R = 1 + A*A*(K - d)*z*z/d
M = l + (l + 1)*u - l*u*z
W = l*Q - M*R
KT = 2*l*A/(l*A + u*B)
P0, P1, P2 = l - (l + 1)*u, l*u*(2*l + 1), 2*l*A*u/d
M0 = l + (l + 1)*u
critical = d + d*(P0 + P1*z + P2*z*z)/(A*A*z*z*M)
h0 = 2*((l + 1)**2*u*u - l*l)
h1 = -2*l*u*(l*c + (l + 1)*(l + 2)*u)
h2, h3 = 2*l*l*u*u*(2*l + 1), 2*l*l*A*u*u/d
H = h0 + h1*z + h2*z*z + h3*z**3


def eq(x, y):
    assert s.cancel(x - y) == 0


eq(W, A*A*z*z*M*(critical - K)/d)
eq(critical.subs(z, 1/A), KT)
eq(s.diff(critical, z), d*H/(A*A*z**3*M*M))
C = (l + 1)*(l + 2) - l*((2*l + 1) + 1/d)/A
Clo = (9*l**3 + 3*l*l + 2*l + 48)/(24 + 9*l)
eq(C.subs(u, s.Rational(5, 8)), Clo)
eq(Clo - s.Rational(15, 8),
   (72*l**3 + 24*l*l - 119*l + 24)/(24*(3*l + 8)))
F = l*l + u*u*(l**3 - 2*l*l - 2*l - 1 + s.Rational(15, 8)*l*u)
eq(h0 - 2*l*u*u*(l*c + s.Rational(15, 8)*u), -2*F)
eq(s.diff(F, l), 2*l + u*u*(3*l*l - 4*l - 2 + s.Rational(15, 8)*u))
eq(s.diff(F, u)/u, 2*(l**3 - 2*l*l - 2*l - 1) + s.Rational(45, 8)*l*u)
eq(F.subs({l: s.Rational(9, 8), u: s.Rational(5, 8)}), s.Rational(643, 8192))
print('PASS: original-K threshold identities and lower-u manual derivative bound.')

eq(2*R - K*Q, 2*(1 - A*z)*((1 - K) + (A - (l + 1)*K)*z))
zh = l*u/(1 + c*u)
P = l + (l*l + 1)*u - u*u
eq(M.subs(z, zh), P/(1 + c*u))
print('PASS: ratio factor and exact hard-interval endpoint M(zh).')

Kbar = (l + 1)/(2*l) - c*c/(6*l*(l + 1)) + d/2 + (
    (l*l + 10*l + 1)*(l + 1 - 2*l*u)*d/(72*l*(l + 1)))
Dcap = 72*l*(l + 1)
kn = ((2*l**3 + 20*l*l + 2*l)*u*u
      - (3*l**3 + 67*l*l + 49*l + 1)*u
      + l**3 + 71*l*l + 143*l + 25)
eq(Kbar*Dcap, kn)
G = 2*l*(1 + c*u)*Dcap - kn*P
p = 40*l**5 + 45744*l**4 + 24823*l**3 - 56694*l*l - 34745*l - 3900
q = 26*l**5 + 8564*l**4 - 2688*l**3 - 6539*l*l + 2572*l + 405
g0, g1 = 3*p/2048, q/64
g2 = (-12*l**5 + 440*l**4 + 393*l**3 + 332*l*l + 1617*l + 386)/16
g3 = -2*l**5 - 20*l**4 - 2*l**3 - 37*l*l - 46*l - 1
g4 = 2*l*(l*l + 10*l + 1)
eq(G.subs(u, v + s.Rational(5, 8)), g0 + g1*v + g2*v*v + g3*v**3 + g4*v**4)
eq(g2 + g3/8, (-16*l**5 + 400*l**4 + 389*l**3 + 258*l*l + 1525*l + 384)/16)
eq(s.diff(p, l), 200*l**4 + 74469*l*l + 182976*l*(l*l - 1) + 69588*l - 34745)
assert s.simplify(p.subs(l, 2/s.sqrt(3)) - (16476 - 28378/s.sqrt(3))/9) == 0
assert 3*16476**2 - 28378**2 == 9064844 > 0
print('PASS: five-term Kbar budget identity and constant-term positive base arithmetic.')
print('No parameter scan, coefficient table, old certificate rerun, or S42 floor conclusion.')
