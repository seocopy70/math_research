# A-1 Delta_q coboundary control — 2026-09-19

## Purpose

Determine whether the frozen structured quotient defect
Delta_q(g)=[F_g(X1^3)-X1^3]_3
is exactly the ordinary coboundary g.[X1^3]-[X1^3].

This gate is a control experiment, not a broader rank-4 scan.

## Dependencies

- Frozen structured 9-representative family.
- Frozen matrix_to_lift and column convention.
- Frozen Magnus degree-3 action.
- Frozen gauge C3+Delta_IA and quotient Q3.
- Existing structured audit mathematics and conventions are reused unchanged.

## Pre-registered tests

### T1 — direct coboundary identity

For every one of the 9 representatives:
Delta_q(g)=g.[X1^3]-[X1^3].
The comparison is made in raw degree-3 coordinates.

### T2 — control vectors

For the fixed degree-3 controls X2^3, X1X2X1, and the fixed non-monomial tensor
X1^3+2X2^3+X1X2X1,
define Delta_w(g)=[F_g(w)-w]_3.
No q=3 versus q=infinity subtraction is used. Prediction: zero failures for every control and representative.

### T3 — composed-class count

For all 81 ordered representative pairs, compare the number of nonzero classes of composed Delta_q(gh) in Q3 with the number predicted directly by
(gh).[X1^3]-[X1^3].
The counts must agree exactly.

The repository currently does not expose a separately reusable implementation of the historical H_adm 1296-element enumeration in the frozen structured script. No new enumeration is invented in this gate; any full-H_adm count is outside scope.

## Decision rules

- PASS-TRIVIAL: T1, T2, T3 all pass. Record that the cocycle is a coboundary and carries no new H1 information; cancel any broader scan of this same cocycle.
- PASS-NONTRIVIAL: T1 fails while the composition law remains valid. Stop and isolate the non-coboundary component before any scan.
- IMPLEMENTATION FAILURE: T2 fails. Do not draw a mathematical conclusion.
- SETUP FAILURE: frozen GSp/lift/convention checks fail.

## Scope boundary

PASS-TRIVIAL closes only the Delta_q cocycle track. It does not imply that the IA quotient datum itself is trivial.
