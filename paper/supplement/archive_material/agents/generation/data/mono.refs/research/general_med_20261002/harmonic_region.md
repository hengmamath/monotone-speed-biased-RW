# A short general-law sign region from canonical second moments

2 October 2026. Status: complete proof, passed the scoped independent
local audit recorded in `interface_audit.md`, using the audited
canonical comparisons and response interface. This is a conditional region
of the general middle interval, not a general offspring reduction.

## Proposition

At every \(1<\lambda<m\), let
\(h=(E(c+X_\lambda)^{-1})^{-1}-c\), \(c=\lambda-1\).
If
\[
 \boxed{\quad (\lambda+1)h\ge1,\quad}
\]
then \(D_\lambda>0\), and hence \(v_\mu'(\lambda)<0\).
No upper bound on offspring support or second offspring moment is assumed.

### Proof

Write \(U=X/(c+X)\), \(a_1=EU=h/(c+h)\),
\(a_2=EU^2\). The audited canonical integer-moment constraint gives
\[
 a_2<\beta_2=h/(\lambda^2-1+h).
\]
The inverse-square tilted escape mean is
\[
 \kappa=\frac{E[X/(c+X)^2]}{E[(c+X)^{-2}]}
 =\frac{c(a_1-a_2)}{1-2a_1+a_2}.
\]
At fixed a1 this expression strictly decreases in a2; its derivative is
\(-c(1-a_1)/(1-2a_1+a_2)^2<0\). Substitution of beta2 yields
\[
 \kappa>\frac{\lambda h}{\lambda+1-h}
 \ge\frac h{1+h}>\frac v{1+v}.
 \tag{1}
\]
The middle inequality is exactly \((\lambda+1)h\ge1\), and the final
strict inequality uses the independently audited general comparison v<h.

The normalized A(x,Y)^(-2) tilt has mean at least kappa, uniformly in
x. Thus J[(1+v)y-v] is uniformly positive on [0,1], for this fixed bias.
The r0 correction has both positive margins, by the exact identity used
in `endpoint_signs.md`, Proposition 2. Equivalently
\[
 D=2E[br_0]-C+2cE[bR J((1+v)y-v)]>0.
\]
The audited response interface gives v'=-D/Z<0. The positivity constants
are allowed to depend on the bias. \(\square\)

## Interpretation

This covers h>=1/2 for every bias above one, and also some smaller values
of h. It follows from only the first nontrivial canonical moment
constraint, together with the full pipe comparison; it does not claim
that those same constraints settle the remaining small-h regime.

It is a new explicit general-law sufficient region relative to the local
source map. It reuses existing correction and canonical moment mechanisms;
literature-wide novelty has not been checked.
