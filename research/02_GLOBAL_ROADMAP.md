# 02. Global Research Roadmap

## One-sentence research question

> Can the canonical orientation character \(\chi:G\to\mathbb Z_3^\times\) of the rank-4 pro-3 Demuškin group be recovered intrinsically from its filtration and associated higher structure?

This remains OPEN.

---

## The whole project at a glance

```text
Demuškin group G
      │
      ▼
Zassenhaus filtration D_i(G)
      │
      ▼
associated graded restricted Lie structure
      │
      ▼
quadratic initial relation R
      │
      ▼
degree-4 probe T
      │
      ├── Phase 1: T is NOT canonical by itself
      │
      ▼
Sp_4(F_3)-orbit module W_45
      │
      ├── Phase 2 representation analysis
      │       │
      │       ├── U_10 ≅ Sym^2(V)
      │       ├── K_35
      │       ├── M_25 = K/U irreducible
      │       └── W ≅ Λ^2(Sym^2(V))
      │
      ▼
E_35 = W/U_10
      │
      ├── 0 → M_25 → E_35 → Sym^2(V)_10 → 0
      │              non-split
      │
      ├── Phase 2-12: E ≠ Sym^4(V)
      │
      └── Phase 2-13+: identify E from its actual structure
      │
      ▼
Track B: independent Hall–Petrescu / filtration calculations
      │
      ▼
connect representation-theoretic structure with group-level higher data
      │
      ▼
FINAL QUESTION
Can intrinsic filtered data recover χ:G→Z_3^×?
```

---

## Phase 0 — arithmetic setup

Define the rank-4 pro-3 Demuškin group

\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle.
\]

Introduce the orientation character

\[
\chi:G\to\mathbb Z_3^\times.
\]

The fundamental difficulty is that mod-3 graded information does not automatically retain the full 3-adic target \(\mathbb Z_3^\times\).

**Status: external mathematical background + OPEN reconstruction question.**

---

## Phase 1 — degree-4 obstruction

Set

\[
R=[X_1,X_2]+[X_3,X_4]
\]

and

\[
T=[[[X_3,X_4],X_1],X_1].
\]

Prove

\[
T\notin(R)_4.
\]

Then test whether T is invariant under the natural symplectic action.

Result:

\[
[gT]\neq[T]
\]

for an explicit symplectic transvection.

Therefore T itself is not a canonical coordinate-free invariant.

**Status: completed.**

---

## Phase 2 — replace T by its full symmetry orbit

Let

\[
H=Sp_4(\mathbb F_3),
\qquad
W=\langle H\cdot[T]\rangle.
\]

### Phase 2-1

Compute the orbit module.

\[
|H|=51840,
\qquad
\dim W=45,
\qquad
W^H=0.
\]

**Completed.**

### Phase 2-3

Compute the H-endomorphism algebra.

\[
\dim End_H(W)=2.
\]

Find non-scalar

\[
N^2=0,
\qquad
\operatorname{rank}N=10.
\]

Hence

\[
0\subset U=\operatorname{im}N\subset K=\ker N\subset W.
\]

Dimensions:

\[
10,35,45.
\]

**Completed.**

### Phase 2-6-A

Identify

\[
U\cong Sym^2(V).
\]

**Completed with intertwiner certificate.**

### Phase 2-7 / 2-8B

Set

\[
M=K/U,
\qquad \dim M=25.
\]

Direct associative-algebra closure gives

\[
\langle A_1,\ldots,A_5\rangle_{alg}=Mat_{25}(\mathbb F_3),
\]

so M is irreducible.

**Completed.**

### Phase 2-10

Identify W independently:

\[
W\cong\Lambda^2(Sym^2(V)).
\]

**Completed with independent verification.**

### Phase 2-11-A

Set

\[
E=W/U.
\]

Then

\[
0\to M_{25}\to E_{35}\to Sym^2(V)_{10}\to0.
\]

Compute

\[
Hom_H(Sym^2(V),E)=0.
\]

Therefore the sequence is non-split.

**Completed.**

### Phase 2-12

Natural dimension-based candidate:

\[
E\stackrel{?}{\cong}Sym^4(V).
\]

Direct intertwiner computation gives

\[
Hom_H(Sym^4(V),E)=0.
\]

Therefore

\[
\boxed{E\not\cong Sym^4(V).}
\]

**Completed negative result. Candidate rejected.**

### Phase 2-13 and later

Do not guess the name of E from dimension.

Instead:

1. recover the actual H-action on E;
2. choose and document a fixed Borel/root convention;
3. compute maximal/highest-weight candidates;
4. determine submodule and quotient structure;
5. only then test named Weyl/simple/tilting/indecomposable candidates by independent intertwiners.

**Current stage.**

---

## Track B — independent group/filtration calculation

Track B must not be used to force a representation-theoretic answer.

Start from

\[
u=x_1^{-2},\qquad v=[x_3,x_4]^{-1},
\]

so that

\[
x_2^{-1}x_1x_2=uv.
\]

Use Hall–Petrescu and the Zassenhaus filtration to extract degree-3/degree-4 information.

A2 is currently closed with

\[
HP_4((uv)^{-3})=-T=2T\neq0
\]

in \(Q_4\).

A1 and A3 remain separate verification targets.

---

## Final stage — orientation reconstruction

The representation-theoretic and Hall–Petrescu tracks eventually have to meet the original arithmetic question.

The final proof, if positive, must construct intrinsically

\[
\chi_{filt}:G\to\mathbb Z_3^\times
\]

and prove equality with the canonical Demuškin orientation.

If impossible, the final result should instead establish the precise information-theoretic obstruction and identify the smallest additional datum required.

**OPEN.**

---

## Methodological rule

Every strong result follows:

\[
\boxed{\text{computation discovery}\to\text{explicit certificate}\to\text{mathematical explanation}\to\text{independent verification}}.
\]

Dimension matching alone is never treated as an isomorphism proof.
