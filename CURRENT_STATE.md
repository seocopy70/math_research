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


## Latest quotient-defect composition control — 2026-09-19

CI run 35417325110, commit 1ee1680f071c77ee3b6042eb1436dfd9f3406.

The absolute normalized relator defect [F_g(R3)-mu(g)R3]_deg3 failed the tested composition law on all 16 ordered pairs and is not promoted.

The q-sensitive difference
Delta_q(g) = [delta_3(g)-delta_infinity(g)] = [F_g(X1^3)-X1^3]_deg3
satisfies the candidate cocycle law
Delta_q(gh)=Delta_q(g)+g·Delta_q(h)
in Q3=A3/(C3+Delta_IA), for all 16 ordered pairs of the four controlled representatives (identity, -I, standard transvection, multiplier-2 diagonal).

Exact CI:
- gauge rank 20;
- Q3 dimension 44;
- candidate-law failures modulo Q3 = 0;
- raw candidate-law failures = 16;
- all 16 composed q-defect classes nonzero.

Important qualification: the reversed action/order diagnostic also has zero failures modulo Q3 on this small set, so the action/order convention is not uniquely fixed by this control alone.

Current gate remains LOCAL, not theorem-level:
- fix the precise action/order convention;
- extend the cocycle audit to a broader structured representative family;
- explicitly verify multiplier-2 GSp compatibility;
- only then authorize a broad rank-4 scan.

The failed absolute defect law and all previous excluded routes remain closed.


## 2026-09-19 correction: quotient cocycle audit

The earlier run 35417325110 is INVALIDATED because the defect helper used the reference relator with the wrong sign. It is not evidence.

Corrected run 35418122079, commit bb39ed1a7191aeae0da07813e40abe47695d292a. With delta_g = [F_g(R3)-mu(g)R3]_deg3, the q-sensitive Delta_q(g) satisfies Delta_q(gh)=Delta_q(g)+g·Delta_q(h) in Q3 for all 16 ordered pairs of the four controlled representatives.

Corrected results: gauge rank 20; Q3 dimension 44; candidate-law failures modulo Q3 0; raw failures 0; reversed diagnostic failures modulo Q3 2; reversed raw failures 2; 11 composed q-defect classes survive Q3.

Status: valid LOCAL PASS. The candidate action/order convention is distinguished on this control set. Next gate is a broader structured representative-family audit with explicit multiplier behavior. No unrestricted full rank-4 scan yet.
