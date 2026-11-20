# Calibrated actual response as a positive measure and whole-credit price

4 October 2026. NEW COMPLETE SELF-CHECKED, independent audit PENDING.
Continuing ONLY the actual (165) mainline; no agent/task. The preceding
large-u strip/actual-energy obstruction/165 interface independently
PASSED SAME sole reviewer; audit_receipt_large_u_overlap_20261004.md.
General unconditional interval[2/sqrt3,m) unchanged; (165) remains OPEN.

New mathematical input relative to the excluded coarse variance/slope
bounds: use EXACT hard calibration to factor the entire response
polynomial around its support endpoint. Its divided-difference moments
form an ACTUAL positive measure. This permits summing ALL response ages
before a legitimate two-measure Jensen/variance price. No original mu
is reduced, and no arbitrary fixed point or marker law is substituted.

## 1. Definitions and an exact calibrated endpoint factorization

Original fixed mu0=0,mu1>0,finite mean,ordinary root,canonical escape X.
Let U=X/(c+X),c=lambda-1,L=1/lambda,u=EU,b=EU^2,a_n=EU^n,
R=v/c>0,alpha in(0,1),C=alpha+lambda*R,

 Q(y)=-R+[1+(lambda+1)R]y-C*y^2,
 t_n=E[U^n Q(U)], t0=0,
 Q(L)=(lambda-alpha)/lambda^2>0,
 gamma=Q(L)/(L-u)=(lambda-alpha)/[lambda*(1-lambda*u)],
 theta=(L*u-b)/(L-u) in(0,u).

U in(0,L) a.s., nonconstant, and u<L, all independently PASSED in the
original actual class. Hard calibration t0=0 is indispensable here.
The elementary polynomial identity is EXACTLY

 Q(y)=gamma*(y-u)+C*(L-y)*(y-theta).                 (166)

Proof: both sides have the same quadratic coefficient, the same value
at L, and the same expectation under U; the last expectation vanishes
because theta=E[(L-U)U]/E(L-U). For a noncalibrated Q the additional
term is t0*(L-y)/(L-u); it is not silently omitted.

Define the ACTUAL endpoint-weighted probability
pi_L(dy)=(L-y)*pi_U(dy)/(L-u). All its weights are bounded; this is
neither an offspring replacement nor an escape distribution fixed point.
Its mean is theta. Equation(166) yields, for ALL n>=1,

 t_n=gamma*Cov_pi(U^n,U)+C*(L-u)*Cov_pi_L(U^n,U)
     >gamma*(a_(n+1)-u*a_n)>0.                    (167)

Both covariances are strictly positive because U is nonconstant and
the endpoint weight is positive a.s. Equivalently, for iid actual U,V,

 t_n=1/2 E[(U^n-V^n)(U-V)*
              {gamma+C*(L-U)*(L-V)/(L-u)}].         (168)

This is a quantitative ALL-order actual response bound, not just the
already known positivity of t_n. It uses no inverse escape moment,
offspring second moment, or derivative of a random tree law.

At n1, in particular,
t1>gamma*(b-u^2). For s>=2 and nprev=a_s/a_(s-1)>=z=b/u,

 tau_s=t_(s-1)/a_s
       >gamma*(1-u/nprev)>=gamma*(1-u/z)>0.         (169)

The bound is uniform over ALL ages at the given actual law. It does
not assume t_n/a_(n+2)>=lambda-alpha, the earlier unproved upgrade.

For completeness, an exact localizing-moment version of (167) is useful.
D_n=L*a_(n-1)-a_n>0, V_n=a_(n-1)*a_(n+1)-a_n^2>0. Then

 D_n*t_n-D_(n+1)*t_(n-1)-Q(L)*V_n
 =C*D_n*E[U^(n-1)(L-U)(U-D_(n+1)/D_n)^2]>0.       (170)

All quantities are bounded moments. Telescoping after division by
D_n*D_(n+1) recovers(167), since V_n/(D_n*D_(n+1))=
a_n/D_(n+1)-a_(n-1)/D_n. No infinite telescope is needed for a fixed n.

## 2. A positive actual divided-difference response measure

Use (168) and U^n-V^n=n int_V^U y^(n-1)dy. The finite positive measure

 omega(dy)=1/2 E[|U-V|*
  {gamma+C*(L-U)*(L-V)/(L-u)}*1_(min(U,V)<y<max(U,V))]dy

is ACTUALLY constructed from the SAME canonical pi_U. Exactly

                t_n/n=int_(0,L)y^(n-1)omega(dy), n>=1. (171)

Its total mass is t1>0. Its density is bounded at fixed lambda and it
has positive mass on an interval between two separated actual quantiles.
Consequently Omega=omega/t1 is a nondegenerate probability on(0,L).
Strict log-convexity and the support upper bound give the NEW constraints

 (t_n/n)^2<(t_(n-1)/(n-1))*(t_(n+1)/(n+1)), n>=2,
 t_(n+1)/t_n<(n+1)/(n*lambda), n>=1,
 t_n>=n*t1*(t2/(2*t1))^(n-1), n>=1.               (172)

The last inequality is Jensen under Omega; equality holds for n1,2
and is strict for n>=3. No assertion about t_(n+1)/t_n<=1/lambda is
made; that stronger bound does not follow for these signed moments.

## 3. Hard calibration forces a quantitative actual child variance

Let kappa=(1-u)sum f_s/R_s^2, V1/c=Rpi=u*kappa/[2-(lambda+1)u*kappa],
A1=lambda+1-lambda*u. The PASSED whole-speed comparison v<V1 gives
a(V1)<alpha<1. Hence the actual z=b/u satisfies

 z>zH=[1+Rpi*(lambda+1-1/u)]/(1+lambda*Rpi)
     =u+(1-u)*[2-(1+u)kappa]/[2-u*kappa]>u.        (173)

The positivity follows from the PASSED V1<h, equivalently
kappa<2/(1+lambda*u)<2/(1+u). Thus
b-u^2>u*(zH-u), t1>gamma*u*(zH-u), and
tau_s>gamma*(1-u/zH), ALL s>=2. This is a necessary hard-actual-law
size relation, not a new assumed variance condition.

Equivalently the ACTUAL marker first defect e=1-rho2 has the bound

 e<(1-a_pipe)/(1+lambda*Rpi),
 a_pipe=[(lambda+1)(2-kappa)-2lambda*u]/
                         [2-(lambda+1)u*kappa].   (174)

All denominators are positive. These inequalities constrain the original
law; they do not identify its branch or marker distribution with the cap.

## 4. Sum the ENTIRE Theta lower credit into a positive sigma x omega kernel

Use the SAME independently PASSED actual probability sigma on(0,1),
rho_s=a_s/beta_s=E_sigma[xi^(s-1){s-(s-1)xi}],
beta_s=h/(lambda^s-d),h=cu/(1-u),d=1-h,
DeltaR_s=rho_s-rho_(s+1)=s E_sigma[xi^(s-1)(1-xi)^2]>0.
DeltaR_s is NOT the old signed ConditionF quantity.

Let k=c/(lambda*loglambda) and Gu_s=s*lambda^(s-1)*(1+L_s)*
a_s*delta_s/u^2, where delta_s=beta_(s+1)*DeltaR_s and
(1+L_s)r_s=1/lambda. The PASSED complete response obeys

 ThetaCredit=(Fstar-Fcap(v))/u^2
 >Thetalow=2lambda*k*sum_(s>=2)(1-1/(2s))*tau_s*Gu_s.

Substituting(171) and the actual sigma formula, and only then summing
ALL s, gives the EXACT positive integral

 Thetalow=6*k*h/(lambda*u^2) int_sigma int_omega
  xi*(1-xi)^2*sum_(j>=0)d^j*lambda^(-2j)*
       Phi(lambda^(-j)*xi*y),
 Phi(r)=(1+r)/(1-r)^4.                            (175)

Indeed lambda^(s-1)beta_s=(h/lambda)sum_j d^j lambda^(-js),
and sum_(s>=2)s(s-1)(2s-1)r^(s-2)=6(1+r)/(1-r)^4. Tonelli is
legitimate because every term is positive. All kernels are bounded
at fixed lambda: 0<xi<1,0<y<L<1 imply r<L and the j weights sum
to1/(1-d/lambda^2). Omega has finite mass t1. No log or inverse moment
assumption is hidden in the resummation.

This is an ENTIRE credit, not a finite prefix or an eventual-age price.
The two measures are actual transforms of the same original law, not
independent free variables to optimize.

## 5. A whole-credit moment/dispersion price, at all actual hard parameters

Normalize sigma2(dxi)=2xi(1-xi)^2*sigma(dxi)/DeltaR2, and Omega=omega/t1.
Both are actual probabilities. Put

 xbar=E_sigma2 xi=2DeltaR3/(3DeltaR2),
 xsecond=E_sigma2 xi^2=DeltaR4/(2DeltaR2),
 ybar=E_Omega y=t2/(2t1), ysecond=E_Omega y^2=t3/(3t1),
 vx=xsecond-xbar^2>=0, vy=ysecond-ybar^2>0,
 Atheta=3*k*h*t1*DeltaR2/(lambda*u^2)>0.

Phi is separately convex after multiplying xi and y, because its
positive power series has Phi''(r)=(28+12r)/(1-r)^6>=28 for r>=0.
Two legitimate successive Jensen inequalities in(175) give

 ThetaJ=Atheta*sum_(j>=0)d^j*lambda^(-2j)*
                           Phi(lambda^(-j)*xbar*ybar),
 ThetaDisp=14*Atheta/[1-d/lambda^4]*
                        [xsecond*vy+ybar^2*vx]>0,
 ThetaCredit>Thetalow>=ThetaJ+ThetaDisp>0.           (176)

To prove the quantitative remainder, first condition on xi and use
strong convexity in y, obtaining 14lambda^(-2j)xi^2*vy. Then apply
strong convexity in xi at ybar, obtaining14lambda^(-2j)ybar^2*vx.
Multiply by the j weight and sum the ENTIRE geometric series
sum_j d^j lambda^(-4j)=1/(1-d/lambda^4). The strict original s2
Theta surplus remains untouched, so nonstrict (176) is sufficient.

This is a rigorous general actual-law SIZE relationship using t1,t2,t3
and three consecutive actual canonical shape defects, with the complete positive
Lambert series retained. It is not a two-point offspring reduction or
an assumed positive arbitrary marker/response relaxation.

## 6. The still-unpaid signed kernel and how the new input enters

Original (165) is STILL OPEN. Its full floor is the independently
PASSED Fcap(v)/u^2=M[P+u(t^2/q-2H)+(u*t/q)Gplus]+2alpha*Gu.
Together with(176), one rigorous sufficient test is the same complete
energy price with ThetaJ+ThetaDisp replacing Thetalow on its RHS.
This test has NOT been proved universally. The exact nonnegative
remainder Thetalow-ThetaJ-ThetaDisp remains available rather than being
declared negligible.

For direct signed-kernel comparison define phi_s(xi)=xi^(s-1)[s-(s-1)xi],
A_s=lambda^(s-1)*a_s*beta_s*W_s(v),
B_s=2s*lambda^(s-1)*beta_(s+1)*
 [a_s*C_s+lambda*k*(1-1/(2s))*(1+L_s)*t_(s-1)],
K(xi)=-2(v/c)uL1+sum A_s phi_s(xi)+B_s[phi_s(xi)-phi_(s+1)(xi)].
Then EXACTLY Fcap(v)+u^2*Thetalow=E_sigma K(xi). This retains P via
the entire signed diagonal A_s and ALL log/canonical response in B_s.


The signed kernel has a COMPLETE chord-and-tail expansion, not a finite
paid prefix. K0=K(0)=-2R*u*L1+A1_coeff+B1_coeff,
K1=K(1)=-2R*u*L1+sum A_s, Pi_i=B_i-sum_(s>i)A_s. Exactly

 E_sigma K=rho2*K1+(1-rho2)*K0+sum_(i>=2)Pi_i*DeltaR_i. (177)

Indeed phi_s-phi2=-sum_(i2)^(s-1)(phi_i-phi_(i+1)); all signed
exchanges are legitimate by the fixed-lambda polynomial-geometric bound.
For a finite N its endpoint B_N*(phi_N-phi_(N+1)) is INCLUDED in
the i=N tail price; it is not dropped. The new ALL-order actual SIZE
(169) gives a rigorous corresponding bound on every complete B_s:

 B_s>2s*lambda^(s-1)*beta_(s+1)*a_s*
  [C_s+lambda*k*(1-1/(2s))*(1+L_s)*gamma*(1-u/nprev)], s>=2.

One may further lower this by nprev>=z>zH, without assigning a law.
Universal Pi_i>=0 and positivity of the root chord are NOT proved;
(177) is the concrete signed-kernel comparison for the continuing165.

There is also an EXACT curvature comparator. Write q=(1-xi)^2 and
Dq=-(2(1-xi))^(-1)*d/dxi. On every compact subset of 0<xi<1,

 Dq^2 K=sum_(i>=2)i(i-1)(i+1)*xi^(i-2)*Psi_i/[4(1-xi)],
 Psi_i=A_(i+1)+B_(i+1)-B_i.                       (178)

For finite N the numerator includes i=2,...,N-1 AND the explicit
endpoint -N(N-1)(N+1)*B_N*xi^(N-2). The polynomial-geometric
bound makes this endpoint tend to zero and permits termwise
differentiation on the stated compact subsets. Neither Psi_i<=0 nor
concavity in q is asserted. Both (177) and the finite version of (178)
have now passed 8 arbitrary-coefficient exact identities, N=2,...,5,
in marker_complete_chord_tail_identities.py. These identities certify
retaining all endpoints, not any sign or the inequality(165).

One hard actual diagnostic mu=.9delta1+.05delta2+.05delta100 at lambda1.1
has sampled positive chord and positive first12 full tail prices;
marker_hard_kernel_probe.json is explicitly UNCERTIFIED. It supplies
NO proof of a general kernel sign. The new proved relations(166)--(176)
are the input for controlling this full actual kernel; no all-order
coefficient sign or closure of(165) has been asserted.

Verification: calibrated_response_positive_measure_identities.py checks
the complete polynomial identity, covariance and localizing remainders,
hard variance algebra, ALL infinite-series generating functions and
quantitative Jensen constant. Manual actual positivity/Tonelli and
strictness proofs are above. New results SELF-CHECKED/audit PENDING. ALL18 generic identities also
PASS both exact V8/BigInt and native Python/Sympy, exit0. The 8 new
finite-chord/curvature identities also pass native Python/Sympy; total
26 native identities, with no unchanged-script rerun.

4 October2026 independent audit UPDATE: ALL(166)--(178),26 exact identities
and manual actual positivity/strictness/Tonelli/Jensen proofs nowPASS the
SAME sole auxiliary. See audit_receipt_calibrated_response_20261004.md.
All165/universal kernel signs remainOPEN. No unchanged accepted rerun.
