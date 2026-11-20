"""All assigned-v kernel identities, with v FREE and fixed actual law."""
import sympy as S
l,x,y,v,a,U,V=S.symbols('l x y v a U V')
c=l-1;t=x+y-x*y;A=c+t
bt=lambda x:x*(1-x)/l
Pc=lambda y:(1-y)*(2*v-(1+v)*y)
Pv=lambda y:(1-a)*y*y+c*((1+v)*y-v)
subs={x:c*U/(1-U),y:c*V/(1-V)}
Q=-v/c+(1+(l+1)*v/c)*V-(a+l*v/c)*V*V
checks=[
 (bt(x)*Pc(y)+bt(y)*Pc(x))/2-(1-t)*(v*t-x*y)/l,
 (v*t-x*y)/A**2-(1-t)*(v*t-x*y)/(l*A**2)-(v*t-x*y)/(l*A),
 (bt(x)*y/A**2).subs(subs)-U*V*(1-l*U)*(1-V)/(l*(1-l*U*V)**2),
 (bt(x)*Pc(y)/A**2).subs(subs)
   -U*(1-l*U)*(1-l*V)*(2*v-(c+(l+1)*v)*V)/(l*c*(1-l*U*V)**2),
 (Pv(y)/A**2).subs(subs)-(1-U)**2*Q/(1-l*U*V)**2,
]
for i,e in enumerate(checks,1):
 assert S.cancel(e)==0,i
print('5 COMPLETE FREE-v polynomial-extension identities PASS locally.')
