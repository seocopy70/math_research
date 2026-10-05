# Paper 4 — Current State (2026-10-05)

## Classification

**PASS / CLOSED — certified core and exact all-s boundary in the declared stress-family scope.**

This file is a navigation summary. The dated audits and `00_RESEARCH_LOG.md` remain the evidence record.

## Certified core

- Delayed-window invisibility: for the declared stress family, the hidden power relation is invisible below the critical lower-window scale; this is the certified lower-bound mechanism.
- Nonzero quadratic initial relation (r_2\in D_2\setminus D_3): the marked critical-layer mechanism survives at (n=p^s+1) in the stated scope.
- (operatorname{ord}_Z(r)\ge2) alone is insufficient for the stronger arbitrary-relation degree-only theorem; the counterexample/boundary is retained.
- The stress family has (s)-independent abelianization and, in the declared mild scope, (H^*(-,\mathbf F_p)) and the associated graded shadow are also (s)-independent.
- Ordinary mod-(p) cohomology and bare graded data are therefore closed as blind routes for the declared stress family.

## Resolved former boundary

The former all-s transfer-defect boundary is now closed by the Magnus prefix-code proof.

- The index-p subgroup comparison (SC) is **PASS / CLOSED**.
- (TF_s) is **PASS / CLOSED** as an immediate abelianized consequence.
- The corrected intrinsic transfer invariant is **PASS / CLOSED** in the declared stress-family scope.
- Therefore
\[
W_{p^s+1}(G_{s,s})\not\cong W_{p^s+1}(G_{s,\infty})
\]
for every odd p and s>=2 in the declared scope, with d even and r_2 nondegenerate.
- Combined with lower-window blindness, the exact critical-boundary threshold is
\[
n_{\rm sep}(s)=p^s+1.
\]

The old order-jump argument remains **FAIL / CLOSED / SUPERSEDED** and is not used.

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

**Paper 4's previously load-bearing all-s boundary is now mathematically closed in the declared stress-family scope. Final manuscript promotion still requires the normal independent manuscript/evidence audit; no old order-jump argument is revived.**


## 2026-10-05 — active SC_s attack: Magnus prefix-code route

A new load-bearing attack on (SC_s) is now authorized and independently audited. The proposed finite-difference variables must be interpreted as **augmentation-algebra coordinates**, not free group generators: \(w_{k,i}=\delta^k(Y_{0,i})\) are linear combinations of the Schreier augmentation generators \(Y_{j,i}\), and the coefficient matrix is lower unitriangular with determinant 1.

Local symbolic checks for \(p=3,5\) verify \(\operatorname{in}(w_{k,i})=X_0^kX_i\) and \(\operatorname{in}(z^p-1)=X_0^p\). For \(p=3,5,7\), the proposed leading monomials form a prefix code and concatenations through word length 3 have no collisions. These are PASS / LOCAL checks only.

The resulting corrected target is a general Magnus-algebra lemma: the leading monomial of a nonzero word in the \(w_{k,i},u\) coordinates is uniquely determined by its coordinate word, so F-degree equals the minimum weighted coordinate degree. Since every coordinate has F-degree at most \(p\), this would imply
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K),
\]
and hence (SC_s) at \(n=p^s+1\).

Status: **OPEN / LOAD-BEARING candidate proof; local symbolic prefix-code checks PASS / LOCAL.** The TF_s truncation/nonzero-transfer step remains a separate open gate even if this lemma closes.


## 2026-10-05 — Magnus prefix-code closure and transfer-boundary resolution

See `research/PAPER4_MAGNUS_PREFIX_CODE_AUDIT_2026-10-05.md`.

The completed Magnus-coordinate argument proves, for every index-p kernel K of a finitely generated free group F,
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
\]
The proof uses the invertible finite-difference coordinate change, the initial terms (X_0^kX_i) and (X_0^p), and the prefix-free code of initial monomials. Independent p=3 sparse Magnus checks confirm the critical examples.

Consequently (SC_s) and (TF_s) are PASS / CLOSED. The stress-family Schreier relation gives the same model lattice already audited, and the truncation image lies in (p^sK^{ab}), so the critical (a=s) transfer witness survives.

The intrinsic transfer predicate is corrected to a line in (W^{ab}[p^s]) modulo (pW^{ab}), evaluated in (K^{ab}/p^sK^{ab}). This removes the lift ambiguity in the earlier shorthand (T=W^{ab}[p^s]).

**Current classification: PASS / CLOSED for the exact unmarked threshold (n_{\rm sep}(s)=p^s+1) in the declared stress-family scope.**


## 2026-10-05 — §9–§11 independent review corrections incorporated

The independent review confirms the Magnus (SC) proof and the resulting separation mechanism, while correcting several statements in the first closure write-up.

- **§9 survival:** nonzero order in the untruncated lattice is not enough. Modulo p^s, the a=s relation gives p^{s-1}U=0 and \((\sigma-1)^{p-1}A_0\equiv\sum_jA_j\pmod p\), hence the critical class is explicitly nonzero in the model quotient. The TF_s image lies in p^sK^ab and cannot kill it.
- **§11 direct representatives:** for a=s, t=z-x_1 and \(\varepsilon_s=-p^{s-1}\sum_jA_j\ne0\); for a=∞, t=z and \(\varepsilon_s=0\) because p^{s-1}U lies in the relator image.
- **Intrinsic scope:** d is even and the alternating quadratic form defined by r_2 is nondegenerate (basic example d=2, r_2=[x_1,x_2]). Because the defining power relation lies in D_3, the degree-2 cup form is unchanged on W_n (n\ge3), so the radical line \(\langle z^*\rangle\) is intrinsic.
- **Schreier indexing:** 0\le j\le p-1.
- **s=1:** deliberately not promoted; the certified exact-separation scope remains s\ge2.

Classification remains **PASS / CLOSED** for the corrected declared stress-family scope; novelty remains a separate literature-audit question.


## 2026-10-05 — weighted-Schreier source audit changes the novelty boundary

The uploaded *Groups of positive weighted deficiency and their applications* TeX source was directly inspected. The source's `uniform2` + `weight_preserve` + `index_p0` + `cor1` chain derives
[
D_n(F)cap Ksubseteq D_{lceil n/pceil}(K)
]
for free pro-(p) (F) and index-(p) (K), after specializing the uniform weight to ordinary Zassenhaus degree. The no-cancellation step is explicit in `cor1` for arbitrary power-commutator factorizations, so there is no remaining gap at the SC derivation level.

Accordingly:

- SC mathematical validity: **PASS / CLOSED**.
- SC as standalone novelty: **CONDITIONAL / likely not novel; do not claim novelty**.
- Magnus prefix-code proof: **PASS / CLOSED as a self-contained reproof/coordinate bridge; no standalone novelty claim**.
- Paper-4 certified theorem: **PASS / CLOSED** in the declared scope.
- Publication novelty: **CONDITIONAL / OPEN**.
- Authorized novelty target: intrinsic (arepsilon_s), exact (a=s) versus (a=\infty) separation, and the sharp threshold (n_{\rm sep}(s)=p^s+1).

The source audit does **not** reopen or weaken the Paper-4 theorem. It narrows the claim about where the contribution is new.
