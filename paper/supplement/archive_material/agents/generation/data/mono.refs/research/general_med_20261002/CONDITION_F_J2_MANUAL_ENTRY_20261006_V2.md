# Condition-F/J2人工入口：精确合同、条件传播与两个三次式

2026-10-06 V2。新增修订依据：独立入口审核PASS；年龄/零点范围修正；H的标量覆盖被一个严格有理点排除。V1冻结保留。挑战证明与源见 CONDITION_F_H_SCALAR_OBSTRUCTION_20261006.md 和 condition_F_H_scalar_obstruction_20261006.py；挑战独立审核待定。

下一唯一主目标为Condition-F/J2的两块9744项张量；不重开5076，不开启9600/S42，不创建代理/任务。本文是精确入口及新候选的接续记录，不是新的正性证明。两个9744 checker依赖仍保留。

## 1. 原已证入口及变量范围

同一原实际terminal-one canonical law，λ<m，2/√3≤λ≤707/500。c=λ−1、U=X/(c+X)、u=EU、b=EU²、e=EU³，h=cu/(1−u)。原Condition-F假设h<1/(λ+1)，等价0<u<λ^−2。令z=b/u、θ=e/b，并写d0=1−u（此处不是旧pipe参数d）。

 A=1+λd0，B=1+λ(λ+1)d0，C3=1+λ(λ+1+λ²)d0，
 r1=1/A，r2=A/B，r3=B/C3。

actual必要约束u<z<r1、z≤θ<r2、u<λ^−2。四阶Gram加严格canonical a4<r3e给

 G(θ)=θ²−(2u+r3)θ+(r3u/z)θ+uz<0。

原全Q,T不等式是

 2u(b−e)Q>[(b−e)+b(u−b)]T。                 (F)

hard校准时它等价于Δ2>0。这里Q,T是完整实际矩阵列的speed sums，不是冻结匹配pipe速度。

精确matched pipe系数κ及严格上界仍是原解析Bose/Euler入口：

 g=c/(λ+1)，ℓL=2(g+g³/3+g⁵/5)，
 ℓU=ℓL+2g⁷/[7(1−g²)]，
 κ<K=c/(λℓL)+d0/2+ℓU(λ+1−2λu)d0/(12c)。

同一实际b的第二prefix为

 E=(K−d0)/d0，R(z)=1+A²Ez²，
 T2=u²R，Q2=u+λu²z+(Au²/d0)z²，
 Df=1+2λuz+(2Au/d0−A²E)z²，
 s2=uR/Df，θcrit=1−s2(1−z)。

已审range给Df>0、0<s2<1、θcrit>z。精确身份

 J2(K,θ)=2u(b−e)Q2−[(b−e)+b(u−b)]T2
       =bu²Df(θcrit−θ)。                    (1)

现在两块9744张量证明的唯一有限正性入口是G(θcrit)≥0，覆盖λ∈[2/√3,707/500]、u=ξ/λ²、z=u+η(r1−u)、ξ,η∈[0,1]（清分母的闭多项式域）。actual原分式只在u>0、z>u评估。

G(z)=(z−u)(z−r3)<0、θcrit>z使G(θcrit)≥0把θcrit放在上Gram根之上；actual G(θ)<0于是θ<θcrit，(1)严格正。κ<K的负系数方向继而给actual F。原精确J(Eenv)>0还用Eenv/b≥z、≤r2、G(Eenv/b)≤0及V3(Eenv)≤V2；严格式来自κ<K。g、E、Eenv不是同一个变量。

## 2. 为什么控制全部assignedΔ_s：入口与传播严格分开

实际hard rawα<1时，解析prefix range先给v<w=V2(K)<h及

 a=(u−wA0/c)/b<α<1，a>λ²u>0，A0=1−(λ+1)u+λb。

这一步独立于J2/F的正性；由实际law固定、speed prefix及cap得到，不用新SIZE或Condition-F张量结论。定义ζ2=2Q2−(λ+1)T2>0、D3=u−(λ+1)b+λe=EU(1−U)(1−λU)>0。

 assignedΔ2=a(b−e)−(w/c)D3，
 J2(K,θ)=bζ2 assignedΔ2。                   (2)

故待付J2(K,θ)>0正是assigned入口，不只是actual F。将δw=w/c、

 Qa(U)=−δw+[1+(λ+1)δw]U−[a+λδw]U²，
 P(U)=Qa(U)−(1−a)U，Δ_s=EU^(s−1)P(U)。

P凹，P(0)=−δw<0，P(1/λ)=ac/λ²>0，在区间(0,1/λ)恰有一个向上零点ξ0；不声称ξ0属于实际支持集合。若Δ2>0，

 Δ_s−ξ0^(s−2)Δ2=EU[U^(s−2)−ξ0^(s−2)]P(U)≥0，s≥2。

于是每个整数s≥2都有Δ_s>0。s=1则Δ1=EP=−(1−a)u<0，root必须单独处理。**单交叉只是给定Δ2后的传播；它没有证明Δ2。** t0=EQa=0也不直接提供EU P的正号。

## 3. 已停止的标量覆盖候选：直接比率入口

由于actual θ<r2，若能证

 M2=a(1−r2)+(w/c)(λ+1−λr2−1/z)>0，          (R)

则Δ2/b>M2>0，Gram张量可在该actualhard合同中绕过。(R)比原入口更强，目前未证；不能把它作为新的未证下界宣称进展。新增尝试保留一个旧全盒证明未利用的合法限制a<1，这由上一节独立prefix校准得到。

不将a或w作为自由参数。设

 Dw=2−(λ+1)u+2λuz+[2Au/d0−(λ+1)uA²E]z²，
 w=cuR/Dw，a=[1−RA0/Dw]/z。

Dw是speed assigned分母，与上一节Df不同。定义两个自然三次式

 C(z)=(1−r2−u)+[2λu(1−r2)+u]z
       +[2Au(1−r2)/d0−A²E(1−r2+u)]z²+uA²Ez³，

 Ba(z)=1+[(2λ+1)u−2]z+[2Au/d0−2λu−A²E]z²
       +[uA²E−2Au/d0]z³。

新源已通用核验

 C=Df(1−r2)−uR(1−z)，
 a−1=Ba/(zDw)，M2=C/(zDw)。                (3)

因此此前明确关键候选是：在原λ,u,z范围、精确E及独立prefix提供的assigned标量限制a<1下，

                    Ba(z)<0 ⇒ C(z)>0。       (H)

这里只是一个受合法校准约束的三次式蕴含，不是任意a<1或任意K。若(H)成立，会证明actualhard所需入口；不能据此自动声称旧无条件F/J(Eenv)全盒合同已人工化。若(H)失败，严格scalar挑战也只能否定这个更强的覆盖引理，不能当实际GW或F反例。

新增严格标量挑战：λ=231/200、u=15/32、z=1119/2000，精确K及全部独立prefix标量限制满足，却Ba<−1/2000、C<−1/1000。故停止该标量覆盖路线；actual H未证明且未给实际GW挑战。没有用有限点确认代替全域。四个(3)身份及四个校准/入口/传播身份的native source exit0只确认代数。未交付草稿曾将Qa一次项的1写成a，已纠正并补核EQa=0、P端值及Δ2/J2身份；(3)不受影响。

## 4. 历史方法对照及最小后备不等式

| 方法 | 准确状态 |
|---|---|
| calibrated向上零点/一交叉 | 已证传播每个s≥2的Δ_s，但前提仍为Δ2>0；不是入口付款 |
| 旧source I的one-crossing修复 | 控制其特定源/高bias合同，不等同assignedΔ2，更不能误借其符号 |
| frozen matched-pipe速度逐项替代 | 已失败。原历史λ=2/√3,u=15/32,z=u+3(r1−u)/4等检查说明必须保留同一actual b的prefix；不重试 |
| 粗Euler k0/旧J0 | 部分强化失败；当前K、κ与同一prefix正确保留。不能放松到自由K然后当作actual预算 |
| genuine-branch频率/localizer与四阶Gram | 都来自actual bounded moments/iid分枝；现行全盒F证明仅用四阶Gram，不需要optional q'>1或branch envelope |
| 新(H)候选 | 精确三次式身份已核；一有理点否定标量覆盖，路线停止；actual H仍open |

若无新的actual/assigned控制，原9744入口可提炼成最小单variance预算

 (θcrit−u)² ≥ (z−u)[r3θcrit/z−u]。            (4)

(4)恰是G(θcrit)≥0，不是新增进展。λ,u,z三个变量中E始终为精确Kcap函数，无第四自由参数。下一步只回到(4)寻求真正新的数量控制，不给H另加未证条件挽救；不直接重写大张量或扫参数。

现阶段准确成果是已独立审核的入口/传播分离、范围修正、共享E消元和H标量覆盖的严格挑战；未得Condition-F人工替换，也未撤P06/P07。5076新增V1保持。唯一辅助仍由父任务复用。
