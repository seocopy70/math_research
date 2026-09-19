# Q3/Q9 S9 target-side orbit span — 2026-09-19

## Status

**PASS — target-side orbit span computed structurally.**

This is downstream of the closed source-map definition gate. It does not redefine the q=9 relation space.

## 1. Target

\[
Q_9^\infty=L_9^{res}/(I_\infty)_9.
\]

The target H-action is well-defined by the preceding target-action audit.

## 2. Source class

\[
\phi_9(S_9)=[S_9],\qquad S_9=X_1^{[9]}.
\]

S9-B gives
\[
(I_\infty)_9\cap L_1^{[9]}=0.
\]
Therefore the quotient map restricted to \(L_1^{[9]}\) is injective.

## 3. Orbit calculation

The closed C3.1 computation established, in the ambient p-layer,
\[
\langle H\cdot S_9\rangle=L_1^{[9]},
\qquad
\dim L_1^{[9]}=4.
\]

Because the quotient map is injective on \(L_1^{[9]}\), its image preserves the orbit-span dimension. Hence
\[
\boxed{
\mathcal O_9:=\langle H\cdot[S_9]\rangle
\cong L_1^{[9]},
\qquad
\dim\mathcal O_9=4.
}
\]

Equivalently, the target-side orbit is exactly the image of the natural 4-dimensional p-layer \(L_1^{[9]}\) inside \(Q_9^\infty\).

## 4. What this does and does not show

It shows that the presentation-derived class \([S_9]\) generates a 4-dimensional H-stable submodule of the frozen q=∞ baseline quotient.

It does **not** show that this 4-dimensional module is a canonical q-invariant, nor that q=3 and q=∞ are distinguished by it. In particular, no orientation character is recovered.

The earlier q=9 relation-space H-stability FAIL remains unchanged. \(\mathcal O_9\) is a quotient-side orbit object, not an H-closure of q=9 relations.

## Decision

\[
\boxed{\dim\mathcal O_9=4\quad\text{and}\quad\mathcal O_9\cong L_1^{[9]}.}
\]

The next gate must ask whether this target-side module supplies a legitimate q=3/q=∞ comparison or whether it is merely the natural p-layer shadow of the source.
