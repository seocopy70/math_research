# HARD ATTACK 50 — DIMENSIONAL OBSTRUCTION FOR THE (2,1) SURVIVOR

Date: 2026-09-20

## Target

Hard Attack 49 proved
\[
H^2(V,\mathbf F_3)\cup K=H^4(V,\mathbf F_3),
\]
so
\[
E_3^{4,0}=E_\infty^{4,0}=0.
\]
The next question is
\[
E_3^{2,1}=\ker(d_2:E_2^{2,1}\to E_2^{4,0})/\operatorname{im}(d_2:E_2^{0,2}\to E_2^{2,1}).
\]

## Pre-check

At the frozen q=3 level, HA45 gives
\[
V\cong\mathbf F_3^4,\qquad W\cong\mathbf F_3^9,
\]
with W central and elementary abelian in Q_2. Hence
\[
\dim E_2^{2,1}=\dim H^2(V)\dim W^*=10\cdot9=90.
\]
Also
\[
\dim E_2^{4,0}=\dim H^4(V)=35.
\]
HA49 established surjectivity of the outgoing d_2, so
\[
\dim\ker d_2^{2,1}=90-35=55.
\]

The incoming source is
\[
E_2^{0,2}=H^2(W,\mathbf F_3).
\]
Since W\cong\mathbf F_3^9 is elementary abelian,
\[
H^*(W,\mathbf F_3)\cong\Lambda(W^*)\otimes\operatorname{Sym}(\beta W^*),
\]
and therefore
\[
\dim H^2(W,\mathbf F_3)=\binom92+9=36+9=45.
\]

## Forced consequence

For every linear differential
\[
d_2^{0,2}:E_2^{0,2}\to E_2^{2,1},
\]
\[
\dim\operatorname{im}d_2^{0,2}\le45.
\]
Therefore
\[
\boxed{\dim E_3^{2,1}\ge55-45=10}.
\]
In particular
\[
\boxed{E_3^{2,1}\neq0}.
\]

This is a dimension obstruction, not a failure to compute the incoming differential: no d_2 argument can eliminate the entire (2,1) sector.

## Stronger boundary

The exact dimension remains open:
\[
\dim E_3^{2,1}=55-\operatorname{rank}(d_2^{0,2}),
\qquad 0\le\operatorname{rank}(d_2^{0,2})\le45.
\]
Thus 10 is a rigorous lower bound, not yet an equality.

The next structural question is:
\[
\text{What is the forced survivor subquotient, and what H-action does it carry?}
\]
The decomposition
\[
H^2(W)=\Lambda^2W^*\oplus\beta_W(W^*)
\]
must be respected; the 9-dimensional fiber-Bockstein summand cannot be discarded.

## Consequences

The filtration-(2,0) relation-jet alone cannot account for the full \(\beta_\rho^2\) problem. The (2,1) sector contains a nonzero page-3 survivor before higher differentials are considered.

This does not prove that the survivor reaches E_\infty, and does not identify it with any previously known 10-dimensional module. Higher differentials remain a separate gate.

## Decision

- \(\dim W=9\): **PASS / CLOSED at q=3**.
- \(\dim H^2(V)=10,\dim H^4(V)=35\): **PASS / CLOSED**.
- rank/outgoing d_2^{2,1}=35: **PASS / CLOSED**.
- \(\dim\ker d_2^{2,1}=55\): **PASS / CLOSED**.
- \(\dim E_2^{0,2}=45\): **PASS / CLOSED**.
- \(E_3^{2,1}\neq0\): **PASS / CLOSED**.
- \(\dim E_3^{2,1}\ge10\): **PASS / CLOSED**.
- exact dimension / structure of E_3^{2,1}: **OPEN / LOAD-BEARING**.
- survival to E_\infty: **OPEN**.
- full \(\beta_\rho^2\): **OPEN / LOAD-BEARING**.
- unique coker maximizer without PD²: **OPEN / DECISIVE**.

## Next authorized attack

Compute
\[
d_2:H^2(W,\mathbf F_3)\to H^2(V,\mathbf F_3)\otimes W^*
\]
structurally, separating \(\Lambda^2W^*\) and \(\beta_W(W^*)\), and identify the resulting quotient as an H-module if possible.

Do not assume rank 45, do not assume a 10-dimensional answer, and do not perform a rho-scan.
