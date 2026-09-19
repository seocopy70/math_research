# S9 admissibility preflight — 2026-09-19

## Status

**PREREQUISITE AUDIT COMPLETE / S9 ADMISSIBILITY NOT YET EXECUTED**

The frozen baseline remains unchanged:

dim I_{infty,9}=13524, and dim I_3^[3]=4.

No S9 term is inserted into the baseline ideal.

## 1. Restricted-power identification

The repository's Gate C-2a artifact fixes the one-generator enveloping-algebra realization over F_3:

X_1^[3]=X_1^3,
and
(X_1^[3])^[3]=X_1^9.

The exact word calculation was independently reproduced:

- X_1^[3] is the single word X_1 X_1 X_1 with coefficient 1;
- (X_1^[3])^[3] is the single word X_1^9 with coefficient 1;
- the latter equals the direct associative ninth power X_1^9.

Thus the ambient restricted-power identification is supported.

This does not yet prove that the Magnus-derived symbol S_9 := Delta_9(9)=X_1^9 is already a well-defined quotient-level restricted-Lie source for the q=9 relation construction.

## 2. Ambient degree-9 independence control

The existing C-2c-1 rank-2 certificate establishes, using exact F_3 Gaussian elimination,

rank L_9=56,
rank L_3^[3]=2,
rank L_1^[9]=2,

and

rank(L_9 + L_3^[3] + L_1^[9])=60.

This validates the restricted ambient layer separation in the small rank-2 tensor control. It is not a full rank-4 degree-9 tensor certificate.

## 3. Implementation invariants frozen before S9 execution

The authoritative convention document requires:

1. Complete closure: every generator acts on every accumulated basis vector until closure stabilizes.
2. Coordinate consistency: all subspace/rank comparisons occur in one common coordinate system; Python uses column action.
3. Exact F_3 rank: use the authoritative exact rank convention; real/numerical np.linalg.matrix_rank or det is forbidden.
4. Sanity checks: rank-nullity and relevant span/kernel identities must be checked before interpreting a result.

These are now confirmed as the mandatory invariants for the forthcoming S9 computation.

## 4. Critical distinction

The audit does not mark the S9 experiment itself as PASS.

The following are separate:

- Ambient identification: X_1^9=X_1^[9] in the restricted enveloping realization — supported/PASS at the C-2a level.
- Quotient-level admissibility of the Magnus-derived S9: whether this source can be inserted into the degree-9 restricted-Lie relation construction without an illicit identification — OPEN.
- Baseline ideal membership: whether S9 is in I_infty,9 — OPEN and must remain untested until admissibility is settled.
- q=9 ideal / H-stability / D9: downstream and blocked.

## 5. Gate consequence

No mathematical conclusion about S9 membership is authorized from this preflight.

The next execution must independently construct the quotient-level degree-9 source in the frozen convention, then test admissibility. Only after that result may the experiment test whether the admissible source is already contained in the frozen 13524-dimensional baseline ideal.

## Evidence

- research/Q3_Q9_GATE_C2a_restricted_power_2026-09-19.py — exact restricted-power identification.
- research/C-2C-1_restricted_ambient_certificate_2026-09-19.py — exact rank-2 ambient degree-9 control.
- research/03_CONVENTIONS_AND_IMPLEMENTATION.md — authoritative implementation invariants.
- research/Q3_Q9_C2c2_exact_degree9_restricted_closure_result_2026-09-19.md — frozen baseline dim I_infty,9=13524.
