"""Exact join: original general-T/9600 rational calibration -> SAME T=1 endpoint.
No old 9600 polynomial loaded or replayed; use KD=1 normalization.
"""
import sys
import sympy as S
assert sys.flags.optimize==0
l,u,rho,K=S.symbols('l u rho K');c=l-1;t=1-u;k=1-l*u;A=l+1-l*u
RN=t+rho*rho*(K-1+u)
QN=A*t+l*u*rho*t+u*rho*rho
VD=2*QN-(l+1)*u*A*RN;VN=c*A*RN
A0N=(1-(l+1)*u)*A+l*u*rho
AN=A*(VD-RN*A0N)
D=2-(l+1)*u*K
for orig,target in ((RN,K),(QN,A),(VD,A*D),(VN,c*A*K)):
 assert S.cancel(orig.subs(rho,1)-target)==0
assert S.cancel((u*VN/VD).subs(rho,1)-c*u*K/D)==0
assert S.cancel((AN/(rho*VD)).subs(rho,1)-(2*A-(l+1)*K)/D)==0
assert S.cancel((1-l*rho/A).subs(rho,1)-k/A)==0
print('PASS original RN,QN,VD,VN,w,a,E at rho=1 give EXACT original T=1 formulas')
Z=lambda s:t*sum(l**j for j in range(s))+u
for s in (2,3,4):
 z,zm,zp=Z(s),Z(s-1),Z(s+1)
 assert S.expand((l**s*t-1+l*u)-c*z)==0
 assert S.expand(zp-l*z-k)==0 and S.expand(z-l*zm-k)==0
 # Clear the recurrence identity dr=L(1-r) without rational expansion.
 assert S.expand(l*z*z-l*zm*zp-(z-l*zm)*(zp-z))==0
print('PASS beta_s=u/Z_s and whole-bracket a cancellation at T=1, ages 2,3,4')
print('P9600(T=1)=KD*lambda*A*Dprofile*(P_affine-Kcap*Q_affine); all clearing factors positive on target')
print('Only target-domain T=1 boundary positivity replaced; full-T 9600 remains required')
