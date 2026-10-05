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


## 2026-10-05 — SC novelty audit closed; research moves downstream

The SC literature audit is now **CLOSED**. The correct publication-level wording is deliberately narrower and stronger than either “SC is classical” or “SC is wholly new”:

- The existing Zassenhaus/Magnus/weighted-Schreier literature supplies the ingredients: uniform-weight realization of Zassenhaus degree, restriction of weights to subgroups, index-p Schreier coordinates, and the no-cancellation/weight-function principle.
- The exact subgroup-depth comparison used by Paper 4,
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K),
\]
was not located as a directly stated prior theorem in the audited sources.
- Paper 4's **new logical step is the assembly/deduction of this comparison in exactly the form needed to control the finite-window truncation**, with the downstream consequence (TF_s) and the intrinsic transfer obstruction.
- The independent Magnus prefix-code proof is retained as a self-contained verification/alternative derivation, not as a claim of new foundational Magnus theory.

Accordingly the SC gate is **PASS / CLOSED** and the novelty audit is **CLOSED**. No further generic Zassenhaus/Schreier literature search is authorized unless a downstream proof forces it.

### Next load-bearing question: how far SC strengthens Paper 4

The next task is no longer to justify SC. It is to maximize the theorem that follows from it.

Authorized targets, in descending priority:

1. **Promote the transfer statement to a clean general lemma:** for every index-p kernel of a finitely generated free pro-p group and every n,
\[
\operatorname{im}(D_n(F)\cap K\to K^{ab})
\subseteq
p^{\lceil n/p\rceil?}K^{ab}
\]
only after the exponent is re-derived carefully from the Jennings product; do not guess the exponent. The already certified critical specialization remains
\[
\operatorname{im}(D_{p^s+1}(F)\cap K\to K^{ab})\subseteq p^sK^{ab}.
\]
2. **Separate marked from intrinsic statements:** first formulate the strongest SC+TF finite-window theorem for an arbitrary index-p character/marked kernel K; then specialize to the intrinsic nondegenerate quadratic stress family where the radical line makes K canonical.
3. **Test scope enlargement of the stress theorem:** determine whether the exact \(p^s+1\) separation can be stated for a broader class of quadratic initial relations than the currently declared nondegenerate alternating scope, without silently inserting a presentation-dependent orientation.
4. **Check sharpness:** use the explicit z^{p^s} witness and the SC bound to state exactly which part is universal (filtration compression) and which part is family-specific (nonzero intrinsic transfer defect).

The governing principle is: **SC is now infrastructure; \(\varepsilon_s\), exact unmarked separation, and the sharp threshold are the theorem.**


## 2026-10-05 — SC theorem strengthening: general transfer-depth law and complete critical-a classification

The SC closure is now promoted from a critical-window tool to a general transfer-depth principle.

For every index-p kernel K of a finitely generated free pro-p group F,
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
Put
m=\lceil n/p\rceil,  e(n)=\lceil\log_p m\rceil.
By the Jennings–Lazard description of the Zassenhaus filtration and abelianization,
\operatorname{im}(D_n(F)\cap K\to K^{ab})\subseteq p^{e(n)}K^{ab}.
At n=p^s+1, e(n)=s, recovering TF_s.

This general transfer-depth statement is PASS / CLOSED.

### Complete classification of the critical window by a

For the declared stress family W_{s,a}=W_{p^s+1}(G_{s,a}), the parameter a is now completely classified at the critical window.

- If 1\le a<s, the defining relation has abelianized form p^s z-p^a x_1=0, and Smith normal form gives
  W_{s,a}^{ab}\cong \mathbf Z_p/p^a\oplus(\mathbf Z_p/p^{s+1})^d.
  Hence 1\le a<b<s are pairwise separated already by abelianization.

- If a>s, then p^a\ge p^{s+1}>p^s+1, so x_1^{p^a}\in D_{p^s+1}(F). The power term disappears in the critical truncation and W_{s,a}=W_{s,\infty}. Thus the entire range a>s is saturated with the a=\infty window.

- If a=s, then abelianization agrees with a=\infty:
  W_{s,s}^{ab}\cong W_{s,\infty}^{ab}\cong \mathbf Z_p/p^s\oplus(\mathbf Z_p/p^{s+1})^d.
  The already certified intrinsic transfer witness \varepsilon_s is nonzero for a=s and zero for a=\infty, hence W_{s,s}\not\cong W_{s,\infty}.

Therefore a\mapsto W_{p^s+1}(G_{s,a}) has exactly one nontrivial boundary layer at a=s; all a>s are saturated with a=\infty, while all a<s are separated by abelianization.

Classification: PASS / CLOSED for odd p, s\ge2, even d, and nondegenerate alternating r_2 in the declared intrinsic stress-family scope.

This strengthens the Paper-4 theorem: the critical window does not merely separate a=s from a=\infty; it completely describes how much of the exponent parameter a survives at the critical truncation.

### Scope boundary

The nondegenerate quadratic hypothesis remains an intrinsicity condition, not a cosmetic computational assumption: it supplies the canonical one-dimensional cup-radical needed to define K. Degenerate quadratic forms have larger radical and do not currently yield a canonical single character. The s=1 case remains intentionally unpromoted.

The failed arbitrary-r degree-only theorem remains FAIL / CLOSED and is not reopened.


## 2026-10-05 — SC_s generalization and uniform sharpness closed

The theorem-strengthening gate is now closed.

For every finitely generated free pro-p group F and open K of index p^s, a subnormal index-p chain F=K_0>K_1>...>K_s=K and repeated application of SC give
\[
D_n(F)\cap K\subseteq D_{\lceil n/p^s\rceil}(K).
\]
The ceiling operation composes exactly, so no rounding loss accumulates.

The bound is **uniformly sharp**. For F=<a,b> and K=ker(F -> C_{p^s}) with a mapping to a generator and b to 0, the Schreier basis contains c_0=a^{p^s}. Hence g_m=a^{p^{m+s-1}}=c_0^{p^{m-1}} lies in D_{p^{m+s-1}}(F)\cap K but not in D_{p^{m-1}+1}(K). Therefore the proposed universal improvement D_n(F)\cap K subseteq D_{\lceil n/p^s\rceil+1}(K) is false.

This establishes the correct publication-level statement: SC_s is a general index-p^s transfer-depth law, and its p^s compression factor is uniformly optimal. We deliberately do **not** claim pointwise sharpness for every integer n; the simpler infinite family of equality witnesses is sufficient.

Evidence: research/PAPER4_SC_SHARPNESS_AND_INDEX_PS_AUDIT_2026-10-05.md.

Interpretation: SC/SC_s are universal filtration infrastructure. The Paper-4-specific contribution remains the intrinsic transfer obstruction, exact critical-window separation, and threshold p^s+1 in the declared nondegenerate quadratic stress-family scope.


## 2026-10-05 — revised manuscript/PDF artifact

The theorem-strengthened Paper 4 manuscript has been regenerated from the authoritative current state. The revision incorporates SC/SC_s, uniform sharpness, the general transfer-depth law, the intrinsic transfer obstruction, exact unmarked separation, the threshold (p^s+1), and the complete critical-window classification of (a).

Artifact audit: `research/PAPER4_REVISED_MANUSCRIPT_AUDIT_2026-10-05.md`.

Local artifacts: `/mnt/data/Paper4_revised_2026-10-05.tex` and `/mnt/data/Paper4_revised_2026-10-05.pdf`.
PDF SHA-256: `8b400f16ff1e3a0cfe7501dbc2b771279b3917f63f18cddb77f67ec9a695a25d`.

Classification remains **PASS / CLOSED** in the declared scope.