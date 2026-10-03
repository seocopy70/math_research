# PAPER 4 — GATE C: INTRINSIC ORBIT/CATEGORY FEASIBILITY AUDIT
## 2026-10-03

### Question

After proving single two-sided orbit transitivity for the critical window
\[
W_n=G/D_n(G),\qquad n=p^s+1,
\]
can the unique admissible quotient-map orbit be recovered from \(W_n\) without choosing a marked quotient map \(\pi:W_n\to Q_n\)?

### 1. Pre-check

**Object.** The candidate object is not a literal marked map. It is the groupoid/category of admissible finite quotient realizations of \(W_n\), with morphisms given by precomposition by \(\operatorname{Aut}(W_n)\) and postcomposition by target isomorphisms.

**Input.** The proposed construction may use only the abstract filtered finite group \(W_n\), together with the fixed admissible target class used in the theorem. It may not use a distinguished generator \(z\), a chosen presentation, or a chosen \(\pi\).

**Functoriality.** An isomorphism \(f:W_n\to W_n'\) transports quotient diagrams by precomposition. Target isomorphisms transport the codomain. Thus the realization groupoid is functorial once the admissible target class is fixed.

**Gauge.** The proven theorem identifies all admissible realizations up to the natural two-sided action \(\operatorname{Aut}(W_n)\times\operatorname{Aut}(Q_n)\).

**Orientation bridge.** The relative split/non-split obstruction is a property of the marked extension diagram. Orbit transitivity proves it is constant on the admissible orbit, but does not by itself produce a formula from \(W_n\).

**q-blindness.** The proposed groupoid definition does not insert the orientation parameter \(q\) into the object. However, if admissibility is defined by explicitly naming the reference Demuškin target presentation, the construction remains relative rather than fully intrinsic.

### 2. Intrinsic candidate: admissible realization groupoid

Define \(\mathcal R(W_n)\) to have:
- objects: epimorphisms \(\pi:W_n\twoheadrightarrow H\) satisfying the declared admissibility conditions (critical Demuškin quotient class, radical-line kernel condition, and the corresponding finite-window target conditions);
- morphisms \((\pi:W_n\to H)\to(\pi':W_n\to H')\): pairs \((a,b)\) with \(a\in\operatorname{Aut}(W_n)\), \(b:H\to H'\) an isomorphism, satisfying \(b\circ\pi=\pi'\circ a\).

The general critical-window orbit theorem implies that, in the declared stress-family setting, \(\mathcal R(W_n)\) is connected and all objects with the same target model are isomorphic; for the fixed \(Q_n\)-target formulation it is a single two-sided orbit.

Hence the relative Boolean obstruction descends to the set of connected components of \(\mathcal R(W_n)\); in the present theorem it is constant because there is one component.

### 3. What is actually proved

The following implication is now valid:
\[
\boxed{
\text{admissible realization groupoid has one component}
\Longrightarrow
\text{relative obstruction is realization-independent}.
}
\]

Therefore, for the declared critical-window class, choosing a marked quotient map is unnecessary for the **value** of the relative obstruction once an admissible realization exists.

This is stronger than the W10 calculation: the gauge ambiguity has been completely absorbed by the quotient-map orbit.

### 4. The remaining obstruction

The phrase “intrinsic realization from \(W_n\) alone” still has a strict logical gap.

To make \(\mathcal R(W_n)\) a genuinely intrinsic construction, the admissibility predicate must itself be definable from \(W_n\) (or from a fixed external target category) without mentioning the hidden presentation or the hidden reference map. In particular, one must still prove one of:

1. a characteristic/universal quotient construction inside \(W_n\) canonically produces the admissible target; or
2. the admissible target class can be specified abstractly enough that \(\mathcal R(W_n)\) is a functor of \(W_n\) alone.

The orbit theorem does **not** prove either statement.

### 5. Sharp boundary

Thus the Gate C attack has a positive partial result but does not close full intrinsic reconstruction.

**PASS / CLOSED:** unique admissible quotient-map orbit, under the stated admissibility hypothesis.

**PASS / LOCAL:** realization-independence of the relative Boolean obstruction inside that admissible orbit.

**OPEN / LOAD-BEARING:** presentation-free, target-free canonical definition of the admissibility predicate and the resulting orbit/category from \(W_n\) alone.

**OPEN:** coarsest intrinsic realization/minimality.

No new carrier search is authorized. The next singular task is to test whether the admissibility predicate can be replaced by an internal universal property of \(W_n\), beginning with characteristic quotients/normal subgroups and the intrinsic radical line, and to stop immediately if the target class itself remains externally specified.
