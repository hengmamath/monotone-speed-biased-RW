# A hand-verifiable low-escape speed theorem

2026-10-06, v2. Internally independently PASS. This revision adds only the requested coordinate display of Z.

**Theorem.** Fix μ0=0, μ1>0, 1<m=Eμν<∞, ordinary GW root law μ, parent weight λ and child weights 1. For the terminal-one canonical X put u=E[X/(λ−1+X)]. If 1<λ<m, λ≤6/5 and u≤1/16, then v′μ(λ)<0, with μ held fixed.

## 1. Analytic interfaces

We import the following finite-mean response/entropy and canonical probability interfaces.

Put c=λ−1, U=X/(c+X), a_s=EU^s, u=a1, b=a2,
\[
h=cu/(1-u),\quad d=1-h,\quad\beta_s=h/(\lambda^s-d),\quad
r_s=\beta_{s+1}/\beta_s,\quad\rho_s=a_s/\beta_s.
\]
Here 0<X<1, a0=β0=1; ρ1=1, 0<ρ_(s+1)<ρ_s≤1 for s≥1, and ρ_s→0. Also Θ_s=kβ_s[−ρ′(s)]>0, k=c/(λ logλ), using the deterministic real-age derivative.

For iid X,Y define A=c+x+y−xy, Jf(x)=E[f(Y)/A²], r0=Jid, q0=J(y²), bt=x(1−x)/λ. The full resolvent \(\mathcal R\) is positive, \(\mathcal Rq_0=r_0\). Set Ψ=J[y²+c((1+v)y−v)], α=min(1,Ψ(0)/q0(0))∈(0,1]; H*=Ψ−αq0≥0. The C1 response gives
\[
v'=-D/Z,\quad D=2E[bt\,\mathcal R\Psi]-C,\quad
C=E[bt\,JP_c],\quad P_c(y)=2v-(1+3v)y+(1+v)y^2.
\tag{1}
\]
The speed quantities are
\[
T=\sum_{s\ge1}\lambda^{s-1}a_s^2,\quad
Q=\sum_{s\ge1}\lambda^{s-1}a_sa_{s-1},\quad
Z=2Q-(\lambda+1)T>0,\quad v=cT/Z.
\]

For τ=X+Y−XY and A=c+τ, write V=Y/(c+Y). Direct substitution gives
\[
\frac{\tau}{A}=\frac{U+V-(\lambda+1)UV}{1-\lambda UV}.
\]
The positive geometric expansion yields E[U/(1−λUV)]=Q and E[UV/(1−λUV)]=T. Hence the response denominator E[τ/A] is exactly Z=2Q−(λ+1)T, with no extra scale factor.

In the hard case 0<α<1,
\[
\alpha=(u-(v/c)A_0)/b,\quad A_0=1-(\lambda+1)u+\lambda b>0.
\]
Entropy gives D≥F*≥Fcap, using the correct first factor a_s−λa_(s+1). The raw cap extracts no Θ lower bound. Its algebra is in §6.

The α=1 case is already elementary from (1). Since H*=Ψ−q0≥0,
\[
D=(1+v)E[bt(r_0-q_0)]+(2/c)E[bt H_*]
 +2E[bt\,\mathcal R H_*]>0.
\]
Expand Pc; r0−q0>0 and bt>0 give strictness. Henceforth 0<α<1.

## 2. Complete moment payment

The π symbols denote the deterministic β reference; the escape law remains actual. Define
\[
B_s=c/(\lambda^s-1),\ f_s=\lambda^{s-1}B_s^2,\ R_s=1-u+uB_s,
\quad \beta_s/u=B_s/R_s,
\]
\[
t=T/u^2,\ q_a=Q/u,\ t_\pi=\sum f_s/R_s^2,
\quad H=\sum s f_s^2\rho_s^2/R_s^3,\ H_\pi=\sum s f_s^2/R_s^3,
\]
\[
p_s=\frac{cs}{\lambda}\frac{\lambda^s+1}{\lambda^s-1}
-\frac{\lambda+1}{\lambda}\ge0,\quad P=\sum f_sp_s\rho_s^2/R_s^2,
\quad M=\frac{2q_a}{2q_a-(\lambda+1)ut}.
\]
Nonnegativity of p_s follows from increasing x coth x. Let L_s=1/λ−r_(s−1), δ_s=a_sr_s−a_(s+1),
\[
G=u^{-2}\sum s\lambda^{s-1}(1+L_s)a_s\delta_s,
\]
\[
G_+=\sum G_s\left[\lambda+
\frac{(s+1)\lambda a_{s+1}}{s a_s(1+L_s)}\right]\ge\lambda G.
\]
G_s denotes the s-th summand. The exact complete-root identity is
\[
F_{\rm cap}/u^2=M[P+u(t^2/q_a-2H)+(ut/q_a)G_+]+2\alpha G.\tag{2}
\]

The relative defect bound is
\[
t_\pi-t\le2\lambda G/(1-u).\tag{3}
\]
For Δ_i=ρ_i−ρ_(i+1), g_i=iλ^(i−2)β_i²,
Γcap=u²G=Σg_iρ_iΔ_i. The pipe tails satisfy
AQ_i=Σ_(n>i)λ^(n−1)β_nβ_(n−1)=hβ_i/c,
AT_i=Σ_(n>i)λ^(n−1)β_n²<AQ_i/λ, and
AQ_i/g_i=λ²(1−dλ^(−i))/(ci)≤λ²/(1−u).
Tonelli gives tπ−t=u^(−2)ΣΔ_i(ρ_i+ρ_(i+1))AT_i, proving (3).

We also have 1≤q_a≤1/(1−u), t≥1, and
\[
t_\pi<16/9,\quad M\le90/79,\quad t/q_a\ge15/16.\tag{4}
\]
Use f_s≤s^(−2), f1=R1=1 and Σs^(−2)<5989/3600<5/3 (five terms plus ∫5∞x^(−2)dx). Thus tπ≤1+(2/3)/(1−u)²≤1187/675<16/9. Put κ=(1−u)tπ. Its bounds are 1−u≤κ≤(1−u)+(2/3)/(1−u)≤5/3; the last function decreases for u≤1/16. Substitution gives (4).

The decreasing sequences β_(s−1)/β_s and ρ_s² satisfy weighted Chebyshev with weights λ^(s−1)β_s². Including ρ_(s−1)/ρ_s>1 for s≥2 gives Q/T>Qπ/Tπ, hence R*=v/c<Rπ. Also b<β2. Since A0>69/80 and
u−Rπ[1−(λ+1)u]=u(2−κ)/[2−(λ+1)uκ]>0,
and β2=u/(λ+1−λu), Rπ=uκ/[2−(λ+1)uκ], we obtain
\[
\alpha>\alpha_\pi=
\frac{(\lambda+1)(2-\kappa)-2\lambda u}{2-(\lambda+1)u\kappa}
\ge\frac{2/3-(12/5)u}{2-2u(1-u)}\ge\frac{992}{3615}.\tag{5}
\]
Its derivative numerator 18u²−10u−13 is negative on [0,1/16].

Let B=(1−u)tπ²−2Hπ. By (3), H≤Hπ and (4),
 t²/q_a−2H≥B−4λtπG. Retain G+ in (2) to obtain
\[
D/u^2\ge M[P+uB]+C_*G,\quad
C_*= \frac{1984}{3615}-\frac{90}{79}\frac65\frac1{16}
\left(\frac{64}{9}-\frac{15}{16}\right)
=\frac{389899}{18277440}>0.\tag{6}
\]
Retain the second-age and root terms:
\[
P\ge\frac{c^2}{(\lambda+1)^3}\rho_2^2,\quad
G\ge(1-\rho_2)/\lambda.
\]
Indeed f2=λ/(λ+1)², p2=c²/[λ(λ+1)], R2≤1; the first G term is (1−ρ2)/λ. With K0=C_*(79/90)(5/6)=389899/24986880,
\[
D/u^2\ge M[P+uB+K_0(1-\rho_2)].\tag{7}
\]

## 3. Six λ-only bounds with full tails

Put T0=Σf_s, H0=Σs f_s², A=Σf_s(1−B_s), Ctail=Σs f_s²(1−B_s). We prove
\[
T_0>1559/1000\ (\lambda\le6/5),\quad
T_0>63/40\ (\lambda\le23/20),\quad A>9/25\ (\lambda\le6/5),
\]
\[
H_0<241/200\ (\lambda>1),\quad
H_0<239/200\ (\lambda\ge23/20),\quad C_{tail}<2/15\ (\lambda\le6/5).
\tag{8}
\]
Also T0>19/12 for λ≤11/10.

Write a=logλ. Then f_s=[sinh(a/2)/sinh(sa/2)]²≤s^(−2). For s≥2 it decreases in λ, because x coth x increases: its derivative has numerator sinh(2x)−2x>0. B_s decreases in λ and B_s≤1/s. These give the endpoint comparisons.

For real x>0, f(x)=λ^(x−1)c²/(λ^x−1)² is decreasing and convex. Its derivatives are f′=−af coth(ax/2) and f″=a²f[coth²(ax/2)+(1/2)csch²(ax/2)]>0. Convex trapezoid comparison gives the entire tail
\[
\sum_{s\ge9}f_s\ge\int_9^\infty f(x)dx+f_9/2
\ge\tau(\lambda):=\frac{c^2}{\lambda L(\lambda)(\lambda^9-1)}+f_9/2,
\tag{9}
\]
where L=c−c²/2+c³/3≥logλ, by integrating 1/(1+t)≤1−t+t². The integral is c²/[λ logλ(λ^9−1)].

For H0 retain the λ decay in the integral tail. x f(x)² decreases, since its logarithmic derivative is 1/x−2a coth(ax/2)<−3/x. Put z=λ^(−8), aL=2c/(λ+1)≤logλ. Expanding (1−e^(−ax))^(−4) with positive terms and integrating gives
\[
\sum_{s\ge9}s f_s^2\le\int_8^\infty x f(x)^2dx
\le E(\lambda):=\frac{c^4z^2}{6\lambda^2}
\left[\frac8{a_L}\frac{3-z}{(1-z)^3}
+\frac1{a_L^2}\left(\frac{2-z}{(1-z)^2}-\frac12\right)\right].\tag{10}
\]
The integral equals (c⁴/λ²)Σ_(j≥0)binom(j+3,3)z^(j+2)[8/((j+2)a)+1/((j+2)²a²)]. Use
binom(j+3,3)/(j+2)=(j+1)(j+3)/6 and
binom(j+3,3)/(j+2)²=((j+2)−1/(j+2))/6.
The geometric sums are z²(3−z)/(1−z)³ and z²(2−z)/(1−z)². Keeping the j=0 negative subtraction z²/2 gives (10). Its remaining coefficients are positive, permitting a≥aL. Convexity of 1/x gives a≥aL. Tonelli justifies the full series.

Every entry below is the floor of 10⁶ times its rational value. Verify each by cross multiplication; no logarithms are evaluated.

|s|f_s(6/5)|f_s(23/20)|f_s(11/10)|B_s(6/5)|
|---|---:|---:|---:|---:|
|1|1000000|1000000|1000000|1000000|
|2|247933|248783|249433|454545|
|3|108682|109675|110440|274725|
|4|59967|60996|61795|186289|
|5|37444|38473|39281|134379|
|6|25235|26248|27053|100705|
|7|17899|18886|19682|77423|
|8|13162|14117|14900|60609|

The three 10⁶τ floors are 48837,60981,76035; the 10⁶E(23/20) ceiling is 4545, directly from (9),(10).

With S=10⁶ and columns w6,w23,w11,z6, the first three column sums plus tails are 1559159/S,1578159/S,1598619/S. These prove the T bounds. For A use 1−B_s≥1−1/s and, on the tail, 1−1/s≥8/9:
\[
A\ge\sum_{s=1}^8(w6_s/S)(1-1/s)+(8/9)(48837/S)
\ge362650/S>9/25.
\]
For Ctail use f_s≤s^(−2), B_s(λ)≥B_s(6/5)≥z6_s/S and the integral tail Σ_(s≥9)s^(−3)≤1/128:
\[
C_{tail}\le\sum_{s=1}^8s^{-3}(1-z6_s/S)+1/128
<131184/S<2/15.
\]
For H0 on λ≥23/20, use f_s(23/20)<(w23_s+1)/S and (10):
\[
H_0<\sum_{s=1}^8s((w23_s+1)/S)^2+4545/S
<1194930/S<239/200.
\]
Finally H0≤Σ_(s=1)^6s^(−3)+∫6∞x^(−3)dx=86701/72000<241/200. This proves all six bounds (8).

## 4. Strict sign

Because R_s=1−u(1−B_s), positivity of the geometric expansion gives tπ≥T0+2uA. Convexity on 0≤z≤1 gives (1−uz)^(−3)−1≤z[(1−u)^(−3)−1], hence Hπ≤H0+Ctail[(1−u)^(−3)−1]. Thus
\[
B>(1-u)(L+18u/25)^2
-2[\bar H+(2/15)((1-u)^{-3}-1)].\tag{11}
\]
Use \(L,\bar H\)=(19/12,241/200), (63/40,241/200), or (1559/1000,239/200) on the three respective λ intervals. Each right side decreases in u: its derivative is
(L+18u/25)(36/25−L−54u/25)−(4/5)(1−u)^(−4)<0.
At u=1/16 the exact values are respectively
\[
973799/51840000>0,\quad -d_1=-21361/3240000,
\quad-d_2=-566237/16200000.
\]
For λ≤11/10, (6) now gives D>0.

On [11/10,23/20] and [23/20,6/5], respectively, c²/(λ+1)³ has derivative c(5−λ)/(λ+1)⁴>0 and supplies P≥A_iρ2² with
A1=10/9261, A2=180/79507. The remaining fixed rational checks are
\[
K_0>2A_2>2A_1,\quad
A_1-d_1/16=11873177/17781120000>0,
\]
\[
A_2-d_2/16=1636194841/20608214400000>0.
\]
For ρ=ρ2∈(0,1), A_iρ²+K0(1−ρ)=A_i+(1−ρ)[K0−A_i(1+ρ)]≥A_i. Equation (7) therefore gives
D/u²>M[A_i−d_i/16]>0 on both intervals. Equation (1) completes v′<0 for all the stated laws.

## 5. Dependencies

Analytic interfaces: `response_interface.md`, `canonical_entropy.md`, `scaled_r0_adjacent_defect_payment.md`. Corrected indices: formal `mellin_index_errata_and_dependency_impact_20261005.md`. All λ-only inputs are proved here; the new arithmetic source uses no old guard.

## 6. Complete-root algebra

The deterministic algebra is as follows. Set W0_s=cs/λ−1+2sL_s,
Hloc_s=s−(s+1)λL_(s+1), Dloc_s=2sL_s−s/λ+Hloc_s r_s,
C_s=α(1+L_s)+R[c+λL_s+(s+1)λL_(s+1)/s], R=v/c.
The raw entropy interface is
Fcap=−2RuL1+Σλ^(s−1)a_s²[(1+v)W0_s+2R Dloc_s]+2Σsλ^(s−1)a_sδ_sC_s.
The root uses a0=1.

Direct algebra gives W0_s−1/λ=p_s−2u s f_s/R_s. Define
J_N=u^(−2)Σ_(s=1)^N λ^(s−1)a_sδ_s[Hloc_s+(s+1)λa_(s+1)/a_s].
With t_N=T_N/u² and Q_N the corresponding partial sums, the finite telescoper is
\[
\sum_{s=1}^N\lambda^{s-1}a_s^2(Dloc_s-W0_s)/u^2
=t_N-1-(Q_{N+1}-u)/(\lambda u^2)+J_N
+(N+1)\lambda^Na_{N+1}^2/u^2.
\]
The last endpoint tends zero by a_s≤λ^(−s). Substitute R=ut/[2q_a−(λ+1)ut] and L1=1/λ−u. The diagonal becomes M[P+u(t²/q_a−2H)+utJ/q_a]. Combining its J term with the whole extra C_s coefficient yields exactly G+ in (2); its α part is 2αG. The finite endpoint vanishes at fixed λ. The additional Θ surplus is nonnegative.
