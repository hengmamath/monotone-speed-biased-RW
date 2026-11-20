# 5076局部末端证书替换：整合证明、依赖与成本（V2）

2026-10-06。原5076上端及完整装配已独立PASS；本V2另加入同一辅助最终PASS的全龄短引理和原P26摘录接口。本文件新增，不覆盖V1或任何冻结证明、程序、manifest、ZIP。未重跑已审源或旧证书，未开启新数学目标，未创建代理/任务。

## 1. 精确结论与替换对象

原设定：μ0=0、μ1>0、仅有限均值m>1，普通GW根同μ，父边权λ、子边1、根均匀子；只使用实际terminal-one canonical逃逸。对

 2/√3≤λ≤707/500，λ<m，u=E[X/(λ−1+X)]>1/2，

新的末端付款链证明Dλ>0，从而v′μ(λ)=−Dλ/Zspeed<0。

原V1退出的逻辑必需执行依赖是P16/L15 child8：

 high_u_original_root_s2.py，旧末端张量degree(46,17,5)、5076项严格正。

旧文件4041 bytes，SHA256 ad808a2ce76a83f55cdbc264b53653301d0d150cdac7d3822de5baa70955d9e6。
文件与旧日志不删除、不覆盖。新的证明用人工可明核的scalar SIZE论证取代其最终正性结论，不以该5076结论证明任何新引理。

P17/L15 child7 high_u_original_root_s2_identities.py只核五个原式/清分母身份，可保留为历史一致性旁证；不再需要其旧P/D构造来证明SIZE。原root+二龄解析接口(93)--(95)仍保留。原P13 general_two_over_sqrt3_certificates.py及外层runner也冻结不改；它们历史重放会继续调用P16，本V2仍是新逻辑装配覆盖层，旧runner不改。

本V2另以第8节纯数学引理取代P26/L15 child2中第11--30行的288 head sign及旧s≥8 tail输入。P26完整文件2538 bytes，SHA256 e691e1c2e400cf15baf820fa67ed6ecc44c3916f6747f689a936dd69327b93bf；它及P13历史调用保留，cap四因素、校准和完整吸收/Lambda身份保留。旧H=λ²P_s/c²是正因子转换，六龄4(2s+3)合288。辅助审核的是传回冻结摘录，未重跑旧循环或独立读取全部Mac字节；SHA由本地主任务核对两旧manifest。

这不撤整个high_lambda/H或highbias模块。仍保留Condition-F、marker实际输入、u≤1/2的9600及λ≥707/500旧分支。整体仍是计算辅助证明；本覆盖层人工化5076末端SIZE与全龄吸收符号。

## 2. 必须保留的上游合同

| 合同 | 本装配所用结论 | 现有来源/检查器 |
|---|---|---|
| canonical与速度定理 | λ<m时实际逃逸正；严格实际矩cap与b>u²；普通根/人工父速度一致；Zspeed>0 | response_interface.md 的外部入口；canonical_entropy.md。外部概率定理原证明未由本项目重审 |
| finite-mean完整响应 | v为C1；v′=−D/Z；正resolvent与完整entropy remainder给D≥F* | response_interface.md、canonical_entropy.md、scaled_r0_mellin_payment.md；使用完整后代响应，不能截第一分枝 |
| α分支与Mellin根恒等式 | α=min(1,raw)>0；α=1严格D>0；hard为0<α<1，t0=0，α=(u−vA0/c)/b；F*完整根+龄展开 | scaled_r0_mellin_payment.md、condition_F_root_payment.md及英文20261005_corrected；正式errata有效。首因子是a_(n+1)−λa_(n+2)，s=n+1 |
| 固定实际law的assigned延伸 | Ftilde(v*)=F*；Cpair−Ctilde=(vZ−N)/λ；沿a(v)的Ftilde严格减。只assigned标量，不assigned树law/D | assigned_polynomial_extension.md/.py，P02保留；正确a=[u−wA0/c]/b，无额外u |
| second-prefix cap与range | 同一实际u,b的v<V2(κ)<V2(K)=w<h；κ<K；1<K<2/(1+λu)，分母正；λ²u<a_bar<α<1 | condition_F_global_gram_payment.md的解析Gram/Euler/prefix部分；root_canonical_profile_payment.md §3及P26的四cap因素。range域23/20≤λ≤3/2、u≤λ^−2覆盖本域 |
| Condition-F/J2与assigned缺陷 | hard使h<1/(λ+1)；精确J2(K,e)>0给assignedΔ2>0；向上零点论证给全部Δ_s≥0（s≥2） | condition_F_global_gram_payment.md；P06 condition_F_global_gram_certificate.py及P07 condition_F_joint_prefix_identities.py保留，exact_qsqrt3.py支持。仍依赖两块各9744项Q(√3)张量 |
| 全龄吸收 | 第8节一条人工引理给全部s≥2严格吸收；root独立保留，丢掉s≥3仅在Δ_s≥0及正括号成立后 | P26_ALL_AGE_ABSORPTION_PURE_LEMMA_20261006_V1.md及两最终PASS回执；原marker下界和root_canonical_profile_payment.md §1吸收/Lambda身份保留。288 sign和旧age-tail退出新逻辑依赖，P26文件/cap不退出 |
| 原root+二龄下界 | 实际a2=b EXACT；a3/b<r2及a_bar+λw/c>0给Δ2/b>M2；D≥F*>Ftilde(w)>u²H2 | high_u_original_root_s2_result.md的(93)--(95)保留。此合同不使用旧5076末端正性，也不需要marker/Jensen高矩profile |

不调用旧错误38998、S3/S4 sign，不把自由marker或自由边际宣称canonical。当前区域无需旧I源曲率/one-crossing分支；λ≥707/500模块自己的既有依赖不在本替换范围。相邻cap/实际矩形状、Condition-F和full-age是实质保留项，不能把新N端点正性反过来当作它们的证明。

## 3. 统一符号及闭覆盖

hard点令c=λ−1，t=1−u，b=a2，

 A=1+λt，B=1+λ(λ+1)t，k=1−λu，ρ=bA/u，z=ρ/A。

actual必要范围为1/2<u<λ^−2、uA<ρ<1、k>0。scalar闭覆盖uA≤ρ≤1只用来证明原有理H2正，不当作实际law。实际assigneda_bar仍<1；scalar路径上a≥1的点不代入原吸收合同。

用同一精确Kcap、E=(K−t)/t，

 g=c/(λ+1)，ℓL=2(g+g³/3+g⁵/5)，
 ℓU=ℓL+2g⁷/[7(1−g²)]，
 K=c/(λℓL)+t/2+ℓU(2λt−c)t/(12c)，
 T2=u²(1+Eρ²)，Q2=u+λu²z+Au²z²/t，
 w=cT2/[2Q2−(λ+1)T2]，a=[u−w(1−(λ+1)u+λb)/c]/b。

原H2为Root/u²加完整二龄项：

 H2=[(1+w)(1−λz)²−2(1−a)(1−λz)]/λ
       +2λz²[B2+2L2M2]，
 B2=(1+w)(1−λr2)²/λ+2(1−a)(r2−r1)，
 M2=a(1−r2)+(w/c)(λ+1−λr2−1/z)，
 r1=1/A，r2=A/B，L2=1/λ−1/A。

设Dρ=2−(λ+1)u+(2λu/A)ρ+[2u/(At)−(λ+1)uE]ρ²，N=ρDρH2。注意N及Dρ是局部标量，与实际响应Dλ、speed分母Zspeed区别。用G=1+λu、E+=(2/G−t)/t，

 Dρ−t(1+Eρ²)=(1−ρ)[k(1+ρ)+(2λu/A)ρ]+G(E+−E)ρ²>0。

故scalar全路径Dρ>0、0<w<h，无循环，N与H2同号。

## 4. 新SIZE证明的完整逻辑组合

以下各引理与完整源、审计回执都在本目录；这里汇总合同，不复制已审系数目录。

1. 右侧排除：a_ρ<0的无循环身份a+λw/c=[1+(w/c)(λ+1−1/u)]/z>0；actual hard要求K>2λ/(λ+1)。u>1/2时K<25(λ+1)/(48λ)+1/4，而λ≥11/8令此上界<2λ/(λ+1)，差由59(λ−11/8)²+(401/4)(λ−11/8)+83/64>0支付。因此11/8≤λ≤707/500实际hard不存在，归α=1合同。
   来源high_u_5076_prefix_geometry_20261006_v2.md；仅右侧逻辑需要路径符号，不用Hv负或自由K反例作为付款。
2. 余域2/√3≤λ≤11/8：N=Σ_{j=0}^5n_jρ^j，N'''>0。证明n4,n5>0，再用R双单调及三个u区间支付曲率下界。来源high_u_5076_rho_derivative_convexity_20261006.md。
3. 同余域N′(1)<0：N′(1)对E仿射；两端自然清分母分别得到Fm,Fp，正性由(k−1/4)²+20k³及90(k+1/5)(k−1/12)²+11k/40支付。因此N′严格凸的非正集包含右端，无内部最小点，minN=min{N(uA),N(1)}。来源high_u_5076_right_derivative_sign_20261006.md。E包络只用于导数，不替换付款预算。
4. 下端：N(uA)=uA[(D0−tT̂0)H0+tT̂0Hh]，权正且H0>0。Hh下界化为五系数一变量四次式，正下界18(k+1/9)(k−1/8)²+11k/160+7/160支付。w=0,h仅代数端值，无actualhard假设。来源high_u_5076_lower_endpoint_payment_20261006.md。
5. 上端：保留exactKcap。粗有限级数界给K<Kb=(λ+1)/(2λ)+t/2+(λ+1)(2λt−c)t/(24λ)。已审N(1)=2kS(K)/(λA²t)，S=P−δQ、Q>0，故S(K)>S(Kb)。24λ²AB²S(Kb)分成A0+B1k+A2k²+A3k³+Σ_{j=4}^7Pjk[2^(1−j)−k^(j−1)]八项；三个低次三次值及正余项给全盒严格正。来源high_u_5076_upper_endpoint_payment_20261006.md。

故hard余域N>0⇒H2>0⇒Dλ≥F*>Ftilde(w)>u²H2>0。右侧α=1连接，得到本文件第1节全部u>1/2结论。所有新引理及最后无循环装配均已收到同一辅助PASS。没有将scalar端点law化，也没有用新SIZE结论证明上游F/κ/assigned/吸收。

## 5. 边界归属与适用域对齐

| 边界 | 归属/理由 |
|---|---|
| λ=2/√3 | 新余域引理闭端包括；Condition-F精确Q(√3)证书也闭端包括；23/20<2/√3保证cap域；第8节吸收引理只需λ>1 |
| λ=11/8 | 新scalar引理闭端包括，但actualhard已由右侧排除；实际证明取α=1，无空隙/循环 |
| λ=707/500 | 右侧排除仍有效；同时与旧≥707/500模块重叠，不撤后者 |
| u=1/2 | 新actual定理严格u>1/2；等号归旧u≤1/2、9600 checker，不撤它。部分新scalar闭端计算可包括等号，不据此扩张本文替换域 |
| u=λ^−2 | actualhard不存在：λ²u<α<1。仅旧/新closed scalar上界可用于比较，不当成actual点 |
| ρ=uA、1 | 新N正性在两端成立，actualρ在开区间；ρ=0、t=0等奇异点不评原分式 |
| α=1 | 单独原人工响应证明，包括raw等号；不使用hard除式 |
| λ=1、m | 不包括；本替换没有跨1声明 |

五个域对齐有理核验：1600>1587（23/20<2/√3），363>256（2/√3<11/8），5656>5500（11/8<707/500），499849<500000（707/500<√2），707<750（707/500<3/2）。因此1/2<u<λ^−2≤3/4、1/4≤t<1/2、0<k<1/2全部合法。

## 6. 人工成本：明确区分新付款与保留计算

计数规则：一个终端有理大小/正负比较算一次；同一源码assert内的and拆计；纯恒等式、域推理、逐字正系数读数不混入比较数；不把两个可选指定纤维检查算作一般证明。

| 新局部付款步骤 | 自然系数/因子 | 核心固定有理比较次数 |
|---|---|---:|
| N''' | 六个n_j自然ρ系数；一个n5比较及三u区间，不是参数扫描 | 8 |
| N′(1) | Fm八个、Fp九个自然k系数，共17；其中108个显式整数c系数条目（48+60），另m0,p0为解析式；两个平方恒等式 | 10 |
| N(uA) | 一个五系数四次式与一个平方分解 | 4 |
| N(1) | 八个因子组；若展开原分母清除的λ,k分子为54单项式，仅三固定低次三次值需比较 | 7 |
| 小计 | 36个核心自然系数/因子组，不是36个数；有108整数条目等实际代数核验负担 | 29 |

另需右侧排除的三项正二次系数59、401/4、83/64，以及上表五个边界对齐比较，共8个简单有理比较；合计37次（其中核心29次）。旧cap的四因素及F的19488个Q(√3)系数仍是保留上游，不能记作新人工付款成本或说已消除。全龄288 sign和旧s≥8 tail已由第8节替代；该引理是几何和身份及正性推理，无年龄/参数/系数枚举，generic代码不是必要正性证书。下端附带上端两正项解释的967/2000 guard及两指定纤维点均非本最短付款链依赖。

通用身份核验也必须读：assigned正确根校准与二龄抵消、六ρ系数桥、两E端分母、下端正权和H0/Hh、上端N1与八因子桥。现有四新局部源全部native optimize=0并有exit0日志，已独立PASS；本整合不重新执行它们。这是一组数页的人工可审局部替换，未称为一行优美证明，也未称整个高bias或全λ速度定理纯人工化。

## 7. 版本与保留状态

权威Mellin呈现仍是speed_monotonicity_english_proof_20261005_corrected.md及mellin_index_errata_and_dependency_impact_20261005.md。旧V3不覆盖、不能无勘误引用；本覆盖层不改其ZIP/manifest。

原5076最后上端/装配回执为audit_receipt_high_u_5076_upper_and_assembly_20261006.md。新全龄数学及文件摘录对接回执分别为audit_receipt_p26_all_age_short_lemma_math_20261006.md、audit_receipt_p26_original_excerpt_and_replacement_20261006.md。原真实摘录、准确行域及保留接口另存；它们不宣称辅助重新读取全部Mac原字节或执行旧循环。

既有全部1<λ<m严格递减计算辅助定理保持；跨1未处理，无外部peer review/新颖性声明。Condition-F V13冻结、其truequadratic补充PASS，但全域付款仍未闭合，两9744保留。9600、S42和其他区域的状态原样保持。

## 8. 核心新增人工引理：全部年龄严格吸收

本节局部使用τ=λ²u；第3节的t=1−u不变，原Mellin校准t_0也不变。

**引理。** 设 \(\lambda>1\)，\(0\le u\le\lambda^{-2}\)，整数 \(s\ge2\)。记
\[
c=\lambda-1,\quad \tau=\lambda^2u,\quad\omega=1-\lambda u,
\quad N_j=\lambda^j(1-u)-1+\lambda u,
\quad r_s=N_s/N_{s+1},\quad e_s=1-\lambda r_s.
\]
则
\[
e_s+(1-\tau)\left[\frac{2s-1}{s(\lambda+1)r_s}-1\right]>0.
\]
因而对 \(C_s=c(1-1/(2s))/(\lambda\log\lambda\,r_s)\)，亦有
\[
e_s+(1-\lambda^2u)(C_s-1)>0.
\]

**证明。** \(\omega\ge c/\lambda>0\)，而 \(N_1=c\)、\(N_{j+1}=\lambda N_j+c\omega\)，故各分母正。令 \(S_s=\sum_{j=0}^s\lambda^j\)。有
\[
e_s=\frac{c\omega}{N_{s+1}}\ge\frac{1-\tau}{S_s},
\qquad\frac1{r_s}=\lambda+\frac{c\omega}{N_s}>\lambda,
\]
第一式使用 \(\omega\ge1-\tau\) 及 \(N_{s+1}\le\lambda^{s+1}-1=cS_s\)。当 \(\tau<1\)，引理左侧严格大于
\[
\frac{(1-\tau)\{s(\lambda+1)-[s-(s-1)\lambda]S_s\}}
{s(\lambda+1)S_s}>0,
\]
因为有限几何和差分给出
\[
s(\lambda+1)-[s-(s-1)\lambda]S_s
=\lambda\left[(s-1)+c\sum_{j=1}^{s-1}j\lambda^j\right]>0.
\]
当 \(\tau=1\)，左侧为 \(e_s>0\)。最后，严格凸 \(1/x\) 的梯形上界给 \(\log\lambda<c(\lambda+1)/(2\lambda)\)，故 \(C_s>(2s-1)/(s(\lambda+1)r_s)\)，第二个结论随之成立。\(\square\)

**Canonical 吸收推论。** 沿实际或合法 assigned hard 合同，设 \(0<a<1\)、\(a>\lambda^2u\)、\(v>0\)，并沿原实际 marker 身份记 \(\delta_s=a_sr_s-a_{s+1}>0\)、\(\xi_s=\Theta_s-C_s\delta_s>0\)。上述引理给
\[
T_s=(1+v)e_s+(1-a)(C_s-1)>0\qquad(s\ge2):
\]
\(C_s\ge1\) 时显然；否则用 \(1-a<1-\tau\)。于是原完整恒等式
\[
\begin{aligned}
\frac{(1+v)\epsilon_s^2}{\lambda}+2(1-a)a_s\gamma_{s-1}
&=a_s^2B_s+2a_s\delta_sT_s+(1+v)\lambda\delta_s^2
 +2(1-a)a_s\xi_s\\
&>a_s^2B_s,
\end{aligned}
\]
其中 \(\epsilon_s=a_s-\lambda a_{s+1}\)、\(B_s=(1+v)e_s^2/\lambda+2(1-a)(r_s-r_{s-1})>0\)。此推论只用于 \(s\ge2\)。根项
\[
R=\frac{(1+v)\epsilon_1^2-2(1-a)u\epsilon_1}{\lambda}
\]
单独保留；校准 \(t_0=0\) 给 \(\Delta_1=-(1-a)u<0\)，不可按非负缺陷删除。

profile比值的严格递增可直接核见
\[
r_s-r_{s-1}=\frac{c\omega(N_s-N_{s-1})}{N_sN_{s+1}}>0,
\]
因而上式B_s>0无需新增系数检查。实际marker严格下界仍为独立上游，未由本纯profile引理替代。
