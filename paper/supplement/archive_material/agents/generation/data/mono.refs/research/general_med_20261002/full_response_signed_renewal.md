# A positive full-response renewal measure and a signed iid source

Updated 3 October 2026. **Complete derivations through Proposition 4 passed one
independent local audit arranged by the parent, using the same sole
reviewer. Repaired Proposition 5 subsequently passed the independent
bias-2 proof audit on 3 October. The final general renewal-balance
inequality below2 is open.** This uses the actual canonical law and the full R, without stopping
at a first branch. It is not a new D_u sign claim. The kernel symmetry
mechanism was already retained in `../../evidence/exclusions/adaptive_corrector_report.md`;
the positive Gamma renewal and the signed conditional-variance source below
are additional explicit derivations relative to that source map.

Use all notation and audited hypotheses of `response_interface.md`.
Write the offspring pgf as f(z)=E z^nu, to distinguish it from test
functions. Write phi(t)=E exp(-tX), a(t)=E X exp(-tX), and
b2(t)=E X^2 exp(-tX). Only E nu=m<infinity is assumed.
All function pairings <u,w> mean integral u(x)w(x) pi(dx), where
pi is the actual canonical escape law at the fixed lambda. J, L and R
act on C([0,1]) as in the audited interface. When a kernel is tested
against a finite signed measure, its measure-domain extension is used;
no unproved L2 boundedness of L is asserted.

## Proposition 1: the full adjoint kernel has a positive Laplace measure

Put Q=RJ and k=Qb. Then Q has a bounded continuous symmetric positive
kernel on [0,1]^2, and k is positive. There are finite positive measures
sigma and zeta on [0,infinity) such that

    k(x)=integral exp(-t*x) sigma(dt),
    rho(s):=F'(s)k(F(s))=integral exp(-t*s) zeta(dt).

They are the actual Neumann-series response measures, and obey

    sigma(dt)=sigma0(dt)+f'(phi(t))*zeta(dt),
    zeta=K sigma,
    sigma0(dt)=t*exp(-c*t)*f'(phi(t))*a(t)/lambda^2 dt.       (1)

The explicit positive kernel K is

    K(s,dt)=exp(-s-lambda*t)
       sum_{j>=0} lambda^(j+1)*s^j*t^(j+1)/[j!*(j+1)!] dt. (2)

Its total mass is 1/lambda. Equivalently, lambda*K(s,.) is the law
Gamma(2+N,rate=lambda), with N Poisson(s). This is a representation of
the original response, not a replacement canonical fixed point.
Here s is the input variable, t is the output variable. For a function
u, (K u)(s)=integral u(t)K(s,dt); for a measure eta, the notation
K eta denotes the output measure A -> integral K(s,A)eta(ds).
The masses are sigma([0,infinity))=k(0),
zeta([0,infinity))=k(0)/lambda, and sigma0([0,infinity))=Jb(0).

### Proof and finite-mean justification

Denominator cancellation gives the symmetric kernel

    (LJ)(x,y)=lambda^(-1) E[nu/(c+x+y+S_(nu-1))^2].

Both J and LJ are symmetric as maps from finite signed measures to
continuous functions. Thus LJ=JL*, and by induction L^n J=J(L*)^n,
so every L^n J is symmetric. The audited r0 contraction gives uniform
convergence of its kernels (the input kernels J(.,y) are uniformly
bounded in the r0 norm). Hence Q is symmetric, continuous and bounded.
In particular Q can be paired with every L1(pi) test.

The actual recursion gives directly

    Jb(x)=lambda^(-2) E[S/(c+x+S)^2]
         =integral exp(-t*x) sigma0(dt).

For any finite positive Laplace measure eta, expand

    F'(x)exp(-s F(x))
       =lambda*exp(-s)/(lambda+x)^2
          sum_{j>=0}(s*lambda)^j/[j!*(lambda+x)^j].

The elementary gamma integral for (lambda+x)^(-j-2) gives (2),
with all exchanges nonnegative. Integration of each gamma term yields
the mass 1/lambda. If a function has Laplace measure eta, then L of
that function has Laplace measure f'(phi(t))*(K eta)(dt): the remaining
nu-1 children are iid. Since f'(phi)<=m, this is finite.

Starting at eta0=sigma0, let eta_(n+1)=f'(phi)*K eta_n.
The mass sum equals sum_n (L^n Jb)(0)=k(0)<infinity, by the audited
resolvent. Thus sigma=sum eta_n is a finite positive measure and (1)
holds. Its Laplace transform agrees with k on [0,1], and defines its
extension to all x>=0. No differentiation of an infinite tree, offspring
second moment, or abstract complete-monotonicity theorem is needed.
The density (2) shows zeta has no atom at zero.

## Proposition 2: exact signed root-configuration source

Define the polynomial

    Pc(y)=(1+v)y^2-(1+3v)y+2v.

Then, with the actual root list S=sum_i X_i,

    D=E[rho(S){2 S^2+2[c-(lambda+1)v]S
                     +(1+v)sum_i X_i^2+2v(nu-lambda^2)}]. (3)

The positive function rho in (3) retains the complete response. In
particular it is not a freely chosen decreasing weight.

### Proof

Centering N-vZ=0 and the exact symmetrized polynomial identity give
C=<b,J Pc>. If P(y)=y^2+c[(1+v)y-v], then D=2<b,QP>-<b,J Pc>.
For a bounded test u define, pi-almost surely,

    (Tu)(y)=(1-y)^2/lambda E[sum_i u(X_i)|F(S)=y].

T maps bounded tests into L1(pi), using E nu<infinity. The actual
iid denominator cancellation gives JT=LJ. Consequently
Q(I-T)Pc=JPc, including this L1 extension, and

    D=<k, 2P-Pc+T Pc>.

At y=F(S), multiplication by (lambda+S)^2 and elementary expansion give

    2P(y)-Pc(y)+T Pc(y)
       =lambda/(lambda+S)^2 E[2S^2+2[c-(lambda+1)v]S
                    +(1+v)sum_i X_i^2+2v(nu-lambda^2)|S].

Pairing against k proves (3). Absolute integrability is explicit:
rho(S)<=lambda*k(0)/(lambda+S)^2, sum_i X_i^2<=S, and E nu<infinity.
Therefore even the S^2 term is integrable without E nu^2.

## Proposition 3: the iid conditional-variance source

For t>0 define tilted child mean u_t=a(t)/phi(t), second moment
z_t=b2(t)/phi(t), and tilted degree moments

    n_t=phi(t) f'(phi(t))/f(phi(t)),
    j_t=phi(t)^2 f''(phi(t))/f(phi(t)).

Explicitly, the tilted child law is exp(-t*x)pi(dx)/phi(t), and
the tilted degree law gives n mass mu(n)*phi(t)^n/f(phi(t)).

All are finite at t>0. Then

    D=integral f(phi(t))*B(t) zeta(dt),                       (4)
    B(t)=(3+v)n_t z_t+2j_t u_t^2
              +2[c-(lambda+1)v]n_t u_t+2v(n_t-lambda^2).

Equivalently, under the independent exponentially tilted child and
degree laws,

    B(t)=[2 n_t^2+(1+v)n_t]u_t^2
         +(3+v)n_t Var_t(X)+2Var_t(nu)u_t^2
         +2[c-(lambda+1)v]n_t u_t+2v(n_t-lambda^2).          (5)

### Proof

Insert the positive Laplace representation of rho in (3). Each of the
unsigned terms is integrable by the preceding bounds, so Tonelli can
be applied separately, followed by subtraction. Independence of children
gives E exp(-tS)=f(phi), E S exp(-tS)=f' a,
E S^2 exp(-tS)=f' b2+f''a^2, E sum_i X_i^2 exp(-tS)=f'b2,
and E nu exp(-tS)=phi f'. These yield (4). The identity
j_t=n_t^2-n_t+Var_t(nu), together with z_t=u_t^2+Var_t(X),
gives (5). f'' at phi(t)<1 is finite even if E nu^2 is infinite.

## Proposition 4: one signed crossing, in a concrete small-speed region

If c-(lambda+1)v>=0, B(t) is strictly decreasing on (0,infinity),
starts positive (possibly +infinity), and ends at
2v(1-lambda^2)<0. Hence it has exactly one zero t_c>0.

This applies throughout the uncovered h<1/(lambda+1) region when
lambda>=2, and also whenever the actual speed v<=c/(lambda+1).
It is a shape statement for the **complete actual degree source**, not
positivity of its integral.

### Proof

Under exponential tilting, u_t and z_t decrease. Under the degree tilt
with parameter phi(t), n_t and j_t decrease, because nu and nu(nu-1)
are increasing functions of nu and phi strictly decreases. The degree
law is nonconstant, so n_t strictly decreases. Thus every positive term
in (4) decreases when c-(lambda+1)v>=0; the term 2v n_t ensures strictness.

Canonical X has essential infimum zero: arbitrarily long initial unary
chains have positive probability. Therefore u_t,z_t ->0. Also phi(t)->0,
and mu(1)>0 implies n_t->1,j_t->0. This gives the negative terminal limit.

For the initial positive sign, write u=EX. Canonical Jensen gives
u<=(m-lambda)/m. Also v<=u/(2-u): writing Z=2E[X/A]-N, the multiplier
E[X/A(X,y)] decreases in y, so N/E[X/A]<=u by covariance.
If E nu^2=infinity, then j_t->infinity and B(t)->infinity.
Otherwise j_0>=m(m-1), z_0>=u^2, and

    B(0)>=m(2m+1+v)u^2+2*c*m*u
                      +2v[m-lambda^2-(lambda+1)*m*u].

The complete coefficient of v is
m*u^2+2[m-lambda^2-(lambda+1)*m*u]. If that coefficient is nonnegative,
the lower bound is positive. If it is negative, substitute v<=u/(2-u).
The result is

    2u/(2-u){(2lambda-1)m-lambda^2
                  +m u[2(m-lambda)+1-mu]}>0.

Indeed m>lambda implies (2lambda-1)m-lambda^2>lambda*c>0,
and m*u<=m-lambda makes the last bracket positive. Continuity at t>0
and strict decrease prove the unique crossing.

## Proposition 5: explicit reversible reference and full susceptibility

Let gamma(dt)=c^2*t*exp(-c*t)dt, a probability measure. Then lambda*K
is a reversible Markov kernel for gamma. Moreover

    zeta(dt)=lambda^(-1)*t*exp(-c*t)*w(t)dt,
    w(t)=E[b(X)(R exp(-t*.))(X)],
    w=beta+K[f'(phi)*w],  beta=(a-b2)/lambda.               (8)

The function w is the Laplace transform of the positive finite weak
response measure, and is bounded. Formula (8) retains the entire actual
response and adds a concrete reversible reference for the tail problem.
Reversibility alone does not imply the sign of D.

### Proof

Termwise multiplication of (2) by gamma(ds) gives the joint density

    c^2 exp(-lambda*(s+t))
       sum_{j>=0}lambda^(j+1)*s^(j+1)*t^(j+1)/[j!*(j+1)!],

which is symmetric. The factor lambda*K gives unit transition mass;
therefore gamma is invariant and detailed balance holds. No L2
invertibility claim for an offspring-weighted kernel is being made.

The positive weak response functional eta(u)=E[bR u] obeys
eta(u)=E[bu]+eta(Lu). Apply this to exp(-t*x). The positive expansion
of F'(s)exp(-tF(s)) and iid children give the equation for w in (8).
Its finite series is inherited from the original audited resolvent.

For each t, the actual root recursion also gives

    K[f'(phi)*a](t)=E[S F'(S) exp(-tF(S))]
                   =a(t)-b2(t).

Detailed balance turns the density of K sigma0 with respect to gamma
into K[f'(phi)*a/(lambda^2*c^2)]=beta/(lambda*c^2). Successive terms of
zeta=K sigma0+K[f'(phi)zeta] thus have densities w_n/(lambda*c^2), where
w_0=beta and w_(n+1)=K[f'(phi)w_n]. Summing their nonnegative series
gives zeta=gamma*w/(lambda*c^2), which is (8). This argument identifies the
canonical response series, rather than asserting uniqueness of arbitrary
solutions of the integral equation.

The parent-arranged audit found and corrected a factor in the original
version: S*F'(S)=X(1-X), with no lambda factor. Accordingly the actual
signed integral is D=lambda^(-1)*integral t*exp(-ct)*w(t)*f(phi(t))*B(t)dt.
The positive factor lambda^(-1) affects magnitude, not sign. Propositions
1--4, sigma0, and the Stein identity are unchanged. The repaired
Proposition 5 subsequently passed the same sole reviewer's bias-2 audit.

## Exact next cancellation problem; not solved

The unresolved task in the preceding region is to control the negative
tail of the *actual* renewal measure:

    integral_(0,t_c) f(phi) B d zeta
       > integral_(t_c,infinity) f(phi) |B| d zeta.           (6)

The added mathematical input is now (1)--(2), which fixes zeta through
the full iid response, and the one-crossing theorem, not a free marginal
or moment relaxation. A proof of (6) needs a quantitative renewal/Stein
estimate for that Gamma kernel. Decreasing B or positivity of each
variance term does not by itself prove (6). A proposed potential u(t)
can be tested against the exact renewal identity

    integral [u-f'(phi) K u] d zeta = integral K u d sigma0,   (7)

whenever both sides are absolutely integrable. Finding a potential with
f(phi)B >= u-f'(phi)K u and a strictly positive right side would directly
cancel the negative tail. No such potential has been proved here.
Bounded potentials automatically satisfy the three relevant absolute
integrals: integral |u|d zeta, integral f'(phi)K|u|d zeta, and
integral K|u|d sigma0 are finite. An unbounded signed potential requires
these verifications before (7) can be used.

This is the active full-response route. It does not claim the target
theorem, a canonical counterexample, a degree-mixture reduction, or a
new universal sign threshold below2 without a separate completed audit.
