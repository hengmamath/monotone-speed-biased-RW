"""260--268 complete low-q certificate; LOCAL PASS, independent audit pending."""
import sympy as S
from fractions import Fraction as F
from collections import defaultdict
from math import comb

def bern(poly, scales):
    de=poly.degree_list()
    co={mo:F(aa)*__import__('functools').reduce(lambda x,y:x*y,
        (F(scales[j])**mo[j] for j in range(len(scales))),F(1))
        for mo,aa in poly.terms()}
    for ax in range(len(scales)):
        gr=defaultdict(dict)
        for mo,aa in co.items():gr[mo[:ax]+mo[ax+1:]][mo[ax]]=aa
        out={}
        for key,bb in gr.items():
            for k in range(de[ax]+1):
                aa=sum((v*F(comb(k,j),comb(de[ax],j)) for j,v in bb.items() if j<=k),F())
                if aa:out[key[:ax]+(k,)+key[ax:]]=aa
        co=out
    assert co and min(co.values())>0
    return de,len(co),min(co.values())

q,c,b,p,dd,a,i=S.symbols('q c b p dd a i')
L=1+c;d=1-c*q;h=c*q;r=1/(L+b);A=c+b*r;B=b*r
Ps=[1,A,A*(A+B),A*(A*A+4*A*B+B*B),
    A*(A**3+11*B*A*A+11*B*B*A+B**3),
    A*(A**4+26*B*A**3+66*B*B*A*A+26*B**3*A+B**4)]
M=1/(p-dd);wi=q*q*b*(b+c)/(d*L);mom=[]
for j in range(6):
    mm=S.cancel(h**(j+1)*M.subs({p:L*d*(1+c/b),dd:d})/wi)
    target=L*r/(q*(b+c)) if j==0 else q**(j-1)*L*r*Ps[j]/(b+c)
    assert S.cancel(mm-target)==0
    mom.append(mm);M=S.cancel(-p*S.diff(M,p))
TL=(a*q*mom[0]+mom[1]/2+mom[2]/(12*a*q)-mom[4]/(720*a**3*q**3))/L
PU=((i+1)*(a*mom[1]+mom[2]/(2*q)+mom[3]/(12*a*q*q))
    +a*a*q*mom[0]-mom[2]/(12*q)+mom[4]/(240*a*a*q**3))/L**2
PL=((i+1)*(a*mom[1]+mom[2]/(2*q)+mom[3]/(12*a*q*q)-mom[5]/(720*a**3*q**4))
    +a*a*q*mom[0]-mom[2]/(12*q))/L**2
assert S.cancel(TL-r/(b+c)*(a+A/2+Ps[2]/(12*a)-Ps[4]/(720*a**3)))==0
assert S.cancel(PU-r/(L*(b+c))*((i+1)*(a*A+Ps[2]/2+Ps[3]/(12*a))
                             +a*a-Ps[2]/12+Ps[4]/(240*a*a)))==0
assert S.cancel(PL-r/(L*(b+c))*((i+1)*(a*A+Ps[2]/2+Ps[3]/(12*a)-Ps[5]/(720*a**3))
                             +a*a-Ps[2]/12))==0
print('261 six generic moment and three tail identities PASS',flush=True)

au=1+c/2-c*c/12+c**3/24;u=q/(q+1);b2=q/(q+2+c)
TU=(au*q*b2+L*L*b2*b2/2+L*L*(L*L+d)*b2**3/(12*au*q))/L
target=2*q*q*(6*q+5)/(6*(q+1)+(L+1)*q*(6*q+5))
n,den=S.fraction(S.factor((target-u*u-TU)/q**2))
C=c**3-2*c*c+12*c+24
expected=24*L*(q+1)**2*(c+q+2)**3*C*(6*c*q*q+5*c*q+12*q*q+16*q+6)
assert S.expand(den-expected)==0
ans=bern(S.Poly(n,q,c),(3,F(1,6)))
assert ans==((6,9),70,F(576))
print('266 theta upper bound:',ans,flush=True)

# The entire coefficient of R in the lower is negative, all i>=2.
b,c,j=S.symbols('b c j');L=1+c;i=2+j;r=1/(L+b)
KR=i*c*r*r+2*i*b*r**3-(2*i-1)*L/(2*(1-b))+(2*i-3)*L*r/2
P=S.Poly(S.cancel(-2*(1-b)*(L+b)**3*KR),b,c,j)
assert len(P.terms())==24 and all(aa>0 for _,aa in P.terms())

# accepted226 lower, k>=1/lambda for the positive alpha term,k<=1
# for the explicitly negative adjacent term; alpha>lambda^2u,R<q.
q,c,v,j=S.symbols('q c v j');L=1+c;i=2+j;d=1-c*q
b=d*v/(q+i);r=1/(L+b)
KR=i*c*r*r+2*i*b*r**3-(2*i-1)*L/(2*(1-b))+(2*i-3)*L*r/2
lower=i*L*r*r+(2*i-1)*L*q/(q+1)*r+q*KR
n,den=S.fraction(S.factor(lower))
expected=-2*(q+1)*(q+i-d*v)*(L*(q+i)+d*v)**3
assert S.expand(den-expected)==0
ans=bern(S.Poly(-n,q,c,v,j),(3,F(1,6),1))
assert ans==((6,4,3,5),840,F(2))
print('262 complete Jminus zero PASS',ans,flush=True)

q,c,v,i,theta,b=S.symbols('q c v i theta b')
L=1+c;d=1-c*q;r=1/(L+b);rp=(1-b)/L;R=q*theta
al=(L*L*q+(1-theta)*d*(L+1))/(q+1)
alo=1+c/2-c*c/12;au=alo+c**3/24
A=c+b*r;B=b*r
P2=A*(A+B);P3=A*(A*A+4*A*B+B*B);P4=A*(A**3+11*B*A*A+11*B*B*A+B**3)
TL=r/(b+c)*(au+A/2+P2/(12*au)-P4/(720*au**3))
PU=r/(L*(b+c))*((i+1)*(au*A+P2/2+P3/(12*au))+au*au-P2/12+P4/(240*au*au))
VU=-(1+c*R)*TL+(1+(L+1)*R)*PU-2*R*(i+1)*L*r*r-2*R*r/(b+c)
tau=1-(al+L*R)*r+(L+1)*R-R/rp
BB=2*i*(al+c*R)/L+2*i*R*r*b/L+2*(i+1)*R*r*r*b+alo*(2*i-1)*tau/L
K=BB-2*VU
AA=S.diff(K,i);CC=K.subs(i,0)
ilow=2*(d-q*b)/(2*b+c*(d-q*b))
targets={'slope':AA,'head':ilow*AA+CC+S.Rational(3,2)*(q*b/d)**2}
for name,expr in targets.items():
    for ep in (0,1-1/(6*(q+1))):
        expr2=expr.subs({b:d*v/(q+2),theta:ep},simultaneous=True)
        nn,den=S.fraction(S.factor(expr2));print(name,'EP',ep,'DEN',den,flush=True)
        C=c**3-2*c*c+12*c+24
        D1=c*q*v-c*q-2*c-q-v-2
        D2=c*q*v-c*q-2*c-2*v
        D3=c*q*v-c*q-2*c-v
        P=q+2-d*v
        if name=='slope':
            expected=(12 if ep==0 else 72)*L*(q+1)**(1 if ep==0 else 2)*C*D1**4
            if ep!=0:expected*=P
            sg=1
        else:
            expected=(1440 if ep==0 else 8640)*L*(q+1)**(1 if ep==0 else 2)*(q+2)**2*C**3*D2*D3*D1**5
            if ep!=0:expected*=P
            sg=-1
        assert S.expand(den-expected)==0
        ans=bern(S.Poly(sg*nn,q,c,v),(3,F(1,6),1))
        print('267 entire head PASS',name,ep,ans,flush=True)

from sympy.polys.fields import field
from sympy.polys.domains import QQ
ff,q,c,z=field('q,c,z',QQ)
L=1+c;h=c*q;d=1-h;u=q/(q+1);b2=q/(q+2+c)
alo=1+c/2-c*c/12;au=alo+c**3/24
b=d/(q+1);r=1/(L+b);l1=b/L;l2=d/(L*(q+2+c))
A=c+b*r;B=b*r
P2=A*(A+B);P3=A*(A*A+4*A*B+B*B)
P4=A*(A**3+11*B*A*A+11*B*B*A+B**3)
P5=A*(A**4+26*B*A**3+66*B*B*A*A+26*B**3*A+B**4)
TU=r/(b+c)*(au+A/2+P2/(12*au))
TL=r/(b+c)*(alo+A/2+P2/(12*alo)-P4/(720*alo**3))
PL=r/(L*(b+c))*(2*(alo*A+P2/2+P3/(12*alo)-P5/(720*alo**3))+alo*alo-P2/12)
V0=-TU+PL;VR=-c*TU+(L+1)*PL-4*L*r*r-2*r/(b+c)
W0=c/L-1+2*l1;Wp=c*W0+4*l1-2*r*(l1+2*L*l2)
al0=(L*L*q+d*(L+1))/(q+1);al1=-d*(L+1)/(q+1)
B10=2*al0/L;B11=2*(al1+c*q)/L+2*q*r*l1+4*q*L*r*r*l1
Ev=d/(q+1)**2;zp=b2/u;eps=u-L*b2
AE=1-(L+1)*u+L*b2*(1-Ev);DE=2-(3*L+1)*u+L*(L+1)*b2*(1-Ev)
phi=(1-zp)*(d-c*c*(q+2+c)/6)/(L*(2*q+3+c))
CE=2*AE*u*phi+eps*DE/L;C0=CE*(2-Ev)/(2*q)
a=q+2;U2=1/a+1/(2*a*a)+1/(6*a**3)
U3=1/(2*a*a)+1/(2*a**3)+1/(4*a**4);L3=U3-1/(12*a**6)
U4=1/(3*a**3)+1/(2*a**4)+1/(3*a**5);L4=U4-1/(6*a**7)
Kn=q*q*(q+1)**2/L*(U3-q*L4+c*(U2-2*q*L3+q*q*U4))
s=d*z/(q+1);e=s*s
J0=(1-e)**2*V0+W0+e*B10+2*e*e*al0/(L*(1-e))-QQ(3,2)*e*(1-e)*(1-s)*Kn-C0*e
J1=(1-e)**2*q*VR+q*Wp-2*d/L+e*B11+e*e*(2*(al1+L*q)/(L*(1-e))-QQ(3,2)*au*q*r)+C0*(2-h)*e
def var(s):
    a=[x for x in s if x]
    return sum(a[j]!=a[j-1] for j in range(1,len(a)))
for name,TT,DT in (
 ('Tlo',u*u*(1+TL),720*L*(q+1)**2*(q+2+c)**5*alo**3),
 ('Tup',u*u*(1+TU),12*L*(q+1)**2*(q+2+c)**3*au)):
    th=TT/(q*(2*q-(L+1)*TT));full=J0+th*J1
    NN,DD=full.numer,full.denom;Zh=DT*(2-(L+1)*TT/q)
    assert Zh.denom.degrees()==(0,0,0)
    common=L*(q+1)**6*(q+2)**7*(q+2+c)**3*(2*q+3+c)*(c**3-2*c*c+12*c+24)*((q+1)**2-d*d*z*z)
    expected=6912*common*Zh if name=='Tlo' else -11520*common*(12*alo)**3*Zh
    assert ff(DD)==expected
    sg=1 if name=='Tlo' else -1
    co=defaultdict(F)
    for (aa,bb,kk),vv in NN.items():
        vv=sg*F(vv.numerator,vv.denominator)/6**bb
        for j in range(aa+1):co[j,bb,kk]+=vv*comb(aa,j)*F(1,29)**(aa-j)*F(86,29)**j
    de=tuple(max(m[j] for m in co) for j in range(3))
    for ax in (0,1):
        groups=defaultdict(dict)
        for mo,vv in co.items():groups[mo[:ax]+mo[ax+1:]][mo[ax]]=vv
        out={}
        for key,bb in groups.items():
            for j in range(de[ax]+1):
                vv=sum((v*F(comb(j,k),comb(de[ax],k)) for k,v in bb.items() if k<=j),F())
                if vv:out[key[:ax]+(j,)+key[ax:]]=vv
        co=out
    groups=defaultdict(dict)
    for (aa,bb,kk),vv in co.items():groups[aa,bb][kk]=vv
    zs=S.symbols('z');bad=[]
    for key,bb in groups.items():
        zz=[sum((v*F(comb(j,k),comb(de[2],k)) for k,v in bb.items() if k<=j),F()) for j in range(de[2]+1)]
        if min(zz)<0:
            pp=S.Poly(sum(S.Rational(v.numerator,v.denominator)*zs**k for k,v in bb.items()),zs)
            st=pp.sturm();s0=[int(S.sign(a.eval(0))) for a in st];s1=[int(S.sign(a.eval(1))) for a in st]
            assert pp.eval(0)>0 and pp.eval(1)>0 and var(s0)==var(s1)==4
            bad.append(key);print('268 Sturm',name,key,s0,s1,flush=True)
        else:assert zz[0]>0 and zz[-1]>0
    assert (de,len(groups),len(bad))==(((29,28,7),870,7) if name=='Tlo' else ((27,30,7),868,8))
    print('268 FULL endpoint PASS',name,de,len(groups),'Sturm',len(bad),flush=True)
print('260--268 LOCAL full low-q budget PASS; independent audit PENDING',flush=True)
