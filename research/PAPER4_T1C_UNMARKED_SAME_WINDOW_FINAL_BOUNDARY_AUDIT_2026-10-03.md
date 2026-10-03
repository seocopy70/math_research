# PAPER 4 — T1-C UNMARKED SAME-WINDOW FINAL BOUNDARY AUDIT — 2026-10-03

## 1. Target

The relative theorem concerns the marked finite extension
\[
E_n(G)=\bigl(W_n(G)\xrightarrow{\pi_n}Q_n=D/D_n(D)\bigr).
\]
The intrinsic target would be a function of the unmarked filtered finite group \(W_n(G)\) alone.

The only legitimate negative test is therefore a same-window separation:
two admissible marked diagrams with isomorphic underlying \(W_n\) but different relative obstruction values.

## 2. Result of the separation test

No valid same-underlying-window pair with different relative extension class has been established.

The previously closed Gate-D orientation example does not transfer: it concerns two orientations on the same underlying specially oriented RAAG, whereas the present target is the splitting class of a quotient extension. Changing a quotient map by postcomposition with an automorphism of \(Q_n\) preserves split/non-split, so that trivial re-marking does not separate the target.

Likewise, the stress-family pair \(G_{s,a},G_{t,a}\) with \(t>s\) is not a same-window pair at the critical depth: the relative theorem precisely detects a finite-layer difference there. At depths \(n\le p^s\), the stress-family windows agree, but their relative extension class is also split in the established threshold theorem, so this gives no unmarked no-go.

Therefore the unmarked factorization problem remains genuinely OPEN.

## 3. Important positive observation

The obstruction need not be non-intrinsic merely because the proof uses a chosen map \(\pi_n\). A marked map can be intrinsically reconstructible from the unmarked finite group in a restricted category.

Thus:
\[
\text{“relative proof”}\not\Rightarrow\text{“non-intrinsic target”}.
\]

Conversely:
\[
\text{“same underlying group not yet separated”}\not\Rightarrow\text{“intrinsic recovery exists”}.
\]

No conclusion in either direction is authorized.

## 4. What is now definitively closed

The following are not legitimate next moves:

- recomputing \(p^s+1\);
- reopening degree 5;
- reopening the scalar/coinvariant or standalone norm shortcuts;
- declaring the relative theorem to be an unmarked intrinsic theorem;
- inventing a carrier that simply stores \(\pi_n\).

## 5. Correct remaining theorem

The precise remaining question is:

> For the declared stress family, is the relative extension diagram \(W_n(G_{s,a})\to D/D_n(D)\) canonically reconstructible from the abstract filtered group \(W_n(G_{s,a})\) at \(n=p^s+1\), or is there an admissible same-window pair with different relative obstruction data?

This is the exact D1/functoriality boundary after T1-C.

## 6. Classification

- relative threshold \(n_{\rm sep}^{rel}(s)=p^s+1\): **PASS / CLOSED** for the declared stress family, based on the integral Fox divisibility + finite-kernel survival argument recorded in the T1-C audit;
- unmarked same-window no-go: **OPEN**;
- canonical reconstruction of the marked quotient map: **OPEN / LOAD-BEARING**;
- intrinsic finite-window factorization: **OPEN / LOAD-BEARING**;
- coarsest intrinsic realization: **OPEN**;
- universal free-by-Demushkin theorem: **OPEN**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

## 7. Final frontier

The mathematical frontier is no longer a threshold calculation. It is a reconstruction/separation problem:
\[
W_{p^s+1}(G_{s,a})
\quad\stackrel{?}{\longrightarrow}\quad
\bigl(W_{p^s+1}(G_{s,a})\to D/D_{p^s+1}(D)\bigr)
\quad\longrightarrow\quad
[\text{extension class}].
\]

Any next computation must first specify which of these two alternatives it attacks:

1. **Reconstruction:** prove \(\pi_n\) is canonical from \(W_n\);
2. **Separation:** construct two admissible markings on isomorphic \(W_n\) with different extension data.

Until one is achieved, there is no justified coarsest intrinsic carrier theorem.
