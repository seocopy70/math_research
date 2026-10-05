# Paper 5 — Intrinsic filtered relation-module factorization audit
Date: 2026-10-05

## Status
**OPEN / LOAD-BEARING.**

The raw pair (pi_2(r), pi_p(r)) is not intrinsically defined for a mixed relation r in D_2\D_3, because pi_p(r) is only defined for elements of D_p. The correct replacement is a filtered relation-module object.

## 1. Intrinsic relation module
Let W_n=F/R_n and M_n:=R_n/[F,R_n]. Give M_n the filtration
M_n^(k):=((R_n cap D_k(F))[F,R_n])/[F,R_n].
The associated graded relation module gr M_n is naturally a module over gr_D(F), hence over the free restricted Lie algebra on V=D_1/D_2.

## 2. Correct two-level jet
For the mixed relation case with initial degree 2, retain the truncated filtered object
J_filt(s,a):=(M_n^(2)/M_n^(p+1), L_2 subset M_n^(2)/M_n^(3)),
together with its induced L(V)-module structure and the distinguished degree-2 relation line L_2.

Equivalently, the secondary datum is the filtered extension
0 -> M_n^(p)/M_n^(p+1) -> M_n^(2)/M_n^(p+1) -> M_n^(2)/M_n^(p) -> 0,
not a chosen vector obtained from a splitting.

Any concrete pair (ell_2, ell_p_bar) must therefore be understood as a choice of splitting/normal form of this filtered object. The splitting gauge must be quotiented before identifying its GL stabilizer.

## 3. Why this fixes B-2b
If r in D_2\D_3, then pi_p(r) is undefined. A decomposition r=r_2 r_p r_{>p} is not canonical and cannot be used as an invariant definition.

The filtered relation module avoids this defect: an automorphism of W_n induces an automorphism of the extension kernel and hence of M_n, preserving its induced filtration. Therefore it preserves the entire truncated filtered object without requiring a lift of the automorphism to Aut(F).

## 4. What is proved and what is not
PASS / LOCAL: if c in [R_n,F] and R_n subseteq D_2, then c in D_3 by [D_2,D_1] subseteq D_3.

OPEN / LOAD-BEARING: identify the concrete four-case jets with filtered-relation-module normal forms, and prove that the induced Aut(W_n)-action maps, after gauge quotient, to the stated projective stabilizer.

Not available: Hopficity does not supply a lift Aut(W_n) -> Aut(F).

## 5. Precise next lemma
Lemma FRM: construct a canonical functor W_n -> J_filt(s,a) from the finite-window realization to the truncated filtered relation-module object, and prove every alpha in Aut(W_n) induces an automorphism of it.

Then prove a normal-form identification lemma: after quotienting by splitting/gauge ambiguity, the four marked cases reduce to
[x,y]+x^[p], [x,y]+z^[p]-x^[p], [x,y], [x,y]+z^[p].

Only after these lemmas may one conclude that Im rho_n is contained in the stabilizer of the intrinsic filtered jet. The stabilizer must then be shown equal to the previously computed matrix groups before importing those groups into the finite-window theorem.

## 6. Stop condition
If the filtered relation-module object is intrinsic but its gauge-quotient stabilizer is strictly larger than the four computed projective groups, the current factorization target fails as formulated. Do not repair the jet ad hoc. Classify the boundary and record it as FAIL/CLOSED or CONDITIONAL as appropriate.
