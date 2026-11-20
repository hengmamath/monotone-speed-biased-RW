# Middle and upper regional proof: sources and verification

Article section: `sections/06e_middle_high.tex` in the companion LaTeX source archive.

All original mathematical source files are under
`supplement/archive_material/agents/generation/data/mono.refs/research/general_med_20261002/`.
They were read without modification. Historical labels such as PASS and statements about previous reviewers were not used as mathematical evidence. No historical author/writer script was run.

## Scope and dependency order

The article proves the full response sign on `[707/500,39/20]` and `[39/20,(3+sqrt(5))/2)`, always intersected with `lambda<m`, for one fixed leafless finite-mean offspring law with positive mass at one. The analytic high-bias theorem finishes the remaining biases. There is no assertion at either `lambda=1` or `lambda=m`.

The common response, canonical moments, harmonic speed inequality, positive kernel, entropy response, and easy calibration region are proved in `sections/02_response.tex` and `sections/06b_moments_entropy.tex` of the companion article. They are mathematical inputs to this regional proof, not finite arithmetic obligations.

The selected route is the middle composition in `CHAIN45HAND_CONTINUATION_COMPLETE_THEOREM_ASSUMPTIONS_AND_FULL_CHAIN_PROOF_LOCAL_V2_20261008.md`, Section 9, with the explicit no-I-condition composition in `CHAIN45HAND_CONTINUATION_I_FREE_MIDDLE_RESPONSE_COMPOSITION_COMPLETE_PROOF_LOCAL_20261008.md`. The finite coefficient work is not used to replace any analytic tail or law comparison.

## Source-to-article mapping

| Article material | Primary local mathematical source and relevant part |
|---|---|
| `eq:mh-C-kernel`, max-source measure bound and the split at `1/(lambda+1)` | `canonical_entropy.md`, Lemma 4; `CHAIN45HAND_CONTINUATION_I_FREE_MIDDLE_RESPONSE_COMPOSITION_COMPLETE_PROOF_LOCAL_20261008.md`, Sections 2–4. The `C` identity is also explicitly checked in the common preliminaries. |
| Complete four-moment speed envelope | `H3HAND_CONTINUATION_COMPLETE_HIGH_ESCAPE_K1_CONCAVITY_AND_TILT_MANUAL_PROOF_LOCAL_V2_20261008.md`, Section 1. All terms `n>=4` are summed geometrically in the body. |
| High-escape F/G reduction, full s concavity, endpoint products and tilt to larger x | Same high-escape source, Sections 2–5. The five scalar targets and the two endpoint polynomial products are stated explicitly in `lem:mh-high-arithmetic`. |
| Rational entropy lower bound and quadratic division | `hybrid_rational_moment_reduction.md`, Sections 1–2. The article proves the two weighted Jensen steps and the full endpoint-minimum argument for `j(U)`. Its outdated conditional scope is replaced only by the later selected middle-composition argument, whose assumptions are stated explicitly. |
| Full moment-interval curvature | `H3HAND_CONTINUATION_COMPLETE_HYBRID_FULL_S_CONCAVITY_MANUAL_PROOF_DISPLAY_V2_20261008.md`, Sections 1–7. The article retains all four curvature cases, including the nontrivial `w` factors in the second kernel. Only nine exact rational signs and one explicit polynomial are finite arithmetic. |
| Lower endpoint normalization, actual A chord, upper products, two integrations | `HYBRIDJOINHAND_CONTINUATION_COMPLETE_TWO_INTEGRAL_AND_REAL_COUPLING_MANUAL_PROOF_LOCAL_20261008.md`, Sections 2–8. The article uses the actual `A(a_1)`, its `1/3` chord cap, `H^-4` normalization, one lambda integration and one unit-interval integration. |
| Base polynomial and whole-half-line positivity | `Q3REPLACEHAND_CONTINUATION_HYBRID_BOUNDARY_P_SMALL_CONSTANT_MANUAL_PROOF_LOCAL_20261008.md`, Sections 1–3, together with the later two-integral source's exact W1 normalization. The article defines `b_j` directly as the degree-five Bernstein coefficients of `W1(707/500,t)`; the coefficients are positive multiples of the source integers, so the three homogeneous comparisons and the continuous proof are unchanged. Exact coefficients are generated in the verifier data. |
| Signed root polynomial, decreasing source and response integral | `full_response_signed_renewal.md`, Propositions 2, 3 and corrected 5; the article gives a shorter, separately checked equivalent derivation described below. It does not need the unused assertion that the source has exactly one crossing. |
| Complete upper-region moment tail, small-speed condition, actual-root affine endpoints, coarse numerator products | `H3HAND_CONTINUATION_COMPLETE_COARSE63_TAIL_SOURCE_AND_HIGH_BIAS_MANUAL_PROOF_DISPLAY_V3_20261008.md`, Sections 2–7. The body includes all infinite tails and root-law inequalities. Only the 63 finite coefficient payments are deferred. |

## Checked equivalent derivation of the signed integral

The new proof uses the already proved identity
`eta((I-L)f)=E[bf]` with the continuous test `f=J P_c` to obtain
`D=eta(2J P_v-J P_c+LJ P_c)`.
The cancellation for `LJ`, conditional exchangeability, and the canonical recursion give the actual root polynomial divided by `lambda(c+x+S)^2`. The exact root polynomial identity is recorded in the article as `eq:mh-root-polynomial` and is independently checked by the standalone verifier.

Taking the elementary Laplace transform of the reciprocal square then gives the corrected factor `1/lambda` and the complete susceptibility `w(t)=eta(exp(-t·))`. All exchanges are justified by a bound proportional to `1+nu`. This derivation neither drops Neumann generations nor assumes a second offspring moment. It avoids the additional Gamma-kernel construction because that construction is not needed for the signed comparison used here.

## Standalone exact verification

The verifier is `verify_middle_high.py`; it uses installed SymPy and reconstructs the displayed rational functions and polynomial products directly. It imports no historical writer, checker, or coefficient table. `exact_checks.json` records the named results; `coefficient_data.json` retains generated controls, shifted coefficient arrays, coarse payments, the base `W_0/W_1` coefficients, and the exact normalization identities.

The checks cover:

- Five scalar signs and eighteen high-escape endpoint Bernstein coefficients.
- Nine curvature rational signs and all six controls of the curvature polynomial.
- The rational price identity, the four curvature identities, and the two signed-kernel normalizations.
- Seventy lower-endpoint controls and the degree-twenty-two chord numerator.
- Eighty-eight normalized upper-endpoint derivative controls, with the exceptional control shifted by `707/500` exactly as stated.
- Nine lambda-boundary derivative controls, the four positive W0 base controls, and the W1 base coefficients and three homogeneous comparisons.
- All sixty-three coarse coefficient polynomials, including zero rows, their rational payments, and the stated block lower bounds.
- Both high-escape endpoint normalizations, the two upper hybrid normalizations, all six coarse rational identities, and the two pointwise signed-response identities.

The verifier completed successfully with exit status **0**. Its exact data contain 206 shifted univariate sign checks, 29 Bernstein-conversion groups, 12 recorded normalization identities, all 63 coarse rows (four zero rows), and all six actual W1 boundary coefficients. The coefficient data file is 400,245 bytes. The upper hybrid normalization checks clear the displayed denominators through coefficient substitutions before expansion.

The named target `A_chord` verifies `lem:mh-chord-arithmetic` in the article.

## Notation and integration notes

- The analytic moments are written as `a_1,a_2,...`, avoiding an extra alias for the common first moment `u`.
- Inside the explicit polynomial lemmas, `u` is the source's independent unit-interval coordinate and is evaluated at `lambda^2 a_1`. This local scope is stated before the products.
- The middle kernel uses `s=a_2/a_1`; the upper interval explicitly resets `s=h/c`, as in its source.
- The low-escape quadratic calculation temporarily uses the source coefficients `C,L,K` and scalar `r=v/(1+v)`. Their local scope is stated. The response identity is restated before the upper argument. These are not additional probabilistic assumptions.
- The article includes the harmonic region through `lem:calibration`, not merely through the inequality `v<h`.

No unresolved source gap was found in the selected mathematical route. The verifier establishes the listed finite identities and inequalities; it does not certify the other regional proofs or the published transience/speed theorems.
