# Unified Lambert head scales225--231

2026-10-04. Sole main task; NO agents/tasks. COMPLETE225--231 andALL42
independentlyPASS SAME sole auxiliary; receipt saved. Previous214--224/20/continuous rectangle PASS same
sole auxiliary; receipt saved and tau_i^p<1 clarified. Its small coverage
has limited value. This is a UNIFIED all-parameter mechanism, not a
microrectangle cover. General165/223 and crossing1 remain OPEN.

Original fixedmu0=0,mu1>0,finite mean only,ordinaryroot,canonical terminal-one
escape. Remaininghard1<lambda<min(m,2/sqrt3),0<alpha_actual<1.
NEW notationq=u/(1-u)=h/c, c=lambda-1,h=cu/(1-u),d=1-h.
Here R=Rp=Tp/Zp is ALWAYS the scalar reference speed quotient; ownv/c<R.
beta_i=h/(lambda^i-d),r_i=beta_next/beta_i,L_i=c d/[lambda(lambda^i-d)],
w_i=lambda^(i-1)beta_i^2,Tp=sumw,Zp=2q-(lambda+1)Tp,
k=c/(lambda loglambda),alpha_p=[u-R(1-(lambda+1)u+lambda beta2)]/beta2,
C_alpha=alpha_p+lambda R. Acceptedhard giveslambda^2u<alpha_p<1,R<q.
Same complete capV_i=sum_(s>i)w_s Ws(R),Hpi=sum i[-S_i^p]_+,
S_i^p=B_i^p-2V_i. Complete quadratic charge
J_i=V_i+k w_i(2i-1)C_alpha r_i-
 k R w_i[(2i-1)/rprev+lambda r_i(2i+1)]/2, i>=2;
Jminus=sum_(i>=2)i^2[-J_i]_+ equals accepted finite220.
No beta law is substituted for actual canonical escape.

## 225. Complete positive Lambert coefficients, with quantitative bounds

LetN>=1,x=lambda^N,Q_N=sum_(j0)^(N-1)lambda^j,z=d lambda^-i.
A_N=cN/(x-1),B_N=cN*x/(x-1)^2-lambda/(x-1),
P_N=(lambda+1)A_N-2lambda/x,
C_N=(lambda+1)B_N-2lambda(1-A_N)/(cN*x).
Accepted206/189 full tail expansions give EXACTLY
 V_i/w_i=(1/lambda) E_Pi[(A_N+R P_N)i+B_N+R C_N],
 Pi(N)=N(1-z)^2 z^(N-1),N>=1, an explicitly normalized scalar probability.
All signed regroupings were already absolutely convergent. NEW:
 lambda^(1-N)<=A_N<=1;
 0<=B_N<=(N-1)/(2N);
 cN/x<=P_N<=cN;
 0<=C_N<=c(N-1)(5N+2)/(6N)<=c(N-1).             (225)
These are ALL-N proofs, not finite-N observations.

A follows from the finite geometric average. B_N=(sum_(j1)^(N-1)j lambda^j)/Q_N^2.
For B upper letD_N=(N-1)Q_N^2-2N sum j lambda^j. D_N(1)=0.
D_N' has negative coefficients only through degreeN-2, and positive
coefficients at degrees>=N-1; D_N'(1)=N^2(N-1)(N-2)/3>=0.
Forlambda>=1 this coefficient ordering impliesD_N'>=0. N1 direct.

P lower is equivalent toN(lambda^(N+1)+1)>=2sum_(j1)^N lambda^j.
It is the convex-chord inequality for powers at indices1,...,N.
For upper define
K_N=Nlambda^(2N)-Nlambda^(N+1)-2Nlambda^N+2lambda Q_N.
K_N=c^2 sum_(j0)^(2N-2)b_j lambda^j, ALLb>=0:
b_j=j(j+1),0<=j<=N-1; b_j=N(2N-1-j),N<=j<=2N-2.
Finite second differences and endpoints prove the polynomial identity;
N1/2 handled directly. AlsocN-P_N=c K_N/[x(x-1)].

C positivity has the ENTIRE polynomial certificate
(lambda+1)N^2lambda^(2N-1)-cNlambda^N Q_N-(2+2Nc)Q_N^2
=c^2sum_(j0)^(2N-2)a_jlambda^j.
For0<=j<=N-2,a_j=(j+1)(j+2)(N-1-j/3)>0.
ForN-1<=j<=2N-2 putr=2N-2-j:
a_j=(N-r-1)[(2r+1)N+r(r+1)]+2r(r+1)(r+2)/3>0,N>=2.
The lower/upper second differences are2(N-1-j),2(j-3N+1).
Boundary values atN-1,N,2N-1,2N are0,2-3N,N(N-2),N(N-1);
N1/2 direct. These exhaust the coefficients of the displayed polynomial.
C_N=c lambda^(1-N)sum a_jlambda^j/(N Q_N^2).
sum a_j=N^2(N-1)(5N+2)/6.
AMGM Q_N>=Nlambda^((N-1)/2), andlambda^j<=lambda^(2N-2), prove the C upper.
AllN1 constantsB1=C1=0. The standalone script checks generic identities,
boundaries, small exceptions and the full coefficient sum.

## 226. ALL-mixture two-sided tails retain the high-N credit

Positive mixture summation225 gives, for EVERYi>=1,
 i lambda r_i^2[1+R(c/lambda+2Lnext)] < V_i/w_i
 <=i(1+cR)/lambda+2R(i+1)L_i+z/(2lambda).         (226)
IndeedE lambda^(1-N)=((1-z)/(1-z/lambda))^2,
E Nlambda^-N=(1-z)^2(1+z/lambda)/[lambda(1-z/lambda)^3],
E(N-1)=2z/(1-z),E(1/N)=1-z.
Lower constant terms are nonnegative. UpperEB<=z/2 andEC<=cE(N-1).
Strictness follows from the positive higherN contributions.
The old206 upper discarded this slope cancellation and had errors
proportional toR L_i/(lambda^2-1). New226 has2R(i+1)L_i instead.
This is substantive control of the FULL Hpi/Jminus charges.

## 227. Complete pipe source and exact whole-cap cancellation

WriteF0=sum wW0,T=Tp. HoldingONLY scalarh,d fixed,
F0=-c T'-(1+c/lambda)T. Polynomial-geometric domination justifiesT'.
ForALLtails, shifting w_sE_s, INCLUDING boundaries, gives
 TailWp_i=(lambda+1)V0_i+2TailT_i-2(i+1)w_next-2q beta_next/lambda.
In particularsumwWp=(lambda+1)F0+2T-2u^2-2(q-u)/lambda.
Consequently
 Fpipe=(2q/Zp)[-c T'-2T+T^2/q]
      =-Zp*[cT/Zp]'.                                  (227)
This differentiates only the scalar reference series, NEVER the actual
random-tree law. It connects the entire source credit with the head
coefficients; root/endpoints have not been deleted.

## 228. Hard calibration normalizes the e-charge by EXACT gap

Lettheta=R/q in(0,1),A=theta*d*(lambda+1)-lambda. ThenEXACTLY
 alpha_p=1-A/(1+q),
 Ehard=(1-alpha_p)/(1+lambda R)
      =A/[(1+q)(1+lambda theta q)].
Hardalpha_p<1 impliesA>0,theta>lambda/[d(lambda+1)],
h<1/(lambda+1). SetD=1-(lambda+1)h>0.
Ehard increases intheta: derivative
[d(lambda+1)+lambda^2q]/[(1+q)(1+lambda theta q)^2]>0.
Hence the ENTIRE admissibleE=min(Evar,Ehard) satisfies
 E q^2<=D u^2/[1+c u]<1.                              (228)
This is the direct hard-gap cancellation of the q^2/q^4 scales,
not a guessed moment relation or an inverse escape assumption.

## 229. A complete Jminus budget, uniform over EVERYhard law withq>=50

Use226 lower. Witha=L_i,r=1/[lambda(1+a)],rprev=(1-lambda a)/lambda,
 J_i/w_i > i A_J-B_J,
 A_J=lambda r^2+2k alpha_p r+
 R[c r^2+2lambda r^3 a+k(lambda r-1/rprev)],
 B_J=k[C_alpha r-R(1/rprev-lambda r)/2]<=q+1.
The last bracket'sk=1 value factorsEXACTLY as
 -[(lambda a+c)(2a^2lambda^2+3a lambda^2+2a lambda+a+lambda^2-1)]
 /[lambda^2(1+a)^3(1-lambda a)].
Sincek<=1, this is a lower bound. Bernoulli lambda^i>=1+ic gives
a<=a_m=d/[lambda(q+2)],r>=r_m=1/[lambda+d/(q+2)] fori>=2.
Drop only the positivefactor(1+a)^3 in the negative denominator and
increase each numerator factor toa_m. Let
N_m=(lambda a_m+c)[2lambda^2 a_m^2+(3lambda^2+2lambda+1)a_m+lambda^2-1]
    /[lambda^2(1-lambda a_m)].
Usingk>=2/(lambda+1),alpha_p>lambda^2u,R<q proves
 A_J>=lambda r_m^2+4lambda^2u r_m/(lambda+1)-q N_m >3-12/q. (229a)

The last inequality is a finite EXACT positive-coefficient certificate,
not an evaluation at points. Substitutelambda=1+h/q,u=q/(1+q),d=1-h.
The rational difference has positive denominator
q(h+q)^3(h+2q)(q+1)(q+2)^2(h+q+1)(2h+q^2+3q)^2.
Its numerator has60 nonnegative coefficients in(h,q), including66q^11.
The standalone symbolic script computes the exact numerator, checks ALL
coefficients and the displayed denominator. Thus it is strictly positive
for EVERYq,h>0 in the admissiblehardbox; no parameter mesh.

Forq>=50,3-12/q>=11/4. Also0<w_i<=w1=u^2<1, because
h^2 y/[lambda(1-dy)^2] increases iny=lambda^-i. Therefore
 Jminus<sum_(i>=1)i^2[q+1-(11/4)i]_+.
ForT>=2,n=floorT,f=T-n in[0,1), exactFaulhaber gives
sum_(i1)^n i^2(T-i)=T^4/12+T^2[-f^2/2+f/2-1/12]
+T[2f^3/3-f^2+f/3]-f^2(1-f)^2/4 <=(T^4+T^2)/12.
TheT^2 coefficient<=1/24,absoluteT coefficient<=1/12;T>=2 pays the latter.
TakeT=(q+1)/(11/4). The ENTIRE charge, including every omittedage, obeys
 Jminus/q^4< (51/50)^4/[12(11/4)^3]
 +(51/50)^2/[12(11/4)50^2]
 =36185979/8318750000<1/200.                         (229b)
Combining228 pays its actual price:
 E^2 Jminus< D^2u^4/[200(1+c u)^2]<1/200.
This is a COMPLETE cumulative quadratic-price theorem underq>=50,
not a speed theorem; the linear Hpi/source budget still needs payment.

## 230. Precise next coupled SIZE, OPEN

Forq>=50 it suffices to prove, uniformly in actualhard parameters,
 Fpipe-Ehard Hpi>=1/100.                             (230 OPEN)
Then222 and229 giveFfloor>1/200 without using the retained positive
root and calibratedspeed credits. A simpler sufficient pair is
Hpi<=q^2/8 andFpipe>=2/15;228/229 would giveFfloor>1/300.
NONE of these linear/source inequalities is presently proved.
The full223 remains the objective for every remainingq, includingq<50.
No unconditionalbiasrange or new rectangle follows from229 alone.

## 231. Global Bernoulli upper for the ENTIRE Hpi, available for230

delta=loglambda. ForALLt>0,
t/(e^t-1)<=1-t/2+t^2/12, e^-t>=1-t+t^2/2-t^3/6.
The first follows by multiplying: its entire exponential remainder has
coefficients(n-3)(n-4)/(12n!)>=0 forn>=5, lower powers vanish.
The second is Taylor's integral remainder with positive fourth derivative.
Letm1=(1+z)/(1-z),m2=(1+4z+z^2)/(1-z)^2,
m3=(1+11z+11z^2+z^3)/(1-z)^3. Positive mixture summation yields
MA=min(1,c/delta-c*m1/2+c*delta*m2/12),
MP=min(c*m1,(lambda+1)c/delta-2lambda+
 [2lambda*delta-(lambda+1)c/2]m1+
 [(lambda+1)c*delta/12-lambda*delta^2]m2+lambda*delta^3*m3/3),
MC=c[5m1/6-1/2-(1-z)/3].
By225's sharperC bound,EC<=MC; EB<=z/2. Hence
 V_i/w_i<=U2_i=[i(MA+R MP)+z/2+R MC]/lambda,
 Hpi<=sum_i i w_i[2U2_i-B_i^p/w_i]_+.               (231)
This is a rigorous ALL-age upper, not a formal asymptotic or numeric
supremum. U2_i<=226 upper<=206 upper in the active lambda<sqrt2 range:
z/2<=2z-z^2 and4i/(lambda^2-1)>=2(i+1). Hence221's explicit bound pays
EVERY omitted negativepart age. The sign of the total230 is stillOPEN.

42 exact checks and complete proofs above independentlyPASS SAME auxiliary.
Diagnostics onq20/50/h(.005,.05,.2,.45) support scale choices only; NO proof
dependency, canonical law is not numerically enclosed. No agents created.
Next: use231 and227 to pay the COUPLED230 rather than isolated cap signs.

Continuation232--237: coupled230 now has complete localproof/exactchecks
onENTIREhardq>=50, independentauditPENDING. See
uniform_high_q_coupled_comparison.md and full portable10535char packet.
This supersedes the historicalOPEN230 label ONLY at the locally proved,
auditpending level. q<50/general223/cross1 remainOPEN.
