# Paper 4 — Complete Research Dossier

> Generated 2026-10-06 from the authoritative `seocopy70/math_research` repository. This is a research-material archive, not a replacement for the manuscript. Historical/superseded arguments are retained explicitly.

## Authority and scope

- Global map: `RESEARCH_MAP.md`
- Control tower: `CURRENT_STATE.md`
- Chronology: `research/00_RESEARCH_LOG.md`
- Continuity protocol: `research/RESEARCH_CONTINUITY_PROTOCOL.md`
- Paper 4 live state: `research/PAPER4_CURRENT_2026-10-05.md`

## Classification convention
PASS / CLOSED, PASS / LOCAL, FAIL / CLOSED, OPEN, CONDITIONAL, HISTORICAL / SUPERSEDED.

## Included source records



---

# SOURCE: research/PAPER4_CURRENT_2026-10-05.md

<!-- blob-sha: 8b5b13fed88353c20b4876b5ff84e77be201c4ac -->

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

## 2026-10-05 — A1 arbitrary pro-p closure

A1 is now **PASS / CLOSED** by a corrected weighted normal-form argument; see `research/PAPER4_GENERAL_SC_ARBITRARY_PROP_A1_CLOSURE_2026-10-05.md`.

For arbitrary pro-p (G) and open (Kle G) of index (p), with
(A=\mathbf F_p[[K]]), (J=I_K), (t=a-1), the completed group algebra has the left (A)-decomposition
[
\mathbf F_p[[G]]=\bigoplus_{r=0}^{p-1}At^r,
qquad t^p=a^p-1\in J.
]
Define
[
E_m=\bigoplus_{r=0}^{p-1}
J^{\max(0,\lceil(m-r)/p\rceil)}t^r.
]
The normal-form multiplication rules, including the previously problematic (t^rBt) terms, give (E_mE_\ell\subseteq E_{m+\ell}). Since (I_G\subseteq E_1),
[
I_G^n\subseteq E_n,
]
and therefore
[
I_G^n\cap A\subseteq J^{\lceil n/p\rceil}.
]
Using (D_n(H)=H\cap(1+I_H^n)) gives
[
\boxed{D_n(G)\cap K\subseteq D_{\lceil n/p\rceil}(K).}
]
Iteration along an index-(p^s) chain gives
[
\boxed{D_n(G)\cap K\subseteq D_{\lceil n/p^s\rceil}(K).}
]

This **supersedes the earlier 2026-10-05 A1 audit that rejected the first augmentation-ideal proof**. The false equality route and Heisenberg counterexample remain correctly classified as failures of that old proof, not counterexamples to A1 itself.

Scope distinction:
- A1/SC/SC_s validity: **PASS / CLOSED for arbitrary pro-p groups**.
- Uniform sharpness: **PASS / CLOSED in the free-pro-p witness family**; no arbitrary-pro-p sharpness claim is made.
- Pointwise sharpness for every n: **OPEN / not required**.
- Paper-4 transfer obstruction, intrinsic separation, and exact threshold: **unchanged PASS / CLOSED** in the declared odd-p, (s\ge2), even-d, nondegenerate alternating stress-family scope.

Publication interpretation: A1 is filtration infrastructure. The Paper-4-specific contribution remains the transfer obstruction, exact unmarked (a=s) versus (a=\infty) separation, and sharp threshold (n_{\mathrm{sep}}(s)=p^s+1).


## 2026-10-05 — Sharpness scope (final)

The Paper-4 sharpness claim is explicitly **uniform optimality of the factor (p^s) in the free-pro-(p) class**, not pointwise equality for every integer (n), and not sharpness for every arbitrary pro-(p) group. The witnesses
[
g_m=a^{p^m},qquad
g_{m,s}=a^{p^{m+s-1}}
]
realize equality at arbitrarily large power degrees and therefore rule out any uniform improvement of the factor (p^s). General-(n) pointwise sharpness would require additional commutator/Lie-word witnesses and is outside Paper 4.

A1 proof wording is also finalized: (J^0=A) is explicitly the convention for the truncated exponent in (E_m); the index-(p^s) chain is justified by a composition series of the finite (p)-group (G/K); and the ceiling-composition identity is reduced to the elementary (m=pq+r) check. The previously incorrect “(r=0) component” wording is not used.

## 2026-10-05 — final manuscript synchronization

The current manuscript `paper4/Paper4_strengthened_2026-10-05.tex` has been synchronized with the latest certified proofs. The obsolete Section-8 “proof architecture” placeholder and all superseded proof routes are excluded from the current manuscript.

Current publication-manuscript audit:
`research/PAPER4_FINAL_MANUSCRIPT_REAUDIT_2026-10-05.md`.

Mathematical proof content and manuscript synchronization: **PASS / CLOSED**. Remaining work is artifact-level compilation/PDF/source/checksum/bibliography/metadata audit only.



---

# SOURCE: research/PAPER4_MANUSCRIPT_FREEZE_2026-10-04.md

<!-- blob-sha: 09ad61bd88ba8d4f8b18aed3678e937d832bbe02 -->

# PAPER 4 — Manuscript freeze / PDF artifact audit — 2026-10-04

## Artifact
A publication-style Paper 4 manuscript was frozen from the authoritative research state on 2026-10-04.

Title:
**Delayed Finite-Window Visibility and Non-Rigidity of Power-Root One-Relator Pro-p Groups**

The manuscript deliberately separates:
- PASS/CLOSED: universal delayed-window lemma for n <= p^s;
- FAIL/CLOSED: arbitrary-r degree-only critical theorem;
- PASS/CLOSED: marked affine critical-lift theorem for nonzero quadratic initial relation r in D_2\D_3;
- PASS/CLOSED: stress-family non-rigidity package;
- OPEN: unmarked same-window separation and the all-s a=s versus a=infinity boundary;
- PASS/LOCAL: s=2,3 Schreier/transfer witnesses.

No superseded same-window order-jump argument is used.

## PDF verification
- Pages: 12
- PDF build: pdflatex, two-pass
- SHA-256: 39937e753368e4cb8c06dfaf2f7808727c3d88e14b75669c937ab0d06520b536
- Manuscript commit: 2c378bb767d9203e18934cf3dd215cfe965462bf
- CI run: 37172461426 (paper4-tex-build, PASS)
- GitHub Actions artifact: `paper4-pdf`, id 11292160916
- Audited local copy: `/mnt/data/Paper4_final_2026-10-04.pdf`

## Classification
**PASS / CLOSED — manuscript artifact complete.**

This closes the writing/PDF-production task, not the mathematical OPEN boundaries recorded in CURRENT_STATE.md.


## Freeze interpretation correction — 2026-10-04

The manuscript/PDF freeze is a **publication-artifact freeze**, not a permanent mathematical no-go. The certified manuscript remains unchanged while the all-s truncation boundary is unresolved. A bounded boundary audit may continue without reopening the manuscript; only a material load-bearing mathematical result (for example, a certified s=3 finite-window separator) authorizes a later manuscript revision.

The current bounded audit is recorded in `research/PAPER4_S3_BOUNDARY_QUOTIENT_AUDIT_2026-10-04.md`. The originally proposed C_3-valued functional on all of K^ab cannot detect the witness 9N_a and is closed as stated; the corrected 9-layer/C_27 projection remains open.


---

# SOURCE: research/PAPER4_FINAL_ARTIFACT_AUDIT_2026-10-05.md

<!-- blob-sha: da902476d962f0c1364b7a9a368a1dbbfd3bdef6 -->

# Paper 4 — final artifact audit addendum — 2026-10-05

## Classification

**PASS / CLOSED — final local manuscript/PDF build audited.**

The repository's `paper4-tex-2026-10-04/paper4/main.tex` was re-read against the authoritative 2026-10-05 Paper 4 state. One stale sentence remained in its abstract: it referred to a direct same-window order-jump separation for 1<=a<s<t. That route is superseded and is not used in the clean final artifact.

The regenerated artifact removes that stale claim and contains the current theorem package:

- arbitrary-pro-p subgroup-depth comparison D_n(G) cap K subseteq D_{ceil(n/p^s)}(K);
- weighted-normal-form proof, not the rejected augmentation-ideal equality route;
- uniform optimality of the p^s compression factor in the free-pro-p class;
- lower-window blindness through p^s;
- intrinsic transfer obstruction epsilon_s;
- exact unmarked separation W_{p^s+1}(G_{s,s}) notcong W_{p^s+1}(G_{s,infinity});
- exact threshold n_sep(s)=p^s+1;
- complete critical-window a-classification;
- the r=z^p boundary against the arbitrary-relator degree-only claim.

## Local artifact

- TeX: `/mnt/data/Paper4_final_2026-10-05.tex`
- PDF: `/mnt/data/Paper4_final_2026-10-05.pdf`
- PDF pages: 6
- Build: pdflatex, two passes
- PDF SHA-256: `94523f44050b343bd788e6c6e451e779a4e5a8455b9ee94d1cf58aa5cf7e1b81`
- TeX SHA-256: `071580ca2ea6c355af5f524ed20067bb5f29795cd2a26d46ee816f6b722f68df`

## Artifact checks

PASS: LaTeX compilation.

PASS: PDF text extraction.

PASS: no stale 1<=a<s<t order-jump claim in the regenerated artifact.

PASS: no arbitrary-r degree-only theorem.

PASS: no arbitrary-pro-p sharpness claim.

PASS: final PDF visually checked on first and last pages; no clipping or page-boundary corruption observed.

The previously recorded 10-page PDF SHA in `PAPER4_REVISED_MANUSCRIPT_AUDIT_2026-10-05.md` refers to an earlier local binary that is not present in the current runtime. It must not be reused as the checksum of this final local PDF.

## Mathematical scope

Odd p, s>=2, even d, nondegenerate alternating quadratic initial relation. Degenerate quadratic intrinsic separation, s=1, arbitrary-relator degree-only visibility, arbitrary-pro-p sharpness, and unrestricted absolute minimality remain unpromoted.

---

# SOURCE: research/PAPER4_FINAL_MANUSCRIPT_REAUDIT_2026-10-05.md

<!-- blob-sha: 36d58e5568632dc74ba35cbbc6e3052fc2487746 -->

# Paper 4 — Final manuscript re-audit — 2026-10-05

## Classification

**PASS / CLOSED — current manuscript proof content synchronized with the latest certified research state.**

This record supersedes the 2026-10-04 manuscript-freeze as the current publication-manuscript audit. The 2026-10-04 file remains historical provenance and is not the source of current theorem statements.

## 1. Proof-version synchronization

The manuscript `paper4/Paper4_strengthened_2026-10-05.tex` has been updated to use only the latest certified proof routes.

### Universal subgroup-depth theorem

The manuscript now uses the corrected **A1 weighted normal-form proof** for arbitrary pro-(p) groups:

[
D_n(G)cap Ksubseteq D_{lceil n/pceil}(K)
]

for open normal (K) of index (p), with the filtration

[
E_m=
igoplus_{r=0}^{p-1}
J^{max(0,lceil(m-r)/pceil)}t^r.
]

The proof explicitly handles the previously problematic (t^rJ^q) terms by normal-form multiplication and uses (t^p=a^p-1in J). It does **not** use the rejected augmentation-ideal equality or the earlier defective (E_mE_ell) argument.

Iteration gives

[
D_n(G)cap Ksubseteq D_{lceil n/p^sceil}(K).
]

The separate Magnus prefix-code proof in
`research/PAPER4_MAGNUS_PREFIX_CODE_AUDIT_2026-10-05.md`
remains an independent verification route, not the manuscript's sole logical foundation.

## 2. Sharpness

The manuscript states only the certified result:

- uniform optimality of the factor (p^s);
- witnesses in the free pro-(p) class;
- no pointwise-sharpness claim for every (n);
- no sharpness claim for arbitrary pro-(p) groups.

## 3. Transfer and critical separation

The manuscript now contains an explicit proof of the critical transfer bound

[
operatorname{im}
igl(D_{p^s+1}(G)cap K	o K^{ab}igr)
subseteq p^sK^{ab},
]

followed by the corrected intrinsic transfer predicate

[
S_s(W)=
operatorname{im}igl(W^{ab}[p^s]	o W^{ab}/pW^{ab}igr),
]

and the normalized defect (arepsilon_s).

The manuscript explicitly computes:

[
arepsilon_s(W_{p^s+1}(G_{s,s}))
e0,
qquad
arepsilon_s(W_{p^s+1}(G_{s,infty}))=0.
]

The exact separation theorem is therefore stated and proved for the certified scope:

- (p) odd;
- (sge2);
- (d) even;
- nondegenerate alternating quadratic initial form (r_2).

## 4. Exact threshold and (a)-classification

The manuscript defines the comparison pair explicitly:

[
n_{m sep}(s)
=
min{n:W_n(G_{s,s})
otcong W_n(G_{s,infty})}.
]

It proves

[
n_{m sep}(s)=p^s+1.
]

It also contains the certified complete critical-window classification:

- (1le a<s): separated by abelianization;
- (a=s): separated by the intrinsic transfer defect;
- (a>s): identical to (a=infty) at the critical window.

## 5. Superseded material excluded from the manuscript

The following are **not** used in the current manuscript:

- the old same-window order-jump proof;
- the old augmentation-ideal intersection equality;
- the defective first (E_mE_ell) proof;
- the rejected same-index Zassenhaus intersection shortcut;
- the old restricted-Lie proof of the transfer bound;
- the superseded (a=1) (H_s)-pushout argument;
- the earlier “Proof architecture” placeholder for the critical separation theorem;
- any claim that arbitrary (operatorname{ord}_Z(r)ge2) implies the critical theorem.

The historical audits remain in the repository solely as provenance and failure records, as required by the research continuity protocol. They are not manuscript evidence for the current proof.

## 6. Current evidence anchors

- `research/PAPER4_GENERAL_SC_ARBITRARY_PROP_A1_CLOSURE_2026-10-05.md`
- `research/PAPER4_MAGNUS_PREFIX_CODE_AUDIT_2026-10-05.md`
- `research/PAPER4_CURRENT_2026-10-05.md`
- `research/00_RESEARCH_LOG.md`

## 7. Publication gate

Mathematical proof content: **PASS / CLOSED**.

Manuscript synchronization: **PASS / CLOSED**.

Remaining publication tasks are artifact-level only: compile the current TeX, audit PDF/source identity, bibliography, page layout, metadata, and final checksum/package contents. No earlier proof route is to be reintroduced merely because it appears in historical research records.


---

# SOURCE: research/PAPER4_PUBLICATION_REAUDIT_2026-10-05.md

<!-- blob-sha: f9aa855a351d08f0a6a39f70287ad591a4bf0a56 -->

# Paper 4 — publication re-audit after 2026-10-05 manuscript review

## Classification

**PASS / CLOSED — mathematical core remains certified in the repository evidence.**

**Publication artifact: NOT SUBMISSION-CLOSED.**

This audit records a new manuscript-level review identifying proof-packaging and statement defects that must be corrected before a submission claim is made. These findings do not by themselves refute the certified Paper-4 theorems; they reopen the publication proof-completeness gate.

## 1. Theorem 4.1 / SC proof

The manuscript proof based on the old weighted product filtration is not valid as written. In particular, the step controlling the conjugation term
\[
\sigma(c)-c
\]
does not justify the claimed weight increase in the Schreier coordinates.

A concrete index-p example is \(c=b-1\), with \(K=\ker(F\to C_p)\), \(a\mapsto1,b\mapsto0\):
\[
\sigma(c)-c=aba^{-1}-b\in J\setminus J^2.
\]
Thus the old multiplication argument cannot support \(E_mE_\ell\subseteq E_{m+\ell}\) in that form.

The replacement proof to use is the Magnus-coordinate / finite-difference proof already independently audited in research/PAPER4_MAGNUS_PREFIX_CODE_AUDIT_2026-10-05.md. Its key coordinates are algebra coordinates
\[
w_{k,i}=(\sigma-1)^kY_{0,i},
\qquad
U=z^p-1,
\]
with ambient weights \(k+1\) and \(p\), and prefix-free initial monomials
\[
X_0^kX_i,\quad X_0^p.
\]
This avoids the defective \(\sigma(c)-c\) estimate entirely.

**Required manuscript action:** replace the old Theorem-4.1 proof in full; do not retain the defective \(E_m\)-multiplication proof.

## 2. Section 8 / critical separation proof

The current manuscript's Section 8 theorem is not publication-grade if it is presented only as “Proof architecture”. The explicit constructions and calculations must occur in the main text or in a clearly cited proof appendix.

At minimum the final proof must specify:
- the \(a\ge2\) and \(a=\infty\) metabelian/finite witness construction actually used;
- the \(a=1\) witness separately, if \(a=1\) is claimed;
- the exact group presentation/name consistently;
- the order/relations of the witness;
- the definition and provenance of the Fox derivatives \(f_x,f_y\), if the integral Fox argument is used;
- the precise quotient/filtration in which the nonvanishing or nonsplitting calculation occurs.

No “Proof architecture” label is acceptable as the final proof of the load-bearing theorem.

## 3. Proposition 9.1 / abelianization

The statement “abelianization does not see \(s\)” must be restricted to the correct parameter range.

For
\[
p^s z-p^a x_1=0
\]
the torsion factor is governed by \(\min(a,s)\). In particular, for \(a>s\), the abelianization still has an \(s\)-dependent \(p^s\)-torsion factor, and for \(a=\infty\) the abelianization still depends on \(s\).

The manuscript must not claim \(s\)-blindness of abelianization in the full \(a\ge s\) range.

## 4. Definition of \(n_{\rm sep}(s)\)

The notation must specify the pair being separated. The lower bound and upper bound previously referred to different comparison pairs.

The final definition should explicitly state that, in the certified unmarked stress-family theorem,
\[
n_{\rm sep}(s)
=
\min\{n:\,
W_n(G_{s,s})\not\cong W_n(G_{s,\infty})
\},
\]
or an equivalent precise definition, and then prove the lower bound and critical-window separation for this same pair.

## 5. Section 5 notation

The duplicate use of \(c_0\) must be removed. In particular, \(c_0=a^{p^s}\) must not coexist with \(c_0=b\) in the conjugate family.

If Schreier conjugates \(a^i b a^{-i}\) are used, their ambient Zassenhaus degree is not \(i+1\). The \(i+1\) weight belongs to the adapted \((\sigma-1)^i\)-coordinates / iterated commutator leading terms. The manuscript must use one convention consistently.

The \(r=0,q=1\) edge case for \(h_1\) must also be defined or excluded.

## 6. Minor mathematical corrections

- In the Jennings product, the condition is \(i p^j\ge n\), not \(ij\ge n\).
- Replace “\(z\in D_n(F)\) only at depth 1” with the precise filtration statement intended.
- The \(r=z^p\) counterexample can be stated more cleanly: for \(s\ge2\), the defining relation makes \(z^{p^s-p}=1\), so the comparison reduces to \(z^p=1\), and the constructed group is independent of \(s\).
- State Proposition 10.1 with \(s\ge2\) if that is its actual hypothesis; retain \(s\ge1\) only for results independently valid there.

## 7. Form and bibliography

Required before submission:
- repair the page-16 overflow/truncation;
- remove Section 14 if it contains workflow language such as PASS/CLOSED, FAIL/CLOSED, or artifact audit;
- cite references [2] and [4] where used, or remove them;
- add the Ershov–Jaikin-Zapirain source (arXiv:1007.1489) and adjust the novelty language around SC/weighted-Schreier machinery;
- strengthen the citation for the cohomological theorem (cd=2 / H^2 statement);
- align the introduction's list of main results with Theorem 4.1 and Proposition 5.1;
- distinguish the Demushkin parameter notation from the Zassenhaus filtration notation \(D_n\).

## 8. Artifact package

The final submission package should contain the actual manuscript source, dossier/evidence files, and reproduction scripts, not only references to them. The checksum manifest must be directly usable by the stated verification command, and PDF title/author metadata should be populated.

## 9. Decision

The mathematical Paper-4 core remains **PASS / CLOSED** under the repository's certified scope.

The manuscript publication gate is **OPEN / LOAD-BEARING** until:
1. Theorem 4.1 proof is replaced by the audited finite-difference Magnus proof;
2. Section 8 is converted from architecture to a complete proof, or the unsupported claim is narrowed/removed;
3. statements 9.1, n_sep, Section 5 notation, and the listed minor errors are corrected;
4. bibliography, layout, metadata, and package contents are re-audited.

No new broad mathematical branch is authorized by this audit. The next action is manuscript repair followed by an independent source-to-PDF proof/artifact audit.


---

# SOURCE: research/PAPER4_LITERATURE_AUDIT_2026-10-05.md

<!-- blob-sha: a23c30ac42b5f2c5b2639895dc5896ca7e39b02c -->

# Paper 4 — literature audit: weighted-Schreier / transfer / finite-window novelty — 2026-10-05

## Verdict

**SC is not a safe standalone novelty claim.** The uploaded Ershov–Jaikin-Zapirain source directly contains the machinery needed to derive it for the Paper-4 free pro-p / index-p setting.

The downstream result remains substantially less threatened: this audit found no source matching the specific Paper-4 combination of the intrinsic torsion-line obstruction `epsilon_s`, the stress family (z^{p^s}=x_1^{p^a}r_2^{-1}), the unmarked separation (a=s) versus (a=\infty), and the exact finite-window threshold (p^s+1).

This is **not a proof of novelty**. It is a bounded negative literature search, and the downstream claims remain **CONDITIONAL / OPEN for publication novelty**.

## 1. Primary prior source

Ershov–Jaikin-Zapirain, *Groups of positive weighted deficiency and their applications*, J. Reine Angew. Math. 677 (2013), 71–134, DOI 10.1515/crelle.2012.013.

The arXiv record confirms the paper's subject and publication identity. The published/source text contains the weighted free-pro-(p) machinery used below.

Relevant chain:

- uniform weight / standard Zassenhaus degree;
- restriction of a weight function;
- explicit index-(p) Schreier generating set;
- W-optimality of that generating set in the free case;
- power-commutator characterization/no-cancellation.

The published text also contains Lemma 3.10 with the index-(p) Schreier generators and its proof via the free restricted Lie algebra. This independently confirms that the mechanism is not an artifact of the uploaded TeX version.

## 2. Independent corroboration of the underlying Zassenhaus/Magnus framework

The later literature continues to treat the Zassenhaus filtration as the standard augmentation/Magnus filtration of free pro-(p) groups. Mináč–Rogelstad–Nguyễn compute graded dimensions for free pro-(p), Demuškin, and related groups and explicitly use the Magnus isomorphism.

Efrat's 2023 JIMJ paper / 2024 NYJM paper develops further word-combinatorial and Magnus methods for the (p)-Zassenhaus filtration and (H^2). This confirms that Magnus/word methods are established infrastructure, not by themselves evidence of novelty.

## 3. Search for the exact Paper-4 downstream construction

Searches targeted:

- finite-window / Zassenhaus + transfer;
- (p^s)-torsion in abelianized index-(p) kernels;
- (D_{p^s+1}) transfer behavior;
- the stress relation (z^{p^s}=x_1^{p^a}r_2^{-1});
- exact threshold (p^s+1);
- intrinsic/unmarked finite-window transfer defects.

No retrieved source matched the complete construction.

The literature does contain important adjacent transfer/cohomological results. In particular, Efrat's work on the Zassenhaus filtration and representations, and later work on Magnus formations, studies finite quotients, cohomology, unitriangular representations, and transfer principles. These are relevant background and must be cited/positioned, but the retrieved material does not state the Paper-4 `epsilon_s) invariant or the exact (a=s) versus (a=\infty) separation at (p^s+1).

## 4. Important literature threat that must be acknowledged

Efrat's transfer/intersection framework is a real neighboring theory. His work explains that cohomological transfer principles can recover several intersection theorems for Zassenhaus-type filtrations and connects finite quotients with cohomology and representations.

Therefore the manuscript must **not** claim that Paper 4 is the first work to connect transfer, finite quotients, Magnus methods, or Zassenhaus filtration.

The defensible claim is narrower:

> the Paper-4 contribution is the specific intrinsic finite-window obstruction and the resulting sharp separation theorem for the declared stress family, if the full literature audit remains negative.

## 5. Novelty classification

| Object | Current classification |
|---|---|
| SC (D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K)) | **PASS/CLOSED mathematically; not standalone novelty** |
| Magnus prefix-code proof of SC | **PASS/CLOSED; self-contained reproof/bridge** |
| TF_s | **PASS/CLOSED mathematically; novelty downstream** |
| intrinsic (epsilon_s) | **OPEN — strongest novelty candidate** |
| unmarked (a=s) vs (a=\infty) separation | **OPEN — strong theorem-level novelty candidate** |
| exact threshold (p^s+1) | **OPEN — strong sharpness/application candidate** |
| overall Paper-4 publication novelty | **CONDITIONAL / OPEN** |

## 6. Required next literature audit

The next search should be narrower rather than broader:

1. Search Efrat/Mináč/Matzri/Quadrelli literature for **transfer maps on (H^1) or (K^{ab})** attached to index-(p) kernels at a prescribed Zassenhaus depth.
2. Search for **Bockstein + cup-product / relation-class combinations** producing a one-dimensional (p^s)-torsion line.
3. Search for **finite quotient separation by transfer**, especially where lower windows are provably identical and only a critical window separates two presentations.
4. Search citations to Ershov–Jaikin-Zapirain and to the relevant Zassenhaus intersection/transfer papers for any later use of the exact inequality or an equivalent finite-window form.
5. Only after these searches remain negative should the manuscript use language such as “apparently new” or “to the best of our knowledge”.

## 7. Bottom line

The literature audit strengthens, rather than weakens, the current Paper-4 strategy:

**remove SC from the novelty headline; retain it as the established filtration-comparison input; concentrate the novelty claim on the intrinsic transfer obstruction and the sharp finite-window separation.**

No mathematical Paper-4 result is reopened by this audit.


---

# SOURCE: research/PAPER4_MAGNUS_PREFIX_CODE_AUDIT_2026-10-05.md

<!-- blob-sha: aae52543ead8406ea40247f736f38b0b0b0af9c3 -->

# Paper 4 — Magnus prefix-code proof audit — 2026-10-05

## Classification

**SC_s: PASS / CLOSED.**  
**TF_s: PASS / CLOSED as a consequence of SC_s.**  
**a=s versus a=∞ at the critical window: PASS / CLOSED in the declared stress-family scope, after correcting the intrinsic torsion-line formulation.**

This audit records the independent proof and verification of the remaining all-s transfer-defect gate.

## 1. Exact subgroup comparison

Let F be a finitely generated free (pro-p) group and let
\[
\chi:F\twoheadrightarrow C_p
\]
be an index-p character. Choose a free basis
\[
z,x_1,\ldots,x_d,
\qquad \chi(z)=1,\quad \chi(x_i)=0,
\]
and put K=ker(chi).

The target is
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
\tag{SC}
\]

The proof uses the completed Magnus algebras over F_p.

### Schreier coordinates

Use the standard index-p Schreier basis
\[
u=z^p,\qquad y_{j,i}=z^j x_i z^{-j}\quad(0\le j\le p-1),
\]
and write
\[
U=u-1,\qquad Y_{j,i}=y_{j,i}-1.
\]
Then the completed group algebra of the free group K is the completed free associative algebra in the degree-one variables U,Y_{j,i}.

Let sigma denote conjugation by z on the Schreier orbit and
\[
\delta=\sigma-1.
\]
For 0\le k<p define
\[
w_{k,i}=\delta^kY_{0,i}.
\]
The transformation from (Y_{0,i},...,Y_{p-1,i}) to (w_{0,i},...,w_{p-1,i}) is invertible over F_p. Its coefficient matrix is unitriangular in the ordered basis e_0, sigma e_0,...,sigma^{p-1}e_0; equivalently its determinant is 1.

Thus U and all w_{k,i} are again a complete free coordinate system of the completed augmentation algebra. They are **algebra coordinates**, not group generators.

## 2. Initial terms

Put
\[
X_0=z-1,\qquad X_i=x_i-1.
\]
For the convention sigma(a)=zaz^{-1},
\[
\sigma(Y)-Y
=(1+X_0)(1+Y)(1+X_0)^{-1}-(1+Y).
\]
Hence its lowest Magnus-degree part is
\[
[X_0,Y].
\]
With degree-lexicographic order in which X_0 is the largest letter,
\[
\operatorname{in}(w_{k,i})=X_0^kX_i,
\qquad
\operatorname{in}(U)=X_0^p.
\tag{I}
\]
The second identity follows from
\[
(1+X_0)^p-1=X_0^p
\]
in characteristic p.

The local symbolic checks give the coefficient determinants
\[
1\pmod p
\]
for p=3,5,7,11, and verify (I) directly for p=3,5.

## 3. Prefix-code lemma

The set of initial monomials
\[
\mathcal C_p=
\{X_0^kX_i:0\le k<p,\ i\ge1\}
\cup\{X_0^p\}
\]
is prefix-free.

Indeed, every X_0^kX_i ends with a letter X_i\ne X_0, while X_0^p consists entirely of X_0's. Two words of the first type cannot prefix one another because after the common X_0-run one encounters X_i versus either X_0 or a different X_j.

Therefore concatenations of codewords have unique parsing. In particular distinct coordinate words have distinct initial monomials.

This is not merely an experimental observation: exhaustive concatenation tests through coordinate-word length 4 for p=3,5,7 found no collisions, independently confirming the parsing argument.

## 4. Magnus-coordinate lemma

Let f be a nonzero element of the completed augmentation algebra of K, written in the U,w_{k,i} coordinates. Give each coordinate the ambient F-weight
\[
\mathrm{wt}(U)=p,
\qquad
\mathrm{wt}(w_{k,i})=k+1.
\]
For a coordinate word W define d(W) as the sum of its weights.

For every nonzero f,
\[
\operatorname{ord}_F(f)=\min_{c_W\ne0}d(W).
\tag{M}
\]

Proof:
1. The lowest homogeneous part of a product is the product of the lowest homogeneous parts because the completed free associative algebra has no zero divisors at the monomial-leading-term level.
2. By (I), the initial monomial of W is the concatenation of the codewords attached to its coordinates.
3. Prefix-freeness makes those concatenations distinct for distinct coordinate words.
4. Hence, at the minimum weighted degree, no distinct coordinate words can cancel their leading monomials.
5. In every fixed degree there are only finitely many coordinate words (the rank is finite), so completion causes no additional cancellation problem.

Thus (M) is a theorem of the completed Magnus-coordinate algebra, not a finite-degree experimental assertion.

## 5. Deduction of SC

Suppose f=g-1 with 0\ne g\in D_n(F)\cap K. If g had K-order ell<ceil(n/p), choose a nonzero lowest K-word contribution of length ell. Every coordinate has ambient weight at most p, so its weighted degree is at most p ell<n. By (M), ord_F(f)<n, contradiction.

Therefore
\[
\boxed{D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K)}
\]
for every n and every index-p kernel K of a free group F.

At
\[
n=p^s+1
\]
this gives exactly
\[
D_{p^s+1}(F)\cap K
\subseteq D_{p^{s-1}+1}(K),
\]
which is (SC_s).

The factor p is sharp: z^{p^s} has F-order p^s, while in K the free coordinate u=z^p gives K-order p^{s-1}.

## 6. Independent computational verification

An independent sparse Magnus implementation over F_3 was used on the concrete index-3 kernel with basis z,x,y.

Verified:
- [z^9,x] has F-order 10 and K-order 4;
- the 9-fold iterated commutator ad_z^9(x) has F-order 10 and K-order 4;
- the triple iterated commutator ad_{z^3}^3(x) has F-order 10 and K-order 4;
- 30 random products/inverses of these D_10(F) witnesses all had K-order at least 4;
- the sharp witness pattern z^{3^s} has ambient/K order ratio 3 at s=1,2,3, and the analogous p=5,s=2 ratio is 5.

These computations are sanity checks; the proof of (SC) is the Magnus-coordinate lemma above.

## 7. TF_s

For
\[
m=p^{s-1}+1,
\]
the Jennings product formula gives
\[
D_m(K)=\prod_{ip^j\ge m}\gamma_i(K)^{p^j}.
\]
After abelianization all gamma_i(K), i>=2, vanish, while the first surviving pure-power exponent is p^s. Hence
\[
\operatorname{im}(D_m(K)\to K^{ab})\subseteq p^sK^{ab}.
\]
Together with (SC_s),
\[
\boxed{
\operatorname{im}(D_{p^s+1}(F)\cap K\to K^{ab})
\subseteq p^sK^{ab}.
}
\tag{TF_s}
\]
Thus TF_s is now PASS / CLOSED, not an independent open lemma.

## 8. N∩K and the stress-family relator

For
\[
G_{s,a}=F/\overline{\langle\!\langle z^{p^s}x_1^{-p^a}r_2^{-1}\rangle\!\rangle},
\]
with a>=1 and r_2 a product of commutators in the x_i, the defining relator has trivial chi-value, so its normal closure R lies in K. Since D_{p^s+1}(F)\subseteq K,
\[
N:=D_{p^s+1}(F)R\subseteq K,
\qquad
N\cap K=N.
\]
Moreover r_2\in[K,K], because all x_i lie in K. Thus r_2 contributes zero in K^{ab}. The abelianized Schreier relation is therefore
\[
p^{s-1}U-p^aA_i=0
\]
(on each conjugate orbit, with the sign depending only on the chosen relator convention). For a=s this is exactly the lattice L_s used in the previous model audits.

For a=∞ the power relation z^{p^s}=r_2 is absent; in K^{ab} the right-hand side is zero, so the U-direction is not subject to the finite p^s relation coming from the stress power.

## 9. Survival of the critical transfer witness

On the a=s side, the model Schreier class
\[
p^{s-1}(\sigma-1)^{p-1}A_0
\]
has order p^s in the untruncated lattice, hence its image modulo p^s is nonzero.

The only possible way the finite-window truncation could kill this class is through the image of D_{p^s+1}(F)\cap K in K^{ab}. But (TF_s) places that entire image inside p^sK^{ab}. Therefore the critical class survives in the finite-window quotient modulo p^s.

The a=∞ side has no corresponding power relation in the U-direction, and the normalized transfer defect is zero in the quotient.

The s=3 model calculation (p=3,s=3) remains an independent local witness and is consistent with this all-s proof.

## 10. Correct intrinsic transfer formulation

The earlier shorthand T=W^{ab}[p^s] was too coarse if interpreted as a single element. In
\[
W^{ab}\cong \mathbf Z/p^s\oplus(\mathbf Z/p^{s+1})^d,
\]
define the canonical one-dimensional subspace
\[
S_s(W):=\operatorname{im}\bigl(W^{ab}[p^s]\to W^{ab}/pW^{ab}\bigr).
\]
This is one-dimensional over F_p in the declared stress-family scope: the p^s-cyclic factor contributes one generator, while the p^{s+1}-factors contribute only p-divisible p^s-torsion and vanish modulo pW^{ab}.

Choose any t\in W^{ab}[p^s] whose image spans S_s(W). The corrected intrinsic predicate is
\[
\varepsilon_s(W):
=
p^{s-1}V(t)
\pmod{p^sK^{ab}}
\in K^{ab}/p^sK^{ab}.
\]
It is well-defined up to multiplication by a unit:
if t is replaced by another lift of the same line, the difference lies in pW^{ab}, hence after applying p^{s-1}V it lies in p^sK^{ab}.

Thus nonvanishing of epsilon_s(W) is independent of the marked lift and isomorphism-invariant, once the cup-radical line defining K is used. This fixes the only genuine gauge ambiguity in the previous transfer formulation.

## 11. Final separation gate

The stress-family cup-radical line is one-dimensional **only in the declared nondegenerate quadratic scope**: d is even and the alternating form defined by r_2 on the x-space is nondegenerate (for example, d=2 and r_2=[x_1,x_2]). In that scope the radical is exactly \(\langle z^*\rangle\), so K is intrinsic.

For W_n with n\ge3, the defining power relation lies in D_3(F), so it does not alter the degree-2 relation class. Hence the same nondegenerate quadratic cup form is visible intrinsically in H^1(W_n,\mathbf F_p) and H^2(W_n,\mathbf F_p), with radical line \(\langle z^*\rangle\).

The corrected \(\varepsilon_s\) is therefore an intrinsic finite-window invariant in this scope.

- a=s: take t=z-x_1. Then V(t)=U-\sum_jA_j, while \(p^{s-1}U=0\) modulo the a=s relation lattice and p^s. Hence
\[
\varepsilon_s(W_{s,s})=-p^{s-1}\sum_jA_j\ne0.
\]
- a=∞: take t=z. Then V(t)=U and \(p^{s-1}U\in\operatorname{im}R\), so
\[
\varepsilon_s(W_{s,\infty})=0.
\]

The separation statement is certified here for **s\ge2**; the s=1 case is intentionally not promoted by this audit.

Hence, for every odd p and s>=2 in the declared stress-family scope,
\[
\boxed{
W_{p^s+1}(G_{s,s})
\not\cong
W_{p^s+1}(G_{s,\infty}).
}
\]

Combined with the already certified lower-window blindness, the exact unmarked separation threshold is
\[
\boxed{n_{\rm sep}(s)=p^s+1}.
\]

## 12. Scope and literature boundary

The standard Magnus embedding and Jennings/Zassenhaus descriptions used here are classical. The web literature check located standard statements of the Magnus embedding and the Zassenhaus/Jennings formulas, but no directly matching index-p subgroup comparison in the form (SC). Therefore the present proof should be treated as an explicit derivation in this setting, not attributed to a previously located theorem.

This does not by itself establish publication-level novelty; a fuller literature audit can be done separately if needed.

## Final classification

- Magnus coordinate change: **PASS / CLOSED**.
- Prefix-code leading-word lemma: **PASS / CLOSED**.
- General (SC): **PASS / CLOSED** for index-p kernels of finitely generated free groups.
- (SC_s): **PASS / CLOSED**.
- (TF_s): **PASS / CLOSED**.
- a=s Schreier critical witness: **PASS / LOCAL -> promoted by TF_s to the declared finite-window conclusion**.
- corrected intrinsic transfer invariant: **PASS / CLOSED in the declared stress-family scope**.
- a=s versus a=∞: **PASS / CLOSED**.
- exact critical boundary threshold n_sep(s)=p^s+1: **PASS / CLOSED** for the declared stress-family scope.
