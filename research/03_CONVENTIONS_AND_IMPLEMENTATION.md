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

The symplectic pairing is

\[
\omega(x,y)=x^TJy.
\]

All matrix products are modulo 3.

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

Since

\[
(Jv)^Tx=v^TJ^Tx=-v^TJx
\]

for alternating J, this differs by a sign from some common textbook transvection conventions depending on whether the pairing is written as \(x^TJy\) or \(y^TJx\). The repository's matrix formula above is the authoritative convention.

Replacing v by -v gives the same matrix over \(\mathbb F_3\), so the 40 nonzero projective directions produce 40 distinct transvections.

Every generated transvection is checked directly by

\[
t_v^TJt_v=J.
\]

## 8. Five generators used in Phase 2-1

The generating vectors are

\[
(1,0,0,0),
(0,1,0,0),
(0,0,1,0),
(0,0,0,1),
(1,0,1,0).
\]

Their associated transvections are constructed by the formula above.

The code verifies that they are symplectic and that the subgroup they generate has order

\[
51840=|Sp_4(\mathbb F_3)|.
\]

Thus the five matrices generate the full intended symplectic group.

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

## 11. Important historical correction

An earlier exploratory calculation used an incorrect symplectic pairing matrix. That calculation was not retained as a valid result.

The authoritative matrix is the J displayed in Section 6, and every current Phase 2 result must use it.

## 12. Reproduction principle

A reader should be able to reproduce each claim from:

1. the mathematical convention in this document;
2. the cited script;
3. the recorded Git commit;
4. the GitHub Actions result where available;
5. an independent implementation or certificate for strong identification claims.

No numerical output is treated as a proof without an explicit mathematical interpretation.
