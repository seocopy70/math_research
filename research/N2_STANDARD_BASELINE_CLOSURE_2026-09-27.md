# N2 CLOSURE AUDIT — STANDARD DEMUŠKIN FAMILY RECOGNITION THRESHOLD
## 2026-09-27

## Decision

The proposed first concrete calculation has now been compared against the existing authoritative research record.

For the standard family
\[
G_{3^s}
=
\langle x_1,\ldots,x_4\mid
x_1^{3^s}[x_1,x_2][x_3,x_4]=1\rangle
\]
and the power-free control \(G_\infty\), the project already contains the essential information-boundary argument:

\[
G_{3^{n-1}}/D_{3^{n-1}}
\cong
G_\infty/D_{3^{n-1}},
\]
while
\[
\chi_{3^{n-1}}\not\equiv\chi_\infty\pmod{3^n},
\]
and the next depth
\[
D_{3^{n-1}+1}
\]
is sufficient within the audited standard family by the intrinsic finite-window/classification argument recorded in the earlier threshold audit.

Therefore the equality
\[
r_{\chi\bmod 3^n}=3^{n-1}+1
\]
for that precise standard-family/category-relative setting is **not a genuinely new theorem to be discovered from scratch**. It is a clean repackaging of an already established information-boundary result.

### Classification

- N2 standard-family threshold calculation: **PASS / LOCAL as a reformulation**
- Novelty of that calculation as a standalone new theorem: **HISTORICAL / SUPERSEDED**
- Category-independent recognition threshold: **OPEN**
- Intrinsic selector stronger than classification-based recognition: **OPEN**
- Broader target/category theory: **OPEN**

---

## 1. What is already established

The controlling audit gives, for the standard \(q=3^s\) family:

\[
G_{3^s}/D_N(G_{3^s})
\cong
G_\infty/D_N(G_\infty)
\qquad(N\le3^s),
\]
because the power relation \(x_1^{3^s}\) lies in the relevant Zassenhaus subgroup of the free group.

At
\[
N=3^s+1,
\]
the finite quotients separate; their abelianizations already distinguish the \(3^s\)-torsion contribution.

For \(n=s+1\),
\[
\chi_{3^s}(x_2)=(1-3^s)^{-1}
\not\equiv1=\chi_\infty(x_2)\pmod{3^n}.
\]

Thus the lower and upper information boundaries were already recorded:
\[
D_{3^{n-1}}
\quad\text{is insufficient,}
\qquad
D_{3^{n-1}+1}
\quad\text{is sufficient}
\]
for the standard family, subject to the previously stated classification dependence.

This is precisely the numerical content that the new \(r_T\) notation packages.

---

## 2. What the new framework genuinely contributes

The new contribution of the present branch is therefore not the numerical equality itself.

The useful new object is the abstract threshold
\[
r_T(\mathcal C;D_\bullet),
\]
which allows one to compare different targets, categories, and filtrations.

The research question becomes:

\[
\boxed{
\text{How does }r_T(\mathcal C;D_\bullet)
\text{ vary with }T,\mathcal C,D_\bullet?
}
\]

This is a broader program than merely restating the known Demuškin calculation.

---

## 3. Consequence for the research plan

The original N2 target
\[
T_k=\chi\bmod p^k
\]
on the standard varying-\(f\) Demuškin family should now be treated as a **baseline example**, not as the main new theorem.

The next genuinely open directions are:

### A. Target variation

Compute
\[
r_T(\mathcal C;D_\bullet)
\]
for targets other than the already understood canonical orientation residue.

Candidates:
- the affine structure itself;
- a specified central extension class;
- a Bockstein/extension datum;
- a restricted cohomological obstruction;
- a joint target \((\chi\bmod p^k,\text{secondary datum})\).

The target must be intrinsic and its isomorphism notion declared before computation.

### B. Category enlargement

Keep the same target
\[
T_k=\chi\bmod p^k
\]
but enlarge \(\mathcal C\).

Possible progression:
\[
\text{standard Demuškin family}
\subset
\text{finite free products of Demuškin blocks}
\subset
\text{rigid elementary-type subclasses}.
\]

The existing project has already closed the finite free-product affine factorization extension, but recognition thresholds for these larger classes have not been established as a general theory.

### C. Filtration comparison

For the same \((\mathcal C,T)\), compare
\[
r_T(\mathcal C;\text{Zassenhaus})
\]
with
\[
r_T(\mathcal C;\text{lower \(p\)-central})
\]
and other precisely defined natural filtrations.

This is especially promising because the project already contains evidence of exponential versus linear depth scales.

---

## 4. Stronger version that remains genuinely open

The strongest natural successor question is no longer merely

\[
r_{\chi\bmod p^k}=? 
\]

but:

> **For which admissible categories \(\mathcal C\), targets \(T\), and natural filtrations \(D_\bullet\) is the recognition threshold finite, and when is it equal to a sharp factorization threshold?**

Formally, investigate conditions implying
\[
r_T(\mathcal C;D_\bullet)
=
f_{\mathcal O}(\mathcal C;D_\bullet)
\]
or strict inequality
\[
r_T<f_{\mathcal O}.
\]

A strict inequality example would be particularly informative: it would demonstrate that an observation may retain information that is unnecessary for recognizing the target.

---

## 5. Research boundary

The following are now frozen:

- the standard-family \(\chi\bmod3^k\) numerical threshold is not treated as a new discovery;
- the known canonical orientation is not claimed as new;
- no closed Fox/\(t_2\) branch is reopened;
- no absolute minimality over arbitrary carriers is claimed.

The new research program is the threshold invariant itself and its behavior under **target/category/filtration variation**.

Classification:

\[
\boxed{
\text{N2 standard baseline: HISTORICAL / SUPERSEDED as novelty target}
}
\]

\[
\boxed{
\text{Recognition-threshold theory beyond that baseline: OPEN}
}
\]

The next authorized gate is therefore **N3: identify the first target/category pair for which \(r_T\) is not already contained in the existing threshold audit, and run the full pre-check before computation.**
