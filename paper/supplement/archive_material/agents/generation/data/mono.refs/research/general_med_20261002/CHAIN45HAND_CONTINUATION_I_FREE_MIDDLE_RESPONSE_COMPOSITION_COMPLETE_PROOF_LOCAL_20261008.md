# 更新后中段的完整响应接合：不需要按 I 的符号分支

2026-10-08 开始，2026-10-09 保存。新增证明，不覆盖旧 glue、旧图、旧回执或冻结 Mellin V3。本文的独立接受状态由本轮固定全文回执决定；旧局部 PASS 不自动变成本文 PASS。

## 1. 对象、进口的准确范围

固定后代律 \(\mu\)，\(\mu(0)=0\)、\(\mu(1)>0\)、\(1<m=\mathbb E_\mu\nu<\infty\)。普通 GW 根也用 \(\mu\)，根均匀选子，非根父边权 \(\lambda\)、各子边权1。\(X\) 是同一实际 terminal-one / artificial-parent canonical 逃逸律；\(Y\) 是其独立副本。取
\[
\lambda_a=707/500\le\lambda\le\lambda_b=39/20,\qquad\lambda<m.
\]
不假设 \(I\le0\)，不变更 \(\mu\)。若 \((\lambda+1)h\ge1\)，[harmonic_region.md](harmonic_region.md) 的完整证明已给 \(D>0\)。因此以下只考虑实际
\[
0<h<1/(\lambda+1),\quad c=\lambda-1,
\quad U=X/(c+X),\quad a=\mathbb EU=h/(c+h),\quad s=\mathbb EU^2/a.
\]
这直接给 \(0<a<\lambda^{-2}\)，不是从 \(I\) 的符号推来。Jensen 与 canonical 严格矩比给
\[
a\le s\le1/(\lambda+1-\lambda a).
\]

明确进口以下已经有固定全文局部独审的数学证明，而不是它们的旧代码输出：

* [response_interface.md](response_interface.md)：实际有限均值 \(C^1\) 响应、正有界全 resolvent \(\mathcal R\) 与 \(v'=-D/Z\)、\(Z>0\)。
* [canonical_entropy.md](canonical_entropy.md)：\(v<h\)、\(\Psi>0\)、完整熵源恒等式及 bounded \(g\)。
* [H3HAND_CONTINUATION_COMPLETE_HIGH_ESCAPE_K1_CONCAVITY_AND_TILT_MANUAL_PROOF_LOCAL_V2_20261008.md](H3HAND_CONTINUATION_COMPLETE_HIGH_ESCAPE_K1_CONCAVITY_AND_TILT_MANUAL_PROOF_LOCAL_V2_20261008.md)，§§1–5：实际 \(h<1/(\lambda+1)\)、\(7/5\le\lambda\le39/20\) 下
  \(2\Psi(x)-JP_c(x)>0\) 对每个 \(x\ge x_*:=1/(\lambda+1)\) 成立。其四矩/完整无限尾入口与本段相同；没有 \(I\) 条件。
* [HYBRIDJOINHAND_CONTINUATION_COMPLETE_TWO_INTEGRAL_AND_REAL_COUPLING_MANUAL_PROOF_LOCAL_20261008.md](HYBRIDJOINHAND_CONTINUATION_COMPLETE_TWO_INTEGRAL_AND_REAL_COUPLING_MANUAL_PROOF_LOCAL_20261008.md) 及其完整有限系数附录：上述实际 \(a,s,A(a)\) 和 \(\lambda\in[\lambda_a,\lambda_b]\) 下，两充分量 \(B_0,B_1>0\)。其进口的 \(s\) 凹性来自固定 DISPLAY_V2，四矩入口只来自 high-k1 的先行 §§1/3；四端点正性由两积分独立支付，没有用最终 hybrid 正性证明先行凹性。

后三份局部证明内的数学责任、原式、全部有限表及回执由本轮有效来源账精确锁定。原概率论文仍按基础接口明列的外部定理进口。

## 2. 全响应同时控制两个源

令 \(b(x)=x(1-x)/\lambda\)，\(\eta(f)=\mathbb E[b(X)(\mathcal Rf)(X)]\)。正 Neumann 级数给 \(\eta\ge b\pi\)，这里 \(\pi=\mathcal L(X)\)。完整熵恒等式对每个非负连续 \(f\) 给
\[
\eta(f)=\mathbb E[g(X)f(X)]+\mathbb E[\delta_g(\mathcal Rf)(F_\lambda(S))]
\ge\mathbb E[g(X)f(X)].
\]
两边是有限正测度；连续测试的序关系延拓到 Borel 集。将任意 Borel 集分别交 \(\{g\ge b\}\) 和 \(\{g<b\}\)，得到
\[
\eta\ge\max(g,b)\pi.\tag{1}
\]
同实际速度下 \(C=\mathbb E[bJP_c]\)、\(\Psi>0\)，所以
\[
D=2\eta(\Psi)-C
\ge\mathbb E\{2\max(g(X),b(X))\Psi(X)-b(X)JP_c(X)\}.\tag{2}
\]
\(g,b,\Psi,JP_c\) 在 \([0,1]\) 有界，故 (2) 全部可积。\(g/b\) 在零附近可以无界；这里没有把它当作有界测试，也没有假设逆逃逸矩。

熵的一子恒等式
\(g(F_\lambda(z))-b(F_\lambda(z))=F_\lambda'(z)g(z)\)，及 \(g(z)>0\) 当 \(0<z<1\)、\(g(1)=0\)、\(g(z)<0\) 当 \(z>1\)，给
\[
g(x)\ge b(x)\quad(0<x\le x_*),\qquad
b(x)\ge g(x)\quad(x_*\le x<1).\tag{3}
\]
两式在 \(x_*\) 取等号；核的正性在该点仍严格。

## 3. 低逃逸变换的全部进口也没有 I 条件

对 \(0<x\le x_*\)，令 \(\theta=\lambda x/(c+x)\in(0,1/\lambda]\)。直接代换给
\[
R_g(x)=g(x)/b(x)=-1/c-\log\theta/[\log\lambda(1-\theta)].
\]
[hybrid_rational_moment_reduction.md](hybrid_rational_moment_reduction.md) §1 的两次积分 Jensen 给
\[
R_g\ge R_{\rm rat}:=
1+\frac{9\lambda(1-\lambda\theta)[28\lambda+17+(17\lambda+19)\theta]}
{c(\lambda+1)(2\lambda+7)(2\lambda+1)(2+7\theta)(2+\theta)}\ge1.\tag{4}
\]
其证明对每个 \(\lambda>1\) 成立：在 \([0,1/2]\)、\([1/2,1]\) 的权 \((1-t)dt\) 质量分别 \(3/8,1/8\)，重心分别 \(2/9,2/3\)；对两倒数线性因子的凸乘积用 Jensen，并用
\(\log\lambda\le c(\lambda+1)/(2\lambda)\)。这没有 canonical、源 \(I\) 或偏置至少 \(\sqrt2\) 的附加前提。

实际四矩及完整无限速度尾给
\[
r:=v/(1+v)\le r_{\rm up}=\frac{aE_4}{2(B+aE_4)},\quad
E_4=c+A(a)s^2,\quad B=1-\lambda a+\lambda as(1-\lambda s)>0.
\]
\(A(a)\) 正是 high-k1 §1 的原函数，由 canonical 三四矩比和完整几何尾取得，没有 \(I\) 条件。固定 \(R\ge1\) 的 signed 核除以 \(1+v\) 后，其 \(r\) 导数是
\(-2R(y^2+c)-2(1-y)<0\)。先用 \(\Psi>0\) 降低 \(R_g\) 到 \(R_{\rm rat}\)，再升高实际 \(r\) 到 \(r_{\rm up}\)，均给正确下界。

完整 \(y\mapsto U\) 变换为
\[
\frac{2RP_v(y)-P_c(y)}{(1+v)A(x,y)^2}
=\frac{-C+LU-KU^2}{(c+x)^2(1-\theta U)^2},
\]
其中 \(C=2r(1+cR)\)、\(L=c+2(\lambda+1)r+2Rc(c+2r)\)、\(K=\lambda(c+C)\)。置
\(D_1=L-2\theta C>0\)、\(E_1=-K+2\theta L-3\theta^2C\)。精确短除法给
\[
\frac{-C+LU-KU^2}{(1-\theta U)^2}
=-C+D_1U+U^2j(U),\quad
j(U)=\frac{E_1-\theta^2D_1U}{(1-\theta U)^2}.
\]
\(j'\) 的分子随 \(U\) 递减，所以最低值落在 \(0\)、\(1/\lambda\) 两端。因此期望严格正的充分量准确为
\[
B_0=-C+D_1a+E_1as,\qquad
B_1=(-C+D_1a)(1-\theta/\lambda)^2+
(E_1-\theta^2D_1/\lambda)as.\tag{5}
\]
当前完整 hybrid 证明支付的正是 (5) 在同实际四矩包络、\(R=R_{\rm rat},r=r_{\rm up}\) 时的两个正值。没有用旧自由矩盒或数组定义另一目标。由 (4)–(5) 及两个比较方向，
\[
2R_g(x)\Psi(x)-JP_c(x)>0\qquad(0<x\le x_*).\tag{6}
\]

## 4. 接点、完整严格性与无循环性

因为 \(707/500>7/5\)，high-k1 的范围包含本文。高逃逸严格核覆盖 \([x_*,1]\)，(6) 覆盖 \((0,x_*]\)，且在 \(x_*\) 有 \(R_g=R_{\rm rat}=1\)。没有空隙或等号处的零核。实际 \(0<X<1\) 几乎处处，故 \(b(X)>0\)。将两个核及 (3) 代入 (2)，得到有界、几乎处处严格正的被积函数，因此
\[
D>0,\qquad v'(\lambda)=-D/Z<0.
\]
上述不依赖 \(I\)；故在本文中段可移去旧装配的 \(H_I\to H_{\rm MIDDLE}\) 依赖边。\(H_I\) 本身的已证一次换号/\(I\ge0\) 条件定理继续保留为备用，不撤其结论，不把这个接合外推到 \(\lambda<707/500\)。

逻辑先后为：实际响应/熵和 canonical 矩 → 完整四矩尾包络 → high-k1 正核及独立 \(s\) 凹性 → 两积分支付真实四端点 → (5)、(6) → max-source 全响应。没有使用中段最终正性来证明任何先行叶。\(\lambda=\lambda_a,\lambda_b\) 都在局部闭域；\(\lambda=m\) 不在模型范围内。与相邻段的接点保持，速度范围仍只有 \((1,m)\)。

本次新增的是这个完整数学接合。hybrid 的2282残余槽、23槽四矩帽、167控制行及 high-k1 的393残余槽等有限算术仍由完整旧局部正文及固定独审承担，未因省去 \(I\) 分支而免除。它是可手核但仍长的证明合集的一部分，不是计算量为零、真人审稿或形式化认证。
