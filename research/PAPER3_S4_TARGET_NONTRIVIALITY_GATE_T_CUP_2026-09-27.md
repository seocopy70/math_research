# Paper 3 S4 Target Nontriviality Gate — T_cup
## 2026-09-27

### Decision

The originally proposed target
\[
T_\cup(G)=\bigl(H^1(G,\mathbf F_p),\cup\bigr)
\]
as an **isomorphism class** is rejected as a nontrivial recognition target in the fixed-rank Demuškin category.

For a Demuškin group of fixed rank, the cup-product pairing is a nondegenerate alternating form. Over \(\mathbf F_p\) (odd \(p\)), all nondegenerate alternating forms of the same finite dimension are isomorphic by the standard symplectic/Darboux classification. Hence, for equal-rank Demuškin groups \(G,H\),
\[
T_\cup(G)\cong T_\cup(H).
\]

Therefore no separation pair of the form
\[
W_n(G)\cong W_n(H),\qquad T_\cup(G)\not\cong T_\cup(H)
\]
can exist under the current target definition.

### Classification

- S4 target \(T_\cup\): **INVALID / TRIVIAL TARGET — CLOSED**
- Recognition threshold as a nontrivial target: **inapplicable** (equivalently, the implication is already true at the empty/zero-information level)
- Rank-4 computation for \(T_\cup\): **STOPPED / NOT AUTHORIZED**
- S4 program: **GATE FAILURE / RE-DESIGN REQUIRED**
- Target Nontriviality Gate: **ACTIVE / LOAD-BEARING**

The notation \(r_{T_\cup}=0\) may be used only as shorthand for the trivial implication; the substantive research classification is that \(T_\cup\) is **not an admissible nontrivial Paper 3 target**.

### Methodological consequence

This establishes a mandatory pre-computation gate for all future Paper 3 targets.

For a candidate target \(T\), require:

**TN1 — Nontriviality**
\[
\exists G,H\in\mathcal C:\quad T(G)\not\cong T(H).
\]

**TN2 — Non-derivability from an already-closed target**
The candidate must not merely be a function of an already established \(\chi\)- or Bockstein-level target in a way that collapses the new theorem to a corollary.

**TN3 — Genuine filtration dependence**
There must be a plausible/verified possibility of
\[
W_n(G)\cong W_n(H),\qquad T(G)\not\cong T(H)
\]
for some finite window.

**TN4 — Prior-art audit**
No existing theorem may already supply the proposed threshold or an equivalent minimal-determining-quotient statement in the declared category.

Only a target passing TN1–TN4 may enter concrete separation computation.

### Candidate status after S4 failure

- \(T_\beta\): prior work / current Paper 3 candidate remains logically separate, but exact threshold and same-target factorization comparison require their own gates.
- \((\cup,\beta)\): **DEFERRED**; high risk of reducing to existing orientation/Bockstein machinery.
- \(\operatorname{Aut}(G)\)-orbit data: **CANDIDATE / UNSELECTED**; changes the target type to an automorphism representation.
- higher Massey-type structure: **CANDIDATE / UNSELECTED**; requires definability, nontriviality, filtration dependence, and prior-art audit.
- higher relation structure: **CANDIDATE / UNSELECTED**; same gates apply.

No candidate is selected by this record.

### Research protocol consequence

The S4 failure is a successful application of the project protocol:
\[
\text{pre-check}\to\text{definition}\to\text{target validation}\to\text{computation}.
\]
The computation stage is intentionally not entered because the target fails before any rank-4 calculation is meaningful.

This record supersedes any active status that treated S4 as ready for rank-4 separation computation.
