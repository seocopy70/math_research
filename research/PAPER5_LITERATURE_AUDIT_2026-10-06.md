# Paper 5 Literature Audit — 2026-10-06

## Scope

Four-gate literature audit for the novelty boundary of Paper 5:
(A) finite Zassenhaus windows, (B) relation module/initial forms, (C) IA/Frattini image, (D) the observed p^2 automorphism-order phenomenon.

## Audit result

General background is established in the literature: Jennings–Lazard Zassenhaus filtration and its restricted-Lie graded object; free pro-p / Magnus–Zassenhaus machinery; Labute initial forms, relation ideals and mildness; general IA/Frattini-kernel facts; and filtration actions/module decompositions.

No prior result was identified that proves, for the specific finite window
\[
W_n=F/(R D_{n+1}),
\]
the intrinsic factorization
\[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(W_n/\Phi(W_n)))
\]
through the relevant mixed degree-(2,p) relation-jet stabilizer and derives the observed p^2 order deficit.

### Gate A — finite Zassenhaus quotients

Prior work covers the definition and graded structure of the Zassenhaus filtration and dimension calculations for finite layers. No identified source gives the specific automorphism calculation for the present W_p.

### Gate B — relation module / initial form

Labute-style initial-form and strongly-free machinery is established. The present relation package mixes degree 2 and degree p:
\[
[x,z],\quad [y,z],\quad [x,y]^{-1}x^p z^{-p}.
\]
No identified source gives the corresponding finite-window relation-jet stabilizer calculation.

### Gate C — IA / Frattini image

IA as the kernel of the Frattini/abelianized linear action is standard. The specific intrinsic W_p computation is not identified in the literature.

**Critical correction:** the current corrected W_p calculation is
\[
D_p(W_p)\cong \mathbf F_p^3,
\qquad
IA(W_p)\cong \operatorname{Hom}(\mathbf F_p^3,\mathbf F_p^3)\cong \mathbf F_p^9,
\]
not \(\mathbf F_p^6\). Consequently
\[
|\operatorname{Aut}(W_p)|=p^{11}(p-1)^2.
\]
The earlier \(\mathbf F_p^2/\mathbf F_p^6\) package is FAIL/CLOSED/SUPERSEDED.

### Gate D — p^2 gap

No identified source gives the specific p^2 automorphism-order deficit for the present finite Zassenhaus windows. The W_p image restriction is a separate boundary calculation; the actual p^2-gap theorem remains to be established at W_{p+1}.

## Novelty boundary

**PASS / CLOSED for the literature audit, within the searched scope:** the specific W_p automorphism calculation and the proposed intrinsic finite-window relation-jet mechanism were not found as prior results.

**OPEN / LOAD-BEARING:** the general odd-p W_{p+1} factorization theorem and p^2 automorphism-order theorem.

## Next gate

Independent verification of the corrected W_p calculation, then intrinsic analysis of
\[
W_{p+1}
\]
and its first new relation-jet layer
\[
D_{p+1}/D_{p+2}.
\]

The literature audit does not license claiming that the entire p^2 phenomenon is new; it establishes only the searched novelty boundary stated above.
