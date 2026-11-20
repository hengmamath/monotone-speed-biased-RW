# Exact arithmetic for the near region

Run with Python 3 and SymPy:

```sh
python verify_near.py
```

The runner reconstructs all expressions in a new temporary directory, checks 28 exact identities, 25 polynomial signs, and 12 exact endpoint comparisons, and compares the regenerated data with the published JSON. It does not overwrite these files or execute an archive program. No floating-point arithmetic, sampling, optimization, or external service is used.

`near_arithmetic_build.py` constructs the complete four-age root and price functions from their definitions. It uses rational functions over `QQ(lambda,u)`. In particular, the core is formed by exact polynomial division in the moment coordinate, and the assigned calibration contains no extra factor of `u`.

`near_high_cap_build.py` constructs the nonlinear cap comparisons and the high-u derivative and endpoint polynomials. Its high-u second coordinate is `k=1-lambda*u_actual`; that convention is recorded in each JSON. It checks the ten cap endpoint comparisons in `Q(sqrt(3))` by rational square comparisons.

`near_identity_check.py` independently reconstructs the complete J1 expression from the original root and all three ages; the root coefficients and exact core division; the recovery and same-T merge identities; the assigned three-moment insertion; all six high-u coefficients; the complete high-u affine cancellation and endpoint identity; the Condition-F threshold derivative; and the nonroot regrouping.

`near_bernstein_check.py` verifies every polynomial sign using exact integers. It also verifies the clearing denominator's positivity on the full parameter rectangle. All checks use a single rectangle, except `high_right_plus`, which uses the three rectangles stated in the manuscript.

Each `certificates/*.certificate.json` contains:

- The complete numerator, denominator, parameter rectangle, and exact bidegree.
- Every scaled integer Bernstein coefficient of the denominator.
- Every scaled integer Bernstein coefficient of the numerator on each rectangle.
- The positive scale that converts each printed integer coefficient to the actual rational Bernstein coefficient.
- The exact subdivision path, if any: `0l`/`0r` bisect the first coordinate; `1l`/`1r` bisect the second coordinate.

For a degree `(M,N)` integer polynomial, the initial scaling is the positive product of the affine-substitution denominators to powers `M,N`, and the least common multiples of the binomial coefficients of degrees `M,N`. Each midpoint split in an axis of degree `d` contributes an additional factor `2^d`. The full coefficient rule is also printed in the manuscript. Thus the JSON contains the complete finite data, including the scaling needed to reproduce them by rational addition and multiplication.

`cap_endpoints.json` and `j1_endpoints.json` contain the exact remaining endpoint values. `verification.json` records the checks and the draft hash at the time of packaging. The scope and the correspondence to the selected source route are in `source_map.md`.
