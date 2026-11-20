"""V2 handles absent regular pole powers as zero (initial KeyError preserved).
LOCAL transparency: both J3 slabs, ten coefficient and two endpoint payments.
Pure stdlib Fraction finite coefficient multiplication/inversion; no symbolic
package, old certificate imports/execution, parameter samples, or sign tables.
The continuous comparison and curvature identities remain separately audited.
"""
from fractions import Fraction as F
from math import comb
N=5
class J:
 def __init__(self,a):self.a=(list(map(F,a))+[F(0)]*N)[:N] if isinstance(a,list) else [F(a)]+[F(0)]*(N-1)
 @staticmethod
 def get(a):return a if isinstance(a,J) else J(a)
 def __add__(self,b):
  b=self.get(b);return J([a+c for a,c in zip(self.a,b.a)])
 __radd__=__add__
 def __neg__(self):return J([-a for a in self.a])
 def __sub__(self,b):return self+-self.get(b)
 def __rsub__(self,b):return self.get(b)+-self
 def __mul__(self,b):
  b=self.get(b);return J([sum((self.a[k]*b.a[i-k] for k in range(i+1)),F(0)) for i in range(N)])
 __rmul__=__mul__
 def inverse(self):
  b=[1/self.a[0]]
  for i in range(1,N):b.append(-sum((self.a[k]*b[i-k] for k in range(1,i+1)),F(0))/self.a[0])
  return J(b)
 def __truediv__(self,b):return self*self.get(b).inverse()
 def __rtruediv__(self,b):return self.get(b)*self.inverse()
 def __pow__(self,k):
  if k<0:return self.inverse()**(-k)
  out=J(1)
  for _ in range(k):out=out*self
  return out
spec=[(2,1,F(1),F(3,8)),(3,3,F(169,36),F(12,25)),(4,6,F(2601,256),F(7,13))]
a=F(5,6);d=F(1,2)
def data(l,j,n,dd,gg,u):
 t=1-u;A=1+l*t;Z={i:1+t*sum((l**v for v in range(1,i)),F(0)) for i in range(1,6)}
 r=Z[j]/Z[j+1];ff=2-r-l*r*r
 K=(l+1)/(2*l)+t/2+(l+1)*(2*l*t-l+1)*t/(24*l)
 cc=-3+2*a*n+a*a*dd;dc=-6+a*(1+2*n*(1+a))+a**3*dd
 g=6*n+4-a*dd+(a*dd-cc)*u+(cc-dc)*u/A
 hh=-6+a*(1+2*n*(1+a));bk=3*n+4-gg*(6*n+4);bh=6-a*(1+n*(1+a))+gg*hh;br=gg*a*dd
 LK=bk+bh+br*a*a;Lt=br*(1-a*a)-bh
 return ff,g,K,LK,Lt

def pol(p,x):
 out=J(0)
 for c in reversed(p):out=out*x+c
 return out

def tangent(q):return J([q.a[0]-d*q.a[1],q.a[1]])

def slab(ell,H,constant,bounds):
 # These are polynomials in the global coordinate u, stored as finite vectors.
 fs,gs,Ls={},{},{}
 for j,n,dd,gg in spec:
  fh,gh,kh,LK,Lt=data(H,j,n,dd,gg,J([d,1]))
  fs[j]=tangent(fh)
  if j==2:fs[j]-=(J([0,1])-d)**2/16
  if j==2:
   g0=data(ell,j,n,dd,gg,J(0))[1].a[0];gd=data(ell,j,n,dd,gg,J(d))[1].a[0]
   gs[j]=J([g0,(gd-g0)/d])
  else:gs[j]=tangent(gh)
  Ls[j]=LK*tangent(kh)+Lt*J([1,-1])
 S={j:sum((ell**i for i in range(j)),F(0)) for j in range(1,5)}
 q={j:1-1/S[j] for j in [2,3,4]};rho=q[2]
 def at(p,u):return pol(p.a,u)
 def regular(j,u):
  A=1+ell*(1-u);Z={i:1+(1-u)*(S[i]-1) for i in range(1,5)}
  P={i:at(fs[i],u)*at(gs[i],u) for i in [2,3,4]};L={i:at(Ls[i],u) for i in [2,3,4]}
  if j==2:return {2:-4*P[2],1:4*u*L[2]}
  if j==3:return {3:-6*ell*A*P[3],2:6*ell*u*L[3],1:8*ell**2*u*A*L[4]/Z[4]**2}
  if j==4:return {3:-8*ell**2*A*P[4],2:8*ell**2*u*A*L[4]/Z[3]}
  raise ValueError(j)
 c={}
 for j in [2,3,4]:
  ms=regular(j,J([1/q[j],1]));m=max(ms)
  for r in range(1,m+1):
   c[j,r]=sum((ms[v].a[v-r]/(S[j]**v*(-q[j])**(v-r)) for v in ms if v>=r),F(0))
 y=J([0,1]);delta={j:q[j]-rho for j in [3,4]};gap=q[4]-q[3]
 Ap=rho*rho*(c[2,1]+3*c[2,2]*(1+rho*y))
 np={j:c[j,1]*(1-delta[j]*y)**2+3*c[j,2]*(1-delta[j]*y)*(1+rho*y)+6*c[j,3]*(1+rho*y)**2 for j in [3,4]}
 B=q[3]**2*np[3]+q[4]**2*np[4]*(1+5*gap*y+(5*gap*delta[4]+10*gap**2)*y*y)
 def G(v):
  u=J(v);A=1+ell*(1-u);Z={i:1+(1-u)*(S[i]-1) for i in range(1,5)};out=J(constant)
  for j in [2,3,4]:
   out+=2*j*ell**(j-2)*A*(-at(fs[j],u)*at(gs[j],u)/Z[j]**3+u*at(Ls[j],u)/(Z[j]**2*Z[j-1]))
  return out.a[0]
 names=['A0','A1','N40','N41','N42','b0','b1','b2','b3','b4','G0','Ghalf']
 vals=Ap.a[:2]+np[4].a[:3]+B.a[:5]+[G(0),G(d)]
 assert len(vals)==len(bounds)==12
 assert d/(1-rho*d)<F(7,10) and delta[3]>F(1,7) and gap>0
 print('SLAB',str(ell),str(H),'constant',constant)
 print('complete normalized pole coefficients',[(str(k),str(v)) for k,v in c.items()])
 for name,v,th in zip(names,vals,bounds):
  dg=th-v if name not in ['G0','Ghalf'] else v-th
  assert dg>0
  print(name,'value',str(v),'bound',str(th),'strict_positive_gap',str(dg))
 print('LOCAL exact twelve finite payments; continuous proof still uses separately audited identities')
 return {'ell':str(ell),'H':str(H),'constant':constant,'poles':{str(k):str(v) for k,v in c.items()},'rows':[{'name':name,'value':str(v),'bound':str(th),'gap':str(th-v if name not in ['G0','Ghalf'] else v-th),'direction':'<' if name not in ['G0','Ghalf'] else '>'} for name,v,th in zip(names,vals,bounds)]}

if __name__=='__main__':
 import json
 rows=[slab(F(23,20),F(5,4),19,[F(9,5),F(2),F(-26),F(18),F(0),F(-14,5),F(0),F(-1),F(1),F(0),F(1,20),F(1)]),slab(F(5,4),F(10,7),20,[F(11,10),F(3,2),F(-22),F(14),F(0),F(-49,10),F(-2),F(-9,5),F(2,3),F(-1,2),F(2),F(3,20)])]
 from pathlib import Path
 out=Path(__file__).with_suffix('.exact_rows.json');assert not out.exists();out.write_text(json.dumps(rows,indent=2)+'\n')
 print('PASS local 24 exact Fraction payments; no fresh full-J3 independent verdict')
