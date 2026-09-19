# HARD ATTACK 8 — FOX ROW / DEMUŠKIN ORIENTATION IDENTIFICATION — 2026-09-19

## Objective

The Nielsen stress test closed the covariance question for the exact Fox row, but left one load-bearing OPEN statement:

\[
J_r(\rho)=0\quad\Longleftrightarrow\quad \rho=\chi_G.
\]

This was attacked directly from the standard characterization of the canonical Demuškin orientation by crossed derivations.

## 1. Standard orientation characterization

For a Demuškin pro-p group G with minimal one-relator presentation
\[
1\to\overline{\langle\!\langle r\rangle\!\rangle}\to F\to G\to1,
\]
the canonical orientation is characterized by the Labute/Serre crossed-derivation condition:

> a character \(\chi:F\to\mathbf Z_p^\times\) gives the canonical orientation precisely when every \(\chi\)-crossed derivation of the free pro-p group into the rank-one module \(\mathbf Z_p(\chi)\) descends through the relator, i.e. kills \(r\).

This characterization is used explicitly in modern formalized work on Demuškin orientations: the crossed derivation is arbitrary on the free generators, and descent is equivalent to the relator equation vanishing for arbitrary generator values. See the cited discussion of Labute's Theorem 4 and the explicit crossed-derivation calculation. citeturn2search0turn2search3

This is exactly the missing bridge needed by the Fox construction; it is not an interpretation invented from the present calculation.

## 2. Fox calculus converts the condition into row vanishing

Let
\[
D:F\to \mathbf Z_p(\chi)
\]
be a \(\chi\)-crossed derivation, with arbitrary generator values
\[
d_i=D(x_i).
\]

For the chosen convention, Fox calculus gives the crossed Leibniz expansion
\[
D(w)=\sum_i \operatorname{ev}_\chi\!\left(\frac{\partial w}{\partial x_i}\right)d_i,
\]
up to the standard left/right convention transpose. The convention used in the project was fixed so that the displayed evaluated row \(J_r(\chi)\) is the coefficient row.

Therefore
\[
D(r)=J_r(\chi)\,d.
\]

Crucially, the \(d_i\) are arbitrary because \(F\) is free. Hence
\[
D(r)=0\quad\text{for every \(\chi\)-crossed derivation }D
\]
if and only if
\[
\boxed{J_r(\chi)=0}.
\]

This is the precise non-circular identification step.

## 3. Consequence for the canonical orientation

Combining §1 and §2 gives
\[
\boxed{
\rho=\chi_G
\quad\Longleftrightarrow\quad
J_r(\rho)=0
}
\]
on the character neighborhood for which the coefficient module is defined.

Thus the earlier A/B/C distinction is resolved at the canonical point:

- \(\ker J_r(\rho)\neq0\) is too weak;
- a specific canonical kernel vector is unnecessary;
- the correct intrinsic condition is the stronger universal statement that **all** \(\rho\)-crossed derivations kill the relator;
- Fox calculus turns that universal statement exactly into row vanishing.

The previous concern that row-zero might be an accidental stronger condition is therefore removed.

## 4. Application to the present rank-4 q=3 group

For
\[
r=x_1^3[x_1,x_2][x_3,x_4]
\]
the universal evaluated row is
\[
J_1=1+A+A^2B^{-1},
\]
\[
J_2=A^2(A-1)B^{-1},
\]
\[
J_3=A^3C^{-1}(D^{-1}-1),
\]
\[
J_4=A^3D^{-1}(1-C^{-1}).
\]

On \((1+3\mathbf Z_3)^4\), all factors removed in the projective reduction are units, so row-zero is equivalent to
\[
A-1=0,\qquad C-1=0,\qquad D-1=0,
\]
and
\[
B(1+A)+A^2=0.
\]

Hence
\[
A=C=D=1,
\qquad
2B+1=0,
\]
so
\[
\boxed{\chi(x_1)=\chi(x_3)=\chi(x_4)=1,\qquad
\chi(x_2)=-\frac12=(1-3)^{-1}.}
\]

This agrees with the exact crossed-derivation computation already in the project, but the logical status is now different: the Fox row is not merely a computationally successful obstruction. It is the coefficient-level expression of the canonical orientation characterization.

## 5. Presentation covariance is now part of the theorem package

The previous Nielsen stress test established the row's exact coordinate covariance under nontrivial generator changes. The standard Fox chain rule gives the general mechanism, while relator conjugation changes the row only by an invertible coefficient unit.

Therefore the correct exact object is the projective/equivalent class of the universal evaluated Fox obstruction family, not the raw coordinate row.

The Nielsen tests gave explicit confirmations:

- \(x_1=y_1y_2^{-1}, x_2=y_2\): zero moves from \((1,-1/2)\) to \((-1/2,-1/2)\);
- \(x_1=y_2,x_2=y_1\): zero moves to \((-1/2,1)\).

Both transformed rows vanish exactly at the transported canonical character.

## 6. What this closes

The following logical gap is now **CLOSED**, subject only to the standard Demuškin orientation characterization and the fixed Fox convention:

\[
\boxed{
\text{canonical orientation}
\Longleftrightarrow
\text{universal crossed-derivation descent}
\Longleftrightarrow
\text{evaluated Fox row}=0.
}
\]

This is stronger than the previous fixed-presentation calculation and stronger than the Nielsen stress test alone.

## 7. What remains OPEN

This closure does **not** yet prove that the Fox scheme is an intrinsic Zassenhaus/Jennings–Lazard filtered carrier.

The exact Fox carrier uses:

- the abelian character torus;
- completed coefficient evaluation;
- characteristic-zero crossed-derivation coefficients.

Thus it is now a rigorously identified **exact characteristic-zero orientation carrier**, but the filtered bridge remains:

\[
\boxed{
\text{intrinsic filtered relation data}
\longrightarrow
\text{exact Fox/orientation locus}.
}
\]

The mod-9 projective relation jet already gives an intrinsic filtered carrier for the first nontrivial digit. The next structural question is whether its construction is the filtered initial form of the exact Fox carrier, and whether the full compatible filtered tower factors naturally through successive truncations of the exact Fox condition.

## Status

- Fox row as crossed-derivation coefficient row: **PASS / CLOSED**.
- Canonical orientation = universal crossed-derivation descent: **PASS / CLOSED**, under the standard Demuškin orientation theorem.
- Canonical orientation = Fox row-zero: **PASS / CLOSED**, under the same theorem and fixed Fox convention.
- Nielsen covariance: **PASS / CLOSED**.
- Fixed q=3 exact \(\mathbf Z_3\) recovery: **PASS / CLOSED**.
- Exact Fox carrier as an intrinsic filtered object: **OPEN**.
- Relation between exact Fox carrier and the intrinsic mod-9/projective relation jet: **NEXT TARGET**.

## Research consequence

The Fox branch is no longer merely an auxiliary obstruction. It is an exact characteristic-zero realization of the canonical orientation criterion.

The remaining research problem has therefore become cleaner:

\[
\boxed{
\text{Can the intrinsic filtered program recover the exact Fox orientation locus
without importing the characteristic-zero crossed-derivation object by definition?}
}
\]

That is now the correct load-bearing question.
