# Exact arithmetic for the low-bias proof

Run python3 verify.py with Python 3 and SymPy. Assertions must be enabled.
The optional --group common|q0|q1|q2|q3 selects a subset. The default
reconstructs all finite arithmetic. Logs are written under
verification_logs; --log-dir PATH selects a different location.
Programs execute in a fresh temporary working directory and do not write
to preserved research sources.

The manuscript contains the actual-law response, marker measure, calibrated
floor, strictness, all infinite-age and infinite-Lambert-tail estimates,
source comparison, quadrature, and all parameter coverage. This supplement
checks only the finite arithmetic stated there. No historical PASS record
is read by the verifier, and no floating-point sign test is used.

| Manuscript label | Reconstructed expressions and checks |
|---|---|
| lem:canonical-marker, lem:assigned-floor, lem:mellin-floor | marker_and_local_identities.py: three original pair-kernel transformations, off-speed identity, corrected first factor a_s-lambda*a_(s+1), calibration, and index algebra |
| lem:calibrated-head | master_local_identity.py: independent actual local floor residual and two telescopes; calibrated_cumulative_head_identities.py: full calibration, root cancellation, neighboring square and finite Young endpoints |
| lem:low-Lambert-tails and lem:low-Q3-arithmetic | lambert_head_scale_identities.py: all-index coefficient identities and the exact positive 60-term rational square numerator |
| lem:low-Q0-arithmetic | marker_and_local_identities.py checks its six displayed rational inequalities directly; low_u_selfcontained_fixed_arithmetic_20261006.py checks the finer prefix/tail arithmetic and every stated final margin |
| lem:low-Q12-arithmetic, first range | low_q_full_coupled_certificate.py: complete rational tails, theta bound, all-age affine reduction, two final rational budgets; all Bernstein coefficients and 15 exact Sturm exceptions |
| lem:low-Q12-arithmetic, second range | mid_q_full_same_e_certificate.py: theta, eight affine-age tests, 25 exact Sturm exceptions, and both complete endpoint budgets (10150 and 10850 positive coefficients) |
| lem:low-Q3-arithmetic, source and price | middle_q_coupled_certificate.py: full source polynomial and two continuous physical-domain price polynomials, followed by the Q3a exact margin |
| Q3b assembly | hard_d_coupled_certificate.py: quadrature/integral identities and complete strict rational margin |
| lem:low-Q3c-arithmetic | finite_h_quarter_certificate.py: nine independent common-denominator identities, three source/gap polynomials, and all 48 indexed head polynomials at both g endpoints; 636112 positive nonzero Bernstein coefficients |
| Q3c final continuous budget | marker_and_local_identities.py: exact logarithmic rational bounds, the general derivative, and both positive endpoint margins |

The arithmetic programs reconstruct every coefficient from the rational
expressions and export the complete exact tables to data/ as lossless gzip
JSON Lines. Each file begins with its variables, degrees, domain and basis;
subsequent rows contain [multi-index, numerator, denominator], with integer
strings and implicit zeros. Both input power polynomials and the actual
checked Bernstein arrays are provided, together with exceptional Sturm
inputs and complete sequences. data/index_all.json lists every table,
entry count, compressed size and SHA-256. The same data are regenerated
on each complete verification run. No external cached table is trusted.

sources.json
records hashes and the correspondence with the byte-preserved archive.
Eight programs were imported from the author's finite-arithmetic sources.
The current copies add lossless table exports; the archive originals are
unchanged and their source hashes are retained.
The Q3c head program has one additional assertion checking that each array
has exactly one zero, at index (0,0), so its sign is strict for x>0.
Two identity programs are fresh independent reconstructions.

The selected manuscript uses the direct finite head route for ages 1–24
and the complete rational budget route for the first two ranges. These
choices avoid importing later analytic simplification arguments.
Chronological comments in original programs do not define proof status.
The printed checks and current result files describe only arithmetic
actually executed by this entry point.
