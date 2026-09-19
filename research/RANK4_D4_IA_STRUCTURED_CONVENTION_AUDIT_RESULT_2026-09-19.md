# Rank-4 D4 Structured Convention Audit — 2026-09-19

## Status

**PASS / CRITICAL IMPLEMENTATION-CONVENTION AUDIT VERIFIED**

Final CI:
- run: `35418900971`
- head commit: `0c4a3d7e454ad9d5b04df2e9b3650872b90d943b`
- workflow: `rank4-d4-ia-structured-defect-composition`
- job: `105832726506`

## Purpose

Before authorizing an unrestricted rank-4 representative scan, audit the exact implementation conventions behind the structured cocycle result:
1. `matrix_to_lift` must induce the declared degree-1 matrix;
2. free-word composition `comp(A,B)` must correspond to ordinary matrix multiplication in the frozen column convention;
3. the GSp multiplier must be checked independently;
4. the quotient-valued q-defect law must be run under the frozen composition/action convention.

## Final verified results

The 9-representative family was checked exactly as follows:
- 9/9 GSp matrix identities pass;
- every constructed free lift reproduces its declared degree-1 matrix;
- for all 81 ordered pairs, `linear_matrix(comp(g,h)) = linear_matrix(g) linear_matrix(h)`;
- gauge rank = 20;
- `dim Q3 = 44`;
- candidate law
  [
  \Delta_q(gh)=\Delta_q(g)+g\cdot\Delta_q(h)
  ]
  has 0 raw failures and 0 failures modulo (Q_3);
- reversed action/order diagnostic has 18 raw and 18 modulo-(Q_3) failures;
- 60 composed q-defect classes survive (Q_3).

Both multiplier-2 GSp representatives are included in the 81-pair audit.

## Convention correction during audit

A temporary test inserting an explicit multiplier factor into the cocycle law produced 12 failures. The attempted normalized cocycle variant also failed. These tests were not promoted.

The final audit restores the frozen raw q-defect law. This is consistent with the definition
[
\Delta_q(g)=[F_g(X_1^3)-X_1^3]_{3},
]
because the multiplier contribution is already contained in the transformed cubic source; an additional external (mu)-factor would double-count it.

The auxiliary direct-source diagnostic was removed after identifying that it mixed the free-word/Magnus substitution representation with the already evaluated defect representation. It was not used as evidence for the gate decision.

## Decision

The implementation/convention audit is **PASS / CLOSED** for the structured family.

This clears the specific pre-scan implementation audit. It does **not** prove full (GSp_4(\mathbf F_3)) covariance, arbitrary free-group coordinate naturality, or canonicality of the quotient datum.

## Next authorized step

A broader rank-4 representative scan may now be considered, but its scope and PASS/FAIL consequence must be fixed before execution. The scan must continue to use:
- the frozen (Q_3=A_3/(C_3+\Delta_{IA}));
- the frozen raw (\Delta_q) law;
- the verified column/matrix composition convention;
- explicit GSp multiplier checks;
- no preferred-lift repair.

No claim of full covariance or canonicality may be inferred merely from a successful broad scan.
