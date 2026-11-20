# Explicit assigned-v polynomial extension and all Mellin identities

4 October2026. Priority clarification requested by the SAME sole reviewer.
Complete local proof and full symbolic identities SELF-CHECKED; independent
audit PENDING. The reviewer has PASSED codeA's288-coefficient absorption
certificate; codesB/C and the theorem glue are still under review.

Fixlambda,mu and the ACTUAL canonical lawpi throughout this paragraph.
Letv_* be its actual speed, t(x,y)=x+y-xy,A=c+t, b_tree(x)=x(1-x)/lambda,
Jf(x)=E[f(Y)/A(x,Y)^2], r0=Jid, q0=J(y^2), g the actual logarithmic
response, andGamma=E[b_tree*r0]-E[g*q0]>0. Define for free scalarv

 P_c(v;y)=(1-y)[2v-(1+v)y],
 P_v(y)=y^2+c[(1+v)y-v],
 C_pair(v)=E[(v*t-XY)/A^2],
 C_tilde(v)=E[b_tree(X)*(J P_c(v))(X)],
 a(v)=(u-v*A0/c)/b, A0=E(1-U)(1-lambda*U)>0,
 F_tilde(v)=2a(v)E[b_tree*r0]-C_tilde(v)
                    +2E[g*(J P_v-a(v)q0)].                 (84)

The symbolF_star ALWAYS denotes the original actual-speed floor.
Assigned arguments in previous root drafts are understood explicitly
asF_tilde in(84), not a natural extension of C_pair.

## Equality only at the actual speed, with exact off-speed correction

Pointwise symmetrization gives

 [b_tree(x)P_c(v;y)+b_tree(y)P_c(v;x)]/2
                         =(1-t)(v*t-xy)/lambda.

Consequently, forEVERYv,

 C_pair(v)-C_tilde(v)=E[(v*t-XY)/A]/lambda
                                =(v*Z-N)/lambda.          (85)

Only atv=v_*=N/Z do these two C's agree. ThusF_tilde(v_*)=F_star.
If F_natural uses C_pair instead, F_tilde(v)=F_natural(v)+(vZ-N)/lambda.
No assigned derivative or identity for F_natural is used.

## Exact negative derivative of THIS extension

DefineD_tilde_g(v)=2E[g J P_v]-C_tilde(v). Then
F_tilde(v)=D_tilde_g(v)+2a(v)Gamma and

 F_tilde'(v)=2cE[g J(y-1)]
              -E[b_tree J((1-y)(2-y))]
              -2*A0*Gamma/(c*b)<0.                        (86)

Every term uses fixed bounded kernels and fixed actual law, so this is
the derivative of an affine scalar expression. All strict signs are
legitimate:Gamma>0,A0>0,b>0,c>0, b_tree>0 and y<1 almost surely.
There is no differentiating the tree law, assigned speed of another law,
or off-speed response D. Hencev_bar>v_* implies
F_star=F_tilde(v_*)>F_tilde(v_bar).

## All original coefficients remain valid for the extension

Putx=cU/(1-U),y=cV/(1-V). Direct pointwise rational algebra, withv
FREE, gives

 b_tree(x)*y/A^2
       =U*V*(1-lambda*U)*(1-V)/[lambda*(1-lambda*U*V)^2],
 b_tree(x)*P_c(v;y)/A^2
       =U*(1-lambda*U)*(1-lambda*V)
           *[2v-(c+(lambda+1)v)V]
                            /[lambda*c*(1-lambda*U*V)^2],
 [(1-a)y^2+c((1+v)y-v)]/A^2
       =(1-U)^2*Q_a(V)/(1-lambda*U*V)^2.                 (87)

These identities need NOvZ=N. Expanding the uniformly convergent
geometric kernel at fixedlambda>1 gives, forEVERYv,a,

 F_tilde(v,a)=sum_(s>=1)w_s
        [eps_s*J_(s-1)(v,a)/(lambda*c)+2gamma_(s-1)t_(s-1)(v,a)],
 J_(s-1)=-2v*a_(s-1)+[c(1+2a)+(3lambda+1)v]a_s
                         -[c(lambda+2a)+lambda(lambda+1)v]a_(s+1).

The terms2aEbr0 and C_tilde yield this J directly. The complete
identityJ=2ct+c[(1+v)eps-2(1-a)a_s] is pure algebra and hence holds
for allv,a. Atcalibrationa=a(v),t0=0. Therefore the entire root identity,
all-index absorption, marker-moment lower replacement, and root+s2+s3
clearing are valid forF_tilde(v_bar). Only the actual-speed response
inequalityD>=F_star is used when returning from(86) to the true speed.

## Dependency correction

The old statement 'C=EbJPc' is used ONLY atv_*. Its previously audited
off-speed pair correction(85) explains why one must specify(84).
The new proof's derivative and every polynomial coefficient already
correspond to(84); specifying it repairs the wording without changing
any final coefficient or certificate. No assertion about C_pair at the
assigned v remains. assigned_polynomial_extension.py checks5 complete
rational identities, including symmetrization, the correction, and all
three kernel transformations. Pending audit; accepted threshold707/500.

LATEST4October2026 INDEPENDENT AUDIT PASS from SAME sole reviewer:
The CORRECTED u<=1/2 package includes this analytic interface. Explicit
assigned extension, off-speed correction, strict derivative, assigned
parameter range, original root regrouping, all-index absorption, canonical
Jensen/moment replacement and positive-term deletion all PASSED. The
wrong38998-calibration global proof remains WITHDRAWN; only the corrected
9600-coefficient small-u result is accepted. NEW high-u Root+s2 payment
is separately SELF-CHECKED/auditPENDING, inhigh_u_original_root_s2_result.md.
