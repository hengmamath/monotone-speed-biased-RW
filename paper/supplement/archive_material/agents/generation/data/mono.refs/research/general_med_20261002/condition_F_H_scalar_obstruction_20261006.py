"""One exact scalar obstruction to H; no GW realization or theorem reversal.
No parameter scan, old certificate replay, or numerical root calculation.
"""
from fractions import Fraction as F
import sys
import sympy as S
assert sys.flags.optimize == 0

# Shared-E elimination, as a generic rational identity.
l, u, z, E = S.symbols('l u z E')
d = 1-u; A = 1+l*d; B = 1+l*(l+1)*d; r2 = A/B
R = 1+A*A*E*z*z
Df = 1+2*l*u*z+(2*A*u/d-A*A*E)*z*z
Dw = 2-(l+1)*u+2*l*u*z+(2*A*u/d-(l+1)*u*A*A*E)*z*z
A0 = 1-(l+1)*u+l*u*z
C = Df*(1-r2)-u*R*(1-z)
Ba = (1-z)*Dw-R*A0
Q2 = u+l*u*u*z+A*u*u*z*z/d
f = 1-u*z; g = 1-r2+u-u*z
L = (1+u-d*r2)*z-u*(1+z*z)
assert S.cancel(S.together(f*C-g*Ba-2*Q2*L/u)) == 0
print('PASS generic shared-E elimination identity')

def cap(l, u):
    c = l-1; t = c/(l+1)
    lo = 2*(t+t**3/3+t**5/5)
    hi = lo+2*t**7/(7*(1-t*t))
    return c/(l*lo)+(1-u)/2+hi*(l+1-2*l*u)*(1-u)/(12*c)

def fiber(l, u, z):
    c = l-1; d = 1-u; A = 1+l*d; B = 1+l*(l+1)*d
    r1 = 1/A; r2 = A/B; r3 = B/(1+l*(l+1+l*l)*d)
    K = cap(l,u); E = (K-d)/d; R = 1+A*A*E*z*z
    Df = 1+2*l*u*z+(2*A*u/d-A*A*E)*z*z
    Dw = 2-(l+1)*u+2*l*u*z+(2*A*u/d-(l+1)*u*A*A*E)*z*z
    A0 = 1-(l+1)*u+l*u*z
    w = c*u*R/Dw; a = (1-R*A0/Dw)/z
    C = Df*(1-r2)-u*R*(1-z)
    Ba = (1-z)*Dw-R*A0
    L = (1+u-d*r2)*z-u*(1+z*z)
    Q2 = u+l*u*u*z+A*u*u*z*z/d
    f = 1-u*z; g = 1-r2+u-u*z
    assert f*C-g*Ba == 2*(1+l*u*z+A*u*z*z/d)*L
    assert a-1 == Ba/(z*Dw)
    M2 = a*(1-r2)+(w/c)*(l+1-l*r2-1/z)
    assert M2 == C/(z*Dw)
    return locals()

# Previously audited actual rare-reset limit: lambda=6/5,
# rho=(149/150)delta_1+(1/150)delta_4, mean r=51/50,
# mu_(epsilon,K)=(1-epsilon)rho+epsilon delta_K; K->infty then epsilon->0.
# Only its inherited limit u->0, z->3/7 is evaluated here.
l0 = F(6,5); r0 = F(51,50); z0 = F(3,7)
assert (l0-r0)/(l0*l0-r0) == z0
q0 = fiber(l0,F(0),z0)
assert F(0) < q0['a'] < 1
assert q0['Ba'] < 0 < q0['C']
assert 1 < q0['K'] < 2
print('PASS inherited actual rare-reset limit: Ba<0<C')

# One rational fiber, with its two allowed z-boundaries.
l = F(231,200); u = F(15,32); z = F(1119,2000)
p = fiber(l,u,z)
assert p['K'] == F(3457424725884287519117405799752531,
                  2785901859006689236658814937497600)
assert F(1241043,1000000) < p['K'] < F(1241044,1000000)
assert p['L'] == -F(18915010971,76096947200000)
assert 3*l*l > 4 and l < F(707,500)
assert 0 < u < 1/(l*l) and u < z < p['r1']
assert 1 < p['K'] < 2/(1+l*u) and (1-u)*p['K'] < 2
assert p['Df'] > 0 and p['Dw'] > 0 and 0 < u*p['R']/p['Df'] < 1
assert 0 < p['w'] < (l-1)*u/(1-u)
assert l*l*u < p['a'] < 1 and p['a'] > F(999,1000)
assert p['f'] > 0 and p['g'] > 0 and p['Q2'] > 0
assert p['Ba'] < -F(1,2000)
assert p['L'] < -F(1,5000)
assert p['C'] < -F(1,1000)
assert p['M2'] < -F(1,500)
left = fiber(l,u,u); right = fiber(l,u,p['r1'])
assert left['Ba'] > 0
assert right['Ba'] < 0 < right['C']
print('PASS z-boundaries: Ba(u)>0; Ba(r1)<0<C(r1)')
print('PASS strict scalar point: lambda=231/200, u=15/32, z=1119/2000')
print('PASS exact K in (1241043/1000000,1241044/1000000); L=-18915010971/76096947200000')
print('PASS Ba<-1/2000, L<-1/5000, C<-1/1000, M2<-1/500, 999/1000<a<1')

def gram(theta):
    return theta*theta-(2*u+p['r3'])*theta+p['r3']*u*theta/z+u*z

def entry(theta):
    return p['Df']*(1-theta)-u*p['R']*(1-z)

good = F(13,20); bad = p['r2']-F(1,1000000)
assert z < good < p['r2'] and gram(good) < -F(1,500)
assert entry(good) > F(3,50)
assert z < bad < p['r2'] and gram(bad) > F(1,100)
assert entry(bad) < -F(1,1000)
print('PASS Gram guard: theta=13/20 gives G<-1/500 and J2 entry>3/50')
print('PASS ratio-only negative J2 witness violates Gram: G>1/100')
print('H scalar covering route stopped; actual GW H and original F not refuted')
