# S9-B — Quotient survival gate (2026-09-19)

## Status

**PASS / CLOSED**

This gate tests the single question
[
S_9in I_{\infty,9} ?
]
after S9-A has established the ambient restricted representative
[
S_9=X_1^{[9]}.
]

No q=9 ideal is constructed here.

## Frozen baseline

The exact C-2c-2 degree-9 restricted-closure certificate gives
[
\dim L_9^{\mathrm{res}}=29144,
qquad
\dim I_{\infty,9}=13524,
]
with ordinary degree-9 relation dimension
[
\dim I^{\mathrm{ord}}_9=13520.
]

Hence the restricted closure adds exactly
[
13524-13520=4
]
new degree-9 relation directions.

The same certificate identifies the only possible genuinely new degree-9 restricted p-source as
[
I_3^{[3]},
qquad \dim I_3^{[3]}=4.
]

Descendants of (I_2^{[3]}) are already contained in the ordinary ideal through
[
[x^{[3]},y]=\operatorname{ad}(x)^3(y),
]
so they do not create an additional degree-9 p-layer.

## Degree-9 restricted-layer separation

Under the frozen free restricted-Lie decomposition, the degree-9 ambient has the direct layers
[
L_9^{\mathrm{res}}
=
L_9
\oplus
L_3^{[3]}
\oplus
L_1^{[9]}.
]

The baseline ideal has:

- an ordinary part inside (L_9);
- the new degree-9 restricted part (I_3^{[3]}subset L_3^{[3]});
- no (L_1^{[9]})-component.

Therefore the projection
[
\pi_1:L_9^{\mathrm{res}}	o L_1^{[9]}
]
annihilates the entire frozen baseline ideal:
[
\pi_1(I_{\infty,9})=0.
]

## S9 projection

By S9-A,
[
S_9=X_1^{[9]}.
]
Its (L_1^{[9]})-projection is the nonzero basis vector
[
\pi_1(S_9)=X_1^{[9]}\neq0.
]

Consequently
[
S_9\notin I_{\infty,9}.
]

Equivalently,
[
oxed{[S_9]\neq0
\quad\text{in}\quad
L_9^{\mathrm{res}}/I_{\infty,9}.}
]

## Decision

[
oxed{\text{S9-B: PASS}}
]

The degree-9 p-power source survives the q=∞ baseline quotient.

This is stronger than a dimension-only statement: it uses the exact restricted-layer decomposition and the certified identification of the baseline's only new degree-9 p-source as (I_3^{[3]}subset L_3^{[3]}), while (S_9) lies in the distinct (L_1^{[9]}) layer.

## Consequence

The previous logical barrier is now removed:

1. **S9-A — ambient admissibility:** PASS.
2. **S9-B — quotient survival:** PASS.
3. Therefore (S_9) is now a legitimate nonzero degree-9 restricted source in the frozen q=∞ quotient.

Still blocked:

- construction of (I_9=\langle R_2,S_9\rangle_{\mathrm{res}});
- H-stability of the resulting degree-9 relation ideal;
- any definition/claim involving (D_9);
- any q=9 comparison conclusion.

## Important scope note

S9-B does **not** claim that (S_9) is H-invariant, that the q=9 relation ideal is H-stable, or that any q=9 filtration invariant has been established. It only establishes survival of the admissible source against the frozen q=∞ baseline ideal.

## Evidence

- S9-A result: `research/Q3_Q9_S9_A_AMBIENT_ADMISSIBILITY_RESULT_2026-09-19.md`.
- C-2c-2 exact degree-9 restricted-closure certificate: `research/Q3_Q9_C2c2_exact_degree9_restricted_closure_result_2026-09-19.md`.
- C-2c-0 definition gate and its prohibition against premature ideal-membership interpretation.
- `research/03_CONVENTIONS_AND_IMPLEMENTATION.md`.

No numerical 29144-dimensional membership matrix was needed: the exact layer decomposition and certified source decomposition give the membership decision structurally.
