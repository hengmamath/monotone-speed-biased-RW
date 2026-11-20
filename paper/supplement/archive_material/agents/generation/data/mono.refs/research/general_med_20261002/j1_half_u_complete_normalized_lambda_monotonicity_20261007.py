"""Exact identity checks for the complete normalized half-u boundary proof.
No grid, sampled-sign inference, old certificates, or full-box assertion.
"""
from fractions import Fraction as Q
import sympy as s
l=s.symbols("l");u=s.Rational(1,2);t=1-u
k=1-l*u;A=1+l*t
K=(l+1)/(2*l)+t/2+(l+1)*(2*l*t-l+1)*t/(24*l);h=K-t
G=2*A-1-l/A;Gp=-1-2*l/A;H=A-l*u/A;Hp=-2*l*u/A
B=A*(G-K*H);Bp=u*(A+1)*G+A*Gp-A*(2*h*H+K*Hp)
root=2*((25+l/k)*B-Bp)/(l*A*A)
q={j:sum(l**i for i in range(j))+1 for j in range(2,6)}
R=1091/(32*q[2])-775/(6*q[2]**2)+8/q[2]**3 \
 +29/(32*(2-l))+359/(16*l)-575/(24*l*l)
assert s.cancel(root-R)==0
Rd=(-3273*q[2]**2+24800*q[2]-2304)/(96*q[2]**4) \
 +(2300-1077*l)/(48*l**3)+29/(32*(2-l)**2)
assert s.cancel(s.diff(R,l)-Rd)==0
N2=1650*l**10-11643*l**9-42259*l**8-33337*l**7+76721*l**6 \
 +190088*l**5+33532*l**4-23312*l**3-5392*l*l+134400*l+33600
N3=3004*l**14+3599*l**13-33545*l**12-91645*l**11-78768*l**10 \
 -2110*l**9+188138*l**8+499251*l**7+490063*l**6+210991*l**5 \
 +103830*l**4-104952*l**3-74976*l*l+173872*l+127584
N4=1920*l**23+11912*l**22+32160*l**21+47014*l**20+34566*l**19 \
 +47091*l**18+269347*l**17+940849*l**16+2238499*l**15 \
 +4128182*l**14+6323852*l**13+8215273*l**12+9014075*l**11 \
 +8204253*l**10+6205389*l**9+3779022*l**8+1775708*l**7 \
 +343224*l**6-109040*l**5+144672*l**4+420416*l**3+228736*l*l \
 +42496*l-51200
expected=[N2/(6*l*l*q[2]**5*q[3]**3),
          N3/(2*q[2]**2*q[3]**4*q[4]**3),
          4*N4/(3*q[2]**2*q[3]**2*q[4]**4*q[5]**3)]
Z={j:1+t*sum(l**i for i in range(1,j)) for j in range(1,6)}
for j,n,expr in zip((2,3,4),(1,3,6),expected):
 r=Z[j]/Z[j+1];v=l*Z[j]*Z[j-1]/Z[j+1]**2;Fs=2-r-l*r*r
 T=2*j*l**(j-2)/Z[j]**3*(Fs*(24-2*n-u*(A+1)/A)
 +u*Z[j]/Z[j-1]*(-(24-n)*K+2*h+v*((24-2*n)*K-2*h)))
 assert s.cancel(s.diff(T,l)-expr)==0
 print("PASS generic complete age derivative identity",j,flush=True)
b=Q(10,7)
p2=190088+76721-33337*b*b-42259*b**3-11643*b**4
p3=490063+499251+188138-2110*b**3-78768*b**4-91645*b**5-33545*b**6
assert p2==Q(65014109,2401)>0 and p3==Q(1509500348,117649)>0
assert 33532-23312-5392==4828>0
assert 210991+103830-104952-74976==134893>0
assert 343224-109040>0 and 144672-51200==93472>0
assert -3273*16+24800*3-2304==19728>0
assert 2300-1077*b==Q(5330,7)>0
print("PASS complete root identity and both explicit positive rational payments",p2,p3)
print("SCOPED: half-u boundary only; full-rectangle curvature unproved")

