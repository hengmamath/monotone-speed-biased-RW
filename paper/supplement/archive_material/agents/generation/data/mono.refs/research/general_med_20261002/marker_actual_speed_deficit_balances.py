"""Complete actual cap-shape/speed-deficit balances; NO total sign claim."""
import sympy as S
count=0
def eq(name,lhs,rhs):
    global count
    assert S.cancel(lhs-rhs)==0,name
    count+=1;print('PASS:',name)
for N in range(2,6):
    bb=S.symbols('b1:'+str(N+1));rr=S.symbols('r2:'+str(N+1))
    beta=[S.Integer(1)]+list(bb);rho=[S.Integer(1),S.Integer(1)]+list(rr)
    a=[beta[i]*rho[i] for i in range(N+1)]
    QN=sum((beta[i-1]-beta[i])*rho[i-1]*rho[i] for i in range(1,N+1))
    drops=[rho[i]-rho[i+1] for i in range(1,N)]
    eq('FULL finite Q balance + beta_N*rho_N^2 endpoint N='+str(N),
       1-QN,sum(drops[i-1]*(a[i]+a[i+1]) for i in range(1,N))
       +beta[N]*rho[N]**2)
    weights=S.symbols('w1:'+str(N+1))
    eq('FULL finite T loss + all triangular tails N='+str(N),
       sum(weights[i-1]*(1-rho[i]**2) for i in range(1,N+1)),
       sum(drops[i-1]*(rho[i]+rho[i+1])*sum(weights[i:]) for i in range(1,N)))
Tp,Qp,LT,LQ,l=S.symbols('Tp Qp LT LQ l')
T=Tp-LT;Q=Qp-LQ;Zp=2*Qp-(l+1)*Tp;Z=2*Q-(l+1)*T
eq('EXACT complete actual speed deficit',Tp/Zp-T/Z,
   2*(Qp*LT-Tp*LQ)/(Zp*Z))
root0,root1,R,Rp,aa,bb,w0,w1=S.symbols('root0 root1 R Rp aa bb w0 w1')
K= root0+R*root1+aa*(w0+R*w1)
Kpipe=root0+Rp*root1+bb*(w0+Rp*w1)
Loss=(bb-aa)*(w0+Rp*w1);B=-root1-aa*w1
eq('COMPLETE cross-diagonal loss including root speed change',
   K,Kpipe-Loss+(Rp-R)*B)
print(count,'complete balance identities PASS; ALL coefficients may be signed.')
print('No positivity of chord/tail/K1 or completion of165 is asserted.')
