# HARD ATTACK 7 — NIELSEN STRESS TEST OF THE FOX CARRIER — 2026-09-19

## Purpose

The previous audit identified a decisive logical gap: Fox calculus gives the evaluated row and its kernel, but does not by itself prove that the canonical Demuškin orientation is characterized by vanishing of the entire row. Before returning to the filtered-to-character bridge, we stress-tested the exact Fox row under nontrivial Nielsen-equivalent presentations.

## Base presentation

\[
G=\langle x_1,x_2,x_3,x_4\mid
r=x_1^3[x_1,x_2][x_3,x_4]\rangle,
\qquad [a,b]=a^{-1}b^{-1}ab.
\]

For an abelian character torus \(\rho(x_i)=(A,B,C,D)\in(1+3\mathbf Z_3)^4\), the evaluated Fox row is
\[
J=(1+A+A^2B^{-1},\;A^2(A-1)B^{-1},\;
A^3C^{-1}(D^{-1}-1),\;A^3D^{-1}(1-C^{-1})).
\]

After multiplying components by units, its zero ideal is
\[
\langle B(1+A)+A^2,\;A-1,\;D-1,\;C-1\rangle.
\]
Thus the unique zero in the chosen \((1+3\mathbf Z_3)^4\) neighborhood is
\[
(1,-1/2,1,1).
\]

## Nielsen test A: \(x_1=y_1y_2^{-1},\;x_2=y_2\)

This is the nontrivial Nielsen move \(y_1=x_1x_2,\;y_2=x_2\).

Direct symbolic Fox differentiation after substitution gives
\[
J'_1=\frac{A^2+AB^2+B^3}{B^3},
\qquad
J'_2=-\frac{A(AB+A+B^2)}{B^3},
\]
\[
J'_3=-\frac{A^3(D-1)}{B^3CD},
\qquad
J'_4=\frac{A^3(C-1)}{B^3CD}.
\]

Hence row-zero is equivalent to
\[
A^2+AB^2+B^3=0,\quad AB+A+B^2=0,\quad C=D=1.
\]
Eliminating \(A\) gives
\[
A=-\frac{B^2}{B+1},
\qquad
\frac{B^3(2B+1)}{(B+1)^2}=0,
\]
so
\[
A=B=-1/2,qquad C=D=1.
\]

The character-coordinate transport is exact: \(x_1=y_1y_2^{-1}\) and \(x_2=y_2\) imply
\[
\rho(y_1)=\rho(x_1)\rho(x_2),\qquad
\rho(y_2)=\rho(x_2),
\]
so the old point \((1,-1/2,1,1)\) becomes \((-1/2,-1/2,1,1)\).

The Fox chain rule was checked symbolically. With old variables replaced by \((A/B,B,C,D)\),
\[
K=
\begin{pmatrix}
1&-A/B&0&0\\
0&1&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},
\]
and
\[
J'=J(A/B,B,C,D)K.
\]
Since \(K\) is invertible on the torus, the row-zero locus is transported exactly.

## Nielsen test B: swap \(x_1,x_2\)

Set
\[
x_1=y_2,\qquad x_2=y_1,\qquad x_3=y_3,\quad x_4=y_4.
\]

Direct differentiation gives
\[
J''_1=\frac{B^2(B-1)}{A},
\qquad
J''_2=\frac{AB+A+B^2}{A},
\]
\[
J''_3=-\frac{B^3(D-1)}{CD},
\qquad
J''_4=\frac{B^3(C-1)}{CD}.
\]

The row-zero equations force
\[
B=1,\qquad 2A+1=0,\qquad C=D=1,
\]
hence
\[
(A,B,C,D)=(-1/2,1,1,1),
\]
again exactly the transported canonical point.

## What the stress test proves

The two genuinely nontrivial Nielsen tests PASS:

1. exact symbolic Fox covariance;
2. exact transport of the row-zero locus;
3. agreement with the known q=3 orientation after coordinate transport.

This is stronger than the earlier frozen-normal-form observation and does not require a representation-theoretic scan.

## Critical logical boundary

The stress test still does **not** prove
\[
\text{canonical Demuškin orientation}\iff J_r(\rho)=0
\]
for an arbitrary presentation.

In particular, \(\ker J_r(\rho)\neq0\) is not a useful replacement: a single row acting on a 4-dimensional coefficient space generically has a nonzero kernel everywhere. The earlier A/B/C distinction therefore remains essential:
\[
\ker J\neq0,\qquad a_{can}\in\ker J,\qquad J=0.
\]

The remaining load-bearing theorem is an identification theorem:
\[
\boxed{J_r(\rho)=0\iff\rho=\chi}
\]
or an intrinsic equivalent statement.

## Decision

- Nielsen covariance of the full evaluated Fox row: **PASS / CLOSED for the tested generators**; the general chain-rule mechanism is standard.
- Row-zero locus covariance under these moves: **PASS / CLOSED**.
- Agreement with the known q=3 orientation in the transformed presentations: **PASS / CLOSED**.
- Row-zero = canonical orientation in general: **OPEN**.
- Intrinsic filtered realization of the Fox carrier: **OPEN**.
- Kernel-locus as standalone criterion: **FAIL / CLOSED**.
- No representation scan authorized.

## Next decisive attack

Do not accumulate more presentation examples. Attack the identification theorem directly.

**Route A:** derive the Fox-row condition from the standard Demuškin duality/orientation axiom using the completed group-ring/Fox resolution. If the dualizing-module condition is exactly row vanishing, the main logical gap closes.

**Route B:** derive the already known mod-9 carrier \([(R,p(P_3))]\) as the filtered initial form of the exact Fox zero ideal. This would connect the exact characteristic-zero object back to the intrinsic filtered program.

Route A should be attempted first; Route B is then the structural comparison.

Fox derivatives are standard tools for encoding crossed-homomorphism constraints from a presentation, but that standard fact does not itself identify the Demuškin orientation with row vanishing. citeturn0search0turn0search1

## Bottom line

The Nielsen attack did not break the Fox construction. It strengthened it as an exact presentation-covariant comparison object.

The remaining weak point is now sharply isolated:

\[
\boxed{\text{covariance is supported; identification with the canonical orientation is the load-bearing OPEN theorem.}}
\]
