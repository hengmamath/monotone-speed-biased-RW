# A short rational reduction of the active low-escape kernel

3 October 2026. The transformations and lower bounds below are COMPLETE
SELF-CHECKED / independently PASSED the same sole parent-arranged reviewer.
The final rational sign lemma is not included in that audit receipt;
it has now independently PASSED via hybrid_rational_sign_certificate.py
and the full assembly in general_sqrt2_monotonicity.md.
This stays within the active general low-x hybrid route;
there is no asserted new speed theorem or numeric proof.

The fresh root-participation covariance in
root_participation_covariance_bound.md is an independently useful true
negative-I variance budget. The reduction here uses the already PASSED
canonical four-moment bound and h<1/(lambda+1); it does not need to
discard or postulate that new covariance. Both retain the original mu.

## 1. A rational entropy-age lower bound

Let ell=log(lambda), c=lambda-1 and theta=lambda*x/(c+x). The low-x
interval0<x<=1/(lambda+1) is exactly0<theta<=1/lambda. Direct algebra gives

    Rg(x)=-1/c-log(theta)/[ell*(1-theta)].                 (1)

In particular Rg at theta0=1/lambda is1. Set

    Rrat=1+9lambda*(1-lambda*theta)
               *[28lambda+17+(17lambda+19)theta]
      /[c(lambda+1)(2lambda+7)(2lambda+1)(2+7theta)(2+theta)]. (2)

Then Rg>=Rrat>=1. Here is a two-interval proof rather than a log series
or large certificate. With B_theta(t)=theta+(1-theta)t,

    -log(theta)/(1-theta)=integral_0^1 dt/B_theta(t),
    Rg-1=(theta0-theta)/ell
       *integral_0^1 (1-t)dt/[B_theta(t)B_theta0(t)].       (3)

The reciprocal product is convex in t (its second derivative is a sum
of three nonnegative terms). Jensen under weight(1-t) on[0,1/2] and
[1/2,1] uses masses3/8,1/8 and means2/9,2/3. It lower-bounds the integral
by

    lambda*[243/{8(2+7theta)(2lambda+7)}
                         +9/{8(2+theta)(2lambda+1)}].    (4)

The trapezoid bound for the convex1/t on[1,lambda] is
ell<=c(lambda+1)/(2lambda). Substitute it into(3), use(4), and combine
the two fractions. Their numerator is
36[28lambda+17+(17lambda+19)theta], giving exactly(2).
All inequalities are valid for everylambda>1 and low x; at theta0
equality Rg=Rrat=1. No canonical-law replacement is involved.

## 2. An exact quadratic lower envelope in U

Let a=E U, s=E U^2/a, U=Y/(c+Y) in[0,1/lambda], and r=v/(1+v).
For any R>=1, transform the actual signed kernel with
A(x,Y)=c+x+(1-x)Y. Direct expansion gives

    [2R P_v(Y)-Pc(Y)]/[(1+v)A(x,Y)^2]
        =[-C+L U-K U^2]/[(c+x)^2(1-theta U)^2],          (5)
    C=2r(1+cR),
    K=lambda*(c+C),
    L=c+2(lambda+1)r+2Rc(c+2r).

Set Dlin=L-2theta*C>0 and Ecurv=-K+2theta*L-3theta^2*C.
The positivity of Dlin follows directly from

    Dlin=c+2r[(lambda+1)-2theta]+2Rc[c+2r(1-theta)].

All terms are positive forlambda>1,theta<=1/lambda and0<=r<1/2.
Exact division in(5) yields

    (-C+L U-K U^2)/(1-theta U)^2
       =-C+Dlin U+U^2 j(U),
    j(U)=[Ecurv-theta^2 Dlin U]/(1-theta U)^2.

Its derivative is

    j'(U)=theta[2Ecurv-theta Dlin-theta^2 Dlin U]
                                              /(1-theta U)^3.

The numerator decreases in U, so j has at most an interior maximum,
and its minimum is at0 or1/lambda (also valid at theta=0). Therefore

    j(U)>=min(Ecurv,
                  [Ecurv-theta^2 Dlin/lambda]/(1-theta/lambda)^2). (6)

This quadratic lower bound has no higher tilted-moment assumption.
Its expected sign is strictly positive if BOTH rational quantities

    B0=-C+Dlin*a+Ecurv*a*s,
    B1=(-C+Dlin*a)(1-theta/lambda)^2
                          +(Ecurv-theta^2 Dlin/lambda)*a*s       (7)

are strictly positive. (5)--(7) are exact algebra and a proved bound;
the sign in(7) is NOT asserted.

## 3. One explicit remaining GENERAL sign lemma

Under actual I<=0, the PASSED harmonic constraint gives0<a<1/lambda^2.
The PASSED four-moment speed bound in general_first_generation_positive.md
supplies

    D2=lambda+1-lambda*a,
    D3=lambda^2+lambda+1-lambda(lambda+1)a,
    D4=lambda^3+lambda^2+lambda+1-lambda(lambda^2+lambda+1)a,
    a<=s<=1/D2,
    E4=c[1+lambda*s^2+lambda^2(D2/D3)^2*s^2]
                                           +lambda^4(D2/D4)^2*s^2,
    B=1-lambda*a+lambda*a*s*(1-lambda*s)>0,
    r<=rup=a*E4/[2(B+a*E4)]<1/2.                          (8)

Precise remaining rational lemma: for EVERY

    sqrt(2)<=lambda<=39/20,
    0<a<1/lambda^2, a<=s<=1/D2, 0<=theta<=1/lambda,

the two expressions B0,B1 in(7), using R=Rrat from(2) and r=rup from(8),
are strictly positive. This was UNPROVED when this reduction was audited.
It is now COMPLETE SELF-CHECKED with the exact integer certificate in
hybrid_rational_sign_certificate.py; independent audit of those new signs
and final assembly is pending. See general_sqrt2_monotonicity.md.
Diagnostic floating-point values were used only to select this candidate;
they supply no verification or proof dependency.

Why this lemma WOULD settle the active kernel: the PASSED actual Psi>0
means replacing Rg by its smaller Rrat can only decrease the expected
signed kernel. For fixed Rrat, its integrand divided by(1+v) decreases
strictly in r: the derivative in the original y variable is

    -2Rrat(y^2+c)-2(1-y)<0.

Thus replacing actual r by rup also gives a lower bound. If(7) were
proved at these replacements, (5)--(8) would imply the actual low-x
kernel2Rg Psi-JPc>0. The PASSED high-x kernel and eta>=max(g,b)pi
would give full D>0 under I<=0. Together with the PASSED I>=0 result
this would give unconditional strict decrease fromsqrt(2), not the full
original1<lambda target. This consequence is CONDITIONAL ONLY.

No new subagent, general two-point reduction, infinite-tree derivative,
unproved integrability, off-range counterexample catalog, or threshold
tuning was used. The full averaged-w route remains available if this
exact stronger rational comparison fails.

Verification: SymPy was already present. Four full symbolic identities
were cleared and factored to zero: the y-to-U signed-kernel coefficients,
the exact quadratic division, the j derivative, and the combination of
the two Jensen fractions into(2). These checks verify complete algebraic
identities, not finitely sampled signs. They do NOT check or establish
the universal sign lemma(7). That sign is now proved by a SEPARATE finite
integer certificate, SELF-CHECKED / independent audit pending.

## Independent reduction audit receipt

The same sole reviewer accepted the complete covariance/Rrat/rational
reduction: w factors and strictness, Jensen weights and combination,
normalized-r derivative, quadratic division and endpoint minimum logic.
The final B0/B1 sign was explicitly outside that receipt. At a=0 the
unfactored B0/B1 vanish, so a closed-domain certificate must first divide
by the common positive a (or permit boundary zeros). The new certificate
script divides by a BEFORE clearing denominators; its sign status is
recorded separately from this completed reduction audit.
