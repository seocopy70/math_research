# TWISTED DEGREE-3 TRUNCATION — FILTRATION ESTIMATE / 2026-09-19

## Objective

Close the remaining degree-truncation part of the twisted obstruction lemma by isolating the first-order coefficient deformation.

## 1. First-order decomposition of a crossed homomorphism

Work modulo 9 and write
\[
\rho(g)=1+3\lambda(g)\pmod9,
\]
where lambda is the mod-3 additive character associated with the first orientation digit.

For a lifted mod-3 cocycle f, choose z on the free generators with z(x_i) congruent to f_i modulo 3. Modulo 9, the crossed rule
\[
z(uv)=z(u)+\rho(u)z(v)
\]
can be expanded as
\[
z(uv)=z(u)+z(v)+3\lambda(u)f(v)\pmod9,
\]
where only f(v) modulo 3 is needed in the correction term.

Thus, after dividing by 3, the deformation part is a bilinear first-order term in lambda and f.

## 2. Filtration consequence

Let I be the augmentation ideal of the free pro-3 group algebra. The ordinary mod-3 derivation f is first-order in I: it factors through
\[
I/I^2.
\]
The first-order action correction 3 lambda(u) f(v) is therefore a product of two first-order pieces. Consequently its associated graded contribution is concentrated in augmentation degree 2.

Equivalently, after division by 3 and reduction modulo 3, the twisted coefficient deformation sees only the quadratic initial form of the relator:
\[
I^2/I^3.
\]

The ordinary power contribution is different: in characteristic 3 the cubic restricted-power term survives because the binomial coefficients in the cube expansion supply the factor 3. Its contribution is exactly the restricted cubic/power projection p(P).

Therefore, for a relator whose initial filtered expansion is
\[
r=(R,P)+O(4),
\]
the quotient
\[
\frac{z(r)}3\pmod3
\]
receives contributions only from R and p(P). Any term of filtered degree >=4 has no component in the degree-2 first-order deformation and no degree-3 restricted-power contribution, so it maps to zero in the obstruction quotient.

This is the required structural reason that the first twisted obstruction factors through the degree-(2,3) jet.

## 3. Exact coordinate formula

The quadratic contribution is the alternating contraction
\[
(\lambda\wedge f)(R),
\]
with the sign fixed by
\[
[x,y]=x^{-1}y^{-1}xy.
\]

The cubic power contribution is
\[
f(p(P)).
\]

Hence
\[
\boxed{
\frac{z(r)}3
=
f(p(P))+(\lambda\wedge f)(R)
\pmod3.
}
\]

For
\[
R=[X_1,X_2]+[X_3,X_4],
\qquad
p(P)=X_1^{(1)},
\]
the formula is
\[
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]

## 4. Important limitation

The filtration argument establishes the information-level truncation, but a publication-level proof should still display the corresponding Magnus/group-ring calculation for the chosen commutator convention. In particular, the signs of the four quadratic coefficients should be checked once from
\[
[x,y]=x^{-1}y^{-1}xy
\]
rather than inferred from the coordinate-free notation.

## Decision

**Degree-(2,3) information truncation: PASS / structurally established, subject to the explicit convention-level sign calculation.**

No broad scan is authorized.