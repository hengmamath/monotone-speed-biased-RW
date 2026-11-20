"""New author finite boundary identities from complete original root/ages.
No old numerator table or certificate is loaded. Exact outputs supplement paper.
"""
from pathlib import Path
import sympy as s,json
P=Path(__file__).resolve().parent
l=s.symbols('l');a=s.Rational(23,20);B=l+1
S={j:sum(l**i for i in range(j)) for j in range(1,6)}
Q={j:S[j]+1 for j in S}
K=(37*l+25)/(48*l);h=(13*l+25)/(48*l);A=Q[2]/2
price=25+2*l/(2-l)
U1=2/l*(s.Rational(1,2)-price)
U2=2/l*(price*l*(K/2-1)+s.Rational(1,2)+2*l+l/2-(h+K)*l)
R=s.cancel(2/l*(price*(2-K)+2*h-1)+U1/A+U2/A**2+1/A**3)
D=96*l**2*Q[2]**3*(2-l)
rootnum=s.cancel(D*R);assert s.fraction(rootnum)[1]==1
assert s.Poly(rootnum,l).degree()<=5
def cof(poly,var=l):
    pp=s.Poly(poly,var);return [str(pp.nth(i)) for i in range(pp.degree()+1)]
def local_pair(num,den,point,order):
    z=s.symbols('z');pn=s.Poly(s.expand(num.subs(l,point+z)),z)
    pd=s.Poly(s.expand(den.subs(l,point+z)),z)
    aa=[pn.nth(i) for i in range(order)]
    dd=[pd.nth(i) for i in range(order)]
    qq=[]
    for i in range(order):qq.append(s.cancel((aa[i]-sum(dd[j]*qq[i-j] for j in range(1,i+1)))/dd[0]))
    return dict(point=str(point),numerator=[str(x) for x in aa],denominator=[str(x) for x in dd],quotient=[str(x) for x in qq])
poledata={
 'lambda0':local_pair(rootnum,96*Q[2]**3*(2-l),0,2),
 'lambda_minus2':local_pair(rootnum,96*l**2*(2-l),-2,3),
 'lambda2':local_pair(rootnum,96*l**2*Q[2]**3,2,1)}
assert poledata['lambda0']['quotient']==['-575/24','359/16']
assert poledata['lambda_minus2']['quotient']==['8','-775/6','1091/32']
assert poledata['lambda2']['quotient']==['29/32']
rootpf=1091/(32*Q[2])-775/(6*Q[2]**2)+8/Q[2]**3+29/(32*(2-l))+359/(16*l)-575/(24*l**2)
assert s.cancel(R-rootpf)==0
data={'root_numerator':cof(rootnum),'root_poles':poledata,'age_terms':{},'age_numerators':{},'payments':{},'endpoints':{}}
half={};zero={}
for j,n in [(2,1),(3,3),(4,6)]:
    m=24-2*n
    C=2*Q[j+1]**2-Q[j]*Q[j+1]-l*Q[j]**2
    J=2*m*Q[2]-l-4
    aj=-(24-n)*(37*l+25)+26*l+50
    bj=m*(37*l+25)-26*l-50
    terms=[(8*j*l**(j-2)*C*J,Q[j]**3*Q[j+1]**2*Q[2]),
           (j*l**max(j-3,0)*aj,6*Q[j]**2*Q[j-1]*(l if j==2 else 1)),
           (j*l**(j-2)*bj,6*Q[j]*Q[j+1]**2)]
    deriv=sum((s.diff(p,l)*d-p*s.diff(d,l))/d**2 for p,d in terms)
    norm={2:6*l**2*Q[2]**5*Q[3]**3,3:2*Q[2]**2*Q[3]**4*Q[4]**3,4:s.Rational(3,4)*Q[2]**2*Q[3]**2*Q[4]**4*Q[5]**3}[j]
    num=s.cancel(norm*deriv);assert s.fraction(num)[1]==1
    assert s.Poly(num,l).degree()=={2:10,3:14,4:23}[j]
    data['age_numerators'][str(j)]=cof(num)
    data['age_terms'][str(j)]={'C':cof(C),'J':cof(J),'aj':cof(aj),'bj':cof(bj)}
    half[j]=s.cancel(sum(p/d for p,d in terms))
    zero[j]=4*j*m*l**(2*j-2)/(S[j]**3*S[j+1])+2*j*m*l**(j-2)/(S[j]**2*S[j+1]**2)
    print('COMPLETE derivative numerator',j,data['age_numerators'][str(j)],flush=True)
b=s.Rational(10,7)
payments={'N2_high':190088+76721-33337*b**2-42259*b**3-11643*b**4,
 'N3_high':490063+499251+188138-2110*b**3-78768*b**4-91645*b**5-33545*b**6}
R0=-l/12-s.Rational(1,12)+44/B-44/B**2-35/(12*l)-299/(12*l**2)
for name,root,ages,floor in [('zero',R0,zero,s.Rational(57,100)),('half',R,half,s.Rational(21,25))]:
    vals=[s.cancel(root.subs(l,a))]+[s.cancel(ages[j].subs(l,a)) for j in [2,3,4]]
    partial=[];v=0
    for value in vals:
        leftnum,leftden=s.fraction(v);rightnum,rightden=s.fraction(value)
        crossnum=leftnum*rightden+rightnum*leftden;crossden=leftden*rightden
        v=s.cancel(v+value)
        partial.append({'cross_numerator':str(crossnum),'cross_denominator':str(crossden),'gcd':str(s.igcd(crossnum,crossden)),'reduced_sum':str(v)})
    gap=s.cancel(v-floor);assert gap>0
    data['endpoints'][name]={'R_T2_T3_T4':[str(x) for x in vals],'partial_additions':partial,'sum':str(v),'floor':str(floor),'gap':str(gap)}
    print('EXACT complete endpoint',name,str(v),'gap',str(gap),flush=True)
for k,v in payments.items():assert v>0;data['payments'][k]=str(v)
data['state']='LOCAL original finite boundary identities; paper and independent audit separate'
out=P/'J1HAND_CONTINUATION_HALF_BOUNDARY_DERIVED_DATA_LOCAL_20261007.json';assert not out.exists()
out.write_text(json.dumps(data,indent=2)+'\n')
print('ROOT finite numerator',data['root_numerator'],'POLE DATA',poledata,flush=True)
print('LOCAL exact finite boundary generation PASS; not full J1 audit',flush=True)
