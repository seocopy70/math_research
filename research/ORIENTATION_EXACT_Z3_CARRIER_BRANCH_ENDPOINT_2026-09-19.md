# ORIENTATION — EXACT Z_3 CARRIER BRANCH ENDPOINT — 2026-09-19

## Scope

This record closes the remaining exact-carrier question after the mod-3 coarsest-quotient theorem and the fixed-q=3 exact full-orientation result.

The target was a **non-tautological, finite/concrete exact \(\mathbf Z_3\)-carrier** analogous to the mod-3 compressed pair
\[
\overline J_3=[(R,p(P))].
\]

## 1. Candidate A: naive exact restricted-Lie scalar extension — FAIL / CLOSED

The characteristic-3 restricted Lie quotient
\[
L^{res}_3(V)/[V,L_2(V)]\cong V^{(1)}
\]
cannot simply be promoted from \(\mathbf F_3\) to \(\mathbf Z_3\). Restricted Lie algebras are characteristic-p structures. Therefore an exact carrier obtained by replacing \(\mathbf F_3\) with \(\mathbf Z_3\) in the same formula is not a defined mathematical object.

This route is permanently closed unless a genuinely different characteristic-zero structure is introduced and independently justified.

## 2. Candidate B: finite exact augmentation / filtered truncation — NOT ESTABLISHED

A natural replacement is to work in
\[
\Lambda=\mathbf Z_3[[F]]
\]
with the augmentation filtration and retain an exact finite truncation of the relation class.

This is a legitimate exact filtered object, but the required recovery functional is the frozen crossed-derivation coefficient law, not the mod-3 linear \(\Theta\). The exact coefficient equations contain nonlinear dependence on the orientation values. No proof was obtained that a fixed finite augmentation truncation, by itself, determines the complete exact crossed-derivation evaluation for arbitrary candidate orientations.

In particular, we must not silently identify
\[
\text{finite augmentation jet}
\quad\Longrightarrow\quad
\text{full exact crossed-derivation law}.
\]

The frozen crossed-derivation convention is retained; no alternative convention is introduced to force such a factorization.

Therefore a concrete finite augmentation quotient has **not** been proved sufficient.

## 3. Candidate C: exact evaluation quotient — PASS as a definition, but not a non-tautological compression

Let the exact projective filtered relation carrier be equipped with the independently specified family of finite-level crossed-derivation coefficient evaluations
\[
\mathcal C_n(J,\rho).
\]

Quotienting by the common kernel of all these evaluations gives a canonical evaluation quotient. Its universal property is immediate: it is the coarsest quotient through which the entire prescribed evaluation family factors.

However, this is only mathematically informative if the evaluation family is regarded as part of the independently fixed structure. If the family is defined as “all information needed to recover \(\chi\),” the quotient is tautological.

Thus:

- **PASS:** canonical evaluation quotient exists once the crossed-derivation evaluation structure is fixed independently.
- **FAIL as the desired strengthening:** no non-tautological finite two-component (or similarly concrete finite) description of that quotient has been proved.

## 4. What remains rigorously true

For the frozen q=3 presentation
\[
r=x_1^3[x_1,x_2][x_3,x_4],
\]
the exact intrinsic crossed-derivation calculation gives
\[
\rho(x_1)=\rho(x_3)=\rho(x_4)=1,
\qquad
1+2\rho(x_2)=0,
\]
hence
\[
\chi(x_2)=-\frac12=(1-3)^{-1}.
\]

Therefore the fixed-q=3 exact relation/evaluation carrier recovers the full orientation. This is a **PASS/CLOSED** result.

The compatible finite-level tower also remains **PASS/CLOSED**:
\[
(J_n)_{n\ge2}\Rightarrow(\chi_n)_{n\ge2}\Rightarrow\chi.
\]

The mod-3 compressed carrier remains the coarsest quotient for the separately defined degree-one linear \(\Theta\)-evaluation category:
\[
\overline J_3=[(R,p(P))].
\]

## 5. Final boundary

The exact branch therefore ends with the following sharp separation:

| Question | Status |
|---|---|
| Fixed q=3, exact filtered relation/evaluation data \(\Rightarrow\) full \(\chi\) | **PASS / CLOSED** |
| Full compatible filtered tower \(\Rightarrow\) full \(\chi\) | **PASS / CLOSED** |
| Naive \(\mathbf Z_3\) restricted-Lie analogue of \(([R],p(P))\) | **FAIL / CLOSED** |
| Canonical exact evaluation quotient | **PASS as a defined universal quotient** |
| Non-tautological finite/concrete exact compression analogous to \(([R],p(P))\) | **OPEN / NOT PROVED** |
| Universal bounded-degree + finite-precision carrier for all \(q=3^s\) | **FAIL / CLOSED** |

The important conclusion is not that an exact finite carrier is impossible. The present work establishes that **no such concrete compression has been derived from the available structure without adding a new theorem or a new independently justified characteristic-zero invariant**.

Accordingly, no further scan is warranted for this branch. A future attempt would need a genuinely new structural ingredient, not another finite search over the already audited carriers.

## Decision

**EXACT Z_3 CARRIER BRANCH: CLOSED AT THE CURRENT STRUCTURAL BOUNDARY.**

This closure concerns only the search for a non-tautological concrete exact compression. It does not weaken the fixed-q=3 full-orientation PASS.
