# Mellin首因子勘误与依赖影响

2026-10-05。必要链的勘误传播核查已由父任务安排的同一辅助闭合：未发现错误传播到既往独立PASS的证书多项式输入；基于那些既有大证书，纠正后的计算辅助证明恢复完成。同一辅助对所示diff及当时附随文本的文字审核已PASS；未取得完整旧基底，不声称独立重建或逐字审查了整份更正英文。没有本轮全重跑大证书；辅助没有独立取得冻结ZIP字节；不是外部peer review或文献优先权结论。

## 保留与更正版

原稿[speed_monotonicity_english_proof_20261004.md](speed_monotonicity_english_proof_20261004.md)、旧v1、冻结V3 ZIP、旧manifest/依赖图及原证书全部保留，不静默覆盖。冻结英文展示仍含已知错误；旧ZIP不能作为无勘误文本直接阅读。

另存[speed_monotonicity_english_proof_20261005_corrected.md](speed_monotonicity_english_proof_20261005_corrected.md)，36477 bytes，SHA256 `754a53d1a68e2f8153ceb5f6380c3ead68e27fe6002a85a56580e84ffeb614b0`。更正版仍使用原附录和精确程序，不重打旧冻结包。

原英文34924 bytes，SHA256 `50de39e9440d427e7f4764b192221f4113c22e4c53948d2d986d61d88c529882`。旧v1 SHA256 `8d7f2355e2a7558562cf86c766d5cea9475ffe189c511ac70bda163c0561242f`；旧ZIP SHA256 `8860422a20991c21041ca2274c65e8fc267aaeee831db88e8288d483008d9ef9`。以上是本地保存/检查的指纹，不声称辅助独立取得了ZIP。

## 正式勘误

原英文L384及旧v1 L382首因子误写为\(a_n-\lambda a_{n+1}\)；应为\(a_{n+1}-\lambda a_{n+2}\)。取\(s=n+1\)时，\(\varepsilon_s=a_s-\lambda a_{s+1}\)。原核的U变换含\(U(1-\lambda U)\)，因此不能省略这一次矩移位。\(J_n\)、\(\gamma_n\)、\(t_n\)及权\((n+1)\lambda^n\)不改。

旧稿在错误展示式后直接定义Ffloor，故只改首因子不够：必须明确恢复同一正确量。更正版定义

\[
\bar\gamma_{s-1}=a_s(r_s-r_s^-)-\delta_s+
\frac{k(1-1/(2s))\delta_s}{r_s},\qquad
F_{\rm floor}(R_*)=\sum_{s\ge1}s\lambda^{s-1}
\left[\frac{\varepsilon_sJ_{s-1}}{\lambda c}
+2\bar\gamma_{s-1}t_{s-1}\right],\quad R_*=v/c.
\]

(15)左侧为\(F_*-F_{\rm floor}(R_*)\)；其完整信用右侧不改，s1项因t0=0为零。(17)左侧也为\(F_{\rm floor}(R_*)\)；其完整头、平方、Young根和速度信用右侧不改。无参数的Ffloor约定为实际R*处的值。

为了避免把实际响应身份用到非实际速度，更正版在原固定law扩展处明确：对\(R\in[R_*,R_p]\)，令w=cR、\(\alpha(w)=(u-RA_0)/a_2\)，在同一正确级数中使用对应的校准J_n/t_n；实际law、eps及barγ固定。这就是215/218/219消费的同一floor和原斜率身份的量。

## 必要链影响与核验范围

| 链/区域 | 此次确认的对应 | 状态 |
|---|---|---|
| 原7/87→Mellin→cap | 正确移位、原核、完整根/尾与同一cap | 必要链接口独立PASS |
| 215–223 | 完整速度信用、有限Abel终端、Young两个端点、根校准与全预算 | 独立PASS |
| Q0 | 正确cap重推161/159/158 | 独立PASS |
| Q1/Q2 | 原J0/J1等于正确Base减整价格；同一θ、分母和变换 | 独立PASS |
| Q3 | 原源/B、全头/平方价格、223归一化及接合 | 独立PASS |
| H小/大u | 正确eps1根、AN/VD、原S4/H2和原表达式清分母 | 独立PASS；大u五身份完整执行通过 |
| H3 | 原根响应/两核及707/500接合，无错误Mellin行依赖 | 独立PASS |
| 更正英文所示diff及当时附随全文 | 未独立取得完整基底或重建整份更正稿；本次状态回写仅本地检查 | 所示范围文字审核PASS；保存检查LOCAL PASS |

以上传播核查与既往区域大证书的独立PASS共同恢复计算辅助证明。此次没有重建所有长系数表，不能描述为“大证书全部再次独立重跑”。完整概率输入仍是原稿明确引用的外部定理；canonical终端一、有限均值响应与全尾论证仍不可由运行符号程序替代。

## 其余明确撤回/澄清

旧S42临时诊断复制了错误首因子，其9.0325及>9结论继续撤回。它在冻结V3之后创建，不属于原必要manifest。纠正后的canonical指定族整核切向已有另行独立PASS；其结论不升级为一般floor比较。

新F包Q1的“减首项ea1”转录明确改为\(eA_1=eu^4\)，局部\(A_i=w_i\beta_i^2\)，不是原矩a1=u。原尾式与正式证书使用的都是i≥2整尾，未发现正式证书有同样错误。该条详见[F转录勘误](s42_mellin_impact_20261005/F_Q1_first_term_erratum_20261005.md)。

## 精确diff与当前状态

[审核点初始diff（保留）](s42_mellin_impact_20261005/english_mellin_correction_20261005.diff)，4079 bytes，SHA256 `3efda22ffc6d22e6e27a21780b04b93db3eafb9c365896d69d9a2edcb8c765c7`。
[审核点本地exact检查（保留）](s42_mellin_impact_20261005/english_mellin_correction_exact_check_20261005.json)原生exit0：错误因子消失、正确因子唯一，J_n及(15)/(17)完整右侧不改，T/16/18/19整块和所有编号保留，diff往返恢复精确，原稿/v1/ZIP指纹不改。它不是新的数学安全审计。

[必要链闭合回执](s42_mellin_impact_20261005/audit_receipt_mellin_necessary_chain_closed_20261005.md)记录父任务转达的最终范围。[当前研究状态](CURRENT_RESEARCH_STATUS_20261005.md)供下一任务接续；新探索与新精简工作尚未恢复，跨λ=1单独未处理。

[文字审核回执](s42_mellin_impact_20261005/audit_receipt_corrected_english_text_20261005.md)保留审核点及严格范围。本次只回写审核状态、范围和指纹，数学正文逐字不变。
[最终原稿→更正版diff](s42_mellin_impact_20261005/english_mellin_correction_20261005_final.diff)，4221 bytes，SHA256 `7aec63e750eb7e9fefb9fe47edaa84ce30e559587a2ef2b6309fbd39390e8d12`；[本次状态回写diff](s42_mellin_impact_20261005/reviewed_text_status_update_20261005.diff)和[最终本地exact检查](s42_mellin_impact_20261005/english_mellin_correction_final_exact_check_20261005.json)记录保存核验。这些保存操作不是扩大独立文字审核的范围。
