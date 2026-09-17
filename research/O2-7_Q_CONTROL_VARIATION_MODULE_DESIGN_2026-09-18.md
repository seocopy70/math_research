# O2-7 — q-control of the transport-variation module

Date: 2026-09-18

## Global position

A3-4 established I = W cap W_d = ker(N), rank(N)=10.
O2-3 established ker(D)=I and O is isomorphic to W/I and to U=im(N).
O2-4 showed the absolute obstruction image depends on transport.
O2-5/O2-6 showed the affine variation Delta D has rank 10, is H-stable, and is basepoint-independent inside the complete B1 family.

A3-4-2 separately certified the q-sensitive degree-4 class d = [X1^[3], X2] in Q4, while the q=infinity control has no X1^[3] contribution.

## Purpose

Test whether the controlled rank-10 variation module Delta O is directly tied to the q=3 p-power contribution, rather than being only a quadratic/transport artifact.

Compare:
1. P = <H orbit of d> inside W, where d=[X1^[3],X2].
2. U = im(N) inside W.
3. the source-side variation im(tau N).
4. the target-side variation Delta O = im(Delta D).

Do not use dimension alone. Whenever two objects share coordinates, test exact subspace equality. Across different spaces, test the explicit induced map.

## q controls

q=3: use the already certified restricted-Lie element d3=[X1^[3],X2].

q=infinity: keep the same quadratic relation R and omit the p-power term X1^[3], so the corresponding p-power contribution is zero.

No other construction may be changed: keep the same H action, word convention, quotient convention, and frozen W construction.

## Dependencies

- Corrected A3-4 artifacts, commit 62886877f97e58e87d59b0075d45e38be6176410.
- A3-4-2 q-sensitivity certificate.
- O2-5/O2-6 verified variation maps.
- Phase 2-3 N and the five generator actions.

## PASS / FAIL

PASS-A: verify dim(P)=10 and P=U as actual subspaces of W.

PASS-B: verify that im(tau N) is the transported copy of P under the explicit frozen coordinate map.

PASS-C: under q=infinity, the p-power source direction collapses to zero. This is a control statement, not a claim that every quadratic object disappears.

If A+B+C pass: the controlled 10-dimensional variation module is directly tied to the q=3 p-power contribution and disappears in the q=infinity control.
If A passes but B fails: U detects the p-power direction, but Delta O has not yet been canonically identified with it.
If A fails: do not infer the identification from dimension 10.
If C cannot be implemented without changing other data: stop and redesign the q=infinity control.

## Boundary

This does not recover the full 3-adic orientation character chi. A successful q=3/q=infinity separation only establishes sensitivity to the presence of the p-power term X1^[3]. It does not distinguish higher q-values such as q=3 versus q=9, nor prove recovery of chi.

## Implementation rule

Do not modify frozen production artifacts. Use an independent script/workflow and reuse certified artifacts through runpy where possible. Every equality claim must be checked as an actual subspace or map equality.