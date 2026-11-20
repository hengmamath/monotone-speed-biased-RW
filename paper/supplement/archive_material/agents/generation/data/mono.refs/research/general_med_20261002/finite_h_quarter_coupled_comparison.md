# 254--259: complete finite-h quarter budget

2026-10-04 LOCAL complete proof and exact certificates; independent audit
PENDING. No agents created. SAME sole auxiliary requested through parent.
Original fixed mu(0)=0,mu(1)>0,finite mean only,ordinary root/canonical
escape. Dependencies214--253 INDEPENDENT PASS. No new tree-law derivative,
inverse moment, offspring reduction or actual-law h=0 limit.

NEW: every actual hard point q in[10,21],0<h<=1/4 has FULL223>1/40.
Together with243(q>=21) and247(q>=10,h>=1/4), this pays ENTIRE actual
hard q>=10 (u>=10/11), pending independent audit. This is an escape-mean
domain, not a new unconditional lambda threshold. General med/q<10 and
crossing lambda=1 remain open.

Notation: c=lambda-1,x=1/q,h=cq,d=1-h,u=1/(1+x),lambda=1+hx;
beta_i=h/(lambda^i-d),wi=lambda^(i-1)beta_i^2,
T=sum wi,Z=2q-(lambda+1)T,R=T/Z,g=q-R,
alpha=[lambda^2+g(x-c)(lambda+1)x]/(1+x),k=a/lambda,
a=c/loglambda. The SAME calibrated R,alpha occur everywhere.
ri=beta_next/beta_i,rprev=beta_i/beta_prev,
Li=cd/[lambda(lambda^i-d)],tau_i=1-(alpha+lambda R)ri+(lambda+1)R-R/rprev.
Bi/wi=2i(alpha+cR)/lambda+2iRriLi+2(i+1)Rlambda ri^2Li+k(2i-1)tau_i;
Vi=sum_(s>i) ws Ws(R),Si=Bi-2Vi,H=sum i[-Si]_+.
Accepted223: for actual0<e<E=min(Evar,Ehard), Evar=d/(q+1)^2,
 P=Fpipe-eH-e^2 Jminus+G0 e^2+Ccal e,
 G0>0,Ccal>0, actualfloor>P. Their definitions/legality are unchanged.
Accepted239/240 give Si>=0 for i>=25 when q<=21,h<=1/4;
229 gives Jminus/q^4<=J(q)=(q+1)^4/[324q(q-4)^3]+(q+1)^2/[36q^3(q-4)].

254 ALL-age cancellation. Hyperbolic cap formula, cosh>=1 and sinh z>=z
give wi<=1/[lambda(1+rho t)^2],t=i/q,rho=(1-h/2)/a.
Accepted236 integral/Taylor remainder gives
 Alo=1+c/2-c^2/12<=a<=Aup=Alo+c^3/24<=1+c/2.
Exact identity lambda(1-h/2)^2-d(1+c/2)^2=h^2(lambda-dx^2)/4>0
implies lambda rho^2>d. Since0<rho<=1, EVERY quadratic coefficient in
lambda(1+rho t)^2-d(1+t)^2 is nonnegative. Thus
 d wi<=wi(q,0)=1/(1+t)^2 for EVERY age. No truncation or limiting law.

255 COMPLETE source and calibration gap, ALL q>=10,0<h<=1/4.
GLOBAL Lambert bounds238 and C_lower232 give
 s(a)=a-x/2+x^2(2-h)/(12a),J4=24-36h+14h^2-h^3,
 sl(a)=s(a)-x^4 J4/(720a^3),sl(a)/lambda<=T/q<=s(a)/lambda.
These include EVERY Lambert N. s,sl increase in a, s(Aup)<1; hence Z>0.
Define tg=2(1-gx)/[x+(lambda+1)(1-gx)]. Exact Bernstein certificates on
the ONE box x in[0,1/10],h in[0,1/4] prove
 sl(Alo)/lambda>t_(1/4), t_(1/8)>s(Aup)/lambda.
Since T/Z increases in T, 1/8<g<1/4.
Full227/238 source comparison gives Fpipe>69/500 if
 P_s(a)=2[s(a)^2-(lambda+1)s(a)+a^2-x^2(2-h)/12]
 -(69/500)x lambda[2lambda-(lambda+1)sl(a)]>0.
P_s increases: s'>0,s'<=1,sl'>0,s>=.95,lambda+1<=2.025,a>=1 give
P_s'>=2(2-.125)>0. Clearing P_s(Alo)'s signed denominator and positive
x power gives a polynomial with110 positive Bernstein coefficients,
degrees(9,10),minimum9325152/125. The gap matrices have90/56 positive
coefficients,degrees(8,9)/(6,7),minima25920/672/5.
Code checks EXACT denominators. Their signs follow
A=h^2x^2-6hx-12<0, both factors hx^2-4hx-2x-8 and hx^2-8hx-6x-16<0,
c^3-2c^2+12c+24>0. The source denominator bound remains positive before
division, as in238; this is the entire source, not a finite prefix.

256 COMPLETE tail derivative bundle. Let delta=loglambda,
M_r=sum_(N>=1)N^r d^(N-1)lambda^(-N(i+1)),F(t)=t/(1-e^-t),
C(t)=t^2 e^-t/(1-e^-t)^2. Exact complete Lambert and fixed-h derivative:
 TailT_i=h^2/(lambda delta) sum d^(N-1)lambda^(-N(i+1))F(Ndelta),
 Vi=-(1+cR)TailT_i+[1+(lambda+1)R](c h^2/lambda^2)
 [(i+1)/delta sum N d^(N-1)lambda^(-N(i+1))F(Ndelta)
 +delta^-2 sum d^(N-1)lambda^(-N(i+1))C(Ndelta)]
 -2R(i+1)w_next-2Rq beta_next/lambda.
The code verifies the derivative identity for a GENERIC N; convergence
and differentiation are the fixed-d scalar ones accepted227.
New GLOBAL C(t)<=1-t^2/12+t^4/240: multiply by2(cosh t-1); coefficients
through6 vanish; for even j>=8 they are
2(j-6)(j^3-9j-40)/(240j!)>0. Combine GLOBAL238
1+t/2+t^2/12-t^4/720<=F(t)<=1+t/2+t^2/12.
Negative TailT coefficient is combined BEFORE bounding.
Set p=lambda^(i+1),b=beta_next, m_r=h^(r+1)M_r:
m0=b,m1=pb^2,m2=p(p+d)b^3,m3=p(p^2+4dp+d^2)b^4,
m4=p(p^3+11dp^2+11d^2p+d^3)b^5. Thus the ENTIRE upper is
 TL=[a m0/x+m1/2+x m2/(12a)-x^3m4/(720a^3)]/lambda,
 PU=[(i+1)(a m1+x m2/2+x^2m3/(12a))+a^2m0/x-x m2/12
       +x^3m4/(240a^2)]/lambda^2,
 Vup=-(1+cR)TL+[1+(lambda+1)R]PU-boundaries >=Vi.
No differentiated inequality, partial N expansion or unestimated tail.

257 SAME-a comparison for EVERY finite head1<=i<=24.
Hold calibrated q,h,g,R,alpha fixed, define D_i(a)=Bi(a)/wi-2Vup(a)/wi.
p<= (41/40)^25<2,b<=1 give m3/m1<=13,m4/m0<=150. Direct derivatives yield
TL'<=(101/100)m0/(x lambda),PU'>=(19/10)m0/(x lambda^2).
UsingR>=q-1/4,cR<=1/4,lambda<=41/40 gives Vup'>=3q^2m0;
code checks the q=10 endpoint of this linear-q inequality.
b>=1/6 since lambda^(i+1)-1<=2(i+1)c, wi<=u^2<1.
tau_i<1: tau_i=1-alpha ri+R[(lambda+1)-lambda ri-1/rprev],
the bracket is negative by (1+Li)ri=1/lambda,rprev=(1-lambda Li)/lambda.
Hence D_i'<=(2i-1)/lambda-6q^2b/wi<=47-q^2<0.
Consequently D_i(a)>=D_i(Aup). SAME a in k and Vup; calibration unchanged.

258 ALL negative head ages certified. Define
 K(t,x)=[(3-9x)t-7/3+3x]/(1+t).
For each i1..24, code proves D_i(Aup)>=K(i x,x), EVERY q>=10,h<=1/4.
Use lambda=1+c,Aup=1+c/2-c^2/12+c^3/24,
 Dn=beta_n^-1=1+x sum_(k1)^n binom(n,k)c^(k-1).
Multiply D_i(Aup)-K by the POSITIVE common denominator
720 lambda^(i+1)x^2 Aup^3 Dnext^5(1+x)Dprev(1+ix).
Nine generic rational identities verify each scaled numerator group
against an independent reconstruction of Bi,TL,PU and both boundaries.
Only then substitute c=hx and remove positive x^2. For g endpoints1/8,1/4
(expression affine in g), all nonzero exact Bernstein coefficients are
positive on ONE x,h box. i1 degrees(27,20),587 coefficients; i24
degrees(188,180),34208 coefficients per endpoint. Omitted coefficients
are zeros, which suffice for the nonstrict comparison. The full48
polynomials were checked; no sampled parameters or microrectangle cover.

259 FULL223 payment, q in[10,21],0<h<=1/4.
Accepted239/240 make H's tail i>=25 zero, so258 controls WHOLE H.
With254 and e<=Evar,
 eH<=u^2(1/q)sum_(i>=1)G_x(i/q),
 G_x(t)=[t((7-9x)-(9-27x)t)/(3(1+t)^3)]_+.
Accepted250's WHOLE BV/non-grid endpoint bound gives sum/q<=
 CH=17160482889458863049/148731921929151943800.
Also e^2 Jminus<=d^2u^4J(q)<=u^4J(q). Therefore retain BOTH credits:
 P>69/500-u^2CH-u^4J(q)+G0 e^2+Ccal e=L(q)+G0 e^2+Ccal e>1/40.
The final inequality is accepted252's single degree5 Bernstein certificate
for ALL q[10,21]. No boundary compactness width is needed now.
Complete actualfloor223/222 transfers this to strict vprime at the actual
points. Joining243 and247 gives ENTIRE actualhard q>=10, auditpending.
Overall theorem still open; next remaining budget is q<10 after earlier
small-u/harmonic/e-paid domains, using the new full derivative bundle.
