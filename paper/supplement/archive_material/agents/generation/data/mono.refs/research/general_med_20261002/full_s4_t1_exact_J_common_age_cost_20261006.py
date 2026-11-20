"""PACK B: exact root chord slope pays common age cost, one quartic.
Taylor bounds follow complete monotonicity; no grids/LP/old certificate imports.
"""
import sys
import sympy as S
from fractions import Fraction as F
assert sys.flags.optimize==0
j,x=S.symbols('j x');l=(1+j)/(1-j)
R=[None,1,2,3+j*j,4*(1+j*j),5+10*j*j+j**4]
for s in (1,2,3,4,5):
 assert S.cancel(sum(l**v for v in range(s))-R[s]/(1-j)**(s-1))==0
fX=[1/(1+x/3)**2,(1-x)/((1+x/3)**2*(1+x)**2),(1-x)**2/((1+x)**2*(1+2*x+x*x/5)**2)]
fY=[(1-x)**2/(1+x/3),(1-x)**4/((1+x/3)**3*(1+x)),(1-x)**6/((1+x)**3*(1+2*x+x*x/5))]
TX=[1-S.Rational(2,3)*x+S.Rational(1,3)*x*x,1-S.Rational(11,3)*x+S.Rational(22,3)*x*x,1-8*x+S.Rational(178,5)*x*x]
TY=[1-S.Rational(7,3)*x+S.Rational(16,9)*x*x,1-6*x+S.Rational(50,3)*x*x,1-11*x+S.Rational(304,5)*x*x]
wx=[S.Rational(1,9),S.Rational(1,24),S.Rational(1,50)]
wy=[S.Rational(2,3),S.Rational(2,9),S.Rational(1,10)]
for i,s in enumerate((2,3,4)):
 for fun,tay in ((fX[i],TX[i]),(fY[i],TY[i])):
  assert S.expand(sum(S.diff(fun,x,n).subs(x,0)*x**n/S.factorial(n) for n in (0,1,2))-tay)==0
 # Exact baseline kernels; 2Y is included in wy.
 X0=2*s*(1+j)**(s-2)*(1-j)**(3*s)/(R[s]**2*R[s+1]**2)
 Y0=4*s*(1-j*j)**(2*s-2)*(1-j)/(R[s]**3*R[s+1])
 assert S.cancel(X0-wx[i]*(1-j)**(2*s+2)*fX[i].subs(x,j*j))==0
 assert S.cancel(2*Y0-wy[i]*(1-j)*fY[i].subs(x,j*j))==0
print('PASS six exact baseline kernels and quadratic Taylor coefficients')
# All f are completely monotone on x in [0,1/25]: factors (1-x)^p and (1+alpha*x)^(-q), alpha>0.
# 1+2x+x^2/5=(1+(1+2/sqrt(5))*x)(1+(1-2/sqrt(5))*x).
U=lambda n:sum((-1)**v*S.binomial(n,v)*j**v for v in range(5))
Cup=sum(wx[i]*U(2*s+2)*TX[i].subs(x,j*j)+wy[i]*(1-j)*TY[i].subs(x,j*j) for i,s in enumerate((2,3,4)))
J=-(6*j**5+54*j**4-18*j**3-87*j*j+62*j-65)/(6*(1+j)*(3+j)**2)
J4=S.Rational(65,54)-S.Rational(511,162)*j+S.Rational(961,162)*j*j-S.Rational(10547,1458)*j**3+S.Rational(29713,4374)*j**4
rem=29713*j*j+176350*j+254529
assert S.cancel(J-J4+j**5*rem/(4374*(1+j)*(3+j)**2))==0
assert S.expand(7*4374*(1+j)*(3+j)**2-rem-(30618*j**3+184613*j*j+282920*j+21033))==0
Q=J4-7*j**5-Cup
coeff=[F(227,5400),-F(391,405),F(106507,16200),-F(27461,3645),-F(389513,273375),-F(418,27),F(3829,900),F(69722,675),-F(77159,450)]
assert S.expand(Q-sum(S.Rational(v.numerator,v.denominator)*j**n for n,v in enumerate(coeff)))==0
Lcoef=coeff[:4]+[coeff[4]+coeff[5]/5+coeff[8]/625]
assert Lcoef[4]==-F(1310961548,273375000)
# Q>=L on 0<=j<=1/5: discard positive j^6,j^7; bound negative j^5,j^8 by j^4/5,j^4/625.
point=F(1,10)
value=sum(v*point**n for n,v in enumerate(Lcoef))
der=sum(n*Lcoef[n]*point**(n-1) for n in range(1,5))
curv=2*Lcoef[2]+6*Lcoef[3]/5+12*Lcoef[4]/25
assert curv==F(2057748779,1139062500)>F(9,5)
margin=value-F(5,18)*der*der
assert margin==F(863242661658907799,4203781347656250000000)>F(1,5000)
print('PASS quartic strong-convexity certificate: J-sum(X0+2Y0)>1/5000')
print('With PACK A and audited root chord/zero-u anchor: full T=1 S4(Kcap)>0; full T remains OPEN')
