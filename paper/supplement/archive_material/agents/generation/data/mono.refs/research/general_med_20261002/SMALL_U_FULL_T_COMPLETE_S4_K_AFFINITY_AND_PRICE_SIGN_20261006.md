# 完整四龄、全 T 的 K 仿射接口及价格符号

2026-10-06。唯一小 u 目标的一个新接口；LOCAL 推导及有限通用身份核验，待父任务复用同一独立辅助。未执行旧 9600、任何参数/系数扫描或多变量系数展开。原审计与冻结程序保持。

## 精确合同

实际 terminal-one canonical 模型及原 legal assigned hard 合同保持。此处只证明其完整标量 S4 的代数比较。令
\[
2/\sqrt3\le\lambda\le707/500,\quad0<u\le1/2,\quad0<T\le1,
\quad c=\lambda-1,\quad t=1-u,\quad k=1-\lambda u>0,
\]
\[
Z_s=t\sum_{j=0}^{s-1}\lambda^j+u,\quad A=Z_2,
\quad r_s=Z_s/Z_{s+1},\quad e_s=1-\lambda r_s,
\quad L_s=1/\lambda-r_{s-1},\quad W_s=s\lambda^{s-1}/Z_s^2.
\]
保留同一 \(\rho=f_2=T(2-T)\)、\(f_s=T^{s-1}[s-(s-1)T]\)，同一实际 \(b=u\rho/A\)。对价格 K 定义
\[
R=t+\rho^2(K-t),\quad Q=At+\lambda u\rho t+u\rho^2,
\quad d=2Q-(\lambda+1)uAR,
\]
\[
a_0=[1-(\lambda+1)u]A+\lambda u\rho,
\quad w=cuAR/d,\quad a=A(d-Ra_0)/(\rho d).
\]
这是原 \(T_2=u^2R/t\)、\(Q_2=uQ/(At)\) 以及
\(w=cT_2/[2Q_2-(\lambda+1)T_2]\)、\(a=[u-wA_0/c]/b\) 的正确校准，\(A_0=a_0/A\)。没有额外 u。

原完整预算为
\[
\mathcal S(K):=S_4(K)/u^2
=\frac{(1+w)E^2-2(1-a)E}{\lambda}
 +\sum_{s=2}^4W_sf_s^2[B_s+2L_sM_s],\quad E=1-\lambda\rho/A,
\]
\[
B_s=(1+w)e_s^2/\lambda+2(1-a)(r_s-r_{s-1}),
\quad M_s=a(1-r_s)+(w/c)[\lambda+1-\lambda r_s-1/(r_{s-1}f_s)].
\]
Root、全部三个年龄及负前矩价格原样保留。

## 仿射身份与严格负 K 系数

递推 \(Z_{s+1}=\lambda Z_s+k\) 给
\[
r_s-r_{s-1}=L_s(1-r_s),\qquad e_s=\lambda r_sL_s.
\]
故每个完整年龄括号中的 a 恰好消去。定义
\[
F_0=(E^2-2E)/\lambda+\sum W_sf_s^2[e_s^2/\lambda+2(r_s-r_{s-1})],
\quad F_a=2E/\lambda,
\]
\[
F_w=E^2/\lambda+\sum W_s\{f_s^2[e_s^2/\lambda+(2L_s/c)(\lambda+1-\lambda r_s)]
 -(2L_s/c)f_s/r_{s-1}\}.
\]
两和均为 s=2,3,4。于是完整 \(\mathcal S=F_0+aF_a+wF_w\)。置
\[
\widehat C=\rho F_0+AF_a,\quad
\widehat H=(\lambda+1)u\widehat C+a_0F_a-cu\rho F_w.
\]
直接代入正确 a,w 得完整清分母身份
\[
\Phi(K):=\rho d(K)\mathcal S(K)
=\mathcal P-K\mathcal Q,
\]
\[
\mathcal P=2Q\widehat C-At(1-\rho^2)\widehat H,
\qquad \mathcal Q=A\rho^2\widehat H.
\]
这里 P,Qcal 与 K 无关。无需展开原 degree(39,15,14) 分子。

关键紧凑价格分解是
\[
\boxed{\widehat H=
\frac{2E}{\lambda}\left(A-\frac{\lambda u\rho^2}{A}\right)
 +2u\rho\sum_{s=2}^4 W_s\frac{L_sf_s}{r_{s-1}}
 [1-\lambda r_{s-1}r_s^2f_s].}
\]
其推导保留负价格：年龄部分先为
\(2u\rho W_s[L_sf_s/r_{s-1}-e_sr_sf_s^2]\)，再用 \(e_s=\lambda r_sL_s\) 因式化。

各 \(Z_s>0\)，\(0<r_s<1/\lambda\)，\(L_s>0\)；\(0<f_s\le1\)，因为
\(f_s'=s(s-1)T^{s-2}(1-T)\ge0\) 且 \(f_s(1)=1\)。因而
\(\lambda r_{s-1}r_s^2f_s<r_s^2f_s<1\)，年龄价格严格正。
又 \(A=\lambda+k>\lambda>1\)，\(\lambda u<1\)，所以
\(E\ge k/A>0\)、\(A^2>\lambda u\rho^2\)。根价格亦严格正。
故 \(\widehat H>0\)、\(\mathcal Q>0\)，并有 \(\partial_K\Phi=-\mathcal Q<0\)。

此结论在上述整个标量 T 域成立，因此覆盖实际 legal hard 子域；未声称任意标量点来自 canonical law。乘任何与 K 无关的正 profile 分母，仿射结构及负 K 系数仍成立。T=1 时 d=A[2-(λ+1)uK]，本式正好恢复已审端点价格。

## 已有短 K 上界可以合法导入

原 finite-atanh Kcap 保持。令 j=c/(λ+1)、ℓL=2(j+j³/3+j⁵/5)、ℓU=ℓL+2j⁷/[7(1-j²)]，并明确
\[
K_{cap}=c/(\lambda\ell_L)+t/2+\ell_U(2\lambda t-c)t/(12c).
\]
由 ℓL>2j、ℓU<2j/(1-j²) 及 2λt−c≥1，得到已审短界
\[
K_{cap}<K_b=\frac{\lambda+1}{2\lambda}+\frac t2+
\frac{(\lambda+1)(2\lambda t-c)t}{24\lambda}
=K_0-k_1u+k_2u^2,
\]
\[
K_0=(\lambda^2+26\lambda+13)/(24\lambda),\quad
k_1=(3\lambda^2+16\lambda+1)/(24\lambda),\quad k_2=(\lambda+1)/12.
\]
在 1<λ≤3/2、0<u≤1/2，Kb>0。\(G=1+\lambda u\) 时
\[
(GK_b)'\ge[-2\lambda^3+9\lambda^2-2\lambda-1]/(24\lambda)>0,
\]
第一步使用 k2−λk1<0、u≤1/2 及丢弃正二次项；第二步使用 λ≤3/2。
而
\[
2-GK_b\big|_{u=1/2}=[6+c(19-37c)]/(96\lambda)>0.
\]
故 2−GKb>0。对所有 0<ρ≤1，保留原 Q,R 的有限身份给
\[
\frac{d(K_b)}{At}-R(K_b)
=(1-\rho)\left[k(1+\rho)+\frac{2\lambda u}{A}\rho\right]
 +\frac{2-GK_b}{t}\rho^2>0.
\]
R(Kb)=t(1−ρ²)+Kbρ²>0，故 d(Kb)>AtR(Kb)>0；又 Kcap<Kb 使 d(Kcap)>d(Kb)>0。
因此可用完整标量付款比较
\[
\Phi(K_{cap})>\Phi(K_b),\qquad
\Phi(K_b)>0\ \Longrightarrow\ S_4(K_{cap})>0.
\]
Kb 只用于清分母标量比较；无需把其 a(Kb) 宣称为合法 hard 校准。

## 结论及限制

全 T 的完整付款确实保留 K 仿射性，K 系数严格负，且短 Kb 上界处的原分母全域为正。这一接口已 LOCAL 闭合，可将下一步未付目标准确写成完整 Φ(Kb)>0。
本稿没有证明这一全 T 正性，也没有断言未清分母的 S4 数值随 K 递减。9600 保留；一般 S42 仍 OPEN。T=1 端点与二阶障碍的既有审计状态不变。当前新增源只核有限通用身份，无原证书导入或运行。
