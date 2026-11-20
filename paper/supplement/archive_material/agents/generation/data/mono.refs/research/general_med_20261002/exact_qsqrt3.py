"""Exact arithmetic in Q(sqrt(3)); no floating-point comparisons."""
from fractions import Fraction as F
from dataclasses import dataclass
@dataclass(frozen=True)
class Q3:
 a:F=F(0)
 b:F=F(0)
 def __init__(self,a=0,b=0):
  object.__setattr__(self,'a',F(a));object.__setattr__(self,'b',F(b))
 @staticmethod
 def co(x):return x if isinstance(x,Q3) else Q3(x)
 def __add__(self,x):
  x=self.co(x);return Q3(self.a+x.a,self.b+x.b)
 __radd__=__add__
 def __neg__(self):return Q3(-self.a,-self.b)
 def __sub__(self,x):return self+-self.co(x)
 def __rsub__(self,x):return self.co(x)+-self
 def __mul__(self,x):
  x=self.co(x);return Q3(self.a*x.a+3*self.b*x.b,self.a*x.b+self.b*x.a)
 __rmul__=__mul__
 def inv(self):
  den=self.a*self.a-3*self.b*self.b
  assert den;return Q3(self.a/den,-self.b/den)
 def __truediv__(self,x):return self*self.co(x).inv()
 def __rtruediv__(self,x):return self.co(x)*self.inv()
 def __pow__(self,n):
  if n<0:return self.inv()**(-n)
  out=Q3(1);base=self
  while n:
   if n%2:out=out*base
   n//=2
   if n:base=base*base
  return out
 def sign(self):
  a,b=self.a,self.b
  if not b:return (a>0)-(a<0)
  if not a:return (b>0)-(b<0)
  if a>0 and b>0:return 1
  if a<0 and b<0:return -1
  diff=a*a-3*b*b
  return ((diff>0)-(diff<0))*(1 if a>0 else -1)
 def __lt__(self,x):return (self-self.co(x)).sign()<0
 def __le__(self,x):return (self-self.co(x)).sign()<=0
 def __gt__(self,x):return (self-self.co(x)).sign()>0
 def __ge__(self,x):return (self-self.co(x)).sign()>=0
 def __abs__(self):return self if self.sign()>=0 else -self

