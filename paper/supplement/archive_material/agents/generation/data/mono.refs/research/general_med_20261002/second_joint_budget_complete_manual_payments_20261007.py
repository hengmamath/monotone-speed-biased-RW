"""LOCAL complete J2. Explicit identities + manual range bounds, no sign tables.
No J3 dependency, old imports, grid, LP or large certificate.
"""
import sympy as s
l,A,rho,c,x,y=s.symbols('l A rho c x y')
a=s.Rational(5,6)
t,u,k=(A-1)/l,(l+1-A)/l,A-l
K=(l+1)/(2*l)+t/2+(l+1)*(2*l*t-l+1)*t/(24*l)
h=K-t
Q=A*t+l*u*rho*t+u*rho**2
R=t+rho**2*h
root=2*(1-l*rho/A)/l*(Q*(2*A-rho-l*rho**2/A)-A*R*(A-l*u*rho**2/A))
CR=-s.diff(root,rho).subs(rho,1)
Z3=1+(A-1)*(1+l)
Z4=Z3+(A-1)*l*l
r2,r3=A/Z3,Z3/Z4
F2,F3=2-r2-l*r2*r2,2-r3-l*r3*r3
L2=(144*K-84*t)/11
L3=(3152*K-2054*t)/297
lower2=2/A**2*(-F2*(18+6*u*(l*t+2)/A)+u*A*L2)
lower3=3*l/Z3**3*(-F3*(s.Rational(46,3)*A+u*(282*l*t+544)/27)+u*Z3*L3)

# Original complete age expression, with generic n and tau.
lf,uf,Kf,Ff,rf,pf,of,nf,tau=s.symbols('lf uf Kf Ff rf pf of nf tau')
tf=1-uf;Af=1+lf*tf;hf=Kf-tf
Qf=Af*tf+lf*uf*rho*tf+uf*rho**2
Rf=tf+rho**2*hf
Uf=of*(Qf*Ff+uf*Af*Rf*lf*rf**2)
Vf=of*uf*Af*Rf/pf
Cs=2*((nf+1)*Vf+s.diff(Vf,rho)-(2*nf+1)*Uf-s.diff(Uf,rho)).subs(rho,1)
actual=3*Cs+tau*(2*Uf-Vf).subs(rho,a)
Ra=tf+a*a*hf
qa=Qf.subs(rho,a)/Af
G=2*tau*qa-6*(2*nf+1+uf*(lf*tf+2)/Af)
E=6*(nf+1)*Kf+12*hf-tau*Ra
T=2*tau*Ra-6*(2*nf+1)*Kf-12*hf
assert s.cancel(pf*(actual-of*Af*(Ff*G+uf/pf*(E+lf*rf*rf*pf*T))))==0
for n,tt,gamma,Lexpected in (
    (1,0,s.Rational(4,11),(144*Kf-84*tf)/11),
    (3,s.Rational(40,3),s.Rational(5,11),(3152*Kf-2054*tf)/297),
    (6,45,s.Rational(7,13),(413*Kf-233*tf)/52)):
    assert s.expand((E+gamma*T).subs({nf:n,tau:tt})-Lexpected)==0

# Analytic adjacent-ratio monotonicity needs only these three mean bounds.
means=(s.Rational(3,5),s.Rational(24,19),s.Rational(129,65))
for j,m in zip((2,3,4),means):
    assert (j-m)/(j+2)>s.Rational(1,3)
lv=s.Rational(23,20)
Zh={j:1+s.Rational(1,2)*sum(lv**i for i in range(1,j)) for j in range(1,6)}
for j,gamma in ((2,s.Rational(4,11)),(3,s.Rational(5,11)),(4,s.Rational(7,13))):
    assert lv*Zh[j]*Zh[j-1]/Zh[j+1]**2<gamma
uv=s.symbols('uv');tv=1-uv
K32=s.Rational(5,6)+tv/2+s.Rational(5,72)*(3*tv-s.Rational(1,2))*tv
assert s.expand(K32-s.Rational(3,2)*tv-(1+89*uv+30*uv**2)/144)==0

# Complete root + complete second-age LOWER comparison >4k.
W=561*c**10+7489*c**9+58103*c**8+280293*c**7+803001*c**6 \
  +1335171*c**5+1180965*c**4+403543*c**3-108838*c*c-75360*c+34944
P1=-22*c**11+5177*c**10+69907*c**9+468159*c**8+1820899*c**7 \
   +4183893*c**6+5457849*c**5+3398021*c**4-126921*c**3-1173234*c*c+4976*c+346080
P2=-143*c**10+8414*c**9+108383*c**8+574844*c**7+1546107*c**6 \
   +2028654*c**5+693193*c**4-1100232*c**3-421092*c*c+1401696*c+993136
P3=-385*c**9+3989*c**8+58830*c**7+226994*c**6+330527*c**5 \
   +133801*c**4+404656*c**3+2005320*c*c+2970740*c+1406136
P4=-539*l**8+768*l**7-2286*l**6-4872*l**5+121073*l**4 \
   +305728*l**3+384440*l*l+219768*l+12912
P5=-385*l**7-1388*l**6+2752*l**5+45030*l**4+125857*l**3+172970*l*l+102284*l+8760
P6=-77*l**6+524*l**5+9498*l**4+33212*l**3+50599*l*l+30616*l+3804
B=[3*l*W.subs(c,l-1)/64,3*P1.subs(c,l-1)/64,3*P2.subs(c,l-1)/32,
   3*P3.subs(c,l-1)/16,3*P4/8,3*P5/4,3*P6/2,
   3*(l+1)*(77*l**4+1077*l**3+4169*l*l+4687*l+1034),
   6*(l+1)**2*(55*l*l+304*l+161),132*(l+1)**3]
N=sum(B[i]*(A-1-l/2)**i for i in range(10))
assert s.cancel(132*A**3*l**3*k*Z3**2*(3*CR/k+lower2-4)-N)==0
assert 34944-s.Rational(75360,4)-s.Rational(108838,16)>0
q=s.Rational(403543,4)+s.Rational(1180965,16)-108838
assert q>0 and 34944-s.Rational(75360)**2/(4*q)>0
assert 346080-s.Rational(1173234,4)-s.Rational(126921,8)-s.Rational(22,2048)>0
assert 993136-s.Rational(421092,4)-s.Rational(1100232,8)-s.Rational(143,1024)>0
assert 1406136-s.Rational(385,512)>0
lm=s.Rational(3,2)
assert 539*lm**8+2286*lm**6+4872*lm**5<121073
assert 385*lm**7+1388*lm**6<45030
assert 77*lm**6<9498
print('PASS identity/manual bounds: complete root + second age >4k.')

# Complete third-age LOWER comparison >-4k.
H=594*c**12+10098*c**11+82566*c**10+432482*c**9+1549133*c**8 \
  +3754647*c**7+5981318*c**6+5917570*c**5+3060160*c**4+300470*c**3 \
  -74023*c*c+209225*c+83152
D=[H.subs(c,l-1)/2,
  2970*l**12+14850*l**11+50093*l**10+128672*l**9+61445*l**8-58983*l**7 \
  +91087*l**6+128543*l**5+211116*l**4+83533*l**3-298148*l*l+157252*l-37824,
  2*(5940*l**12+29700*l**11+93255*l**10+208036*l**9+195246*l**8+286776*l**7 \
     +309122*l**6+239414*l**5+161281*l**4-129234*l**3+92760*l*l-54940*l-1576),
  8*l*(2970*l**11+14850*l**10+42965*l**9+83304*l**8+108371*l**7+147663*l**6 \
     +108759*l**5+57687*l**4-15542*l**3+1691*l*l-15398*l-1970),
  8*l*l*(2970*l**10+14850*l**9+38810*l**8+65348*l**7+91325*l**6+67887*l**5 \
     +28117*l**4-7755*l**3-11823*l*l-11655*l-3546),
  16*l**3*(l+1)*(l*l+l+1)*(594*l**6+1782*l**5+1785*l**4+1120*l**3-659*l*l-1450*l-1379),
  -6304*l**4*(l+1)**2*(l*l+l+1)**2]
Av=1+l*(s.Rational(1,2)+y)
N3=sum(D[i]*y**i for i in range(7))
assert s.cancel((2376*Z3**3*Z4**2*(lower3+4)).subs(A,Av)-N3)==0
assert 209225-s.Rational(74023,2)>0
assert 128672-58983>0 and 128543+211116-298148-37824>0
assert 161281-129234>0 and 92760-54940-1576>0
assert 57687-15542-15398-1970>0
assert 67887-7755-11823-11655-3546>0
fold=16*l**3*(l+1)*(l*l+l+1)*(594*l**6+1782*l**5+1588*l**4+726*l**3-1053*l*l-1647*l-1379)
assert s.expand(D[5]+D[6]/2-fold)==0
assert 594+1782+1588+726-1053-1647-1379==611>0
print('PASS identity/manual bounds: complete third age >-4k.')

# Complete fourth age is positive, using only a cubic square bound.
p=s.symbols('p');v=p-s.Rational(1,2)
assert s.expand(s.Rational(2,3)-2*p+p*p+p**3-(s.Rational(1,24)-v/4+v*v+v*v*(p+1)))==0
assert s.Rational(1,24)-s.Rational(1,64)==s.Rational(5,192)>0
assert s.Rational(953,156)>6
Hmax=21+s.Rational(37,2)/s.Rational(63,40)
assert Hmax==s.Rational(2063,63)
assert 8+s.Rational(1,2)*(6-s.Rational(2,3)*Hmax)==s.Rational(16,189)>0
print('PASS manual bounds: complete fourth age >0.')
print('LOCAL complete J2=4b+3C0>0 on 23/20<=lambda<=3/2,0<u<=1/2.')
print('J3 is independent audited small-computer bridge; J1 and full 9600 removal remain OPEN.')
