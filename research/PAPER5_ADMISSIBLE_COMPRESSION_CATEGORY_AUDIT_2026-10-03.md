# PAPER 5 ADMISSIBLE COMPRESSION CATEGORY AUDIT — 2026-10-03

## Question

Can “compression” be made mathematically nontrivial by fixing an admissible comparison category/order, rather than comparing arbitrary intrinsic objects by an undefined notion of “smaller”?

## 1. Pre-check

Object:
- the already intrinsic admissible realization groupoid \(\mathfrak R_{d,n}^{ad}(W_n)\), for the declared critical-window class;
- the relative split/non-split Boolean \(b:\mathfrak R_{d,n}^{ad}(W_n)\to \mathbf 2\), already constant on its single realization orbit.

Input:
- only the unmarked finite filtered group \(W_n\), with its intrinsic filtration/cohomology data;
- no external marked quotient, Demushkin presentation, torsion parameter, or chosen orientation.

Functoriality:
- source isomorphisms act on realizations by precomposition;
- target isomorphisms act by postcomposition;
- intrinsic compression objects must be invariant under filtered-group isomorphism.

Gauge:
- source automorphisms and target isomorphisms are quotiented;
- literal quotient maps are therefore not admissible as the final invariant.

Orientation bridge:
- the only presently certified bridge is the realization-independent relative Boolean on the admissible realization groupoid.

q-blindness:
- the compression object itself must not contain the external torsion parameter \(q\); the target class \(\mathcal C_{d,n}\) is already q-free by its intrinsic finite abelianization characterization.

Separation:
- the current critical-window orbit theorem gives one admissible realization orbit, so no same-window separation pair exists at the orbit level.

Stop check:
- all nine pre-check items are satisfied at the level needed to define a comparison category. No new carrier computation is authorized.

## 2. The only non-tautological comparison category available at present

Define an **admissible finite realization factorization** over \(W\) to be a pair
\[
(C,e),\qquad e:\mathfrak R^{ad}(W)\longrightarrow C,
\]
where \(C\) is an isomorphism-invariant finite object functorially attached to \(W\), and \(e\) is natural under filtered-group isomorphisms.

For two such factorizations define
\[
(C,e)\preceq(C',e')
\]
iff there exists a natural map
\[
u:C'\to C
\]
such that
\[
e=u\circ e'.
\]
Thus \(C\) is at least as compressed as \(C'\): all information retained by \(C\) factors through \(C'\).

This order is meaningful only after the **preserved-information package** is fixed. The present project has two natural choices.

### Package B: preserve only the relative Boolean

Require a map \(\bar b:C\to\mathbf 2\) with
\[
b=\bar b\circ e.
\]

Then the two-point Boolean object itself is an admissible compression:
\[
\mathfrak R^{ad}(W)\xrightarrow{\ b\ }\mathbf 2.
\]
Because \(b\) is constant on the declared critical realization groupoid, its image is actually a singleton \(\mathbf 1\) for each fixed critical source.

Therefore Boolean-preserving compression has a terminal/coarsest object which contains no realization information. Any claimed “minimal carrier” at this level is mathematically trivial.

### Package R: preserve the full realization orbit/category

Require \(e\) to retain the complete gauge-invariant realization object, i.e. the one-component orbit/groupoid already constructed.

Then the realization groupoid itself is the canonical terminal compression under the above factorization order. Any further quotient identifies distinct realization data and therefore leaves the declared package R.

Hence “minimality” at this level is also immediate: the groupoid is minimal only because the entire realization object was declared non-compressible.

## 3. Intermediate packages are possible, but must be declared

A genuinely nontrivial compression can exist only after specifying an intermediate invariant package \(I\) satisfying
\[
\mathbf 2\ \text{(Boolean)}\ \subsetneq I\ \subsetneq\ \mathfrak R^{ad}(W)
\]
in an explicitly defined category.

Examples of admissible preserved packages would have to be stated structurally, e.g.
- the target isomorphism class plus its intrinsic H^1-radical line;
- the quotient-map orbit but not its morphism group;
- a specified finite cohomological action;
- a specified extension-class orbit.

The project currently has no theorem selecting one of these packages canonically.

## 4. Why arbitrary “coarsest intrinsic compression” is ill-posed

Suppose \(C\) is an intrinsic compression. Without a fixed preserved-information package, one can always postcompose it with a quotient
\[
C\twoheadrightarrow C'
\]
and call \(C'\) “smaller”. Repeating this eventually reaches a constant object. Conversely, if one declares the full realization object to be preserved, no nontrivial compression is permitted.

Thus the phrase “coarsest intrinsic realization” has no invariant mathematical meaning by itself. It becomes meaningful only relative to an admissible category and a declared notion of information preservation.

This is not a failure of the realization-groupoid construction. It is a boundary on what a minimality theorem can logically claim.

## 5. Attempted escape: use all functorial finite quotients

Taking the category of all finite intrinsic quotients of \(W\) does not solve the problem. Its terminal object is the trivial quotient. Restricting to quotients that recover the Boolean again produces the Boolean object as the coarsest retained datum. Restricting to quotients that recover the full realization orbit simply reinstates the realization groupoid as the preserved object.

Therefore no canonical nontrivial minimality theorem emerges from “all functorial finite quotients”.

## 6. Structural consequence

The research frontier is now sharply divided:

1. **Boolean compression:** PASS / CLOSED, but trivial.
2. **Full realization compression:** PASS / CLOSED, but tautologically minimal once the full realization package is declared.
3. **Nontrivial intermediate compression:** OPEN. It requires a new admissible information package, not merely a new quotient construction.
4. **Absolute/coarsest intrinsic compression without a declared package:** FAIL / CLOSED as an ill-posed minimality target.

The earlier characteristic-intersection and characteristic-generated-kernel no-go results remain relevant only as candidate failures inside a future declared intermediate category; they do not prove an absolute no-go.

## 7. Research decision

The correct Paper 5 endpoint is therefore a **compression trichotomy/boundary theorem**, unless a mathematically natural intermediate preserved-information package can be independently identified.

No further carrier search is authorized under the current definition of the problem.

A future nontrivial branch is authorized only if it begins by proposing an explicit intermediate package \(I\), then passes the full Object/Input/Functoriality/Gauge/Orientation/q-blindness/Separation/Novelty/Stop pre-check.

## Classification

- admissible comparison category/order: **PASS / CLOSED**;
- Boolean-only compression boundary: **PASS / CLOSED**;
- full-realization compression boundary: **PASS / CLOSED**;
- absolute coarsest intrinsic compression without declared preserved information: **FAIL / CLOSED**;
- nontrivial intermediate compression: **OPEN**;
- universal characteristic-compression no-go: **OPEN** (not proved by the present results).

## Next authorized action

Do not reopen characteristic quotients merely to search for a “smaller” object.

If continuing Paper 5, the only mathematically substantive next step is to test whether there exists a **canonical intermediate preserved-information package** forced by the existing realization groupoid and the relative extension class. If none is forced, the trichotomy/boundary is the structural endpoint.


## 2026-10-03 — PAPER 5 DEFINITION RE-AUDIT: THREE LOGICAL CORRECTIONS

The submitted comparison-category formulation was rechecked against the authoritative compression audit. The structural endpoint is retained, but three claims in the proposed formulation are too strong or order-theoretically reversed.

1. **Factorization domain:** the relative Boolean is naturally a function (b:\mathfrak R^{ad}(W)\to\mathbf2), not merely a scalar (B(W)), unless one has already proved it is constant on the realization groupoid. On the present critical source it is constant, so the singleton conclusion is valid, but the definition should state the groupoid-level factorization first.

2. **Order direction:** if ((C,e)\preceq(C',e')) means there is (u:C'\to C) with (e=u\circ e'), then (C) is **coarser/more compressed** than (C'). Under this convention the coarsest object is **minimal**, not maximal, in the preorder. The phrase “maximal coarsest object” is reversed and must be corrected.

3. **Characteristic-invariant dichotomy is not proved:** the fact that (mathcal K(W)) is a single Aut(W)-orbit implies that an Aut(W)-invariant scalar function on the orbit is constant. It does **not** imply that every characteristic finite invariant either completely preserves all kernel-orbit information or collapses to (Q_n^{ab}). An invariant can retain orbit-level data such as stabilizer/action information without distinguishing individual orbit points. Therefore the proposed “complete preservation vs complete identification” theorem is not valid as stated. The authoritative status remains **OPEN** for universal characteristic-compression no-go.

4. **q-blindness is not automatic:** the fact that the target class is q-blind does not by itself imply an arbitrary intrinsic finite invariant cannot recover q indirectly from W. q-blindness must remain an explicit restriction on admissible objects, or be proved for the particular construction.

Result classification after correction:
- admissible factorization category/order: **PASS / CLOSED**, after correcting the order language and groupoid-level Boolean definition;
- Boolean-only endpoint: **PASS / CLOSED, trivial**;
- full-realization endpoint: **PASS / CLOSED, tautological up to the declared equivalence notion**;
- universal characteristic-compression dichotomy/no-go: **OPEN**;
- absolute coarsest without preserved-information package: **FAIL / CLOSED (ill-posed)**;
- nontrivial intermediate package: **OPEN**.

No new computation is authorized by this correction. The structural stop remains in force.
