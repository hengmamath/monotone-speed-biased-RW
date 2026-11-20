"""PACK A: common COMPLETE-priced kernel lines; one global Kb, no grids.
Hand range proofs accompany seven small univariate identities.
"""
import sys
import sympy as S
from fractions import Fraction as F
assert sys.flags.optimize==0
c,h=S.symbols('c h');l=c+1;k=1-h;u=h/l;t=1-u
K0=(l*l+26*l+13)/(24*l);k1=(3*l*l+16*l+1)/(24*l);k2=(l+1)/12
K=K0-k1*u+k2*u*u;r=(l+5)/8;Kline=K0-r*u
assert S.cancel(Kline-K-k2*u*(1/(2*l)-u))==0
qline=u*Kline;a=1/(l+1);b=(l+1)/(l*l+l+1);d=1/l
# X denominator upper quadratic: leftover = h^3 ab[-2(a+b)+ab h] <=0.
D=(1-a*h)**2*(1-b*h)**2;d1=2*(a+b);d2=a*a+4*a*b+b*b
assert S.cancel(D-(1-d1*h+d2*h*h)-h**3*a*b*(-2*(a+b)+a*b*h))==0
p0=d1+d-1-K0/l;p1=K0/l+r/l**2-d2-d*d1;p2=d*d2-r/l**2
assert S.cancel(k*(1-qline)-t*(1-d1*h+d2*h*h)-h*(p0+p1*h+p2*h*h))==0
sx=(c+1)**2*(c+2)**2*(c*c+3*c+3)**2
N1=-98*c**8-745*c**7-2214*c**6-2863*c**5-338*c**4+3387*c**3+3726*c*c+1356*c+48
N2=-c**8-38*c**7-123*c**6+358*c**5+2747*c**4+6288*c**3+6876*c*c+3480*c+576
N3=-c**7-16*c**6-55*c**5+24*c**4+503*c**3+1134*c*c+1068*c+368
assert S.cancel(p0+p1/2+p2/4-N1/(96*sx))==0
assert S.cancel(-p1-p2-N2/(24*sx))==0
assert S.cancel(p2-N3/(8*sx))==0
assert 3387-(98*F(1,32)+745*F(1,16)+2214*F(1,8)+2863*F(1,4)+338*F(1,2))>0
assert 358-(F(1,8)+38*F(1,4)+123*F(1,2))>0
assert 503-(F(1,16)+16*F(1,8)+55*F(1,4))>0
print('PASS common X line: priced X_s >= (1-u)X_s(0), all s>=2, 0<c<=1/2')
# Y denominator exact, coefficient pairs over h in [0,1/2].
y1=3*a+b;y2=3*a*a+3*a*b;y3=a**3+3*a*a*b;y4=a**3*b
C0=K0*(l+1)**2/(2*l*l);C1=r*(l+1)**2/(2*l**3)
M0=y1+d-C0;M1=d*C0+C0*a+C1-y2-2*d*y1
M2=y3+2*d*y2-d*(C0*a+C1)-C1*a
M3=d*C1*a-y4-2*d*y3;M4=2*d*y4
YN=t*(1-h*(C0-C1*h)*(1-a*h))-(1-2*u)*(1-a*h)**3*(1-b*h)
assert S.cancel(YN-h*(M0+M1*h+M2*h*h+M3*h**3+M4*h**4))==0
G0=-c**7-37*c**6-85*c**5+190*c**4+916*c**3+1144*c*c+432*c-48
G1=-2*c**9-75*c**8-265*c**7+213*c**6+2624*c**5+5260*c**4+4316*c**3+1144*c*c-96*c+48
G2=-7*c**8-150*c**7-486*c**6+731*c**5+6606*c**4+13752*c**3+12656*c*c+4704*c+240
G3=-14*c**8-297*c**7-921*c**6+1381*c**5+11634*c**4+22776*c**3+19264*c*c+5952*c-192
common=c*c+3*c+3
assert S.cancel(M0-G0/(48*(c+1)**3*(c+2)*common))==0
assert S.cancel(M0+M1/2-G1/(96*(c+1)**4*(c+2)**2*common))==0
assert S.cancel(M2-G2/(48*(c+1)**4*(c+2)**3*common))==0
assert S.cancel(M2+M3/2-G3/(96*(c+1)**4*(c+2)**3*common))==0
assert 190-(F(1,8)+37*F(1,4)+85*F(1,2))>0 and 432*F(3,20)-48>0
assert 213-(2*F(1,8)+75*F(1,4)+265*F(1,2))>0
assert 48-96*F(1,2)==0
assert 731-(7*F(1,8)+150*F(1,4)+486*F(1,2))>0
assert 1381-(14*F(1,8)+297*F(1,4)+921*F(1,2))>0 and 5952*F(3,20)-192>0
print('PASS common Y line: priced Y_s >= (1-2u)Y_s(0), all s>=2, 3/20<=c<=1/2')
print('Every original X/Y price retained. Geometry transfers second-age ratios to every age.')
