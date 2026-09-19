# HARD ATTACK 12 — FULL FILTERED EXTENSION DATA VS ASSOCIATED GRADED DATA — 2026-09-20

## Target

The remaining structural bottleneck is
\[
\text{intrinsic filtered relation tower}\longrightarrow\text{exact Fox obstruction tower}.
\]
Before attempting a theorem, distinguish two very different meanings of “full filtered tower”.

## 1. Associated graded data is not the same as a compatible filtered lift

The mod-3 Zassenhaus object records successive quotients
\[
G_n/G_{n+1}
\]
and their restricted-Lie operations. Such associated graded data records initial forms. It does not, by itself, specify the extension/gluing data required to reconstruct an actual element of the completed filtered group.

This is exactly the distinction already exposed by the integral-augmentation failure and the Nielsen failure of naive degree-3 Fox truncation.

For the Demuškin family
\[
r_q=x_1^q[x_1,x_2][x_3,x_4],
\qquad q=3^s,
\]
the power term first occurs in Zassenhaus degree $3^s$. Hence every fixed finite graded window below degree $3^s$ agrees with the power-free control, while the exact orientation already differs:
\[
\chi_{3^s}(x_2)=(1-3^s)^{-1}\neq1.
\]
This gives the finite-window obstruction in a presentation-independent conceptual form.

Decision: **FAIL / CLOSED** for any claim that a fixed finite associated-graded window determines the full $3$-adic orientation.

## 2. Stronger observation: if “full filtered tower” means actual compatible filtered quotients, it can reconstruct the relator

For a complete separated pro-$3$ filtration, an actual compatible system of residues
\[
r_n\in F/F_n
\]
determines a unique element
\[
r\in\varprojlim_n F/F_n\cong F.
\]
The Zassenhaus filtration of a free pro-$p$ group is the standard complete filtered structure, and the completed Fox calculus is continuous on the corresponding completed group algebra.

Therefore, if the proposed $J_n$ literally retains the compatible filtered residue of the relation element (together with enough structure to apply the Fox boundary), then the exact Fox row can be recovered by continuity:
\[
(r_n)_n\longmapsto r\longmapsto [J_r].
\]

This is mathematically legitimate, but it exposes a novelty boundary: such a $J_n$ is no longer a finite graded compression. It is essentially the completed filtered relation itself, and the factorization through Fox is close to formal once the boundary/Fox map is included as part of the functorial structure.

Decision: **PASS / LOCAL** for the formal completeness implication; **NOT YET A NEW THEOREM** as a compressed intrinsic carrier.

## 3. The decisive distinction

There are therefore only two viable interpretations:

### A. Graded tower
\[
\{\operatorname{gr}_n(R)\}_{n\ge1}.
\]
This loses extension data. No theorem currently shows it determines the exact Fox coefficient tower, and finite-window obstructions show why bounded truncations cannot.

### B. Filtered extension tower
\[
\{R/F_nR\}_n
\quad\text{with compatible transition maps and intrinsic boundary structure}.
\]
This can reconstruct the completed relation by inverse limit. The remaining nontrivial issue is then not existence of the limit but whether the resulting object is canonical under presentation/gauge changes and whether the Fox boundary is an independently defined natural transformation rather than imported by definition.

The project must not call A and B the same object.

## 4. Consequence for the research question

The genuine target is now sharper:
\[
\boxed{
\text{Can one define a proper intermediate object }J^{\mathrm{mid}}
\text{ that retains enough extension data for exact Fox reconstruction,}
\newline
\text{but is strictly smaller than the full completed Fox/presentation object?}
}
\]

A successful $J^{\mathrm{mid}}$ must satisfy simultaneously:
1. q-blind definition;
2. presentation/gauge functoriality;
3. no candidate-$\chi$ input;
4. enough extension data to determine all $3$-adic digits;
5. a non-circular natural map to the exact Fox obstruction;
6. a genuine information reduction relative to the full completed relator.

If no such object exists, the correct endpoint is a sharp impossibility theorem: **full $3$-adic orientation requires characteristic-zero extension data beyond the bare associated graded relation object.**

## Decision

**STRUCTURAL BOUNDARY SHARPENED.**

- finite/bounded associated-graded carrier → full $\chi$: **FAIL / CLOSED**;
- full compatible filtered extension data → exact relation/Fox object: **PASS / LOCAL**, essentially by completeness/continuity;
- nontrivial intermediate intrinsic compression: **OPEN** and is now the only remaining substantive carrier question.

Record: this audit.
