# Complete S4: a strictly concave signed core and recovery chord

2026-10-07. New global profile-shape lemma, LOCAL pending the same
independent auditor. No new positive coverage interval is claimed.
The independently verified gap stays 5/6<rho<102399/102400. Original
9600 and the general S42 OPEN status are retained. No new agent/task,
grid, LP, coefficient-sign scan, installation or external publication.

## Exact contract and old inputs

Keep the actual canonical / assigned-hard full-S4 contract,
2/sqrt(3)<=lambda<=707/500, 0<u<=1/2, K=Kb, t=1-u, k=1-lambda*u,
A=1+lambda*t, Z_s=t*sum(lambda^j,j=0,...,s-1)+u,
r_s=Z_s/Z_(s+1), W_s*L_s=s*lambda^(s-2)*k/Z_s^3=:omega_s.
Set L=lambda+1, h=Kb-t, R=t+rho^2*h,
Q=At+lambda*u*rho*t+u*rho^2, E=1-lambda*rho/A,
G=2A-rho-lambda*rho^2/A, H=A-lambda*u*rho^2/A,
Phi_R=(2E/lambda)*(QG-ARH). Let

    F_s=2-r_s-lambda*r_s^2,
    U_s=omega_s*(Q*F_s+u*A*R*lambda*r_s^2),
    V_s=omega_s*u*A*R/r_(s-1), n_s=s*(s-1)/2.

The audited full budget is Phi=Phi_R+2rho*sum(U_s*f_s^2-V_s*f_s,s=2..4),
with f_s=T^(s-1)*(s-(s-1)T). The normalization is unchanged:
Phi=rho*d*S4/u^2. All root and price terms remain in this budget.

Old audited inputs used here include h>0, Ah>1 and the fact that Ah is
increasing in t on 23/20<=lambda<=3/2, 1/2<=t<=1. The new upper cap is

    Ah<=L*(lambda^2+2lambda+13)/(24lambda)
       <=Hbar:=(35-3lambda)/24<4/3.                       (1)

Indeed the difference between Hbar and the middle expression is
(lambda-1)*(13-7lambda-lambda^2)/(24lambda)>0 for lambda<=3/2.
This explicitly retains the common Kb profile, not an independent margin.

We use 23/20<=lambda<=10/7 for new profile estimates; it contains the
actual lambda interval. Bounds that only require lambda<=3/2 are marked
through their constants. All signs below concern the actual joint profiles.

## 1. Each B_s=2U_s-V_s has strictly positive rho coefficients

First collect elementary profile bounds. r_s increases with u, with
derivative lambda^s/Z_(s+1)^2, and increases with s. At u=0, r2 and r3
decrease with lambda. Their minima on lambda<=3/2 are 10/19 and 38/65.
Thus for s>=2, r_s>1/2, 1/r2<=19/10, 1/r3<=65/38.
Also r2<5/7 (the already audited half-core bound), r3<3/4, r4<5/6,
and lambda*r_s<1. For r4, the last upper bound follows from
5lambda^4-lambda^3-lambda^2-lambda-2
 =(lambda-1)*(5lambda^3+4lambda^2+3lambda+2)>0 at u=1/2.

B_s is quadratic in rho. After removing positive omega_s, its coefficients
are

    [rho^0]: At*[2F_s+u*(2lambda*r_s^2-1/r_(s-1))],
    [rho^1]: 2F_s*lambda*u*t,
    [rho^2]: u*[2F_s+Ah*(2lambda*r_s^2-1/r_(s-1))].         (2)

The constant brackets are strictly positive. Since F_s>2-2r_s and
lambda*r_s^2>1/4, lower bounds for s=2,3,4 are respectively
1/7, 1/20, 7/114. Here use A<=5/2 for s2, 1/r2<=19/10 for s3,
and 1/r3<=65/38 for s4. The linear coefficients are positive.

For the quadratic brackets, a nonnegative price coefficient makes the
sign immediate. Otherwise (1) with Ah<4/3 gives for s3,s4 respective
lower bounds 2/15 and 1/19.

For s2 the price coefficient is negative, since
2lambda*r2^2<2r2<10/7<A. Use Ah<=Hbar and set m=Hbar-1>0:

    bracket2 >=f(A):=4-2r2+2lambda*m*r2^2-Hbar*A,
    r2=A/(L*A-lambda).

At fixed lambda, r2_A=-lambda/Z3^2 and
f_A<=2lambda/Z3^2-Hbar<3/4-61/48<0. Hence f(A)>=f(L).
With S=1+lambda+lambda^2, the exact numerator of f(L) is

    24S^2*f(L)=3c^6-8c^5-85c^4-206c^3-169c^2+14c+64,
    c=lambda-1, 0<c<=3/7.

Discard the positive terms. The fixed bounds c^2<1/5, c^3<2/25,
c^4<7/200, c^5<3/200 give a lower bound 85/8>0. Thus every coefficient
in (2) is positive. In particular, B_s(rho)>0 for all rho>=0.
No new unproved inequality is used to infer this sign.

## 2. Signed core and exact higher-order recovery

Let Psi(rho)=Phi_R+2rho*sum(U_s-V_s,s=2..4), so Psi(1)=Phi(1), and

    Lcore(rho)=(Psi(rho)-Psi(1))/(1-rho)
                      -2rho*sum(n_s*(2U_s-V_s),s=2..4).    (3)

The quotient has its polynomial extension at rho=1. Lcore has degree
at most four. Write epsilon=1-T, rho=1-epsilon^2,
d2=1, d3=3-2epsilon, d4=6-8epsilon+3epsilon^2. Then exactly

    Phi(T)=Phi(1)+epsilon^2*[Lcore(rho)+epsilon*Bstar
                                             +epsilon^2*Jstar],
    Bstar=2rho*[2B3+(8-3epsilon)*B4],
    Jstar=2rho*[U2+U3*d3^2+U4*d4^2].                      (4)

Bstar,Jstar>0 for 0<T<1, by Section 1 and U_s>0. Equation (4) follows
from f_s=1-epsilon^2*d_s. It retains all original negative prices.

This is the SAME audited signed-quartic/positive-recovery budget. For its
audited C and D2=U2-V3, the exact interface is

    Lcore=C+2rho*[(rho-1)*D2+V3+(6rho-5)*U3].              (5)

Formal placeholders in the source only check these polynomial identities;
they are not a free-marginal sign argument or a new probabilistic branch.

## 3. Uniform strict concavity of Lcore

Write Phi_R=sum(q_j*rho^j,j=0..5), and
alpha_s=omega_s*F_s, beta_s=omega_s*u*A*lambda*r_s^2,
gamma_s=omega_s*u*A/r_(s-1). Thus U_s=alpha_s*Q+beta_s*R,
V_s=gamma_s*R. Let eta_s=[rho^2]B_s>0, proved in Section 1.
If Lcore=sum(c_j*rho^j,j=0..4), direct rho-only coefficient identities give

    c4=-q5,
    c3=-(q4+q5)-2*sum(n_s*eta_s),
    c2=-(q3+q4+q5)-2u*sum(omega_s*T_s),
    T_s=F_s*(1+2n_s*lambda*t)+Ah*(lambda*r_s^2-1/r_(s-1)). (6)

We now prove c2<0 and c3+2c4<0 without any lambda,u coefficient table.

Each T_s>0. For s2, using Ah<=4/3 and lambda*r2^2<r2 yields

    T2>=(8/3)A-2+(10/3-4A)*r2.

If A<=2, substitute r2<5/7 to get T2>(8-4A)/21>=0.
If A>=2, r2<=2/(lambda+2)<=40/63 instead gives
T2>=8A/63+22/189>0. This is a two-case structural estimate, not a
subdivision of the remaining rho interval.
For s3, F3>1/2, lambda*t>=23/40, lambda*r3^2>1/4 give
T3>89/40-11/5=1/40>0. For s4, F4>1/3 and 1/r3<=65/38 give
T4>79/30-130/57=67/190>0.

The root has exact identities

    q4=2u*(h+lambda^2*t/A^2),
    q5=(2lambda*u/A^2)*(1-Ah)<0,
    q3+q4+q5=(2/lambda)*[-(1+2lambda)u+lambda^2*(t^2+u)/A
                                     +lambda*Ah+lambda*u*h*k/A].

The last sum is positive. Indeed

    lambda^2*(t^2+u)-A/2
      =lambda^2*(t-(2lambda+1)/(4lambda))^2
                          +(12lambda^2-4lambda-9)/16>0,

whose last term is >=227/1600 at lambda>=23/20. Using Ah>1, the root
sum is strictly greater than (2/lambda)*[lambda*(1-2u)-u+1/2]>=0.
Hence c2<0. Also

    q4+3q5=(2u/A^2)*[Ah*(A-3lambda)+lambda^2*t+3lambda]
       >=(2u/A^2)*[(4/3)A+lambda^2*t-lambda]>0,

because A-3lambda<0, Ah<=4/3, A>=3/2 and lambda<=3/2.
Thus c4>0 and c3+2c4=-(q4+3q5)-2sum(n_s*eta_s)<0.
For 0<=rho<=1,

    Lcore''=2c2+6rho*(c3+2rho*c4)<0.                       (7)

This is a genuinely new global size/shape inequality. It does not assert
that Phi has a minimum at T=1 or that Lcore is nonnegative.

## 4. Proved natural low-degree lower bound

Let C0=Lcore(1), the complete epsilon^2 coefficient. Also
Lcore(0)=Psi(0)-Phi(1)=2A^2*t/lambda-Phi(1).
Strict concavity (7) gives the strict chord bound for 0<rho<1:

    Lcore(rho)>(1-rho)*(2A^2*t/lambda-Phi(1))+rho*C0.

Therefore the COMPLETE budget satisfies, for 0<T<1,

    Phi(T)>Phi(1)+epsilon^2*C0+epsilon^3*Bstar
       +epsilon^4*[2A^2*t/lambda-Phi(1)-C0+Jstar].          (8)

At T=1 the formula is equality; rho=0 is only a regular polynomial
boundary, not an evaluation of the singular original assigned calibration.
The old negative-second-order example is compatible: C0 may be negative.
The signed core is now controlled by a PROVED chord, with positive third
and fourth-age recovery terms. No endpoint/coupling inequality is silently
assumed in claiming (8).

The sign of the right side of (8) over the remaining gap is still unpaid.
In particular, positivity of its combined epsilon^4 coefficient is not
claimed here. This package supplies a global strict-concavity lemma and
a proved lower bound, not a new coverage interval or a full manual proof.
The next real payment must jointly compare Phi(1), C0 and the displayed
recovery terms. The original 9600 remains retained.
