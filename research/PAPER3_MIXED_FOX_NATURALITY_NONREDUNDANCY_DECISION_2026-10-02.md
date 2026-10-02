# MIXED FOX — NATURALITY CLOSURE AND NON-REDUNDANCY DECISION — 2026-10-02

## 0. Executive result

The remaining "morphism-level naturality" objection is narrower than previously stated.

At the only morphism level required for an intrinsic finite carrier—filtered finite-pair **isomorphisms**—the Demuškin classification supplies the missing lift. Thus the Mixed Fox construction descends from the canonical Demuškin pair to a projective finite object **up to canonical isomorphism class**.

The full statement for arbitrary non-invertible pair morphisms remains open and is not needed to establish presentation/gauge-independent intrinsicity.

A separate correction is mandatory: the earlier audit treated the case q=N_k. In the declared odd-p Demuškin family q is p^s or 0, whereas
\[
N_k=p^{k-1}+1
\]
is not a p-power. Hence q=N_k is impossible. The boundary case is vacuous and must not be used as evidence.

## 1. Correct reconstruction theorem

Let p be odd, d fixed, and
\[
N=N_k=p^{k-1}+1.
\]
For standard infinite Demuškin groups,
\[
q\in\{p,p^2,p^3,\ldots\}\cup\{0\}.
\]

If q<N, then q=p^s with s<k, and the first q-dependent Zassenhaus graded defect occurs below N. Hence Q_k determines q.

If q>=p^k, then q>N. The q-power term is invisible through D_{N+1}; all such q, together with q=0, produce the same truncated standard window.

There is no q=N case.

Therefore:
\[
(Q_k,A_k)
\quad\Longrightarrow\quad
[E_k\to Q_k]
\]
up to extension-window isomorphism, with the reconstruction reduced to the two genuine q-ranges:
\[
q<p^k
\quad\text{or}\quad
q\ge p^k/ q=0.
\]

The external literature supports the underlying classification: infinite Demuškin groups are classified by rank and q, with the odd-p one-relator form
\[
x_1^q[x_1,x_2][x_3,x_4]\cdots.
\]
Labute's classification is recorded in modern literature. citeturn0search4turn1search0

## 2. Morphism-level lift for isomorphisms

Suppose two declared finite pairs are isomorphic:
\[
(Q_k(G),A_k(G))\cong(Q_k(H),A_k(H)).
\]

The isomorphism Q_k(G)≅Q_k(H) gives
\[
\dim_{\mathbf F_p}H^1(Q_k(G),\mathbf F_p)
=
\dim_{\mathbf F_p}H^1(Q_k(H),\mathbf F_p),
\]
hence the same Demuškin rank d.

The pair-level reconstruction above gives the same q-regime:
- q<p^k is recovered by the first intrinsic graded defect;
- q>=p^k (or q=0) is the single truncated regime.

Thus G and H have the same classification invariants at the precision relevant to the window. In the q<p^k regime they have the same q; in the q>=p^k regime their windows are already isomorphic.

Consequently there exists an extension-window isomorphism
\[
\mathsf W_k^{ext}(G)\cong\mathsf W_k^{ext}(H).
\]

The Mixed Fox projective object is invariant under such an extension-window isomorphism because:
1. group-algebra isomorphisms induce isomorphisms of augmentation ideals and mixed maximal ideals;
2. relation modules are transported by the induced presentation-equivalent Fox/Lyndon maps;
3. Nielsen changes act by invertible Fox Jacobians;
4. relation-generator changes and relator conjugation act by units/invertible gauge;
5. projectivization removes these gauge factors;
6. truncation modulo the mixed maximal-ideal power is functorial under the induced filtered algebra isomorphism.

Therefore the mixed Fox object is constant up to projective isomorphism on every isomorphism fiber of the finite pair.

## 3. Important categorical boundary

This proves the statement actually needed for **intrinsicity**:
\[
W_k(G)\cong W_k(H)
\Longrightarrow
\mathcal M_k^{mix}(G)\cong
\mathcal M_k^{mix}(H).
\]

It does NOT prove a functor for arbitrary non-invertible homomorphisms of bare pairs. Such morphisms need not lift to morphisms of the Demuškin extension windows, and no such lifting theorem has been established.

Hence the correct classification is:

- filtered finite-pair isomorphism covariance: **PASS / CLOSED**;
- arbitrary Pair_k morphism functoriality: **OPEN / OUTSIDE CURRENT INTRINSICITY NEED**.

This corrects the previous overstatement that full categorical naturality was still load-bearing for the carrier's basic well-definedness.

## 4. Consequence for finite-pair factorization

At the declared standard Demuškin scope, the chain is now:

\[
G
\longmapsto
W_k(G)
\longmapsto
\mathsf W_k^{ext}(G)
\longmapsto
\mathcal M_k^{mix}(G),
\]

with each arrow well-defined up to the relevant isomorphism/projective gauge.

Thus the original finite-pair factorization is:

\[
\boxed{
W_k
\longmapsto
[\mathcal M_k^{mix}]
}
\]

**PASS / LOCAL**, promoted from the previous extension-window-only status.

The weighted Magnus estimate remains the bridge showing that this finite object represents the intended precision-k mixed jet; the Zassenhaus-dimension literature independently controls the finite Demuškin filtration data. citeturn0academia23

## 5. Non-redundancy attack

Now the decisive point.

Within the declared fixed-rank standard Demuškin family, the finite extension window has no hidden continuous parameter beyond the discrete q-classification data at this precision:

- q=p^s with s<k gives a distinct q-regime visible below N_k;
- q>=p^k and q=0 collapse to the same window.

Therefore any isomorphism-invariant finite carrier constructed solely from this canonical window can only distinguish the same finite q-regimes already distinguished by the completed Kummer/orientation selector.

The mixed Fox carrier may be a different *representation* of that information, but this alone is not a new recognition theorem.

In particular, extracting chi mod p^k from the Mixed Fox object by first recovering q and then applying the known Demuškin classification is explicitly **classification repackaging**, not a new orientation bridge.

Hence:

\[
\boxed{
\text{Mixed Fox as a new recognition carrier}
=
\textbf{FAIL / CLOSED — REDUNDANT}
}
\]

at the declared standard fixed-rank Demuškin scope.

This does not say the Fox construction is mathematically false or useless. It says it does not survive the project's non-redundancy gate as a new finite recognition theorem.

## 6. What survives

The following remain valid local mathematical statements:

1. The mixed (3,I)-adic Fox relation jet has a legitimate finite extension-window formulation.
2. The Demuškin restricted pair determines that window up to isomorphism class.
3. The projective Fox construction is invariant under the relevant finite-window isomorphism/gauge operations.
4. Therefore a finite-pair, projective Mixed Fox object is well-defined up to isomorphism at the declared scope.

What does **not** survive as a new theorem is the claim that this produces a genuinely new selector of the canonical orientation residue.

## 7. Research decision

The Mixed Fox branch is now closed as a candidate for a **genuinely new finite recognition carrier**.

Classification:
- admissible Demuškin category: **PASS / CLOSED**;
- pair → extension-window reconstruction: **PASS / CLOSED**, corrected to the genuine q-ranges;
- finite-pair isomorphism covariance: **PASS / CLOSED**;
- finite-pair → projective Mixed Fox object: **PASS / LOCAL**;
- arbitrary non-invertible Pair_k functoriality: **OPEN**, but not load-bearing for intrinsic isomorphism-class carrier status;
- Mixed Fox orientation recognition as a new result: **FAIL / CLOSED — REDUNDANT**;
- genuinely new carrier: **OPEN**, because this branch is now closed and another carrier would be required.

## 8. Stop

Do not:
- reopen the q=N_k case;
- compute W_11/W_12;
- perform a large Fox scan;
- reprove Paper 2;
- use classification q→chi as a purported new bridge.

The next authorized research branch is a genuinely different finite-input carrier, subject to the standing tests:
Object → Input → Functoriality → Gauge → Orientation bridge → q-blindness → Separation → Novelty → Stop.

