"""Rebuild both complete clearing identities, independently of certificate."""
import sympy as S
l,u,rho,A1,VN,VD,AN,N,Nm,Np,fs=S.symbols('l u rho A1 VN VD AN N Nm Np fs')
c=l-1;a=AN/(rho*VD);v=u*VN/VD
ep=1-l*rho/A1
Root=((1+v)*ep**2-2*(1-a)*ep)/l
root=rho*(VD+u*VN)*(A1-l*rho)**2-2*(rho*VD-AN)*(A1-l*rho)*A1
assert S.cancel(l*rho*VD*Root-root/A1**2)==0
rs=N/Np;rm=Nm/N;ec=1-l*rs;LC=1/l-rm
As=c*fs/N
Bs=(1+v)*ec**2/l+2*(1-a)*(rs-rm)
Ms=a*(1-rs)+(v/c)*(l+1-l*rs-N/(Nm*fs))
ds=N**3*Np**2*Nm
tail=c**2*rho*(VD+u*VN)*fs**2*(Np-l*N)**2*N*Nm
tail+=2*l*c**2*(rho*VD-AN)*(N**2-Nm*Np)*fs**2*Np*Nm
tail+=2*c**2*(N-l*Nm)*AN*(Np-N)*fs**2*Np*Nm
tail+=2*c*(N-l*Nm)*rho*u*VN*fs*((l+1)*Np*Nm*fs-l*N*Nm*fs-N*Np)*Np
assert S.cancel(l*rho*VD*As**2*(Bs+2*LC*Ms)*ds-tail)==0
Rnum,A0num,Qnum=S.symbols('Rnum A0num Qnum')
z=rho/A1;A0=A0num/A1;V=c*A1*Rnum/VD
assert S.cancel((1-V*A0/c)/z-A1*(VD-Rnum*A0num)/(rho*VD))==0
print('3 COMPLETE original rational clearing/calibration identities PASS locally.')
