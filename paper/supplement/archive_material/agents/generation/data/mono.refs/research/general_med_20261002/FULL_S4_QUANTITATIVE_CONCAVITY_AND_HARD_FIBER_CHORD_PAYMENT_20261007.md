# Complete S4: quantitative concavity and a whole-fiber size test

2026-10-07. NEW LOCAL results, pending the same independent auxiliary.
The previous strict-concavity/chord lemma has FINAL PASS, with its
receipt and a separate V2 explanatory addendum now saved. No original
or audited file is modified. No new agent/task, scan or old certificate
is run.

This package proves a stronger uniform signed-core inequality and pays
the plain chord on the entire remaining T interval of the named old
negative-second-order fiber. It does NOT pay the general (lambda,u)
domain and does NOT assert that this assigned scalar fiber is realized
by a canonical offspring law. The independently verified general gap
remains 5/6<rho<102399/102400; original 9600 remains retained. The
overall speed result remains computationally assisted, and S42 is OPEN.

## 1. Stronger uniform sign and exact concavity surplus

Use exactly the profiles, Kb, Phi, Psi, Bstar, Jstar and Lcore from
FULL_S4_SIGNED_CORE_STRICT_CONCAVITY_AND_RECOVERY_CHORD_20261007.md.
Write Lcore=sum(c_j*rho^j,j=0..4), p=Phi(1), C0=Lcore(1),
ell0=Lcore(0)=2A^2*t/lambda-p. The audited signs are
c2<0,c4>0,c3+2c4<0 and eta_s=[rho^2](2U_s-V_s)>0.

There is a stronger sign, c3+4c4<0, proved without a parameter table.
The root coefficient identity is

    q4+5q5=(2u/A^2)*[Ah*(A-5lambda)+lambda^2*t+5lambda].

Since A-5lambda<0 and Ah<4/3, its bracket is strictly greater than

    (4/3)A+lambda^2*t-(5/3)lambda
      >=4/3-lambda+lambda^2/2
       =5/6+(lambda-1)^2/2>0.

Here A=1+lambda*t and t>=1/2; no additional moment input is assumed.
Thus c3+4c4=-(q4+5q5)-2sum(n_s*eta_s)<0.

Define the explicit concavity surplus

    H(rho)=-c2-(1+rho)*c3-(1+rho+rho^2)*c4.

Exactly,

    Lcore(rho)=(1-rho)*ell0+rho*C0+rho*(1-rho)*H(rho).    (1)

Also H(0)>-c2+3c4>0 and
H'(rho)=-c3-(1+2rho)c4>(3-2rho)c4>=c4>0 on [0,1].
This is a proved size inequality for the surplus, not concavity being
identified with positivity of Phi.

Put a=5/6 and

    Ka=ell0-C0+a*H(a)=[Lcore(a)-C0]/(1-a).

For rho>=a, substituting (1) into the exact complete recovery identity
and using rho*H(rho)>=a*H(a) gives

    Phi(T)>=p+C0*epsilon^2+Bstar*epsilon^3
                       +[Ka+Jstar]*epsilon^4,            (2)

where epsilon=1-T. This keeps the complete root and all negative prices.
Ka is kept signed; no unproved positivity assumption is attached to it.

## 2. One continuous quartic envelope for the WHOLE remaining region

For rho>=a, epsilon<=1/sqrt(6)<5/12. Audited positivity of every rho
coefficient of B_s=2U_s-V_s, and positivity of the coefficients of U_s,
show these profiles increase with rho. All d_s are positive and decrease
with epsilon. Consequently

    Bstar>=b:=2a*[2B3(a)+(27/4)B4(a)]>0,
    Jstar>=j:=2a*[U2(a)+(169/36)U3(a)+(2601/256)U4(a)]>0. (3)

The constants use d3(5/12)=13/6 and d4(5/12)=51/16. Hence the complete
budget has the proved uniform four-term bound

    Phi(T)>=p+C0*epsilon^2+b*epsilon^3+(Ka+j)*epsilon^4.   (4)

Likewise, the previously audited plain chord is at least

    p+C0*epsilon^2+b*epsilon^3+(ell0-C0+j)*epsilon^4.       (5)

All four coefficients are explicit functions of the same lambda,u,Kb
profile. The sign of (4) or (5) on the general domain is STILL OPEN;
this text does not turn an additional unproved lower bound into payment.
Unlike a succession of rho endpoints, (4) is a single continuous
quartic envelope for the whole remaining gap.

## 3. Actual size test on the old difficult fiber, all T at once

For lambda=231/200,u=1/2,K=Kb, exact Fraction evaluation gives

    p>1/8, C0>-251/100, b>2, ell0-C0+j>41/5.              (6)

For reference b=2.0815971100..., j=3.6824837264... and
ell0-C0+j=8.2112588439... . The small source checks (6) exactly;
these constants are claimed ONLY on this named coupled scalar fiber.
Thus its plain chord exceeds

    Q(x)=1/8-(251/100)x^2+2x^3+(41/5)x^4,
    0<=x<=1/sqrt(6).

A short continuous proof gives Q>1/100. For x<=1/5, drop the positive
terms: Q>=1/8-251/2500=123/5000>1/100. On [1/5,1/4], Q'' increases,
Q''(1/5)=329/250>0 and Q'(1/4)=-147/400<0. Hence Q decreases there
and is at least Q(1/4)=201/6400>1/100. For x>=1/4,
Q''>=Q''(1/4)=413/100>4, so

    Q(x)>=201/6400-(147/400)(x-1/4)+2(x-1/4)^2
          >=201/6400-(147/400)^2/8
           =18591/1280000>1/100.

Therefore there is NO negative point of the plain chord anywhere in
the whole remaining interval on this one old difficult fiber. This
includes rho=1. It is stronger than the five isolated point checks,
but it is not a general parameter reduction or a new general coverage
interval.

At epsilon=1/3, the exact plain chord lies between 0.05462 and 0.05463,
and the complete value is 0.1107473727... . The exact surplus identity
Phi-chord=epsilon^4*rho*H(rho)>0 is checked at the five previously named
diagnostic points; no new grid or free-marginal search is used.

## Remaining work

The uniform envelope (4), including its signed C0 and Ka, is now proved.
The missing payment is a joint size comparison of its explicit four
coefficients over the actual coupled lambda,u domain. The named-fiber
constants (6) must not be extended to that domain. No whole dependency
has been removed, and no human/computer percentage change is asserted.
