# PAPER 3 — F2 SAME-W3 CONTROL GATE

Date: 2026-10-01

## Purpose

After the uniform F1 result, the next authorized enlargement is the genuinely different Blumer–Quadrelli F2 family. The question is whether an F2 non-1-cyclotomic group can share W3 with a cyclotomic control, reproducing the decisive same-window obstruction.

## Pre-check

Object: W_n=G/D_n, with T_cyc the existence of a 1-cyclotomic orientation.

Input: only the finite filtered group W_n; no q or orientation is inserted into the definition.

Functoriality: filtered-group isomorphisms induce the comparison.

Gauge: no chosen presentation coordinate may be used as the final separator.

Orientation bridge: global F2 non-1-cyclotomicity is literature input; the new target is finite-window visibility of that obstruction.

q-blindness: W_n itself is q-blind. Any separator must be formulated intrinsically from W_n.

Separation: first test the smallest case (p,d,q)=(3,2,3).

Novelty: a repeat of the known F2 non-1-cyclotomic theorem is not a result; only same-window/different-target, sharp threshold, or a reusable carrier is load-bearing.

Stop: do not run large computation until a concrete cyclotomic control with W3 equality is identified.

## First structural test

For d=2, take the F2 quadratic relation space
R_F2=< [X1,Y1]+[X2,Y2], [Z1,Z2] >
with {Z1,Z2} an unpaired pair, e.g. [X1,X2].

For the most immediate cyclotomic controls supplied by the elementary-type literature, namely free products of two rank-2 Demushkin cyclotomic pairs, the quadratic relation space is
R_ctrl=< [X1,Y1], [X2,Y2] >.

These two 2-planes are not equivalent under GL(V) in the rank-4 case: the Pfaffian of the pencil a([X1,Y1]+[X2,Y2])+b[X1,X2] is proportional to a^2, whereas the Pfaffian of a[X1,Y1]+b[X2,Y2] is proportional to ab. The first has a repeated projective root; the second has two distinct roots. Thus W3 cannot be isomorphic between this F2 example and this natural cyclotomic free-product control.

This is a local obstruction to the obvious control, not a no-go theorem for all cyclotomic groups.

## Classification

- F2 same-W3 cyclotomic obstruction: OPEN / DECISIVE.
- Natural free-product cyclotomic control: FAIL / CLOSED as a W3-matching control in the smallest rank-4 test.
- Broad F2 finite-window recognition: OPEN / CONDITIONAL.
- No large computation authorized yet.

## Next authorized search

Search for cyclotomic groups outside the immediate free-product control class whose W3 quadratic relation space has the F2 repeated-root type. Candidate source classes include cyclotomic semidirect products and other elementary-type constructions. If no such control exists under a meaningful category, that negative result itself may become a structural boundary.


## 2026-10-01 — F2 SAME-W3 CYCLOTOMIC CONTROL PRE-CHECK / LITERATURE AUDIT

The required pre-check was completed before any new computation. The search was restricted to genuinely cyclotomic constructions capable in principle of producing a rank-4, two-dimensional quadratic relation space of the F2 repeated-root Pfaffian type.

Primary literature checked:
- Quadrelli–Weigel, *Profinite Groups with a Cyclotomic p-Orientation* (arXiv:1811.02250 / Doc. Math. 25 (2020)): cyclotomicity is preserved under free products and specified fibre/semidirect constructions; the elementary-type framework is generated from free pro-p groups and Demushkin groups by free products and cyclotomic semidirect/fibre-product operations.
- Mináč–Pasini–Quadrelli–Tân, *Koszul algebras and quadratic duals in Galois cohomology* (Adv. Math. 380 (2021), arXiv:1808.01695): the cyclotomic semidirect construction is explicitly part of the elementary-type class.
- Blumer–Quadrelli, arXiv:2603.15464v2: the F2 family has the two-dimensional quadratic relation space used in the present gate and is globally non-1-cyclotomic.

Pre-check conclusion:
1. The literature confirms that cyclotomic semidirect/fibre-product constructions are legitimate control classes; therefore the search space is mathematically real, not an invented construction.
2. However, no explicit rank-4 cyclotomic example with W3 quadratic relation pencil GL4-equivalent to the F2 repeated-root type was found in the targeted search.
3. The standard elementary-type free-product control is already FAIL/CLOSED by the Pfaffian test recorded above.
4. The elementary-type cyclotomic semidirect operation changes the generator/relation count in a way that does not immediately furnish a rank-4, two-relation F2-type quadratic shadow; this is a structural warning, not yet a no-go theorem.
5. No large computation is authorized. The next legitimate task is an explicit construction-level search among cyclotomic fibre products/semidirect products and their smallest rank-preserving combinations, with the W3 relation pencil computed symbolically before any finite-group enumeration.

Classification:
- existence of a meaningful cyclotomic control class: **PASS / CLOSED**;
- existence of an actual F2-matching W3 control: **OPEN / DECISIVE**;
- free-product control: **FAIL / CLOSED**;
- broad F2 finite-window recognition: **OPEN / CONDITIONAL**.

Important boundary: absence of a matching example in this targeted literature audit is not a proof that no cyclotomic control exists.


## 2026-10-01 — F2 STANDARD ELEMENTARY-TYPE CONTROL SEARCH CLOSED

A construction-level symbolic search was completed for the smallest rank-4, two-relator cyclotomic controls generated by the standard elementary-type operations (free groups, Demushkin groups, free products, and cyclotomic semidirect products).

The rank/relation bookkeeping is decisive at this size. A cyclotomic semidirect product Z_p^m ⋊ G adds m generators and m·d + binom(m,2) quadratic action/commutativity relators at the minimal-presentation level. Therefore a rank-4, two-relator elementary-type object can arise only through the following relevant shapes:

1. free product of two rank-2 one-relator factors (Demushkin rank-2 factors or the rank-2 cyclotomic semidirect factor Z_p ⋊ Z_p): the two quadratic relation forms live on disjoint 2-planes, giving Pfaffian proportional to ab;
2. one rank-2 free factor extended by a single cyclotomic semidirect Z_p direction and then free-producted with one free generator: the two quadratic action forms share the semidirect direction, giving identically zero Pfaffian.

The F2 relation plane has Pfaffian proportional to a^2. Hence neither elementary-type shape can be W3-isomorphic to F2. This is an intrinsic GL4 obstruction, not a coordinate artifact.

This closes the standard elementary-type control route:
- **F2 same-W3 control inside the standard elementary-type class: FAIL / CLOSED.**
- **F2 same-W3 control among arbitrary cyclotomic pro-p groups: OPEN / CONDITIONAL.**
- No finite W4 computation is authorized, because no genuine W3 match exists in the tested meaningful control class.

The remaining possibility would require a cyclotomic control outside the standard elementary-type construction scheme whose quadratic relation plane nevertheless has the F2 repeated-root Pfaffian type. No such example was found in the targeted literature search. This is a boundary, not an absolute no-go theorem for every cyclotomic pro-p group.
