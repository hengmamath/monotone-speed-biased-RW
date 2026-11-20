# Near-region source map and bounded check report

The article section is `sections/06n_near_region.tex` in the companion LaTeX source archive. It proves the near region `2/sqrt(3) <= lambda <= 707/500`, with `lambda<m`, for the same actual canonical escape law as the common foundations. The statement uses the ordinary Galton–Watson root, no leaves, positive unary probability, and finite offspring mean. It does not cover a new offspring-law class or evaluate a speed at the algebraic boundary `u=0`.

The parent manuscript supplies `lem:full-response`, `lem:canonical-moments`, `lem:harmonic-speed`, `lem:entropy-response`, and `lem:calibration`. The common marker section supplies `lem:canonical-marker`, `lem:assigned-floor`, and `lem:mellin-floor`. This near-region section uses their conclusions with the fixed actual law. It does not independently repeat their probabilistic construction.

All source files below belong to the selected CHAIN45 main-V2 route and are under `../../archive_material/agents/generation/data/mono.refs/research/general_med_20261002/` relative to this directory.

| Body component | Selected mathematical source and retained scope |
|---|---|
| Second-prefix comparison and cap | `condition_F_joint_prefix_payment.md`; analytic Bose/Euler material in `condition_F_global_gram_payment.md`; `CFPCAPHAND_CONTINUATION_COMPLETE_ORIGINAL_CAP_AND_ASSIGNED_RANGE_MANUAL_PROOF_LOCAL_V2_20261008.md`. Only the analytic reference sum and assigned range are used; no old Gram tensor is used. |
| Actual three-moment inequality and positive assigned gaps | `CANONICAL_ENDPOINT_ZERO_NONLINEAR_MOMENT_COMPARISON_20261006.md`; `CF_ACTUAL_CANONICAL_NONLINEAR_ENTRY_REPLACEMENT_20261006_V3_SCOPE_CLARIFIED.md`; `CONDITION_F_NONLINEAR_FULL_HARD_MANUAL_PAYMENT_20261006.md`; `CF_NONLINEAR_THREE_BUDGETS_SELF_CONTAINED_APPENDIX_20261006.md`. The actual iid recursion, the nonlinear upper bound for the third moment, and the upward-zero propagation are all in the body. |
| All-age absorption | `P26_ALL_AGE_ABSORPTION_PURE_LEMMA_20261006_V1.md`; `P26_ALL_AGE_ABSORPTION_MANUAL_REPLACEMENT_20261006_V1.md`; analytic parts of `root_canonical_profile_payment.md`. The body proves the inequality for every integer age and supplies a geometric dominator; no finite head certificate pays an omitted infinite tail. |
| Assigned root regrouping | `assigned_polynomial_extension.md`; the root/profile analytic interface in `root_canonical_profile_payment.md`. The complete J identity, the negative root contribution, the positive off-speed comparison, and the fixed-law interpretation are retained. |
| Four-age profile and K-affinity | `SMALL_U_FULL_T_COMPLETE_S4_K_AFFINITY_AND_PRICE_SIGN_20261006.md`; `SMALL_U_FULL_T_KB_FIXED_FIBERS_AND_COMPLETE_PRICE_MERGE_20261006.md`. The body uses `max(0,M_s)` before substituting the lower moments and truncating; it then keeps all three negative prices. |
| Low and middle rho | `SMALL_U_FULL_T_POWER_LOWER_LOW_RHO_HALF_MANUAL_PAYMENT_20261006.md`; `SMALL_U_COMPLETE_F4_MIDDLE_RHO_TWO_THIRDS_MANUAL_PAYMENT_20261006.md`; `RHO56SOURCEHAND_CONTINUATION_COMPLETE_ORIGINAL_D_PROFILE_MANUAL_PROOF_LOCAL_V2_20261008.md`. The shared `rho U_3-V_4>0` claim is used on its stated `rho>=1/2` domain, not by extending the middle region's full positivity claim. |
| The rho=3/4 and rho=5/6 reductions | `RHO34SOURCEHAND_CONTINUATION_COMPLETE_ORIGINAL_F_TO_FA_AND_ENDPOINT_MANUAL_PROOF_LOCAL_V2_20261008.md`; `RHO56SOURCEHAND_CONTINUATION_COMPLETE_ORIGINAL_F56_XI_MIXED_ENDPOINT_MANUAL_PROOF_LOCAL_V2_20261008.md`. The independent endpoint root sign precedes the rho monotonicity argument. |
| Signed core and quartic recovery | `FULL_S4_SIGNED_CORE_STRICT_CONCAVITY_AND_RECOVERY_CHORD_20261007.md`; `FULL_S4_QUANTITATIVE_CONCAVITY_AND_HARD_FIBER_CHORD_PAYMENT_20261007.md`; `FULL_S4_THREE_COUPLED_BUDGET_CLOSURE_AND_CURVATURE_OBSTRUCTION_20261007.md`; `THREE_COUPLED_BUDGET_CLOSURE_20261007_V2_ZERO_DERIVATIVE_DISPLAY.md`. The exact recovery identity and the coupled quartic implication are in the body. |
| The three coupled functions and endpoint anchor | `J1HAND_CONTINUATION_COMPLETE_J1_MANUAL_PROOF_LOCAL_V2_20261007.md`; `J2SOURCEHAND_CONTINUATION_COMPLETE_ORIGINAL_SOURCE_J2_MANUAL_PROOF_LOCAL_V2_20261008.md`; `J3HAND_CONTINUATION_COMPLETE_J3_MANUAL_PROOF_LOCAL_20261007.md`; `SELFCONTAINED_COMPLETE_T1_ENDPOINT_AND_9600_INTERFACE_20261006_V3_STATUS_CLARIFIED.md`; `SMALL_U_COMPLETE_S4_QUANTIFIED_T1_NEIGHBORHOOD_20261006.md`. The exact same finite rational functions are used. Fresh Bernstein calculations replace the long finite coefficient payments; no old 9600 table is imported. |
| High-u geometry and endpoints | `high_u_5076_prefix_geometry_20261006_v2.md`; `high_u_5076_rho_derivative_convexity_20261006.md`; `high_u_5076_right_derivative_sign_20261006.md`; `high_u_5076_lower_endpoint_payment_20261006.md`; `high_u_5076_upper_endpoint_payment_20261006.md`. The body retains the exact cap, proves curvature, uses the right derivative to reduce to two endpoints, and pays both endpoints. The free-K upper boundary is not used as a replacement for the budget. |

The selected route's finite functions have been regenerated in a new exact arithmetic implementation. The proof mechanism and all nonfinite steps are retained in the body. The new coefficient certificate is a replacement for the finite scalar sign calculations only. The obsolete extra-u calibration, withdrawn three-age global certificate, old Gram tensors, and old 5076/9600 coefficient files are not dependencies of the current verifier.

## Current finite lemmas and executable correspondence

| Body lemma or calculation | Fresh generated targets |
|---|---|
| `lem:near-cap-arithmetic` | `cap_lambda_derivative`; ten exact endpoint comparisons in `cap_endpoints.json`. The complete polynomial is reconstructed from `P,R_B,k_n`; the resulting derivative's denominator is one. |
| `lem:near-intermediate-arithmetic` | `rho34_u_derivative`, `rho34_endpoint`, `rho56_u_derivative`, `rho56_g_derivative`, `rho56_quarter`, `rho56_mixed`. These are also the first six rows of `lem:near-finite-certificate`. |
| `lem:near-finite-certificate`, signed core | `core_c2`, `core_c34`. The division by `u` in the latter is performed exactly before evaluating the algebraic boundary. |
| `lem:near-finite-certificate`, J1 | `j1_curvature`, `j1_left_derivative`, `j1_right_derivative`; the two exact endpoint margins in `j1_endpoints.json`. J1 is additionally reconstructed from the original root and all three age terms in the independent identity check. |
| `lem:near-finite-certificate`, coupled functions and anchor | `j2`, `j3`, `t1`. The `t1` rectangle starts at `15/13`, below `2/sqrt(3)`; the J3 target includes the displayed strict margin `(1-lambda*u)/20`. |
| Positive recovery coefficients | `age2_constant`, `age2_quadratic`, `age3_constant`, `age3_quadratic`, `age4_constant`, `age4_quadratic`. These supplement the elementary body proof. The quadratic coefficient is divided by `u` exactly. |
| `lem:near-high-arithmetic` | `high_right_minus`, `high_right_plus`, `high_upper`. Only `high_right_plus` requires a subdivision, exactly the three rectangles printed in the lemma. |
| High-u lower endpoint | `high_lower_quartic`, the difference between the exact quartic and the completed-square lower bound. |

Every one of the 25 polynomial sign targets passed. The denominator of each target was separately verified positive by exact Bernstein coefficients on its full rectangle. Twenty-four targets use one rectangle; `high_right_plus` uses three. The independent identity program passed 28 complete algebraic identities. All 12 endpoint comparisons passed in exact arithmetic. The published JSON contains every coefficient and the explicit positive scaling, not a numerical sample or a summary hash in place of the calculation.

## Scope of the review

The near-region analytic transitions were checked against the selected sources, including finite-mean integrability of the iid child-list comparison, legality of the assigned speed, the full negative root term, the integer all-age absorption, the direction of the profile substitution, both shared rho comparisons, the noncircular endpoint use, and the high-u derivative geometry. No remaining analytic gap was identified within this scope, assuming the stated common foundation lemmas.

One endpoint wording was corrected during the final review: `lem:near-cap-arithmetic` requires `u>0` for its strict final comparison `K_B<K_T`; at `u=0` those two rational quantities are equal. The actual use already has `u>0`. The coefficient calculations remain valid on their closed algebraic rectangles.

The body uses `Delta_s^{ass}` for assigned gaps, separately from the marker `Delta_s`. The absorption lemma explicitly uses integer ages; the preceding upward-zero comparison may still be stated for real ages. 
