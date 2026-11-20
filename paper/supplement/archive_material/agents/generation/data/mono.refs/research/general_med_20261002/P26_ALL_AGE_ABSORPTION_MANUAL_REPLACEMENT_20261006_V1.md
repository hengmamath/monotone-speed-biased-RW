# P26：全部年龄 profile 吸收的短人工替换

2026-10-06。完整人工小引理与新一般身份源 native exit0；独立审核 PENDING。只新增文件，原 P26、冻结英文/errata、V13 不改。没有运行旧证书、参数扫描、年龄枚举、系数检查或创建代理/任务。

## 1. 精确合同与非重复性

权威合同来自 root_canonical_profile_payment.md §1 的(74)、general_two_over_sqrt3_verified_20261004.md 的(6)，以及 root_canonical_profile_payment.py 最初 s=2..7 loop。288 个控制中261严格正；它只证明采用较小 k_log=2/(lambda+1) 时 P_s>0。s>=8 原由 C_s>345/344>1 人工支付。

其他既有人工输入是实际 canonical marker 对 Theta_s 的严格下界、profile ratios/identity、a>lambda^2*u、完整吸收(75)、Lambda 和完整根 regrouping。P26 同文件还含三个标量身份及四个 cap 因素的检查；本稿只替换288项 sign 模块，不宣称删掉全部 P26 依赖。

此项与 S33 不重复：S33 支付 low-lambda 的 q=3..10 完整价格核 K 的 h 导数（取代另一928附录）；P26 属于高-lambda assigned/root 链，支付所有非根年龄同一负 adjacent/log defect 的吸收符号。它不支付根 SIZE，也不证明 Condition-F。

本稿证明更强的纯 profile 范围：每个 lambda>1、整数 s>=2、0<=lambda^2*u<=1 均成立；u=0 仅作为 profile 有理表达的连续端点。实际 canonical u>0。

## 2. 短引理与证明

记 c=lambda-1，t=lambda^2*u，omega=1-lambda*u=1-t/lambda>0，
N_s=lambda^s*(1-u)-1+lambda*u，D_s=N_(s+1)，r_s=N_s/D_s。

这是原 beta_(s+1)/beta_s；beta_s=c*u/N_s，beta_1=u，r_1=1/[1+lambda*(1-u)]，指标未改变。N_1=c，N_(j+1)=lambda*N_j+c*omega，故 N_s,D_s>0。

设 e_s=1-lambda*r_s=c*omega/D_s，并取原288检查所用的较小 C：

C0_s=(2s-1)/(s*(lambda+1)*r_s)。

要证 E0_s=e_s+(1-t)*(C0_s-1)>0。

令 S_s=sum_(j=0..s)lambda^j，D0=lambda^(s+1)-1=c*S_s。D_s=D0-lambda*u*(lambda^s-1)<=D0，且 omega>=1-t。因此

e_s>=c*(1-t)/D0=(1-t)/S_s，

而 D_s/N_s=lambda+c*omega/N_s>lambda，故

C0_s>lambda*(2s-1)/[s*(lambda+1)]。

对 t<1，代入给出

E0_s>(1-t)*R_s/[s*(lambda+1)*S_s]，
R_s=s*(lambda+1)-[s-(s-1)*lambda]*S_s。

一条有限几何和差分身份完成全部年龄：

R_s=lambda*[(s-1)+c*sum_(j=1..s-1)j*lambda^j]>0。

该身份由 (lambda-1)*sum j*lambda^j=(s-1)*lambda^s-sum_(j=1..s-1)lambda^j 直接取得。没有按年龄查系数。t=1 时 E0_s=e_s>0。证毕。

可核查的更强精确三正项分解如下。写 p=lambda^s，N=N_s，D=D_s，D0=lambda*p-1，S_s=D0/c：

G_e=c*t*[c*D0+(1-t)*(p-1)]/[lambda*D*D0]>=0，

E0_s=G_e+(1-t)*R_s/[s*(lambda+1)*S_s]
       +(1-t)*(2s-1)*c*omega/[s*(lambda+1)*N]。

t<1 时第二、三项严格正；t=1 时第一项等于 c^2/(lambda*D)>0。这是原 coupled profile 的身份，而不是新未证中间下界。

## 3. 对接精确288对象

原 frozen checker 的多项式是

P_s=s*(lambda+1)*N_s*(D_s-lambda*N_s)
 +(1-t)*[(2s-1)*D_s^2-s*(lambda+1)*N_s*D_s]。

严格正分母 s*(lambda+1)*N_s*D_s 给出原样身份

P_s=s*(lambda+1)*N_s*D_s*E0_s>0。

因此不仅六个 head s=2..7，而且全部 s>=2 都由同一个人工引理取得正性。288 Bernstein sign 控制可由此替换；其原文件保留。旧 s>=8 人工尾也被同一引理覆盖，不需要新检查。

## 4. 回到实际 canonical 吸收

原 k_log=c/(lambda*log(lambda))>2/(lambda+1)，由严格凸 1/x 的梯形上界取得。故实际

C_s=k_log*(1-1/(2s))/r_s>C0_s，

e_s+(1-lambda^2*u)*(C_s-1)>0。

实际/assigned hard 参数沿已审原合同 0<a<1、a>lambda^2*u、v>0。若 C_s>=1，则 T_s=(1+v)*e_s+(1-a)*(C_s-1)>0 显然；若 C_s<1，则 1-a<1-t 给 T_s>e_s+(1-t)*(C_s-1)>0。

保留原实际 marker 身份 Theta_s>C_s*delta_s，xi_s=Theta_s-C_s*delta_s>0；eps_s=a_s-lambda*a_(s+1)，delta_s=a_s*r_s-a_(s+1)>0，
gamma_(s-1)=a_s*(r_s-r_(s-1))-delta_s+Theta_s。原完整吸收恒等式为

(1+v)*eps_s^2/lambda+2*(1-a)*a_s*gamma_(s-1)
 =a_s^2*B_s+2*a_s*delta_s*T_s
  +(1+v)*lambda*delta_s^2+2*(1-a)*a_s*xi_s
 >a_s^2*B_s，

B_s=(1+v)*e_s^2/lambda+2*(1-a)*(r_s-r_(s-1))>0。

同时 gamma_(s-1)+eps_s/lambda=a_s*(1/lambda-r_(s-1))+Theta_s>a_s*L_s。与已审 Delta_s>=0 和完整根 regrouping 接合，原(76)/(7)完整 floor 原样成立。实际法则与全部 marker/根/龄补偿均保持，没有自由边际替代或逐项 pipe 速度替代。

Mellin 当前正确首因子仍为 a_(n+1)-lambda*a_(n+2)，这里 s=n+1 的 eps_s 与之相同。lambda=1 不在本引理范围，不处理跨1。

## 5. 验证与状态

新源只核 generic recurrence、e-gap、weighted-geometric residual、E0/E exact decomposition、原 P_s 分母身份以及原完整吸收/Lambda 身份。所有 generic assert native exit0；不导入任何旧 checker 或288正性结果。有限和正性是上述人工论证，不是枚举断言。

本稿局部完整，独立审核 PENDING。若同一辅助核准，必要链中P26的288 sign模块可 RETIRED；目前旧模块保留等待审核。原 cap/range、Condition-F 2x9744、small-u9600和其他分区检查未被此次改动。5076人工替换已审状态保持。Condition-F V13已冻结，新truequadratic补充PASS回执单独新增。
