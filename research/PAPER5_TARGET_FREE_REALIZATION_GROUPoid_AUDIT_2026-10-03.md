# PAPER 5 — TARGET-FREE REALIZATION GROUPoid / EXISTENCE GATE AUDIT
## 2026-10-03

### Question

After the target class \(\mathcal C_{d,n}\) has been intrinsically characterized, can the admissible quotient-realization object be defined from the unmarked filtered source \(W_n\) alone, without naming the external Demuškin group \(D\), a canonical kernel, or a marked quotient map?

### Pre-check

**Object.** Define the intrinsic admissible realization groupoid
\[
\mathfrak R^{\mathrm{ad}}_{d,n}(W)
\]
whose objects are epimorphisms
\[
\pi:W\twoheadrightarrow H
\]
such that:

1. \(H\in\mathcal C_{d,n}\);
2. the induced map on \(H^1(-,\mathbf F_p)\) has kernel equal to the intrinsic cup-radical line of \(H^1(W,\mathbf F_p)\).

A morphism \(\pi\to\pi'\) is a pair
\[
(\alpha,\beta),\qquad
\alpha\in\operatorname{Aut}(W),\quad
\beta:H\xrightarrow\sim H',
\]
with \(\beta\pi=\pi'\alpha\).

**Input.** Only the abstract finite filtered group \(W\), its intrinsic Zassenhaus filtration, its mod-p cup pairing, and the target-free class \(\mathcal C_{d,n}\). No external \(D\), \(q\), orientation, chosen generators, or marked quotient kernel.

**Functoriality.** An isomorphism \(f:W\to W'\) transports objects by \(\pi\mapsto\pi f^{-1}\), and transports morphisms by conjugation. Thus \(\mathfrak R^{\mathrm{ad}}\) is functorial up to canonical equivalence.

**Gauge.** Source automorphisms and target isomorphisms are explicitly quotiented through the groupoid morphisms.

**Orientation bridge.** The relative split/non-split Boolean is already invariant under both source automorphisms and target isomorphisms on the declared admissible orbit.

**q-blindness.** \(\mathcal C_{d,n}\) contains no external \(q\); its intrinsic characterization identifies the finite target up to isomorphism and intentionally collapses \(q=0\) with \(q\ge n\).

**Separation.** The earlier C2/W-critical-window orbit theorem supplies the required separation boundary at the quotient-map level: canonical marked-map uniqueness fails, but the admissible two-sided orbit is unique once the target class and radical-line condition are fixed.

**Stop check.** No new carrier, threshold, or blind scan is required. The present gate is a definition/functoriality/existence gate.

---

## 1. Intrinsic definition

The key point is that the target class theorem has removed the external target label.

The predicate
\[
\pi:W\twoheadrightarrow H,qquad H\in\mathcal C_{d,n},
\qquad
\ker H^1(\pi)=\operatorname{Rad}\cup H^1(W,\mathbf F_p)
\]
is now expressed entirely in terms of intrinsic data attached to \(W\), \(H\), and the already characterized class \(\mathcal C_{d,n}\).

Therefore \(\mathfrak R^{\mathrm{ad}}_{d,n}(W)\) is an intrinsic realization groupoid. It is not a choice of a representative quotient map.

This is stronger than the previous conditional formulation “once an external target \(Q_n\) is supplied”.

---

## 2. Existence for the actual critical window

For the declared critical source
\[
W_{d,n}=D^{(0)}_d/D_n(D^{(0)}_d),
\qquad n=p^s+1,
\]
the canonical projection
\[
\pi_0:W_{d,n}\twoheadrightarrow Q_{d,n}=W_{d,n}
\]
(or, in the free-by-Demushkin realization, the previously established admissible quotient to the Demushkin shadow) supplies an object of \(\mathfrak R^{\mathrm{ad}}_{d,n}(W)\).

More generally, in the declared stress family the established critical-window quotient map has the intrinsic cup-radical line as its \(H^1\)-kernel. Since the target-class theorem identifies its target with the unique class \(\mathcal C_{d,n}\), the existence predicate is satisfied.

Thus for the intended source:
\[
\boxed{\mathfrak R^{\mathrm{ad}}_{d,n}(W_{d,n})\neq\varnothing.}
\]

This is an intrinsic existence statement after the target-class reduction. It does **not** claim that an arbitrary finite filtered p-group with the same superficial invariants necessarily has such a realization.

---

## 3. One-component theorem

Let
\[
\pi:W_n\twoheadrightarrow H
\]
be any object of \(\mathfrak R^{\mathrm{ad}}_{d,n}(W_n)\).

By the target-class theorem,
\[
H\cong Q_{d,n}.
\]
Choose an isomorphism \(\beta:H\xrightarrow\sim Q_{d,n}\). Then
\[
\beta\pi:W_n\twoheadrightarrow Q_{d,n}
\]
is an admissible quotient map with the intrinsic radical-line \(H^1\)-kernel.

The critical-window orbit theorem then gives
\[
\beta\pi
=
\phi\circ\pi_0\circ\alpha
\]
for some
\[
\alpha\in\operatorname{Aut}(W_n),
\qquad
\phi\in\operatorname{Aut}(Q_{d,n}).
\]

Hence every object of \(\mathfrak R^{\mathrm{ad}}_{d,n}(W_n)\) is isomorphic, in the realization groupoid, to the canonical object \(\pi_0\).

Therefore
\[
\boxed{\mathfrak R^{\mathrm{ad}}_{d,n}(W_n)
\text{ is nonempty and connected}}
\]
for the declared critical source family.

This is the precise target-free replacement for the impossible canonical marked quotient map.

---

## 4. Factorization of the relative Boolean

Let
\[
\epsilon(\pi)\in\{\mathrm{split},\mathrm{nonsplit}\}
\]
denote the relative extension obstruction attached to an admissible realization \(\pi\).

The obstruction is invariant under:

- precomposition by \(\operatorname{Aut}(W_n)\);
- postcomposition by target isomorphisms;
- replacement of the target by an isomorphic member of \(\mathcal C_{d,n}\).

Since the realization groupoid is connected,
\[
\epsilon(\pi)=\epsilon(\pi_0)
\]
for every object \(\pi\).

Thus the Boolean factors through the intrinsic realization groupoid:
\[
\boxed{
W_n
\longmapsto
\mathfrak R^{\mathrm{ad}}_{d,n}(W_n)
\longmapsto
\{\mathrm{split},\mathrm{nonsplit}\}.
}
\]

This is a genuine factorization statement, not a claim of a canonical marked map.

---

## 5. What has now been closed

The previous two load-bearing questions can be separated sharply.

### Closed

1. **Target class**
   \[
   \mathcal C_{d,n}=\{Q_{d,n}\}
   \quad\text{up to abstract isomorphism}.
   \]

2. **Target-free realization groupoid**
   The admissible realization groupoid can be defined without the external target label.

3. **Existence for the declared critical source**
   The actual \(W_n\) has an admissible realization.

4. **Gauge uniqueness**
   All admissible realizations are in one two-sided orbit.

5. **Boolean realization-independence**
   The relative split/non-split value is constant on the intrinsic realization groupoid.

The combined structural statement is therefore:

\[
\boxed{
W_n
\rightsquigarrow
\mathfrak R^{\mathrm{ad}}_{d,n}(W_n)
\simeq *
\rightsquigarrow
\epsilon_n\in\{\mathrm{split},\mathrm{nonsplit}\}.
}
\]

Here \(\simeq *\) means “nonempty and connected as a groupoid”, not that there is a canonical representative.

---

## 6. What is NOT closed

There is an important remaining logical boundary.

The definition of \(\mathfrak R^{\mathrm{ad}}\) is intrinsic, but it is still an **existential quotient construction**:
\[
\exists\,\pi:W\twoheadrightarrow H
\quad
(H\in\mathcal C_{d,n}).
\]

It does not yet give a presentation-free, finite-internal formula that constructs a specific normal subgroup, a canonical quotient object, or a smaller list of invariants from \(W\).

Therefore the following remain open:

- a canonical characteristic quotient realizing the same target;
- a non-existential finite internal recipe for constructing \(\mathfrak R^{\mathrm{ad}}\);
- a proof that this realization groupoid is **coarsest** among all admissible intrinsic finite realizations;
- an absolute minimality theorem across arbitrary invariant categories.

The C2 no-go prevents replacing the groupoid by a unique marked kernel.

---

## 7. Why this is not a tautological “we just define the quotient”

There is a real reduction here.

Before the target-class theorem, the definition
“quotients \(W\to Q_n\)” used an externally named object \(Q_n\). That was not target-free.

After the target-class theorem, \(Q_n\) is replaced by the intrinsically characterized class \(\mathcal C_{d,n}\). The admissibility condition is likewise intrinsic because the cup-radical line is intrinsic.

Thus the construction no longer imports the answer by naming the target. What remains existential is precisely the **existence of a quotient satisfying an intrinsic predicate**, which is a genuine but weaker reconstruction statement.

The non-tautological next step would be to replace this existential predicate by an internal universal/characteristic construction. That step is not presently proved.

---

## 8. Novelty boundary

The underlying ingredients are classical:

- Demushkin classification;
- nondegenerate cup product;
- Zassenhaus filtration;
- Burnside basis theorem;
- invariance of extension classes under source/target equivalence.

The project-specific structural contribution is their finite-shadow composition:

\[
\boxed{
\text{intrinsic target class}
+
\text{critical-window orbit transitivity}
\Rightarrow
\text{intrinsic connected realization groupoid}
+
\text{factorization of the relative Boolean}.
}
\]

This should not be presented as a new classification of Demushkin groups.

---

## 9. Final classification

- target-class intrinsic characterization: **PASS / CLOSED**;
- target isomorphism-class uniqueness: **PASS / CLOSED**;
- canonical marked quotient kernel/map: **FAIL / CLOSED**;
- target-free admissible realization groupoid: **PASS / CLOSED** for the declared critical source/class;
- existence of an admissible realization for the declared \(W_n\): **PASS / CLOSED**;
- connectedness / one realization orbit: **PASS / CLOSED** under the established critical-window orbit theorem;
- relative Boolean factorization through the intrinsic realization groupoid: **PASS / LOCAL**;
- non-existential presentation-free construction of that groupoid: **OPEN / LOAD-BEARING**;
- coarsest intrinsic realization/minimality: **OPEN**;
- universal theorem beyond the declared odd-(p), even-rank Demushkin critical-window family: **OPEN**.

---

## 10. Next authorized action

Do **not** search for another carrier.

The remaining legitimate attack is a single structural question:

> Can \(\mathfrak R^{\mathrm{ad}}_{d,n}(W)\) be replaced by a smaller, explicitly characteristic finite object constructed internally from \(W\), while preserving the same realization class and the relative Boolean?

The first candidates are:

1. characteristic subgroups generated/intersected from all admissible kernels;
2. the corresponding maximal/minimal characteristic quotients;
3. whether these constructions collapse to the trivial quotient or to a quotient larger than \(Q_n\);
4. if they fail, a proof that the connected realization groupoid is the natural stopping point.

A positive result would advance the **coarsest intrinsic realization** problem. A negative result would establish a new minimality boundary. No conclusion is assumed in advance.
