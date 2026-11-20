# 完整归一化 J1：从原根与三龄到全矩形正下界的逐步人工正文（LOCAL 待最终独审）

2026-10-07。主任务为本轮原生成稿作者，原唯一辅助负责独立核验；没有新增辅助或重启旧任务。
旧文件、旧程序证书及失败稿全部保留。本稿完整嵌入所需原生成、连续比较、全部有限表和付款；
读者可以只按纸面有限乘加、短除法和分数交叉相乘复核每步。
仍有大量整数算术，不能把附上80系数等同免核验，更不能把本局部结果称整体速度人工定理。
LOCAL 标签表示本组装稿尚需独审；各已审局部命题的状态按固定回执判定。

## 1. 精确局部命题、完整原函数和正分母

本稿目标是

    F(l,u)>57/100>11/20，
    23/20≤l≤H=707/500，0≤u≤1/2。                    (J1)

这是原归一化代数付款 F=(25p+C0)/(kA)，不是速度本身。
设 t=1−u，k=1−lu，A=1+lt，S_j=Σ_(i=0..j−1)l^i，Zj=Sj−(Sj−1)u，

    K=(l+1)/(2l)+t/2+(l+1)(2lt−l+1)t/(24l)，h=K−t，
    G=2A−1−l/A，G_rho=−1−2l/A，
    Hroot=A−lu/A，Hroot_rho=−2lu/A，
    Broot=A(G−K Hroot)，
    Broot_rho=u(A+1)G+A G_rho−A(2h Hroot+K Hroot_rho)，
    R=2[(25+l/k)Broot−Broot_rho]/(lA²)。

对 (j,n)=(2,1),(3,3),(4,6)，令 m=24−2n，

    rj=Zj/Z_(j+1)，vj=lZjZ_(j−1)/Z_(j+1)²，fj=2−rj−lrj²，
    Tj=2j l^(j−2)/Zj³ * {fj[m−u−u/A]
          +uZj/Z_(j−1)[−(24−n)K+2h+vj(mK−2h)]}，
    F=R+T2+T3+T4。                                    (1)

一切价格和三龄都在(1)中。Broot/Hroot 只为避免与下文 B=l+1、H端点混名。
原带 rho 下标是指定的原 rho 导数，下面 F_uu 是 u 导数。
全域 l>0、k≥1−H/2>0、A≥1+l/2>0、Zj≥(Sj+1)/2>0，故(1)光滑。

取 rho=l/(l+1)，xa=1−rho u，y=u/xa；qj=1−1/Sj、qk=l，
dj=1−(qj−rho)y，dk=1−(l−rho)y。
主文另明确 A 极点约定 q_a=rho、d_a=1、c_ar=c_2r（r=1,2,3,4），与附录 I 完全一致。
y 对 u 与 l 均增加，故

    0≤y≤(H+1)/(H+2)=1207/1707<71/100，
    71/100−1207/1707=497/170700>0。                    (2)

xa>0，dj=(1−qj u)/xa>0，dk=k/xa>0。
附录 I 的完整移动极点证明给全部光滑主部 c_jr 的有限提取，
以及二次余项 −23(l+1)/(6l) 的二阶贡献；第二龄末项在无穷远为 O(u)，不是 O(1)。
没有从一个根代理推完整身份。

## 2. 原移动极点到同参数联合上界

对 ma=4、m3=m4=3、m5=2，定义

    Nj(y)=Σ_(r=1..mj) r(r+1)c_jr dj^(mj−r)(1+rho y)^(r−1)/2，
    Pa=rho²Na=p0+p1y+p2y²+p3y³。

附录 I 完整证明有限主部无尾与正规化二阶身份，乘正 d4⁵ 得

    X=xa³d4⁵F_uu/2
     =Pa d4⁵+q3²N3(d4/d3)⁵+q4²N4+q5²N5 d4⁵/d5⁴
        +ck l²d4⁵/dk³−23(l+1)xa³d4⁵/(6l)，              (3)
    ck=(l−1)²(−l³+23l²+l+1)/(12l⁴)>0。

后一个正性由 l<2 得括号>21l²+l+1。N3/N4二次、N5线性；
这里的 N3 不等于附录 III 上边界导数的同名分子，也不等于均值分子 N_orig。

设 B=l+1、L2=1+l²、D=l²/(B L2)、e=l³/(S3S4)、z=l⁴/(S4S5)。
附录 II 从原 c 提取，经有限生成和完整连续符号付款给

    Pa>59/16>0，p2>0，p3=−80l⁴/B⁸<0，
    N3>−9，N5=t0+t1y<0（0≤y<1），t1>0。             (4)

附录 IV 的几何比较完整证明 r3=(d4/d3)⁵ 的双边包络
L=1−5ey−y²/50≤r3≤U=1−5ey+y²/20。
由于 N3+9>0，准确地

    N3r3=(N3+9)r3−9r3≤(N3+9)U−9L
                             =N3U+(63/100)y²。        (5)

这是允许变号的比较；不能将 N3 当全正。
附录 V 以精确有限几何式给

    d4⁵≤Ra=1−5Dy+10D²y²−5D³y³，
    d4⁵/d5⁴≥R45=1+(4z−D)y+10z²y²+10z²(D+2z)y³
                                  −4Dz(D²+5Dz+5z²)y⁴。 (6)

Pa>0 和 N5<0 分别保证(6)两个乘法的正确方向。
附录 IV 还证明 d4⁵/dk³<5 及23(l+1)xa³d4⁵/(6l)>3/4。
故在同一个 l,y 下，由(3)–(6)得完整严格上界

    X<P=Pa Ra+q3²[N3U+(63/100)y²]+q4²N4
                  +q5²N5R45+5ck l²−3/4
       =Σ_(i=0..6)bi y^i。                             (7)

修正项有 q3² 前缀。Pa/N3/N4/N5 均来源于(1)全部价格，
没有用独立绝对极值替代共享参数。

## 3. 七个系数界及实际依赖

完整原生成证明及连续付款已全部嵌入以下附录，得

| 系数 | 全域严格界 | 完整来源 |
|---|---|---|
| b0 | −1867/300 | 附录 I：原u²三元乘法、四身份、72槽、13付款 |
| b1 | 48/5 | 附录 II 的原有已审 Pstar/A1 全文：15奇偶块、25+24导出槽 |
| b2 | −87/10 | 同文：原均值下界、Pstar31、正支路的凹平方根弦方向 |
| b3 | 7 | 附录 II：原三分项、G18/A17/W21有限生成及连续分组 |
| b4 | 5 | 附录 II：原四分项、正几何、GU/GW及正确M3修复 |
| b5 | 0 | 附录 V：−5D³p2、10D²p3、−4q5²t1Dz(D²+5Dz+5z²)三个负项 |
| b6 | 1/20 | 附录 V：b6=400l¹⁰/[B¹¹L2³]及两平方不等式、683/76160付款 |

b6实际为正，但只需它的严格上界。
附录 II 中的 b2 点态上界包含 q3²·63/100 的校正；它不是原 u-Taylor 的 F 系数。
原均值下界 N_orig<0 本身不能给点态上界；Pstar>0 先给 M>0，
随后乘凹平方根的弦下界，方向才合法。b1则用平方根上界；两者不能交换。
已经有完整原生成纸面的 G/J3、J5 和这两支路在本轮直接复用，不重复开发。

## 4. 全域曲率的短终端付款

由 y≥0、上述七界及 b5<0，

    P<J(y)=−1867/300+48y/5−87y²/10+7y³+5y⁴+y⁶/20。 (8)

即使 y=0，b0 严格界仍给严格不等式。
J'=48/5−87y/5+21y²+20y³+3y⁵/10。
前三项配方得

    21(y−29/70)²+4197/700，

其余两项在 y≥0 非负，故 J'>0。
用分数乘加和交叉相乘作唯一终端付款

    J(71/100)=−638236148237/60000000000000<0。           (9)

因此 X<P<J(y)≤J(71/100)<0。
由 xa³d4⁵/2>0，得原完整 F 在全矩形满足 F_uu<0。
这一步使用完整函数和全部已付条件，并非仅点上曲率或固定 l 边界。

## 5. 两条 lambda 边界、两端付款和完整 J1

附录 III 全文给原完整根与三龄的两条连续证明及所有原有限身份：

    F_l(l,0)>1/4，F_l(l,1/2)>0；
    F(23/20,0)>57/100，F(23/20,1/2)>21/25。            (10)

端点记录八个原分项分值和八次逐次加法，故不借旧固定 l 曲率证书。
由(10)的 l 单调性，F(l,0)>57/100、F(l,1/2)>21/25。
固定任意 l，F_uu<0 给凹函数弦

    F(l,u)≥(1−2u)F(l,0)+2uF(l,1/2)>57/100>11/20。     (11)

(11)含 u=0、1/2 两边，严格性来自两端付款；在内部曲率弦也严格。
这是(J1)的完整局部证明，可替换六 Taylor 矩形在该原目标的用途。
旧矩形证书仍保存，整体速度证明仍有其余计算依赖。

## 6. 精确人工算术清单：读者仍须完成什么

本稿把表作为原有限规则的输出；下表逐项列出必须复核的运算。
各集合大量重用，不应将行数相加为宣传性的“总输入”，也不主张整数或正文长度减少。

| 支路 | 须核对的表及有限算术 | 连续比较由什么给出 |
|---|---|---|
| 原完整移动极点 | 原三龄四项及根分解；各极点全部光滑M；四个A、三个Z3、三个Z4、两个Z5主部的有限提取；k主部；次数≤2余项与二次系数 | 清除全部主部后有限多项式及原无穷远增长，无数值符号假设 |
| G/J3 原共同生成 | 20个有限jet；103完整原单项（不可只取均值列）；13偶块及分母上界；x=0/−1/−2等短除法行；六G及五J付款、端值 | 完整倒数种子、G凸性、J3单调/凹性，原符号分组 |
| J5 原共同生成 | 两epsilon系数；W/R到5阶递推；五平均块；全部低次分子和四次/一次部分除法；导数和端点付款 | U凸、V凹、仿射组合方向 |
| b1/b2 | 15E/O块；原奇偶种子及多项式乘法；DxE1/DxO1四最高行抵消；Pstar31、Estar25、Bstar24共80完整槽；Pstar首6/末25尾支付、A1二次头支付 | 先证明各分子有限且次数≤30/24/23，再用整个区间的连续符号，N<0与M>0、平方根上下界各自正确方向 |
| b0 | K/P/E/V和原根U三元；四个二阶式；每项分母包络；P18/P28最高抵消；9+15+19+29=72槽；24移位槽；G3/G4共48槽（复用72）；13完整有理付款 | GR/GA凹性、G3/G4单分界幂、正几何方差给分母均值，K3/K4递减、k项递增 |
| Pa/N3/N5/b3/b4 | 原raw与均值记号区分；九个原分母/增长界，j5 aq5−I抵消；18向量共245完整槽及p3单项；N3导数有限式；W21 l²B整除与最高抵消；Q4/V7/GU/GW/zR有限生成；19付款 | 所有负项配对、单中心幂、正几何方差、z强凸；M3必须用184/l²+132/l³−88/l⁴，不能用失败旧指数 |
| 比率及高次 | 小几何恒等式、r3二次导数、四主付款及各粗界；Ra/R45准确乘积；b5三负项、b6两平方及683/76160 | 允许N3变号；rk对y/l双单调，末负余项量化 |
| 零边界 | 原根短分式；原年龄有限几何和到六X/Y身份；六对数导数界；R0'(10/7)和三个B付款 | 正几何因子、逆幂单调，全部连续方向在附录 |
| 上边界 | 三个C及J/a/b线性种子；根共同分子六槽、2/3/1项三次短除法；九个K商法则；11+15+24=50槽；两高幂付款与低幂配对 | 原有价格compact三项；先证明有限次数10/14/23，再作显式连续配对 |
| 两端及终端 | 八个R/T2/T3/T4分数；八次未约分加法与约分等值；两个正差；配方4197/700、y上界497/170700、J付款(9) | 先有边界单调和完整曲率，再用端点弦；点值不能独自证明连续域 |

这是一份无需运行程序也能逐步核验的证明正文。
不同算法的程序确实核对全部输出等号，人工独审另外检查原生成、次数、每个连续方向及连接逻辑；
这些事实不等于声称审计者已仅用纸笔逐个重算全部大整数。
精确证书是辅助证据；这里的证明依据是正文中公开的有限规则、全部输出和连续论证。

## 7. 来源分类、旧状态和整体限制

本轮先以 J1HAND_CONTINUATION_INDEPENDENT_DEPENDENCY_REVIEW_LOCAL_20261007.md
分类A（原纸面完整）、B（符号已付、身份桥薄）、C（端点叶子待展开）。
只补B/C：优先b0，随后自然系数与b3/b4，再上边界和端点；A原全文直接嵌入。
80槽原b1/b2在前轮已经有有限人工生成，不再将它们视为新未付款的程序证书。
原106旧高次A1/A2和六Taylor矩形不在新主链中；它们及其失败/成功记录均不删除。

旧暂停点和MANIFEST均可读且全部匹配；J3第二段的真实独审证据已找到并保存，
不以父对话的口头通过替代实际回执。y=0末行正确版本用≤，历史<版本保留。
J3两段及其后原生成人工支路的固定来源在先前完整来源包和本轮封存包中。

整个速度单调性研究仍是原限定范围的 COMPUTATIONAL：
1<lambda<m、mu0=0、mu1>0、有限均值、ordinary GW root、实际terminal-one canonical escape law。
跨lambda=1未闭合，general canonical S42完整floor OPEN，旧Mellin V3 FROZEN；
Mellin勘误仍是 a_(n+1)−lambda*a_(n+2)。本稿只完成J1局部人工化，不扩张整体定理。
没有当前授权阻碍；历史被拒绝ps诊断仍停止，未重试、提权或绕行。

## 8. 完整附录：原生成、全部有限表和连续付款逐字保存

以下不是只有参考文献清单。正文全部嵌入；历史LOCAL/条件文字保留其当时范围，
当前整体组装状态只由本稿前言和针对固定稿本的最终独审回执决定。
附录中同名局部符号以其独立小节定义为准；尤其正文U2r为raw，附录均值U2r为avg。

---

## 附录 I：原 b0 三元生成、次数与全部算术（含原移动极点全文）

原文件 J1HAND_CONTINUATION_STANDALONE_B0_ORIGINAL_MANUAL_PROOF_LOCAL_20261007.md，bytes 23300，SHA256 39cdc45de884219dcbd09afac3f6720e342757ec76e93cbbeb9d5090cb96dd3e。

# J1 强常数 b0：原二阶生成到完整有限付款（LOCAL 待独审）

2026-10-07，主任务作者，原唯一辅助独立核验；不改已有已审文件。
这里只补齐此前原身份算术桥，已有连续比较复用并完整写明。
72 个多项式系数和13条付款仍须执行有限算术核验，列出它们并不自动免核。

## 1. 对象、完整原式和结论

l∈[a,H]=[23/20,707/500]，B=l+1，S_j=Σ_(i=0..j−1)l^i，q_j=1−1/S_j，rho=l/B。
完整原F是原根R加全部T2,T3,T4及同一价格K；完整原分解/身份原文在附录逐字提供。
原联合曲率上界的常数为

    b0=eR+23B/(6l)+e2+e3+e4+4ck l²−3/4，
    eR=[u²]R(l,u)，ej=[u²]Tj(l,u)，
    ck=(l−1)²(−l³+23l²+l+1)/(12l⁴)。                       (1)

该式由完整移动极点身份取y=0、所有比率包络常数为1而校正为0取得。
要证 b0<−1867/300；不会由它单独宣告完整J1曲率或整体速度定理。

## 2. 三元有限乘法代替求导黑盒

所有三元组表示到u²的系数，余项不参与所取系数。
乘法为 (ab)_i=Σ_(k=0..i)a_k b_(i−k)，0≤i≤2；若d0≠0，

    (1/d)0=1/d0，(1/d)1=−d1/d0²，
    (1/d)2=d1²/d0³−d2/d0²。                              (2)

因Zj=Sj(1−qj*u)，对任意有限非负整数指数r_j，令

    H_r=∏Sj^(−r_j)，A_r=Σr_j qj，
    C_r=[A_r²+Σr_j qj²]/2，
    ∏Zj^(−r_j)=H_r(1+A_r u+C_r u²)+O(u³)。                 (3)

(3) 由每个(1−q*u)^−r的二阶系数r(r+1)q²/2与有限乘法得到。
故对三元(P0,P1,P2)，定义

    L(P0,P1,P2;r)=H_r(P2+A_rP1+C_rP0)。                   (4)

这就是所有后续原二阶系数的全部求值规则，没有调用求导程序。
S1=1、q1=0，所以j=2的Z1因素也被准确保留。

## 3. 同一个K、P、E、V的全部初始三元

直接代t=1−u于原二次K，得

    K0=(l²+26l+13)/(24l)，K1=−(3l²+16l+1)/(24l)，K2=B/12，
    h=(K0−1)+(K1+1)u+K2u²。

对(j,n)=(2,1),(3,3),(4,6)，m=24−2n，原P=m−u−u/A，A=B−lu，
故P三元为

    (m,P1,P2)=(m,−1−1/B,−l/B²)。

原E=−(24−n)K+2h、V=mK−2h，只需

    E0=−(22−n)K0−2，E1=−(22−n)K1+2，
    V0=(22−2n)K0+2，V1=(22−2n)K1−2。                     (5)

原年龄四项恰为

    Tj=2j l^(j−2)[2P/Zj³−P/(Zj²Zj+1)
            +l(uV−P)/(Zj Zj+1²)+uE/(Zj²Zj−1)]。

各三元为P=(m,P1,P2)、uV−P=(−m,V0−P1,V1−P2)、uE=(0,E0,E1)。
所以 **完整原ej的显式生成式** 是

    ej=2j l^(j−2){2L(m,P1,P2;{j:3})
       −L(m,P1,P2;{j:2,j+1:1})
       +lL(−m,V0−P1,V1−P2;{j:1,j+1:2})
       +L(0,E0,E1;{j:2,j−1:1})}。                         (6)

例如第一括号直接是[ P2+3qj P1+6qj²m ]/Sj³；
第二括号是[ P2+(2qj+qj+1)P1+(3qj²+2qj qj+1+qj+1²)m ]/(Sj²Sj+1)。
其余两项同(3),(4)，因此只需三项乘加，价格未被删去。

## 4. 原完整根的生成及抵消

附录的根分解R=Rreg+U1/A+U2/A²+2u/A³，price=25+l/k，k=1−lu。
其三元是(25+l,l²,l³)。由原分解先消去2h−2u=2K−2，得

    [u²]Rreg=2/l[l³(2−K0)−l²K1−(23+l)K2]。

再由U1=2(1−u−price)/l及
U2=2/l[price*l(Ku−1)+u+2l+lu−2(h+K)lu]，收集得

    U10=−2(24+l)/l，U11=−2(1+l²)/l，U12=−2l²，
    U20=−2(23+l)，U21=2[(21+l)K0−l²+3]+2/l，
    U22=2[(21+l)K1+l²K0−l³−2]。

于是 **完整原eR的显式生成式** 为

    eR=2/l[l³(2−K0)−l²K1−(23+l)K2]
       +(U12+rho U11+rho²U10)/B
       +(U22+2rho U21+3rho²U20)/B²+6rho/B³。              (7)

最后一项来自2u/A³的一次乘法。这里可逐行看到价格、K和h的全部贡献。

## 5. 四个有限多项式及无尾次数闭合

定义

    D3=4B⁴(1+l²)⁴S3⁵，D4=3B⁵(1+l²)⁵S3²S5⁴，
    W8=−12lB⁴(eR+23B/(6l)+5)，
    W14=6lB⁵S3⁴(1−e2)，P18=−D3e3，P28=−D4e4/(2l)。      (8)

这些定义与(6),(7)给出原身份，不能先把下文整数数组当作(8)的前提。
各l^−1来自K的分母，在W8/W14的l、e3前缀l、e4/(2l)前缀l中消除。
下表逐个原年龄四项列出消去该l以后可取的几何分母包络。
L2=1+l²；分母为包络表示每一项的实际分母整除它，忽略有理常数。

| j | 第1项 | 第2项 | 第3项 | 第4项 |
|---|---|---|---|---|
| 2 | B⁵ | B⁴S3³ | B³S3⁴ | B³ |
| 3 | B²S3⁵ | B³L2³S3⁴ | B⁴L2⁴S3³ | B²S3³ |
| 4 | B⁵L2⁵ | B⁴L2⁴S5³ | B³L2³S5⁴ | B³L2³S3² |

使用S4=B L2，各清分母因子恰覆盖全部包络。
根(7)只需lB⁴，故(8)都是真正有限多项式，未假定形式级数末项零就没有尾。
无穷远增长度也可直接核：eR≤3，e2≤−1，e3暂≤−3，e4暂≤−5。
因此次数先≤8、14、19、29。
第4项还保留一个关键抵消：K0=l/24+O(1)、K1=−l/8+O(1)，
2qj+qj−1=3+O(1/l)，所以

    E1+(2qj+qj−1)E0=O(1)，不是O(l)。

其他三项更低，故e3≤−4、e4≤−6，把P18/P28的次数降为18/28。
等价的有限最高行为[P18]19=0、[P28]29=0；不靠程序截断推出该事实。

## 6. 72个系数的公开有限生成配方

从S_j的全1系数、l=(0,1)、B=(1,1)、L2=(1,0,1)开始；
加法逐槽相加、乘法有限卷积。每个非零常数分母d的除法为

    q0=a0/d0，q_i=(a_i−Σ_(k=1..i)d_k q_(i−k))/d0。        (9)

原l^−1只作指数平移，在第5节的前缀中显式消除后才用(9)。
把(5)–(8)逐项应用(9)，只算到已证明的8/14/18/28，即得以下完整输出。
其中72=9+15+19+29；高消去行若采用暂次数19/29则另外两行精确为0。

| i | W8 | W14 | P18 | P28 |
|---|---:|---:|---:|---:|
| 0 | 21 | -21 | -19 | -8 |
| 1 | -202 | 41 | 291 | 101 |
| 2 | -684 | 1118 | 3182 | 1697 |
| 3 | 1083 | 348 | 9837 | 8773 |
| 4 | -130 | -1196 | 20055 | 29383 |
| 5 | -44 | -1780 | 35634 | 75589 |
| 6 | -48 | 7214 | 58699 | 164217 |
| 7 | -21 | 10446 | 89223 | 315576 |
| 8 | 1 | 5676 | 127529 | 551472 |
| 9 | — | -4684 | 155230 | 887415 |
| 10 | — | -4028 | 154671 | 1323705 |
| 11 | — | -1308 | 124747 | 1830884 |
| 12 | — | 855 | 76133 | 2345458 |
| 13 | — | 33 | 31506 | 2772762 |
| 14 | — | 6 | 8897 | 3015892 |
| 15 | — | — | 1505 | 3007959 |
| 16 | — | — | 1710 | 2743705 |
| 17 | — | — | 2651 | 2281048 |
| 18 | — | — | 1255 | 1724386 |
| 19 | — | — | — | 1182889 |
| 20 | — | — | — | 737577 |
| 21 | — | — | — | 419907 |
| 22 | — | — | — | 221469 |
| 23 | — | — | — | 110303 |
| 24 | — | — | — | 53093 |
| 25 | — | — | — | 24282 |
| 26 | — | — | — | 9858 |
| 27 | — | — | — | 2992 |
| 28 | — | — | — | 544 |

例如W8的常数21与首阶−202，可由(7)先乘12lB⁴再用(9)两行核定。
所有其余行同样有唯一明确算术配方；长表仍是必须核验的工作，不能由其被展示自动签发身份。

令c=l−1，移位只需

    [c^i]W(1+c)=Σ_(r≥i)W_r binom(r,i)。                  (10)

把W8/W14低0..7阶保留，得

    GR=−24+512c+212c²−1516c³−1735c⁴−717c⁵−167c⁶−13c⁷，
    GA=12720+65400c+101416c²−87404c³−553834c⁴
                   −899167c⁵−739702c⁶−273390c⁷。

其正尾分别是c⁸及
c⁸(50154+106803c+53458c²+13710c³+1830c⁴+117c⁵+6c⁶)，
也必须由(10)逐槽核验，不能用正性猜测身份。

## 7. 完整连续付款

c∈[3/20,207/500]，GR''≤424−9096*(3/20)=−4702/5<0，
GA''≤202832−524424*(3/20)−6646008*(3/20)²=−1268339/50<0。
其他二阶导数项负，因此这些是上界。13个正差的前四条证明端点GR>50、GA>19000，
凹函数高于端点弦，得全域W8≥GR>50、W14≥GA>19000。
又l<10/7、B<17/7、S3<219/49，用第11、12条正差，得

    eR+23B/(6l)<−61/12，e2<19/20。                       (11)

P18、P28只有负常数，分别由291l−19、101l−8吸收，所以二者正。
令

    G3=12P18−lP18'−228(l−1)，
    G4=37P28−2lP28'−296(l−1)。

G3的逐槽系数是(12−i)P18_i，再作两个常/一次调整；
G4是(37−2i)P28_i，同理。完整分界为：
G3常数0，幂1..11正、幂12为0、幂13..18负；
G4常数0，幂1..18正、幂19..28负。
因此G3/l¹²、G4/l¹⁹严格递减；第5、6条给右端正，于是二者全域正。
加回正补偿，得lP18'/P18<12、lP28'/P28<37/2。

对正系数有限几何和S，令w_i=l^i/S，mu=lS'/S，则

    l mu'=Σi²w_i−(Σi w_i)²=(1/2)Σ_(i,j)(i−j)²w_iw_j≥0。

L2同理；分母对数导数是这些均值的正整数和。因此lD3'/D3、lD4'/D4非递减。
第7、8条左端付款使全域分别大于12、39/2，故
K3=P18/D3、K4=2lP28/D4均严格递减。
第9、10条右端付款遂给e3=−K3<−31/20、e4=−K4<−11/10。      (12)
不得把方差用于有负常数的P18/P28。

对g=ck l²=(l−1)²f，f=(23−l+1/l+1/l²)/12，
1<l<2时f>21/12、−1/3<f'<0，故
g'=(l−1)[2f+(l−1)f']>0；第13条给4g(H)<131/100。          (13)

## 8. 全部13条有限有理付款

每项由(8)–(10)和有限几何和定义，端点用有理Horner逐项求值。
本表是运算结果；每个等号也需要核验，而不是只见正分子就略去等号来源。

```text
1. GR_low_minus50 = 1944044309/1280000000 > 0
2. GR_high_minus50 = 48244460307910800641/7812500000000000000 > 0
3. GA_low_minus19000 = 660392929651/128000000 > 0
4. GA_high_minus19000 = 372066455701670327623/781250000000000000 > 0
5. G3_high = 10722705645044890500791022208991057609443433341078783053/381469726562500000000000000000000000000000000000 > 0
6. G4_high = 22873115990932986386900132081770195342986851410752196028382399015827728478490158297/7275957614183425903320312500000000000000000000000000000000000000000000000 > 0
7. D3_mean_low_minus12 = 2946950/18495461 > 0
8. D4_mean_low_minus39_over2 = 6512473599591/39905103826082 > 0
9. K3_high_minus31_over20 = 71211294472584950474242920830799142022748849980946729435913906909/2438239495229468824479324272272914332442878631142401818710700705220 > 0
10. K4_high_minus11_over10 = 117466532707398063706520135616133782811070033790520330882536258505004684573745514290540757598671800383881/5398190480980487774255365966252147734763283146369805522952837782045571167607459388013544765819389272378290 > 0
11. root_denominator_gap = 257/501126 > 0
12. age2_denominator_gap = 3088128155147509/195962204579669820 > 0
13. k_high_gap = 485446619269/62481125000000 > 0
```

由(1),(11)–(13)，在同一完整参数域上

    b0<−61/12+19/20−31/20−11/10+131/100−3/4
       =−1867/300。                                      (14)

## 9. 准确成本和剩余

本局部纸面给原u=0三元生成、四项抵消、清分母包络、次数闭合、72系数的有限除法、
移位、两分界、13有限付款及连续符号；程序只作独立交叉核验。
人工核验仍包括72槽与两个高抵消行、24个完整移位槽、两分界的48槽算术、13分数等号及正差。
这几个集合有复用，不是相加后就得到所有整数出现总成本；未称72表已自动免核。
整体J1的其他生成身份、其他系数及边界仍在本轮继续梳理，本稿不是完整J1最终PASS。
失败源/旧稿保留；原限定全速度范围和OPEN/FROZEN项不变。

## 附录：原完整移动极点身份证明（原已审来源，逐字保留）

# Complete normalized J1: independent moving-pole curvature identity

2026-10-07. **Complete LOCAL identity proof, independently reconstructed
by the sole auxiliary; actual exact checks PASS.** This is a rational
identity, not a curvature sign estimate or a complete replacement of
the six Taylor rectangles. All original files remain unchanged.

## 1. Complete original input and statement

For 23/20<=lambda<=707/500 and 0<=u<=1/2 set
\[
t=1-u,\quad k=1-\lambda u,\quad A=1+\lambda t,
\quad S_j=\sum_{i=0}^{j-1}\lambda^i,\quad
Z_j=S_j-(S_j-1)u,
\]
\[
K=\frac{\lambda+1}{2\lambda}+\frac t2+
\frac{(\lambda+1)(2\lambda t-\lambda+1)t}{24\lambda},
\quad h=K-t.
\]
The complete normalized F is the original root plus ALL three ages
in Section 2 of
`COMPLETE_FIRST_JOINT_BUDGET_SIX_COUPLED_TAYLOR_RECTANGLES_20261007_LOCAL.md`.
Explicitly,
\[
G=2A-1-\lambda/A,\quad G_\rho=-1-2\lambda/A,
\quad H=A-\lambda u/A,\quad H_\rho=-2\lambda u/A,
\]
\[
B=A(G-KH),\quad B_\rho=u(A+1)G+AG_\rho-A(2hH+KH_\rho),
\]
\[
R=\frac2{\lambda A^2}[(25+\lambda/k)B-B_\rho].
\]
For (s,n_s)=(2,1),(3,3),(4,6), write
\[
m_s=24-2n_s,\quad P_s=m_s-u-u/A,
\quad E_s=-(24-n_s)K+2h,\quad V_s=m_sK-2h.
\]
Then the original age, including its complete signed price, is
\[
T_s=\frac{2s\lambda^{s-2}}{Z_s^3}
\left[(2-r_s-\lambda r_s^2)P_s+
\frac{uZ_s}{Z_{s-1}}(E_s+v_sV_s)\right],
\]
\[
r_s=Z_s/Z_{s+1},\quad
v_s=\lambda Z_sZ_{s-1}/Z_{s+1}^2,
\qquad F=R+T_2+T_3+T_4.
\]
The labels rho on G_rho,H_rho,B_rho refer to the prescribed original
rho derivatives; all later primes and F_uu below are u derivatives.

Define
\[
q_a=\rho=\lambda/S_2,\quad q_j=1-1/S_j\ (j=3,4,5),
\quad q_k=\lambda,
\]
\[
x_a=1-\rho u,\quad y=u/x_a,\quad
d_j=1-(q_j-\rho)y,
\qquad (m_a,m_k,m_3,m_4,m_5)=(4,1,3,3,2).
\]
Below c_jr are the complete principal coefficients defined in
Sections 3–4. Let
\[
N_j(y)=\sum_{r=1}^{m_j}\frac{r(r+1)}2c_{jr}
d_j^{m_j-r}(1+\rho y)^{r-1},\quad P_a=\rho^2N_a.
\]
For a, d_a=1. The target identity is
\[
\boxed{\frac{x_a^3F_{uu}}2=
P_a+\frac{q_3^2N_3}{d_3^5}+\frac{q_4^2N_4}{d_4^5}
+\frac{q_5^2N_5}{d_5^4}+\frac{c_kq_k^2}{d_k^3}
-\frac{23(\lambda+1)}{6\lambda}(1+\rho y)^{-3}.}       \tag{1.1}
\]

## 2. Short exact decompositions from the original root and ages

Expand the original age braces without inequalities. Its exact
four-term form is
\[
T_s=2s\lambda^{s-2}\left[
\frac{2P_s}{Z_s^3}-\frac{P_s}{Z_s^2Z_{s+1}}
+\frac{\lambda(uV_s-P_s)}{Z_sZ_{s+1}^2}
+\frac{uE_s}{Z_s^2Z_{s-1}}\right].                 \tag{2.1}
\]
For a direct check, the third term combines
−lambda P_s/(Z_sZ_(s+1)^2) from −lambda r_s² with
u lambda V_s/(Z_sZ_(s+1)^2) from the v_s price.
The other terms are the remaining two f_s terms and remaining price.

The root has a similarly exact useful decomposition. Write
Q=25+lambda/k and
\[
U_1=\frac2\lambda(1-u-Q),
\]
\[
U_2=\frac2\lambda[Q\lambda(Ku-1)+u+2\lambda+
\lambda u-2(h+K)\lambda u],
\]
\[
R_{\rm reg}=\frac2\lambda[Q(2-K)+2h-2u].
\]
Expanding the original G,H and B_rho gives
\[
\boxed{R=R_{\rm reg}+U_1/A+U_2/A^2+2u/A^3.}        \tag{2.2}
\]
For example B=(2−K)A²−A−lambda+Klambda*u and
\[
B_\rho=u(2A^2+A-1)-\frac{\lambda u(A+1)}A
-A-2\lambda-2hA^2+2(h+K)\lambda u.
\]
Substitution immediately verifies (2.2), including the u terms in U2.
R_reg is regular at the A pole, although it still has the distinct
k pole. These are identities of the complete original root.

## 3. All regular numerators of the complete principal parts

The following explicit lists specify the entire principal part at
each pole. Every omitted part is regular at the designated pole,
as follows directly from (2.1)–(2.2). They also give a finite manual
route to every coefficient, without expanding a large bivariate
numerator.

### A pole (a, represented as j=2)

The complete A-pole part is sum_(v=1..4) M_av/A^v, where
\[
M_{a4}=-8u,
\quad M_{a3}=2u+8(22-u)+4u/Z_3,
\]
\[
M_{a2}=U_2-4(22-u)/Z_3+4\lambda u/Z_3^2+4uE_2,
\]
\[
\begin{aligned}
M_{a1}={}&U_1+4\lambda(uV_2-22+u)/Z_3^2\\
&+6\lambda u[-2/Z_3^3+1/(Z_3^2Z_4)
+\lambda/(Z_3Z_4^2)+E_3/Z_3^2]\\
&+8\lambda^2u[-2/Z_4^3+1/(Z_4^2Z_5)+\lambda/(Z_4Z_5^2)].
\end{aligned}                                                    \tag{3.1}
\]
Here the root supplies 2u/A³,U2/A²,U1/A. Age 2 supplies the fourth,
third, second and first poles obtained by P2=22−u−u/A. Age 3
supplies the middle single-pole bracket, including its original
uE3/(Z3²A) price. Age 4 supplies the final single-pole bracket.
Thus every root and age A contribution is included.

### Z3 pole

The complete part is sum_(v=1..3) M_3v/Z3^v, where
\[
M_{33}=12\lambda P_3,
\]
\[
M_{32}=6\lambda[-P_3/Z_4+uE_3/A]
+4\lambda(uV_2-P_2)/A,
\]
\[
M_{31}=6\lambda^2(uV_3-P_3)/Z_4^2
-4P_2/A^2+8\lambda^2uE_4/Z_4^2.                    \tag{3.2}
\]
These are precisely the age-3 triple/double/single terms, age-2
double/single terms and age-4 single price contribution. The root
is regular at this pole. This recovers the separately audited full
N3 principal part.

### Z4 pole

The complete part is sum_(v=1..3) M_4v/Z4^v, where
\[
M_{43}=16\lambda^2P_4,
\]
\[
M_{42}=8\lambda^2[-P_4/Z_5+uE_4/Z_3]
+6\lambda^2(uV_3-P_3)/Z_3,
\]
\[
M_{41}=8\lambda^3(uV_4-P_4)/Z_5^2-6\lambda P_3/Z_3^2.
                                                               \tag{3.3}
\]
Age 4 supplies all three orders and age 3 supplies the double and
single additions. Root and age 2 are regular here.

### Z5 pole

Only age 4 contributes, with
\[
M_{52}=8\lambda^3(uV_4-P_4)/Z_4,
\quad M_{51}=-8\lambda^2P_4/Z_4^2.                 \tag{3.4}
\]
Its other two terms are regular here.

### k pole

Only the original root's lambda/k factor contributes. At u_k=1/lambda,
\[
c_k=\left.2B/A^2\right|_{u=u_k}
=\boxed{\frac{(\lambda-1)^2(-\lambda^3+23\lambda^2+\lambda+1)}
 {12\lambda^4}}.                                 \tag{3.5}
\]
For a direct derivation, A(u_k)=lambda,
K(u_k)=1+(lambda+1)(lambda−1)²/(24lambda²),
G(u_k)=2(lambda−1), H(u_k)=(lambda²−1)/lambda.
Substitution yields (3.5), with no price omission.

## 4. Finite coefficient definition and completeness of pole matching

Put u_j=1/q_j. For a use S_a=S2,Z_a=A; for j=3,4,5 use S_j,Z_j.
All M_jv in (3.1)–(3.4) are regular near u_j. This follows from
the distinct ordered slopes
\[
0<q_a<q_3<q_4<q_5<1<q_k<2.
\]
For example, at the A pole the other values are
k=−lambda,Z3=−lambda,Z4=−lambda*S2,Z5=−lambda*S3,
all nonzero. No singular denominator is silently evaluated as regular.

Since Z_j=S_j(1−q_ju), expand M_jv about u_j and use
u−u_j=−(1−q_ju)/q_j. The COMPLETE standard coefficient is
\[
\boxed{c_{jr}=\sum_{v=r}^{m_j}
\frac{M_{jv}^{(v-r)}(u_j)}
 {(v-r)!\,S_j^v(-q_j)^{v-r}}.}                   \tag{4.1}
\]
This formula includes every signed contribution and all lower-order
terms generated by variation of higher-pole numerators. The finite
jets used in the new source are exactly these derivatives divided by
their factorials. In particular c_a4=−8/(lambda*S2³).

Equations (2.1)–(3.5) show that the only possible finite u poles of F
are these five, with orders at most (4,1,3,3,2). Subtracting
\[
\sum_{r=1}^4c_{ar}(1-\rho u)^{-r}
+c_k(1-\lambda u)^{-1}
+\sum_{j=3}^5\sum_{r=1}^{m_j}c_{jr}(1-q_ju)^{-r}
\]
therefore removes ALL finite poles. The remainder is a polynomial
in u. No separate unsigned bounding operation occurs in this argument.

## 5. Exact infinity degree and quadratic remainder coefficient

This is the important remainder check; a root-only calculation would
not by itself establish the complete remainder degree.

As u tends to infinity at fixed lambda in the stated interval,
\[
A,k,Z_j\ (j\ge2)=O(u)\text{ with nonzero leading coefficients},
\quad P_s=-u+O(1),\quad K,h=\kappa u^2+O(u),
\quad \kappa=(\lambda+1)/12.
\]
In the four age terms (2.1), the first two are O(u^(−2)), the third
is O(1), and the fourth is O(1) for s=3,4. For s=2 the fourth is
**O(u)** because Z1=1. Thus each complete age grows at most linearly;
one must not incorrectly treat all ages as bounded at infinity.

Use the exact root decomposition (2.2). Since Q=25+O(u^(−1)),
\[
R_{\rm reg}=
\frac2\lambda[-25\kappa+2\kappa]u^2+O(u)
=-\frac{46\kappa}{\lambda}u^2+O(u).
\]
U1/A is O(1), U2/A² is O(u), and 2u/A³ is O(u^(−2)). Therefore
\[
F(u)=\beta u^2+O(u),\qquad
\boxed{\beta=-\frac{23(\lambda+1)}{6\lambda}}.     \tag{5.1}
\]
Every subtracted standard pole term decays at infinity. The polynomial
remainder of Section 4 thus has degree at most two and its exact
quadratic coefficient is beta. Its linear and constant coefficients
are irrelevant after two u derivatives. This establishes the complete
remainder contribution, including the original ages.

## 6. Differentiation and the common y-coordinate identity

For a standard pole term, direct differentiation gives
\[
\frac12\frac{d^2}{du^2}\frac{c_{jr}}{(1-q_ju)^r}
=\frac{r(r+1)}2c_{jr}q_j^2(1-q_ju)^{-r-2}.
\]
The exact common-coordinate identities are
\[
x_a=(1+\rho y)^{-1},\quad
1-q_ju=x_a d_j.
\]
After multiplication by x_a³ the term becomes
\[
q_j^2\frac{r(r+1)}2c_{jr}
\frac{(1+\rho y)^{r-1}}{d_j^{r+2}}.
\]
Collecting the same pole powers over d_j^(m_j+2) gives precisely
q_j²N_j/d_j^(m_j+2). For a the denominator is one, giving Pa;
for k, m_k=1, giving c_kq_k²/d_k³. Finally the polynomial remainder
contributes beta*x_a³, which is exactly the last term in (1.1).
This proves the complete requested curvature identity.

All x_a and d_j are positive on the physical rectangle, but positivity
is needed only for later inequalities, not for the algebraic equality.
No Pa/Nj sign or curvature inequality has been inferred here.

## 7. Actual independent checks, comparison and status

Self-contained new source:
`J1_INDEPENDENT_MOVING_POLE_IDENTITY_20261007.py`.
It imports no research source, old certificate or runner. Its rational
coefficient arithmetic uses numerator/denominator polynomials in
QQ[lambda] and gcd reduction, rather than the main task's fraction-field
implementation. All smooth contributions above were independently
derived before comparison with the exploration source.

The actual completed run, exit code 0, checked:

1. The original full three-age braces against the four-term identities.
2. The complete original root+three ages against each of the four
   smooth principal-part lists PLUS an explicit regular remainder;
   after exact cancellation each remainder lacks the designated
   independent denominator symbol.
3. Finite exact local extraction at A,Z3,Z4,Z5, of orders 4,3,3,2;
   the k coefficient was independently obtained from the complete root.
4. Exact agreement with all three separately audited N3 coefficients;
   also c_a4 and the resulting Pa cubic coefficient
   −80lambda^4/S2^8 were checked explicitly.
5. Generic second-derivative and common-coordinate identities for
   pole powers r=1,2,3,4.
6. The exact K quadratic coefficient and beta, with the complete
   infinity-degree proof in Section 5.

Its final output was
`PASS full moving-pole curvature identity by complete pole matching and infinity`,
followed by a scope line excluding Pa/N5 signs, full F_uu<0 and removal
of the six rectangles. No sampled parameter sign is used.

The main exploration file
`j1_remaining_moving_pole_qq_laurent_jets_exploration_20261007.py`
was then read as a comparison. Its A,Z4,Z5 regular numerator lists
and its local-to-standard coefficient formula agree with (3.1),
(3.3), (3.4), (4.1), term by term. It was not imported or rerun as
the basis of this identity proof. The new proof also includes Z3,
k and the complete quadratic remainder, which that exploration
alone did not certify.

This is a complete LOCAL identity result with finite exact algebraic
checks, awaiting the main task's review of the new proof. It is not
an auxiliary independent final audit of its own newly written proof.
Pa/N5 signs and the final coupled curvature payment remain separate.
Old six-rectangle files and all prior audit files are retained, and
no full-J1 or overall speed-theorem status is changed by (1.1) alone.



---

## 附录 II：自然系数和 b3/b4（含原 b1/b2、G/J3、J5 全文）

原文件 J1HAND_CONTINUATION_STANDALONE_NATURAL_COEFFICIENT_MANUAL_PROOF_LOCAL_V2_20261007.md，bytes 100883，SHA256 52dc38ff2a46df6e8ed4c67586424b913671bf6c8ffae2449fe3ffaefcaa5412。

# J1 剩余自然系数：原有限提取、抵消与全部导出算术（LOCAL 待独审）

2026-10-07。主任务补齐 Pa/N3/N5、b3/b4 的原身份算术桥；唯一辅助独核。
原连续符号论证已审，完整正文在附录保留；新来源链须另获全文独审才算补齐。
18个完整向量共245槽是运算输出，另有p3单项；每个等号和19条付款仍须手核。
本稿不把附表、程序exit0或旧数学PASS自动等同人工已完成核验。

## 1. 共用原生成层与全部有限运算

l∈[23/20,H=707/500]，B=l+1、L2=1+l²、S_j=Σ_(i=0..j−1)l^i，
x=l+l^−1，rho=l/B、D=l²/(B L2)、d3=l²/(B S3)、e=l³/(S3S4)、z=l⁴/(S4S5)。
S4=B L2，q3=lB/S3，q5=lS4/S5，d5=q5−rho=l²S3/(B S5)。
原完整c2r/c3r及c51/c52用附录 A 的光滑主部和有限epsilon提取取得。
附录 A 同时逐字给出已审103单项及j5两式，读者可离开程序核验全部输入。
N4保留完整原有限定义及二次次数，不额外引入一个λ展开表。

对有限系数用卷积 (ab)_i=Σa_jb_(i−j)、三角除法
q0=a0/d0，q_i=(a_i−Σ_(j=1..i)d_jq_(i−j))/d0 (d0≠0)，
导数系数 f'_i=(i+1)f_(i+1)，移位 [c^i]f(1+c)=Σ_(r≥i)f_r binom(r,i)。 (1)
λ的负幂仅作指数平移，先用下节的显式前缀消除；其余种子B,L2,S3,S5常数全为1。
整个运算都是有限乘加和低次分母除法；下节先证明次数闭合，再列完整输出，绝不由截断尾零推无尾。

## 2. 原raw系数的分母包络与增长度

记u_jr=l²c_jr；本正文的 U2r（r=1,2,3,4）专指同一个原raw量 u_2r=l²c_2r。
它与附录 A 用来表示均值 avg(l²c_2r) 的同名 U2r 不同；正文(3)一律使用原raw，绝不先取均值。
附录 A 的103原单项末列虽取偶部，前三列就是完整原raw单项，不能只取均值。
逐行代入

    x=L2/l，x+1=S3/l，x+2=B²/l，x²+x−1=S5/l²。

所有单项的分母和增长度可直接收集为下表；忽略非零有理常数。
增长度表示分子次数减分母次数，形式无穷远只用于有理次数账，不扩张物理域。

| 原系数 | 分母包络 | 增长度上界 |
|---|---|---:|
| c21 | l⁴B³S3² | −1 |
| c22 | l³B² | −2 |
| c23 | l²B³ | −3 |
| c24 | lB³ | −4 |
| c31 | l⁵B S3 | −2 |
| c32 | l³B S3² | −3 |
| c33 | lB S3³ | −5 |
| c51 | l⁶B L2²S3²S5 | −2 |
| c52 | l³B L2²S3S5² | −5 |

根前四行从原U21..24单项直接看出。例如U21最多有l^−2、B^−3、S3^−2，
再除l²就是第一行；U32含1/(x+1)时抵消一个l，故c32只需l³。
c33=12l[18−S3/(lB)−S3/l²]/S3³，直接给第三极点的最后一行。

j5两行可进一步保持原抵消，避免扩大包络。
其u5=S5/(lB L2)、t5=−1/(lB L2)、a=S3S5/l³、I=B²L2²/l³，
故

    a q5−I=−B L2/l³，                                  (2)

因为lS3−B L2=−1。L0/L1均只需l²B L2²分母；
P50=12−S5/(lB L2)−S5/(l²S3)，
q5P51=1+B³L2²/(l²S3²)。
套原 c51=8[L1−(1+a)L0+(aq5−I)P50−q5P51]/(lS5)、
c52=8(L0−q5P50)/(lS5)，逐项即得两行包络。
K(t5)=O(1)、K1=O(l)、a=O(l³)、P50=O(1)，所以两增长度分别≤−2、−5。
这里先使用(2)抵消正高次项，没有把原两Laurent系数假定同时负。

## 3. Pa 四系数：有限原求和和低次收集

原定义

    p_i=rho^(i+2)Σ_(r=1..4)κ_r binom(r−1,i)c2r，κ_r=r(r+1)/2。

定义三个有限分子 A_p0、A_p1、A_p2，由原求和直接生成

    A_p0=6l²B³S3²(U21+3U22+6U23+10U24)，
    A_p1=−2lB³(3U22+12U23+30U24)，
    p0=A_p0/(6l²B⁵S3²)，p1=−A_p1/(2B⁶)。                (3)

每个单项分母都被前缀覆盖，故A_p0、A_p1都是有限多项式。
增长度上界分别给次数10、4。它们的11与5系数由(1)及附录原单项逐行产生。
p2更短，原U23/U24四项直接给

    6c23+30c24=[−24B−36lB−192l+1056l²]/(l²B³)
               =12(85l²−21l−2)/(l²B³)，
    p2=12l²A_p2/B⁷，A_p2=85l²−21l−2。

而c24=−8/(lB³)给p3=10rho⁵c24=−80l⁴/B⁸。
这两式没有新表输入，p0/p1的表则是(3)的有限输出，不是把它们当作新定义替换原Pa。

## 4. N3：三个原分子和导数的无分式生成

原 a0=c31+3c32+6c33、
a1=−2d3c31+3(rho−d3)c32+12rho c33，
a2=d3²c31−3d3rho c32+6rho²c33。
rho−d3=lL2/(B S3)，套第2节包络就得有限分子

    A0=−12l⁵B S3³a0，A1=−12l³B²S3³a1，A2=12lB³S3³a2。    (4)

因此a0=−A0/(12l⁵B S3³)，a1=−A1/(12l³B²S3³)，a2=A2/(12lB³S3³)。
增长度分别≤−2、−3、−4，清分母次数分别12、11、10，故A0/A1/A2次数≤10/8/6。
完整11+9+7槽用(1)从原c31/c32/c33生成；这27槽必须核验，不以旧源码等号代付。

导数不需再次注册一个无法追溯的身份。原a0商法则直接给

    6l⁶B²S3⁴a0'
      =[(5B S3+lS3+3lB S3')A0−lB S3 A0']/2=:W(l)。      (5)

W次数≤13；再用(1)移位c=l−1得到14槽W_c，而非由点值拟合。
原N3的连续下界证明使用这14槽的前5负、后9正模式，附录 B 完整保留其三条付款和方向。

## 5. N5：原两系数到U/V/W

原t0=c51+3c52、t1=−d5c51+3rho c52。定义

    U=3l⁴B²L2²S3S5² t1/2，
    V=−3l⁶B²L2²S3²S5²(t0+t1)/2，W=V+l²S3U。             (6)

第2节包络和d5=l²S3/(B S5)使它们有限；
t1增长度≤−3、t0+t1≤−2，前缀次数20、24给U≤17、V≤22；W≤22。
反解是

    t1=2U/(3l⁴B²L2²S3S5²)，t0=−2W/(3l⁶B²L2²S3²S5²)。  (7)

U18槽、V23槽由两原式有限乘加得，W23槽是它们的复用卷积。
U,V的低负项配对证明正性，继而t1>0、N5(1)<0、N5(y)<0，对0≤y<1成立。
完整方向和正数配对见附录 B；不要求c51、c52同负。

## 6. b3 三分项：全部归一化可追溯

原联合上界给

    Ja=p3−5Dp2+10D²p1−5D³p0，
    J3=q3²(a1/20−5ea2)，J5=10q5²z²[t0(D+2z)+t1]，
    b3=Ja+J3+J5。

令Ta=B⁸L2³S3²，G18(c)=6Ta(15/2−Ja)在l=1+c的移位。
第3节分母直接被Ta清除（p0的l²由D³的l⁶消掉），故是次数≤18有限多项式。
完整19槽来自(1),(3)，没有未付高次尾。

令T3=240lB²L2S3⁶，A17=T3(−J3−1/2)。代(4)可写成最短纯乘法

    A17=B²L2S3 A1+100l⁵A2−120lB²L2S3⁶。                (8)

次数≤17，完整18槽由此有限卷积生成。

J5同样代(7)，得到

    Z=W(S5+2l²)−B L2S3S5 U，W21=Z/(l²B)，
    J5=−20l⁸W21/(3B²L2³S3²S5⁷)。                        (9)

除法也是有限：U0=−7,U1=−64、W0=−7,W1=−78，所以Z0=0、Z1=0；
U(−1)=346、V(−1)=−346、W(−1)=0，故Z(−1)=0，B整除Z。
这两个交错和必须从完整U/V有限Horner核验。
U最高17/16槽为60/360，W最高22/21槽为60/480；
(S5+2l²)最高两槽1/1，B L2S3S5最高两槽1/3，
因此Z26=60−60=0、Z25=(480+60)−(360+3*60)=0。
Z次数≤24，除l²B次数3后W21≤21；完整22槽由(1)有限除法取得。
附录 C 的单负项付款、三组A17付款及W21九低负项配对使Ja<15/2、J3<−1/2、J5<0，故b3<7。

## 7. b4 的五次以下抵消与派生有限模式

原Ba=−5Dp3+10D²p2−5D³p1。用(3)直接收集

    Ba=5l⁶Q4/(2B⁹L2³)，
    Q4=160L2²+48L2 A_p2+A_p1
       =4635l⁴−5116l³+4430l²−856l+99。                  (10)

五槽一行就能由上述三个短多项式相乘核验。
其商法则导数为

    Ba'=5l⁵V7/(2B¹⁰L2⁴)，
    V7=(6B L2−9lL2−6l²B)Q4+lB L2Q4'。                  (11)

次数≤7，c移位的8槽由(1)明确给出。它的前三正后五负模式，配合右端付款，使Ba严格递增且Ba<16/5。
原B3=q3²a2/20=lA2/(240B S3⁵)；A2就是已生成的P6，无需另一个新身份输入。
原T=q5²t1=2U/(3l²S3S5⁴)、C=−q5²t0=2W/(3l⁴S3²S5⁴)。
完整四次系数是

    b4=Ba+B3+10z²(D+2z)T+4Dz(D²+5Dz+5z²)C。            (12)

两个导数比较分子直接由有限导数生成

    GU=12U−lU'−84(l−1)−788(l³−l)，
    GW=15W−lW'−105(l−1)−1197(l³−l)−1352(l³−l²)。        (13)

它们18/23槽，是(12−i)U_i、(15−i)W_i逐槽及明确低项补偿，非外加两张表。
几何z的强凸分子也只需

    R(c)=[5S4S5−96l⁴]_(l=1+c)，                          (14)

其8槽从全1几何和相乘再二项式移位取得。
附录 D 正系数分母方差、GU/GW单中心幂模式、七个商方向及z强凸下界、十一付款均已完整纸面。
尤其第4节的S3≥3l后184/l²+132/l³−88/l⁴采用正确V2修复，沿旧双向审计分工保留。
于是Ba<16/5、B3<1/4、剩余B5<31/20，合成b4<5。

## 8. 所有18向量245槽与19条付款

下列向量按升幂顺序，带_c者是c=l−1，其余是l。
它们逐槽由(1)–(14)生成；原Pa3为单项−80l⁴/B⁸，单独保留，不混入245槽计数。
每个完整向量均须人工乘回、核生成式和指定符号分界，不能仅检查其正负号。

```text
Pa0num (11 slots):
-33, -184, -154, 1042, 8467, 14076, 17367, 8554, 2974, -1480, 11

Pa1num (5 slots):
35, 152, 126, -4108, 395

Pa2num (3 slots):
-2, -21, 85

N3a0num (11 slots):
88, 311, -52, -1240, -3869, -3832, -11750, -4375, 11522, 4988, 19

N3a1num (9 slots):
-176, -179, 1455, 1303, 978, -30233, -34371, 661, 3454

N3a2num (7 slots):
-88, 132, 184, -5297, 7141, 15981, 3473

U17 (18 slots):
-7, -64, 53, 615, 2788, 6619, 12547, 18584, 23038, 24277, 21704, 16836, 11121, 6230, 2996, 1097, 360, 60

V22 (23 slots):
-7, -78, -97, 611, 3553, 10776, 23597, 42284, 64598, 87938, 107949, 121125, 124023, 115335, 96774, 72361, 47762, 27393, 13323, 5413, 1697, 420, 60

N3derivativeW_c (14 slots):
-202797, -1422486, -4135131, -6011031, -2893758, 5158369, 11938400, 12261059, 7731101, 3149207, 809054, 119241, 7729, 19

G18_c (19 slots):
84720, 120120, -421320, 2354640, 24534380, 84852720, 173695205, 243223590, 247818005, 189357570, 110067820, 48936390, 16670935, 4368060, 889300, 141480, 16785, 1260, 45

A17 (18 slots):
-176, -827, -922, -483, -2512, -51677, -147080, -301928, -974062, 258693, 1250960, 154703, -69598, -18377, -9266, -4200, -960, -120

W21 (22 slots):
-22, -110, -510, -1506, -3503, -6684, -9532, -9826, -3075, 12549, 36307, 62172, 81850, 89141, 82095, 64797, 43812, 25068, 12022, 4577, 1320, 240

Q4 (5 slots):
99, -856, 4430, -5116, 4635

Ba_derivativeV7_c (8 slots):
25632, 84160, 87472, -47624, -219142, -232982, -112989, -23175

W22 (23 slots):
-7, -78, -104, 540, 3535, 11380, 27053, 52306, 86552, 125688, 162118, 187024, 193042, 178152, 146435, 106548, 68109, 37716, 17776, 6930, 2117, 480, 60

GU17 (18 slots):
0, 0, 530, 4747, 22304, 46333, 75282, 92920, 92152, 72831, 43408, 16836, 0, -6230, -5992, -3291, -1440, -300

GW22 (23 slots):
0, 0, 0, 3931, 38885, 113800, 243477, 418448, 605864, 754128, 810590, 748096, 579126, 356304, 146435, 0, -68109, -75432, -53328, -27720, -10585, -2880, -420

z_R7_c (8 slots):
4, -34, 24, 241, 324, 180, 45, 5
```

下面19有限分数来自各明确表达式的端点、尾和、二次强凸或有限Horner付款。
negative_upper两项应为负，其余为正；这些等号的有限计算同样是手核义务。

```text
Pa0_lower_minus4 = 160675465900/204293284731
Pa1_negative_upper = -22615/7
N3_a1_negative_upper = -16961024/343
N3_derivative_budget_gap = 1081802149096626/96889010407
N3_a0_high_plus9 = 86846158517756652247422093279585703/95460081663326673010814336960641467
b3_G18_gap = 359400/49
b3_A17_gap = 18189669/2000
b3_W21_gap = 1539
GU_high = 372681716724267183117836828769206252633479504292979/76293945312500000000000000000000000000000000
GW_high = 883284457463439139699825107795620400344812936153773454304578180671/11920928955078125000000000000000000000000000000000000000000
T_den_mean_low_minus12 = 100700724/499475603
C_den_mean_low_minus15 = 147088307/499475603
T_low_below39 = 254845116944941495366404222139/995155787741560146917928173901
C_low_below121 = 82780171026377443093298534088608401/731221564872531306312502181547150681
Ba_derivative_V7_high = 19437165137129426394219/312500000000000000
Ba_high_below16over5 = 666238887500822203367896826418637674301519088/11461907125818277515141132191619471734156724715
M3_below1over4 = 14394610002517/2269323746550000
z_strong_convex_gap = 44545221930352751/115467878400000000
M5_below31over20 = 351780861501037/17973360345047040
```

附录 B–D 已完整给出这些有限值如何进入连续证明，复用它们而不重复研究已审连续符号。
当前补的是原一般身份来源；既有程序证书和数学PASS均保留，不误称原先没有正确证明。
GJGEN根/第三极点的26+24raw单项、j5两项、245导出槽、19付款、W21的两交错和
仍是实际有限算术工作。派生模式共用源向量，不应再假设它们免核或简单相加作总整数成本。
完整J1尚需本轮上-u身份和两端有限叶子的纸面补齐，并需要最终整体正文独审。

## 附录 A：已审原有限提取及b1/b2正文（逐字保留）

# 原 b2 单侧上界 Pstar 与 A1：生成式、奇偶抵消和有限除法的完整局部人工证明（已审 FINAL PASS）

2026-10-07，唯一主研究任务作者；原唯一辅助已完成独立 FINAL PASS。
正式全文回执：PSA1GEN_CONTINUATION_INDEPENDENT_MANUAL_AUDIT_20261007_PASS_V2.md。
被核 LOCAL V2 与所有旧稿均保留；本展示仅按回执更换状态，不改数学正文。
本文只完成已审联合曲率上界的两个系数支路，不宣称整体速度定理人工化。
所有旧稿、旧证书、失败 V1 以及修正 V2 原样保留。
本稿列出全部原定义、有限生成方法、连续比较和算术付款；配套程序是交叉核验材料。
下列 80 个整数是公开递推的输出，不能脱离生成步骤另充一般身份的输入。
不以整数增加为淘汰理由，也不声称正文比旧稿短。

## 1. 固定共同参数与命题

始终取同一个原参数 l∈[23/20,707/500]，令

    B=l+1，rho=l/B，S_j=1+l+...+l^(j−1)，q_j=1−1/S_j，
    x=l+l^−1=2+v，s=l−l^−1=√(v(v+4))>0，Q=x²+x−1。

因为 dx/dl=1−l^−2>0、ds/dl=1+l^−2>0，本闭域恰给

    va=9/460≤v≤vb=42849/353500<1/8，
    sL=129/460≤s≤sH=249849/353500<71/100，
    1/8−vb=2677/707000，71/100−sH=284/88375>0。       (1)

倒数参数 l^−1 及 x=2 是形式有理代换，未改变物理应用参数。
设 D=q4−rho=rho/x、e=q4−q3=rho/[x(x+1)]、z=q5−q4=D/Q。
附录 A、B 给出完整原光滑分子和有限主部系数 c_(j,r)；极点阶数为 4,3,3,2。
它们从原完整根和三龄贡献相加后提取，不能删去跨龄、价格或校正项。
为完整指定待证对象，写 κ_r=r(r+1)/2，并定义

    p_i=rho^(i+2) Σ_(r=1..4) κ_r binom(r−1,i)c_(2,r)，i=0,1,2，
    n_(j,0)=c_(j,1)+3c_(j,2)+6c_(j,3)，j=3,4，
    n_(j,1)=−2(q_j−rho)c_(j,1)+3(rho−q_j+rho)c_(j,2)+12rho c_(j,3)，
    n_(j,2)=(q_j−rho)²c_(j,1)−3(q_j−rho)rho c_(j,2)+6rho²c_(j,3)，
    n_(5,0)=c_(5,1)+3c_(5,2)，
    n_(5,1)=−(q5−rho)c_(5,1)+3rho c_(5,2)。

故一次、二次系数为

    b1=p1−5Dp0+q3²(n_(3,1)−5e n_(3,0))+q4²n_(4,1)
          +q5²[n_(5,1)+(4z−D)n_(5,0)]，
    b2=p2−5Dp1+10D²p0
          +q3²[n_(3,2)−5e n_(3,1)+n_(3,0)/20+63/100]
          +q4²n_(4,2)+q5²[10z²n_(5,0)+(4z−D)n_(5,1)]。 (2)

这里 b2 是既有联合曲率上界 P 的二次系数，含 +63/100 校正，不是原 F 的 u-Taylor 系数。
本稿依次证明整个共同闭域上

    b2(l)<−87/10；然后 b1(l)<48/5。                         (3)

已审附录 A/B 的结论却是倒数均值下界

    avg(b2)>−20963/2500+v/2>−87/10。                        (4)

(4) 只用于给出下文 N<0；它本身不能当成 (3) 的点态上界。

## 2. 所有原主部均从有限生成式取得

对一般 u，t=1−u，A=1+lt，Z_j=1+t(S_j−1)，

    K=B/(2l)+[1/2+(l^−1−l)/24]t+Bt²/12，h=K−t，
    P_n=24−2n−u−u/A。

令 u_j=1/q_j、epsilon=1−q_ju，则 Z_j=S_j epsilon。
原光滑分子 M_(j,r) 给出的有限提取公式为

    c_(j,r)=Σ_(k≥r) [epsilon^(k−r)]M_(j,k)(u_j(1−epsilon))/S_j^k。 (5)

附录 A 第 2–3 节写出 j=2,3,4 的全部原分子、K/t 的相反项抵消、非零几何分母和全部 20 个有限 jet；第 4 节及附录逐一写出 103 个 l^a/B^b 单项。
不是援引程序才能使用的黑盒：这些已审正文逐字附于本稿，可从 (5) 逐项核验。

为同样明确 j=5，只需常数与一次项。令

    u5=Q/(Bx)，t5=−1/(l²Bx)，a=(x+1)Q，I=x²(x+2)，q5=Bx/Q，
    K0=K(t5)，K1=u5[1/2+(l^−1−l)/24+Bt5/6]，
    L0=10K0+2t5，L1=10K1+2u5，
    P50=12−Q/(Bx)−Q/[l(x+1)]，
    P51=u5+Qx(x+2)/[l(x+1)²]。

原两行是 M52=8l³[u(10K+2t)−P6]/Z4、M51=−8l²P6/Z4²，
且 Z4(u5(1−epsilon))=[l³/S4](1+a epsilon)。于是

    c52=8(L0−q5P50)/(l³Q)，
    c51=8[L1−(1+a)L0+(aq5−I)P50−q5P51]/(l³Q)。           (6)

分母非零，epsilon 提取由 (1+a epsilon)^−1=1−a epsilon+O(epsilon²) 即得；M51 的 −I P50 不能漏掉。
附录 B 第 2–4 节完整展示这两行的倒数平均、五块生成式和低次除法，供复核。

## 3. 原倒数奇部的种子、递推和单项规则

对上述有理函数定义

    E(f)=[f(l)+f(l^−1)]/2，O(f)=[f(l)−f(l^−1)]/(2s)，
    f(l)=E(f)+s O(f)。                                     (7)

凡只含 x 的系数保持不动。设 W0=2,W1=x；R0=1,R1=x−1；
H0=1,H1=x；C0=1,C1=x+1。四列都按 T_n=xT_(n−1)−T_(n−2) 生成。
H_n=(l^(n+1)−l^(−n−1))/s，C_n=(l^(n+1)−l^−n)B/(ls)。
种子直接成立，乘 x 后减前一项即归纳。所需最高下标 5，无无限级数：

    H2=x²−1，H3=x³−2x，H4=x⁴−3x²+1，H5=x⁵−4x³+3x；
    C2=x²+x−1，C3=x³+x²−2x−1，
    C4=x⁴+x³−3x²−2x+1，C5=x⁵+x⁴−4x³−3x²+3x+1；
    W5=x⁵−5x³+5x，R5=x⁵−x⁴−4x³+3x²+3x−1。

利用 B²=l(x+2)，对 l^a/B^b 写 b=2k 或 2k+1，n=a−k，则

    E(l^a/B^(2k))=W_|n|/[2(x+2)^k]，
    E(l^a/B^(2k+1))=R_max(−n,n−1)/[2(x+2)^k]，
    O(l^a/B^(2k))=0 若 n=0；
                     H_(n−1)/[2(x+2)^k] 若 n>0；
                    −H_(−n−1)/[2(x+2)^k] 若 n<0；
    O(l^a/B^(2k+1))= C_(n−1)/[2(x+2)^(k+1)] 若 n≥1；
                    −C_(−n)/[2(x+2)^(k+1)] 若 n≤0。        (8)

例如奇数 B 次规则由
f(l)−f(l^−1)=(l^n−l^(1−n))/[B(x+2)^k]，
再乘 B，用 B²=l(x+2)，恰得 C_(n−1) 或 −C_(−n)。特别 n=0 是负号。
上式对负 k 也成立。它们是有限有理身份，不是点值拟合。

记原块 u_jr=l²c_jr、v_3r=l c_3r；记 U_jr=E(u_jr)、OU_jr=O(u_jr)，
V_3r=E(v_3r)、OV_3r=O(v_3r)。下列 15 偶块及 15 奇块由 (5),(6),(8) 得到。
对 j=3 的附加 V 块还可只用 l^−1=(x−s)/2 做交叉核验：

    V_3r=[xU_3r−v(x+2)OU_3r]/2，
    OV_3r=[xOU_3r−U_3r]/2。                                (9)

示例：c24=−8/(lB³)，u24=−8l/B³。在 (8) 中 k=1,n=0，
所以 U24=−4/(x+2)，OU24=4/(x+2)²，直接核定最容易混淆的奇部符号。
其余块按附录 A 的全部单项套 (8)，或对 j=5 套 (6)，只需有限收集。
偶部 j=5 采用已审低次除法的紧凑表达，未先展开十次分子。

全部偶块（** 表示整数乘幂；Q=x²+x−1）：

```text
U21 = -(33*x**5 + 35*x**4 - 273*x**3 - 499*x**2 - 300*x - 172)/(12*(x + 1)**2*(x + 2))
U22 = -(35*x**2 + 416*x - 916)/(12*(x + 2))
U23 = -2*(x - 43)/(x + 2)
U24 = -4/(x + 2)
U31 = -(88*x**4 + 47*x**3 - 1252*x**2 + 201*x + 4534)/(24*(x + 1))
V31 = -(88*x**5 + 47*x**4 - 1340*x**3 + 135*x**2 + 4259*x - 194)/(24*(x + 1))
U32 = -(89*x**3 - 24*x**2 - 173*x - 300)/(24*(x + 1)**2)
V32 = -(89*x**4 - 24*x**3 - 1426*x**2 - 317*x + 5076)/(24*(x + 1)**2)
U33 = -6*(x - 5)*(x + 7)/(x + 1)**3
V33 = -6*(x**3 + 2*x**2 - 20*x - 3)/(x + 1)**3
U41 = -(7*x**8 + 53*x**7 - 155*x**6 - 1128*x**5 - 1427*x**4 + 443*x**3 + 1629*x**2 + 616*x - 62)/(3*x*(x + 1)**2*(x + 2))
U42 = -(14*x**6 + 37*x**5 - 128*x**4 - 101*x**3 + 560*x**2 + 854*x + 348)/(3*x**2*(x + 1)**2*(x + 2))
U43 = -8*(x**3 + x**2 - 13*x - 12)/(x**3*(x + 1)*(x + 2))
U51 = 7*x**4/3+12*x**3-287*x**2/3-81*x+434/3+(355-113*x)/(3*Q)+8*x/(x+1)**2-18/x-20/(3*x**2)
U52 = (5*x-22)/3-48*(x+1)/Q**2+(113*x-211)/(3*Q)-8/(x+1)+74/(3*x)+10/(3*x**2)
```

全部奇块（OU/OV 按上面的 O 定义；下标与对应偶块相同）：

```text
U21 = (11*x**3 + 19*x**2 - 284*x - 524)/(4*(x + 2)**2)
U22 = (35*x - 374)/(12*(x + 2))
U23 = 2*(x + 44)/(x + 2)**2
U24 = 4/(x + 2)**2
U31 = (88*x**4 + 223*x**3 - 982*x**2 - 1895*x + 194)/(24*(x + 1)*(x + 2))
V31 = (88*x**5 + 223*x**4 - 1070*x**3 - 2099*x**2 + 2565*x + 4534)/(24*(x + 1)*(x + 2))
U32 = (89*x**3 + 154*x**2 - 2371*x - 5076)/(24*(x + 1)**2*(x + 2))
V32 = (89*x**4 + 154*x**3 - 1296*x**2 - 2861*x - 300)/(24*(x + 1)**2*(x + 2))
U33 = 6*(x + 3)/((x + 1)**2*(x + 2))
V33 = 6*(x**3 + 4*x**2 - 14*x - 35)/((x + 1)**3*(x + 2))
U41 = (7*x**8 + 67*x**7 - 35*x**6 - 1304*x**5 - 3571*x**4 - 3555*x**3 - 549*x**2 + 1136*x + 484)/(3*x*(x + 1)**2*(x + 2)**2)
U42 = (14*x**6 + 65*x**5 - 26*x**4 - 563*x**3 - 1154*x**2 - 1024*x - 360)/(3*x**2*(x + 1)**2*(x + 2)**2)
U43 = 8*(x**3 + 3*x**2 - 9*x - 12)/(x**3*(x + 1)*(x + 2)**2)
U51 = -(7*x**8 + 57*x**7 - 158*x**6 - 968*x**5 - 836*x**4 + 268*x**3 + 45*x**2 - 94*x - 20)/(3*x**2*(x + 2)*(x**2 + x - 1))
U52 = -(5*x**7 - 2*x**6 + 100*x**5 + 272*x**4 + x**3 - 183*x**2 - 94*x - 10)/(3*x**2*(x + 2)*(x**2 + x - 1)**2)
```

## 4. 点态 b2 的同参数重组

给任意 15 块 Z=(Z_U21,...,Z_U52；Z_V31,...,Z_V33)，定义四个线性函数

    wa=(10/x²，−5/x+10/x²，1−10/x+10/x²，3−15/x+10/x²)，
    GA(Z)=Σ_(r=1..4)κ_r wa_r Z_U2r/(x+2)²，
    G4(Z)=(x+1)²/[x²(x+2)²]*(Z_U41/x²−3Z_U42/x+6Z_U43)，
    J3(Z)={ (1+10/x)Z_U31/(x+1)²−3(x+6)Z_U32/(x+1)²
           +(6−60/[x(x+1)])Z_U33
           +(x+2)(Z_V31+3Z_V32+6Z_V33)/20 }/(x+1)²，
    T=x⁴+4x³+3x²+5，alpha=(Q²−3Q+6)/Q⁴，beta=3vT/Q⁴，
    J5(Z)=alpha Z_U51−beta Z_U52。

把 rho=l/B、q3=B/(x+1)、q4=rho(x+1)/x、q5=Bx/Q 代入 (2)，
利用 B²=l(x+2)，原点态 b2 恰为上面四个函数取原 u/v 块之和，
再加 63l(x+2)/[100(x+1)²]。每个权重只含 x，故

    E2:=E(b2)=GA(U,V)+G4(U,V)+J3(U,V)+J5(U,V)
                     +63x(x+2)/[200(x+1)²]，
    O2:=O(b2)=GA(OU,OV)+G4(OU,OV)+J3(OU,OV)+J5(OU,OV)
                     +63(x+2)/[200(x+1)²]，
    b2=E2+sO2。                                             (10)

校正的奇部为正，不能移入别的参数或遗漏。附录 A/B 的均值恰为本式 E2。

令

    Dx=x⁵(x+1)⁶(x+2)³Q⁵，D2=Dx Q，F2=(x+2)D2，
    t*=−87/10，N=2400D2(t*−E2)，M=−2400F2 O2，
    Pstar=6261(x+2)N+(1242+26261v)M
         =2400F2[6261(t*−E2)−(1242+26261v)O2]。             (11)

由已审 (4)，N<−(18888/25)D2<0（还可保留 v 的额外余量）。
原单侧间隙的准确身份为

    −87/10−b2=[N+sM/(v+4)]/(2400D2)。                     (12)

## 5. 清分母次数闭合：不存在未算的高次尾项

下表从第 3 节各块及第 4 节权重逐项相乘即可核验。
表内“分母包络”表示除一个非零有理常数外，约分前可取的共同分母；
“增长度 d”是分子次数减分母次数的上界，允许负数。
写 X1=x+1、X2=x+2。

| b2 分组 | 偶部包络 | 奇部包络 | 偶/奇增长度上界 |
|---|---|---|---|
| GA | x²X1²X2³ | x²X1²X2⁴ | −2 / −3 |
| G4 | x⁵X2³ | x⁵X2⁴ | 0 / −1 |
| J3 | xX1⁶ | xX1⁶X2 | 3 / 2 |
| J5 | x²X1²Q⁶ | x²X2Q⁶ | 0 / −1 |
| 校正 | X1² | X1² | 0 / −1 |

因此 D2E2、F2O2 都是有限多项式，而 F2E2 也是。
deg F2=27，E2 增长度≤3、O2 增长度≤2，(11) 中额外线性因子再增 1，
故 **Pstar 是次数≤30 的有限多项式**。这不依赖 32 项形式级数的末项为零。
例如 G4 第一项的偶分母是 x⁵X2³：U41 的 X1² 与权重 X1² 先抵消；
J3 第三项最大偶分母是 xX1⁶；J5 第二项给 Q⁶。
这些显式因子解释了为何清分母不会留下有理尾。

## 6. 有限低次除法、完整系数输出和 Pstar 付款

下面给出可用有理数逐行人工执行的唯一生成配方。
设 [v^i] 指形式系数，所有负下标为零。初始多项式仅为

    X=(2,1)，X1=(3,1)，X2=(4,1)，Q=(5,5,1)。

已展示的块分子按 x=2+v 移位：若 f(x)=Σ f_r x^r，

    [v^i]f(2+v)=Σ_(r≥i) f_r binom(r,i)2^(r−i)。             (13)

相乘用有限卷积 (ab)_i=Σ_(j=0..i)a_j b_(i−j)。
任一展示分母 d 的 d0≠0，除法 q=a/d 只需三角递推

    q0=a0/d0，q_i=[a_i−Σ_(j=1..i)d_j q_(i−j)]/d0。          (14)

分母幂用有限卷积，或先对一次/二次种子用 (14) 再乘。
各块最多八次已展开分子；偶 J5 用表中紧凑式分别除一次/二次分母，不展开十次分子。
将 (13),(14) 应用于 (10)，得 e2_i,o2_i；用它们与 F2 的有限卷积给

    p_i=2400 Σ_(j=0..i)f2_j {
          −6261[(87/10)δ_(i−j,0)+e2_(i−j)]
          −1242o2_(i−j)−26261o2_(i−j−1)}，0≤i≤30。          (15)

首项可以从原块直接复核：

    Dx0=4665600000，Dx1=47822400000，
    F20=93312000000，F21=1073088000000，
    e2_0=−2148253553/259200000，e2_1=8172730631/622080000，
    o2_0=−177190553/38880000，o2_1=239841271/34560000。

例如 p0=2400*93312000000*
[6261(−87/10+2148253553/259200000)+1242*177190553/38880000]
=689945328725472000。
全部 p_i、稍后生成的 a_i,b_i 均列在第 9 节一张完整表里，未省略尾项。
由 (15) 的完整输出，p0..p5>0、p6..p30<0，且

    −Σ_(i=6..30)p_i=48918611498119281214400<10^23。

在本域 0<v≤1/8，v^i≤1/8^6 对所有 i≥6，因此

    Pstar=Σ_(i=0..30)p_i v^i
         ≥p0−10^23/8^6=308475602162972000>0。               (16)

这是有限有理身份加一次尾付款，未用参数网格、浮点值或 Taylor 矩形。
degree30 的系数算术仍须逐项核对；将它们写为 (15) 的推导结果没有消灭算术成本。

## 7. Pstar 给出原正分支上的点上界

令 L(v)=(1242+26261v)/6261。端点直接有

    L(va)=129/460=sL，L(vb)=249849/353500=sH。

对 s(v)=√(v(v+4))，微分得 s'=(v+2)/s、s''=−4/s³<0。
故在整个 [va,vb] 上，凹函数大于等于其弦：s≥L>0。
关键方向顺序如下：N<0；(16) 给 Pstar>0；(11) 中
6261(v+4)>0 及 1242+26261v>0，故 M>0。
这之后才允许把正 M 乘上弦下界。由 (12)，

    −87/10−b2
      ≥[N+L M/(v+4)]/(2400D2)
       =Pstar/[6261*2400(v+4)D2]>0。                       (17)

端点处 s=L 仍由 Pstar 严格正保证严格上界。
平均下界、Pstar 身份、M 的正性、弦下界及最终点上界各自方向均已说明。

## 8. A1 从同一原块与抵消直接生成

下面仍用同一个 l,x,v,s，不另选倒数分支。
对任意原 u/v 块，定义

    Ra=Σ_(r=1..4)κ_r[(r−1)−5/x]u_2r/(x+2)，
    R4=(x+1)²/[x²(x+2)]*
                 [−2u41/x+3(1−1/x)u42+12u43]，
    R3={−(2x+5)(u31+v31)/[x(x+1)]
          +3(x²−5)(u32+v32)/[x(x+1)]
          +(12−30/[x(x+1)])(u33+v33)}/(x+1)²，
    R5=x[(3−2Q)u51+3((x−1)Q+4)u52]/Q³。

直接代入 (2) 的 b1、B²=l(x+2)，分别得到

    b1=(Ra+R4)/B+R3+(B/l)R5。                              (18)

例如根 p1−5Dp0 恰为 Ra/B；j=4 恰为 R4/B。
j=3 可用 1/rho=B/l=1+1/l，故 l²c*(1+1/l)=u+v。
其 c31 的权重 −2rho/(x+1)−5rho/[x(x+1)] 给第一项；
c32 的 3rho[1−(1+5/x)/(x+1)] 给第二项，c33 给第三项。
j=5 用 d5=q5−rho、z=rho/(xQ) 后，c51 的权重变成
q5²(−q5+rho+4z−D)=q5²rho(3−2Q)/(xQ)，c52 的权重为
3q5²(rho+4z−D)=3q5²rho[(x−1)Q+4]/(xQ)，即 R5*(B/l)。

写 EA/OA 为 Ra+R4 的 E/O，ER3/OR3、ER5/OR5 同理；
把相同线性函数分别施于第 3 节偶、奇表即可。
利用准确身份

    1/B=1/2−s/[2(x+2)]，B/l=(x+2)/2−s/2，s²=v(x+2)，

得到（相反奇项在乘法前保留）

    E1=E(b1)=(EA−vOA)/2+ER3
                    +[(x+2)ER5−v(x+2)OR5]/2，
    O1=O(b1)=[OA−EA/(x+2)]/2+OR3
                    +[(x+2)OR5−ER5]/2，b1=E1+sO1。         (19)

第 3 节表与此式已完整规定 A1 身份，无需读取旧 E/B 数组。

| A1 原分组 | 偶分母包络 | 奇分母包络 | 偶/奇增长度上界 |
|---|---|---|---|
| Ra | xX1²X2² | xX1²X2³ | 0 / −1 |
| R4 | x⁵X2² | x⁵X2³ | 2 / 1 |
| R3 | xX1⁶ | xX1⁶X2 | 1 / 0 |
| R5 | xX1²Q⁵ | xX2Q⁵ | 1 / 0 |

(19) 最多多一个 X2 分母，故 **DxE1、DxO1 均为有限多项式**。
deg Dx=24，E1 增长度≤2、O1≤1，得到次数上界 26、25。
令

    Bstar=24DxO1，Estar=2400Dx(48/5−E1)−71Bstar。

这里 Bstar 的符号是正的 +24，而不是历史 V1 中错误的 −24。
它们恰给点态间隙

    48/5−b1=[Estar+(71−100s)Bstar]/(2400Dx)。              (20)

用 (13),(14) 和 (19) 得 e1_i,o1_i、有限 Dx 系数 d_i，然后

    b_i=24Σ_(j=0..i)d_j o1_(i−j)，0≤i≤25，
    a_i=2400[(48/5)d_i−Σ_(j=0..i)d_j e1_(i−j)]−71b_i，0≤i≤26。 (21)

上界已由显式分母和增长度闭合，故只需这些有限行。
在最高行直接由相同递推得 b24=b25=0、a25=a26=0。
因此 Bstar 的次数≤23、Estar≤24，**没有被截断的更高尾项**。
首两阶原函数值为

    e1_0=275206129/32400000，e1_1=7337497/194400000，
    o1_0=101957171/64800000，o1_1=−27381047/34560000。

于是 b0=24*4665600000*101957171/64800000=176181991488；
a0=2400*4665600000*(48/5−275206129/32400000)−71b0
=−124735578048。其余行由 (21) 给第 9 节完整表。

## 9. 全部有限输出及 A1 连续付款

下表中 p、a、b 分别是 Pstar、Estar、Bstar 的升幂系数；“—”表示超过已证明次数、精确为零，不是缺失数据。
它们是 (15),(21) 的结果，原逻辑输入是已展示的原有限分子和单项规则。

| i | p_i (Pstar) | a_i (Estar) | b_i (Bstar) |
|---|---:|---:|---:|
| 0 | 689945328725472000 | -124735578048 | 176181991488 |
| 1 | 14385520830720888000 | 4597556549688 | 1717150820472 |
| 2 | 99667690800498912000 | 209880488015928 | 8072929953432 |
| 3 | 354284507022293587200 | 1563644457209080 | 23977173245720 |
| 4 | 716843122078921924800 | 5940590133508744 | 50091246287336 |
| 5 | 681865196519101225600 | 14574320441654472 | 78044975358568 |
| 6 | -547030474460507865200 | 25617835139144444 | 94101929718236 |
| 7 | -3262320395635362624000 | 34170499852716786 | 90044065052034 |
| 8 | -6612848341691805159800 | 35839061732497293 | 69608107884717 |
| 9 | -9039349498625668404300 | 30254496264058403 | 44036330321407 |
| 10 | -9463068458233242314960 | 20881318452569853 | 23014515298337 |
| 11 | -8002102308579882015570 | 11906566780707021 | 10005981770169 |
| 12 | -5634372654092246262572 | 5645542316644497 | 3638062695253 |
| 13 | -3371637716282662922302 | 2233474398086214 | 1110710559666 |
| 14 | -1740453239628646242996 | 737715873077493 | 285621099157 |
| 15 | -783433866629804885238 | 203038765849662 | 61972780378 |
| 16 | -309667874969853980344 | 46348089268203 | 11336958507 |
| 17 | -107819072594968641860 | 8707805690248 | 1738744412 |
| 18 | -33045375955332376864 | 1331191442925 | 220507525 |
| 19 | -8879778925309427772 | 162877338106 | 22529814 |
| 20 | -2078123888068975656 | 15572359412 | 1775708 |
| 21 | -419877658239448088 | 1121954985 | 100585 |
| 22 | -72473793020531336 | 57410550 | 3610 |
| 23 | -10553507713369914 | 1866469 | 61 |
| 24 | -1276722040738772 | 29140 | — |
| 25 | -125805178195126 | — | — |
| 26 | -9828776430268 | — | — |
| 27 | -585318372182 | — | — |
| 28 | -24945892480 | — | — |
| 29 | -677336800 | — | — |
| 30 | -8800000 | — | — |

此外边界抵消行 a25=a26=b24=b25=0，(15) 外次数全为零。
所有 b0..b23>0；a0<0，a1..a24>0，故 v≥va>0 上 Bstar>0，且

    Estar≥a0+a1v+a2v²=H(v)，H'(v)=a1+2a2v>0，
    H(va)=1205019416255211/26450>0。                        (22)

由 (1)，71−100s≥71−100sH=1136/3535>0；Dx>0。
把这些放入 (20)，得 b1<48/5，完成第二条点上界。
这里用 s 的**上界**使 71−100s 正；Pstar 用 s 的**弦下界**且事先证明 M 正。
两条方向不同，不能交换或仅以局部均值代替。

## 10. 与完整 J1 基线的连接及准确依赖

本稿 (17),(20) 新完成 Pstar 与 A1 的原身份来源手算化，保留已审 G/J3、J5 下界。
旧完整 J1 的其他系数付款仍复用：b0<−1867/300、b3<7、b4<5、b5<0、b6<1/20，
以及原联合上界、移动极点身份、矩形边界与端点值；本稿没有为这些另给新的原生成证明。
为使旧 J1 连接的变量同样明确，原 u∈[0,1/2]，
x_a=1−rho*u，y=u/x_a，d4(y)=1−(q4−rho)y。
由于 rho≤707/1207，x_a≥1707/2414>0，且 y 随 u、rho 递增，
故 0≤y≤1207/1707；D=rho/x<1/2、y<71/100 又给 d4>0。
这里 d4(y) 是正的归一化因子，不是第 1 节的间隙 q4−rho。
原完整 F 及联合曲率上界的其他支持仍按上述明确旧输入复用。

在原 y≥0 的域，旧组装因此给

    P(y)<H_J1(y)=−1867/300+(48/5)y−(87/10)y²+7y³+5y⁴+y⁶/20，
    H_J1'(y)=(48/5−(87/5)y+21y²)+20y³+3y⁵/10
                 ≥4197/700>0，
    H_J1(71/100)=−638236148237/60000000000000<0，
    71/100−1207/1707=497/170700>0。

在旧已审 0≤y≤1207/1707 上 P<0；结合原正归一化
x_a³d4⁵ F_uu/2<P，仍得 F_uu<0。
旧端点和 lambda 边界付款继而给既有 J1 结论 F>57/100>11/20。
这是**使用明确保留输入的 J1 连接**，不是本轮新审完整全域速度定理。

依赖分层如下：

1. 本局部证明的定义与引理：附录 A 的原 root/j3/j4 与已审 G/J3 人工证明；附录 B 的原 j5 与已审 J5 人工证明。正文 (5)–(22) 完整给出本轮生成和付款。
2. 本轮新增结果：相同原参数的所有 15 奇块、b2 的点态偶奇重组、Pstar 次数闭合与符号、A1 R 分组及抵消、完整 80 系数的有限除法出处；正式 PASS 状态由另存独立回执决定。
3. 支持交叉核验：主作者 generic V2、有限 Fraction 卷积；辅助由原 QQ[l] 光滑极点重新生成的全部一般身份与不同有限付款。精确程序通过不自动代替全文人工审计。
4. 仍保留的旧 J1 输入：上列其他系数、完整联合上界与其支持、原移动极点身份、端点/边界付款。完整包保留原全文和历史审计证据。
5. 整体速度定理仍是原限定范围的 COMPUTATIONAL 证明，不是整体人工证明：1<lambda<m、mu0=0、mu1>0、有限均值、ordinary GW root、实际 terminal-one canonical escape law；跨 lambda=1 未处理，general canonical S42 floor OPEN，旧 Mellin V3 FROZEN。

失败记录：作者 V1 已正确产生奇块和 Pstar，但 Bstar 归一化符号错误；其 A1 输出不被采纳。
V2 修正为 +24DxO1；所有失败源/native/data 和修正说明保存。
历史被拒绝的 ps 诊断仍停止，未重试、提权或绕过；当前证明写入与核验无授权障碍。

## 附录 A：既有 G/J3 已审完整人工证明（逐字保留）

# 原生成式到 G/J3 凸性与几何尾：完整人工局部证明（已审 FINAL PASS）

2026-10-07。主任务作者，原唯一辅助完成独立FINAL PASS。
正式完整回执：GJGEN_CONTINUATION_INDEPENDENT_MANUAL_AUDIT_20261007_PASS.md。
旧J5、完整J1、全部历史文件均保留；原已审LOCAL V3与被拒签V2均不覆盖。
本稿从未合并的原光滑极点给出有限提取、相反项抵消、倒数递推和每个极点的低次除法。
分式系数由这些步骤产生；程序只作补充交叉核验，不作为一般身份或连续判号的前提。
整数出现次数仍可记账，但不以多常数为唯一淘汰理由，也不声称本稿短于旧稿。
此处的G/J3是J1曲率分析中的局部分组，不是整体速度定理。

## 1. 局部命题、原定义与曲率权重

设l>0，B=l+1，S_j=1+l+...+l^(j−1)，q_j=1−1/S_j，rho=l/B，
x=l+l^−1∈[2,17/8]，v=x−2，D=q4−rho，e=q4−q3。
对一般u，令

    t=1−u，A=1+lt，Z_j=1+t(S_j−1)，k=1−lu，
    K=B/(2l)+t/2+B(2lt−l+1)t/(24l)
     =B/(2l)+[1/2+(l^−1−l)/24]t+Bt²/12，h=K−t，
    P_n=24−2n−u−u/A。

原年龄项在Z_j处的光滑分子记M_(j,r)，即局部极点项为Σ_r M_(j,r)/Z_j^r。
第2节给出原完整分子。取u_j=1/q_j，epsilon=1−q_ju，故Z_j=S_j epsilon。
标准主部系数为

    c_(j,r)=Σ_(s≥r) [epsilon^(s−r)]M_(j,s)(u_j(1−epsilon))/S_j^s。    (1)

只取有限系数，所有其余分母在u_j非零；其值在第3节列出。
令κ_r=r(r+1)/2。根极点j=2有四阶，定义

    p_i=rho^(i+2) Σ_(r=1..4) κ_r binom(r−1,i)c_(2,r)，i=0,1,2。

j=3,4有三阶。令d_j=q_j−rho，并定义

    n_(j,0)=c_(j,1)+3c_(j,2)+6c_(j,3)，
    n_(j,1)=−2d_j c_(j,1)+3(rho−d_j)c_(j,2)+12rho c_(j,3)，
    n_(j,2)=d_j²c_(j,1)−3d_j rho c_(j,2)+6rho²c_(j,3)。

这些等于Σκ_r c_(j,r)(1−d_j y)^(3−r)(1+rho y)^(r−1)的0、1、2次项。
对f(l)记avg(f)=[f(l)+f(l^−1)]/2，设

    Ja=p2−5Dp1+10D²p0，J4=q4² n_(4,2)，
    J3=q3²[n_(3,2)−5e n_(3,1)+n_(3,0)/20+63/100]，
    G(x)=avg(Ja+J4)，J(x)=avg(J3)。

这里b2=Ja+J3+J4+J5是既有联合二次上界P的二次系数，含J3的+63/100校正，
不是原F在u处的Taylor二次系数。本文只人工化该b2中的G/J3倒数均值分组。

我们将从上述原函数证明

    G''>91/768>0，J'>56/5>11，
    G+J>−31/20+v/2≥−31/20>−5/3。                         (2)

原l∈[23/20,707/500]给v∈[9/460,42849/353500]⊂[0,1/8]。
l^−1和l=1均只是这里的形式有理求值；未扩张物理速度定理范围。

## 2. 先在原极点内抵消

j=2的原完整分子为

    price=25+l/k，
    R2=2/l[price(−l+Klu)+u+2l+lu−2(h+K)lu]，
    R1=2/l[−price−u+1]，
    M24=−8u，M23=2u+8(22−u)+4u/Z3，
    M22=R2−4(22−u)/Z3+4lu/Z3²+4u(−23K+2h)，
    M21=R1+4l[u(22K−2h)−22+u]/Z3²
         +6l[−2u/Z3³+u/(Z3²Z4)+lu/(Z3Z4²)+u(−21K+2h)/Z3²]
         +8l²[−2u/Z4³+u/(Z4²Z5)+lu/(Z4Z5²)]。

这里M24表示M_(2,4)，以下同。根分子不含在u2处为零的A的倒数。
j=3原未合并的三行是

    M33=12lP3，
    M32=6l[−P3/Z4+u(−21K+2h)/A]+4l[u(22K−2h)−P1]/A，
    M31=6l²[u(18K−2h)−P3]/Z4²−4P1/A²
         +8l²u(−18K+2h)/Z4²。

因h=K−t，同分母的K、t项先相加，分别有
6(−19K−2t)+4(20K+2t)=−34K−4t，
6(16K+2t)−8(16K+2t)=−2(16K+2t)。故

    M32=−6lP3/Z4−l[u(34K+4t)+4P1]/A，
    M31=−2l²[u(16K+2t)+3P3]/Z4²−4P1/A²。                (3)

j=4的原三行是

    M43=16l²P6，
    M42=8l²[−P6/Z5+u(−18K+2h)/Z3]+6l²[u(18K−2h)−P3]/Z3，
    M41=8l³[u(12K−2h)−P6]/Z5²−6lP3/Z3²。

在M42的Z3项，8(−16K−2t)+6(16K+2t)=−2(16K+2t)，于是

    M42=−8l²P6/Z5−2l²[u(16K+2t)+3P3]/Z3，
    M41=8l³[u(10K+2t)−P6]/Z5²−6lP3/Z3²。                (4)

这些抵消在取平均或绝对值前进行，避免旧绝对范数路线的损失。

## 3. 所有有限提取都只需三项

几何和S3=l(x+1)、S4=lBx、S5=l²(x²+x−1)直接给下表。
写u=u_j(1−epsilon)、t=t_j+u_j epsilon。表内Z_i=ζ_i(1+b_i epsilon)。

| j | u_j | t_j | A0与b_A | 所需其他ζ_i与b_i |
|---|---|---|---|---|
| 2 | B/l | −1/l | A=B epsilon，不使用A^−1 | ζ3=−l,b3=−(x+2)；ζ4=−lB,b4=−(x+1)；ζ5=−l²(x+1),b5=−x(x+2)/(x+1) |
| 3 | (x+1)/B | −1/(lB) | A0=l/B,b_A=x+1 | ζ4=−l²/B,b4=−(x+1)² |
| 4 | Bx/[l(x+1)] | −1/[l²(x+1)] | A0=B/(x+1),b_A=x | ζ3=l/(x+1),b3=x(x+2)；ζ5=−l²/(x+1),b5=−x²(x+2) |

所有ζ_i和j=3,4的A0非零；根price还用k0=−l非零。
为避免反复展开，记

    K0=K(t_j)，K1=u_j[1/2+(l^−1−l)/24+Bt_j/6]，
    L(a,b)_0=aK0+bt_j，L(a,b)_1=aK1+bu_j。

若P的常数24−2n为C（本稿只需C=12,18,22），记其三项为P_C,0/1/2，则

    P_C,0=C−u_j−u_j/A0，
    P_C,1=u_j+(u_j/A0)(1+b_A)，
    P_C,2=−(u_j/A0)b_A(1+b_A)。                          (5)

这是把(1−epsilon)/(1+b_A epsilon)乘到二次得到的，不需高阶Taylor矩形。
以下统一记m_(r,i)=[epsilon^i]M_(j,r)，当前j由所在段决定。
两个普通乘法规则是

    [epsilon]P/Z=(P1−bP0)/ζ，
    [epsilon]uL/Z=u_j[L1−(1+b)L0]/ζ。                    (6)

对于j=3，令P18=P3、P22=P1，使用该行几何数据，全部所需m为

    m30=12lP18,0，m31=12lP18,1，m32=12lP18,2，
    m20=−6lP18,0/ζ4−l[u3 L(34,4)_0+4P22,0]/A0，
    m21=−6l(P18,1−b4P18,0)/ζ4
         −l{u3[L(34,4)_1−(1+b_A)L(34,4)_0]
              +4(P22,1−b_A P22,0)}/A0，
    m10=−2l²[u3 L(16,2)_0+3P18,0]/ζ4²−4P22,0/A0²。

对于j=4，令P12=P6、P18=P3，全部所需m为

    m30=16l²P12,0，m31=16l²P12,1，m32=16l²P12,2，
    m20=−8l²P12,0/ζ5−2l²[u4 L(16,2)_0+3P18,0]/ζ3，
    m21=−8l²(P12,1−b5P12,0)/ζ5
         −2l²{u4[L(16,2)_1−(1+b3)L(16,2)_0]
               +3(P18,1−b3P18,0)}/ζ3，
    m10=8l³[u4 L(10,2)_0−P12,0]/ζ5²−6lP18,0/ζ3²。

两者由(1)都给

    c1=m10/S_j+m21/S_j²+m32/S_j³，
    c2=m20/S_j²+m31/S_j³，c3=m30/S_j³。                  (7)

根j=2的price=24−(B/l)epsilon+O(epsilon²)。设u0=B/l,t0=−1/l，
K0/K1仍由上述公式。先列R2常/一次项与R1常数：

    r20=40K0u0−44+2u0/l+2u0+4t0u0，
    r21=2{−(B/l)(−1+K0u0)+20u0(K1−K0)−u0/l−u0+2u0(u0−t0)}，
    r10=−2(23+u0)/l。

写ζ3=−l,b3=−(x+2),ζ4=−lB,ζ5=−l²(x+1)，则根所需八项是

    m40=−8u0，m41=8u0，
    m30=176−6u0+4u0/ζ3，
    m31=6u0+4u0(−1−b3)/ζ3，m32=4u0(b3²+b3)/ζ3，
    m20=r20−4(22−u0)/ζ3+4lu0/ζ3²−4u0(21K0+2t0)，
    m21=r21−4[u0−b3(22−u0)]/ζ3+4lu0(−1−2b3)/ζ3²
         −4u0[21K1+2u0−21K0−2t0]，
    m10=r10+4l[u0(20K0+2t0)−22+u0]/ζ3²
         +6l[−2u0/ζ3³+u0/(ζ3²ζ4)+lu0/(ζ3ζ4²)−u0(19K0+2t0)/ζ3²]
         +8l²[−2u0/ζ4³+u0/(ζ4²ζ5)+lu0/(ζ4ζ5²)]。

特别是22−u的epsilon一次项为+u0。由(1)，根四个c为

    c1=m10/B+m21/B²+m32/B³，c2=m20/B²+m31/B³，
    c3=m30/B³+m41/B⁴，c4=m40/B⁴。                       (8)

M24只有一次项，因而这里不需要三次提取。

## 4. 倒数平均完全由两个二阶递推产生

令W0=2,W1=x；R0=1,R1=x−1，两者都按T_n=xT_(n−1)−T_(n−2)递推。
逐次相乘即得

    W2=x²−2，W3=x³−3x，W4=x⁴−4x²+2，
    R2=x²−x−1，R3=x³−x²−2x+1，R4=x⁴−x³−3x²+2x+1。

因为avg(l^a)=W_|a|/2、avg(l^n/B)=(l^n+l^(1−n))/(2B)，
后一种在n≤0时等于R_−n/2，在n≥1时等于R_(n−1)/2。
又B²=l(x+2)。故对任意整数a,b，写b=2k或2k+1，得到唯一单项平均规则

    T(l^a/B^(2k))=W_|a−k|/[2(x+2)^k]，
    T(l^a/B^(2k+1))=R_max(k−a,a−k−1)/[2(x+2)^k]。       (9)

负k也成立。T对只含x的系数线性；将第3节有限表达式按l^a/B^b展开再用(9)即可。
本稿实际只用W/R0..4。附录给出全部103个单项，便于逐项核对，并不另输入系数身份。

记U_jr=avg(l²c_jr)，另在j=3记V_3r=avg(l c_3r)。由(5)–(9)逐项得到

    U21=−(33x⁵+35x⁴−273x³−499x²−300x−172)/[12(x+1)²(x+2)]，
    U22=−(35x²+416x−916)/[12(x+2)]，
    U23=−2(x−43)/(x+2)，U24=−4/(x+2)，
    U31=−A31/[24(x+1)]，U32=−A32/[24(x+1)²]，U33=−6A33/(x+1)³，
    V31=−B31/[24(x+1)]，V32=−B32/[24(x+1)²]，V33=−6B33/(x+1)³，
    U41=−(7x⁸+53x⁷−155x⁶−1128x⁵−1427x⁴+443x³+1629x²+616x−62)
          /[3x(x+1)²(x+2)]，
    U42=−(14x⁶+37x⁵−128x⁴−101x³+560x²+854x+348)/[3x²(x+1)²(x+2)]，
    U43=−8(x³+x²−13x−12)/[x³(x+1)(x+2)]，                 (10)

其中六个小多项式为

    A31=88x⁴+47x³−1252x²+201x+4534，
    A32=89x³−24x²−173x−300，A33=(x−5)(x+7)，
    B31=88x⁵+47x⁴−1340x³+135x²+4259x−194，
    B32=89x⁴−24x³−1426x²−317x+5076，B33=x³+2x²−20x−3。

例如，(8)给l²c23=176l²/B³−6l/B²−4/B²+8l/B³。
(9)把这四项变成[88−6−2x+4]/(x+2)，正是U23；U24同理。
再如l²c43=192l/(B³x³)−16/[B²x²(x+1)]−16/(B³x²)，
平均后为96/[x³(x+2)]−8/[x(x+1)(x+2)]−8(x−1)/[x²(x+2)]，
三项同分母的分子为−8(x³+x²−13x−12)，给U43。
其余行同用(9)；附录把每一行的有限单项及其平均完全列出。

## 5. 曲率权重先化成只含x的因子

几何和给D=rho/x，d3=rho/(x+1)，e=rho/[x(x+1)]，
rho⁴=l²/(x+2)²，q4²rho²=l²(x+1)²/[x²(x+2)²]，q3²rho²=l²/(x+1)²。
将第1节权重分别乘回即可，记w=(10/x²,−5/x+10/x²,1−10/x+10/x²,3−15/x+10/x²)：

    GA=avg(Ja)=Σ_(r=1..4)κ_r w_r U2r/(x+2)²，
    G4=avg(J4)=(x+1)²/[x²(x+2)²]*(U41/x²−3U42/x+6U43)，
    J={ (1+10/x)U31/(x+1)²−3(x+6)U32/(x+1)²
         +(6−60/[x(x+1)])U33+(x+2)(V31+3V32+6V33)/20 }/(x+1)²
       +63x(x+2)/[200(x+1)²]。                          (11)

J的U32负号来自−3d3rho−15e(rho−d3)=−3rho²(x+6)/(x+1)²，不能误写成正项。
其63/100常数项用了avg(q3²)=x(x+2)/[2(x+1)²]。

代入(10)，按四个根项和三个j4项分别收集，得

    GA=A/[12x²(x+1)²(x+2)³]，G4=−C/[3x⁵(x+2)³]，
    A=51x⁵+11794x⁴−56505x³−63788x²+89820x+86320，
    C=7x⁸+53x⁷−197x⁶−1239x⁵−899x⁴+1034x³−1779x²−5546x−2834。

因此G=NG/[12x⁵(x+1)²(x+2)³]，其中

    NG=x³A−4(x+1)²C。                                   (12)

这里原U41的(x+1)²在权重中消去，再把U41/x²、−3U42/x、6U43相加就是C。
根四项按κ=(1,3,6,10)相加就是A；保留这些因子，无需展开十次完整判号分子。
同样J=NJ/[2400x(x+1)^6]，(11)的各组分别给

    NJ=−100(x+10)(x+1)A31+300x(x+6)A32−86400[x(x+1)−10]A33
       −5x(x+2)[(x+1)³B31+3(x+1)²B32+864(x+1)B33]
       +756x²(x+2)(x+1)⁴。                              (13)

这是完整原身份的因子来源；下步只做这些显式有限多项式的局部除法。

## 6. 分式系数的全部有限除法

若N(a+h)=Σn_i h^i、D0(a+h)=Σd_i h^i，d0≠0，则局部商的递推是

    q0=n0/d0，q_i=[n_i−Σ_(k=1..i)d_k q_(i−k)]/d0。      (14)

N/[(x−a)^m D0]的主部系数依次是q0/(x−a)^m,...,q_(m−1)/(x−a)。
各n_i来自(12)/(13)和(10)的小多项式：
[h^i](a+h)^r=binom(r,i)a^(r−i)，乘积按有限卷积。
不需求一般参数清分母的零检验。下面给出每一个输入列和商列，按(14)可逐行核。

| 对象与中心 | n_i（按i从0递增） | d_i | q_i |
|---|---|---|---|
| G,0，m=5 | 11336,44856,62820,118600,92260 | 96,336,456,300,96 | 1417/12,1295/24,−763/8,11327/12,−417857/192 |
| G,−1，m=2 | −960,1920 | −12,24 | 80,0 |
| G,−2，m=3 | −2327256,9151176,−14669340 | −384,1728,−3264 | 96969/16,110123/32,139051/64 |
| J,0，m=1 | −34774000 | 2400 | −86935/6 |
| J,−1，m=6 | −30744000,−6343440,1922980,109830,317501,−22861 | −2400,2400,0,0,0,0 | 12810,154531/10,1758223/120,3505463/240,11579043/800,3475999/240 |

例如G在0处第二商为(44856−336*1417/12)/96=1295/24；
在−1处第二商为(1920−24*80)/(−12)=0。
J在−1处因d1=−d0，有q_i=q_(i−1)−n_i/2400。
这些局部数不是新的外加身份表，它们来自完整列出的有限生成式。

减去所有主部后，剩余有理函数没有有限极点，因此是多项式。
G的分子/分母同为十次，首项比为−28/12=−7/3，所以该多项式为常数−7/3。
J的分母首四项为2400(x⁷+6x⁶+15x⁵+20x⁴+...)，
由(13)取分子首四项−440x¹⁰−2435x⁹+230x⁸+23406x⁷，长除逐步给

    p3=−440/2400=−11/60，
    p2=(−2435−14400p3)/2400=41/480，
    p1=(230−2400(15p3+6p2))/2400=7/3，
    p0=(23406−2400(20p3+15p2+6p1))/2400=−4469/2400。

以上消尽主部和多项式部分，余项无有限极点且在无穷远趋零，故恒为零。
最终由原函数导出的完整分式是

    G=−7/3+139051/[64(x+2)]+110123/[32(x+2)²]+96969/[16(x+2)³]
      +80/(x+1)²−417857/(192x)+11327/(12x²)−763/(8x³)
      +1295/(24x⁴)+1417/(12x⁵)，                         (15)
    J=p+Σ_(j=1..6)a_j/(x+1)^j−c/x，
    p=−11x³/60+41x²/480+7x/3−4469/2400，c=86935/6，
    a=(3475999/240,11579043/800,3505463/240,1758223/120,154531/10,12810)。 (16)

至此旧21个分式系数均有原极点、递推和低次除法的纸面来源。

## 7. G的连续凸性保留两个x极点抵消

记a,b,c2,d,e2,f,g,h2分别为(15)中的正系数
139051/64,110123/32,96969/16,417857/192,11327/12,763/8,1295/24,1417/12。
逐项微分给

    G''=2a/(x+2)³+6b/(x+2)⁴+12c2/(x+2)⁵+480/(x+1)⁴
         +(−2d/x³+6e2/x⁴)−12f/x⁵+20g/x⁶+30h2/x⁷。

六个单独正项随x递减，在H=17/8处依次为

    202256/3267，28191488/395307，264790016/4348377，
    393216/78125，848691200/72412707，7429160960/410338673，

分别大于61,71,60,5,11,18，其和大于226。
两个x极点必须合并：其导数为6(dx−4e2)/x⁵，
且2d−4e2=55393/96>0，故组合在x≥2递增，在2处为−146009/768。
另−12f/x⁵≥−2289/64。因此整个区间

    G''>226−146009/768−2289/64=91/768>0。                (17)

由(15)直接代入及一次微分，有

    G(2)=22619/9216>49/20，G'(2)=−1135105/110592>−21/2。

凸函数位于左端切线之上（也可对G''积分两次），所以

    G>49/20−(21/2)v。                                  (18)

## 8. J的有限几何尾及完整连续导数下界

令delta_j=a_j−c。由(16)，其值为

    delta=(−467/80,−36871/2400,28063/240,19523/120,14459/15,−10075/6)。

有限几何和Σ_(j=1..6)(x+1)^−j=1/x−1/[x(x+1)^6]给

    J=p+Σdelta_j/(x+1)^j−c/[x(x+1)^6]。

这保留了大c/x的抵消。直接微分并将j=3,4,5,6及最后一项同乘(x+1)^7，得到

    J'=p'−delta1/(x+1)²−2delta2/(x+1)³+R(x)/(x+1)^7，
    R=6(c+c/x−a6)+c(x+1)/x²
      −3delta3(x+1)³−4delta4(x+1)²−5delta5(x+1)。        (19)

前两个正项递减，后三个正delta项被减去，它们随x增加。因此在x≤H，以下H处付款给统一界：

    6(c+c/H−a6)>50900，c(H+1)/H²>10000，
    3delta3(H+1)³<10800，4delta4(H+1)²<6400，5delta5(H+1)<15100。

对应正差依次为1455/17,23500/867,776725/8192,17225/384,925/24，全部正。
故R>28600。又(H+1)^7=(25/8)^7<3000，且

    p'=−11x²/20+41x/240+7/3
       ≥−11H²/20+41*2/240+7/3>1/6，
    −delta1/(x+1)²≥−delta1/(H+1)²>1/2，
    −2delta2/(x+1)³≥−2delta2/(H+1)³>1。

代入(19)，得到整个区间J'>1/6+28600/3000+1/2+1=56/5>11。
J(2)=−31657/8100>−4；积分给

    J>−4+11v。                                        (20)

## 9. 分组合成、范围与尚未完成之处

(18)+(20)给G+J>−31/20+v/2≥−31/20>−5/3，最后差为7/60，局部命题(2)证毕。
结合原已审J5的avg(J5)≥−4272/625，原定义b2=Ja+J3+J4+J5还给

    avg(b2)>−20963/2500+v/2≥−20963/2500>−87/10，差787/2500。

在既有原对象定义N_orig=2400D2[−87/10−avg(b2)]中，
D2=x⁵(x+1)^6(x+2)³(x²+x−1)^6>0，故还得到

    N_orig<−(18888/25)D2<0，因2400*787/2500=18888/25。

这是原曲率二次系数的偶部符号对象，未调用N系数表或原K/B/E及低头数据。
原单侧b2<−87/10仍由此前Pstar已审链支付，不在此重新声称完成其人工化。

J5的完整原生成式人工证明与正式回执在同目录POLEGEN_CONTINUATION系列，未修改。
本稿只是补全G/J3身份来源及局部连续界；A1、原b2单侧上界、J3其余曲率付款和完整J1组装仍按旧已审链。
因此不能将此局部avg(b2)下界说成整体人工速度单调性定理。
跨lambda=1未处理，general canonical S42 floor OPEN，旧Mellin V3冻结。

正文实际展开最高为U41/C的八次小多项式；NG/NJ形式次数10保持因子，局部截断最高5次。
没有高阶二维Taylor矩形、参数抽样、apart或通分判号分子表。
13块和极点局部数需要有限算术，附录明确列出103单项；不把推导数据重新命名为零成本。
完整V3正文、103单项及五数字修复已由上述正式回执独核；本副本只升级状态文字。
所有算术与原已钉住V3相同，完整状态转写diff/字节/hash另存READBACK JSON。
配套有限生成段、局部除法/付款源均是补充；V3冗长direct-lambda补充中止exit130，不伪称exit0。
独立辅助从原QQ[l]双坐标、局部Fraction、103单项/显示及逐段人读完成核验；
各阶段actualexit0、未就绪/显示失败与作者中止的准确状态均在正式回执分别保留。

## 附录：每个原均值块的单项平均账

下表每行表示对应l^power*c_jr的C(x)l^a/B^b项；末列为用(9)取得的平均。
其C(x)由第3节有限公式展开并同类相加，读者可逐项乘回并核原分子、分母。
同一块的末列相加得到(10)。这给出完整有限人工路径，不以生成表的程序输出作证明前提。

### U21

| a | b | C(x) | 单项平均 |
|---:|---:|---|---|
| -2 | -1 | $-3$ | $- \frac{3 \left(x - 1\right) \left(x + 2\right)}{2}$ |
| -2 | 0 | $\frac{3}{2}$ | $\frac{3 \left(x^{2} - 2\right)}{4}$ |
| -1 | -1 | $- \frac{32}{3}$ | $- \frac{16 \left(x + 2\right)}{3}$ |
| -1 | 0 | $\frac{215}{6}$ | $\frac{215 x}{12}$ |
| -1 | 1 | $- \frac{47 x^{2} + 94 x + 95}{6 \left(x + 1\right)^{2}}$ | $- \frac{\left(x - 1\right) \left(47 x^{2} + 94 x + 95\right)}{12 \left(x + 1\right)^{2}}$ |
| -1 | 2 | $- \frac{8}{x + 1}$ | $- \frac{4 \left(x^{2} - 2\right)}{\left(x + 1\right) \left(x + 2\right)}$ |
| 0 | 0 | $- \frac{7}{2}$ | $- \frac{7}{2}$ |
| 0 | 1 | $4 \left(x - 5\right)$ | $2 \left(x - 5\right)$ |
| 0 | 2 | $- 2 \left(2 x^{2} + 6 x + 7\right)$ | $- \frac{x \left(2 x^{2} + 6 x + 7\right)}{x + 2}$ |
| 0 | 3 | $16$ | $\frac{8 \left(x - 1\right)}{x + 2}$ |
| 1 | 0 | $\frac{11}{6}$ | $\frac{11 x}{12}$ |
| 1 | 1 | $- \frac{793}{6}$ | $- \frac{793}{12}$ |
| 1 | 2 | $88 \left(x + 2\right)$ | $88$ |

### U22

| a | b | C(x) | 单项平均 |
|---:|---:|---|---|
| -1 | 0 | $- \frac{11}{3}$ | $- \frac{11 x}{6}$ |
| -1 | 1 | $\frac{11}{6}$ | $\frac{11 \left(x - 1\right)}{12}$ |
| 0 | 0 | $-22$ | $-22$ |
| 0 | 1 | $28$ | $14$ |
| 0 | 2 | $- 4 \left(x + 1\right)$ | $- \frac{2 x \left(x + 1\right)}{x + 2}$ |
| 1 | 1 | $\frac{1}{6}$ | $\frac{1}{12}$ |
| 1 | 2 | $94$ | $\frac{94}{x + 2}$ |
| 2 | 2 | $-44$ | $- \frac{22 x}{x + 2}$ |

### U23

| a | b | C(x) | 单项平均 |
|---:|---:|---|---|
| 0 | 2 | $-4$ | $- \frac{2 x}{x + 2}$ |
| 1 | 2 | $-6$ | $- \frac{6}{x + 2}$ |
| 1 | 3 | $8$ | $\frac{4}{x + 2}$ |
| 2 | 3 | $176$ | $\frac{88}{x + 2}$ |

### U24

| a | b | C(x) | 单项平均 |
|---:|---:|---|---|
| 1 | 3 | $-8$ | $- \frac{4}{x + 2}$ |

### U31

| a | b | C(x) | 单项平均 |
|---:|---:|---|---|
| -3 | 0 | $- \frac{4}{3}$ | $- \frac{2 x \left(x^{2} - 3\right)}{3}$ |
| -2 | -2 | $-6$ | $- 3 x \left(x + 2\right)$ |
| -2 | -1 | $- \frac{6 \left(x^{2} + x - 1\right)}{x + 1}$ | $- \frac{3 \left(x - 1\right) \left(x + 2\right) \left(x^{2} + x - 1\right)}{x + 1}$ |
| -2 | 0 | $20$ | $10 \left(x^{2} - 2\right)$ |
| -2 | 1 | $\frac{17 \left(x + 2\right)}{12 \left(x + 1\right)}$ | $\frac{17 \left(x + 2\right) \left(x^{2} - x - 1\right)}{24 \left(x + 1\right)}$ |
| -1 | -2 | $- \frac{196}{x + 1}$ | $- \frac{196 \left(x + 2\right)}{x + 1}$ |
| -1 | -1 | $\frac{127 x + 140}{x + 1}$ | $\frac{\left(x + 2\right) \left(127 x + 140\right)}{2 \left(x + 1\right)}$ |
| -1 | 0 | $- \frac{2 \left(9 x^{2} + 38 x + 38\right)}{3 \left(x + 1\right)}$ | $- \frac{x \left(9 x^{2} + 38 x + 38\right)}{3 \left(x + 1\right)}$ |
| -1 | 1 | $- \frac{67 x + 151}{4 \left(x + 1\right)}$ | $- \frac{\left(x - 1\right) \left(67 x + 151\right)}{8 \left(x + 1\right)}$ |
| 0 | -1 | $\frac{88}{x + 1}$ | $\frac{44 \left(x + 2\right)}{x + 1}$ |
| 0 | 0 | $- \frac{4 \left(x + 2\right)}{x + 1}$ | $- \frac{4 \left(x + 2\right)}{x + 1}$ |
| 0 | 1 | $- \frac{235 x + 218}{12 \left(x + 1\right)}$ | $- \frac{235 x + 218}{24 \left(x + 1\right)}$ |
| 1 | 1 | $\frac{17}{12}$ | $\frac{17}{24}$ |

### V31

| a | b | C(x) | 单项平均 |
|---:|---:|---|---|
| -4 | 0 | $- \frac{4}{3}$ | $- \frac{2 \left(x^{4} - 4 x^{2} + 2\right)}{3}$ |
| -3 | -2 | $-6$ | $- 3 \left(x + 2\right) \left(x^{2} - 2\right)$ |
| -3 | -1 | $- \frac{6 \left(x^{2} + x - 1\right)}{x + 1}$ | $- \frac{3 \left(x + 2\right) \left(x^{2} - x - 1\right) \left(x^{2} + x - 1\right)}{x + 1}$ |
| -3 | 0 | $20$ | $10 x \left(x^{2} - 3\right)$ |
| -3 | 1 | $\frac{17 \left(x + 2\right)}{12 \left(x + 1\right)}$ | $\frac{17 \left(x + 2\right) \left(x^{3} - x^{2} - 2 x + 1\right)}{24 \left(x + 1\right)}$ |
| -2 | -2 | $- \frac{196}{x + 1}$ | $- \frac{98 x \left(x + 2\right)}{x + 1}$ |
| -2 | -1 | $\frac{127 x + 140}{x + 1}$ | $\frac{\left(x - 1\right) \left(x + 2\right) \left(127 x + 140\right)}{2 \left(x + 1\right)}$ |
| -2 | 0 | $- \frac{2 \left(9 x^{2} + 38 x + 38\right)}{3 \left(x + 1\right)}$ | $- \frac{\left(x^{2} - 2\right) \left(9 x^{2} + 38 x + 38\right)}{3 \left(x + 1\right)}$ |
| -2 | 1 | $- \frac{67 x + 151}{4 \left(x + 1\right)}$ | $- \frac{\left(67 x + 151\right) \left(x^{2} - x - 1\right)}{8 \left(x + 1\right)}$ |
| -1 | -1 | $\frac{88}{x + 1}$ | $\frac{44 \left(x + 2\right)}{x + 1}$ |
| -1 | 0 | $- \frac{4 \left(x + 2\right)}{x + 1}$ | $- \frac{2 x \left(x + 2\right)}{x + 1}$ |
| -1 | 1 | $- \frac{235 x + 218}{12 \left(x + 1\right)}$ | $- \frac{\left(x - 1\right) \left(235 x + 218\right)}{24 \left(x + 1\right)}$ |
| 0 | 1 | $\frac{17}{12}$ | $\frac{17}{24}$ |

### U32

| a | b | C(x) | 单项平均 |
|---:|---:|---|---|
| -2 | -1 | $- \frac{6}{x + 1}$ | $- \frac{3 \left(x - 1\right) \left(x + 2\right)}{x + 1}$ |
| -2 | 1 | $- \frac{17}{12 \left(x + 1\right)}$ | $- \frac{17 \left(x^{2} - x - 1\right)}{24 \left(x + 1\right)}$ |
| -1 | -1 | $- \frac{13 x - 95}{\left(x + 1\right)^{2}}$ | $- \frac{\left(x + 2\right) \left(13 x - 95\right)}{2 \left(x + 1\right)^{2}}$ |
| -1 | 0 | $\frac{6 \left(x + 3\right)}{\left(x + 1\right)^{2}}$ | $\frac{3 x \left(x + 3\right)}{\left(x + 1\right)^{2}}$ |
| -1 | 1 | $\frac{21}{x + 1}$ | $\frac{21 \left(x - 1\right)}{2 \left(x + 1\right)}$ |
| 0 | -1 | $- \frac{88}{\left(x + 1\right)^{2}}$ | $- \frac{44 \left(x + 2\right)}{\left(x + 1\right)^{2}}$ |
| 0 | 0 | $\frac{4}{x + 1}$ | $\frac{4}{x + 1}$ |
| 0 | 1 | $- \frac{17 x - 127}{12 \left(x + 1\right)^{2}}$ | $- \frac{17 x - 127}{24 \left(x + 1\right)^{2}}$ |

### V32

| a | b | C(x) | 单项平均 |
|---:|---:|---|---|
| -3 | -1 | $- \frac{6}{x + 1}$ | $- \frac{3 \left(x + 2\right) \left(x^{2} - x - 1\right)}{x + 1}$ |
| -3 | 1 | $- \frac{17}{12 \left(x + 1\right)}$ | $- \frac{17 \left(x^{3} - x^{2} - 2 x + 1\right)}{24 \left(x + 1\right)}$ |
| -2 | -1 | $- \frac{13 x - 95}{\left(x + 1\right)^{2}}$ | $- \frac{\left(x - 1\right) \left(x + 2\right) \left(13 x - 95\right)}{2 \left(x + 1\right)^{2}}$ |
| -2 | 0 | $\frac{6 \left(x + 3\right)}{\left(x + 1\right)^{2}}$ | $\frac{3 \left(x + 3\right) \left(x^{2} - 2\right)}{\left(x + 1\right)^{2}}$ |
| -2 | 1 | $\frac{21}{x + 1}$ | $\frac{21 \left(x^{2} - x - 1\right)}{2 \left(x + 1\right)}$ |
| -1 | -1 | $- \frac{88}{\left(x + 1\right)^{2}}$ | $- \frac{44 \left(x + 2\right)}{\left(x + 1\right)^{2}}$ |
| -1 | 0 | $\frac{4}{x + 1}$ | $\frac{2 x}{x + 1}$ |
| -1 | 1 | $- \frac{17 x - 127}{12 \left(x + 1\right)^{2}}$ | $- \frac{\left(x - 1\right) \left(17 x - 127\right)}{24 \left(x + 1\right)^{2}}$ |

### U33

| a | b | C(x) | 单项平均 |
|---:|---:|---|---|
| -1 | 0 | $- \frac{12}{\left(x + 1\right)^{2}}$ | $- \frac{6 x}{\left(x + 1\right)^{2}}$ |
| 0 | 0 | $\frac{216}{\left(x + 1\right)^{3}}$ | $\frac{216}{\left(x + 1\right)^{3}}$ |
| 0 | 1 | $- \frac{12}{\left(x + 1\right)^{2}}$ | $- \frac{6}{\left(x + 1\right)^{2}}$ |

### V33

| a | b | C(x) | 单项平均 |
|---:|---:|---|---|
| -2 | 0 | $- \frac{12}{\left(x + 1\right)^{2}}$ | $- \frac{6 \left(x^{2} - 2\right)}{\left(x + 1\right)^{2}}$ |
| -1 | 0 | $\frac{216}{\left(x + 1\right)^{3}}$ | $\frac{108 x}{\left(x + 1\right)^{3}}$ |
| -1 | 1 | $- \frac{12}{\left(x + 1\right)^{2}}$ | $- \frac{6 \left(x - 1\right)}{\left(x + 1\right)^{2}}$ |

### U41

| a | b | C(x) | 单项平均 |
|---:|---:|---|---|
| -5 | -1 | $\frac{20}{3 \left(x + 1\right)}$ | $\frac{10 \left(x - 1\right) \left(x + 2\right) \left(x^{3} - 3 x - 1\right)}{3 \left(x + 1\right)}$ |
| -4 | 0 | $- \frac{2 \left(5 x - 4\right)}{3 x}$ | $- \frac{\left(5 x - 4\right) \left(x^{4} - 4 x^{2} + 2\right)}{3 x}$ |
| -3 | -1 | $\frac{16}{3 \left(x + 1\right)^{2}}$ | $\frac{8 \left(x + 2\right) \left(x^{2} - x - 1\right)}{3 \left(x + 1\right)^{2}}$ |
| -3 | 0 | $-56$ | $- 28 x \left(x^{2} - 3\right)$ |
| -3 | 1 | $- \frac{4 \left(x + 1\right)}{3 x}$ | $- \frac{2 \left(x + 1\right) \left(x^{3} - x^{2} - 2 x + 1\right)}{3 x}$ |
| -2 | -1 | $40 \left(x + 1\right)$ | $20 \left(x - 1\right) \left(x + 1\right) \left(x + 2\right)$ |
| -2 | 0 | $\frac{2 \left(5 x + 3\right)}{3 \left(x + 1\right)}$ | $\frac{\left(5 x + 3\right) \left(x^{2} - 2\right)}{3 \left(x + 1\right)}$ |
| -2 | 1 | $- \frac{20 \left(x + 1\right)}{x}$ | $- \frac{10 \left(x + 1\right) \left(x^{2} - x - 1\right)}{x}$ |
| -1 | 0 | $\frac{2 \left(15 x^{3} + 38 x^{2} + 21 x + 8\right)}{x \left(x + 1\right)}$ | $\frac{15 x^{3} + 38 x^{2} + 21 x + 8}{x + 1}$ |
| -1 | 1 | $\frac{2 \left(x + 1\right) \left(9 x^{2} + 9 x + 14\right)}{3 x}$ | $\frac{\left(x - 1\right) \left(x + 1\right) \left(9 x^{2} + 9 x + 14\right)}{3 x}$ |
| -1 | 2 | $- \frac{8 \left(x + 1\right) \left(x^{3} + 2 x^{2} - x - 1\right)}{x}$ | $- \frac{4 \left(x + 1\right) \left(x^{2} - 2\right) \left(x^{3} + 2 x^{2} - x - 1\right)}{x \left(x + 2\right)}$ |
| 0 | 0 | $\frac{4}{3 \left(x + 1\right)}$ | $\frac{4}{3 \left(x + 1\right)}$ |
| 0 | 1 | $- \frac{210 \left(x + 1\right)^{2}}{x}$ | $- \frac{105 \left(x + 1\right)^{2}}{x}$ |
| 0 | 2 | $\frac{6 \left(x + 1\right) \left(15 x^{2} + 29 x - 1\right)}{x}$ | $\frac{3 \left(x + 1\right) \left(15 x^{2} + 29 x - 1\right)}{x + 2}$ |
| 0 | 3 | $- \frac{16 \left(x + 1\right)}{x}$ | $- \frac{8 \left(x - 1\right) \left(x + 1\right)}{x \left(x + 2\right)}$ |
| 1 | 2 | $\frac{108 \left(x + 1\right) \left(x + 2\right)}{x}$ | $\frac{108 \left(x + 1\right)}{x}$ |

### U42

| a | b | C(x) | 单项平均 |
|---:|---:|---|---|
| -4 | 0 | $- \frac{8}{3 x \left(x + 1\right)^{2}}$ | $- \frac{4 \left(x^{4} - 4 x^{2} + 2\right)}{3 x \left(x + 1\right)^{2}}$ |
| -3 | 1 | $\frac{4}{3 x \left(x + 1\right)}$ | $\frac{2 \left(x^{3} - x^{2} - 2 x + 1\right)}{3 x \left(x + 1\right)}$ |
| -2 | 1 | $\frac{20}{x \left(x + 1\right)}$ | $\frac{10 \left(x^{2} - x - 1\right)}{x \left(x + 1\right)}$ |
| -1 | 0 | $- \frac{16}{x}$ | $-8$ |
| -1 | 1 | $- \frac{4 \left(6 x + 7\right)}{3 x \left(x + 1\right)}$ | $- \frac{2 \left(x - 1\right) \left(6 x + 7\right)}{3 x \left(x + 1\right)}$ |
| -1 | 2 | $- \frac{8 \left(x + 1\right)}{x}$ | $- \frac{4 \left(x + 1\right) \left(x^{2} - 2\right)}{x \left(x + 2\right)}$ |
| 0 | 1 | $\frac{6}{x}$ | $\frac{3}{x}$ |
| 0 | 2 | $\frac{2 \left(3 x^{3} + 54 x^{2} + 99 x + 56\right)}{x^{2} \left(x + 1\right)}$ | $\frac{3 x^{3} + 54 x^{2} + 99 x + 56}{x \left(x + 1\right) \left(x + 2\right)}$ |
| 0 | 3 | $\frac{16 \left(x + 1\right)}{x^{2}}$ | $\frac{8 \left(x - 1\right) \left(x + 1\right)}{x^{2} \left(x + 2\right)}$ |
| 1 | 2 | $- \frac{108 \left(x + 1\right)}{x^{2}}$ | $- \frac{108 \left(x + 1\right)}{x^{2} \left(x + 2\right)}$ |

### U43

| a | b | C(x) | 单项平均 |
|---:|---:|---|---|
| 0 | 2 | $- \frac{16}{x^{2} \left(x + 1\right)}$ | $- \frac{8}{x \left(x + 1\right) \left(x + 2\right)}$ |
| 0 | 3 | $- \frac{16}{x^{2}}$ | $- \frac{8 \left(x - 1\right)}{x^{2} \left(x + 2\right)}$ |
| 1 | 3 | $\frac{192}{x^{3}}$ | $\frac{96}{x^{3} \left(x + 2\right)}$ |


## 附录 B：既有 J5 已审完整人工证明（逐字保留）

# 原两极点到凸凹性：J5 的完整手算局部证明（已审 FINAL PASS）

2026-10-07，主任务作者；原唯一辅助完成新生成式链的独核。
正式回执：NNEG_CONTINUATION_J5_GENERATOR_MANUAL_INDEPENDENT_AUDIT_20261007_PASS_V2.md。
原凸凹/仿射核心由该辅助最初提出，已由主任务在此前回执独核；本稿复用该明确双向来源。
本文给出原生成式、倒数平均、低次除法和连续比较的完整推导。
不需要运行配套程序才能使用任何步骤；程序仅作额外交叉核验。
本文仍用导出的紧凑有理分组判定导数符号，没有声称完全绕开这种表示。
重要改进是这些分组系数不再作为外加的一般身份数据输入，而从原两极点逐行手算得到。
整数出现账仍有客观意义，但不是本文清晰度的唯一判断标准；不声称总整数减少或整体速度定理完成。
本已审展示副本依固定V2回执升级历史LOCAL标签，并直接写回原未合并分子。
旧 LOCAL V1/V2与两版回执原样保存；逐项转写diff及字节/hash另存READBACK JSON。

## 1. 局部命题与全部定义

设l>0，S_j=1+l+...+l^(j−1)，q_j=1−1/S_j，rho=l/S2，
D=q4−rho，z=q5−q4，x=l+l^−1。假设2≤x≤17/8，令v=x−2。
对一般u，定义

    t=1−u，A=1+lt，Z_j=1+t(S_j−1)，
    K(t)=(l+1)/(2l)+[1/2+(l^−1−l)/24]t+(l+1)t²/12，
    P(u)=12−u−u/A，
    M2(u)=8l³[u(10K(t)+2t)−P(u)]/Z4，
    M1(u)=−8l²P(u)/Z4²。

原未合并生成式为 K=B/(2l)+t/2+B(2lt−l+1)t/(24l)，其中 B=l+1。
展开它的最后一项即得到上面的二次式。若原写法采用 h_orig=K−t，
则原分子的 12K−2h_orig=10K+2t，因而得到此处 M2；特别保留其中的−P项。
令u0=1/q5，epsilon=1−q5u。因Z5=S5*epsilon，定义其两个主部系数

    c2=M2(u0)/S5²，
    c1=M1(u0)/S5+[epsilon]M2(u0(1−epsilon))/S5²。          (1)

中括号只取一次项。M1,M2在u0光滑，下面给出所需分母的非零正值。
定义

    N0=c1+3c2，N1=−(q5−rho)c1+3rho*c2，
    J5(l)=q5²[10z²N0+(4z−D)N1]。

对f(l)，记avg(f)=[f(l)+f(l^−1)]/2。我们将证明

    U(x)=avg(l²c1)，V(x)=avg(l²c2)，
    U''(x)>0，V''(x)<0，
    avg(J5)≥−4272/625>−7。                              (2)

倒数只是形式有理代换。原应用l∈[23/20,707/500]给
v∈[9/460,42849/353500]，而1/8−42849/353500=2677/707000>0，
所以本引理覆盖所需原域，不扩张物理速度定理到l≤1。

## 2. 原两极点只需常数项和一次项

写B=l+1，Q=x²+x−1，a=(x+1)Q，I=(x+2)x²。
有限几何和给S3=l(x+1)，S4=lBx，S5=l²Q，因此

    u0=Q/(Bx)，t0=−1/(l²Bx)，A(u0)=l(x+1)/(Bx)>0，
    Z4(u0)=l³/S4>0，
    u=u0(1−epsilon)，t=t0+u0*epsilon，
    Z4=(l³/S4)(1+a*epsilon)。                            (3)

令L0=10K(t0)+2t0，L1=u0[10K'(t0)+2]，并写P=P0+P1*epsilon+O(epsilon²)。
直接对P微分，或使用d(u/A)/du=B/A²，得

    P0=12−Q/(Bx)−Q/[l(x+1)]，
    P1=u0+Qx(x+2)/[l(x+1)²]。                           (4)

把(3)代入M2/S5²，先不展开几何分母：

    M2/S5²=8/(lS5) * [(1−epsilon)(L0+L1*epsilon+O(epsilon²))
                     −q5(P0+P1*epsilon+O(epsilon²))]/(1+a*epsilon)。

利用(1+a*epsilon)^−1=1−a*epsilon+O(epsilon²)，(1)给

    c2=8(L0−q5P0)/(lS5)，
    c1=8[L1−(1+a)L0+(a*q5−I)P0−q5P1]/(lS5)。            (5)

M1/S5的贡献是−8I*P0/(lS5)。这同时固定了一次项的符号；没有高阶Laurent展开。

## 3. 倒数平均由二阶递推生成

定义W0=2，W1=x；R0=1，R1=x−1；两者都按T_n=xT_(n−1)−T_(n−2)递推。
直接将l和l^−1相加，或对分子乘x，得到

    avg(l^−n)=W_n/2，
    avg(l^−n/B)=(l^−n+l^(n+1))/(2B)=R_n/2。             (6)

两个种子可直接核，乘x后减前一项即可归纳；只需n≤5。
例如R2=x²−x−1，R3=x³−x²−2x+1，
R4=x⁴−x³−3x²+2x+1，R5=x⁵−x⁴−4x³+3x²+3x−1。
W1=x，W2=x²−2。它们是递推结果，不是另付的高次符号表。

定义五个原平均块F0=avg(l^−1L0)，F1=avg(l^−1L1)，C0=avg(l^−1P0)，
B0=avg(l^−1q5P0)，B1=avg(l^−1q5P1)。由(4)、K的二次式和(6)，

    F0=5(W1+W2)/2−7R3/(2x)−5(R4−R2)/(24x)+5R5/(12x²)，
    F1=Q/x[7R1/2+5(R2−R0)/24−5R3/(6x)]，
    C0=6x−Q(x−1)/(2x)−Q(x²−2)/[2(x+1)]，
    B0=6x(x+2)/Q−x/2−x(x²+x−2)/[2(x+1)]，
    B1=x/2+x²(x+2)(x²+x−2)/[2(x+1)²]。                  (7)

可逐项核这五行：L0=5B/l+[7+5(l^−1−l)/12]t0+5Bt0²/6；
L1=u0[7+5(l^−1−l)/12+5Bt0/3]。
q5=Bx/Q使q5P0=12Bx/Q−1−Bx/[l(x+1)]、
q5P1=1+Bx²(x+2)/[l(x+1)²]；再各乘l^−1取(6)的平均，便是(7)。
由(5)，不含新身份输入的原生成形式为

    V=8(F0−B0)/Q，
    U=8[F1−(1+a)F0+aB0−IC0−B1]/Q。                    (8)

## 4. 从五块到导数分组：全部低次算术

为便于判断导数，只作以下可手核的除法。先由递推收集

    24x²F0=H=60x²(W1+W2)−84xR3−5x(R4−R2)+10R5
           =5x⁵−29x⁴+124x³+63x²−64x−10，
    24x²F1/Q=p=84xR1+5x(R2−R0)−20R3
             =−15x³+99x²−54x−20。                     (9)

这里最高的已展开多项式 H 次数为5；(x+1)H 等乘积保留因子而逐项除以 x²，
不再展开一个六次分子。用于判号的完整通分分子也无需展开。下面三条分式拆分都只需乘回分母核验：

    1/(xQ)=−1/x+(x+1)/Q，
    1/(x²Q)=−1/x²−1/x+(x+2)/Q，
    x/[(x+1)Q]=1/(x+1)+(1−x)/Q。                      (10)

对V，把(9)代入(8)，得到

    V=[5x³−17x²+136x+63−64/x−10/x²]/(3Q)
      −8x/[(x+1)Q]−48x(x+2)/Q²。

用5x³−17x²+136x+63=(5x−22)Q+163x+41、x(x+2)=Q+x+1，
再逐项套(10)，即得到

    V=(5x−22)/3−48(x+1)/Q²+(113x−211)/(3Q)
      −8/(x+1)+74/(3x)+10/(3x²)。                      (11)

U有更多抵消，以下记录中间行使它不成为“清分母即可”的黑盒。
分别代入(8)的五项，它们依次为

    8F1/Q=p/(3x²)，
    −8(1+a)F0/Q=−H/(3x²Q)−(x+1)H/(3x²)，
    8aB0/Q=48x(x+1)(x+2)/Q−4x(x+1)−4x(x²+x−2)，
    −8IC0/Q=−48x³(x+2)/Q+4x(x+2)(x−1)
             +4x²(x+2)(x²−2)/(x+1)，
    −8B1/Q=−4x/Q−4x²(x+2)(x²+x−2)/[(x+1)²Q]。

先用x²+x−2=(x+2)(x−1)消去相反的
−4x(x²+x−2)与+4x(x+2)(x−1)。另两个Q项合成

    48x(x+2)(x+1−x²)/Q=96x²(x+2)/Q−48x(x+2)，

其中用x+1−x²=2x−Q。接着用三个短除法

    (x+2)(x²−2)/(x+1)=x²+x−3−1/(x+1)，
    (x+2)²(x−1)/(x+1)²=x+1−(3x+5)/(x+1)²，
    x²(3x+5)/(x+1)²=3x−1+(1−x)/(x+1)²。

还有−4x²/(x+1)=−4x+4−4/(x+1)。来自p与H的非Q部分可直接逐项除：

    [p−(x+1)H]/(3x²)=−5x⁴/3+8x³−95x²/3−202x/3
                      +100/3+20/(3x)−10/(3x²)。

与上述非Q项相加就是下面的首两行。Q分子尚为

    −H/(3x²)+92x³+188x²+8x−4+4(1−x)/(x+1)²，

代入(9)的H并逐项除以3x²，便是下面花括号。因此

    U=7x⁴/3+12x³−287x²/3−514x/3+112/3
      +20/(3x)−10/(3x²)−4/(x+1)
      +{[271x³+593x²−100x−75+64/x+10/x²]/3
         +4(1−x)/(x+1)²}/Q。                          (12)

最后只用

    271x³+593x²−100x−75=(271x+322)Q−151x+247，
    −4/(x+1)+4(1−x)/[(x+1)²Q]
       =8x/(x+1)²+(8−12x)/Q

及(10)，便把(12)化为

    U=7x⁴/3+12x³−287x²/3−81x+434/3
      +(355−113x)/(3Q)+8x/(x+1)²−18/x−20/(3x²)。        (13)

(11)、(13)是原生成式的推导结果，不是输入另一套系数身份或运行apart所得的前提。
手核路线已列出每个递推、除法和收集中间行；所有分母在本域为正。

## 5. 原均值函数的连续凸凹性

在2≤x≤17/8上，5≤Q<6，5≤Q'=2x+1<11/2。
设Aq=355−113x≥919/8>0，Bq=113x−211∈[15,233/8]⊂(0,30)。
Q'^2−Q=3x²+3x+2>0。由(13)，

    U''=28x²+72x−574/3
         +[226Q'Q+2Aq(Q'^2−Q)]/(3Q³)
         +16(x−2)/(x+1)⁴−36/x³−40/x⁴。

中间两项非负，多项式部分递增，负项在2处最小，因此

    U''≥194/3−9/2−5/2=173/3>0。                       (14)

由(11)，

    V''=−48{(x+1)(6Q'^2−4Q)−4Q'Q}/Q⁴
         +[2Bq(Q'^2−Q)−226Q'Q]/(3Q³)
         −16/(x+1)³+148/(3x³)+20/x⁴。

第一花括号至少3(6*25−4*6)−4*(11/2)*6=246，
故其负项≤−48*246/6⁴=−82/9。
第二分子舍去负的−2BqQ后仍≤2*30*(11/2)²−226*5*5=−3835<0。
其余正项至多148/(3*8)+20/16=89/12。因此

    V''≤−82/9+89/12=−61/36<0。                        (15)

这证明的是整个闭区间的凸凹性，不依赖端点抽样或高次导数分子符号表。

## 6. 左端切线和原几何权重

直接把x=2代入(11)、(13)及它们的一阶导数，得

    U(2)=−12013/45，U'(2)=−68921/270，
    V(2)=87/50，V'(2)=526/45。

与−267、−256、7/4、12的正差依次为2/45、199/270、1/100、14/45。
凸函数在切线之上、凹函数在切线之下；可对(14)、(15)积分一次验证。故

    U>−267−256v，V<7/4+12v≤13/4。                     (16)

展开J5的定义，q5−rho=D+z给

    J5=q5²[(D²−3Dz+6z²)c1+3(10z²+(4z−D)rho)c2]。

原几何和直接给D=l²/S4、z/D=1/Q、rho/D=x、q5²D²=l²/Q²，
而10+4xQ−xQ²=−vT，T=x⁴+4x³+3x²+5。因此

    avg(J5)=alpha*U−beta*V，
    alpha=(Q²−3Q+6)/Q⁴>0，beta=3vT/Q⁴≥0。             (17)

为吸收(16)的仿射损失，设F(q)=16q⁴/625−q²+3q−6。
F(5)=0，F'(5)=29/5，F''(5)=142/25>0，F'''(q)=384q/625>0。
在q≥5积分导数，F(q)≥29(q−5)/5。又Q−5=5v+v²≥5v，所以

    alpha(2)−alpha≥29v/Q⁴，alpha(2)=16/625。

Q²−3Q+6≤24，且T(x)<T(9/4)=23393/256<100。
因此256v*alpha+(7/4+12v)*beta≤7119v/Q⁴，
267[alpha(2)−alpha]≥7743v/Q⁴，差624v/Q⁴≥0。
结合(16)、(17)，终得

    avg(J5)≥−267*16/625=−4272/625>−7，差103/625。

在v=0时最后收益差可以为0，最终严格性仍来自103/625。局部命题(2)证毕。

## 7. 此证明省去的依赖和仍未解决的简化

本文不使用旧E17/R6/N30，也不用U/V的11/9项完整分子表。
旧紧凑分式18系数仍作为推导结果出现，但其一般身份不再依赖源程序清分子验证：
(3)–(13)给出纸面上全部低次步骤。算术并未凭空消失，不能重新命名为零常数证明。
配套源POLEGEN_CONTINUATION_FIVE_BLOCK_MANUAL_DERIVATION_20261007.py/native
不读旧文件、不调用apart、不作参数网格；实际exit0仅为上述纸面证明的补充证据。
新原生成式到五块和全部收集步骤已获上述V2正式独核，17项输入bytes/hash匹配。
两套独立原QQ[l]源实际exit0与逐段人工审读合并为证据；作者自核不等同独审。

如果要求在五块(8)上不作(11)/(13)式的任何分组就直接看出凸凹性，当前尚无更短证明。
原生成块间抵消明显，分别取绝对值或逐块粗估不能保留(14)/(15)的强余量。
下一可研究是否把(12)的低次收集合成更自然的正核；不重跑已失败的漏P、常数U和无抵消norm路线。
此处只证明J5原分组的局部均值界，未处理其余G/J3输入，更未改变整体速度定理范围。



## 附录 B：旧Pa/N5与N3连续符号证明（来源桥已由本正文补明）

# J1 完整移动极点：Pa、N5 全域符号的短解析付款

2026-10-07。完整 LOCAL 系数符号证明，待唯一辅助独立审计。
完整移动极点身份正另行独立重建；本稿先证明下面明确定义的有理系数函数的连续符号，
只有身份和符号均核验后，才可把它们用作完整F曲率项。
旧六Taylor矩形、源码和runner继续保留。

## 1. 对象和域

令 lambda∈[23/20,707/500]、u∈[0,1/2]，
S_j=sum_(i=0..j−1)lambda^i、rho=lambda/S2、y=u/(1−rho*u)。
已有连续几何引理给0<=y<=Y=S2/(lambda+2)<17/24<1。
所有后文分母为正。由完整原F的Laurent提取拟得到的Pa和N5定义如下；
本稿的符号论证不依赖它们的数值抽样。

## 2. Pa的完整四系数及两次透明配对

定义Pa=p0+p1*y+p2*y²+p3*y³，其中
\[
p_0=\frac{
11\lambda^{10}-1480\lambda^9+2974\lambda^8+8554\lambda^7+
17367\lambda^6+14076\lambda^5+8467\lambda^4+1042\lambda^3
-154\lambda^2-184\lambda-33}{6\lambda^2S_2^5S_3^2},
\]
\[
p_1=-\frac{395\lambda^4-4108\lambda^3+126\lambda^2+152\lambda+35}{2S_2^6},
\quad
p_2=\frac{12\lambda^2(85\lambda^2-21\lambda-2)}{S_2^7},
\quad p_3=-\frac{80\lambda^4}{S_2^8}.                           \tag{1}
\]
取b=10/7，本域1<lambda<b。首先
\[
2974\lambda^8-1480\lambda^9
=\lambda^8(2974-1480\lambda)
>\frac{6018}{7}\lambda^8>0,
\]
\[
1042\lambda^3-154\lambda^2-184\lambda-33
\ge671\lambda^2>0.
\]
原p0分子的负项全部在这两组内，且没有重复使用正项。
剩余8554lambda^7+17367lambda^6+14076lambda^5+8467lambda^4
至少为48464lambda^4；另一个11lambda^10也为正。因此
\[
p_0>\frac{48464\lambda^2}{6S_2^5S_3^2}
>\frac{48464}{6(17/7)^5(219/49)^2}
=\frac{977848604824}{204293284731}>4,                          \tag{2}
\]
最后付款正差为160675465900/204293284731。

把p1的分子除以正lambda³：
\[
395\lambda-4108+126/\lambda+152/\lambda^2+35/\lambda^3
\le395b-4108+126+152+35=-22615/7<0.
\]
所以p1>0。因lambda>=1，
85lambda²−21lambda−2>=62lambda²>0，故p2>0。
最后S2²>=4lambda，给
\[
0<-p_3=80(\lambda/S_2^2)^4\le80/256=5/16.
\]
现在0<=y<1，故
\[
\boxed{P_a(y)>4-5/16=59/16>0.}                               \tag{3}
\]
p0的低阶配对及p1的负分子比较均是连续论证，(2)只是一条固定有理付款；
没有依据端点值猜测单调性。

## 3. N5的线性结构：避开已经失败的原始系数双负假设

定义N5=b0+b1*y。下面两个完整有限身份足够：
\[
b_1=\frac{2U_{17}}{3\lambda^4S_2^2(\lambda^2+1)^2S_3S_5^2},
\quad
b_0+b_1=-\frac{2V_{22}}{3\lambda^6S_2^2(\lambda^2+1)^2S_3^2S_5^2},       \tag{4}
\]
其中
\[
\begin{aligned}
U_{17}={}&60\lambda^{17}+360\lambda^{16}+1097\lambda^{15}
+2996\lambda^{14}+6230\lambda^{13}+11121\lambda^{12}
+16836\lambda^{11}+21704\lambda^{10}\\
&+24277\lambda^9+23038\lambda^8+18584\lambda^7+12547\lambda^6
+6619\lambda^5+2788\lambda^4+615\lambda^3+53\lambda^2-64\lambda-7,
\end{aligned}
\]
\[
\begin{aligned}
V_{22}={}&60\lambda^{22}+420\lambda^{21}+1697\lambda^{20}
+5413\lambda^{19}+13323\lambda^{18}+27393\lambda^{17}
+47762\lambda^{16}+72361\lambda^{15}\\
&+96774\lambda^{14}+115335\lambda^{13}+124023\lambda^{12}
+121125\lambda^{11}+107949\lambda^{10}+87938\lambda^9
+64598\lambda^8+42284\lambda^7\\
&+23597\lambda^6+10776\lambda^5+3553\lambda^4
+611\lambda^3-97\lambda^2-78\lambda-7.
\end{aligned}
\]
在lambda>=1，
\[
615\lambda^3+53\lambda^2-64\lambda-7\ge597\lambda^2>0,
\]
\[
611\lambda^3-97\lambda^2-78\lambda-7\ge429\lambda^2>0.
\]
其余所有显示的整数系数均正，故U17、V22正。
分母全正，所以b1>0且N5(1)=b0+b1<0。
对同一个lambda以及全部0<=y<1，
\[
\boxed{N_5(y)=N_5(1)-b_1(1-y)<0.}                            \tag{5}
\]
这里y=1只是该线性多项式的代数付款点；不评价域外速度或canonical law。
证明不要求原始c51,c52同时为负，已记录的c52变号障碍完全保留。

## 4. 身份及依赖范围

Pa的四个身份(1)、N5的两个身份(4)可从各极点的有限Laurent导数公式
或等价的局部有限系数乘法/求逆逐步核验。
本稿配套自包含精确源码
`j1_pa_n5_uniform_signs_manual_payment_20261007.py`
重新实现完整原根/三龄的这些光滑Laurent贡献，并核上述六个身份、
p0的一条有理正差和p1的有理负上界；没有参数网格、LP、
旧证书或高阶Taylor重跑。
完整原F的身份核验由另一个完整身份文件和唯一辅助独立审计承担。

保留有限Laurent/整数展开身份和显示的短算术依赖，
不称完全免计算。N3>−9、rk<5等已有引理状态不变；
本稿没有证明F_uu<0或最后联合付款，不能退役六个旧矩形。



# 完整 J1 的第三移动极点：全区间 N3(y)>−9

2026-10-07。完整 LOCAL 系数引理，待同一唯一辅助独立审计。
这是统一比率引理需要的符号义务，不是完整 F_uu<0 证明。
保留所有旧文件及六个 Taylor 矩形。

## 1. 完整函数和精确极点系数

仍取原完整 F=R+T2+T3+T4 和共享 K，精确定义见
`COMPLETE_FIRST_JOINT_BUDGET_SIX_COUPLED_TAYLOR_RECTANGLES_20261007_LOCAL.md` 第2节。
23/20<=lambda<=H=707/500，0<=u<=1/2。
记 S_j=sum_(i=0..j−1)lambda^i、p_j=S_j−1、
Z_j=S_j−p_j u、A=Z2、rho=lambda/S2、q3=p3/S3、
alpha=q3−rho、y=u/(1−rho*u)>=0。

取 P_s=24−2n_s−u(A+1)/A，n=(1,3,6)。
原完整年龄式可以逐项展开为一个通用的短身份：
\[
T_s=2s\lambda^{s-2}\left[
\frac{2P_s}{Z_s^3}-\frac{P_s}{Z_s^2Z_{s+1}}
+\frac{\lambda\{u[(24-2n_s)K-2h]-P_s\}}{Z_sZ_{s+1}^2}
+\frac{u[-(24-n_s)K+2h]}{Z_s^2Z_{s-1}}\right].       \tag{1}
\]
这是展开 f_s=2−r_s−lambda*r_s² 和 v_s=lambda*Z_s*Z_(s−1)/Z_(s+1)²；
价格没有被删除。根 R 在 q3 极点正规。

定义光滑函数（在 u*=S3/p3 附近）：
\[
\begin{aligned}
L_{33}&=12\lambda P_3,\\
L_{32}&=6\lambda[-P_3/Z_4+u(-21K+2h)/A],\\
L_{31}&=6\lambda^2[u(18K-2h)-P_3]/Z_4^2,\\
L_{22}&=4\lambda[u(22K-2h)-P_2]/A,\quad L_{21}=-4P_2/A^2,\\
L_{41}&=8\lambda^2u(-18K+2h)/Z_4^2.
\end{aligned}
\]
这里 P2 表示年龄 s=2 的 P，不是多项式余项。
由 (1)，q3 处的全部极部来自
L33/Z3³+(L32+L22)/Z3²+(L31+L21+L41)/Z3。
所以在标准极部 sum_(r=1..3)c_(3r)/(1−q3*u)^r 中，
\[
\begin{aligned}
c_{33}&=L_{33}(u_*)/S_3^3,\\
c_{32}&=(L_{32}+L_{22})(u_*)/S_3^2-L_{33}'(u_*)/(S_3^3q_3),\\
c_{31}&=(L_{31}+L_{21}+L_{41})(u_*)/S_3
-(L_{32}+L_{22})'(u_*)/(S_3^2q_3)+L_{33}''(u_*)/(2S_3^3q_3^2).
\end{aligned}                                                    \tag{2}
\]
所有求值正规，因为 A(u*)=rho>0、Z4(u*)=−lambda²/S2 !=0。
令
\[
N_3(y)=c_{31}(1-\alpha y)^2+
3c_{32}(1-\alpha y)(1+\rho y)+6c_{33}(1+\rho y)^2
=:a_0+a_1y+a_2y^2.
\]
(2) 给出以下完整精确系数：
\[
a_0=-\frac{19\lambda^{10}+4988\lambda^9+11522\lambda^8-4375\lambda^7
-11750\lambda^6-3832\lambda^5-3869\lambda^4-1240\lambda^3
-52\lambda^2+311\lambda+88}{12\lambda^5S_2S_3^3},                 \tag{3}
\]
\[
a_1=-\frac{3454\lambda^8+661\lambda^7-34371\lambda^6-30233\lambda^5
+978\lambda^4+1303\lambda^3+1455\lambda^2-179\lambda-176}
{12\lambda^3S_2^2S_3^3},                                      \tag{4}
\]
\[
a_2=\frac{3473\lambda^6+15981\lambda^5+7141\lambda^4-5297\lambda^3
+184\lambda^2+132\lambda-88}{12\lambda S_2^3S_3^3}.              \tag{5}
\]
这些式子可以用 (2)、原二次 K 及有限几何和手算；配套小源码只核验这些通用身份和后文三条付款。

## 2. a1 和 a2 的正性

令 b=10/7，记 (4) 的分子为 V1（a1=−V1/正分母）。
先除以正 lambda^5，用 1<=lambda<b，对每个正项取上界，
对两个负项取 −34371−30233，丢掉另两负项，得到
\[
V_1/\lambda^5
\le3454b^3+661b^2+978+1303+1455-34371-30233
=-\frac{16961024}{343}<0.                                    \tag{6}
\]
故 a1>0。对 (5)，
7141lambda^4−5297lambda^3>=1844lambda^3>0，
132lambda−88>=44>0，其余项正，故 a2>0。

## 3. a0 连续递减与一个端点付款

令 c=lambda−1>=0。微分 (3) 并展开得到准确身份
\[
a_0'=\frac{W(c)}{6\lambda^6S_2^2S_3^4},                       \tag{7}
\]
其中
\[
\begin{aligned}
W(c)={}&-202797-1422486c-4135131c^2-6011031c^3-2893758c^4\\
&+c^5(5158369+11938400c+12261059c^2+7731101c^3
+3149207c^4+809054c^5+119241c^6+7729c^7+19c^8).
\end{aligned}
\]
本域 c<3/7。括号各系数均正，所以正部分 <=它在 3/7 的值，
即
\[
\sum_{j=5}^{13}[c^j]W\,(3/7)^j
=\frac{18566998494411753}{96889010407}<202797,
\]
\[
202797-\frac{18566998494411753}{96889010407}
=\frac{1081802149096626}{96889010407}>0.                       \tag{8}
\]
其余负项保留或丢掉都给 W<0。分母正，故 a0 严格递减。
于是 a0(lambda)>=a0(H)>−9，因为
\[
9+a_0(H)=
\frac{86846158517756652247422093279585703}
{95460081663326673010814336960641467}>0.                      \tag{9}
\]
(8) 是一次明确的正系数 Horner/分数运算，不是为每个 lambda
建立符号表；(9) 只在已有连续递减论证之后使用。

## 4. 完整符号义务结论

由 (3)–(9) 及 y>=0，
\[
\boxed{N_3(y)=a_0+a_1y+a_2y^2>-9
\quad(23/20\le\lambda\le707/500,\ 0\le u\le1/2).}
\]
因此已经独立审计的双边比率引理条件 N>=−9 在这里可满足；
它给 N3*r3<=N3*(1−5ey+y²/20)+(63/100)y²。
若乘以 q3²，修正项也必须乘以 q3²。
本稿仅支付第三极点符号义务。Pa、N5、完整移动极点曲率身份和
最后联合曲率付款仍未证明；六个旧矩形仍是全矩形的证明依赖。
不改变整体速度定理状态或一般 canonical S42 的 OPEN 状态。

完整小源码：`j1_n3_uniform_signed_lower_bound_20261007.py`。
保留 (6)、(8)、(9) 三个短有理算术依赖，不称完全免计算。



## 附录 C：旧b3完整连续分组付款（逐字保留）

# J1 中间系数 b3<7：三分项短结构证明 LOCAL

2026-10-07。唯一辅助作为新证明作者，从原完整根和全部三龄重新进行有限局部提取。
下面是一条完整 LOCAL 连续证明，待主任务独立复核；本文件不把作者自核称为独立最终审计。
原已审 \(b_3<13/2\) 和四个固定表基线均保留。
本稿没有重跑旧证书，没有新的 55 次全系数差表、网格、LP 或双变量符号表。
仍保留有限有理身份及小单变量系数结构，未称完全无计算。

## 1. 完整函数和 b3 的三项来源

域 \(\lambda\in[23/20,707/500]\)。定义
\[
S_j=\sum_{r=0}^{j-1}\lambda^r,\quad L_2=1+\lambda^2,\quad
\rho=\lambda/S_2,\quad q_j=1-S_j^{-1},
\]
\[
D=q_4-\rho,\quad e=q_4-q_3,\quad z=q_5-q_4.
\]
原 \(F=R+T_2+T_3+T_4\) 仍为完整六矩形定义第 2 节。
完整 moving-pole 身份和其原函数来源已独立通过。
写 \(P_a=p_0+p_1y+p_2y^2+p_3y^3\)，
\(N_3=a_0+a_1y+a_2y^2\)，\(N_5=t_0+t_1y\)。
联合上界 \(P\) 中 \(N_4\) 至多二次，变号校正仅为二次，常数付款也不贡献三次系数。
因此完整的三次系数恰为
\[
b_3=J_a+J_3+J_5,                                      \tag{1}
\]
\[
J_a=p_3-5Dp_2+10D^2p_1-5D^3p_0,\qquad
J_3=q_3^2(a_1/20-5ea_2),
\]
\[
J_5=10q_5^2z^2\{t_0(D+2z)+t_1\}.                       \tag{2}
\]
这些是同一 \(\lambda\) 下完整极点曲率多项式的分项，并未更换原函数。
只需分别证明 \(J_a<15/2,\ J_3<-1/2,\ J_5<0\)。

## 2. Ja：唯一负项由常数吸收

设 \(c=\lambda-1\)，故 \(0<c<3/7\)。
对正分母 \(T_a=S_2^8L_2^3S_3^2\)，从 (2) 有精确身份
\[
6T_a(15/2-J_a)=G_{18}(c).                              \tag{3}
\]
\(G_{18}\) 的常数至最高次完整系数为

    84720, 120120, -421320, 2354640, 24534380, 84852720,
    173695205, 243223590, 247818005, 189357570, 110067820,
    48936390, 16670935, 4368060, 889300, 141480, 16785, 1260, 45

唯一负系数是二次项。其余每项系数正，\(c>0\)，并且
\[
84720-421320c^2>
84720-421320(3/7)^2=359400/49>0.
\]
所以 \(G_{18}>0\)。正 \(6T_a\) 和 (3) 给
\[
\boxed{J_a<15/2.}                                    \tag{4}
\]
这里保留的是 18 次、19 个小整数的单负结构；未把未知高次符号藏入“余项”。
这些整数也可从原 \(p_i\) 用有限乘加、再按二项式 \(\lambda=1+c\) 逐项核对。

## 3. J3：三组原 lambda 系数与一个短付款

令正分母 \(T_3=240\lambda S_2^2L_2S_3^6\)。
同一完整原 \(a_1,a_2\) 给
\[
T_3(-J_3-1/2)=A_{17}(\lambda),                         \tag{5}
\]
其中保留原 \(\lambda\) 幂分组为
\[
\begin{aligned}
A_{17}={}&\lambda^9(258693+1250960\lambda+154703\lambda^2)\\
&-(176+827\lambda+922\lambda^2+483\lambda^3
 +2512\lambda^4+51677\lambda^5\\
&\hspace{17mm}+147080\lambda^6+301928\lambda^7+974062\lambda^8)\\
&-\lambda^{12}(69598+18377\lambda+9266\lambda^2
 +4200\lambda^3+960\lambda^4+120\lambda^5).
\end{aligned}                                        \tag{6}
\]
本域 \(1<23/20\le\lambda<3/2\)。除以正 \(\lambda^8\)：
低负块每个 \(\lambda^{j-8}\le1\)，故整个低负块不小于 \(-1479667\)。
中正块用 \(\lambda\ge23/20\) 得下界
\[
258693(23/20)+1250960(23/20)^2+154703(23/20)^3
=17497403801/8000.
\]
高负块用 \(\lambda<3/2\) 得严格下界
\[
-[69598(3/2)^4+18377(3/2)^5+9266(3/2)^6+
4200(3/2)^7+960(3/2)^8+120(3/2)^9]
=-44698473/64.
\]
正确方向是先给负块的正幅值上界，再加负号。
因此
\[
\frac{A_{17}}{\lambda^8}>
\frac{17497403801}{8000}-1479667-\frac{44698473}{64}
=\frac{18189669}{2000}>0.                              \tag{7}
\]
所以 \(A_{17}>0\)，由 (5) 和正 \(T_3\) 得
\[
\boxed{J_3<-1/2.}                                    \tag{8}
\]
这没有使用 \(a_1,a_2\) 的独立参数极值，也没有引入另一张 55 次差表。

## 4. J5：原 21 次分项的九负项一次配对

完整原 \(t_0,t_1\) 在 (2) 中合并后恰为
\[
J_5=-\frac{20\lambda^8W_{21}(\lambda)}
 {3S_2^2L_2^3S_3^2S_5^7}.                             \tag{9}
\]
\(W_{21}\) 的完整升幂系数是

    -22, -110, -510, -1506, -3503, -6684, -9532, -9826, -3075,
    12549, 36307, 62172, 81850, 89141, 82095, 64797, 43812, 25068,
    12022, 4577, 1320, 240

索引 0 至 8 的九负项总绝对值为 \(34768\)，其他系数全正。
由于 \(\lambda\ge1\)，低幂不大于 \(\lambda^{10}\)，于是这九负项与第 10 次项的合并满足
\[
36307\lambda^{10}-\sum_{j=0}^8|W_{21}[j]|\lambda^j
\ge(36307-34768)\lambda^{10}=1539\lambda^{10}>0.
\]
其余正项保留，故 \(W_{21}>0\)。正分母和 (9) 给
\[
\boxed{J_5<0.}                                       \tag{10}
\]
这是完整 \(t_0,t_1\) 合并后的分项；没有假设原始两个 Laurent 系数同时为负。

## 5. 完整三次系数及准确依赖

由 (1)、(4)、(8)、(10)，整个闭 \(\lambda\) 域严格有
\[
\boxed{b_3<15/2-1/2=7.}                              \tag{11}
\]
这是新的较弱三次系数付款，可以供更强常数付款后的新归约使用。
它不修改旧 \(b_3<13/2\) 基线，不自动支付 \(b_1,b_2,b_4\)，也不扩张全速度定理。

新源 J1_INDEPENDENT_SHAPE_CHECK_20261007_SHORT_B3_STRUCTURE.py
先按已审原完整极点分项，使用辅助自己的 \(\mathbb Q[\lambda]\) 有理多项式/局部系数实现重新提取
\(P_a,N_3,N_5\)，再从 (2) 直接构造三个分项。
它只读取该旧身份源的函数和类定义，不执行旧证书或旧测试入口。
其钉住的原身份源 SHA-256 是
4b46aaa4eaa125608d7dc9b89a1852a1e2fd6eff7036f80cb3b9c67ffdda982b。
新源一般参数精确核 (3)、(5)、(9)；另核三个分式的原 Q10/V14/W21 因子身份，
并用独立二项式移位核完整 \(G_{18}\) 向量。
不存在参数点抽样。

实际执行 exit 0。原生输出保存于
J1_INDEPENDENT_SHAPE_CHECK_20261007_SHORT_B3_STRUCTURE.native.txt，包含

    PASS three complete original-F part identities for b3
    PASS Pa3<15/2 one-negative-coefficient structure; short gap 359400/49
    PASS N3-part<-1/2 three signed blocks, one short payment 18189669/2000
    PASS N5-part<0 low negative block absorbed by 36307 lambda^10, gap 1539
    PASS continuous written argument: b3=Pa3+N3part+N5part<15/2-1/2=7

仍需主任务对这份新 LOCAL 稿独立审核身份、符号模式和两个有理付款，
之后才能登记为独立 PASS。本稿作者没有为自己的新结果签发独审回执。


## 附录 D：旧b4正确V2完整连续付款（逐字保留）

# J1 四次项 b4<5：正几何、有限加权均值和低次结构 LOCAL V2

2026-10-07。主任务作者完整推导，本地精确执行通过；待唯一辅助独立审计。
本 V2 保留原稿，唯一辅助仅作为第4节修复作者改正 S3≥3lambda 后三个倒幂及 M3 付款；
原作者的其余部分由唯一辅助独立核验，第4节修复由主任务另行独立核验，作者与核验者分开。
正确 P6/lambda^4 的低项为184/lambda²+132/lambda³−88/lambda⁴；不修改任何旧输入。
旧 b4 的 55 次固定表及已通过完整 J1 链保留，不覆盖原文件。
这是完整曲率联合上界 P 的四次项付款；没有替换完整原 F 的根项、三龄或变号价格。
没有端点抽样推全域、网格、LP、旧固定符号表执行。
保留下述自然多项式身份、符号模式及十一条精确有理运算，不称免计算。

## 1. 同一个参数的完整四次系数

域 lambda∈[a,H]=[23/20,707/500]。设 S_j=Σ_(i=0..j−1)lambda^i，
S2=1+lambda，L2=1+lambda²，rho=lambda/S2，q_j=1−1/S_j，
D=q4−rho，z=q5−q4。它们全在同一个 lambda 上。
完整原 F 及完整移动极点来源、联合曲率上界 P 已分别独立审计通过；
原函数定义见 J1_COMPLETE_CURVATURE_ALTERNATIVE_PROOFS_AND_FULL_SOURCES_20261007.md 第 1、2 节。
写 P_a=p0+p1*y+p2*y²+p3*y³，N3=a0+a1*y+a2*y²，N5=t0+t1*y。
联合上界中的 N4 至多二次；校正只贡献二次；常数价格不贡献四次。
把联合比率 R_a=1−5D*y+10D²*y²−5D³*y³ 和
R45=1+(4z−D)y+10z²y²+10z²(D+2z)y³−4Dz(D²+5Dz+5z²)y⁴
展开，完整四次项恰为

    b4 = B_a+B_3+B_5,
    B_a = −5D*p3+10D²*p2−5D³*p1,
    B_3 = q3²*a2/20,
    B_5 = 10z²(D+2z)*T+4Dz(D²+5Dz+5z²)*C,
    T=q5²*t1, C=−q5²*t0.                              (1)

从完整原根与三龄作有限 Laurent 提取，以下五个一般参数身份成立：

    B_a=5lambda⁶*Q4/(2S2⁹L2³),
    Q4=4635lambda⁴−5116lambda³+4430lambda²−856lambda+99,
    B_3=lambda*P6/(240S2*S3⁵),
    P6=3473lambda⁶+15981lambda⁵+7141lambda⁴−5297lambda³
         +184lambda²+132lambda−88,
    T=2U/(3lambda²*S3*S5⁴),
    C=2W/(3lambda⁴*S3²*S5⁴), W=V+lambda²*S3*U.          (2)

其中 U=U17,V=V22 是原已审 N5 符号引理的完整自然多项式。
为便于手工核对，其升幂系数全部列出：

    U: −7,−64,53,615,2788,6619,12547,18584,23038,24277,
       21704,16836,11121,6230,2996,1097,360,60
    V: −7,−78,−97,611,3553,10776,23597,42284,64598,87938,
       107949,121125,124023,115335,96774,72361,47762,
       27393,13323,5413,1697,420,60

U,V>0 在 lambda≥1 已由低负项与第 3 次项配对证明；例如
615lambda³+53lambda²−64lambda−7≥597lambda²>0，
611lambda³−97lambda²−78lambda−7≥429lambda²>0，其余项正。
故 W,T,C>0。

## 2. T,C 严格递减：不对有负系数的分子使用方差

对正系数多项式 S=Σ d_i lambda^i，令
mu_S=lambda*S'/S，w_i=d_i lambda^i/S。有限乘加直接给

    lambda*mu_S' = Σ i²*w_i−(Σ i*w_i)²
                 = (1/2)Σ_(i,j)(i−j)²*w_i*w_j≥0.       (3)

因此 mu_S3 和 mu_S5 均非递减。这只用于正系数 S3,S5，未用于 U,W。
为了比较 U,W 的分子均值，定义自然低次剩余：

    G_U=12U−lambda*U'−84(lambda−1)−788(lambda³−lambda),
    G_W=15W−lambda*W'−105(lambda−1)−1197(lambda³−lambda)
                               −1352(lambda³−lambda²). (4)

完整升幂系数为

    G_U: 0,0,530,4747,22304,46333,75282,92920,92152,72831,
         43408,16836,0,−6230,−5992,−3291,−1440,−300
    G_W: 0,0,0,3931,38885,113800,243477,418448,605864,754128,
         810590,748096,579126,356304,146435,0,−68109,−75432,
         −53328,−27720,−10585,−2880,−420

G_U/lambda¹² 和 G_W/lambda¹⁵ 均严格递减：所有正项在中心幂之前，
除以中心幂后导数负；所有负项在中心幂之后，除以中心幂后导数也负。
这是连续逐项导数论证。两条右端有理付款为

    G_U(H)=372681716724267183117836828769206252633479504292979
            /76293945312500000000000000000000000000000000 >0,
    G_W(H)=883284457463439139699825107795620400344812936153773454304578180671
            /11920928955078125000000000000000000000000000000000000000000 >0.

所以两 G 在全域都正。(4) 中扣去的每个补偿项在 lambda>1 正，故
lambda*U'/U<12，lambda*W'/W<15。
另一方面由 (3) 及左端付款

    [2+mu_S3+4mu_S5−12](a)=100700724/499475603>0,
    [4+2mu_S3+4mu_S5−15](a)=147088307/499475603>0,

得到两分母的对数导数分别严格大于 12、15。
用 (2) 作商的对数导数，lambda*T'/T<0，lambda*C'/C<0。
T,C 为正，故它们全域严格递减。最后两条左端付款为

    39−T(a)=254845116944941495366404222139
               /995155787741560146917928173901>0,
    121−C(a)=82780171026377443093298534088608401
               /731221564872531306312502181547150681>0.

于是

    0<T<39，0<C<121。                                 (5)

## 3. B_a<16/5：一个七次导数分子

对 (2) 直接求导得

    B_a'=5lambda⁵*V7/(2S2¹⁰L2⁴).

令 c=lambda−1∈[3/20,207/500]，V7(1+c) 的完整升幂系数为

    25632,84160,87472,−47624,−219142,−232982,−112989,−23175.

V7(1+c)/c³ 严格递减，理由与上节相同：正项幂 0、1、2 在 3 之前，
负项在 3 及其后；幂 3 项导数为零，其余导数严格负。
右端付款

    V7(H)=19437165137129426394219/312500000000000000>0

给全域 V7>0，所以 B_a 严格递增。另一端点付款

    16/5−B_a(H)=666238887500822203367896826418637674301519088
                 /11461907125818277515141132191619471734156724715>0

给

    B_a<16/5。                                       (6)

没有只用两端数值声称中间单调。

## 4. B_3<1/4：S3≥3lambda 后七个低次单调商

lambda≥1 时，P6 的高正项与 −5297lambda³−88 配对：
3473lambda⁶+15981lambda⁵+7141lambda⁴−5297lambda³−88
≥21210lambda³>0，其他项正。所以 P6>0。
S3−3lambda=(lambda−1)²≥0，于是

    B_3 ≤ [3473lambda²+15981lambda+7141−5297/lambda
            +184/lambda²+132/lambda³−88/lambda⁴]/(240*243*S2). (7)

置 b=10/7，lambda∈[a,H]⊂[a,b)。
lambda²/S2 和 lambda/S2 均递增，1/S2 递减；
−1/(lambda*S2) 递增；lambda^(−2)/S2 与 lambda^(−3)/S2 递减；
−lambda^(−4)/S2 递增。每一方向都由商的一阶导数或正单调乘积立即给出。
按照项的符号，正递增项用 b，正递减项用 a，负递增项用 b，得

    B_3 ≤ M3 := [3473b²/(1+b)+15981b/(1+b)+7141/(1+a)
             −5297/(b(1+b))+184/(a²(1+a))+132/(a³(1+a))
             −88/(b⁴(1+b))]/58320.

修正后的准确 M3=552936326634983/2269323746550000。
固定有理付款

    1/4−M3=14394610002517/2269323746550000>0

给

    B_3<1/4。                                       (8)

## 5. D,z 的连续几何上界

直接化简 D=lambda²/[S2*L2]。求导

    D'=lambda*(2+lambda−lambda³)/(S2²L2²)>0。

最后正号因为 lambda<3/2，
2+lambda−lambda³>2−(5/4)lambda>1/8。
故 0<D<D(b)=700/2533。

z=lambda⁴/(S4*S5)>0。要证 z<5/96，等价于 R(c)>0，其中

    R(c)=5S4S5−96lambda⁴
         =4−34c+24c²+241c³+324c⁴+180c⁵+45c⁶+5c⁷.    (9)

在 c≥c0=3/20，R''≥48+1446c0+3888c0²=M2=17619/50。
Taylor 积分余项（或两次积分 R''≥M2）给

    R(c)≥R(c0)+R'(c0)(c−c0)+(M2/2)(c−c0)².

完整数据 R(c0)=110487007/256000000，
R'(c0)=−72729257/12800000。
右边的二次式即使在全实轴也至少为

    R(c0)−R'(c0)²/(2M2)
      =44545221930352751/115467878400000000>0。

所以 R>0 全域，得到

    0<D<700/2533，0<z<5/96。                         (10)

这是连续强凸下界，未引入参数网格或细分。

## 6. B_5<31/20 与完整结论

(1) 中 B_5 的所有因素为正；对 D,z,T,C 它逐项非递减。
由 (5)、(10)，令 d=700/2533、r=5/96，得到严格上界

    B_5 < M5=10r²(d+2r)*39+4dr(d²+5dr+5r²)*121
             =5501385534664375/3594672069009408。

末条固定付款

    31/20−M5=351780861501037/17973360345047040>0

给 B_5<31/20。于是由 (1)、(6)、(8)

    b4 <16/5+1/4+31/20=5。                          (11)

本稿只支付 b4，不自动支付 b1,b2，也不单独证明 F_uu<0。
与已独立通过强化 b0 和较弱 b3 相组合，仍需显式核最后多项式。

## 7. 可复核来源与准确计算依赖

新源 j1_followup_short_b4_structure_20261007_v2.py 使用主任务自己的
QQ(lambda) 四阶局部系数实现，从完整原根/三龄的已审有限极点分解重建 Pa,N3,N5；
一般参数直接核 (1)、(2) 的全部五个身份，两导数身份及 R(c) 身份。
源码及实际 exit 0 原生输出均同目录保存。
十一项有理付款：GUH,GWH，两分母均值左端，两 T/C 左端，V7H，BaH，M3，
z 二次下界，M5。它们是精确有限运算，不是数值证据。
新输入包括原 U,V 的自然系数，G_U,G_W 的可逐项生成符号结构，两个七次向量，
以及 Q4/P6 与所有有理身份；并没有宣称“删掉 56 个整数便无新整数”。
所绕过的是旧 b4 差表的 55 次、56 个大整数归约证书。
完整低次论证比原证书短且有结构，但仍需要以上有限代数付款及独立核验。



---

## 附录 III：两条完整边界、原50槽与两端逐项求值

原文件 J1HAND_CONTINUATION_STANDALONE_BOUNDARY_MANUAL_PROOF_LOCAL_20261007.md，bytes 42370，SHA256 b5504fd2dc31e485fe4fcb35c9512e50b90859c729e725774108964c740d8e33。

# 完整 J1 两条边界：原短除法、有限商法则及两端逐项求值（LOCAL 待独审）

2026-10-07。原根和全部三龄保留同一价格。已有连续符号证明不重复作为新工作；
本稿补足原根六项部分分式、上边界50槽身份的显式有限生成、两端完整有理求值。
本文含全部旧上边界证明及零边界的完整人工来源。程序输出是辅助交叉核验；
纸面证明通过有限规则和以下具体整数、分数逐步复核，表格本身不是免核验声明。

## 1. 原定义与上边界的同价格代入

原 F=R+T2+T3+T4 的完整定义和根分解见附录 C，原 t=1−u。
u=1/2 时 A=(l+2)/2，k=(2−l)/2，K=(37l+25)/(48l)，h=(13l+25)/(48l)。
令 S_j=Σ_(i=0..j−1)l^i，Q_j=S_j+1，特别 Q1=2、Q2=l+2。
对 (j,n)=(2,1),(3,3),(4,6)，令 m=24−2n，

    Cj=2Q_(j+1)²−Qj Q_(j+1)−lQj²，Jj=2mQ2−l−4，
    aj=−(24−n)(37l+25)+26l+50，bj=m(37l+25)−26l−50。       (1)

原年龄的 f=Cj/Q_(j+1)²、P=Jj/(2Q2)、v=lQjQ_(j−1)/Q_(j+1)²，
uZj/Z_(j−1)=Qj/(2Q_(j−1))。两个完整价格括号分别为 aj/(48l)、bj/(48l)，
原前缀2j l^(j−2)/Zj³=16j l^(j−2)/Qj³。因此逐因子相乘得

    Tj(l,1/2)=8j l^(j−2)CjJj/(Qj³Q_(j+1)²Q2)
               +j l^(j−3)aj/(6Qj²Q_(j−1))
               +j l^(j−2)bj/(6QjQ_(j+1)²)。             (2)

这里第二龄的 l^−1 真实保留；不允许用一项价格近似替代(2)。
每个 Cj 用(1)两次有限乘法和减法直接收集；其完整系数输出为：

| 年龄 | 种子 | 完整常数至最高次系数 |
| --- | --- | --- |
| 2 | C | 4, 0, 3, 2, 2 |
| 2 | J | 84, 43 |
| 2 | aj | -525, -825 |
| 2 | bj | 500, 788 |
| 3 | C | 4, 0, 1, 3, 2, 2, 2 |
| 3 | J | 68, 35 |
| 3 | aj | -475, -751 |
| 3 | bj | 400, 640 |
| 4 | C | 4, 0, 1, 1, 3, 2, 2, 2, 2 |
| 4 | J | 44, 23 |
| 4 | aj | -400, -640 |
| 4 | bj | 250, 418 |

一切向量按常数到最高次排列，含所有零槽；不得从非零槽推断尾。

## 2. 根六项分式的三个短除法

原根分解的 Qprice=25+2l/(2−l)，U1=2(1/2−Qprice)/l，
U2=2[Qprice*l(K/2−1)+1/2+2l+l/2−(h+K)l]/l，
Rreg=2[Qprice(2−K)+2h−1]/l。代入 R=Rreg+U1/A+U2/A²+1/A³。
由这四项的显示分母 l²、(l+2)³、(2−l) 可直接清除，有限共同分子为

    P(l)=−36800−2336l+13280l²+22568l³+60l⁴−5340l⁵，
    R(l,1/2)=P(l)/[96l²(l+2)³(2−l)]。                  (3)

(3)的六个输出整数仍需对上述四项的共同分子作有限乘加，
不是引用“CAS apart”。每项在形式无穷远至多 l^−1，故 P 次数≤5；
分母次数6，因而 R 是真分式。这只用于次数账，不扩张研究参数域。

若 a(z)/d(z) 的 d0≠0，前三项短除法是

    q0=a0/d0，q1=(a1−d1q0)/d0，
    q2=(a2−d1q1−d2q0)/d0。                            (4)

在 l=0，取 a=P、d=96(l+2)³(2−l)，得到 l²R 的前两项。
在 l=−2，取 z=l+2、a=P(−2+z)、d=96l²(2−l)，得到 (l+2)³R 前三项。
在 l=2，取 a=P(2)、d=96l²(l+2)³，得到 (2−l)R 的一项。
有限二项式移位产生的全部所需小整数如下：

| 极点 | a0,a1,a2（按所需） | d0,d1,d2（按所需） | q0,q1,q2（按所需） |
| --- | --- | --- | --- |
| 0 | -36800, -2336 | 1536, 1536 | -575/24, 359/16 |
| -2 | 12288, -213760, 306512 | 1536, -1920, 768 | 8, -775/6, 1091/32 |
| 2 | 22272 | 24576 | 29/32 |

逐行将三列整数代入(4)，精确得到

    Rhalf=1091/[32(l+2)]−775/[6(l+2)²]+8/(l+2)³
            +29/[32(2−l)]+359/(16l)−575/(24l²)。       (5)

减去(5)后，三个全部极点的所有主部均消失；剩余真分式的分子
被次数6的 l²(l+2)³(2−l) 整除，但其次数≤5，故只能是零。
所以这里的三个形式极点不是区间数值证据，而是全部有限有理身份的逐步证明。

## 3. 九个短商法则分子，直接生成50槽

下式中的撇号是 l 导数；给定多项式 f 的导数逐槽为 f'_i=(i+1)f_(i+1)，
乘法逐槽为 (fg)_i=Σ_(r=0..i)f_r g_(i−r)。因此本节不再需要一般有理约分。
把 Q2=l+2、Q2'=1、Q1=2 先收集，可以避免在第二龄人为多添一个 Q2 分母。

定义

    K21=(C2'J2+C2J2')Q2Q3−C2J2(4Q3+2Q2Q3')，
    K22=lQ2a2'−a2(Q2+2l)，
    K23=b2'Q2Q3−b2(Q3+2Q2Q3')，
    N2=96l²K21+Q2²Q3³K22+2l²Q2³K23。                (6)

分别对(2)的三项求导，分母为 Q2⁵Q3³、6l²Q2³、3Q2²Q3³；
乘 6l²Q2⁵Q3³，正好得到(6)的三个多项式。故

    T2'=N2/(6l²Q2⁵Q3³)。                              (7)

再定义

    K31=[C3J3+l(C3'J3+C3J3')]Q3Q4Q2
          −lC3J3(3Q3'Q4Q2+2Q3Q4'Q2+Q3Q4)，
    K32=a3'Q3Q2−a3(2Q3'Q2+Q3)，
    K33=(b3+lb3')Q3Q4−lb3(Q3'Q4+2Q3Q4')，
    N3=48K31+Q3Q4³K32+Q2²Q3²K33。                   (8)

三个商法则分母依次为 Q2²Q3⁴Q4³、2Q3³Q2²、2Q3²Q4³。
乘 2Q2²Q3⁴Q4³ 得(8)，故

    T3'=N3/(2Q2²Q3⁴Q4³)。                            (9)

最后定义

    K41=[2C4J4+l(C4'J4+C4J4')]Q4Q5Q2
          −lC4J4(3Q4'Q5Q2+2Q4Q5'Q2+Q4Q5)，
    K42=(a4+la4')Q4Q3−la4(2Q4'Q3+Q4Q3')，
    K43=(2b4+lb4')Q4Q5−lb4(Q4'Q5+2Q4Q5')，
    N4=24lQ3²K41+(Q2²Q4Q5³K42)/2
                     +(lQ2²Q3²Q4²K43)/2。            (10)

三个导数是32lK41/(Q2²Q4⁴Q5³)、2K42/(3Q4³Q3²)、
2lK43/(3Q4²Q5³)。乘 3Q2²Q3²Q4⁴Q5³/4 得(10)，即

    T4'=4N4/(3Q2²Q3²Q4⁴Q5³)。                        (11)

a4=−400−640l、b4=250+418l 全部系数为偶数，故(10)确实是整数多项式。
这里的 N3/N4 专指上边界导数分子，与移动极点的 N_j(y) 名称不同。

有限性已经由(6),(8),(10)证明。次数还可在乘法前用(2)核对：

| 年龄 | 三项形式无穷远增长度上界 | 导数上界 | 正规化分母次数 | 分子次数上界 |
|---|---|---:|---:|---:|
| 2 | −3、−2、−4 | −3 | 13 | 10 |
| 3 | −5、−4、−6 | −5 | 19 | 14 |
| 4 | −7、−6、−8 | −7 | 30 | 23 |

有理函数求导把增长度至少减1；已经有限的正规化分子遂得到这些次数，
绝非因为输出末行或被截断级数为零。完整50槽由九个 K 的有限卷积直接得到：

| 次幂 | N2 | N3 | N4 |
| --- | --- | --- | --- |
| 0 | 33600 | 127584 | -51200 |
| 1 | 134400 | 173872 | 42496 |
| 2 | -5392 | -74976 | 228736 |
| 3 | -23312 | -104952 | 420416 |
| 4 | 33532 | 103830 | 144672 |
| 5 | 190088 | 210991 | -109040 |
| 6 | 76721 | 490063 | 343224 |
| 7 | -33337 | 499251 | 1775708 |
| 8 | -42259 | 188138 | 3779022 |
| 9 | -11643 | -2110 | 6205389 |
| 10 | 1650 | -78768 | 8204253 |
| 11 | — | -91645 | 9014075 |
| 12 | — | -33545 | 8215273 |
| 13 | — | 3599 | 6323852 |
| 14 | — | 3004 | 4128182 |
| 15 | — | — | 2238499 |
| 16 | — | — | 940849 |
| 17 | — | — | 269347 |
| 18 | — | — | 47091 |
| 19 | — | — | 34566 |
| 20 | — | — | 47014 |
| 21 | — | — | 32160 |
| 22 | — | — | 11912 |
| 23 | — | — | 1920 |

例子：C2(0)=4、J2(0)=84、Q2(0)=Q3(0)=2，K22(0)=1050，
于是 N2(0)=Q2(0)²Q3(0)³·1050=33600。其他49槽依同一有限法核验，
应检查所有行及已证明次数，而非只检查示例或程序 PASS。

## 4. 全连续符号和边界单调性

附录 A 全文给出由(5)、(7)、(9)、(11)得到的连续正性证明。
根导数有三组正项；N2/N3 高负幂分别用 l≤10/7 给
65014109/2401、1509500348/117649，两组低幂有显式正项配对；
N4 的两个负项分别由343224l⁶和144672l⁴支付。
没有把50个系数一律假定为正，也没有用采样推全域正性。
所以 F_l(l,1/2)>0。

零边界的完整正文和独立审计中的原根短除法、原年龄有限几何身份，
均逐字保存在附录 B。它们证明 F_l(l,0)>1/4；已有纯代数推导不再重新算作新成果。

## 5. 两端的原函数逐项有理求值与实际加法

取 a=23/20。零边界使用附录 B 的原根 R0，并用直接有限几何式

    Tj(l,0)=4jm l^(2j−2)/(Sj³S_(j+1))
                  +2jm l^(j−2)/(Sj²S_(j+1)²)。        (12)

上边界用(2)、(5)，没有旧固定 λ 曲率或它的系数表依赖。
每项均用 l=a 精确代入有限几何和；所得 R、T2、T3、T4 分数如下：

| 边界 | 原完整分项 | 精确分值 |
| --- | --- | --- |
| zero | R | -36095287/3402160 |
| zero | T2 | 1276747648000/153394524747 |
| zero | T3 | 351604951731200000/158384001929967223 |
| zero | T4 | 47556881245300899840000000/74185509958660931204544203 |
| half | R | 102249275/195536754 |
| half | T2 | 1903793429227000/1159606697331663 |
| half | T3 | -6400702070195120000/118466732212112788389 |
| half | T4 | -24174268810613394227425280000000/19064449894922810454108947239521 |

为了完整暴露大整数加法，定义 V0=0，逐次加 R,T2,T3,T4。
若 V_(i−1)=p/q、下一项=r/s，则未约分分子 X=ps+rq、分母 Y=qs，
取 g=gcd(|X|,Y)，V_i=(X/g)/(Y/g)。下面记录所有四次等号；
g 的最大性可用欧几里得除法核验，等值与最终符号只需检查整除和整数乘加。

边界 zero：

| 步 | X | Y | g | V_i |
| --- | --- | --- | --- | --- |
| 1 | -36095287 | 3402160 | 1 | -36095287/3402160 |
| 2 | -1193119616851887389 | 521872716313253520 | 1849 | -645278321715461/282245925534480 |
| 3 | -2962697928068875685997086334803 | 44703239214578465426845156349040 | 396368281 | -7474609019153264905163/112782080094291060153840 |
| 4 | 4809056307814723111363852082445016239758163579911 | 8366796125993524218040794902186187374232260189520 | 68617800787 | 70084675589396387271362464256836518653/121933318031647807524198828593188782960 |

边界 half：

| 步 | X | Y | g | V_i |
| --- | --- | --- | --- | --- |
| 1 | 102249275 | 195536754 | 1 | 102249275/195536754 |
| 2 | 490830531524883285452325 | 226745729512893844441902 | 5751081 | 85345786561671325/39426627709276542 |
| 3 | 9858278344434072451527973679019205425 | 4670743746861529955190402965527670838 | 28804689 | 342245609540657510710425433825/162152201916206418864317645142 |
| 4 | 2604813357489947005417512515503220251619437145800752850197825 | 3091342528782923806085020280440649141349388381753512156056982 | 2331934122401667 | 1117018415085946227122957186306579293438218475/1325656029081618938569609234545181507892240946 |

最终付款：

F(a,0)−57/100=2913421556785684912845659793594561829/609666590158239037620994142965943914800>0。

F(a,1/2)−21/25=86683766434657968112135732215670670218402009/33141400727040473464240230863629537697306023650>0。

两个分母和差的分子都正，所以 F(a,0)>57/100、F(a,1/2)>21/25。
由第4节连续单调性，整个零/上边界分别有同一下界。
若独立已证明整个原矩形 F_uu<0，则凹函数的弦给
F(l,u)≥(1−2u)F(l,0)+2uF(l,1/2)>57/100。
本稿本身只闭合边界身份、单调性及两端算术，不独自宣告整个 J1 或速度定理。

## 6. 保留的有限核验负担

须核对：(i)原同价格代入；(ii)三个 C 和九个线性种子；(iii)根清分母六整数，
及三个极点2/3/1项短除法；(iv)九个 K 商法则与50槽有限卷积；
(v)两条高幂付款及低幂配对；(vi)两端八个分值、八次加法和两个付款；
(vii)零边界原几何表示、六条对数导数及三付款（附录 B 已审）。
这些是公开的逐步算术，仍须执行；附上表不会自动免去核验。

原生成新源 J1HAND_CONTINUATION_HALF_BOUNDARY_ORIGINAL_GENERATION_LOCAL_20261007.py
不读旧50槽。主任务辅助生成的数据和原生输出均保留，唯一辅助另核纸面和不同算法输出。

---

## 附录 A：已审完整上边界连续证明

来源 J1_HALF_U_COMPLETE_NORMALIZED_LAMBDA_MONOTONICITY_20261007_LOCAL.md，下文历史LOCAL/条件状态只表示原文件当时范围。

# 完整归一化 J1：u=1/2 边界对 lambda 严格增加

2026-10-07。完整 LOCAL 解析证明，待同一唯一辅助独立审计。不由点值推断连续符号；保留原完整根、三龄及全部价格。本结论只覆盖这一条边界。

## 1. 完整函数的精确代入

取原完整 F(lambda,u)=(25p+C0)/(kA)，定义见
`COMPLETE_FIRST_JOINT_BUDGET_SIX_COUPLED_TAYLOR_RECTANGLES_20261007_LOCAL.md` 第2节 (2)+(3)。
本证明严格使用同一 K 和原根+全部 s=2,3,4 年龄。
在 u=1/2 时，
\[
t=1/2,\quad k=1-\lambda/2,\quad A=(\lambda+2)/2,
\quad K=(37\lambda+25)/(48\lambda),\quad h=(13\lambda+25)/(48\lambda),
\quad Z_j=(S_j+1)/2,\quad S_j=\sum_{i=0}^{j-1}\lambda^i.
\]
令 \(Q_j=S_j+1\)，所以
\(Q_2=\lambda+2,\ Q_3=\lambda^2+\lambda+2,\ Q_4=\lambda^3+\lambda^2+\lambda+2\)，
\(Q_5=\lambda^4+\lambda^3+\lambda^2+\lambda+2\)。
所有 Q、lambda、2−lambda 在域 23/20<=lambda<=707/500 正。

原完整根准确化为
\[
R_{1/2}=
\frac{1091}{32Q_2}-\frac{775}{6Q_2^2}+\frac8{Q_2^3}
+\frac{29}{32(2-\lambda)}+\frac{359}{16\lambda}
-\frac{575}{24\lambda^2}.                                      \tag{1}
\]
此式可直接代入上述 t,k,A,K,h 于原根并清分母逐项核验。
其导数分组为
\[
R_{1/2}'=
\frac{-3273Q_2^2+24800Q_2-2304}{96Q_2^4}
+\frac{2300-1077\lambda}{48\lambda^3}
+\frac{29}{32(2-\lambda)^2}>0.                                \tag{2}
\]
确实，本域包含于 [1,10/7]；3<=Q2<4 给第一分子
>=−3273·16+24800·3−2304=19728>0；
第二分子>=2300−1077·10/7=5330/7>0。最后项严格为正。

## 2. 三个精确导数身份

从原年龄式代入第1节参数，取共同分母再用商法则，得到
\[
T_2'=\frac{N_2}{6\lambda^2Q_2^5Q_3^3},\quad
T_3'=\frac{N_3}{2Q_2^2Q_3^4Q_4^3},\quad
T_4'=\frac{4N_4}{3Q_2^2Q_3^2Q_4^4Q_5^3},                    \tag{3}
\]
其中完整整数多项式如下，没有删掉价格：
\[
\begin{aligned}
N_2={}&1650\lambda^{10}-11643\lambda^9-42259\lambda^8
-33337\lambda^7+76721\lambda^6+190088\lambda^5\\
&+33532\lambda^4-23312\lambda^3-5392\lambda^2+134400\lambda+33600,\\
N_3={}&3004\lambda^{14}+3599\lambda^{13}-33545\lambda^{12}
-91645\lambda^{11}-78768\lambda^{10}-2110\lambda^9
+188138\lambda^8\\
&+499251\lambda^7+490063\lambda^6+210991\lambda^5
+103830\lambda^4-104952\lambda^3-74976\lambda^2+173872\lambda+127584,\\
N_4={}&1920\lambda^{23}+11912\lambda^{22}+32160\lambda^{21}
+47014\lambda^{20}+34566\lambda^{19}+47091\lambda^{18}
+269347\lambda^{17}\\
&+940849\lambda^{16}+2238499\lambda^{15}+4128182\lambda^{14}
+6323852\lambda^{13}+8215273\lambda^{12}+9014075\lambda^{11}
+8204253\lambda^{10}\\
&+6205389\lambda^9+3779022\lambda^8+1775708\lambda^7
+343224\lambda^6-109040\lambda^5+144672\lambda^4
+420416\lambda^3+228736\lambda^2+42496\lambda-51200.
\end{aligned}                                                  \tag{4}
\]
(3) 是有理恒等式，(4) 只是三个分子的完整展开，不是连续符号的计算黑箱。
配套新源码自包含地重建原根与三龄，清分母核验 (1)–(4)。
人工核验也可按原年龄式的乘积/商法则与 Qj'=Sj' 逐步完成。

## 3. 两条短有理付款证明 N2、N3 正

令 b=10/7。本域 1<=lambda<b。将 N2 的中高阶组合除以正 lambda^5：
\[
\begin{aligned}
&190088+76721\lambda-33337\lambda^2
-42259\lambda^3-11643\lambda^4\\
&\quad\ge190088+76721-33337b^2-42259b^3-11643b^4
=\frac{65014109}{2401}>0.                                  \tag{5}
\end{aligned}
\]
余下有 1650lambda^10、134400lambda、33600，以及
\[
33532\lambda^4-23312\lambda^3-5392\lambda^2
\ge4828\lambda^2>0.
\]
故 N2>0。这里的下界用正项 lambda>=1、负项 lambda<=b，方向分别明确。

同样，将 N3 的以下完整组除以正 lambda^6：
\[
\begin{aligned}
&490063+499251\lambda+188138\lambda^2-2110\lambda^3
-78768\lambda^4-91645\lambda^5-33545\lambda^6\\
&\quad\ge490063+499251+188138-2110b^3-78768b^4
-91645b^5-33545b^6
=\frac{1509500348}{117649}>0.                              \tag{6}
\end{aligned}
\]
余下 3004lambda^14、3599lambda^13、173872lambda、127584 均正；
最后一组
\[
210991\lambda^5+103830\lambda^4-104952\lambda^3-74976\lambda^2
\ge134893\lambda^2>0.
\]
因此 N3>0。两次低阶组合都可以先把正高次幂降低到最大负幂，
再用 lambda>=1 降到 lambda²；没有把负高次幂错误降低。

## 4. N4 的两组显式正项配对

N4 只有两个负系数。对 lambda>=1，
\[
343224\lambda^6-109040\lambda^5
=\lambda^5(343224\lambda-109040)>0,
\]
\[
144672\lambda^4-51200\ge93472>0.
\]
(4) 的所有其他项严格为正，故 N4>0。这里没有 24 个逐项数值检验，
只有上述两次透明配对与其余整数系数的显式正性。

## 5. 完整边界结论及用途

(3) 分母全正，故三龄的导数均正。与完整根 (2) 相加，
\[
\boxed{\partial_\lambda F(\lambda,1/2)>0
\quad(23/20\le\lambda\le707/500).}                          \tag{7}
\]
结合已由主任务独立审阅的固定下 lambda 边界
F(23/20,1/2)>84/100，得整条上 u 边界 F(lambda,1/2)>84/100。
端点界依赖原固定边界证明；本文件不重新把它当作新连续证据。

若未来另行完整证明 F_uu<0 于全矩形，则 (7) 与已经独立审计的
零 u 单调性给出的 F(lambda,0)>57/100 可通过端点弦闭合
F(lambda,u)>57/100>11/20。但这里没有证明全矩形曲率，也没有
正 u 的 lambda 单调性。J1 六矩形仍保留，普通 GW 根、terminal-one
实际分布、有限均值、Mellin 勘误和整体定理范围均不改变。

完整精确身份核验小源码：
`j1_half_u_complete_normalized_lambda_monotonicity_20261007.py`。
该源码只检查新身份和 (5),(6) 的有理数正性，不调用旧证书或 runner。



---

## 附录 B1：已审完整零边界连续证明

来源 J1_ZERO_U_FULL_NORMALIZED_LAMBDA_MONOTONICITY_20261007_LOCAL.md，下文历史LOCAL/条件状态只表示原文件当时范围。

# 完整归一化 J1：零 u 边界对 lambda 严格增加

2026-10-07。完整 LOCAL 解析证明，待唯一辅助独立核验。只证明零 u 代数边界，不是正 u 的 lambda 比较；不退役六个 Taylor 矩形，不涉及 u=0 的速度或 canonical law 实现。

## 1. 精确目标、原完整函数与根

令 F(lambda,u)=(25p+C0)/(kA)，k=1-lambda*u、A=1+lambda(1-u)，使用原完整根及全部 s=2,3,4 年龄和同一 Kb。精确定义是 `COMPLETE_FIRST_JOINT_BUDGET_SIX_COUPLED_TAYLOR_RECTANGLES_20261007_LOCAL.md` 第 2 节的 (2)+(3)，不是去掉负价格后的表达式。本证明在 23/20<=lambda<=707/500 上给出

\[
\partial_\lambda F(\lambda,0)>1/4.                 \tag{1}
\]

由原完整根在 u=0 的代入并作部分分式，准确得到

\[
R_0(\lambda)=-\frac\lambda{12}-\frac1{12}
+\frac{44}{\lambda+1}-\frac{44}{(\lambda+1)^2}
-\frac{35}{12\lambda}-\frac{299}{12\lambda^2}.
\]

这是归一化 J1 的完整根，不是旧 C_R0 或 raw p。微分得

\[
R_0'=-\frac1{12}-\frac{44(\lambda-1)}{(\lambda+1)^3}
+\frac{35}{12\lambda^2}+\frac{299}{6\lambda^3}.
\]

在 1<=lambda<=10/7<2 上，(lambda-1)/(lambda+1)^3 的导数为 (4-2lambda)/(lambda+1)^4>0，而最后两个正项递减。因此 R0' 递减，且本区间上

\[
R_0'(\lambda)\ge R_0'(10/7)>17.                  \tag{2}
\]

最后一个只是明确的单点有理运算；它不是连续符号的点值推断，连续比较已由逐项单调性证明。

## 2. 保留全部三龄的几何表示

令 j=(lambda-1)/(lambda+1)、x=j^2。设

\[
\begin{aligned}
X_2(x)&=(1+x/3)^{-2},\\
X_3(x)&=\frac{1-x}{(1+x/3)^2(1+x)^2},\\
X_4(x)&=\frac{(1-x)^2}{(1+x)^2(1+2x+x^2/5)^2},\\
Y_2(x)&=\frac{(1-x)^2}{1+x/3},\\
Y_3(x)&=\frac{(1-x)^4}{(1+x/3)^3(1+x)},\\
Y_4(x)&=\frac{(1-x)^6}{(1+x)^3(1+2x+x^2/5)}.
\end{aligned}
\]

取 n=(1,3,6)、m_s=24-2n_s=(22,18,12)，w_X=(1/9,1/24,1/50)、w_Y=(2/3,2/9,1/10)。完整 s 龄在零 u 时准确为

\[
T_s(\lambda,0)=m_s\left[
w_{X,s}(1-j)^{2s+2}X_s(j^2)
+\frac{w_{Y,s}}2(1-j)Y_s(j^2)\right].             \tag{3}
\]

可以直接清分母核 (3)：把 lambda=(1+j)/(1-j) 代入原年龄式，使用有限几何和。所有价格在 u=0 因原始 u 因子为零；这不是在正 u 时删价。

因每个 X_s、Y_s 是正递减因子的乘积，它们在本域均介于 0 与 1 之间。注意这里 X_s、Y_s 不是随机变量。

## 3. 三条粗导数付款

设

\[
a=40/43,\quad J=7/40,\quad X=J^2,\quad D=800/1849.
\]

本 lambda 域给出 3/43<=j<J，故 1-j<=a、dj/dlambda=2/(lambda+1)^2<=D，且 1-j^2>=1-X>0。由显式对数微分，作为 j 的函数，负导数可用下列常数控制：

\[
\begin{aligned}
L_{X,2}&=4J/3,\\
L_{X,3}&=2J[(1-X)^{-1}+2/3+2],\\
L_{X,4}&=2J[2(1-X)^{-1}+6+4X/5],\\
L_{Y,2}&=2J[2(1-X)^{-1}+1/3],\\
L_{Y,3}&=2J[4(1-X)^{-1}+2],\\
L_{Y,4}&=2J[6(1-X)^{-1}+5+2X/5].
\end{aligned}                                                   \tag{4}
\]

具体而言，-(d/dj)X_s(j^2)<=L_X,s，Y_s 同理。例如

\[
-\frac d{dj}\log X_3(j^2)
=2j\left[\frac1{1-j^2}+\frac2{3+j^2}+\frac2{1+j^2}\right]
\le L_{X,3}.
\]

其余五式同样逐因子微分；乘以 X_s 或 Y_s<=1 即得到其负导数界。所有替换分母正，方向明确。

写 p_s=2s+2，由乘积微分及 (3)-(4)，

\[
0<-T_s'(\lambda,0)\le B_s:=m_sD\left[
w_{X,s}(p_sa^{p_s-1}+a^{p_s}L_{X,s})
+\frac{w_{Y,s}}2(1+aL_{Y,s})\right].              \tag{5}
\]

只剩三条固定的短有理付款：

\[
B_2<41/4,\qquad B_3<9/2,\qquad B_4<2.           \tag{6}
\]

每个 B_s 都已由 (4)-(5) 完整定义；(6) 可由分数乘法和交叉相乘逐步核验。相应精确小源码独立检查了原表达式到 (3) 的通用恒等式及这三条断言；没有抽样、旧证书或大符号表。保留这三条有理算术依赖，不称完全免计算。

## 4. 完整联合结论和边界

完整 F(lambda,0)=R0+T2+T3+T4。串联 (2) 和 (5)-(6)，

\[
\partial_\lambda F(\lambda,0)
>17-(41/4+9/2+2)=1/4.
\]

这证明 (1)。若另外使用新固定边界完整凹性证明给出的 F(23/20,0)>57/100，则整个零 u 边界上 F(lambda,0)>57/100。这个结论只利用原函数的代数延拓，不评价 u=0 的速度。

正 u 的 lambda 比较 F(lambda,u)>=F(23/20,u) 仍未证明；本结果不闭合整个 J1 矩形，也不退役旧六 Taylor 付款。普通 GW 根、实际 terminal-one law、有限均值、Mellin 勘误和整体定理边界均不变。

完整精确身份/算术源码：`j1_zero_u_full_normalized_lambda_monotonicity_20261007.py`。


---

## 附录 B2：原零边界代数来源及独立审计全文

来源 J1_INDEPENDENT_SHAPE_CHECK_20261007_ZERO_U_MONOTONICITY_AUDIT_PASS.md，下文历史LOCAL/条件状态只表示原文件当时范围。

# Independent audit PASS: complete normalized J1, zero-u lambda boundary

2026-10-07. **FINAL PASS within the stated boundary scope.** The same
single auxiliary independently audited the new main-task proof, after
the main task separately reviewed this auxiliary's fixed-lambda
concavity candidate. There was no new reviewer, restarted old task,
grid, LP, or old certificate execution.

## 1. Audited inputs and exact scope

Audited written proof:

`J1_ZERO_U_FULL_NORMALIZED_LAMBDA_MONOTONICITY_20261007_LOCAL.md`

SHA-256:
`895cbd334b1be7b3826e7778d9f65d8a5ec3b6bc9c0c5d82df69340556fde181`.

Audited accompanying source:

`j1_zero_u_full_normalized_lambda_monotonicity_20261007.py`

SHA-256:
`5036dca3d1c43892283e9ed966ae21cf9bff8634f16e56580c1cc92acfd2575c`.

The exact input function is Section 2, equations (2)+(3), of
`COMPLETE_FIRST_JOINT_BUDGET_SIX_COUPLED_TAYLOR_RECTANGLES_20261007_LOCAL.md`.
The auxiliary used those complete root and ALL s=2,3,4 age definitions,
specialized them independently at u=0, and checked the written
derivation, parameter domain, all comparison directions, all six
log-derivative bounds, and every finite payment.

The approved conclusion is precisely
\[
\boxed{\partial_\lambda F(\lambda,0)>1/4
\quad(23/20\le\lambda\le707/500).}
\]
This is the normalized algebraic zero-u boundary. It is not a speed
evaluation or canonical-law realization at u=0, and is not a lambda
comparison for positive u. The original-rho normalized-definition
transfer is an established input to this scoped audit, not newly
audited here.

## 2. Independent complete-root calculation

At u=0 put A=1+lambda. The original shared price specializes to
\[
K_0=\frac{\lambda^2+26\lambda+13}{24\lambda}.
\]
Using the original root, H=A, H_rho=0, and h=K0−1 gives directly
\[
R_0=\frac2\lambda\left[
48+2\lambda-\frac{24+\lambda}{A}
-\frac{\lambda(23+\lambda)}{A^2}-(23+\lambda)K_0\right].
\]
For a short manual verification of the partial fraction identity, use
\[
(\lambda+23)(\lambda^2+26\lambda+13)
=\lambda^3+49\lambda^2+611\lambda+299,
\]
\[
-\frac{2(24+\lambda)}{\lambda A}=-\frac{48}\lambda+\frac{46}A,
\qquad
-\frac{2(23+\lambda)}{A^2}=-\frac2A-\frac{44}{A^2}.
\]
Combining these terms yields exactly the proof's
\[
R_0=-\frac\lambda{12}-\frac1{12}+\frac{44}A-\frac{44}{A^2}
-\frac{35}{12\lambda}-\frac{299}{12\lambda^2}.
\]
Direct differentiation gives the displayed R0-prime formula.
The derivative of (lambda−1)/(lambda+1)^3 is
(4−2lambda)/(lambda+1)^4>0 on [1,10/7]; thus its negative multiple
decreases there. The two positive inverse powers also decrease.
Since 707/500<10/7, the continuous endpoint comparison is valid.
Independent exact Fraction arithmetic gives
\[
R_0'(10/7)=\frac{63090877}{3684750},\qquad
R_0'(10/7)-17=\frac{450127}{3684750}>0.
\]
No point value is used to infer an otherwise unproved continuous sign.

## 3. Independent three-age identity by finite geometric sums

Let S_s=1+lambda+...+lambda^(s−1). At u=0, Z_s=S_s,
r_s=S_s/S_(s+1), and all explicit price terms have their original
factor u=0. For the retained age factor,
\[
\lambda S_s=S_{s+1}-1,\qquad
f_s=2-r_s-\lambda r_s^2
=\frac{2\lambda^s}{S_{s+1}}+\frac{S_s}{S_{s+1}^2}.
\]
Consequently the COMPLETE zero-u age is
\[
\frac{T_s}{m_s}
=\frac{4s\lambda^{2s-2}}{S_s^3S_{s+1}}
+\frac{2s\lambda^{s-2}}{S_s^2S_{s+1}^2},
\qquad m_s=24-2n_s.
\]
This supplies a short direct derivation of the manuscript's geometric
representation without requiring a large symbolic expansion. With
j=(lambda−1)/(lambda+1), x=j^2,
\[
S_2=\frac2{1-j},\quad
S_3=\frac{3(1+x/3)}{(1-j)^2},\quad
S_4=\frac{4(1+x)}{(1-j)^3},\quad
S_5=\frac{5(1+2x+x^2/5)}{(1-j)^4}.
\]
Substitution gives, age by age, exactly
\[
T_s=m_s\left[w_{X,s}(1-j)^{2s+2}X_s(j^2)
+\frac{w_{Y,s}}2(1-j)Y_s(j^2)\right],
\]
with ALL six X/Y functions and ALL six weights as written in the
audited proof. For example the first displayed geometric-sum term
produces wY/2=(1/3,1/9,1/20), and the second produces
wX=(1/9,1/24,1/50). No age or signed contribution was omitted.

## 4. Independent check of all log-derivative directions

The exact parameter bounds are
\[
\frac3{43}\le j\le\frac{207}{1207}<\frac7{40}=J,
\quad 1-j\le a=\frac{40}{43},
\quad 0<\frac{dj}{d\lambda}\le D=\frac{800}{1849}.
\]
All X/Y factors are positive and decreasing on this j interval, and
are at most one. Writing x=j^2, their exact negative log derivatives
are 2j times, respectively,
\[
\begin{array}{ll}
X_2:&2/(3+x),\\
X_3:&1/(1-x)+2/(3+x)+2/(1+x),\\
X_4:&2/(1-x)+2/(1+x)+(4+4x/5)/(1+2x+x^2/5),\\
Y_2:&2/(1-x)+1/(3+x),\\
Y_3:&4/(1-x)+3/(3+x)+1/(1+x),\\
Y_4:&6/(1-x)+3/(1+x)+(2+2x/5)/(1+2x+x^2/5).
\end{array}
\]
For x<=X=J^2, replace 1/(1−x) by 1/(1−X),
1/(3+x) by 1/3, 1/(1+x) by 1, and the last denominator by 1.
For its positive numerator use x<=X. These substitutions give exactly
ALL six constants in equation (4) of the proof, with the correct upper
direction. Multiplication by X_s or Y_s<=1 gives the asserted bounds
on their ordinary negative derivatives.

Applying the product rule to (1−j)^p X_s and (1−j)Y_s gives
\[
-\frac{dT_s}{dj}=m_s\left[
w_X\{p(1-j)^{p-1}X_s+(1-j)^p(-X_s')\}
+\frac{w_Y}2\{Y_s+(1-j)(-Y_s')\}\right]>0.
\]
All terms are positive and all exponents are nonnegative; therefore
substituting 1−j<=a, X/Y<=1, the six derivative bounds, and
dj/dlambda<=D gives exactly the B_s in equation (5). There is no
incorrect sign reversal or independent-parameter extremization.

## 5. Independently recomputed exact short payments

The auxiliary rebuilt all three B_s from the explicit derivative
factor bounds above using standard-library Fraction arithmetic,
without importing or evaluating the author's source. The values and
their strictly positive gaps are
\[
B_2=\frac{151715039899998400}{14832326152275669},\qquad
\frac{41}4-B_2=\frac{1265212643308829}{59329304609102676}>0,
\]
\[
B_3=\frac{147204329518241835200}{33519409067903870199},\qquad
\frac92-B_3=\frac{7266022574651161391}{67038818135807740398}>0,
\]
\[
B_4=\frac{976461498325985889472198}{516478228054618799982925},\qquad
2-B_4=\frac{56494957783251710493652}{516478228054618799982925}>0.
\]
This independent run completed with exit code 0 and printed
`PASS independent Fraction payments`. These finite rational operations
are retained exact-arithmetic dependencies, now with explicit positive
integer-numerator certificates. No floating point evidence is used.

The supplied source was separately rerun to completion, exit code 0.
It produced the same three exact B_s and printed
`PASS generic full root/three-age identities at u=0` and
`PASS written analytic bounds imply F_lambda(lambda,0)>1/4 everywhere`.
This corroborates the independent manual identity derivation and
independent Fraction payments; it is not the sole basis of the verdict.

The combination is therefore valid on the whole stated lambda interval:
\[
F_\lambda(\lambda,0)=R_0'+T_2'+T_3'+T_4'
>17-\left(\frac{41}4+\frac92+2\right)=\frac14.
\]
The strict root/payment comparisons supply strictness at every endpoint
as well as in the interior.

## 6. Verdict and limitations

**PASS** for the entire written zero-u monotonicity proof, including
the original complete root and all three ages, its generic algebraic
identity, the six derivative bounds, and the three short rational
payments. The algebraic identity was also derived manually above,
rather than assumed from the supplied source's assertions.

Combining this audited zero-u monotonicity with the separately
lead-reviewed lower-lambda boundary result gives
F(lambda,0)>57/100. It does not give F(lambda,u)>=F(23/20,u) for u>0.
The six Taylor rectangles remain the existing full-rectangle proof;
no source or old deliverable was modified or retired by this audit.
There are no confirmed errors or mathematical blockers in this scope.


---

## 附录 C：完整原函数及全部移动极点身份

来源 J1_INDEPENDENT_MOVING_POLE_CURVATURE_IDENTITY_20261007_LOCAL.md，下文历史LOCAL/条件状态只表示原文件当时范围。

# Complete normalized J1: independent moving-pole curvature identity

2026-10-07. **Complete LOCAL identity proof, independently reconstructed
by the sole auxiliary; actual exact checks PASS.** This is a rational
identity, not a curvature sign estimate or a complete replacement of
the six Taylor rectangles. All original files remain unchanged.

## 1. Complete original input and statement

For 23/20<=lambda<=707/500 and 0<=u<=1/2 set
\[
t=1-u,\quad k=1-\lambda u,\quad A=1+\lambda t,
\quad S_j=\sum_{i=0}^{j-1}\lambda^i,\quad
Z_j=S_j-(S_j-1)u,
\]
\[
K=\frac{\lambda+1}{2\lambda}+\frac t2+
\frac{(\lambda+1)(2\lambda t-\lambda+1)t}{24\lambda},
\quad h=K-t.
\]
The complete normalized F is the original root plus ALL three ages
in Section 2 of
`COMPLETE_FIRST_JOINT_BUDGET_SIX_COUPLED_TAYLOR_RECTANGLES_20261007_LOCAL.md`.
Explicitly,
\[
G=2A-1-\lambda/A,\quad G_\rho=-1-2\lambda/A,
\quad H=A-\lambda u/A,\quad H_\rho=-2\lambda u/A,
\]
\[
B=A(G-KH),\quad B_\rho=u(A+1)G+AG_\rho-A(2hH+KH_\rho),
\]
\[
R=\frac2{\lambda A^2}[(25+\lambda/k)B-B_\rho].
\]
For (s,n_s)=(2,1),(3,3),(4,6), write
\[
m_s=24-2n_s,\quad P_s=m_s-u-u/A,
\quad E_s=-(24-n_s)K+2h,\quad V_s=m_sK-2h.
\]
Then the original age, including its complete signed price, is
\[
T_s=\frac{2s\lambda^{s-2}}{Z_s^3}
\left[(2-r_s-\lambda r_s^2)P_s+
\frac{uZ_s}{Z_{s-1}}(E_s+v_sV_s)\right],
\]
\[
r_s=Z_s/Z_{s+1},\quad
v_s=\lambda Z_sZ_{s-1}/Z_{s+1}^2,
\qquad F=R+T_2+T_3+T_4.
\]
The labels rho on G_rho,H_rho,B_rho refer to the prescribed original
rho derivatives; all later primes and F_uu below are u derivatives.

Define
\[
q_a=\rho=\lambda/S_2,\quad q_j=1-1/S_j\ (j=3,4,5),
\quad q_k=\lambda,
\]
\[
x_a=1-\rho u,\quad y=u/x_a,\quad
d_j=1-(q_j-\rho)y,
\qquad (m_a,m_k,m_3,m_4,m_5)=(4,1,3,3,2).
\]
Below c_jr are the complete principal coefficients defined in
Sections 3–4. Let
\[
N_j(y)=\sum_{r=1}^{m_j}\frac{r(r+1)}2c_{jr}
d_j^{m_j-r}(1+\rho y)^{r-1},\quad P_a=\rho^2N_a.
\]
For a, d_a=1. The target identity is
\[
\boxed{\frac{x_a^3F_{uu}}2=
P_a+\frac{q_3^2N_3}{d_3^5}+\frac{q_4^2N_4}{d_4^5}
+\frac{q_5^2N_5}{d_5^4}+\frac{c_kq_k^2}{d_k^3}
-\frac{23(\lambda+1)}{6\lambda}(1+\rho y)^{-3}.}       \tag{1.1}
\]

## 2. Short exact decompositions from the original root and ages

Expand the original age braces without inequalities. Its exact
four-term form is
\[
T_s=2s\lambda^{s-2}\left[
\frac{2P_s}{Z_s^3}-\frac{P_s}{Z_s^2Z_{s+1}}
+\frac{\lambda(uV_s-P_s)}{Z_sZ_{s+1}^2}
+\frac{uE_s}{Z_s^2Z_{s-1}}\right].                 \tag{2.1}
\]
For a direct check, the third term combines
−lambda P_s/(Z_sZ_(s+1)^2) from −lambda r_s² with
u lambda V_s/(Z_sZ_(s+1)^2) from the v_s price.
The other terms are the remaining two f_s terms and remaining price.

The root has a similarly exact useful decomposition. Write
Q=25+lambda/k and
\[
U_1=\frac2\lambda(1-u-Q),
\]
\[
U_2=\frac2\lambda[Q\lambda(Ku-1)+u+2\lambda+
\lambda u-2(h+K)\lambda u],
\]
\[
R_{\rm reg}=\frac2\lambda[Q(2-K)+2h-2u].
\]
Expanding the original G,H and B_rho gives
\[
\boxed{R=R_{\rm reg}+U_1/A+U_2/A^2+2u/A^3.}        \tag{2.2}
\]
For example B=(2−K)A²−A−lambda+Klambda*u and
\[
B_\rho=u(2A^2+A-1)-\frac{\lambda u(A+1)}A
-A-2\lambda-2hA^2+2(h+K)\lambda u.
\]
Substitution immediately verifies (2.2), including the u terms in U2.
R_reg is regular at the A pole, although it still has the distinct
k pole. These are identities of the complete original root.

## 3. All regular numerators of the complete principal parts

The following explicit lists specify the entire principal part at
each pole. Every omitted part is regular at the designated pole,
as follows directly from (2.1)–(2.2). They also give a finite manual
route to every coefficient, without expanding a large bivariate
numerator.

### A pole (a, represented as j=2)

The complete A-pole part is sum_(v=1..4) M_av/A^v, where
\[
M_{a4}=-8u,
\quad M_{a3}=2u+8(22-u)+4u/Z_3,
\]
\[
M_{a2}=U_2-4(22-u)/Z_3+4\lambda u/Z_3^2+4uE_2,
\]
\[
\begin{aligned}
M_{a1}={}&U_1+4\lambda(uV_2-22+u)/Z_3^2\\
&+6\lambda u[-2/Z_3^3+1/(Z_3^2Z_4)
+\lambda/(Z_3Z_4^2)+E_3/Z_3^2]\\
&+8\lambda^2u[-2/Z_4^3+1/(Z_4^2Z_5)+\lambda/(Z_4Z_5^2)].
\end{aligned}                                                    \tag{3.1}
\]
Here the root supplies 2u/A³,U2/A²,U1/A. Age 2 supplies the fourth,
third, second and first poles obtained by P2=22−u−u/A. Age 3
supplies the middle single-pole bracket, including its original
uE3/(Z3²A) price. Age 4 supplies the final single-pole bracket.
Thus every root and age A contribution is included.

### Z3 pole

The complete part is sum_(v=1..3) M_3v/Z3^v, where
\[
M_{33}=12\lambda P_3,
\]
\[
M_{32}=6\lambda[-P_3/Z_4+uE_3/A]
+4\lambda(uV_2-P_2)/A,
\]
\[
M_{31}=6\lambda^2(uV_3-P_3)/Z_4^2
-4P_2/A^2+8\lambda^2uE_4/Z_4^2.                    \tag{3.2}
\]
These are precisely the age-3 triple/double/single terms, age-2
double/single terms and age-4 single price contribution. The root
is regular at this pole. This recovers the separately audited full
N3 principal part.

### Z4 pole

The complete part is sum_(v=1..3) M_4v/Z4^v, where
\[
M_{43}=16\lambda^2P_4,
\]
\[
M_{42}=8\lambda^2[-P_4/Z_5+uE_4/Z_3]
+6\lambda^2(uV_3-P_3)/Z_3,
\]
\[
M_{41}=8\lambda^3(uV_4-P_4)/Z_5^2-6\lambda P_3/Z_3^2.
                                                               \tag{3.3}
\]
Age 4 supplies all three orders and age 3 supplies the double and
single additions. Root and age 2 are regular here.

### Z5 pole

Only age 4 contributes, with
\[
M_{52}=8\lambda^3(uV_4-P_4)/Z_4,
\quad M_{51}=-8\lambda^2P_4/Z_4^2.                 \tag{3.4}
\]
Its other two terms are regular here.

### k pole

Only the original root's lambda/k factor contributes. At u_k=1/lambda,
\[
c_k=\left.2B/A^2\right|_{u=u_k}
=\boxed{\frac{(\lambda-1)^2(-\lambda^3+23\lambda^2+\lambda+1)}
 {12\lambda^4}}.                                 \tag{3.5}
\]
For a direct derivation, A(u_k)=lambda,
K(u_k)=1+(lambda+1)(lambda−1)²/(24lambda²),
G(u_k)=2(lambda−1), H(u_k)=(lambda²−1)/lambda.
Substitution yields (3.5), with no price omission.

## 4. Finite coefficient definition and completeness of pole matching

Put u_j=1/q_j. For a use S_a=S2,Z_a=A; for j=3,4,5 use S_j,Z_j.
All M_jv in (3.1)–(3.4) are regular near u_j. This follows from
the distinct ordered slopes
\[
0<q_a<q_3<q_4<q_5<1<q_k<2.
\]
For example, at the A pole the other values are
k=−lambda,Z3=−lambda,Z4=−lambda*S2,Z5=−lambda*S3,
all nonzero. No singular denominator is silently evaluated as regular.

Since Z_j=S_j(1−q_ju), expand M_jv about u_j and use
u−u_j=−(1−q_ju)/q_j. The COMPLETE standard coefficient is
\[
\boxed{c_{jr}=\sum_{v=r}^{m_j}
\frac{M_{jv}^{(v-r)}(u_j)}
 {(v-r)!\,S_j^v(-q_j)^{v-r}}.}                   \tag{4.1}
\]
This formula includes every signed contribution and all lower-order
terms generated by variation of higher-pole numerators. The finite
jets used in the new source are exactly these derivatives divided by
their factorials. In particular c_a4=−8/(lambda*S2³).

Equations (2.1)–(3.5) show that the only possible finite u poles of F
are these five, with orders at most (4,1,3,3,2). Subtracting
\[
\sum_{r=1}^4c_{ar}(1-\rho u)^{-r}
+c_k(1-\lambda u)^{-1}
+\sum_{j=3}^5\sum_{r=1}^{m_j}c_{jr}(1-q_ju)^{-r}
\]
therefore removes ALL finite poles. The remainder is a polynomial
in u. No separate unsigned bounding operation occurs in this argument.

## 5. Exact infinity degree and quadratic remainder coefficient

This is the important remainder check; a root-only calculation would
not by itself establish the complete remainder degree.

As u tends to infinity at fixed lambda in the stated interval,
\[
A,k,Z_j\ (j\ge2)=O(u)\text{ with nonzero leading coefficients},
\quad P_s=-u+O(1),\quad K,h=\kappa u^2+O(u),
\quad \kappa=(\lambda+1)/12.
\]
In the four age terms (2.1), the first two are O(u^(−2)), the third
is O(1), and the fourth is O(1) for s=3,4. For s=2 the fourth is
**O(u)** because Z1=1. Thus each complete age grows at most linearly;
one must not incorrectly treat all ages as bounded at infinity.

Use the exact root decomposition (2.2). Since Q=25+O(u^(−1)),
\[
R_{\rm reg}=
\frac2\lambda[-25\kappa+2\kappa]u^2+O(u)
=-\frac{46\kappa}{\lambda}u^2+O(u).
\]
U1/A is O(1), U2/A² is O(u), and 2u/A³ is O(u^(−2)). Therefore
\[
F(u)=\beta u^2+O(u),\qquad
\boxed{\beta=-\frac{23(\lambda+1)}{6\lambda}}.     \tag{5.1}
\]
Every subtracted standard pole term decays at infinity. The polynomial
remainder of Section 4 thus has degree at most two and its exact
quadratic coefficient is beta. Its linear and constant coefficients
are irrelevant after two u derivatives. This establishes the complete
remainder contribution, including the original ages.

## 6. Differentiation and the common y-coordinate identity

For a standard pole term, direct differentiation gives
\[
\frac12\frac{d^2}{du^2}\frac{c_{jr}}{(1-q_ju)^r}
=\frac{r(r+1)}2c_{jr}q_j^2(1-q_ju)^{-r-2}.
\]
The exact common-coordinate identities are
\[
x_a=(1+\rho y)^{-1},\quad
1-q_ju=x_a d_j.
\]
After multiplication by x_a³ the term becomes
\[
q_j^2\frac{r(r+1)}2c_{jr}
\frac{(1+\rho y)^{r-1}}{d_j^{r+2}}.
\]
Collecting the same pole powers over d_j^(m_j+2) gives precisely
q_j²N_j/d_j^(m_j+2). For a the denominator is one, giving Pa;
for k, m_k=1, giving c_kq_k²/d_k³. Finally the polynomial remainder
contributes beta*x_a³, which is exactly the last term in (1.1).
This proves the complete requested curvature identity.

All x_a and d_j are positive on the physical rectangle, but positivity
is needed only for later inequalities, not for the algebraic equality.
No Pa/Nj sign or curvature inequality has been inferred here.

## 7. Actual independent checks, comparison and status

Self-contained new source:
`J1_INDEPENDENT_MOVING_POLE_IDENTITY_20261007.py`.
It imports no research source, old certificate or runner. Its rational
coefficient arithmetic uses numerator/denominator polynomials in
QQ[lambda] and gcd reduction, rather than the main task's fraction-field
implementation. All smooth contributions above were independently
derived before comparison with the exploration source.

The actual completed run, exit code 0, checked:

1. The original full three-age braces against the four-term identities.
2. The complete original root+three ages against each of the four
   smooth principal-part lists PLUS an explicit regular remainder;
   after exact cancellation each remainder lacks the designated
   independent denominator symbol.
3. Finite exact local extraction at A,Z3,Z4,Z5, of orders 4,3,3,2;
   the k coefficient was independently obtained from the complete root.
4. Exact agreement with all three separately audited N3 coefficients;
   also c_a4 and the resulting Pa cubic coefficient
   −80lambda^4/S2^8 were checked explicitly.
5. Generic second-derivative and common-coordinate identities for
   pole powers r=1,2,3,4.
6. The exact K quadratic coefficient and beta, with the complete
   infinity-degree proof in Section 5.

Its final output was
`PASS full moving-pole curvature identity by complete pole matching and infinity`,
followed by a scope line excluding Pa/N5 signs, full F_uu<0 and removal
of the six rectangles. No sampled parameter sign is used.

The main exploration file
`j1_remaining_moving_pole_qq_laurent_jets_exploration_20261007.py`
was then read as a comparison. Its A,Z4,Z5 regular numerator lists
and its local-to-standard coefficient formula agree with (3.1),
(3.3), (3.4), (4.1), term by term. It was not imported or rerun as
the basis of this identity proof. The new proof also includes Z3,
k and the complete quadratic remainder, which that exploration
alone did not certify.

This is a complete LOCAL identity result with finite exact algebraic
checks, awaiting the main task's review of the new proof. It is not
an auxiliary independent final audit of its own newly written proof.
Pa/N5 signs and the final coupled curvature payment remain separate.
Old six-rectangle files and all prior audit files are retained, and
no full-J1 or overall speed-theorem status is changed by (1.1) alone.



---

## 附录 IV：连续有符号比率、k界与余项付款

原文件 J1_UNIFORM_SIGNED_POLE_RATIO_LEMMA_20261007_LOCAL.md，bytes 4976，SHA256 01b604234dd99003c2bbff163ac307557aeb3dcaeba80d10d10a860127ff8226。

# J1 全 lambda 区间：有符号相邻极点的连续比率引理

2026-10-07。完整 LOCAL 引理，待同一唯一辅助独立审计。该引理本身不证明完整 F 的曲率；特别是下文 N>=−9 的应用是明确的条件式。

## 1. 参数和精确几何和

在 23/20<=lambda<=H=707/500、0<=u<=1/2 上，记
\[
S_j=1+\lambda+\cdots+\lambda^{j-1},\quad
\rho=\lambda/(1+\lambda),\quad y=u/(1-\rho u),
\quad Y=(\lambda+1)/(\lambda+2).
\]
令 q_j=1−1/S_j (j=3,4,5)，q_k=lambda，并记
\[
\alpha=q_3-\rho=\frac{\lambda^2}{S_2S_3},\qquad
 e=q_4-q_3=\frac{\lambda^3}{S_3S_4},\qquad
 D=q_4-\rho=\frac{\lambda^2}{S_4}=\alpha+e,
\qquad \delta_k=q_k-\rho=\frac{\lambda^2}{S_2}.       \tag{1}
\]
这些身份直接由 S_(j+1)=S_j+lambda^j 和 S4=S2(1+lambda²) 得到。我们有 0<=y<=Y<17/24<71/100；所有 d_j=1−(q_j−rho)y 正，因为 d_j=(1−q_j u)/(1−rho u)，而 q_j<1、q_k<2。

## 2. 五个连续粗界

\[
0<\alpha<19/100,\quad 0<e<9/100,\quad
D<28/100,\quad 0<\alpha-2e<11/1000.             \tag{2}
\]
这里不是由端点数值推断连续性质。alpha 的导数分子是 lambda(2+2lambda−lambda³)>0 于 [1,10/7]；因 lambda<3/2，有 2+2lambda−lambda³>=2−lambda/4>0。所以
alpha<=alpha(10/7)=700/3723<19/100。

为了控制 e，令 c=lambda−1>=0。直接展开
\[
9S_3S_4-100\lambda^3
=8-30c+6c^2+89c^3+63c^4+9c^5.
\]
函数 30c−89c³ 在 c>=0 的最大值是 20 sqrt(10/89)<7（平方后为 4000<4361）。因此上式>1，其余三项非负，从而 e<9/100。由 D=alpha+e 得 D<28/100。

又
\[
\alpha-2e=\frac{\lambda^2}{S_3}\frac{(\lambda-1)^2}{S_4}.
\]
第一因子严格增加，导数分子 lambda(2+lambda)>0。第二因子的导数分子是
(lambda−1)(3+3lambda+3lambda²−lambda³)>0；在本域 lambda<3/2 时，括号>=3+3lambda+(3/2)lambda²>0。故乘积增加。在 H 处
\[
\alpha-2e=\frac{3569671633500}{332868529723769}
<\frac{11}{1000},\qquad
\frac{11}{1000}-(\alpha-2e)|_H
=\frac{91882193461459}{332868529723769000}>0.
\]

## 3. 允许变号的双边二次包络

令 d3=1−alpha*y、d4=1−D*y，r3=(d4/d3)^5。由 (2) 和 y<71/100，d3>43/50。准确微分得
\[
r_3''(y)=\frac{10e(1-Dy)^3}{(1-\alpha y)^7}
\{2e-\alpha+\alpha Dy\}.                         \tag{3}
\]
因为 alpha−2e>0，且 0<1−Dy<=1，分别丢掉正项和负项可得
\[
-\frac{1}{25}<r_3''(y)<\frac{1}{10}.            \tag{4}
\]
(4) 的仅有两条定量付款是
\[
5\frac9{100}\frac{11}{1000}(50/43)^7<1/50,
\quad
5\frac9{100}\frac{19}{100}\frac{28}{100}\frac{71}{100}(50/43)^7<1/20.
\]
其正差分别为
78459236107/13590930555350 和 6234236107/5436372222140。

r3(0)=1、r3'(0)=−5e，对 (4) 两次积分给出
\[
L(y):=1-5ey-y^2/50\ \le\ r_3(y)\ \le\
U(y):=1-5ey+y^2/20.                              \tag{5}
\]
端点 y=0 为等号，故这里只使用弱不等号。

对任意实函数 N，若已另行证明 N(y)>=−9，则
\[
\begin{aligned}
N r_3&=(N+9)r_3-9r_3\\
&\le(N+9)U-9L=N U+(63/100)y^2.                 \tag{6}
\end{aligned}
\]
该论证不要求 N 非负。N3>=−9 是尚待证明的完整 F 系数义务，不能由本引理代付。

## 4. k 极点的统一比率界

记 dk=1−delta_k*y，rk=d4^5/dk^3。其对数导数为
\[
\frac{r_k'}{r_k}=
\frac{3\delta_k-5D+2D\delta_k y}{d_4d_k}>0,
\quad
3\delta_k-5D=\frac{\lambda^2(3\lambda^2-2)}{S_4}>0.
\]
因此 rk<=rk(Y)。准确代入得
\[
r_k(Y)=\frac{S_2^2(S_4+1)^5}
{(\lambda+2)^2S_4^5(2-\lambda)^3}=:\Phi(\lambda).
\]
Phi 也严格增加。确实，
\[
(\log\Phi)'=\frac2{S_2}-\frac2{\lambda+2}
-\frac{5S_4'}{S_4(S_4+1)}+\frac3{2-\lambda}>0.
\]
第一差为正。有限几何和给 lambda*S4'/S4<3，且 S4+1>=5，故负项>−3/lambda>=−3；最后项>3。本域所有分母正，比较方向没有改变。

所以对整个连续域，
\[
\boxed{\frac{d_4^5}{d_k^3}\le\Phi(H)<5.}       \tag{7}
\]
最后付款的正差是
\[
5-\Phi(H)=
\frac{7810521133897555222894719434215789155174968196289255}
{30553488005938652603121311614689577421321167214257851}>0.
\]

## 5. 可保留的负多项式付款

若完整曲率身份中有项 −23(lambda+1)/(6lambda)*(1−rho*u)^3*d4^5，则其绝对值>3/4。因为
\[
\frac{23(\lambda+1)}{6\lambda}>\frac{391}{60},
\quad 1-\rho u>12/17,\quad d_4>4/5,
\]
最后一个来自 D<28/100、y<71/100。因此
\[
\frac{23(\lambda+1)}{6\lambda}(1-\rho u)^3d_4^5
>\frac{391}{60}(12/17)^3(4/5)^5
=\frac34+\frac{19077}{18062500}>\frac34.         \tag{8}
\]
这里明确是“若身份中有该项”的应用；该身份仍须由完整 F 的多项式余项另行核验。

## 6. 覆盖和保留依赖

本引理证明 (2)、(5)、(7) 及条件式 (6)、(8)。精确源码 `j1_uniform_signed_pole_ratio_lemma_20261007.py` 只核验这里的小几何身份、微分身份及四条有理付款；不导入或运行旧矩形证书，不作采样。完整 F 的 Pa/N3/N5 符号、统一系数付款、另一条 u=1/2 边界仍未由本文件证明。J1 六个 Taylor 矩形仍是完整矩形的现有证明依赖。


---

## 附录 V：完整联合上界及 b5/b6 短证明

原文件 J1_JOINT_CURVATURE_UPPER_AND_HIGH_COEFFICIENTS_20261007_LOCAL.md，bytes 4549，SHA256 320147e4eaf94d0fb1aa48fefcfb91f78aa40482df21f71187a763465a9b5e53。

# J1 完整联合曲率上界与两个最高次系数的短付款

2026-10-07。完整 LOCAL 推导，待唯一辅助独立审计。
依赖已有完整moving-pole身份、Pa/N5、N3及有符号比率的指定PASS范围。
本稿支付b5<0和b6<1/20；不宣告其余系数或六矩形人工替代。

## 1. 同一lambda/u及所有符号输入

域lambda∈[23/20,707/500]、u∈[0,1/2]。
S_j=sum_(i=0..j−1)lambda^i，
rho=lambda/S2、xa=1−rho*u、y=u/xa、qj=1−1/Sj，
dj=1−(qj−rho)y (j=3,4,5)，qk=lambda、dk=1−(lambda−rho)y。
设D=q4−rho=lambda²/S4、e=q4−q3、z=q5−q4、
delta5=q5−rho=D+z。所有xa/dj/dk、D/e/z正。

完整身份证明和主任务独立复核已支付
\[
X:=x_a^3d_4^5F_{uu}/2
=P_a d_4^5+q_3^2N_3(d_4/d_3)^5+q_4^2N_4
+q_5^2N_5d_4^5/d_5^4+c_k\lambda^2d_4^5/d_k^3
-\frac{23(\lambda+1)}{6\lambda}x_a^3d_4^5.                 \tag{1}
\]
这里Pa三次，N3/N4二次，N5线性，来自完整根+全部三龄。
已审符号Pa>0、N3>−9、N5<0；Pa=p0+p1y+p2y²+p3y³中
p2>0、p3=−80lambda⁴/S2⁸<0；N5=t0+t1*y中t1>0。
完整root系数
ck=(lambda−1)²(−lambda³+23lambda²+lambda+1)/(12lambda⁴)>0，
因为lambda<2给其括号>21lambda²+lambda+1>0。

## 2. 三个联合包络逐项合法

v=Dy∈[0,1)，准确展开给
\[
(1-v)^5-\{1-5v+10v^2-5v^3\}
=-v^3(5-5v+v^2)\le0.
\]
故d4⁵<=Ra:=1−5Dy+10D²y²−5D³y³。
Pa>0保证Pa*d4⁵<=Pa*Ra，没有单独极大化其正负系数。

已审双边比率和N3>−9给
\[
N_3(d_4/d_3)^5
\le N_3 U+(63/100)y^2,\quad U=1-5ey+y^2/20.
\]
乘q3²时修正项也必须乘q3²。

对相邻4/5极点，d4=d5+zy，且0<=delta5*y<1。由
(1+E)^4>=1+4E+6E²+4E³，
E=zy/d5>=zy+z*delta5*y²+z*delta5²*y³，
E²>=z²y²(1+2delta5*y)、E³>=z³y³，得
\[
d_4^5/d_5^4=d_4(1+E)^4\ge R_{45}.
\]
其中保留共享参数后的准确短多项式是
\[
\begin{aligned}
R_{45}&=(1-Dy)[1+4zy+(4z\delta_5+6z^2)y^2
 +(4z\delta_5^2+12z^2\delta_5+4z^3)y^3]\\
&=1+(4z-D)y+10z^2y^2+10z^2(D+2z)y^3
 -4Dz(D^2+5Dz+5z^2)y^4.                                  \tag{2}
\end{aligned}
\]
由于N5<0，乘该下包络给上界；不需要原始c51/c52同时为负。
已审rk<5与ck>0给k项<5cklambda²。
已审负余项定量付款（其条件已由完整身份满足）给最后项<−3/4。
因此整个完整函数满足
\[
\boxed{X<P(y):=P_aR_a+q_3^2[N_3U+(63/100)y^2]+q_4^2N_4
+q_5^2N_5R_{45}+5c_k\lambda^2-3/4.}                       \tag{3}
\]
Pa、N3、N4、N5都在同一lambda/y；没有删除负价格或换canonical law。
P的次数至多6，记P=sum_(i=0..6)b_i*y^i。

## 3. b5是三个负项之和

N3*U次数<=4、N4次数<=2。故由(2)准确读出
\[
b_5=-5D^3p_2+10D^2p_3
-4q_5^2t_1Dz(D^2+5Dz+5z^2).                              \tag{4}
\]
全部已审p2>0、p3<0、t1>0，且D/z/q5正，
三个显示项各为负。因此
\[
\boxed{b_5<0.}                                            \tag{5}
\]
这不需要原degree42差多项式的符号表，只使用完整短乘积的次数和已付符号。

## 4. b6用两个基本平方不等式支付

只有Pa*Ra可能有y6项，所以
\[
b_6=-5D^3p_3
=\frac{400\lambda^{10}}{S_2^{11}(\lambda^2+1)^3}>0.         \tag{6}
\]
S2²>=4lambda、lambda²+1>=2lambda；本域lambda>1时均严格。
因而
\[
b_6<\frac{400\lambda^{10}}{(1024\lambda^5)S_2(8\lambda^3)}
=\frac{25\lambda^2}{512S_2}.
\]
lambda²/S2的导数lambda(lambda+2)/S2²正，
lambda<10/7给lambda²/S2<100/119。因此
\[
\boxed{0<b_6<625/15232<1/20,}                              \tag{7}
\]
最后短付款正差是1/20−625/15232=683/76160>0。
不需要探索degree17差多项式的全部符号，也不需要近临界点取样。

## 5. 准确的剩余付款

常数项另有完整新稿支付b0<−59/10，独立审计另记。
若未来再支付
b1<19/2、b2<−9、b3<13/2、b4<9/2，
则P可用
Q(y)=−59/10+(19/2)y−9y²+(13/2)y³+(9/2)y⁴+(1/20)y⁶上界。
该条件归约本身可逐步核验：
Q'=19/2−18y+(39/2)y²+18y³+(3/10)y⁵；
前三项最小值139/26>0，其余项非负，
所以Q增加；Y<71/100，且
Q(71/100)=−4310956816079/20000000000000<0。
但这四个中间系数界当前仍未付款，不能使用条件归约宣告全曲率。

配套自包含新源
`j1_joint_curvature_upper_and_high_coefficients_20261007.py`
核(2)、高次系数(4)/(6)、平方几何身份及短有理付款。
完整原F身份、各连续比率与系数符号有独立的完整证明/回执；
此源没有网格、LP、原大证书或高阶Taylor重跑。
旧六Taylor矩形及整体速度定理范围继续保留。


