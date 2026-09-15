# Literature Verification — 2026-09-15

## 1. Executive conclusion

The literature cross-check strongly supports the basic Demuškin setup and the graded quadratic framework. It does **not** establish the specific degree-4 calculation or the resulting 45-dimensional module as previously known results. The attempted recovery of canonical orientation from the mod-3 Zassenhaus graded structure remains an open research question.

The central distinction is:

> correctness of our calculation ≠ novelty of the calculation.

Both must be checked independently.

## 2. Results supported by established theory

### 2.1 Standard rank-4 pro-3 Demuškin presentation

The standard form used in this research is

\[
r=x_1^3[x_1,x_2][x_3,x_4].
\]

Thus the chosen rank-4, \(p=3\) example is not an ad hoc construction.

### 2.2 Quadratic initial relation

The associated quadratic relation used throughout the calculation is

\[
R=[X_1,X_2]+[X_3,X_4].
\]

This agrees with the standard symplectic quadratic relation for the rank-4 Demuškin case.

The corresponding alternating pairing on \(H^1(G,\mathbb F_3)\) is represented, in the chosen basis, by the standard symplectic matrix

\[
J=\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}.
\]

### 2.3 Graded/mildness framework

The use of Zassenhaus filtration, initial forms, graded presentations, and the quadratic/Koszul/PBW framework is consistent with established Demuškin and mild pro-p group theory.

This validates the general bridge from the group presentation to the relevant graded Lie/group-algebra calculation.

### 2.4 Canonical orientation

Demuškin groups have a distinguished/canonical orientation

\[
\chi_G:G\to\mathbb Z_3^\times,
\]

related to the dualizing module. The orientation image is an important classification invariant.

Therefore the eventual research target is a reconstruction problem for an already-established object, not the introduction of a new definition of orientation.

## 3. Results currently classified as independent calculations

### 3.1 Degree-4 element

Define

\[
T=[[X_3,X_4],X_1],X_1.
\]

The current calculation gives

\[
T\neq0,
\qquad
T\notin(R)_4.
\]

For the non-membership calculation, the multidegree of \(T\) is

\[
(2,0,1,1).
\]

Since

\[
(R)_4=[R,L_2],
\]

the two components of \(R\), namely \([X_1,X_2]\) and \([X_3,X_4]\), cannot generate this multidegree from an admissible degree-2 Lie element. In the second case one would require a multiple of \([X_1,X_1]\), which vanishes.

Thus the current result is a direct linear-algebra/free-Lie calculation rather than a theorem imported from the literature.

### 3.2 45-dimensional symplectic module

The current construction yields a 45-dimensional \(Sp_4(\mathbb F_3)\)-module \(W\), with computed properties

\[
\dim W=45,
\qquad
W^{Sp_4(\mathbb F_3)}=0,
\qquad
W_{Sp_4(\mathbb F_3)}=0.
\]

A literature search did not identify the exact same result as a previously published theorem. It must therefore remain labelled as a result of this research until a primary-source search proves otherwise.

## 4. Important warning concerning orientation

The canonical orientation takes values in

\[
\mathbb Z_3^\times,
\]

whereas the current representation-theoretic probe is over \(\mathbb F_3\).

In the relevant \(q=3\) situation, the orientation can contain information in the principal-unit direction \(1+3\mathbb Z_3\), which is invisible after reduction modulo 3.

Consequently,

\[
W^{Sp_4(\mathbb F_3)}=0
\]

should not be interpreted as evidence that orientation is absent from the full filtered group structure.

The correct statement is narrower:

> the present degree-4 mod-3 probe does not directly exhibit a trivial symplectic representation carrying the canonical orientation.

## 5. Potential no-go phenomenon

Some literature on oriented/\(\theta\)-abelian pro-p groups indicates that the Zassenhaus filtration can lose information about the image of an orientation. This is highly relevant, but the exact scope must be checked before applying such a result to the present Demuškin setting.

Open distinctions to resolve:

1. Is the statement about the full filtered group, the associated graded object, or only a reduced invariant?
2. Does it apply to all Demuškin groups or only a broader/different class of oriented pro-p groups?
3. Does the loss occur only after passing to mod-p graded data?
4. Can additional extension data or higher filtered operations restore the lost p-adic information?

No impossibility theorem should be claimed here until these distinctions are verified from the primary sources.

## 6. Relation to recent higher-structure work

Recent work on pro-3 Demuškin groups with \(q=3\) studies higher \(A_\infty\)/\(A_3\)-formality and detects nontrivial higher structure.

This is potentially close to the present degree-4 obstruction, but the relationship has **not** yet been established.

The current research direction is different in emphasis:

\[
\text{Zassenhaus filtration}
\to
\text{degree-4 Lie obstruction}
\to
Sp_4(\mathbb F_3)\text{-module}
\to
\text{orientation reconstruction?}
\]

while the related literature studies higher homotopy/cohomological structure.

The precise connection, if any, remains open.

## 7. Research-position statement

The safest current characterization is:

> The Demuškin presentation, quadratic relation, graded framework, and canonical orientation are established background. The degree-4 element \(T\), its non-membership in \((R)_4\), and the resulting 45-dimensional symplectic module are presently treated as independent computations. Whether this module, or a richer filtered/higher structure built from it, can encode or reconstruct the canonical 3-adic orientation is an open question requiring further work.

## 8. Required next verification

Before the next major computation, verify at primary-source level:

- canonical orientation and its uniqueness/classification role;
- exact no-go statements concerning orientation versus Zassenhaus filtration;
- recent pro-3 Demuškin \(A_3\)/\(A_\infty\) non-formality results;
- possible identification of the present degree-4 obstruction with a Massey-product, higher multiplication, or other known obstruction.

Only after this should the representation-theoretic analysis of the radical, socle, composition factors, and extensions of \(W\) be interpreted as evidence toward orientation reconstruction.
