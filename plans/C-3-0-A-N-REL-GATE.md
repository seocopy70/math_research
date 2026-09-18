# C-3-0: A_n^rel definition gate

## 0. Status and purpose

**DEFINITION / PREDICTION GATE — NO LARGE COMPUTATION YET**

This gate fixes the diagnostic observable and records a concrete mathematical prediction derived from the filtration structure.

It does **not** claim that A_n^rel is a q-invariant of gr(G), nor that it gives weak-data recovery.

The prediction is useful precisely because it can fail for identifiable mathematical reasons.

---

## 1. Setting

Let F be the free pro-3 group on x_1,...,x_4,

\[
V=F/\Phi(F)\cong \mathbf F_3^4,
\]

and let D_n be the standard descending 3-Zassenhaus filtration.

Let r_q be the project's defining relator s_q. This notation must be checked against the repository definition before implementation.

Let

\[
N_q=\overline{\langle\!\langle r_q\rangle\!\rangle},
\qquad
G_q=F/N_q.
\]

The q=infinity case means the pure-commutator baseline; it is not a numerical 3-adic value.

---

## 2. Definition of A_n^rel

For the chosen ambient linear group H, define

\[
A_n^{\mathrm{rel}}(q)
=
\left\{
g\in H:
\begin{array}{l}
\text{there is a free-pro-3 automorphism }\widetilde g
\\
\text{inducing }g\text{ on }V
\\
\text{with }\widetilde g(r_q)\in N_qD_n(F)
\end{array}
\right\}.
\]

Equivalently, this is the linear image of automorphisms of the finite filtered quotient G_q/D_n(G_q), subject to the fixed coordinate convention.

This is deliberately a **diagnostic observable**. Since G_q/D_n is stronger data than gr(G_q), no claim is made that A_n^rel is an invariant of the graded object alone.

The full abstract quotient G_q/D_n must not be used to claim weak-data q-recovery.

---

## 3. Ambient group convention

The degree-2 initial relation spans a one-dimensional line, so for n>=3 its stabilizer in GL(V) lies in a generalized symplectic group.

The orientation-sensitive ambient group is therefore

\[
H=GSp(V),
\]

not automatically Sp(V).

For rank 4 over F_3:

\[
|Sp_4(\mathbf F_3)|=51840,
\qquad
|GSp_4(\mathbf F_3)|=103680.
\]

For rank 2:

\[
GSp_2(\mathbf F_3)=GL_2(\mathbf F_3),
\qquad
Sp_2(\mathbf F_3)=SL_2(\mathbf F_3).
\]

The multiplier is denoted by \(\mu(g)\in\mathbf F_3^\times\).

Every implementation must state whether it is testing GSp or its multiplier-1 subgroup Sp.

---

## 4. Easy filtration prediction

Suppose q=3^s.

Since

\[
x_1^q\in D_q(F),
\]

the finite-q relator and the q=infinity relator agree modulo D_n whenever n<=q.

Therefore the expected identity is

\[
A_n^{\mathrm{rel}}(q)=A_n^{\mathrm{rel}}(\infty),
\qquad n\le q,
\]

provided the same lift convention is used on both presentations.

This is a filtration-indexing statement and should be checked directly in the implementation.

It implies that the first potentially q-sensitive level is

\[
n=q+1.
\]

---

## 5. Derived prediction at n=q+1

At n=q+1, the new q-power contribution first appears in degree q.

Let \(\bar x_1\in L_1\) denote the degree-one generator and let

\[
\bar x_1^{[q]}
\]

denote its q-restricted power in the free restricted graded Lie algebra.

The proposed reduction is:

> after the degree-2 initial relation is accounted for, relator preservation at the first q-sensitive level forces the degree-q pure restricted-power source associated with x_1 to transform by the GSp multiplier.

Thus, if

\[
g(\bar x_1)=\sum_i a_i\bar x_i,
\]

the pure L_1^{[q]} coordinates of the q-power term give the necessary condition

\[
a_i^q=a_i
\]

on coefficients, together with

\[
a_1=\mu(g)
\]

when the source coordinate is identified with the relator multiplier.

Because the p-map in a free restricted Lie algebra is **not additive**, this must not be implemented as the false identity

\[
(x+y)^{[q]}=x^{[q]}+y^{[q]}.
\]

Only the pure restricted-power source coordinates are being projected out. The cross terms belong to other degree-q Lie components and must be handled separately.

Hence the current prediction is

\[
A_{q+1}^{\mathrm{rel}}(q)
\subseteq
\left\{
g\in GSp(V):
g\bar x_1=\mu(g)\bar x_1
\right\}.
\]

This is a **necessary-condition prediction only**.

### Assumptions requiring independent verification

The derivation uses at least:

1. the defining relation ideal does not eliminate or identify the relevant pure \(L_1^{[q]}\) source coordinate;
2. changing a chosen lift by an IA/D_2 correction does not alter this source coordinate modulo D_{q+1};
3. the degree-2 relation contributes with the expected multiplier and does not introduce an additional degree-q obstruction in the projected source;
4. the relevant relator class and multiplier are well-defined under the chosen quotient/module.

These must be proved or computationally falsified before the prediction is promoted.

The relevant Quadrelli/free-restricted-basis statement should be checked against the exact source used by the project; no citation is treated as verified merely from this draft.

---

## 6. Rank-4 stabilizer size

The predicted subgroup

\[
\{g\in GSp_4(\mathbf F_3):g\bar x_1=\mu(g)\bar x_1\}
\]

has expected size

\[
2\cdot\frac{|Sp_4(\mathbf F_3)|}{3^4-1}
=
2\cdot648
=
1296,
\]

because Sp_4(F_3) is transitive on the 80 nonzero vectors and the two multiplier values in F_3^* contribute separately.

Inside Sp_4(F_3), the corresponding vector stabilizer has order

\[
648.
\]

This is **not** the same as the ordinary line stabilizer, which is larger.

---

## 7. Rank-2 control

Use

\[
G_q^{(2)}
=
\langle x_1,x_2\mid x_1^q[x_1,x_2]\rangle.
\]

For q=3 the first potentially sensitive level is n=4.

The rank-2 ambient group is

\[
GSp_2(\mathbf F_3)=GL_2(\mathbf F_3),
\qquad |GL_2(\mathbf F_3)|=48.
\]

The predicted necessary subgroup is

\[
\left\{
g\in GL_2(\mathbf F_3):
g\bar x_1=\det(g)\bar x_1
\right\}.
\]

With the column-vector convention

\[
g=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\]

the condition is

\[
c=0,
\qquad
a=ad-bc=\det(g),
\]

so

\[
d=1.
\]

Therefore the subgroup has **4 elements**, not 6:

\[
\left\{
\begin{pmatrix}
a&b\\
0&1
\end{pmatrix}
:
a\in\mathbf F_3^\times, b\in\mathbf F_3
\right\}.
\]

This corrects the order-6 count in the draft.

For comparison:

- ordinary line stabilizer of \(\langle\bar x_1\rangle\) in GL_2(F_3) has order 12;
- the vector/multiplier condition above has order 4;
- SL_2(F_3) has order 24;
- its vector stabilizer of \(\bar x_1\) has order 3.

The E0 prediction is therefore **not** “A_4(3) has order 6”. The test should first ask whether every admissible element lies in the predicted order-4 subgroup.

Equality is not predicted at this stage.

---

## 8. Rank-2 scope

Rank 2 is now more than a purely implementation-only control, but it remains **not a model of the rank-4 obstruction geometry**.

It provides a genuine mathematical prediction test for the proposed first-q-sensitive mechanism:

\[
A_{q+1}^{\mathrm{rel}}(q)
\subseteq
\{g:g\bar x_1=\mu(g)\bar x_1\}.
\]

It does not test W_45, I_35, or the rank-4 degree-4 obstruction.

A failure is valuable: it identifies which structural assumption in Section 5 is false or incomplete.

---

## 9. Experiments

### E0 — rank 2, q=3, n=4

Enumerate GL_2(F_3) and test the relator-preservation/lift condition under the project's exact lift convention.

Required outputs:

- actual A_4^rel(3);
- predicted order-4 subgroup;
- each representative's lift/admissibility result;
- independent check of matrix convention;
- independent check of D_4 indexing;
- if possible, extraction of the degree-3 pure restricted-power coordinate.

Do not infer equality with the predicted subgroup unless all elements have been tested and the lift search is mathematically complete.

### E1 — rank 4, q=3, n=4

Only after E0 passes its definition and convention gates.

Test representative GSp_4(F_3) elements and compare the observed admissibility with the necessary condition

\[
g\bar x_1=\mu(g)\bar x_1.
\]

Compare the mechanism with the project's existing degree-4 q=3 obstruction data, but do not identify the two constructions without a proof.

### E2 — q=9, n=10

Go/no-go only after E0 and E1.

The expected first-sensitive level is n=10.

The abelianization shortcut at n=10 is explicitly recorded as non-novel; the research interest is whether the same threshold is visible through the prescribed relator/lift observable in a structurally meaningful way.

---

## 10. Interpretation

### POSITIVE

E0 and/or E1 confirm the predicted **necessary condition** after independent validation of the lift and filtration machinery.

This supports the mechanism but does not prove equality, canonicity, weak-data recovery, or orientation recovery.

### NEGATIVE

The prediction fails after the implementation and conventions are independently validated.

Record the exact counterexample and determine which assumption in Section 5 fails.

A negative result is preserved as a mathematical result, not treated as an implementation failure by default.

### INCONCLUSIVE

The computation depends on an incomplete lift search, ambiguous quotient equivalence, or an unverified source-coordinate identification.

Do not promote it to a mathematical positive or negative result.

---

## 11. Relationship to the main research goal

The current primary target remains:

> Determine the smallest filtered/graded level, within a prescribed structural observable, at which q=3^s for s>=2 can be distinguished from q=infinity.

The q=3 case is retained as a mechanism/control case because existing higher A_3-formality work already distinguishes q=3 from q!=3.

The present prediction is potentially more useful because it gives a concrete mechanism that can be tested at q=9, where the trivial abelianization threshold is n=10.

Orientation recovery remains downstream.

---

## 12. Non-goals

This gate does not:

- define q by A_n^rel;
- claim A_n^rel is a gr(G) invariant;
- claim A_n^rel is canonical or presentation-independent;
- prove equality with a line or vector stabilizer;
- prove the n=q+1 threshold is minimal for every observable;
- replace the existing Q3/Q9 or O2 tracks;
- justify switching to the p-descending filtration;
- introduce Massey/A-infinity machinery.

