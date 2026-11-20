# Exact missing joint-budget lemma and a checked structural obstruction

2026-10-07. The preceding quantitative-concavity/whole-hard-fiber package
has received same-auxiliary FINAL PASS; receipt saved separately. This
new reduction and diagnostic are LOCAL. No new general positivity or
9600 dependency removal is claimed.

## The precise unproved lemma

Retain the actual coupled Kb profiles and the complete quartic envelope
from FULL_S4_QUANTITATIVE_CONCAVITY_AND_HARD_FIBER_CHORD_PAYMENT_20261007.md.
For 2/sqrt(3)<=lambda<=707/500,0<u<=1/2, write p=Phi(1)>0,
C0=Lcore(1),a=5/6 and the same positive b,j and signed Ka. The proposed
joint lemma is exactly

    25p+C0 >= 0,
    4b+3C0 >= 0,
    Ka+j+4C0 >= 0.                                      (J)

All three inequalities are UNPROVED on the general domain. These are
joint inequalities in the SAME lambda,u,Kb; no coefficient has been
replaced by an independent worst-case constant. The old difficult fiber
is not assumed to be an extremum. A sufficient lemma need not be necessary
for positivity of the complete Phi or for the quartic itself.

## Why (J) would pay the entire remaining gap

This implication is proved. With x=epsilon<=1/sqrt(6), the already
audited envelope and the second and third inequalities of (J) give

    Phi >= p+C0*g(x),
    g(x)=x^2-(3/4)x^3-4x^4.                              (1)

We have 0<=g(x)<1/25. For the lower sign, x<33/80 and
1-(3/4)*(33/80)-4*(33/80)^2=1/100>0.
For the upper sign put f=1-25g. On [0,1/4], f decreases because
f'=x[-50+(225/4)x+400x^2] and the increasing bracket is negative at
1/4. Therefore f>=f(1/4)=31/256. On [1/4,infinity), f'' increases
and f''(1/4)=425/8>50. Since f(3/10)=53/800 and f'(3/10)=69/80,

    f(x)>=53/800+(69/80)(x-3/10)+25(x-3/10)^2
          >=37639/640000>0.                             (2)

If C0>=0, (1) gives Phi>=p. If C0<0, the first inequality of (J)
gives -C0<=25p; then (1)-(2) imply

    Phi>=p*(1-25g)>= (37639/640000)*p>0.                 (3)

Thus no endpoint minimization in T is needed. The audited p>1/1000
would even give Phi>37639/640000000 on the whole remaining region.
Equations (1)-(3) are conditional on (J); they are not claimed as an
unconditional new coverage result.

## A verified obstruction to a common endpoint-concavity shortcut

We tested natural curvature structures at one exact coupled point,
lambda=707/500,u=1/2,K=Kb. Let N=kA>0. Write J1,J2,J3 for the three
left sides of (J), only within this paragraph. Exact rational
differentiation in u, holding lambda fixed, gives

    J1'' in (37,38),
    (J1/N)'' in (-60,-59),
    (J2/N)'' in (18,19),
    (J3/N)'' in (329,330).                              (4)

All three J_i are positive at this point. Nevertheless (4) refutes
concavity of the raw first budget, and refutes a common kA-normalized
concavity argument for all three budgets. The strict signs persist
into the neighboring interior by continuity. These are tests of
actual coupled profiles, not independently assigned margins.

There is also an obstruction to discarding higher ages in a possible
normalized first-budget concavity proof. Decompose J1 into its root
and complete s=2,3,4 contributions. With

    J1_root=25Phi_R(1)-Phi_R'(1),
    J1_s=2[(24-2n_s)U_s(1)-(24-n_s)V_s(1)-U_s'(1)+V_s'(1)],

the same exact point satisfies

    ((J1_root+J1_2)/N)'' in (1,2)>0.                    (5)

So root plus complete second age alone is not concave after this
normalization. The third/fourth contributions are necessary for the
observed negative full first-budget curvature at this point. Equation
(5) does not itself prove their general concavity or global dominance.

The old difficult fiber also obstructs stronger ratio shortcuts. At
lambda=231/200,u=1/2,Kb, exact Fraction evaluation gives

    b+C0 < -2/5,
    Ka+j+5C0 < -1/10,
    Ka+4C0 < -5/4.                                    (6)

Thus b>=-C0 is false, Ka+j>=-5C0 is false, and dropping the positive
fourth-order floor j does not pay even the proposed third budget on
this known fiber. These are genuine negative points of the stated
stronger inequalities on coupled profiles, not negative points of
Phi or of the proposed three-budget lemma. The source checks (6) using
definitions from the small audited Fraction source (main() is not
executed), whose SHA256 dependency is asserted explicitly.

## What remains open

There is no verified negative point of (J) here, and no proved extremum
location. The three global signs (J) themselves are the next exact
target. A promising first-budget normalization and decreasing raw
second/third budgets remain conjectural; local curvature/derivative
observations do not prove them. Further work must provide a genuine
joint size argument, or a rigorous coupled counterexample to (J),
rather than more identity-only variants.

No new agent/task, parameter grid, free-marginal scan, old certificate,
installation or external publication was used. The general verified
gap and original 9600 are unchanged; overall computational dependence
and S42 OPEN are retained.
