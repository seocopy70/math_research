# CURRENT STATE — 2026-09-19

## Research question
Can the canonical orientation character chi:G -> Z_3^times be recovered intrinsically from filtered/graded data?

## Authoritative current branch
Rank-4 D4 IA / filtered extension datum.

## Frozen negative results
- The original linear-only rank-4 D4 lifting observable is FAIL/CLOSED: lift-independence fails.
- The naive q=9 degree-9 relation space is not H-stable.
- The artificial H-closure of S9 is not a valid fixed-presentation relation space.
- The Q3/Q9 S9 orbit route is CLOSED at the definition level.
- Preferred Nielsen lifts are prohibited as a repair.

## Current degree-3 IA quotient datum
A3 is the frozen degree-3 associative target, dim(A3)=64.
C3 is the ordinary correction space, rank 4.
First-layer IA variation Delta_IA has rank 20.
G3=C3+Delta_IA has rank 20.
Therefore
Q3=A3/G3 has dimension 44.

Higher IA layers were exhaustively checked at degree 3 and are invisible there.
First-layer fibre composition/change-law and basepoint-independence were locally verified.

## Covariance status
The admissible category
H_adm={g in GSp4(F3): g e1 = mu(g)e1}
has 1296 elements.

CI run 35416804953: PASS.
Across all 1296 elements, C3, Delta_IA, and G3 are invariant; ranks 4,20,20. The q-sensitive source transforms by the multiplier.

## Representative control
CI run 35416952791: PASS.
Tested identity, -I, e1 -> e1+e2, and diag(2,1,2,1), with both left/right first-layer fibre parameterizations.

For all cases:
- IA variation rank 20;
- q=3/q=infinity change laws agree;
- 276 composition pairs have zero failure modulo C3;
- Q3 dimension 44;
- every non-identity tested representative has q-sensitive defect surviving Q3.

## Current gate
OPEN: define and audit the quotient-valued defect transformation/composition law on the admissible category, including the GSp multiplier convention.

No full rank-4 representative scan is authorized before that law is established.

## Key current commits
- covariance audit: c620ce5a962031cfff90d49aa8500ea39cc16dc1
- representative audit: 12805fe1a2486a4ba234b2607bf197468cd48a7a
- latest research-record commit: 109fcfec009cf0e30ac6102bc7052e40dc0b0dab
