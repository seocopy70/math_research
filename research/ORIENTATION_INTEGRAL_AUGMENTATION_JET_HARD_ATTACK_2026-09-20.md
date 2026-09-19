# HARD ATTACK 9 — PLAIN \(\mathbf Z_3\)-AUGMENTATION JET \(I^2/I^4\) FAILS AT DEFINITION — 2026-09-20

## Executive verdict

The proposed next object
\[
\mathcal R_3^{\mathbf Z_3}=\langle r-1\rangle\subset I^2/I^4,
\qquad I=\ker(\mathbf Z_3[[F]]\to\mathbf Z_3),
\]
cannot be used as stated.

For the frozen relation
\[
r=x_1^3[x_1,x_2][x_3,x_4],
\]
one has, with \(X_i=x_i-1\),
\[
x_1^3-1=3X_1+3X_1^2+X_1^3.
\]
The commutator product begins in ordinary augmentation degree 2:
\[
[x_1,x_2][x_3,x_4]-1
=
(X_1X_2-X_2X_1)+(X_3X_4-X_4X_3)+O(I^3)
\]
(up to the fixed commutator convention).

Consequently
\[
r-1=3X_1+
\bigl([X_1,X_2]+[X_3,X_4]\bigr)
+O(I^3),
\]
and therefore
\[
\boxed{r-1\notin I^2.}
\]

So the previously proposed \(I^2/I^4\) integral carrier is not merely unproved: its defining class does not exist in the stated quotient.

## 1. Why this matters

Over \(\mathbf F_3\), the term \(3X_1\) disappears and the Zassenhaus degree-2/3 relation jet is well-defined:
\[
R=[X_1,X_2]+[X_3,X_4],
\qquad
P_3=X_1^{[3]}.
\]

Over \(\mathbf Z_3\), ordinary augmentation degree and Zassenhaus degree no longer coincide. The p-power term has a mixed integral expansion
\[
x_1^3-1=3X_1+3X_1^2+X_1^3.
\]

Thus one cannot obtain an exact characteristic-zero degree-(2,3) object simply by replacing the coefficient field \(\mathbf F_3\) by \(\mathbf Z_3\).

This is independent confirmation of the earlier rejection of naive \(\mathbf Z_3\)-scalar extension of the restricted-Lie carrier.

## 2. Correct filtered alternatives

There are two mathematically different repairs.

### A. Return to the mod-3 Zassenhaus filtration

The standard Zassenhaus filtration is defined from the augmentation ideal of
\[
\mathbf F_3[[F]],
\]
not from the ordinary augmentation filtration of \(\mathbf Z_3[[F]]\).

Then
\[
x_1^3-1\equiv X_1^3
\]
in characteristic 3, and the degree-(2,3) carrier \((R,P_3)\) is recovered.

But this necessarily discards the exact 3-adic coefficient information. It cannot by itself produce
\[
-\frac12\in\mathbf Z_3^\times
\]
rather than merely its mod-9 shadow.

This agrees with the already closed bounded finite-information obstruction.

### B. Introduce a mixed \(3\)-adic/Zassenhaus weight

One may instead impose a weighted filtration on \(\mathbf Z_3[[F]]\) in which
\[
\operatorname{wt}(X_i)=1,
\qquad
\operatorname{wt}(3)=2.
\]
Then
\[
3X_1
\quad\text{and}\quad
X_1^3
\]
both have weight 3, while the quadratic commutator relation has weight 2.

For the frozen relation the first terms are therefore
\[
r-1
=
R+
(3X_1+X_1^3+\text{degree-3 commutator terms})
+O_{\mathrm{wt}}(4).
\]

This is a legitimate direction for a mixed integral filtration, but it does **not** immediately give an exact \(\mathbf Z_3\)-valued jet: the associated weight-3 quotient identifies coefficients modulo the next weight and has p-torsion behavior. In particular, the class of \(3X_1\) is not an unrestricted exact 3-adic coefficient.

So this repair may recover the mod-3 p-layer, but it does not automatically recover the full exact Fox equation.

## 3. The decisive exact-information obstruction

The key structural fact is:

> Any finite associated graded piece of a p-adic/Zassenhaus-type filtration is designed to record a finite residue layer. It cannot, by itself, retain the entire exact \(3\)-adic scalar \(-1/2\).

The exact value
\[
-\frac12=1+3+3^2+3^3+\cdots
\]
requires infinitely many compatible 3-adic digits.

Therefore an exact full-\(\chi\) theorem from a **single finite graded jet** would require an additional characteristic-zero coefficient object, not merely a finite associated-graded relation class.

This matches the already established information-theoretic obstruction for bounded degree plus finite coefficient precision.

## 4. Gauge checks for the corrected mixed direction

The earlier expected conjugation formula remains correct at the filtered level. If
\[
r-1=R+P+O_{\mathrm{wt}}(4),
\qquad
u=1+v+O_{\mathrm{wt}}(2),
\]
then
\[
uru^{-1}-1
=
(r-1)+[v,R]+O_{\mathrm{wt}}(4),
\]
so the degree-2/3 pair transforms schematically as
\[
(R,P)\mapsto(R,P+[v,R]).
\]

Likewise, multiplying the relation generator by a scalar/unit changes the pair by the corresponding common leading unit, modulo higher filtration terms.

These calculations support the gauge mechanism, but they do not repair the missing exact characteristic-zero carrier.

## 5. Strong consequence for the current research program

The proposed \(I^2/I^4\) branch must be closed before any computation is expanded.

Correct status:

- plain \(\mathbf Z_3\)-augmentation object \(r-1\in I^2/I^4\): **FAIL / CLOSED — undefined as stated**;
- mod-3 Zassenhaus degree-(2,3) relation jet: **PASS / CLOSED**;
- mixed p-adic/Zassenhaus weighted jet: **OPEN**, but finite graded pieces cannot by themselves contain all 3-adic digits;
- exact universal Fox obstruction scheme: **PASS / CLOSED** as the exact characteristic-zero comparison object, subject to the stated standard Fox/Demuškin hypotheses;
- intrinsic exact two-component filtered compression: **OPEN**;
- bounded finite-information full-\(\chi\) carrier: **FAIL / CLOSED**.

## 6. New research boundary

The previous next target was phrased as

\[
\text{integral }I^2/I^4\text{ relation carrier}
\longrightarrow
\text{Fox row}.
\]

That target is now rejected.

The correct target is narrower and stronger:

\[
\boxed{
\text{intrinsic mod-3 filtered jet tower}
\quad\stackrel{?}{\longrightarrow}\quad
\text{exact Fox orientation locus}
}
\]

with the explicit requirement that the missing 3-adic digits enter through a separately justified inverse-limit or coefficient-lifting mechanism.

Any successful bridge must explain exactly where those digits live. If they are absent from the filtered input, the correct outcome is a no-go theorem rather than a forced construction.

## 7. Literature consistency check

Standard references define the Zassenhaus filtration through the augmentation ideal of the completed \(\mathbf F_p\)-group algebra; this is not the same object as the ordinary augmentation filtration of \(\mathbf Z_p[[F]]\). The distinction is therefore structural, not terminological.

Relevant references:
- Labute, *Classification of Demushkin Groups*, Canadian J. Math. 19 (1967).
- Jennings/Lazard description of the Zassenhaus filtration.
- Quadrelli et al., *Koszul Algebras and Quadratic Duals in Galois Cohomology* (2021), §3.2–3.3, for the completed \(\mathbf F_p[[G]]\) augmentation/Zassenhaus correspondence.

## Final classification

\[
\boxed{\textbf{FAIL / CLOSED}}
\]
for the plain \(\mathbf Z_3\)-augmentation \(I^2/I^4\) proposal.

\[
\boxed{\textbf{OPEN}}
\]
for a genuinely mixed integral filtration together with a non-tautological bridge to the exact Fox scheme.

The failure is useful: it identifies a precise reason why the tempting characteristic-zero analogue of the mod-3 relation jet does not exist in the naive form.
