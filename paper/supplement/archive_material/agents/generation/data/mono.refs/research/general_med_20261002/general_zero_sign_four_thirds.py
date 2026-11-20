"""Exact algebra for the direct tilted-mean >=4/3 zero-sign proof.
This verifies identities/endpoints; probabilistic assembly is in the note.
"""
import sympy as S
n, lam, K, v, alpha, b, z = S.symbols('n lam K v alpha b z')
v0=1/(lam+1); A0=3+v0
d=(2-n)*(2*n-lam)/n; a=A0*(n-lam)/2
assert S.factor(2-lam-2*(n-1)*(n-lam)/n-d)==0
delta=(lam+1)*v-(lam-1)-(3+v)*(n-lam)/(2*K)-2*(n-1)*(n-lam)/n
assert S.factor(delta.subs(v,v0)-(d-a/K))==0
q=(alpha*v-b)**2/(v*(3+v))
assert S.factor(S.diff(S.log(q),v)
    -(3*alpha*v+3*b+2*b*v)/(v*(3+v)*(alpha*v-b)))==0
assert S.factor(S.Rational(4,27)-z*(1-z)**2
                -(z-S.Rational(1,3))**2*(S.Rational(4,3)-z))==0
T=8*(2-n)**2*(2*n-lam)**3*(lam+1)**3/(27*(3*lam+4)**2*lam**2*n*(n-1)*(n-lam))
ratio=(8*d**3/(27*a*(2-n)))/(2*A0*v0*lam**2*(n-1)/n**2)
assert S.factor(T-ratio)==0
dn=-2/(2-n)+6/(2*n-lam)-1/n-1/(n-1)-1/(n-lam)
assert S.factor(S.diff(S.log(T),n)-dn)==0
dll=(-3/(2*n-lam)**2-3/(lam+1)**2+18/(3*lam+4)**2
      +2/lam**2+1/(n-lam)**2)
assert S.factor(S.diff(S.log(T),lam,2)-dll)==0
edge=8*(2-lam**2)**2*(2*lam-1)**3*(lam+1)**2/(27*(3*lam+4)**2*lam**2*(lam-1)**2)
assert S.factor(T.subs(n,lam**2)-edge)==0
de=(-4*lam/(2-lam**2)+6/(2*lam-1)+2/(lam+1)
    -6/(3*lam+4)-2/lam-2/(lam-1))
assert S.factor(S.diff(S.log(edge),lam)-de)==0
assert S.factor(2/lam+2/(lam-1)-6/(2*lam-1)
    -2*(lam**2-lam+1)/(lam*(lam-1)*(2*lam-1)))==0
for lv, expected in [(S.Integer(1),S.Rational(8000,11907)),
                     (S.Rational(7,6),S.Rational(8788,11025))]:
    got=S.factor(T.subs({n:S.Rational(4,3),lam:lv}))
    assert got==expected
    print('Endpoint',lv,'ratio',got,'positive gap',1-got)
print('Ten full symbolic identities and two exact endpoint ratios passed.')
