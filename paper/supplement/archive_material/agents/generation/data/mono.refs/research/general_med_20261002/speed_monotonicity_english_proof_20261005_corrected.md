# Strict decrease of speed for parent-biased walks above one

> Correction, 5 October 2026, to the preserved 4 October assembly.
> The Mellin first factor and the floor used in (15)/(17) are corrected below.
> The same sole parent-arranged reviewer closed the necessary-chain impact
> audit: the previously audited regional polynomial inputs are unchanged.
> This audit did not rerun all large certificates or independently acquire
> the frozen ZIP bytes. Text/diff review passed for the displayed diff
> and accompanying texts. The reviewer did not receive the full preserved base
> or independently reconstruct every byte of this corrected exposition.
> See [the erratum and dependency-impact record](mellin_index_errata_and_dependency_impact_20261005.md).

4 October 2026, assembly revision V2. Modular computation-assisted proof in the original
finite-mean setting. The analytic and regional sign modules have passed
the same sole independent reviewer arranged by the parent task; the last
middle module was independently rerun to completion. The final assembly,
normalizations, endpoint coverage and integrability have also been reviewed
locally. The present English exposition is newly assembled from those
modules. No external peer review or literature-priority claim is made.

The referenced appendices and exact programs are part of this proof.
In particular the regional polynomial signs are not claimed to have short
hand proofs. The final dependency DAG and certificate manifest identify
the required appendices and distinguish imported probability theorems,
hand arguments, generic algebra checks and large exact computations.

## Theorem and conventions

Fix a probability distribution \(\mu\) on the nonnegative integers such
that \(\mu(0)=0\), \(\mu(1)>0\), and
\[
1<m=\sum_{k\ge1}k\mu(k)<\infty.
\]
There is no further offspring moment assumption. Let \(T\) be the ordinary
Galton–Watson tree: its root, as well as every other vertex, has offspring
law \(\mu\). No survival conditioning is needed. At a nonroot vertex with
\(k\) children, the walk moves to its parent with probability
\(\lambda/(\lambda+k)\) and to each child with probability
\(1/(\lambda+k)\). At the ordinary root it chooses a child uniformly.
The distribution \(\mu\) is held fixed when \(\lambda\) varies.

Then the deterministic speed satisfies
\[
v_\mu\in C^1((1,m)),\qquad v_\mu'(\lambda)<0
\quad\text{for every }1<\lambda<m.
\tag{T}
\]
Consequently \(v_\mu(\lambda_1)>v_\mu(\lambda_2)\) whenever
\(1<\lambda_1<\lambda_2<m\). This implies the requested inequality on
\[
1<\lambda_1<\lambda_2<
\min\{m,(3+\sqrt5)/2\}.
\]
Joining across \(\lambda=1\) is a separate question and is not treated here.

### Imported probabilistic facts

Add an artificial parent \(o_*\) to the root and give the root the same
parent weight \(\lambda\) as a nonroot vertex. Set
\[
X=B_\lambda=P_{\lambda,o}^{T_*}(\tau_{o_*}=\infty).
\]
This is always the actual escape on the sampled tree, equivalently the
limit of finite-depth recursions with terminal value one. With
\(F_\lambda(s)=s/(\lambda+s)\), it satisfies
\[
X\overset d=F_\lambda(S),\qquad
S=\sum_{j=1}^{\nu}X_j,
\tag{1}
\]
where \(\nu\sim\mu\) and the \(X_j\) are iid actual subtree escapes,
independent of \(\nu\). No arbitrary distributional fixed point is used.

We import transience and \(0<X<1\) almost surely for \(1<\lambda<m\),
the equality of ordinary-root and artificial-parent speeds, and the speed
representation
\[
v_\mu(\lambda)=
\frac{\mathbb E[(\nu-\lambda)X_0/
(\lambda-1+\sum_{j=0}^{\nu}X_j)]}
{\mathbb E[(\nu+\lambda)X_0/
(\lambda-1+\sum_{j=0}^{\nu}X_j)]}.
\tag{2}
\]
The precise speed source is Aïdékon, *Speed of the biased random walk on
a Galton–Watson tree*, Theorem 1.1, arXiv:1111.4313v4. The explicit
leafless convention and range \(\lambda<m\) are recorded in
Song–Wang–Xiang, *Monotonicity of speed for biased random walk on
Galton–Watson tree*, equation (2.1), arXiv:1610.08151v1.
Their Lemma 2.1 is the precise reference for equality of ordinary-root
and artificial-parent speeds.
Their minimum-offspring-two monotonicity theorem is not used.
Here extinction has probability zero and \(0<\mu(1)<1\), so our
\(\lambda>1\) applications lie in the cited transient speed range.
The retained primary excerpts check the finite-mean hypotheses and
parent-weight convention; the original probabilistic proofs are imported.
See [source boundary](../../evidence/imported_speed_formula.md),
[Aïdékon](https://arxiv.org/abs/1111.4313) and
[Song–Wang–Xiang](https://arxiv.org/abs/1610.08151).

All arguments from this point use (1), the actual canonical coupling,
and (2). Since \(\mu(1)>0\), arbitrarily long finite unary segments have
positive probability; their terminal-one escape tends to zero as their
length grows. Thus the actual escape is nonconstant with essential
infimum zero. Since \(m>1\), genuine branches also have positive probability.

## 1. The actual finite-mean response

Put \(c=\lambda-1\), \(t(x,y)=x+y-xy\), \(A(x,y)=c+t(x,y)\).
Independent pair variables \(X,Y\) always have the actual law at the
same bias. Conditional exchangeability in (2), substitution
\(Y=F_\lambda(S)\), and symmetrization give
\[
N=\mathbb E[XY/A],\qquad Z=\mathbb E[t/A]>0,\qquad v=N/Z.
\tag{3}
\]
On \(C([0,1])\) define
\[
(\mathcal L f)(x)=
\mathbb E[\nu F_\lambda'(x+S_{\nu-1})
f(F_\lambda(x+S_{\nu-1}))],\qquad
(Jf)(x)=\mathbb E[f(Y)/A(x,Y)^2].
\]
Write \(r_{\rm a}=J(y)\), \(q_{\rm a}=J(y^2)\),
\(b_{\rm t}(x)=x(1-x)/\lambda\). The subscript a distinguishes these
anchor functions from the scalar cap ratios used later.

**Response lemma.** The inverse
\(\mathcal R=(I-\mathcal L)^{-1}=\sum_{j\ge0}\mathcal L^j\) is a positive
bounded operator. The actual speed is \(C^1\) on \((1,m)\), and
\[
v'=-D/Z,\qquad
D=2\mathbb E[b_{\rm t}\mathcal R\Psi]-C_{\rm pair},
\tag{4}
\]
where
\[
\Psi=J[y^2+c((1+v)y-v)],\qquad
C_{\rm pair}=\mathbb E[(vt-XY)/A^2].
\]

**Proof.** Denominator cancellation and conditional exchangeability in
(1) give
\[
(I-\mathcal L)r_{\rm a}=q_{\rm a},\qquad
\min r_{\rm a}>0,\quad \min q_{\rm a}>0.
\]
Indeed \(\mathcal L r_{\rm a}=J[y(1-y)]\). Positivity therefore makes
\(\mathcal L\) a strict contraction in
\(\|f\|_{r_{\rm a}}=\sup|f|/r_{\rm a}\), with contraction factor at most
\(1-\min q_{\rm a}/r_{\rm a}<1\). The integrable bound
\(\nu\|f\|_\infty/\lambda\) establishes the operator on continuous tests.

Continuity of the actual law precedes differentiation. Terminal-one
iteration dominates every fixed law. For two ordered nonzero fixed
laws, use the primitive of the smaller law's positive anchor
\(r_{\rm a}\). Along ordered interpolation the fixed-point residual
has derivative at least
\(\gamma\mathbb E[V-U]\), \(\gamma>0\), because the larger-law response
operator applied to this anchor is smaller. Both fixed-point residuals
are zero, so the laws coincide. Same-tree one-sided bias limits satisfy
(1) and dominate a positive canonical escape at a slightly larger bias
below \(m\); they are nonzero. This uniqueness identifies them with the
canonical law, giving \(W_1\) continuity. This argument identifies
canonical limits; it does not replace the escape law by a free fixed law.

For local Lipschitz continuity, fix the base anchor. Uniform convergence
of child-law response on that fixed test follows by truncating
\(\nu\le K\), and then bounding the discarded part by a constant times
\(\mathbb E[\nu;\nu>K]\). The residual coercivity remains at least half
its base value locally. Its parameter perturbation is bounded by
\(|\delta|\|r_{\rm a}\|/(4\lambda_-)\), using
\(s/(\lambda+s)^2\le1/(4\lambda)\). Hence the canonical laws are
locally Lipschitz in \(W_1\).

For the ordered same-tree pair \(X,X_\delta\), the positive measures
\[
\eta_\delta(f)=
\mathbb E\left[\delta^{-1}\int_{X_\delta}^{X}f(s)\,ds\right]
\]
have bounded mass for both signs of \(\delta\). Expand (1) by changing
the bias first and the child law second. Uniform convergence of the
child-law operators on each fixed continuous test, multiplied by this
already bounded mass, gives
\[
\eta_\delta((I-\mathcal L)f)=\mathbb E[b_{\rm t}f]+o(1).
\]
Taking \(f=\mathcal R g'\) proves, for every \(g\in C^1([0,1])\),
\[
\frac{d}{d\lambda}\mathbb E g(X_\lambda)
=-\mathbb E[b_{\rm t}(X_\lambda)(\mathcal R g')(X_\lambda)].
\tag{5}
\]
There is no dominated-convergence assumption on the random pointwise
quotient \((X-X_\delta)/\delta\).

Strong continuity of the operators on fixed tests, together with locally
uniform geometric Neumann tails, gives strong continuity of their
resolvents and of (5). On compact bias intervals inside \((1,m)\),
the pair kernels in (3) have bounded continuous first derivatives.
Apply (5) to both marginals and the explicit bias derivative, freezing
the base \(v\), to the kernel \((xy-vt)/A\). This yields (4), and proves
\(C^1\) regularity. Averaged tests that vary with \(\delta\) have uniformly
convergent derivatives; their error is again multiplied only by the
bounded mass \(\eta_\delta(1)\). Every offspring truncation above uses
finite mean only. Full details are in
[response_interface.md](response_interface.md). \(\square\)

## 2. Canonical moments and the entropy reduction

Set
\[
W=(c+X)^{-1},\quad h=(\mathbb EW)^{-1}-c,\quad d=1-h,\quad
U=X/(c+X),\quad a_s=\mathbb E U^s,\quad u=a_1.
\]
Then \(0<h<1\), \(0<U<1/\lambda\), \(u=h/(c+h)\). Define
\[
\beta_s=\frac{h}{\lambda^s-d},\quad \beta_0=1,\quad
\rho_s=a_s/\beta_s.
\]

**Canonical comparison lemma.** For integers \(s\ge1\),
\[
\rho_0=\rho_1=1,\qquad
\rho_s>\rho_{s+1}>0,\qquad \rho_s\longrightarrow0.
\tag{6}
\]
Moreover \(v<v_\pi<h\), where \(v_\pi\) is the symmetric quotient of
the scalar comparison moments \(\beta_s\), and \(\inf\Psi>0\).

**Proof.** For the actual root sum \(S\), put
\[
H=(c+S)^{-1}=\frac{W_1}{1+W_1T_{\rm sib}}.
\]
The offspring number is not size biased. Its sibling sum is independent
of \(W_1\). Recursion gives \(\lambda W\overset d=1+H\) and
\(\mathbb EH=d\mathbb EW\). The multiplier
\(\mathbb E[(1+aT_{\rm sib})^{-1}]\) decreases in \(a\).
For a bounded increasing test \(f\), chosen-child comparison followed
by decreasing-function covariance under \(W_1\)-size bias gives
\[
\mathbb E[Hf(1-cH)]\ge d\mathbb E[Wf(U)].
\]
For \(f(t)=t^s\), the chosen-child comparison is strict on a genuine
branch. It gives
\[
(\lambda^s-d)a_s-(\lambda^{s+1}-d)a_{s+1}>0.
\]
This is (6). Its limit follows from
\(\lambda^sa_s=\mathbb E(\lambda U)^s\to0\) by bounded convergence.

The pair expansion in (3) gives
\[
N=cT_{\rm act},\quad Z=2Q_{\rm act}-(\lambda+1)T_{\rm act},
\quad
T_{\rm act}=\sum_{s\ge1}\lambda^{s-1}a_s^2,\quad
Q_{\rm act}=\sum_{s\ge1}\lambda^{s-1}a_sa_{s-1}.
\tag{7}
\]
All series converge geometrically at each fixed \(\lambda>1\).
The scalar \(\beta_s\) are moments of \(\lambda^{-L}\) with
\(P(L=j)=h d^{j-1}\). This is an auxiliary moment sequence, not the
canonical law of a substituted Galton–Watson tree. The strict ratios
in (6) and covariance of decreasing sequences give \(v<v_\pi\).
The exact telescoping identity (4) in
[canonical_entropy.md](canonical_entropy.md) gives \(v_\pi<h\).
Finally direct expansion yields
\(\Psi(0)>(h-v)\mathbb EW>0\); the normalized inverse-square tilt
from \(x=0\) to \(x>0\) has increasing density in \(Y\). Its defining
polynomial is increasing. Thus \(\Psi\) is uniformly positive. \(\square\)

Define, for \(x>0\), with \(g(0)=0\),
\[
g(x)=\frac{x(c+x)\log(1+c/x)}{\lambda c\log\lambda}-x/c,
\quad
\alpha=\min\{1,\Psi(0)/q_{\rm a}(0)\},\quad H_*=\Psi-\alpha q_{\rm a}.
\]
The same tilt shows \(H_*\ge0\), and \(\alpha>0\). The unary identity
\(g(F_\lambda(s))=b_{\rm t}(F_\lambda(s))+F_\lambda'(s)g(s)\)
and the entropy defect
\[
\delta_g=F_\lambda'(S)\left[\sum_{j=1}^{\nu}g(X_j)-g(S)\right]\ge0
\]
give the exact identity
\[
D=F_*+2\mathbb E[\delta_g(\mathcal RH_*)(F_\lambda(S))]\ge F_*,
\quad
F_*=2\alpha\mathbb E[b_{\rm t}r_{\rm a}]
-C_{\rm pair}+2\mathbb E[gH_*].
\tag{8}
\]
The child entropy is positive on every genuine branch: for any positive
finite list with sum \(S\),
\[
\sum_jg(x_j)-g(S)=\frac1{\lambda c\log\lambda}
\int_0^c(c-a)\sum_{i<j}
\frac{x_ix_j(2a+x_i+x_j)}
{(a+S)(a+x_i)(a+x_j)}\,da.
\]
Also
\[
0\le\delta_g\le\lambda^{-1}
(\max_{[0,1]}g+1/c)\nu.
\tag{9}
\]
This proves integrability under finite mean, without discarding siblings.

If \(\alpha=1\), then
\[
\lambda(2\mathbb E[b_{\rm t}r_{\rm a}]-C_{\rm pair})
=2\mathbb E[X(1-X)J((1+v)y-v)(X)]
+(1+v)\mathbb E[XY(1-X)(1-Y)/A^2]>0.
\tag{10}
\]
The first term is nonnegative by the normalized tilt; the second is
strictly positive. Hence \(D>0\) for every \(\lambda>1\) in this branch,
including \(\Psi(0)=q_{\rm a}(0)\).

The remaining branch has \(0<\alpha<1\) and exact calibration
\[
A_0=1-(\lambda+1)u+\lambda a_2>0,\qquad
\alpha=\frac{u-(v/c)A_0}{a_2}.
\tag{11}
\]
The strict speed and moment comparisons imply \(\alpha>\lambda^2u\),
so \(u<\lambda^{-2}\), equivalently \(h<1/(\lambda+1)\).
No sign assumption on an additional source curvature is imposed.

## 3. The actual marker and the complete floor

Put \(q=u/(1-u)\), so \(h=cq\), and let
\[
r_i=\beta_{i+1}/\beta_i,\qquad
r_i^-=\beta_i/\beta_{i-1},\qquad
L_i=\frac{cd}{\lambda(\lambda^i-d)}.
\]
Thus \((1+L_i)r_i=1/\lambda\),
\(r_i^-=(1-\lambda L_i)/\lambda\), \(L_{i+1}=r_iL_i\).
The chosen-child indicator comparison gives the actual nonnegative
tail defect
\[
A_{\rm m}(t)=
\mathbb E[(1-\lambda U){\bf1}_{\lambda U>t}]
-d\mathbb E[(1-U){\bf1}_{U>t}]\ge0.
\]
Layer cake and positive summation construct the actual probability
\[
\sigma(dt)=\frac{A_{\rm m}(t)\,dt}{h(1-t)^2},\qquad
\rho_s=\mathbb E_\sigma[t^{s-1}(s-(s-1)t)]\quad(s\ge1).
\tag{12}
\]
It is supported in \((0,1)\), and
\[
\Delta_i:=\rho_i-\rho_{i+1}
=i\mathbb E_\sigma[t^{i-1}(1-t)^2]>0,\quad
e:=\Delta_1,\quad \Delta_i\le ie.
\tag{13}
\]
Thus one actual marker controls every age.

Only the deterministic Mellin transform is differentiated in its age
variable. The inequality \(-\log(1-z)>z+z^2/2\) gives
\[
-\rho'(s)>(1-1/(2s))(\rho_s-\rho_{s+1}),\qquad s\ge1.
\tag{14}
\]
For \(s>1\) the differentiated integrands are bounded. At \(s=1\),
the finite derivative of \(\mathbb E U^s\), followed by Fatou in (12),
first proves the required log integrability of \(\sigma\); dominated
convergence then applies. No inverse escape moment or unweighted
\(\log U\) integrability is assumed.

Here is an explicit definition of the floor being certified. Write
\[
k=\frac{c}{\lambda\log\lambda},\quad
\gamma_{s-1}=k\mathbb E[U^s\log(1/U)]-a_s+a_{s+1},\quad
\delta_s=a_sr_s-a_{s+1}.
\]
The exact relation is
\[
\gamma_{s-1}=a_s(r_s-r_s^-)-\delta_s+\Theta_s,
\qquad \Theta_s=k\beta_s[-\rho'(s)].
\]
With \(R_*=v/c\), set
\[
\mathcal Q(U)=-R_*+[1+(\lambda+1)R_*]U
-(\alpha+\lambda R_*)U^2,\quad t_n=\mathbb E[U^n\mathcal Q(U)].
\]
Calibration gives \(t_0=0\). The concave quadratic has a single upward
zero in \((0,1/\lambda)\); therefore \(t_n>0\) for \(n\ge1\).
Write \(\varepsilon_s=a_s-\lambda a_{s+1}\), with \(s=n+1\).
The exact Mellin expression for \(F_*\) is
\[
F_*=\sum_{n\ge0}(n+1)\lambda^n
\left[\frac{(a_{n+1}-\lambda a_{n+2})J_n}{\lambda c}
+2\gamma_nt_n\right],
\]
\[
J_n=-2va_n+[c(1+2\alpha)+(3\lambda+1)v]a_{n+1}
-[c(\lambda+2\alpha)+\lambda(\lambda+1)v]a_{n+2}.
\]
Define the floor from the corrected Mellin series above. For \(s\ge1\), set
\[
\bar\gamma_{s-1}=a_s(r_s-r_s^-)-\delta_s
+\frac{k(1-1/(2s))\delta_s}{r_s},
\]
\[
F_{\rm floor}(R_*)=\sum_{s\ge1}s\lambda^{s-1}
\left[\frac{\varepsilon_sJ_{s-1}}{\lambda c}
+2\bar\gamma_{s-1}t_{s-1}\right].
\]
All moments are from the same actual canonical law. The \(s=1\) surplus
vanishes because \(t_0=0\). Equation (14) therefore gives
\[
F_*-F_{\rm floor}(R_*)
=2\sum_{s\ge2}s\lambda^{s-1}
\left[\Theta_s-\frac{k(1-1/(2s))\delta_s}{r_s}\right]t_{s-1}>0.
\tag{15}
\]
All shifts and expansions have polynomial times geometric dominators at
fixed \(\lambda>1\). Below, an unqualified \(F_{\rm floor}\) means
\(F_{\rm floor}(R_*)\). Consequently proving the whole floor nonnegative
is sufficient, and all regional proofs below actually obtain strict
positivity. Equations (12)–(15) are proved in
[scaled_r0_adjacent_defect_payment.md](scaled_r0_adjacent_defect_payment.md)
and the Mellin appendix.

### A calibrated full budget, with all endpoints

Define scalar comparison quantities from the complete series
\[
w_i=\lambda^{i-1}\beta_i^2,\quad
T_p=\sum_{i\ge1}w_i,\quad Z_p=2q-(\lambda+1)T_p,\quad
R_p=T_p/Z_p,\quad \kappa_p=(1-u)T_p/u^2.
\]
They satisfy \(R_*<R_p<q\), \(\kappa_p>1\), \(Z_p>0\).
Let
\[
\alpha_p=\frac{u-R_p[1-(\lambda+1)u+\lambda\beta_2]}{\beta_2},
\quad \mathcal C=\alpha_p+\lambda R_p.
\]
Actual hard calibration gives
\[
\lambda^2u<\alpha_p<\alpha(R_p)<\alpha<1,\qquad
\alpha(R_p)-\alpha_p=\mathcal C e/(1-e).
\tag{16}
\]
The scalar moments remain comparison weights throughout.
Indeed
\(\alpha_p=[\lambda^2q+(1-\theta)d(\lambda+1)]/(q+1)\),
\(\theta=R_p/q<1\), gives \(\alpha_p>\lambda^2u\).
Writing \(\alpha_p\) in terms of \(\kappa_p\), the strict
\(\alpha_p<1\) is equivalent to
\(\kappa_p>2\lambda/(\lambda+1)>1\). Thus this use of
\(\kappa_p>1\) has no extra hypothesis.

For a scalar \(R\) put
\[
W_i^0=ci/\lambda-1+2iL_i,\quad
W_i^p=cW_i^0+4iL_i
-2r_i[iL_i+(i+1)\lambda L_{i+1}],\quad
W_i^s(R)=W_i^0+RW_i^p,
\]
\[
V_i=\sum_{j>i}w_jW_j^s(R_p)>0,\quad
\tau_i=1-\mathcal C r_i+(\lambda+1)R_p-R_p/r_i^-.
\]
Scalar calibration gives \(\tau_1=0\), \(\tau_i>0\) for \(i\ge2\).
Define
\[
\frac{B_i}{w_i}=
\frac{2i(\alpha_p+cR_p)}{\lambda}
+2iR_pr_iL_i+2(i+1)R_p\lambda r_i^2L_i
+k(2i-1)\tau_i,\quad S_i=B_i-2V_i,
\]
\[
W_i^{\rm Y}=\frac{k w_i(2i-1)R_p}{r_i^-}\ (i\ge2),\quad W_1^{\rm Y}=0,
\quad
J_i=V_i+k w_i(2i-1)\mathcal C r_i
-\frac{W_i^{\rm Y}+W_{i+1}^{\rm Y}}2\quad(i\ge2).
\]
Finally \(F_\pi=u^2W_1^s(R_p)-2R_puL_1+V_1\).

Define the exact calibrated speed-credit coefficient by
\[
C_{\rm cal}:=
C_{\rm head}\,\frac{u^2(\kappa_p-1)(2-e)}{Z_p}>0,
\]
where the explicit positive fixed-moment coefficient is
\[
C_{\rm head}=2A_0u[-k\log(a_2/u)-1+a_2/u]
+(u-\lambda a_2)
[2-(3\lambda+1)u+\lambda(\lambda+1)a_2]/\lambda>0.
\]
This definition uses the actual second moment and the same actual defect
\(e\). The regional \(C_0\) introduced in (19) is a lower bound for
the normalized coefficient, not its definition.

Applying the audited fixed-moment affine comparison and exact root
correction to this same corrected floor gives
\[
F_{\rm floor}(R_*)>
F_\pi+\sum_{i\ge1}\Delta_i\rho_iS_i
+e^2\left[V_1+\frac{2u^2\mathcal C}{\lambda(1-e)}
-\frac{W_2^{\rm Y}}2\right]
+\sum_{i\ge2}\Delta_i^2J_i+C_{\rm cal}e,
\tag{17}
\]
The first sum in (17) starts at \(i=1\); its first factor is
\(\rho_1=1\). The retained calibrated speed credit must not be dropped
when certifying the full regional budget.

For completeness, the affine comparison holds actual moments fixed.
It uses the explicit extension
\[
\widetilde F(w)=2\alpha(w)\mathbb E[b_{\rm t}r_{\rm a}]
-\mathbb E[b_{\rm t}J P_c(w)]
+2\mathbb E[g(JP_v(w)-\alpha(w)q_{\rm a})],
\]
where \(\alpha(w)=(u-wA_0/c)/a_2\),
\(P_c(w;y)=(1-y)[2w-(1+w)y]\),
\(P_v(w;y)=y^2+c[(1+w)y-w]\).
For \(R\in[R_*,R_p]\), define \(F_{\rm floor}(R)\) by the same
corrected series with \(w=cR\), \(\alpha(w)=(u-RA_0)/a_2\), and the
corresponding calibrated \(J_n\) and \(t_n\). The actual law,
\(\varepsilon_s\), and \(\bar\gamma_{s-1}\) remain fixed. Equations
(215), (218), and (219) of calibrated_cumulative_head_payment.md
apply to this floor and give (17) at \(R=R_*\).
At the actual speed, \(\widetilde F(v)=F_*\).
It is not an off-speed use of the actual velocity response identity:
the exact correction is
\(C_{\rm pair}(w)-\mathbb E[b_{\rm t}JP_c(w)]=(wZ-N)/\lambda\).
Its full negative slope is
\[
-\widetilde F'(w)=
2c\mathbb E[gJ(1-y)]
+\mathbb E[b_{\rm t}J((1-y)(2-y))]
+2A_0\Gamma/(ca_2),\quad
\Gamma=\mathbb E[\delta_g r_{\rm a}(F_\lambda(S))]>0.
\]
The derivative of its calibrated \(t_n(R)\) equals
\(-a_2\operatorname{Cov}_{\pi_2}(U^n,
(1-U)(1-\lambda U)/U^2)>0\), with density
\(d\pi_2=U^2d\pi/a_2\). The inverse-looking factor is integrable under
this density, with expectation \(A_0/a_2\).
Writing \(R=w/c\), the full negative floor slope has the exact scales
\[
-\partial_R F_{\rm floor}(R)
>c[-\partial_w\widetilde F(w)]>C_{\rm head}>0.
\]
The complete moment-profile gain is
\[
R_p-R_*>u^2(\kappa_p-1)e(2-e)/Z_p.
\]
This comes from the exact complete loss balances
\(R_p-R_*=2q\sum_i\Delta_iY_i/(Z_pZ)\), with the all-age bound
\(Y_i>u(\kappa_p-1)\beta_i(\rho_i+\rho_{i+1})\).
The positive profile sum
\(\sum_i\beta_i(\rho_i^2-\rho_{i+1}^2)\) is at least its first term
\(ue(2-e)\); also \(Z<2q\).
At \(R_p\), expansion gives the exact sum of
\(\Delta_i\rho_iS_i\), the positive squares \(V_i\Delta_i^2\),
the same-defect calibration terms, and adjacent negative products.
Young's inequality charges every adjacent product through the displayed
\(J_i\) and \(W_2^{\rm Y}/2\). The exact first correction has
\(2u^2\mathcal C/[\lambda(1-e)]\); its \(k\) terms cancel. These steps
prove (17), including its strict comparison and every endpoint.
See [calibrated_cumulative_head_payment.md](calibrated_cumulative_head_payment.md),
equations (214)–(219), and its independent receipt.
The prior slope proof is equations (121)–(123) of
joint_SIZE_speed_deficit_correction.md. The complete loss identities
and coercivity are (182)–(185) of marker_root_and_whole_signed_payment.md
and (200b) of actual_defect_paid_subdomain.md. The scalar tail positivity
used above is (189) of marker_cumulative_two_capacity_payment.md and
(206a) of actual_square_shape_high_age_payment.md. Their scoped manual
arguments and receipts are included in the manifest; their unrelated
historical candidate SIZE claims and diagnostics are not dependencies.

The actual defect satisfies
\[
0<e<E_{\rm hard}:=\frac{1-\alpha_p}{1+\lambda R_p}
<E_{\rm var}:=\frac{d}{(q+1)^2}.
\]
The audited hard-gap estimate is
\[
q^2E_{\rm hard}\le
\frac{[1-(\lambda+1)h]u^2}{1+cu}.
\]
Since \(d^2-[1-(\lambda+1)h]=h^2+ch>0\), it implies
\[
s:=\sqrt e<d/(q+1).
\tag{18}
\]
The strict hard/variance comparison also follows by direct calibrated
algebra. These statements hold for all actual hard \(q>0\).

At \(E_{\rm var}\), the positive componentwise lower bound for
\(C_{\rm head}\) uses
\[
A_E=E_{\rm var},\quad D_E=(2-h)E_{\rm var},\quad
\epsilon=u-\lambda\beta_2>0,
\]
\[
\phi_{\rm lo}=
\frac{d-c^2(q+2+c)/6}{(q+2+c)(2q+3+c)},\quad
C_{E,\rm lo}=E_{\rm var}
[2u\phi_{\rm lo}+(2-h)\epsilon/\lambda].
\]
In the low/middle boxes below, \(\phi_{\rm lo}>0\). Thus (17) may use
\[
\frac{C_{\rm cal}}{u^2}\ge C_0[\theta(2-h)-1],\quad
\theta=R_p/q,\quad C_0=\frac{C_{E,\rm lo}(2-E_{\rm var})}{2q}>0,
\tag{19}
\]
because \((\kappa_p-1)/Z_p=[\theta(2-h)-1]/(2q)>0\).

## 4. Full tails and the middle-q mechanism

This section records the key new mechanism of the final gap proof.
Assume actual hard calibration and \(3\le q\le10\). Then \(h<1/2\) and
\(c=h/q\le1/6\). Set
\[
a=c/\log\lambda,\quad
a_L=1+c/2-c^2/12\le a\le a_U=a_L+c^3/24.
\]
For each age put \(b=\lambda L_i\), \(r=1/(\lambda+b)\),
\(r^-=(1-b)/\lambda\), \(A_1=c+br\), \(B_1^{\rm geom}=br\).
Here \(B_1^{\rm geom}\) is only a geometric-moment variable, not the
head \(B_1\) in (17). The six geometric moments give
\[
P_2=A_1(A_1+B_1^{\rm geom}),\quad
P_3=A_1(A_1^2+4A_1B_1^{\rm geom}+(B_1^{\rm geom})^2),
\]
\[
P_4=A_1(A_1^3+11B_1^{\rm geom}A_1^2
+11(B_1^{\rm geom})^2A_1+(B_1^{\rm geom})^3),
\]
\[
P_5=A_1(A_1^4+26B_1^{\rm geom}A_1^3
+66(B_1^{\rm geom})^2A_1^2
+26(B_1^{\rm geom})^3A_1+(B_1^{\rm geom})^4).
\]
Define normalized complete-tail bounds
\[
\mathrm{TL}(a)=\frac r{b+c}
[a+A_1/2+P_2/(12a)-P_4/(720a^3)],\quad
\mathrm{TU}(a)=\frac r{b+c}[a+A_1/2+P_2/(12a)],
\]
\[
\mathrm{PU}(a)=\frac r{\lambda(b+c)}
[(i+1)(aA_1+P_2/2+P_3/(12a))
+a^2-P_2/12+P_4/(240a^2)],
\]
\[
\mathrm{PL}(a)=\frac r{\lambda(b+c)}
[(i+1)(aA_1+P_2/2+P_3/(12a)-P_5/(720a^3))
+a^2-P_2/12].
\]
These follow from the complete Lambert sums and the global inequalities
\[
1+t/2+t^2/12-t^4/720\le\frac t{1-e^{-t}}
\le1+t/2+t^2/12,
\]
\[
1-t^2/12\le\frac{t^2}{2(\cosh t-1)}
\le1-t^2/12+t^4/240.
\]
Their remainders hold for every positive \(t\), hence every Lambert index.
The scalar derivative is taken at fixed \(h,d\), and all sums converge.
No inequality is formally differentiated to obtain a derivative bound.

The exact boundary correction is
\[
\mathcal B_i=2R_p(i+1)\lambda r^2+2R_pr/(b+c).
\]
The full upper and lower for \(V_i/w_i\) are
\[
\mathrm{VU}=-(1+cR_p)\mathrm{TL}(a_U)
+[1+(\lambda+1)R_p]\mathrm{PU}(a_U)-\mathcal B_i,
\]
\[
\mathrm{VL}=-(1+cR_p)\mathrm{TU}(a_U)
+[1+(\lambda+1)R_p]\mathrm{PL}(a_L)-\mathcal B_i.
\tag{20}
\]
The replacements are justified by direct monotonicity of these
normalized scalar functions. Their proof uses \(c\le1/6,b\le1,a\ge1\),
not \(q\le3\); this validates the extension of the earlier tail lemma.

At age one, let
\(T_{\rm lo}=u^2[1+\mathrm{TL}_1(a_L)]\),
\(T_{\rm up}=u^2[1+\mathrm{TU}_1(a_U)]\).
They bound the COMPLETE \(T_p\). A 160-coefficient exact certificate on
\(x=1/q\in[1/10,1/3],h\in[0,1/2]\) proves
\[
T_{\rm up}<
\frac{2q^2(6q+5)}
{6(q+1)+(\lambda+1)q(6q+5)}.
\tag{21}
\]
Thus both tight calibration denominators are positive,
\[
\theta_{\rm lo/up}=
\frac{T_{\rm lo/up}}{q[2q-(\lambda+1)T_{\rm lo/up}]},
\quad 0<\theta<1-\frac1{6(q+1)}.
\]

### All-age price bounds

Bernoulli gives \(b\le d/(q+i)\). Since
\(\lambda^i=d(1+c/b)\), the bounds \(\log\lambda\le c\) and
\(\log z\ge2(z-1)/(z+1)\) give
\[
i\ge i_{\rm lo}=
\frac{2(d-qb)}{2b+c(d-qb)}.
\]
The lower head \(B_i(k=a_L/\lambda)/w_i-2\mathrm{VU}\) and lower
quadratic
\[
\mathrm{VL}+\frac{a_L}{\lambda}(2i-1)\alpha_p r
-\frac{a_U R_p}{2\lambda}
[(2i-1)(1/r^--\lambda r)+2\lambda r]
\]
are affine in \(i\). Their slopes are nonnegative. Substitute
\(b=dv/(q+2)\), \(0\le v\le1\), and the two affine calibration
endpoints \(0,1-1/[6(q+1)]\). Exact whole-box polynomial certificates
then prove for EVERY integer \(i\ge2\)
\[
[-S_i]_+\le4w_i\beta_i^4,\qquad
[-J_i]_+\le8w_i\beta_i^4.
\tag{22}
\]
Four head checks have 735,1207,7719,9768 nonzero Bernstein entries;
the last has 25 degree-ten Sturm exceptions. After removing endpoint
factors, their endpoint values are positive and full Sturm variations
are five at both ends. Four quadratic checks have 1980,2975,8288,10745
nonzero positive entries. The maximum comparison degree is 34.
Every original denominator is reconstructed symbolically with its sign,
including the negative cubic factor \(-12a_L\) in the quadratic family.
Cleared polynomial boundaries are not singular actual substitutions.
The portable packet and program provide the exact expressions.

### Whole-marker damping with the same actual defect

Let \(M_i=w_i\beta_i^4\). This is a positive Hausdorff sequence with
measure
\[
\eta=\frac{h^6}{\lambda}\sum_{n\ge0}\binom{n+5}{5}d^n
\delta_{\lambda^{-(n+5)}},
\quad\eta([0,1])=1/\lambda,\quad
\operatorname{supp}\eta\subset[0,\lambda^{-5}].
\]
The function \(Y/(1-t+t\sqrt Y)^2\) is concave on \([0,1]\) for
\(0\le t<1\). Apply Tonelli and Jensen to the WHOLE sequence (13),
then subtract the equal first terms \(eM_1\), to obtain
\[
\sum_{i\ge2}\Delta_iM_i
\le e\sum_{i\ge2}i(1-s)^{i-1}M_i.
\]
Since \(\rho_i\le1-e\) for \(i\ge2\), (22) bounds the complete negative
head. Put \(t_*=qs/(1-s)<qd/(q+h)\le1\), using (18). Bernoulli and
the exact identity
\[
(1-t)+t/(1+y)-1/(1+ty)
=t(1-t)y^2/[(1+y)(1+ty)]\ge0
\]
yield
\[
\frac{\text{whole negative head}}{u^2}
\le4s^2(1+s)[(1-t_*)K_6+t_*K_7].
\tag{23}
\]
Here \(K_6=\sum_{i\ge2}iM_i/u^2\),
\(K_7=\sum_{i\ge2}iM_iq/[(q+i)u^2]\).
The entire negative square price is at most \(8e^2K_J\), where
\(K_J=\sum_{i\ge2}i^2M_i/u^2\). The same actual \(e=s^2\) remains
in every head, root, square and speed term.

For explicit whole-tail upper bounds, put \(A=q+2\),
\[
U_j=\frac{A^{1-j}}{j-1}+\frac1{2A^j}+\frac{j}{12A^{j+1}},
\quad L_j=U_j-\frac{j(j+1)(j+2)}{720A^{j+3}}.
\]
The global Laplace remainder bounds the full sum
\(\sum_{i\ge2}(q+i)^{-j}\) between \(L_j,U_j\).
The decreasing function \(z/(z-d)^6\), with
\(z=\lambda^i\ge1+ci\), gives
\(M_i\le q^6(1+ci)/[\lambda(q+i)^6]\). It follows that
\[
K_6\le\frac{q^4(q+1)^2}{\lambda}
[U_5-qL_6+c(U_4-2qL_5+q^2U_6)],
\]
\[
K_7\le\frac{q^5(q+1)^2}{\lambda}
[U_6-qL_7+c(U_5-2qL_6+q^2U_7)],
\]
\[
K_J\le\frac{q^4(q+1)^2}{\lambda}
[U_4-2qL_5+q^2U_6
+c(U_3-3qL_4+3q^2U_5-q^3L_6)].
\tag{24}
\]
Every negative coefficient uses a lower tail bound and every positive
coefficient an upper bound. All tails are included.

### Complete middle budget

In (17), the exact first head is \(eS_1\), since \(\rho_1=1\).
Combining it with \(F_\pi\) and the positive root square gives
\((1-e)^2V_1+u^2W_1^s-2R_puL_1+eB_1\).
Moreover
\[
2R_puL_1/u^2=2\theta d/\lambda,\qquad
W_2^{\rm Y}/(2u^2)=3k\lambda R_pr_1/2
\le3a_UR_pr_1/2.
\]
The numerator of \(\phi_{\rm lo}\) in (19) is positive, since
\(c^2(q+2+c)\le31/216\) and \(d\ge1/2\) in the present box.
Using (19), (20), (23), (24), the COMPLETE lower bound is
\[
\begin{split}
\mathscr L={}&(1-e)^2\mathrm{VL}_1+W_1^s-2\theta d/\lambda
+eB_1/u^2\\
&+e^2[2\mathcal C/(\lambda(1-e))-3a_UR_pr_1/2]\\
&-4s^2(1+s)[(1-t_*)K_6+t_*K_7]-8e^2K_J\\
&+C_0[\theta(2-h)-1]e .
\end{split}
\tag{25}
\]
Here (24)'s explicit uppers are used for the \(K\)'s, and
\(F_{\rm floor}>u^2\mathscr L\). All quantities use the same calibration.
This expression is affine in \(\theta\). Substitute
\(s=dz/(q+1)\), \(0\le z\le1\), and both tight \(\theta\) endpoints.
The exact denominators are
\[
34560\,\mathcal B\,\widehat Z_{\rm lo},\qquad
-11520\,\mathcal B(12a_L)^3\widehat Z_{\rm up},
\]
where
\[
\mathcal B=\lambda(q+1)^6(q+2)^{10}(q+2+c)^3(2q+3+c)
(c^3-2c^2+12c+24)[(q+1)^2-d^2z^2]>0,
\]
\[
\widehat Z_{\rm lo/up}=
D_{T,\rm lo/up}[2-(\lambda+1)T_{\rm lo/up}/q]>0,
\]
\[
D_{T,\rm lo}=720\lambda(q+1)^2(q+2+c)^5a_L^3,\quad
D_{T,\rm up}=12\lambda(q+1)^2(q+2+c)^3a_U.
\]
These are symbolic identities in the program, not sampled signs.
Reverse the upper numerator sign. Substitute \(q=1/x,c=hx\) and
multiply the numerators by the positive powers \(x^{28},x^{26}\).
Their degrees in \(x,h,z\) are \((49,28,6),(49,30,6)\).
On the SINGLE box
\([1/10,1/3]\times[0,1/2]\times[0,1]\), all 10150 and 10850 exact
tensor Bernstein coefficients are strictly positive.
Thus both endpoints of (25), and its entire actual calibration interval,
are positive. This proves \(F_{\rm floor}>0\) for every actual hard
\(3\le q\le10\). All of this module, including its original root and
whole-tail reconstruction, has independent PASS:
[final receipt](audit_receipt_mid_q_full_same_e_20261004.md),
[portable proof and code](audit_packet_mid_q_full_same_e_20261004.md).

## 5. Other audited regions and exhaustive assembly

The following scoped propositions are the remaining regional appendices
of this modular proof. Their stated scopes, complete tails and original
speed interfaces were independently audited; their certificates are
listed in the manifest. Historical open labels in older files are
superseded by the dated receipts.

**Small escape proposition.** If \(\lambda\le6/5\) and \(u\le1/30\),
then, in the actual hard branch,
\[
F_*\ge(\alpha+9/1630)\Gamma_{\rm cap}+u^3/500>0.
\]
The proof combines an exact full-root own-speed diagonal telescoper with
a relative whole-tail budget paid by the same canonical defect.
Six rational prefix/tail comparisons prove the scalar boundary margin
\(>1/500\), and \(\alpha>3/10\) pays the entire remaining error.
It has no condition \(u=O(c)\).
See [complete proof](actual_defect_relative_finite_lift.md) and
[receipt](audit_receipt_actual_defect_relative_20261004.md).

**Low-q proposition.** For actual hard \(1/29\le q\le3\) and
\(1<\lambda<2/\sqrt3\), \(F_{\rm floor}>0\).
The complete tail bundle (20) yields all-age \(J_i>0\) and
\([-S_i]_+\le(3/2)w_i\beta_i^2\).
Whole-marker Hausdorff Jensen, equal first-term subtraction and the
root/source merge give the same-e full budget with the square and
calibrated speed credits retained. Both tight-calibration endpoints
are certified on one \(q,c,z\) macrobox:
1723 positive Bernstein groups and 15 degree-seven Sturm exceptions,
positive endpoints and equal variations four. The generic geometric
moments, denominators and entire tail are part of the exact program.
See [proof packet](audit_packet_low_q_full_coupled_20261004.md) and
[receipt](audit_receipt_low_q_full_coupled_20261004.md).

**High-q proposition.** For every actual hard \(q\ge10\) at low bias,
\(F_{\rm floor}>0\). Its exhaustive subcover is:

| Region | Complete budget margin | Audited proof and receipt |
|---|---|---|
| q>=21 | >1/5000 | middle_q_coupled_comparison.md; audit_receipt_middle_q_20261004.md |
| q>=10,h>=1/4 | >1/100 | hard_d_coupled_comparison.md; audit_receipt_hard_d_coupled_20261004.md |
| 10<=q<=21,0<h<=1/4 | >1/40 | finite_h_quarter_coupled_comparison.md; audit_receipt_finite_h_quarter_20261004.md |

These use global Lambert bounds, a whole-age head envelope with its
complete BV summation error and complete Faulhaber quadratic charge.
The last region has 48 whole-box head certificates, with 636112 positive
nonzero coefficients, and no unpaid age tail. The full source/root and
speed terms are included. The finite-quarter budget also uses the
audited degree-five one-interval budget in
critical_boundary_coupled_comparison.md, not just its boundary strip.

**High-bias proposition.** Under the original setting,
\[
v_\mu'(\lambda)<0\quad(2/\sqrt3\le\lambda<m).
\]
This is the corrected independent-PASS theorem
[general_two_over_sqrt3_verified_20261004.md](general_two_over_sqrt3_verified_20261004.md).
Its complete proof includes assigned fixed-law algebra, actual Gram
constraints, the corrected 9600-coefficient root certificate for
\(u\le1/2\), the 5076-coefficient root/second-age certificate for
\(u>1/2\), and the previously audited kernel glue for
\(\lambda\ge707/500\). The extra-u AN/38998 proof is withdrawn and is
not a dependency. The exact left endpoint is included.
See [receipt](audit_receipt_general_two_over_sqrt3_20261004.md).

To conclude, fix \(1<\lambda<m\). The high-bias proposition handles
\(\lambda\ge2/\sqrt3\). Otherwise (10) handles raw
\(\Psi(0)/q_{\rm a}(0)\ge1\), including equality. Positivity of \(\Psi\)
excludes a zero or negative raw calibration. In the remaining hard
case, \(q>0\). If \(q\le1/29\), then \(u\le1/30\) and
\(\lambda<2/\sqrt3<6/5\), so the small-escape proposition applies.
If \(1/29\le q\le3\), the low-q proposition applies. If \(3\le q\le10\),
Section 4 applies. If \(q\ge10\), the high-q proposition applies.
There are no gaps at \(q=1/29,3,10,21\), at \(h=1/4\), or at
\(\lambda=2/\sqrt3\).

Each remaining hard region gives
\(D\ge F_*>F_{\rm floor}>0\), or directly \(D\ge F_*>0\) in the
small-escape region. Equations (4) and \(Z>0\) prove (T).
For any \(1<\lambda_1<\lambda_2<m\), the compact interval lies inside
the proven \(C^1\) range. The mean value theorem gives
\(v_\mu(\lambda_1)>v_\mu(\lambda_2)\). No endpoint derivative or
continuity at one or at \(m\) is used. \(\square\)

## 6. Verification boundary

The deterministic polynomial checks use exact rational arithmetic.
After affine rescaling to a unit box, a polynomial's tensor Bernstein
coefficients give a convex combination with nonnegative weights summing
to one. Positive coefficients prove positivity on the entire closed
box. A small number of univariate groups instead use their complete
exact Sturm sequences: positive endpoints and no roots prove positivity.
This is different from numerical evidence or evaluating a parameter
grid. Generic denominator identities and original-expression
normalizations are checked before the regional signs are applied.

The proof uses no second offspring moment, inverse escape moment,
unproved uniform integrability, actual infinite-tree derivative,
offspring two-point reduction, or free escape fixed point. Withdrawn
calibration proofs, general H(1)>0, the failed universal low-bias
Condition F, zero-J beyond its audited low-q scope, and numerical
diagnostics are excluded. The exact integrability inventory and all
endpoint checks are in [final_dependency_dag_20261004.md](final_dependency_dag_20261004.md).

Reproducibility entry: final_certificate_runner_20261004.py and its
manifest. Running programs alone checks their finite algebraic claims;
the hand proofs justifying complete tails, signs of substitutions,
canonical provenance and finite-mean response remain indispensable.
The external probability theorems remain explicitly cited inputs.
