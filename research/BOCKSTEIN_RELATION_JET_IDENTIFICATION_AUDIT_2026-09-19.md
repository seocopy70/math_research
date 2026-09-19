# Bockstein–relation-jet identification audit — 2026-09-19

## Gate
Determine whether the intrinsic Bockstein
\[
\beta:H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3)
\]
identifies, under transgression, with the restricted-cubic/power component \(p(P_3)\) of the degree-(2,3) filtered relation jet.

## Pre-check

**Object.** For a minimal one-relator pro-3 presentation \(1\to R\to F\to G\to1\), with
\[
r=(R_2,P_3)+O(4),
\]
compare the Bockstein tensor with the degree-3 power functional determined by \(P_3\).

**Input.** Only the intrinsic coefficient sequence
\[
0\to\mathbf F_3\xrightarrow{3}\mathbf Z/9\to\mathbf F_3\to0
\]
and the filtered relation class; no q-label is inserted into the definition.

**Functoriality.** Transgression identifies \(H^2(G,\mathbf F_3)\) with the dual of the mod-3 relation module. Cup product gives the quadratic relation component. The Bockstein is natural.

**Gauge.** Changing the generator of \(H^2\) rescales both the quadratic and Bockstein coordinates by the same unit. A presentation/lift change changes the cubic jet by the standard \([v,R_2]\) gauge term, which is invisible to degree-one evaluation.

**Orientation bridge.** The previously established recovery functional
\[
\Theta(\lambda)(f)=f(p)+(\lambda\wedge f)(R)
\]
requires the Bockstein-derived \(p\) to agree with \(p(P_3)\), up to the common projective scalar.

## 1. Transgression calculation

### 1.1 Convention synchronization: cup product and Bockstein

A crucial normalization point is that the cup-product coefficient and the Bockstein coefficient must be read in the **same transgression/fundamental-class convention**. It is not sufficient to say that the Bockstein is defined only up to an independent projective sign.

If the degree-2 and p-power coefficients of the relator are written as (a_{ij}) and (a_i), then in one fixed standard trace/transgression convention the corresponding formulas have the same global sign:
\[
\operatorname{tr}(\chi_i\cup\chi_j)=-a_{ij},
\qquad
\operatorname{tr}(\beta\chi_i)=-a_i.
\]
Changing the generator of the one-dimensional (H^2) line rescales both tensors simultaneously. Thus the projective pair ([(R,p)]) is unaffected, while an isolated replacement (p\mapsto-p) with (R) fixed is **not** an allowed gauge transformation.

The literature formula supplies the general identification; the frozen relator is independently checked below by a direct (mathbf Z/9)-lifting obstruction calculation.

For a minimal one-relator pro-p presentation, the standard five-term/transgression sequence gives
\[
0\to H^1(G,\mathbf F_p)\to H^1(F,\mathbf F_p)
\to H^1(R,\mathbf F_p)^F
\xrightarrow{\mathrm{tr}}H^2(G,\mathbf F_p)\to0.
\]
Since there is one relation, transgression identifies the one-dimensional relation-dual line with \(H^2(G,\mathbf F_p)\).

The quadratic cup-product pairing is the dual form of the degree-2 initial relation. This is the standard relation–cup correspondence for one-relator pro-p groups.

For the Bockstein, take a basis \(f_i\) of \(H^1(G,\mathbf F_p)\) dual to generators \(x_i\). The connecting homomorphism for
\[
0\to\mathbf F_p\to\mathbf Z/p^2\to\mathbf F_p\to0
\]
measures the obstruction to lifting \(f_i\) to a \(\mathbf Z/p^2\)-valued homomorphism. Under transgression, this obstruction is exactly the coefficient of the \(x_i^p\) term in the relator modulo the next filtration level, up to the convention-dependent global sign.

Equivalently, if
\[
P_p=\sum_i a_iX_i^{[p]}+C_p,
\]
where \(C_p\) lies in the commutator part of the degree-p restricted Lie piece, then
\[
\beta(f_i)=\pm a_i\,\omega
\]
after identifying the one-dimensional relation-dual line with \(H^2\). The sign depends only on the chosen transgression/fundamental-class convention and is common to the whole Bockstein vector.

This is the precise point at which the restricted-cube/Frobenius twist enters: the coefficient vector is naturally in \(V^{(1)}\), not an untwisted copy of \(V\).

### 1.2 Direct (mathbf Z/9) check for the frozen relator

For
\[
r_3=x_1^3[x_1,x_2][x_3,x_4],
\]
let (widetilde f_i:F\tomathbf Z/9) be the lift of the mod-3 generator (f_i). The Bockstein obstruction is represented by the relator value divided by (3).

For (f_1),
\[
widetilde f_1(x_1^3)=3,
\]
while each commutator has zero exponent sum under an abelian target:
\[
widetilde f_1([x_1,x_2])=
widetilde f_1([x_3,x_4])=0.
\]
Hence
\[
\frac{widetilde f_1(r_3)}3\equiv1\pmod3.
\]
For (i=2,3,4), the power term contributes zero and the commutators again have zero exponent sum, so
\[
\frac{widetilde f_i(r_3)}3\equiv0\pmod3.
\]
This independently verifies, for the frozen presentation,
\[
\beta(f_1)=\pm\omega,qquad
\beta(f_2)=\beta(f_3)=\beta(f_4)=0,
\]
with the sign fixed only after the same transgression/fundamental-class convention is chosen. Therefore the Bockstein coefficient vector agrees with (p(P_3)=X_1^{(1)}) projectively, without relying on the general formula alone.

## 2. Application to the frozen q=3 relation

For
\[
r_3=x_1^3[x_1,x_2][x_3,x_4],
\]
the degree-3 filtered component has power part
\[
P_3=X_1^{[3]}
\]
and therefore
\[
p(P_3)=X_1^{(1)}
\]
up to the same global scalar/convention sign.

Hence the intrinsic Bockstein has
\[
p_\beta\sim X_1^{(1)}.
\]

For the q=\infty control relation
\[
r_0=[x_1,x_2][x_3,x_4],
\]
there is no degree-3 power term, so
\[
p(P_3)=0,
\qquad
\beta=0
\]
for the first Bockstein layer in the frozen basis.

Thus the Bockstein identifies the power direction, not the scalar 4 mod 9.

## 3. Hand recovery check

With
\[
R=[X_1,X_2]+[X_3,X_4],
\qquad
p=X_1^{(1)},
\]
the previously audited functional is
\[
\Theta(\lambda)(f)=f(p)+(\lambda\wedge f)(R).
\]
Writing \(\lambda=(a_1,a_2,a_3,a_4)\) and evaluating on the dual basis gives
\[
a_1=0,\qquad 1-a_2=0,\qquad a_3=0,\qquad a_4=0
\]
in \(\mathbf F_3\), hence
\[
\lambda=e_2^*.
\]
The corresponding orientation character is
\[
\chi(x_1),\chi(x_2),\chi(x_3),\chi(x_4)
\equiv(1,4,1,1)\pmod9.
\]

The calculation uses the projective pair, so the common scalar ambiguity in \((R,p)\) does not affect the zero set.

## 4. Independent literature cross-check

The standard Demushkin/one-relator literature confirms two ingredients used here:

1. transgression identifies the one-dimensional relation-dual line with \(H^2\);
2. the degree-2 initial relation determines the cup-product pairing.

The Bockstein is the standard operator detecting the p-power coefficients of a one-relator presentation. This agrees with the present identification of the power direction.

The literature check is a methodological validation, not a substitute for the convention/sign synchronization and the direct (mathbf Z/9) calculation above. The final manuscript should cite the precise one-relator transgression/Bockstein source rather than hide the identification behind “standard calculation”.

## 5. Critical boundary

The audit establishes the identification only up to the common scalar/sign inherent in the choice of transgression generator of \(H^2\). That is sufficient for the projective carrier \([(R,p)]\) and for the zero-set reconstruction.

It does **not** provide a canonical absolute representative \(p\) without choosing a generator of \(H^2\), nor does it produce higher 3-adic digits.

## Decision

**PASS / CLOSED for the projective mod-9 identification, under the standard one-relator transgression/relation–Bockstein formula, with the cup/Bockstein convention synchronization explicitly stated and independently checked for the frozen relator.**

More precisely:

- intrinsic pair \((\smile,\beta)\): **PASS**;
- \(\beta\leftrightarrow p(P_3)\) projectively: **PASS / CLOSED** under the standard transgression formula, with the same global sign convention as the cup-product coefficient and an independent frozen-relator \(\mathbf Z/9\) check;
- absolute sign/normalization of \(p\): **CONDITIONAL / gauge-dependent**;
- \((\smile,\beta)\to\chi\bmod9\): **PASS / CLOSED** at the stated projective degree-(2,3) level;
- no broad scan is authorized.

## Literature anchors

The relation–cup correspondence and transgression for one-relator pro-p groups are documented in the standard Demushkin literature; see the cited sources recorded in the research session. The Bockstein/power-coefficient formula is the classical one-relator transgression calculation and should be cited explicitly in the final manuscript. The present audit should be described as “standard formula + direct frozen-relator lift check”, not as a new general cochain proof.
