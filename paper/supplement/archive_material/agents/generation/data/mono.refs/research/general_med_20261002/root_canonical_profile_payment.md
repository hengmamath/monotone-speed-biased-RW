CURRENT4October: the analytic lower-profile reduction survives, but its alleged universal three-term SIZE certificate is WITHDRAWN. Corrected S3 is negative at an exact relaxed point; root SIZE remains OPEN. The separately accepted707/500 theorem andF/J(E) are intact.

# Joint canonical absorption and a pipe-exact root profile

4 October 2026. COMPLETE local proofs, SELF-CHECKED; independent audit
PENDING. A SUBSEQUENT complete root SIZE certificate is saved in
general_2_over_sqrt3_root_glue.md; its independent audit is PENDING.
The original theorem below2/sqrt(3) remains OPEN.
Sole main task; no agent created. This continues the independently PASSED
global F/J(E), rather than repeating a rejected scalar variance floor.

Use the notation of condition_F_root_payment.md: c=lambda-1,
u=a1, b=a2, eps_s=a_s-lambda*a_(s+1), w_s=s*lambda^(s-1),
r_s=beta_(s+1)/beta_s, delta_s=a_s*r_s-a_(s+1),
Theta_s=k*beta_s*(-rho'(s)), k=c/(lambda*log(lambda)), and
Delta_s=t_(s-1)-(1-a)*a_s>=0 for s>=2. The hard case has
0<a<1, t0=0, and a=(u-v*A0/c)/b, A0=1-(lambda+1)u+lambda*b>0.
All laws and the marker sigma remain their ACTUAL canonical objects.

## 1. One absorption inequality for every nonroot index

The PASSED v<h gives, by exact calibration,

 a > (u-h*A0/c)/b = lambda*h/c*(u/b-1)
   > lambda*h/c*(1/r1-1) = lambda^2*u.                 (72)

Thus u<1/lambda^2, and 1-a<1-lambda^2*u. Set

 e_s=1-lambda*r_s>0,
 L_s=c*d/[lambda*(lambda^s-d)]>0,
 C_s=k*(1-1/(2*s))/r_s,
 B_s=(1+v)*e_s^2/lambda+2*(1-a)*(r_s-r_(s-1))>0.

The exact PASSED gamma/marker identities give

 gamma_(s-1)=a_s*(r_s-r_(s-1))-delta_s+Theta_s,
 Lambda_s:=gamma_(s-1)+eps_s/lambda=a_s*L_s+Theta_s,
 Theta_s>C_s*delta_s.                                (73)

For every lambda>=23/20 and integer s>=2,

 e_s+(1-lambda^2*u)*(C_s-1)>0.                        (74)

If C_s>=1 this is immediate. Otherwise (72) and v>0 imply
(1+v)*e_s+(1-a)*(C_s-1)>0 as well.

Proof of (74): convexity of 1/x on [1,lambda] gives
log(lambda)<c*(lambda+1)/(2*lambda), hence k>2/(lambda+1).
For s>=8, r_s<1/lambda and
C_s>15*lambda/[8*(lambda+1)]>=345/344>1.
For s=2,...,7 set

 N_s=lambda^s*(1-u)-1+lambda*u,
 D_s=lambda^(s+1)*(1-u)-1+lambda*u,
 P_s=s*(lambda+1)*N_s*(D_s-lambda*N_s)
       +(1-lambda^2*u)*[(2*s-1)*D_s^2-s*(lambda+1)*N_s*D_s].

The denominator s*(lambda+1)*N_s*D_s is positive, and P_s is its
product with (74) using the smaller k=2/(lambda+1).
After u=t/lambda^2, H_s=lambda^2*P_s/c^2 is a polynomial of degree
(2*s+2,3). Expand lambda=23/20+L, and convert ONLY t to degree-three
Bernstein coefficients. Every L-power coefficient is nonnegative;
the four constant-L coefficients are strictly positive. The six
polynomials contain 288 coefficients, 261 positive. The short exact
script rebuilds the original P_s and every coefficient, not a rounded
array. Thus this verifies (74) on the entire lambda>=23/20,0<=t<=1.

Writing xi_s=Theta_s-C_s*delta_s>0, the full absorption is

 (1+v)*eps_s^2/lambda+2*(1-a)*a_s*gamma_(s-1)
 =a_s^2*B_s
   +2*a_s*delta_s*[(1+v)*e_s+(1-a)*(C_s-1)]
   +(1+v)*lambda*delta_s^2+2*(1-a)*a_s*xi_s
 >a_s^2*B_s.                                        (75)

Combining (75) and Lambda_s>a_s*L_s with the COMPLETE root identity,

 F_star > Root+sum_(s>=2) w_s*a_s^2*B_s
                   +2*sum_(s>=2)w_s*a_s*L_s*Delta_s,  (76)
 Root=[(1+v)*eps1^2-2*(1-a)*u*eps1]/lambda.

This absorbs ALL low and high adjacent/log deficits jointly. It does
not say that the remaining positive sums pay Root. Every comparison
is EXACT in the endpoint-one pipe limit, including its unary ages.

## 2. A new lower profile from the ACTUAL marker, with no unknown p

The PASSED marker is a probability sigma on (0,1), and
rho_s=E_sigma[t^(s-1)*(s-(s-1)*t)]. Put

 rho2=b/beta2, T=1-sqrt(1-rho2),
 f_s(T)=T^(s-1)*(s-(s-1)*T), A_s=beta_s*f_s(T).

For all integers s>=2,

 rho_s>=f_s(T), and a_s>=A_s.                        (77)

Indeed X=(1-t)^2 has EX=1-rho2. The function
F_s(X)=(1-sqrt(X))^(s-1)*[1+(s-1)*sqrt(X)] has derivative
-s*(s-1)/2*(1-sqrt(X))^(s-2), which is increasing.
Hence F_s is convex on [0,1] (affine for s=2), and Jensen proves (77).
No assertion that arbitrary sigma reconstructs a physical law is made.
The profile is exact at s=1,2 and on EVERY full pipe (rho2=T=1).

Since rho_(s-1)<=1,
a_(s-1)/a_s<=1/[r_(s-1)*f_s(T)]. Consequently, define

 M_s=a*(1-r_s)+(v/c)*[lambda+1-lambda*r_s
                                  -1/(r_(s-1)*f_s(T))].

Actual canonical next-moment bounds and calibration give
Delta_s/a_s>M_s, while F gives Delta_s>=0. Thus

 F_star > Root + sum_(s>=2)w_s*A_s^2
                         *[B_s+2*L_s*max(0,M_s)].    (78)

This is a NEW sufficient universal scalar SIZE lemma. The subsequent
three-term physical certificate now proves it in the active gap,
SELF-CHECKED and awaiting independent audit.
It preserves the entire canonical pipe profile without using a free
branch mark, a geometric moment floor, or a minimum log slope.
Omitting terms of this positive sum yields valid finite lower bounds.

## 3. Assigned second-prefix cap is legitimate for the COMPLETE floor

For a fixed actual escape law, use the EXPLICIT polynomial extension
F_tilde(v,a)=2aEbr0-E[b_tree J P_c(v)]+2E[g(J P_v-a*q0)]
=D_tilde_g(v)+2aGamma, whereGamma>0 is fixed. At the actual speed only,
E[b_tree J P_c(v_*)]=C_pair(v_*), andF_tilde(v_*)=F_star. Off speed their
exact correction is(vZ-N)/lambda; see assigned_polynomial_extension.md.
Directly in these fixed bounded polynomial kernels,

 dD_tilde_g/dv=2*c*E[g(X)*J(y-1)(X)]
            -E[b_tree(X)*J((1-y)*(2-y))(X)]<0.

Along a(v)=(u-v*A0/c)/b, its derivative is -A0/(c*b)<0;
therefore the COMPLETE F_tilde(v,a(v)) strictly decreases in v.
This is differentiation of a finite affine expression at a FIXED law,
not differentiation of the random law or use of pipe speed for a block.

The PASSED Gram proof supplies kappa<K<k0, with
k0=[lambda^2+13*lambda+6-lambda*(3*lambda+7)*u
                                 +2*lambda^2*u^2]/(12*lambda).
For 23/20<=lambda<=3/2,0<=u<=1/lambda^2,

 (1+lambda*u)*k0<2.                                 (79)

After clearing the positive denominator, its four t=lambda^2*u
Bernstein coefficients are

 -lambda^3*(lambda^2-11*lambda+6),
 -lambda^2*(3*lambda^3-32*lambda^2+28*lambda-1)/3,
 -lambda*(lambda-1)*(3*lambda^3-28*lambda^2+10*lambda+5)/3,
 -(lambda-1)^2*(lambda^3-8*lambda^2-lambda+2).

All are positive: the three cubics have negative derivatives on this
interval and are negative already at23/20; the first quadratic is
negative by the elementary endpoint bounds. Also K>1 follows from
K>2/(lambda+1)+(1-1/lambda^2)/2>1 on this interval.

Let v_bar=V2(K) from the audited Gram proof, using the SAME actual
u,b and replacing only kappa by the proven upper bound K.
Direct Q2/T2 algebra shows V2(K)<=v_pi(K) when K>1:
with rho=b/beta2<=1 the numerator of that ratio comparison is
(1-rho^2)*u^3*(K-1)/(1-u)
 +lambda*(rho-rho^2)*u*beta2*T_pi(K)>=0.
By (79), v_pi(K)=c*u*K/[2-(lambda+1)*u*K]<h.
Thus v<v_bar<h and a_bar=(u-v_bar*A0/c)/b>lambda^2*u.
The PASSED strict J2(K,e)>0 is precisely Delta2(v_bar,a_bar)>0;
since -u+(lambda+1)b-lambda*e=-E[U(1-U)(1-lambda*U)]<0,
it also implies a_bar>0. In the ACTUAL hard case a_bar<a<1.
The upward-zero argument consequently gives every assigned Delta_s>=0.
All of (75)--(78) apply to this assigned pair, and

 F_star(actual)=F_tilde(v_*,a)>F_tilde(v_bar,a_bar)>the RHS of(78)
                                  evaluated at(v_bar,a_bar). (80)

This reduces the next sufficient lemma to explicit lambda,u,T:
b=beta2*T*(2-T), v_bar=V2(K), a_bar by calibration, actual feasibility
b>=u^2 and a_bar<1. The exact sum (78), or a finite positive truncation,
must still be proved nonnegative. NO sign conclusion is asserted yet.

## 4. Certified checks and next boundary

The original audited rare family lambda6/5, low skeleton
(149/150)delta1+(1/150)delta4, mean51/50, has
u/epsilon->1/(lambda-r), b/u->3/7, rho2->33/35.
The conservative rational T=19/25 is valid because(1-T)^2>2/35.
The NEW lower profile (78), including Delta, has normalized leading
coefficient>1/10000, using64 terms and exact rational a0 intervals.
Even the larger assigned V2(K) passes the same strict check. Ignoring
the Delta payment instead gives a negative partial bound, so it cannot
be discarded. These are one-family certified asymptotic FLOOR checks,
not a universal proof or a new population computation.

SUBSEQUENT COMPLETE SELF-CHECKED: (78)/(80) is paid by onlys=2,3,
using actual b>=u^2. The full covering parameter box has all38998
rational Bernstein coefficients strictly positive; complete clearing
identities pass. See general_2_over_sqrt3_root_glue.md and the exact
root_three_term_payment_certificate.py/.identities.py files. Independent
audit PENDING; the accepted threshold remains707/500. The original
below2/sqrt3 gap and joining at1 remain OPEN.


4 October2026 PRIORITY AUDIT REJECTION: the new38998-coefficient root
certificate and proposed general2/sqrt3 threshold are WITHDRAWN. CodeC
used AN=A1*(VD-u*Rnum*A0num), an erroneous extra u; the correct
calibration is AN=A1*(VD-Rnum*A0num). CodeB also tested the wrong
(1-u*V*A0/c)/z instead of(1-V*A0/c)/z withV=v_bar/u. The old result
certifies a wrong assigned a; no new speed threshold follows. Accepted
general707/500 remains intact. Old scripts retained as obsolete wrong-
calibration artifacts; rebuilding originalS3 plus independent complete
calibration/clearing identities is the sole priority. CodeA's288
absorption certificate independently PASSED; remaining interface and
corrected SIZE sign are PENDING. No agent created.

LATEST4October2026 INDEPENDENT AUDIT PASS from SAME sole reviewer:
The CORRECTED u<=1/2 package includes this analytic interface. Explicit
assigned extension, off-speed correction, strict derivative, assigned
parameter range, original root regrouping, all-index absorption, canonical
Jensen/moment replacement and positive-term deletion all PASSED. The
wrong38998-calibration global proof remains WITHDRAWN; only the corrected
9600-coefficient small-u result is accepted. NEW high-u Root+s2 payment
is separately SELF-CHECKED/auditPENDING, inhigh_u_original_root_s2_result.md.
