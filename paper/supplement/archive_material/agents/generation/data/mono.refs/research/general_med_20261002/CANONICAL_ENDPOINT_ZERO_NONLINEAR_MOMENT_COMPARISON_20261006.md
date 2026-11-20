# p(1)=0 的 actual canonical 非线性三矩比较

2026-10-06。新的端点推论及原宽 CF 点修复，短源 native exit0；独立审核待定。
通用三核恒等式已审，但本稿直接证明端点严格性，不以极限代替严格性。

## 1. 自洽的 actual 证明

固定 μ0=0、μ1>0、仅有限 m=Eν>1，1<λ<m，普通根同 μ；X 只取实际
terminal-one canonical 逃逸。c=λ−1、U=X/(c+X)，所以 0<U<1/λ。
设 u=EU、b=EU²、e=EU³、q=b/u、t=e/u。

**结论：**

                  e/b < 1/(λ+1−λq)。                     (T)

q−t>0，且 Cauchy 给 t≥q²。因此
η=(q−t)/(1−q) 满足 0<η≤q<1/λ<1。置

 p(y)=(y−η)(1−y)=(1+η)y−y²−(q−t)−ηq。

直接有 p(0)=−η<0、p(1)=0 及 E[U p(U)]=0。
给定实际 ν 和 iid 孩子 x_i=U_i，写

 S=Σ_i x_i/(1−x_i)，F=S/(1+S)=λU_parent，
 Q_i=Σ_(j≠i)x_j/(1−x_j)，A_i=[1+(1−x_i)Q_i]^−1，
 A_η(Q)=[1+(1−η)Q]^−1。

有 F=1−A_i(1−x_i)、Σ_i x_iA_i=F。二次凹性身份为

 p(F)=A_i p(x_i)+A_i(1−A_i)(1−x_i)²。

乘 x_iA_i 后全子求和。条件 iid 校准给
EΣ_i x_i A_η(Q_i)²p(x_i)=0。因此

 J:=E[Fp(F)]
  =EΣ_i x_i[A_i²−A_η(Q_i)²]p(x_i)
    +EΣ_i x_iA_i²(1−A_i)(1−x_i)²>0。

第一核非负：A_i 随 x_i 递增，平方差与 p(x_i) 均同号于 x_i−η。
第三核在每个 ν≥2 根严格正，因为实际孩子均正、Q_i>0、0<A_i<1。
P(ν≥2)>0，所以其期望严格正。中核因 p(1)=0 消失。
有符号交换由常数倍 Σ_i x_i 控制，期望为常数倍 m u<∞；第三和
被 Σ_i x_iA_i=F<1 控制。无需后代二阶矩。

普通根同 μ 给 F 与 λU 同分布。用校准直接算

 J=λc[(1+η)b−(λ+1)e]
  =λcu[q−(λ+1−λq)t]/(1−q)>0。

所有被除因子正，故 t<q/(λ+1−λq)，即 (T)。没有 CF、speed 或大证书输入。

## 2. 与原 strict κ 界的精确关系

A=λ+1−λu、B=(λ+1)A−λ、D=λ+1−λq、κ=λ/(λ+1)²。
沿已经独立证明的 actual ρ2=Aq<1，原线性上界
θlin=(A/B)[1−κ(1−Aq)] 与新 θnl=1/D 的差恰为

 θlin−θnl=λ²(1−Aq)[Aq+(λ+1)u]/[BD(λ+1)²]>0。

所以 (T) 严格强于原线性界。等价的 profile 形式是

 ρ2−ρ3 > [λ/(AD)]ρ2(1−ρ2)，ρ3=Bt，

其中 λ/(AD)>κ，且当 u,q↓0 时该变系数趋 κ；不与已审的常数 κ sharp 冲突。
在 q=1/A 的形式端点，两上界同为 A/B。

## 3. 来源核对

这是今日已审 actual iid 三核恒等式的 p(1)=0 端点推论。现有
ACTUAL_IID_ADJACENT_PROFILE_STRICT_SINGLE_CROSS_PROOF_20261006_V2.md
及 CANONICAL_SHARP_ADJACENT_PROFILE_AND_SINGLE_CROSS_SHORT_RESEARCH_NOTE_20261006.md
写的是 p(1)>0 通用引理，并以指定 η 证明 κ 界；它们已有同一个 D 和正因子。
此前 scaled_r0_adjacent_defect_payment.md 第2节仅是给定入口后的矩传播。
按需读取这些来源及对 mono.md、00_START_HERE、med_bias、研究 Markdown 的
精确式检索，未见 η=(q−t)/(1−q) 或 (T) 的显式陈述。它是已有内核的
直接新端点应用；本核对不构成全历史、外部文献或新颖性声明。

## 4. 只复核原 u=.6 宽 CF 障碍

仍取原 λ230941/200000、u3/5、z1307153/2000000，此处旧 CF 的 z=q。
保持原 Kcap、同一 assigned a,w。用 θnl=1/(λ+1−λz)，

 Cnl=Df(1−θnl)−uR(1−z)
    =(1−z)[λDf−uR(λ+1−λz)]/(λ+1−λz)。

actual (T) 与 Ar=Df/(zDw)>0 直接给 Δ2/b>Cnl/(zDw)。固定点 exact 核验

 原线性 Cp∈(−13,−12)/10^6，
 Cnl∈(21,22)/1000，Cnl/(zDw)∈(25,26)/1000，
 θcrit−θnl∈(10,11)/1000。

因此新 actual 输入修复原宽 CF 标量障碍。没有给该点指派 actual 第三矩
或实际 GW μ；若 actual law 落在此矩点，新的下界确实支付 assigned Δ2。
未证明 Cnl 全域非负、CF 全域人工替换或一般 S42 complete floor 引理。
原两9744、full-T9600及内部审核计算辅助速度定理全部保留。
