# Paper 5 — IA/GL runtime correction and current boundary
Date: 2026-10-04

## Action completed

The executable `research/scripts/paper5_ia_gl_decomposition.g` was strengthened and committed at commit 0745df9336075c44b1b990a6b097042c02f104cc.

The decisive map Aut(W) -> GL(W/Phi(W)) now uses a validated GroupHomomorphismByImages built from the actual generators of Group(Concatenation(A.glAutos,A.agAutos)), rather than relying on the internal generator list directly with GroupHomomorphismByImagesNC.

The report now records:
- actual kernel order;
- v3 of the actual kernel;
- whether the candidate agAutos subgroup equals that kernel;
- the exact factorization |IA_kernel| |L| = |Aut(W)|.

## Why this matters

The decisive quantity is now the actual kernel, not Size(Group(A.agAutos)). This directly tests the implementation correction that agAutos must not be identified with IA without proof.

## Current mathematical boundary

Recovered repository artifacts certify:
- rank-2 negative control: the total-order gap is 3, not 3^2;
- rank-3 p=3,n=4 total-order pattern: split/non-split 3-valuation differs by 2;
- order arithmetic predicts IA orders 3^27 versus 3^25, while the predicted linear-image 3-valuation remains 3.

But the rank-3 IA localization is still OPEN / REPRODUCTION PENDING until the corrected GAP script actually runs and all gates pass.

No claim that IA causes the gap is promoted before that runtime certificate.

## Immediate stop rule

Do not move to Aut(W)->Aut(Q), IA filtration, or p=5 structural promotion until the corrected p=3,n=4 runtime closes.

After closure:
1. identify the exact IA kernel;
2. compute its first nontrivial filtration/layer responsible for the deficit;
3. only then test the quotient-action kernel;
4. use p=5 as a cross-prime test, not as the discovery engine.

## Classification

- corrected executable: PASS / REPOSITORY
- rank-2 negative control: PASS / REPOSITORY
- rank-3 p=3 total-order pattern: PASS / REPOSITORY
- rank-3 IA localization: OPEN / REPRODUCTION PENDING
- IA filtration: BLOCKED until IA localization
- Aut(W)->Aut(Q): BLOCKED until IA localization
- p=5 structural theorem: DEFERRED
