# Two actual finite-mean sign regions for the full response

2 October 2026. Status: complete local arguments, passed a third scoped
audit by the same parent-arranged reviewer. These finish transfer steps in
the earlier endpoint candidates. They do not fill the general interior
middle gap and do not address the join from below one.

Use the definitions and independently audited response interface in
`response_interface.md`, and the complete entropy identity and general
Psi positivity in `canonical_entropy.md` (both independently locally audited).

## Proposition 1: a law-dependent strict-decrease interval to the right of one

For every fixed offspring law under the original finite-mean hypotheses
there is an epsilon>0 such that the speed is strictly decreasing on
\((1,1+\epsilon)\subset(1,m)\).

### Proof

Put \(e=E\nu^{-1}<1\), \(b_0=E(\nu+1)^{-1}\). Then
\(2b_0-e=E[(\nu-1)/(\nu(\nu+1))]>0\).
Choose \(1<\Lambda<\min\{m,1/e\}\).
For the depth-n terminal-one recursion the inverse escape \(R_n=1/X_n\)
obeys, by the harmonic-mean inequality,
\[
 R_{n+1}=1+\lambda/(\sum_{i=1}^{\nu}1/R_{n,i})
 \le1+\lambda\nu^{-2}\sum_{i=1}^{\nu}R_{n,i}.
\]
Since children are iid and independent of \(\nu\),
\(ER_{n+1}\le1+\lambda e ER_n\). Iteration from \(R_0=1\)
and monotone convergence give
\[
 E[1/X_\lambda]\le(1-\lambda e)^{-1}
 \quad(1\le\lambda\le\Lambda).
 \tag{1}
\]

The actual same-tree right limit at one dominates \(X_\Lambda>0\),
has a finite inverse first moment by (1), and satisfies the recursion
at one. Ordered uniqueness extends to the comparison of this law with
the canonical law at one: its kernel
\(r_\rho(x)=E[Y/(x+Y-xY)^2]\) is continuous and bounded by
\(E(1/Y)\); its residual is \(J(y^2)\ge EY^2>0\).
The exact ordered interpolation proof in Lemma 2 of the interface
therefore applies unchanged to these two laws. Thus
\(X_\lambda\to X_1\) almost surely as \(\lambda\downarrow1\).
There is no differentiability assumption in this argument.

At one the imported root-degree formula and exchangeability give
\(v(1)=E[(\nu-1)/(\nu+1)]=1-2b_0\).
The assigned logarithmic response has the useful integral form
\[
 g_\lambda(x)=\frac{x(1-x)}{\lambda c\log\lambda}
 \int_0^c\frac{c-s}{(x+s)(1+s)}ds.
\]
Consequently \(0\le g_\lambda(x)\le(1-x)/2\), since
\(\lambda\log\lambda\ge c\), and
\(g_\lambda(x)\to(1-x)/2\) for each \(x>0\).

All pair integrands in \(D_g=2E[g\Psi]-C\) are dominated uniformly
for \(1<\lambda\le\Lambda\) by a constant times
\(1/(X_\Lambda Y_\Lambda)\), using
\(A\ge t(X_\Lambda,Y_\Lambda)\ge\sqrt{X_\Lambda Y_\Lambda}\).
The copies are independent, and (1) makes this majorant integrable.
Thus \(D_g\) has a continuous right extension at one. The speed also
converges to its value at one by bounded convergence of N,Z.

A symmetric expansion at one gives, with \(t=X_1+Y_1-X_1Y_1\),
\[
 D_g(1)=(1+v(1))/2-v(1)E[1/t].
\]
Writing \(a=1/x-1\), \(b=1/y-1\),
\[
 1/t=1+ab/(1+a+b)
 \le\tfrac14(1/x+1/y)+\tfrac12,
\]
because \(4ab\le(a+b)(1+a+b)\). Together with (1), this yields
\[
 D_g(1)\ge\frac{1-v(1)E(1/X_1)}2
 \ge\frac{2b_0-e}{2(1-e)}>0.
 \tag{2}
\]
Hence \(D_g(\lambda)>0\) on some right neighborhood of one.
General canonical Psi positivity and the full entropy identity give
\(D>D_g>0\) there. The audited response interface then gives
\(v'=-D/Z<0\), proving the proposition. Only inverse first moments
were used, and they were proved from the canonical finite-depth
construction; no second offspring moment was assumed. \(\square\)

## Proposition 2: a law-dependent strict-decrease interval below m

For every such fixed offspring law there is eta>0 for which the speed
is strictly decreasing on \((m-\eta,m)\subset(1,m)\).

### Proof

Write \(\mu_\lambda=EX_\lambda\), \(a_\lambda=EX_\lambda^2\).
Same-tree monotonicity gives a limit at m satisfying the recursion at m.
If its mean were positive, then
\[
 EX_*=E[S_*/(m+S_*)]<ES_*/m=EX_*,
\]
where strictness holds on \(S_*>0\); finite mean legitimizes the last
expectation. Thus \(\mu_\lambda\to0\).

Fix \(\sqrt m<\lambda_0<m\). For \(\lambda\ge\lambda_0\), split
offspring at K. On \(\nu\le K\) use \(X^2\le S^2/\lambda_0^2\);
on \(\nu>K\) use \(X^2\le X\le S/\lambda_0\). Conditional iid
expansion gives
\[
 a_\lambda\le\frac m{\lambda_0^2}a_\lambda
 +\frac{Km}{\lambda_0^2}\mu_\lambda^2
 +\frac{E[\nu;\nu>K]}{\lambda_0}\mu_\lambda.
 \tag{3}
\]
Divide by the positive \(\mu_\lambda\), take \(\lambda\uparrow m\)
at fixed K, then let K increase. Since \(m/\lambda_0^2<1\) and the
offspring first-moment tail vanishes,
\(a_\lambda/\mu_\lambda\to0\).

Let \(\kappa=E[X/(c+X)^2]/E[(c+X)^{-2}]\). Near m, c is bounded
away from zero. Uniform Taylor bounds therefore show
\(E[X/(c+X)^2]=\mu_\lambda/c^2+O(a_\lambda)\) and
\(E[(c+X)^{-2}]=c^{-2}+O(\mu_\lambda)\).
Thus \(\kappa/\mu_\lambda\to1\), and \(\mu_\lambda<2\kappa\)
in some left neighborhood of m.

For every positive escape law the elementary decreasing-weight covariance
bound in the speed quotient gives \(v/(1+v)\le\mu_\lambda/2\).
The increasing-density comparison from the inverse-square tilt to
\(A(x,Y)^{-2}\) then yields \(J[(1+v)y-v]>0\) uniformly in x for
each fixed nearby bias. There is no positive lower bound uniform as
\(\lambda\uparrow m\).
Use the exact correction identity from `high_bias.md`, Section 4:
\[
 \lambda(2E[br_0]-C)
 =2E[X(1-X)J((1+v)y-v)]
 +(1+v)E\frac{XY(1-X)(1-Y)}{A^2}>0.
\]
This identity can be checked by symmetrization and \(N-vZ=0\).
Since \(\Psi=q_0+cJ[(1+v)y-v]\), the full response is
\[
 D=2E[br_0]-C+2cE[bR J((1+v)y-v)]>0.
\]
The audited speed derivative proves the proposition. \(\square\)

## Coverage

These are law-dependent neighborhoods and give no explicit positive
distance between them. Their union can leave a substantial middle gap.
Proposition 1 uses a right-hand limit at one only; no monotonicity claim
across one has been made. The whole requested general theorem remains
open in this research record.
