# Q3/Q9 — q=9 degree-9 restricted relation space result

Date: 2026-09-19

## Status

**PASS — degree-9 q=9 relation-space construction.**

This gate is downstream of S9-A and S9-B and does not modify the frozen q=infinity baseline.

## 1. Definition

With the already-closed ambient identification
\[
S_9=X_1^{[9]}\in L_1^{[9]},\qquad S_9\neq0,
\]
define
\[
I_9:=\langle R_2,S_9\rangle_{res},
\qquad
I_{9,9}:=I_9\cap L_9^{res}.
\]

The frozen baseline is
\[
I_{\infty}:=\langle R_2\rangle_{res},
\qquad
\dim I_{\infty,9}=13524.
\]

## 2. Degree-9 closure argument

The new generator S9 has degree 9.

Therefore:

- any ordinary bracket involving S9 has degree at least 10;
- any restricted 3-power of S9 has degree 27;
- hence neither can contribute to the degree-9 piece.

Consequently the degree-9 part is exactly
\[
I_{9,9}=I_{\infty,9}+\langle S_9\rangle.
\]

S9-B established the structural non-membership
\[
(I_{\infty})_9\cap L_1^{[9]}=0,
\]
while
\[
S_9\in L_1^{[9]},\quad S_9\neq0.
\]

Hence the sum is direct:
\[
\boxed{I_{9,9}=I_{\infty,9}\oplus\langle S_9\rangle}.
\]

## 3. Exact F3 check

A small exact Gaussian-elimination check over F3 verifies that the S9 coordinate is a nonzero independent direction in the L1^[9] layer:

- baseline projection to L1^[9]: rank 0;
- S9 projection: rank 1.

No floating-point rank calculation is used.

The committed audit script is:
research/Q3_Q9_S9_q9_degree9_relation_space_2026-09-19.py

Local exact execution passed with:
\[
\dim I_{\infty,9}=13524,
\qquad
\dim I_{9,9}=13525.
\]

## 4. Gate decision

\[
\boxed{\dim I_{9,9}=13525}
\]

and therefore
\[
\boxed{\dim I_{9,9}-\dim I_{\infty,9}=+1}.
\]

This is a genuine q=9 degree-9 relation-space increment. It is not a retroactive modification of the baseline.

## 5. Scope boundary

Established:

- q=9 restricted ideal is now defined under the closed S9-A convention;
- its degree-9 relation space differs from the frozen baseline by exactly one S9 direction;
- exact F3 independence of the new direction was checked.

Not established:

- H-stability of I9 or I9,9;
- the precise identification of gr9(G9) with a quotient by I9,9;
- any D9 definition or interpretation;
- any q=9 invariant or orientation recovery.

Those remain separate downstream gates.

## Reproducibility

Script:
research/Q3_Q9_S9_q9_degree9_relation_space_2026-09-19.py

Workflow:
.github/workflows/q3-q9-s9-degree9-relation-space.yml

The baseline certificate remains:
research/Q3_Q9_C2c2_exact_degree9_restricted_closure_result_2026-09-19.md

S9-B structural certificate:
research/Q3_Q9_S9_B_STRUCTURAL_LEMMA_RESULT_2026-09-19.md
