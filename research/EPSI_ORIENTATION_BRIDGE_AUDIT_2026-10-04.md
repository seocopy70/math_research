# E_psi orientation bridge audit — 2026-10-04

## Verdict

The next load-bearing gate was attacked directly. The result is a sharp split:

- **Single-character canonical orientation bridge: FAIL / CLOSED.**
- **Orbit/groupoid-valued affine package: OPEN.**
- **Abstract unmarked same-window separation for arbitrary r in D_2\\D_3: OPEN.**

The obstruction is not a defect of the affine definition. It is symmetry: in the basic control relation r=[x_1,x_2], the automorphism group contains the natural SL_2(Z_p)-action on the rank-two free factor, and the nonzero order-p characters used by the affine separator form a single nonzero orbit. Hence no individual nonzero character psi can be recovered canonically from the abstract finite window.

This does not rule out an intrinsic *orbit-valued* package. It changes the required bridge: one must recover an invariant set/groupoid of admissible affine characters/representations, or an orbit-invariant defect functional, rather than a distinguished psi.

## 1. Object/Input

At the critical window n=p^s+1, the affine construction uses
A_s=Z/p^{s+1}, U_s=1+p^s A_s
and order-p characters
psi_alpha(x_i)=1+p^s alpha_i,
alpha in F_p^d.

The marked quadratic lemma supplies a pair (psi,delta) with psi(r)=1 and v_p(delta(r))=s for every nonzero r in D_2\\D_3.

The unmarked problem asks whether this data can be recovered from the abstract group W_n(G_s(r)) without a chosen presentation, generator z, or chosen psi.

## 2. Symmetry attack on a canonical single psi

Take the control relation
r=[x_1,x_2]
in rank two.

The determinant-one Nielsen automorphisms of the free rank-two factor preserve the commutator relator up to conjugacy. They therefore induce automorphisms of the corresponding quotient G_s(r), and hence of every finite window W_n(G_s(r)).

On the order-p character space
V=Hom(F,U_s) ~= F_p^2,
these automorphisms induce the standard SL_2(F_p)-action.

For the quadratic form B corresponding to [x_1,x_2], the marked affine lemma says that every nonzero alpha can be paired with a cocycle u giving a nonzero critical translation: the functional
L_B(alpha,u)
is nonzero for alpha != 0, after choosing u appropriately.

Thus the set of successful nonzero characters is SL_2(F_p)-stable and contains a full nonzero orbit. Since SL_2(F_p) acts transitively on V\\{0}, no individual nonzero psi is fixed by the automorphism group.

Therefore:

**No abstractly canonical single character psi can be the orientation bridge in the stated control class.**

This is a genuine no-go, not merely an absence of a proof.

## 3. What remains possible

The no-go is only for a distinguished representative. The following intrinsic objects remain viable:

1. the full automorphism orbit of successful characters;
2. the groupoid of affine representations (rho_{psi,delta}) satisfying the critical valuation condition;
3. an orbit-invariant evaluation ideal/function on the character space;
4. a quotient of the affine package by the natural gauge and automorphism actions.

Any successful unmarked separation theorem must factor through one of these orbit-level objects. A theorem that chooses one psi by a presentation convention is not intrinsic.

## 4. Separation boundary

The above symmetry does **not** prove that
W_{p^s+1}(G_s(r)) ~= W_{p^s+1}(G_t(r))
for some t>s, nor does it prove non-isomorphism.

It only proves that the proposed route
abstract window -> distinguished psi -> affine separator
cannot be made canonical in the control class.

The remaining mathematical question is therefore:

Can an orbit-invariant affine defect be recovered from W_{p^s+1}(G_s(r)) and shown to be present for s but absent for t>s?

This is the correct next gate.

## 5. Classification

| Claim | Status |
|---|---|
| affine E_psi definition | PASS / CLOSED |
| marked quadratic separator | PASS / CLOSED |
| canonical single-psi orientation bridge | FAIL / CLOSED |
| orbit/groupoid-valued orientation bridge | OPEN / LOAD-BEARING |
| abstract same-window separation | OPEN |
| arbitrary-degree degree-only theorem | FAIL / CLOSED |

## 6. Stop rule

Do not search for a preferred generator/character inside the rank-two control class. That would be presentation-dependent and mathematically non-intrinsic.

The next authorized attack is orbit-level: formulate the affine defect as an automorphism/gauge-invariant object of the abstract finite window and test whether that object separates s from t. If no such orbit-level defect exists, close the E_psi formulation at the marked theorem.


## 7. Intrinsic carrier salvage: torsion-annihilator subspace

The single-character no-go suggests replacing a distinguished psi by the canonical subspace
\[
\mathcal A(W)=\operatorname{Ann}_{H^1(W,\mathbf F_p)}(T_W),
\qquad
T_W=\operatorname{Tor}(W^{ab}).
\]

This object is intrinsic to the abstract finite window and contains no presentation label or chosen generator.

For the critical window of G_s(r), write the abelianization of r as
\[
\bar r=p^k a
\]
with a primitive vector a when \bar r\ne0, and k=\infty when \bar r=0. Since r\in D_2, k\ge1.

At n=p^s+1,
\[
W_n(G_s(r))^{ab}
\cong
(\mathbf Z/p^{s+1})^{d+1}/\langle p^s z-p^k a\rangle.
\]

An order-p character with psi(z)=1 on the additive character coordinates replaced by alpha(z)=0 and alpha(a)=0 annihilates T_W in every case k<s, k=s, k>s, and k=\infty. The remaining question is whether alpha can also be chosen so that the nonzero quadratic alternating form B=\rho_2(r) is detected.

Because B\ne0 is alternating, there exists a nonzero alpha in a^perp with B(alpha,-)\ne0. Otherwise a^perp would lie in rad(B), forcing the radical to have codimension at most one, impossible for a nonzero alternating form.

Therefore the marked quadratic separator can be chosen inside the intrinsic carrier \mathcal A(W).

**Classification:** intrinsic character carrier \mathcal A(W): **PASS / CLOSED** as a canonical object; existence of a successful marked affine character inside \mathcal A(W): **PASS / CLOSED** for r\in D_2\\D_3, modulo routine linear-algebra formalization.

This is not yet unmarked separation. For t>s the carrier itself is also present, so the missing information is the orbit-invariant *defect attached to the extension relation*, not the character carrier alone.
