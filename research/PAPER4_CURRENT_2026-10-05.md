# Paper 4 — Current State (2026-10-05)

## Classification

**PASS / CLOSED — certified core.**  
**OPEN / LOAD-BEARING — exact same-window/all-s extension boundary.**

This file is a navigation summary. The dated audits and `00_RESEARCH_LOG.md` remain the evidence record.

## Certified core

- Delayed-window invisibility: for the declared stress family, the hidden power relation is invisible below the critical lower-window scale; this is the certified lower-bound mechanism.
- Nonzero quadratic initial relation (r_2\in D_2\setminus D_3): the marked critical-layer mechanism survives at (n=p^s+1) in the stated scope.
- (operatorname{ord}_Z(r)\ge2) alone is insufficient for the stronger arbitrary-relation degree-only theorem; the counterexample/boundary is retained.
- The stress family has (s)-independent abelianization and, in the declared mild scope, (H^*(-,\mathbf F_p)) and the associated graded shadow are also (s)-independent.
- Ordinary mod-(p) cohomology and bare graded data are therefore closed as blind routes for the declared stress family.

## Explicit open boundary

The exact unmarked statement
[
W_{p^s+1}(G_s)\not\cong W_{p^s+1}(G_t)
]
and the exact threshold (n_{\rm sep}(s)=p^s+1) are **OPEN**.

The proposed order-jump/quotient argument is **FAIL / CLOSED** because the defining normal subgroups are not nested.

The all-(s) transfer-defect route is **OPEN / LOAD-BEARING** through ((SC_s)) / ((TF_s)). The (p=3,s=2) and (p=3,s=3) calculations are **PASS / LOCAL** only.

## Historical/superseded routes

Retain, but do not treat as current:

- the old same-window order-jump claim;
- augmentation-ideal intersection shortcut;
- same-index Zassenhaus intersection shortcut;
- restricted-Lie induction for (TF_s);
- universal (E_\psi) generator branch unless deliberately reopened as a separate generalization;
- other failed intrinsic-orientation/carrier proposals.

## Current repository anchors

- manuscript/freeze: `research/PAPER4_MANUSCRIPT_FREEZE_2026-10-04.md`
- evidence index: `research/02_EVIDENCE_INDEX.md`
- chronology/corrections: `research/00_RESEARCH_LOG.md`
- transfer boundary: `research/PAPER4_ALL_S_TRANSFER_DEFECT_REDUCTION_2026-10-04.md`
- root visibility audit: `research/PAPER4_ROOT_VISIBILITY_NONRIGIDITY_AUDIT_2026-10-04.md`

**Do not call Paper 4 FINAL without explicitly resolving the OPEN all-(s) boundary or intentionally freezing the paper with that boundary stated.**


## 2026-10-05 — active SC_s attack: Magnus prefix-code route

A new load-bearing attack on (SC_s) is now authorized and independently audited. The proposed finite-difference variables must be interpreted as **augmentation-algebra coordinates**, not free group generators: \(w_{k,i}=\delta^k(Y_{0,i})\) are linear combinations of the Schreier augmentation generators \(Y_{j,i}\), and the coefficient matrix is lower unitriangular with determinant 1.

Local symbolic checks for \(p=3,5\) verify \(\operatorname{in}(w_{k,i})=X_0^kX_i\) and \(\operatorname{in}(z^p-1)=X_0^p\). For \(p=3,5,7\), the proposed leading monomials form a prefix code and concatenations through word length 3 have no collisions. These are PASS / LOCAL checks only.

The resulting corrected target is a general Magnus-algebra lemma: the leading monomial of a nonzero word in the \(w_{k,i},u\) coordinates is uniquely determined by its coordinate word, so F-degree equals the minimum weighted coordinate degree. Since every coordinate has F-degree at most \(p\), this would imply
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K),
\]
and hence (SC_s) at \(n=p^s+1\).

Status: **OPEN / LOAD-BEARING candidate proof; local symbolic prefix-code checks PASS / LOCAL.** The TF_s truncation/nonzero-transfer step remains a separate open gate even if this lemma closes.
