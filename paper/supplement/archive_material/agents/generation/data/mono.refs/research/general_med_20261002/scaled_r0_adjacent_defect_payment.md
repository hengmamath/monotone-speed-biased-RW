# Paying a negative neighbouring moment defect with the actual log response

3 October 2026. Local derivation independently PASSED the SAME sole
parent-arranged reviewer: actual marker/Fatou, all signed coefficients,
half-response cutoff, variance budget and positive cap feedback.
This continues the sole actual scaled-r0 task. No agent or parallel task.
All old Mellin and slope-loss results are now independently PASSED.
The global F_star sign remains UNPROVED.

New use of an OLD representation: med_bias.md (21) already records the
actual marked-moment measure. It is not a newly discovered representation.
Below it is reconstructed from the PASSED complete chosen-child inequality
and used to measure how much negative neighbouring debt can be paid.
An arbitrary marker measure is never substituted for the actual law.

## 1. Actual marked measure and a quantitative derivative/defect inequality

Use c=lambda-1,h,d=1-h,U,a_s from scaled_r0_mellin_payment.md and put

 beta_s=h/(lambda^s-d), rho(s)=a_s/beta_s (s>=0),
 r_s=beta_(s+1)/beta_s=(lambda^s-d)/(lambda^(s+1)-d),
 delta_s=a_s*r_s-a_(s+1)=beta_(s+1)[rho(s)-rho(s+1)]>0 (s>=1),
 delta_0=0, r_0=a_1.

Here a_s=E U^s for real s>0; no random tree law is differentiated.
Define the ACTUAL nonnegative chosen-child tail defect, for 0<t<1,

 A(t)=E[(1-lambda*U)1_(lambda*U>t)]
                       -d E[(1-U)1_(U>t)]>=0.

This is the PASSED chosen-child inequality with an increasing indicator
test. Layer cake, including real s>=1, gives

 h[rho(s)-rho(s+1)]=s int_0^1 t^(s-1) A(t)dt.

Since rho(1)=1 and rho(s+n)->0, positive summation proves

 sigma(dt)=A(t)dt/[h(1-t)^2], int sigma=1,
 rho(s)=E_sigma[t^(s-1){s-(s-1)t}], s>=1.         (9)

The last limit uses lambda*U<1 a.s. and bounded convergence. Thus sigma
is constructed from the SAME actual pi, and (9) is not a free relaxation.

Differentiating only this deterministic Mellin transform gives

 -rho'(s)=E_sigma t^(s-1)
       [{s(1-t)+t}(-log t)-(1-t)]
    >(1-1/(2s))[rho(s)-rho(s+1)], s>=1.           (10)

For s>1, derivatives are bounded integrands. At s=1, rho'(1) exists and
is finite from bounded U^s log(1/U) locally for s>0. Fatou applied to
(1-phi_(1+e)(t))/e yields integrability of -log t-(1-t), hence of -log t;
dominated convergence then justifies the displayed derivative at one.
No unweighted log of U or inverse escape moment is assumed.

To prove (10), write z=1-t and use
-log(1-z)>z+z^2/2. Then

 [1+(s-1)z](-log(1-z))-z
     >(s-1/2)z^2+(s-1)z^3/2.

Also rho(s)-rho(s+1)=s E_sigma[t^(s-1)(1-t)^2].
Strictness holds because the actual sigma is supported in (0,1).

Define the complete actual response surplus

 Theta_s=k beta_s[-rho'(s)]>0,
 C_s=k*(1-1/(2s))/r_s, k=c/(lambda log lambda).

Then the exact and quantitative formulas are

 gamma_(s-1)=a_s(r_s-r_(s-1))-delta_s+Theta_s,
 Theta_s>C_s delta_s.                            (11)

These keep the actual TWO defects of the PASSED Mellin identity: (11)
merely reorganizes them, rather than deleting branch information.

## 2. Calibrated weights uniformly pay a moment of the same law

Keep the hard case 0<a<1,t_0=0 and the PASSED quadratic Q_a.
Set

 epsilon=min(lambda-a,t_1/a_3)>0.

Then the quantitative bound is

 t_n>=epsilon*a_(n+2), n>=1, strict for n>=2.      (12)

Proof: P(u)=Q_a(u)-epsilon*u^2 is concave, negative at0, and nonnegative
at1/lambda. Also E[U P(U)]=t_1-epsilon*a_3>=0. Thus P has one upward
sign crossing b in (0,1/lambda); if its endpoint is zero, positivity
inside follows from this expectation and actual nonconstant U. For n>=2,

 E[U^n P(U)]-b^(n-1)E[U P(U)]
     =E[U{U^(n-1)-b^(n-1)}P(U)]>0.

This proves (12). The tempting upgrade epsilon=lambda-a is NOT used;
calibration of t_0 alone does not justify it.

## 3. Exact signed normal form: the negative neighbouring price

Write s=n+1,w_s=s lambda^(s-1), t=t_(s-1), and define

 B=c(1+2a)+(3lambda+1)v,
 C=c(lambda+2a)+lambda(lambda+1)v,

 P_s=(1-lambda*r_s)/(lambda*c)
          [B-C*r_s-2v/r_(s-1)]
       +2(r_s-r_(s-1))
          [1+(lambda+1)v/c-(a+lambda*v/c)r_s-v/(c*r_(s-1))],

 L_s=2[a{(lambda+1)/lambda-r_(s-1)}-lambda*r_s
                       +lambda*v/c{1-c*r_s-r_(s-1)}].

Let f_s=e_(s-1)*J_(s-1)/(lambda*c)+2gamma_(s-1)*t_(s-1),
so the PASSED exact Mellin identity is F_star=sum w_s f_s. Full expansion
gives the EXACT new identity

 f_s=a_s^2 P_s+a_s delta_s L_s+lambda(1+v)delta_s^2
          +2Theta_s t_(s-1)
          -(2v/c)a_s delta_(s-1){1/(lambda*r_(s-1))-1}.  (13)

It is not a statement that its displayed local terms are all positive.
The last term is a genuine negative price from the PREVIOUS canonical
moment defect. Positive log response from the previous index can pay it.

Importantly P_s is independent of a: its a coefficient is zero, since
(1-r_s)/lambda=r_s(1-r_(s-1)). This cancellation is exact. However it
uses the actual assigned OWN v; it cannot be assigned the pipe speed.

Summing (13) and shifting the last negative series one place yields

 F_star=sum_(s>=1)w_s a_s^2 P_s
  +sum_(s>=1)w_s[a_s delta_s L_s+lambda(1+v)delta_s^2
       +2Theta_s t_(s-1)
       -(2v/c)*lambda*(s+1)/s*a_(s+1)delta_s
                                         *{1/(lambda*r_s)-1}]. (14)

All series converge absolutely: a_s<=lambda^(-s), delta_s<=lambda^(-s-1),
and (11) bounds Theta_s using bounded gamma and two geometric moments.
The fixed-parameter r_s,r_(s-1),L_s,P_s are bounded in s. Thus shifted
series and expansions have polynomial-geometric domination.

## 4. A direct payment lemma, not just positivity of the remainder

For any fixed allocation 0<alpha<=1, the SAME s-th positive response
pays the whole negative defect at index s+1 whenever s>=2 and

 epsilon >= [v*d/(alpha*k)]*(s+1)/(s-1/2)
                                  /(lambda^(s+1)-d).        (15)

More precisely, under (15),

 2alpha*w_s Theta_s t_(s-1)
  >w_(s+1)*(2v/c)*a_(s+1)delta_s
                                    *{1/(lambda*r_s)-1}.    (16)

Proof uses ONLY (10)--(12) and the exact identity
1/(lambda*r_s)-1=c*d/[lambda*(lambda^s-d)]. After cancellation,
the sufficient inequality is exactly (15). This is a SIZE comparison
between an explicit negative price and the actual retained log response.

Consequently the condition is AUTOMATIC for all sufficiently large s.
For alpha=1/2 one may take

 N=max(2,ceil(log_lambda[d+4v*d/(k*epsilon)])-1).              (17)

For every s>=N, half the positive Theta payment suffices; the other half
remains for L_s and the signed cap baseline. If the logarithm argument
is below lambda^3, N=2. The integer cutoff depends on the actual law;
no uniform finite negative prefix or J_1>0 is asserted.

## 5. The first price and the actual unary variance budget

The first defect has no upstream payment because t_0=0. Its exact
shifted negative price is

 Debt_1=4v*d*a_2*delta_1/(lambda-d),
 delta_1=beta_2-a_2>0.                            (18)

Let p=mu(1),q=1-p, and R be the SAME actual genuine-branch variable from
the PASSED unary decomposition. Total variance of lambda*U, which equals
U_child on a unary root and R on a genuine branch, gives

 (lambda^2-p)Var U=q Var R+(p*c^2/q)a_1^2.        (19)

This is the general-degree version of OLD med_bias.md (20). The mixture
has ER=(lambda-p)a_1/q, hence the between-class term is p*c^2*a_1^2/q.
Only bounded U and R are involved. Subtracting the matched pipe variance
gives the exact root-defect budget

 delta_1=a_1^2*c^2*(d-p)*(lambda^2-d*p)
       /[h*q*(lambda^2-d)*(lambda^2-p)]
                         -q*Var R/(lambda^2-p).             (20)

Also

 E(1-R)=c(d-p)/[q(lambda-d)].                              (21)

Thus the FIRST price is tied to the actual branch mean AND variance,
not a freely chosen marker. A merely Jensen-log lower bound is quadratic
in E(1-R), whereas the leading upper budget in (20) is linear in d-p.
This does not prove a failure of the complete branch log payment; it
explains why its Jensen floor cannot simply be assumed to pay (18).

One exact sufficient local root condition, not proved universally, is
L_1>=4v*d/(lambda^2-d). It makes a_1*delta_1*L_1 pay (18), since
a_2/a_1<r_1. If it fails, retain its signed residual with the full (14).

There is also exact POSITIVE calibration feedback to retain. Define the
cap calibration at the ACTUAL v (not the pipe speed)

 a_cap(v)=[c(lambda+1)+h-c(lambda+1)d*v/h]/(c+h)>0,
 Acal=a_cap(v)+lambda*v/c>0,
 f_1=(lambda+1)/lambda-a_1>0.

The hard-case equality t_0=0 gives

 a=a_cap(v)+Acal*delta_1/a_2.                     (22)

Positivity a_cap follows from v<h; indeed it exceeds
lambda^2*h/(c+h). Put L_1^cap=L_1(a_cap(v),v). The COMPLETE local
root block from (14), including its shifted debt, is EXACTLY

 a_1*delta_1*L_1+lambda(1+v)delta_1^2-Debt_1
 =delta_1[a_1*L_1^cap-4v*d*beta_2/(lambda-d)]
  +delta_1^2[lambda(1+v)+2a_1*Acal*f_1/a_2
                                      +4v*d/(lambda-d)].  (23)

The quadratic coefficient is strictly positive. Thus a negative LINEAR
root price is partly paid by the calibration feedback in the SAME
defect; it must not be separated into unrelated free moment constraints.
The linear coefficient in (23) is proved strictly positive in the active
negative-I gap in scaled_r0_first_defect_paid.md, now independently PASSED.
The complete first DEFECT block is paid; its separate cap-baseline term
and the rest of (14) remain unclosed.

## Precise boundary and next obligation

NEW independently PASSED: actual reconstruction (9), strict derivative/defect
bound (10)--(11), calibrated payment (12), exact normal form (13)--(14),
negative neighbouring SIZE comparison (15)--(17), actual root budget
(18)--(21) and same-defect calibration payment (22)--(23). The accompanying
script verifies the full cap expansion and
all rational normalizations independently of test points.

The remaining head is precise: the independently PASSED root-price payment,
finitely many shifted
prices before N, the potentially negative local L_s prices, and the
cap baseline with actual v. The far shifted prices are genuinely paid.
Neither positivity of the baseline nor the complete signed sum (14) has
been proved. Root payment is proved only on its stated parameter domain.
The all-q pipe theorem cannot
be imported with an uncalibrated substitute v.

No numeric sign is a dependency. No claim J_1>0, arbitrary-sigma law,
finite inverse moment, offspring second moment, offspring reduction,
micro-threshold search or overall theorem below707/500 is made.
