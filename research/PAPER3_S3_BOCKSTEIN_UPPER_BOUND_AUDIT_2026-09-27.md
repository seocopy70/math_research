# PAPER 3 — S3 BOCKSTEIN UPPER-BOUND AUDIT — 2026-09-27

## Status at entry

S1 and S2 are already independently closed:
- S1: (W_p(G_p)\cong W_p(G_{p^2})) for the declared unmarked truncated filtered-object definition.
- S2: (eta_{G_p}\not\congeta_{G_{p^2}}) and (operatorname{Im}eta_{G_p}\neoperatorname{Im}eta_{G_{p^2}}).
- Consequently (r_{T_\beta}(\mathcal C;D_\bullet)\ge p+1) is established as a **PASS / LOCAL** lower bound.

## Active gate

**S3: upper bound**
[
r_{T_\beta}(\mathcal C;D_\bullet)\le p+1.
]

The target claim is:
[
W_{p+1}(G)\cong W_{p+1}(H)
\Longrightarrow
\beta_G\cong\beta_H
]
for the explicitly declared fixed-rank Demuškin category.

If proved under the stated category and isomorphism notion, this closes
[
r_{T_\beta}=p+1.
]

## Proposed proof route — NOT YET VALIDATED

1. Identify exactly which (p)-power operation is functorially encoded by the truncated filtered group (W_{p+1}(G)), rather than assuming that the associated graded data alone suffices.
2. Audit whether the Bockstein (eta_G) is intrinsically recoverable from that operation for the entire declared Demuškin category, including basis-free/isomorphism-natural formulation.
3. Use the one-relator/Bockstein formula only as an independent verification of the intrinsic reconstruction, not as a substitute for proving that (W_{p+1}) carries the required information.
4. Verify the implication under arbitrary filtered-object isomorphism (W_{p+1}(G)\cong W_{p+1}(H)).
5. Check the boundary cases (p=2) separately; the current S1/S2 candidate and Bockstein formula were developed for odd (p).

## Critical caution

The sentence “the (p)-power map (D_1/D_2\to D_p/D_{p+1}) is part of (W_{p+1})” must be proved as a **canonical operation of the truncated group/filtration**, not merely inferred from a chosen presentation.

Likewise, “the Demuškin Bockstein is exactly the dual of that (p)-power map” requires a precise natural statement, including the target/source identifications and any dualizing-orientation dependence. A presentation-specific coefficient formula alone does not establish the upper bound.

## Classification

**OPEN — S3 active.**

No upper-bound theorem is claimed yet. The expected value (p+1) is a working hypothesis only.

## Next verification order

**pre-check → precise truncated-operation definition → literature/formula audit → intrinsic reconstruction lemma → arbitrary-isomorphism implication → independent presentation check → classify → immediately record.**
