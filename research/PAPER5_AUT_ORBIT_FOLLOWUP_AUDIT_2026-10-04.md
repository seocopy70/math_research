# Paper 5 — Aut-orbit follow-up audit (2026-10-04)

## Provenance
User supplied the reported contents/results of aut_common.g, aut3.log, and p5aut.log. The source artifacts are not currently present in the repository tree, so this document records them as user-reported evidence only.

## Reported results
- p=3, s=1, a=1: 72 admissible kernels; orbit sizes 9, 9, 54; all non-split.
- p=3, s=1, a=2: 9 admissible kernels; one orbit; non-split.
- p=3, s=2, a=1, n=10: 81 admissible kernels; one Aut(W_10)-orbit; reported |Aut(W_10)|=2*3^30; |K|=3^9; 3^10 complements per kernel.
- p=5,n=6: reported Aut orders reproduce the p^2 p-primary split/non-split gap and show s-dependence in the total order.

## Structural claims not yet certified
1. The 9+9+54 orbit split is not yet fully explained by intrinsic orbit invariants. pi(z) in Phi(Q) is reported to distinguish two size-9 orbits, but no invariant explaining all three orbit sizes is yet certified.
2. The single-orbit statement at (3,2,1,10) is a strong local signal but is not a theorem until independently reproduced.
3. The complement count 3^10 is not yet connected to a structural cohomological/automorphism calculation.
4. The p=5 order pattern is cross-prime evidence, not yet a decomposition theorem.

## Gate consequence
The new data do not invalidate the current Paper 5 pre-check. They sharpen the questions for the authorized IA/GL decomposition:
- determine whether the p^2 loss lies in IA(W), the linear image, or the fixed-quotient action;
- record whether the orbit invariants are visible through the same intrinsic layers;
- only after p=3,n=4 closure should p=5,n=6 be used as the cross-prime structural test.

## Classification
PASS / LOCAL — strong user-reported computational evidence for an Aut-orbit layer; reproduction and structural factorization remain OPEN.
