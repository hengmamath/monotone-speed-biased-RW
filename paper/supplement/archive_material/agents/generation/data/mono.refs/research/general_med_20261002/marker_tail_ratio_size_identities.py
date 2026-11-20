"""ALL-tail actual speed-deficit SIZE, no individual complete-price sign."""
import sympy as S
l,h,d,x,Y,u,K,T,b0,b1,r0,r1,V=S.symbols('l h d x Y u K T b0 b1 r0 r1 V')
c=l-1;beta=h/(x-d);bn=h/(l*x-d);bp=h/(x/l-d);Qp=h/c
count=0
def eq(name,left,right):
    global count
    assert S.cancel(left-right)==0,name
    count+=1;print('PASS:',name)
eq('EXACT full cap Q age telescope',x/l*beta*bp,Qp*(bp-beta))
eq('ALL-i adjacent tail-ratio difference',
   (x*bn*bn+Y)/beta-Y/bn,x*(bn*bn/beta-Y/Qp))
eq('EXACT root gap from ENTIRE kappa',
   (T/u-u-T).subs(T,u*u*K/(1-u)),u*(K-1))
eq('ALL actual speed-deficit SIZE including positive remainder',
   (r0+r1)*V-T*(b0*r0+b1*r1),
   b0*(r0+r1)*(V/b0-T)+T*(b0-b1)*r1)
print(count,'exact all-tail SIZE identities PASS; monotonicity proof in manuscript.')
print('Actual complete signed defect prices may be negative;165 OPEN.')
