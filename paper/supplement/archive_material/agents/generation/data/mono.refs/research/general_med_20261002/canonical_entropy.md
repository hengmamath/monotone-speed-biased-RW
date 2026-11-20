# General canonical comparison and the complete branch source

Date: 2 October 2026. Status: complete local proofs through Lemma 4;
self-checked and passed one independent local audit arranged by the parent.
The quantitative sign candidate
at the end is explicitly **unproved**.

The setting, \(\mathcal C=C([0,1])\), \(J,L,R,r_0,q_0,b,N,Z,v,\Psi,C\)
are those in [response_interface.md](response_interface.md).
Only \(E\nu<\infty\) is assumed, and \(1<\lambda<m\).
All laws are the actual canonical laws; children are iid and independent
of the offspring count. We never replace them by arbitrary fixed points.

## Lemma 1: a canonical integer-moment constraint for arbitrary offspring

Put
\[
 W=(c+X)^{-1},\quad w=EW,\quad h=w^{-1}-c,\quad d=1-h,
 \qquad U=1-cW=X/(c+X).
\]
Then \(0<h<1\), \(0<U<1/\lambda\) almost surely, and
\(a_1=EU=h/(c+h)\). Define
\[
 a_n=EU^n,\quad \beta_n=h/(\lambda^n-d),\quad
 \rho_n=a_n/\beta_n \quad(n\ge0).
\]
Here \(a_0=\beta_0=1\). Then
\[
 \rho_0=\rho_1=1,\qquad
 \rho_n>\rho_{n+1}>0\quad(n\ge1),\qquad \rho_n\to0.
 \tag{1}
\]
In particular,
\(a_n/a_{n-1}<\beta_n/\beta_{n-1}\) for \(n\ge2\).
This constraint uses the actual chosen child and the actual root sum.

### Proof

For \(S=\sum_{i=1}^{\nu}X_i\), put
\(H=(c+S)^{-1}=W_1/(1+W_1T)\),
where \(T=\sum_{i=2}^{\nu}X_i\) is independent of \(W_1\).
The recursion implies \(\lambda W\overset d=1+H\), so
\(EH/EW=\lambda-1/w=d\). The canonical positive escape is less than
one, giving \(1/\lambda<w<1/c\), and hence \(0<h<1\).

The multiplier \(M(a)=E[H/W_1\mid W_1=a]=E(1+aT)^{-1}\)
decreases in \(a\). For any bounded increasing \(f\),
\[
 E[H f(1-cH)]\ge E[H f(U_1)]
 =wE_{\rm size\ bias}[M(W_1)f(1-cW_1)]
 \ge d E[W f(U)].
 \tag{2}
\]
The last inequality is the covariance inequality for two decreasing
functions under \(W_1\)-size bias. No size bias of \(\nu\) is used.
The first inequality is strict for the test \(f(u)=u^n\), \(n\ge1\):
on a genuine branch, \(T>0\), \(0<H<W_1\), and the test is strictly
increasing. Genuine branches have positive probability.

Since \(H=\lambda W-1\) and \(1-cH=\lambda U\) in the parent law,
(2) with \(f(u)=u^n\) yields
\[
 (\lambda^n-d)a_n-(\lambda^{n+1}-d)a_{n+1}>0
 \quad(n\ge1).
\]
Dividing by \(h\) proves strict decrease. Direct calculation gives
\(\rho_1=1\). Finally
\(\lambda^n a_n=E[(\lambda U)^n]\to0\) by bounded convergence,
because \(X<1\) implies \(\lambda U<1\) almost surely. Therefore
\(\rho_n\to0\). This last step needs no bounded offspring support
or strict deterministic escape cap. \(\square\)

## Lemma 2: the speed is strictly below the harmonic escape h

For every canonical law in this setting,
\[
 \boxed{\quad v<h.\quad}
 \tag{3}
\]
Consequently \(\inf_{[0,1]}\Psi>0\) for every \(1<\lambda<m\).

### Proof

Substituting \(x=cU/(1-U)\), with an independent copy \(V\), gives
\[
 N=cT,\quad Z=2Q-(\lambda+1)T,
 \quad T=\sum_{n\ge1}\lambda^{n-1}a_n^2,
 \quad Q=\sum_{n\ge1}\lambda^{n-1}a_na_{n-1}.
\]
All expansions are absolutely convergent: \(U\le1/\lambda\) and
\(\lambda UV\le1/\lambda<1\). Thus
\[
 v=c/[2K-(\lambda+1)],\qquad
 K=\frac{\sum_{n\ge1}\lambda^{n-1}a_n^2(a_{n-1}/a_n)}{T}.
\]
The comparison sequence \(\beta_n\) is the moment sequence of
\(U_\pi=\lambda^{-L_h}\), where
\(P(L_h=j)=h(1-h)^{j-1}\), \(j\ge1\).
Call its symmetric quotient \(v_\pi\). This is just a comparison
law; no identification with the speed of a different GW tree is needed.

The sequence \(\beta_{n-1}/\beta_n
=\lambda+dc/(\lambda^{n-1}-d)\) strictly decreases. By (1),
\(a_{n-1}/a_n\ge\beta_{n-1}/\beta_n\), strictly for \(n\ge2\).
The canonical averaging weights are the pipe averaging weights tilted
by the decreasing sequence \(\rho_n^2\). The elementary covariance
inequality for two decreasing sequences therefore yields
\(K>K_\pi\). Both quotient denominators are positive (they equal
\(Z/T\) for their respective actual positive probability laws), so
\(v<v_\pi\).

A short exact telescoping proves \(v_\pi<h\). Put
\[
 Q_* =\sum_{n\ge1}\frac{\lambda^{n-1}}{(\lambda^n-d)^2},\qquad
 R_* =\sum_{n\ge1}
 \frac{\lambda^{n-1}}{(\lambda^n-d)^2(\lambda^{n-1}-d)}.
\]
Then \(K_\pi=\lambda+dcR_*/Q_*\) and
\(v_\pi=1/(1+2dR_*/Q_*)\). Let
\(s_n=(\lambda^{n-1}-d)^{-1}\), \(s_{n+1}=(\lambda^n-d)^{-1}\).
Since
\(s_n-s_{n+1}=c\lambda^{n-1}s_ns_{n+1}\),
\[
 2hR_*-Q_*
 =c^{-1}\sum_{n\ge1}(s_n-s_{n+1})s_{n+1}(2h-s_n^{-1})
 =c^{-1}\sum_{n\ge1}(s_n-s_{n+1})^2(s_n^{-1}-h)>0.
 \tag{4}
\]
For the second equality subtract the displayed square term; the
remaining series telescopes as
\(\sum_n\{h(s_n^2-s_{n+1}^2)-(s_n-s_{n+1})\}
=hs_1^2-s_1=0\), because \(s_1=1/h\).
Each square term is nonnegative, and those for \(n\ge2\) are positive.
Equation (4) is exactly \(v_\pi<h\).

For the law kernel put \(z=E(c+X)^{-2}\). Direct expansion gives
\[
 \Psi(0)=1-c(1-v)w-c\lambda vz
 >1-(c+v)w=(h-v)w>0,
 \tag{5}
\]
where \(cz<w\) since \(X>0\). The polynomial
\(P(y)=y^2+c[(1+v)y-v]\) is increasing. Relative to the
\((c+Y)^{-2}\) tilt, the \(A(x,Y)^{-2}\) tilt has increasing density,
since \(d[(c+y)/A(x,y)]/dy=\lambda x/A(x,y)^2\ge0\).
Its normalized expectation of \(P\) is therefore at least
\(\Psi(0)/z\). As \(J1(x)\ge1/\lambda^2\),
\(\Psi(x)\ge\Psi(0)/(\lambda^2z)>0\) uniformly. \(\square\)

## Lemma 3: an exact positive child-pair formula for the entropy defect

Let \(\ell=\log\lambda\),
\[
 g(x)=\frac{x(c+x)\log(1+c/x)}{\lambda c\ell}-\frac{x}{c}
 \quad(x>0),\qquad g(0)=0.
\]
For any finite positive list \(x_1,\ldots,x_n\), \(S=\sum_i x_i\),
\[
 \boxed{
 \sum_i g(x_i)-g(S)
 =\frac1{\lambda c\ell}\int_0^c(c-a)
 \sum_{i<j}
 \frac{x_ix_j(2a+x_i+x_j)}{(a+S)(a+x_i)(a+x_j)}\,da.}
 \tag{6}
\]
Every displayed pair contribution is positive for \(n\ge2\), while
the formula retains the complete sum \(S\) in the denominator.

### Proof

The elementary integral identity
\[
 x(c+x)\log(1+c/x)
 =cx+c^2/2-\int_0^c\frac{a(c-a)}{a+x}\,da
\]
follows by polynomial division under \(\int_0^c(a+x)^{-1}da\).
Subtract its value at \(S\) from its sum at the children. Since
\(\int_0^c a(c-a)/a\,da=c^2/2\), the remaining bracket is
\[
 \frac{n-1}{a}-\sum_i\frac1{a+x_i}+\frac1{a+S}
 =\frac1a\left[\sum_i\frac{x_i}{a+x_i}-\frac{S}{a+S}\right]
 =\frac1a\sum_{i<j}
 \frac{x_ix_j(2a+x_i+x_j)}{(a+S)(a+x_i)(a+x_j)}.
\]
The linear terms of \(g\) cancel. This proves (6), with all terms
integrable at \(a=0\). Differentiation of the integral identity gives
\[
 g''(x)=-\frac2{\lambda c\ell}\int_0^c
          \frac{a(c-a)}{(a+x)^3}\,da<0\quad(x>0).
\]
In particular \(g\) is strictly concave,
\(g(0)=g(1)=0\), and \(g\ge0\) on \([0,1]\). \(\square\)

## Lemma 4: complete entropy identity and a quantitative response floor

For the actual child list put
\[
 \delta_g=F_\lambda'(S)
       [\sum_i g(X_i)-g(S)]\ge0.
\]
Then
\[
 D=D_g+2E[\delta_g(R\Psi)(F_\lambda(S))],
 \qquad D_g=2E[g(X)\Psi(X)]-C.
 \tag{7}
\]
The extra term is strictly positive for all the current offspring laws.
Moreover, with
\[
 a_* =\min\{1,\Psi(0)/q_0(0)\}>0,
 \qquad H_* =\Psi-a_*q_0\ge0,
\]
one has the fully proved lower bound
\[
 \boxed{\quad D\ge K_*+2E[g(X)H_*(X)],
 \qquad K_*=2a_*E[br_0]-C.\quad}
 \tag{8}
\]
The response retained in this bound is not truncated at the first branch.
Its precise nonnegative omitted term is
\[
 D-[K_*+2E(gH_*)]
 =2E[\delta_g(RH_*)(F_\lambda(S))]\ge0.
 \tag{8a}
\]

### Proof, including unbounded offspring integrability

The unary identity, checked by substituting
\(x=c/(\lambda^t-1)\), is
\(g(F_\lambda(s))=b(F_\lambda(s))+F_\lambda'(s)g(s)\).
Subtracting the definition of \(\delta_g\) gives
\[
 g(F_\lambda(S))=b(F_\lambda(S))
           +F_\lambda'(S)\sum_i g(X_i)-\delta_g.
\]
For bounded continuous \(f\), stationarity and child exchangeability
therefore yield
\[
 E[g(X)(I-L)f(X)]=E[b(X)f(X)]-E[\delta_g f(F_\lambda(S))].
 \tag{9}
\]
To justify all expectations with unbounded \(\nu\), let
\(M=\max_{[0,1]}g\). Since \(g(S)\ge-S/c\),
\[
 0\le\delta_g\le\lambda^{-1}(M+1/c)\nu,
 \tag{10}
\]
which is integrable by finite mean. The middle exchangeability term is
bounded by \(M\|f\|_\infty\nu/\lambda\). These explicit bounds replace
the bounded-degree draft's compact-support argument.

Take \(f=R\Psi\) in (9), using the convergent bounded inverse from
the interface lemma, to obtain (7). Lemma 2 and positivity of \(R\)
make \(R\Psi>0\). Strictness of (6) on genuine branches makes the
last term strictly positive. Tonelli applies directly to the positive
source in (6); (10) supplies its finite expectation.

For (8), the polynomial
\((1-a_*)y^2+c[(1+v)y-v]\) is increasing, and its normalized
inverse-square expectation at \(x=0\) is nonnegative by the definition
of \(a_*\). The same increasing-density comparison as in Lemma 2
shows \(H_*\ge0\) everywhere. Since \(Rq_0=r_0\),
\(R\Psi=a_*r_0+RH_*\ge a_*r_0\).
Insert this into (7). Applying (9) also with \(f=r_0\) yields
\(E[\delta_g r_0(F(S))]=E[br_0]-E[gq_0]\), and hence (8).
\(\square\)

## Precise next sign lemma — not yet proved

A candidate sufficient inequality for arbitrary finite-mean canonical
laws is
\[
 \boxed{\quad K_*+2E[gH_*]>0.\quad}
 \tag{11}
\]
It is stronger than \(D>0\); failure of (11) would reject this response
floor, not monotonicity. It keeps the actual speed in \(H_*\) and the
canonical recursion in the source. It has a new positive contribution
absent from the excluded scalar correction alone, namely the logarithmic
response of the nonnegative remainder \(H_*\). Nonetheless it is only a
lower bound for the complete response and must first be screened.

The exact next alternative if (11) fails is to retain
\(2E[bRH_*]\) itself in
\(D=K_*+2E[bRH_*]\), or to raise the response floor for \(H_*\) by
its own branch source. Neither will be declared positive merely from
its individual kernels being nonnegative.

## Relationship with the earlier materials

The chosen-child comparison, integer-moment constraint, pipe quotient
comparison, logarithmic sensitivity, and full entropy identity are
reconstructions/extensions of mechanisms already retained in the source
drafts. They are not labeled newly discovered theorems here. This run
explicitly removes bounded-degree hypotheses from their limiting and
integrability interfaces. The short square-sum identity (4), the
symmetric pair-source formula (6), and the remainder floor (8)/(8a)
are new local derivations relative to the retained source map; no
literature-wide novelty claim has been checked.
