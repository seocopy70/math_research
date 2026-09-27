# Paper 3 — Carrier vs Target Separation Gate
Date: 2026-09-27
Status: **OPEN / LOAD-BEARING**

## Structural correction

A same-target comparison
\[
f_T=\min\{n:T\text{ factors through }W_n\},
\qquad
r_T=\min\{n:W_n\text{ determines }T\}
\]
is definitionally the same information condition at category level. Therefore a theorem asserting a numerical inequality \(f_T\ne r_T\) for the same target is not a meaningful separation theorem.

The correct separation architecture is
\[
O\xrightarrow{\Phi}T,
\]
where O is a richer finite carrier/observation and T is a genuinely coarser global target. The meaningful comparison is
\[
f_O \quad\text{versus}\quad r_T.
\]

## Consequence for T_beta

The computation
\[
f_{T_\beta}=r_{T_\beta}=p+1
\]
is retained as a consistency check, but it is not a separation result. Once the carrier is literally T_beta, equality is forced by the definitions.

The T_beta branch is therefore **CLOSED** as a separation candidate.

## Candidate screen

### Candidate A — affine/Kummer carrier O_k → coarser Bockstein target T_beta

Take O_k to be the finite affine/Kummer carrier from the established Paper 2 factorization theorem, with
\[
f_{O_k}=p^{k-1}+1
\]
in the declared affine crossed-cocycle category. For k>=2, the Bockstein target is a coarser consequence of the mod-p^k orientation/Kummer data.

For k=3 and p=3, the affine carrier has depth 10, while the independently established Bockstein recognition threshold is 4.

This gives a **control example of carrier-vs-target separation**, but it is not yet a new theorem: the gap is created by deliberately compressing a richer carrier to a coarser target. Its mathematical value is to validate the corrected architecture, not to support a novelty claim.

### Candidate B — higher Bockstein-extension carrier

The previously proposed mod-27 coefficient-extension carrier
\[
\mathcal B_{27}
=
(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9)
\]
remains a possible richer carrier. It is functorial and coordinate-free, but its exact factorization depth and a genuinely coarser target map are not yet established.

Status: **OPEN / CANDIDATE**, no computation authorized yet.

### Candidate C — multi-parameter category

Expand from fixed-rank Demushkin groups to a precisely declared class such as finite free pro-p products of Demushkin blocks. Then compare a blockwise carrier with aggregate targets (for example, a multiset/count of blockwise invariants).

This may avoid the one-parameter collapse of the fixed-rank Demushkin category, but the target must pass the same non-redundancy and prior-art gates.

Status: **OPEN / CANDIDATE**, deferred until Candidate A is formally recorded as the control case and Candidate B is screened.

## Decision

- same-target \(f_T\) vs \(r_T\): **INVALID / CLOSED — definitional identity**
- T_beta as separation target: **FAIL / CLOSED**
- affine carrier → Bockstein target: **PASS / CONTROL, NOT NOVELTY**
- higher Bockstein-extension carrier: **OPEN / STRONG CANDIDATE**
- multi-parameter category: **OPEN / SECONDARY CANDIDATE**

## Next authorized action

Do **not** launch another large computation.

First perform a line-by-line non-redundancy/prior-art audit of Candidate B, the mod-27 Bockstein-extension carrier, and determine:

1. its exact object and morphisms;
2. whether it genuinely contains more information than T_beta;
3. a canonical compression \(\Phi(\mathcal B_{27})=T\);
4. an upper factorization bound;
5. an independent lower recognition bound for T;
6. whether the resulting gap is structural rather than merely a chosen over-rich encoding.

Only if Candidate B survives this gate should computation begin.
