# S9-A — Ambient admissibility gate (2026-09-19)

## Status

**PASS / CLOSED**

This gate is deliberately limited to **ambient restricted-power admissibility**. It does not assert quotient survival and does not test membership in (I_{\infty,9}).

## Frozen inputs

- C-2c-0 defines (S_9:=\Delta_9(9)) and records (S_9=X_1^9) first as an associative Magnus word.
- Gate C-2a independently verifies, over (mathbf F_3), that
  [
  X_1^{[3]}=X_1^3,qquad
  (X_1^{[3]})^{[3]}=X_1^9.
  ]
- C-2c-1 verifies the relevant degree-9 restricted ambient layer in the rank-2 control; it is not used as a rank-4 certificate.
- C-2c-2 freezes the rank-4 baseline (dim I_{\infty,9}=13524), with no (S_9) inserted.

## Gate criterion

The ambient gate asks only whether the already-defined Magnus source (S_9=X_1^9) has a legitimate restricted-power representative in the degree-9 ambient convention.

The C-2a exact calculation gives the representative
[
S_9=X_1^{[9]}:=(X_1^{[3]})^{[3]}
]
inside the restricted-power layer.

This is an **ambient identification**, not a quotient-level statement.

## Checks

1. (X_1^{[3]}) is the single associative word (X_1^3) with coefficient (1inmathbf F_3). — PASS.
2. ((X_1^{[3]})^{[3]}) is the single word (X_1^9) with coefficient (1). — PASS.
3. The iterated restricted-power word equals the direct associative ninth power (X_1^9). — PASS.
4. No (S_9) term has been inserted into (I_{\infty,9}). — PASS.
5. The frozen baseline (\dim I_{\infty,9}=13524) is unchanged. — PASS.

## Decision

[
oxed{\text{S9-A: PASS}}
]

From this point onward, (S_9) may be used as the restricted ambient element (X_1^{[9]}) for the **quotient-survival test only**.

The following remain unproven and are explicitly not inferred:

- (S_9\neq0) in (L_9^{\mathrm{res}}/I_{\infty,9});
- (S_9\notin I_{\infty,9});
- any (q=9) relation ideal;
- H-stability or (D_9);
- any q=3/q=9 conclusion.

## Evidence

- Gate C-2a restricted-power identification.
- `research/Q3_Q9_S9_admissibility_preflight_2026-09-19.md`.
- `research/Q3_Q9_C2c2_exact_degree9_restricted_closure_result_2026-09-19.md`.
- `research/03_CONVENTIONS_AND_IMPLEMENTATION.md`.

No new quotient-membership claim is introduced by this record.
