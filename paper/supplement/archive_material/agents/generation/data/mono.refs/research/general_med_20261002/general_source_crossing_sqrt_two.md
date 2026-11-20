# General finite-mean source crossing from sqrt(2), via actual tilted recursion

3 October 2026. Complete source-shape theorem and conditional speed-sign theorem;
independently passed the same sole parent-arranged reviewer. General fixed leafless mu,
mu(1)>0, finite1<m<infinity, only finite mean. This does not prove speed
monotonicity in the negative-I region or change the audited unconditional
general-law threshold39/20.

## Statement

Fix sqrt(2)<=lambda<m. If the original actual speed satisfies
v<=1/(lambda+1), the actual complete root source B(t) has exactly one
positive-to-negative zero. Every zero is strict; no touching or flat
zero can occur. Global monotonicity of B or G is not claimed.
In particular the source conclusion holds in the uncovered original
harmonic region h<1/(lambda+1), since the audited v<h is strict.

Consequently, for any original h, if I>=0 then v_mu'(lambda)<0.
The case I=0 is included and gives a strict sign. If I<0, crossing
alone does not establish the speed sign; entropy/response compensation
remains a separate quantitative obligation.

Previously independently audited inputs: canonical actual-law interfaces,
v<h, harmonic-h sign region, signed source and normalized derivative,
source endpoint signs, and complete decreasing-response transfer. New
input: the actual-tilt stochastic supersolution, full-law degree resolvent
and variance-adapted bound (4) in general_tilt_degree_harmonic.md.
Their proofs are explicit; none constructs a binary reference GW law.

## 1. General downward-zero lemma when the tilted mean is at least2

Assume the actual v<=1/(lambda+1). Then

    beta=(lambda+1)v-c<=2-lambda.                (1)

At any t>0 put n=n_t, V=Var_t nu, K=n+V/(n-1),
u=u_t, R=E_t X^2/u, e=R-u, a=3+v, r=(n-1)/n.
Every quantity is from the actual exponential child/degree tilt at
the fixed original mu and bias. All degree moments exist at t>0.

At a zero G=B/(n*u)=0, the exact zero-eliminated identity, before any
degree-excess lower bound, is

    G'/2=-a*(V_Xstar+e^2)/2
          +e*[beta-(a/2+2j_t/n)*u]
          -u^2*V_nustar-v*lambda^2*V/n^2.        (2)

If n<=lambda^2, the already audited original derivative formula has
all nonpositive terms and a strictly negative final degree-variance
term. Hence G'<0 there, without using (2).

Consider n>lambda^2 and n>=2. Then n>lambda, and the new actual-tilt
bound u>=(n-lambda)/K, together with j_t/n=K*r, gives

    beta-(a/2+2j_t/n)*u
       <=beta-2*(n-1)*(n-lambda)/n-a*u/2.        (3)

For1<lambda<2, the function (n-1)(n-lambda)/n increases on n>=2,
since its derivative is1-lambda/n^2>0. At n=2 its doubled value is
2-lambda. Therefore (1) and a*u/2>0 make (3) strictly negative.
Forlambda>=2, (1) makes beta<=0, while n>lambda makes the
subtracted term positive; again the bracket is strictly negative.

All remaining terms of (2) are nonpositive, and V>0: mu_t still has
positive mass at1 and at some genuine degree. The final term is strictly
negative because v>0. Thus

    G(t)=0, n_t>lambda^2, n_t>=2 => G'(t)<0.      (4)

This is a genuine general zero-sign lemma, not a finite-moment model or
a claim that the actual tilted law is fixed by mu_t.

## 2. Every zero descends when lambda>=sqrt(2)

Every zero with n_t<=lambda^2 descends by the audited derivative.
Every other zero has n_t>lambda^2>=2 and descends by (4). Hence all
zeros have strictly negative derivative throughout the stated bias range.
The left endpoint sqrt(2) is included; equality n=lambda^2 is already
covered by the strict degree-variance term.

## 3. Continuity, endpoint signs, and no hidden tangency

For any compact positive t interval, bounded child transforms and
the factor phi(t)^k with phi(t)<1 dominate every required polynomial
degree moment. Thus G is C1 at every t>0 with no original second/third
offspring moment assumption. Its denominator n_t*u_t is strictly positive.

The positive initial source is an independently audited general-law
lemma. If E nu^2=infinity then B(t)->+infinity at0. Otherwise, writing
u0=EX and using m*u0<=m-lambda, v<=u0/(2-u0), z0>=u0^2,
j0>=m(m-1), the adverse v-coefficient substitution gives

    B(0)>=2u0/(2-u0)*{(2lambda-1)m-lambda^2
                           +m*u0[2(m-lambda)+1-m*u0]}>0.

If that coefficient is nonnegative, simply delete its nonnegative term.
Therefore G>0 on some initial interval in both cases.
Arbitrarily long initial unary chains give essinf X=0; X>0 almost surely
gives phi(t)->0. Exponential child tilting yields u_t,z_t->0 and the
degree law yields n_t->1,j_t->0. Thus

    B(t)->2v(1-lambda^2)<0, G(t)->-infinity.

In particular all zeros lie in a compact subinterval of (0,infinity).
Continuity gives at least one zero. Every zero has negative derivative,
so is isolated with positive sign immediately to its left and negative
sign immediately to its right. Infinitely many compact zeros would have
an accumulation zero with derivative0, contradiction. If there were two
consecutive zeros, their incompatible intervening signs would force an
additional zero between them. Hence there is exactly one t_c, with
G>0 before and G<0 after. There is no tangency, flat zero or additional
upward crossing. Since n_t*u_t>0, B has the same signs.

## 4. Conditional complete-response speed sign, including I=0

The previously audited full actual response identity is

    D=lambda^(-1)*integral w(t)B(t)dxi(t),
    dxi=t*exp(-ct)*f(phi(t))dt, I=integral B dxi.

The actual susceptibility w is bounded, positive and strictly decreasing.
All signed integrals are absolutely finite using only E nu<infinity.
The unique crossing gives

    lambda*D=w(t_c)I+integral[w(t)-w(t_c)]B(t)dxi(t)>w(t_c)I.

The last integral is strictly positive: both factors have the same strict
sign on either side and dxi has a positive density on t>0. Therefore
I>=0 implies D>0 and v'=-D/Z<0, including I=0.
If h>=1/(lambda+1), the already audited harmonic sign theorem supplies
v'<0 independently, so the conditional speed statement holds for any h.

## Precise remaining general mechanism

Under the same actual speed condition, for1<lambda<sqrt(2) the only
unproved downward-zero region is

    lambda^2<n_t<2, original h<1/(lambda+1).

There the exact general quadratic (6) of general_tilt_degree_harmonic.md
retains the actual child size-biased variance, a helpful e^2 term, and
the nonnegative multi-degree excess Tdeg. The full-law harmonic resolvent
and the original weighted-harmonic child bound can be inserted without
using an arbitrary fixed point or a two-point offspring reduction.
Forlambda>=sqrt(2), general negative-I full-response compensation remains
open even though the shape is now settled in the uncovered h region.

Status: complete source/conditional-sign proof, independently passed.
Unconditional general speed theorem remains39/20; cross-one joining is
separate; no agents created or original user materials modified.
