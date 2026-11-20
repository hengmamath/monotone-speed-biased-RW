import export_exact as EX
"""271--274 LOCAL full middle-q proof; independent audit PENDING."""
import sympy as S
from fractions import Fraction as F
from collections import defaultdict
from math import comb

def bx(co,de,axes):
 for ax in axes:
  gr=defaultdict(dict)
  for m,a in co.items():gr[m[:ax]+m[ax+1:]][m[ax]]=a
  out={}
  for key,bb in gr.items():
   for k in range(de[ax]+1):
    a=sum((v*F(comb(k,j),comb(de[ax],j)) for j,v in bb.items() if j<=k),F())
    if a:out[key[:ax]+(k,)+key[ax:]]=a
  co=out
 return co

def variation(a):
 a=[x for x in a if x]
 return sum(a[j]!=a[j-1] for j in range(1,len(a)))

# Extend the root theta upper using COMPLETE scalarT.
q,c,x,h,w=S.symbols('q c x h w');L=1+c;d=1-c*q;u=q/(q+1);b2=q/(q+2+c)
aU=1+c/2-c*c/12+c**3/24
TU=(aU*q*b2+L*L*b2*b2/2+L*L*(L*L+d)*b2**3/(12*aU*q))/L
Tg=2*q*q*(6*q+5)/(6*(q+1)+(L+1)*q*(6*q+5))
n,den=S.fraction(S.factor(((Tg-u*u-TU)/q**2).subs({q:1/x,c:h*x},simultaneous=True)))
la=1+h*x;C=h**3*x**3-2*h*h*x*x+12*h*x+24;D=1+2*x+h*x*x
assert S.expand(den-24*(1+x)**2*la*D**3*C*(5*h*x*x+6*h*x+6*x*x+16*x+12))==0
pp=S.Poly(S.expand(n.subs(x,S.Rational(1,10)+S.Rational(7,30)*w)),w,h)
de=pp.degree_list();co=bx({m:F(a)/2**m[1] for m,a in pp.terms()},de,(0,1))
assert len(co)==160 and min(co.values())==F(4899,156250)
EX.polynomial(pp,metadata={"check":"theta","coordinate":"x=1/10+7*w/30; h in [0,1/2]"})
EX.emit("bernstein",co,pp.gens,de,{"check":"theta","domain":[["0","1"],["0","1/2"]]})
print('271 COMPLETE theta upper160 PASS',flush=True)

# Full normalized tail bounds; only scalar a is bounded/differentiated.
q,c,b,i,th=S.symbols('q c b i th');L=1+c;d=1-c*q;R=q*th;r=1/(L+b);rp=(1-b)/L
al=(L*L*q+(1-th)*d*(L+1))/(q+1);aL=1+c/2-c*c/12;aU=aL+c**3/24
A=c+b*r;B=b*r
P2=A*(A+B);P3=A*(A*A+4*A*B+B*B)
P4=A*(A**3+11*B*A*A+11*B*B*A+B**3)
P5=A*(A**4+26*B*A**3+66*B*B*A*A+26*B**3*A+B**4)
TL=r/(b+c)*(aU+A/2+P2/(12*aU)-P4/(720*aU**3))
TU=r/(b+c)*(aU+A/2+P2/(12*aU))
PU=r/(L*(b+c))*((i+1)*(aU*A+P2/2+P3/(12*aU))+aU*aU-P2/12+P4/(240*aU*aU))
PL=r/(L*(b+c))*((i+1)*(aL*A+P2/2+P3/(12*aL)-P5/(720*aL**3))+aL*aL-P2/12)
boundary=2*R*(i+1)*L*r*r+2*R*r/(b+c)
VU=-(1+c*R)*TL+(1+(L+1)*R)*PU-boundary
VL=-(1+c*R)*TU+(1+(L+1)*R)*PL-boundary
tau=1-(al+L*R)*r+(L+1)*R-R/rp
BB=2*i*(al+c*R)/L+2*i*R*r*b/L+2*(i+1)*R*r*r*b+aL*(2*i-1)*tau/L
KH=BB-2*VU
KJ=VL+aL/L*(2*i-1)*al*r-aU/L*R*((2*i-1)*(1/rp-L*r)+2*L*r)/2
il=2*(d-q*b)/(2*b+c*(d-q*b));v=S.symbols('v')
for family,K,price in (('H',KH,4),('J',KJ,8)):
 AA=S.diff(K,i);CC=K.subs(i,0)
 for kind,ee in (('slope',AA),('price',il*AA+CC+price*(q*b/d)**4)):
  for ep in (0,1-1/(6*(q+1))):
   ee0=ee.subs({b:d*v/(q+2),th:ep},simultaneous=True).subs({q:1/x,c:h*x},simultaneous=True)
   n,den=S.fraction(S.factor(ee0));la=1+h*x;C=h**3*x**3-2*h*h*x*x+12*h*x+24
   M=la*(1+2*x)+(1-h)*v*x;P=1+2*x-(1-h)*v*x
   F1=(1-h)*v+h*(1+2*x);F2=(2-h)*v+h*(1+2*x);AL=h*h*x*x-6*h*x-12
   if family=='H':
    if kind=='slope':ex=(12 if ep==0 else 72)*(1+x)**(1 if ep==0 else 2)*la*C*M**4
    else:ex=(1440 if ep==0 else 8640)*(1+x)**(1 if ep==0 else 2)*(1+2*x)**4*la*F1*F2*C**3*M**5
    sg=1
   else:
    if kind=='slope':ex=(60 if ep==0 else 720)*(1+x)**(1 if ep==0 else 2)*la*AL**3*M**6
    else:ex=(720 if ep==0 else 4320)*x*(1+x)**(1 if ep==0 else 2)*(1+2*x)**4*la*AL**3*F1*F2*C*M**6
    sg=-1
   if ep!=0:ex*=P
   assert S.expand(den-ex)==0
   pp=S.Poly(S.expand(sg*n.subs(x,S.Rational(1,10)+S.Rational(7,30)*w)),w,h,v);de=pp.degree_list()
   co=bx({m:F(a)/2**m[1] for m,a in pp.terms()},de,(0,1));groups=defaultdict(dict)
   for (a,b0,k),aa in co.items():groups[a,b0][k]=aa
   EX.polynomial(pp,metadata={"family":family,"kind":kind,"theta":str(ep),"x":"1/10+7*w/30","h":["0","1/2"],"v":["0","1"]})
   EX.emit("mixed_bernstein_power",co,pp.gens,de,{"family":family,"kind":kind,"theta":str(ep)})
   EX.bernstein_from_mixed(co,de,2,{"family":family,"kind":kind,"theta":str(ep),"x":"1/10+7*w/30","h":["0","1/2"],"v":["0","1"]})
   bad=[];count=0
   for key,bb in groups.items():
    zz=[sum((aa*F(comb(k,j),comb(de[2],j)) for j,aa in bb.items() if j<=k),F()) for k in range(de[2]+1)]
    count+=sum(aa!=0 for aa in zz)
    if min(zz)<0:
     assert family=='H' and kind=='price' and ep!=0
     pp0=S.Poly(sum(S.Rational(aa.numerator,aa.denominator)*v**j for j,aa in bb.items()),v)
     while pp0.eval(0)==0:pp0=pp0.exquo(S.Poly(v,v))
     while pp0.eval(1)==0:pp0=pp0.exquo(S.Poly(1-v,v))
     st=pp0.sturm();EX.sturm(pp0,st,{"family":family,"kind":kind,"theta":str(ep),"group":list(key),"interval":["0","1"]});s0=[int(S.sign(a.eval(0))) for a in st];s1=[int(S.sign(a.eval(1))) for a in st]
     assert pp0.eval(0)>0 and pp0.eval(1)>0 and pp0.degree()==10 and variation(s0)==variation(s1)==5
     bad.append(key)
    else:assert max(zz)>0
   if bad:assert len(bad)==25
   print('271/272 ALL ages',family,kind,ep,de,count,'Sturm',len(bad),'PASS',flush=True)

# Same-e secant identity; no actual-law differentiation.
t,y=S.symbols('t y');assert S.cancel(1-t+t/(1+y)-1/(1+t*y)-t*(1-t)*y*y/((1+y)*(1+t*y)))==0
print('273 actual-marker SAME-e whole damping PASS',flush=True)

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
a=q+2

def Upp(j):return 1/((j-1)*a**(j-1))+1/(2*a**j)+QQ(j,12)/a**(j+1)
def Low(j):return Upp(j)-QQ(j*(j+1)*(j+2),720)/a**(j+3)
K6=q**4*(q+1)**2/L*(Upp(5)-q*Low(6)+c*(Upp(4)-2*q*Low(5)+q*q*Upp(6)))
K7=q**5*(q+1)**2/L*(Upp(6)-q*Low(7)+c*(Upp(5)-2*q*Low(6)+q*q*Upp(7)))
KJ=q**4*(q+1)**2/L*(Upp(4)-2*q*Low(5)+q*q*Upp(6)+c*(Upp(3)-3*q*Low(4)+3*q*q*Upp(5)-q**3*Low(6)))
s=d*z/(q+1);e=s*s
J0=(1-e)**2*V0+W0+e*B10+2*e*e*al0/(L*(1-e))-4*e*(1+s)*((1-q*s/(1-s))*K6+q*s/(1-s)*K7)-8*e*e*KJ-C0*e
J1=(1-e)**2*q*VR+q*Wp-2*d/L+e*B11+e*e*(2*(al1+L*q)/(L*(1-e))-QQ(3,2)*au*q*r)+C0*(2-h)*e
for name,TT,DT in (
 ('Tlo',u*u*(1+TL),720*L*(q+1)**2*(q+2+c)**5*alo**3),
 ('Tup',u*u*(1+TU),12*L*(q+1)**2*(q+2+c)**3*au)):
 theta=TT/(q*(2*q-(L+1)*TT));full=J0+theta*J1;NN,DD=full.numer,full.denom
 Zh=DT*(2-(L+1)*TT/q)
 base=L*(q+1)**6*(q+2)**10*(q+2+c)**3*(2*q+3+c)*(c**3-2*c*c+12*c+24)*((q+1)**2-d*d*z*z)
 expected=34560*base*Zh if name=='Tlo' else -11520*base*(12*alo)**3*Zh
 assert ff(DD)==expected;sg=1 if name=='Tlo' else -1
 power=max(m[0]-m[1] for m in NN);co=defaultdict(F)
 for (aa,bb,kk),vv in NN.items():
  k=power+bb-aa;vv=sg*F(vv.numerator,vv.denominator)/2**bb
  for j in range(k+1):co[j,bb,kk]+=vv*comb(k,j)*F(1,10)**(k-j)*F(7,30)**j
 de=tuple(max(m[j] for m in co) for j in range(3));co=bx(co,de,(0,1,2))
 assert min(co.values())>0
 EX.emit("budget_input_power",NN.items(),("q","c","z"),NN.degrees(),{"endpoint":name,"sign":sg,"x_power":power})
 EX.emit("bernstein",co,("x_box","h_box","z"),de,{"endpoint":name,"x":["1/10","1/3"],"h":["0","1/2"],"z":["0","1"]})
 assert (power,de,len(co))==((28,(49,28,6),10150) if name=='Tlo' else (26,(49,30,6),10850))
 print('274 COMPLETE same-e budget',name,power,de,len(co),'positive, min',min(co.values()),flush=True)
print('271--274 LOCAL full middle-q PASS; independent audit PENDING',flush=True)
