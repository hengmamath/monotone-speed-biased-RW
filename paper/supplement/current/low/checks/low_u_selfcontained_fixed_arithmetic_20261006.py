import export_exact as EX
"""Only the displayed fixed rational arithmetic; no old guard or scan."""
from fractions import Fraction as F
import sys
if sys.flags.optimize: raise RuntimeError('optimize=0 required')
S=10**6
ls=(F(6,5),F(23,20),F(11,10))
w=[(1000000,1000000,1000000,1000000),(247933,248783,249433,454545),(108682,109675,110440,274725),(59967,60996,61795,186289),(37444,38473,39281,134379),(25235,26248,27053,100705),(17899,18886,19682,77423),(13162,14117,14900,60609)]
def f(l,n): return l**(n-1)*(l-1)**2/(l**n-1)**2
def floor(x): return x.numerator*S//x.denominator
def ceil(x): return -((-x.numerator*S)//x.denominator)
def tau(l):
 c=l-1; L=c-c*c/2+c*c*c/3
 return c*c/(l*L*(l**9-1))+f(l,9)/2
for n,row in enumerate(w,1):
 assert tuple(floor(f(l,n)) for l in ls)==row[:3]
 assert floor((ls[0]-1)/(ls[0]**n-1))==row[3]
tails=[floor(tau(l)) for l in ls]
assert tails==[48837,60981,76035]
l=ls[1]; c=l-1; z=l**(-8); a=2*c/(l+1)
E=c**4*z*z/(6*l*l)*(8/a*(3-z)/(1-z)**3+1/(a*a)*((2-z)/(1-z)**2-F(1,2)))
assert ceil(E)==4545
assert [sum(r[j] for r in w)+tails[j] for j in range(3)]==[1559159,1578159,1598619]
A=sum(F(r[0],S)*(1-F(1,n)) for n,r in enumerate(w,1))+F(8,9)*F(tails[0],S)
C=sum(F(1,n**3)*(1-F(r[3],S)) for n,r in enumerate(w,1))+F(1,128)
H=sum(n*F(r[1]+1,S)**2 for n,r in enumerate(w,1))+F(4545,S)
assert floor(A)==362650 and ceil(C)==131184 and ceil(H)==1194930
assert sum(F(1,n**3) for n in range(1,7))+F(1,72)==F(86701,72000)
coef=F(1984,3615)-F(90,79)*F(6,5)/16*(F(64,9)-F(15,16))
K=coef*F(79,90)*F(5,6)
assert coef==F(389899,18277440) and K==F(389899,24986880)
def boundary(L,H): return F(15,16)*(L+F(9,200))**2-2*(H+F(2,15)*(F(16,15)**3-1))
assert [boundary(L,H) for L,H in [(F(19,12),F(241,200)),(F(63,40),F(241,200)),(F(1559,1000),F(239,200))]]==[F(973799,51840000),-F(21361,3240000),-F(566237,16200000)]
A1=F(10,9261); A2=F(180,79507)
assert K>2*A2>2*A1
assert A1-F(21361,3240000)/16==F(11873177,17781120000)>0
assert A2-F(566237,16200000)/16==F(1636194841,20608214400000)>0
print('PASS all fixed rational checks; native optimize=0')

EX.emit("prefix_floor_table",[((n,j),value) for n,row in enumerate(w,1) for j,value in enumerate(row)],("age","column"),(8,3),{"unit":"1/1000000","columns":["f(6/5)","f(23/20)","f(11/10)","B(6/5)"]})
EX.emit("exact_scalar_values",[((j,),v) for j,v in enumerate(tails+[E,A,C,H,coef,K])],("index",),(8,),{"fields":["tau6_floor","tau23_floor","tau11_floor","E23","A_lower","C_upper","H_upper","Cstar","K0"]})
