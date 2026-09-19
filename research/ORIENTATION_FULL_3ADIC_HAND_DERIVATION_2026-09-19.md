# ORIENTATION — FULL 3-ADIC LIFT AFTER MOD-9 — HAND DERIVATION — 2026-09-19

## Objective

Determine whether the successful degree-(2,3) relation-jet recovery can be pushed to the full canonical orientation character for the frozen rank-4 q=3 Demushkin group, without another finite scan.

## 1. Correct commutator convention

Use the standard convention
\\[
[x,y]=x^{-1}y^{-1}xy.
\\]

For a character
\\[
\rho:G\to 1+3\mathbf Z_3
\\]
and a crossed derivation
\\[
D(gh)=D(g)+\rho(g)D(h),
\\]
write r_i=\rho(x_i) and f_i=D(x_i).

Evaluating the defining relation
\\[
r=x_1^3[x_1,x_2][x_3,x_4]
\\]
gives four coefficient equations. Up to multiplication by units coming from the commutator denominators, they are

\\[
C_1=1+r_2+r_2+\text{terms involving }(r_1-1),(r_3-1),(r_4-1),
\\]
\\[
C_2\sim r_1-1,qquad C_3\sim 1-r_1,qquad C_4\sim r_1-1.
\\]

More explicitly, after imposing the latter equations,
\\[
r_1=r_3=r_4=1,
\\]
the remaining coefficient is exactly
\\[
C_1=1+2r_2.
\\]

Therefore the condition that arbitrary generator values extend to crossed derivations forces
\\[
1+2r_2=0,
\\]
hence
\\[
\\boxed{r_2=(1-3)^{-1}}.
\\]

This is the exact 3-adic value, not merely a mod-9 approximation.

## 2. Finite truncations

Modulo 3^n the same hand calculation gives
\\[
\\boxed{\rho_n(x_1)=\rho_n(x_3)=\rho_n(x_4)=1,\qquad
\rho_n(x_2)\equiv(-2)^{-1}\pmod{3^n}.}
\\]

The first values are
\\[
\chi(x_2)\equiv4\pmod9,
\\]
\\[
\chi(x_2)\equiv13\pmod{27},
\\]
\\[
\chi(x_2)\equiv40\pmod{81},
\\]
\\[
\chi(x_2)\equiv121\pmod{243}.
\\]

Thus there is no new undetermined 3-adic digit after the mod-9 result: the entire tower is forced by the same relation equation once q=3 is identified.

## 3. Why this does not contradict the earlier mod-9 construction

The mod-9 relation-jet construction recovered the first nontrivial digit intrinsically from the degree-(2,3) coupling.

The full 3-adic lift uses stronger data: the actual filtered relation (equivalently its compatible relation-jet tower), together with the canonical crossed-derivation characterization of the Demushkin orientation.

So the correct distinction is:

- bare associated graded object: insufficient;
- finite degree-(2,3) enriched jet: sufficient for chi mod 9;
- compatible full filtered relation-jet tower: sufficient for the full chi;
- no claim is made that the degree-(2,3) jet alone numerically contains all higher 3-adic digits.

## 4. Intrinsicness

The orientation characterization used here is intrinsic: the canonical Demushkin orientation is characterized by the lifting/1-cyclotomic property, and is functorial under group isomorphisms. The standard Demushkin normal form for q=3 has
\\[
r=x_1^3[x_1,x_2][x_3,x_4]
\\]
and the canonical orientation satisfies
\\[
\chi(x_2)=(1-3)^{-1},qquad
\chi(x_i)=1\ (i\ne2).
\\]

Independent literature confirms this standard formula and the intrinsic uniqueness of the canonical orientation; see the cited Demushkin classification/orientation references in the research record.

## 5. Strong conclusion and boundary

The higher-order question can now be closed in the following precise sense:

\\[
\\boxed{
\text{For this rank-4 q=3 Demushkin group, the compatible full filtered relation data
recover the entire canonical }\chi:G\to\mathbf Z_3^\times.
}
\\]

Moreover every finite truncation mod 3^n is determined by the same exact relation equation, so the higher 3-adic digits do not require a new independent invariant at each level.

However, this does **not** prove that a finite low-degree graded carrier such as J_3 alone determines the complete 3-adic character. Nor does it prove an abstract categorical minimality theorem for a finite enrichment.

## Final decision

- Mod-9 recovery from projective degree-(2,3) relation jet: PASS / CLOSED.
- Full 3-adic recovery from the compatible full filtered relation-jet tower: PASS / CLOSED, conditional on the standard intrinsic crossed-derivation characterization of the canonical Demushkin orientation.
- Higher-digit tower as a genuinely new independent obstruction at each level: **not needed** for this q=3 normal form.
- Bare associated graded recovery: FAIL / CLOSED.
- Minimality of the enriched carrier: OPEN as a separate categorical question.

No finite scan was used.
