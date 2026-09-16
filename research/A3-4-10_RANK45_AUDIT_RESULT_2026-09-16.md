# A3-4-10 Rank-45 Audit and Canonical Tau Distinction — 2026-09-16

## 1. Why the audit was run

The previous A3-4-10 computation reported bracket-obstruction rank 45. Separately, the quotient-induced canonical correspondence

\[
\tau=(\pi|_{W_d})^{-1}\circ(\pi|_{W_{45}})
\]

was verified to fix the 35-dimensional intersection \(I=W_{45}\cap W_d\). Since \(\dim W_{45}=45\), this implies \(\operatorname{rank}(\tau-I)\le 10\). Therefore a rank-45 obstruction could not arise from the naive formula

\[
[\tau(w)-w,X_i].
\]

The purpose of this audit was to identify the source of the apparent contradiction.

## 2. Audit result

The audit of the exact A3-4-10 implementation found:

- \(\dim W_{45}=45\)
- \(\dim W_d=45\)
- \(\dim I=35\)
- the A3-4-10 affine H-intertwiner \(X\) has
  \[
  \operatorname{rank}(X-I)=45,
  \qquad \ker(X-I)=0.
  \]
- \(X\) does **not** fix \(I\):
  \[
  \operatorname{rank}((X-I)|_I)=35.
  \]
- the A3-4-10 obstruction matrix \(D\) is exactly the degree-5 ambient bracket applied to \((X-I)\):
  \[
  D=\operatorname{Bracket}(X-I),
  \]
  with rank 45.

Thus the rank-45 calculation itself is internally consistent. The error was interpretive: the A3-4-10 affine H-intertwiner \(X\) is not the same map as the canonical quotient-induced \(\tau\).

## 3. Why X and tau must be distinguished

A3-4-10 constructs \(X\) by solving the H-intertwining equations together with the affine condition sending the chosen 35-dimensional subspace to the corresponding \(K\)-subspace. The constrained system has 2025 unknowns and rank 2024, leaving a one-dimensional solution family.

By contrast, the canonical quotient-induced \(\tau\) is fixed directly by the quotient coordinates. Its restriction to \(I\) is the identity.

Therefore the earlier phrase “the verified intertwiner” was too ambiguous. From now on:

- \(X\) = an affine H-module intertwiner selected by the A3-4-10 linear system;
- \(\tau\) = the canonical quotient-induced correspondence.

The old rank-45 obstruction is a statement about \(X\), not yet about canonical \(\tau\).

## 4. Correct next experiment

A new computation was added:

`research/A3-4-10_CANONICAL_TAU_REVALIDATION_2026-09-16.py`

It reconstructs \(\tau\) from the true recursive relation space \(\dim(R)_4=15\), verifies:

\[
\operatorname{rank}(\tau-I)\le10,
\qquad
(\tau-I)|_I=0,
\]

and then computes the genuine canonical degree-5 bracket discrepancy

\[
\Delta_\tau(w,X_i)=[\tau(w)-w,X_i].
\]

This is the computation that must replace the old rank-45 interpretation before any \(q=\infty\) comparison is attempted.

## 5. Current status

The q-specific interpretation is intentionally **not** claimed yet. The control experiment with the internal H-automorphism \(u=I+N\) already showed that zero intersection with true \((R)_5\) is not by itself q-specific. The present audit adds a more fundamental correction: the previously measured rank 45 belonged to a noncanonical affine H-intertwiner \(X\), not to the canonical quotient correspondence \(\tau\).

Next target: run the canonical-\(\tau\) revalidation and only then reassess A3-4-11 and the need for a \(q=\infty\) control.
