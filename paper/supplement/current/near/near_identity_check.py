"""Independent exact identities linking the near-region finite targets to the body."""
import sympy as sp
import near_arithmetic_build as q

count=0
def check(name,value):
    global count
    assert value==0,(name,value)
    count+=1
    print('IDENTITY PASS',name,flush=True)
def conv(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def padded(a,n):return a+[0]*(n-len(a))

# This construction uses the original complete root and three assigned ages,
# independently of the polynomial quotient used by the target generator.
L,u,A,K,eta,k=q.L,q.u,q.A,q.K,q.eta,q.k
G=2*A-1-L/A;Gr=-1-2*L/A
H=A-L*u/A;Hr=-2*L*u/A
Br=A*(G-K*H)
Brr=u*(A+1)*G+A*Gr-A*(2*eta*H+K*Hr)
root=2*((25+L/k)*Br-Brr)/(L*A**2)
ages=0
for s in range(2,5):
    n=s*(s-1)//2;m=24-2*n
    v=L*q.Z[s]*q.Z[s-1]/q.Z[s+1]**2
    f=2-q.r[s]-L*q.r[s]**2
    ages+=2*s*L**(s-2)/q.Z[s]**3*(f*(m-u-u/A)+u*q.Z[s]/q.Z[s-1]*(-(24-n)*K+2*eta+v*(m*K-2*eta)))
check('J1 from original root and all three ages',(25*q.p+q.C0)/(k*A)-root-ages)

# Recover the whole root polynomial by independent finite convolution.
first=conv(q.Qc,[2*A,-1,-L/A])
second=[A*x for x in conv(q.Rc,[A,0,-L*u/A])]
bracket=[x-y for x,y in zip(first,second)]
root_coeff=[2/L*x for x in conv(bracket,[1,-L/A])]
for i in range(6):check('root coefficient %d'%i,root_coeff[i]-q.qr[i])
core_times=conv(q.cc,[1,-1])
age_source=[0]+[2*sum(q.n[s]*q.bc[s][i] for s in range(2,5)) for i in range(3)]
rhs=q.psic[:];rhs[0]-=q.p
subtract=padded(conv(age_source,[1,-1]),6)
for i in range(6):check('complete core division %d'%i,core_times[i]-rhs[i]+subtract[i])

# Recovery and merge hold with formal U_s,V_s, so no moment is substituted.
x=sp.symbols('x');Us=sp.symbols('U2:5');Vs=sp.symbols('V2:5')
rho=1-x*x;f=[1-x*x,1-x*x*(3-2*x),1-x*x*(6-8*x+3*x*x)]
age_change=2*rho*sum(Us[i]*(f[i]**2-1)-Vs[i]*(f[i]-1) for i in range(3))
Bstar=2*rho*(2*(2*Us[1]-Vs[1])+(8-3*x)*(2*Us[2]-Vs[2]))
Jstar=2*rho*(Us[0]+Us[1]*(3-2*x)**2+Us[2]*(6-8*x+3*x*x)**2)
check('exact quartic recovery',sp.expand(age_change+2*rho*x*x*sum([1,3,6][i]*(2*Us[i]-Vs[i]) for i in range(3))-x**3*Bstar-x**4*Jstar))
T=1-x
check('same-T first merge',sp.expand(rho*rho-f[1]-T*T*x*x))
check('same-T second merge',sp.expand(f[1]**2-rho*f[2]-T**4*x*x))

# Direct rational check of the assigned third-moment insertion.
ff,L,u,z,R,Q=sp.field('lambda,u,z,R,Q',sp.QQ)
c=L-1;Dw=Q-(L+1)*u*R;Df=Q-R
w=c*u*R/Dw;a=(u-w*(1-(L+1)*u+L*u*z)/c)/(u*z)
theta=1/(L+1-L*z)
gap=a*(1-theta)+w/c*(L+1-L*theta-1/z)
check('assigned gap after canonical three-moment bound',gap-(1-z)*(L*Df-u*R*(L+1-L*z))/((L+1-L*z)*z*Dw))

# Recover the six high-u coefficients without using their listed answers.
ff,L,u,E=sp.field('lambda,u,E',sp.QQ)
c=L-1;t=1-u;k=1-L*u;A=1+L*t;B=1+L*(L+1)*t
P=L+2*k*k/B**2+4*L**2*t*k/(A*B)
C2=L+2*k*k/B**2+4*k*(L+1-L*A/B)/(A*c)
W=L-2*k/B+2*k*k/B**2
d=[2-(L+1)*u,2*L*u/A,2*u/(A*t)-(L+1)*u*E]
h0=[2*A/L,-2-1/L,0,P/A**2]
qv=L+1-1/u
hv=[2*qv*A/(L*c),1/L-2*(1+qv)/c,2*(A-2*k)/(A**2*c),C2/A**2]
nc=[x+y for x,y in zip(conv(d,h0),[c*u*x for x in conv([1,0,E],hv)])]
S0=d[0]*P+c*u*C2
listed=[2*A/L,4*u-2-2/L,-2*A*E/L+4*u/(L*t)-4*u*B/A**2,2*E+S0/A**2-2*u*(2*L+1)/(L*A*t),2*u/A**3*(L*P+E*A*(A-2*k)),2*u/A**2*(P/(A*t)-E*W)]
for i in range(6):check('high-u natural coefficient %d'%i,nc[i]-listed[i])
K=t*(1+E)
S=k*(1-u*K)*(1+2*L/B**2)-A*t*((L+1)*K-2*L)+2*L**2*t*(2*L-(L+1)*u*K*A)/(A*B)
check('high-u upper endpoint full root and age',sum(nc)-2*k*S/(L*A**2*t))
Spositive=k*((c+2*k)*(1+2*L/B**2)/(L+1)+4*L**3*t*t/(A*B))
Sprice=A*t+u*k*(1+2*L/B**2)/(L+1)+2*L**2*t*u/B
check('high-u upper endpoint affine price',S-Spositive+((L+1)*K-2*L)*Sprice)

# Check the original H2 before cancellation at a free assigned speed.
ff,L,u,z,w=sp.field('lambda,u,z,w',sp.QQ)
c=L-1;t=1-u;k=1-L*u;A=1+L*t;B=1+L*(L+1)*t
r1=1/A;r2=A/B;L2=1/L-r1
a=(u-w*(1-(L+1)*u+L*u*z)/c)/(u*z)
H2=((1+w)*(1-L*z)**2-2*(1-a)*(1-L*z))/L+2*L*z*z*((1+w)*(1-L*r2)**2/L+2*(1-a)*(r2-r1)+2*L2*(a*(1-r2)+w/c*(L+1-L*r2-1/z)))
J=1/u-(L+1)+L*z
H0=2/(L*z)-2-1/L+z*z*(L+2*k*k/B**2+4*L*L*t*k/(A*B))
Hv=(1-L*z)**2/L-2*(1-L*z)*J/(L*c*z)+2*z*z*k*k/B**2+4*k*z*z/(A*c)*(L+1-L*A/B-1/z)
check('high-u H2 complete affine cancellation',H2-H0-w*Hv)

# The cap threshold and its derivative are the displayed finite rational
# identities used before the three-moment insertion, not a law substitution.
ff,L,u,z=sp.field('lambda,u,z',sp.QQ)
c=L-1;A=1+L*(1-u);M=L+(L+1)*u-L*u*z
Kcal=1-u+(1-u)*(L-(L+1)*u+L*u*(2*L+1)*z+2*L*A*u*z*z/(1-u))/(A*A*z*z*M)
Hpoly=2*((L+1)**2*u*u-L*L)-2*L*u*(L*c+(L+1)*(L+2)*u)*z+2*L*L*u*u*(2*L+1)*z*z+2*L*L*A*u*u*z**3/(1-u)
check('Condition-F threshold derivative',Kcal.diff(z)-(1-u)*Hpoly/(A*A*z**3*M*M))

# Jensen's deterministic age profile and the complete root regrouping.
ss,ts,es,gs,aa,ww,ll=sp.symbols('a_s t_s eps gamma a w lambda')
Delta=ts-(1-aa)*ss
original=es*(2*ts+(1+ww)*es-2*(1-aa)*ss)/ll+2*gs*ts
regrouped=(1+ww)*es**2/ll+2*(1-aa)*ss*gs+2*(gs+es/ll)*Delta
check('complete nonroot regrouping',sp.expand(original-regrouped))
print('NEAR IDENTITIES PASS',count,flush=True)
