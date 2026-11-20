# 全龄 profile 吸收引理

**引理。** 设 \(\lambda>1\)，\(0\le u\le\lambda^{-2}\)，整数 \(s\ge2\)。记
\[
c=\lambda-1,\quad t=\lambda^2u,\quad\omega=1-\lambda u,
\quad N_j=\lambda^j(1-u)-1+\lambda u,
\quad r_s=N_s/N_{s+1},\quad e_s=1-\lambda r_s.
\]
则
\[
e_s+(1-t)\left[\frac{2s-1}{s(\lambda+1)r_s}-1\right]>0.
\]
因而对 \(C_s=c(1-1/(2s))/(\lambda\log\lambda\,r_s)\)，亦有
\[
e_s+(1-\lambda^2u)(C_s-1)>0.
\]

**证明。** \(\omega\ge c/\lambda>0\)，而 \(N_1=c\)、\(N_{j+1}=\lambda N_j+c\omega\)，故各分母正。令 \(S_s=\sum_{j=0}^s\lambda^j\)。有
\[
e_s=\frac{c\omega}{N_{s+1}}\ge\frac{1-t}{S_s},
\qquad\frac1{r_s}=\lambda+\frac{c\omega}{N_s}>\lambda,
\]
第一式使用 \(\omega\ge1-t\) 及 \(N_{s+1}\le\lambda^{s+1}-1=cS_s\)。当 \(t<1\)，引理左侧严格大于
\[
\frac{(1-t)\{s(\lambda+1)-[s-(s-1)\lambda]S_s\}}
{s(\lambda+1)S_s}>0,
\]
因为有限几何和差分给出
\[
s(\lambda+1)-[s-(s-1)\lambda]S_s
=\lambda\left[(s-1)+c\sum_{j=1}^{s-1}j\lambda^j\right]>0.
\]
当 \(t=1\)，左侧为 \(e_s>0\)。最后，严格凸 \(1/x\) 的梯形上界给 \(\log\lambda<c(\lambda+1)/(2\lambda)\)，故 \(C_s>(2s-1)/(s(\lambda+1)r_s)\)，第二个结论随之成立。\(\square\)

**Canonical 吸收推论。** 沿实际或合法 assigned hard 合同，设 \(0<a<1\)、\(a>\lambda^2u\)、\(v>0\)，并沿原实际 marker 身份记 \(\delta_s=a_sr_s-a_{s+1}>0\)、\(\xi_s=\Theta_s-C_s\delta_s>0\)。上述引理给
\[
T_s=(1+v)e_s+(1-a)(C_s-1)>0\qquad(s\ge2):
\]
\(C_s\ge1\) 时显然；否则用 \(1-a<1-t\)。于是原完整恒等式
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
