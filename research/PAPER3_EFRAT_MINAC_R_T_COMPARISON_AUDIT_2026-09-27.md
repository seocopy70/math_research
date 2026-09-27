# Paper 3 — Efrat–Mináč / (r_T) Comparison Audit
Date: 2026-09-27

## Purpose

Determine whether the proposed category-level finite-window recognition threshold
(r_T(\mathcal C;D_\bullet)) is merely a reformulation/corollary of existing finite-determinacy and minimal-determining-quotient theory.

## Verified prior art

### Efrat–Mináč

Efrat–Mináč, *Galois groups and cohomological functors* (TAMS 2017; arXiv:1103.1508), constructs a canonical third quotient for the relevant absolute Galois-group class and proves that it determines the full mod-(q) cohomology ring, with a minimality theorem. For (q=p) odd, the relevant third term agrees with the third Zassenhaus term.

Their cohomological-duality framework also explicitly contains:
- cup-product/decomposable (H^2) data;
- a Bockstein + cup-product example.

Therefore the following broad claim is already closed as non-novel:

> finite filtered information can determine a cohomological invariant.

### Efrat 2014

Efrat, *The Zassenhaus filtration, Massey products, and representations of profinite groups* (Adv. Math. 263 (2014), 389–411), gives representation-theoretic characterizations of Zassenhaus terms by intersections of kernels of upper-triangular unipotent representations under stated hypotheses.

Therefore a general “finite representation data ↔ Zassenhaus depth” bridge is also prior art.

## (r_T) comparison

Define
[
r_T(\mathcal C;D_\bullet)
=
\min\{n:
W_n(G)\cong W_n(H)
\Rightarrow
T(G)\cong T(H)
\text{ for all }G,H\in\mathcal C\}.
]

This is not automatically equivalent to a minimal determining quotient. To establish equivalence one must specify:
1. the admissible category (mathcal C);
2. the filtration (D_\bullet);
3. the target functor (T);
4. the notion of isomorphism/naturality;
5. whether “minimal” means filtration depth, quotient factorization, or minimal object in a larger carrier category.

## Candidate axes

| Axis | Prior-art status | Current status |
|---|---|---|
| Cup/decomposable cohomology at depth 3 | Explicit Efrat–Mináč | NON-NOVEL / CLOSED |
| Bockstein + cup | Explicit Efrat–Mináč framework | NON-NOVEL / CLOSED |
| Pure Bockstein exact (r_{T_\beta}=p+1) | Not verified | OPEN / HYPOTHESIS |
| Factorization vs recognition thresholds | Not yet matched to an exact prior theorem | OPEN |
| Filtration dependence of (r_T) | Not yet matched to an exact prior theorem | OPEN |
| Explicit sharp separation pairs | Existing minimality is related, but exact requested form not yet matched | OPEN |
| Uniform ((\mathcal C,D_\bullet,T)\mapsto r_T) formalism | No exact prior theorem located | OPEN / LOAD-BEARING |

## Critical caution

The pure Bockstein value (r_{T_\beta}=p+1) must not be assumed from the Efrat–Mináč Bockstein/cup duality triple. A separate proof of both:
- factorization at (p+1), and
- non-recognition below (p+1)

is required.

Likewise, the phrase “minimal determining quotient” must not be treated as synonymous with (r_T) until the relevant carrier category and equivalence are formally identified.

## Next gate

N3 must proceed theorem-by-theorem:
1. identify the exact Efrat–Mináč theorem/proposition corresponding to each candidate target;
2. translate its hypotheses and conclusion into (r_T) language;
3. test whether the translation gives equality, only an upper bound, or no implication;
4. only then select a target for computation.

**Classification: OPEN / LOAD-BEARING.**
