# P26精确检查拆分与替代调用位置

2026-10-06。只读核对旧脚本/manifest，未运行旧证书。新全龄引理已交同一辅助优先审计，当前回执未到；5076装配V1和全部冻结文件不改，装配V2待PASS。

## 冻结身份与调用

P26=root_canonical_profile_payment.py，当前实文件2538 bytes，SHA256 e691e1c2e400cf15baf820fa67ed6ecc44c3916f6747f689a936dd69327b93bf。与final_certificate_manifest_20261004_v2.json及delivery_bundle_manifest_20261004_v3_complete.json该path记录完全一致。assembly_review_packet_02_python_manifest_replay_20261004.md第41行映射P26→L15 child2。

P13=general_two_over_sqrt3_certificates.py：scripts tuple第13行列P26，第二项；第21--23行逐一subprocess.run(...,check=True)。P13自身是L15。旧runner/P13/P26不改，历史重放仍会完整执行P26；新装配仅作逻辑依赖覆盖，不能声称旧调用已删除。

manifest source_scope_notes只接受root_canonical_profile_payment.md中已审 assigned-range/common comparison及all-index absorption；旧S3/global-root和obsolete general_2_over_sqrt3链接排除。

## 每个脚本检查所付对象

|旧P26行|检查|本轮处理|
|---|---|---|
|11--15|s=2..7构造原N,D,P_s|新引理原样对接同P_s，全部s>=2；无需六龄枚举|
|16--18|u=t/lambda^2清分母、除lambda^2*c^2、六个degree=(2s+2,3)断言|只是旧Bernstein表示构造；随288模块成为历史旁证，不成为新正性依赖|
|19--24|lambda=23/20+L展开，t三次Bernstein转换，288完整位置|新人工正几何和取代整个表示；无新系数表|
|25|288位置全非负|直接P_s>0替代；261个严格正计数不再需要|
|26|每龄四个constant-L位置严格正，共24个|直接P_s>0涵盖；无边界缺口|
|27--29|total/positive累计及(288,261)计数|历史证书成本记录，非新证明输入|
|30|15*(23/20)/(8*(23/20+1))=345/344|旧s>=8人工尾的端点数值；新全龄引理无需它|
|32--38|原完整吸收的exact polynomial identity|保留既有人工身份；新generic源另核同身份，代码仅复核|
|39|gamma+eps/lambda=a_s*(1/lambda-rprev)+Theta|保留Lambda身份；新generic源亦独立复核|
|41--42|a(h)=lambda*h/c*(u/b-1)校准身份|保留，连同v<h、canonical b/u<r1推出a>lambda^2*u；新profile引理不证明这些实际输入|
|43--51|k0及2-(1+lambda*u)*k0清分母，四Bernstein factors身份|保留cap/range接口，不属于288吸收sign模块|
|52--57|三个cubic在23/20负，以及各导数在[23/20,3/2]负的端点上界：3+3比较|保留；它们证明后三cap因素正|
|58|quadratic的端点组合正|保留；证明第一cap因素正|
|59|报告输出|无新增数学断言；输出不能混同各模块均已被替代|

四个保留cap因素原样为

-lambda^3*(lambda^2-11lambda+6)，
-lambda^2*(3lambda^3-32lambda^2+28lambda-1)/3，
-lambda*(lambda-1)*(3lambda^3-28lambda^2+10lambda+5)/3，
-(lambda-1)^2*(lambda^3-8lambda^2-lambda+2)。

它们在23/20<=lambda<=3/2正，支付(1+lambda*u)*k0<2，随后K<k0、K>1等已审解析接口给v<V2(K)<h及lambda^2*u<a_bar<alpha<1。新引理扩大纯profile域，不扩大合法assigned域，也不撤cap四因素。

## 不误用root及与完整floor接合

全部strict吸收明确从s>=2开始；原marker下界、delta/xi正性、finite-mean/geometric可积性仍是既有人工输入。完整floor为Root+sum_(s>=2)w_s*a_s^2*B_s+2sum_(s>=2)w_s*a_s*L_s*Delta_s，其中Root=[(1+v)*eps1^2-2(1-a)*u*eps1]/lambda。

t0=0给Delta1=-(1-a)*u<0，因此不能对s=1套用非负Delta删除，亦不声称吸收付掉Root。s>=3的项只有在已审Delta_s>=0、B_s>0后才可删除。P06/P07的Condition-F和assigned Delta2/J2合同不变，两个9744保留。

新引理不是S33的重复：S33是另一low-lambda q3..10价格核h导数，替代928附录；P26是high-lambda根装配的全龄adjacent/log吸收符号。P02 assigned extension、four cap因素、Condition-F、small-u9600、其它高lambda分支均保留；5076 SIZE已审人工替换状态不变。

## 后续装配V2的精确改动范围（尚未执行）

仅在审核PASS后新增HIGH_U_5076_INTEGRATED_ASSEMBLY_20261006_V2.md，V1不覆盖。其上游合同表原V1第34行由“s>=8解析尾+s2..7/288”改为“一条全龄纯数学引理s>=2”；第32行cap四因素及第33行F的19488仍保留。原V1第109行成本说明删288依赖但不删cap四因素或19488。P13/旧runner保持冻结历史重放，不制作新大证书或无故重跑。

纯数学页P26_ALL_AGE_ABSORPTION_PURE_LEMMA_20261006_V1.md包含全部符号、几何和证明和canonical推论，不引用代码或288证书。generic源仅是可选恒等式旁证；无需算法正性证书。当前仍等待同一辅助PASS，再更新装配。
