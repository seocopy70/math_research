# Chronological Research Log — 2026-09-15

This is a compact navigation layer. Detailed certificates remain in phase-specific files.

## Main chain

Demuškin group → Zassenhaus filtration → quadratic relation R → degree-4 probe T → symplectic orbit W → representation structure → possible higher/3-adic orientation information.

## Major completed transitions

### Degree-4 obstruction
\[
R=[X_1,X_2]+[X_3,X_4],\qquad T=[[[X_3,X_4],X_1],X_1].
\]

Proved \(T\notin(R)_4\).

### Phase 1 symmetry test

With the authoritative symplectic form J and an explicit transvection,
\[
[gT]\neq[T]\text{ in }Q_4.
\]
Thus T itself is not canonical.

### Phase 2-1

Five explicit transvections generate \(Sp_4(\mathbb F_3)\), order 51840. The orbit span has dimension 45 and has no H-fixed vector.

### Phase 2-3

\[
\dim End_H(W)=2.
\]
A non-scalar nilpotent \(N\) satisfies \(N^2=0\), rank 10, giving
\[
0<U_{10}<K_{35}<W_{45}.
\]

### Phase 2-6-A

\[
U\cong Sym^2(V).
\]

### Phase 2-7 / 2-8B

\[
M=K/U,\qquad \dim M=25,
\]
and M is irreducible by direct matrix-algebra closure.

### Phase 2-10

\[
W\cong\Lambda^2(Sym^2(V)).
\]
This has an independent verification certificate.

### Phase 2-11-A

\[
E=W/U,
\]
with
\[
0\to M_{25}\to E_{35}\to Sym^2(V)_{10}\to0
\]
non-split.

### Phase 2-12

The natural 35-dimensional candidate was tested and rejected:
\[
Hom_H(Sym^4(V),E)=0.
\]
This is a genuine mathematical negative result.

## Current stage

Phase 2-13: identify E from its actual highest/maximal-weight and submodule structure, without guessing a named 35-dimensional module from dimension alone.

## Important failed paths

- Early wrong symplectic pairing matrix: discarded.
- T itself canonical: disproved.
- Premature standard-label identification of M: not promoted because of central-character constraints.
- Phase 2-10 first implementation: code integration failure (`AW` missing), later fixed and independently verified.
- E ≅ Sym^4(V): mathematically rejected.

## Final research question

Does intrinsic filtered/higher structure determine
\[
\chi:G\to\mathbb Z_3^\times?
\]

**OPEN.**
