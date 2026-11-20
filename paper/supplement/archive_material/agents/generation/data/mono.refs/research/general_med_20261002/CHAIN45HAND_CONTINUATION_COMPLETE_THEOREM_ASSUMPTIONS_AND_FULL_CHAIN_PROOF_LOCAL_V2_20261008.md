# 当前 45 宏节点：完整定理、有效证明合集与全链接合

2026-10-08 开始，2026-10-09 保存。本文是更新后的统一数学证明正文，不复制历史归档。它和有效来源账列出的完整局部正文、全部有限附录共同构成证明；本文单文件没有重新打印百万字节的局部表。各旧 LOCAL/PENDING 标题的当前状态取决于准确固定正文的正式局部回执，不取决于标题、作者输出或后来的口头记录。本轮最终独立接受与保全回执另存。V2只明确区分 master 首项 eS1 与 Q1 正参考首项 eA1=eu⁴；V1保留。

唯一辅助仍为原独立核验者；独立 AI 审读、真人审稿、形式化证明和 whole-problem verifier 是不同层级。本次没有执行旧 checker、作者生成器、外层 runner 或网格。Mellin V3、旧文件、旧失败及冻结记忆全部保持。当前新只追加记忆为 `agents/generation/memory/mono/events.chain45_full_review_20261008.jsonl`。

## 1. 证明对象与证据层级

本证明所需对象为固定 \(\mu\)，满足
\[
\mu(0)=0,\quad\mu(1)>0,\quad1<m=\sum_{k\ge1}k\mu(k)<\infty.
\]
普通 GW 根和其他顶点都用 \(\mu\)。根均匀选子；非根有 \(k\) 个子时父边概率 \(\lambda/(\lambda+k)\)，各子边概率 \(1/(\lambda+k)\)。\(\mu\) 在 \(\lambda\) 变化时保持固定。无需有界子代、二阶子代矩或两点子代归约。由于无叶，树不会灭绝。

内部已审的有限算术模块给下文全部局部引理。它们是完整有限数学证明的组成部分：原函数、清分母、次数封口、完整系数、负项支付和连续域推理均已公开。**公开数组仍须逐项核对**；本轮统一审查承接各固定局部数学独审，重新审跨模块推理，并没有重新计算每个数组的每个整数。因此这里可以给出明确的完整证明合集及内部接受状态，不能给出真人或形式化认证，也不能宣称得到一份很短、无需有限算术的统一证明。

分类约定：

* **P**：明确进口的原概率论文定理及适用性；原论文证明没有由本轮重新证明。
* **A**：公开完整解析/概率接口推导，有限均值可积性明确；固定局部独审和本轮接合审查分列。
* **F**：完整可手核但有时很长的有限有理算术证明。软件曾用来生成或独立复核；证明成立的理由是全部身份和连续支付，不是 exit0。
* **C**：只能靠未展示的程序证书承接的 sign 前提。当前有效充分路线不选用这种前提；历史更广自由盒仍可能用它们。
* **U/N**：尚未证明的命题 / 数值证据。两者都不能成为本定理前提。

逐个宏节点的范围、必要性、完整正文、精确回执、有限算术和本轮重核边界见本轮 `EFFECTIVE_45_NODE_EVIDENCE_AND_ARITHMETIC_LEDGER` 的 Markdown/JSON。基础宏目录原有123个 source pins 不是全部二级子证明的闭包；本轮另固定真正使用的二级正文和回执，不把所有历史文件加入前提。

## 2. 原概率入口：完整陈述与适用性

使用已提供的 [primary excerpts](../../evidence/imported_speed_formula.md)，及 [response_interface.md](response_interface.md) 的定义展开。

**P0-a。** Aïdékon，*Speed of the biased random walk on a Galton–Watson tree*，`paper_id=Aidekon-speed-GW`，`arXiv:1111.4313v4`，`theorem_id=Theorem 1.1`。其有限均值超临界 GW 树、在非灭绝事件上的 \(\lambda\)-biased walk，当 \(\lambda_c<\lambda<m\) 时有确定速度，并给
\[
v=\frac{\mathbb E[(\nu-\lambda)\beta_0/(c+\sum_{i=0}^{\nu}\beta_i)]}
{\mathbb E[(\nu+\lambda)\beta_0/(c+\sum_{i=0}^{\nu}\beta_i)]},\qquad c=\lambda-1,
\tag{P}
\]
其中 iid \(\beta_i\) 为该树的实际 artificial-parent 逃逸概率，且与原 \(\nu\) 独立。无叶时灭绝概率为0，\(\lambda_c=\mu(1)<1\)；本证明只取 \(1<\lambda<m\)，满足其范围。没有额外二阶子代矩。

**P0-b。** Song–Wang–Xiang，*Monotonicity of the speed of biased random walk on a Galton–Watson tree*，`paper_id=Song-Wang-Xiang-monotonicity-GW`，`arXiv:1610.08151v1`，`theorem_id=equation (2.1), Lemma 2.1, equation (2.2)`。保留的原文说明无叶普通根的根均匀选子规则；Lemma 2.1 说明所用普通根/附加父顶点模型的速度一致；(2.1) 与 (P) 一致，(2.2) 给 actual canonical 递推
\[
X\overset d=F_\lambda(S_\nu),\quad F_\lambda(z)=z/(\lambda+z),\quad
S_\nu=\sum_{i=1}^{\nu}X_i.
\]
取 terminal-one 极限，不取任意分布固定点。\(\lambda<m\) 时 actual \(X>0\)；有限 \(\nu\) 几乎处处给 \(X<1\)。本研究不使用该文最少子代至少二的单调性结果。

这是明确的论文定理进口，而非无出处概率假设。其原证明不重新认证。其余本地引理都保持同一个 actual 逃逸律与同参数 iid 孩子。

## 3. 完整速度归一化与实际 C¹ 响应（A1）

令 iid \(X,Y\) 与 \(\tau=x+y-xy\)、\(A=c+\tau\)。从 (P) 条件交换性及递推的分母取消，得到
\[
N=\mathbb E[XY/A],\quad Z_{\rm act}=\mathbb E[\tau/A]>0,
\qquad v=N/Z_{\rm act}.
\tag{1}
\]
没有把另一标量 \(Z_p\) 当作此分母。置
\[
Jf(x)=\mathbb E[f(Y)/A(x,Y)^2],\quad
\mathcal L f(x)=\mathbb E[\nu F_\lambda'(x+S_{\nu-1})f(F_\lambda(x+S_{\nu-1}))],
\]
\[
r_0=J\mathrm{id},\quad q_0=J(y^2),\quad b(x)=x(1-x)/\lambda.
\]
精确分母取消和 iid 交换性给
\((I-\mathcal L)r_0=q_0\)。在 \([0,1]\) 上 \(r_0,q_0\) 连续且最小值正，故 \(r_0\) 加权范数下
\[
\|\mathcal L\|\le1-\min(q_0/r_0)<1,\qquad
\mathcal R=(I-\mathcal L)^{-1}\ge0,\quad\mathcal Rq_0=r_0.
\tag{2}
\]
\(\mathbb E\nu<\infty\) 控制该算子；没有使用 \(\mathbb E\nu^2\)。

[response_interface.md](response_interface.md) §§固定律唯一性/参数正则性证明：ordered fixed-law 插值的 \(r_0\) 严格 coercivity 给非零固定律唯一性；terminal-one 一侧极限保持非零，因此 actual 律 \(W_1\)-连续。子代 \(\nu>K\) 的尾由 \(\mathbb E[\nu;\nu>K]\) 控制，给局部 Lipschitz。对有界连续测试 \(f\)，用有限正差商测度
\(
\eta_h(f)=\mathbb E[h^{-1}\int_{X_{\lambda+h}}^{X_\lambda}f(z)dz]
\)
和 fixed-test 强连续，而不是未证算子范数收敛，得到
\[
\frac d{d\lambda}\mathbb Ef(X_\lambda)
=-\mathbb E[b(X)(\mathcal R f')(X)]\quad(f\in C^1).
\]
完整 pair-test 的导数一致收敛和 resolvent 局部连续给 \(v\in C^1((1,m))\)，准确响应为
\[
\Psi=J[y^2+c((1+v)y-v)],\quad
C=\mathbb E[(v\tau-XY)/A^2],\quad
D=2\mathbb E[b\mathcal R\Psi]-C,\quad v'=-D/Z_{\rm act}.
\tag{3}
\]
同实际速度 \(N-vZ=0\) 的对称取消还给 \(C=\mathbb E[bJP_c]\)，\(P_c(y)=(1-y)[2v-(1+v)y]\)。所有比较速度下使用此式必须带下一节的 off-speed 修正。

## 4. canonical 严格比较、熵恒等式和 alpha 分支（A2/A3）

置 \(W=(c+X)^{-1}\)、\(h=(\mathbb EW)^{-1}-c\)、\(d=1-h\)、\(U=X/(c+X)\)、\(a_i=\mathbb EU^i\)，
\[
u=a_1=h/(c+h),\quad\beta_i=h/(\lambda^i-d),\quad
\rho_i=a_i/\beta_i.
\]
[canonical_entropy.md](canonical_entropy.md) 的 chosen-child 比较采用原 \(\nu\) 而非 size-biased 子代；同 \(W_1\) 的 size bias 下的递减 multiplier covariance 给
\[
\rho_0=\rho_1=1,\quad\rho_i>\rho_{i+1}>0\ (i\ge1),\quad\rho_i\to0,
\qquad v<v_p<h,
\tag{4}
\]
\(v_p\) 是 \(\beta_i\) 的标量参考商，不是另一 GW 律的速度。极限用 \(\lambda U<1\) 的 bounded convergence；严格性来自正概率的实际分枝。完整 inverse-square tilt 给 \(\inf\Psi>0\)。

同稿完整 child-pair 积分给 bounded、非负的熵函数
\[
g(x)=\frac{x(c+x)\log(1+c/x)}{\lambda c\log\lambda}-x/c,\quad g(0)=0,
\]
及 \(\delta_g=F_\lambda'(S)[\sum_i g(X_i)-g(S)]\ge0\)，在分枝上严格正。
\(\delta_g\le\lambda^{-1}(\max g+1/c)\nu\)，故有限均值足够可积。对 bounded continuous \(f\) 的 stationarity 给
\[
\mathbb E[g(I-\mathcal L)f]=\mathbb E[bf]-\mathbb E[\delta_g f(F_\lambda(S))].
\tag{5}
\]
这里没有把零点无界的 \(g'\) 交给上一节的 \(C^1\) 测试响应。令
\[
\alpha=\min(1,\Psi(0)/q_0(0))>0,\quad H_*=\Psi-\alpha q_0\ge0,
\]
由 (2)、(5) 得完整 floor
\[
D=F_*+2\mathbb E[\delta_g(\mathcal RH_*)(F_\lambda(S))]\ge F_*,
\quad F_*=2\alpha\mathbb E[br_0]-C+2\mathbb E[gH_*].
\tag{6}
\]
若 raw \(\Psi(0)/q_0(0)\ge1\)，含等号，则 \(J[(1+v)y-v]\ge0\)，并有精确 correction
\[
\lambda(2\mathbb E[br_0]-C)
=2\mathbb E[X(1-X)J((1+v)y-v)(X)]
+(1+v)\mathbb E[XY(1-X)(1-Y)/A^2]>0.
\tag{7}
\]
故 \(D>0\)。以后均为实际 hard \(0<\alpha<1\)，精确校准
\[
A_0=1-(\lambda+1)u+\lambda a_2>0,\quad
\alpha=(u-(v/c)A_0)/a_2>\lambda^2u,
\quad u<\lambda^{-2},\quad h<1/(\lambda+1).
\tag{8}
\]
不假设 general \(F_*\) 总是正；它由各区域引理分别支付。

## 5. 唯一实际 marker、修正 Mellin 与固定律 affine 信用（MARKER_CAL/FLOOR）

chosen-child indicator 比较给 \(A_m(t)\ge0\)。layer cake、\(\rho_i\to0\) 和正求和构造同一实际概率
\[
\sigma(dt)=A_m(t)dt/[h(1-t)^2],\quad
\rho_s=\mathbb E_\sigma[t^{s-1}(s-(s-1)t)],\quad
\Delta_i=i\mathbb E_\sigma[t^{i-1}(1-t)^2]>0.
\]
\(e=\Delta_1\)、\(\rho_2=1-e\)、\(\Delta_i\le ie\)。\(\sigma\) 来自同一 actual 律，不是自由标记。real-age transform 的微分与 Fatou 在 \(s=1\) 给
\(-\rho'(s)>(1-1/(2s))\Delta_s\)，无需 inverse escape moment。

令 \(r_s=\beta_{s+1}/\beta_s\)、\(r_s^-=\beta_s/\beta_{s-1}\)、\(\delta_s=a_sr_s-a_{s+1}\)、\(k=c/(\lambda\log\lambda)\)，
\[
\varepsilon_s=a_s-\lambda a_{s+1},\quad
\Theta_s=k\beta_s[-\rho'(s)],\quad
\bar\gamma_{s-1}=a_s(r_s-r_s^-)-\delta_s+
k(1-1/(2s))\delta_s/r_s.
\]
对校准二次 \(Q_\alpha(U)=-R_*+[1+(\lambda+1)R_*]U-(\alpha+\lambda R_*)U^2\)，\(R_*=v/c\)，令 \(t_n=\mathbb EU^nQ_\alpha(U)\)。\(t_0=0\)，单向上零点给 \(t_n>0\) 当 \(n\ge1\)。完整、正确的 floor 是
\[
F_{\rm floor}(R_*)=\sum_{s\ge1}s\lambda^{s-1}
\left[\frac{\varepsilon_sJ_{s-1}}{\lambda c}+2\bar\gamma_{s-1}t_{s-1}\right],
\]
\[
J_n=-2va_n+[c(1+2\alpha)+(3\lambda+1)v]a_{n+1}
-[c(\lambda+2\alpha)+\lambda(\lambda+1)v]a_{n+2}.
\tag{9}
\]
**首因子是 \(a_{n+1}-\lambda a_{n+2}\)**。冻结 V3 的旧索引不单独使用。Mellin errata 及 corrected English §§1–3 是明确呈现来源。全龄展开、索引平移和尾由 fixed \(\lambda>1\) 的多项式乘几何级数支配；
\[
F_*-F_{\rm floor}(R_*)
=2\sum_{s\ge2}s\lambda^{s-1}
[\Theta_s-k(1-1/(2s))\delta_s/r_s]t_{s-1}>0.
\tag{10}
\]

固定实际 \(\lambda,\pi\)，自由 scalar 速度 \(w\) 下使用 [assigned_polynomial_extension.md](assigned_polynomial_extension.md) 的 \(\widetilde F(w)\)，不是 natural \(C_{\rm pair}(w)\) 响应。其准确区别为
\[
C_{\rm pair}(w)-\mathbb E[bJP_c(w)]=(wZ-N)/\lambda;
\quad\widetilde F(v)=F_*;\quad-\widetilde F'(w)>0.
\tag{11}
\]
导数是固定实际矩的 affine 标量导数，不是沿树律的 \(\lambda\) 导数。

完整 calibrated-head 身份 (214)–(219) 给低偏置各区域共用的 master budget。令
\[
q=u/(1-u)=h/c,\quad w_i=\lambda^{i-1}\beta_i^2,
T_p=\sum_iw_i,\quad Z_p=2q-(\lambda+1)T_p>0,\quad R_p=T_p/Z_p,
\]
\(\alpha_p\) 为 \(\beta_2\) 上的 scalar 校准，\(\mathcal C=\alpha_p+\lambda R_p\)。完整尾 \(V_i>0\)、头 \(S_i=B_i-2V_i\) 和 Young 价 \(J_i\) 的精确定义在有效 FLOOR 正文中；**Young 两端均保留**。严格预算为
\[
F_{\rm floor}>
F_p+\sum_{i\ge1}\Delta_i\rho_iS_i
+e^2[V_1+2u^2\mathcal C/(\lambda(1-e))-W_2^Y/2]
+\sum_{i\ge2}\Delta_i^2J_i+C_{\rm cal}e.
\tag{12}
\]
首项 \(\rho_1=1\)，所以 (12) 的第一头项是 \(eS_1\)。另在 Q1 的正参考全和 \(A_i=w_i\beta_i^2\) 中，\(A_1=u^4\)，故减去首龄的准确量是 \(eA_1=eu^4\)，不是 \(eu\)。它与 \(eS_1\)、\(eB_1\) 或校准速度信用是不同项，不能互换。\(C_{\rm cal}\) 保持同实际 \(a_2\)、同 \(e\)。完整 fixed-moment 负斜率和 complete moment-profile speed deficit 给这项信用；二级来源只引用 (121)–(123)、(182)–(185)、(189)、(200b)、(206a) 的已证身份/尾，不引用其历史未证 universal SIZE。

校准及硬 gap 给
\[
0<e<E_{\rm hard}=(1-\alpha_p)/(1+\lambda R_p),\quad
\sqrt e<d/(q+1).
\tag{13}
\]
\(E_{\rm var}=d/(q+1)^2\) 是另一个方差 cap；不把它当实际 \(e\) 或 \(d^2/(q+1)^2\)。下文每项都用同 \(\sigma,e,\sqrt e\)，不独立优化根和价格。

## 6. 低偏置全部闭覆盖及每个完整区域付款

取 \(1<\lambda<\lambda_0:=2/\sqrt3\)，同时 \(\lambda<m\)。\(\lambda_0<6/5\) 与 \(\lambda_0-1<1/6\) 保证下列论文的闭代数域包含实际域。

**Q0。** 若 \(q\le1/15\)，则 \(u\le1/16\)。[low_u_selfcontained_manual_theorem_english_20261006_v2.md](low_u_selfcontained_manual_theorem_english_20261006_v2.md) 完整证明用 raw entropy cap、完整两类尾、32有理单元及4尾单元给 \(D>0\)。它也展开 \(Z_{\rm act}=2Q-(\lambda+1)T\) 的准确坐标。六个旧 guard 已在该自包含证明中支付。

**Q1。** 若 \(1/15<q\le3\)，则 \(q\in[1/29,3]\)。有效 Q1 三份完整证明依次支付同 \(\theta\) 的 Lambert 上界及全部 \(J_i>0\)、所有 \(i\ge2\) 的 \(S_i\ge-3w_i\beta_i^2/2\)、最后的完整同 \(e\) 预算。选择的是 `Q1KSTRUCTHAND...V3` 的九函数/新 Kcreditlo418，全字节对应固定 full-chain PASS；旧13904、旧K480和坏导出数组不成为 sign 前提。正 Hausdorff 头 Jensen 只能在正权重 cap 后使用。完整上价差、平方根余项、三个同 \(e\) 的 \(\theta\) 导数方向给
\[
F_{\rm floor}>u^2G\ge u^2\widehat H(e,\theta)
\ge u^2\widehat H(e,\theta_{\rm up})>0.
\]
低 q 用原三个线性函数的正乘积，高 q 用 \(a>0,J_{\rm pay}>0,K_{\rm pay}>0\) 的端点/单调性付款；\(q=2\)、\(e=0,E\)、二次系数为0均包含在完整正文与附录中。

**Q2。** 若 \(3<q\le10\)，使用八个独立已审 Q2 完整模块。原全龄 4/8 价格桥给 \([-S_i]_+\le4M_i\)、\([-J_i]_+\le8M_i\)。静态全龄 cap
\(dM_i\le(q/(q+i))^6\) 后，同一 marker 的正核 Jensen 和双 Jensen 才合法；两边完整求和后减准确首项。根侧保留 (12) 的 \(e\) 首项、Young 首端与校准速度信用。当前原首龄归一化给
\[
F_{\rm floor}/u^2>A_{\rm root}(e)-C(q,d,\sqrt e(q+1)/d)
>2/15-13/100=1/300.
\]
H0、平方H/角、平方V桥、完整head4、cost、root、年龄 \(\theta\) 桥和同e接合各有自己的固定回执；任一单独模块不是全 Q2 定理。

**Q3。** 若 \(q>10\)，共享 SOURCE/PRICE/AJ 三份最新完整证明只计一次。它们含原正分母、原全龄 shape 与一般 Faulhaber 二次价。共同实际预算
\(F_{\rm floor}>F_p-eH-e^2J_{\rm minus}\) 保持同 hard cap，所有尾由完整 shape/BV 支撑和跳跃误差支付。

* \(q\ge21\)：最新 A/B 全龄同e正文的 Q3a 给 \(F_{\rm floor}>1/5000\)。
* \(10<q<21,h\ge1/4\)：同正文 Q3b 保持同 \(h\) 的源、线性价和二次价，给 \(F_{\rm floor}>1/100\)。
* \(10<q<21,0<h<1/4\)：选择 `Q3REPLACEHAND...NO40706...CANDIDATE` 加 FZERO/actual-cap V2 和完整叶图，**该准确 candidate 正文已被固定新的 full-chain PASS 接受**。原 \(G\) 到 \(x_0\) 的 \(f_0\) 旁路、真实 \(W_x\to U\)、独立 H 与同原 \(h_0F\) 及真实 \(h\) 积分，给 \(F_{\rm floor}>1/40\)。旧40706、旧 N/M sign 或旧 whole-head PASS 不导入为新符号前提。

\(q=1/15\) 归 Q0，\(q=3\) 归 Q1，\(q=10\) 归 Q2，\(q=21\) 归 Q3a，\(h=1/4\) 归 Q3b，各自是已付闭端。由 (6)、(10) 及上述严格支付，低段全部 \(D>0\)。

## 7. 近偏置：actual CF、assigned 全龄与完整根（H_CF/H_P26）

取 \(\lambda_0\le\lambda\le\lambda_a:=707/500\)。实际 hard 中 (8) 成立。原 second-prefix 来自同实际 \(u,a_2\)，用原 finite-atanh \(K_{\rm cap}\)；最新 CF/P26 cap 完整正文给
\[
1<K_{\rm cap}<k_0<2/(1+\lambda u),\quad
v<w=V_2(K_{\rm cap})<h,\quad\lambda^2u<a(w)<\alpha<1.
\tag{14}
\]
其原 log 尾、公分母、全部17向量107槽、次数和四正因子均打印。它不使用 CF sign 或根 SIZE 证明分母/range。

actual 非线性三矩正文独立用同 root/children iid 的三核校准给
\[
\theta=a_3/a_2<1/(\lambda+1-\lambda z),\quad z=a_2/u.
\]
最新 legal-hard W 全域人工证明（\(u=5/8\) 分段，三个短预算全文）给
\(W=\lambda D_f-uR(\lambda+1-\lambda z)>0\)。准确入口由 CF scope V3 原式给
\[
\Delta^{\rm ass}_2/a_2>
\frac{(1-z)W}{(\lambda+1-\lambda z)zD_w}>0.
\tag{15}
\]
校准 \(Q_a\) 减 \((1-a)U\) 的凹二次唯一向上零点将 (15) 传播到每个 \(s\ge2\)。**这是入口后传播**，不反过来证明入口。actual nonlinear M 与 W 仅取代实际 H 所需路径；旧更广自由 Gram/envelope 的两块9744仍保存。

P26 全龄纯引理用有限几何和给
\[
e_s+(1-\lambda^2u)(C_s-1)>0\quad(s\ge2),\qquad
C_s=k(1-1/(2s))/r_s.
\]
其完整 absorption 身份、(15) 及 marker 下界给
\[
\widetilde F(w)>
\mathrm{Root}+\sum_{s\ge2}s\lambda^{s-1}a_s^2B_s
+2\sum_{s\ge2}s\lambda^{s-1}a_sL_s\Delta_s^{\rm ass}.
\tag{16}
\]
\(B_s,L_s>0\)。root 独立保留；\(\Delta^{\rm ass}_1=-(1-a)u<0\) 与 \(\Delta^{\rm marker}_1=e>0\) 是不同对象，不能互换。288龄枚举退出当前吸收 sign，cap 四因子不退出。

## 8. 近偏置全部 root SIZE：小 u 与大 u

**\(0<u\le1/2\)。** 同一 actual marker 的 Jensen 下 profile
\[
T=1-\sqrt{1-\rho_2},\quad f_s=T^{s-1}[s-(s-1)T],\quad
a_s\ge\beta_sf_s,
\]
且 \(a_2=\beta_2f_2\) **精确相等**。在 (16) 中先用 \(\Delta^{\rm ass}_s>0\)、\(B_s>0\) 删除 \(s\ge5\) 的正项；对前三龄先用真实括号的 \(\max(0,M_s)\)，再可放松到完整 signed \(M_s\)。因此即使 \(M_s<0\)，仍有正确下界，不能直接对负括号代换 \(a_s^2\)。完整清分母后得到原
\[
\Phi(K)=\rho\,d_K S_4(K)/u^2,\quad\rho=T(2-T),\quad0<T\le1.
\]
这里 \(d_K\) 是原价格分母，和 \(1-h\) 不混名。全 T 仿射身份从完整 root、全部 \(s=2,3,4\) 原式给 \(\partial_K\Phi<0\)，\(d_K(K_b)>0\)，所以
\(\Phi(K_{\rm cap})>\Phi(K_b)\)。\(K_b\) 不被声称为另一合法 hard 校准。

当前四块完整原 \(\Phi(K_b)\) 支付为
\[
\begin{array}{c|c}
0<\rho\le1/2&A(1-u)/40\\
1/2\le\rho\le2/3&A(1-u)/200\\
2/3\le\rho\le3/4&1/8\\
3/4\le\rho\le5/6&1/100
\end{array}
\]
表的右列都是严格下界。第二块先给 \(U_3\rho-V_4>0\) 的共同 D profile；最新 RHO34 全源和 RHO56 g/F56/shared-D 全源正文明确使用它的 \(\rho\in[1/2,1]\) 域，而不是把第二块整个 \(\Phi\) 结论域外推。RHO34 的 \(\eta,A\eta\) 是 \(\rho\)-无关出口，再向 RHO56 传递；箭头全向前。

**\(5/6\le\rho\le1\)。** 先独立证明 \(p=\Phi(K_b;T=1)>1/1000\)，两端原严格余量分别 \(181/176400\)、\(541757/470400000\)。它不从 J1 或 all-T 正性反推。完整 signed-core/quartic 正文保留同 \(\lambda,u,K_b\) 的所有价格，给
\[
\Phi\ge p+C_0x^2+bx^3+(K_a+j)x^4,\quad x=1-T\le1/\sqrt6.
\]
J1 最新完整正文以原 moving poles、同参数七系数、全 \(u\) 严格凹性和两条边界证明取代六 Taylor 矩形；给 \((25p+C_0)/(kA)>57/100\)。最新 J2 original-source V2 和最新完整 J3 分别给剩余两耦合预算。三者合成
\(25p+C_0\ge0\)、\(4b+3C_0\ge0\)、\(K_a+j+4C_0\ge0\)。故
\[
\Phi\ge p+C_0g(x),\quad g=x^2-3x^3/4-4x^4,
\quad0\le g<1/25,\quad1-25g\ge37639/640000.
\]
若 \(C_0\ge0\)，\(\Phi\ge p\)；否则 \(-C_0\le25p\)，因此全片
\(\Phi>37639/640000000>0\)。末零点导数是 \(f'(0)=0\)；J3 的 \(y=0\) 末行用 \(\le\)，严格最终付款来自其它正余量，不从零点假设严格导数。所有 \(\rho\) 接点闭域重叠，完整9600的当前实际调用已经由这些完整局部证明替代；旧更广 \([23/20,3/2]\) 自由盒不被重新宣称证明。

**\(u>1/2\)。** 高u五个最新局部完整正文先独立排除 \(\lambda\ge11/8\) 的 actual hard；余域保留同 \(K_{\rm cap}\) 的原 root+完整二龄。正分母使 \(H_2\) 与 \(N\) 同号；\(N'''>0\)、\(N'(1)<0\) 排除内部最小，两个完整端点均严格正。故
\[
D\ge F_*>\widetilde F(w)>u^2H_2>0.
\]
等号 \(u=1/2\) 归小u；\(u=\lambda^{-2}\) 不属于 actual hard。完整5076仅在当前 actual 调用中被替代，不能把五个 SIZE 正文当作 CF/cap/absorption 的逆向证明。

## 9. 中段的更短完整接合与高偏置完整尾

**\(\lambda_a\le\lambda\le\lambda_b\)。** 本轮新增完整 [I-free middle response composition](CHAIN45HAND_CONTINUATION_I_FREE_MIDDLE_RESPONSE_COMPOSITION_COMPLETE_PROOF_LOCAL_20261008.md) 逐步证明：\(\eta(f)=\mathbb E[b\mathcal Rf]\ge\max(g,b)\pi\)，high-k1 对 \(x\ge1/(\lambda+1)\) 严格正，最新 hybrid 两积分对低 x 严格正。三个进口都只要求 actual \(h<1/(\lambda+1)\)，没有 \(I<0\)。因此该段直接 \(D>0\)，省去原 \(I\) 分支。\(H_I\) 的已证 \(I\ge0\) 条件定理仍在45宏账中接受为备用，当前充分证明不用它。两 x 区在等号闭接，\(g=b\) 而核仍严格正。\(g/b\) 可无界，但 \(\max(g,b)\Psi-bJP_c\) 有界，完整响应可积性没有缺口。

**\(\lambda_b\le\lambda<m\)。** 选择 latest coarse DISPLAY_V3 的完整原63块支付证明。非调和实际域 \(s=h/c<9/25\)、\(r=a_2/\beta_2\in(0,1)\)。完整无限矩尾给 \(T\le\bar T\)、\(Q\ge\lambda T+D_0\) 及速度上界。\(39/20\le\lambda<2\) 的两个真实 r 端点支付 \(D_0>\bar T\)，从而 \(c-(\lambda+1)v>0\)；\(\lambda\ge2\) 用 \(v<h\) 给同条件。

修正后的 full signed renewal 为
\[
D=\lambda^{-1}\int w_{\rm resp}(t)B(t)\,d\xi(t),\quad
I=\int B(t)\,d\xi(t),\quad
\xi(dt)=te^{-ct}f(\varphi(t))dt.
\]
\(w_{\rm resp}>0\) 有界递减；原完整 source \(B\) 递减。双截断、有限均值 root 可积性和 Chebyshev 给
\[
D\ge\lambda^{-1}\frac{\int w_{\rm resp}d\xi}{\int d\xi}I.
\]
**正因子 \(1/\lambda\) 保留**。真实根的 unary 参与率 \(p\) 位于 \([0,z_H/z]\)，仿射下界只在这两个端点评估；两个端点 \(F_0(v),F_1(v)\) 对 v 再取 \([0,V]\) 两端，全部分母在实际域正。新63行含59正块4零块，所有原普通系数、支付整数、原乘积和四完整尾均打印，给 \(F_0(V),F_1(V)>0\)，故 \(I>0,D>0\)。扩大 \(c,s,r\) 盒只证分子，不能在其中声称实际分母都正。旧511证书不再额外导入。

## 10. 有效 DAG、二级来源闭包与没有被证明的旁路

原45宏目录的 literal `SPEED` 祖先为44个，独立 NEW_JENSEN 只通过注释窄接 Q1/Q2。本轮有效图明确加这两条窄边；其通用全龄 Jensen不接 signed 核，不代替头价、S11、root 或 cost。新中段实际证明再去 \(H_I\to H_{\rm MIDDLE}\)，保留 \(H_I\) 为已审备用。因此更新有效充分路线为44个可达宏节点，另一个为已审备用；这不是45个不可约原子引理，也不是只需44次数值比较。

三个容易形成假循环的地方在正文中严格先后：

1. CF cap/range 在非线性 CF 入口和 SIZE 前建立；\(\Delta_2>0\) 先建立再传播、删除正龄。
2. T1 独立锚先于 J123/quartic，J1 不推出 p 正；rho2 shared-D 与 rho3 rho-free出口向后传，未借下游最终正性。
3. high-k1 的先行四矩尾包络 → hybrid s凹性 → 两次完整积分端点 → 低x signed 正性 → 完整 D。不能拿旧整个 hybrid PASS 证明新曲率或新端点。

必须补固定的二级短证明包括 actual 非线性三矩、highu五正文、quartic两正文、校准负斜率/全矩 loss/全 tail 子引理及 rational Rg/min-j/max-source 接合。它们都是必要已证部分的最新有效呈现；旧 universal223、general canonical S42、低bias blanket hybrid 以及 (5) 以外的更强零点导数/variance SIZE，仍分别是未证或被反例排除的旁路。没有把它们设为前提。

本轮没有发现当前足够路径中的新数学反例或待证 sign；修复了 source-closure 展示不完整，并给出了实际省去 I 分支的新接合。若某读者尚未核完 F 层的整数身份，准确状态是“有限算术证明公开且内部独审承接；该读者尚未逐项完成核验”，不能由此把程序输出叫真人证明，也不能误称已证解析结论重新 OPEN。

## 11. 主定理与完整结尾

**定理（当前严格可陈述范围）。** 在第1节固定普通无叶 GW 模型、\(\mu(1)>0\)、仅有限均值 \(1<m<\infty\) 下，actual deterministic speed
\[
v_\mu\in C^1((1,m)),\qquad v_\mu'(\lambda)<0\quad(1<\lambda<m).
\]
所以任意 \(1<\lambda_1<\lambda_2<m\) 都有 \(v_\mu(\lambda_1)>v_\mu(\lambda_2)\)。证明依赖第2节明列的概率定理进口和本轮有效来源账锁定的完整已审局部有限数学证明。

**证明。** 固定 \(\lambda\in(1,m)\)。raw alpha 分支用 (7) 给 \(D>0\)；actual hard 用 (8)。在 \((1,\lambda_0)\) 第6节五个 q/h区域全覆盖；在 \([\lambda_0,\lambda_a]\) 第7–8节两 u区全覆盖；在 \([\lambda_a,\lambda_b]\) 第9节两 x核全覆盖；在 \([\lambda_b,m)\) 第9节完整尾/root给 \(D>0\)。邻段均含相关端点，任何 \(m\) 以下的截断不留下空隙。第3节 \(Z_{\rm act}>0\)、实际 \(C^1\) 及 (3) 给严格负导数。对 \([\lambda_1,\lambda_2]\subset(1,m)\) 用中值定理得到严格两偏置比较。无需 \(\lambda\downarrow1\) 或 \(\lambda\uparrow m\) 的一致估计。\(\square\)

这个证明合集尚无外部真人审稿、形式化认证或原全 \((0,m)\) 问题的 verifier PASS。没有新颖性主张；跨 \(\lambda=1\)、端点与 \(\mu(1)=0\) 均未在本轮处理。完整有限算术规模与独立 AI 审查限度必须和定理一起读，不能把“数学闭合”缩写为“几行纯手算已证明”。

## statement

以下逐字保留原 `agents/generation/data/mono.md` 的完整非形式问题陈述，以区分它与本轮只处理的上于一范围；本节不是对原全域的证明声明。

Let \(\nu\) be the offspring distribution of a Galton–Watson tree and assume

\[
m_1:=\min\{k:\mathbb P(\nu=k)>0\}= 1,
\qquad
m:=\mathbb E\nu \in (1,\infty).
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

Prove the Lyons--Pemantle--Peres monotonicity conjecture: $v$ is monotone decreasing function on $(0,m)$.
