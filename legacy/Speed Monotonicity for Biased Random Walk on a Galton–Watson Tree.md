# Speed Monotonicity for Biased Random Walk on a Galton–Watson Tree

## 1. The general problem

Let $T$ be a supercritical Galton–Watson tree with offspring distribution $\nu$, with

$$
m:=\mathbb E[\nu]>1.
$$

Assume throughout that there are no leaves,

$$
\mathbb P(\nu=0)=0.
$$

For $\lambda\ge 0$, consider the $\lambda$-biased random walk $X=(X_n)$ on $T$. If the current vertex $x$ has $k$ children, then

$$
P(X_{n+1}=\overleftarrow x\mid X_n=x)
=
\frac{\lambda}{\lambda+k},
$$

while each child is chosen with probability

$$
\frac{1}{\lambda+k}.
$$

Thus larger $\lambda$ corresponds to a stronger bias toward the root.

For $0\le \lambda<m$, the walk is transient and has a deterministic positive speed

$$
v(\lambda)
:=
\lim_{n\to\infty}\frac{|X_n|}{n}>0.
$$

Lyons, Pemantle and Peres asked whether

$$
\boxed{
\lambda\longmapsto v(\lambda)
\text{ is nonincreasing on }[0,m).
}
$$

This is the **Lyons–Pemantle–Peres speed monotonicity problem**.

For a deterministic $d$-ary tree,

$$
v(\lambda)=\frac{d-\lambda}{d+\lambda},
$$

so the statement is immediate. For general deterministic or random trees, however, speed monotonicity can fail. Thus, if the conjecture is true for Galton–Watson trees, it must use the particular independence structure of the Galton–Watson environment.

---

## 2. Why the problem is difficult

Let

$$
\beta=\beta_\lambda(T)
$$

denote the probability, starting from the root, of never hitting its parent.

If the root has $\nu$ children and the corresponding descendant subtrees have escape probabilities $\beta_1,\dots,\beta_\nu$, then

$$
\boxed{
\beta
\overset d=
\frac{\sum_{i=1}^{\nu}\beta_i}
{\lambda+\sum_{i=1}^{\nu}\beta_i}.
}
\tag{2.1}
$$

Here the $\beta_i$ are i.i.d. copies of $\beta$, independent of $\nu$.

Thus the relevant conductance or escape-probability random variable itself changes nonlinearly with $\lambda$.

The difficulty is that the speed is not simply the expectation of the local radial drift

$$
\frac{\nu-\lambda}{\nu+\lambda}.
$$

The environment seen from the particle is biased relative to the original Galton–Watson law, and this invariant distribution also depends on $\lambda$.

Aïdékon obtained an explicit representation of $v(\lambda)$ in terms of the escape probabilities. This representation is the main starting point for analytic approaches to the monotonicity problem.

---

## 3. Previously known progress

Write

$$
m_1:=\min\{k\ge1:\mathbb P(\nu=k)>0\}.
$$

The main known monotonicity results can be summarized as follows.

- Ben Arous–Fribergh–Sidoravicius proved monotonicity in a small-bias regime.

- Aïdékon subsequently obtained a universal monotonicity range up to

  $$
  \lambda\le\frac12.
  $$

- Song–Wang–Xiang proved, assuming $m_1\ge2$, that the speed is strictly decreasing for

  $$
  0\le\lambda
  \le
  \frac{m_1}{1+\sqrt{1-1/m_1}}.
  $$

There are also strong regularity results for $v(\lambda)$. In particular, under suitable moment assumptions the speed is differentiable, and in fact analytic, throughout the ballistic regime.

However, these regularity results do not determine the sign of

$$
v'(\lambda).
$$

The global conjecture

$$
v'(\lambda)<0,
\qquad 0<\lambda<m,
$$

remains open in general.

---

## 4. The first genuinely random test case: $\nu\in\{2,3\}$

Consider the offspring distribution

$$
\mathbb P(\nu=2)
=
\mathbb P(\nu=3)
=
\frac12.
$$

Then

$$
m=\frac52,
\qquad
m_1=2.
$$

The Song–Wang–Xiang theorem gives monotonicity only up to

$$
\lambda
\le
\frac{2}{1+\sqrt{1/2}}
=
1.171572\ldots.
$$

A recent computer-assisted argument pushes the verified interval for this special case to

$$
0\le\lambda\le1.755.
$$

The full conjectured interval is

$$
0\le\lambda<\frac52.
$$

The obstruction in the previous analytic/computer-assisted approaches comes from estimates of the form

$$
-\partial_\lambda\beta
\lesssim
\frac{\beta}{2-\lambda},
$$

which naturally deteriorate as $\lambda\uparrow2$.

The main observation below is that one can instead reorganize the argument so that the relevant RDE comparison is controlled by the **maximal** offspring number $3$, producing a factor $3-\lambda$ rather than $2-\lambda$.

---

>[!warning]
>The full-range argument below was derived in our discussion and has not yet been independently verified or checked against the literature. It should therefore be regarded as a **provisional proof** rather than an established theorem.

>[!thm] Provisional theorem
>Suppose
>$$
>\mathbb P(\nu=2)=\mathbb P(\nu=3)=\frac12.
>$$
>Then
>$$
>\boxed{
>v'(\lambda)<0,
>\qquad
>0<\lambda<\frac52.
>}
>$$

The important feature of the argument is that it does not try to sharpen the existing upper bounds on $-\partial_\lambda\beta$. Instead, it changes the direction in which the RDE is used.

---

## 5. Symmetrization of Aïdékon's speed formula

Let

$$
c:=\lambda-1.
$$

Let $\beta_0,\beta_1,\dots$ be independent copies of $\beta$, and let

$$
S:=\sum_{i=1}^{\nu}\beta_i.
$$

Aïdékon's formula can be written as

$$
v(\lambda)
=
\frac{
\mathbb E\left[
\dfrac{(\nu-\lambda)\beta_0}
{c+\beta_0+S}
\right]
}{
\mathbb E\left[
\dfrac{(\nu+\lambda)\beta_0}
{c+\beta_0+S}
\right]
}.
\tag{5.1}
$$

Conditioning on $\nu$ and using exchangeability,

$$
\mathbb E\left[
\frac{\nu\beta_0}{c+\beta_0+S}
\right]
=
\mathbb E\left[
\frac{S}{c+\beta_0+S}
\right].
\tag{5.2}
$$

Now define

$$
X:=\beta_0,
\qquad
Y:=\frac{S}{\lambda+S}.
$$

By the RDE, $X$ and $Y$ are independent copies of $\beta$.

Since

$$
S=\frac{\lambda Y}{1-Y},
$$

we have

$$
c+X+S
=
\frac{c+X+Y-XY}{1-Y}.
$$

Substituting into the numerator of (5.1) and using the symmetry of $(X,Y)$ gives

$$
\lambda
\mathbb E\left[
\frac{XY}{c+X+Y-XY}
\right].
$$

Similarly, the denominator becomes

$$
\lambda
\mathbb E\left[
\frac{X+Y-XY}{c+X+Y-XY}
\right].
$$

Hence

$$
\boxed{
v(\lambda)
=
\frac{
\mathbb E\left[
\dfrac{XY}
{\lambda-1+X+Y-XY}
\right]
}{
\mathbb E\left[
\dfrac{X+Y-XY}
{\lambda-1+X+Y-XY}
\right]
}.
}
\tag{5.3}
$$

This is the first structural simplification: the offspring variable $\nu$ has disappeared explicitly from the speed formula. Its effect is encoded entirely in the law of $\beta$.

For a probability law $\pi$, define

$$
\mathcal V_\lambda(\pi)
:=
\frac{
\mathbb E_\pi\left[
\dfrac{XY}
{\lambda-1+X+Y-XY}
\right]
}{
\mathbb E_\pi\left[
\dfrac{X+Y-XY}
{\lambda-1+X+Y-XY}
\right]
},
\tag{5.4}
$$

where $X,Y$ are independent with law $\pi$.

Then

$$
v(\lambda)
=
\mathcal V_\lambda(\operatorname{Law}(\beta_\lambda)).
$$

---

## 6. A pathwise scaling comparison from the RDE

For the $\{2,3\}$ offspring law,

$$
0\le\beta_\lambda\le1-\frac{\lambda}{3}.
$$

The following comparison is the key point.

>[!lem] Scaling comparison
>Let
>$$
>0<\lambda_1<\lambda_2<3.
>$$
>On the same realization of a tree whose offspring numbers are at most $3$,
>$$
>\boxed{
>\beta_{\lambda_2}
>\le
>\frac{3-\lambda_2}{3-\lambda_1}
>\beta_{\lambda_1}.
>}
>\tag{6.1}
>$$

Set

$$
r:=\frac{3-\lambda_2}{3-\lambda_1}.
$$

Suppose at some stage of the finite-depth recursion that the values corresponding to $\lambda_2$ are at most $r$ times those corresponding to $\lambda_1$.

If the sum of the $\lambda_1$-values of the children is $S$, then

$$
S\le3\left(1-\frac{\lambda_1}{3}\right)
=
3-\lambda_1.
$$

Therefore,

$$
\frac{rS}{\lambda_2+rS}
\le
r\frac{S}{\lambda_1+S}
$$

is equivalent to

$$
\lambda_2-\lambda_1
\ge
(1-r)S.
$$

But

$$
1-r
=
\frac{\lambda_2-\lambda_1}{3-\lambda_1},
$$

and $S\le3-\lambda_1$, so the inequality follows.

Passing to the infinite-depth limit gives (6.1).

Infinitesimally, (6.1) corresponds formally to

$$
-\partial_\lambda\beta_\lambda
\ge
\frac{\beta_\lambda}{3-\lambda}.
\tag{6.2}
$$

The important point is the appearance of

$$
3-\lambda,
$$

rather than $2-\lambda$.

Thus nothing singular happens at $\lambda=2$.

---

## 7. Monotonicity of the speed functional in the escape law

The next ingredient is a stochastic monotonicity property of $\mathcal V_\lambda$.

>[!lem] Monotonicity of the symmetric speed functional
>Fix
>$$
>1\le\lambda<\frac52.
>$$
>For probability distributions in the range produced by the $\{2,3\}$ RDE,
>$$
>\boxed{
>\pi_1\le_{\mathrm{st}}\pi_2
>\quad\Longrightarrow\quad
>\mathcal V_\lambda(\pi_1)
>\le
>\mathcal V_\lambda(\pi_2).
>}
>\tag{7.1}
>$$

To see the relevant first variation, write

$$
t=x+y-xy,
\qquad
A=\lambda-1+t.
$$

If

$$
V=\mathcal V_\lambda(\pi),
$$

then

$$
\frac{\partial}{\partial x}
\left(
\frac{xy-Vt}{A}
\right)
=
\frac{K_V(y)}{A^2},
\tag{7.2}
$$

where

$$
K_V(y)
=
y^2+(\lambda-1)y
-(\lambda-1)V(1-y).
\tag{7.3}
$$

Hence, under a monotone interpolation $X_s$ of probability laws,

$$
\frac{d}{ds}
\mathcal V_\lambda(\operatorname{Law}(X_s))
=
\frac{2}{Z_s}
\mathbb E\left[
\dot X_s
\frac{K_{V_s}(Y_s)}
{
\bigl(
\lambda-1+X_s+Y_s-X_sY_s
\bigr)^2
}
\right],
\tag{7.4}
$$

where $Y_s$ is an independent copy of $X_s$ and $Z_s>0$.

Thus it is enough to prove that

$$
\mathbb E\left[
\frac{K_V(Y)}
{
\bigl(
\lambda-1+x+(1-x)Y
\bigr)^2
}
\right]
\ge0
\tag{7.5}
$$

for every admissible $x$.

### The range $1\le\lambda\le3/2$

Let

$$
a_\lambda:=1-\frac{\lambda}{2},
\qquad
b_\lambda:=1-\frac{\lambda}{3}.
$$

Since

$$
\frac{xy}{x+y-xy}
\le
\frac{b_\lambda}{2-b_\lambda},
$$

the speed satisfies

$$
V\le\frac{b_\lambda}{2-b_\lambda}.
$$

The kernel $K_V(y)$ is increasing in $y$, so

$$
K_V(y)\ge K_V(a_\lambda).
$$

A direct calculation gives

$$
K_V(a_\lambda)
\ge
\frac{
\lambda(\lambda^2-9\lambda+12)
}{
4(\lambda+3)
}.
$$

This is strictly positive on $[1,3/2]$.

Hence the kernel is pointwise nonnegative in this range.

### The range $3/2\le\lambda<5/2$

Here pointwise positivity is no longer needed.

Let

$$
\mu:=\mathbb E[Y].
$$

Writing

$$
N:=
\mathbb E\left[
\frac{XY}{A}
\right],
\qquad
W:=
\mathbb E\left[
\frac{X}{A}
\right],
$$

we have

$$
V=\frac{N}{2W-N}.
$$

For fixed $X=x$, the function

$$
y\longmapsto
\frac{1}{\lambda-1+x+(1-x)y}
$$

is decreasing. Hence

$$
N\le\mu W,
$$

which implies

$$
\boxed{
V\le\frac{\mu}{2-\mu}.
}
\tag{7.6}
$$

Define

$$
J(x)
:=
\frac{
\mathbb E\left[
\dfrac{Y(Y+\lambda-1)}
{
(\lambda-1+x+(1-x)Y)^2
}
\right]
}{
(\lambda-1)
\mathbb E\left[
\dfrac{1-Y}
{
(\lambda-1+x+(1-x)Y)^2
}
\right]
}.
\tag{7.7}
$$

The desired inequality (7.5) is equivalent to

$$
J(x)\ge V.
$$

The reweighting density appearing in $J(x)$ has a monotone likelihood-ratio relation to the one at $x=0$, which gives

$$
J(x)\ge J(0).
$$

Moreover,

$$
J(0)
\ge
\frac{
(\lambda-1)\mu
}{
(\lambda-1+b_\lambda)(1-\mu)
}.
$$

For $\lambda\ge3/2$,

$$
\lambda-1\ge b_\lambda,
$$

and therefore

$$
J(0)
\ge
\frac{\mu}{2-\mu}
\ge V.
$$

This proves the stochastic monotonicity (7.1).

---

## 8. Replace the true change of the RDE by deterministic scaling

Fix

$$
1\le\lambda<\frac52
$$

and let $h>0$ be small.

By the pathwise comparison,

$$
\beta_{\lambda+h}
\le
\left(
1-\frac{h}{3-\lambda}
\right)\beta_\lambda.
\tag{8.1}
$$

Combining this with the stochastic monotonicity of $\mathcal V_{\lambda+h}$ gives

$$
v(\lambda+h)
\le
\mathcal V_{\lambda+h}
\left(
\operatorname{Law}
\left[
\left(
1-\frac{h}{3-\lambda}
\right)\beta_\lambda
\right]
\right).
\tag{8.2}
$$

Define the right-hand side by $G(h)$. Then

$$
G(0)=v(\lambda),
$$

and therefore

$$
v'(\lambda)\le G'(0).
\tag{8.3}
$$

The advantage is that one no longer differentiates the RDE fixed point $\beta_\lambda$ itself. One only differentiates an explicit deterministic scaling of a fixed random variable.

---

## 9. Derivative under deterministic scaling

Let $X,Y$ be independent copies of $\beta_\lambda$, and define

$$
t:=X+Y-XY,
$$

$$
g:=\frac{XY}{t},
$$

and

$$
w:=\frac{t}{\lambda-1+t}.
$$

Introduce the probability measure

$$
dQ
=
\frac{w}{\mathbb Ew}\,dP.
$$

Then

$$
v(\lambda)=E_Q[g].
\tag{9.1}
$$

Set

$$
k:=\frac{1}{3-\lambda}.
$$

Under the deterministic deformation

$$
X_h=(1-kh)X,
\qquad
Y_h=(1-kh)Y,
$$

together with $\lambda\mapsto\lambda+h$, direct differentiation gives

$$
\left.
\frac{d}{dh}g_h
\right|_{h=0}
=
-k g(1+g),
\tag{9.2}
$$

and

$$
\left.
\frac{d}{dh}\log w_h
\right|_{h=0}
=
-H_\lambda(X,Y),
\tag{9.3}
$$

where

$$
H_\lambda(x,y)
=
\frac{
1+\dfrac{\lambda-1}{3-\lambda}
\bigl(1-g(x,y)\bigr)
}{
\lambda-1+x+y-xy
}.
\tag{9.4}
$$

Consequently,

$$
\boxed{
G'(0)
=
-\frac{1}{3-\lambda}
E_Q[g(1+g)]
-
\operatorname{Cov}_Q(g,H_\lambda).
}
\tag{9.5}
$$

Thus the problem has been reduced to controlling one explicit covariance.

---

## 10. Bounding the covariance by the oscillation of $H_\lambda$

The function $g(x,y)$ is increasing in both coordinates, while $H_\lambda(x,y)$ is decreasing in both coordinates.

Let

$$
a_\lambda
=
\left(
1-\frac{\lambda}{2}
\right)_+,
\qquad
b_\lambda
=
1-\frac{\lambda}{3}.
$$

Then

$$
H_\lambda(b_\lambda,b_\lambda)
\le
H_\lambda(X,Y)
\le
H_\lambda(a_\lambda,a_\lambda).
$$

Since $g\ge0$,

$$
-\operatorname{Cov}_Q(g,H_\lambda)
\le
v(\lambda)
\left[
H_\lambda(a_\lambda,a_\lambda)
-
H_\lambda(b_\lambda,b_\lambda)
\right].
$$

Also,

$$
E_Q[g(1+g)]
\ge E_Q[g]
=
v(\lambda).
$$

Hence

$$
G'(0)
\le
-M(\lambda)v(\lambda),
\tag{10.1}
$$

where

$$
M(\lambda)
=
\frac{1}{3-\lambda}
-
H_\lambda(a_\lambda,a_\lambda)
+
H_\lambda(b_\lambda,b_\lambda).
\tag{10.2}
$$

Thus it remains only to prove

$$
M(\lambda)>0.
$$

At this point the probabilistic problem has been reduced to an explicit deterministic rational inequality.

---

## 11. Positivity of the deterministic remainder

For any $z$,

$$
H_\lambda(z,z)
=
\frac{
1+
\dfrac{
2(\lambda-1)(1-z)
}{
(3-\lambda)(2-z)
}
}{
\lambda-1+2z-z^2
}.
\tag{11.1}
$$

### Case 1: $1\le\lambda\le2$

Here

$$
a_\lambda=1-\frac{\lambda}{2},
\qquad
b_\lambda=1-\frac{\lambda}{3}.
$$

A direct computation gives

$$
H_\lambda(a_\lambda,a_\lambda)
=
\frac{
4(\lambda^2-\lambda+6)
}{
\lambda(4-\lambda)(3-\lambda)(\lambda+2)
},
$$

and

$$
H_\lambda(b_\lambda,b_\lambda)
=
\frac{
9(\lambda^2-2\lambda+9)
}{
\lambda(9-\lambda)(3-\lambda)(\lambda+3)
}.
$$

Therefore

$$
M(\lambda)
=
\frac{
P(\lambda)
}{
(9-\lambda)(4-\lambda)(3-\lambda)(\lambda+2)(\lambda+3)
},
\tag{11.2}
$$

where

$$
P(\lambda)
=
\lambda^4
-13\lambda^3
-15\lambda^2
-3\lambda
+198.
$$

On $[1,2]$,

$$
P'(\lambda)
=
4\lambda^3
-39\lambda^2
-30\lambda
-3
<0.
$$

Moreover,

$$
P(2)=44>0.
$$

Hence

$$
M(\lambda)>0,
\qquad
1\le\lambda\le2.
$$

### Case 2: $2\le\lambda<5/2$

Here

$$
a_\lambda=0.
$$

One obtains

$$
M(\lambda)
=
\frac{
18\lambda(\lambda-1)^2
-
(9-\lambda^2)^2
}{
\lambda(9-\lambda)(3-\lambda)(\lambda-1)(\lambda+3)
}.
\tag{11.3}
$$

The denominator is positive.

For the numerator,

$$
18\lambda(\lambda-1)^2
$$

is increasing on $[2,5/2]$, while

$$
(9-\lambda^2)^2
$$

is decreasing there.

At $\lambda=2$,

$$
18\cdot2\cdot1^2-(9-4)^2
=
36-25
=
11>0.
$$

Therefore

$$
M(\lambda)>0,
\qquad
2\le\lambda<\frac52.
$$

Combining with (10.1),

$$
G'(0)<0.
$$

Hence

$$
\boxed{
v'(\lambda)<0,
\qquad
1\le\lambda<\frac52.
}
$$

---

## 12. The remaining interval $0<\lambda<1$

For small bias one can use a simpler direct RDE differentiation.

Let $\beta_n$ denote a finite-depth approximation to the escape probability and put

$$
D_n:=-\beta_n'(\lambda).
$$

One proves inductively that

$$
0\le D_n
\le
\frac{\beta_n}{2-\lambda}.
\tag{12.1}
$$

Indeed, if

$$
S=\sum_i\beta_i,
\qquad
T=\sum_iD_i,
$$

then

$$
\frac{D}{\beta}
=
\frac{1}{\lambda+S}
+
\frac{\lambda}{\lambda+S}
\sum_i
\frac{\beta_i}{S}
\frac{D_i}{\beta_i}.
$$

Since there are at least two children,

$$
\lambda+S\ge2,
$$

which yields the inductive estimate (12.1).

Let

$$
S_{r,n}:=\sum_{i=1}^r\beta_{n,i},
\qquad
T_{r,n}:=\sum_{i=1}^rD_{n,i},
$$

and define

$$
F_{r,n}
:=
\mathbb E\left[
\frac{S_{r,n}}
{\lambda-1+S_{r,n}}
\right],
\qquad
r=3,4.
$$

Then

$$
F_{r,n}'
=
-
\mathbb E\left[
\frac{
S_{r,n}
+
(\lambda-1)T_{r,n}
}{
(\lambda-1+S_{r,n})^2
}
\right].
$$

Since $\lambda<1$ and (12.1) holds,

$$
0
\le
-\frac{F_{r,n}'}{F_{r,n}}
\le
\frac23.
$$

Define

$$
\rho_n
=
\frac{3F_{4,n}}{4F_{3,n}},
$$

$$
q_n
=
\frac{\rho_n}{1+\rho_n},
$$

and

$$
R_n=2+q_n.
$$

Then

$$
R_n'\le\frac16.
$$

Passing to the infinite-depth limit gives

$$
R'(\lambda)\le\frac16.
$$

The speed can also be written as

$$
v(\lambda)
=
\frac{R(\lambda)-\lambda}
{R(\lambda)+\lambda},
$$

with

$$
2\le R(\lambda)\le3.
$$

Therefore

$$
v'(\lambda)
=
\frac{
2\bigl(
\lambda R'(\lambda)-R(\lambda)
\bigr)
}{
(R(\lambda)+\lambda)^2
}.
$$

Since

$$
\lambda R'(\lambda)
\le
\frac16
<
2
\le R(\lambda),
$$

we obtain

$$
\boxed{
v'(\lambda)<0,
\qquad
0<\lambda<1.
}
$$

Together with the previous argument, this gives the provisional conclusion

$$
\boxed{
v'(\lambda)<0,
\qquad
0<\lambda<\frac52.
}
$$

---

## 13. Conceptual difference from previous approaches

The previous strategy can be schematically described as

$$
\text{differentiate the escape-probability RDE}
$$

$$
\Downarrow
$$

$$
\text{upper-bound }-\partial_\lambda\beta
$$

$$
\Downarrow
$$

$$
\frac{1}{2-\lambda},
$$

which degenerates as $\lambda\uparrow2$.

The new strategy is instead

$$
\text{symmetrize the speed formula}
$$

$$
\Downarrow
$$

$$
\text{prove stochastic monotonicity of the speed functional}
$$

$$
\Downarrow
$$

$$
\text{lower-bound the decay of the escape probability}
$$

$$
\Downarrow
$$

$$
\beta_{\lambda+h}
\le
\left(
1-\frac{h}{3-\lambda}
\right)\beta_\lambda
$$

$$
\Downarrow
$$

$$
\text{reduce the derivative to a deterministic rational inequality}.
$$

The change from $2-\lambda$ to $3-\lambda$ is not a constant improvement. It comes from reversing the role played by the RDE sensitivity estimate:

- the old approach controls how **large** the variation of $\beta_\lambda$ can be, hence sees the minimal offspring number;

- the new approach controls how **small** the decay of $\beta_\lambda$ can be, hence sees the maximal offspring number.

This is what allows the proof to pass through $\lambda=2$ and reach the critical value

$$
m=\frac52.
$$

---

## 14. Possible implications for the general problem

Suppose more generally that the offspring distribution has bounded support,

$$
m_1\le\nu\le M.
$$

The same pathwise RDE argument gives

$$
\boxed{
\beta_{\lambda_2}
\le
\frac{M-\lambda_2}
{M-\lambda_1}
\beta_{\lambda_1},
\qquad
0<\lambda_1<\lambda_2<M.
}
\tag{14.1}
$$

Thus the maximal-degree scaling comparison is not special to the $\{2,3\}$ model.

The more delicate ingredient is the symmetric representation of the speed and the resulting stochastic monotonicity of its functional.

This suggests that, for the general Lyons–Pemantle–Peres conjecture, the useful structural question may be:

> Can Aïdékon's speed formula be rewritten in a form whose dependence on the escape-probability law is monotone with respect to stochastic order?

If such an order principle can be established for more general offspring distributions, then the RDE comparison based on the maximal offspring number may provide a route to global monotonicity that avoids the usual low-bias barrier.

For unbounded offspring distributions, one would need a substitute for the deterministic upper degree $M$, so an additional idea would be required.

---

## 15. Main takeaways

1. The general conjecture asks whether

   $$
   v'(\lambda)<0,
   \qquad
   0<\lambda<m,
   $$

   for biased random walk on every leafless supercritical Galton–Watson tree.

2. Existing general results prove monotonicity only in restricted low-bias regimes.

3. The model

   $$
   \nu\sim\operatorname{Unif}\{2,3\}
   $$

   has critical bias

   $$
   m=\frac52
   $$

   and is arguably the simplest genuinely random test case.

4. Previous methods encounter a technical barrier near $\lambda=2$ because they use estimates involving

   $$
   \frac{1}{2-\lambda}.
   $$

5. The provisional argument above instead combines

   $$
   \text{symmetrization}
   +
   \text{stochastic order}
   +
   \text{maximal-degree RDE comparison}.
   $$

6. If the argument is correct, it proves

   $$
   \boxed{
   v'(\lambda)<0
   \quad\text{for all}\quad
   0<\lambda<\frac52
   }
   $$

   for $\nu\sim\operatorname{Unif}\{2,3\}$.

---

## References

1. R. Lyons, R. Pemantle and Y. Peres,  
   *Biased random walks on Galton–Watson trees*,  
   Probability Theory and Related Fields **106** (1996), 249–264.

2. R. Lyons, R. Pemantle and Y. Peres,  
   *Unsolved problems concerning random walks on trees*,  
   in *Classical and Modern Branching Processes*, IMA Volumes in Mathematics and its Applications **84** (1997), 223–238.

3. G. Ben Arous, A. Fribergh and V. Sidoravicius,  
   *A proof of the Lyons–Pemantle–Peres monotonicity conjecture for high biases*,  
   Communications on Pure and Applied Mathematics **67** (2014), 519–530.

4. E. Aïdékon,  
   *Speed of the biased random walk on a Galton–Watson tree*,  
   Probability Theory and Related Fields **159** (2014), 597–617.

5. G. Ben Arous, Y. Hu, S. Olla and O. Zeitouni,  
   *Einstein relation for biased random walk on Galton–Watson trees*,  
   Annales de l'Institut Henri Poincaré, Probabilités et Statistiques **49** (2013), 698–721.

6. A. Bowditch and Y. Tokushige,  
   *Differentiability of the speed of biased random walks on Galton–Watson trees*,  
   ALEA **17** (2020), 609–642.

7. A. Bowditch and Y. Tokushige,  
   *The speed of a biased random walk on a Galton–Watson tree is analytic*,  
   Electronic Communications in Probability **25** (2020), Paper 65.

8. H. Song, L. Wang and K. Xiang,  
   *The speed of a biased walk on a Galton–Watson tree without leaves is monotonic for low values of bias*,  
   Journal of Applied Probability **62** (2025), 1044–1052.

9. M. Mandarapu and S. Kunkunuru,  
   *A Computer-Assisted Proof of Speed Monotonicity for the Biased Random Walk on a Galton-Watson Tree Beyond the Known Range*,  
   arXiv:2609.29894 (2026).