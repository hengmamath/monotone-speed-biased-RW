# 完整价格：低 rho 半区的人工付款

2026-10-06。唯一完整小 u / 全 T 目标；新增连续区域证明，LOCAL，待父任务复用同一辅助。没有网格、大表、系数扫描或旧证书执行。上一全 T K 仿射接口独立 PASS 保持；9600 不作整体退出。

## 精确结论

保留原完整 root、s=2,3,4、共同 rho=T(2−T)、f_s 和正确 assigned 校准。原目标 lambda∈[2/sqrt3,707/500]、0<u≤1/2 的标量覆盖中，对
\[
0<\rho\le1/2\quad(0<T\le1-1/\sqrt2)
\]
证明紧凑幂下界及完整预算
\[
\boxed{\mathcal V(\rho)>A(1-u)/40>0,\qquad
\Phi(K_{cap})>\Phi(K_b)\ge\mathcal V(\rho).}
\]
这里 Phi=rho*d*S4/u²。新区域是原全 T 标量覆盖的连续区域，未声称其中有实际 canonical hard law。证明本身在更宽 1<lambda≤3/2、0<u≤1/2 成立；不扩大速度定理的人工范围或原 CF 合同。

令 t=1−u、k=1−lambda*u、Z_s=t sum_(j=0..s−1)lambda^j+u、A=Z2=lambda+k，r_s=Z_s/Z_(s+1)、L_s=1/lambda−r_(s−1)、W_s=s lambda^(s−1)/Z_s²。原短价格
\[
K_b=(\lambda+1)/(2\lambda)+t/2+(\lambda+1)(2\lambda t-\lambda+1)t/(24\lambda),
\]
\[
R=t+\rho^2(K_b-t),\quad Q=At+\lambda u\rho t+u\rho^2,
\quad E=1-\lambda\rho/A.
\]
原紧凑完整根为
\[
\Phi_R=\frac{2E}{\lambda}
\{Q(2A-\rho-\lambda\rho^2/A)-AR(A-\lambda u\rho^2/A)\}.
\]
幂下界只需记成
\[
\mathcal V=\Phi_R+2\rho\sum_{s=2}^4
 [U_s\rho^{s(s-1)}-V_s\rho^{s-1}],
\quad U_s>0,\quad V_s=uAR H_s,
\]
\[
H_s=W_sL_s/r_{s-1}
=s\lambda^{s-2}k/(Z_s^2Z_{s-1}).
\]
这些是完整年龄正平方和负前矩价格；全和原样保留后，可仅删除正平方取得下界。

## 三个全部负价格的常数

证明
\[
H_2\le1/2,\qquad H_3\le1/4,\qquad H_4\le4/25.
\]
始终有 0<k<1、A≥1+k 及 A≥2−k，后一条由 u≤1/2 得到。
H2=2k/A²≤2k/(1+k)²≤1/2，最后等价于 (1−k)²≥0。

写 B=Z3=lambda*A+k，C=Z4=lambda²*A+(lambda+1)k。
\[
B^2-\lambda(A+k)^2=(\lambda-1)(\lambda A^2-k^2)>0,
\quad C-\lambda(A+2k)=(\lambda-1)(\lambda A-k)>0,
\quad B>A+k.
\]
因而 H3≤3k/[(A+k)²A]、H4≤4k/[(A+2k)²(A+k)]。
当 k≤1/2，用 A≥2−k 得
\[
H_3\le3k/[4(2-k)]\le1/4,
\qquad H_4\le2k/(2+k)^2\le4/25,
\]
两分式在该区间递增。
当 k≥1/2，用 A≥1+k；以下两固定因子证明所需比较：
\[
(1+2k)^2(1+k)-12k=(2k-1)(2k^2+5k-1)\ge0,
\]
\[
(1+3k)^2(1+2k)-25k=(2k-1)(9k^2+15k-1)\ge0.
\]
故三个 H_s 界全部成立，无参数枚举。

## Kb/t 和根下界

由
\[
K_b/t=(\lambda+1)/(2\lambda t)+1/2
 +(\lambda+1)(2\lambda t-\lambda+1)/(24\lambda)
\]
可见其 t 导数为 (lambda+1)[1/12−1/(2lambda*t²)]<0。所以
\[
K_b/t\le(37\lambda+25)/(24\lambda)\le31/12,
\quad R/t\le1+(19/12)\rho^2\le67/48.
\]
在 rho≤1/2，2A−rho−lambda*rho²/A>0，Q≥At，且 E>0。保留完整根后删除其一个正项，得到
\[
\frac{\Phi_R}{At}\ge\frac2\lambda E
 [A(2-R/t)-\rho-\lambda\rho^2/A]
\ge\frac2\lambda g(A,\rho),
\]
\[
g(A,\rho)=\frac{29}{48}(A-\lambda\rho)-\rho
 +\frac{\lambda^2\rho^3}{A^2}.
\]
第二步使用一般恒等式 E(AD−rho−lambda*rho²/A)=D(A−lambda*rho)−rho+lambda²rho³/A²，以及 2−R/t≥29/48。
g 在 rho≤1/2 严格递减，因为
\[
g_\rho=-29\lambda/48-1+3\lambda^2\rho^2/A^2<0
\]
（lambda/A<1）。所以 g(A,rho)≥g(A,1/2)。后者在 A≥1+lambda/2 严格递增，因为
\[
g_A(A,1/2)=29/48-\lambda^2/(4A^3)>29/48-1/4>0.
\]
于是
\[
\frac{\Phi_R}{At}\ge
F(\lambda):=\frac5{24\lambda}+\frac{\lambda}{(\lambda+2)^2}.
\]
F'(lambda)=−5/(24lambda²)+(2−lambda)/(lambda+2)³<0 在 1<lambda≤3/2：第二项≤1/27，第一项≤−5/54。因此
\[
\frac{\Phi_R}{At}\ge F(3/2)=461/1764.
\]
这里只比较根的可证下界；没有断言完整预算在 rho=1 取最小值。

## 联合付款

全部负价格满足
\[
\frac{2\rho\sum V_s\rho^{s-1}}{At}
=2u(R/t)\sum H_s\rho^s
\le\frac{67}{48}\left(\frac18+\frac1{32}+\frac1{100}\right)
=8911/38400.
\]
因此保留 root 与所有负价格后
\[
\frac{\mathcal V}{At}\ge461/1764-8911/38400>1/40.
\]
最后比较清分母仅为
461*38400−(8911+960)*1764=289956>0。
正平方可删除是因为 Us>0；这里已由 root 覆盖全部负价格，并非把单项正性当付款。

完整 Phi(Kb) 也可直接使用 f_s≤rho^(s−1) 删除正平方，得到同一付款，无需依赖尚未审核的幂下界转录。Kcap<Kb 的全 T 仿射比较已经独立 PASS。

本次闭合低 rho 半区。rho>1/2 的 V/完整付款仍未证；没有接近 rho1 的新断言，没有启动第二分支。原9600计算证明、全部已审实际入口、T1严格余量及其局部最大障碍保持。
