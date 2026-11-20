# Exact coefficient tables

The aggregate inventory is `index_all.json`. Each program also writes its
own `*_index.json`. `python3 ../check_data.py` checks that the aggregate
inventory contains every compressed table in this directory, agrees with
all program inventories, and losslessly decodes every rational entry.

Every `.jsonl.gz` table starts with a JSON header giving its variables,
degrees, basis kind and metadata. Subsequent lines are
`[multi_index, numerator, denominator]`; the two integers are decimal
strings. Omitted indices within the declared coordinate degrees are
exactly zero. Thus sparse storage retains the complete array, including
all zero coefficients. The corresponding power table is the input
polynomial before the recorded coordinate scaling; a Bernstein table
records the exact coefficients after scaling to the unit box.

Table filenames begin with the verifying program and a consecutive table
number. The following rules identify the expressions and their domains.
All expression definitions and all denominator signs appear in the
manuscript; the adjacent executable is also an unambiguous reconstruction
of each input power polynomial.

* `lambert_head_scale_identities`: the 60-term ordinary numerator in
  Lemma `lem:low-Q3-arithmetic`, with nonnegative ordinary variables as
  specified in its table header.
* `low_u_selfcontained_fixed_arithmetic_20261006`: the exact Q0 floor
  prefix and the rational prefix/tail quantities used in
  Lemma `lem:low-Q0-arithmetic`.
* `low_q_full_coupled_certificate`: first the theta bound, the negative
  coefficient of R, the all-age lower bound and four slope/head tests
  in the first range of Lemma `lem:low-Q12-arithmetic`. Their scaled
  coordinates have upper bounds (3, 1/6, 1); any remaining age variable
  is an ordinary nonnegative power. Then, for `Tlo` and `Tup` in order,
  the complete budget input, the mixed Bernstein/power array, and the
  complete Bernstein array on q in [1/29, 3], c in [0, 1/6], z in [0, 1].
  The input power polynomial has the recorded overall sign. Each
  exceptional group is followed by its exact univariate input and its
  full Euclidean Sturm sequence, on [0, 1]. There are 7 exceptions for
  `Tlo` and 8 for `Tup`.
* `mid_q_full_same_e_certificate`: the theta bound, then the eight
  all-age tests in the second range of Lemma `lem:low-Q12-arithmetic`.
  The first normalized coordinate w satisfies x = 1/10 + 7w/30,
  with w in [0, 1], h in [0, 1/2], and the third coordinate v in [0, 1].
  Each test records the input, mixed array and complete Bernstein
  array; all 25 exceptional groups include their exact inputs and full
  Sturm sequences on [0, 1]. The final two complete budgets use
  x in [1/10, 1/3], h in [0, 1/2], z in [0, 1], with the recorded
  overall sign and removed x power.
* `middle_q_coupled_certificate`: the physical-domain price test at
  g = 0 and g = 1, with x in [0, 1/10], h in [0, 1/2], v in [0, 1],
  and t an ordinary nonnegative variable; then the full source
  polynomial and its exact negative-coefficient payment. These are
  the finite obligations in Lemma `lem:low-Q3-arithmetic`.
* `finite_h_quarter_certificate`: tables 001/002, 003/004 and 005/006
  are respectively the input/Bernstein pairs for the lower-gap bound
  g = 1/4, the upper-gap bound g = 1/8, and the source bound 69/500
  in Lemma `lem:low-Q3c-arithmetic`. All use x in [0, 1/10] and
  h in [0, 1/4]. Tables 007 onward are the input/Bernstein pairs for
  the 48 indexed head polynomials, in increasing age i = 1,...,24
  and, within each age, g = 1/8 followed by g = 1/4. The same closed
  box applies. Each Bernstein array has precisely one zero, at
  (0, 0), and every other coefficient is strictly positive.

Negative entries in a complete Bernstein table for an exceptional Q1
or Q2 group are intentional: the polynomial for that group is verified
by its exact Sturm sequence instead. The program checks positive
endpoint values and equality of endpoint sign-variation counts after
removing zero entries. Stored tables are evidence of the actual finite
calculation; the verification programs reconstruct them from the input
expressions and do not use them as a trusted cache.
