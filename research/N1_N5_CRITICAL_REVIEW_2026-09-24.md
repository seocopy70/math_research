# N1–N5 Critical Review — 2026-09-24

## Purpose

This is the standalone controlling record of the N1–N5 critical review. It consolidates the logic/novelty audit before manuscript drafting. It does not reopen closed research routes.

## N1 — Existing Kummerian/cyclotomic theory

**Finding: KNOWN / CLOSED as prior art.**

The audited literature establishes:
- Kummerianity via surjectivity of finite-coefficient maps
  (H^1(G,\mathbf Z_p(\theta)/p^n)\to H^1(G,\mathbf F_p)).
- A torsion-free Demuškin pro-(p) group has a unique canonical orientation making the oriented pair Kummerian.
- Labute's classical work supplies the relevant Demuškin orientation/cocycle criterion.

**Consequence:** the paper must not claim discovery of the canonical orientation itself.

## N2 — Does quotient/inheritance literature already imply the selector?

**Finding: NO DIRECT IMPLICATION IDENTIFIED / CLOSED AS AN OBJECTION.**

The audited quotient-inheritance results start with an already oriented Kummerian pair and impose additional hypotheses, including a restriction-map condition in the relevant formulation. They do not, as stated, begin with an arbitrary finite candidate
[
\rho:Q_k\to(\mathbf Z/3^k)^\times
]
and recognize the canonical orientation from (Q_k) alone.

Therefore N2 does not collapse the finite-window theorem by citation alone.

## N3 — Full-group finite-level uniqueness

**Finding: HISTORICAL / NOT NOVEL.**

The all-level lifting criterion and uniqueness of the canonical Demuškin orientation are already present in Labute and modern Kummerian formulations. This part is imported as the existence/base framework, not claimed as a new theorem.

## N4 — Arbitrary-candidate factorization through the finite quotient

**Finding: MATHEMATICAL PASS / CLOSED.**

For an arbitrary candidate \(\rho\), the relevant \(\rho\)-twisted crossed cocycles factor through
[
Q_k=G/P_{k+1}
]
by the finite semidirect-filtration argument (U1–U2). This is logically separate from quotient inheritance because the candidate orientation is not assumed in advance.

This proves that the finite Kummer predicate is genuinely defined on the finite filtered quotient.

## N5 — Exact finite-window recognition theorem

**Finding: NO EXACT PRIOR THEOREM IDENTIFIED IN THE AUDITED CORPUS; NOVELTY SURVIVES CONDITIONALLY.**

The checked literature did not identify a theorem with all of the following simultaneously:

1. input is the bare finite quotient (Q_k=G/P_{k+1});
2. \(\rho\) is an arbitrary candidate, rather than a pre-supplied canonical orientation;
3. the selector is the intrinsic Kummer lifting predicate \(\mathsf K_k(Q_k,\rho)\);
4. the predicate recognizes exactly \(\chi_G\bmod 3^k\);
5. factorization through \(Q_k\) is established for arbitrary candidates;
6. no presentation coordinate, \(q\), or dualizing action is supplied as selector input.

This is a **conditional novelty statement**, not a claim of absolute priority. Before submission, the exact formulation must still be checked against additional quotient/cohomology references and any equivalent reformulation.

## Scope controls

- Current theorem scope: the fixed rank-4, (q=3) Demuškin group under study.
- “q-blind” means (q) is not an input to the selector; it does **not** assert uniformity over all (q).
- (P_{k+1}) is proved sufficient. Minimality of the finite depth remains **OPEN**.
- The canonical orientation's existence is classical and imported.
- U5 must use the coefficient-extension/Yoneda variation identity and the PD² dual-map argument; the superseded informal “(H^0=) socle” argument must not be used.

## Final gate table

| Gate | Question | Status | Role |
|---|---|---|---|
| N1 | Is the Kummerian/canonical orientation theory already known? | KNOWN / CLOSED | Prior art |
| N2 | Does quotient inheritance already imply the finite selector? | NO DIRECT IMPLICATION / CLOSED | Objection rejected |
| N3 | Is full-group finite-level uniqueness new? | HISTORICAL / NOT NOVEL | Imported framework |
| N4 | Do arbitrary candidates factor through (Q_k)? | PASS / CLOSED | Mathematical foundation |
| N5 | Is the exact finite-window selector already stated in checked literature? | NOT IDENTIFIED / CONDITIONAL | Remaining novelty boundary |

## Manuscript consequence

The manuscript should be organized around the finite-window recognition/factorization theorem. It must explicitly state that canonical Demuškin orientation is classical, avoid “minimal window” language, and define “q-blind” only as absence of (q) from selector input.

This document is the controlling standalone N1–N5 audit record. The chronological research log remains the audit trail.
