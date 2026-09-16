# 03. Mathematical and Computational Conventions

This document fixes the conventions needed for independent reproduction.

## 1. Base field

All finite-field calculations in the degree-4 representation-theoretic track are over

\[
\mathbb F_3=\{0,1,2\},
\]

with arithmetic modulo 3.

## 2. Group commutator

The group convention is

\[
[a,b]=a^{-1}b^{-1}ab.
\]

This convention controls all Hall–Petrescu signs.

## 3. Free Lie algebra

Let

\[
L=\mathbb L_{\mathbb F_3}(X_1,X_2,X_3,X_4).
\]

The Lie bracket is implemented inside the free associative algebra as

\[
[A,B]=AB-BA.
\]

The code represents a word by a tuple of letters, for example

\[
X_1X_3X_4X_2\leftrightarrow(1,3,4,2).
\]

## 4. Quadratic relation

The initial quadratic relation is

\[
R=[X_1,X_2]+[X_3,X_4].
\]

In the implementation this is constructed as the sum of the first and sixth degree-2 brackets in lexicographic pair order:

\[
[X_1,X_2]+[X_3,X_4].
\]

## 5. Degree-4 target

The target is exactly

\[
\boxed{T=[[[X_3,X_4],X_1],X_1].}
\]

Its multidegree is

\[
(2,0,1,1).
\]

The code constructs it by nested calls to `bracket`.

## 6. Symplectic form

Vectors are column vectors in \(\mathbb F_3^4\).

We use

\[
J=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}.
\]

The symplectic pairing is \(\omega(x,y)=x^TJy\). All matrix products are modulo 3.

This J is the authoritative convention for the current repository.

## 7. Symplectic transvection

The implementation uses

\[
\boxed{t_v=I+v(Jv)^T.}
\]

Acting on a column vector x,

\[
t_vx=x+v(Jv)^Tx.
\]

Replacing v by -v gives the same matrix over \(\mathbb F_3\), so the 40 nonzero projective directions produce 40 distinct transvections.

Every generated transvection is checked directly by \(t_v^TJt_v=J\).

## 8. Five generators used in Phase 2-1

The generating vectors are

\[
(1,0,0,0),\n(0,1,0,0),\n(0,0,1,0),\n(0,0,0,1),\n(1,0,1,0).
\]

Their associated transvections are constructed by the formula above. The code verifies that they are symplectic and that the subgroup they generate has order

\[
51840=|Sp_4(\mathbb F_3)|.
\]

## 9. Action on Lie words

If g is a 4x4 matrix, its j-th column gives the image of \(X_j\). The induced degree-4 action is obtained by substituting these linear combinations into the associative-word representation and reducing modulo 3.

This is the action used to generate the orbit of T.

## 10. Quotient coordinates

Degree-4 computations use

\[
Q_4=L_4/(R)_4,
\qquad
(R)_4=[R,L_2].
\]

The implementation embeds Lie elements into the 256-dimensional degree-4 associative word space, selects independent columns for \((R)_4\), and then represents the quotient orbit module relative to a complementary basis.

## 11. Coordinate consistency protocol

The authoritative Python representation uses column action \(v\mapsto Av\). GAP `GModuleByMats` uses row vectors with right action. Therefore Python action matrices, endomorphisms, and subspace bases must all be transposed when converted to GAP. This applies equally to generators and to objects such as \(N\), kernels, images, and socle bases.

Equality of subspaces must be checked in one common ambient coordinate system by span/rank, never from dimensions alone.

A structural contradiction caused by a coordinate conversion mismatch is classified as **INVALID TEST**, not as a mathematical failure.

## 12. Finite-field rank protocol

All rank, kernel, image, independence, and span calculations involving \(\mathbb F_3\)-data must use exact finite-field arithmetic.

The repository's authoritative Phase 2-1 routine `rank3()` is the verified reference rank function and should be reused rather than reimplemented in new experiments whenever possible.

The following real/numerical linear-algebra calls are forbidden for the finite-field track:

- `numpy.linalg.matrix_rank`
- `numpy.linalg.det`

They compute over the real/numerical field and can produce values that are mathematically irrelevant to \(\mathbb F_3\) rank questions. Future `np.linalg` usage is surfaced by the repository-wide audit for explicit review.

The CI audit `FINITE_FIELD_RANK_AUDIT_2026-09-17.py` scans all tracked research Python files and fails on forbidden `matrix_rank` or `det` calls.

## 13. Sanity invariants

Before accepting a finite-field result, check relevant necessary identities such as:

- \(N^2=0\Rightarrow\operatorname{im}N\subseteq\ker N\);
- rank-nullity;
- nonzero finite-dimensional modules have nonzero socle;
- any nonzero submodule meets the socle nontrivially;
- \(\dim U+\dim V>\dim M\Rightarrow U\cap V\neq0\);
- intertwiner identities such as \(Q\rho_M(g)=\rho_N(g)Q\).

If a necessary condition fails, stop and classify the calculation as **INVALID TEST** until coordinate and field conventions have been reconciled.

## 14. Important historical correction

An earlier exploratory calculation used an incorrect symplectic pairing matrix. That calculation was not retained as a valid result.

An earlier B1-1 diagnostic also used `numpy.linalg.matrix_rank` on \(\mathbb F_3\)-data and printed a spurious real-field rank. That number is not a valid mathematical result and is not retained. The corrected calculation reuses `rank3()` and independently checks the GAP \(\mathbb F_3\) rank.

## 15. Reproduction principle

A reader should be able to reproduce each claim from:

1. the mathematical convention in this document;
2. the cited script;
3. the recorded Git commit;
4. the GitHub Actions result where available;
5. an independent implementation or certificate for strong identification claims.

No numerical output is treated as a proof without an explicit mathematical interpretation.
