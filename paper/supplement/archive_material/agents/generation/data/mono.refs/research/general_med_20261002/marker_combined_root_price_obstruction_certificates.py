"""Exact ENTIRE combined defect-root price obstruction at canonical boundary.
Integer rational grid encloses every prefix term; NO floating-point signs.
"""
from fractions import Fraction as F
l=F(21,20);u=F(17,20);c=l-1;h=c*u/(1-u);d=1-h
N=160;grid=10**15
beta=lambda n:h/(l**n-d)
Ls=lambda n:c*d/(l*(l**n-d))
def W0(n):return c*n/l-1+2*n*Ls(n)
def Wp(n):
    H=n-(n+1)*l*Ls(n+1);r=beta(n+1)/beta(n)
    return c*W0(n)+2*(2*n*Ls(n)-F(n)/l+H*r)
def enclose(terms):
    zz=list(terms)
    lower=sum((q.numerator*grid//q.denominator for q in zz),0)
    return F(lower,grid),F(lower+len(zz),grid)
wt=lambda n:l**(n-1)*beta(n)**2
Tlo,Thi=enclose(wt(n) for n in range(1,N+1))
S0lo,S0hi=enclose(wt(n)*W0(n) for n in range(1,N+1))
S1lo,S1hi=enclose(wt(n)*Wp(n) for n in range(1,N+1))
q=1/l;x=q**(N+1)
Ttail=h*h/c*x/(1-d*x)**2
Jtail=h*h/l*x*((N+1)-N*q)/((1-q)**2*(1-d*x)**2)
Ltail=Ls(N+1)
# For EVERY n>N: W0>0, Wp>0 by the manuscript inequalities.
assert c*(N+1)/l-1>0
assert c*c*(N+1)/l-c>0
assert (N+1)*(l+1-2/l)-1/l>0
Thi+=Ttail
S0hi+=(c/l+2*Ltail)*Jtail
S1hi+=(c*c/l+2*(c+2)*Ltail)*Jtail
Qp=h/c
Zlo=2*Qp-(l+1)*Thi;Zhi=2*Qp-(l+1)*Tlo
assert Zlo>0
Rp=lambda tt:tt/(2*Qp-(l+1)*tt)
Rlo,Rhi=Rp(Tlo),Rp(Thi)
b2=beta(2);A0=1-(l+1)*u+l*b2
alpha=lambda R:(u-R*A0)/b2
K0=lambda R:u*u/l*(2*alpha(R)+(1-2*l*u)*(1-R*(2-(l+1)*u)/u))
assert K0(1)-K0(0)>0
Bhi=2*u*Ls(1)-S1lo;Blo=2*u*Ls(1)-S1hi
assert Blo>0
Cs_hi=2*Qp*Bhi/(Zlo*Zlo)
Vhi=(2-u-b2)*Thi-2*u*u
assert Vhi>0
assert S1lo-u*u*Wp(1)>0
TailKlo=S0lo-u*u*W0(1)+Rlo*(S1lo-u*u*Wp(1))
D1upper=(K0(Rhi)+Cs_hi*Vhi-TailKlo)/(u*u)
assert D1upper<-F(1,4)
print('PASS: exact160 prefix + ALL T/S0/S1 tails => D1/u^2<-1/4')
assert alpha(Rhi)>F(9,10) and alpha(Rlo)<1
print('PASS: same genuine canonical boundary HARD, 9/10<alpha<1')
print('Per-defect combined root-price positivity is TOO STRONG;165 OPEN.')
