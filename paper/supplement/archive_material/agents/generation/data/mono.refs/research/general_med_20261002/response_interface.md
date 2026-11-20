# General finite-mean response interface above one

Date: 2 October 2026. Status: complete local derivation, self-checked,
and passed one independent local audit arranged by the parent task.
This is an interface
lemma, **not** a proof of the sign of the middle-bias speed derivative.
Original notes are unchanged.

## Setting and external boundary

Fix an offspring law with no leaves, positive mass at one, and finite mean
\(1<m=E\nu<\infty\). Throughout this file \(1<\lambda<m\).
\(X_\lambda\) is the actual escape probability from an artificial parent,
constructed as the limit of depth recursions with terminal value one.
The root of the original walk has the ordinary offspring law and selects
a child uniformly. The artificial-parent modification does not affect
speed in the transient regime.

We use the positivity of this canonical escape and the speed representation
quoted in [the retained primary-source excerpts](../../evidence/imported_speed_formula.md).
These are imported probabilistic facts; their original proofs have not been
re-audited here. The source convention and finite-mean hypotheses were
checked against those excerpts. All functional-analytic steps below are
proved here. In particular, an arbitrary fixed-point law is not substituted
for the canonical law.

The precise imported formula is Aidekon, *Speed of the biased random walk
on a Galton--Watson tree*, Theorem 1.1, arXiv:1111.4313v4, with the
leafless convention made explicit in Song--Wang--Xiang,
arXiv:1610.08151v1, equation (2.1):
\[
 v_\mu(\lambda)=
 \frac{E[(\nu-\lambda)\beta_0/(\lambda-1+\sum_{i=0}^{\nu}\beta_i)]}
      {E[(\nu+\lambda)\beta_0/(\lambda-1+\sum_{i=0}^{\nu}\beta_i)]}.
\]
Here \(\beta_i\) are iid actual parent-avoidance probabilities, independent
of \(\nu\), and the transition convention is parent weight \(\lambda\)
and child weight one. The no-leaf finite-mean setting above, with
\(1<\lambda<m\), lies inside the cited theorem's range. Conditional
exchangeability gives
\(E[\nu\beta_0/(c+\beta_0+S)]=E[S/(c+\beta_0+S)]\).
Substituting \(Y=F_\lambda(S)\), \(S=\lambda Y/(1-Y)\), and symmetrizing
turns the numerator and denominator into \(\lambda N\) and \(\lambda Z\),
respectively, where \(N,Z\) are defined in Corollary 4 below.

Write \(\pi_\lambda=\operatorname{Law}(X_\lambda)\),
\(c=\lambda-1\), \(F_\lambda(s)=s/(\lambda+s)\), and
\(A(x,y)=c+x+y-xy\). All child variables and pair variables below are
independent, and children are independent of \(\nu\).

## Lemma 1: the response operator and its actual convergent inverse

On the Banach space \(\mathcal C=C([0,1];\mathbb R)\), set
\[
 (Lf)(x)=E\left[\nu F_\lambda'(x+S_{\nu-1})
       f(F_\lambda(x+S_{\nu-1}))\right],
 \qquad (Jf)(x)=E\frac{f(Y)}{A(x,Y)^2}.
\]
Let \(r_0=J\mathrm{id}\) and \(q_0=J(y^2)\). Then
\[
 (I-L)r_0=q_0,
 \quad \min r_0>0,\quad \min q_0>0.
 \tag{1}
\]
Consequently the norm
\[
 \|f\|_{r_0}=\sup_{[0,1]}|f|/r_0
\]
is equivalent to the usual sup norm, and
\[
 \|L\|_{r_0}\le\theta:=1-\min_{[0,1]}q_0/r_0<1.
\]
The inverse \(R=(I-L)^{-1}=\sum_{j\ge0}L^j\) converges in operator norm
in this norm and is positive. No offspring moment beyond \(E\nu<\infty\)
is required.

### Proof

\(0\le F_\lambda'\le1/\lambda\), so the integrand is dominated by
\(\nu\|f\|_\infty/\lambda\). Dominated convergence gives \(L f\in\mathcal C\)
and boundedness. Since \(c\le A\le\lambda\),
\(r_0\ge EY/\lambda^2>0\) and \(q_0\ge EY^2/\lambda^2>0\).
The elementary cancellation
\[
 F_\lambda'(s)r_0(F_\lambda(s))
 =\lambda^{-1}E\frac{Y}{(c+s+Y)^2}
\]
and conditional exchangeability give
\[
 Lr_0(x)=\lambda^{-1}E\frac{S_\nu}{(c+x+S_\nu)^2}
         =J[y(1-y)](x).
\]
The last equality uses the canonical recursion
\(Y=F_\lambda(S_\nu)\) in law. Thus (1) follows. Positivity of \(L\)
implies \(|Lf|\le\|f\|_{r_0}Lr_0\), proving the contraction and the
Neumann-series assertions. \(\square\)

## Lemma 2: continuity and local Lipschitz continuity of the canonical law

The canonical laws are continuous in \(W_1\) on \((1,m)\), and are locally
Lipschitz in that metric. Constants may depend on the base bias and law;
no estimate uniform as \(\lambda\downarrow1\) is asserted.

### Proof

For completeness, continuity does not assume differentiability. At a
fixed \(\lambda>1\), let \(\rho\) be a nonzero fixed law, construct
\(r_\rho\) as in Lemma 1, and put \(u_\rho(x)=\int_0^x r_\rho(s)ds\).
If \(\sigma\ge_{\mathrm{st}}\rho\), denominator cancellation shows
\(L_{\lambda,\sigma}r_\rho\le L_{\lambda,\rho}r_\rho\).
For an ordered coupling \(U\le V\), set \(U_t=(1-t)U+tV\),
\(\rho_t=\operatorname{Law}(U_t)\). The derivative of
\[
 E_\sigma u_\rho(X)
 -E_{\nu,\sigma}u_\rho(F_\lambda(S_\nu))
\]
is exactly
\[
 \frac d{dt}\mathcal E_\lambda(\rho_t)
 =E[(V-U)(r_\rho-L_{\lambda,\rho_t}r_\rho)(U_t)]
 \ge\gamma_\rho E[V-U],
\]
where \(\mathcal E_\lambda\) denotes this residual and
\(\gamma_\rho=E_\rho X^2/\lambda^2>0\). Differentiation under the
offspring expectation is justified by \(\nu\|r_\rho\|_\infty/\lambda\).
Two ordered nonzero fixed laws must coincide. Iteration from terminal
value one stochastically dominates every fixed law, so the canonical law
is the unique nonzero fixed law on \([0,1]\).

Same-tree one-sided limits as the bias tends to an interior
\(\lambda\) satisfy the recursion by bounded convergence: \(\nu\) is
finite almost surely. Choose \(\lambda<\Lambda<m\). Both limits dominate
the positive canonical escape at \(\Lambda\), so they are nonzero.
Uniqueness identifies them. Same-tree bounded convergence gives
\(W_1\) continuity.

For local Lipschitz continuity fix the base \(\lambda\), \(r_0\),
\(u(x)=\int_0^x r_0\), and \(\gamma=\min q_0>0\). If \(\rho\to\pi_\lambda\)
in \(W_1\), then
\[
 \|L_{\lambda,\rho}r_0-Lr_0\|_\infty\longrightarrow0.
 \tag{2}
\]
To check the uniformity, truncate \(\nu\) at \(K\); for \(\nu\le K\),
uniform continuity of the fixed function \(r_0\) and product-law
convergence on compact sets apply uniformly in \(x\). The discarded
tail is bounded by \(2\|r_0\|_\infty E[\nu;\nu>K]/\lambda\).
Hence all laws on the ordered interpolation between
\(\pi_\lambda\) and \(\pi_{\lambda+h}\) have
\(r_0-L_{\lambda,\rho}r_0\ge\gamma/2\) for small \(|h|\).

Let \(\mathcal E_\lambda(\rho)=E_\rho u(X)-E_{\nu,\rho}u(F_\lambda(S_\nu))\).
Integration along the ordered interpolation yields
\[
 |\mathcal E_\lambda(\pi_{\lambda+h})|
 \ge (\gamma/2)W_1(\pi_{\lambda+h},\pi_\lambda).
\]
On the actual law the fixed-point relation also gives
\[
 \mathcal E_\lambda(\pi_{\lambda+h})
 =E_{\nu,\pi_{\lambda+h}}
       [u(F_{\lambda+h}(S_\nu))-u(F_\lambda(S_\nu))].
\]
Its absolute value is at most
\(|h|\|r_0\|_\infty/(4\lambda_-)\), where
\(\lambda_-\) is a fixed positive lower bound for nearby biases, because
\(s/(\alpha+s)^2\le1/(4\alpha)\). This proves the assertion. \(\square\)

## Lemma 3: the weak bias derivative, with no infinite-tree differentiation

For every \(f\in C^1([0,1])\),
\[
 \frac{d}{d\lambda}E f(X_\lambda)
   =-E[b(X_\lambda)(R f')(X_\lambda)],
 \qquad b(x)=x(1-x)/\lambda.
 \tag{3}
\]
Here \(f'\) is continuous and bounded on the specified compact interval.
This does not assert the formula for unbounded-derivative tests on
\((0,1)\), for inverse moments, or for pointwise infinite-tree derivatives.

### Proof

Use the actual same-tree ordered coupling \((X,X_h)\) at
\((\lambda,\lambda+h)\). For continuous \(a\) define the positive measure
\[
 \eta_h(a)=E\left[\frac1h\int_{X_h}^{X}a(s)ds\right]
 \quad (h\ne0).
\]
Positivity holds for either sign of \(h\), and
\(\eta_h(1)=W_1(\pi_{\lambda+h},\pi_\lambda)/|h|\) is bounded by Lemma 2.
For a primitive \(u\) of \(a\),
\((Eu(X_h)-Eu(X))/h=-\eta_h(a)\).

In the recursion, first change the parameter while holding the child
law at \(\pi_{\lambda+h}\), then change the child law at the base
parameter. The parameter difference divided by \(h\) converges to
\(-E[b(X)a(X)]\). The bound
\(\|a\|_\infty/(4\lambda_-)\) is independent of \(S_\nu\), so dominated
convergence is legitimate even when \(\nu\) has no second moment.

For the child-law difference set
\(X_s=(1-s)X+sX_h\), \(\rho_s=\operatorname{Law}(X_s)\).
Conditional exchangeability of iid coupled children gives its exact
quotient as
\[
 -\int_0^1 E\left[
  \frac{X-X_h}{h}(L_{\lambda,\rho_s}a)(X_s)\right]ds.
\]
For each fixed continuous \(a\),
\[
 \sup_{0\le s\le1}
 \|L_{\lambda,\rho_s}a-La\|_\infty\longrightarrow0
 \tag{4}
\]
by the same finite-mean truncation argument as (2). Multiplication by
the bounded mass \(\eta_h(1)\) proves that the last display equals
\(-\eta_h(La)+o(1)\). Thus
\[
 \eta_h((I-L)a)=E[ba]+o(1)
 \quad\text{for each fixed }a\in\mathcal C.
 \tag{5}
\]
Now take \(a=Rf'\), which is continuous by the **already proved**
operator-norm Neumann convergence of Lemma 1. Then (5) gives
\(\eta_h(f')\to E[bRf']\), proving (3) for two-sided \(h\).

No dominated convergence for the possibly large random variables
\((X-X_h)/h\) is used. Their bounded expectations suffice because
the error in (4) is uniform in \(x,s\). Long unary pipes and near-zero
escape mass therefore cause no missing uniform-integrability hypothesis.
\(\square\)

### Continuity of this derivative

The derivative in (3) is continuous in the bias. In a neighborhood of
a base \(\lambda\), (1), (2), and parameter continuity give a common
strict contraction for the nearby operators in the base \(r_0\) norm.
For each fixed test, these operators converge strongly (uniformly on
\([0,1]\)), by finite-mean truncation. The uniformly geometric Neumann
tails and convergence of each finite sum show strong convergence of
the resolvents. This is sufficient for continuity of (3); convergence
of the operators in sup operator norm is neither assumed nor needed.

## Corollary 4: the actual speed is C1 above one and has the full response

Set
\[
 t=x+y-xy,\quad N=E[XY/A],\quad Z=E[t/A],\quad v=N/Z,
\]
\[
 \Psi(x)=J[y^2+c((1+v)y-v)](x),
 \qquad C=E[(vt-XY)/A^2].
\]
Then \(v\in C^1((1,m))\) and
\[
 \boxed{\quad v'(\lambda)=-D_\lambda/Z,\qquad
 D_\lambda=2E[bR\Psi]-C.\quad}
 \tag{6}
\]

### Proof

For the base value \(v=v(\lambda)\), freeze \(v\) and consider
\(H_\alpha(x,y)=(xy-vt)/(\alpha-1+t)\).
All first derivatives are bounded and continuous on compact bias
intervals contained in \((1,m)\), uniformly in \((x,y)\in[0,1]^2\).
Its base \(x\)-derivative is \(\Psi(x)\) after averaging over \(y\),
and its explicit bias derivative averages to \(C\).
Apply Lemma 3 to each marginal, or its identical interpolation proof
to this pair kernel. It gives
\[
 \left.\frac d{d\alpha}E H_\alpha(X_\alpha,Y_\alpha)
 \right|_{\alpha=\lambda}=C-2E[bR\Psi].
\]
The left side is \(Z v'(\lambda)\). The same proof applied to the
numerator and denominator separately first establishes differentiability
of their quotient, since \(Z>0\). Strong resolvent continuity and bounded
kernel derivatives give continuity of \(v'\). \(\square\)

For the two marginal differences, tests averaged against the other
marginal may themselves depend on \(h\). Their derivatives converge
uniformly on \([0,1]\) to the base averaged derivatives, since the
pair-kernel derivatives are uniformly continuous on the compact square
and \(\pi_{\lambda+h}\to\pi_\lambda\) in \(W_1\). The resulting error is
bounded by that uniform difference times \(\eta_h(1)\), whose boundedness
was proved before differentiability. Thus this use of Lemma 3 does not
silently require the tests to stay literally fixed.

## What remains

This file settles the regularity interface in the formula for \(D\)
throughout \((1,m)\), under only finite mean. It does not establish
\(D\ge0\) on the general middle interval. The next work is quantitative
control of the complete branch response, with its canonical iid source
retained.

Current continuation, 3 October: the interface and general strict sign
from sqrt2 are independently PASSED. The sole selected remaining route
is I<0 COMPLETE compensation on2/sqrt3<=lambda<sqrt2. New self-checked,
independently PASSED repaired source-curvature identity and an explicit actual chord
counterexample are in negative_i_source_curvature.md and
negative_i_explicit_finite_k.md. The universal curvature-payment SIZE
remains UNPROVED. No interface hypothesis or arbitrary escape law changes.

General H1>0 was mislabeled PASSED in an earlier packet and is NOT an
audited interface dependency. The accepted curvature proof uses direct
negative-I/source-one-crossing C1>0. Specific finiteK endpoint enclosures
have their own certificate. See curvature_dependency_repair.md.
