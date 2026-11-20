"""LOCAL V2: correction of the three inverse powers in the B3 bound.
The auxiliary authored only this correction; the lead independently reviews it.
All other mathematical content remains the original lead-authored proof.
LOCAL exact identities and short continuous payments for b4<5.
The own QQ(lambda) four-jet reconstructs Pa,N3,N5 from the full audited
root/three-age pole decomposition. No old scalar certificate is executed.
Natural low-degree coefficient structures are explicit computational inputs.
"""
import sympy as s
from sympy.polys.domains import QQ
field=QQ.frac_field("l");l=field.gens[0];m=4
def cv(v):return field.convert(v)
class Jet:
 def __init__(self,v):self.v=(list(v)+[cv(0)]*m)[:m] if isinstance(v,list) else [cv(v)]+[cv(0)]*(m-1)
 @staticmethod
 def get(a):return a if isinstance(a,Jet) else Jet(a)
 def __add__(self,a):
  a=self.get(a);return Jet([x+y for x,y in zip(self.v,a.v)])
 __radd__=__add__
 def __neg__(self):return Jet([-x for x in self.v])
 def __sub__(self,a):return self+-self.get(a)
 def __rsub__(self,a):return self.get(a)+-self
 def __mul__(self,a):
  a=self.get(a);return Jet([sum((self.v[j]*a.v[i-j] for j in range(i+1)),cv(0)) for i in range(m)])
 __rmul__=__mul__
 def inverse(self):
  vv=[1/self.v[0]]
  for i in range(1,m):vv.append(-sum((self.v[j]*vv[i-j] for j in range(1,i+1)),cv(0))/self.v[0])
  return Jet(vv)
 def __truediv__(self,a):return self*self.get(a).inverse()
 def __rtruediv__(self,a):return self.get(a)*self.inverse()
 def __pow__(self,n):
  if n<0:return self.inverse()**(-n)
  out=Jet(1)
  for _ in range(n):out=out*self
  return out
Sj={j:sum((l**i for i in range(j)),cv(0)) for j in range(1,6)}
rho=l/Sj[2]
def extract(j):
 q=(Sj[j]-1)/Sj[j];u=Jet([Sj[j]/(Sj[j]-1),cv(1)]);t=1-u
 Z={i:1+t*(Sj[i]-1) for i in range(1,6)};A=Z[2];k=1-l*u
 K=(l+1)/(2*l)+t/2+(l+1)*(2*l*t-l+1)*t/(24*l);h=K-t
 P=lambda n:24-2*n-u*(A+1)/A
 if j==4:
  sm={3:16*l*l*P(6),
   2:8*l*l*(-P(6)/Z[5]+u*(-18*K+2*h)/Z[3])+6*l*l*(u*(18*K-2*h)-P(3))/Z[3],
   1:8*l**3*(u*(12*K-2*h)-P(6))/Z[5]**2-6*l*P(3)/Z[3]**2}
 elif j==3:
  sm={3:12*l*P(3),
   2:6*l*(-P(3)/Z[4]+u*(-21*K+2*h)/A)+4*l*(u*(22*K-2*h)-P(1))/A,
   1:6*l*l*(u*(18*K-2*h)-P(3))/Z[4]**2-4*P(1)/A**2+8*l*l*u*(-18*K+2*h)/Z[4]**2}
 elif j==5:
  sm={2:8*l**3*(u*(12*K-2*h)-P(6))/Z[4],
      1:-8*l*l*P(6)/Z[4]**2}
 elif j==2:
  price=25+l/k
  R2=2/l*(price*(-l+K*l*u)+u+2*l+l*u-2*(h+K)*l*u)
  R1=2/l*(-price-u+1)
  sm={4:-8*u,3:2*u+8*(22-u)+4*u/Z[3],
   2:R2-4*(22-u)/Z[3]+4*l*u/Z[3]**2+4*u*(-23*K+2*h),
   1:R1+4*l*(u*(22*K-2*h)-22+u)/Z[3]**2
    +6*l*(-2*u/Z[3]**3+u/(Z[3]**2*Z[4])+l*u/(Z[3]*Z[4]**2)+u*(-21*K+2*h)/Z[3]**2)
    +8*l*l*(-2*u/Z[4]**3+u/(Z[4]**2*Z[5])+l*u/(Z[4]*Z[5]**2))}
 else:raise ValueError(j)
 order=max(sm)
 cs={r:sum((sm[v].v[v-r]/(Sj[j]**v*(-q)**(v-r)) for v in range(r,order+1)),cv(0)) for r in range(1,order+1)}
 # y polynomials: calculate with same jet arithmetic, of degree<=3.
 dy=Jet([cv(1),-(q-rho)]);py=Jet([cv(1),rho])
 np=sum((s.Rational(r*(r+1),2)*Jet(cs[r])*dy**(order-r)*py**(r-1) for r in cs),Jet(0))
 coeff=[a*rho*rho if j==2 else a for a in np.v[:order]]
 return cs,coeff


from fractions import Fraction as F
ls=s.Symbol('l');a=s.Rational(23,20);H=s.Rational(707,500)
S2,S3,S4,S5=(Sj[j] for j in [2,3,4,5]);L2=1+l*l
q3,q4,q5=(1-1/Sj[j] for j in [3,4,5]);D=q4-rho;z=q5-q4
Pa=extract(2)[1];N3=extract(3)[1];N5=extract(5)[1]
Ba=-5*D*Pa[3]+10*D*D*Pa[2]-5*D**3*Pa[1]
B3=q3*q3*N3[2]/20
B5=10*q5*q5*z*z*(D+2*z)*N5[1]-4*q5*q5*D*z*(D*D+5*D*z+5*z*z)*N5[0]
def poly(v):
 out=cv(0)
 for x in reversed(v):out=out*l+x
 return out
def same(a,b):assert a==b
Ulist=[-7,-64,53,615,2788,6619,12547,18584,23038,24277,21704,16836,11121,6230,2996,1097,360,60]
Vlist=[-7,-78,-97,611,3553,10776,23597,42284,64598,87938,107949,121125,124023,115335,96774,72361,47762,27393,13323,5413,1697,420,60]
U,V=poly(Ulist),poly(Vlist);W=V+l*l*S3*U
T=q5*q5*N5[1];C=-q5*q5*N5[0]
same(T,2*U/(3*l*l*S3*S5**4));same(C,2*W/(3*l**4*S3**2*S5**4))
Q4=4635*l**4-5116*l**3+4430*l*l-856*l+99
P6=3473*l**6+15981*l**5+7141*l**4-5297*l**3+184*l*l+132*l-88
same(Ba,5*l**6*Q4/(2*S2**9*L2**3));same(B3,l*P6/(240*S2*S3**5))
same(B5,10*z*z*(D+2*z)*T+4*D*z*(D*D+5*D*z+5*z*z)*C)
print('PASS five complete original-F b4 part/weighted N5 identities')
expr=lambda x:x.as_expr()
coeff=lambda x:s.Poly(expr(x),ls)
Uc,Vc,Wc=map(expr,[U,V,W]);GU=12*Uc-ls*s.diff(Uc,ls)-84*(ls-1)-788*(ls**3-ls)
GW=15*Wc-ls*s.diff(Wc,ls)-105*(ls-1)-1197*(ls**3-ls)-1352*(ls**3-ls**2)
for name,g,k in [('GU',GU,12),('GW',GW,15)]:
 pol=s.Poly(g,ls);v=[pol.nth(i) for i in range(pol.degree()+1)]
 low=2 if name=='GU' else 3
 assert all(x==0 for x in v[:low]) and all(x>0 for x in v[low:k]) and v[k]==0 and all(x<0 for x in v[k+1:])
 print(name,'complete ascending coefficients',v)
 # g/lambda^k strictly decreases: low positive powers have negative exponents,
 # high negative powers have positive exponents. Its endpoint is positive.
 assert g.subs(ls,H)>0

def val(x,t):return s.cancel(expr(x).subs(ls,t))
def payment(name,g):
 g=s.cancel(g);assert g>0;print('PAYMENT',name,str(g))
for name,g in [('GU_H',GU.subs(ls,H)),('GW_H',GW.subs(ls,H))]:payment(name,g)
ss3,ss5=map(expr,[S3,S5])
mu3=ls*s.diff(ss3,ls)/ss3;mu5=ls*s.diff(ss5,ls)/ss5
payment('denT_mean_at_lo_minus12',(2+mu3+4*mu5-12).subs(ls,a))
payment('denC_mean_at_lo_minus15',(4+2*mu3+4*mu5-15).subs(ls,a))
payment('39_minus_Tlo',39-val(T,a));payment('121_minus_Clo',121-val(C,a))
# Finite weighted variance of the positive S_j coefficients implies mu_j is
# nondecreasing. Together with GU/GW this proves T,C strictly decreasing.
VV=s.expand(((6*(1+ls)*(1+ls*ls)-9*ls*(1+ls*ls)-6*ls*ls*(1+ls))*(4635*ls**4-5116*ls**3+4430*ls**2-856*ls+99)+ls*(1+ls)*(1+ls*ls)*(18540*ls**3-15348*ls**2+8860*ls-856)))
c=s.Symbol('c');Vshift=s.Poly(VV.subs(ls,1+c),c)
v7=[25632,84160,87472,-47624,-219142,-232982,-112989,-23175]
assert [Vshift.nth(i) for i in range(8)]==v7
assert s.cancel(s.diff(expr(Ba),ls)-5*ls**5*VV/(2*(1+ls)**10*(1+ls*ls)**4))==0
payment('V7_shift_at_H_minus1',Vshift.as_expr().subs(c,H-1))
payment('16over5_minus_BaH',s.Rational(16,5)-val(Ba,H))
# V7(c)/c^3 strictly decreasing by the displayed three-positive/five-negative
# coefficients. Thus V7>0 and Ba increases through the entire closed interval.
corrected_B3_upper=(3473*ls**2+15981*ls+7141-5297/ls+184/ls**2+132/ls**3-88/ls**4)/(58320*(1+ls))
assert s.cancel(corrected_B3_upper-expr(P6)/(58320*(1+ls)*ls**4))==0
print('PASS V2 corrected P6/lambda^4 low-power identity')
aF,bF=F(23,20),F(10,7)
M3=(3473*bF*bF/(1+bF)+15981*bF/(1+bF)+7141/(1+aF)-5297/(bF*(1+bF))+184/(aF**2*(1+aF))+132/(aF**3*(1+aF))-88/(bF**4*(1+bF)))/F(240*243)
assert M3==F(552936326634983,2269323746550000)
assert F(1,4)-M3==F(14394610002517,2269323746550000)
payment('1over4_minus_M3',s.Rational((F(1,4)-M3).numerator,(F(1,4)-M3).denominator))
# z<5/96: R=5*S4*S5-96*lambda^4. Strong-convexity lower quadratic
# at c=3/20 is positive at its minimum, throughout c>=3/20.
R=s.expand(5*expr(S4)*expr(S5)-96*ls**4).subs(ls,1+c).expand()
r7=[4,-34,24,241,324,180,45,5]
assert [s.Poly(R,c).nth(i) for i in range(8)]==r7
ca=s.Rational(3,20);M2=48+1446*ca+3888*ca*ca
R0=R.subs(c,ca);R1=s.diff(R,c).subs(c,ca)
print('z_quadratic_data R0 R1 M2',R0,R1,M2)
payment('z_lower_quadratic_minimum',R0-R1*R1/(2*M2))
# D increases: numerator lambda*(2+lambda-lambda^3)>0 for lambda<3/2.
DD=expr(D)
assert s.cancel(s.diff(DD,ls)-ls*(2+ls-ls**3)/((1+ls)**2*(1+ls*ls)**2))==0
assert DD.subs(ls,s.Rational(10,7))==s.Rational(700,2533)
dF,zF=F(700,2533),F(5,96)
M5=10*zF*zF*(dF+2*zF)*39+4*dF*zF*(dF*dF+5*dF*zF+5*zF*zF)*121
assert M5==F(5501385534664375,3594672069009408)
gap5=F(31,20)-M5
payment('31over20_minus_M5',s.Rational(gap5.numerator,gap5.denominator))
assert s.Rational(16,5)+s.Rational(1,4)+s.Rational(31,20)==5
print('PASS continuous proof b4=Ba+B3+B5<16/5+1/4+31/20=5')
print('LOCAL author exact execution; separate independent audit is required')
