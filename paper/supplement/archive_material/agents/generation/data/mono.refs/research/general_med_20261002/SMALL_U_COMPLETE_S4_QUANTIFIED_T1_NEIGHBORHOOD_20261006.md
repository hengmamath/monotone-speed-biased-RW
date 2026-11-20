# 完整四龄：T1 有限损失与定量邻域

2026-10-06。唯一 rho>2/3 目标。暂未得到贯通剩余区域的短下界，本稿给明确端点邻域及余量，LOCAL待同一辅助。没有网格、系数扫描、大表或旧证书运行。

## 合同与严格结论

原 lambda∈[2/√3,707/500]、0<u≤1/2、同一 rho=T(2−T)、f_s、完整 root 和 s=2,3,4、正确 assigned a,w 全保留。K=Kb 为原已审短界，Phi=rho*d*S4/u²。证明
\[
\boxed{\Phi(T)\ge\Phi(1)-100(1-T)^2\quad(2/3\le\rho\le1),}
\]
并从已审 T1 合同提取统一 Phi(1)>1/1000。因此
\[
\boxed{319/320\le T\le1,
\quad\Phi(K_b)>3/128000>0.}
\]
等价 rho≥102399/102400。已审 K 仿射接口给 Phi(Kcap)>Phi(Kb)；T1端点也是标量边界。本稿未声称实际 hard law 可实现性，也未证明幂下界V在此区域正。

## 1. 从已审原 T1 提取统一余量

记 t=1−u、k=1−lambda*u、A=Z2=lambda+k、B=Z3=lambda²+(lambda+1)k，Z_s=t sum_(j=0..s−1)lambda^j+u。原 T1 的清分母付款 Phi_b=D*S4/u²，新 Phi(1)=A*Phi_b，归一化接合已审 PASS。

k≥1/2 时已审完整端点合同给 Phi_b/k>181/132300；A>3/2，故
\[
\Phi(1)>181/176400>1/1000.
\]
k≤1/2 时，已审原根加完整二龄合同及八项正预算给
\[
\Phi(1)>\frac{k A_0}{12\lambda^3A^2B^2},
\quad A_0=\lambda^3c^2(\lambda^2+2)(23\lambda^2+\lambda+1-\lambda^3),
\quad c=\lambda-1.
\]
此处只用已审 A0 项和其他项非负；不重核旧预算。用
\[
k\ge293/1000, c\ge3/20, \lambda^2+2\ge10/3,
\quad23\lambda^2+\lambda+1-\lambda^3\ge1849/60,
\]
\[
A\le2,\quad B\le7/2,
\]
得到
\[
\Phi(1)>\frac{293}{1000}\frac9{400}\frac{10}3\frac{1849}{60}\frac1{588}
=541757/470400000>1/1000.
\]
第四个下界来自 lambda≤3/2、lambda²≥4/3、lambda+1>43/20；k界来自原707/500上端及u≤1/2。两片的端点余量均已严格量化。

## 2. 精确完整函数与 root 损失

用原 Kb=(lambda+1)/(2lambda)+t/2+(lambda+1)(2lambda*t−lambda+1)t/(24lambda)，
\[
R=t+\rho^2(K_b-t),\quad Q=At+\lambda u\rho t+u\rho^2,
\quad E=1-\lambda\rho/A,
\]
\[
\Phi(T)=\Phi_R(\rho)+2\rho\sum_{s=2}^4[U_s(\rho)f_s^2-V_s(\rho)f_s],
\]
\[
U_s=W_sL_s[QF_s+uAR\lambda r_s^2],\quad F_s=2-r_s-\lambda r_s^2\in(0,2),
\quad V_s=W_sL_suAR/r_{s-1}>0.
\]
这里 r_s=Z_s/Z_(s+1)、L_s=1/lambda−r_(s−1)、W_s=s lambda^(s−1)/Z_s²。
这是已审完整年龄抵消身份，没有冻结a/w或改变校准。同T merge的两个严格余量仍包含于此精确总和。

设 G=2A−rho−lambda*rho²/A、H=A−lambda*u*rho²/A、J=QG−ARH，则 Phi_R=2EJ/lambda。在 rho≥2/3，
\[
3/2<A\le5/2,\quad Q\le A,\ Q'\le11/8,
\quad R\le5/3,\ R'\le7/3,
\quad0<E\le2/3,\quad0<G\le37/9,\quad0<H\le A.
\]
这些界来自 Q(1)=A、Kb≤5/3、Kb>t、u*t≤1/4、lambda/A>1/2。因QG与ARH均正，
所用 Kb≤5/3 可直接由 Kb 的 u 导数为 −1/2−(lambda+1)(4lambda*t−lambda+1)/(24lambda)<0，以及 Kb(lambda,0)=(lambda+26+13/lambda)/24 在1<lambda≤3/2递减得到。Kb>t则由其首项>1/2、第二项=t/2、第三项正得到。
\[
|J|\le\max(185/18,125/12)=125/12.
\]
又 J'=Q'G−ARH'−[Q|G'|+AR'H]，两括号为正，分别至多587/72、241/12。因此 |J'|≤241/12。用lambda≥23/20得
\[
|\Phi_R'|\le\frac4{3}\frac{125}{12}
 +\frac{80}{69}\frac{241}{12}=855/23<40.
\]
故 root 从 rho1 到rho 的损失至多 (855/23)(1−rho)。未要求其单调或为全预算最小值。

## 3. 完整年龄正平方的有限损失；负价格有利

设 eps=1−T、n_s=s(s−1)/2。精确积分给
\[
1-f_s=s(s-1)\int_T^1x^{s-2}(1-x)dx\le n_s\epsilon^2,
\quad1-\rho f_s^2\le(1+2n_s)\epsilon^2,
\quad1-\rho=\epsilon^2.
\]
由已审 H2≤1/2,H3≤1/4,H4≤4/25，及 r1≤2/3,r2<3/4,r3<3/4，得到
\[
W_sL_s\le m_s,
\quad(m_2,m_3,m_4)=(1/3,3/16,3/25).
\]
r3界仅用 r3随u增及3lambda³−lambda²−lambda−2在23/20为721/8000>0；不依赖中间区间最终付款。
Q、R及U_s随rho递增；Q(1)=A、R(1)=Kb、uA≤7/8。因此
\[
U_s(1)\le(155/24)m_s,\qquad
0\le U_s'\le(115/24)m_s.
\]
第一常数为2A+uAKb≤5+35/24；第二为2Q'+uAR'≤11/4+49/24。
每个完整正平方的损失满足
\[
2[U_s(1)-\rho U_s(\rho)f_s^2]
\le2m_s[115/24+(155/24)(1+2n_s)]\epsilon^2.
\]
三龄相加，Σm_s=769/1200、Σm_s(1+2n_s)=1549/400，总代价为
\[
C_{age}=10109/180.
\]
负价格全部保留：因为rho,R,f_s均不超过端点值，
−2rho*V_s(rho)*f_s≥−2V_s(1)，从T1下降时它们的变化有利，无需额外收费。
故完整函数
\[
\Phi(T)\ge\Phi(1)-(855/23+10109/180)\epsilon^2,
\]
\[
855/23+10109/180=386407/4140<100.
\]
这是完整有限loss界，不是仅保留两龄或单项正性。

## 4. 明确邻域及真正剩余区间

若 eps≤1/320，则
\[
\Phi(T)>1/1000-100/320^2=3/128000>0.
\]
因此原完整Kb付款新增闭合 rho∈[102399/102400,1]（LOCAL）。前低rho≤1/2已独立PASS，中间rho≤2/3也已收到独立PASS。真正剩余为
\[
2/3<\rho<102399/102400.
\]
邻域很短，本稿不把定量连续性扩成整个上半区。原T1局部max障碍保持，正余量已明确支付有界损失；完整9600不整体退出，一般S42仍OPEN。只新增文件，无第二分支。
