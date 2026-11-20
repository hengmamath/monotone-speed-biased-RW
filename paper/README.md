# Monotonicity of the Speed of Biased Random Walks on Galton–Watson Trees

GPT-6 Astra and Heng Ma · November 20, 2026

## Manuscripts

- [Hexagon version](hexagon.pdf) ([LaTeX source](hexagon.tex)): analytic proofs and a sketch of the computer-assisted proof.
- [Full version](github.pdf) ([LaTeX source](github.tex)): the complete mathematical arguments and reductions to finite arithmetic checks.
- [Computation supplement](supplement/README.md): exact coefficient data, verification programs and source records.

The manuscripts state their AI usage and human-verification status. Heng Ma takes responsibility for the paper.

## Compile the manuscripts

Use a TeX Live or MacTeX installation with `latexmk` and BibTeX. From this `paper/` directory, run:

```sh
latexmk -norc -pdf -interaction=nonstopmode -halt-on-error -outdir=build hexagon.tex github.tex
```

The resulting PDFs are written to `build/`. This command only compiles the manuscripts; it does not run coefficient verification.

Each main TeX file contains its own preamble. Both editions share the first five sections in `sections/`, including the linear-response results loaded by the preliminaries. Section 3 gives two proofs: direct comparison and linear response. The sixth section is a sketch in the Hexagon version and a full proof in the GitHub version. The common bibliography is `references.bib`; `references_hexagon.bib` supplies the short version's companion-manuscript citation.

## Computer-assisted proof

The full manuscript proves the analytic reductions, parameter-domain coverage and infinite-tail bounds. The [supplement guide](supplement/README.md) maps each finite arithmetic lemma to its data and verification program and gives reproduction instructions. Verification requires Python 3 and SymPy. These computations are separate from LaTeX compilation and can be expensive.

For laws allowing single-child vertices, the computer-assisted argument establishes a strictly negative speed derivative on `(1,m)`. Together with the analytic result on `(0,1)` and continuity at bias one, this yields strict decrease throughout `(0,m)`.

## Earlier version

A draft treating at least two children per vertex is preserved in [commit 9374a17, dated September 25, 2026](https://github.com/hengmamath/monotone-speed-biased-RW/commit/9374a17682392e39152f1f39f8e7193ef8365c97).
