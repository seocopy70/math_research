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


## 8. Critical correction — the proposed Tor-annihilator carrier is invalid as stated

The preceding Section 7 is **FAIL / CLOSED and superseded**.

The proposed object
\[
\mathcal A(W)=\operatorname{Ann}_{H^1(W,\mathbf F_p)}(\operatorname{Tor}(W^{ab}))
\]
cannot serve as a nonzero carrier when W is a finite p-group. Indeed W^{ab} is itself a finite p-group, hence
\[
\operatorname{Tor}(W^{ab})=W^{ab}.
\]
But
\[
H^1(W,\mathbf F_p)\cong\operatorname{Hom}(W^{ab},\mathbf F_p),
\]
and the evaluation pairing between H^1(W,F_p) and W^{ab} is nondegenerate on the finite elementary-p quotient. Therefore a character that annihilates all of Tor(W^{ab}) is the zero character:
\[
\operatorname{Ann}_{H^1(W,\mathbf F_p)}(W^{ab})=0.
\]

So the earlier claim

> intrinsic character carrier A(W): PASS / CLOSED

is false.

The abelianization calculation written above does not rescue it. At the critical window the abelianization is finite, so every class is torsion in the ordinary abelian-group sense. The intended distinction was evidently between different pieces of a presentation-level or pro-p abelianization before finite truncation; that distinction was not encoded in the stated abstract finite-window object.

### Consequence

The successful marked character cannot currently be promoted to an intrinsic character carrier by this construction.

The valid result remains only:

- marked E_psi quadratic separator: **PASS / CLOSED**;
- distinguished single-psi abstract bridge: **FAIL / CLOSED**;
- proposed Tor-annihilator carrier: **FAIL / CLOSED**;
- orbit/groupoid-valued extension defect: **OPEN / LOAD-BEARING**.

A replacement carrier must be built from an actually nontrivial intrinsic structure of the finite window (for example a canonical filtration quotient, Bockstein/extension datum, or a functorially defined character subset), not from ordinary torsion annihilation of W^{ab}.

This correction is a substantive mathematical correction, not merely a wording change.


## 2026-10-04 — critical review: proposed Sp-orbit closure is NOT certified

The proposed conclusion r in D_2\D_3 -> Sp-orbit of psi is a single intrinsic orbit -> abstract same-window separation is **FAIL / CLOSED as a proof route**. Four independent gaps were identified.

1. **Degenerate quadratic forms exist.** For odd p, D_2/D_3 is the alternating square. r_2=[x_1,x_2] in rank 4 is nonzero but rank 2, with radical <X_3,X_4>. Its stabilizer is not full Sp_4 and is not transitive on all nonzero character directions. Thus r in D_2\D_3 does not imply a nondegenerate symplectic space, and the exponent s is unrelated to the rank of B.

2. **Transitivity is insufficient for separation.** Even for a nondegenerate 2m-dimensional B, Sp_{2m} transitivity on nonzero vectors only removes a representative choice. It does not construct an intrinsic defect whose value differs for s and t.

3. **B is not shown to be recoverable from W.** The quotient map G_s(r)->W does not canonically retain the original free presentation, generators, or r_2 in D_2/D_3. Intrinsic recovery must be constructed from canonical data of W itself and proved to factor the marked B.

4. **Equivariance does not compare unrelated windows.** Sp-equivariance of marked constructions under automorphisms of one presentation does not establish equality of an intrinsic defect across the s and t windows.

Correct classification: marked affine quadratic separator **PASS / CLOSED**; single-character intrinsic bridge **FAIL / CLOSED**; torsion-annihilator carrier **FAIL / CLOSED**; nondegenerate symplectic special case **CONDITIONAL** and still insufficient for unmarked separation; general Sp-orbit bridge **FAIL / CLOSED as stated**; intrinsic orbit/groupoid defect **OPEN / LOAD-BEARING**; abstract same-window separation **OPEN**.


## 2026-10-04 — refinement: the higher-jet critical pair is genuinely separated, but is not exponent-same-family separation

For the exploratory pair
\[
r_A=[x_1,x_2],\qquad r_B=[x_1,x_2]x_1^{p^m},
\]
the previously proposed \(\operatorname{Aut}(F)\)-orbit argument is unnecessary and too strong. The separation at the first window where the added tail becomes visible has a direct intrinsic certificate from abelianization.

Indeed, for \(n=p^m\), the added factor \(x_1^{p^m}\) lies in \(D_{p^m}(F)\), so
\[
W_{p^m}(G_A)\cong W_{p^m}(G_B).
\]
At \(n=p^m+1\), the abelianization of the free truncated quotient retains the class of \(x_1^{p^m}\):
\[
W_{p^m+1}(G_A)^{ab}\cong(\mathbf Z/p^{m+1})^4,
\]
whereas the relation for \(G_B\) imposes \(p^m x_1=0\), giving
\[
W_{p^m+1}(G_B)^{ab}\cong
\mathbf Z/p^m\oplus(\mathbf Z/p^{m+1})^3
\]
(up to the displayed choice of basis). Hence
\[
W_{p^m}(G_A)\cong W_{p^m}(G_B),qquad
W_{p^m+1}(G_A)\not\cong W_{p^m+1}(G_B).
\]
This is a valid **PASS / CLOSED Zassenhaus-critical higher-jet separation**.

However, it does not compare \(G_s(r)\) and \(G_t(r)\) for one fixed relation \(r\). It therefore does not close the exact unmarked same-window problem of the control family. Its significance is narrower: a finite window can intrinsically detect a higher filtered tail at its first visible degree, even when the quadratic initial form is unchanged.

The earlier claim that this proves or disproves recovery of the marked E_\psi parameter \(s\) is not valid. The marked parameter is target-indexed; the higher-tail degree \(m\) is a property of the chosen relator.


## 2026-10-04 — critical audit correction: higher-jet argument does not close the unmarked problem

The exploratory conclusion was over-promoted in the final session analysis.

1. For (r_A=[x_1,x_2]), (r_B=r_Ac) with (c\in D_3\setminus D_4), one cannot infer (W_{p^m}(G_A)cong W_{p^m}(G_B)) for (p^m>3). The filtration is descending:
[
D_{p^m}\subset D_3,
]
so (c\in D_3) does not imply (c\in D_{p^m}).

2. The valid generic observation is only:
[
c\in D_k Longrightarrow 	ext{the two relators have the same image in }F/D_k.
]
This yields equality of the corresponding quotient presentations modulo (D_k), but not automatic abstract non-isomorphism at (k+1).

3. The argument that an automorphism cannot send a leading degree-2 relator to degree-2 plus degree-3 is invalid. IA automorphisms act trivially on abelianization while changing higher commutator terms; Magnus' commutator-transvection generators provide explicit higher-term modifications. Therefore a separation claim must compute the actual automorphism orbit, not merely compare filtered degrees. External verification: standard descriptions of IA generators (x_imapsto x_i[x_j,x_k]) confirm this mechanism. 

4. Consequently the proposed theorem
[
c\in D_k\setminus D_{k+1}
Rightarrow W_k	ext{ same and }W_{k+1}	ext{ non-isomorphic}
]
is **FAIL/CLOSED as stated**.

5. The claim that the marked E_psi theorem has abstract content “exactly (B)” is also too strong. The verified statement is weaker: the marked theorem supplies a quadratic marked separator; the target parameter (s) is externally chosen in (E_s), and no intrinsic bridge from an abstract finite window to that marked package has been established.

### Correct boundary

- marked quadratic E_psi theorem: **PASS/CLOSED (marked)**;
- higher-tail pair (r_A=[x_1,x_2]), (r_B=[x_1,x_2]x_1^{p^m}): **PASS/CLOSED** for its stated abelianization separation;
- generic filtered-tail critical separation theorem: **FAIL/CLOSED as stated**;
- abstract recovery of (s) / (G_s(r)) versus (G_t(r)) same-window separation: **OPEN/LOAD-BEARING**;
- intrinsic orbit/groupoid affine defect: **OPEN/LOAD-BEARING**.
