"""Exact finite Laurent identities for the explicit Pa/N5 sign lemma.
A scoped algebraic/short-arithmetic check, not a full-J1 curvature verdict.
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

pa=extract(2)[1];n5=extract(5)[1]
S2,S3,S5=(Sj[j] for j in [2,3,5])
P0=11*l**10-1480*l**9+2974*l**8+8554*l**7+17367*l**6+14076*l**5+8467*l**4+1042*l**3-154*l*l-184*l-33
expected=[P0/(6*l*l*S2**5*S3**2),-(395*l**4-4108*l**3+126*l*l+152*l+35)/(2*S2**6),12*l*l*(85*l*l-21*l-2)/S2**7,-80*l**4/S2**8]
assert all(a==b for a,b in zip(pa,expected))
U17=60*l**17+360*l**16+1097*l**15+2996*l**14+6230*l**13+11121*l**12+16836*l**11+21704*l**10+24277*l**9+23038*l**8+18584*l**7+12547*l**6+6619*l**5+2788*l**4+615*l**3+53*l*l-64*l-7
V22=60*l**22+420*l**21+1697*l**20+5413*l**19+13323*l**18+27393*l**17+47762*l**16+72361*l**15+96774*l**14+115335*l**13+124023*l**12+121125*l**11+107949*l**10+87938*l**9+64598*l**8+42284*l**7+23597*l**6+10776*l**5+3553*l**4+611*l**3-97*l*l-78*l-7
assert n5[1]==2*U17/(3*l**4*S2**2*(l*l+1)**2*S3*S5**2)
assert n5[0]+n5[1]==-2*V22/(3*l**6*S2**2*(l*l+1)**2*S3**2*S5**2)
from fractions import Fraction as F
b=F(10,7)
low=F(48464,6)/(1+b)**5/(1+b+b*b)**2
assert low==F(977848604824,204293284731)
assert low-4==F(160675465900,204293284731)>0
assert 395*b-4108+126+152+35==-F(22615,7)<0
assert 2974-1480*b==F(6018,7)>0
assert 1042-154-184-33==671>0
assert 85-21-2==62>0
assert 80*F(1,4)**4==F(5,16)
assert 4-F(5,16)==F(59,16)>0
assert 615+53-64-7==597>0
assert 611-97-78-7==429>0
print('PASS all four Pa coefficients and two complete N5 identities')
print('PASS explicit positive pairings and two short rational payments')
print('Written continuous proof gives Pa>59/16 and N5<0 on full domain')
print('SCOPED: full moving-pole identity and final curvature payment audited separately')
