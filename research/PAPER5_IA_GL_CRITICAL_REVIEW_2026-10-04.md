# Paper 5 — IA/GL critical review and recording
Date: 2026-10-04

## Critical verdict

The previous conclusion is directionally correct but must be stated one notch more conservatively.

The rank-2 result 3 is a valid negative control against any universal p^2 law. The rank-3 p=3,n=4 order pattern is a strong numerical localization candidate, but it is not yet an IA theorem.

The corrected executable now computes the actual kernel of the induced action Aut(W) -> GL(W/Phi(W)), rather than treating agAutos as IA by definition.

However, the corrected script itself is not a mathematical PASS until it has been executed successfully and all registered gates pass.

## What is genuinely established

1. Rank-2: the 3-adic valuation difference of the split and non-split automorphism orders is 1. Therefore a universal p^2 automorphism-gap statement is false.

2. Rank-3 p=3,n=4: the recovered total orders have 3-adic valuation difference 2.

3. Order arithmetic is compatible with a decomposition in which the linear image has 3-adic valuation 3 in both split and non-split cases and the residual difference lies in the kernel.

4. This is only a candidate localization until the actual kernel is computed.

## Important correction to wording

Do not say: The p^2 gap is an IA-layer defect.

Say: The p^2 gap is numerically consistent with an IA-kernel localization; the actual-kernel computation remains open.

Likewise, do not say that the IA kernel is already 3^27 versus 3^25. Those are order-arithmetic predictions.

## Implementation audit

The script correction is materially useful: it constructs the full generated automorphism group; constructs the induced action from actual generators; uses a validated homomorphism rather than GroupHomomorphismByImagesNC; computes the actual kernel; and separately reports whether agAutos happens to equal that kernel.

This removes the most serious implementation ambiguity.

A remaining runtime gate is still mandatory: the actual GAP execution must verify that the induced map is valid, that the generator checks pass, and that the kernel/image product reconstructs the full automorphism order.

## What must NOT be inferred

Even after IA localization passes, IA-defect does not automatically imply the Paper 4 detector, an intrinsic minimal carrier, or the unresolved Paper 4 distinction G_{s,s} versus G_{s,infinity}. A factorization/information-preservation theorem would be required.

## Correct next order

1. Execute corrected p=3,n=4 IA/GL audit.
2. If all gates pass, close the actual IA localization.
3. Compare the IA kernel structure, not just its order.
4. Locate the first filtration layer carrying the split/non-split defect.
5. Only then inspect Aut(W) -> Aut(Q).
6. Only after those steps use p=5 as a cross-prime validation.
7. Do not reopen Paper 4.

## Status table

| Item | Status |
|---|---|
| rank-2 negative control | PASS / REPOSITORY |
| rank-3 total-order pattern | PASS / REPOSITORY |
| universal p^2 law | FAIL / CLOSED |
| candidate IA localization | PASS / LOCAL-PREDICTED |
| actual IA kernel | OPEN / RUNTIME PENDING |
| IA filtration | BLOCKED |
| Aut(W) -> Aut(Q) | BLOCKED |
| p=5 structural theorem | DEFERRED |
| Paper 4 impact | NONE on established results |
| Paper 4 unresolved windows | remain OPEN |

## Final boundary

The scientifically strongest current claim is:

The automorphism-order deficit is rank/window dependent. In the tested rank-3 p=3,n=4 cases, the 3^2 deficit is numerically localized to the candidate IA factor, but the intrinsic IA-kernel decomposition has not yet been certified by the corrected runtime.

This boundary is authoritative for Paper 5 as of 2026-10-04.