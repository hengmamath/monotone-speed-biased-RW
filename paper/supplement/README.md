# Exact computations accompanying Section 6

This supplement accompanies *Monotonicity of the Speed of Biased Random Walks on Galton–Watson Trees*, dated 20 November 2026.

The article contains the complete mathematical proof: weak linear response under a finite first offspring moment, the canonical moment and entropy arguments, all infinite-tail estimates, all positive-denominator checks, the regional reductions, and their final assembly. Only the stated finite arithmetic checks are supplied here. For laws with single-child vertices, the computer-assisted argument establishes `v in C^1((1,m))` with `v' < 0` there. The manuscript also proves strict decrease on `(0,1)` and continuity at bias one; together these results give strict decrease throughout `(0,m)`.

## Reproduce the current arithmetic

Use Python 3 with SymPy, with assertions enabled (do not use `-O`). The release was checked with Python 3.14.7 and SymPy 1.14.0. From the directory containing this README, run `sh verify_all.sh`, or run the regions separately:

```sh
python3 current/low/verify.py
python3 current/low/check_data.py
python3 current/near/verify_near.py
python3 current/middle_high/verify_middle_high.py
```

These commands reconstruct the actual rational expressions and check exact identities and coefficient signs. They do not infer signs from floating-point samples and do not read historical PASS receipts as evidence. The low and near verifiers use temporary working directories. The middle/high verifier regenerates `exact_checks.json` and `coefficient_data.json` beside its program.

The regional guides specify the individual targets and their source correspondence:

- [Low region](current/low/README.md), including the complete rational budgets, exceptional Sturm checks, and the 48 finite head polynomials.
- [Near region](current/near/source_map.md), including the full four-age expressions, their 14-row finite sign lemma, and the high-moment endpoints.
- [Middle and upper regions](current/middle_high/source_map.md), including both kernel inequalities, the two integrations, and the 63 root coefficient inequalities.

## Finite lemmas and data

Stable LaTeX labels identify the statements independently of page or theorem renumbering.

| Article statements | Verification and exact data |
|---|---|
| `lem:low-Q0-arithmetic` | Six rational prefix/tail inequalities, with their exact values, in `current/low/`. |
| `lem:low-Q12-arithmetic` | Complete rational budget and age-polynomial reconstructions, Bernstein arrays, and 15 and 25 exceptional Sturm groups in `current/low/`. |
| `lem:low-Q3-arithmetic` | Whole-source, continuous age-price, and square-cost polynomial data in `current/low/`. |
| `lem:low-Q3c-arithmetic` | Three source/gap arrays and all 48 head arrays, comprising 636,112 positive nonzero coefficients, in `current/low/`. |
| `lem:near-cap-arithmetic` | Cap derivative array and exact algebraic endpoint comparisons in `current/near/certificates/`. |
| `lem:near-intermediate-arithmetic`, `lem:near-finite-certificate` | The six intermediate comparisons and eight signed-core/coupled-budget checks in `current/near/certificates/`. |
| `lem:near-high-arithmetic` | Two derivative endpoint polynomials and the upper-endpoint polynomial, with the three explicit rectangles for the exceptional polynomial, in `current/near/certificates/`. |
| `lem:mh-high-arithmetic`, `lem:mh-curvature-arithmetic` | The exact scalar functions and high-kernel/curvature arrays in `current/middle_high/coefficient_data.json`. |
| `lem:mh-lower-arithmetic`, `lem:mh-chord-arithmetic`, `lem:mh-integral-arithmetic` | All lower endpoint, chord, normalized derivative and boundary arrays in the same data file. |
| `lem:mh-coarse-arithmetic` | All 63 polynomial rows, their rational coefficient payments and block lower bounds in the same data file. |

The low-region `data/` directory contains losslessly compressed JSON Lines tables and an index. Entries preserve exact rational numbers, multi-indices, coordinate domains and polynomial degrees; the exceptional Sturm records include their input polynomials and complete sequences. The near-region JSON contains full numerator and denominator coefficients, the exact positive scales, domain rectangles and endpoint values. The middle/high JSON contains the complete shifted power coefficients, Bernstein controls, normalization identities and coarse coefficient payments. `current/low/check_data.py` independently decompresses every listed table and checks the complete inventory, rational entries and file identities. No summary hash stands in for a coefficient table.

Some additional finite identities and simple positivity checks are included to help reproduce the analytic algebra. They are distinguished from the arithmetic lemmas in the regional guides. The programs verify arithmetic only; the mathematical reasons that each finite statement is sufficient are in the article.

## Historical source records

`archive_material/` preserves the research sources in their original notation and language. The old 45-node index in `current_route_results.csv` and `current_route_results_and_dependencies.json` records that historical proof route. The present article selects some simpler finite routes and supplies fresh arithmetic checks, so that index is not the executable proof of the present manuscript.

From the `paper/` directory, the separate command

```sh
python3 supplement/inspect_current_registry.py
```

checks the original 167 archived identities and the old dependency order. It does not verify polynomial signs. Additional unchanged sources are listed with their hashes in `additional_sources.json`; the current low-region program provenance is recorded in `current/low/sources.json`.

AI-assisted mathematical review records are not substitutes for the displayed proofs or the exact arithmetic. This package has not undergone independent human refereeing or formal proof verification.
