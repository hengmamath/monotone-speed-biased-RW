# Whole high-q coupled payment232--237

2026-10-04. COMPLETE232--237 independentlyPASS SAME sole auxiliary;
receipt saved. No agents/subtasks created. Original user files unchanged.
Depends on independently PASSED214--231, including actual canonical-law
floor222, full Lambert mixture225, scalar derivative227, hard normalization228,
and entire quadratic charge229. No new actual-law differentiation,
offspring moment, inverse escape moment, arbitrary fixed point or two-point
reduction. This closes candidate230 on ONE continuous nonlocal domain;
q<50 and the full general med gap remain OPEN. Cross lambda=1 is separate.

Notation is that of lambert_head_scale_comparison.md: c=lambda-1,
q=u/(1-u)=h/c, d=1-h, R=Rp, alpha=alpha_p, beta_i=h/(lambda^i-d),
w_i=lambda^(i-1)beta_i^2, r_i=beta_next/beta_i,
L_i=c d/[lambda(lambda^i-d)], z=d lambda^-i, k=c/(lambda loglambda).
All alpha/R in this file are the SAME calibrated scalar reference, never
independently assigned. Actual hard0<alpha_actual<1 implies
lambda^2u<alpha<1, R<q, h<1/(lambda+1)<1/2. Assume q>=50 throughout.
The cap price is Hpi=sum_i i[-S_i^p]_+, S_i^p=B_i^p-2V_i.
Recall exact B_i^p/w_i=2i(alpha+cR)/lambda+2iR r_i L_i
+2(i+1)R lambda r_i^2 L_i+k(2i-1)tau_i^p, tau_i^p>=0.

## 232. Global N1-exact polynomial remainders for every Lambert term

For EVERY integer N>=1,c>=0,
 A_N>=1-(N-1)c/2,
 A_N<=1-(N-1)c/2+(N^2-1)c^2/12,
 P_N<=Nc-(N-1)(5N+2)c^2/6+(N^2-1)(4N+1)c^3/12.       (232)
Multiply A inequalities by (1+c)^N-1. Lower difference coefficient c^j,
j>=3, is -binom(N,j-1)(j-2)(N+1)/(2j)<=0; low coefficients vanish.
Upper difference coefficient c^j,j>=4, is
 binom(N,j-2)(j-3)(N+1)[(j-4)N+5j-8]/[12j(j-1)]>=0.
This includes j=N+1,N+2; other coefficients vanish. N1 is exact.
P follows from A upper and GLOBAL Taylor-integral lower
(1+c)^(1-N)>=1-(N-1)c+N(N-1)c^2/2-N(N-1)(N+1)c^3/6;
the fourth derivative is nonnegative, for every c>=0.

Put b=lambda L_i=c z/(1-z). Under Pi(N)=N(1-z)^2z^(N-1),
 E A_N<=A=1-b+(cb+b^2)/2,
 E P_N<=P=c+2b-4cb-5b^2+(9/2)c^2b+(25/2)cb^2+8b^3,
 E B_N<=z/2, E C_N<=C=(5/3)b+c z/3.                 (232b)
The last is225's sharper C upper; EN,EN^2,EN^3 and E(1/N)=1-z
give these identities. Thus V_i/w_i<=U3=[i(A+RP)+z/2+RC]/lambda,
for EVERY age i. Remainders are global; no omitted-N or age tail.

## 233. The scalar quotient is within one of its harmonic cap

With delta=loglambda, the full Lambert lower gives
Tp>=h/(lambda delta)-1/(2lambda)>2q/(lambda+1)-1/(2lambda).
The second inequality is k>2/(lambda+1). Subtract the Tp value
2q(q-1)/[(lambda+1)q-lambda] corresponding to R=q-1. The difference is
[lambda(lambda+1)-q c^2]/[2lambda(lambda+1)((lambda+1)q-lambda)]>0:
q c^2=h^2/q<=1/200, while lambda(lambda+1)>2.
Hence g=q-R belongs to(0,1). Exact calibration becomes
 alpha=[lambda^2+g(1-h)(lambda+1)/q^2]/(1+1/q).        (233)

## 234. One global polynomial certificate pays the finite-q price error

Set x=1/q in(0,1/50], t=i/q>=0, w=h z/(1-z), b=xw,
lambda=1+hx, R=1/x-g, alpha as233. Bernoulli lambda^i>=1+ic implies
0<w<=(1-h)/(1+t). Set r=1/(lambda+b), rprev=(1-b)/lambda,
k0=2/(lambda+1), tau=1-(alpha+lambda R)r+(lambda+1)R-R/rprev.
Since actual tau>=0,k>=k0, replace k by k0 to lower B_i^p/w_i.
Let BB=2i(alpha+cR)/lambda+2iR r b/lambda+2(i+1)Rr^2b
+k0(2i-1)tau and U=U3 from232b. Define
 shape=2ht+4(t-1/3)w-(2h+3)z/3.
Then throughout the ENTIRE physical parameter domain,
 BB-2U>=shape-10x(1+ht).                             (234)

The standalone script is a FINITE EXACT identity/positive-coefficient
proof of234, not point sampling. Form err=(BB-2U-shape)/x+10(1+ht).
Its denominator is
 -3(h+w)(x+1)(hx+1)(hx+2)(1-wx)(hx+wx+1)^2 <0.
Negate its numerator. Substitute w=(1-h)v/(1+t),0<=v<=1,
and multiply by (1+t)^7 to clear. Result has degrees(x,h,t,v)=(6,8,8,7),
and is affine in g. At g=0 and1 convert ONLY x,h,v to Bernstein bases
on[0,1/50],[0,1/2],[0,1], respectively; retain ordinary t powers,
so ALL t>=0 are covered. Each endpoint has4319 nonzero coefficients,
ALL positive; minimum27/56. The script constructs the exact polynomial,
checks the exact denominator and all coefficients using Fraction.
For power coefficients a_k on an axis of degree D the transformation is
b_j=sum_(k<=j)a_k binom(j,k)/binom(D,k). Bernstein basis and t powers
are nonnegative. Affine interpolation covers EVERY g in[0,1].
This is one continuous certificate, not a rectangle grid or a tail truncation.

## 235. A uniform all-age shape inequality and the COMPLETE linear charge

For the ACTUAL age w,z above, let env(t)=(9t-7)/[3(1+t)]. Then
 shape>=env(t)+ht/4, EVERY t=i/q.                    (235a)
If t<=1/3, use w<=d/(1+t), z<=d. Difference after subtracting ht/4
is at least h[(7/4)t-4(t-1/3)/(1+t)+1/3]+2h^2/3>=0.
If t>=1/3,y=ht<=2, use lambda^i<=e^y<=(1+y/2)/(1-y/2),
w>=d(1-y/2)/(1+t-y/2), and z<=d/(1+y). The exponential inequality
follows by integrating the positive derivative of2atanh(y/2)-y;
y=2 follows by the zero lower bound. The resulting difference is
-h M/[12(t+1)(y+1)(y-2t-2)]>=0, where
M=t^3(18-6y)+t^2(27y^2+19y+60)+t(11y^2-11y+18)
 +40+44y-24y^2+(16y-8y^2)/t.
Every displayed group is positive or nonnegative on0<=y<=2: the
quadratic middle group has negative discriminant, the concave constant
group has endpoint values40,32, and the last is8y(2-y)/t.
If y>=2, drop the nonnegative w term; (2h+3)d<=3 and z<=d/(1+y)
give shape>=2y-1/(1+y)>=3+y/4>=env(t)+y/4.

Since q>=50,234--235 imply S_i^p/w_i>=env(t)-10/q
+ht(1/4-10/q)>=env(t)-10/q. In particular ALL i>=q have S_i^p>0.
No unestimated age tail remains. Also y=lambda^i>=1+ic and monotonicity
of y/(y-d)^2 give w_i<=(1+ht)/[lambda(1+t)^2]. Accepted228 yields
Ehard q^2<=D u^2/(1+cu), D=1-(lambda+1)h<=1-2h. For t<=1,
D(1+ht)<=1; consequently Ehard q^2 w_i<=1/(1+t)^2.
It follows, including EVERY negative price age, that
 Ehard Hpi<=(1/q)sum_(i>=1) G(i/q),
 G(t)=[t(38-42t)/(15(1+t)^3)]_+.                   (235b)
G has support[0,19/21], is unimodal: derivative numerator38-160t+42t^2.
G<=1/4 because15-107t+213t^2+15t^3>0 (quadratic discriminant -1331).
For a unimodal function vanishing at0/infinity, its right Riemann sum
exceeds its integral by at most mesh*maximum: integrate the positive
part of its derivative, whose integral equals the maximum. Thus
 Ehard Hpi<=I+1/(4q),
 I=integral G=1159/600-(14/5)log(40/21).             (235c)

## 236. Complete scalar source, with a uniform explicit finite-q error

Let f(h)=(1-h)(2h+1)/6>=1/6. Claim
 Fpipe>f(h)-1/q.                                    (236)
Write a=c/log(1+c), x=1/q, ell=1+hx. The EXACT integral
a=integral_0^1(1+c)^s ds and Taylor's integral remainder imply
a0=1+c/2-c^2/12<=a<=a0+c^3/24<=1+c/2.
No formal series. Let T=Tp, tT=T/q. The full Lambert sum is
T=(h^2/ell)sum_(N>=1)N d^(N-1)/(exp(Ndelta)-1).
GLOBAL inequalities s/(exp(s)-1)>=1-s/2 and<=1-s/2+s^2/12 give
t0=(a-x/2)/ell<=tT<=t1=s0/ell,
s0=a-x/2+x^2(2-h)/(12a). Note s0<=1 since h<=1/2,x<=1/50,
so t1<=1/ell, below the vertex (1+1/ell)/2.
Holding ONLY h,d fixed, the accepted227 derivative gives
 Fpipe=2Gactual/[2-(ell+1)tT],
 Gactual=tT^2/x-(1+1/ell)tT/x+K,
 K=(c h^2)/(ell^2 delta^2)sum d^(N-1) C(Ndelta),
 C(s)=s^2exp(s)/(exp(s)-1)^2>=1-s^2/12.
For the last GLOBAL bound, multiply by2(cosh(s)-1); coefficient at
s^(2n),n>=3 is[(2n)(2n-1)-12]/[6(2n)!]>=0; lower powers vanish.
Hence K>=a^2/(x ell^2)-x(2-h)/(12ell^2).
The quadratic in tT is decreasing up to t1; using t0 for the denominator
and t1,Klower for G shows that236 follows from P(a)>0, where
P(a)=2[s0^2-(ell+1)s0+a^2-x^2(2-h)/12]
 -(f-x)x ell[2ell-(ell+1)(a-x/2)].
P is increasing for a>=a0 in the stated interval: ds0/da in(0,1),
s0>=.99,ell+1<=2.01,2a>=2, and f-x>0. Thus P'(a)>=2(2-.03)>0.
At a=a0 the exact rational expression is
 P(a0)=x^3 Kpoly(h,x)/[72(h^2x^2-6hx-12)^2].
The standalone script expands Kpoly, checks its constant6912, and bounds
ALL its negative coefficients on h<=1/2,x<=1/50 by
4889076797501063/8000000000000<700. All other monomials are nonnegative;
Kpoly>6912-700>0. This finite identity proves236 on the whole domain.
All Lambert bounds were summed over EVERY N; all differentiated terms
are scalar geometric series with fixed d<1, as established in227.

## 237. Coupled230 is closed on the ENTIRE hard q>=50 domain

By235c--236,
Fpipe-Ehard Hpi>1/6-1/q-I-1/(4q)>=1/6-1/40-I.
With s=19/61, log(40/21)>2(s+s^3/3+s^5/5), a global positive atanh
series (or integrated geometric remainder). Therefore the last expression
is strictly greater than3535510187/253378890300>1/100.
This proves previously OPEN230. Accepted222 and229 then give
 Ffloor>Fpipe-e Hpi-e^2Jminus>1/200,                 (237)
since actual e<Ehard and E^2Jminus<1/200. Consequently v_mu'(lambda)<0
for EVERY original-law actual hard state q>=50 (u>=50/51), subject to the
already accepted actual differentiability/floor chain. Original alpha>=1
states were already proved. This is an actual first-moment region,
not yet a common bias interval or the full general theorem. q<50 remains
OPEN; crossing1 and continuity/local-interval deductions are not used here.

Supporting executable uniform_high_q_coupled_certificate.py is standalone;
it checks every new finite certificate exactly. The all-N and whole-age
arguments are the proofs above, not inferred from finite-N checks.
STATUS: full proof/exact checks independentlyPASS SAME sole auxiliary;
audit_receipt_uniform_high_q_20261004.md saved. q<50 remains OPEN.
