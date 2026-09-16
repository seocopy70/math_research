# Computational Sanity Protocol — 2026-09-17

## Purpose

This protocol is now mandatory for the Demuškin filtration/module computations in `math_research`, especially whenever Python and GAP are used together.

## Coordinate consistency

1. Declare the authoritative action convention explicitly. The project Python matrices use **column action** `v -> A v`.
2. GAP `GModuleByMats` uses **row vectors with right action**. Therefore Python action matrices must be transposed before entering GAP.
3. The same conversion must be applied to endomorphisms and subspace bases, not only to generators.
4. For an authoritative Python endomorphism `N` satisfying `N A_g = A_g N`, its GAP row-action representative is `N^T`; `im(N)` must therefore be compared with the row span of `N^T`.
5. A result involving mismatched coordinates is classified **INVALID TEST**, not a mathematical counterexample.
6. Equality of subspaces must be checked in a common ambient coordinate system by exact span/rank comparison, not by dimensions alone.

## Field consistency

All rank, kernel, image, and span calculations for this project are over the declared finite field, currently `F_3` unless stated otherwise.

- NumPy `matrix_rank` is a numerical rank over the reals and is **not** an `F_3` rank test.
- Any diagnostic based on `np.linalg.matrix_rank` must not be used as a mathematical finite-field result.
- Use an exact modular Gaussian-elimination rank routine or a finite-field system such as GAP for `F_3`.
- Important rank values should be independently checked when practical.

## Structural sanity invariants

Before accepting a module-theoretic result, check necessary conditions such as:

- `N^2 = 0` implies `im(N) subseteq ker(N)`.
- Every nonzero finite-dimensional module has nonzero socle.
- Every nonzero submodule intersects the socle nontrivially.
- `dim U + dim V > dim M` forces `U intersection V != 0`.
- Rank-nullity holds over the declared field.
- An intertwiner satisfies `Q rho_M(g) = rho_N(g) Q` in the declared coordinate convention.

If a necessary condition fails, stop and classify the computation as **INVALID TEST** until the implementation and coordinate conventions are reconciled.

## Current B1-1 application

The earlier printed `RANK_N_FROM_EXACT_PYTHON = 24` was produced by `np.linalg.matrix_rank` and is therefore not an `F_3` rank. The authoritative finite-field rank is independently expected to be 10 and must be printed using exact modular rank in the corrected rerun.

The GAP socle comparison is coordinate-correct only when `N^T` is supplied to the row-action representation. The prior comparison using untransposed `N` is invalid and must not be treated as a mathematical negative result.
