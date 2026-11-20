# General actual-tilt degree resolvent and variance tradeoff

3 October 2026. Complete key lemma; independently passed the same sole
parent-arranged reviewer. Only finite original E nu is assumed. At every t>0 the actual
exponentially tilted degree law has all polynomial moments. No general
law is replaced by a two-point offspring law.

Use the exact likelihood-ratio proof in canonical_tilt_supersolution.md:
for the one fixed original law mu and its terminal-one canonical pi,

    pi_t(dx)=exp(-tx)*pi(dx)/phi(t),
    mu_t(k)=mu(k)*phi(t)^k/f(phi(t)),
    pi_t>=_st T_(mu_t)(pi_t).                       (1)

Here T is one step of F(s)=s/(lambda+s), with children iid pi_t and
independent degree mu_t. The new reference mu_t need not have mean
above lambda; pi_t is not asserted to be its canonical fixed law.
The original mu, lambda, speed v and canonical law stay fixed.

Put c=lambda-1>0, w_t=E_t(c+X)^(-1), h_t=w_t^(-1)-c>0,
u_t=E_t X>=h_t. Conditional separate concavity of
H_k=(sum Wi^(-1)-(k-1)c)^(-1), Wi=1/(c+Xi), gives

    E_t H_k<=w_t/[k-(k-1)c*w_t].

For k=1 this is equality. Every integrand is bounded by1/c, so the
infinite degree sum can be taken without a second offspring moment.
The decreasing test 1/(c+x) in (1) and the exact root transform imply

    lambda*w_t<=1+E_(mu_t) E_t H_nu
       <=1+w_t E_(mu_t)[1/(nu-(nu-1)c*w_t)].       (2)

Substituting w_t=1/(c+h_t) and rearranging yields the full-law constraint

    E_(mu_t)[(nu-1)/(c+nu*h_t)]<=1.                (3)

This retains the entire actual tilted degree distribution, not only
its support or mean. The same inequality applies to the original
canonical law at t=0 by its finite-mean root recursion, independently
of whether original higher degree moments exist.

## A variance-adapted lower bound, no fixed-point substitution

At t>0 write n=E_(mu_t) nu>1, V=Var_(mu_t) nu>0,

    K=n+V/(n-1)=E_(mu_t)[nu*(nu-1)]/(n-1).

K is a real moment ratio at this t; it is not an offspring degree and
does not define a reference GW law. Under the degree probability tilt
proportional to (nu-1)mu_t, the mean nu is K. Jensen in (3) gives

    1>=E[(nu-1)/(c+nu*h_t)]
       >=(n-1)/(c+K*h_t).

Therefore, whenever n>lambda,

    u_t>=h_t>=(n-lambda)/K.                       (4)

All expectations are finite at t>0 because phi(t)<1 and
mu_t(k) is proportional to mu(k)*phi(t)^k. No original E nu^2
or E nu^3 is assumed, and no t=0 use of K is needed.
Also K>=2, since nu*(nu-1)>=2*(nu-1) pointwise for integer nu>=1.

## Exact third-degree dispersion retained by the source derivative

Under the size-biased degree tilt proportional to nu*mu_t/n, let
Vstar be Var(nu-1). Define the nonnegative actual excess

    Tdeg=E_(mu_t)[(nu-1)*(nu-K)^2]/n>=0.

The definitions give E nu^2=(K+1)n-K, V=(n-1)(K-n), and direct
expansion yields exactly

    j_t/n=K*(n-1)/n,
    Vstar=K*V/n^2+Tdeg.                          (5)

Thus finite multi-degree mixtures contribute an additional negative
term -u_t^2*Tdeg to half the zero derivative, rather than being collapsed
to a binary law. Tdeg=0 only when the tilted support is contained in
{1,K}; no such equality is assumed. This local inequality/identity is
not a two-point reduction of the original canonical problem.

## General zero-eliminated identity

Use the audited normalized source G=B/(n*u), u=u_t, and put

    R=E_t X^2/u, e=R-u=Var_t X/u>=0,
    a=3+v, beta=(lambda+1)v-c, r=(n-1)/n,
    V_Xstar=Var under X*pi_t/u.

At any source zero G(t)=0 the exact derivative is

    G'/2=-a*(V_Xstar+e^2)/2
          +e*[beta-(a/2+2K*r)*u]
          -(K*u^2+v*lambda^2)*V/n^2-u^2*Tdeg.     (6)

This follows by substituting the zero equation
a*(u+e)+2K*r*u-2beta+2v*(1-lambda^2/n)/u=0
in the independently audited G' formula. Away from a zero the original
half derivative differs from the right side of (6) by e*G/2.
The helpful e^2 and actual Tdeg terms are retained.

The new source-zero proof in general_source_crossing_sqrt_two.md uses
only (4) and the exact zero identity with nonnegative degree variances;
it does not require the additional dispersion formula (5).
