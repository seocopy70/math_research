# Paper 5 — rank-2 automorphism-gap audit, 2026-10-04

## Scope
This audit records the new rank-2 control computation for the Paper 5 Aut(W_n) program. It is a boundary test for the earlier hypothesis that the split/non-split automorphism-order deficit is universally p^2.

## Reproduced computation
For p=3 and n=4, both tested rank-2 windows have order |W|=729:

| case | |Aut(W)| | factorization |
|---|---:|---|
| s=0,a=1 | 78732 | 2^2 * 3^9 |
| s=1,a=1 | 26244 | 2^2 * 3^8 |

Hence the exact ratio is 3. This is a repository-recorded/reproduced computation, not a prediction.

## Structural correction
The earlier shorthand IA = Product(A.agOrder) is invalid as a definition of the IA kernel. AutPGrp documents agAutos as a soluble normal subgroup and glAutos as automorphisms acting nontrivially on the Frattini quotient; the actual IA group is ker(Aut(W) -> Aut(W/Phi(W))).

The repository now contains an explicit rank-2 audit script at research/scripts/paper5_rank2_actual_ia_kernel.g. The script computes the actual Frattini-action kernel and corresponding linear image and checks the exact product formula. Its numerical output is not promoted here unless separately recorded.

## Consequence
The rank-2 calculation FAILS the universality of the p^2-gap conjecture.
It does not show that the p=3,n=4 rank-3 family has no p^2 IA defect. It shows only that the exponent of the automorphism-order deficit depends on structural parameters and cannot be stated as a universal p^2 phenomenon across ranks.

The correct Paper 5 question is therefore: What intrinsic structural quantity controls the IA-kernel order difference between the split and non-split windows, and under what rank/window hypotheses does it equal p^2 (or p, or another power)?

## Classification
- rank-2 total-order computation: PASS / LOCAL
- universal p^2-gap claim across rank: FAIL / CLOSED
- rank-2 IA/GL decomposition: OPEN / REPRODUCTION PENDING
- rank-3 p=3,n=4 IA localization: OPEN / LOAD-BEARING
- quotient action Aut(W)->Aut(Q): OPEN
- p=5 cross-prime structural theorem: DEFERRED

## Next authorized step
Do not run more p=5 calculations yet. First certify the actual Frattini kernel/image for the rank-3 p=3,n=4 four-case family. In parallel, use the rank-2 result as a negative control: any proposed formula for the IA defect must specialize to a single factor 3 in the rank-2 control.