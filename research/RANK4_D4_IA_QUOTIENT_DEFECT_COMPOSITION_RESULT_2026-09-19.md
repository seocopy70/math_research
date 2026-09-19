# Rank-4 D4 Quotient-Valued q-Defect Composition Audit — 2026-09-19

## Status
**PASS / LOCAL — CORRECTED**

## Important correction
The earlier CI run `35417325110` used an implementation bug: the helper `defect` added the reference relator term instead of subtracting it. That made the earlier reported cocycle result invalid. It is superseded and must not be used as evidence.

The corrected implementation uses
[
delta_g=[F_g(R_3)-mu(g)R_3]_{deg3}.
]

## Corrected CI
- Run: `35418122079`
- Commit: `bb39ed1a7191aeae0da07813e40abe47695d292a`
- Workflow: `rank4-d4-ia-quotient-defect-composition`

## q-sensitive defect
[
Delta_q(g)=[delta_3(g)-delta_infty(g)]
=[F_g(X_1^3)-X_1^3]_{deg3}.
]

For (F_{gh}=F_gcirc F_h), the tested law is
[
oxed{Delta_q(gh)=Delta_q(g)+gcdotDelta_q(h)}
]
in (Q_3=A_3/(C_3+Delta_{mathrm{IA}})).

## Corrected exact results

[
operatorname{rank}(C_3+Delta_{mathrm{IA}})=20,
qquad
dim Q_3=44.
]

Across all 16 ordered pairs of identity, (-I), the standard transvection (e_1mapsto e_1+e_2), and (operatorname{diag}(2,1,2,1)):

- candidate-law failures modulo (Q_3): **0**;
- candidate-law raw failures: **0**;
- reversed action/order diagnostic failures modulo (Q_3): **2**;
- reversed raw failures: **2**;
- composed q-defect classes surviving (Q_3): **11**.

Therefore the corrected audit gives a genuine **local PASS** for the candidate cocycle law, and the reversed convention is distinguished on this control set.

## Scope

This does not establish arbitrary free-group coordinate naturality, full (GSp_4(mathbf F_3)) cocycle covariance, canonicality under all coordinate choices, or recovery of (chi).

## Next gate

Broaden the audit to a structured representative family, explicitly checking the now-fixed action/order convention and multiplier behavior. No unrestricted full rank-4 scan is authorized yet.
