# Rejected Hypotheses and Computational Failures

This document records failed approaches and rejected mathematical hypotheses so that future researchers and AI systems do not repeat the same dead ends.

## 1. T itself is canonical

### Hypothesis
The specific degree-4 vector

\[
T=[[[X_3,X_4],X_1],X_1]
\]

might itself be a canonical filtered invariant.

### Result
Rejected.

For an explicit symplectic transvection g,

\[
[gT]\neq[T]\quad\text{in }Q_4.
\]

Certificate:

\[
\operatorname{rank}(R_4)=5,
\qquad
\operatorname{rank}([R_4\mid gT-T])=6.
\]

Therefore T depends on the chosen coordinates and cannot by itself be the desired canonical invariant.

### What remains possible
The full orbit module of T may contain canonical subquotients or extension data.

---

## 2. Wrong symplectic pairing matrix in an early exploration

### Failure
An early exploratory calculation used a different pairing matrix J. This changed the intended symplectic structure and produced an unreliable orbit calculation.

### Correction
The authoritative matrix is

\[
J=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}.
\]

All current Phase 2 computations explicitly verify symplecticity and the generated group order 51840.

### Lesson
The exact symplectic convention must be fixed before interpreting representation-theoretic output.

---

## 3. M ≅ L(2,1) as an immediate identification

### Initial temptation
The 25-dimensional quotient

\[
M=K/U
\]

showed dimensions and maximal-vector behavior that suggested a standard highest-weight label.

### Correction
This name was not promoted to a theorem. The central element

\[
-I\in Sp_4(\mathbb F_3)
\]

acts trivially on degree-4 tensors, so every degree-4 subquotient considered here has trivial central action. Under standard C2 highest-weight conventions, careless identification with a module having the opposite central character would be inconsistent.

### Current status
M is safely described as a 25-dimensional irreducible \(Sp_4(\mathbb F_3)\)-module. Its exact highest-weight label is not needed for the already established results.

---

## 4. W ≅ an unverified 45-dimensional standard module

### Initial temptation
Because W has dimension 45 and has a structured endomorphism algebra, several familiar representation-theoretic candidates were considered.

### Resolution
The identification

\[
W\cong\Lambda^2(Sym^2V)
\]

was only accepted after a direct intertwiner computation and an independent verification with full-rank witness.

### Lesson
Dimension agreement is never treated as an isomorphism certificate.

---

## 5. Phase 2-10 implementation failure: missing `AW`

### Failure
The first Phase 2-10 script attempted to obtain `AW` from the Phase 2-7 script. Phase 2-7 did not define/export that object.

### Result
The GitHub Actions run failed with a `KeyError: 'AW'`.

### Correction
The fixed implementation imports the authoritative Phase 2-1 action matrices and generators directly.

### Status
Code/integration failure, not a mathematical failure.

The corrected run succeeded, followed by an independent verification run.

---

## 6. E ≅ Sym^4(V)

### Why it was considered

\[
\dim E=35=\dim Sym^4(V).
\]

This made Sym^4(V) a natural candidate for testing.

### Result
Rejected by direct intertwiner computation:

\[
\operatorname{Hom}_H(Sym^4(V),E)=0.
\]

Therefore

\[
\boxed{E\not\cong Sym^4(V).}
\]

This is a genuine mathematical negative result, not a code failure.

### Lesson
The 35-dimensional E must be identified from its actual module structure rather than from dimension.

---

## 7. Current unresolved identification of E

The current E is

\[
E=W/U,
\qquad \dim E=35,
\]

with non-split exact sequence

\[
0\to M_{25}\to E_{35}\to Sym^2(V)_{10}\to0.
\]

The exact standard representation-theoretic name of E remains OPEN.

The next step is direct highest/maximal-weight and submodule analysis, followed by independent intertwiner verification of any candidate.

---

## 8. Methodological warning

The following are explicitly prohibited in this research archive:

- promoting a dimension match to an isomorphism;
- treating raw program output as proof;
- silently deleting failed computations;
- conflating mod-3 representation data with the full 3-adic orientation character;
- claiming orientation reconstruction before an intrinsic construction and proof exist.
