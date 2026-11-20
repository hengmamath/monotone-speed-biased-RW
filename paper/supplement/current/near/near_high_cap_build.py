"""Finite cap and high-u arithmetic, reconstructed from displayed formulas."""
from pathlib import Path
import json
import pickle
import sympy as sp

OUT=Path(__file__).with_name('near_arithmetic_data')
field,L,u=sp.field('lambda,u',sp.QQ)
ls,us=sp.symbols('lambda u');rat=sp.QQ

def save(name,expr,box,second='u'):
    ne,de=expr.numer.as_expr(),expr.denom.as_expr()
    value=de.subs({ls:(sp.Rational(box[0])+sp.Rational(box[1]))/2,us:(sp.Rational(box[2])+sp.Rational(box[3]))/2})
    assert value!=0
    if value<0:ne,de=-ne,-de
    pn,pd=sp.Poly(ne,ls,us),sp.Poly(de,ls,us)
    mult=sp.ilcm(*(sp.denom(x) for x in pn.coeffs()+pd.coeffs()))
    pn=sp.Poly(mult*ne,ls,us);de=sp.expand(mult*de)
    with (OUT/(name+'.pickle')).open('wb') as f:pickle.dump({'name':name,'num':pn.as_expr(),'den':de,'box':box,'second_variable':second},f)
    print(name,pn.degree_list(),'den',sp.factor(de),flush=True)

# The cap lemma uses the actual scalar u.
A=1+L*(1-u);B=1+L*(L+1)*(1-u)
P=L**2*(L+1)**2*(1-u**2)+2*L+1
RB=A*P-(L+1)**2*(1-u)*(1-L*u)**2
kn=(2*L**3+20*L**2+2*L)*u**2-(3*L**3+67*L**2+49*L+1)*u+L**3+71*L**2+143*L+25
FB=(144*L**2*(L+1)*RB-kn*(L*RB+u*B*P))/(L+1)
assert FB.denom==1
save('cap_lambda_derivative',FB.diff(L),['1','3/2','0','3/4'])
fs=FB.as_expr().subs(ls,2/sp.sqrt(3))
f3=sp.diff(fs,us,3);a3=sp.expand(fs).coeff(us,3);a6=sp.expand(fs).coeff(us,6)
J=sp.simplify((f3-6*a3)/us)
checks={
 'a3 negative':-a3,'a6 negative':-a6,
 'Jprime(3/4) positive':sp.diff(J,us).subs(us,sp.Rational(3,4)),
 'J(3/4) negative':-J.subs(us,sp.Rational(3,4)),
 'f(1/2)>2':fs.subs(us,sp.Rational(1,2))-2,
 'fprime(1/2)>-18':sp.diff(fs,us).subs(us,sp.Rational(1,2))+18,
 'fprime(1/2)<0':-sp.diff(fs,us).subs(us,sp.Rational(1,2)),
 'fsecond(3/5)>1000':sp.diff(fs,us,2).subs(us,sp.Rational(3,5))-1000,
 'fprime(3/5)>0':sp.diff(fs,us).subs(us,sp.Rational(3,5)),
 'fprime(3/4)>0':sp.diff(fs,us).subs(us,sp.Rational(3,4)),
}
endpoint_records=[]
for name,value in checks.items():
    value=sp.simplify(value)
    aa=sp.expand(value).coeff(sp.sqrt(3),0)
    bb=sp.expand(value).coeff(sp.sqrt(3),1)
    assert aa.is_Rational and bb.is_Rational,(name,aa,bb)
    if aa>=0 and bb>=0: guard=aa+bb
    elif aa<0 and bb>0: guard=3*bb*bb-aa*aa
    elif aa>0 and bb<0: guard=aa*aa-3*bb*bb
    else: raise AssertionError((name,'nonpositive algebraic number',value))
    assert guard>0,(name,value,guard)
    endpoint_records.append({'name':name,'value':str(value),'rational_part':str(aa),'sqrt3_part':str(bb),'positive_rational_guard':str(guard)})
    print('cap exact endpoint PASS',name,str(value),flush=True)
(OUT/'cap_endpoints.json').write_text(json.dumps(endpoint_records,indent=2))

# In the remaining objects the second coordinate is k=1-lambda*u_actual.
k=u;c=L-1
ua=(1-k)/L;t=(c+k)/L;A=L+k;B=L**2+(L+1)*k
P=L+2*k**2/B**2+4*L**2*t*k/(A*B)
C2=L+2*k**2/B**2+4*k*(L+1-L*A/B)/(A*c)
W=L-2*k/B+2*k**2/B**2
S0=(2-(L+1)*ua)*P+c*ua*C2
def Y(E):
    return (4*ua-2-2/L)+2*(-2*A*E/L+4*ua/(L*t)-4*ua*B/A**2)+3*(2*E+S0/A**2-2*ua*(2*L+1)/(L*A*t))+(8*ua/A**3)*(L*P+E*A*(A-2*k))+(10*ua/A**2)*(P/(A*t)-E*W)
dm=L*A**4*(c+k)*B**2
Fm=-Y(ua/t)*dm/2
Fp=-Y((2/(2-k)-t)/t)*(2-k)*dm/2
assert Fm.denom==1 and Fp.denom==1
save('high_right_minus',Fm,['23/20','11/8','0','1/2'],'k')
save('high_right_plus',Fp,['23/20','11/8','0','1/2'],'k')
Kb=(L+1)/(2*L)+t/2+(L+1)*(2*L*t-L+1)*t/(24*L)
S=k*(1-ua*Kb)*(1+2*L/B**2)-A*t*((L+1)*Kb-2*L)+2*L**2*t*(2*L-(L+1)*ua*Kb*A)/(A*B)
Pu=24*L**2*A*B**2*S
assert Pu.denom==1
save('high_upper',Pu,['23/20','11/8','0','1/2'],'k')

# The lower endpoint's displayed quartic, including its strict remainder.
Q=rat(2518569,32000000)-rat(29541,200000)*k-rat(7316903,3200000)*k**2+rat(1790369,80000)*k**3-rat(57507,8000)*k**4
simple=rat(3,40)-rat(3,20)*k-rat(5,2)*k**2+18*k**3
assert simple==18*(k+rat(1,9))*(k-rat(1,8))**2+rat(11,160)*k+rat(7,160)
save('high_lower_quartic',Q-simple,['23/20','11/8','0','1/2'],'k')
