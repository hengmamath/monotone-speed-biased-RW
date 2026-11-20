# Imported speed representation: source boundary

The only imported probabilistic speed representation used by the main
notes is Aïdékon, *Speed of the biased random walk on a Galton–Watson
tree*, Theorem 1.1, arXiv:1111.4313v4. Song–Wang–Xiang,
*Monotonicity of speed for biased random walk on Galton–Watson tree*,
Eq. (2.1), arXiv:1610.08151v1, explicitly states the leafless range
lambda<m. Both use parent-edge weight lambda, iid parent-avoidance
probabilities independent of the offspring count, and finite mean m>1.
Their monotonicity theorem requiring minimum offspring at least two is
not used for the present minimum-one problem.

Aïdékon's printed theorem uses (lambda_c,m). For lambda>1 the present
applications are within its range since extinction is zero and p_1<1.
For the entire low interval, use the explicit leafless interface in
Song–Wang–Xiang rather than silently narrowing lambda to lambda>p_1.
The artificial-parent modification has only finitely many visits in the
transient regime and does not change limiting speed.

Sources: [Aïdékon](https://arxiv.org/abs/1111.4313) and
[Song–Wang–Xiang](https://arxiv.org/abs/1610.08151). The following local
text excerpts record the exact source interface; the original papers'
proofs are not re-audited by this cleanup.

## Song–Wang–Xiang, §2, Eq. (2.1)

```text
    Let T∗ be the tree obtained from T by adding an artificial parent e∗ to the root e. For any
vertex x ∈ T∗ , let
                                     τx = min{n ≥ 0, Xn = x},

where min ∅ = ∞, and (Xn )∞
                          n=0 is a λ-biased random walk on T∗ . And for x 6= e∗ , let


                                   β(x) := β(x, λ) = Px (τx∗ = ∞)

be the quenched probability of never reaching the parent x∗ of x when starting from x. Since T
has no leaf and λ < m, we have β(x) > 0 due to transience. Let (βi )i≥0 be generic i.i.d. random
variables distributed under P as β(e), and independent of ν.

                                                 3

    In [2], Aı̈dékon gave the following expression of ℓλ :
                                                                
                                (ν − λ)β0               (ν + λ)β0
                    ℓλ = E           Pν        /E            Pν      , λ < m.                                                   (2.1)
                             λ − 1 + i=0 βi         λ − 1 + i=0 βi

Notice (2.1) holds trivially for λ = 0. Here we point out that RWλ on T∗ and RWλ on T has a
slight difference, but due to λ < m and transience, these two biased random walks have the same
speed when starting at e. Indeed, we have the following

```

## Aïdékon, Theorem 1.1

```text
(1.3)                             τx := min{n ≥ 1 : Xn = x}

be the hitting time of the vertex x by the biased random walk, with the notation that
min ∅ := ∞, and, for x 6= e∗ ,
                                     β(x) := Px (τx∗ = ∞)
be the quenched probability of never reaching the parent of x when starting from x. Notice
that we have β(x) > 0 if and only if the subtree rooted at x is infinite. Then, let (βi , i ≥ 0)
be, under P, generic i.i.d. random variables distributed as β(e), and independent of ν.

Theorem 1.1. Suppose that m ∈ (1, ∞) and λ ∈ (λc , m). Then,
                                       ,                   
                           (ν − λ)β0               (ν + λ)β0
(1.4)          `λ = E                      E                    .
                        λ − 1 + νi=0 βi       λ − 1 + νi=0 βi
                                P                       P

Notice that
        h `λ is thei speed
                        h of a λ-biased
                                   i    random walk on a “regular” tree with offspring
```
