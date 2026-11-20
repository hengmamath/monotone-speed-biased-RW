# Low-region verification snapshot

The full portable entry point completed successfully with assertions enabled.
It reconstructed all finite inputs and checked all ten arithmetic programs;
no historical status file or cached coefficient table was used as a premise.

- Command: `python3 verify.py`; exit status 0; wall time 572.937 seconds.
- Environment: Python 3.14.7, SymPy 1.14.0.
- Export: 239 gzip tables containing 886,006 stored exact rational entries.
- Compressed table size: 78,719,143 bytes (about 75.07 MiB).
- Independent unpacking: `python3 check_data.py`; exit status 0.
  It decoded every table and checked exact rational canonical forms,
  dimensions, duplicate indices, hashes, sizes and inventory equality.
  The aggregate index includes exactly every exported gzip table and
  agrees with all individual program indices.
- All current arithmetic-program hashes and all eight byte-preserved
  source-program hashes were rechecked after completion.

The tables include the full input and Bernstein arrays for Q1 and Q2,
all 15 + 25 exceptional Sturm polynomials and complete sequences, the
Q3 source and price polynomials, and all 48 Q3c head arrays. The latter
contain 636,112 strictly positive nonzero Bernstein coefficients and
exactly one zero per array, at index (0, 0).

See `data/README.md` for the table-to-lemma map, `data/index_all.json`
for the complete exact inventory, `sources.json` for provenance, and
`verification_logs/result_all.json` for individual program results.
`verification_logs/release_validation.json` records this final snapshot.

The manuscript proves the response and marker reductions, denominator
signs, infinite-tail estimates, strictness and regional coverage. This
snapshot certifies the stated finite arithmetic checks; it does not
replace the analytic proofs or constitute a formal proof-assistant check.
