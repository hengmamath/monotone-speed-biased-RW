# Q3c：不以 40706 为数学前提的完整替换装配候选

2026-10-08。固定候选，待原同一个唯一辅助独立全链审计。历史文件全部保留；本稿没有在审计前宣布旧证书退出。这里的完整性指下面明定 Q3c 分支及原解析接口的装配，不能推成一般 m1=1 全部 (0,m) 定理、跨 lambda=1 或一般 canonical S42 结论。各叶的完整正文、固定正式回执及原始源码须随最后证明包保存；标题中历史 PENDING 字样不能代替正式回执状态。

## 1. 实际入口、符号字典和需要替换的唯一节点

保持原整数 offspring 律 mu(0)=0、mu(1)>0、有限均值 1<m<infinity，普通 GW 根，非根 parent 权 lambda、每个 child 权 1；实际 escape X 是 terminal-one finite-depth canonical 极限。只在原已审响应链适用的 hard 分支 1<lambda<min(m,2/sqrt(3))、0<alpha_actual<1 内使用 Q3c。记 c=lambda-1、L=lambda、U=X/(c+X)、u=EU、q_old=u/(1-u)、h=c q_old、d=1-h。本文参数域是

    10<=q_old<=21, x=1/q_old, 0<h<=1/4,
    c=hx, L=1+hx, u=1/(1+x), d=1-h.

q_old 可以为实数；年龄 i 为正整数。beta_i=h/(L^i-d)、w_i=L^(i-1)beta_i^2、T=sum_(i>=1)w_i、Zp=2q_old-(L+1)T、R=T/Zp。这里 R 是原参考校准 R_p，绝不是实际 assigned speed R*=v/c；实际速度证明只在固定实际 moments 时把 R* 比较到 R_p。置

    alpha_p=[L^2 q_old+(1-R/q_old)d(L+1)]/(q_old+1),
    g=q_old-R,
    alpha_p=[L^2+g d(L+1)x^2]/(1+x).

源/间隙完整人工叶 Q3CHAND_CONTINUATION_COMPLETE_SOURCE_AND_GAP_MANUAL_PROOF_LOCAL_20261008.md 和其正式 PASS 收据给 Zp>0、1/8<g<1/4、Fpipe>69/500。本稿不从旧 40706 的正文或运行得到这三条。

rho_i=EU^i/beta_i、Delta_i=rho_i-rho_(i+1)、e=Delta_1=1-rho_2 是同一个实际 defect。原 hard 校准给 0<e<Ehard<Evar=d/(q_old+1)^2；下面也允许 e=0 的代数闭边界。完整的实际入口见 calibrated_cumulative_head_payment.md (214)–(222) 及 audit_receipt_calibrated_cumulative_head_20261004.md：

    Ffloor(R*)>Fpipe-e Hhead-e^2 Jminus,
    Hhead=sum_(i>=1)i[-S_i]_+,
    S_i=B_i^p-2V_i(R), Jminus=sum_(i>=2)i^2[-J_i]_+.

原更强式还含正 root square 和 calibrated speed credit；只舍去它们一次。i=1 的 k 项先精确抵消；Young 从 i=2 开始，W_1=0，W_2/2 仅付一次。原响应链为 Zact>0、v'=-D/Zact、D>=Fstar>Ffloor。因此 Ffloor>0 给原域 v'<0；不能把参考 Zp、D_i 或 F 直接当作实际 D、Zact。

原 40706 节点只证明有限头同一显式函数 F=D_i(1+c/2)-K 的 F_h>0 和 F>0。下面重新证明其同-a 扩展和头比较，随后重新装配 same-e 预算。旧 Q3CHAND 同-e 装配中引用 40706 的 §3 **不是**本稿数学前提；旧全装配 PASS 也不作为本稿结论的证明。

## 2. 全 N 尾界先在实际 a 使用

a_actual=c/log L=integral_0^1 L^r dr。带完整积分余项的三/四阶 Taylor 给

    1<=Alo=1+c/2-c^2/12<=a_actual
       <=Aup=Alo+c^3/24<=alin=1+c/2.

原 w_i、V_i、年龄比与两真实边界保持不变。令 n=i+1、p=L^n、B=(p-d)/h、b0=1/B，完整几何矩是

    m0=1/B, m1=p/B^2, m2=p(p+d)/B^3,
    m3=p(p^2+4dp+d^2)/B^4,
    m4=p(p^3+11dp^2+11d^2p+d^3)/B^5.

自由比较参数 a>=1 定义

    TL(a)=[a m0/x+m1/2+x m2/(12a)-x^3 m4/(720a^3)]/L,
    PU(a)=[n(a m1+x m2/2+x^2 m3/(12a))
                 +a^2 m0/x-x m2/12+x^3 m4/(240a^2)]/L^2,
    Vup(a)=-(1+hxR)TL(a)+[1+(L+1)R]PU(a)
                  -2Rn p/(LB^2)-2R/(xLB).

Q3CHAND_CONTINUATION_COMPLETE_WEIGHT_TAIL_AND_SAME_A_INTERFACE_MANUAL_PROOF_LOCAL_20261008.md §§1–4 和正式 PASS 从完整所有 N>=1 Lambert/F/C 界、固定 h,d 的原尾求导、两个真实望远镜首端证明 V_i<=Vup(a_actual)。没有声称 Vup(a) 对每个自由 a 仍是实际尾上界。以下仅改变显式函数 D_i(a)。

令 r=beta_(i+1)/beta_i、rprev=beta_i/beta_(i-1)、ell_i=cd/[L(L^i-d)]，tau=1-(alpha_p+LR)r+(L+1)R-R/rprev，定义

    BB(a)=2i(alpha_p+hxR)/L+2iRr ell_i
                 +2nRLr^2 ell_i+(a/L)(2i-1)tau,
    D_i(a)=BB(a)-2Vup(a)/w_i.

BB(a_actual)=B_i^p/w_i，所以 S_i/w_i>=D_i(a_actual)。原 B_i^p 是未归一化头价，BB 已除 w_i；这个归一化不能重复除一次。

## 3. 独立重证 D_i'(a)<0 对全部 a>=1

固定 q_old,h,g,i、p、五矩、w_i；只改变同一个 a。1<=i<=24 时 c<=1/40、n<=25。log(1+c)<c 和完整指数级数 n!>=2*3^(n-2) 给

    p<exp(5/8)<=1+5/8+(5/8)^2/[2(1-5/24)]
                              =569/304<2.

p-1=c sum_(j=0)^(n-1)L^j<2nc，故 b0>1/(1+2n/q_old)>=1/6；b0<=1。由原正矩得 m3/m1<=13、m4/m0<=150。又 w_i<=w_1=u^2<1：写 y=L^-i，w_i=h^2 y/[L(1-dy)^2]，其 y 因子导数为 (1+dy)/(1-dy)^3>0，y<=1/L。

ell_i<=d/[L(q_old+i)] 给 L ell_i<1。完整通分身份

    (L+1)-Lr-1/rprev
       =-(L+1)ell_i(c+L ell_i)/[(1+ell_i)(1-L ell_i)]<0

与 alpha_p,R>0 给 tau<1，首龄 tau_1=0 被包括；这里不需 tau>=0。通常导数为

    TL_a=[m0/x-x m2/(12a^2)+x^3m4/(240a^4)]/L,
    PU_a=[n(m1-x^2m3/(12a^2))+2a m0/x
                                      -x^3m4/(120a^3)]/L^2.

对 **所有** a>=1，13x^2/(12a^2)<=13/1200<1，故 n 项正。舍去负 TL 项及正 PU n 项，150x^4/240<=1/16000、150x^4/120<=1/8000，得

    TL_a<(101/100)m0/(xL),
    PU_a>(19/10)m0/(xL^2).

同一个 R=q_old-g>q_old-1/4、cR<=1/4、L<=41/40，于是

    Vup_a>m0/(xL^2)[(19/10)(2q_old+1/2)
                               -(101/100)(41/40)(5/4)]
              >3q_old^2 m0.

最后严格差的完整付款是

    (19/10)(2q_old+1/2)-(101/100)(41/40)(5/4)
                      -3q_old(41/40)^2
      =(1037/1600)q_old-1101/3200>=19639/3200>0.

因此 D_i'(a)=(2i-1)tau/L-2Vup_a/w_i
<47-6q_old^2 b0/w_i<=47-q_old^2<0。每步对 a 的唯一要求已列为 a>=1，无旧 40706 N/M 表、66 付款或其正性前提。由 a_actual<=alin，合法得到

    S_i/w_i>=D_i(a_actual)>=D_i(alin).

## 4. 实际 F 的全式及与新函数合同的逐项匹配

在 alin=(2+hx)/2，原年龄比和权重逐式为

    r=(B-dx)/(LB), rprev=[B-(L+1)dx]/[L(B-dx)],
    ell_i=dx/(B-dx), w_i=p/(B-dx)^2,
    K(t,x)=[(3-9x)t-7/3+3x]/(1+t), t=i x.

取上节五矩、TL、PU、Vup 和 BB 的完整原式，F=BB-2Vup/w_i-K=D_i(alin)-K。与 Q3HHAND 的归一化生成的匹配不是只在 h=0 的一致：置 eta=dx/B、c=hx 后，五个归一化矩分别为

    m0/(xw_i)=(1-eta)^2/(c+eta),
    m1/w_i=(1-eta)^2,
    x m2/w_i=(1-eta)^2(c+2eta),
    x^2m3/w_i=(1-eta)^2(c^2+6c eta+6eta^2),
    x^3m4/w_i=(1-eta)^2(c^3+14c^2eta+36c eta^2+24eta^3).

将这五式、r、rprev、ell_i 代入完整 BB/TL/PU，恰是 Q3HHAND V2 §2 的 G；同一原 K 被减掉。V2 的 alpha=[L^2+g d(2+hx)x^2]/(1+x)，没有 V1 曾误写的额外 L 分母。本稿附属小身份源码从实际 beta/alpha 和归一化矩重建上列匹配；完整 G 六分块一般身份仍由独立原 BB/TL/PU 来源、固定 V2 全文及其正式 PASS 承担。

注意 HH 中自由 q_rho=d/B，不是 q_old。真实 B=(L^(1+t/x)-d)/h、q_rho=d/B、W=(B+dB_h)/B^2，沿 h 固定 x,t,g 时 q_rho,h=-W；实际头固定 i 等价于固定 t=i x，n=i+1 恒定。实际 i=1..24 给 x<=t<=12/5、x<=1/10，故完全包含在已审 HH 实年龄 n>=2 的函数合同中。g 沿比较族固定只是证明每个标量 g 的不等式，没有对实际固定 mu 的 g(h) 或 offspring law 求导。

## 5. 不经 40706 的严格余量

完整 HH V2 余项证明和正式 PASS 给 H/x>-15/2+m_j，三段 t 为 [0,1/8]、[1/8,1/2]、[1/2,12/5]，

    m1=67933/1215000,
    m2=5036407/31104000,
    m3=8462947/826200000=:mstar>0.

Q3DX 的完整三分区 U>3/4 正式 PASS 和真实链式导数给 F_h=U+H>3/4-(15/2)x+m_j x>=mstar x>0。m1-mstar=37731493/826200000，m2-mstar=2005065823/13219200000 均正。x=1/10 时前两个常数抵消而 mstar x 仍严格正。

同一原 F 的 Q3CHAND hzero 完整人工叶和正式 PASS 给

    F(0)=x P(x,t,g)/[15(1+t)(1+x)(1+t-x)(1+t+x)^5]>0.

P 完整 128 槽、82 非零，其来源先从同一个完整 BB-2V/w-K 生成；不是 Q2 的另一个 h0 价格。真实积分 B=1+(t+x) integral_0^1(1+hxr)^(n-1)dr 给 h∈[0,1/4] 光滑延拓、q_rho(0)=1/(1+t+x)。六块分母 (1+x)、L、(2+hx)、h+q_rho、1-(2+hx)q_rho x>=133/160、(1+t) 全正。固定 t 所属段，微积分基本定理给

    F(h)>F(0)+h mstar x>0,
    S_i/w_i>K(t,x)+F(0)+h mstar x>K(t,x), i=1..24.

新链从原全式、U、H、h0 正性积分直接得此结论。未用旧 N 的 2042 项、M 的 38664 项、66 付款或其结论；也未声称全域 W3/F_xh>0 或 H_h>=-2。

## 6. 完整无穷尾及 same-e 线性价

共享 Q3HAND source/price/shape 独审完整叶给对每个实际 i>=1

    S_i/w_i>=env(t)-eta0+ht(3/4-eta0),
    env(t)=(9t-7)/[3(1+t)], eta0=28/(5q_old)<=14/25.

3/4-eta0>=19/100>0，负部必须 t<217/183。i>=25、q_old<=21 给 t>=25/21>217/183，差 2/427>0；所有余龄的负部为零。该输入只用共享源/价格/形状叶，不用旧有限头比较。

全年龄权界 d w_i<=(1+t)^-2 的完整双曲证明在独审 weight/tail 叶：a_actual<=1+c/2，rho=(1-h/2)/a_actual<=1，L rho^2>d，L rho>d；通分二次系数全正。恒等 L(1-h/2)^2-d(1+c/2)^2=h^2(L-dx^2)/4>0 含全部 t>=0，不截龄。

用 **同一个** 实际 e<=d/(q_old+1)^2，全部负头只在 i<=24，所以

    e Hhead<=d/(q_old+1)^2 sum_(i=1)^24 i w_i[-K(ix,x)]_+
       <=(u^2/q_old) sum_(i>=1)G_x(i/q_old),
    G_x(t)=[t((7-9x)-(9-27x)t)/(3(1+t)^3)]_+.

右边增加的余龄项非负，仅为上界；没有声称它是实际尾。归一化 i=q_old t 与 d w_i 界准确产生 u^2/q_old，e 与 square 项没有分别改值。Q3CHAND quadrature/endpoint 完整独审叶包含支撑端导数跳差、BV 核误差 TV<=10/3、全积分凸性、两端完整 log 正余项，给整个范围

    q_old^-1 sum_(i>=1)G_x(i/q_old)<CH,
    CH=17160482889458863049/148731921929151943800.

故 e Hhead<u^2 CH；e=0 时仍严格，因为 CH>0。

## 7. 全龄二次价和最终连续预算

共享 AJ 的完整独审人工叶从全 N 正混合、两个边界、Bernoulli 及一般 Faulhaber 给

    Jminus<q_old^4 J(q_old),
    J(q)=(q+1)^4/[324q(q-4)^3]+(q+1)^2/[36q^3(q-4)].

这是同一个 J_i、R、alpha_p、w_i，不是另一个归一化 square 价。所有分母 q>=10 正；完整 112 槽中 60 非零的有限身份和全龄尾均在正文。仍用同一 e，

    e^2 Jminus<d^2 u^4 J(q_old)<=u^4 J(q_old).

e=0 时比较也严格，因为 J(q_old)>0。原实际 master-floor 给

    Ffloor>Lb(q_old)=69/500-u^2 CH-u^4 J(q_old).

精确一般导数为

    [(q+1)^3/q] Lb'(q)=-2CH+A(q)+Bq(q),
    A(q)=q(q+1)^3/[27(q-4)^4],
    Bq(q)=(q^2-2q+2)/[18q(q-4)^2].

A 的 log 导数 1/q+3/(q+1)-4/(q-4)<0，Bq'=(-q^3-6q+8)/[18q^2(q-4)^3]<0。所以 Lb' 至多一次从正变负，内部极小不可能，最小值在 10 或 21。两个完整正余量为

    Lb(10)-1/40=195098675960795601986623/65597470507242819053271000,
    Lb(21)-1/40=713805528405149594753/359931251068547703996000.

均严格正。于是原实际 Q3c 分支 Ffloor>1/40>0，由 §1 原解析入口 D>0、Zact>0、v'<0。h、q_old 的闭边界均覆盖，实际 h>0、e>0 条件从原 hard 入口保留。不扩大 lambda 域或树律类。

## 8. 数学依赖图、历史引用及有限算术诚实账本

有向数学图为：原 canonical/实际响应/entropy/master-floor入口 → same-e 不等式；共享 Lambert 源 → 源/间隙与原尾五矩；同-a 全部 a>=1 重证 → D_i(alin)；原 G 身份 → U/H/h0 F 正性 → 积分 F>0；共享价格/shape → 全龄负部支撑；双曲全龄权 → Gx；Gx 完整 BV/log → CH；共享 AJ → J；CH/J 与两端形状预算 → Ffloor>1/40 → 原 Q3c 速度分支。每个源/接口的固定正式收据需实读及检查依赖。

不接受旧 head N/M、旧 same-e §3 或旧整体 same-e PASS 为新图前提。旧保存清单、审计 INPUTS 和完整历史封存包可能包含它们的 bytes/hash，属于历史/来源校验，**不是数学使用**；若任何新接受叶的论证实际上从旧正性得到所需结论，独立审计必须判循环并拒绝退出。

新 H 核心有限工作为：746 个普通身份项（18 leading+728 remainder）；362 负 remainder 系数合并 20 组；24 个小角点多项式共 431 个非零普通系数；108 条 h-Bernstein/shifted-t Horner 链共 600 完整系数槽；20 舍入帽及 60 分区付款。上述计数重叠，不能加称独立系数总数。另有同一 h0 F 的 128 槽/82 非零、32 控制和 8 g/t、8 x 付款；U 三分区、一般指数全尾和小有理付款。共享源/间隙 256 槽/96 非零及共享 AJ 112 槽/60 非零是原有人工叶，单列为全链既有有限成本。

旧主头 40706=2042+38664 非零；新 H 身份 746 相比约 54.57 倍减少（身份输出数口径，**不是**运行复杂度或全链总数）。实质结构改善是降低到 H 一阶余项，保留完整极点一次信用，用真实 q/W corridor 及凹性/仿射角点、按 20 组付款后积分。新链仍用完整有限恒等式、小角点、Bernstein/Horner 与有理支付，故也包含较小精确证据的重写，不能称“完全无证书”。

只有唯一辅助在固定全文、完整数学叶及真实接口上保存全链 FINAL PASS 后，才可在新依赖清单记录 40706 不再是 Q3c 必要证据。旧源、原表和旧回执永远保留。Q1 13904、hybrid 3852 的必要性没有由本装配改变；后续按准确清单另做，不据本分支签整体速度定理。
