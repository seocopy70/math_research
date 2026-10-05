# Paper 5 Step 3 — Intrinsic Upper-Bound Re-audit (2026-10-06)

## Classification

**FAIL / CLOSED as submitted proof.**

The proposed generic Step-3 theorem claiming Im(Aut(W_n) -> GL(V_n)) = S'_11(p) for all declared odd p and the displayed order |S'_11(p)| = p^(n-3)(p-1)^2 is not established by the submitted argument. The p=5,n=6 runtime remains PASS / LOCAL and is recorded separately.

## 1. The local runtime is valid but does not close the upper bound

Run 37381098677 is a single case: (p,n,s,a)=(5,6,0,1). It has 113 computed automorphism generators and the direct permutation comparison gives actual order = candidate order = 2000. This is valid local evidence only.

It cannot prove Im <= S'_11(p) for general p,n.

Evidence: evidence/local/p5_n6_sa01_direct_perm.txt.

## 2. The proposed definition of S'_11 is not yet intrinsic

The submitted definition uses an arbitrary linear lift of M in GL(V_n) to the free pro-p presentation and then imposes a relation-preservation condition.

A linear map on V_n=W_n/Phi(W_n) does not canonically determine an endomorphism of the free pro-p presentation. Independence from the choice of lift is exactly part of the finite-window lifting/factorization problem. Therefore the assertion that the condition depends only on M because C_{a,b,k} is a basis is not a proof of intrinsicity.

The already-closed kernel-preservation result for explicitly constructed lifts gives a lower-bound construction; it does not manufacture an arbitrary lift for every automorphism of W_n.

## 3. The upper-bound argument uses the unresolved lifting bridge

The key inference is g in Aut(W_n) => a lift g-tilde with g-tilde(R) subset R => g-bar in S'_11(p). The first implication is not available for an arbitrary finite-window automorphism merely from the existence of the finite quotient. A lift to the chosen free presentation must be constructed and shown to preserve the relevant kernel/relation data in the correct quotient.

Thus the sentence that coefficients are forced because g-tilde(R) is contained in R cannot be used until the required lifting/factorization statement is independently supplied.

## 4. The claimed matrix shape/order is internally unsupported

The displayed block matrix with arbitrary vectors u,v and a nontrivial strictly upper-triangular N does not by itself have order p^(n-3)(p-1)^2. Those parameters would contribute substantially more p-power freedom unless additional equations are explicitly derived.

The asserted trace condition is not a substitute for deriving the complete parameter constraints and counting the resulting subgroup. No such general derivation is supplied in the submitted proof.

## 5. Restricted-power/Jacobson issue remains essential

The Paper-5 correction history already established that a naive linear model of the degree-(2,p) relation is insufficient: the restricted p-power component carries Jacobson/substitution terms. Therefore the statement that the filtered relation expansion automatically produces linear equations in the entries of g-bar requires a precise corrected operator calculation.

The corrected second-jet/kernel-preservation work is useful and closed in its declared mod-p Magnus layer, but it does not by itself identify the full image of arbitrary finite-window automorphisms.

## 6. Lower bound versus upper bound

- explicit relation-preserving lifts: PASS / CLOSED / GENERAL within declared scope;
- corresponding explicit subgroup S'_11(p) subset Im: PASS / CLOSED where the corrected target has been explicitly realized;
- arbitrary-image upper bound Im subset S'_11(p): OPEN / LOAD-BEARING for the general Step-3 problem;
- general equality and the resulting uniform automorphism-order theorem: OPEN / CONDITIONAL.

The special n=p corrected structure has its own dedicated closure record and must not be conflated with the generic n=6 local diagnostic.

## 7. Final classification of the submitted claim

Submitted generic Step-3 upper-bound proof = FAIL / CLOSED.

This does not mean the Paper-5 programme failed. It means the proposed proof did not close the last general image-factorization gate.

The correct current boundary remains: Im(Aut(W_n) -> GL(V_n)) subseteq S'_11(p) is OPEN / LOAD-BEARING, with the p=5,n=6 permutation equality retained as PASS / LOCAL only.

## 8. Authorized next gate

Do not run another prime sweep merely to compensate for the missing proof.

The next task is to derive an intrinsic upper-bound constraint directly from the corrected finite-window relation package, without assuming an automorphism of W_n lifts to an automorphism of F/R. If that cannot be done, the correct outcome is a counterexample or a narrower theorem scope—not promotion of the local equality.