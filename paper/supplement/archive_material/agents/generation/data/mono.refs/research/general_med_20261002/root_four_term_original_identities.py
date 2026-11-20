"""Full ORIGINAL speed/calibration and complete Z-tail clearing identities.

In particular the original a=[u-vA0/c]/b is substituted, not a pair of
normalized formulas sharing an error. No global sign is asserted here.
"""
import sympy as S
l,u,rho,A1,kn,kd=S.symbols('l u rho A1 kn kd')
c=l-1;z=rho/A1;b=u*z;kk=kn/kd
T2=u*u*(1+rho*rho*(kk-1+u)/(1-u))
Q2=u+l*u*u*z+A1*u*u*z*z/(1-u)
v_original=c*T2/(2*Q2-(l+1)*T2)
A0=1-(l+1)*u+l*b
a_original=(u-v_original*A0/c)/b
RN=(1-u)*kd+rho*rho*(kn-(1-u)*kd)
QN=A1*(1-u)*kd+l*u*rho*(1-u)*kd+u*rho*rho*kd
VD=2*QN-(l+1)*u*A1*RN;VN=c*A1*RN
A0N=(1-(l+1)*u)*A1+l*u*rho
AN=A1*(VD-RN*A0N)
assert S.cancel(v_original-u*VN/VD)==0
assert S.cancel(a_original-AN/(rho*VD))==0

N,Nm,Np,fs=S.symbols('N Nm Np fs')
vv=u*VN/VD;aa=AN/(rho*VD)
rs=N/Np;rm=Nm/N;LC=1/l-rm
Bs=(1+vv)*(1-l*rs)**2/l+2*(1-aa)*(rs-rm)
Ms=aa*(1-rs)+vv/c*(l+1-l*rs-N/(Nm*fs))
ds=N**3*Np**2*Nm
tail=rho*(VD+u*VN)*fs**2*(Np-l*N)**2*N*Nm
tail+=2*l*(rho*VD-AN)*(N*N-Nm*Np)*fs**2*Np*Nm
tail+=2*(N-l*Nm)*AN*(Np-N)*fs**2*Np*Nm
tail+=2*(N-l*Nm)*rho*u*A1*RN*fs*((l+1)*Np*Nm*fs-l*N*Nm*fs-N*Np)*Np
assert S.cancel(l*rho*VD*(fs/N)**2*(Bs+2*LC*Ms)*ds-tail)==0
print('3 COMPLETE ORIGINAL-speed/calibration/Z-tail identities PASS locally.')
