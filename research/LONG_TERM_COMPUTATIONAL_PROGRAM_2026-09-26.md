# LONG-TERM COMPUTATIONAL RESEARCH PROGRAM — 2026-09-26

## Purpose

This is the authoritative long-term research-program record downstream of the frozen main paper and the successor paper. It is updated whenever a successor result changes the executable research agenda.

The frozen publication manuscript remains protected. Long-term work must not modify the frozen paper unless a later explicit publication decision authorizes it.

## Governing research protocol

Every task follows:

**pre-check → define object/input → justify legitimacy → execute → independent verification → classify → record immediately.**

A computation is evidence, not automatically a theorem. In particular:

- reproducing the canonical Demuškin orientation is not by itself a novelty claim;
- presentation-specific calculations do not establish an intrinsic selector;
- a result for a restricted carrier/category must not be promoted to an absolute statement;
- CLOSED, OPEN, PASS/LOCAL, and CONDITIONAL statuses must be kept separate.

The current successor audit closes affine-category sharpness. It does **not** close absolute minimality over arbitrary carriers, nor unconditional publication priority.

---

# I. Current mathematical baseline — supersedes earlier duplicated task statements

## 1. Finite-window objects

For the standard Demuškin family

\[
G_f=\langle x_1,\ldots,x_d\mid
x_1^{p^f}[x_1,x_2][x_3,x_4]\cdots=1\rangle,
\]

with odd p, d≥2, and

\[
Q_k=G_f/P_{p^{k-1}+1}(G_f),
\]

the successor theory establishes the finite-window affine factorization depth

\[
n_{\rm aff}(k)=p^{k-1}+1.
\]

The relevant finite affine coefficient group is

\[
S_k=A_k\rtimes U_{1,k},\qquad A_k=\mathbf Z/p^k,
\]

with the affine crossed-cocycle representation \((\rho,z)\).

For the rank-4 p=3 instance used in the papers, the canonical orientation residues are

\[
\rho_2\equiv4\pmod9,\qquad
\rho_2\equiv13\pmod{27},\qquad
\rho_2\equiv40\pmod{81}.
\]

These are independently verified finite computations, not the conceptual source of the theorem.

## 2. Affine sharpness — CLOSED

The category-relative sharpness statement is now closed:

\[
n_{\rm aff}(k)=p^{k-1}+1
\]

is sharp for **all d≥2 and all f≥1**.

No surjectivity assumption on the orientation character is required.

The lower-bound witnesses split into two regimes:

- f<k: the canonical affine witness with z(x_1)=1 survives on x_1^{p^{k-1}};
- f≥k: the d=2 witness with \rho(x_2)=1+p and z(x_2)=1 survives on x_2^{p^{k-1}}, by LTE.

Thus the d=2 boundary is included, and no x_3 witness is needed.

**Status: PASS / CLOSED — affine crossed-cocycle factorization minimality.**

This does **not** prove absolute minimality for arbitrary information carriers.

## 3. q-collapse — CLOSED at the abstract finite-quotient level

For fixed k,

\[
f\ge k\quad\Longrightarrow\quad
Q_k^{(f)}\cong Q_k^{(\infty)},
\]

and the induced orientation information modulo p^k is the same.

Equivalently, the finite window becomes q-blind once f reaches the k-level threshold.

This is an information-loss/isomorphism statement. It does not imply that every possible marked, structured, or external carrier loses q-information.

**Status: PASS / CLOSED for the stated bare finite quotient statement.**

## 4. Selector impossibility boundary — CLOSED in the stated broad class

A uniform selector on the whole elementary-type class \mathcal{ET}_p cannot recover all orientations from the bare finite quotient.

In particular,

\[
G=\mathbf Z_p *_p \mathbf Z_p
\]

is a q-blind/free-product example for which the relevant finite Kummer predicate does not distinguish arbitrary orientations.

Therefore the correct statement is not “finite quotients always determine orientation”, but rather:

> finite-window recognition succeeds in the Demuškin/PD² affine setting, while a uniform isomorphism-natural selector on the whole \mathcal{ET}_p class is impossible.

**Status: PASS / CLOSED for the stated q-blindness/impossibility boundary.**

## 5. Finite Demuškin free products — CLOSED for the current affine window

For

\[
D_1 *_p\cdots *_p D_r,
\]

where the D_i are finite Demuškin blocks in the class treated by the successor work, the same affine window

\[
p^{k-1}+1
\]

is uniform.

This is a genuine extension of the single-block sharpness phenomenon, but it does not yet close the recursively generated elementary-type class

\[
\mathcal{ET}_p^{\rm rig}
=
\lim_{\to}(-*_p-,-\rtimes\mathbf Z_p).
\]

**Status: PASS / CLOSED for finite Demuškin block free products; OPEN for the recursive class.**

---

# II. Updated long-term research directions

The old four-task list is superseded by the following application-oriented program. The ordering below reflects current mathematical readiness, not a claim about importance.

## Priority A — Finite local-anabelian decision procedure

### Question

For concrete p-adic fields K whose maximal pro-p Galois group is Demuškin, can the finite quotient

\[
Q_k=G_K(p)/P_{p^{k-1}+1}
\]

be used as a practical finite-level test for the canonical cyclotomic orientation modulo p^k?

A useful comparison problem is:

> Given two independently specified local fields K_1,K_2 with validated Demuškin presentations and abstractly isomorphic finite quotients Q_k^{(1)}≅Q_k^{(2)}, what additional naturality/identification data are required before one may conclude that their canonical orientations agree modulo p^k?

### What is already available

- the affine finite-window theorem;
- the exact sharp depth;
- the q-collapse boundary;
- an explicit reconstruction formula in the standard family;
- Newton-style recovery of the relevant p-adic residue in the standard parameterization.

### What remains to prove

The finite-window theorem does **not** by itself prove that an arbitrary abstract isomorphism of Q_k's canonically transports the orientation. The successor audit explicitly leaves the statement

> “bare abstract Q_k determines the canonical orientation without naturality/functoriality hypotheses”

unestablished.

Therefore the implementation must keep three inputs separate:

1. the abstract finite group Q_k;
2. the natural map from G_K(p) to Q_k;
3. any identification/presentation data used to interpret the recovered character.

The case \mu_p\not\subset K, where the maximal pro-p Galois group is free rather than Demuškin in the relevant setting, is a useful contrast, but it must be formulated carefully and checked against the exact local-field hypotheses.

### First concrete experiments

- p=3,5;
- small k;
- low-rank local examples;
- independently validate the G_K(p) presentation and orientation convention before constructing Q_k.

### Deliverable

A reproducible finite-level recognition prototype and a table separating:

- quotient isomorphism;
- candidate orientation;
- recovered residue;
- naturality assumptions;
- what information is lost.

**Status: OPEN / HIGH PRIORITY.**

---

## Priority B — Finite Kummerianity test for Demuškin free products

### Question

Can Kummerianity/1-cyclotomicity be tested using only finite data for the closed class

\[
D_1 *_p\cdots *_p D_r?
\]

The proposed finite test uses the successor finite quotient together with the twisted lifting equations and Jacobian/non-singularity data.

### Mathematical route

For a candidate orientation \rho, work with

\[
\mathsf K_k(Q_k,\rho):
H^1(Q_k,\mathbf Z/p^k(\rho))
\longrightarrow H^1(Q_k,\mathbf F_p)
\]

and the corresponding finite crossed-cocycle system.

The implementation should test:

1. construction of Q_k;
2. candidate orientations;
3. solvability of the finite lifting equations;
4. uniqueness;
5. compatibility across k;
6. agreement with independently known Kummerianity.

The relationship to the quotient-inheritance literature must be stated precisely: the finite-window result is not simply a restatement of quotient inheritance, because the successor theorem supplies the specific affine factorization depth and removes the need to assume the quotient property as an input.

### Deliverable

A prototype decision procedure plus a theorem/conjecture boundary:

- **proved** for the currently closed finite Demuškin block-product class;
- **experimental** for broader elementary-type groups.

**Status: OPEN / HIGH PRIORITY.**

---

## Priority D — Zassenhaus dimension and free-product combinatorics

### Question

Can the sharp-window Zassenhaus calculations be turned into explicit dimension formulas for finite free products of Demuškin blocks?

The starting mechanism is the established power-term valuation:

\[
x_1^{p^f}\in P_{p^f}\setminus P_{p^f+1},
\]

combined with the free-pro-p product behavior of the Zassenhaus filtration.

### Target

Derive explicit formulas for the dimensions of relevant filtration quotients in

\[
D_1 *_p\cdots *_p D_r,
\]

and compare them with existing dimension calculations for pro-p groups.

The recursive \mathcal{ET}_p^{\rm rig} extension remains OPEN and should not be assumed.

### Deliverable

A formula, proof, and small-parameter computational verification.

**Status: OPEN / MEDIUM-HIGH PRIORITY.**

---

## Priority C — Massey products and A_3-formality

### Question

Can the finite-window equations be interpreted precisely in terms of Massey products, canonical Hochschild classes, or A_3-formality?

The attractive heuristic is that the relation equations and their twisted coefficient terms encode higher cohomological information. However, the exact identification

\[
F_i=0\quad\Longleftrightarrow\quad A_3\text{-formality}
\]

must **not** be treated as established merely from the current computations.

### Required work

- verify the exact definitions and hypotheses in the 2026 Pál–Quick literature;
- identify which finite obstruction is genuinely represented by F_i;
- distinguish q-detection from finite-window orientation recognition;
- test the q-collapse regime f≥k to determine exactly which higher operation becomes invisible at the finite level.

### Potential result

A precise example of an A_3/A_\infty obstruction that is not recoverable from the bare finite window, or a positive finite-level criterion under additional structure.

**Status: OPEN / EXPLORATORY.**

---

# III. Broader speculative programs — retained, but explicitly not current theorems

## 1. p-adic holography / information-theoretic translation

The current mathematics supports only a structural analogy, not a physical result.

A genuine p-adic holography program would need, at minimum:

1. a specified bulk object such as a Bruhat–Tits tree;
2. a precisely defined boundary state/function space;
3. a gauge action realizing the Demuškin group;
4. an observable whose finite-depth restriction corresponds to Q_k;
5. a correlation-function calculation showing actual indistinguishability in the q-collapse regime.

The group isomorphism

\[
Q_k^{(f)}\cong Q_k^{(\infty)}
\]

alone is not a holographic correlation-function result.

**Status: OPEN / SPECULATIVE.**

## 2. p-adic coding-theory translation

A possible route is to interpret the relation as a parity-check constraint over A_k and study what information survives a p^{k-1}+1 local view.

To become a mathematical coding-theory result, the program must define:

- the code;
- alphabet and rate;
- parity-check/Tanner structure;
- decoding or local-testability notion;
- the exact information-loss statistic;
- a theorem connecting q-collapse to that statistic.

The current finite-window theorem is not itself a coding theorem.

**Status: OPEN / SPECULATIVE.**

## 3. Langlands / deformation-theoretic extension

The current result is genuinely at the one-dimensional orientation/determinant level. A GL(2) extension would require new deformation theory.

A concrete target is to compare the deformation functors/rings of a finite quotient and the full Galois group at the k-th infinitesimal level, rather than merely observing that the determinant/cyclotomic character is fixed modulo p^k.

Potential tasks:

- formulate the precise deformation functors;
- determine the map between finite-quotient and full-group deformation rings;
- test whether the finite window controls a k-th infinitesimal neighborhood;
- only then investigate modularity-lifting analogies.

The free-product/q-blindness analogy with L-parameters is presently conceptual, not a theorem.

**Status: OPEN / SPECULATIVE.**

---

# IV. Current priority order

The previous experimental order is superseded.

### 1. A — finite local-anabelian recognition prototype
Closest to the established theorem, but must resolve naturality/input boundaries.

### 2. B — finite Kummerianity decision procedure
Natural algorithmic continuation of the closed finite Demuškin/free-product result.

### 3. D — Zassenhaus dimension formulas
A comparatively safe pure-combinatorial extension with a clear proof target.

### 4. C — Massey/A_3-formality
Potentially deep, but dependent on a precise literature-level identification of the finite obstruction.

### 5. p-adic coding / holography
Keep as a structured research memo until a genuine observable/information-theoretic formulation exists.

### 6. Langlands / GL(2) deformation
Long-range program requiring substantial new deformation-theoretic input.

---

# V. Explicit CLOSED / OPEN ledger

## CLOSED

- \(n_{\rm aff}(k)=p^{k-1}+1\) is sharp for every odd p, every f≥1, and every d≥2 in the affine crossed-cocycle factorization category.
- The d=2 f≥k lower-bound witness is valid.
- q-collapse \(f\ge k\Rightarrow Q_k^{(f)}\cong Q_k^{(\infty)}\) for the stated family.
- The corresponding orientation information modulo p^k is unchanged in that collapse.
- Uniform bare finite-window recognition cannot hold on the whole \mathcal{ET}_p class.
- The finite Demuškin block free-product class has the same sharp affine window.

## OPEN

- absolute minimality over an arbitrary, explicitly defined carrier category;
- recursive \mathcal{ET}_p^{\rm rig} closure;
- naturality/functoriality conditions under abstract Q_k isomorphism;
- concrete local-field implementation;
- finite Kummerianity decision algorithm beyond the already closed theorem class;
- Zassenhaus dimension formulas for Demuškin block free products;
- precise Massey/A_3-formality interpretation;
- physical/information-theoretic translations;
- GL(2) deformation/Langlands extensions.

## CONDITIONAL / NON-NOVELTY BOUNDARY

The following are classical or imported and must not be presented as new:

- existence/uniqueness of the canonical Demuškin orientation;
- Kummerianity / 1-cyclotomicity itself;
- standard oriented elementary-type closure results.

The defensible successor novelty boundary remains:

1. finite quotient use in the present affine twisted-obstruction factorization;
2. exact sharp depth \(p^{k-1}+1\) for all affine crossed-cocycle representations in the stated Demuškin family.

Publication priority remains **CONDITIONAL**, because literature search cannot logically establish the absence of an equivalent formulation.

---

# VI. Operational rule for future work

When a new result is obtained:

1. update this file first if it changes the long-term program;
2. supersede, rather than duplicate, older task statements;
3. record the mathematical classification separately from implementation status;
4. never promote a prototype or numerical confirmation to a theorem without a proof gate;
5. preserve the frozen main-paper record and all prior CLOSED results.

**Current long-term program status: OPEN / AUTHORIZED FOR STAGED IMPLEMENTATION.**

The next authorized research action is Priority A, subject to its pre-check and naturality boundary.
