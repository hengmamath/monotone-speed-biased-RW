"""Exact root endpoint SIZE and genuine canonical curvature obstruction.
No full kernel sign or completion of165 is claimed.
"""
import sympy as S
from fractions import Fraction as F

l,u,R,A,K,T,Q,c0,t0=S.symbols('l u R A K T Q c0 t0')
c=l-1; h=c*u/(1-u); d=1-h
be=lambda n:h/(l**n-d)
Ls=lambda n:c*d/(l*(l**n-d))
rr=be(2)/u; H1=1-2*l*Ls(2)
W1=(1+c*R)*(c/l-1)+2*(1+(l+1)*R)*Ls(1)-2*R*(1/l-H1*rr)
C1=A*(1+Ls(1))+R*(c+l*Ls(1)+2*l*Ls(2))
endpoint=-2*R*u*Ls(1)+u*u*W1+2*u*be(2)*C1
formula=(2*A+(1-2*l*u)*(1-R*(2-(l+1)*u)/u))/l
count=0
def eq(name,left,right):
    global count
    assert S.cancel(left-right)==0,name
    count+=1;print('PASS:',name)
eq('COMPLETE actual K0 including ROOT',endpoint/u**2,formula)
eq('ACTUAL endpoint ratio J',
   1-(T/(2*Q-(l+1)*T))*(2-(l+1)*u)/u,
   2*(Q-T/u)/(2*Q-(l+1)*T))
den=2-(l+1)*u*K; Rp=u*K/den
api=((l+1)*(2-K)-2*l*u)/den
eq('COMPLETE pipe endpoint comparison',formula.subs({A:api,R:Rp}),
   2*(2*l+3-4*l*u-K*(l+2-2*l*u))/(l*den))
ll=1+c0; at=ll+2-2*t0
diff=12*ll*(2*at-1)-at*(ll*ll+13*ll+6-(3*ll+7)*t0+2*t0*t0)
eq('WHOLE low-half Euler payment polynomial',diff,
   t0*(22-26*t0+4*t0*t0)+c0*(19+t0-8*t0*t0)
   +c0*c0*(6+5*t0-c0))
eq('COMPLETE cap quotient from T and Q',
   (u*u*K/(1-u))/(2*u/(1-u)-(l+1)*u*u*K/(1-u)),Rp)

# Genuine canonical limit: mu_K=(43/60)delta1+(17/60)deltaK.
lam=F(21,20); uu=F(17,20); cc=lam-1
hh=cc*uu/(1-uu);dd=1-hh; N=160
beta=lambda n:hh/(lam**n-dd)
kapN=(1-uu)*sum((lam**(n-1)*beta(n)**2/uu**2 for n in range(1,N+1)),F(0))
x=lam**(-N-1)
kapTail=cc/(1-uu)*x/(1-dd*x)**2
speed=lambda kap:uu*kap/(2-(lam+1)*uu*kap)
assert 2-(lam+1)*uu*(kapN+kapTail)>0
assert speed(kapN)>5
assert speed(kapN+kapTail)<F(28,5)
print('PASS: exact160 prefix + ENTIRE tail => 5<Rcap<28/5')
assert (F(157420)-F(5289)*F(28,5))/136000>F(9,10)
assert (F(157420)-F(5289)*5)/136000<1
print('PASS: actual canonical boundary is HARD, 9/10<alpha<1')

lv=S.Rational(21,20);uv=S.Rational(17,20);cv=lv-1
hv=cv*uv/(1-uv);dv=1-hv
bb=lambda n:hv/(lv**n-dv)
LL=lambda n:cv*dv/(lv*(lv**n-dv))
k=S.symbols('k'); a0=1-(lv+1)*uv+lv*bb(2)
alpha=(uv-R*a0)/bb(2)
aa=[];bz=[]
for n in (2,3):
    rat=bb(n+1)/bb(n); Hn=n-(n+1)*lv*LL(n+1)
    W=(1+cv*R)*(cv*n/lv-1)+2*(1+(lv+1)*R)*n*LL(n)-2*R*(n/lv-Hn*rat)
    Cn=alpha*(1+LL(n))+R*(cv+lv*LL(n)+S.Rational(n+1,n)*lv*LL(n+1))
    tp=-R*bb(n-1)+(1+(lv+1)*R)*bb(n)-(alpha+lv*R)*bb(n+1)
    aa.append(lv**(n-1)*bb(n)**2*W/uv**2)
    bz.append(2*n*lv**(n-1)*bb(n+1)*
              (bb(n)*Cn+lv*k*(1-S.Rational(1,2*n))*(1+LL(n))*tp)/uv**2)
psi=40*(612786583359429443433*R*k+67056257313893314158*R
       -1111014301942994947470*k+11993158935550613404760)/1034283120293591470077493
eq('EXACT signed Psi2/u^2 INCLUDING complete Theta coefficient',aa[1]+bz[1]-bz[0],psi)
eq('EXACT complete canonical boundary calibration',alpha,(157420-5289*R)/136000)
assert psi.subs({R:5,k:S.Rational(20,21)})>S.Rational(1,2)
assert 612786583359429443433*5-1111014301942994947470>0
print('PASS: k>20/21, R>5 => Psi2/u^2>1/2 EXACTLY')
print(count,'generic identities PASS; exact whole-tail rational signs PASS.')
print('Root endpoint SIZE verified; global concavity is a METHOD obstruction.')
print('The full actual energy inequality165 remains OPEN.')
