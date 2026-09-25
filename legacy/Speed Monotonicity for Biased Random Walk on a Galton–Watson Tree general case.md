# Speed Monotonicity for Biased Random Walk on a Galton–Watson Tree

## General offspring laws with \(m_1\ge 2\): reduction to an RDE inequality and proof of Lemma A

### 1. Setup

Let \(\nu\) be the offspring distribution of a Galton–Watson tree and assume

\[
m_1:=\min\{k:\mathbb P(\nu=k)>0\}\ge 2,
\qquad
m:=\mathbb E\nu>1.
\]

Consider the \(\lambda\)-biased random walk, where at a vertex with \(k\) children the transition probabilities are

\[
P(x\to \overleftarrow x)=\frac{\lambda}{\lambda+k},
\qquad
P(x\to x_i)=\frac1{\lambda+k}.
\]

For \(0<\lambda<m\), let

\[
v(\lambda)
=
\lim_{n\to\infty}\frac{|X_n|}{n}
\]

denote the deterministic speed.

The Lyons--Pemantle--Peres monotonicity conjecture asks whether

\[
v'(\lambda)<0,
\qquad 0<\lambda<m.
\]

The purpose of this note is to reduce the problem, for a completely general offspring law, to inequalities concerning the fixed point of a one-dimensional recursive distributional equation.

---

## 2. Escape probabilities and the recursive distributional equation

Let

\[
\beta=\beta_\lambda
\]

be the quenched probability, starting from a vertex, of never visiting its parent.

If \(\beta_1,\beta_2,\dots\) are the escape probabilities associated with the child subtrees, then

\[
\boxed{
\beta
\stackrel d=
\frac{\sum_{i=1}^{\nu}\beta_i}
{\lambda+\sum_{i=1}^{\nu}\beta_i}.
}
\tag{2.1}
\]

The variables \((\beta_i)\) are iid copies of \(\beta\) and are independent of \(\nu\).

Write

\[
\pi_\lambda:=\operatorname{Law}(\beta_\lambda).
\]

Thus the dependence of the random environment on \(\lambda\) is encoded entirely in the fixed-point law \(\pi_\lambda\).

---

## 3. Eliminating the offspring variable from the speed formula

Aïdékon's formula can be written as

\[
v(\lambda)
=
\frac{
\mathbb E\left[
\dfrac{(\nu-\lambda)\beta_0}
{\lambda-1+\beta_0+\sum_{i=1}^{\nu}\beta_i}
\right]
}{
\mathbb E\left[
\dfrac{(\nu+\lambda)\beta_0}
{\lambda-1+\beta_0+\sum_{i=1}^{\nu}\beta_i}
\right]
},
\tag{3.1}
\]

where \(\beta_0,\beta_1,\dots\) are iid copies of \(\beta\), independent of \(\nu\).

Set

\[
S:=\sum_{i=1}^{\nu}\beta_i.
\]

By exchangeability,

\[
\mathbb E\left[
\frac{\nu\beta_0}
{\lambda-1+\beta_0+S}
\right]
=
\mathbb E\left[
\frac{S}
{\lambda-1+\beta_0+S}
\right].
\tag{3.2}
\]

Now define

\[
Y:=\frac{S}{\lambda+S}.
\]

By the RDE, \(Y\) has the same law as \(\beta\), and \(Y\) is independent of \(\beta_0\).

Let

\[
X:=\beta_0.
\]

Since

\[
S=\frac{\lambda Y}{1-Y},
\]

we have

\[
\lambda-1+X+S
=
\frac{\lambda-1+X+Y-XY}{1-Y}.
\]

After substitution into (3.1), the antisymmetric term \(Y-X\) disappears after expectation, and we obtain the universal representation

\[
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
\right]},
}
\tag{3.3}
\]

where \(X,Y\) are iid with law \(\pi_\lambda\).

This formula no longer contains the offspring variable explicitly.

> [!prop]
> For every offspring law with no leaves, all dependence on the offspring distribution enters the speed only through the fixed-point law \(\pi_\lambda\) of the RDE (2.1).

This suggests defining, for an arbitrary probability measure \(\pi\) on \([0,1]\),

\[
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
\right]},
\tag{3.4}
\]

so that

\[
v(\lambda)=\mathcal V_\lambda(\pi_\lambda).
\tag{3.5}
\]

The monotonicity problem therefore splits naturally into two questions:

1. how the fixed-point law \(\pi_\lambda\) moves as \(\lambda\) increases;
2. how the functional \(\mathcal V_\lambda(\pi)\) responds to stochastic changes of \(\pi\).

The second issue is Lemma A.

---

# 4. Lemma A: monotonicity with respect to the escape-probability law

For the remainder of the proof, assume

\[
\lambda>1,
\qquad
c:=\lambda-1>0.
\]

Let \(\pi=\pi_\lambda\) be the nonzero RDE fixed point.

We prove that the first variation of \(\mathcal V_\lambda\) in every positive stochastic direction is strictly positive at \(\pi\).

Equivalently, \(\mathcal V_\lambda\) is locally strictly increasing with respect to stochastic order near the fixed-point law.

---

## 5. First variation of the speed functional

Write

\[
V:=\mathcal V_\lambda(\pi).
\]

For \(x,y\in[0,1]\), define

\[
A(x,y):=c+x+y-xy.
\]

Consider

\[
\frac{xy-V(x+y-xy)}{A(x,y)}.
\]

Differentiating with respect to \(x\),

\[
\frac{\partial}{\partial x}
\left(
\frac{xy-V(x+y-xy)}{A(x,y)}
\right)
=
\frac{
y^2+cy-cV(1-y)
}{
A(x,y)^2
}.
\tag{5.1}
\]

Therefore define the response kernel

\[
\boxed{
\Psi_\lambda(x)
:=
\mathbb E\left[
\frac{
Y^2+cY-cV(1-Y)
}{
\{c+x+(1-x)Y\}^2
}
\right],
}
\tag{5.2}
\]

where \(Y\sim\pi\).

If

\[
\Psi_\lambda(x)>0
\qquad\text{for every }x\in[0,1],
\tag{5.3}
\]

then every infinitesimal upward perturbation of the escape probabilities increases the speed functional.

The main task is therefore to prove (5.3).

---

# 6. Reduction to a one-dimensional fixed-point inequality

Define

\[
J(x)
:=
\frac{
\displaystyle
\mathbb E\left[
\frac{Y(Y+c)}
{\{c+x+(1-x)Y\}^2}
\right]
}{
\displaystyle
c\,
\mathbb E\left[
\frac{1-Y}
{\{c+x+(1-x)Y\}^2}
\right]
}.
\tag{6.1}
\]

Then

\[
\Psi_\lambda(x)
=
c\,
\mathbb E\left[
\frac{1-Y}
{\{c+x+(1-x)Y\}^2}
\right]
\bigl(J(x)-V\bigr).
\tag{6.2}
\]

Hence it is enough to prove

\[
J(x)>V.
\]

We first compare \(J(x)\) with \(J(0)\).

The function

\[
y\longmapsto
\frac{y(y+c)}{c(1-y)}
\]

is strictly increasing.

The probability measure appearing in \(J(x)\) has density proportional to

\[
\frac{1-y}
{\{c+x+(1-x)y\}^2}.
\]

Relative to the corresponding measure at \(x=0\), its density ratio is proportional to

\[
\left(
\frac{c+y}
{c+x+(1-x)y}
\right)^2.
\]

Moreover,

\[
\frac{d}{dy}
\frac{c+y}
{c+x+(1-x)y}
=
\frac{\lambda x}
{\{c+x+(1-x)y\}^2}
\ge0.
\]

Thus the family of measures is ordered in the monotone likelihood-ratio order, and consequently

\[
J(x)\ge J(0).
\tag{6.3}
\]

Therefore it suffices to prove

\[
\boxed{
J(0)>V.
}
\tag{6.4}
\]

Explicitly,

\[
J(0)
=
\frac{
\displaystyle
\mathbb E\left[\frac{\beta}{c+\beta}\right]
}{
\displaystyle
c\,
\mathbb E\left[
\frac{1-\beta}{(c+\beta)^2}
\right]}.
\]

Hence everything reduces to the following inequality.

> [!lem] Fixed-point inequality
> Let \(\beta\) satisfy the RDE (2.1), with \(\nu\ge1\) almost surely and \(\lambda>1\). Then
> \[
> \boxed{
> \frac{
> \displaystyle
> \mathbb E\left[\frac{\beta}{\lambda-1+\beta}\right]
> }{
> \displaystyle
> (\lambda-1)
> \mathbb E\left[
> \frac{1-\beta}{(\lambda-1+\beta)^2}
> \right]
> }
> >
> V,
> }
> \tag{6.5}
> \]
> where \(V=\mathcal V_\lambda(\pi_\lambda)\).

Remarkably, the proof uses only the no-leaf property \(\nu\ge1\). Thus \(m_1\ge2\) is stronger than what is needed for Lemma A itself.

---

# 7. The natural transformed variable

Introduce

\[
Z:=\frac{\beta}{c+\beta}
=
\frac{\beta}{\lambda-1+\beta}.
\tag{7.1}
\]

Since \(0<\beta<1\),

\[
0<Z<\frac1\lambda.
\]

Write

\[
a_n:=\mathbb E[Z^n],
\qquad n\ge0,
\tag{7.2}
\]

so that

\[
a_0=1,
\qquad
a:=a_1.
\]

Also define

\[
\mathsf S
:=
\sum_{n=0}^{\infty}
\lambda^n a_{n+1}^2,
\tag{7.3}
\]

and

\[
\mathsf T
:=
\sum_{n=0}^{\infty}
\lambda^n a_n a_{n+1}.
\tag{7.4}
\]

The series converge absolutely since \(Z<1/\lambda\).

---

## 8. Rewriting the speed in terms of moments of \(Z\)

The inverse transformation is

\[
\beta=\frac{cZ}{1-Z}.
\]

Let \(Z,W\) be independent copies.

A direct computation gives

\[
\frac{XY}{c+X+Y-XY}
=
\frac{cZW}{1-\lambda ZW},
\tag{8.1}
\]

and

\[
\frac{X+Y-XY}{c+X+Y-XY}
=
\frac{Z+W-(\lambda+1)ZW}
{1-\lambda ZW}.
\tag{8.2}
\]

Expanding

\[
\frac1{1-\lambda ZW}
=
\sum_{n\ge0}\lambda^n(ZW)^n
\]

yields

\[
\boxed{
V
=
\frac{
c\,\mathsf S
}{
2\mathsf T-(\lambda+1)\mathsf S
}.
}
\tag{8.3}
\]

On the other hand,

\[
c\,\frac{1-\beta}{(c+\beta)^2}
=
\frac{(1-Z)(1-\lambda Z)}{c}.
\]

Hence

\[
J(0)
=
\frac{
ca
}{
1-(\lambda+1)a+\lambda a_2
}.
\tag{8.4}
\]

The denominators in (8.3) and (8.4) are positive. Cross multiplication shows that

\[
J(0)>V
\]

is equivalent to

\[
\boxed{
(1+\lambda a_2)\mathsf S
<
2a\mathsf T.
}
\tag{8.5}
\]

Thus Lemma A has been reduced to a pure moment inequality for the transformed fixed-point variable \(Z\).

---

# 9. The key RDE consequence: a reweighted stochastic domination

The essential use of the recursive structure occurs now.

Let

\[
S=\sum_{i=1}^{\nu}\beta_i.
\]

From the RDE,

\[
\beta=\frac{S}{\lambda+S}.
\]

Consequently,

\[
\lambda Z
=
\frac{S}{c+S}.
\tag{9.1}
\]

Because \(\nu\ge1\), write

\[
S=B+H,
\]

where

\[
B=\beta_1,
\qquad
H=\sum_{i=2}^{\nu}\beta_i.
\]

The crucial facts are

\[
B\perp H,
\qquad
H\ge0.
\tag{9.2}
\]

Let

\[
h(s):=\frac{s}{c+s}.
\]

Then

\[
h(B)\stackrel d=Z,
\qquad
h(B+H)\stackrel d=\lambda Z.
\tag{9.3}
\]

We prove the following reweighted stochastic comparison.

> [!lem] Reweighted stochastic domination
> For every bounded increasing function \(f\),
> \[
> \boxed{
> \frac{
> \mathbb E[(1-\lambda Z)f(\lambda Z)]
> }{
> 1-\lambda a
> }
> \ge
> \frac{
> \mathbb E[(1-Z)f(Z)]
> }{
> 1-a
> }.
> }
> \tag{9.4}
> \]

### Proof

Since \(h\) and \(f\) are increasing,

\[
f(h(B+H))\ge f(h(B)).
\]

Weighting by \((c+B+H)^{-1}\),

\[
\frac{
\mathbb E\left[
\dfrac{f(h(B+H))}{c+B+H}
\right]
}{
\mathbb E[(c+B+H)^{-1}]
}
\ge
\frac{
\mathbb E\left[
\dfrac{f(h(B))}{c+B+H}
\right]
}{
\mathbb E[(c+B+H)^{-1}]
}.
\tag{9.5}
\]

We compare the \(B\)-marginal on the right with the measure weighted by \((c+B)^{-1}\).

The density ratio between the two measures is proportional to

\[
r(B)
:=
(c+B)
\mathbb E\left[
\frac1{c+B+H}
\,\middle|\,
B
\right].
\]

Using the independence of \(B\) and \(H\),

\[
r(B)
=
\mathbb E\left[
\frac{c+B}{c+B+H}
\right].
\]

For every fixed \(H\ge0\), the function

\[
B\longmapsto
\frac{c+B}{c+B+H}
\]

is increasing. Hence \(r(B)\) is increasing.

Because \(f(h(B))\) is also increasing, the one-dimensional monotone covariance inequality gives

\[
\frac{
\mathbb E\left[
\dfrac{f(h(B))}{c+B+H}
\right]
}{
\mathbb E[(c+B+H)^{-1}]
}
\ge
\frac{
\mathbb E\left[
\dfrac{f(h(B))}{c+B}
\right]
}{
\mathbb E[(c+B)^{-1}]
}.
\tag{9.6}
\]

Finally,

\[
1-h(s)=\frac{c}{c+s}.
\]

Using (9.3), equations (9.5)--(9.6) become precisely (9.4).

\(\square\)

---

# 10. Consequence: a sharp bound on successive moment ratios

Set

\[
\theta
:=
\frac{1-\lambda a}{1-a}.
\tag{10.1}
\]

Since \(0<a<1/\lambda\),

\[
0<\theta<1.
\]

Apply (9.4) with

\[
f(z)=z^n.
\]

Then

\[
\frac{
\lambda^n(a_n-\lambda a_{n+1})
}{
1-\lambda a
}
\ge
\frac{
a_n-a_{n+1}
}{
1-a
}.
\]

Equivalently,

\[
(\lambda^n-\theta)a_n
\ge
(\lambda^{n+1}-\theta)a_{n+1}.
\]

Therefore

\[
\boxed{
\frac{a_{n+1}}{a_n}
\le
\frac{\lambda^n-\theta}
{\lambda^{n+1}-\theta},
\qquad n\ge0.
}
\tag{10.2}
\]

For \(n=0\), equality holds and gives

\[
a=\frac{1-\theta}{\lambda-\theta}.
\tag{10.3}
\]

This is the decisive structural consequence of the RDE.

---

# 11. The extremal geometric comparison law

Define a geometric random variable \(K\) by

\[
\mathbb P(K=k)
=
(1-\theta)\theta^k,
\qquad
k\ge0,
\]

and let

\[
Z_*:=\lambda^{-(K+1)}.
\tag{11.1}
\]

Its moments are

\[
b_n
:=
\mathbb E[Z_*^n]
=
\frac{1-\theta}
{\lambda^n-\theta},
\qquad
n\ge0.
\tag{11.2}
\]

In particular,

\[
b_0=1,
\qquad
b_1=a.
\]

Moreover,

\[
\frac{b_{n+1}}{b_n}
=
\frac{\lambda^n-\theta}
{\lambda^{n+1}-\theta}.
\]

Hence (10.2) says

\[
\frac{a_{n+1}}{a_n}
\le
\frac{b_{n+1}}{b_n}.
\tag{11.3}
\]

Thus

\[
d_n:=\frac{a_n}{b_n}
\]

is decreasing, with

\[
d_0=d_1=1.
\]

In particular,

\[
a_2\le b_2.
\tag{11.4}
\]

Define

\[
\mathsf S_*
=
\sum_{n\ge0}\lambda^n b_{n+1}^2,
\qquad
\mathsf T_*
=
\sum_{n\ge0}\lambda^n b_nb_{n+1}.
\tag{11.5}
\]

We next compare \(\mathsf S/\mathsf T\) with the geometric reference ratio.

---

## 12. Comparison of the two moment series

Define probability measures on \(\mathbb Z_{\ge0}\) by

\[
P_n
=
\frac{\lambda^n a_na_{n+1}}{\mathsf T},
\]

and

\[
P_n^*
=
\frac{\lambda^n b_nb_{n+1}}{\mathsf T_*}.
\]

Then

\[
\frac{P_n}{P_n^*}
=
\frac{\mathsf T_*}{\mathsf T}
d_nd_{n+1}.
\]

Since \(d_n\) is decreasing, the likelihood ratio \(P_n/P_n^*\) is decreasing. Therefore

\[
P\le_{\mathrm{st}}P^*.
\tag{12.1}
\]

Furthermore,

\[
r_n^*
:=
\frac{b_{n+1}}{b_n}
=
\frac{\lambda^n-\theta}
{\lambda^{n+1}-\theta}
\]

is increasing in \(n\).

Hence

\[
\begin{aligned}
\frac{\mathsf S}{\mathsf T}
&=
\sum_{n\ge0}
P_n\frac{a_{n+1}}{a_n}
\\
&\le
\sum_{n\ge0}P_n r_n^*
\\
&\le
\sum_{n\ge0}P_n^*r_n^*
\\
&=
\frac{\mathsf S_*}{\mathsf T_*}.
\end{aligned}
\tag{12.2}
\]

Combining this with \(a_2\le b_2\),

\[
\boxed{
(1+\lambda a_2)\frac{\mathsf S}{\mathsf T}
\le
(1+\lambda b_2)
\frac{\mathsf S_*}{\mathsf T_*}.
}
\tag{12.3}
\]

Thus the general RDE fixed point has been reduced to an explicit geometric model.

---

# 13. Closing the geometric comparison

Let

\[
q:=1-\theta.
\]

From (11.2),

\[
\mathsf T_*
=
q^2
\sum_{n\ge0}
\frac{\lambda^n}
{(\lambda^n-\theta)(\lambda^{n+1}-\theta)}.
\]

The identity

\[
\frac{\lambda^n}
{(\lambda^n-\theta)(\lambda^{n+1}-\theta)}
=
\frac1{\lambda-1}
\left(
\frac1{\lambda^n-\theta}
-
\frac1{\lambda^{n+1}-\theta}
\right)
\]

gives the telescoping formula

\[
\boxed{
\mathsf T_*
=
\frac{q}{\lambda-1}.
}
\tag{13.1}
\]

Also,

\[
\mathsf S_*
=
q^2
\sum_{n\ge0}
\frac{\lambda^n}
{(\lambda^{n+1}-\theta)^2}.
\tag{13.2}
\]

Since

\[
a=\frac q{\lambda-\theta},
\]

and

\[
1+\lambda b_2
=
\frac{(\lambda+1)(\lambda-\theta)}
{\lambda^2-\theta},
\]

we obtain

\[
\frac{
(1+\lambda b_2)\mathsf S_*
}{
2a\mathsf T_*
}
=
\frac{
(\lambda^2-1)(\lambda-\theta)^2
}{
2(\lambda^2-\theta)
}
\sum_{n\ge0}
\frac{\lambda^n}
{(\lambda^{n+1}-\theta)^2}.
\tag{13.3}
\]

Thus it remains to prove

\[
\sum_{n\ge0}
\frac{\lambda^n}
{(\lambda^{n+1}-\theta)^2}
<
\frac{
2(\lambda^2-\theta)
}{
(\lambda^2-1)(\lambda-\theta)^2
}.
\tag{13.4}
\]

Let

\[
f(t)
=
\frac{\lambda^t}
{(\lambda^{t+1}-\theta)^2}.
\]

The function \(f\) is strictly decreasing. Therefore

\[
\begin{aligned}
\sum_{n\ge0}f(n)
&<
f(0)+\int_0^\infty f(t)\,dt
\\
&=
\frac1{(\lambda-\theta)^2}
+
\frac1{
\lambda\log\lambda\,(\lambda-\theta)
}.
\end{aligned}
\tag{13.5}
\]

Using

\[
\log\lambda>
\frac{2(\lambda-1)}{\lambda+1},
\qquad
\lambda>1,
\tag{13.6}
\]

we obtain

\[
\sum_{n\ge0}f(n)
<
\frac1{(\lambda-\theta)^2}
+
\frac{\lambda+1}
{2\lambda(\lambda-1)(\lambda-\theta)}.
\tag{13.7}
\]

Finally,

\[
\begin{aligned}
&
\frac{
2(\lambda^2-\theta)
}{
(\lambda^2-1)(\lambda-\theta)^2
}
-
\left[
\frac1{(\lambda-\theta)^2}
+
\frac{\lambda+1}
{2\lambda(\lambda-1)(\lambda-\theta)}
\right]
\\
&\qquad
=
\frac{
(\lambda-1)(\lambda+\theta)
}{
2\lambda(\lambda+1)(\lambda-\theta)^2
}
>0.
\end{aligned}
\tag{13.8}
\]

This proves (13.4).

Consequently,

\[
(1+\lambda b_2)\mathsf S_*
<
2a\mathsf T_*.
\]

By (12.3),

\[
(1+\lambda a_2)\mathsf S
<
2a\mathsf T.
\]

Using the equivalence (8.5), we conclude

\[
\boxed{
J(0)>V.
}
\tag{13.9}
\]

This proves the fixed-point inequality (6.5).

---

# 14. Completion of Lemma A

By (6.3),

\[
J(x)\ge J(0)>V
\qquad
\text{for every }x\in[0,1].
\]

Hence, from (6.2),

\[
\boxed{
\Psi_\lambda(x)>0,
\qquad x\in[0,1].
}
\tag{14.1}
\]

In fact, since

\[
c+x+(1-x)Y\le c+1=\lambda,
\]

we obtain the uniform lower bound

\[
\Psi_\lambda(x)
\ge
\frac{
c(1-\mathbb E\beta)
}{
\lambda^2
}
\bigl(J(0)-V\bigr)
>0.
\tag{14.2}
\]

This yields the following local stochastic monotonicity statement.

> [!lem] Lemma A — local fixed-point response
> Fix \(\lambda>1\), and let \(\pi_\lambda\) be the nonzero fixed point of the RDE (2.1).
>
> There exists a neighborhood \(\mathcal U\) of \(\pi_\lambda\), for instance in \(W_1\), such that whenever
> \[
> \pi_0,\pi_1\in\mathcal U,
> \qquad
> \pi_0\le_{\mathrm{st}}\pi_1,
> \qquad
> \pi_0\ne\pi_1,
> \]
> one has
> \[
> \boxed{
> \mathcal V_\lambda(\pi_0)
> <
> \mathcal V_\lambda(\pi_1).
> }
> \tag{14.3}
> \]

### Proof

Choose the monotone quantile coupling

\[
X_0\le X_1
\qquad\text{a.s.}
\]

and define

\[
X_t=(1-t)X_0+tX_1,
\qquad
\pi_t=\operatorname{Law}(X_t).
\]

For \(\pi_0,\pi_1\) sufficiently close to \(\pi_\lambda\), the entire path \((\pi_t)\) remains in a neighborhood where the response kernel is uniformly positive.

Let

\[
D_t
=
\mathbb E_{\pi_t}
\left[
\frac{X+Y-XY}
{c+X+Y-XY}
\right].
\]

Differentiating the quotient defining \(\mathcal V_\lambda(\pi_t)\),

\[
\frac d{dt}
\mathcal V_\lambda(\pi_t)
=
\frac2{D_t}
\mathbb E\left[
(X_1-X_0)
\Psi_{\pi_t}(X_t)
\right].
\tag{14.4}
\]

Since

\[
X_1-X_0\ge0
\]

and the kernel is strictly positive,

\[
\frac d{dt}
\mathcal V_\lambda(\pi_t)>0
\]

unless \(\pi_0=\pi_1\).

Integrating over \(t\in[0,1]\) proves (14.3).

\(\square\)

---

# 15. What has been reduced, and what remains

For a general offspring law with \(m_1\ge2\), the speed problem has now been reduced to the behavior of the RDE fixed point.

The speed has the universal form

\[
v(\lambda)
=
\mathcal V_\lambda(\pi_\lambda),
\]

where

\[
\beta_\lambda
\stackrel d=
\frac{\sum_{i=1}^{\nu}\beta_{\lambda,i}}
{\lambda+\sum_{i=1}^{\nu}\beta_{\lambda,i}}.
\]

Lemma A establishes that, for \(\lambda>1\),

\[
\boxed{
\text{near the RDE fixed point, increasing the escape-probability law
in stochastic order increases the speed functional.}
}
\]

The proof is distribution-free in the following sense: the only specific structural property of the offspring law used in the proof of Lemma A is the decomposition

\[
\sum_{i=1}^{\nu}\beta_i
=
\beta_1+\sum_{i=2}^{\nu}\beta_i,
\]

together with

\[
\beta_1
\perp
\sum_{i=2}^{\nu}\beta_i,
\qquad
\sum_{i=2}^{\nu}\beta_i\ge0.
\]

Thus Lemma A itself only requires

\[
\nu\ge1
\qquad\text{a.s.}
\]

and not the stronger assumption \(m_1\ge2\).

---

# 16. Universal comparison when the bias changes

For \(h>0\), the RDE gives a useful pathwise comparison.

Let

\[
S_\lambda
=
\sum_i\beta_{\lambda,i}.
\]

Since every subtree escape probability decreases as \(\lambda\) increases,

\[
S_{\lambda+h}\le S_\lambda.
\]

Therefore

\[
\begin{aligned}
\beta_{\lambda+h}
&=
\frac{S_{\lambda+h}}
{\lambda+h+S_{\lambda+h}}
\\
&\le
\frac{S_\lambda}
{\lambda+h+S_\lambda}.
\end{aligned}
\]

Since

\[
S_\lambda
=
\frac{\lambda\beta_\lambda}{1-\beta_\lambda},
\]

we obtain

\[
\boxed{
\beta_{\lambda+h}
\le
T_{\lambda,h}(\beta_\lambda),
}
\tag{16.1}
\]

where

\[
\boxed{
T_{\lambda,h}(x)
=
\frac{\lambda x}
{\lambda+h(1-x)}.
}
\tag{16.2}
\]

Consequently,

\[
\boxed{
\pi_{\lambda+h}
\le_{\mathrm{st}}
(T_{\lambda,h})_\#\pi_\lambda.
}
\tag{16.3}
\]

This comparison is universal: it does not involve \(m_1\), \(m\), or an upper bound on the offspring distribution.

---

# 17. Reduction to the root-response problem

For sufficiently small \(h\), the two probability laws in (16.3) lie in the neighborhood where Lemma A applies. Therefore

\[
\begin{aligned}
v(\lambda+h)
&=
\mathcal V_{\lambda+h}(\pi_{\lambda+h})
\\
&\le
\mathcal V_{\lambda+h}
\bigl((T_{\lambda,h})_\#\pi_\lambda\bigr).
\end{aligned}
\tag{17.1}
\]

Define

\[
G_\lambda(h)
:=
\mathcal V_{\lambda+h}
\bigl((T_{\lambda,h})_\#\pi_\lambda\bigr).
\tag{17.2}
\]

Then

\[
G_\lambda(0)=v(\lambda).
\]

Hence, whenever the relevant derivatives exist,

\[
v'(\lambda)
\le
G_\lambda'(0).
\tag{17.3}
\]

Thus the remaining problem is the following.

> [!lem] Lemma B — root-bias response
> For the RDE fixed-point law \(\pi_\lambda\),
> \[
> \boxed{
> G_\lambda'(0)<0.
> }
> \tag{17.4}
> \]

If Lemma B holds, then

\[
v'(\lambda)<0.
\]

Therefore, for the general offspring law, the monotonicity problem is reduced to

\[
\boxed{
\text{Lemma A: stochastic response of the speed functional}
\quad+\quad
\text{Lemma B: direct root-bias response}.
}
\]

Lemma A is proved above.

The remaining unresolved step is Lemma B.

---

# 18. Conceptual interpretation

The usual approach tries to control the full derivative

\[
-\partial_\lambda\beta_\lambda.
\]

This is difficult because a change in \(\lambda\) propagates recursively through the entire tree.

The present reduction separates two effects.

### Direct root response

Freeze all descendant escape probabilities and change only the root bias.

The resulting change in the root escape probability is exactly

\[
x
\longmapsto
T_{\lambda,h}(x)
=
\frac{\lambda x}{\lambda+h(1-x)}.
\]

### Descendant response

In the true model, the descendant escape probabilities also decrease when \(\lambda\) increases. Therefore

\[
\beta_{\lambda+h}
\le
T_{\lambda,h}(\beta_\lambda).
\]

Lemma A shows that this additional decrease can only reduce the speed functional further.

Thus one does not need to estimate the total derivative of the recursive conductance. It is sufficient to prove that the minimal response obtained by changing only the root bias already decreases the speed.

This is exactly the content of Lemma B.

---

# 19. Summary of the reduction

For a general no-leaf offspring law, and in particular for every law with \(m_1\ge2\),

\[
\boxed{
\beta_\lambda
\stackrel d=
\frac{\sum_{i=1}^{\nu}\beta_{\lambda,i}}
{\lambda+\sum_{i=1}^{\nu}\beta_{\lambda,i}}
}
\]

and

\[
\boxed{
v(\lambda)
=
\mathcal V_\lambda(\pi_\lambda)
=
\frac{
\mathbb E\left[
\dfrac{XY}{\lambda-1+X+Y-XY}
\right]
}{
\mathbb E\left[
\dfrac{X+Y-XY}{\lambda-1+X+Y-XY}
\right]}.
}
\]

The RDE fixed point satisfies the strict inequality

\[
\boxed{
\frac{
\mathbb E\left[
\dfrac{\beta}{\lambda-1+\beta}
\right]
}{
(\lambda-1)
\mathbb E\left[
\dfrac{1-\beta}{(\lambda-1+\beta)^2}
\right]
}
>
v(\lambda),
\qquad \lambda>1.
}
\]

This implies strict positivity of the first-variation kernel

\[
\boxed{
\Psi_\lambda(x)>0,
\qquad 0\le x\le1,
}
\]

and hence proves the local stochastic monotonicity statement of Lemma A.

Moreover,

\[
\boxed{
\pi_{\lambda+h}
\le_{\mathrm{st}}
(T_{\lambda,h})_\#\pi_\lambda,
\qquad
T_{\lambda,h}(x)
=
\frac{\lambda x}{\lambda+h(1-x)}.
}
\]

Consequently,

\[
\boxed{
v'(\lambda)
\le
\left.
\frac d{dh}
\mathcal V_{\lambda+h}
\bigl((T_{\lambda,h})_\#\pi_\lambda\bigr)
\right|_{h=0}.
}
\]

The remaining task is therefore to prove that the right-hand side is strictly negative.

This is Lemma B.