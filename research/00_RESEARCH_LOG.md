# Research Log

## 2026-09-15 — Literature verification checkpoint

### Purpose

Before extending the degree-4 representation-theoretic calculation, the existing research was compared against the mathematical literature. The purpose was to separate:

1. facts already established in the literature;
2. calculations independently obtained in this research;
3. consequences obtained by combining the two;
4. questions that remain genuinely open.

### Established background

For the rank-4 pro-3 Demuškin case under study, the standard presentation can be taken in the form

\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle.
\]

The corresponding quadratic initial relation in the relevant graded setting is

\[
R=[X_1,X_2]+[X_3,X_4].
\]

The Demuškin structure carries a canonical orientation

\[
\chi_G:G\to \mathbb Z_3^\times,
\]

arising from the dualizing structure. This orientation is a substantially studied invariant and must be treated as established background rather than rediscovered terminology.

### Independent computations in this research

The degree-4 element

\[
T=[[X_3,X_4],X_1],X_1
\]

was investigated inside the free Lie algebra. The calculation gives

\[
T\neq0,
\qquad
T\notin (R)_4.
\]

The argument uses the multidegree of \(T\) and the structure of \((R)_4=[R,L_2]\), together with nonvanishing of \(T\) in the free Lie algebra.

The resulting degree-4 probe produces a 45-dimensional \(Sp_4(\mathbb F_3)\)-module \(W\), for which the current calculation gives

\[
\dim W=45,
\qquad
W^{Sp_4(\mathbb F_3)}=0,
\qquad
W_{Sp_4(\mathbb F_3)}=0.
\]

These are recorded as research calculations, not as literature theorems.

### Major conceptual correction

The original hoped-for chain

\[
T\to W\to \mathbf 1\to \chi_G
\]

must not be assumed. The canonical orientation is \(3\)-adic, while the current representation-theoretic probe is over \(\mathbb F_3\). In particular, the absence of a trivial submodule or quotient in \(W\) does not by itself show that orientation is unrelated to the construction.

A more precise research question is:

\[
\text{How much information about }\chi_G:G\to\mathbb Z_3^\times
\text{ survives in the Zassenhaus filtration?}
\]

and, if the mod-3 graded object is insufficient,

\[
\text{what additional filtered or }3\text{-adic information is required?}
\]

### Next checkpoint

Before calculating the radical/socle structure of \(W\), verify at primary-source level:

- the precise canonical-orientation theorem;
- the exact scope of claims that Zassenhaus filtration may lose orientation information;
- the recent work on non-formality / higher \(A_\infty\) structure for pro-3 Demuškin groups with \(q=3\);
- whether the degree-4 obstruction found here has a known interpretation in that higher-structure literature.
