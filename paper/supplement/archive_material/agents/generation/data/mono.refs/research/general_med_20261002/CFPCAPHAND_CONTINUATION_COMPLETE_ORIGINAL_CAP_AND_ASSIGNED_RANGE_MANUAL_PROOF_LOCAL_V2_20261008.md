# CF/P26 原 cap：四因子、有限生成、正分母、次数及实际范围接口

2026-10-08。完整可逐步核验的原 cap 证明；新独立审计由另存固定输入回执控制。本稿不重新证明已审 CF 非线性正性、全龄吸收、J1/J2/J3 或根 SIZE。全部旧正文、代码、回执与冻结记忆保留。四因子来自原 P26 第43–58行的 cap，而非原 P26 第11–30行的288龄枚举。

## 1. 固定对象与扩大标量域

全篇有限 cap 域为
\[
 23/20\le\lambda\le3/2,\qquad 0\le u\le\lambda^{-2}.
 \tag{1}
\]
令 \(c=\lambda-1,G=\lambda+1,d=1-u,g=c/G\)，使用原三项 atanh 包围
\[
 \ell_L=2(g+g^3/3+g^5/5),\qquad
 \ell_U=\ell_L+\frac{2g^7}{7(1-g^2)},
\]
\[
 K=K_{\rm cap}=\frac{c}{\lambda\ell_L}+\frac d2+
 \frac{\ell_U}{12c}(G-2\lambda u)d,
\]
\[
 k_0=\frac{\lambda^2+13\lambda+6
            -\lambda(3\lambda+7)u+2\lambda^2u^2}{12\lambda}.
 \tag{2}
\]
这里 \(k_0\) 是旧 coarse cap，\(K\) 是原 finite-atanh cap，均不是后来 small-u S4 比较的 \(K_b\)。本文四因子支付 \(2-(1+\lambda u)k_0\)，不是原 Gram 页另一组 \(2-(1+u)k_0\) 因子。

在 (1) 中，\(c>0,\lambda>0,d\ge1-\lambda^{-2}>0\)，\(0<g<1\) 且
\[
 1-g^2=4\lambda/G^2>0,\qquad
 G-2\lambda u\ge G-2/\lambda=c(\lambda+2)/\lambda>0.
\]
所以 (2) 的全部原分母和末项为正。\(u=0\) 与 \(u=\lambda^{-2}\) 只属于此扩大代数域；实际 hard 调用仍是 \(0<u<\lambda^{-2}\)。

## 2. 原有限 log 表达与完整公分母

对 \(0<g<1\)，直接积分几何级数给
\(\log\lambda=2\int_0^g(1-x^2)^{-1}\,dx
 =2\sum_{j\ge0}g^{2j+1}/(2j+1)\)。积分的余项正，且对 \(j\ge3\) 分母 \(2j+1\ge7\)，严格大于7的尾项存在。因此
\[
 2g<\ell_L<\log\lambda<\ell_U<\frac{2g}{1-g^2}
      =\frac{cG}{2\lambda}<c.
 \tag{3}
\]
最后 \(G<2\lambda\) 用 \(\lambda>1\)。严格 \(\ell_U<2g/(1-g^2)\) 也可逐项比较：前三分母有3、5，余尾用7，至少一个严格差。这里没有截去 log 的未知尾后当等式使用。

为把所有有限生成完全显式化，定义
\[
 D=15G^4+5c^2G^2+3c^4
   =23+48\lambda+98\lambda^2+48\lambda^3+23\lambda^4,
\]
\[
 J=105G^6-70c^2G^4-14c^4G^2-6c^6
  =15+554\lambda+1569\lambda^2+2444\lambda^3
        +1569\lambda^4+554\lambda^5+15\lambda^6.
\]
这两组向量由有限 binomial 乘法得到，显式系数全正。合并 \(\ell_U\) 的原分母时
\(7(1-g^2)(15+5g^2+3g^4)+15g^6
 =105-70g^2-14g^4-6g^6\)，故
\[
 \ell_L=\frac{2cD}{15G^5},\qquad
 \ell_U=\frac{cJ}{210\lambda G^5}.
\]
于是 (2) 的原 \(K\) 精确等于
\[
 K=\frac{N_K}{D_K},\quad D_K=2520\lambda G^5D>0,
\]
\[
 N_K=18900G^{10}+1260\lambda G^5D(1-u)
                    +DJ(G-2\lambda u)(1-u).
 \tag{4}
\]
这是原有理式的公分母来源，不是为得到漂亮系数改换价格。原 \(K>0\) 由 (2) 的正项直接保证。

有限次数在展开前已经闭合：\(D,J\) 分别四次、六次；\(D_K\) 十次，首系数 \(57960\)；\(N_K\) 三个乘积的 \(\lambda\) 次数至多10、10、11，\(u\) 次数至多0、1、2。\([\lambda^{11}]N_K=345(1-3u+2u^2)\) 不是零多项式，因此二元显示次数为 \((11,2)\)。某个固定 u 切片可以降次，但没有更高项。此处谈的是所列公分母表示的次数，不暗称每个切片都是约分后11／10次。全部展开向量在附录中打印。

## 3. 从有限价格到旧 coarse cap 与下界1

使用 (3) 的 \(\ell_L>2g,\ell_U<c\)，而 \((G-2\lambda u)d>0\)，得到
\[
 K<\frac G{2\lambda}+\frac{1-u}{2}
                 +\frac{(G-2\lambda u)(1-u)}{12}=k_0.
 \tag{5}
\]
把右边乘 \(12\lambda\)，直接收集就是 (2) 的 k0 分子：
\(6G+6\lambda(1-u)+\lambda(G-2\lambda u)(1-u)\)。没有导入 CF 正性或年龄吸收。

下界1同样独立。在区间 \([1,\lambda]\)，严格凸函数 \(x^{-1}\) 严格低于端点弦，所以
\(\log\lambda<c(1+1/\lambda)/2=cG/(2\lambda)\)。结合 (3)，
\[
 K>\frac{2}{G}+\frac{1-\lambda^{-2}}2>1,
\]
\[
 \frac{2}{G}+\frac{1-\lambda^{-2}}2-1
       =\frac{c[2-c^2]}{2\lambda^2G}>0,
 \qquad2-c^2\ge7/4.
 \tag{6}
\]
这个独立正下界用于后面的 prefix 比较；没有从 \(\Delta_2>0\) 反推它。

## 4. 原三次分子及四因子生成，完整无尾

仅作原代换 \(\tau=\lambda^2u\in[0,1]\)。由 (2) 直接得到
\[
 k_0=\frac{M(\lambda,\tau)}{12\lambda^3},\quad
 M=\lambda^2(\lambda^2+13\lambda+6)
                  -\lambda(3\lambda+7)\tau+2\tau^2.
\]
于是原清分母恰为
\[
 C(\lambda,\tau)=12\lambda^4[2-(1+\lambda u)k_0]
                 =24\lambda^4-(\lambda+\tau)M.
 \tag{7}
\]
这是一次乘二次的有限产品，\(\tau\) 次数至多三；最高系数 \(-2\ne0\)，所以三次精确，四次以上完全不存在。\(\lambda\) 次数至多五，首项来自常数 \(-\lambda^5\)，故显示二元次数为 \((5,3)\)。没有多项式除法、未知商余项或截断。

展开全部四个普通系数为
\[
 \begin{split}
 p_0&=-\lambda^3(\lambda^2-11\lambda+6),\\
 p_1&=\lambda^2(1-10\lambda-\lambda^2),\\
 p_2&=\lambda(3\lambda+5),\\
 p_3&=-2,\qquad C=\sum_{i=0}^3p_i\tau^i.
 \end{split}
\]
定义 \(B_j^3(\tau)=\binom3j\tau^j(1-\tau)^{3-j}\)。其权和为1，且直接有限乘法给
\[
 1=\sum_{j=0}^3B_j^3,\quad
 \tau=B_1^3/3+2B_2^3/3+B_3^3,\quad
 \tau^2=B_2^3/3+B_3^3,\quad \tau^3=B_3^3.
\]
因此四个控制值是
\[
 \beta_0=p_0,\quad\beta_1=p_0+p_1/3,\quad
 \beta_2=p_0+2p_1/3+p_2/3,\quad
 \beta_3=p_0+p_1+p_2+p_3.
\]
逐项代入得到原 P26 的全部四因子：
\[
 \begin{split}
 \beta_0&=-\lambda^3(\lambda^2-11\lambda+6),\\
 \beta_1&=-\frac{\lambda^2}{3}(3\lambda^3-32\lambda^2+28\lambda-1),\\
 \beta_2&=-\frac{\lambda c}{3}(3\lambda^3-28\lambda^2+10\lambda+5),\\
 \beta_3&=-c^2(\lambda^3-8\lambda^2-\lambda+2),
 \end{split}
 \tag{8}
\]
\[
 \boxed{C(\lambda,\tau)=\sum_{j=0}^3\beta_jB_j^3(\tau).}
 \tag{9}
\]
四因子均五次 \(\lambda\) 表达，因式中没有需另作假设的零或负分母；唯一3为正。附录给四个完整展开向量及其内置零，以便由原 (7) 逆重构。

## 5. 四因子的全部连续符号付款

第一因子由原二次的端点组合支付：
\[
 -\lambda^2+11\lambda-6
 \ge-(3/2)^2+11(23/20)-6=22/5>0.
\]
对另外三个因子记括号三次为 \(f_1,f_2,f_3\)。全部左端值与整个区间的导数上界是

|函数|\(f_i(23/20)\)|\(f_i'(\lambda)\) 的全区间上界|
|---|---|---|
|\(3\lambda^3-32\lambda^2+28\lambda-1\)|\(-52459/8000\)|\(9(3/2)^2-64(23/20)+28=-507/20\)|
|\(3\lambda^3-28\lambda^2+10\lambda+5\)|\(-127739/8000\)|\(9(3/2)^2-56(23/20)+10=-683/20\)|
|\(\lambda^3-8\lambda^2-\lambda+2\)|\(-65673/8000\)|\(3(3/2)^2-16(23/20)-1=-253/20\)|

各导数的二次正项使用上端、一次负项使用下端，所以这些是真正全区间上界；不假设导数单调，不以两点取样替代证明。三者均严格递减且在左端负，故全区间负。\(\lambda,c,1/3\) 正，于是四个 \(\beta_j\) 全部严格正。

权 \(B_j^3\ge0\) 且和1，故 (9) 严格正，含 \(\tau=0\) 和 \(\tau=1\) 两端；它们分别由 \(\beta_0,\beta_3\) 支付。分母 \(12\lambda^4>0\)，因而完整标量 cap 定理是
\[
 \boxed{(1+\lambda u)k_0<2,
 \quad1<K_{\rm cap}<k_0<\frac2{1+\lambda u}.}
 \tag{10}
\]
所有连续符号付款就是上述一二次、三左端、三导数七笔，加 (6) 的 \(7/4\) 下界；实际域包含另有两笔在第8节列出。附带精确 source 共核十笔，不把它们叫全题有限算术总量。

## 6. 原 second-prefix 所有正分母

固定 (1) 的 \(u\)，令 \(A=1+\lambda d\)、\(r_1=1/A\)，对 \(0\le z\le r_1\) 定义原 normalized prefix
\[
 Q=2+2\lambda uz+2Au z^2/d,\quad
 R=1+A^2(K-d)z^2/d,\quad D_f=Q-R,
 \quad D_w=Q-G uR.
\]
\(K>1\ge d\) 给 \(R>0\)；\(Q>0\)。两分母的完整二次式为
\[
 D_f=1+2\lambda uz+[2Au/d-A^2(K-d)/d]z^2,
\]
\[
 D_w=2-Gu+2\lambda uz+
                [2Au/d-GuA^2(K-d)/d]z^2.
\]
它们的线性系数非负，常数分别1和 \(2-Gu>0\)；后一差由
\(u\le\lambda^{-2}\) 和 \(2\lambda^2-G=c(2\lambda+1)>0\) 保证。若二次系数非负，整个非负 z 域正；若二次系数负，它是凹函数，不小于两个端点值的线性插值。右端直接代入原式为
\[
 D_f(r_1)=(2-K)/d>0,\qquad
 D_w(r_1)=[2-GuK]/d>0.
 \tag{11}
\]
第一项由 (10)；第二项由
\(1+\lambda u-Gu=1-u=d>0\) 和 \(K>0\)，所以
\(2-GuK>2-(1+\lambda u)K>0\)。故整个域 \(D_f,D_w>0\)。所有因子 \(d,A,z\) 的正性使用情况清楚：在本二次分母引理允许 z=0，在实际校准下一节要求 z>0，不作零分母延拓。

原实际 \(b=uz\)、\(\rho=Az\)，\(\beta_2=u/A\)。使用同一 K，
\[
 T_2=u^2R,\qquad
 Q_2=u+\lambda u^2z+Au^2z^2/d=uQ/2.
\]
原 ζ2 的完整归一化身份为
\[
 \zeta_2=2Q_2-GT_2=uD_w>0\quad(u>0).
\]
该 \(u\) 因子保留，\(V_2(K)=cT_2/\zeta_2=cuR/D_w\)。这不是对未归一化对象再次除 \(u^2\)。

## 7. 原 pipe 上界和 assigned 校准：无 CF 循环

取实际 \(0<u<\lambda^{-2}\)、\(u<z<r_1\)，仍固定同一法则的 u,b。设
\[
 T_\pi=u^2K/d,\quad Q_\pi=u/d,\quad
 v_\pi(K)=\frac{cT_\pi}{2Q_\pi-GT_\pi}
           =\frac{cuK}{2-GuK}.
\]
上节保证全部比较分母正。直接有限乘法给精确二项差
\[
 T_\pi Q_2-T_2Q_\pi
 =(1-\rho^2)\frac{u^3(K-1)}d
       +\lambda(\rho-\rho^2)u\beta_2T_\pi\ge0.
 \tag{12}
\]
它通过正分母交叉相乘（共同的 \(GT_2T_\pi\) 恰抵消）给
\[
 V_2(K)\le v_\pi(K)<h,\qquad h=cu/d.
 \tag{13}
\]
严格后项等价于
\(Kd<2-GuK\)，即 \((1+\lambda u)K<2\)，正好由 (10) 支付。前项标量 \(\rho=1\) 可等号，实际 \(\rho<1\) 且 K>1 则严格；不把 pipe 的速度当作另一个实际法则。

实际 upstream 进口仍是原解析 second-prefix/Euler 比较
\(v<V_2(\kappa)\)、\(\kappa<K_{\rm cap}\)，同一固定实际 u,b；其全级数与概率证明未在本有限 cap 稿中重证。T2对K斜率 \(u^2\rho^2/d>0\)，Q2 固定，故
\(\partial_KV_2=2cQ_2(\partial_KT_2)/\zeta_2^2>0\)。如果需要 κ 到 K 的整段正分母，因为 \(\zeta_2\) 随 K 减少，较小 κ 的分母更大，始终正。得到
\[
 0<v<w:=V_2(K)<h.
\]
没有使用 CF 的 \(\Delta_2>0\) 来取得 w<h 或 cap 域。

原 canonical hard 进口为 actual variance \(b>u^2\)、\(b<\beta_2\)、raw \(0<\alpha<1\)，及
\(\alpha=(u-vA_0/c)/b\)。其中
\[
 A_0=1-Gu+\lambda b>(1-u)(1-\lambda u)>0.
\]
这一前置 actual hard 域已由原 v<h/raw 校准得到 \(u<\lambda^{-2}\)，不是 CF 传播结论。定义同一 assigned pair
\[
 a=\frac{u-wA_0/c}{b}.
\]
则 w>v 给 a<α<1，w<h 给
\[
 a>\frac{u-hA_0/c}{b}
  =\frac{\lambda h}{c}\left(\frac ub-1\right)
  >\frac{\lambda h}{c}(A-1)=\lambda^2u>0.
 \tag{14}
\]
中间严格不等式正好用 \(b/u=z<1/A\)，没有假设某个自由第三矩能实现此法则。因此原合法 assigned range 是
\[
 \boxed{\lambda^2u<a<\alpha<1,\qquad v<w<h,\qquad D_f,D_w>0.}
\]
完整 CF、非根 \(\Delta_s\) 传播、原根和全龄价格仍由自己的已审模块付款。

## 8. 45 节点实际入口出口及证明责任

本稿标量 cap 覆盖原 actual near-bias 调用域，精确包含比较为
\[
 4/3-(23/20)^2=13/1200>0,\qquad
 3/2-707/500=43/500>0.
\]
实际固定 μ₀=0、μ₁>0、有限 m>1、ordinary root 同 μ、terminal-one canonical／父权 λ每子权1、λ<m 保持。原 MARKER_CAL 由实际矩和 raw hard 提供 \(u<\lambda^{-2}\) 与原固定法则；上节的 actual prefix/\(\kappa\) 解析进口保持，未导入旧 P06 Gram sign 或已审 nonlinear CF sign。

旧宏节点清单把四 cap 来源列在 H_P26，而 H_CF 的正文把 legal assigned range 作为先行输入。这是来源责任位置应明确的表示问题，不是 cap 的数学循环：本稿 §§1–7 独立于 CF 正性，应该先作为 H_CF 的内部前置引理来源；H_P26 在 CF 已给非根正 Δ 后再复用同 cap 配合全龄吸收。新 source overlay 将完整本稿同时列入 H_CF 与 H_P26，保留原45父关系，不添加反向 CF←P26 边，也不让 cap 依赖它将支持的 Δ2。

本稿的新输出恰是原范围、不变 Kcap、正 prefix 分母和四因素 cap；没有把新 Kcap 与 Kb 对换。H_P26 的 all-age 条件仍为已审 \(s\ge2\)，原 root s=1 的 \(\Delta_1=-(1-a)u<0\) 不能删除；marker Δ 的非负差分是另一个对象。旧288及旧s≥8 tail 在最新实际链已被全龄证明替代，不执行也不重新退休一次。其旧source依然保存。

H_S4_COMMON 的 full-T K-affinity、正d、Kcap<Kb和完整根／三龄支出沿旧scope采用；H_SMALLU、H_HIGHU、已审 J2 新全文、T1 正锚和更低／更高λ支路均保持。本 cap 证明不单独给 Fstar或Φ正性，不是完整根 SIZE，也不证明新速度区间。其他解析／概率定理和旧已审节点仍作为明确作用域进口，未在本轮从零重审。

## 附录. 全部有限展开向量的读取规则

向量 \([v_0,\ldots,v_n]\) 一律指 \(\sum_{i=0}^nv_i\lambda^i\)；空向量是零多项式，全部内置零保留。有限乘法是 \((f*g)_j=\sum_{i=0}^jf_ig_{j-i}\)，超出已列范围的系数为零。以此从 (4)、(7) 得下面完整向量，再用第4节的四行基变换可逆重构四因子 (8)。原分母和次数来源已先在正文封口，附录不是事后猜测一个任意多项式。

本稿结论以 §§3–7 的连续比较成立。配套 Fraction 有限生成只作精确一致性证据；新正式独立审核必须同时接受原对象、生成、次数、付款和实际接口，不能只签四个因子表或十个正分数。整体纯人工速度定理状态保持未完成。

### 全部原有限系数

**D 与 J：按 对象行0=D、1=J 幂的完整 λ 向量。**

|幂 j|完整向量（常数起）|
|---|---|
|0|`[23, 48, 98, 48, 23]`|
|1|`[15, 554, 1569, 2444, 1569, 554, 15]`|

**D_K：按 u（唯一零次） 幂的完整 λ 向量。**

|幂 j|完整向量（常数起）|
|---|---|
|0|`[0, 57960, 410760, 1431360, 3144960, 4631760, 4631760, 3144960, 1431360, 410760, 57960]`|

**N_K：按 u 幂的完整 λ 向量。**

|幂 j|完整向量（常数起）|
|---|---|
|0|`[19245, 231787, 1133491, 3234365, 6062114, 7828398, 7034598, 4361114, 1816865, 471991, 61687, 345]`|
|1|`[-345, -43477, -309915, -1094663, -2466186, -3733794, -3896838, -2761310, -1339437, -411289, -69711, -1035]`|
|2|`[0, 690, 26924, 128298, 373072, 668196, 831240, 668196, 373072, 128298, 26924, 690]`|

**M：按 τ 幂的完整 λ 向量。**

|幂 j|完整向量（常数起）|
|---|---|
|0|`[0, 0, 6, 13, 1]`|
|1|`[0, -7, -3]`|
|2|`[2]`|

**C：按 τ 幂的完整 λ 向量。**

|幂 j|完整向量（常数起）|
|---|---|
|0|`[0, 0, 0, -6, 11, -1]`|
|1|`[0, 0, 1, -10, -1]`|
|2|`[0, 5, 3]`|
|3|`[-2]`|

**β0..β3：按 控制行j 幂的完整 λ 向量。**

|幂 j|完整向量（常数起）|
|---|---|
|0|`[0, 0, 0, -6, 11, -1]`|
|1|`[0, 0, 1/3, -28/3, 32/3, -1]`|
|2|`[0, 5/3, 5/3, -38/3, 31/3, -1]`|
|3|`[-2, 5, 4, -16, 10, -1]`|

### 全部小有理付款的精确记录

|付款|正值|
|---|---|
|quadratic_lower|22/5|
|cubic1_negative_left|52459/8000|
|cubic2_negative_left|127739/8000|
|cubic3_negative_left|65673/8000|
|cubic1_negative_derivative_cap|507/20|
|cubic2_negative_derivative_cap|683/20|
|cubic3_negative_derivative_cap|253/20|
|K_lower_residual_factor|7/4|
|actual_lambda_lower_square_gap|13/1200|
|actual_lambda_upper_gap|43/500|

以上向量为原有限产品的完整输出；同一对象的因式与展开是重复表示，不另作全局成本加总。原源 root_canonical_profile_payment.py，2538字节，SHA256 e691e1c2e400cf15baf820fa67ed6ecc44c3916f6747f689a936dd69327b93bf，仅只读第43–58行与原校准 identity；其整个288循环没有执行。旧原主文与 all-age 最终回执作为保全／接口来源留存，新四因素正性由本稿全部原链及连续付款证明。
