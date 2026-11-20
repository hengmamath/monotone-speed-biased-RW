"""244--247 local exact checks. Independent audit pending; full proofs separate."""
import sympy as S
from fractions import Fraction as F
t,h=S.symbols('t h')
A=S.Rational(217,25);B=S.Rational(183,25);end=A/B
G=t*(A-B*t)*(1+t/2)/(3*(1+t)**3)
gp=(2*A-(2*A+4*B)*t-(A+B)*t*t)/(6*(1+t)**4)
gpp=(-10*A-4*B+(4*A+10*B)*t+2*(A+B)*t*t)/(6*(1+t)**5)
assert S.cancel(S.diff(G,t)-gp)==0 and S.cancel(S.diff(G,t,2)-gpp)==0
assert A+B==16 and 1<end<2 and 2*B>A
assert S.cancel(G.subs(t,0))==0 and S.cancel(G.subs(t,end))==0
assert gp.subs(t,end)<0 and gp.subs(t,0)==S.Rational(217,75)
positive=6*(1+t)**4+2*A-(2*A+4*B)*t-(A+B)*t*t
expected=S.Rational(584,25)-S.Rational(566,25)*t+20*t*t+24*t**3+6*t**4
assert S.expand(positive-expected)==0
disc=S.Rational(566,25)**2-4*S.Rational(584,25)*20
assert disc==-S.Rational(847644,625) and disc<0
assert S.Rational(217,75)+2<S.Integer(5)
primitive=S.Rational(1,6)*(16*S.log(1+t)-B*(1+t)+8/(1+t)**2-B/(1+t))
assert S.cancel(S.diff(primitive,t)-G)==0
exactI=S.Rational(8,3)*S.log(16/B)-4+B/3-B*B/192
assert S.simplify(primitive.subs(t,end)-primitive.subs(t,0)-exactI)==0
print('244--245 complete weighted head/derivative/integral identities PASS')
s=F(217,583)
logup=2*(s+s**3/3+s**5/(5*(1-s*s)))
Iup=F(8,3)*logup-4+F(183,25)/3-F(183,25)**2/192
C=Iup+F(1,160)
assert C==F(122243248244149,483498900280000) and C>F(1,12)
omega=F(9,5)
Jup=F(11,10)**4/(12*omega**3)+F(11,10)**2/(12*omega*100)
assert Jup==F(187913,8748000)
print('246 COMPLETE quadratic normalized charge',Jup,'PASS')
f=(1-h)*(2*h+1)/6;p=1-2*h
budget=f-S.Rational(1,25)-p*S.Rational(C.numerator,C.denominator)-p*p*S.Rational(Jup.numerator,Jup.denominator)
assert S.cancel(S.diff(budget,h)-((1-4*h)/6+2*S.Rational(C.numerator,C.denominator)+4*p*S.Rational(Jup.numerator,Jup.denominator)))==0
assert 2*C-F(1,6)>0
margin=F(3,16)-F(1,25)-C/2-Jup/4
assert margin==F(16616808991576441,1057412094912360000) and margin>F(1,100)
assert budget.subs(h,S.Rational(1,4))==S.Rational(margin.numerator,margin.denominator)
print('247 WHOLE q>=10,h>=1/4 budget',margin,'>1/100 PASS')
print('All new exact checks PASS. Independent audit pending; general med still OPEN.')
