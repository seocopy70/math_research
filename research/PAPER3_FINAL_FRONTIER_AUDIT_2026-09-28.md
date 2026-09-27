# PAPER 3 — 2026-09-28 FINAL FRONTIER AUDIT

## Scope
This audit records the post-recognition stage after the corrected selector-minimality proof and the finite cup-line compression proof. It separates (A) mathematical closure, (B) publication novelty, and (C) remaining research questions.

## A. Selector-window minimality
For the fixed rank-4, q=3 pro-3 Demushkin group and k>=2, put N=3^{k-1} and W_m=G/D_m(G). The canonical character satisfies chi(x_2)=(1-3)^{-1} mod 3^k and has exact order N on the free x_2-direction of G_ab.

There are two ranges below N:

1. m <= 3^{k-2}: chi does not factor through W_m, because D_m(G) maps to a nontrivial subgroup in the free x_2-direction whose chi-image is nontrivial mod 3^k.

2. 3^{k-2} < m <= N: chi does factor through W_m, but K_k(W_m,chi_m) fails. In W_m the image of x_2 has exact order N. For a lift z of the mod-3 character f(x_2)=1, the relation x_2^N=1 forces
   0=S_N(u)z(x_2), u=(1-3)^{-1}, S_N(u)=1+u+...+u^{N-1}.
   LTE gives v_3(S_N(u))=k-1, so z(x_2) is divisible by 3, contradicting z(x_2)=1 mod 3.

Since W_{N+1} is sufficient by D1-D3, the exact selector threshold is

  n_selector(k)=3^{k-1}+1.

This is a genuine selector-minimality theorem for the fixed rank-4 q=3 scope. It is independent of the earlier affine sharpness theorem. The stronger uniform q statement remains a separate theorem: for q=3^f with f<k the same LTE endpoint argument works; when f>=k the reduction chi mod 3^k is trivial, so that argument no longer proves a nontrivial selector lower bound.

Status: PASS / CLOSED at fixed rank-4, q=3.

## B. Finite 1-dimensional carrier
Let Q_k=G/D_{3^{k-1}+1} and
C_k=im(H^1(Q_k,F_3) tensor H^1(Q_k,F_3) -> H^2(Q_k,F_3)).
The prior objection that naturality alone cannot prove dim C_k=1 is now repaired by relation-module/cup-product duality. Writing Q_k=F/R_k with R_k=R D_{3^{k-1}+1}(F), the added relators lie in D_3(F), so the image of R_k in D_2(F)/D_3(F) remains the one-dimensional Demushkin quadratic initial relation. The duality theorem identifies this image rank with the rank of the finite cup map. Hence dim C_k=1 and C_k -> H^2(G,F_3) is nonzero, therefore injective.

The D2 variation identity places false-branch outputs in C_k, and D2 supplies at least one nonzero surviving witness for every false candidate. Therefore C_k is a sufficient 1-dimensional intrinsic finite selector carrier, and dimension 0 cannot recognize the false candidates in this linear selector-carrier category.

Status: PASS / CLOSED at the declared category/scope.

## C. Canonical functional O_k -> F_p
The stronger question whether the global detector lambda_k:O_k->H^2(G,F_p) can itself be reconstructed functorially from the finite pair E_k->Q_k alone is still OPEN. It is no longer load-bearing for recognition because C_k supplies a direct 1-dimensional finite carrier.

Do not conflate:
- finite-pair reconstruction of a canonical functional on the whole O_k;
- existence of a 1-dimensional finite selector carrier C_k sufficient for recognition.

## D. Publication novelty audit — current conclusion
The audited literature establishes the classical Kummerian criterion and uniqueness of the canonical Demushkin orientation, including the equivalent cocycle criterion and quotient inheritance under additional hypotheses. Efrat–Quadrelli (2019) and Quadrelli (2024) explicitly formulate Kummerianity through surjectivity of H^1(G,Z_p(theta)/p^n)->H^1(G,F_p) and cocycle criteria; Quadrelli's quotient-inheritance proposition requires N subset Ker(theta) plus a restriction-surjectivity hypothesis. These are not the same as arbitrary-candidate factorization through Q_k=G/D_{p^{k-1}+1}.

The Zassenhaus/cohomology literature establishes the filtration, restricted Lie algebra, and relation/cup-product duality. It does not, in the sources checked, state the exact finite selector theorem with all of the following simultaneously: bare Q_k as finite input, arbitrary principal-unit candidate rho, arbitrary-candidate factorization of twisted H^1 through Q_k, and recognition of exactly chi mod p^k without presentation/q input.

The current novelty statement must remain conditional, not absolute: no exact prior theorem matching this package was identified in the audited corpus. The finite-factorization/finite-recognition assembly is the narrowest plausible novelty boundary; canonical orientation/Kummerianity themselves are classical.

Important audit boundary: this is not an exhaustive proof of priority. Before submission, the manuscript should phrase novelty as “no exact matching theorem was identified in the literature checked” and should not say “first” or “newly discovered” without a broader human literature review.

## E. Remaining authorized work
1. Independent line-by-line proof audit of D1 semidirect filtration and D2 coefficient-variation/PD^2 step.
2. Reconcile manuscript wording with the now-closed selector minimality theorem; remove all stale statements saying minimality is open.
3. Reconcile the generalized report: uniform-in-q recognition is now closed only where the corrected proof genuinely covers q; the endpoint sharpness argument needs the f<k versus f>=k split.
4. Compile the manuscript and perform a final notation/convention audit.
5. Only after these, decide whether the stronger finite-pair functional reconstruction is worth pursuing; it is not required for the main theorem.

## Final status
- Finite-window recognition: PASS / CLOSED at declared Demushkin scope.
- Selector threshold p^{k-1}+1: PASS / CLOSED for fixed rank-4 q=3; broader q endpoint scope requires explicit qualification.
- 1D finite cup-line selector carrier: PASS / CLOSED.
- Absolute carrier minimality: not a meaningful unqualified question; 1D is minimal in the declared linear selector-carrier category.
- Canonical O_k functional from E_k->Q_k alone: OPEN / NOT LOAD-BEARING.
- Publication novelty: OPEN / CONDITIONAL.
- Manuscript readiness: CONDITIONAL on final proof/notation/compilation audit.
