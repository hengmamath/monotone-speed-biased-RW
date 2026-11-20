"""NEW calibrated cumulative head: generic exact IDs, no point sampling."""
import sympy as S
l,u,b,q,i,k,r,rp,Ls,La,R,Ca,da,rho,D,Dp,n,w,V=S.symbols(
'l u b q i k r rp Ls La R Ca da rho D Dp n w V')
c=l-1; A0=1-(l+1)*u+l*b
an,an1,an2=S.symbols('an an1 an2')
alpha=(u-q*A0)/b
tn=-q*an+(1+(l+1)*q)*an1-(alpha+l*q)*an2
count=0
def eq(name,left,right):
    global count
    assert S.cancel(left-right)==0,name
    count+=1
    print('PASS:',name)
eq('complete calibrated t derivative',S.diff(tn,q),
   A0*an2/b-(an-(l+1)*an1+l*an2))
B2=S.symbols('B2')
ap=(u-R*(1-(l+1)*u+l*B2))/B2
e=S.symbols('e')
ab=(u-R*(1-(l+1)*u+l*B2*(1-e)))/(B2*(1-e))
eq('same-e full calibration',ab-ap,(ap+l*R)*e/(1-e))
a=S.symbols('a')
np=r*(rho-D)/rho
nprev=rp*rho/(rho+Dp)
tau=lambda aa,nn,pp:1-(aa+l*R)*nn+(l+1)*R-R/pp
eq('same-law ratio correction',tau(a+da,np,nprev)-tau(a,r,rp),
   -da*np+(a+l*R)*r*D/rho-R*Dp/(rp*rho))
# r(1+Ls)=1/l; remaining C_i terms independent of alpha.
CC=S.symbols('CC')
Bact=w*rho*(2*i*r*((a+da)*(1+Ls)+CC)+k*(2*i-1)*tau(a+da,np,nprev))
Bp=w*(2*i*r*(a*(1+Ls)+CC)+k*(2*i-1)*tau(a,r,rp))
eq('full B correction including previous defect',
   (Bact-rho*Bp).subs(Ls,1/(l*r)-1),
   w*rho*da*(2*i/l-k*(2*i-1)*np)+k*w*(2*i-1)*((a+l*R)*r*D-R*Dp/rp))
eq('square price positive correction',
   Bact-(2*rho-D)*V-rho*(Bp-2*V),Bact-rho*Bp+D*V)
eq('exact i1 k cancellation',
   (e*(w*da*(2/l-k*r*(1-e))+k*w*Ca*r*e)+e*e*V).subs(da,Ca*e/(1-e)),
   e*e*(V+2*w*Ca/(l*(1-e))))
# Cap neighboring relation at ALL index i.
x,d,h=S.symbols('x d h')
r0=(x/l-d)/(x-d);r1=(x-d)/(l*x-d)
Lprev=c*d/(l*(x/l-d));Li=c*d/(l*(x-d));Ln=c*d/(l*(l*x-d))
eq('ALL-index adjacent cap normalization',1/(l*r0*r1),l+(l+1)*Lprev)
Omega=S.symbols('Omega')
J0=k*w*(2*i-1)*Ca*r1-(k*w*(2*i-1)*R/r0+k*l*r1*w*(2*i+1)*R)/2
eq('complete adjacent-square coefficient',
   J0/(k*w*(2*i-1)*l*R*r1),
   Ca/(l*R)-(l+1)/2-1/(2*i-1)-(l+1)*Lprev/2)
eq('EXACT Lprev cutoff boundary',
   (Lprev-Omega/(l+1)),
   -Omega*(x/l-d*(1+c*(l+1)/(l*Omega)))/((l+1)*(x/l-d)))
eq('ALL-index cap L recurrence',Lprev/Li,l*(1+Lprev))
# Full Young endpoints, all arbitrary finite sequences.
for N in range(2,6):
    DD=[S.Integer(0)]+list(S.symbols('D1:'+str(N+1)))
    WW=[S.Integer(0),S.Integer(0)]+list(S.symbols('W2:'+str(N+1)))+[S.Integer(0)]
    cross=-sum(WW[j]*DD[j]*DD[j-1] for j in range(2,N+1))
    charged=-sum((WW[j]+WW[j+1])*DD[j]**2/2 for j in range(1,N+1))
    eq('complete Young endpoint N='+str(N),cross-charged,
       sum(WW[j]*(DD[j]-DD[j-1])**2/2 for j in range(2,N+1)))
aa=S.symbols('aa')
tauinf=1-aa/l
G=2*(aa+c*R)/l+2*k*tauinf-2*(1+c*R)/l
eq('EXACT cap leading margin',G,2*(k-1/l)+2*aa*(1-k)/l)
eq('ALL-index cap response error',
   tau(aa,r1,r0)-tauinf,(aa+l*R)*Ln-l*R*Lprev)
eq('hard variance bound',1-u*u/(u/(l+1-l*u)),(1-u)*(1-l*u))
eq('complete D at variance endpoint',
   2-(3*l+1)*u+l*(l+1)*u*u,(1-l*u)*(2-(l+1)*u))
eq('hard alpha defect denominator',
   (1-ap)/(ap+l*R+1-ap),(1-ap)/(1+l*R))
eq('complete Ehard parameter derivative',
   S.diff((1-ap)/(1+l*R),R),(1-u)/(B2*(1+l*R)**2))
print(count,'generic exact identities PASS; signs/full tails require manuscript proof.')

