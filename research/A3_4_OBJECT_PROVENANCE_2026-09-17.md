# A3-4 Object Provenance Registry

Date: 2026-09-17

## Purpose

Record the definition, construction source, coordinate dependencies, and verification status of the core A3-4 objects so that later stages do not need to rediscover an object's origin by reopening historical phase scripts.

This is a provenance record, not a new mathematical result.

## Core objects

| ID | Object | Definition / role | Construction source | Current verification |
|---|---|---|---|---|
| `A3-W` | \(W\) | degree-4 invariant subspace used in A3-4 | `research/A3_4_BUILD_DATA_2026-09-17.py` | dim 45 |
| `A3-Wd` | \(W_d\) | degree-4 subspace generated from \(d\) | `research/A3_4_BUILD_DATA_2026-09-17.py` | dim 45 |
| `A3-I` | \(I=W\cap W_d\) | ambient intersection | `research/A3_4_BUILD_DATA_2026-09-17.py` | dim 35 |
| `P23-N` | \(N\) | historical non-scalar nilpotent in \(\operatorname{End}_H(W)\) | Phase 2-3 exact commutant computation | historical: \(N^2=0\), rank 10, kernel dimension 35 |
| `P23-K` | \(K_N=\ker N\) | kernel of `P23-N` | Phase 2-3 | historical dimension 35; equality with `A3-I` not yet established |
| `A3-tau` | \(\tau\) | constrained intertwiner \(W\to W_d\) | A3-4 artifact-only tau audit | rank 45; intertwiner and I-identification checks PASS |

## Dependency graph

```text
A3-W ───────────────┐
  │                 │
  ├─ H-action ──────┼──> P23-N ──> P23-K = ker(N)
  │                 │
  └──────────────┐  │
                 ▼  │
A3-Wd ───────> A3-I = W ∩ Wd
                 │
                 └──────────── comparison: P23-K ?= A3-I

A3-W + A3-Wd + A3-I + H-action ──> A3-tau
```

## Historical origin of `P23-N`

The Phase 2-3 computation defines

\[
B=A_2+A_3+A_4+A_5,
\]

verifies the cyclic/Krylov condition for \(B\), computes the exact \(H\)-commutant of the degree-4 action on \(W\), and obtains a 2-dimensional \(\operatorname{End}_H(W)\). After identifying the identity, the script selected a non-scalar nullspace basis element as `N` and directly verified

\[
N^2=0,\qquad \operatorname{rank}N=10,\qquad \dim\ker N=35.
\]

Therefore the historical definition is computational: `P23-N` is the selected non-scalar nilpotent generator of the computed commutant, rather than an independently stated geometric formula.

## Important caveat

The current A3-4 artifact contains `W`, `Wd`, generator matrices, `R4`, and the intersection coordinate data, but does not yet contain the historical `N`. A fresh End_H(W) audit performed before this registry did not reproduce the historical rank-10 nilpotent from its tested 2-dimensional span. Consequently, `P23-N` and `A3-I` must not be identified by assumption.

The next mathematical audit should reconstruct `P23-N` in the authoritative coordinate/action convention and compare `ker(P23-N)` directly with `A3-I`. If they differ, the H-equivariant identification/gauge between the two 35-dimensional objects must be investigated.

## Artifact pipeline baseline

The A3-4 artifact pipeline establishes the following execution architecture:

1. Build `A3-W`, `A3-Wd`, and `A3-I` once.
2. Store them in artifact schema `A3-4-data-v1`.
3. Downstream K/tau audits read the artifact only and do not import or execute phase scripts.

This provenance registry is intended to make that architecture semantically traceable as well as computationally isolated.
