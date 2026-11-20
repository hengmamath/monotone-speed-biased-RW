"""Generate exact near-region rational sign obligations in QQ(lambda,u)."""
import pickle
import json
import time
from pathlib import Path
import sympy as sp

OUT=Path(__file__).with_name('near_arithmetic_data');OUT.mkdir(exist_ok=True)
field,L,u=sp.field('lambda,u',sp.QQ)
ls,us=sp.symbols('lambda u')
rat=sp.QQ
c=L-1;k=1-L*u
Z={s:1+(1-u)*sum(L**i for i in range(1,s)) for s in range(1,6)}
A=Z[2];r={s:Z[s]/Z[s+1] for s in range(1,5)}
K=(L+1)/(2*L)+(1-u)/2+(L+1)*(2*L*(1-u)-L+1)*(1-u)/(24*L)
eta=K-1+u
Qc=[A*(1-u),L*u*(1-u),u];Rc=[1-u,field.zero,eta]
E=[A**2*(1-u),A*(1-u)*(2*L*u-1),2*A*u-L*(1-u)-A**2*eta,-u*(1+L**2*(1-u)/A),L*u*(eta-1/A),field.zero]
qr=[2/L*(E[i]-(L*E[i-1]/A if i else 0)) for i in range(6)]
omega={s:s*L**(s-2)*k/Z[s]**3 for s in range(2,5)}
n={s:s*(s-1)//2 for s in range(2,5)}
uc={s:[omega[s]*(Qc[i]*(2-r[s]-L*r[s]**2)+u*A*L*r[s]**2*Rc[i]) for i in range(3)] for s in range(2,5)}
vc={s:[omega[s]*u*A*Rc[i]/r[s-1] for i in range(3)] for s in range(2,5)}
bc={s:[2*uc[s][i]-vc[s][i] for i in range(3)] for s in range(2,5)}
psic=[qr[i]+(2*sum(uc[s][i-1]-vc[s][i-1] for s in range(2,5)) if 1<=i<=3 else 0) for i in range(6)]
p=sum(psic)
cc=[-sum(psic[j] for j in range(i+1,6))-(2*sum(n[s]*bc[s][i-1] for s in range(2,5)) if 1<=i<=3 else 0) for i in range(5)]
C0=sum(cc)
def ev(coeffs,x):return sum(a*x**i for i,a in enumerate(coeffs))
Hc=[-cc[2]-cc[3]-cc[4],-cc[3]-cc[4],-cc[4]]
b=rat(5,3)*(2*ev(bc[3],rat(5,6))+rat(27,4)*ev(bc[4],rat(5,6)))
j=rat(5,3)*(ev(uc[2],rat(5,6))+rat(169,36)*ev(uc[3],rat(5,6))+rat(2601,256)*ev(uc[4],rat(5,6)))
Ka=cc[0]-C0+rat(5,6)*ev(Hc,rat(5,6))

# Coefficients of every numerator and denominator are exact rational numbers.
def save(name,expr,box):
    start=time.time()
    ne,de=expr.numer.as_expr(),expr.denom.as_expr()
    denvalue=de.subs({ls:(sp.Rational(box[0])+sp.Rational(box[1]))/2,us:(sp.Rational(box[2])+sp.Rational(box[3]))/2})
    assert denvalue!=0
    if denvalue<0:ne,de=-ne,-de
    pn,pd=sp.Poly(ne,ls,us),sp.Poly(de,ls,us)
    mult=sp.ilcm(*(sp.denom(x) for x in pn.coeffs()+pd.coeffs()))
    pn=sp.Poly(pn.as_expr()*mult,ls,us);de=sp.expand(de*mult)
    item={'name':name,'num':pn.as_expr(),'den':de,'box':box}
    with (OUT/(name+'.pickle')).open('wb') as f:pickle.dump(item,f)
    print(name,pn.degree_list(),len(pn.terms()),'den',sp.factor(de),'seconds',round(time.time()-start,2),flush=True)

if __name__=='__main__':
    F=(25*p+C0)/(k*A)
    print('objects built',flush=True)
    save('j1_curvature',-F.diff(u).diff(u),['23/20','707/500','0','1/2'])
    F0=field.from_expr(F.as_expr().subs(us,0));Fh=field.from_expr(F.as_expr().subs(us,sp.Rational(1,2)))
    save('j1_left_derivative',F0.diff(L)-rat(1,4),['23/20','707/500','0','1/2'])
    save('j1_right_derivative',Fh.diff(L),['23/20','707/500','0','1/2'])
    save('j2',4*b+3*C0,['23/20','3/2','0','1/2'])
    save('j3',Ka+j+4*C0-k/20,['23/20','10/7','0','1/2'])
    save('t1',p-rat(1,1000),['15/13','707/500','0','1/2'])
    def Fslice(x):return ev(qr,x)-4*x*x*u*k*ev(Rc,x)/A
    def gslice(x):return k*ev(Qc,x)/A**3
    F34=Fslice(rat(3,4));F56=Fslice(rat(5,6));g34=gslice(rat(3,4))
    save('rho34_u_derivative',-F34.diff(u),['23/20','3/2','0','1/2'])
    save('rho34_endpoint',field.from_expr(F34.as_expr().subs(us,sp.Rational(1,2)))-rat(1,8),['23/20','3/2','0','1/2'])
    save('rho56_u_derivative',-F56.diff(u),['23/20','3/2','0','1/2'])
    save('rho56_g_derivative',-g34.diff(u),['23/20','3/2','0','1/2'])
    save('rho56_quarter',field.from_expr(F56.as_expr().subs(us,sp.Rational(1,4))),['23/20','3/2','0','1/2'])
    save('rho56_mixed',field.from_expr((F56+rat(27,32)*g34).as_expr().subs(us,sp.Rational(1,2)))-rat(1,100),['23/20','3/2','0','1/2'])
    save('core_c2',-cc[2],['23/20','10/7','0','1/2'])
    save('core_c34',-(cc[3]+4*cc[4])/u,['23/20','10/7','0','1/2'])
    for s in range(2,5):
        save('age%d_constant'%s,bc[s][0],['23/20','10/7','0','1/2'])
        save('age%d_quadratic'%s,bc[s][2]/u,['23/20','10/7','0','1/2'])
    objs={'F':F,'qr':qr,'Qc':Qc,'Rc':Rc,'K':K,'eta':eta,'uc':uc,'vc':vc,'p':p,'cc':cc,'Hc':Hc,'C0':C0,'b':b,'j':j,'Ka':Ka}
    def exprs(v):
        if isinstance(v,list):return [exprs(x) for x in v]
        if isinstance(v,dict):return {k:exprs(x) for k,x in v.items()}
        return v.as_expr()
    with (OUT/'objects.pickle').open('wb') as f:pickle.dump(exprs(objs),f)
    left=F0.as_expr().subs(ls,sp.Rational(23,20))-sp.Rational(57,100)
    right=Fh.as_expr().subs(ls,sp.Rational(23,20))-sp.Rational(21,25)
    assert left>0 and right>0
    (OUT/'j1_endpoints.json').write_text(json.dumps({'J1(23/20,0)-57/100':str(left),'J1(23/20,1/2)-21/25':str(right)},indent=2))
    print('j1 exact endpoint margins',left,right,flush=True)
