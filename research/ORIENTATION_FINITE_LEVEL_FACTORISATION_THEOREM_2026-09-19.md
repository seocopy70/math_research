# ORIENTATION — FINITE-LEVEL FACTORIZATION / INVERSE-LIMIT THEOREM — 2026-09-19

## Objective

Close the theorem-level logical gap between the already verified crossed-derivation calculation and the statement

\[
\text{compatible full filtered relation-jet tower}\Longrightarrow
\chi:G\to\mathbf Z_3^\times.
\]

The purpose is not to claim that a finite low-degree jet already contains the full character. The claim proved here is the weaker and precise factorization statement: once the full compatible finite-level relation-jet tower is supplied, each finite level determines the corresponding reduction of the canonical orientation, and these reductions are compatible.

---

## 1. Frozen group and convention

\[
G=
\left\langle
x_1,x_2,x_3,x_4
\mid
r=x_1^3[x_1,x_2][x_3,x_4]
\right\rangle,
\]

with

\[
[x,y]=x^{-1}y^{-1}xy.
\]

Write

\[
\chi_n:G\to(\mathbf Z/3^n)^\times
\]

for the reduction of the canonical orientation modulo \(3^n\).

Because the q=3 Demuškin orientation has image in \(1+3\mathbf Z_3\), every \(\chi_n\) is in the subgroup \(1+3(\mathbf Z/3^n)\) for \(n\ge2\).

---

## 2. Definition of the finite-level relation datum

For each \(n\ge2\), let \(J_n(G)\) denote the intrinsic finite-level filtered relation datum obtained by truncating the defining filtered relation and its relation-module/jet structure to the precision needed modulo \(3^n\), with the presentation/lift gauge already quotiented in the same manner as the projective degree-(2,3) construction.

The tower comes with canonical reduction maps

\[
\pi_{n+1,n}:J_{n+1}(G)\longrightarrow J_n(G).
\]

The definition is deliberately stronger than the bare associated graded restricted Lie object and weaker than retaining a chosen free lift: \(J_n\) records the filtered relation information required to evaluate the universal crossed-derivation relation modulo \(3^n\), while forgetting the arbitrary choices killed by the established relation-jet gauge.

**Important scope condition.** This theorem does not assert that an arbitrary finite filtered quotient or arbitrary finite graded carrier is such a \(J_n\). It applies to the compatible full filtered relation-jet tower defined with this information content.

---

## 3. Universal finite-level extraction map

For a candidate character

\[
\rho:G\to(\mathbf Z/3^n)^\times
\]

whose reduction modulo 3 is trivial, consider the \(\rho\)-crossed derivation condition

\[
D(gh)=D(g)+\rho(g)D(h).
\]

Evaluating this condition on the defining filtered relation gives a linear coefficient functional on the degree-one values

\[
(f_1,f_2,f_3,f_4).
\]

By construction of \(J_n\), this functional depends only on the finite-level relation datum and \(\rho\bmod3^n\). Denote it by

\[
\mathcal C_n(J_n,\rho)\in
\operatorname{Hom}_{\mathbf Z/3^n}
(V,\mathbf Z/3^n),
\qquad
V=G/G_2.
\]

Define

\[
\Phi_n(J_n)
=
\left\{
\rho\in\operatorname{Hom}(G,(\mathbf Z/3^n)^\times):
\mathcal C_n(J_n,\rho)=0
\right\}.
\]

The zero condition is intrinsic because the degree-one relation-module gauge term is annihilated by \(V^*\), exactly as in the already closed degree-(2,3) projective-jet audit.

---

## 4. Finite-level uniqueness calculation

For the frozen q=3 relation, write

\[
r_i=\rho(x_i).
\]

The exact crossed-derivation calculation gives, after the three auxiliary coefficients are imposed,

\[
r_1=r_3=r_4=1,
\]

and the remaining coefficient equation is

\[
1+2r_2=0
\pmod{3^n}.
\]

Since \(2\) is a unit modulo \(3^n\), this has the unique solution

\[
r_2=-2^{-1}=(1-3)^{-1}
\pmod{3^n}.
\]

Therefore

\[
\boxed{
\Phi_n(J_n)=\{\chi_n\}.
}
\]

This proves the finite-level uniqueness statement for every \(n\ge2\).

For the first levels,

\[
\chi_2(x_2)=4\pmod9,
\]

\[
\chi_3(x_2)=13\pmod{27},
\]

\[
\chi_4(x_2)=40\pmod{81},
\]

\[
\chi_5(x_2)=121\pmod{243},
\]

and

\[
\chi_n(x_i)=1\quad(i\ne2).
\]

---

## 5. Compatibility

The reduction map

\[
\mathbf Z/3^{n+1}\to\mathbf Z/3^n
\]

sends

\[
1+2r_2=0\pmod{3^{n+1}}
\]

to

\[
1+2r_2=0\pmod{3^n}.
\]

The same is true for the three equations forcing \(r_1,r_3,r_4\) to equal \(1\).

Hence

\[
\chi_{n+1}\bmod3^n=\chi_n.
\]

Equivalently, the extraction maps commute with truncation:

\[
\boxed{
\Phi_n\circ\pi_{n+1,n}
=
\operatorname{red}_{n+1,n}\circ\Phi_{n+1}
}
\]

on the compatible tower.

Thus the family

\[
(\chi_n)_{n\ge2}
\]

is an element of the inverse system

\[
\varprojlim_n
\operatorname{Hom}(G,(\mathbf Z/3^n)^\times).
\]

---

## 6. Inverse-limit reconstruction

Because

\[
\mathbf Z_3^\times
\cong
\varprojlim_n(\mathbf Z/3^n)^\times,
\]

a compatible family \((\chi_n)_n\) determines a unique continuous character

\[
\chi:G\to\mathbf Z_3^\times
\]

whose reduction modulo \(3^n\) is \(\chi_n\) for every \(n\).

Therefore

\[
\boxed{
(J_n)_{n\ge2}
\longmapsto
(\chi_n)_{n\ge2}
\longmapsto
\chi
}
\]

is well-defined and unique.

For the frozen q=3 group,

\[
\boxed{
\chi(x_2)=(1-3)^{-1},
\qquad
\chi(x_1)=\chi(x_3)=\chi(x_4)=1.
}
\]

---

## 7. What has actually been proved

The theorem-level conclusion is:

> **Finite-level factorization / inverse-limit theorem.**
> For the frozen rank-4 q=3 Demuškin presentation, once the compatible full filtered relation-jet tower \( (J_n)_{n\ge2} \) is supplied in the sense of §2, the canonical orientation reductions factor through the finite levels:
> \[
> J_n\mapsto\chi_n\in(\mathbf Z/3^n)^\times,
> \]
> the maps are compatible under truncation, and their inverse limit is the canonical
> \[
> \chi:G\to\mathbf Z_3^\times.
> \]

The proof uses only:
1. the intrinsic crossed-derivation characterization of the canonical orientation;
2. the exact finite-level coefficient equations;
3. uniqueness of the solution modulo \(3^n\);
4. compatibility under reduction;
5. completeness of \(\mathbf Z_3^\times\) as the inverse limit of its finite quotients.

---

## 8. Critical boundary — no overclaim

This theorem does **not** prove either of the following:

1. that the projective degree-(2,3) jet \(J_3\) alone determines all higher \(\chi_n\);
2. that there exists a single bounded-degree finite carrier from which the whole inverse system can be reconstructed.

Those remain separate OPEN questions.

It also does not prove a categorical absolute minimality theorem for \(J_3\).

The theorem closes only the previously identified logical gap: **full compatible tower \(\Rightarrow\) finite-level reductions \(\Rightarrow\) inverse-limit character.**

---

## 9. Decision

**PASS / THEOREM CLOSED at the stated information level.**

The finite-level factorization and inverse-limit step is now explicit. The remaining substantive questions are minimality and whether a bounded-degree finite carrier can already determine the entire 3-adic character.
