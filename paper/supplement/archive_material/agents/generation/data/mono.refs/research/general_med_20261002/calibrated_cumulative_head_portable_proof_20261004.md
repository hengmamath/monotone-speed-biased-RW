# Portable audit214--224: calibrated cumulative head
NEW214--224 self-checkPASS/auditPENDING. Prior121--123,11,166--213 PASS
same sole auxiliary. No agents created. General165 OPEN; additional domain only.

Canonical U=X/(c+X),c=λ-1,L=1/λ,
μ0=0,μ1>0,finite mean only,ordinaryroot;1<λ<min(m,2/sqrt3),0<α<1.
a_s=EU^s,u=a1,b=a2,A0=1-(λ+1)u+λ b,R=v/c,
h=cu/(1-u),d=1-h,β_s=h/(λ^s-d),β0=1,
ρ_s=a_s/β_s,ρ0=ρ1=1,Δ_i=ρ_i-ρ_next,Δ0=0,
r_i=β_next/β_i,L_i=L-rprev,w_i=λ^(i-1)β_i^2.
Tp=sum w,Qp=u/(1-u),Zp=2Qp-(λ+1)Tp,Rp=Tp/Zp>R,
k=c/(λ logλ),2/(λ+1)<k<1,k>1/λ.
Actual-marker:0<ρ_i<=1,Δ_i<=i e,e=1-ρ2>0.
E_i=r_i[i L_i+(i+1)λ Lnext],
W0_i=ci/λ-1+2iLi,Wp_i=cW0_i+4iLi-2E_i,Ws(q)=W0_s+q Wp_s.
V_i(q)=Σ_(s>i)w_s Ws(q)>0 forq>=0;206 upper
V_i/w_i<=(1+cq)[i+2z_i-z_i^2]/λ+
4q L_i[i/(λ^2-1)+λ^2/(λ^2-1)^2],z_i=d λ^-i.
Fpipe=-2Rp uL1+sum w Ws(Rp)>0. Define
C_i=α(1+Li)+q[c+λ Li+(i+1)λ Lnext/i],
τ_i=1-(α+λ q)n_i+(λ+1)q-q/nprev,n_i=a_next/a_i,
B_i=w_i ρ_i[2i r_i C_i+k(2i-1)τ_i].
Accepted207: Ffloor(q)=Fpipe+Bp(Rp-q)+sum Δ_i S_i(q),
S_i=B_i-(ρ_i+ρ_next)V_i(q); all components use SAME moments.

214--215. Hold actual moments FIXED,α(q)=(u-qA0)/b,R<=q<=Rp.
Rp<u/(1-u) implies0<α(Rp)<α(R)<1.
t_n=-q a_n+[1+(λ+1)q]a_next-(α(q)+λ q)a_(n+2).
t_n'=(A0/b)a_(n+2)-E U^n(1-U)(1-λ U)>0,n>=1,t0'=0.
Indeed pi2=U^2*pi/b,psi=(1-U)(1-λ U)/U^2 strictly decreasing,
t_n'=-b Cov_pi2(U^n,psi)>0; E_pi2 psi=A0/b finite.
Also t_n'<(A0/b)a_(n+2). No inverseU assumption.
Accepted121--123 gives -∂_v Fstar>Chead/c,
Chead=2A0u[-k log(b/u)-1+b/u]+(u-λ b)
[2-(3λ+1)u+λ(λ+1)b]/λ>0.
Fstar-Ffloor=2Σ_(s>=2)s λ^(s-1)
[Θ_s-λ k(1-1/(2s))(1+Ls)delta_s]t_(s-1).
Brackets>0 by11,so -∂_q Ffloor>Chead,
Ffloor(R)>Ffloor(Rp)+Chead(Rp-R). Fixed-law affine algebra;
series absolutely polynomial-geometric.

216--218. α_p=[u-Rp(1-(λ+1)u+λ β2)]/β2,
Cα=α_p+λ Rp,e=1-ρ2,da=α(Rp)-α_p=Cα e/ρ2.
0<α_p<α(Rp)<1,α_p>λ^2u. Let B_i^p useβ moments,
α_p,Rp andn_i=r_i,nprev=rprev; S_i^p=B_i^p-2V_i(Rp).
ForactualbarB_i atRp,barα=α_p+da, exact
barB_i-ρ_i B_i^p=w_i ρ_i da c_i+
k w_i(2i-1)[Cα r_i Δ_i-Rp Δ_prev/rprev],
c_i=2i/λ-k(2i-1)n_i>1/λ.
Use(1+Li)r_i=L,r_i-n_i=r_i Δ_i/ρ_i,
1/nprev-1/rprev=Δ_prev/(rprev ρ_i). Hence
Ffloor(Rp)=Fpipe+sum Δ_i ρ_i S_i^p+Corr,
Corr=sum Δ_i^2 V_i+da sum w_i ρ_i Δ_i c_i+
k sum w_i(2i-1)[Cα r_i Δ_i^2-Rp Δ_i Δ_prev/rprev].
V_i Δ_i^2 retained.

219--220. W_i=k w_i(2i-1)Rp/rprev,i>=2,W1=0,
J_i=V_i+k w_i(2i-1)Cα r_i-(W_i+Wnext)/2,i>=2.
The EXACTi1 correction is e^2[V1+2u^2 Cα/(λ ρ2)];
k cancels since da*n1=Cα*r1*e.
Young pays all cross products; otherda terms>0:
Corr>=e^2 G(e)+Σ_(i>=2)Δ_i^2 J_i,
G(e)=V1+2u^2 Cα/[λ(1-e)]-W2/2>0.
Root: Cα/(λ Rp)>1,k λ r1<1,so its calibration>2u^2Rp
andW2/2<3u^2Rp/2. Ω=Cα/(λ Rp)-(λ+1)/2>0 since
α_p>λ^2u,Rp<u/(1-u),u<1/λ.
1/(λ rprev r_i)=λ+(λ+1)Lprev gives
J_i/[k w_i(2i-1)λ Rp r_i]>
Ω-1/(2i-1)-(λ+1)Lprev/2.
Thus ALLi>=NQ haveJ_i>0, for
NQ=max(2,ceil(1/2+1/Ω),
1+max(0,ceil(log_λ(d[1+c(λ+1)/(λ Ω)])))).
Charges<=Ω/2;Δ_i<=i e gives
Corr>=e^2[G(e)-Jminus],Jminus=Σ_(i2)^(NQ-1)i^2[-J_i]_+.

221--222. Hpi=sum i[-S_i^p]_+ is FINITE. Scalarβ moments:U=λ^-A,P(A=n)=h d^(n-1);
never substituted for canonical escape. Its calibrated concave quadratic hasQ0<0,
Q(L)>0,EQ=0; a single sign crossing gives τ_i^p>0 fori>=2,τ1=0.
τinf=1-α_p/λ, τ_i^p=τinf+Cα Lnext-λ Rp Lprev.
Lprev<=(λ+1)Li,Lnext<=Li and complete206 upper give
S_i^p/w_i>=gp*i-k-L_i(A*i+B),
gp=2(k-1/λ)+2α_p(1-k)/λ>0,
A=2cRp+2k λ Rp(λ+1)+8Rp/(λ^2-1),
B=4(1+cRp)/c+8Rp λ^2/(λ^2-1)^2.
Li<=L1 λ^(-i+1); ALLi>=
Npi=max(2,ceil(4k/gp),1+max(0,ceil(log_λ(4L1(A+B)/gp))))
have S_i^p>0. HenceHpi=Σi<Npi i[-S_i^p]_+.
sum Δ_i ρ_i S_i^p>=-eHpi. Accepted185/200 gives
Rp-R>u^2(κ-1)e(2-e)/Zp,κ=(1-u)Tp/u^2>1.
Consequently COMPLETE222:
Ffloor>Fp-eHpi+e^2[G(e)-Jminus]+Chead u^2(κ-1)e(2-e)/Zp.
UniversalRHS>=0 OPEN.

223. E=min((1-u)(1-λ u),(1-α_p)/(1+λ Rp)),actual0<e<E.
Atb_E=β2(1-E),setA_E=1-(λ+1)u+λ b_E,
D_E=2-(3λ+1)u+λ(λ+1)b_E,zp=β2/u,epsp=u-λ β2,
C_E=2A_E u[-k logzp-1+zp]+epsp D_E/λ>0.
b_E>=u^2 makesA_E,D_E positive; -klogz-1+z decreases forz<L<k.
HenceChead>=C_E,G(e)>=G(0). ALL-e sufficient quadratic:
P(e)=Fp+[C_E u^2(κ-1)(2-E)/Zp-Hpi]e+[G(0)-Jminus]e^2.
Endpoints/vertex check minimum; universal minP>=0 NEXT/OPEN.

224. Whole rectangle λ in[104999/100000,105001/100000],
u in[84999/100000,85001/100000]: full rational certificate below proves
Fp-E Hpi-E^2Jminus>1/20, hence Ffloor>1/20 for all originalhardlaws/legal e, by222.
Nonempty by PASSEDfiniteK transfer μ_K=(43/60)δ1+(17/60)δK:
atλ21/20,u->17/20,α->α_p in(0,1).
Outward rational10^15 rounding throughout.
P512: gp atkl=2/(λ+1) is a LOWER becausegp increases ink;
A usesk<=1. AssertionsP*gp_lo>=4,L1 λ^(-P+1)(A+B)_hi<=gp_lo/4
pay EVERY omittedS_i^p. NQ20 assertions pay EVERY omittedJ_i.
Tp full omitted tail<=h^2/c λ^(-P-1)/(1-d λ^(-P-1))^2.
V_P full upper206 enters reverse sums. Fp omits only POSITIVEfulltail206.
Bcap useskl since true τ>=0;J keeps signed k dependence.
E uses hard-bound UPPER endpoints. Exact assertion givesmargin>1/20.
20 IDs and certificate nativePASS; auditPENDING. General165/223 OPEN.
