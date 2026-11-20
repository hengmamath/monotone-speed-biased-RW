import export_exact as EX
"""254--259 exact finite-h quarter certificate; all arithmetic rational."""
import sympy as S
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from fractions import Fraction as F
from math import comb
from collections import defaultdict
rr,C,X=ring('C,X',QQ)
def scaled_groups(i,C,X,L,AC,P0,Di,Dn,Dp,G):
    nn=i+1;P=L*L*P0;T=1+i*X
    F2=X*P+X-C
    F3=X*X*P*P+4*(X-C)*X*P+(X-C)**2
    F4=X**3*P**3+11*(X-C)*X*X*P*P+11*(X-C)**2*X*P+(X-C)**3
    W=1-G*X;O=X+(L+1)*W
    Tau=X*(1+X)*Dn*Dp-Di*Dp*(X*L*L+G*(X-C)*(L+1)*X*X+L*W*(1+X))+(L+1)*W*(1+X)*Dn*Dp-W*(1+X)*Di*Dn
    TLN=720*AC**4*Dn**4+360*X*AC**3*P*Dn**3+60*X*AC**2*P*F2*Dn**2-X*P*F4
    PUN=240*nn*X*AC**3*P*Dn**3+120*nn*X*AC**2*P*F2*Dn**2+20*nn*X*AC*P*F3*Dn+240*AC**4*Dn**4-20*X*AC**2*P*F2*Dn**2+X*P*F4
    N=[1440*i*L*P0*AC**3*Dn**5*Dp*T*(X*X*L*L+G*(X-C)*(L+1)*X**3+C*W*(1+X)*X),
       1440*i*(X-C)*W*L*P0*X*AC**3*Dn**4*(1+X)*Dp*T,
       1440*nn*(X-C)*W*Di*L*L*P0*X*AC**3*Dn**3*(1+X)*Dp*T,
       720*(2*i-1)*AC**4*L*P0*X*Dn**4*T*Tau,
       2*L*(1+X)*Dp*T*Di*Di*(X+C*W)*TLN,
       -6*AC*(1+X)*Dp*T*Di*Di*O*PUN,
       2880*nn*W*L**3*P0*X*AC**3*Dn**3*(1+X)*Dp*T*Di*Di,
       2880*W*L*AC**3*Dn**4*(1+X)*Dp*T*Di*Di,
       -720*L*L*P0*X*X*AC**3*Dn**5*(1+X)*Dp*((3-9*X)*i*X-QQ(7,3)+3*X)]
    K=720*L*L*P0*X*X*AC**3*Dn**5*(1+X)*Dp*T
    return N,K
def numerator(i,G):
    L=1+C;AC=1+C/2-C*C/12+C**3/24
    def D(n):return 1+X*sum(comb(n,k)*C**(k-1) for k in range(1,n+1))
    nn,K=scaled_groups(i,C,X,L,AC,L**(i-1),D(i),D(i+1),D(i-1),G)
    return sum(nn),K
def bern(cc,elev=0):
    deg=(max(a[0] for a in cc)+elev,max(a[1] for a in cc)+elev)
    coefs={mo:co/10**mo[0]/4**mo[1] for mo,co in cc.items()}
    for axis in (0,1):
        groups=defaultdict(dict)
        for mo,co in coefs.items():groups[mo[:axis]+mo[axis+1:]][mo[axis]]=co
        out={}
        for key,aa in groups.items():
            for j in range(deg[axis]+1):
                val=sum((co*F(comb(j,k),comb(deg[axis],k)) for k,co in aa.items() if k<=j),F())
                if val:out[key[:axis]+(j,)+key[axis:]]=val
        coefs=out
    meta={"check":"Q3c source/gap or head","age":str(globals().get("i","")),"g_endpoint":str(globals().get("ep","")),"domain":[["0","1/10"],["0","1/4"]]}
    EX.emit("power",cc,("x","h"),(max(m[0] for m in cc),max(m[1] for m in cc)),meta)
    EX.emit("bernstein",coefs,("x_box","h_box"),deg,meta)
    return deg,coefs
i,c,x,L,a,p0,di,dn,dp,g=S.symbols('i c x L a p0 di dn dp g', positive=True)
d=(x-c)/x;R=(1-g*x)/x;alpha=(L**2+g*(x-c)*(L+1)*x)/(1+x)
r=di/dn;rp=dp/di;li=(x-c)/(L*di);w=p0/di**2
tau=1-(alpha+L*R)*r+(L+1)*R-R/rp
p=L**2*p0;b=1/dn
m0=b;m1=p*b**2;m2=p*(p+d)*b**3
m3=p*(p*p+4*d*p+d*d)*b**4
m4=p*(p**3+11*d*p*p+11*d*d*p+d**3)*b**5
TL=(a*m0/x+m1/2+x*m2/(12*a)-x**3*m4/(720*a**3))/L
PU=((i+1)*(a*m1+x*m2/2+x*x*m3/(12*a))+a*a*m0/x-x*m2/12+x**3*m4/(240*a*a))/L**2
direct=[2*i*(alpha+c*R)/L,2*i*R*r*li,2*(i+1)*R*L*r*r*li,
 a*(2*i-1)*tau/L,2*(1+c*R)*TL/w,-2*(1+(L+1)*R)*PU/w,
 4*R*(i+1)*L*p0/(dn**2*w),4*R*b/(x*L*w),
 -((3-9*x)*i*x-S.Rational(7,3)+3*x)/(1+i*x)]
groups,K=scaled_groups(i,c,x,L,a,p0,di,dn,dp,g)
for j,(num,target) in enumerate(zip(groups,direct),1):
    assert S.cancel(num/K-target)==0,j
    print('GENERIC piece',j,'PASS',flush=True)


# ALL-N scalar derivative identity, not derivative of an inequality.
n,y,hh,dd,ll,jj=S.symbols('n y hh dd ll jj', positive=True)
v=hh**2*n*dd**(n-1)*y**(jj+1)/(ll*(1-y))
vp=S.diff(v,ll)-n*y*S.diff(v,y)/ll
bundle=hh**2*n*n*dd**(n-1)*y**(jj+1)/ll**2*((jj+1)/(1-y)+y/(1-y)**2)
assert S.cancel(-(ll-1)*vp-(1+(ll-1)/ll)*v-(-v+(ll-1)*bundle))==0
assert F(41,40)**25<2
assert F(19,10)*F(41,2)-F(101,100)*F(41,40)*F(5,4)>30*F(41,40)**2
# Exact identity proving all-age variance/weight cancellation.
xx,hh=S.symbols('xx hh')
assert S.expand((1+hh*xx)*(1-hh/2)**2-(1-hh)*(1+hh*xx/2)**2-hh**2*((1+hh*xx)-(1-hh)*xx**2)/4)==0
# Three source/gap macro certificates.
x,h=S.symbols('x h');ell=1+h*x;c=h*x
alo=1+c/2-c*c/12;aup=alo+c**3/24
J=24-36*h+14*h*h-h**3
sup=lambda a:a-x/2+x*x*(2-h)/(12*a)
slo=lambda a:sup(a)-x**4*J/(720*a**3)
target=lambda g:2*(1-g*x)/(x+(ell+1)*(1-g*x))
source=2*(sup(alo)**2-(ell+1)*sup(alo)+alo**2-x*x*(2-h)/12)-S.Rational(69,500)*x*ell*(2*ell-(ell+1)*slo(alo))
A=h*h*x*x-6*h*x-12
cases=[(slo(alo)/ell-target(S.Rational(1,4)),1,60*ell*A**3*(h*x*x-4*h*x-2*x-8)),
 (target(S.Rational(1,8))-sup(aup)/ell,-1,24*ell*(h*x*x-8*h*x-6*x-16)*(c**3-2*c*c+12*c+24)),
 (source,-1,90000*A**3)]
for expr,sg,expected in cases:
    num,den=S.fraction(S.factor(expr));assert S.expand(den-expected)==0
    pp=S.Poly(sg*num,x,h);xp=min(mo[0] for mo,co in pp.terms())
    cc={(mo[0]-xp,mo[1]):F(co) for mo,co in pp.terms()}
    deg,bc=bern(cc);assert len(bc)==(deg[0]+1)*(deg[1]+1) and min(bc.values())>0
    print('SOURCE/GAP',deg,len(bc),'min',min(bc.values()),flush=True)
# Every possible negative head age. Sign interpolation is affine in g.
for i in range(1,25):
    for ep in (QQ(1,8),QQ(1,4)):
        N,K=numerator(i,ep)
        xp=min(mo[0]+mo[1] for mo in N);assert xp==2
        cc={(mo[0]+mo[1]-xp,mo[0]):F(co.numerator,co.denominator) for mo,co in N.items()}
        deg,bc=bern(cc);assert all(a>0 for a in bc.values())
        assert len(bc)==(deg[0]+1)*(deg[1]+1)-1 and (0,0) not in bc
        print('HEAD',i,ep,deg,len(bc),'min',min(bc.values()),flush=True)
print('254--259 ALL exact checks PASS; full budget uses accepted 229/250/252.',flush=True)
