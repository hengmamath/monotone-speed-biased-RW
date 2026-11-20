# An actual exponential tilt dominates its tilted recursive output

3 October 2026. Complete canonical lemma; independently passed the same
sole parent-arranged reviewer. This is a new actual-law constraint for the zero-crossing task,
not a claim that the tilted law is a canonical fixed point.

Fix any original finite-mean leafless offspring law, lambda>1 below its
mean, and its actual terminal-one canonical escape pi. Put

    phi(t)=E exp(-tX), f(z)=E z^nu,
    pi_t(dx)=exp(-tx)*pi(dx)/phi(t),
    mu_t(k)=mu(k)*phi(t)^k/f(phi(t)), t>0.

Children in the one-step output below are iid pi_t and independent of
nu with law mu_t. Let T_t(pi_t) be the law of F(sum children), using
the original F(s)=s/(lambda+s). This is a one-step map at a changing
reference offspring law mu_t, not the actual canonical law of mu_t.
The original mu and its actual speed remain fixed throughout.

## Exact monotone likelihood ratio

Let M be the original root-sum law of S. The canonical identity gives
pi=F_#M. Thus pi_t is the push-forward by F of
exp(-tF(s))*M(ds)/phi(t), whereas T_t(pi_t) is the push-forward of
exp(-ts)*M(ds)/f(phi(t)). The ratio of the former density to the latter is

    f(phi(t))/phi(t) * exp(t*(s-F(s))).              (1)

It increases strictly with s, since 1-F'(s)>=1-1/lambda>0.
The elementary increasing-likelihood covariance inequality therefore gives

    pi_t >=_st T_t(pi_t).                          (2)

No iteration, nonzero fixed-point identification or survival assertion
for mu_t is used. The tilted offspring mean can fall below lambda;
inequality (2) and the following bounded expectations remain valid there.

## Degree-four tilted harmonic bound

For original mu=p delta1+q delta4, let

    q_t=q*phi(t)^3/(p+q*phi(t)^3), n_t=1+3q_t,
    W_t=1/(c+X_t), w_t=E_t W, h_t=1/w_t-c, c=lambda-1.

Since W decreases, (2) and lambda*W(F(s))=1+1/(c+s) give

    (q_t+c)w_t<=1+q_t E_t[1/(c+X1+...+X4)].       (3)

The separate-concavity Jensen bound from the independently audited
degree-four source proof gives the right side at most
1+q_t*w_t/(4-3c*w_t). Multiplying positive denominators yields

    (c*w_t-1)*[3(q_t+c)w_t-4]>=0.

Because c*w_t<1, it follows that

    h_t>=(n_t-lambda)/4, u_t=E_t X>=h_t.           (4)

The final inequality is ordinary Jensen for 1/(c+x). These are bounds
on the actual child tilt, not on an arbitrary fixed point for mu_t.

## Two additional precise constraints for continuation below7/5

Retaining the original harmonic escape h gives

    phi(t)/(c+h_t)=E[exp(-tX)/(c+X)]<=1/(c+h),
    h_t>=phi(t)*(c+h)-c.                          (5)

In particular the audited h>=(m-lambda)/4 makes the right side at least
3(q+c)*phi(t)/4-c. Unlike (4), this retains the original q.

There is also a bounded-test moment constraint useful at a source zero.
Under pi_t write u=E_t X, R=E_t X^2/u, and Vstar for the variance
under X*pi_t/u. Under that size-biased probability law,

    E[1/(c+X)]=h_t/[u(c+h_t)], E[1/X]=1/u,
    Var[1/(c+X)]<=1/[u(c+h_t)]-h_t^2/[u^2(c+h_t)^2].

The bound uses 1/(c+X)^2<=1/[X(c+X)]. Cauchy--Schwarz for covariance
of X and 1/(c+X) then gives

    Vstar>=[h_t*(R-u)-c*(u-h_t)]^2
                         /[u(c+h_t)-h_t^2].       (6)

The numerator's inner term is nonnegative by Jensen under size bias.
All expectations displayed above are finite: X>0 almost surely,
size bias cancels 1/X, and c>0 bounds the other functions. No original
inverse moment or formal tree derivative is required.

For a lower bound H<=h_t, 0<H<=u, (6) implies the convenient version

    Vstar>=[H*(R-u)-c*(u-H)]_+^2/[u(c+H)-H^2].     (7)

Indeed, putting e=R-u, the quotient of [h*(c+e)-cu]^2 by
u(c+h)-h^2 increases wherever its numerator's inner term is positive:
the derivative bracket, after removing its positive factors, is
u*[c*(2(c+e)+u)+h*(e-c)]>0 for 0<h<=u.

(5)--(7) also passed independent audit, but no general zero-sign
conclusion below7/5 is drawn from them. They preserve actual tilt
information lost by using h_t>=(n_t-lambda)/4 alone. A finite-moment
relaxation is not substituted for the canonical law.

Audit range clarification: when choosing
H=max((n_t-lambda)/4,phi(t)*(c+h)-c), H>0 is guaranteed only in
the candidate region n_t>lambda^2, not for every t. As t->infinity
this maximum tends to -c/4. Formula (7) requires a separately stated
0<H<=h_t<=u_t, as already imposed. The reviewer checked monotonicity
using the positive derivative factor
u*[2c(c+e)+c(u-h)+e*h]>0 for0<=h<=u.
