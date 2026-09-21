# Literature novelty audit — Pál–Quick / Blumer–Quadrelli — 2026-09-21

## Purpose

This record audits three newly added papers against the surviving research question:

\[
\text{intrinsic Zassenhaus/Jennings–Lazard filtered input}
\longrightarrow
\chi_G \bmod 3^k
\]

and, more specifically, whether a finite-window recognition theorem on

\[
Q_k=G/P_{k+1}(G)
\]

is already present in the literature.

The audit is a novelty comparison, not a claim that the present project has publication-level novelty.

---

## 1. Pál–Quick, arXiv:2601.07551v2

**A_3-formality for Demushkin groups at odd primes**, Ambrus Pál and Gereon Quick.

The paper studies the continuous-cochain differential graded \(\mathbf F_p\)-algebra of a pro-p Demushkin group. For odd p it proves A_3-formality when the q-invariant is not 3 and failure of A_3-formality when q=3, by explicit computation of the Benson–Krause–Schwede canonical class in Hochschild cohomology.

### Relevance

This is a strong independent precedent that higher cohomological structure can detect the q=3 layer.

### Exact logical boundary

Its input is the continuous cochain DGA and its Hochschild/cohomological structure. It is therefore **not** a theorem that the intrinsic Zassenhaus/Jennings–Lazard filtered group, its finite quotient \(G/P_{k+1}\), or its graded restricted Lie algebra alone canonically reconstructs \(\chi\bmod 3^k\).

Therefore:

- higher cohomological detection of q=3: **FAIL / CLOSED as novelty**;
- filtration-only reconstruction: **not closed by this paper**;
- equality/factorization between the project’s relation-jet/Bockstein carrier and the Pál–Quick BKS class: **OPEN**.

Important caution: this paper prevents the overstatement that “higher structure cannot see q”. It demonstrably can.

Source: arXiv:2601.07551. citeturn0academia0

---

## 2. Blumer–Quadrelli, arXiv:2603.15464v2

**Variations of Demushkin Groups that are not Absolute Galois Groups**, Simone Blumer and Claudio Quadrelli.

The paper constructs families of pro-p groups with elementary presentations that fail to become 1-cyclotomic oriented pro-p groups, and studies their relation to properties expected of maximal pro-p Galois groups. The project-source audit also confirms explicit use of the p-Zassenhaus filtration, its associated graded restricted Lie algebra, completed group algebra/Jennings machinery, and canonical orientation language.

### Relevance

This paper establishes that the combination

\[
\text{Demuškin groups + p-Zassenhaus filtration + graded restricted Lie algebra + cyclotomic/oriented structure}
\]

is already present in the literature.

### Exact logical boundary

The paper does **not**, in the audited material, state the stronger factorization

\[
\operatorname{Fil}_{\mathrm{intr}}(G)\longrightarrow\chi_G
\]

with the orientation excluded from the input and reconstructed from the filtered object itself.

Nor does the audited material supply the specific finite-window theorem

\[
G/P_{k+1}(G)\longrightarrow \chi_G\bmod 3^k
\]

as a q-blind, presentation-independent recognition predicate of the type being developed here.

Therefore:

- Demuškin + Zassenhaus/graded methods as a general methodological combination: **FAIL / CLOSED as novelty**;
- intrinsic filtered-input → orientation factorization: **OPEN**;
- finite-window recognition on \(G/P_{k+1}\): **OPEN / LITERATURE VERIFICATION REQUIRED**.

Source: arXiv:2603.15464. citeturn0academia1

---

## 3. Pál–Quick, arXiv:2607.01028v2

**A_3-formality for pro-2 Demushkin groups**, Ambrus Pál and Gereon Quick.

The paper proves that continuous cochain DGAs of all pro-2 Demushkin groups are A_3-formal, using an explicit computation of the BKS canonical class and interpreting its data through higher Massey-product defining systems.

### Relevance

This is less directly connected to the present p=3 filtration problem, but it is methodologically relevant: the same Demuškin classification/orientation background can support prime-dependent higher cohomological invariants.

### Exact logical boundary

It does not provide the desired p=3 filtration-only or finite-window reconstruction theorem.

Therefore:

- independent precedent for higher cohomological analysis of Demuškin groups: **FAIL / CLOSED as novelty**;
- relevance to the p=3 filtered finite-window problem: **background/methodological only**;
- direct closure of the present factorization question: **NO**.

Source: arXiv:2607.01028. citeturn0academia2

---

## 4. Consolidated novelty boundary

| Claim | Status after this audit |
|---|---|
| Canonical Demuškin orientation exists | **FAIL / CLOSED as novelty** |
| Canonical orientation is unique | **FAIL / CLOSED as novelty** |
| Demuškin + Zassenhaus/graded Lie methods are new | **FAIL / CLOSED** |
| Higher cohomological structure can detect q=3 | **FAIL / CLOSED** |
| BKS/Hochschild invariant = the project's filtered relation-jet carrier | **OPEN** |
| Full intrinsic Zassenhaus graded object directly recovers \(\chi\) | **OPEN / current negative evidence says bare graded object is q-blind** |
| \(G/P_{k+1}\) alone gives a natural q-blind recognition predicate for \(\chi\bmod3^k\) | **OPEN / LITERATURE VERIFICATION REQUIRED** |
| Existing Kummerian/oriented quotient-inheritance results already imply the exact finite-window theorem | **OPEN / must compare hypotheses line-by-line** |
| Overall novelty | **OPEN / CONDITIONAL** |

### Current interpretation

The project must **not** be described as discovering canonical Demuškin orientation.

If a theorem is eventually proved, the candidate contribution is narrower:

> an intrinsic filtered/finite-window factorization or recognition theorem for the already-known canonical orientation, with the orientation and q-invariant excluded from the defining input.

The key unresolved novelty gate is therefore not “is the orientation known?” but:

\[
\boxed{
\text{Is the finite, q-blind, presentation-independent recognition map on }G/P_{k+1}
\text{ already known?}
}
\]

and, separately, whether the project's intrinsic obstruction carrier is genuinely different from an existing Kummerian/oriented formulation.

---

## 5. Next authorized comparison

Before claiming novelty, compare line-by-line:

1. the project's finite-window Kummer predicate on \(Q_k=G/P_{k+1}\);
2. finite-coefficient Kummerian/oriented quotient-inheritance theorems;
3. the exact role of \(K_{\theta}\), \(K_{\theta\bmod3^k}\), or equivalent kernels;
4. whether those theorems assume an already-given orientation;
5. whether the project constructs the finite coefficient character without inserting \(\chi\), q, or the dualizing action;
6. whether the resulting statement is genuinely a factorization theorem rather than a reformulation of Serre's classical orientation criterion.

No broader novelty claim is authorized until this comparison is completed.

## Classification

**LITERATURE NOVELTY AUDIT = PASS / LOCAL.**

It closes several broad novelty claims but does not close the surviving finite-window factorization novelty gate.
