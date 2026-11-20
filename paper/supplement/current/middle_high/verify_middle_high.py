"""Rebuild the regional rational functions without importing historical writers."""
import json
from pathlib import Path
import sympy as S

l,u,t,a,s,r,e,x,y,v=S.symbols('lambda u t a s r e x y v')
c=l-1
RAT=S.Rational
out={}
data={'shifted_sign_checks':[],'bernstein_checks':[],'normalization_identities':[],'coarse_payments':[]}

def positive_shifted(expr,base=RAT(7,5)):
    num,den=S.fraction(S.cancel(expr))
    pn=S.Poly(S.expand(num.subs(l,l+base)),l)
    pd=S.Poly(S.expand(den.subs(l,l+base)),l)
    assert all(z>=0 for z in pn.all_coeffs()) and pn.eval(0)>0
    assert all(z>=0 for z in pd.all_coeffs()) and pd.eval(0)>0
    data['shifted_sign_checks'].append({'expression':str(expr),'base':str(base),
      'numerator_ascending':[str(z) for z in reversed(pn.all_coeffs())],
      'denominator_ascending':[str(z) for z in reversed(pd.all_coeffs())]})
    return [pn.degree(),pd.degree()]

def bernstein_controls(expr,coords,degrees):
    poly=S.Poly(S.expand(expr),*coords)
    for d,coord in zip(degrees,coords):
        assert poly.degree(coord)<=d
    if len(coords)==1:
        result=[S.expand(sum(coef*S.binomial(j,b[0])/S.binomial(degrees[0],b[0])
                     for b,coef in poly.terms() if b[0]<=j)) for j in range(degrees[0]+1)]
        data['bernstein_checks'].append({'coordinates':[str(z) for z in coords], 'degrees':degrees,'polynomial':str(poly.as_expr()),'controls':[str(z) for z in result]})
        return result
    controls=[]
    for j in range(degrees[0]+1):
        for k in range(degrees[1]+1):
            controls.append((j,k,S.expand(sum(coef*S.binomial(j,b[0])/S.binomial(degrees[0],b[0])
                *S.binomial(k,b[1])/S.binomial(degrees[1],b[1])
                for b,coef in poly.terms() if b[0]<=j and b[1]<=k))))
    data['bernstein_checks'].append({'coordinates':[str(z) for z in coords], 'degrees':degrees,'polynomial':str(poly.as_expr()),'controls':[[j,k,str(z)] for j,k,z in controls]})
    return controls

D2=l+1-l*a
D3=l*l+l+1-l*(l+1)*a
D4=l**3+l*l+l+1-l*(l*l+l+1)*a
Ac=c*l+c*l*l*(D2/D3)**2+l**4*(D2/D4)**2
Amax=S.cancel(Ac.subs(a,l**-2)); A0=S.cancel(Ac.subs(a,0))
f1=c*(2*c+1)/l**2
f2=c*((4-l)*c+(2-l))/l**3
gammas=[3*c/l**2,(2*l+1)/(l+1)**2]
out['high_scalar']=[positive_shifted(z) for z in [l*l-Amax,l-f1-gammas[0],l-f1-gammas[1],l**3-l*l+l-2,l**5+l**4-l**3-3*l*l+1]]

H2=l*l+l-u; H3=l**3+l*l+l-(l+1)*u
H4=l**4+l**3+l*l+l-(l*l+l+1)*u
Den=H2**2*H3**2*H4**2
En=c*Den+c*l**3*H3**2*H4**2+c*l**4*H2**2*H4**2+l**6*H2**2*H3**2
Vn=l*(l-u)*Den+l*l*u*H2*H3**2*H4**2-u*l**4*H3**2*H4**2+u*En
Ln=H2*l*(2*c+1)+((4-l)*c+(2-l))*l
Ns=[c*Ln*Vn-En*H2*(l**4-3*c*l*u), c*Ln*Vn*(l+1)**2-En*H2*(l**3*(l-u)*(l+1)**2+l**5*u)]
for i,N in enumerate(Ns):
    controls=bernstein_controls(N,[u],[8])
    for q in controls: positive_shifted(q)
    out['high_endpoint_'+str(i)]=len(controls)
    EE=S.cancel((c+Ac*s*s).subs({a:u/l**2,s:l/H2}))
    BB=(1-l*a+l*a*s*(1-l*s)).subs({a:u/l**2,s:l/H2})
    sig=(f1+f2*l/H2)*(BB+u*EE/l**2)-EE*(1/l-gammas[i]*u/l**2)
    normden=l**5*H2*Den*((l+1)**2 if i else 1)
    assert S.cancel(S.together(sig-N/normden))==0
    data['normalization_identities'].append({'name':'high_endpoint_'+str(i),'lhs':str(sig),'rhs':str(N/normden),'residual':'0'})

zeta=S.symbols('zeta')
p=12+6*zeta; q=2*(2-l+zeta)/l
curve=1-l**-2*(2-3*l*s+(p*s-q)**2/(36*s))
scalars=[]
for zz in [0,c/l]:
    for ss in [l**-2,1/(l+1-1/l)]:
        scalars.append(curve.subs({zeta:zz,s:ss}))
w=(1-l**-2)**2
h0=4-2*l-2/l+2*zeta+2*(c-zeta)/w
gg=2+l*(l-2-zeta)-l*(c-zeta)/w
Xmax=l*l/(l*l+l-1)
scalars += [6*Xmax-2-2*c/(l*(1-l**-2)**3)*(3*Xmax-2),-gg.subs(zeta,0),(-12*gg-h0*h0).subs(zeta,0),RAT(1,10)-gg.subs(zeta,c/l),l*l-RAT(1,5)-h0.subs(zeta,c/l)]
out['hybrid_curvature_scalar']=[positive_shifted(z) for z in scalars]
FF=l**4-(1+12*c-10*c*t)*(4*l*l*t-2*t*t-l**4)
for z in bernstein_controls(FF,[t],[5]):positive_shifted(z)
out['hybrid_curvature_polynomial']=6

theta=t/l
R=1+9*l*(1-l*theta)*(28*l+17+(17*l+19)*theta)/(c*(l+1)*(2*l+7)*(2*l+1)*(2+7*theta)*(2+theta))
price=(1/l-theta)*2*l/(c*(l+1))*l*(RAT(243,8)/((2+7*theta)*(2*l+7))+RAT(9,8)/((2+theta)*(2*l+1)))
assert S.cancel(price-(R-1))==0

def sigma(i,aa,ss,AA,RR):
    T=1+c*RR; mb=c*(1+2*c*RR)
    eb=-l*c+2*theta*mb
    ld=2*(l+1)+4*c*RR-4*theta*T
    er=-2*l*T+4*theta*(l+1)+8*theta*c*RR-6*theta**2*T
    ww=1 if i==0 else (1-theta/l)**2
    m0=mb*ww; l0=ld*ww
    m1=eb if i==0 else eb-theta**2*mb/l
    l1=er if i==0 else er-theta**2*ld/l
    E4=c+AA*ss**2; B=1-l*aa+l*aa*ss*(1-l*ss)
    return (B+aa*E4)*(m0+m1*ss)+aa*E4*(l0+l1*ss)/2-E4*T*ww

RR,AA=S.symbols('R A_scalar')
TT=1+c*RR; MM=1+2*c*RR; zz=c/TT
ww=(1-theta/l)**2
xx=1-3*l*s
curves=[a*c*l*(xx*(2*theta*MM-l)-l*MM),
 l*l*TT*(a*(2-2*theta/l*(2-l+zz)+3*s*(-l+4*theta+2*zz*theta-3*theta*theta))-1),
 a*c*l*(-l*xx+MM*((xx+1)*(2*theta-theta*theta/l)-l)),
 l*l*TT*ww*(a*(4-2*l-2*theta+2*zz+2*(c-zz)/ww+3*s*(2*l*theta+l*(l-2-zz)-l*(c-zz)/ww))-1)]
for i in range(2):
    for jj,AAvalue in enumerate([0,l*l]):
        assert S.cancel(S.diff(sigma(i,a,s,AAvalue,RR),s,2)/2-curves[2*i+jj])==0
EE=c+AA*s*s; BB=1-l*a+l*a*s*(1-l*s)
rr=a*EE/(2*(BB+a*EE))
CC=2*rr*(1+c*RR); LL=c+2*(l+1)*rr+2*RR*c*(c+2*rr); KK=l*(c+CC)
DD=LL-2*theta*CC; EC=-KK+2*theta*LL-3*theta*theta*CC
Bs=[-CC+DD*a+EC*a*s,(-CC+DD*a)*ww+(EC-theta*theta*DD/l)*a*s]
for i in range(2):assert S.cancel(Bs[i]-a*sigma(i,a,s,AA,RR)/(BB+a*EE))==0
out['hybrid_normalizations_and_curvature_identities']=7

for i in range(2):
    for b,AA in enumerate([0,l*l]):
        low=S.cancel(l**(8+2*i)*sigma(i,u/l**2,u/l**2,AA,1)/l)
        controls=bernstein_controls(low,[u,t],[4,2+i])
        for _,_,z in controls:positive_shifted(z)
        out['hybrid_lower_'+str(i)+'_'+str(b)]=len(controls)

out['A_chord']=positive_shifted(RAT(1,3)-Amax+A0)
Dr=(l+1)*(2*l+7)*(2*l+1)*(2*l+7*t)*(2*l+t)
Zr=c*Dr+9*l*l*(1-t)*(28*l*l+17*l+(17*l+19)*t)
Tn=Dr+Zr; M0=c*(Dr+2*Zr)
Nm=-l*l*c*Dr+2*t*M0
Nd=2*l*(l+1)*Dr+4*l*Zr-4*t*Tn
Ne=-2*l**3*Tn+4*t*l*(l+1)*Dr+8*t*l*Zr-6*t*t*Tn
delta0=(l*l+l+1)**2*(l*l+1)**2
alpha0=c*l*delta0+c*l*l*(l+1)**2*(l*l+1)**2+l**4*(l*l+l+1)**2
H=l*l+l-u
assert S.cancel(S.together(c*R-Zr/Dr))==0
hh,deltaA,alphaA,ee,vv,dr,mm,nm,nd,ne,tn=S.symbols('H delta alpha E_n V_n D_r M_0 N_m N_d N_e T_n')
e4=ee/(deltaA*hh**2); bplus=vv/(l**2*deltaA*hh**2)
normalized_coeff=[(mm/dr,nm/(l*dr),nd/(l*dr),ne/(l**2*dr),1),
 (mm/dr*ww,(l*l*nm-t*t*mm)/(l**3*dr),nd/(l*dr)*ww,(l*l*ne-t*t*nd)/(l**4*dr),ww)]
abstractN=[l*hh*vv*mm+l*vv*nm+u*ee*(hh*nd+ne)/2-l**3*hh*ee*tn,
 (l*hh*vv*mm+u*ee*hh*nd/2-l**3*hh*ee*tn)*(l*l-t)**2+l**3*vv*(l*l*nm-t*t*mm)+l*l*u*ee*(l*l*ne-t*t*nd)/2]
for i,(m0,m1,l0,l1,weight) in enumerate(normalized_coeff):
    sig=bplus*(m0+m1*l/hh)+u/l**2*e4*(l0+l1*l/hh)/2-e4*tn/dr*weight
    rhs=abstractN[i]/(l**(3+4*i)*deltaA*hh**3*dr)
    assert S.cancel(S.together(sig-rhs))==0
    data['normalization_identities'].append({'name':'hybrid_upper_'+str(i),'lhs':str(sig),'rhs':str(rhs),'residual':'0'})
assert S.expand((1-u/l+u/hh-l*l*u/hh**2+u*ee/(l*l*deltaA*hh**2))*(l*l*deltaA*hh**2)-(deltaA*(l*(l-u)*hh**2+l*l*u*hh-l**4*u)+u*ee))==0
for b,(alpha,delta) in enumerate([(alpha0,delta0),(3*alpha0+u*delta0,3*delta0)]):
    En=c*delta*H**2+alpha*l*l
    Vn=delta*(l*(l-u)*H**2+l*l*u*H-l**4*u)+u*En
    NN=[l*H*Vn*M0+l*Vn*Nm+u*En*(H*Nd+Ne)/2-l**3*H*En*Tn,
        (l*H*Vn*M0+u*En*H*Nd/2-l**3*H*En*Tn)*(l*l-t)**2+l**3*Vn*(l*l*Nm-t*t*M0)+l*l*u*En*(l*l*Ne-t*t*Nd)/2]
    for i,N in enumerate(NN):
        N=S.expand(N)
        K=S.expand(H*S.diff(N,u)+4*N)
        controls=bernstein_controls(K,[u,t],[3,4+i])
        for j,k,z in controls:
            base=RAT(707,500) if b==1 and i==0 and j==0 and k==4 else RAT(7,5)
            positive_shifted(z,base)
        out['hybrid_upper_u_derivative_'+str(i)+'_'+str(b)]=len(controls)
        if b==0:
            W=S.cancel(N.subs(u,0)/(l**(5+i)*(l+1)))
            for z in bernstein_controls(S.diff(W,l),[t],[3+i]):positive_shifted(z)
            if i==0:
                base_controls=bernstein_controls(W.subs(l,RAT(707,500)),[t],[3])
                assert all(z>0 for z in base_controls)
                out['boundary_W0_coefficients']=[str(z) for z in base_controls]
            else:
                bs=bernstein_controls(W.subs(l,RAT(707,500)),[t],[5])
                PP=sum(S.binomial(5,j)*bs[j]*t**j*(1-t)**(5-j) for j in range(6))
                assert S.expand(W.subs(l,RAT(707,500))-PP)==0
                assert 72*bs[0]+25*bs[1]>0 and 10*bs[2]-40*bs[0]>0 and 10*bs[3]-187*bs[0]>0
                assert all(bs[j]>0 for j in [0,4,5])
                out['boundary_W1_coefficients']=[str(z) for z in bs]
            out['hybrid_boundary_derivative_'+str(i)]=4+i

cc=e+RAT(19,20); ll=cc+1; L=cc+2+s; dd=1-cc*s
DN=s*dd*L**2+ll*r*s*s*(1+s)*L-ll**2*r*r*s*s*(1+s)**2
AN=(1-(2*cc+1)*s)*L+ll**2*r*s*(1+s)
BN=(1-s)*L+r*s*(1+s)
EN=cc*(2*cc+3)*s-(cc+2)
TN=s*s*L*L*(5+2*r*r*(1+s)**2)
polys=[S.cancel((TN*(AN+cc*L*EN)+10*ll*cc*s*L*DN)/s**2),S.cancel(((TN*EN+10*ll*s*DN)*L*BN+(1+s)*r*s*AN*(cc*TN+5*DN))/s**2)]
aone=s/(1+s); atwo=r*s/L
Dzero=aone*(1-ll*aone)+ll*atwo*(aone-ll*atwo)
Tbar=s*s*((1+s)**-2+RAT(2,5)*r*r)
z=(1-2*aone+atwo)/cc**2; wzero=(1-aone)/cc
zH=ll*ll*z-2*ll*wzero+1
VV=cc*Tbar/(cc*Tbar+2*Dzero)
Fzero=2-2*(cc+(ll+1)*VV)*dd*wzero+2*VV*zH
Fone=2-2*(cc+(ll+1)*VV)*dd*wzero+(1+VV)*atwo*zH/z
for name,lhs,rhs in [('D0',Dzero,DN/((1+s)**2*L**2)),('Tbar',Tbar,TN/(5*(1+s)**2*L**2)),('zH',zH,AN/(cc**2*(1+s)*L)),('z',z,BN/(cc**2*(1+s)*L)),('F0',Fzero,2*s*s*polys[0]/(cc*(1+s)*L*(cc*TN+10*DN))),('F1',Fone,2*s*s*polys[1]/((1+s)*L*BN*(cc*TN+10*DN)))]:
    assert S.cancel(S.together(lhs-rhs))==0
    data['normalization_identities'].append({'name':'coarse_'+name,'lhs':str(lhs),'rhs':str(rhs),'residual':'0'})
out['coarse_normalizations']=6
lower=[[151,197,173,99,28,3],[40,235,278,133,25,RAT(2,5)]]
for i,P in enumerate(polys):
    PE=S.Poly(S.expand(P),e)
    count=0
    for kk in range(7):
        for jj,z in enumerate(bernstein_controls(PE.nth(kk),[r],[3+i])):
            count+=1
            ps=S.Poly(z,s)
            if ps.is_zero:
                data['coarse_payments'].append({'polynomial':i,'e_power':kk,'bernstein_index':jj,'coefficients_ascending':[],'payment':'0'})
                continue
            first=min(k[0] for k,vv in ps.terms() if vv)
            pay=ps.nth(first)+sum(vv*RAT(9,25)**(k[0]-first) for k,vv in ps.terms() if k[0]>first and vv<0)
            assert pay>0
            if kk<6:assert first==0 and pay>=lower[i][kk]
            data['coarse_payments'].append({'polynomial':i,'e_power':kk,'bernstein_index':jj,'coefficients_ascending':[str(ps.nth(k)) for k in range(ps.degree()+1)],'first_power':first,'payment':str(pay)})
    out['coarse_'+str(i)]=count

tt=x+y-x*y; AA=l-1+tt
Pv=lambda yy:yy**2+(l-1)*((1+v)*yy-v)
Pc=lambda yy:(1-yy)*(2*v-(1+v)*yy)
assert S.expand(x*(1-x)*Pc(y)+y*(1-y)*Pc(x)-2*(l-AA)*(v*tt-x*y))==0
ss,nn,qq=S.symbols('S nu sum_squares')
FF=ss/(l+ss)
root=2*ss**2+2*(c-(l+1)*v)*ss+(1+v)*qq+2*v*(nn-l*l)
assert S.cancel((l+ss)**2*(2*Pv(FF)-Pc(FF))+l*((1+v)*qq-(1+3*v)*ss+2*v*nn)-l*root)==0
out['direct_signed_response_identities']=2
data['normalization_identities'].append({'name':'C_kernel','lhs':str(x*(1-x)*Pc(y)+y*(1-y)*Pc(x)),'rhs':str(2*(l-AA)*(v*tt-x*y)),'residual':'0'})
data['normalization_identities'].append({'name':'signed_root','lhs':str((l+ss)**2*(2*Pv(FF)-Pc(FF))+l*((1+v)*qq-(1+3*v)*ss+2*v*nn)),'rhs':str(l*root),'residual':'0'})
path=Path(__file__).with_name('exact_checks.json')
path.write_text(json.dumps(out,indent=2)+'\n')
data['boundary_W0_coefficients']=out['boundary_W0_coefficients']
data['boundary_W1_coefficients']=out['boundary_W1_coefficients']
Path(__file__).with_name('coefficient_data.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if not k.endswith('_coefficients')},indent=2))
