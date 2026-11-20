"""Complete local identities for joint-prefix F payment; no global sign claim."""
import sympy as S
l,u,z,t,k,q=S.symbols('l u z t k q')
c=l-1;h=c*u/(1-u);d=1-h;x=c+h;H=c+2*h
A1=l+1-l*u;A2=l*l+l+1-l*(l+1)*u;A3=l**3+l*l+l+1-l*(l*l+l+1)*u
r3=A2/A3;b=u*z;e=b*t;beta2=h/(l*l-d)
Tpi=u*u*k/(1-u)
T2=u*u+(Tpi-u*u)*(b/beta2)**2
Q2=u+l*u*b+(l*l-d)/c*b*b
AA=A1*A1*(k-1+u)/(1-u)
R=1+AA*z*z
D2=1+2*l*u*z+(2*A1*u/(1-u)-AA)*z*z
s2=u*R/D2;tc=1-s2*(1-z)
J2=2*u*(b-e)*Q2-((b-e)+b*(u-b))*T2
G=lambda w:w*w-(2*u+r3)*w+r3*u/z*w+u*z
p=1-q
ecap=((l*l-p)*b-((l-p)*u-(l*l-p)*b)**2/(q-(l-p)*u))/(l**3-p)
markden=q*(1-u)-c*u
CC=c*(1-(l+1)*z)+q*(1-z)
tB=(c*(l+1)+q-u*CC**2/(z*markden))/(c*(l*l+l+1)+q)
NB=z*markden*((c*(l*l+l+1)+q)*tc-(c*(l+1)+q))+u*CC**2
A=c**3*(1+u)/(l*(1-u)**2*(l-u)**2)+1/((1-u)*(1+u))
QB=c*(1+u)/((1-u)*(1+u*(z-u)*A))
QBx=H/(1+x*H/c*(b-u*u)*(x*x/(l*(x+1)**2)+x/H**2))
checks=[
 h/(l*l-d)-u/A1,
 (l*l-d)/(l**3-d)-A1/A2,
 (l**3-d)/(l**4-d)-A2/A3,
 T2-u*u*R,
 (2*u*Q2-T2)-u*u*D2,
 J2-b*(2*u*Q2-T2)*(1-t-s2*(1-z)),
 G(z)-(z-u)*(z-r3),
 ecap/b-tB,
 NB-z*markden*(c*(l*l+l+1)+q)*(tc-tB),
 QB-QBx,
 D2.subs(z,1/A1)-(2-k)/(1-u),
 (D2-u*R).subs(z,1/A1)-(2-(1+u)*k)/(1-u),
]
# Independently verify the certificate's cleared numerator and denominators.
kn,kd,w,tn,dn=S.symbols('kn kd w tn dn')
zn=u*A1+w*(1-u)*(1-l*u)
rn=(1-u)*kd+(kn-(1-u)*kd)*zn**2
dnew=A1*(1-u)*kd+2*l*u*zn*(1-u)*kd+2*u*zn**2*kd-A1*(kn-(1-u)*kd)*zn**2
tnew=dnew-u*rn*(A1-zn)
zk=zn/A1
N=A3*zn*A1*tn**2-(2*u*A3+A2)*zn*A1*tn*dn+A2*u*A1**2*tn*dn+A3*u*zn**2*dn**2
checks += [
 dnew/(A1*(1-u)*kd)-D2.subs({k:kn/kd,z:zk}),
 tnew/dnew-tc.subs({k:kn/kd,z:zk}),
 N/(A3*A1**2*dn**2)-zk*G(tn/dn).subs(z,zk),
]
for i,expr in enumerate(checks,1):
 assert S.cancel(expr)==0,(i,S.factor(expr))
print(f'{len(checks)} full normalized/joint-prefix payment identities PASSED locally.')
