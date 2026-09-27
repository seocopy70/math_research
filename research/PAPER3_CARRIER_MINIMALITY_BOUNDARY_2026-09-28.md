# PAPER 3 — CARRIER MINIMALITY BOUNDARY — 2026-09-28

## Status

**ABSOLUTE carrier minimality is not yet an OPEN numerical problem; it is first an ill-posed categorical question.**

The object
\[
\mathcal O_k=H^2(Q_k,\mathbf F_p)/\operatorname{im}(\operatorname{tra}_k)
\]
is a canonical finite cohomological carrier. Asking whether it is “absolutely minimal” has no mathematical meaning until the allowed carrier category and recognition morphisms are fixed.

## 1. Why absolute minimality is undefined

At least three inequivalent notions are possible.

### A. Linear quotient carriers

Require a carrier to be a quotient
\[
\mathcal O_k\twoheadrightarrow C
\]
in finite \(\mathbf F_p\)-vector spaces, with the selector induced by a linear map.

Then the problem becomes a finite quotient/minimum-dimension problem. Different quotients of the same dimension can exist, and a unique minimum need not exist.

### B. Functorial cohomological carriers

Require \(C\) to be naturally constructed from the finite extension
\[
E_k\twoheadrightarrow Q_k
\]
and functorial under isomorphisms of the finite filtered pair.

This is substantially more restrictive. The transgression quotient is then a natural candidate for a universal stable degree-2 carrier, but minimality still requires a separate categorical theorem.

### C. Arbitrary recognition carriers

If arbitrary sets, nonlinear maps, or predicates are allowed, “dimension” ceases to be meaningful. A Boolean carrier can record only whether a false candidate has a nonzero witness, while retaining no cohomological information. Thus no absolute vector-space minimality statement can survive without restrictions.

## 2. Correct replacement question

The mathematically meaningful frontier is:

\[
\boxed{
\text{For a specified carrier category }\mathcal C,
\text{ is }\mathcal O_k
\text{ initial/terminal/minimal among separating carriers?}
}
\]

The strongest natural version is a **universal quotient theorem**:

> Every functorial linear carrier that detects every false lift factors through \(\mathcal O_k\), or through a canonical quotient of \(\mathcal O_k\).

That is a precise theorem target. It is stronger and cleaner than the phrase “absolute minimality.”

## 3. What D2 already proves about lower quotients

D2 proves that the full transient sector
\[
\operatorname{im}(\operatorname{tra}_k)
\]
cannot be load-bearing for recognition: it is invisible after the first deeper finite step and cannot contain a separating witness with nonzero global inflation.

Therefore passing from \(H^2(Q_k)\) to \(\mathcal O_k\) is justified.

D2 does **not** prove that no proper quotient
\[
\mathcal O_k\twoheadrightarrow C
\]
can still separate every false lift.

That is exactly the remaining carrier question.

## 4. Current classification

- \(H^2(Q_k)\) as carrier: **too large / transient directions present**.
- quotient by \(\operatorname{im}(\operatorname{tra}_k)\): **PASS / CLOSED as a sufficient carrier**.
- absolute minimality of \(\mathcal O_k\): **NOT WELL-POSED until carrier category is specified**.
- linear quotient minimality: **OPEN**.
- functorial universal minimality: **OPEN**.
- arbitrary recognition-carrier minimality: **not a meaningful invariant**.

## 5. Recommended research direction

Do not attempt another large cohomology computation.

First fix the category to the strongest natural one:

\[
\mathcal C_k=
\{	ext{finite }\mathbf F_p\text{-linear functorial carriers of }
(E_k\to Q_k)\}.
\]

Then ask whether every separating carrier receives a canonical map from \(\mathcal O_k\), or equivalently whether the intersection of all admissible separating kernels is zero.

This converts “minimality” into a concrete kernel-intersection problem rather than an undefined dimension hunt.
