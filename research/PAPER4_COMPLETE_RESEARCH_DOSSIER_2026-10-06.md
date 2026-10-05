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


---

# SOURCE: research/PAPER4_ALL_S_TRANSFER_DEFECT_PROOF_AUDIT_2026-10-04.md

<!-- blob-sha: 12b008dc44b88244350fc2994f927a758c754d7b -->

# Paper 4 — all-s transfer-defect proof audit — 2026-10-04

Proposed proof does not close the all-s boundary. The model Schreier-lattice calculation remains PASS / LOCAL, but the proposed Step 7 does not prove the load-bearing truncation-image bound TF_s: im(D_{p^s+1}(F)∩K -> K^ab) subset p^s K^ab.

The missing bridge remains SC_s: D_{p^s+1}(F)∩K subset D_{p^{s-1}+1}(K), or an independent direct proof of TF_s. The k=1 argument conflates ambient leading degree with internal Schreier degree and does not control cancellation or the associated-graded map for the subgroup intersection. Step 8 only explains the internal abelianization consequence after that missing bridge has effectively been assumed.

The identity u^{p^{s-1}} having ambient weight p^s is valid for that element, but does not imply that every g in D_{p^s+1}(F)∩K has u-coordinate divisible by p^s. The proposed bi-degree substitution also lacks a theorem comparing ambient and subgroup filtrations.

Separate scope warning: a general nonzero quadratic initial relation need not have a unique one-dimensional cup-radical line. The broader quadratic-family statement therefore needs an explicit radical hypothesis or restriction to the audited control/stress scope.

Classification: model lattice PASS / LOCAL; Step 7 proof route FAIL / CLOSED; TF_s OPEN / LOAD-BEARING; all-s a=s versus a=infinity OPEN / LOAD-BEARING; Paper 4 certified core PASS / CLOSED — FROZEN. No all-s promotion and no new Paper 4 computation is authorized.


---

# SOURCE: research/PAPER4_ALL_S_TRANSFER_DEFECT_REDUCTION_2026-10-04.md

<!-- blob-sha: bdf00d39e35d8713e490a4afd3825951bc7ad6ea -->

# Paper 4 — all-s transfer-defect reduction (2026-10-04)

## Target

For the remaining boundary
\[
W_{p^s+1}(G_{s,s}) \stackrel{?}{\cong} W_{p^s+1}(G_{s,\infty}),\qquad s\ge2,
\]
prove the intrinsic transfer defect is nonzero on the \(a=s\) side and zero on the \(a=\infty\) side.

## Pre-check

- **Object:** \(W=W_{p^s+1}\), its intrinsic cup-radical line, \(K=\ker\chi\), and the canonical transfer \(V:W^{ab}\to K^{ab}\).
- **Input:** only the unmarked finite group \(W\); no chosen \(z\), marked quotient, or external orientation.
- **Functoriality:** the radical line determines \(K\); \(T=W^{ab}[p^s]\) is characteristic; transfer is natural.
- **Gauge:** the generator of \(T\) is only defined up to a unit, harmless for the zero/nonzero predicate.
- **Orientation bridge:** none is inserted; the candidate is a finite-group invariant.
- **q-blindness:** the definition uses only \(W\), its cup product, \(W^{ab}\), and transfer.
- **Separation:** the \(a=s\) side is reduced to a single critical norm/Jacobson class; the \(a=\infty\) side vanishes after the same normalization.
- **Novelty:** this is not the closed scalar/coinvariant route; it uses the cyclic action on \(K^{ab}\).
- **Stop condition:** the only remaining load-bearing issue is the effect of the finite-window truncation relations on the integral Schreier class.

## New reduction

Let \(A_i\) denote the conjugate Schreier generators for \(x_1\), \(U=z^p\), and \(\sigma(A_i)=A_{i+1}\). The relation coming from
\[
z^{p^s}=x_1^{p^s}[x_1,x_2]\cdots
\]
gives in the abelianized index-\(p\) kernel
\[
p^{s-1}U-p^sA_i=0\qquad(0\le i<p).
\]
Ignoring the truncation relations for the moment, put
\[
L_s=\mathbb Z U\oplus\bigoplus_{i=0}^{p-1}\mathbb Z A_i\,
/\langle p^{s-1}U-p^sA_i\rangle.
\]
Then
\[
\delta^{p-1}A_0=(\sigma-1)^{p-1}A_0
=\sum_{j=0}^{p-1}(-1)^{p-1-j}\binom{p-1}{j}A_j.
\]
The class has exponent exactly \(p^s\) in \(L_s\): after quotienting by \(U=0\), the relations become \(p^sA_i=0\), so the image is the nonzero vector
\[
\bigl((-1)^{p-1-j}\binom{p-1}{j}\bigr)_{j=0}^{p-1}
\in (\mathbb Z/p^s)^p,
\]
whose first and last coefficients are units. Hence
\[
\operatorname{ord}_{L_s}(\delta^{p-1}A_0)=p^s,
\qquad
p^{s-1}\delta^{p-1}A_0\ne0.
\]
Therefore the desired transfer defect follows once the actual truncation relations do not alter this class modulo the order-\(p\) witness.

## Exact remaining lemma

It is enough to prove the following integral filtration statement for the index-\(p\) kernel \(K\):
\[
\operatorname{im}\bigl(D_{p^s+1}(F)\cap K\to K^{ab}\bigr)
\subseteq p^s K^{ab}.
\tag{TF_s}
\]
Indeed, the standard index-\(p\) Zassenhaus comparison reduces the source to
\[
D_{p^s+1}(F)\cap K\subseteq D_{p^{s-1}+1}(K),
\]
and every element of \(D_{p^{s-1}+1}(K)\) maps into \(p^sK^{ab}\) by the defining Zassenhaus product description: all commutator factors vanish in \(K^{ab}\), while the first possible pure-power exponent at filtration index \(p^{s-1}+1\) is \(p^s\).

Thus (TF_s), once written as a self-contained lemma with its subgroup-comparison input explicitly cited/proved, prevents the truncation relations from killing the order-\(p\) class
\[
p^{s-1}\delta^{p-1}A_0.
\]

## Consequence if (TF_s) is certified

The intrinsic transfer predicate
\[
\varepsilon(W):\quad p^{s-1}V(T)\ne0\in K^{ab}
\]
is true for \(a=s\) and false for \(a=\infty\). Hence
\[
W_{p^s+1}(G_{s,s})\not\cong W_{p^s+1}(G_{s,\infty})
\]
for every odd \(p\) and \(s\ge2\) in the declared stress-family scope.

Combined with lower-window blindness, this closes the exact unmarked threshold at \(p^s+1\) for the full stress-family parameter range \(1\le a\le s\) (with \(a=s\) handled by this boundary lemma).

## Classification

- model Schreier lattice order computation: **PASS / LOCAL**;
- reduction of the general boundary to (TF_s): **PASS / LOCAL**;
- (TF_s) itself: **OPEN / LOAD-BEARING**;
- all-s transfer-defect separation: **OPEN / LOAD-BEARING**;
- Paper 4 final freeze: blocked only by certification of (TF_s), plus independent verification and record synchronization.


## 2026-10-04 — Literature/direct-proof review correction

The missing bridge was re-tested by two routes.

### Jennings route
Jennings recursion at \(n=p^s+1\) gives a \(p\)-power contribution from \(D_{p^{s-1}+1}(F)\), but an element of its product can lie in \(K\) even when the underlying factor does not. Hence recursion alone does not imply \((SC_s)\).

### Shalev route
Shalev Proposition 1.2 was checked as a filtration identity for a single group. On the evidence currently verified it does **not** state the index-\(p\) subgroup comparison needed here. It must therefore not be cited as if it proves \((SC_s)\).

### Counterexamples to stronger shortcuts
The abelian example \(F=\mathbf Z, K=p\mathbf Z\) proves that \(I_F^n\cap\mathbf F_p[K]=I_K^n\) and \(D_n(F)\cap K\subseteq D_n(K)\) are invalid in general. These failures do not refute the degree-loss comparison \((SC_s)\), but they eliminate the previous augmentation-ideal shortcut.

### Current exact status
\[
(SC_s):\quad D_{p^s+1}(F)\cap K\subseteq D_{p^{s-1}+1}(K)
\]
remains **OPEN / LOAD-BEARING**. Consequently \((TF_s)\) remains **OPEN / LOAD-BEARING**. The model Schreier order computation and the \((3,2)\) local transfer witness remain PASS / LOCAL.

The all-s conclusion is therefore only **CONDITIONAL** on certifying \((SC_s)\) or directly proving \((TF_s)\). No all-s boundary closure is claimed.


---

# SOURCE: research/PAPER4_DIRECTION2_COHOMOLOGY_BLINDNESS_CLOSURE_2026-10-04.md

<!-- blob-sha: b1ffc48922062927c288ec1b5701d1dfddb3a102 -->

# PAPER 4 — DIRECTION 2: MOD-p COHOMOLOGY BLINDNESS — CLOSURE AUDIT — 2026-10-04

## Target

Close Direction 2 at the strongest justified level:

> For the declared odd-p stress family
> \[
> G_{s,a}=\langle z,x_1,\ldots,x_d\mid
> z^{p^s}=x_1^{p^a}[x_1,x_2][x_3,x_4]\cdots[x_{d-1},x_d]\rangle,
> \]
> with \(p\) odd, \(s\ge1\), and finite \(a\ge1\), together with the \(a=\infty\) case in which the \(x_1^{p^a}\) term is absent, the ordinary mod-p cohomology algebra \(H^\bullet(G_{s,a},\mathbf F_p)\) is independent of \(s\) and \(a\) within this declared family.

This is a blindness theorem for the ordinary graded cohomology ring. It is not a claim that the groups, finite windows, higher operations, or filtered extension data are isomorphic.

## 1. Definition / scope audit

Write the defining relator in the free pro-p group as
\[
r_{s,a}=z^{p^s}x_1^{-p^a}
([x_1,x_2][x_3,x_4]\cdots[x_{d-1},x_d])^{-1}
\]
for finite \(a\), with the \(x_1^{-p^a}\) factor omitted for \(a=\infty\).

For odd \(p\),
\[
z^{p^s}\in F^p\subseteq F_{(3)},\qquad
x_1^{p^a}\in F^p\subseteq F_{(3)}
\]
for every \(s,a\ge1\). Hence
\[
r_{s,a}\equiv
[x_1,x_2][x_3,x_4]\cdots[x_{d-1},x_d]
\pmod{F_{(3)}}
\]
up to sign/unit convention.

Thus the degree-2 Zassenhaus initial relation is independent of both \(s\) and \(a\).

Classification: PASS / CLOSED.

## 2. Literature theorem controlling the whole cohomology ring

Quadrelli, arXiv:2011.03233v3, Proposition 2.1 states that for a finitely generated one-relator pro-p group
\[
G=\langle x_1,\ldots,x_d\mid r\rangle
\]
whose relator satisfies
\[
r\equiv [x_1,x_2][x_3,x_4]\cdots[x_{n-1},x_n]
\pmod{G_{(3)}},
\]
the mod-p cohomology algebra is quadratic; the indicated degree-one cup products give the generator of \(H^2\), all other basis products vanish (apart from graded-commutativity), and
\[
H^k(G,\mathbf F_p)=0\quad(k\ge3).
\]

This theorem applies directly because the only \(s,a\)-dependent terms in \(r_{s,a}\) lie in \(F_{(3)}\).

Independent literature control is therefore stronger than a mere associated-graded calculation: it determines the entire ordinary cohomology ring.

## 3. Explicit cohomology algebra

Let
\[
V=H^1(G_{s,a},\mathbf F_p)
=\langle\chi_z,\chi_1,\ldots,\chi_d\rangle.
\]
Then
\[
H^0\cong\mathbf F_p,\qquad
H^1\cong V,\qquad
H^2\cong\mathbf F_p\omega,\qquad
H^k=0\ (k\ge3).
\]

With the dual basis to \(z,x_1,\ldots,x_d\),
\[
\chi_1\cup\chi_2
=\chi_3\cup\chi_4
=\cdots
=\chi_{d-1}\cup\chi_d
=\omega
\]
up to the global sign/unit convention for the relator, while
\[
\chi_z\cup\chi_i=0,\qquad
\chi_i\cup\chi_j=0
\]
for all other unordered pairs not appearing in the displayed commutators. Since \(p\) is odd, graded commutativity supplies the reverse-order signs.

Consequently the algebra is determined solely by the quadratic commutator form and contains no \(s\)- or \(a\)-parameter.

Classification: PASS / CLOSED.

## 4. Why this closes the "all H*" question

There is no hidden higher ordinary cohomology degree in which \(s\) or \(a\) could reappear:
\[
H^k(G_{s,a},\mathbf F_p)=0\quad(k\ge3).
\]
Therefore the full graded ring
\[
H^\bullet(G_{s,a},\mathbf F_p)
\]
is already exhausted by \(H^0,H^1,H^2\) and the degree-one cup product.

Hence, for every two allowed parameter choices,
\[
\boxed{
H^\bullet(G_{s,a},\mathbf F_p)
\cong
H^\bullet(G_{t,b},\mathbf F_p)
}
\]
as graded \(\mathbf F_p\)-algebras.

For the fixed marked presentation there is an evident parameter-independent identification sending the degree-one dual basis to the corresponding degree-one dual basis and the common degree-two generator to the common generator. As an abstract graded algebra, the conclusion is even presentation-independent.

Classification: PASS / CLOSED.

## 5. What is NOT proved by this closure

This closure does **not** imply any of the following:

1. \(G_{s,a}\cong G_{t,b}\).
2. \(W_n(G_{s,a})\cong W_n(G_{t,b})\) for all \(n\).
3. The critical finite windows at \(n=p^s+1\) are isomorphic.
4. Higher Bockstein, Massey, \(A_\infty\), integral Magnus, relation-module, or filtered extension data are equal.
5. The \(a=s\) and \(a=\infty\) groups/windows are indistinguishable by every cohomological operation.

In particular, ordinary \(H^\bullet(-,\mathbf F_p)\) is now certified as a **blind invariant**, not as a proof of group-level non-rigidity.

## 6. Independent verification / adversarial checks

### Check A — filtration degree

For odd \(p\), \(p^m\ge3\) for every \(m\ge1\), so every power term \(z^{p^s}\) and \(x_1^{p^a}\) lies in the third Zassenhaus term. Thus no parameter-dependent term survives in \(D_2/D_3\).

PASS.

### Check B — one-relator hypothesis

The family has one defining relator, and the relator lies in the Frattini subgroup because its lowest term is a commutator. Hence the presentation is minimal and \(H^2\) has dimension one.

PASS.

### Check C — higher ordinary cohomology

The cited Proposition 2.1 gives \(H^k=0\) for \(k\ge3\) under precisely the required quadratic commutator congruence.

PASS.

### Check D — no accidental use of \(q=p^a\)

The cohomology object and its identification use only the degree-two initial commutator form. No \(q\)-dependent coefficient is inserted.

PASS.

### Check E — boundary \(a=s\) versus \(a=\infty\)

Both satisfy exactly the same congruence modulo \(F_{(3)}\), so the same conclusion applies:
\[
H^\bullet(G_{s,s},\mathbf F_p)
\cong
H^\bullet(G_{s,\infty},\mathbf F_p).
\]

PASS.

## 7. Literature boundary

The cited result is stronger than the earlier internal statement "the associated graded is s-blind": it gives the full ordinary mod-p cohomology algebra and its vanishing above degree two for this one-relator quadratic-commutator family.

This also corrects the methodological wording that had suggested a separate mildness argument was required to close Direction 2. Mildness is compatible with the conclusion, and Gärtner's one-relator/mildness results provide independent background, but Proposition 2.1 already closes the exact cohomology-ring claim directly.

## 8. Final classification

\[
\boxed{\text{DIRECTION 2: PASS / CLOSED}}
\]

Precise theorem-level content:

> For odd \(p\), within the declared stress family with \(s\ge1\), finite \(a\ge1\), and \(a=\infty\), the ordinary mod-p cohomology algebra \(H^\bullet(G_{s,a},\mathbf F_p)\) is independent of \(s\) and \(a\). The common algebra is concentrated in degrees \(0,1,2\), with \(H^2\) generated by the common quadratic commutator cup class.

The route is closed. No further computation of ordinary \(H^\bullet(-,\mathbf F_p)\) is authorized as a route to the remaining \(a=s\) versus \(a=\infty\) finite-window separation.

## 9. Consequence for Paper 4

The remaining boundary is now sharply isolated:
\[
\text{ordinary }H^\bullet(-,\mathbf F_p)
\quad\text{blind}
\qquad\Longrightarrow\qquad
\text{look beyond ordinary cohomology}.
\]

The load-bearing problem, if pursued, must retain information not present in the ordinary graded cohomology ring: filtered extension/deformation data, integral p-adic relation data, or another genuinely higher structure. The closed Direction 2 route must not be reopened merely by recomputing the same \(H^1/H^2/H^\ast\) invariants.


---

# SOURCE: research/PAPER4_FILTERED_EXTENSION_EXTRACTION_NO_GO_2026-10-04.md

<!-- blob-sha: b07c21e02e737c76ac19af99c6a8102085cb8d09 -->

# PAPER4_FILTERED_EXTENSION_EXTRACTION_NO_GO_2026-10-04.md

## Target

Test whether the intrinsic one-step Zassenhaus extension
\[
1\to K_n:=D_n(G)/D_{n+1}(G)\to W_{n+1}(G)\to W_n(G)\to1
\]
provides a new canonical defect that extracts the hidden \(p^s\)-power relation, without introducing a marked orientation/character.

The active boundary is the unresolved critical case \(n=p^s\), especially the \(a=s\) versus \(a=\infty\) stress comparison.

## Pre-check

### Object — PASS

The extension above is canonical and q-blind: it is determined by the Zassenhaus filtration of the finite window and contains the kernel, its filtration degree, conjugation action, and the extension itself.

Since \([D_n,G]\subseteq D_{n+1}\), the kernel \(K_n\) is central.

### Input — PASS

Allowed input is only the filtered finite extension. The hidden \(q=p^a\), a chosen character, and a chosen presentation are not inserted into the object.

### Functoriality — PASS

An isomorphism of filtered finite windows induces an isomorphism of the corresponding one-step extensions. Thus the extension is an intrinsic object over the finite-window isomorphism class.

### Gauge — PASS, with a decisive boundary

Choose a section \(s:W_n\to W_{n+1}\). Because the kernel is central, the section defines a 2-cocycle
\[
c_s(g,h)=s(g)s(h)s(gh)^{-1}\in K_n.
\]
Replacing \(s\) by another section changes \(c_s\) by a coboundary. Hence any proposed p-power/commutator defect computed from a particular lift or section is not canonical unless it descends through this gauge action.

This is standard central-extension theory. The intrinsic datum is the extension-equivalence class \([c_s]\in H^2(W_n,K_n)\), not an individual lift formula. The Zassenhaus setting additionally identifies the graded layer with restricted-Lie p-power/commutator data, but that does not remove the section gauge.

### Orientation bridge — FAIL / CLOSED for a scalar defect

The one-step extension has no distinguished generator, character, or affine direction. A p-power/commutator formula for a selected lift therefore depends on a section/lift choice unless an additional canonical orientation bridge is supplied.

The previously explored marked \(E_\psi\) construction supplies such an orientation only in the marked presentation category; the present object intentionally forgets that marking. No intrinsic map from the abstract extension to a distinguished \(\psi\) has been established.

Therefore the proposed route
\[
\text{unmarked extension}\to\text{distinguished lift defect}
\]
fails the mandatory orientation/gauge test.

### q-blindness — PASS

The extension itself contains no inserted \(q=p^a\).

### Separation — NOT A NEW TESTABLE INVARIANT

After quotienting section/lift gauge, the remaining canonical object is the extension-equivalence class itself. But this is precisely the isomorphism class of the structured map
\[
W_{n+1}\twoheadrightarrow W_n.
\]
Therefore asking whether this full package separates two cases is equivalent to the original finite-window extension-isomorphism problem; it is not a lower-complexity extraction theorem.

In particular, the filtered-extension package does not produce a new scalar/carrier automatically. Any genuine separation would require classifying the extension class (or an explicitly declared quotient of it), which is the same structural problem in different language.

This does **not** prove that the two critical windows are isomorphic. It proves that the proposed 'extension extraction' strategy does not reduce that question unless an additional intrinsic quotient/factorization theorem is supplied.

## Independent structural verification

The central-extension interpretation agrees with standard extension theory: central extensions with fixed action are classified by \(H^2\), with changes of section changing cocycles by coboundaries. The Zassenhaus filtration also has canonical restricted-Lie p-power and commutator operations on \(D_n/D_{n+1}\). These facts confirm the gauge analysis, but they do not provide the missing orientation bridge.

## Result

**Filtered-extension extraction as a new canonical defect: FAIL / CLOSED.**

More precisely:

- canonical one-step filtered extension: **PASS / CLOSED**;
- section/lift gauge analysis: **PASS / CLOSED**;
- intrinsic scalar/orientation defect from the unmarked extension alone: **FAIL / CLOSED**;
- full extension-equivalence class as a separator: **OPEN**, but it is exactly the original structured finite-window isomorphism problem, not a new extraction method;
- ordinary mod-p cohomology route: **PASS / CLOSED and STOPPED**;
- arbitrary degree-only theorem: **FAIL / CLOSED**.

## Stop decision

Do not return to carrier hunting, new \(E_\psi\) variants, ordinary cohomology, or ad hoc lift decorations.

The research branch has reached its legitimate boundary. Any further progress would require a genuinely new theorem proving a canonical quotient/factorization of the full extension-equivalence class, not another candidate invariant search.

The bounded research objective is therefore closed at the method level: **the existing one-step filtered extension is the correct next structural layer, but it does not by itself yield a new intrinsic compression/extraction map.**


---

# SOURCE: research/PAPER4_ROOT_VISIBILITY_NONRIGIDITY_AUDIT_2026-10-04.md

<!-- blob-sha: cd9dbe5eb9b9f515a811569a3eda4c2457c9742a -->

# PAPER 4 — Root-visibility generalization / non-rigidity audit — 2026-10-04

## Executive conclusion

The two proposed upgrades do not have the same status.

1. **General root-visibility theorem for arbitrary r with Zassenhaus order >=2: OPEN; the hypothesis is insufficient for the full-relation claim.**
   Counterexample:
   G=<z,x,y | z^3=[x,y]^3>.
   Here r=[x,y]^3 lies in D_6(F), while the critical window is W_4. Since D_6(F) is contained in D_4(F), the relation reduces in W_4 to z^3=1. Thus the full-relation critical visibility claim is not established. Merely assuming ord_Z(r)>=2 is insufficient to ensure that r survives at the critical layer. Importantly, this example does not show that the root term z^3 itself is invisible: z^3 lies in D_3, so it can be visible in W_4.

2. **Stress-family non-rigidity theorem: PASS / LOCAL, with a substantially stronger proof package than previously recorded.**
   For fixed odd p, d, and a, s>a,
   G_{s,a}=<z,x_1,...,x_d | z^{p^s}=x_1^{p^a}[x_1,x_2]...[x_{d-1},x_d]>
   has:
   - G_{s,a}^{ab} = Z_p^d + Z/p^a, independent of s;
   - the same quadratic Zassenhaus initial form rho=[X_1,X_2]+...+[X_{d-1},X_d], hence the same mild quadratic package and the same F_p-cohomology ring;
   - the same associated graded restricted Lie algebra / graded group-algebra package;
   - identical windows W_n(G_{s,a}) for all t>=s whenever n<=p^s;
   - at its own critical window n_s=p^s+1, abelianization Z/p^a + (Z/p^{s+1})^d.

## Generalization attack

The universal presentation identity is
W_n(G_{s,r}) = F/(D_n(F), z^{p^s} r^{-1}).
Hence if n<=p^s,
W_n(G_{s,r}) = F/(D_n(F),r),
independently of s. This is a genuine universal delayed-visibility lemma.

At n=p^s+1, visibility is not automatic: it depends on whether r survives at that level and on a nontrivial filtered extension defect. The counterexample above shows that ord_Z(r)>=2 does not guarantee survival.

The viable theorem shape is therefore not arbitrary r. A candidate replacement is a root-visibility theorem under a specified critical-survival hypothesis, where the hypothesis must be intrinsic and non-tautological.

## Non-rigidity proof package

### A. Abelianization

Abelianizing gives
G_{s,a}^{ab} = Z_p^{d+1}/<(p^s,-p^a,0,...,0)>
= Z_p^d + Z/p^a.
At n=p^s+1,
W_n^{ab} = Z/p^a + (Z/p^{s+1})^d.
The SNF script independently verifies representative cases.

### B. Cohomology

The defining relator has Zassenhaus invariant 2 for odd p, since the quadratic commutator part is nonzero and all p^a,p^s power terms have degree at least p>=3.

For a one-relator pro-p group with Zassenhaus invariant prime to p, Gartner's Corollary 5.10 gives mildness. Mild groups have cd=2, and in the quadratic one-relator case the F_p-cohomology algebra is controlled by the quadratic initial relation. The initial relation is the same rho for every s. Therefore the full F_p-cohomology ring is s-independent in this family.

### C. Associated graded

By mildness, the graded group algebra is the quotient by the ideal generated by rho. Since rho is independent of s, the associated graded algebra and restricted-Lie package are s-independent.

### D. Delayed finite-window identity

For t>=s and n<=p^s, both z^{p^s} and z^{p^t} are in D_n(F). Therefore
W_n(G_{s,a}) is isomorphic to W_n(G_{t,a})
as filtered quotients of the same free group.

### E. Critical-window separation

At n_s=p^s+1,
exp(W_{n_s}(G_{s,a})^{ab}) = p^{s+1}.
Thus the sequence of own-critical windows is pairwise separated by abelianization exponent.

Qualification: this does not prove that W_{p^s+1}(G_{s,a}) is separated from every G_{t,a} at the same numerical window for t>s. That comparison remains OPEN.

## Novelty control

The ingredients themselves are established: Demushkin classification, Zassenhaus initial forms, mildness, quadratic cohomology, and finite quotient abelianization.

The potentially new package is the explicit delayed finite-window visibility theorem for the stress family, combining:
same abelianization + same F_p-cohomology + same gr + same windows through p^s + own-critical-window separation at p^s+1.

This still needs a dedicated literature search before any novelty claim.

## Current classification

- arbitrary-r root-term visibility at p^s+1: **OPEN**;
- full-relation critical visibility from only ord_Z(r)>=2: **OPEN / hypothesis insufficient for proof**;
- universal delayed-window lemma n<=p^s: **PASS / CLOSED**;
- stress-family G^{ab} independence of s: **PASS / CLOSED**;
- stress-family H^*(G,F_p) independence of s: **PASS / LOCAL** pending citation-level lemma packaging;
- stress-family associated graded independence: **PASS / LOCAL** pending the same packaging;
- own-critical-window exponent separation: **PASS / CLOSED**;
- full same-window W_{p^s+1}(G_s) vs W_{p^s+1}(G_t), t>s: **OPEN**;
- broader non-tautological root-visibility theorem: **OPEN**.

## Independent check

Script: research/scripts/paper4_root_visibility_checks_2026-10-04.py
Executed independently with SymPy. Representative SNF cases passed, and the delayed-window filtration inequalities passed.

## Literature control

The relevant literature confirms the mildness/cohomology/graded facts used above. No source located in this audit directly states the exact combined delayed-window package. This is not a novelty certification.

## Next authorized attack

1. Make direction 2 the main Paper 4 branch: formalize the delayed-window/non-rigidity theorem for G_{s,a}, with a precise definition of the coarse infinite invariants.
2. Do not claim the arbitrary-r theorem.
3. For direction 1, do not claim a counterexample to root-term visibility from the z^3=[x,y]^3 example. Instead identify the narrowest non-tautological class where the RHS r survives at the critical layer; first test quadratic relators and identify the exact witness hypothesis.
4. Do not reopen frozen threshold calculations or Paper 5 compression routes.


## 2026-10-04 — SAME-WINDOW SEPARATION ATTACK / NOVELTY CONTROL

The first direct attack on the unresolved comparison
W_{p^s+1}(G_{s,a}) versus W_{p^s+1}(G_{t,a}), t>s,
does not close the problem by abelianization: both windows have the same abstract abelianization type Z/p^a plus d copies of Z/p^{s+1}. The distinction, if present, must therefore be a filtered extension/lift invariant beyond abelianization and beyond the associated graded object.

A concrete candidate is now isolated: the intrinsic cup-radical line L in H^1(W,F_p), together with its p^s-power/extension datum in the critical filtered layer. Conceptually, in the critical source the p^s-power of a lift of the radical direction is tied by the defining relation to the Demushkin quadratic part, whereas for t>s the defining relation is already invisible at the same window and the radical power is an independent lift datum. This is only a **candidate invariant**, not yet a theorem: one must define it functorially from the finite group and prove invariance under changing lifts and under abstract filtered-group isomorphism.

A higher-Bockstein / augmentation-algebra formulation is a promising concrete implementation: the target should be a finite-window operation attached to the radical character whose first nonzero filtered value occurs at p^s+1. No claim of existence or nonvanishing is made yet.

Novelty control was tightened by direct inspection of arXiv:2603.15464v2. That paper studies other Demushkin variations with presentations whose Zassenhaus graded relation is independent of the variation parameter, and proves quadratic/Koszul cohomology and graded-algebra properties while detecting the variation through finer 1-cyclotomic structure. Therefore the present project must not claim novelty for “same cohomology + same graded object” alone. The potentially novel component is the explicit delayed-window identity together with critical finite-window separation/non-rigidity.

Classification:
- same-window separation by abelianization: **FAIL / CLOSED** as a route;
- same-window separation by intrinsic filtered radical-power datum: **OPEN / LOAD-BEARING**;
- higher-Bockstein implementation: **OPEN**;
- novelty of the coarse cohomology/graded package alone: **HISTORICAL / SUPERSEDED as novelty claim**;
- novelty of delayed finite-window visibility + critical-window separation: **OPEN / literature check incomplete**.


---

# SOURCE: research/PAPER4_A_S_TRANSFER_SCHREIER_W10_AUDIT_2026-10-04.md

<!-- blob-sha: 452c27862bfc83d3fad6b6e9978190b43e3092b3 -->

# Paper 4 — corrected intrinsic radical Schreier/transfer calculation at W_10
## 2026-10-04

### Executive correction

The proposed character
\[
\chi(z)=\chi(x)=1,\qquad \chi(y)=0
\]
is **not** the cup-radical character for
\[
G_{2,2}=\langle z,x,y\mid z^9=x^9[x,y]\rangle.
\]
Modulo \(D_3\), the defining relation has initial form \([x,y]\). Hence the cup pairing has \(\langle x^*,y^*\rangle\ne0\) and radical line \(\langle z^*\rangle\). Therefore the intrinsic radical character is
\[
\boxed{\chi(z)=1,\quad\chi(x)=\chi(y)=0.}
\]
The same statement holds for \(W_{10}\), because passing to \(W_{10}\) does not change the degree-2 relation data.

This correction is load-bearing: the Schreier calculation must use \(K=\ker(z^*)\), not the kernel of \(z^*+x^*\).

### Corrected Schreier system

Use transversal \(\{1,z,z^2\}\). Put
\[
u=z^3,
\quad a_0=x,\ a_1=zxz^{-1},\ a_2=z^2xz^{-2},
\quad b_0=y,\ b_1=zyz^{-1},\ b_2=z^2yz^{-2}.
\]
Thus there are seven Schreier generators.

Conjugation \(\sigma=\operatorname{Ad}(z)\) gives in \(K^{ab}\):
\[
\sigma(u)=u,
\qquad
\sigma(a_0)=a_1,\ \sigma(a_1)=a_2,\ \sigma(a_2)=u a_0u^{-1}\equiv a_0,
\]
and similarly
\[
\sigma(b_0)=b_1,\quad \sigma(b_1)=b_2,\quad \sigma(b_2)\equiv b_0.
\]
Therefore, with basis
\[
(u,a_0,a_1,a_2,b_0,b_1,b_2),
\]
the actual mod-3 action is
\[
P=
\begin{pmatrix}
1&0&0&0&0&0&0\\
0&0&0&1&0&0&0\\
0&1&0&0&0&0&0\\
0&0&1&0&0&0&0\\
0&0&0&0&0&0&1\\
0&0&0&0&1&0&0\\
0&0&0&0&0&1&0
\end{pmatrix}.
\]
Hence
\[
(P-I)^2
\]
is zero on \(u\), and on each 3-cycle is the all-ones map. In particular
\[
(\sigma-1)^2[a_0]=[a_0]+[a_1]+[a_2]\ne0
\]
provided these classes survive in \(M\).

### Actual \(M=K^{ab}/3K^{ab}\)

The Reidemeister–Schreier relators coming from
\[
r=z^9x^{-9}[x,y]^{-1}
\]
have zero commutator contribution after abelianization and give, up to an overall sign convention,
\[
3u-9a_0=0,\qquad
3u-9a_1=0,\qquad
3u-9a_2=0.
\]
The three conjugate \([x,y]\)-terms vanish in \(K^{ab}\).

The additional \(D_{10}(F)\)-relations do not impose linear relations in \(K^{ab}/3K^{ab}\). A direct augmentation-ideal check gives the needed comparison: in characteristic 3, three factors of \((z-1)\) collapse to \(z^3-1\in I(K)\), while \((x-1),(y-1)\in I(K)\); hence a degree-10 augmentation term whose group element lies in K has K-augmentation degree at least \(\lceil10/3\rceil=4\). Therefore \(D_{10}(F)\cap K\subseteq D_4(K)\subseteq D_2(K)=K^3[K,K]\), so the truncation relations vanish in the mod-3 abelianization. This is the only filtration-comparison input needed here.

Consequently
\[
M\cong \mathbf F_3^7
\]
with the displayed basis. Equivalently, the Smith form of the three abelianization relations is
\[
\operatorname{SNF}=\operatorname{diag}(3,9,9),
\]
so after tensoring with \(\mathbf F_3\) no generator class is killed.

### Transfer/Jacobson consequence

For the corrected intrinsic kernel, the short torsion class in \(W^{ab}\) is represented by
\[
\tau_s=zx^{-1}
\]
in the \(a=s=2\) case, while \(\tau_\infty=z\) on the \(a=\infty\) side. Both map nontrivially to \(W/K\cong C_3\), as required for the transfer computation.

The critical norm expansion is
\[
N_\sigma=3+3(\sigma-1)+(\sigma-1)^2
\]
over \(\mathbf F_3\) at the level of the last filtered term, so the new contribution is the \((\sigma-1)^2\)-term. The corrected Schreier calculation gives
\[
(\sigma-1)^2[a_0]=a_0+a_1+a_2\ne0
\quad\text{in }M.
\]

More strongly, the \(a=s\) Schreier abelianization has relations
\[
3u=9a_i\quad(i=0,1,2),
\]
and no further relation from \(D_{10}(F)\) survives in \(K^{ab}\). Therefore
\[
3(a_0+a_1+a_2)\ne0
\]
in \(K^{ab}\): if it vanished, the vector \(3(a_0+a_1+a_2)\) would lie in the lattice generated by \((3u-9a_i)_{i=0}^2\), which it does not. This is the actual integral lift needed for the \(s=2\) transfer defect, not merely a mod-3 shadow.

Thus the critical transfer/Jacobson witness survives:
\[
\boxed{3(\sigma-1)^2[a_0]\ne0\ \text{in }K^{ab}.}
\]

### Independent algebra check

The calculation is independently encoded in `research/scripts/paper4_w10_schreier_transfer_check_2026-10-04.py`; the script checks the Schreier action matrix, Smith form, and integral lattice nonvanishing.

For the relation matrix
\[
A=
\begin{pmatrix}
3&-9&0&0&0&0&0\\
3&0&-9&0&0&0&0\\
3&0&0&-9&0&0&0
\end{pmatrix},
\]
the Smith normal form is \(\operatorname{diag}(3,9,9)\), with four free factors. The vector
\[
3(0,1,1,1,0,0,0)
\]
is not in the row lattice of \(A\). This independently verifies the nonzero integral class used above.

### Classification

- intrinsic cup-radical character correction: **PASS / CLOSED**;
- corrected Schreier presentation and 7-generator action: **PASS / LOCAL**;
- \(M=K^{ab}/3K^{ab}\cong\mathbf F_3^7\): **PASS / LOCAL**, subject to the stated standard Zassenhaus subgroup-comparison lemma;
- \((\sigma-1)^2[a_0]\ne0\) in actual \(M\): **PASS / LOCAL**;
- integral nonvanishing \(3(\sigma-1)^2[a_0]\ne0\) in actual \(K^{ab}\): **PASS / LOCAL** under the same filtration-comparison input;
- \(a=s\) transfer-defect separator at \((p,s)=(3,2)\): **PASS / LOCAL**, not yet promoted to a general \(s\ge2\) theorem;
- general \(a=s\) vs. \(a=\infty\) separation for all \(s\ge2\): **OPEN**.

### Logical boundary

This calculation does **not** justify the original \(\chi(z)=\chi(x)=1\) claim; that branch is rejected as non-intrinsic. It also does not by itself prove the all-\(s\) transfer formula. The result is a certified base-case witness for the exact remaining boundary, subject to the standard subgroup-filtration comparison lemma being written out in the final proof.
