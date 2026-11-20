"""Exploration only: local Laurent coefficients through exact QQ(lambda) jets.
An algebraic extraction implementation, not a full-J1 sign proof.
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
for j in [4,5,2]:
 cs,coef=extract(j)
 for i,a in enumerate(coef):print("Pa" if j==2 else "N"+str(j),"COEF",i,s.factor(a.as_expr()),flush=True)
print("Candidate extraction only; not independently audited, no continuous signs asserted.")

