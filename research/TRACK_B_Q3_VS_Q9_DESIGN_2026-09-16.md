# Track B — q=3 vs q=9 comparison design

## Purpose
Determine whether the q-dependent orientation-image parameter is visible in the ordinary degree-4 quadratic shadow, or only in the restricted/Zassenhaus refinement.

## Common setup
G_q = <x1,x2,x3,x4 | x1^q [x1,x2][x3,x4] = 1>, q in {3,9}.

The degree-2 initial form is the same in both cases:
R = [X1,X2] + [X3,X4].
Hence Q4=L4/(R)_4 and the Sp4(F3)-module W=<Sp4(F3)·T> are constructed from the same quadratic data and are not expected to distinguish q.

## q-sensitive location
For q=3, x1^3 first contributes at Zassenhaus degree 3.
For q=9, x1^9 first contributes at Zassenhaus degree 9.
Therefore degree 3 is the first natural q-sensitive probe.

## A3 result used as baseline
After removing the degree-2 correction from C(x1)=x2 x1 x2^{-1}, the degree-3 restricted class was certified as

in_3(s) = X1^[3] + 2[[X3,X4],X1] + 2[[X3,X4],X2].

Its degree-4 commutator correction was certified to be nonzero in Q4 and to lie inside W45:

d4 = 2[[[X3,X4],X1],X1] + 2[[[X3,X4],X2],X1] ∈ W45, d4 != 0 in Q4.

## Comparison protocol
1. Keep the same quadratic Lie algebra Q4 and same W45 as the common control.
2. For q=3 compute the restricted/Zassenhaus classes through degree 4.
3. For q=9 compute the corresponding classes through degree 4; x1^9 should not enter at these degrees.
4. Compare only representation-theoretic invariants under the same Sp4(F3) action, not raw coordinates.
5. If q=3 and q=9 agree through degree 4, conclude only that degree <=4 data does not distinguish these q values; do not infer that the full filtration loses q.
6. If they differ, identify the first degree and the exact module/subquotient carrying the difference.

## Critical control
Do not attribute every difference to q merely because the defining integer exponent differs. The comparison must explicitly separate:
- common quadratic relation R;
- ordinary Lie degree-4 module W;
- restricted p-power contribution;
- higher Zassenhaus degree where x1^9 can first appear.

## Status
Design recorded. The actual q=3/q=9 computation remains to be executed and independently checked.
