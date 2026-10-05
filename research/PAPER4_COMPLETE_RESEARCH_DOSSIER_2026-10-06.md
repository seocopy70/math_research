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


---

# SOURCE: research/PAPER4_REPRESENTATION_LAYER_GATE_RESULT_2026-10-04.md

<!-- blob-sha: eb34b150fe7d7178288e4a8bf2ba6ad1d23bfb88 -->

# PAPER4_REPRESENTATION_LAYER_GATE_RESULT_2026-10-04.md

## Scope

This audit executes the pre-registered bounded representation-layer feasibility gate. It does not reopen arbitrary candidate hunting, ordinary cohomology, the failed arbitrary-degree theorem, or the marked single-character E_psi theorem.

Fixed object:
\[
W_{p^s+2}\to W_{p^s+1}\to W_{p^s},
\]
together with the pre-registered adjacent-layer extension, module, restricted p-power/commutator, and compatibility data.

## Gate execution

### 1. Object — PASS / CLOSED

The two-step filtered tower is intrinsic and q-blind. Its morphisms are filtered isomorphisms. The canonical central extension classes and restricted operations are determined by the finite filtered groups.

### 2. Input — PASS / CLOSED

No hidden q=p^a, distinguished character, presentation-dependent generator, or chosen section is inserted.

### 3. Functoriality — PASS / CLOSED

A filtered isomorphism of tower objects transports extension classes, module structures, restricted operations, and adjacent-layer compatibility. Hence any construction made solely from the pre-registered data is functorial.

### 4. Gauge — PASS / CLOSED

Section/lift choices act by the usual coboundary equivalence. The two-step tower therefore supports an affine representation *groupoid* only after quotienting the auxiliary choices. A chosen scalar evaluation is not intrinsic.

### 5. Orientation bridge — FAIL / CLOSED for a distinguished coordinate

The one-character bridge remains impossible by the established symmetry argument. The two-step tower does not canonically select a representative psi. Passing from a representative to its full orbit/groupoid removes the coordinate choice, but does not itself produce a scalar or canonical affine coordinate.

### 6. Orbit/groupoid construction — PASS / CLOSED as a reformulation, not as compression

For a fixed admissible affine target, the groupoid of filtered representations/crossed-derivation data can be defined functorially from the tower. This resolves the representability question at the level needed for a legitimate formulation.

However, this groupoid is a functor of the *entire declared tower*. Without a further factorization theorem, it is equivalent in information content to a structured representation of the original finite-window isomorphism problem. It is therefore not yet a coarser intrinsic carrier.

### 7. Separation — OPEN / LOAD-BEARING

The orbit/groupoid formulation does not, by itself, prove that the a=s and a=infinity critical windows have different groupoids. Conversely, no theorem currently proves that the groupoids coincide. Establishing either statement requires an actual comparison theorem for the tower objects.

Thus the remaining issue is a **detector failure**, not an information-failure theorem.

## Independent structural check

The supplied literature on higher cohomological structure confirms the general methodological point: ordinary cohomology can be blind while a higher canonical obstruction class detects extra structure. This does not transfer automatically to the present finite-window problem, because a finite-window factorization through such a higher operation has not been proved. Therefore no literature result is promoted as a solution here.

## Final classification

- one-step scalar defect: **FAIL / CLOSED**;
- distinguished single-psi orientation bridge: **FAIL / CLOSED**;
- two-step affine representation groupoid: **PASS / CLOSED as a canonical reformulation**;
- compression of that groupoid to a smaller intrinsic carrier: **OPEN**;
- exact unmarked same-window separation a=s versus a=infinity: **OPEN / LOAD-BEARING**;
- arbitrary candidate hunting: **STOPPED**.

## Consequence

The pre-registered representation-layer branch has reached its legitimate boundary. Further progress requires a genuinely new factorization theorem showing that the affine representation groupoid, or the full tower extension structure, descends to a strictly smaller intrinsic invariant that separates the critical cases.

No additional carrier, character, lift decoration, or ad hoc representation is authorized merely to continue the search.


---

# SOURCE: research/PAPER4_GENERAL_SC_ARBITRARY_PROP_A1_CLOSURE_2026-10-05.md

<!-- blob-sha: e9581628b1e582836b475a62c590df87b2cfe4ed -->

# Paper 4 — A1 arbitrary pro-p SC closure audit — 2026-10-05

## Claim

For every pro-p group G, every open subgroup K <= G with [G:K]=p^s,
\[
D_n(G)\cap K\subseteq D_{\lceil n/p^s\rceil}(K).
\tag{A1}
\]

Here D_n denotes the p-Zassenhaus filtration.

## Verdict

**PASS / CLOSED.**

The earlier augmentation-ideal equality route was false and remains rejected. The corrected proof uses a weighted normal-form filtration on the completed group algebra and does not require G to be free.

## Index-p proof

Let [G:K]=p and choose a in G with G/K=<aK>. Put
\[
A=\mathbf F_p[[K]],\qquad B=\mathbf F_p[[G]],\qquad J=I_K,\qquad t=a-1.
\]
As a left A-module,
\[
B=\bigoplus_{r=0}^{p-1}At^r.
\]
Because a^p in K and char(F_p)=p,
\[
t^p=a^p-1\in J.
\]
Normality of K gives aJa^{-1}=J.

The crucial point is NOT the false identity
\[
I_G^n=\sum_j J^{n-j}t^jB.
\]
Instead define, for m>=1,
\[
E_m=
\bigoplus_{r=0}^{p-1}
J^{\max(0,\lceil(m-r)/p\rceil)}t^r.
\tag{E_m}
\]
For (m\le r) we use the convention (J^0=A); equivalently, the exponent in (E_m) is always interpreted as (max(0,\lceil(m-r)/p\rceil)). Thus (E_m) is well-defined for all (m\ge1).

The normal-form multiplication rules imply
\[
E_mE_\ell\subseteq E_{m+\ell}.
\tag{*}
\]
More explicitly, define the weight of a normal-form monomial (c t^r), with (c\in J^q) and (0\le r<p), to be (pq+r). If \(\sigma(c)=aca^{-1}\), then
\[
tc=\sigma(c)t+(\sigma(c)-c),
\]
and, because \(\sigma(J^q)=J^q\), both coefficients on the right lie in (J^q). Iterating gives (t^rJ^q\subseteqsum_{j=0}^rJ^qt^j). On multiplying by a further (t^s), every resulting (t^{j+s}) is written as
\[
t^{j+s}=(t^p)^u t^v,
\qquad j+s=up+v,quad0\le v<p,
\]
and (t^p=a^p-1\in J). Thus the weight (pq+r) is not decreased by multiplication. Hence products of terms of weights at least (m) and \(\ell\) have weight at least (m+\ell), proving (*).

Since
\[
I_G=JB+tB\subseteq E_1,
\]
multiplicativity gives
\[
I_G^n\subseteq E_n
=
\bigoplus_{r=0}^{p-1}
J^{\max(0,\lceil(n-r)/p\rceil)}t^r.
\tag{NF}
\]
The decomposition is direct. Hence
\[
I_G^n\cap A\subseteq J^{\lceil n/p\rceil}.
\tag{AI}
\]
Using the dimension-subgroup identity
\[
D_n(H)=H\cap(1+I_H^n)
\]
for pro-p groups, (AI) gives
\[
D_n(G)\cap K\subseteq D_{\lceil n/p\rceil}(K).
\tag{SC}
\]

This proof explicitly handles the previously missed terms t^rBt: they are normalized inside the direct-sum E_m decomposition rather than discarded.

## Index-p^s extension

Since (G/K) is a finite (p)-group, it admits a composition series with successive quotients of order (p). Pulling this series back to (G) gives a subnormal chain
\[
G=K_0>K_1>\cdots>K_s=K,
\qquad [K_{i-1}:K_i]=p.
\]
For [G:K]=p^s choose this chain
\[
G=K_0>K_1>\cdots>K_s=K,
\qquad [K_{i-1}:K_i]=p.
\]
Applying (SC) successively gives
\[
D_n(G)\cap K\subseteq D_{\lceil n/p^s\rceil}(K),
\tag{SC_s}
\]
because
\[
\left\lceil\frac{\lceil m/p\rceil}{p}\right\rceil
=
\left\lceil\frac m{p^2}\right\rceil
\]
and hence the ceiling operation composes exactly. The elementary identity follows by writing (m=pq+r), (0\le r<p), and checking the two cases (r=0) and (r>0).

## Consequences

1. **A1 is arbitrary-pro-p, not free-pro-p.** No freeness assumption enters the group-algebra normal-form argument.
2. The previously certified free-pro-p SC/SC_s results remain valid.
3. At the Paper-4 critical index n=p^s+1,
\[
D_{p^s+1}(G)\cap K
\subseteq
D_{p^{s-1}+1}(K),
\]
which supplies the subgroup-depth bound used in the transfer truncation argument.
4. The separate free-pro-p sharpness witness remains the correct sharpness statement for SC_s. A1 does not enlarge that sharpness claim to arbitrary pro-p groups.
5. The old augmentation-ideal equality, the Heisenberg counterexample, and the old Lemma-2/Lemma-3 route remain **FAIL / CLOSED / SUPERSEDED**. They are not part of the proof.

## Audit status

- A1 index-p arbitrary pro-p: **PASS / CLOSED**.
- A1 index-p^s arbitrary pro-p: **PASS / CLOSED**.
- Pointwise sharpness for every n: **OPEN / not needed**.
- Uniform sharpness in the free-pro-p witness family: **PASS / CLOSED**.
- Paper-4 downstream transfer obstruction and exact critical-window theorem: unchanged and remain PASS / CLOSED in the declared stress-family scope.

## Publication wording

Do not claim a new foundational theorem about augmentation ideals. The defensible statement is:

> We prove the precise index-p Zassenhaus subgroup-depth comparison needed for the finite-window argument for arbitrary pro-p groups, by a weighted normal-form filtration of the completed group algebra; iterating along an index-p^s chain yields the corresponding p^s comparison. The result is used as filtration infrastructure for the intrinsic transfer obstruction and sharp finite-window separation.


## Sharpness scope (explicit)

The statement proved here is **uniform optimality of the factor (p^s) in the free-pro-(p) class**, not pointwise optimality for every (n) and not optimality for every arbitrary pro-(p) group.

For the one-step case, (F=\langle a,b\rangle) and the standard index-(p) kernel give witnesses (g_m=a^{p^m}) with
[
\nu_F(g_m)=p^m,qquad \nu_K(g_m)=p^{m-1}
=left\lceil\frac{p^m}{p}\right\rceil.
]
For index (p^s), take the corresponding kernel (K_s) and
[
g_{m,s}=a^{p^{m+s-1}},
]
so
[
\nu_F(g_{m,s})=p^{m+s-1},qquad
\nu_{K_s}(g_{m,s})=p^{m-1}
=left\lceil\frac{p^{m+s-1}}{p^s}\right\rceil.
]
Letting (m) vary gives arbitrarily large witness degrees and proves that the factor (p^s) cannot be uniformly improved in the free-pro-(p) class.

No claim is made that equality occurs for every integer (n), and no claim is made that the bound is sharp for every arbitrary pro-(p) group. Such pointwise or groupwise sharpness is outside the Paper-4 theorem and is not a gate for closure.


---

# SOURCE: research/PAPER4_SC_SHARPNESS_AND_INDEX_PS_AUDIT_2026-10-05.md

<!-- blob-sha: 9a83975dda555bfe6640f03aa9df2ef1b4c21da7 -->

# Paper 4 — SC Sharpness and Index-p^s Strengthening Audit — 2026-10-05

## Gate

**Target:** strengthen the certified subgroup-depth comparison
\[
D_n(F)\cap K\subseteq D_{\lceil n/p^s\rceil}(K),\qquad [F:K]=p^s,
\]
by (i) proving the factor \(p^s\) is uniformly sharp and (ii) isolating the exact index-\(p^s\) generalization.

**Classification: PASS / CLOSED** for both theorem statements below.

## 1. Index-p^s generalization

Let \(F\) be a finitely generated free pro-p group and let \(K\le F\) be open of index \(p^s\). Since \(F/K\) is a finite p-group, choose a subnormal chain
\[
F=K_0>K_1>\cdots>K_s=K,\qquad [K_{i-1}:K_i]=p.
\]
Every \(K_i\) is again free pro-p.

Applying the certified index-p comparison successively gives
\[
D_n(K_{i-1})\cap K_i
\subseteq D_{\lceil n/p\rceil}(K_i).
\]
Induction therefore yields
\[
\boxed{D_n(F)\cap K\subseteq D_{\lceil n/p^s\rceil}(K).}
\tag{SC_s}
\]

The ceiling identity needed at each step is, for integer \(m\ge1\),
\[
\left\lceil\frac{\lceil m/p\rceil}{p}\right\rceil
=\left\lceil\frac{m}{p^2}\right\rceil,
\]
and hence iteratively
\[
\left\lceil\frac{\cdots\lceil m/p\rceil\cdots}{p}\right\rceil
=\left\lceil\frac{m}{p^s}\right\rceil.
\]
This is an elementary integer identity.

## 2. Sharpness

The correct sharpness statement is **uniform sharpness**, not pointwise sharpness for every integer n.

Let \(F=\langle a,b\rangle\) be free pro-p and
\[
K=\ker\bigl(F\to C_{p^s}\bigr),
\qquad a\mapsto1,\quad b\mapsto0.
\]
A Schreier basis for \(K\) contains
\[
c_0=a^{p^s}.
\]
Thus \(c_0\) is a free generator of \(K\), so by the exact Zassenhaus degree of a free generator and its p-power tower,
\[
c_0^{p^{m-1}}\in D_{p^{m-1}}(K)\setminus D_{p^{m-1}+1}(K).
\]
Set
\[
g_m=a^{p^{m+s-1}}=c_0^{p^{m-1}},
\qquad n_m=p^{m+s-1}.
\]
Then
\[
g_m\in D_{n_m}(F)\cap K
\]
and
\[
g_m\notin D_{\lceil n_m/p^s\rceil+1}(K),
\qquad
\lceil n_m/p^s\rceil=p^{m-1}.
\]
Hence the replacement
\[
D_n(F)\cap K\subseteq D_{\lceil n/p^s\rceil+1}(K)
\]
is false in general, already on the infinite sequence \(n=n_m\).

For \(s=1\), this specializes to the simpler witness \(a^{p^m}\), with \(K=\ker(F\to C_p)\).

### Important scope correction

The stronger sentence sometimes proposed for arbitrary
\(n=p(m-1)+r\) — namely that suitable commutator corrections produce a sharp witness for every n — is **not needed and is not promoted**. It has not been independently proved here. The infinite family \(n=p^{m+s-1}\) is sufficient to establish optimality of the uniform factor \(p^s\).

## 3. What this proves for Paper 4

The universal theorem package is now:

1. **SC (index p):**
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
\]

2. **SC_s (index p^s):**
\[
D_n(F)\cap K\subseteq D_{\lceil n/p^s\rceil}(K).
\]

3. **Uniform sharpness:** the factor \(p^s\) cannot be replaced uniformly by a stronger depth bound \(\lceil n/p^s\rceil+1\).

4. **Critical transfer consequence:** combining SC_s with Jennings–Lazard gives the corresponding depth compression needed for the Paper-4 stress family; at \(n=p^s+1\) the previously certified transfer exponent is exactly \(s\).

The distinction is important: SC/SC_s are universal filtration infrastructure; the genuinely Paper-4-specific theorem remains the intrinsic transfer obstruction and the exact critical-window separation in the declared nondegenerate quadratic stress-family scope.

## 4. Result classification

- Index-p SC: **PASS / CLOSED**.
- Index-p^s SC_s: **PASS / CLOSED**.
- Uniform sharpness of SC_s: **PASS / CLOSED**.
- Pointwise sharpness for every n: **OPEN / not required**.
- SC as standalone literature novelty: **not claimed**; the audited weighted-Schreier literature supplies the component machinery.
- Paper-4 downstream intrinsic separation: **PASS / CLOSED** in the declared scope.

## 5. Publication wording

Do **not** write “we discovered the subgroup-depth inequality from scratch.” The defensible statement is:

> The paper isolates and proves the precise index-p subgroup-depth comparison needed for the finite-window argument, extends it functorially along index-p^s chains, and proves that the resulting p^s compression factor is uniformly optimal. The subsequent intrinsic transfer obstruction and critical-window separation are the Paper-4-specific contribution.



---

# SOURCE: research/PAPER4_WEIGHTED_SCHREIER_DERIVATION_AUDIT_2026-10-05.md

<!-- blob-sha: 6c7295da53c2dae21e121a156d12f714111966bc -->

# Paper 4 — weighted-Schreier derivation gate — 2026-10-05

## Classification

**SC novelty: CONDITIONAL -> likely not independent novelty.**

The uploaded source \`arXiv-1007.1489v3\` is the full TeX source of *Groups of positive weighted deficiency and their applications*. Direct inspection of the relevant Section 2.4 / Section 3 material shows that its weighted-Schreier machinery is strong enough to derive the Paper-4 subgroup comparison
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K)
\]
for a free pro-p group F and an index-p subgroup K, after specializing the uniform weight to the ordinary Zassenhaus filtration.

This does **not** invalidate the Paper-4 theorem. It changes the novelty boundary: the SC statement itself should not be presented as a new standalone theorem until an independent obstruction is found.

## 1. Relevant statements in the source

The source explicitly establishes:

1. **Uniform weight = Zassenhaus order.** Its Proposition \`uniform2\` states that for a finitely generated free pro-p group with a uniform weight function W there is beta in (0,1) such that
\[
W(f)=\beta^{d_F(f)},
\]
where \(d_F(f)\) is the Zassenhaus degree.

2. **Restriction to a closed subgroup remains a weight function.** Its Corollary \`weight_preserve\` states that if W is a weight function on free pro-p F, then its restriction to any closed subgroup H is again a weight function.

3. **Index-p weighted Schreier basis.** Its Lemma \`index_p0\` gives, for an index-p subgroup H and suitable generator x,
\[
X'=\bigcup_{y\ne x}\{y,[y,x],\ldots,[y,\underbrace{x,\ldots,x}_{p-1}],x^p\},
\]
and states that X' is W-optimal when F is free and W is a weight function.

4. **Exact weights of the Schreier generators.** In the proof of its Lemma \`indexp\`, the source states
\[
W(x^p)\le W(x)^p,\qquad
W([y,\underbrace{x,\ldots,x}_{k}])\le W(y)W(x)^k,
\]
with equality in the free/weight-function case.

5. **No-cancellation property.** Its Proposition \`cor1\` characterizes weight functions by power-commutator factorization: the weight of an element is determined by the largest weight of its nonzero power-commutator terms. Thus the weighted filtration is not merely a generator-by-generator upper bound.

## 2. Specialization to the Paper-4 SC

Choose the uniform weight on F with every free generator of weight beta. By \`uniform2\`,
\[
W_F(g)=\beta^{d_F(g)}.
\]

Choose the index-p kernel K and the Schreier basis X' from \`index_p0\`, with the transversal generator z outside K.

The Schreier generators have Zassenhaus/weight exponents at most
\[
1,2,\ldots,p-1,p.
\]
Equivalently, after writing \(W_K=\left.W_F\right|_K\), every generator of X' has W_K-weight exponent at most p.

Because \(W_K\) is again a weight function, the power-series/power-commutator characterization implies that a nontrivial K-element whose ordinary K-Zassenhaus degree is \ell has some nonzero K-coordinate monomial of length \ell, and that monomial has weighted exponent at most \(p\ell\). Hence
\[
d_F(g)\le p\,d_K(g).
\]
Therefore
\[
d_F(g)\ge n\quad\Longrightarrow\quad
d_K(g)\ge\left\lceil\frac np\right\rceil,
\]
which is exactly
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
\]

The key point is that this derivation is not merely heuristic: the source's weight-function characterization supplies the required non-cancellation statement.

## 3. Consequence for the Paper-4 prefix-code proof

The Paper-4 Magnus prefix-code proof remains mathematically valid, but its role changes.

It should **not** be advertised as a new general index-p Zassenhaus comparison theorem unless a genuinely stronger statement is isolated.

Its safer role is:

- an explicit self-contained Magnus-coordinate derivation of the comparison in the precise notation needed by Paper 4;
- a transparent bridge from the free-presentation coordinates to the transfer calculation;
- an independent verification/alternative proof of a consequence already accessible from weighted-Schreier theory.

The previous wording “strongest novelty candidate = SC” should therefore be downgraded.

## 4. What remains potentially novel

The literature threat is substantially weaker for the downstream Paper-4 objects:

### (a) The finite-window transfer obstruction
\[
\varepsilon_s(W)
=p^{s-1}V(t)\pmod{p^sK^{ab}}.
\]

The uploaded weighted-Schreier source does not contain this finite-window torsion-line construction.

### (b) The exact \(a=s\) versus \(a=\infty\) separation

The source contains no theorem matching the Paper-4 stress family
\[
z^{p^s}=x_1^{p^a}r_2^{-1}
\]
and no finite-window comparison proving non-isomorphism at \(n=p^s+1\).

### (c) The exact threshold
\[
n_{\mathrm{sep}}(s)=p^s+1
\]
for the declared stress family.

The weighted-Schreier machinery explains the subgroup-filtration estimate needed for the proof, but does not by itself produce the Paper-4 torsion defect or the separation theorem.

## 5. Novelty classification after the source audit

- General index-p Zassenhaus comparison SC: **CONDITIONAL / likely standard corollary of weighted-Schreier theory**.
- Paper-4 Magnus prefix-code implementation: **PASS / mathematically valid; novelty not claimed**.
- Transfer bound TF_s: **PASS / CLOSED mathematically; novelty dependent on downstream construction**.
- Intrinsic finite-window \(\varepsilon_s\): **OPEN / strongest current novelty candidate**.
- \(a=s\) versus \(a=\infty\) separation at \(p^s+1\): **OPEN / strong theorem-level novelty candidate**.
- Exact threshold \(p^s+1\): **OPEN / strong application-level novelty candidate**.
- Paper-4 mathematical result overall: **PASS / CLOSED** in the declared scope.
- Publication novelty overall: **CONDITIONAL / OPEN**.

## 6. Governance consequence

Do not reopen the mathematical Paper-4 proof merely because SC has a close prior derivation.

The correct response is to **move the novelty center of gravity downstream**:
weighted-Schreier comparison -> transfer bound -> intrinsic \(\varepsilon_s\) -> exact finite-window separation.

The next literature search should therefore target the exact \(\varepsilon_s\), finite-window torsion-line obstruction, and the \(a=s\) versus \(a=\infty\) family, not generic index-p Schreier theory.


## 2026-10-05 — direct source recheck: SC derivation is genuinely covered by the weighted-Schreier chain

The uploaded source was decompressed and the cited statements were inspected line-by-line, rather than inferred from the earlier summary. The relevant chain is exact:

`uniform2` gives (W_F(g)=\beta^{d_F(g)}) for the uniform weight on free (F).

`weight_preserve` says the restriction (W_K=W_F|_K) is again a weight function on the closed subgroup (K).

`index_p0) gives the standard index-(p) Schreier generating set
[
X'={y,[y,z],ldots,[y,z,ldots,z],z^p}
]
and says it is (W_K)-optimal in the free case.

The proof of `indexp` gives equality of weights in the free/weight-function case:
[
W_K([y,z,ldots,z]_j)=W_F(y)W_F(z)^j=\beta^{j+1},
qquad
W_K(z^p)=W_F(z)^p=\beta^p.
]
Thus every Schreier generator has ambient Zassenhaus exponent at most (p).

Finally, `cor1`(ii) is explicitly a **global no-cancellation statement for every (fin K)** in its power-commutator factorization in (X'):
[
W_K(f)=max{W_K(c)^{p^k}:\alpha_{c,k}
e0}.
]
This is the precise missing logical step needed to turn generator weight bounds into an elementwise comparison.

Hence, if (d_K(f)=ell), a nonzero K-power-commutator term of K-degree at most (ell) has ambient exponent at most (pell), and `cor1` prevents cancellation at the maximal (W_K)-weight. Since (W_K(f)=W_F(f)=\beta^{d_F(f)}), one gets
[
d_F(f)le p,d_K(f).
]
Therefore
[
D_n(F)cap Ksubseteq D_{lceil n/pceil}(K).
]

### Review verdict

The earlier caution about “is cor1 strong enough?” is now resolved **YES**: `cor1` is stated for arbitrary (fin F), not merely for generators or selected optimal words, and its proof explicitly rules out cancellation in the relevant power-commutator factorization.

The correct novelty statement is consequently stronger than “the SC proof resembles prior work”:

- **SC itself is a derivable consequence of prior weighted-Schreier machinery under the Paper-4 hypotheses.**
- The Magnus prefix-code proof is a valid self-contained reproof/coordinate realization, but should not be presented as the novel theorem.
- The novelty audit must move downstream to the intrinsic transfer obstruction (arepsilon_s), the (a=s) versus (a=\infty) finite-window separation, and the exact threshold (p^s+1).

This is a literature-method transfer result, not a negative result about Paper 4's mathematics.


## 2026-10-05 — SC literature audit CLOSED by decision

The project now treats the SC audit as closed. The distinction is:

**Prior literature:** supplies the weighted-Schreier/Zassenhaus ingredients.

**Paper-4 deduction:** assembles those ingredients into the exact depth-comparison
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K),
\]
in the form required for the finite-window transfer argument.

No audited source was found stating this exact subgroup-depth comparison as the Paper-4 lemma, although the weighted-Schreier machinery is sufficient to derive it. Therefore the safe novelty language is **new logical deduction/assembly**, not “new underlying Zassenhaus/Schreier theory.”

Classification:
- SC mathematical validity: **PASS / CLOSED**.
- SC literature audit: **PASS / CLOSED**.
- SC as independent foundational theorem: **not claimed**.
- SC as a new Paper-4 logical step in the proof chain: **YES — claimable**.
- Further generic SC literature search: **STOPPED**.
- Novelty audit moves downstream to \(\varepsilon_s\), intrinsic finite-window separation, and the exact threshold \(p^s+1\).

The Magnus prefix-code proof remains as an independent self-contained verification and should be presented as such.


---

# SOURCE: research/PAPER4_FINAL_BOUNDARY_ATTACK_2026-10-04.md

<!-- blob-sha: 1acec9422ba303e6d7f79fb365eb98e2439bdd3d -->

# Paper 4 — Final Boundary Attack (2026-10-04)

## Purpose

This record closes the two remaining boundary attacks from the 2026-10-04 Paper 4 audit. It records only results that survived the final attack; unresolved cases remain explicitly OPEN.

## 1. Same numerical-window separation: CLOSED

For the stress family
\[
G_{s,a}=\langle z,x_1,\ldots,x_d\mid
z^{p^s}=x_1^{p^a}[x_1,x_2]\cdots[x_{d-1},x_d]\rangle,
\qquad 1\le a<s<t,
\]
put \(n_s=p^s+1\).

Because \(p^t>n_s\), the defining relation of \(G_{t,a}\) is invisible in the \(n_s\)-window, whereas the relation of \(G_{s,a}\) survives at its critical layer:
\[
W_{n_s}(G_{t,a})=F/(D_{n_s},r_D),
\]
\[
W_{n_s}(G_{s,a})=F/(D_{n_s},z^{p^s}r_D^{-1}).
\]

There is a canonical epimorphism
\[
W_{n_s}(G_{s,a})\twoheadrightarrow W_{n_s}(G_{t,a})
\]
whose kernel is generated by the image of \(z^{p^s}\), hence has order at most \(p\). A class-2 finite \(p\)-group witness establishes that \(z^{p^s}\notin D_{p^s+1}(G_{s,a})\); therefore the kernel has order exactly \(p\). Consequently
\[
|W_{p^s+1}(G_{s,a})|
=p\,|W_{p^s+1}(G_{t,a})|,
\]
so the two finite windows are not isomorphic.

This supersedes the earlier relative-extension/non-splitting formulation as the load-bearing separation argument: direct same-window order separation is sufficient.

### Exact threshold

Combined with the already-closed universal blindness result
\[
W_n(G_s(r))\cong F/(D_n(F),r)\qquad(n\le p^s),
\]
the stress family has the exact unmarked separation threshold
\[
\boxed{n_{\mathrm{sep}}(s)=p^s+1}.
\]

## 2. Boundary \(a=s\) versus \(a=\infty\)

At \(n=p^s+1\), the two cases have the same finite-window abelianization:
\[
W_n^{ab}\cong \mathbb Z/p^s\oplus(\mathbb Z/p^{s+1})^d.
\]
Ordinary associated-graded/restricted-Lie data, naive short-line \(p^s\)-power tests, and scalar abelianized/coinvariant extension defects were attacked and do not provide a general separator. These routes are CLOSED as non-load-bearing approaches.

For \(p=3,s=1\), the \(A_3\)-formality obstruction distinguishes the two cases, and the obstruction factors through the critical finite window \(W_4\). Thus
\[
W_4(G_{1,1})\not\cong W_4(G_{1,\infty}).
\]
This case is CLOSED.

For \(s\ge2\), the general boundary
\[
\boxed{W_{p^s+1}(G_{s,s})\stackrel{?}{\cong}W_{p^s+1}(G_{s,\infty})}
\]
remains OPEN. The existing \(A_3\)-formality route does not resolve it in general, since the relevant odd-\(p\) Demushkin cases with \(q\ne3\) are \(A_3\)-formal.

The remaining problem is therefore genuinely narrower: find a functorial invariant of the finite group \(W_{p^s+1}\) (or an explicit finite-window isomorphism) that resolves the \(q=p^s\) versus \(q=0\) boundary for \(s\ge2\). Re-running mod-\(p\) cohomology, ordinary \(gr_Z\), ordinary Bockstein, or scalar coinvariant defects is not expected to advance this boundary.

## Status ledger

- lower-window blindness: **CLOSED**
- critical survival: **CLOSED**
- direct same-window order jump: **CLOSED**
- exact unmarked stress-family threshold \(p^s+1\): **CLOSED**
- \(a=s\) vs \(a=\infty\), \((p,s)=(3,1)\): **CLOSED**
- \(a=s\) vs \(a=\infty\), \(s\ge2\): **OPEN / LOAD-BEARING**

## Record discipline

This file records the 2026-10-04 attack outcome. It does not claim a universal theorem beyond the stated stress-family scope, and it does not close the remaining \(s\ge2\) boundary.


---

# SOURCE: research/PAPER4_D1_GLOBAL_LOWER_FILTRATION_SIGNATURE_AUDIT_2026-10-02.md

<!-- blob-sha: fdddba4089fbda9571aa5dd4c8129c56110b58f9 -->

# PAPER 4 — GATE D1 FORMALIZATION: GLOBAL LOWER-FILTRATION SIGNATURE — 2026-10-02

## Decision

A definition-level D1 candidate survives the intrinsicity pre-check:

\[
\boxed{\Lambda_E(u,x):=
\max\{m\le n+1:\exists\ \tilde u,\tilde x\in Y,
\ \tilde u\mapsto u,\ \tilde x\mapsto x,\ [\tilde u,\tilde x]\in D_m(Y)\}}
\]

for an adjacent finite window
\[
E:\quad 1\to A=D_n/D_{n+1}\to Y=W_{n+1}\xrightarrow{\pi}X=W_n\to1,
\qquad L_1=X/\Phi(X),
\]
with \(u,x\in L_1\). The value \(n+1\) is assigned when the commutator is trivial in \(Y\); equivalently one may regard \(\Lambda_E(u,x)\) as the full set of attainable filtration depths rather than a single maximum.

The associated **global lower-filtration signature** of \(u\) is
\[
\boxed{
\mathcal L_E(u)=\bigl(\Lambda_E(u,x)\bigr)_{x\in L_1},
}
\]
or, without choosing a scalar encoding,
\[
\mathscr R_m(u)=\{x\in L_1:\exists\text{ lifts with }[\tilde u,\tilde x]\in D_m(Y)\},
\qquad
\mathcal L_E(u)=(\mathscr R_m(u))_{m=2}^{n+1}.
\]

This is deliberately a **global signature**, not a distinguished pair \((u,x)\), and not a bilinear map \(L_1\times L_1\to A\).

## 1. Object

The input is only the abstract filtered adjacent pair \((Y\twoheadrightarrow X)\), with its characteristic filtration and the induced degree-one quotient \(L_1=X/\Phi(X)\).

For each \(u\in L_1\), all lifts of \(u\) in \(Y\) are allowed. For each \(x\in L_1\), all lifts are allowed. The signature records which lower-filtration depths can be achieved simultaneously for that pair.

No presentation, generator, section, displayed \(q\), or orientation is part of the definition.

## 2. Why the definition is gauge/lift-independent

The crucial point is the existential quantifier over the **entire lift fiber**.

If an automorphism of the presentation or a change of section replaces a chosen lift by another lift in the same fiber, that new lift is already included in the defining set. Thus \(\mathscr R_m(u)\) is defined by the finite group extension itself, not by a selected representative.

This avoids the false step
\[
[\tilde u,\tilde x]\bmod D_{q+1}
\quad\text{is automatically independent of arbitrary }D_2\text{-lift changes}.
\]
That step was closed in the raw origin-restricted pairing audit.

## 3. Functoriality

A filtered isomorphism of adjacent windows transports:
- the filtration \(D_m\);
- the projection \(Y\to X\);
- the Frattini quotient \(L_1\);
- the complete lift fibers;
- the commutator relation.

Therefore
\[
\mathcal L_E(u)
\longmapsto
\mathcal L_{E'}(f(u))
\]
naturally under filtered isomorphism.

No claim is made yet for arbitrary non-isomorphic graph morphisms.

## 4. q-blindness

The definition contains no distinguished \(q\). It is defined simultaneously at every filtration depth available in the finite window.

The number \(q\) may later appear as the first exceptional depth in a particular target class, but that is an **output interpretation**, not an input to \(\mathcal L_E\).

This satisfies the required q-blindness test at the definition level.

## 5. Relation to the lower-obstruction problem

The previous failed formulation asked whether a particular pair satisfies
\[
[\tilde u,\tilde x]\notin D_q.
\]
That is too local and is unstable as a purported canonical degree-q value.

The present object instead records the entire depth profile
\[
m\longmapsto \mathscr R_m(u)
\]
against **all** degree-one directions simultaneously.

Thus a direction with one lower-degree contaminating origin is not merely assigned a yes/no label; the obstruction is part of its full global signature.

This directly addresses the current D1 requirement.

## 6. Independent model checks

### (a) Rank-two special edge

For
\[
G=\langle v,w\mid wvw^{-1}=v^{1+q}\rangle,
\]
the canonical special direction satisfies
\[
\Lambda_E(\bar w,\bar v)=q,
\]
because the first nontrivial commutator survives in \(D_q/D_{q+1}\).

The same depth is visible in the reverse pair up to the usual convention/sign/inverse:
\[
\Lambda_E(\bar v,\bar w)=q.
\]

This confirms that the signature retains the intended higher-depth defect without introducing \(q\) into its definition.

### (b) Long ordinary-chain contamination

In the audited chain
\[
r_1-r_2-a\to s,
\]
the special direction has q-depth against the relevant origin, whereas an ordinary contaminated direction has a degree-2 obstruction. Hence
\[
\mathcal L_E(\bar s)\neq \mathcal L_E(\bar s+\bar r_1)
\]
already at the lower part of the filtration profile.

This is the precise local phenomenon the scalar q-layer projection lost.

### (c) Separated two-sink model

For
\[
G=\langle a,b,s,t\mid sas^{-1}=a^{1+q},\;
tbt^{-1}=b^{1+q}\rangle,
\]
the signature detects
\[
\Lambda_E(\bar s,\bar a)=q,
\qquad
\Lambda_E(\bar t,\bar b)=q.
\]

However,
\[
\Lambda_E(\bar s+\bar t,\bar a)=q
\]
because the \(t\)-component is invisible to the \(a\)-sector in this model. Therefore D1 does **not** itself imply that q-active directions are literal sink directions.

This is not a failure of D1. It is an explicit warning that D2 must extract a quotient/kernel from the **relations among the full signatures**, rather than declaring the q-active locus to be \(N_q^\perp\).

### (d) Isolated special direction

The isolated-special counterexample remains controlling for the unrestricted class: an isolated special vertex can have orientation value 1 while contributing no special-edge lower-filtration signature. Thus no D1 object built solely from special-edge defects can recover the unrestricted orientation without an additional admissibility restriction or marked input.

D1 therefore does not reopen the already CLOSED unrestricted Gate-D no-go.

## 7. Non-tautology test

The construction does not reference \(\chi\), \(\omega_q\), Kummerianity, or a declared special-vertex set.

It is therefore not a disguised definition of the desired orientation.

The possible objection is different: the signature may be **too rich** because it records a large portion of the filtered multiplication. This is a coarseness/novelty question for D2/D3, not a definition-level failure.

## 8. Precise D1 theorem target

The load-bearing D1 statement is:

> For every admissible adjacent window, the family \(\mathcal L_E(u)\) is an intrinsic, presentation-independent, lift-independent, filtered-isomorphism-covariant global lower-filtration signature of \(u\in L_1\).

This statement is now defensible at the definition level.

What is **not** proved:
1. \(\mathcal L_E\) is linear in \(u\);
2. the sets \(\mathscr R_m(u)\) are always subspaces;
3. \(\mathcal L_E\) alone determines \(\omega_q\);
4. a canonical \(N_q\) can already be extracted;
5. the unrestricted specially oriented class admits positive orientation recovery.

## 9. Classification

- global lower-filtration signature definition \(\mathcal L_E\): **PASS / LOCAL**;
- presentation/lift/gauge independence: **PASS / LOCAL**;
- filtered-isomorphism covariance: **PASS / LOCAL**;
- q-blindness: **PASS / LOCAL**;
- non-tautological definition: **PASS / LOCAL**;
- linearity/subspace structure: **OPEN / LOAD-BEARING**;
- canonical quotient extraction \(N_q\): **OPEN / LOAD-BEARING**;
- orientation bridge \(N_q\to\omega_q\): **OPEN / LOAD-BEARING**;
- unrestricted Gate D: **FAIL / CLOSED** remains controlling;
- Paper 4: **OPEN / LOAD-BEARING** only on a declared restricted admissible class/input.

## 10. Stop rule for the next step

Do **not** immediately define
\[
N_q:=\operatorname{span}\{u:\mathcal L_E(u)\text{ is q-invisible}\}.
\]
The current separated two-sink examples already show why that would be too coarse.

The authorized D2 attack is narrower:

> Determine whether the **relations among the signatures**
> \[
> \{\mathcal L_E(u):u\in L_1\}
> \]
> canonically define a linear quotient \(U/N_q\), without inserting \(q\), \(\omega_q\), a graph, or a chosen basis.

The first test must be the smallest separated two-sink and the chordal-tree controls. If the resulting quotient still admits an orientation-changing automorphism, D2 closes for that signature.

## Final status

\[
\boxed{
\text{D1: intrinsic global lower-filtration signature = PASS / LOCAL}
}
\]

The result is a **definition-level advance**, not yet an orientation theorem. The next legitimate gate is D2, but only through relations among the full signatures, not through a q-visible locus or a pairwise obstruction.


---

# SOURCE: research/PAPER4_D2_CRITICAL_REAUDIT_2026-10-02.md

<!-- blob-sha: 8d4f5f6e704a1cbd7694fcf261cd71895f01c824 -->

# PAPER 4 D2 CRITICAL RE-AUDIT — 2026-10-02

## Purpose
This audit corrects the scope of the D2 no-go after a critical review. It does not reopen the already closed D1 depth-signature scalar obstruction. It prevents two stronger statements from being used without proof.

## 1. Surviving D2 theorem
For the rank-two special-edge model
\[
G=\langle v,w\mid wvw^{-1}=v^{1+q}\rangle,
\]
nonzero scalar multiples satisfy
\[
S_E(\lambda\bar w)=S_E(\bar w),
\qquad \omega_q(\lambda\bar w)=\lambda.
\]
Hence the D1 global lower-filtration depth signature does not determine the normalized orientation coefficient. Any quotient whose information is exhausted by the D1 signature cannot recover this normalization.

**Classification: FAIL / CLOSED.**

## 2. First coefficient-valued incidence quotient
In the audited chordal tree, the coefficient-valued incidence package gives a relation
\[
u-s-t\in\ker\Phi,
\qquad \omega_q(u-s-t)=-1\ne0.
\]
This proves that this **particular first-coefficient incidence quotient** is not an orientation carrier.

What it does not prove is failure of the entire restricted finite extension. The coefficient map is a projection of the extension information; higher extension structure may distinguish directions identified by the first coefficient quotient.

**Classification: FAIL / CLOSED for the first-coefficient incidence quotient; full extension = OPEN.**

## 3. Isolated ordinary-direction argument: correction
The mixed model with an ordinary isolated direction \(z\) yields a family of linear functionals
\[
\omega_c(\alpha s+\beta z)=\alpha+c\beta
\]
that agree on the normalized filtered-profile locus. This establishes that the profile alone does not constrain arbitrary linear extensions on all of \(U\).

It does **not** establish that the canonical orientation itself is non-unique, because no proof was given that the alternative \(\omega_c\) satisfies the canonical orientation's defining torsion-free/Kummerian conditions. Therefore the earlier conclusion “filtered q-profile alone cannot determine canonical orientation” is withdrawn in this unrestricted form.

**Classification: OVERCLAIM — HISTORICAL / SUPERSEDED.**

## 4. Consequence for D3
D3 is not authorized as an unconstrained search for another carrier. The surviving question is narrower:
\[
\text{Can a minimal intrinsic nonlinear extension invariant retain exactly the information}
\]
\[
\text{lost by D1 and by the first coefficient quotient, and then determine the canonical orientation?}
\]
The candidate must be defined from the finite extension itself, not by inserting \(q\), a presentation, a basis, a section, or \(\omega_q\).

Before computation the full continuity pre-check is mandatory: Object, Input, Functoriality, Gauge, Orientation bridge, q-blindness, Separation, Novelty, Stop.

## 5. Current boundary
- D1 depth signature → normalized orientation: **FAIL / CLOSED**.
- D1-relation quotient → normalized orientation: **FAIL / CLOSED**.
- First coefficient-valued incidence quotient → orientation: **FAIL / CLOSED**.
- Full restricted finite extension / genuinely nonlinear invariant: **OPEN / LOAD-BEARING**.
- Same-window class-level non-identifiability for the unrestricted un-oriented input remains a separate negative boundary; it is not replaced by the overclaimed isolated-ordinary functional argument.

## 6. Research discipline
Do not use the withdrawn \(\omega_c\) family as a canonical-orientation counterexample. Do not claim that the full extension has failed merely because its first coefficient projection has failed. Do not restart carrier hunting. The next authorized step is target-first definition of the smallest nonlinear extension invariant, followed by independent model verification and immediate classification.


---

# SOURCE: research/PAPER4_D2_SIGNATURE_RELATION_QUOTIENT_NO_GO_AUDIT_2026-10-02.md

<!-- blob-sha: 75220c5418214d440b7fb8ae6679c1536b280d31 -->

# PAPER 4 — GATE D2: SIGNATURE-RELATION QUOTIENT NO-GO — 2026-10-02

## Decision

The authorized D2 route — extracting a canonical linear quotient from **relations among the full D1 depth signatures**
\[
\mathcal L_E(u)=\bigl(\mathscr R_m(u)\bigr)_{m=2}^{n+1}
\]
— is **FAIL / CLOSED for orientation normalization**.

The obstruction is earlier and sharper than the previously known chordal-tree kernel obstruction:

> The D1 signature records **attainable filtration depth**, but not the nonzero scalar coefficient of the first surviving defect.

Already in the rank-two special-edge model, every nonzero scalar multiple of the special direction has exactly the same D1 signature, while the canonical orientation functional takes different values on those multiples.

Thus no quotient, relation space, or factorization constructed solely from the D1 signature can carry the normalized orientation functional.

## 1. D2 object under test

Let
\[
E:1\to A=D_n/D_{n+1}\to Y\to X=W_n\to1,
\qquad U=L_1=X/\Phi(X).
\]

D1 supplies
\[
S_E:U\longrightarrow\mathscr S_E,
\qquad
S_E(u)=\mathcal L_E(u)
=(\mathscr R_m(u))_m,
\]
where
\[
\mathscr R_m(u)=
\{x\in U:\exists\text{ lifts }\tilde u,\tilde x
\text{ with }[\tilde u,\tilde x]\in D_m(Y)\}.
\]

The authorized D2 question is whether the relations among the values of $S_E$ can canonically define
\[
U\twoheadrightarrow U/N_E
\]
and then a normalized orientation functional on $U/N_E$.

The crucial point is that any such construction **from the signature values alone** is constant on the fibers of $S_E$.

## 2. Decisive rank-two special-edge calculation

Take
\[
G=\langle v,w\mid wvw^{-1}=v^{1+q}\rangle,
\qquad q=p^f,
\]
with $p$ odd.

In degree one, write $\bar v,\bar w\in U$.

For the special direction $\bar w$, the first nontrivial commutator with $\bar v$ occurs at depth $q$:
\[
[w,v]=v^q
\quad\text{mod higher filtration}.
\]

Now replace $w$ by any nonzero scalar multiple $\lambda w$ in $U$, $\lambda\in\mathbf F_p^\times$.

At the depth level, the commutator changes by a nonzero scalar:
\[
[\lambda w,v]
\equiv \lambda\,[w,v]
\pmod{D_{q+1}},
\]
so its **depth remains exactly $q$**.

The same observation holds against every degree-one direction $x$: multiplying the first argument by a nonzero scalar cannot turn a nonzero leading filtered commutator into zero or create a lower filtration term. Consequently
\[
\boxed{S_E(\lambda\bar w)=S_E(\bar w)
\qquad(\lambda\in\mathbf F_p^\times).}
\]

But the canonical orientation satisfies
\[
\omega_q(\bar w)=1,
\qquad
\omega_q(\lambda\bar w)=\lambda.
\]

Choose $\lambda\neq1$. Then
\[
S_E(\lambda\bar w)=S_E(\bar w)
\quad\text{but}\quad
\omega_q(\lambda\bar w)\neq\omega_q(\bar w).
\]

This is a direct factorization obstruction:
\[
\boxed{\omega_q\text{ does not factor through }S_E.}
\]

No calculation of a larger model is needed to establish this D2 no-go.

## 3. Why “relations among signatures” cannot rescue the loss

Suppose one forms any formal linearization of the signature values, for example a vector space generated by symbols $[S_E(u)]$ and imposes all intrinsic relations among those symbols.

Because
\[
S_E(\lambda\bar w)=S_E(\bar w),
\]
the relation
\[
[S_E(\lambda\bar w)]-[S_E(\bar w)]=0
\]
is forced.

Any linear map induced from the signature therefore identifies $\lambda\bar w$ with $\bar w$ at the level of available information.

But the desired orientation difference is
\[
\omega_q(\lambda\bar w-\bar w)
=(\lambda-1)\neq0.
\]

Hence the orientation cannot be recovered from any quotient whose defining information is exhausted by D1 signature relations.

This also rules out the tempting “universal linear factor” construction:
\[
N_E=\bigcap\{\ker\ell:
\ell\text{ is linear and factors through }S_E\}.
\]
In the rank-two model, the equality of signatures for $\bar w$ and $\lambda\bar w$ forces every such $\ell$ to vanish on $\bar w$ when $\lambda\neq1$. Therefore the resulting factor loses the very direction on which normalization is required.

## 4. Independent control: separated two-sink model

Consider
\[
G=
\langle a,b,s,t\mid
sas^{-1}=a^{1+q},\;
tbt^{-1}=b^{1+q}\rangle.
\]

For $\lambda\neq0$,
\[
S_E(\lambda\bar s)=S_E(\bar s),
\qquad
S_E(\lambda\bar t)=S_E(\bar t),
\]
while
\[
\omega_q(\lambda\bar s)=\lambda,
\qquad
\omega_q(\lambda\bar t)=\lambda.
\]

Thus the obstruction is not an artifact of the two-generator model.

Moreover, the earlier D1 observation
\[
S_E(\bar s+\bar t)
\]
can retain q-depth information from both sink sectors without determining their coefficients. The depth signature therefore detects **support/visibility**, not the normalized coefficient sum required by $\omega_q$.

This explains why the earlier scale-fixing construction had to use a coefficient-valued object such as the restricted-power target and a normalized extension defect. Pure depth data cannot perform that scale fixing.

## 5. Independent control: chordal tree

For the audited chordal tree
\[
s-a-u-b-t
\]
with special edges $a\to s$, $b\to t$, $a\to u$, $b\to u$, the q-defect coefficient package satisfies
\[
\Phi(s)=P_a,\qquad
\Phi(t)=P_b,\qquad
\Phi(u)=P_a+P_b.
\]

The relation
\[
u-s-t\in\ker\Phi
\]
has
\[
\omega_q(u-s-t)=-1\neq0.
\]

Therefore even after one enriches the depth signature enough to retain its first surviving coefficient through the particular pairing package, the resulting incidence relation itself is not an orientation quotient: its kernel contains nonzero orientation mass.

This is a second, logically independent obstruction:
- D1 depth-only signature loses **scalar normalization**;
- coefficient-valued incidence relations can retain coefficients but may introduce **orientation-nonzero kernel directions**.

Thus the two obvious linearizations fail for opposite reasons.

## 6. Exact boundary

The D2 result does **not** say that no finite-window orientation recovery is possible in every enriched input.

It says precisely:

\[
\boxed{
\text{D1 global depth signature alone}
\not\Longrightarrow
\text{normalized }\omega_q.
}
\]

To restore normalization, the input must retain some coefficient-valued, nonabelian extension datum beyond the D1 depth sets.

The most economical surviving direction is not a new carrier search. It is the already identified restricted-origin finite extension:
\[
E|_{H(O_q)}
\]
together with its intrinsic first nonzero extension coefficient relative to the intrinsic restricted-power target.

That object must pass a **fresh** Object/Input/Functoriality/Gauge/q-blindness/Separation/Novelty/Stop audit before any D3 claim.

## 7. Classification

- D1 global lower-filtration depth signature: **PASS / LOCAL**.
- D2 quotient from relations among D1 signatures: **FAIL / CLOSED**.
- D2 orientation factorization through depth signature: **FAIL / CLOSED**.
- Scalar-normalization information in D1: **FAIL / CLOSED**.
- Coefficient-valued incidence quotient as an orientation carrier: **FAIL / CLOSED** by the chordal-tree relation $u-s-t$.
- Restricted-origin coefficient-valued extension datum: **OPEN / LOAD-BEARING**.
- Unrestricted Gate D: **FAIL / CLOSED** remains controlling.
- Paper 4: **OPEN**, but only for a newly specified enriched input/restricted admissible class.

## 8. Next authorized action

Do not continue manipulating $\mathcal L_E$ or search for another quotient of its depth relations.

The only authorized continuation is:

1. define the **smallest coefficient-valued intrinsic extension object** that augments D1 exactly enough to restore scalar normalization;
2. run the full pre-check;
3. test it first on the rank-two special edge, separated two-sink, long ordinary-chain, and chordal-tree controls;
4. independently test whether its orientation kernel is contained in $\ker\omega_q$;
5. if that fails, record a stronger impossibility boundary and stop the branch.

This is a target-preserving refinement, not a return to unconstrained carrier hunting.

## Final status

\[
\boxed{\text{D2 = FAIL / CLOSED for the D1 depth-signature route.}}
\]

The failure is structural: **depth remembers when a defect first appears, but not how much of the normalized orientation direction produced it.**


## CORRECTION — 2026-10-02

A convention-sensitive sentence in §4 is superseded. In the separated two-sink model, absence of an edge does **not** mean commutation. Therefore one must not claim that the full D1 signature of \(s+t\) equals that of \(s\).

The D2 no-go does **not** depend on that claim. It is already decisive in the rank-two special-edge model, where nonzero scalar multiples \(\lambda\bar w\) have the same depth signature but different orientation values. In the separated model, mixed directions such as \(s+t\) instead carry lower-filtration contamination against the wrong origin; this is consistent with the corrected nonabelian filtered-profile analysis.

The separated model remains an independent control for support/lower-obstruction detection, not a second proof of scalar-fiber equality.


## CORRECTION — 2026-10-02

A convention-sensitive sentence in §4 is superseded. In the separated two-sink model, absence of an edge does **not** mean commutation. Therefore one must not claim that the full D1 signature of (s+t) equals that of (s).

The D2 no-go does **not** depend on that claim. It is already decisive in the rank-two special-edge model, where nonzero scalar multiples (lambdaar w) have the same depth signature but different orientation values. In the separated model, mixed directions such as (s+t) instead carry lower-filtration contamination against the wrong origin; this is consistent with the corrected nonabelian filtered-profile analysis.

The separated model remains an independent control for support/lower-obstruction detection, not a second proof of scalar-fiber equality.


---

# SOURCE: research/PAPER4_D3_MINIMAL_NONLINEAR_EXTENSION_AUDIT_2026-10-02.md

<!-- blob-sha: 45c92d13e0918d3cd9929a451d1032ed146b418c -->

# PAPER 4 D3 — MINIMAL NONLINEAR EXTENSION AUDIT — 2026-10-02

## Decision

The first genuinely nonlinear candidate is the **intrinsic finite conjugation-action extension** of the adjacent window, not the first coefficient projection.

For
[
E_n:1	o A_n=D_n/D_{n+1}	o Y=W_{n+1}	o X=W_n	o1,
]
with the intrinsic origin sector (O_nsubset L_1=X/Phi(X)), retain the full group extension together with the filtration and the induced conjugation action of (Y) on the canonical subgroup generated by the origin lift-fibres. The candidate observable is the resulting nonlinear action/defect, rather than its linearized first coefficient.

The key reason this is the correct next object is that a special edge is defined by a multiplicative conjugation law
[
wvw^{-1}=v^{1+q},
]
and the q-dependent information is therefore an automorphism/action in the finite extension. The first coefficient quotient (Phi) discards precisely part of this multiplicative structure.

## 1. Object

Let (widehat O_nle Y) be the subgroup generated by the full lift-fibres of the intrinsic origin sector (O_n). Do not choose a basis or section. The candidate datum is
[
mathcal C_n(O_n):=
igl(Y,widehat O_n, A_n, X, mathrm{conj}_Y(widehat O_n)igr)
]
up to filtered extension isomorphism.

Equivalently, retain the conjugation action as a group-valued object rather than applying a first-order coefficient map.

This is strictly richer than D1 and strictly richer than the first coefficient-valued incidence quotient.

## 2. Pre-check

### Object — PASS / LOCAL
The object is a finite filtered extension with a canonically generated origin-lift subgroup and its conjugation action. No presentation, basis, or chosen section is required in the definition.

### Input — PASS / LOCAL
The input is the adjacent finite window together with the already intrinsic origin sector (O_n). No q, orientation, or displayed graph is inserted.

### Functoriality — PASS / LOCAL
A filtered isomorphism of adjacent windows transports the extension, the origin sector, its lift-generated subgroup, and conjugation action.

### Gauge — PASS / LOCAL
Changing lifts changes representatives inside the same generated subgroup and conjugation action. No chosen splitting is retained.

### Orientation bridge — OPEN / LOAD-BEARING
The intended bridge is the special-edge action
[
wvw^{-1}=v^{1+q},
]
which should allow recovery of the multiplicative factor (1+q) from the finite extension. A global reconstruction theorem for arbitrary degree-one elements is not yet proved.

### q-blindness — PASS / LOCAL
The object is defined from the finite filtered groups and their group law only. q is not named.

### Separation — PASS / LOCAL
In the rank-two special-edge model, the extension distinguishes the first survival of the conjugation correction at the q-layer. In the undirected/ordinary case the corresponding action is trivial at that layer. Thus the object is capable of retaining information discarded by D1.

### Novelty — CONDITIONAL
The underlying conjugation relation is classical and the canonical orientation theorem of Blumer–Quadrelli–Weigel already identifies the canonical orientation on the full oriented RAAG. The potentially new statement would be a **finite-window, q-blind factorization through the minimal nonlinear extension action**. No novelty claim is made until this finite factorization is proved and compared against the literature.

### Stop — PASS
The definition-level gates are sufficient to justify the four-control audit below. No computation beyond those controls is authorized.

## 3. Four-control audit

### A. Rank-two special edge — PASS / LOCAL

For
[
G=langle v,wmid wvw^{-1}=v^{1+q}angle
]
the D1 signature identifies all nonzero scalar multiples of (ar w), but the full conjugation law does not discard the multiplicative action. The q-correction survives in the adjacent extension and is exactly the type of information required to distinguish the normalized action from a scalar-blind depth profile.

This closes the scalar-obstruction only for the **new object**, not yet for the global orientation theorem.

### B. Separated two-sink — PASS / LOCAL

For
[
sas^{-1}=a^{1+q},qquad tbt^{-1}=b^{1+q},
]
the nonlinear action is origin-specific. Lower-filtration contamination prevents the erroneous identification of (s+t) with a pure sink, while the full action retains the separate conjugation data. Thus the convention correction is respected.

### C. Long ordinary-chain — PASS / LOCAL

The long ordinary chain produces lower-degree commutator contamination before the q-layer. Hence the nonlinear extension action must be conditioned on the absence of lower obstruction; it cannot be replaced by a q-layer projection alone.

This confirms that the full extension carries strictly more information than the filtered q-profile.

### D. Chordal-tree — OPEN / LOAD-BEARING

The earlier relation
[
u-s-tinkerPhi,qquadomega_q(u-s-t)
e0
]
does not by itself kill the full action object, because (Phi) is only a projection. The required test is whether the full conjugation-action object still identifies (u) with (s+t) or separates them.

No valid argument currently proves a kernel of the full object with nonzero orientation mass. Therefore the previous coefficient-quotient no-go cannot be promoted to the full extension.

## 4. What can already be proved conceptually

The literature independently confirms the structural bridge: for a specially oriented graph, the canonical orientation is characterized by Kummerianity, and the canonical orientation assigns (1+q) to special/sinkhole vertices and (1) to ordinary vertices. Moreover, in the local two-generator arguments the canonical orientation is determined by the structure of the locally uniform two-generator subgroup. citeturn0search0turn3search1turn3search0

Therefore the finite-extension candidate is not inventing a new orientation law: it isolates the multiplicative conjugation mechanism from which the known local orientation law arises.

What is **not** proved is the crucial compression statement:
[
mathcal C_q(O_q)
Longrightarrow
omega_qpmod {p^k}
]
for every admissible graph and every degree-one element.

## 5. The actual remaining theorem

The research question has now reduced to a precise statement:

> **Finite nonlinear orientation-factorization theorem (candidate).**
> On an explicitly orientation-rigid admissible class, the canonical orientation modulo (p^k) factors naturally through the adjacent finite extension-action object (mathcal C_q(O_q)).

The necessary admissible-class restriction cannot be omitted. The same-window counterexample with an isolated special vertex proves that an un-oriented finite window cannot determine the canonical orientation on the unrestricted specially oriented class.

A natural restricted class is:
[
(mathrm{OR})qquad
	ext{every special vertex is the terminus of at least one special edge}.
]
This is a genuine restriction and is consistent with the literature's description of specially oriented graphs; it is **not** yet a sufficiency theorem for finite-window orientation recovery. citeturn3search0turn3search1

## 6. Minimality boundary

The candidate is minimal only in a **relative** sense:

- D1 depth data is too coarse because it identifies nonzero scalar multiples.
- The first coefficient incidence quotient is too coarse because its kernel can carry nonzero orientation mass.
- The full multiplicative conjugation action is the first surviving object that retains the group law responsible for the q-correction.

Absolute minimality among all possible finite invariants is **not established and is not claimed**.

## 7. Final classification

- nonlinear extension-action object: **PASS / LOCAL**;
- definition-level pre-check: **PASS / LOCAL**;
- scalar information lost by D1: **restored locally**;
- first coefficient quotient no-go: **unchanged, FAIL / CLOSED**;
- full extension no-go: **not proved**;
- unrestricted orientation recovery from bare finite window: **FAIL / CLOSED**;
- orientation-rigid restricted class: **OPEN / LOAD-BEARING**;
- finite nonlinear orientation factorization: **OPEN / LOAD-BEARING**;
- absolute minimality: **OPEN / NOT AUTHORIZED**.

## 8. Next authorized action

Do not search for another carrier.

The next and only authorized proof attack is to formalize the orientation bridge for (mathcal C_q(O_q)): characterize, intrinsically from the finite conjugation action, the degree-one elements whose local action has the special factor (1+q), then prove that these local values glue to a single linear character modulo (p^k).

The proof must explicitly handle:
1. mixed degree-one elements;
2. overlapping special sinks;
3. separated sinks;
4. lower-filtration contamination;
5. the chordal-tree model;
6. the orientation-rigid restriction (OR).

If the full-action kernel contains nonzero orientation mass, classify **FAIL / CLOSED** and stop this branch. If the local factors glue uniquely, classify **PASS / LOCAL** first; a theorem-level PASS requires a separate literature/non-reencoding audit.


## 2026-10-02 — D3 DEFINITIONAL CORRECTION: RAW ORIGIN-LIFT SUBGROUP IS NOT NORMAL

A definition-level audit of the proposed D3 object found a genuine flaw that must control the branch before any orientation-bridge computation.

The previous object used the subgroup generated by the complete lift-fibres of the intrinsic origin sector and then asserted a conjugation action of the whole extension group (Y) on that subgroup. In general that subgroup is **not normal in (Y)**, so a global conjugation action (Y\curvearrowright\widehat O) is not defined.

Decisive control: the chordal-tree model with ordinary origins (a,b) and special vertices (s,t,u), with special edges (a\to s, b\to t, a\to u, b\to u). Let (H=\langle a,b\rangle\le Y). There is no defining relation between (t) and (a). Quotienting by the normal closure of (b,s,u) gives the free pro-(p) group on (a,t). Hence (tat^{-1}\notin\langle a\rangle), and therefore (tat^{-1}\notin H). Thus (H) is not normal in (Y).

Consequently the statement “the full conjugation action of (Y) on the origin-lift subgroup” is **not a valid object as written**. The prior D3 object-level PASS is superseded.

The minimal canonical repair is to replace the raw origin-lift subgroup by its **normal closure** in (Y), or equivalently to formulate the datum as the conjugation action on the normal closure of the origin sector. This repaired object is materially richer and may risk re-encoding more of the finite window; it therefore requires a fresh full pre-check before any computation.

Classification:
- raw origin-lift subgroup with (Y)-conjugation action: **FAIL / CLOSED**;
- previous D3 object-level PASS: **HISTORICAL / SUPERSEDED**;
- normal-closure conjugation object: **OPEN / LOAD-BEARING**;
- orientation bridge: **NOT YET AUTHORIZED** until the repaired object passes Object/Input/Functoriality/Gauge/Orientation-bridge/q-blindness/Separation/Novelty/Stop.

This is a definition correction, not a carrier hunt. The next authorized step is the fresh pre-check of the normal-closure repair, followed only if it passes by the mixed/chordal orientation-bridge test.


## 2026-10-02 — D3 REPAIRED-OBJECT PRE-CHECK: NORMAL CLOSURE PASSES OBJECT-LEVEL TEST, BUT ORIENTATION BRIDGE IS NOT FINITE/INTRINSICALLY SPECIFIED

The canonical repair was audited before any new computation.

Define (N_O) as the normal closure in (Y) of the preimage of the intrinsic origin sector (O_q). Then (N_O\triangleleft Y), so the conjugation action (Y\to\operatorname{Aut}(N_O)) is well-defined. The repaired package
[
\mathcal C_q^{\mathrm{nc}}=(Y,X,A_q,O_q,N_O,\operatorname{conj}_Y|_{N_O})
]
is intrinsic, functorial, lift/section-independent, and q-blind at the definition level.

However, the required orientation bridge still fails the mandatory pre-check in its present form: no canonical finite quotient of the action (Y\to\operatorname{Aut}(N_O)) has been exhibited whose scalar character is (omega_q\bmod p^k). Taking the action on (N_O) itself is not a bridge; it merely retains a large nonabelian object. Taking its obvious q-layer linearization collapses back to the already closed coefficient/incidence package. Using the literature's Kummerian criterion would be circular/re-encoding for the present finite-window program, because the criterion quantifies over all (n\ge1) and supplies the orientation as part of the oriented pair rather than extracting it from one finite window.

Independent literature control: Blumer–Quadrelli–Weigel prove that for an oriented pro-(p) RAAG there is a torsion-free Kummerian orientation exactly in the specially oriented case, and that this orientation is unique; their local locally-uniform argument likewise determines the canonical orientation from the full 2-generator group structure. This validates the *global mechanism* but does not furnish the required finite-window factorization. citeturn7search1turn4search0

Therefore no orientation-bridge computation is logically authorized from the repaired object yet. A further computation would be another carrier hunt unless a specific finite scalar quotient/action character is first derived non-tautologically from the repaired package.

Classification:
- raw origin-lift conjugation object: **FAIL / CLOSED**;
- normal-closure conjugation package: **PASS / LOCAL** at Object/Input/Functoriality/Gauge/q-blindness;
- finite orientation bridge from the repaired package: **OPEN / LOAD-BEARING**;
- finite-window factorization theorem: **OPEN**;
- absolute minimality: **OPEN / NOT AUTHORIZED**;
- unrestricted class: **FAIL / CLOSED** by the isolated-special same-window obstruction.

**Stop condition reached:** do not perform another blind computation. The next legitimate move is target-first derivation of a *specific finite scalar character* of the normal-closure action, with a full pre-check. If no such character can be defined without reintroducing the orientation or q, D3 closes as a finite-carrier realization failure while the negative Gate-D theorem remains a principal result.


---

# SOURCE: research/PAPER4_E1_KZ_RELATION_DEFECT_AUDIT_2026-10-02.md

<!-- blob-sha: b43ca3e0487677626d059f97fea93c2f26b57fbd -->

# PAPER 4 — GATE E1: K–Z RELATION DEFECT AUDIT — 2026-10-02

For G_s=<x,y,z | z^(p^s)=[x,y]>, N_s=cl(<z>) and D=G_s/N_s ~= Z_p^2, Palaisti's relation defect is the coinvariant class of the lifted D-relator in W_s=N_s/Phi(N_s).

The lifted relator is w=[x,y]=z^(p^s). Since Phi(N_s)=N_s^p[N_s,N_s] and z^(p^s) is a p-power in N_s for s>=1, w belongs to Phi(N_s). Therefore

delta_{G_s}=0 in (W_s)_D.

This is gauge-robust: the allowed scalar normalization of the transgression cannot change zero to nonzero.

Classification:
- E1 computation delta_{G_s}=0: PASS / CLOSED.
- delta_G as carrier of the K–Z deep-tail parameter s: FAIL / CLOSED.
- bridge deep correction <-> Palaisti delta_G: FAIL / CLOSED.
- filtered/p-adic/higher relation-module successor: OPEN / LOAD-BEARING.
- matched cd=3 control: OPEN, but not authorized yet.

The key boundary is that the K–Z correction survives in the ambient group but is annihilated at the first Frattini quotient. Literature confirms that Zassenhaus-filtered relation modules and initial-form methods are legitimate objects for pro-p presentations, but this does not yet establish finite-window factorization.

Next authorized task: fresh pre-check of the smallest filtered relation object retaining the p-power tail without simply re-encoding the presentation; only if it survives intrinsicity, gauge, finite-window and non-reencoding tests may the cd=3 matched-control search resume.

---

# SOURCE: research/PAPER4_E2_FILTERED_RELATION_MODULE_PRECHECK_2026-10-02.md

<!-- blob-sha: cfe30ee0b257935cc3a335a031e59f239905d269 -->

# PAPER 4 — GATE E2: FILTERED RELATION-MODULE PRE-CHECK — 2026-10-02

Candidate: replace the mod-p defect W_D by a p-adic/Zassenhaus-filtered relation object before attempting a matched cd=3 control.

For D ~= Z_p^2 with free presentation F(x,y) -> D and relator r=[x,y], the K-Z lift sends r to z^(p^s). At the presentation level, Fox differentiation of z^(p^s)[x,y]^{-1}, followed by evaluation in D, contains the coefficient p^s in the z-column. Thus the filtered/p-adic relation data can in principle retain the depth parameter that W=N/Phi(N) destroys.

Literature confirms that pro-p relation modules admit Zassenhaus filtrations and that initial forms/Fox data are standard. This is only a legitimacy check, not a finite-window theorem.

Pre-check:
- Object: filtered relation module / p-adic transgression datum — PASS / LOCAL as a legitimate candidate.
- Input: full extension plus quotient presentation — currently too much input for the finite-window problem; OPEN.
- Functoriality: relation-module constructions are natural under suitable presentation morphisms, but the exact extension class here needs a dedicated gauge proof — OPEN.
- Gauge: relator inversion/unit scaling preserves p-adic valuation, but lift changes are not yet controlled — OPEN / LOAD-BEARING.
- Orientation bridge: not specified — OPEN.
- q-blindness: candidate definition need not insert q — PASS / LOCAL.
- Separation: presentation-level p^s signal exists — PASS / LOCAL; intrinsic finite-window separation not established.
- Novelty: filtered relation modules are prior methodology; only a new finite-window factorization would be novel — CONDITIONAL.
- Stop: because gauge and finite-window factorization are unresolved, no carrier computation or matched cd=3 search is authorized.

Conclusion: E2 remains OPEN / LOAD-BEARING, not PASS. The project should not claim that the p-adic coefficient p^s is already an intrinsic finite-window invariant. The next decisive test is lift-independence of the p-adic extension class, followed by whether any finite Zassenhaus window can recover its first nonzero p-adic valuation without re-encoding the presentation.


---

# SOURCE: research/PAPER4_E2_P_ADIC_EXTENSION_CLASS_AUDIT_2026-10-02.md

<!-- blob-sha: 2d9f856a90dc49c60141e566cd77b073f1f0bcde -->

# PAPER 4 — GATE E2: P-ADIC EXTENSION CLASS ON K–Z — 2026-10-02

The filtered candidate can be sharpened before any finite-window computation.

Let M=(N_s^ab)_D. The extension induces an abelianized extension and a p-adic transgression class epsilon_s in the D-coinvariant relation data. Unlike delta_G in W_s=N_s/Phi(N_s), this object is not killed merely because the lifted relator is a p-power.

For K–Z, N_s is normally generated by z, so M is cyclic as a Z_p-module. The five-term homology sequence gives 0 -> H_2(G_s,Z_p) -> H_2(D,Z_p) -> M -> H_1(G_s,Z_p) -> H_1(D,Z_p) -> 0.

Using the K–Z amalgam decomposition G_s = <z> *_{<t>} F(x,y), the map from the amalgamating Z_p into H_1(<z>) is multiplication by p^s, hence injective. Mayer–Vietoris therefore gives H_2(G_s,Z_p)=0.

Also G_s^ab ~= Z_p^2 direct sum Z/p^s, while D^ab ~= Z_p^2. Hence the kernel of H_1(G_s,Z_p) -> H_1(D,Z_p) is Z/p^s.

Consequently 0 -> Z_p -> M -> Z/p^s -> 0. Because M is cyclic and contains an injected copy of Z_p, M ~= Z_p. The image epsilon_s of a generator of H_2(D,Z_p) therefore has exact p-adic valuation s, up to multiplication by a p-adic unit.

This is a genuine structural improvement over E1: the first-Frattini defect is zero, but the p-adic extension class retains the K–Z tail depth exactly at the full-extension level.

Classification:
- p-adic extension class as full-extension object: PASS / LOCAL.
- exact K–Z valuation v_p(epsilon_s)=s: PASS / LOCAL.
- finite Zassenhaus-window factorization of epsilon_s: OPEN / LOAD-BEARING.
- presentation-independent finite-window detector: OPEN.
- matched cd=3 search: NOT YET AUTHORIZED.

The remaining bottleneck is sharply isolated: prove or refute that epsilon_s modulo p^m, or an equivalent finite truncation, factors through a finite Zassenhaus window of G_s. The current result is not such a factorization theorem.


---

# SOURCE: research/PAPER4_E2_QPOS_HOMOLOGY_CORRECTION_2026-10-02.md

<!-- blob-sha: b17ad7e8ceaebe219a452a1f6cae2c858829bb5b -->

# PAPER 4 — E2 q>0 HOMOLOGICAL CARRIER CORRECTION — 2026-10-02

## Critical correction

The previous gate treated q>0 as if the q=0 E2 transgression source H_2(D,Z_p) remained available. That is not correct.

For an infinite Demushkin group with q=p^a>0 and standard odd-p relation
r_D=x_1^{p^a}[x_1,x_2]...[x_{d-1},x_d],
the one-relator Fox/cellular boundary after tensoring with the trivial Z_p-module is the exponent-sum vector
(p^a,0,...,0). Multiplication by p^a on Z_p is injective. Hence
H_2(D,Z_p)=0.
For q=0 the exponent-sum vector is zero and the same calculation gives H_2(D,Z_p)≅Z_p.

Therefore the E2 transgression class
H_2(D,Z_p) -> (N^{ab})_D
that carried the K–Z q=0 depth signal has no nonzero source in q>0.

## Intrinsic abelian extension check

For the stress presentation
G_{s,a}=<z,x_1,...,x_d | z^{p^s}=r_D>,
the abelianized relation is
p^s z=p^a x_1.
The quotient map G_{s,a}->D induces a surjection on H_1. Its kernel contains the free rank-one z-direction; the untwisted five-term sequence now starts with H_2(D,Z_p)=0, so
(N^{ab})_D -> ker(H_1(G)->H_1(D))
is an isomorphism.

The resulting short exact sequence of Z_p-modules
0 -> Z_p -> H_1(G) -> H_1(D) -> 0
is classified on the torsion summand by an Ext^1 class in
Ext^1_Zp(Z/p^a,Z_p) ≅ Z/p^a.
The relation p^s z=p^a x_1 represents the class p^s mod p^a (up to sign/unit convention). Hence for s>=a the abelian homological extension class is already zero and cannot distinguish s>a.

This is stronger than the earlier statement 'abelianization saturates': the entire untwisted H_1/coinvariant extension layer is saturated at q-depth a.

## Consequence

The previous 'q>0 higher filtered E2' target must be split:

- untwisted E2 homological/transgression object: **FAIL / CLOSED for s>a**;
- pure abelianization detector: **FAIL / CLOSED**;
- abelian H_1-extension class: **FAIL / CLOSED for s>a**;
- BBG-type gauge warning: **PASS / LOCAL stress control only**;
- genuinely nonabelian higher relation data: **OPEN / LOAD-BEARING**;
- twisted/dualizing-coefficient replacement: **OPEN / NOT YET DEFINED**, but it is a different object and cannot be called E2 continuation without a new pre-check;
- finite-window factorization of a new nonabelian object: **OPEN**.

## Methodological consequence

Do NOT continue searching for a 'higher filtered truncation of E2' in the untwisted Z_p homology. That route is structurally exhausted for q>0 beyond a.

The only legitimate successor is a genuinely nonabelian relation object (e.g. relation-module/Magnus/Zassenhaus layer) whose definition is intrinsic and whose finite-window factorization is proved. A twisted coefficient construction may be investigated separately, but it must first pass Object/Input/Gauge/q-blindness and must not smuggle the quotient orientation into the input.

## Sources

Demushkin standard q>0 relations and orientation: Labute classification / Souza–Zalesskii 2026.
Pro-p Fox/relation-module calculus: NSW-style relation module and Fox derivative framework.
PD^2 dualizing-module framework: Ben-Bassat–Gropper 2026.


---

# SOURCE: research/PAPER4_F1_KZ_ADAPTIVE_THRESHOLD_AUDIT_2026-10-02.md

<!-- blob-sha: f367ffafeb57011f67767a099da85884e6825b47 -->

# PAPER 4 — F1 ADAPTIVE THRESHOLD ON THE K–Z FAMILY — 2026-10-02

## Result

The K–Z family does not merely give a negative fixed-depth example. Its abelianization gives an explicit positive adaptive bound for the p-adic valuation truncation.

Let
\[
G_s^{ab}\simeq \mathbf Z_p^2\oplus \mathbf Z/p^s.
\]
For the Zassenhaus quotient
\[
Q_n^{(s)}=G_s/D_n(G_s),
\]
functoriality gives
\[
(Q_n^{(s)})^{ab}
\simeq
G_s^{ab}/D_n(G_s^{ab}).
\]

Since \(G_s^{ab}\) is abelian, if \(e=\lceil\log_p n\rceil\), then
\[
D_n(G_s^{ab})=(G_s^{ab})^{p^e},
\]
and hence
\[
(Q_n^{(s)})^{ab}
\simeq
(\mathbf Z/p^e)^2\oplus\mathbf Z/p^{\min(s,e)}.
\]

Take
\[
n=p^m.
\]
Then \(e=m\), so the torsion exponent in the finite-window abelianization is exactly
\[
p^{\min(s,m)}.
\]
Therefore the intrinsic quantity
\[
\tau_m(Q_{p^m})
:=
\min\{s,m\}
\]
is recoverable from the finite quotient itself.

Because E2 gives \(v_p(\epsilon_s)=s\), this recovers the truncated valuation
\[
\min(v_p(\epsilon_s),m).
\]
Equivalently, it determines whether \(\epsilon_s\equiv0\pmod{p^m}\), and if nonzero, determines its exact valuation below \(m\).

The calculation uses only intrinsic finite-group data (the abelianization and its exponent), not the presentation parameter \(s\).

## Sharpness within the K–Z family

The previous same-window lemma shows that a depth \(n\) cannot uniformly recover \(\epsilon_s\bmod p^m\) across all \(s\) if there exist
\[
s<t<m,qquad p^s\ge n.
\]
Thus any universal K–Z-family threshold for \(m\)-digit valuation information must satisfy, up to the integer boundary,
\[
n>p^{m-1}
\]
when \(m\ge2\).

The explicit construction \(n=p^m\) therefore gives the correct exponential scale, although this audit does not prove that \(p^m\) is the absolutely minimal threshold.

## Classification

- adaptive K–Z valuation recovery from a finite window: **PASS / LOCAL**;
- explicit intrinsic realization via \((G/D_{p^m}(G))^{ab}\): **PASS / LOCAL**;
- lower-bound scale \(n>p^{m-1}\) for uniform K–Z-family valuation recovery: **PASS / LOCAL**;
- exact minimal threshold \(n=p^{m-1}+1\) or similar: **OPEN**;
- general free-by-Demushkin finite-window factorization: **OPEN / LOAD-BEARING**;
- orientation recovery from the E2 class: **OPEN**.

This positive result prevents overclaiming the preceding F1 no-go: the K–Z family kills a fixed-depth/uniform-in-extension-depth detector, but it does not kill an \(m\)-dependent finite-window factorization.


---

# SOURCE: research/PAPER4_F1_KZ_SAME_WINDOW_P_ADIC_NO_GO_AUDIT_2026-10-02.md

<!-- blob-sha: 547486e95f187a46a0c06ef4833553ae32b42c41 -->

# PAPER 4 — F1 FINITE-WINDOW FACTORIZATION STRESS TEST FOR THE K–Z p-ADIC EXTENSION CLASS — 2026-10-02

## 1. Target

For the K–Z family
\[
G_s=\langle x,y,z\mid z^{p^s}=[x,y]\rangle,
\qquad
N_s=\overline{\langle z\rangle}^{G_s},
\qquad
D\simeq \mathbf Z_p^2,
\]
E2 gives a full-extension p-adic transgression class \(\epsilon_s\) whose valuation is
\[
v_p(\epsilon_s)=s
\]
up to the unit ambiguity from the choice of generator of \(H_2(D,\mathbf Z_p)\).

The F1 question is whether a finite Zassenhaus window can determine finite truncations of this class.

## 2. Pre-check

- **Object:** finite truncation \(\epsilon_s\bmod p^m\), with intrinsic content at least its valuation when nonzero.
- **Input:** the bare finite Zassenhaus quotient \(G/D_n(G)\); no presentation, lift, or hidden parameter \(s\).
- **Functoriality:** the quotient is functorial under pro-p homomorphisms preserving the filtration.
- **Gauge:** the scalar representative is only defined up to a \(\mathbf Z_p^\times\)-unit; valuation is the invariant tested here.
- **Orientation bridge:** none is assumed. This is a test of the E2 extension object itself.
- **q-blindness:** the K–Z family has fixed quotient \(D\simeq\mathbf Z_p^2\); no q-parameter is inserted.
- **Separation:** test whether distinct \(s\) can have the same finite window but different \(\epsilon_s\bmod p^m\).
- **Novelty:** this is not a new homological calculation; the possible new content is the finite-window non-factorization boundary.
- **Stop:** if the same finite window supports different E2 valuations, factorization at that depth is impossible.

## 3. Exact same-window lemma

Let \(F=F(x,y,z)\) be the free pro-p group and let \(D_n(F)\) be its Zassenhaus filtration. For
\[
r_s=z^{p^s}[x,y]^{-1},
\qquad
G_s=F/\overline{\langle\!\langle r_s\rangle\!\rangle},
\]
functoriality gives
\[
D_n(G_s)=D_n(F)\,\overline{\langle\!\langle r_s\rangle\!\rangle}/\overline{\langle\!\langle r_s\rangle\!\rangle}.
\]
If \(p^s\ge n\), then
\[
z^{p^s}\in D_{p^s}(F)\subseteq D_n(F).
\]
Therefore, modulo \(D_n(F)\), the relator \(r_s\) reduces to \([x,y]^{-1}\). Hence
\[
\boxed{
G_s/D_n(G_s)
\cong
F/\bigl(D_n(F),[x,y]\bigr)
}
\qquad(p^s\ge n).
\]
In particular, for any \(s,t\) satisfying \(p^s\ge n\) and \(p^t\ge n\),
\[
\boxed{G_s/D_n(G_s)\cong G_t/D_n(G_t).}
\]

This is the correct K–Z same-window statement. It does **not** identify the quotient with \(\mathbf Z_p^3/D_n\); the surviving commutators \([x,z]\), \([y,z]\) remain, exactly as found in the earlier critical correction.

## 4. Separation of the E2 invariant

E2 independently gives
\[
v_p(\epsilon_s)=s.
\]
Thus for \(s\ne t\), the full-extension p-adic invariants have different valuations.

More strongly, if
\[
1\le s<t<m
\]
and \(p^s\ge n\), then
\[
\epsilon_s\not\equiv0\pmod{p^m},
\qquad
\epsilon_t\equiv0\pmod{p^m},
\]
up to the harmless unit ambiguity. Yet the same finite window occurs:
\[
G_s/D_n(G_s)\cong G_t/D_n(G_t).
\]

Therefore no map
\[
F_{n,m}\colon G/D_n(G)\longrightarrow
\text{(finite data determining }\epsilon_G\bmod p^m)
\]
can exist uniformly on the K–Z family at a fixed depth \(n\) whenever the family contains two such parameters \(s,t<m\) with \(p^s\ge n\).

Equivalently: **there is no uniform finite depth, independent of the hidden extension-depth parameter, that recovers the E2 p-adic class on the whole K–Z family.**

## 5. Exact logical boundary

This is deliberately weaker than the previously withdrawn cd=2/cd=3 matched-window theorem.

It proves:

- fixed-depth factorization uniformly across the K–Z family: **FAIL / CLOSED**;
- uniform bound \(n=n(p,d,m)\) for recovering \(\epsilon\bmod p^m\) across all such extensions: **FAIL / CLOSED**;
- a group-dependent depth \(n=n(G,m)\): **OPEN**;
- the possibility that \(n=p^m\) (or another relation-depth bound) suffices for this particular family: **OPEN**;
- a bare finite window canonically identifying the extension decomposition \(1\to N\to G\to D\to1\): **OPEN**;
- orientation recovery from the E2 object: **OPEN**.

The counterexample does not show that an individual \(G_s\) lacks a finite detecting window. Indeed, once the window reaches the relation depth, the tail may become visible.

## 6. Independent check against the withdrawn argument

The proof uses only the free presentation and functoriality of the Zassenhaus filtration. It never compares \(G_s\) with \(\mathbf Z_p^3\). Thus the earlier error involving surviving \([x,z]\) and \([y,z]\) cannot enter.

The correct conceptual picture is:

\[
\text{same finite window for all }s\text{ with }p^s\ge n
\quad\not\Rightarrow\quad
\text{same full extension class}.
\]

The deep-tail parameter is genuinely invisible to any fixed lower window, even though the ambient nonabelian quotient itself changes relative to the abelian control.

## 7. Consequence for Paper 4

E2 is now a genuine negative finite-window boundary, but not yet a full Paper-4 theorem about cd=3 or orientation.

The remaining load-bearing question is adaptive thresholding:
\[
\boxed{
\text{Can an intrinsic finite window of depth controlled by }m
\text{ recover }\epsilon\bmod p^m
\text{ for each individual extension?}
}
\]

No carrier computation is authorized before that question is answered. In particular, do not return to the withdrawn \(\mathbf Z_p^3\) matched pair.

## Classification

- E2 full-extension p-adic valuation \(v_p(\epsilon_s)=s\): **PASS / LOCAL**.
- K–Z same-window lemma for \(p^s\ge n\): **PASS / CLOSED**.
- uniform finite-depth factorization of E2 across the K–Z family: **FAIL / CLOSED**.
- group-dependent/adaptive finite-window factorization: **OPEN / LOAD-BEARING**.
- orientation recovery from E2: **OPEN**.
- previous K–Z vs \(\mathbf Z_p^3\) matched-window no-go: **HISTORICAL / SUPERSEDED**.



---

# SOURCE: research/PAPER4_F1_MINIMAL_THRESHOLD_AND_DEMUSHKIN_STRESS_AUDIT_2026-10-02.md

<!-- blob-sha: 5fb3648562d21fc88c10ad8403d962892b612578 -->

# PAPER 4 — F1 MINIMAL THRESHOLD AND STANDARD DEMUSHKIN EXTENSION TEST — 2026-10-02

## A. Exact K–Z threshold

For
\[
G_s^{ab}\simeq \mathbf Z_p^2\oplus\mathbf Z/p^s
\]
and \(Q_n=G_s/D_n(G_s)\), put \(e(n)=\lceil\log_p n\rceil\). Then
\[
Q_n^{ab}\simeq(\mathbf Z/p^{e(n)})^2\oplus
\mathbf Z/p^{\min(s,e(n))}.
\]

To recover \(\min(s,m)\) uniformly for all \(s\), one must have \(e(n)\ge m\). For \(m\ge2\), this is equivalent to
\[
n>p^{m-1}.
\]
Thus the exact smallest integer depth is
\[
\boxed{n_m^{\mathrm{KZ}}=p^{m-1}+1}.
\]

Sufficiency: at this depth \(e(n)=m\), so the finite abelianization recovers \(\min(s,m)\).

Necessity: if \(n\le p^{m-1}\), then \(e(n)\le m-1\), and the two parameters
\[
s=e(n),\qquad t=m
\]
have identical \(\min(s,e(n))=e(n)\), while \(\min(s,m)=e(n)\ne m=\min(t,m)\). Hence no invariant extracted solely from this abelianization can uniformly recover \(\min(s,m)\) at that depth. More strongly, the same-window lemma gives identical full Zassenhaus windows whenever \(p^s\ge n\), so for suitable \(s<t<m\) no full-window factorization can recover the m-truncation.

Boundary: \(m=1\) is trivial for the K–Z family with \(s\ge1\), since every \(\epsilon_s\) is divisible by \(p\).

## B. Standard higher-rank q=0 Demushkin stress model

For odd p and even \(d\ge4\), let
\[
D_d=\langle x_1,\ldots,x_d\mid
r_D=[x_1,x_2][x_3,x_4]\cdots[x_{d-1},x_d]\rangle,
\]
the standard q=0 Demushkin group. Consider the one-relator extension candidate
\[
\widetilde G_{s,d}
=
\langle z,x_1,\ldots,x_d
\mid
z^{p^s}=r_D
\rangle,
\]
with N the normal closure of z and quotient \(D_d\).

The initial Zassenhaus form of the defining relation is exactly the Demushkin quadratic relation \(r_D\). Since q=0 Demushkin groups are mild, the candidate presentation has the same quadratic initial form and is a natural mild test model; mildness gives cd_p \(\widetilde G_{s,d}=2\). However, a general theorem that this particular N is free pro-p is not being asserted here without an explicit kernel theorem. Therefore this is a **stress model for the homological mechanism, not yet a certified free-by-Demushkin example**.

Its abelianization is nevertheless immediate:
\[
\widetilde G_{s,d}^{ab}
\simeq
\mathbf Z_p^d\oplus\mathbf Z/p^s.
\]
Thus the same finite-window calculation yields
\[
(\widetilde G_{s,d}/D_{p^m})^{ab}
\simeq
(\mathbf Z/p^m)^d\oplus\mathbf Z/p^{\min(s,m)}.
\]

So the K–Z adaptive abelianization mechanism is not rank-2-specific: it persists for the standard q=0 Demushkin relation at the level of this one-relator extension model.

## C. q != 0 boundary

For a standard Demushkin quotient with finite torsion invariant \(q=p^a\), the defining relation has an abelianized \(p^a x_1\) component. Replacing it by
\[
z^{p^s}=r_D
\]
gives, at the abelianized level, one relation
\[
p^s z=p^a x_1.
\]
Smith normal form therefore produces a torsion factor of order
\[
p^{\min(a,s)}
\]
rather than \(p^s\).

Hence the simple abelianization detector saturates at the quotient's own Demushkin q-invariant. It cannot recover arbitrarily deep extension depth once \(s>a\).

This is a genuine structural warning: the K–Z/q=0 mechanism is not a universal abelianization theorem. For q>0, higher nonabelian/filtered relation data would be required to see the tail beyond the intrinsic quotient torsion.

## D. Current frontier

- exact K–Z minimal valuation threshold \(p^{m-1}+1\): **PASS / CLOSED**;
- q=0 higher-rank standard-relation stress model: **PASS / LOCAL** at abelianized homological level;
- certification that the stress model's kernel N is free: **OPEN**;
- q>0 abelianization saturation at \(\min(a,s)\): **PASS / LOCAL**;
- general free-by-Demushkin finite-window recovery of extension depth: **OPEN / LOAD-BEARING**;
- general finite scalar character beyond abelianization: **OPEN**;
- E2 -> orientation: **OPEN**.

## E. Stop / next authorized test

Do not claim a general theorem from the stress model. The next decisive test is kernel certification for \(\widetilde G_{s,d}\), or alternatively an independently sourced free-by-Demushkin family with q>0 and variable extension depth. If the kernel is certified free and q>0 still exhibits saturation, then the program obtains a genuine positive/negative dichotomy:
q=0: abelianization may detect arbitrary depth;
q>0: abelianization alone cannot.



---

# SOURCE: research/PAPER4_GATE_D_SAME_WINDOW_DIFFERENT_ORIENTATION_AUDIT_2026-10-02.md

<!-- blob-sha: 6d853f6813c65f78421a23233e2c7f980c4c81c0 -->

# PAPER 4 GATE D — SAME-WINDOW / DIFFERENT-ORIENTATION COUNTEREXAMPLE — 2026-10-02

## Decision

Gate D is **FAIL / CLOSED** for the current admissible class of specially oriented pro-p RAAGs if the finite input is the un-oriented adjacent Zassenhaus window
[
W_q(G)\leftarrow W_{q+1}(G),
]
because the class contains isolated vertices whose ordinary/special status changes the canonical orientation without changing the underlying pro-p group at all.

This is stronger than a same-window counterexample: the two oriented objects have the **same underlying group**, hence identical (W_n) for every (n), but different canonical orientations.

## 1. Literature-controlled construction

The definition of oriented pro-ℓ RAAGs permits a vertex to be special when it is isolated or is the terminus of a special edge. In particular, the source explicitly gives two oriented graphs on the same isolated vertices with identical geometric realization, one declaring a vertex ordinary and the other declaring it special (Remark 2.4). A specially oriented graph requires only that the terminus of every special edge be special, so an isolated special vertex is allowed.

For a linear orientation λ, the canonical orientation is
[
\theta_{\Gamma,\lambda}(v)=1 quad(v\in V^o),
qquad
\theta_{\Gamma,\lambda}(v)=\lambda(1) quad(v\in V^s).
]
These are definition-level statements in Blumer–Quadrelli–Weigel.

## 2. Counterexample with nontrivial q-layer retained

To avoid the objection that a completely edgeless graph does not exhibit a visible q-defect, fix any nontrivial specially oriented graph Γ_0 containing at least one special edge, with (q=p^f) and
[
\lambda(1)=1+q.
]
Let (z) be a new isolated vertex and form two disjoint unions:
[
\Gamma_A=\Gamma_0\sqcup\{z\}_{\mathrm{ordinary}},
qquad
\Gamma_B=\Gamma_0\sqcup\{z\}_{\mathrm{special}}.
]
Both are specially oriented; if Γ_0 is chordal, both are chordal as well.

Crucially, the presentation relation contributed by (z) is empty in either case. Therefore
[
G_{\Gamma_A,\lambda}=G_{\Gamma_B,\lambda}
\cong G_{\Gamma_0,\lambda}\;\widehat{*}\;\mathbf Z_p
]
as **un-oriented pro-p groups**.

Hence, for every (n),
[
W_n(\Gamma_A)\cong W_n(\Gamma_B),
]
and in fact the filtered groups can be identified through the identity on the common underlying group. In particular the adjacent windows at the q-jump are identical:
[
W_q(\Gamma_A)\leftarrow W_{q+1}(\Gamma_A)
=
W_q(\Gamma_B)\leftarrow W_{q+1}(\Gamma_B).
]

## 3. Orientation discrepancy

On the common subgroup (G_{\Gamma_0,\lambda}), the canonical orientations agree. On the isolated factor generated by (z),
[
\theta_A(z)=1,
qquad
\theta_B(z)=1+q.
]
Modulo (p^k), with (q=p^{k-1}),
[
1+q\not\equiv1\pmod{p^k}.
]
Thus
[
[\theta_A\bmod p^k]\ne[\theta_B\bmod p^k].
]

At the degree-one level, if (\bar z\) denotes the isolated direction, the induced orientation functional differs by
[
\omega_A(\bar z)=0,
qquad
\omega_B(\bar z)=1
]
after the usual normalization (\lambda(1)=1+p^{k-1}).

Therefore the same un-oriented finite adjacent window supports two distinct orientation targets.

## 4. Why this is a genuine Gate D no-go

This is not a failure of the proposed affine-hull observable, and it is not a carrier-specific failure.

The counterexample has:

- **same Object:** the underlying pro-p group is literally the same;
- **same Input:** every finite Zassenhaus window is the same;
- **same Functoriality:** the identity identifies the filtered objects;
- **different Target:** the canonical orientations differ;
- **no Gauge rescue:** this is not a presentation or lift change; the ordinary/special status of (z) is part of the oriented structure;
- **q-blindness is irrelevant to the obstruction:** even an arbitrarily sophisticated functor of the complete un-oriented filtered group cannot distinguish the two targets;
- **Separation is exact:** the two targets differ already on the isolated degree-one direction (z);
- **Novelty boundary:** the negative result is a class-level observability obstruction, not a failed carrier;
- **Stop:** no further carrier search can repair the statement on this admissible class.

## 5. Relation to the earlier T1 work

The recent T1 affine-hull failure remains valid but is now demoted from the primary obstruction to a **secondary realization failure**.

The decisive hierarchy is:

[
\text{Gate D fails}
\Longrightarrow
\text{no }W_q\text{-only carrier can recover orientation on the current class}
\Longrightarrow
\text{T1 carrier construction is impossible without extra input}.
]

Thus the failure of the affine-hull construction was not the deepest obstruction. The deeper obstruction is that the target orientation is not a function of the declared un-oriented finite input on the current class.

## 6. Exact boundary

The result does **not** say that finite-window orientation recovery is impossible for every restricted class.

It says:

[
\boxed{
\text{For specially oriented pro-p RAAGs allowing isolated special vertices,}
\quad
W_q\leftarrow W_{q+1}
\not\Rightarrow
\theta\bmod p^k.
}
]

A positive Paper 4 theorem can therefore only survive after adding a rigidity hypothesis that makes the ordinary/special status of isolated directions observable from the declared input, or after changing the input to include the missing orientation marking.

The most natural restriction is to require every special vertex to be the terminus of at least one special edge. That restriction is **not yet proved sufficient**; it is a new admissibility boundary, not a rescue theorem.

## Classification

**Gate D: FAIL / CLOSED — current specially oriented RAAG class.**

- same underlying group: PASS / decisive;
- same finite windows: PASS / decisive;
- different canonical orientation mod (p^k): PASS / decisive;
- class-level no-go for un-oriented finite-window carriers: PASS / CLOSED;
- restricted class with no isolated special vertices: OPEN;
- Paper 4 general finite-window orientation theorem: OPEN only after redefining the admissible class/input.

## Source

Blumer, Quadrelli, Weigel, *Oriented right-angled Artin pro-ℓ groups and maximal pro-ℓ Galois groups*, especially the definition of oriented graphs/RAAGs and Remark 2.4 / Definition 2.5 / the canonical orientation definition. 


---

# SOURCE: research/PAPER4_GATE_T_GENERAL_PROOF_CLAIM_AUDIT_2026-10-03.md

<!-- blob-sha: 19312712b60ff8e31cdd764814bd480b0d10e9ec -->

# GATE T — GENERALIZATION CLAIM / INDEPENDENT REVIEW REQUIRED — 2026-10-03

## Reported new result

A new hand proof is reported for the relative relation-window threshold in the stress family, extending to general odd prime p, a>=1, and even rank d>=2:
n_sep^rel(s)=p^s+1.

The reported proof replaces the earlier generator-by-generator survival argument with an explicit test group E'. In E', z has order p^(s+1), y acts on z by u=1-q with q=p^a, and the defining relation is realized as z^(p^s)=r. The claimed consequences are:
1. no choice of lift can make r trivial, hence the pushed-out finite extension is nonsplit;
2. z^(p^s) has exact Zassenhaus depth p^s, so it survives at depth p^s+1;
3. nonsplitting descends back to the original marked extension by quotient/pushout naturality;
4. higher even rank is reduced by sending extra Demushkin generators to 1.

GAP cross-checks are reported for 10 cases with p=3,5,7 and s<=4, including the previously unresolved s=3,n=28 boundary, and agree with earlier direct W computations.

## Correction from critical review (2026-10-03)

The following points are now explicitly corrected in this audit.

1. The suggestion that exact depth of z^(p^s) can be proved by a cyclic quotient is **withdrawn**. In the proposed E', the relation [z,y]=z^(-q) puts z^q in the commutator subgroup; when a<=s, z^(p^s) dies in the abelianization. Hence there need not be a cyclic quotient in which z has order p^(s+1). The exact-depth step must instead be established by the filtered-algebra calculation used in the proof, with its coefficient ring and filtration stated precisely.
2. The proof's use of F_p[[E']] must not be conflated with the Z_p[[G]] I-adic filtration. The relevant standard identification is the mod-p completed group-algebra augmentation filtration for the p-Zassenhaus series; the proof should name the exact theorem rather than saying vaguely “I-adic = normal-word degree.”
3. The concrete E' construction and the calculation phi(r)=z^(p^s) are reported to be present in the proof note. They still need line-by-line verification, but their absence is no longer an identified gap.
4. A Q-equivariance requirement is unnecessary. It is enough to exhibit the stated surjective homomorphism Psi and the commutative diagram with D, and then prove the extension/nonsplitting implication.
5. The lift-independence calculation is reported complete: since ker(E' -> D)=<z>, lifts differ by z-powers (z^i x, z^j y), so the section obstruction must be checked against exactly those changes.
6. The d>=4 reduction is not justified by the false general slogan “a split extension remains split under every quotient.” The actual proof uses the fact that the extra generators map into the abelian kernel <z>, so their mutual commutators become trivial. That specific argument is the one to audit.

## Current classification before independent proof audit

- Reported general relative threshold: CONDITIONAL / pending independent proof audit.
- Computational cross-checks: PASS / LOCAL.
- Orientation recovery: OPEN; the result separates s with a fixed a and does not by itself recover a or chi.
- p=2, q=0, s=0: OUT OF SCOPE.
- Unmarked/abstract-group realization: OPEN.
- Novelty: OPEN / literature audit required.

## Load-bearing proof point

The critical hand-proof step is the assertion that the relevant I-adic filtration agrees with the required normal/Zassenhaus word depth. This must be stated with the exact coefficient ring and filtration theorem used. No promotion to PASS/CLOSED is authorized until this identification, the construction of E', and the quotient/pushout implication are independently checked.

## Governance

Do not replace the older a=1 correction by this report merely because the claim is stronger. The older a=1 OPEN status remains authoritative until the new proof survives independent audit. If the proof closes the gap, supersede the older correction explicitly with a dated correction and preserve the historical record.

## Immediate next checks

1. Verify the exact definition and presentation of E'.
2. Verify the Q-equivariant quotient/pushout map from the original finite extension to E'.
3. Verify nonsplitting in E' by a lift-independent argument.
4. Verify exact Zassenhaus depth of z^(p^s), including the coefficient/filtration theorem.
5. Verify the d>=4 reduction.
6. Independently compare GAP cases, including p=3,s=3,a=1,n=28.
7. Perform novelty/literature search only after the theorem statement is fixed.
