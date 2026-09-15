# Phase 2-13C Sanity Recheck — 2026-09-16

## Reason for reopening

The previous torus table

    (1,1)->2, (1,2)->1, (2,1)->1, (2,2)->2

cannot be a one-dimensional group character because the identity must act by 1 and characters must be multiplicative.

## Hard checks required

1. t(1,1) = I4.
2. rho(1,1) = I35.
3. rho(t1 t2) = rho(t1) rho(t2) for all 16 pairs in T(F3).
4. The fixed-line scalar satisfies chi(1,1)=1.
5. chi(2,2)=chi(2,1)chi(1,2).
6. Fixed-line basis is taken from the exact unique U+-fixed line, not reconstructed independently for each torus element.

Any failed assertion invalidates the character computation and blocks Phase 2-14.

## Status

Phase 2-14 remains BLOCKED until this audit passes.
