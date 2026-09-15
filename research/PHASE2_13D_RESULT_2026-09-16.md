# PHASE 2-13D RESULT — U TORUS CHARACTER CROSS-CHECK

Date: 2026-09-16

## Purpose

The Phase 2-13C torus-character sanity audit on
\(E=W/U\) produced the finite-field character
\[
\chi_E=(1,2,2,1),
\]
which matches the product character on
\(T(\mathbb F_3)\cong(\mathbb F_3^\times)^2\).

To independently check the coordinate convention, we now perform the same
fixed-line/torus calculation on
\[
U=\operatorname{im}N\cong \operatorname{Sym}^2(V).
\]
The character expected from highest weight \((2,0)=2\omega_1=2\varepsilon_1\)
is \(a^2\), which is trivial on \(\mathbb F_3^\times\).

## Method

The calculation does **not** simply read off the highest vector of the
\(\operatorname{Sym}^2(V)\) model.

Instead it:

1. imports the already certified Phase 2-6A restricted action of the five
   finite-group generators on the actual module \(U=\operatorname{im}N\);
2. reconstructs the full \(Sp_4(\mathbb F_3)\) group by exact matrix BFS;
3. records a word in the same five generators for every group element;
4. expresses the four positive-root generators and four split-torus elements
   as exact words in those generators;
5. obtains their action on the actual 10-dimensional \(U\) from the same
   restricted representation;
6. computes the common positive-unipotent fixed space over \(\mathbb F_3\);
7. extracts the torus scalar on that one-dimensional fixed line and checks
   the character law.

This avoids the failed generic restriction route from the first implementation.
That failure was an implementation-level coordinate reconstruction issue, not
a mathematical counterexample.

## Verified run

GitHub Actions run:
\[
35018871489
\]

Job:
\[
104549148591
\]

Head commit:
`edcf3b2e738ba3854097c5825328a7658aead4ca`

## Result

The successful run reports:

\[
\boxed{\dim U=10}
\]
\[
\boxed{|Sp_4(\mathbb F_3)|=51840}
\]
\[
\boxed{|U^+(\mathbb F_3)|=81}
\]
\[
\boxed{\dim U^{U^+}=1}
\]

For the torus elements ordered as
\[
(1,1),(1,2),(2,1),(2,2),
\]
the observed character is
\[
\boxed{(1,1,1,1)}.
\]

It is exactly the trivial character.

The run also reports the previously established
\[
\dim\operatorname{Hom}_H(U,\operatorname{Sym}^2V)=1
\]
and a full-rank intertwiner.

## Interpretation

This is the desired independent coordinate-convention cross-check:

- \(U\) has a unique positive-unipotent fixed line;
- its finite-field torus character is trivial;
- this agrees exactly with
  \[
  (2,0)=2\varepsilon_1
  \quad\Longrightarrow\quad
  \chi(a,b)=a^2=1
  \quad(a\in\mathbb F_3^*).
  \]

Together with the Phase 2-13C result
\[
\chi_E=(1,2,2,1)=ab,
\]
the two sides are now mutually consistent with the proposed highest-weight
labels \((2,0)\) for \(U\) and \((2,1)\) for the fixed line in \(E\), under the
chosen \(C_2\) torus convention.

## Strict limitation

This still does **not** prove
\[
E\cong\nabla(2,1).
\]
The finite-field torus character is only a character of
\(T(\mathbb F_3)\), and distinct algebraic weights can collapse to the same
character modulo the small torus.

The next decisive step is therefore an algebraic/hyperalgebra-level
comparison with the candidate costandard module \(\nabla(2,1)\), or an
explicit full-rank intertwiner after constructing the dual Weyl module.

## Methodological status

The result passes the project's required pattern:

\[
\boxed{\text{computation}\to\text{certificate}\to\text{interpretation}\to\text{independent cross-check}}.
\]
