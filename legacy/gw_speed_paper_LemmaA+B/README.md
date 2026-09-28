# Speed monotonicity on Galton–Watson trees with at least two offspring

English research draft, 25 September 2026.

## Files

- `speed_monotonicity.tex`: self-contained LaTeX manuscript, with an embedded bibliography.
- `build/speed_monotonicity.pdf`: compiled manuscript.
- `.latexmkrc`: puts the PDF and auxiliary files in `build/`.
- `references.bib`: an optional BibTeX copy of the bibliography; not needed for compilation.
- `verification/check_algebra.py`: exact symbolic checks of the algebra used in the proof.
- `verification/verification_results.json`: output from the executed verification script.

## Compile

From this directory, run:

```sh
latexmk -pdf speed_monotonicity.tex
```

A normal TeX Live installation with `newpx`, `amsmath`, `amsthm`, `mathtools`,
`aliascnt`, `hyperref`, and `cleveref` is sufficient. No bibliography program is
needed: all five references are embedded in the `.tex` file. The author field
is blank and may be filled in before circulation.

## Verify the algebra

Python is optional and is not required to compile or read the proof. With
SymPy installed, run:

```sh
python verification/check_algebra.py
```

The script executes 18 exact checks. It uses no floating-point tests. It checks
the response cancellation, the two endpoint factorizations, their positive
coefficient certificates, and related identities. It writes the JSON report
next to the script.

The script is **not** a formal proof checker for the probabilistic arguments,
conditional independence, limiting arguments, or cited results. Those steps
are stated and proved, or attributed to precise published results, in the
manuscript.

## Mathematical scope

The draft fixes the offspring law and assumes

`P(nu >= 2) = 1` and `E[nu] < infinity`.

The central statement is strict decrease of the speed `v(lambda)` on
`[0, E[nu])`, with a strictly negative upper right Dini derivative for every
`1 < lambda < E[nu]`. A separate corollary invokes the published
Bowditch–Tokushige differentiability theorem under an exponential-moment
assumption to conclude classical `v'(lambda) < 0` everywhere in the transient
interval.

Lemma A is a **local** stochastic-order comparison for nearby escape laws,
uniform over nearby parameters. Lemma B is the root-only response inequality.
Both follow from the scalar tilted-moment inequality Gamma > 0.

The draft does **not** settle the case `P(nu = 1) > 0`. It also does not assert
speed monotonicity under stochastic ordering of the offspring distribution.
Here `nu` means the offspring variable and `v` means the speed.

## External inputs and review status

The probability arguments use Aïdékon's speed formula, the annealed escape
continuity result of Bowditch–Tokushige (Proposition 2.9, via Lemma 4.7), and
the low-parameter monotonicity result of Song–Wang–Xiang. The optional
classical differentiability corollary uses Theorem 1.1 of Bowditch–Tokushige.
The numbering used for Song–Wang–Xiang is explicitly identified as that of
the linked arXiv version.

The separate preprint claiming analyticity, arXiv:2006.03433, is not used; its
arXiv record flags an error in the analytic argument. No analyticity claim
is needed in this manuscript.

This is a working research draft assembled from the present proof development.
The algebra has been checked and the PDF has been compiled and visually
inspected. Independent mathematical review and a full priority assessment
remain necessary before submission or claims of an externally verified result.
