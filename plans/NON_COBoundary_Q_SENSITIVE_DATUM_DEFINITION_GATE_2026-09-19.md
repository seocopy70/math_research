# Non-Coboundary q-Sensitive Datum Definition Gate — 2026-09-19

## Motivation

The previous quotient defect
Delta_q(g) = [F_g(X1^3)-X1^3]_3
is exactly the coboundary g.(X1^3)-X1^3. Its cocycle law is automatic, so broader scans of that law cannot provide new information.

This gate defines the requirements for any replacement object.

## Definition requirements

A candidate datum D must satisfy all six conditions before broad computation:

1. **q-blind definition boundary**
   D is defined from a single admissible input structure. The definition may not subtract or compare q=3 and q=infinity objects in advance.

2. **Non-coboundary**
   D must not have the form g.v-v for a fixed pre-existing vector v in the target representation. If it does, the candidate is closed as a universal coboundary.

3. **Lift/IA legitimacy**
   D must be invariant under the allowed lift fibre, or be formulated as a rigorously defined quotient/torsor/extension datum. Preferred lifts are forbidden.

4. **Coordinate legitimacy**
   The construction must be invariant under the allowed free-group coordinate changes, or the exact quotient/action under which it is invariant must be proved.

5. **Nontriviality witness**
   There must be a concrete algebraic witness that the candidate is not zero, not merely a universal p-layer shadow, and not forced by the already-frozen linear representation.

6. **Delayed q-separation**
   Only after 1–5 pass may q=3 and q=infinity be instantiated and compared.

## PASS / FAIL consequence

- Failure of (1) or (2): CLOSE immediately; no scan.
- Failure of (3) or (4): CLOSE as non-intrinsic; no preferred-lift repair.
- Failure of (5): CLOSE as tautological/p-layer shadow.
- Failure of (6): CLOSE as circular q-recovery.
- Only a candidate satisfying all six authorizes a small structured computation.

## Candidate source

The primary source should be the retained IA / filtered extension structure. Delta_IA itself is not automatically q-sensitive and must not be relabeled as such without a new definition.

## Separate orientation bridge gate

Independently audit the statement

g e1 = mu(g)e1

against the target orientation character chi. The audit must determine exactly whether this condition:
- merely defines the admissible linear subgroup,
- determines mu(g),
- or has any mathematically proved relation to chi.

No implication is assumed from notation alone.

## Current status

**OPEN — definition only. No computation authorized yet.**
