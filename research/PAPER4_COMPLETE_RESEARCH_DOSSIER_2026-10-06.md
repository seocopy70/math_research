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


---

# CHRONOLOGICAL MASTER LOG

The complete repository research log is reproduced below so that the dossier preserves chronology as well as final audits.



## SOURCE: research/00_RESEARCH_LOG.md

<!-- blob-sha: 6894173bb3c0e14cb11f14cc003c5d2e4b23d011 -->

# Research Log — Active/Post-Paper-3 Chronology

> **Scope:** This chronological ledger is for active research after Papers 1–3 were frozen. Papers 1–3 historical provenance is indexed at `research/archive/PAPERS1-3_RESEARCH_HISTORY.md` and remains in their dated proof/audit records. Do not re-copy frozen Paper 1–3 history into this file.

## 2026-10-04 — TF_s literature review and subgroup-comparison correction

A direct re-check was performed after the transfer-defect reduction identified the load-bearing lemma
\[
(TF_s):\quad \operatorname{im}(D_{p^s+1}(F)\cap K\to K^{ab})\subseteq p^sK^{ab},
\]
with the proposed sufficient comparison
\[
(SC_s):\quad D_{p^s+1}(F)\cap K\subseteq D_{p^{s-1}+1}(K).
\]

### Direct-proof audit

1. The augmentation-ideal shortcut \(I_F^n\cap\mathbf F_p[K]=I_K^n\) is **FAIL / CLOSED**. The example \(F=\mathbf Z, K=p\mathbf Z\) gives \(t^p-1\in I_F^p\cap\mathbf F_p[K]\) but \(t^p-1\notin I_K^2\).
2. The stronger-looking inclusion \(D_n(F)\cap K\subseteq D_n(K)\) is also **FAIL / CLOSED** by the same example: \(D_2(F)\cap K\) contains \(t^p\), whereas \(t^p\notin D_2(K)\).
3. Jennings recursion does not close \((SC_s)\): writing an element of \(D_{p^s+1}(F)\cap K\) as a product involving a \(p\)-th power from \(D_{p^{s-1}+1}(F)\) does not imply that the preimage factor lies in K.

### Literature audit

Shalev's Proposition 1.2, as located in the cited 1990 literature, concerns identities built from the filtration of a **single group G**. It does not, on the currently verified evidence, state the required index-\(p\) intersection comparison \(D_{pn}(F)\cap K\subseteq D_n(K)\), nor its special case \((SC_s)\). The Shalev result therefore remains **PASS as a literature fact but NOT DIRECTLY APPLICABLE** to the missing bridge.

The Lazard product formula
\[
D_n(G)=\prod_{ip^j\ge n}\gamma_i(G)^{p^j}
\]
and the corresponding Jennings recursion remain **PASS**. Consequently, once \((SC_s)\) is supplied, the implication
\[
D_{p^s+1}(F)\cap K\subseteq D_{p^{s-1}+1}(K)
\Longrightarrow
\operatorname{im}(D_{p^s+1}(F)\cap K\to K^{ab})\subseteq p^sK^{ab}
\]
is valid.

### Classification

- augmentation-ideal intersection equality: **FAIL / CLOSED**;
- same-index Zassenhaus intersection inclusion: **FAIL / CLOSED**;
- Jennings-only proof of \((SC_s)\): **FAIL / CLOSED as an approach**;
- Shalev Proposition 1.2: **PASS / LOCAL, not directly applicable**;
- \((SC_s)\): **OPEN / LOAD-BEARING**;
- \((TF_s)\): **OPEN / LOAD-BEARING**;
- all-s transfer-defect separation: **OPEN / LOAD-BEARING**;
- Paper 4 final freeze: **BLOCKED** by this missing bridge (or an alternative direct proof of \((TF_s)\).

### Governance correction

An earlier 2026-10-04 log entry labeled the intrinsic transfer-defect boundary "CLOSED". That label is **superseded**. The verified status is only **PASS / LOCAL** for the \((p,s)=(3,2)\) witness and **OPEN / LOAD-BEARING** for the all-s theorem. No all-s claim is to be promoted from the local witness.

The most defensible fallback is now a **CONDITIONAL** Paper 4 statement: if \((SC_s)\) or directly \((TF_s)\) is certified, then the transfer-defect calculation closes the remaining a=s vs. a=∞ boundary.


## 2026-10-04 — Restricted-Lie TF_s proof audit: proposed induction rejected

A new proposed proof of
\[
(TF_s):\quad \operatorname{im}(D_{p^s+1}(F)\cap K\to K^{ab})\subseteq p^sK^{ab}
\]
was audited and is **NOT VALID**. The Paper 4 certified core remains closed, but this argument does **not** close the all-s boundary.

### Independent audit findings

1. **Wrong graded object / restricted structure.** The lower-central-series graded object \(\bigoplus_i\gamma_i(F)/\gamma_{i+1}(F)\) is the ordinary free Lie algebra in the free-group case; the standard free restricted Lie algebra belongs to the Zassenhaus/dimension filtration, not the lower-central grading used in the proposal. Thus the asserted restricted-Lie setup is not legitimate as stated.

2. **Ambient \(\gamma_i(F)\) versus \(\gamma_i(K)\) mismatch.** The target concerns \(c\in\gamma_i(F)\subseteq K\), but the induction actually controls images of \(\gamma_i(K)\) (or its associated graded pieces). These are not the same filtration. In particular \([z,x]\in\gamma_2(F)\cap K\) is generally a Schreier degree-1 generator for \(K\), not an element of \(\gamma_2(K)\). Hence the claimed generation of the relevant \(\gamma_i(F)\)-image by \([z,\mathcal L_{K,i-1}]\), \([x,\mathcal L_{K,i-1}]\), \([y,\mathcal L_{K,i-1}]\) is not a proof of the stated ambient-filtration bound.

3. **Base cases are not enough to repair the mismatch.** The explicit \(i=4,5\) computations may verify particular cyclic-commutator witnesses, but they do not establish the full image of \(\gamma_i(F)\cap K\to K^{ab}\).

4. **The Zassenhaus implication is not reversible in the way used.** From \(c\in\gamma_i(F)\) and \(c^{p^j}\in D_{p^s+1}(F)\), membership in \(D_{p^s+1}\) does not by itself force \(ip^j\ge p^s+1\); an element of \(\gamma_i(F)^{p^j}\) can have strictly larger Zassenhaus weight. The displayed proof therefore cannot use that implication as a general deduction.

5. **Therefore the central bound**
\[
\operatorname{im}(\gamma_i(F)\cap K\to K^{ab})\subseteq p^{\lceil i/p\rceil-1}K^{ab}
\]
remains **UNPROVEN**. The numerical cyclic examples are **PASS / LOCAL**, not an induction theorem.

### Classification

- restricted-Lie induction as written: **FAIL / CLOSED as a proof route**;
- proposed \(\gamma_i(F)\)-to-\(K^{ab}\) divisibility bound: **OPEN / LOAD-BEARING**;
- \((TF_s)\): **OPEN / LOAD-BEARING**;
- all-\(s\) transfer-defect separation: **OPEN / LOAD-BEARING**;
- Paper 4 certified core: **PASS / CLOSED**;
- Paper 4 all-\(s\) boundary: **OPEN**, so no FINAL/all-\(s\) promotion.

This entry supersedes any session-level claim that the restricted-Lie induction had proved \((TF_s)\). No all-\(s\) theorem is to be recorded from this argument.


## 2026-10-04 — s=3 model Schreier transfer witness

The remaining Paper 4 boundary (a=s) versus (a=\infty) was advanced by a bounded ((p,s)=(3,3)), (n=28) Schreier-lattice calculation. With the corrected intrinsic radical character \(\chi(z)=1,\chi(x)=\chi(y)=0\), the untruncated Schreier abelianization has relations \(9u-27a_i=0\). The critical model class
\[
9(\sigma-1)^2a_0=9a_0-18a_1+9a_2
\]
is not in the integral row lattice (SNF \(\operatorname{diag}(9,27,27)\)); hence the model class is nonzero. This extends the \(s=2\) local pattern to \(s=3\).

This is **PASS / LOCAL only**. It does not prove survival in the actual \(K^{ab}\) of \(W_{28}\), because the truncation image \(D_{28}(F)\cap K\to K^{ab}\) is still controlled by the unresolved subgroup-filtration comparison \((SC_s)\) (or a direct replacement). The next authorized attack is therefore the actual truncation image at \((p,s)=(3,3)\), not an all-\(s\) promotion.

Evidence: `research/PAPER4_S3_MODEL_SCHREIER_TRANSFER_2026-10-04.md`, commit `f423bc41f7d41023fdeaf5e8de657229118e338a`.


## 2026-10-04 — same-window order-jump correction / exact-threshold rollback

A direct audit of the previously “CLOSED” same-window order-jump argument found a fatal subgroup-containment error. The proposed canonical epimorphism
\[
W_{p^s+1}(G_s)\twoheadrightarrow W_{p^s+1}(G_t)
\]
was justified by treating the defining normal subgroups as nested, but
\(N_s=D_n\langle\!\langle z^{p^s}r^{-1}\rangle\!\rangle\) and
\(N_t=D_n\langle\!\langle r\rangle\!\rangle\) are not nested in the required direction because \(z^{p^s}\notin D_{p^s+1}\). Hence the claimed order jump \(|W_s|=p|W_t|\) is invalid.

A direct finite computation at the test case reported in the audit gives equal orders for the two compared windows, consistent with the structural objection. Therefore:

- “same-window order jump” = **FAIL / CLOSED as a proof route**;
- exact unmarked threshold \(n_{\mathrm{sep}}(s)=p^s+1\) = **OPEN**;
- certified lower bound \(n_{\mathrm{sep}}(s)\ge p^s+1\) = **PASS / CLOSED in the stated scope**;
- all-s same-window separation = **OPEN / LOAD-BEARING**;
- the existing \((p,s)=(3,2)\) and \((3,3)\) transfer calculations remain **PASS / LOCAL** only;
- a proof that \(G_s\not\cong G_t\) is also not currently certified and must not be inferred from the window calculation.

This supersedes the earlier evidence-index wording that promoted the exact threshold to CLOSED. It does not invalidate the certified Paper 4 core below this boundary.


## 2026-10-04 — decision: do not start the general E_ψ generator as a Paper 4 step

The proposed replacement of the Demuškin-specific test group E' by a universal twisted-character test family E_ψ is recognized as a potentially useful route toward a broader theorem, but it is **not authorized as the next Paper 4 computation**.

Reason: the current Paper 4 mathematical core is to be treated as complete in its certified scope, while the exact all-s boundary remains an explicitly OPEN/CONDITIONAL extension rather than a publication-blocking task. Building E_ψ would therefore reopen a broader general theorem whose legitimacy, intrinsic definition, and separation mechanism are not yet established. In particular, the existence of a twisted character ψ annihilating a Fox-derivative expression is not by itself a proof that a canonical finite test group E_ψ exists or that it yields n_sep=p^s+1.

Classification:
- Paper 4 certified core: **PASS / CLOSED**.
- all-s transfer-defect / exact-threshold boundary: **OPEN / intentionally left open**.
- universal E_ψ test-group construction: **OPEN / future generalization**, not a Paper 4 dependency.
- Direction 1 generator implementation: **DEFERRED**, not started.

Decision consequence: stop the new general-theorem branch here and move to Paper 4 organization/writing. If later reopened as a separate generalization program, the first task must be a pre-check defining E_ψ intrinsically and proving functoriality/gauge invariance before any large computation.


## 2026-10-04 — decision: bounded test-family generalization challenge

The certified Paper 4 core is mathematically real but judged too narrow relative to the original generalization ambition. A bounded **test-family generalization challenge** is therefore authorized before organization/writing.

This does not reopen the failed arbitrary-(r) degree-only theorem, the frozen core, or Paper 5 compression. The first broader family is
[
G_{s,a}(r_2)=langle z,x_1,ldots,x_dmid z^{p^s}=x_1^{p^a}r_2
angle,
qquad s>age2,
]
with odd (p) and a nonzero quadratic initial relation (r_2). The rank-two stress relation (r_2=[x_1,x_2]) is the control case; at least one genuinely different quadratic form must be tested.

The target is to determine whether the critical relative-window mechanism at (n=p^s+1) is structural beyond the Demuškin-specific quadratic form.

Pre-check obligations before computation:
- Object: relative finite-window extension (W_n(G)	o D/D_n(D)) and its first intrinsic candidate obstruction.
- Input: (p,s,a,d,r_2); (q=p^a) may parameterize the family but must not be inserted into the finite-window object.
- Functoriality: quotient maps and admissible generator changes must induce the obstruction.
- Gauge: quotient only by explicitly justified automorphisms/normalizations.
- Orientation bridge: state the map from finite-window data to the relative extension/orientation datum before testing.
- q-blindness: the candidate finite object is defined without (q).
- Separation: compare the control stress case with a genuinely different quadratic form.
- Novelty: distinguish any broader theorem from the already closed stress-family threshold.
- Stop: if intrinsicity or the orientation bridge fails, stop rather than enlarging the family.

Gate:
- PASS = theorem-level factorization survives for the broader class, with an independent non-control example;
- FAIL = the mechanism is essentially Demuškin-specific or admissible quadratic inputs exhibit incompatible behavior at the same critical window;
- CONDITIONAL = survival requires an explicit nondegeneracy hypothesis on (r_2);
- OPEN = coherent broader pattern appears but intrinsic factorization/general proof remains unresolved.

Immediate next action: perform this pre-check, then test the smallest non-control quadratic cases before any large computation.


## 2026-10-04 — bounded generalization challenge: user proposal reviewed and execution plan fixed

The user proposed replacing the Demushkin-only test group by a universal E_psi generator for arbitrary relations r, motivated by small p=3,s=1 experiments showing split at n=3 and non-split at n=4 for several relations. This proposal was reviewed against the authoritative research state.

### Decision
**ACCEPT the broader research ambition, but do not jump directly to the universal E_psi generator.** The current authorized branch is the bounded quadratic test-family challenge recorded in CURRENT_STATE.md. This is the correct middle ground between the narrow certified Paper 4 core and the previously failed arbitrary-(r), degree-only theorem.

### Why the correction is necessary
The s=1 experiments are too weak for the intended test (the active family requires s>a>=2), and the degree-3 relation [[x,y],y] is not a quadratic initial relation. Thus they cannot by themselves establish that the critical p^s+1 mechanism is structural. The universal claim “psi exists => n_sep=p^s+1” also requires an intrinsic definition of E_psi, functoriality/gauge invariance, and a proved separation mechanism before it can be treated as a theorem program.

### Authorized experiment
Use G_{s,a}(r_2)=<z,x_1,...,x_d | z^{p^s}=x_1^{p^a}r_2>, with odd p and s>a>=2, nonzero quadratic initial r_2. Keep r_2=[x_1,x_2] as the control and test a genuinely non-equivalent quadratic form, preferably first at d>=4 where rank-2 versus rank-4 quadratic forms give a real comparison. The finite-window object must remain q-blind.

### Required pre-check
Object / Input / Functoriality / Gauge / Orientation bridge / q-blindness / Separation / Novelty / Stop must be discharged before substantial computation. If intrinsicity or the orientation bridge fails, the branch stops.

### Classification
- arbitrary-r degree-only theorem: **FAIL / CLOSED**;
- Paper 4 certified core: **PASS / CLOSED**;
- all-s exact-threshold/transfer-defect boundary: **OPEN / intentionally not a blocker for this challenge**;
- bounded quadratic-family generalization: **OPEN — active challenge**;
- universal E_psi generator: **OPEN / future generalization, DEFERRED**.

Immediate next action: pre-check, then smallest genuinely non-control quadratic test case; no large s=2 computation before that gate passes.


## 2026-10-04 — strategic correction: universal E_psi branch reopened deliberately

The user challenged the earlier conservative decision to defer the universal E_psi generator, correctly distinguishing **governance discipline** from **risk aversion**. The repository continuity protocol is intended to prevent silent scope drift, revive superseded proofs, and promote exploratory computations to theorem status without validation. It does not forbid a consciously chosen high-risk generalization challenge.

### Decision
The universal E_psi direction is therefore **REOPENED as an explicit exploratory branch**. This is a deliberate research gamble, not a reclassification of the failed arbitrary-r degree-only theorem.

The target is stronger than the bounded quadratic-family challenge: construct, or prove impossible to construct, an intrinsically defined finite twisted-character test object E_psi for a broad class of relations r, and determine whether the p^s+1 separation mechanism survives.

### Non-negotiable discipline
The branch remains subject to the protocol's pre-check. In particular, E_psi must not be defined by secretly inserting the unknown q/orientation, and the twisted Fox condition must be shown to be presentation/gauge invariant before large computations. A failure of intrinsicity is a valid and potentially useful **FAIL / CLOSED** result for this construction.

### Strategic consequence
The bounded quadratic-family branch is no longer the sole next step. It becomes a control/benchmark family for the universal branch. The research order is now:

**E_psi intrinsic definition → functoriality/gauge audit → minimal generator → p=3,s=2/3 stress tests → separation/factorization attempt → classify → record.**

The Paper 4 certified core remains frozen. The old arbitrary-r degree-only theorem remains FAIL/CLOSED. No result from this exploratory branch may be back-propagated into Paper 4 without a separate theorem audit.


## 2026-10-04 — E_psi intrinsic-definition attack: first closure and remaining boundary

The universal E_psi branch was attacked from the definition rather than from computation.

### Definition correction

The earlier informal condition “twisted Fox derivative = 0” is not the correct detector for
[
z^{p^s}=r.
]
The correct affine condition is **nonzero critical translation**.

Set
[
A_s=\mathbf Z/p^{s+1}\mathbf Z,qquad U_s=1+pA_s,qquad
E_s=A_s\rtimes U_s.
]
For a character
[
\psi:F\to U_s
]
and a crossed homomorphism
[
\delta:F\to A_s,qquad
\delta(gh)=\delta(g)+\psi(g)\delta(h),
]
the affine representation is
[
\rho_{\psi,\delta}(g)=(\delta(g),\psi(g)).
]

Define the twisted Fox evaluation ideal
[
I_\psi(r)=
\sum_i A_s\,\psi\!\left(\frac{\partial r}{\partial x_i}\right)
=
\{\delta(r):\delta\in Z^1(F,A_{s,\psi})\}.
]

Then the critical relation admits an affine lift with
[
z\mapsto(1,1)
]
iff
[
\psi(r)=1,qquad p^s\in I_\psi(r).
]

This is the correct E_psi object: the finite affine target together with the twisted evaluation ideal. The group alone is not the invariant.

### Definition/gauge/functoriality audit

- **Object:** PASS / CLOSED for the affine test datum.
- **Input:** PASS / CLOSED.
- **Functoriality:** PASS / CLOSED in the marked free-presentation category; individual Fox coordinates change, but the evaluation ideal and affine-lift existence are invariant.
- **Gauge:** PASS / CLOSED when \psi(r)=1; affine translation changes \delta by a coboundary and leaves \delta(r) unchanged, while unit rescaling preserves the valuation condition.
- **q-blindness:** PASS / CLOSED. The target is indexed by the critical window s and does not insert an unknown q into the recognition object.
- **Orientation bridge:** OPEN / LOAD-BEARING for unmarked finite windows. The affine representation has a canonical linear character \psi, but recovering that character intrinsically from the abstract finite window has not been proved.

### Affine target depth

For
[
E_s=A_s\rtimes U_s,
]
one has
[
D_{p^s}(E_s)=p^sA_s\ne1,qquad D_{p^s+1}(E_s)=1.
]
This follows from Lazard's product formula together with
[
[E_s,E_s]=pA_s,qquad
\gamma_i(E_s)=p^{i-1}A_s (i\ge2)
]
until vanishing.

Hence E_s is an exact finite detector for the p^s/p^s+1 boundary.

### General quadratic input

For every tested nonzero quadratic initial relation
[
r\in D_2(F)\setminus D_3(F),
]
there are explicit characters/cocycles producing
[
\psi(r)=1,qquad v_p(\delta(r))\le s.
]
Independent finite-word checks covered:
- p=3,5;
- s=1,2,3;
- random quadratic words in rank 3;
- all 26 nonzero canonical quadratic forms in rank 2 for p=3;
- all 124 nonzero canonical quadratic forms in rank 2 for p=5.

These are **PASS / LOCAL** only.

The formal general lemma still needs a proof with the higher-order contribution audit closed. In particular, in the pure-commutator case the chosen order-p character isolates the quadratic commutator contribution at the p^s scale, but higher Zassenhaus terms must be bounded carefully; if they contribute at lower valuation that only helps, while an exact cancellation at the critical scale must be excluded algebraically.

### Marked separation result

The affine lift gives
[
\rho(z^{p^s})=(p^s,1)=\rho(r)\ne1,
]
while
[
\rho(z^{p^t})=1qquad(t>s).
]
Because
[
D_{p^s+1}(E_s)=1,
]
the representation factors through the marked critical window
[
W_{p^s+1}(G_s(r))
]
but not through the lower window.

Thus the **marked affine/representation critical threshold is a theorem candidate at p^s+1 for arbitrary nonzero quadratic initial relation**.

This does **not** prove
[
W_{p^s+1}(G_s(r))\not\cong W_{p^s+1}(G_t(r))
]
as abstract unmarked finite groups. The missing implication is precisely the intrinsic orientation/character bridge from the abstract window to the affine representation package.

### Classification

- universal arbitrary-degree E_psi theorem: **FAIL / CLOSED** in the old degree-only form;
- affine E_psi definition: **PASS / CLOSED**;
- functorial/gauge/q-blindness pre-check: **PASS / CLOSED** in the marked category;
- quadratic affine separator: **OPEN / LOAD-BEARING theorem candidate**;
- marked critical-window separation: **PASS / LOCAL → theorem candidate**;
- unmarked orientation bridge: **OPEN / LOAD-BEARING**;
- unmarked same-window separation: **OPEN**.

Authoritative detail: `research/EPSI_INTRINSIC_DEFINITION_AUDIT_2026-10-04.md`.


## 2026-10-04 — E_psi quadratic separator audit closes the marked theorem

The E_psi branch was subjected to a second, adversarial audit of the proposed quadratic lemma.

### Correction 1: degree-two Zassenhaus piece
The previously used expression
\[
\rho_2(r)=\sum_i a_iX_i^{[p]}+\sum_{i<j}b_{ij}[X_i,X_j]
\]
was wrong for odd-p Zassenhaus filtration. Since F^p is contained in D_p and hence D_3,
\[
D_2/D_3\cong\Lambda^2H_1(F,\mathbf F_p),
\]
and the degree-two initial form is purely alternating.
Classification: FAIL / CLOSED for the p-power-term formulation; superseded.

### Correction 2: higher terms are not automatically negligible
The earlier statement that the D_3-tail is harmless without calculation was also rejected. The p-power part of D_3=gamma_3 F^p contributes at order p before cocycle normalization and therefore at the same normalized p^s-scale. The gamma_3-part, in contrast, contributes only at order p^(2s) and vanishes modulo p^(s+1).

### Closed argument
Let r=r_2 h, h in D_3, and write epsilon=p^s. Use order-p characters
\[
\psi_\alpha(x_i)=1+\varepsilon\alpha_i.
\]
For
\[
r_2=\sum_{i<j}b_{ij}[x_i,x_j],
\]
the crossed-homomorphism calculation gives
\[
\delta(r_2)\equiv p^sL_B(\alpha,u)\pmod{p^{s+1}},
\]
where for a basic commutator
\[
L_{ij}(\alpha,u)=-\alpha_j u_i+\alpha_i u_j.
\]
If B is nonzero, choose a vertex k incident to a nonzero edge. Then L_B(t e_k, dot) is a nonzero linear functional for t nonzero.

After scaling the cocycle by p^(s-1), the p-power part of h contributes an alpha-independent linear functional C_h(u) at the same p^s-scale; the gamma_3-part is zero modulo p^(s+1). Varying t in F_p, at most one value can make C_h+L_B(t e_k, dot) identically zero. Since p is odd, choose another value and then choose u with nonzero total functional.

Hence
\[
\exists(\psi,\delta):\quad \psi(r)=1,\quad v_p(\delta(r))=s,
\]
and therefore p^s is in I_psi(r).

### Classification
- affine E_psi object: PASS / CLOSED;
- marked functoriality/gauge/q-blindness: PASS / CLOSED;
- quadratic affine separator for every r in D_2\D_3: PASS / CLOSED;
- marked critical-window detection at p^s+1: PASS / CLOSED;
- abstract unmarked orientation/character bridge: OPEN / LOAD-BEARING;
- abstract same-window separation: OPEN;
- arbitrary-degree degree-only theorem: FAIL / CLOSED.

### Research boundary
This closes the marked quadratic E_psi theorem candidate without reviving the old arbitrary-degree claim. The next authorized attack is the intrinsic orientation bridge, not another random quadratic sweep or an enlargement of the relation class.

Authoritative detailed audit: research/EPSI_INTRINSIC_DEFINITION_AUDIT_2026-10-04.md.


## 2026-10-04 — E_psi orientation-bridge audit

The single-character orientation bridge was tested by symmetry rather than by further computation. In the control family r=[x_1,x_2] (rank two), determinant-one Nielsen automorphisms preserve the relator up to conjugacy and act as SL_2(F_p) on the nonzero order-p character space. The marked affine separator works for nonzero character directions, so the successful set is a full nonzero orbit. Therefore no individual nonzero psi is canonical.

**FAIL / CLOSED:** distinguished single-psi bridge.

**OPEN / LOAD-BEARING:** orbit/groupoid-valued bridge.

This is not a no-go for unmarked separation itself. It only rules out presentation-independent selection of one character. The next attack must define an orbit-invariant affine defect directly from the abstract finite window.

Authoritative detail: research/EPSI_ORIENTATION_BRIDGE_AUDIT_2026-10-04.md.


## 2026-10-04 — intrinsic character-carrier salvage

After closing the single-character bridge, the intrinsic replacement
\[
\mathcal A(W)=\operatorname{Ann}_{H^1(W,\mathbf F_p)}(\operatorname{Tor}(W^{ab}))
\]
was identified.

For a critical quadratic window, writing \bar r=p^k a, one can choose a nonzero character direction alpha with alpha(a)=0 and B(alpha,-)\ne0, where B is the nonzero alternating degree-two initial form. Hence the marked affine separator may be chosen inside the canonical carrier.

Classification: **PASS / CLOSED** for the carrier and **PASS / CLOSED** for existence of a successful marked character in it. The carrier itself is not a separator; the extension-defect attached to the power relation remains **OPEN / LOAD-BEARING**.


## 2026-10-04 — critical correction: Tor-annihilator carrier was invalid

The proposed intrinsic carrier
\(\operatorname{Ann}_{H^1(W,\mathbf F_p)}(\operatorname{Tor}(W^{ab}))\)
was adversarially checked and found to be zero for finite p-group windows: W^{ab} is itself finite torsion, and H^1(W,F_p)=Hom(W^{ab},F_p). Therefore the claimed PASS/CLOSED carrier is **FAIL/CLOSED** and superseded.

This correction does not affect the marked quadratic E_psi theorem or the single-character symmetry no-go. It reopens only the carrier construction. The next legitimate intrinsic candidate must exploit filtered extension/Bockstein data rather than ordinary torsion of W^{ab}.


## 2026-10-04 — E_psi Sp-orbit closure claim critically rejected

A proposed closure of the unmarked orientation bridge via an Sp-orbit was adversarially audited and is **not valid**. The decisive counterexample is already in rank 4: r_2=[x_1,x_2] is nonzero in D_2/D_3 but defines a rank-2 degenerate alternating form. Its stabilizer preserves the radical, so it is not the full Sp_4(F_p) and does not act transitively on all nonzero character directions. More generally, r in D_2\D_3 does not imply nondegeneracy, and the Zassenhaus exponent s has no reason to equal half the rank of B.

Even if a nondegenerate special case has a transitive symplectic orbit, transitivity does not imply abstract finite-window separation: one still needs an intrinsic defect on the orbit/representation groupoid and a proof that it differs for s and t. Likewise, the assertion that B is recovered from the abstract finite window merely because the window is a quotient of G_s(r) is not a valid intrinsicity argument.

Classification: Sp-orbit bridge for all D_2\D_3: **FAIL / CLOSED as stated**; nondegenerate symplectic subcase: **CONDITIONAL** only; orbit/groupoid-valued intrinsic defect: **OPEN / LOAD-BEARING**; abstract unmarked same-window separation: **OPEN**. This supersedes the proposed PASS/CLOSED Sp-orbit conclusion. The marked E_psi theorem remains PASS/CLOSED.


## 2026-10-04 — critical correction: marked (s) is target-indexed, not an invariant of (r_2)

The proposed next gate “does (v_p(\delta(r))) depend only on (r_2)?” was audited against the actual marked E_\psi construction. That question was ill-posed.

In the closed marked lemma, (s) is fixed **before** constructing the affine target:
\[
A_s=\mathbf Z/p^{s+1}\mathbf Z,qquad E_s=A_s\rtimes(1+p^sA_s).
\]
The lemma then asserts that for every nonzero quadratic initial relation (r\in D_2\setminus D_3), after choosing the order-(p) character and cocycle in that (E_s), one can arrange
\[
\psi(r)=1,qquad v_p(\delta(r))=s.
\]
Thus (s) is not extracted from (r), and there is no single (\delta) whose valuation is an invariant attached to (r_2). The cocycle takes values in the (s)-dependent module (A_s).

For (r_A=[x_1,x_2]), this is explicit for every (s\ge1): take \(\psi(x_1)=1+p^s\), \(\psi(x_i)=1\) for (i>1), and choose the normalized cocycle with (u_2=1) and the other relevant coordinate zero. Then
\[
\delta([x_1,x_2])\equiv p^s\pmod{p^{s+1}},
\]
so the same fixed relation admits a critical affine lift at every target index (s).

Therefore:
- “marked (s) is determined by (r_2)” = **FAIL / CLOSED as a formulation**;
- “same (r_2) implies same marked (s)” = **FAIL / CLOSED**;
- the deduction that marked (s) is not an abstract invariant from that premise is **superseded**;
- the genuine unmarked orientation/orbit-level problem remains **OPEN / LOAD-BEARING**.

This also separates two notions previously conflated: (i) the Zassenhaus degree of a higher tail inserted into a relator, and (ii) the externally indexed critical depth of the affine detector. They are different parameters and must not be identified.

For the exploratory pair (r_A) versus (r_B=r_Ax_1^{p^m}), any separation caused by the added degree-(p^m) tail is therefore a filtered-relator/quotient statement, not evidence that the marked E_\psi exponent parameter is encoded by the quadratic initial form.


## 2026-10-04 — refinement: the higher-jet critical pair is genuinely separated, but is not exponent-same-family separation

For the exploratory pair
\[
r_A=[x_1,x_2],\qquad r_B=[x_1,x_2]x_1^{p^m},
\]
the previously proposed \(\operatorname{Aut}(F)\)-orbit argument is unnecessary and too strong. The separation at the first window where the added tail becomes visible has a direct intrinsic certificate from abelianization.

Indeed, for \(n=p^m\), the added factor \(x_1^{p^m}\) lies in \(D_{p^m}(F)\), so
\[
W_{p^m}(G_A)\cong W_{p^m}(G_B).
\]
At \(n=p^m+1\), the abelianization of the free truncated quotient retains the class of \(x_1^{p^m}\):
\[
W_{p^m+1}(G_A)^{ab}\cong(\mathbf Z/p^{m+1})^4,
\]
whereas the relation for \(G_B\) imposes \(p^m x_1=0\), giving
\[
W_{p^m+1}(G_B)^{ab}\cong
\mathbf Z/p^m\oplus(\mathbf Z/p^{m+1})^3
\]
(up to the displayed choice of basis). Hence
\[
W_{p^m}(G_A)\cong W_{p^m}(G_B),qquad
W_{p^m+1}(G_A)\not\cong W_{p^m+1}(G_B).
\]
This is a valid **PASS / CLOSED Zassenhaus-critical higher-jet separation**.

However, it does not compare \(G_s(r)\) and \(G_t(r)\) for one fixed relation \(r\). It therefore does not close the exact unmarked same-window problem of the control family. Its significance is narrower: a finite window can intrinsically detect a higher filtered tail at its first visible degree, even when the quadratic initial form is unchanged.

The earlier claim that this proves or disproves recovery of the marked E_\psi parameter \(s\) is not valid. The marked parameter is target-indexed; the higher-tail degree \(m\) is a property of the chosen relator.


## 2026-10-04 — E_psi / critical-separation audit: proposed closure rejected

A full audit of the session-level claim that the E_psi branch is now closed found a decisive filtration error and an unsupported automorphism-orbit step.

### Decisive correction

For the Zassenhaus filtration, if (c\in D_3\setminus D_4) and (p^m>3), then
[
D_{p^m}\subset D_3,
]
not (D_3\subset D_{p^m}). Hence for
[
r_A=[x_1,x_2],qquad r_B=r_Ac,qquad c\in D_3\setminus D_4,
]
the two relators do **not** have the same image modulo (D_{p^m}). Therefore the assertion that
[
W_{p^m}(G_A)\cong W_{p^m}(G_B)
]
follows from the filtration degree of (c) is false.

What is valid is only the formal low-window statement: if (c\in D_k), then the two defining relators have the same image in (F/D_k(F)), so the corresponding presented quotients have the same presentation modulo (D_k). This does **not** imply non-isomorphism at (k+1); an abstract isomorphism may come from an automorphism of the free quotient.

### Second correction: automorphism argument

The statement “an automorphism preserves degree, therefore it cannot send a degree-2 element to degree-2 plus degree-3” is invalid. IA automorphisms act trivially on abelianization while changing higher filtered terms; Magnus generators include commutator transvections (x_i\mapsto x_i[x_j,x_k]). Thus preservation of the leading graded class does not rule out adding higher Zassenhaus/lower-central terms. Any claimed separation of (r_A) from (r_Ac) therefore requires an actual orbit calculation, not a degree argument.

### Consequence

The proposed general statement
[
c\in D_k\setminus D_{k+1}\Longrightarrow
W_k(G_A)\cong W_k(G_B),W_{k+1}(G_A)\not\cong W_{k+1}(G_B)
]
is **FAIL/CLOSED as stated**. The first implication is presentation-level and valid; the second is not automatic.

The specific pair
[
[x_1,x_2],quad [x_1,x_2][x_1,[x_1,x_2]]
]
does not establish a critical (p^m+1) separation. In particular, for (p^m>3) it is already different modulo (D_{p^m}) at the presentation level, and its abstract orbit under automorphisms remains a separate question.

### E_psi boundary correction

The statement “marked E_psi theorem has abstract content exactly equal to the intrinsic quadratic invariant B” is also too strong. What is established is only:
- the marked theorem depends on a quadratic initial relation and an externally chosen target (E_s);
- (s) is not extracted from (r_2);
- no intrinsic single-character bridge has been constructed;
- therefore the marked theorem does not currently supply an unmarked recovery of (s).

This is **OPEN**, not FAIL/CLOSED. The possibility of an independent abstract invariant of the family (G_s(r)) remains unresolved.

### Current classification after audit

- marked quadratic E_psi theorem: **PASS/CLOSED (marked scope)**;
- single canonical psi bridge: **FAIL/CLOSED**;
- Tor-annihilator carrier: **FAIL/CLOSED**;
- Sp-orbit universal bridge: **FAIL/CLOSED as stated**;
- quadratic kernel-rank separation: **PASS/CLOSED**;
- generic (D_k/D_{k+1}) critical separation theorem: **FAIL/CLOSED as stated**;
- specific (G_s(r)\) vs (G_t(r)) abstract same-window separation: **OPEN/LOAD-BEARING**;
- abstract unmarked shadow of the marked E_psi theorem: **OPEN**.

This correction does not reopen the failed arbitrary-degree theorem. It restores the authoritative boundary that exact unmarked same-window separation is unresolved.


## 2026-10-04 — d=3, p=3 cubic-jet audit: Q3 computation and W4 separation

A direct linear-algebra audit of the proposed rank-2 quadratic control case
\[
F=F(x_1,x_2,x_3),\qquad r_2=[x_1,x_2]
\]
confirms the following.

1. The degree-3 free Lie space has dimension 8 over \(\mathbf F_3\). For
\[
\Delta:L_2\oplus L_2\to L_3,\qquad
\Delta(u_1,u_2)=[u_1,x_2]+[x_1,u_2],
\]
one obtains \(\dim\operatorname{im}\Delta=6\). Moreover
\[
[r_2,V]\subseteq\operatorname{im}\Delta,
\]
so
\[
Q_3(r_2)=L_3/([r_2,V]+\operatorname{im}\Delta)
\]
has dimension 2. A valid quotient basis is represented by
\[
c_1=[x_3,[x_1,x_3]],\qquad c_2=[x_3,[x_2,x_3]].
\]
Independent tensor-model row reduction over \(\mathbf F_3\) gives rank 6 for \(\operatorname{im}\Delta\) and rank 8 after adjoining \(c_1,c_2\).

2. The stabilizer of \(e_1\wedge e_2\) in \(GL_3(\mathbf F_3)\) has order
\[
|SL_2(\mathbf F_3)|\,|\mathbf F_3^\times|\,|\mathbf F_3^2|
=24\cdot2\cdot9=432.
\]
The earlier 432 value is correct; the 864 value would correspond to incorrectly using \(GL_2\) rather than the determinant-one condition forced by fixing \(e_1\wedge e_2\).

3. On \(Q_3\), the unipotent radical and the scalar \(\lambda\in\mathbf F_3^\times\) act trivially, while the \(SL_2\)-part acts naturally on \(\langle c_1,c_2\rangle\cong\mathbf F_3^2\). Hence the stabilizer has exactly two orbits:
\[
\{0\},\qquad Q_3\setminus\{0\}.
\]

4. The proposed \(W_4\)-separation is valid for the specific zero/nonzero comparison, but the original proof contained a filtration error. It is false that
\[
\gamma_3(F)^3\subseteq\gamma_4(F).
\]
The correct statement is
\[
D_4(F)=\gamma_4(F)\,\gamma_2(F)^3\,\gamma_3(F)^3\,F^9,
\]
so the lower-central degree-3 layer of the \(W_4\) quotient is taken modulo the appropriate 3-power relations; equivalently its relevant cubic layer is an \(\mathbf F_3\)-quotient of \(L_3\), not the integral \(L_3\) used in the draft argument.

For
\[
r_A=[x_1,x_2],\qquad
r_B=[x_1,x_2]c_1,
\]
the degree-3 normal-closure contribution is respectively
\[
\langle [[x_1,x_2],x_i]:i=1,2,3\rangle
\]
of dimension 3, and that same 3-space plus \(\langle c_1\rangle\), of dimension 4. Thus the corresponding cubic lower-central quotient has dimensions 5 and 4 (over \(\mathbf F_3\)). Therefore
\[
W_4(G_A)\not\cong W_4(G_B).
\]
At \(W_3\), both relators have the same image modulo the degree-3 tail, so
\[
W_3(G_A)\cong W_3(G_B).
\]

Classification: **PASS / CLOSED (specific \(d=3,p=3\), zero-vs-nonzero cubic orbit separation)**.

Important boundary: this does **not** prove that every pair of distinct \(Q_3\)-orbits gives distinct \(W_4\)-isomorphism classes in general. In the present \(d=3,p=3\) example there are only two stabilizer orbits, and the zero/nonzero pair is separated by the cubic-layer dimension.

The broad criterion
\[
W_n\text{-iso}\iff \operatorname{Aut}(F/D_n)\text{-orbit of the truncated relator}
\]
remains **OPEN**. An isomorphism between two quotient groups does not automatically imply that their defining kernels are conjugate under an automorphism of the universal truncated free group; this is a Nielsen/lifting issue and requires a separate theorem.

Next authorized attack: formulate the general cubic-layer map
\[
Q_3(r_2)\longrightarrow \text{isomorphism invariants of }W_4
\]
carefully, first for arbitrary odd \(p\) and rank \(d\), before attempting the full \(Q_k\) tower.


## 2026-10-04 — correction: the d=3,p=3 cubic W4 separation is NOT certified

The immediately preceding audit over-promoted the pair
\[
r_A=[x_1,x_2],\qquad r_B=[x_1,x_2]c_1,qquad c_1=[x_3,[x_1,x_3]]
\]
to PASS/CLOSED. That promotion is **superseded and withdrawn**.

The error is more fundamental than the earlier \(\gamma_3^3\subseteq\gamma_4\) mistake. For the inhomogeneous relator \(r_B=r_2+c_1\), the leading lower-central term is still \(r_2\) in degree 2. Passing to the associated lower-central graded object therefore initially imposes the degree-2 relation \(r_2\), whose degree-3 consequences are \([r_2,V]\). One cannot simply add \(c_1\) as an independent degree-3 relation in \(\gamma_3(W_4)/\gamma_4(W_4)\).

Equivalently: the fact that the normal closures of \(r_2\) and \(r_2c_1\) are different in the universal truncated presentation does **not** imply that \(c_1\) contributes an additional independent relation to the cubic lower-central layer of the quotient. The relation \(r_2c_1=1\) identifies the degree-2 word \(r_2\) with a degree-3 correction; it does not separately kill \(c_1\).

Therefore the claimed dimensions
\[
\dim \gamma_3(W_4(G_A))/\gamma_4=5,\qquad
\dim \gamma_3(W_4(G_B))/\gamma_4=4
\]
are not established and should not be used.

What remains valid from the computation:
- \(Q_3(r_2)\) has dimension 2 with representatives \(c_1,c_2\);
- the stabilizer of \(e_1\wedge e_2\) has order 432;
- its action on \(Q_3\) has zero and nonzero orbits;
- \(Q_3\) therefore contains genuinely non-removable cubic directions at the presentation/jet level.

What is **not** established:
\[
W_3(G_A)\cong W_3(G_B),\qquad
W_4(G_A)\not\cong W_4(G_B)
\]
for the zero/nonzero cubic pair. The \(W_3\) equality is still presentation-level and safe; the \(W_4\) non-isomorphism is **OPEN**.

The next correct attack is not another dimension count based on the same lower-central layer. It must test an invariant that sees the *extension class/filtered lift* of the cubic jet, e.g. a canonical p-power/commutator extension datum in \(W_4\), or directly compute the full finite 3-group isomorphism type for the smallest case. The \(Q_3\) orbit remains a candidate input, not yet a certified \(W_4\)-classification invariant.

Classification of the cubic result after correction:
- \(Q_3\) computation: **PASS / LOCAL**;
- nonzero cubic directions modulo IA gauge: **PASS / LOCAL**;
- zero-vs-nonzero \(Q_3\) orbit \(\Rightarrow W_4\) non-isomorphism: **OPEN**;
- general \(Q_3\to W_4\)-isomorphism classification: **OPEN / LOAD-BEARING**.


## 2026-10-04 — DIRECTION 2 CLOSED: ordinary mod-p cohomology is s/a-blind

The requested Direction 2 attack was completed to the full ordinary cohomology-ring level rather than stopping at H^1, H^2, or the associated graded.

### Target
For odd p, stress family G_{s,a}=<z,x_1,...,x_d | z^{p^s}=x_1^{p^a}[x_1,x_2][x_3,x_4]...>, with s>=1, finite a>=1, and a=infinity meaning the power term is absent.

### Core proof
Because p^s,p^a>=3, both power terms lie in the third p-Zassenhaus term. Therefore the relator is congruent modulo the third term to the same quadratic commutator product for every s,a.

Quadrelli, arXiv:2011.03233v3, Proposition 2.1, applies directly: the mod-p cohomology algebra is quadratic; H^k(G,F_p)=0 for k>=3; and the cup product in H^1 is exactly the common symplectic commutator form. Thus the complete ordinary graded algebra H^bullet(G_{s,a},F_p) is independent of s and a in the declared family.

### Independent verification
- filtration check: PASS;
- minimal one-relator presentation: PASS;
- complete H^bullet determination: PASS;
- a=s versus a=infinity: PASS;
- q-blindness: PASS.

The literature source is stronger than the earlier internal associated-graded observation: it closes the whole ordinary cohomology ring, not merely gr_Z.

### Boundary
This does **not** prove G_{s,a} isomorphic to G_{t,b}, equality of finite windows, or equality of higher operations such as Massey/Bockstein/A_infinity data. It proves only that ordinary mod-p cohomology cannot recover the hidden s or a in this family.

### Classification
**Direction 2 = PASS / CLOSED.**

The route is closed. The remaining finite-window boundary must use information beyond the ordinary cohomology ring, if it is pursued at all. No repetition of ordinary H^* calculations is authorized.

Authoritative audit: research/PAPER4_DIRECTION2_COHOMOLOGY_BLINDNESS_CLOSURE_2026-10-04.md.


## 2026-10-04 — Direction 3 decision: ordinary cohomology is now discarded; filtered extension/lift becomes the active invariant layer

The completed Direction 2 audit establishes **PASS / CLOSED** for ordinary mod-p cohomology in the declared odd-p stress family: the full ordinary cohomology ring is s/a-blind. Repeating H^*, cup-product, or ordinary quadratic-cohomology calculations is therefore no longer an authorized route to the hidden finite-window parameter.

### Strategic conclusion

**Ordinary cohomology is no longer a research target.** The remaining information must be sought one layer above the ordinary cohomology ring, in the **filtered extension/lift structure** of the finite Zassenhaus tower.

The working object is not a new cohomology ring. The first intrinsic candidate is the filtered extension/lift groupoid over a critical window:
[
mathsf{Lift}_n(W_n)
=
left{
widetilde W	woheadrightarrow W_n:
widetilde W	ext{ is an admissible }(n+1)	ext{-level filtered lift}

ight}/cong,
]
together with the kernel
[
K_n=D_n/D_{n+1}
]
and the induced conjugation/trivial-action data and extension class. Since
([D_n,G]subseteq D_{n+1}), the successive Zassenhaus layer is central; however, the research target is the **actual filtered lift/extension package**, not merely its abstract class in ordinary (H^2).

For the present problem the decisive question is:

> Does the critical filtered lift/extension fiber over (W_{p^s}(G_s)) versus (W_{p^s+1}(G_s)) retain the hidden (p^s)-power relation even though the ordinary cohomology ring does not?

### Required next gate

Before computation, audit:
1. **Object:** define the admissible filtered lift groupoid independently of the hidden q/s parameter.
2. **Input:** specify exactly which filtration/layer/lift data are retained.
3. **Functoriality:** prove invariance under finite-window isomorphism and admissible presentation changes.
4. **Gauge:** quotient lift choices and generator changes correctly.
5. **Orientation bridge:** determine whether the lift package carries the affine/orientation information without choosing a distinguished character.
6. **q-blindness:** the recognition object must not contain q=p^a.
7. **Separation:** test whether the extension/lift package differs for the a=s versus a=infinity boundary or for s versus t at the critical level.
8. **Novelty:** distinguish the actual filtered lift invariant from merely restating an ordinary cohomology extension class.
9. **Stop:** if the lift object collapses to the already-blind ordinary ring or is not intrinsic, close that formulation rather than adding ad hoc decorations.

### Immediate research target

The first concrete construction is the **one-step filtered extension**
[
1	o D_n/D_{n+1}	o W_{n+1}	o W_n	o1
]
viewed as a structured lift, with its p-power/commutator lifting data retained. The next attack should determine whether the hidden relation contributes a nontrivial, gauge-invariant defect to this lift package at (n=p^s).

Classification:
- ordinary cohomology route: **PASS / CLOSED and STOPPED**;
- filtered extension/lift object: **OPEN / LOAD-BEARING**;
- intrinsic extension defect: **OPEN**;
- abstract same-window separation: **OPEN**;
- arbitrary-degree degree-only theorem: **FAIL / CLOSED** and remains closed.

This entry is the controlling decision for the next research branch.


## 2026-10-04 — filtered-extension extraction/no-go boundary CLOSED

The post-cohomology Direction 3 was executed at the structural level rather than by another candidate hunt. The canonical one-step Zassenhaus extension
\[
1\to K_n=D_n/D_{n+1}\to W_{n+1}\to W_n\to1
\]
was fixed as the only active object.

### Gate result
- Object: **PASS / CLOSED**. The extension is canonical, q-blind, and functorial under filtered finite-window isomorphism.
- Input: **PASS / CLOSED**. No hidden q=p^a, marked character, or presentation choice is inserted.
- Gauge: **PASS / CLOSED**. Since [D_n,G]⊂D_{n+1}, the kernel is central. A section produces a 2-cocycle, and changing the section changes it by a coboundary. Hence a defect computed from a selected lift is not intrinsic unless it descends through this gauge action.
- Orientation bridge: **FAIL / CLOSED** for the proposed scalar/carrier extraction. The unmarked extension contains no distinguished character/orientation. The marked E_psi construction does not supply an intrinsic bridge after the marking is forgotten.
- q-blindness: **PASS / CLOSED**.
- Separation: the full extension-equivalence class is not a new lower-level invariant; it is exactly the structured isomorphism class of W_{n+1}->W_n. Thus using the full package to separate the critical cases is equivalent to solving the original finite-window extension-isomorphism problem.

### Independent structural check
Standard central-extension theory identifies section changes with coboundaries and the intrinsic extension with its cohomology class. Zassenhaus layers additionally carry canonical restricted-Lie p-power/commutator operations. These facts validate the gauge analysis, but neither supplies the missing unmarked orientation bridge.

### Classification
**Filtered-extension extraction as a new canonical defect = FAIL / CLOSED.**

This is a method-level no-go, not a proof that the critical a=s and a=infinity windows are isomorphic. The latter remains **OPEN** if one insists on exact finite-window classification. No further candidate hunting is authorized merely to avoid that boundary.

Authoritative audit: research/PAPER4_FILTERED_EXTENSION_EXTRACTION_NO_GO_2026-10-04.md.

### Stop decision
Do not reopen ordinary cohomology, search for another carrier, invent another E_psi variant, or add ad hoc lift decorations. Further progress would require a genuinely new theorem giving a canonical quotient/factorization of the full extension-equivalence class. The current extraction branch is therefore closed at its legitimate boundary.


## 2026-10-04 — correction: filtered-extension no-go was method-level, not tower-wide

Adversarial review identified a real overreach in the immediately preceding stop. The prior result correctly closes the attempt to extract a canonical scalar defect from a chosen section/lift of the **unmarked one-step extension**, because section changes act by coboundaries and no distinguished orientation is present. But that does not justify a blanket no-go for all canonical representations of the same extension, nor for multi-step compatible tower data.

### Corrected failure taxonomy
A negative result must distinguish:
1. **representation failure** — a chosen coordinate cannot expose information present in the fixed structure;
2. **information failure** — the full declared structure itself lacks the target information;
3. **detector failure** — the information may be present, but no functorial extraction operator has yet been found.
Only (2) is a structural no-go for the declared object.

### Pre-registered bounded reopening
The branch is reopened only as a representation-layer feasibility gate, not as candidate hunting. The admissible structure layers are fixed in advance:
- extension class;
- induced module/conjugation structure;
- canonical restricted p-power and commutator operations;
- their adjacent-layer compatibility;
- two-step/full finite tower extension compatibility.

The minimum multi-step object is W_{p^s+2}->W_{p^s+1}->W_{p^s}. No new carrier, character, or ad hoc lift decoration may be introduced merely because one layer fails.

### E_psi mechanism audit
The marked affine detector succeeds through a combination of:
- **filtered depth**: D_{p^s}(E_s) nontrivial but D_{p^s+1}(E_s)=1;
- **orientation/representation**: psi and delta provide the directed affine evaluation of the hidden relation.

Thus the one-step unmarked extension cannot be expected to reproduce the marked detector merely from filtered depth. The intrinsic target, if it exists, should be an affine representation **orbit/groupoid**, not a canonically selected single psi.

Representability will be used only after defining the category of admissible filtered tower structures and the functor to affine representation groupoids; it will not be assumed as a slogan.

### Classification
- one-step scalar defect from unmarked extension: **FAIL / CLOSED**;
- one-step/tower representation-layer feasibility: **OPEN / LOAD-BEARING**;
- exact unmarked same-window separation: **OPEN**;
- no arbitrary candidate hunt authorized.

Authoritative pre-registration: research/PAPER4_REPRESENTATION_LAYER_PREREGISTRATION_2026-10-04.md.


## 2026-10-04 — representation-layer gate reaches its boundary

The pre-registered two-step filtered-tower feasibility gate has now been executed. The intrinsic object is
\(W_{p^s+2}\to W_{p^s+1}\to W_{p^s}\), with central extension classes, induced module structure, restricted p-power/commutator operations, and adjacent-layer compatibility.

- Object/Input/Functoriality/Gauge: **PASS / CLOSED**.
- Distinguished single-character orientation bridge: **FAIL / CLOSED**, consistent with the earlier symmetry no-go.
- An affine representation **groupoid/orbit construction** is legitimate and functorial from the full declared tower, but at this level it is only a canonical reformulation of the structured finite-window problem, not a strictly smaller carrier.
- No comparison theorem currently shows that the groupoids differ for (a=s) versus (a=\infty), and none shows that they coincide.
- Therefore the remaining obstruction is classified as **detector failure / OPEN**, not information failure.

This closes the bounded representation-layer branch at its pre-registered stop rule. No new carrier, character, lift decoration, or ad hoc representation hunt is authorized. The exact unmarked same-window separation remains **OPEN / LOAD-BEARING** and now requires a genuinely new factorization/compression theorem rather than another candidate search.

Authoritative audit: research/PAPER4_REPRESENTATION_LAYER_GATE_RESULT_2026-10-04.md.


## 2026-10-04 — Paper 4 manuscript/PDF final artifact audit

Paper 4 manuscript was finalized from the certified research state and built from
the dedicated `paper4-tex-2026-10-04` branch. The four manuscript corrections
were applied: direct same-window order separation for (1\le a<s<t);
the (a=s) versus (a=\infty), (s\ge2) boundary remains OPEN;
the arbitrary-(r) degree-only generalization is explicitly closed using
the (r=z^p) counterexample; and the Zassenhaus/Jennings--Lazard and
quadratic-cohomology literature boundary was recorded in the manuscript.

Final CI result: `paper4-tex-build` run 37172461426 = PASS.
PDF: 12 pages.
SHA-256: `39937e753368e4cb8c06dfaf2f7808727c3d88e14b75669c937ab0d06520b536`.
GitHub Actions artifact: `paper4-pdf`, id 11292160916.
The local audited PDF is `/mnt/data/Paper4_final_2026-10-04.pdf`.

Classification: **PASS / CLOSED — manuscript artifact complete**.
This closes the writing/PDF-production task only; the mathematical OPEN boundary
(G_{s,s}) versus (G_{s,\infty}) for (s\ge2) remains unchanged.


## 2026-10-04 — Paper 5 redefined around Aut(W_n)

The compression formulation of Paper 5 was judged too tautological to carry the intended mathematical contribution. The active branch is therefore redefined as concrete finite-group structure: Aut(W_n), its IA kernel, its image on W_n/Phi(W_n), induced action on admissible quotients Q_n, and radical/shear effects.

The user supplied completed calculations reporting exact automorphism orders for (p,n)=(3,4) and (5,6). The p-parts exhibit the same factor p^2 deficit from split to non-split cases at both primes. The p=3,n=4 admissible-kernel enumeration reports 81/9/72 kernels with orbit pattern 1/1/3 respectively.

Because the current repository did not yet contain the supplied scripts/logs for these new calculations, the evidence is recorded as PASS / LOCAL, user-reported rather than independently certified. No structural theorem is promoted from the order comparison alone.

The next authorized computation is the IA/GL decomposition for all p=3,n=4 cases, followed by the induced Aut(W) -> Aut(Q) image/kernel. The aim is to identify the exact layer responsible for the p^2 gap. Only after independent closure at p=3 will the same measurement be run at p=5.

Audit: research/PAPER5_AUT_STRUCTURE_IA_GL_PRECHECK_2026-10-04.md.


## 2026-10-04 — Paper 5 Aut-orbit follow-up evidence (user-supplied logs)

The user supplied three computational artifacts/results for the active Aut(W_n) branch (aut_common.g, aut3.log, p5aut.log). The artifacts are not yet committed to the current repository, so the following is recorded as USER-REPORTED / REPRODUCTION PENDING, not theorem-level evidence.

Reported p=3 orbit structure: (3,1,1) has 72 admissible kernels in Aut-orbits 9+9+54; (3,1,2) has 9 kernels in one orbit; (3,2,1), n=10, has 81 kernels in one Aut(W_10)-orbit, with reported |Aut(W_10)|=2*3^30, |K|=3^9, and 3^10 complements per kernel. The two size-9 orbits in (3,1,1) are reported to be distinguished by pi(z) in Phi(Q) versus outside Phi(Q); a complete invariant explanation of 9/9/54 is still open.

Reported p=5,n=6 orders: s=0,a=1 -> 2^2 5^109; s=1,a=1 -> 2^2 5^107; s=2,a=1 -> 2^2 5^109; s=1,a=2 -> 2^5 3 5^107; s=0,a=2 -> 2^7 3 5^109. This reproduces the reported p^2 p-primary split/non-split gap and shows s-dependence in total Aut order, but remains observational pending independent rerun.

Interpretation: Aut-orbit structure is now a strong candidate structural layer, but the authoritative Paper 5 gate still requires the p=3,n=4 IA/GL decomposition and fixed-quotient action analysis before the larger n=10 orbit result is promoted. Classification: PASS / LOCAL candidate evidence; reproduction and structural factorization OPEN. Audit: research/PAPER5_AUT_ORBIT_FOLLOWUP_AUDIT_2026-10-04.md.


## 2026-10-04 — Paper 5 IA/GL decomposition gate advanced

The five Paper 5 external calculation artifacts have now been restored under `research/external/paper5_aut/`: `aut_common.g`, `aut3.g`, `aut3.log`, `p5aut.g`, and `p5aut.log`. The earlier provenance label “user-reported / artifacts not in repository” is superseded.

The recovered p=3,n=4 calculation gives exact reported automorphism orders:
- s=0,a=1: (|Aut(W)|=2^2 3^{30});
- s=1,a=1: (|Aut(W)|=2,3^{28}), with 72 admissible kernels in orbits 9+9+54;
- s=0,a=2: (|Aut(W)|=2^5 3^{30});
- s=1,a=2: (|Aut(W)|=2^4 3^{28}), with one orbit of size 9;
- s=2,a=1: (|Aut(W)|=2^2 3^{30}), one orbit of size 81 and (3^{10}) complements.

Exact order arithmetic gives the following prediction, not yet a certified decomposition:
[
(0,1): (|IA|,|L|)=(3^{27},2^2 3^3),quad
(1,1): (3^{25},2,3^3),
]
[
(0,2): (3^{27},2^5 3^3),quad
(1,2): (3^{25},2^4 3^3).
]
Thus the p-primary (3^2) loss is predicted to lie entirely in the IA layer, while the linear image keeps (3^3) in all four cases.

A new executable audit was added at `research/scripts/paper5_ia_gl_decomposition.g`. It directly checks the Frattini action, the AutPGrp linear-image order, the IA factor from `agOrder`, and the exact factorization (|Aut(W)|=|IA||L|).

The GAP AutPGrp documentation confirms that `glAutos` are the automorphisms acting nontrivially on the Frattini quotient and that `agAutos` generate the normal solvable part, so this script targets the intended IA/GL split rather than introducing an ad hoc layer.

### Classification

- external artifacts: **PASS / REPOSITORY**
- total-order and orbit data: **PASS / REPOSITORY**
- IA-defect localization by order arithmetic: **PASS / LOCAL-PREDICTED**
- executable IA/GL decomposition: **OPEN / REPRODUCTION PENDING**
- quotient-action image/kernel: **OPEN**
- p=5 structural theorem: **DEFERRED until p=3 closure**

Audit: `research/PAPER5_IA_GL_DECOMPOSITION_AUDIT_2026-10-04.md`.


## 2026-10-04 — Paper 5 IA/GL execution gate: runtime boundary

The IA/GL localization was taken to the execution boundary. The repository now contains the five external GAP artifacts and the dedicated decomposition script. A local environment check was performed for GAP; GAP/AutPGrp is not installed in the available runtime, so the new executable gate could not be rerun here.

Accordingly, no IA-kernel equality or full Aut(W) generation claim is promoted. The exact-order arithmetic remains **PASS / LOCAL-PREDICTED**: for p=3,n=4 the split/non-split 3^2 gap is numerically localized to the candidate IA factor while the candidate linear image retains v_3=3 in all four cases.

Required next execution checks remain:
- displayed W generators generate W;
- agAutos act trivially on W/Phi(W);
- glAutos generate a linear image of the recorded order;
- the induced action homomorphism has kernel exactly <agAutos>;
- <glAutos,agAutos>=Aut(W);
- |IA| |L| = |Aut(W)|.

The available runtime cannot certify these until GAP/AutPGrp is executed in a suitable GAP environment. Classification: **OPEN / REPRODUCTION PENDING**. p=5 remains deferred.


## 2026-10-04 — Paper 4 roadmap alignment and Q-direction decision

External handoff roadmap `research/external/GENERAL_THEOREM_ROADMAP_HANDOFF_2026-10-04.md` was compared against `RESEARCH_MAP.md`, `CURRENT_STATE.md`, and the continuity protocol.

- Roadmap-level next target remains correct: **unmarked same-window separation** in the S/hard region, beginning with the smallest control case and then generalization.
- The roadmap's original L4/L5 implementation (extension-class/orbit separation) is no longer the best immediate route. One-step extension extraction, distinguished-single-psi bridge, naive Sp-orbit bridge, and two-step representation compression have already reached their recorded boundaries.
- Current best implementation is the intrinsic finite-group predicate
  \(Q(W):\exists(g,H),\ \langle g,H\rangle=W,\ 1\ne g^{p^s}\in H\).
- Q evidence is **PASS / LOCAL**: p=3,s=1,r=x^3 was exhaustively tested (52,488 positive generating pairs in W_s, 0 in W_t); p=5,s=1,r=x^5,n=6 has 10,226 positives in W_s and 0 in W_t among 200,000 random pairs. The latter is sample evidence, not proof.
- Frattini-lift reformulation gives a natural transformed-relator problem \(r'=\alpha^{-1}(r)\). Killing x yields the necessary abelian z-exponent condition \(v_p(\epsilon(r'))\le s\), reproducing the easy/high-valuation obstruction.
- The remaining hard boundary is nonabelian: rule out all relevant transformed relators in the \(v_p(\bar r)\le s\) region. The earlier restricted-Lie root-capture attempt is invalid without control of the induced filtration \(H\cap D_k(W)\); a Root-Capture lemma or equivalent Magnus/PBW statement is still **OPEN / LOAD-BEARING**.

**Decision:** the roadmap's Theorem-C direction is retained at the strategic level, but its implementation is updated to **Q-invariant → p=3,s=1,r=x^3 transformed-tuple/Frattini-lift audit → nonabelian Magnus/PBW obstruction → general lemma if possible**. Do not restart the already-closed L4/L5 extraction as a standalone carrier hunt.

Detailed alignment record: `research/PAPER4_ROADMAP_ALIGNMENT_AND_NEXT_STEP_2026-10-04.md`.
Classification: Q = **PASS / LOCAL**; Q theorem and nonabelian obstruction = **OPEN / LOAD-BEARING**.

Immediate next authorized action: classify Q-positive p=3,s=1,r=x^3 pairs up to the relevant automorphism/Frattini-lift structure and inspect the transformed relator at the minimal Magnus/PBW degree needed to isolate the common obstruction.


## 2026-10-04 — Paper 4 Q pre-check: current Q definition is too weak

Before executing the planned p=3,s=1,r=x^3 transformed-tuple audit, the current Q definition itself was rechecked under the continuity protocol.

The recorded predicate is:
Q(W): there exist g and H with <g,H>=W and 1 != g^(p^s) in H.

Immediate structural consequence: Q-positive implies ord(g)>p^s. Thus Q necessarily contains an exponent witness. More importantly, if H is allowed to be an arbitrary subgroup subject only to <g,H>=W, then H can be chosen after an element g with nontrivial p^s-th power; the predicate therefore does not by itself encode the intended nonabelian transformed-relator/Frattini-lift obstruction. It is at best an exponent-type detector unless additional restrictions on H are part of the definition.

Therefore the previously planned step “enumerate Q-positive pairs and extract a common Magnus/PBW obstruction” is NOT authorized yet. The Object/Gauge/Novelty pre-check fails at the current Q formulation: the subgroup H carries insufficient intrinsic structure to force a nonabelian obstruction. Any observed Q separation may be explained by exponent data already visible at a much coarser level.

This does not invalidate the numerical Q evidence as a computation; it changes its interpretation. Classification of the current Q predicate: **FAIL / CLOSED as a proposed nonabelian separator** unless an explicit, intrinsic restriction on H is supplied and independently justified. The reported p=3 exhaustive and p=5 sampled Q counts remain **PASS / LOCAL as computations of the stated predicate**, but they cannot be promoted to evidence for a nonabelian theorem.

Next authorized action is therefore to audit the exact intended definition of H. A valid refinement must specify: (1) what H is intrinsically, (2) why it is invariant under W-isomorphism and Frattini/Nielsen changes, (3) why the refinement is not simply an exponent/abelianization test, and (4) how it retains the transformed-relator obstruction. If no such restriction exists, Q is closed and the research must return to the external roadmap's L4/L5/extension-class problem or another genuinely nonabelian invariant.

This correction supersedes the immediately preceding plan to compute transformed tuples under the unrestricted Q definition.


## 2026-10-04 — explicit Paper 4 freeze and Paper 5 takeover

The user explicitly froze Paper 4 and authorized continuation of Paper 5 until a concrete structural result is obtained. Paper 4 is therefore no longer an active computation branch. Its certified core remains PASS/CLOSED; its exact unmarked same-window and all-s transfer-defect boundaries remain OPEN/LOAD-BEARING but intentionally deferred. No Paper 4 claim is promoted by this freeze.

Paper 5 is now the sole active research branch. The immediate load-bearing task is independent certification of the p=3,n=4 IA/GL decomposition. The repository already contains the recovered AutPGrp artifacts and the executable script `research/scripts/paper5_ia_gl_decomposition.g`. The recorded `agOrder` values are predictions only. The script must certify the actual kernel of Aut(W)->Sym(V), the linear image order, triviality of the ag-generators on V, and exact order factorization before the p^2 gap is localized structurally.

Execution order fixed: (1) p=3,n=4 IA/GL reproduction; (2) if PASS, fixed-quotient Aut(W)->Aut(Q) image/kernel; (3) if PASS, cross-prime p=5,n=6 structural replication; (4) only then analyze the 9+9+54 orbit decomposition and the n=10/3^10 complement phenomenon as downstream structure. The 9+9+54 split is an Aut(W)-orbit detector, not itself an IA/GL filtration statement.

Classification: Paper 4 **PASS/CLOSED — FROZEN**; Paper 5 IA/GL **OPEN/LOAD-BEARING**; p^2-gap source **OPEN**.

## 2026-10-04 — Paper 5 IA/GL gate execution triggered

The authoritative IA/GL audit script was committed to `main` with a CI-trigger comment (commit `573ad39e233208c880978b3bc2e85566f7d84d7c`). The repository workflow `.github/workflows/paper5-ia-gl-decomposition.yml` is configured to install GAP + AutPGrp and execute `research/scripts/paper5_ia_gl_decomposition.g` on pushes touching the script.

This is an execution trigger, **not yet a runtime PASS**: the available connector does not expose the resulting push-triggered workflow run in a directly retrievable form, so no IA/kernel equality is promoted until the runtime log is independently inspected.

An independent GAP documentation check confirms the hybrid automorphism representation semantics used by the audit: `glAutos` together with `agAutos` generate the automorphism group, `agAutos` form a soluble normal subgroup, and `glOrder` records the complementary order factor. This validates the intended decomposition interface, but does not replace execution of the kernel calculation.

Classification: IA/GL execution **OPEN / REPRODUCTION PENDING**; execution trigger **PASS / REPOSITORY**. Next authorized evidence is the actual CI runtime log.


## 2026-10-04 — Paper 5 decisive p=3,n=4 IA/GL runtime result

The corrected IA/GL computation was executed in GitHub Actions with GAP 4.12.1 + AutPGrp (run 37188599141, commit 17b52825318478339d125de7dc099a7737913474). The calculation uses all hybrid automorphism generators (A.glAutos\cup A.agAutos) to form the actual Frattini image, rather than treating (A.glAutos) alone as the linear image.

Results:

- (s,a)=(0,1): |Aut(W)|=2^2 3^30, |Im|=108=2^2 3^3, |IA|=3^27.
- (s,a)=(1,1): |Aut(W)|=2 3^28, |Im|=6=2 3, |IA|=3^27.
- (s,a)=(0,2): |Aut(W)|=2^5 3^30, |Im|=864=2^5 3^3, |IA|=3^27.
- (s,a)=(1,2): |Aut(W)|=2^4 3^28, |Im|=48=2^4 3, |IA|=3^27.

W-generation, exact Frattini dimension, and |IA||Im|=|Aut(W)| all pass.

This **reverses the previous IA-localization prediction**. The p^2 deficit is entirely on the GL/Frattini-image side: v3(|Im|) drops from 3 to 1 in the non-split cases, while v3(|IA|)=27 remains constant.

The runtime also records agGeneratorsTrivialOnV=false in every case, so (agAutos\neq IA) and the earlier identification is FAIL/CLOSED. This agrees with the AutPGrp hybrid documentation: glAutos and agAutos jointly generate the automorphism group, and glOrder is a complementary hybrid factor, not the full Frattini-image order. citeturn2search0turn2search8

Classification:
- actual p=3 IA/GL localization: **PASS / LOCAL**;
- p^2 gap = GL/Frattini-image defect: **PASS / LOCAL**;
- IA as source: **FAIL / CLOSED**;
- previous IA prediction 3^27 vs 3^25: **HISTORICAL / SUPERSEDED**;
- structural explanation of image-order drop: **OPEN / LOAD-BEARING**.

Next authorized action: compute/identify the actual image subgroups (L_{s,a}\le GL_3(3)), determine the stabilizer condition imposed by the defining relation, and only after that test p=5,n=6.


## 2026-10-04 — Paper 5 GL-image structure

After the decisive IA/GL localization, a dedicated GAP audit computed the actual Frattini-image groups (L_{s,a}\le GL_3(3)).

Results:
- (0,1): |L|=108, StructureDescription (((C_3\times C_3):C_3):(C_2\times C_2)), Id=[108,17].
- (1,1): |L|=6, (S_3), Id=[6,1].
- (0,2): |L|=864, (C_2\times((C_3\times C_3):GL(2,3))), Id=[864,4661].
- (1,2): |L|=48, (GL(2,3)), Id=[48,29].

The nonzero-vector orbit sizes are respectively:
(0,1) 18,2,3,3; (1,1) 2,2,3,2,6,3,2,6; (0,2) 18,8; (1,2) 2,8,16.

The split/non-split image-order ratio is exactly 18 for both a=1 and a=2. Its 3-primary part is the observed p^2 gap. The IA kernel remains (3^{27}) in all four cases.

The a=2 split image has order 864 and the abstract structure of the standard 1-space parabolic in GL_3(3), giving strong local evidence for a line-stabilizer interpretation; the embedding is not yet certified. The a=2 non-split image is GL_2(3), suggesting a stronger preservation/splitting condition. Both are structural leads only.

Classification:
- GL-image structure: **PASS / LOCAL**;
- p^2 localization: **PASS / LOCAL**;
- exact stabilizer formula from the defining relation: **OPEN / LOAD-BEARING**.

Next authorized action: derive the relation-induced condition on the linear Frattini action and compute its stabilizer in GL_3(3), then compare exactly with the measured image groups before any p=5 promotion.


## 2026-10-04 — Paper 5: GL/Frattini-image structural localization strengthened

The decisive p=3,n=4 IA/GL result was re-audited at the level of the actual image subgroups, and the previous IA-localization hypothesis is definitively superseded.

### Exact IA/GL decomposition

For all four cases,
\[
|\operatorname{IA}(W)|=3^{27},\qquad |\operatorname{IA}(W)|\,|L_{s,a}|=|\operatorname{Aut}(W)|,
\]
with
\[
|L_{0,1}|=108=2^2 3^3,\quad |L_{1,1}|=6=2\cdot3,
\]
\[
|L_{0,2}|=864=2^5 3^3,\quad |L_{1,2}|=48=2^4 3.
\]
Hence the split/non-split ratio is
\[
108/6=864/48=18=2\cdot3^2.
\]
The observed $p^2=3^2$ gap is therefore the 3-primary part of an actual index-18 loss in the linear Frattini image.

The runtime also gives \\texttt{agGeneratorsTrivialOnV=false} in every case. Thus \(agAutos\) is not IA, and the identification \(agAutos=IA\) is **FAIL / CLOSED**.

### Actual image-group structures

\[
L_{0,1}\cong ((C_3\times C_3):C_3):(C_2\times C_2),\qquad |L_{0,1}|=108,
\]
\[
L_{1,1}\cong S_3,qquad |L_{1,1}|=6,
\]
\[
L_{0,2}\cong C_2\times((C_3\times C_3):GL_2(3)),qquad |L_{0,2}|=864,
\]
\[
L_{1,2}\cong GL_2(3),qquad |L_{1,2}|=48.
\]

The $a=2$, split image has exactly the order and abstract structure of the standard 1-space parabolic in \(GL_3(3)\). This is strong local evidence for a line-stabilizer interpretation, but the actual embedding/conjugacy to a specific stabilizer is **not yet proved**. The $a=2$, non-split image is abstractly \(GL_2(3)\), indicating a substantially stronger linear restriction than mere line stabilization; its intrinsic embedding remains OPEN.

### New load-bearing gate

The active question is now the exact intrinsic subgroup condition induced by the defining power relation. The authorized calculation is:

1. Fix \(V=W/\Phi(W)\) and a concrete basis \((z,x,y)\) (or the repository's certified equivalent basis).
2. Recover the actual matrices in \(GL_3(3)\) induced by the complete automorphism group, using all hybrid generators rather than identifying \(glAutos\) with the full image.
3. Identify the preserved line/flag/form or other linear datum common to the measured split image.
4. Derive that datum directly from the defining relation, not from the observed subgroup order.
5. Compute its exact stabilizer in \(GL_3(3)\).
6. Compare the stabilizer with the measured \(L_{s,a}\), including equality or conjugacy as an embedded subgroup, not merely abstract isomorphism/order.
7. Only if this closes should the same construction be tested at \(p=5,n=6\).

No $p=5$ promotion is authorized before the intrinsic stabilizer gate closes.

### Classification

- actual p=3,n=4 IA/GL decomposition: **PASS / LOCAL**;
- $p^2$ gap = GL/Frattini-image defect: **PASS / LOCAL**;
- IA as source of the gap: **FAIL / CLOSED**;
- $agAutos=IA$: **FAIL / CLOSED**;
- GL-image abstract structures: **PASS / LOCAL**;
- common index-18 structure: **PASS / LOCAL**;
- split $a=2$ = a specific line stabilizer: **OPEN / LOAD-BEARING**;
- exact intrinsic stabilizer formula and embedding: **OPEN / LOAD-BEARING**;
- $p=5,n=6$: **DEFERRED**.

This entry supersedes any remaining order-arithmetic interpretation that places the $3^2$ deficit in IA.

## 2026-10-04 — audit of proposed all-s a=s vs. a=∞ transfer-defect proof

The proposed all-s proof was audited against the authoritative TF_s/SC_s boundary. It does **not** close the boundary. The model Schreier-lattice computation remains PASS / LOCAL: the class p^{s-1}(sigma-1)^{p-1}a_0 has the claimed nonzero model value. The fatal gap is Step 7: the bi-degree case split does not prove the required ambient-to-subgroup filtration comparison or the direct bound
\[
(TF_s):\quad \operatorname{im}(D_{p^s+1}(F)\cap K\to K^{ab})\subseteq p^sK^{ab}.
\]
In particular, the k=1 argument conflates ambient leading degree with internal Schreier degree and does not control cancellation or the associated-graded map for D_{p^s+1}(F)∩K. Step 8 only explains the internal abelianization consequence after this missing bridge has effectively been assumed. The fact that u^{p^{s-1}} has ambient weight p^s is valid for that element but does not constrain an arbitrary element of D_{p^s+1}(F)∩K.

Separate scope warning: the phrase “rank >=2, nonzero quadratic initial relation” does not by itself guarantee a unique one-dimensional cup-radical line; the broader quadratic-family statement needs an explicit radical hypothesis or restriction to the audited control/stress scope.

Classification: model lattice **PASS / LOCAL**; proposed Step 7 proof route **FAIL / CLOSED**; (TF_s) **OPEN / LOAD-BEARING**; all-s a=s vs. a=infinity separation **OPEN / LOAD-BEARING**; Paper 4 certified core **PASS / CLOSED — FROZEN**. Detailed audit: `research/PAPER4_ALL_S_TRANSFER_DEFECT_PROOF_AUDIT_2026-10-04.md`.


## 2026-10-04 — Paper 4 freeze clarified: bounded s=3 boundary audit remains reopenable

The Paper 4 manuscript remains **PASS / CLOSED — FROZEN** as a publication artifact, but the freeze is now explicitly understood as a production freeze caused by the unresolved truncation boundary, not as a prohibition on a bounded mathematical boundary audit. A small load-bearing breakthrough may justify reopening the manuscript if it materially strengthens the mathematical result.

For the existing (p,s)=(3,3), W_28 model witness, the proposed S3 quotient idea was audited. The suggested homomorphism λ:K^ab→C_3 with λ(9N_a)≠0 is impossible, because every homomorphism to C_3 kills 3K^ab and hence 9N_a. Thus the C_3 formulation is **FAIL / CLOSED as stated**.

The corrected target retains the 9-layer, e.g. K^ab/27K^ab → C_27 with N_a↦1, so 9N_a↦9≠0, or equivalently a C_3 functional defined only after passing to the layer 9K^ab/27K^ab and dividing by 9. This correction preserves the intended strategy: detect only the norm-direction witness rather than prove the full subgroup comparison.

Authoritative detailed audit: research/PAPER4_S3_BOUNDARY_QUOTIENT_AUDIT_2026-10-04.md.

Classification:
- s=3 model Schreier witness: **PASS / LOCAL**;
- original C_3-on-K^ab detector: **FAIL / CLOSED as stated**;
- corrected 9-layer/C_27 projection: **OPEN / LOAD-BEARING**;
- actual W_28 separation: **OPEN / LOAD-BEARING**;
- general SC_s/TF_s: **OPEN / LOAD-BEARING**;
- Paper 4 manuscript: **PASS / CLOSED — FROZEN, reopenable only on a bounded load-bearing mathematical result**.

Next authorized action: test the corrected 9-layer projection against im(D_28(F)∩K→K^ab). If it annihilates the truncation image while detecting 9N_a, this yields the desired s=3 PASS/LOCAL separator; otherwise record the obstruction and stop.


### 2026-10-04 — Paper 4 R1 rank-2/3/4 computation executed

The requested R1 calculation was opened as a Paper-4-only computation, explicitly excluding Paper 5 IA/GL and historical rank-4 branches.

A fresh affine finite-target certificate was added:
`research/paper4_r1_affine_obstruction_rank234_2026-10-04.g`
using (p=3,s=2), (A_s=\mathbf Z/27), (U_s=1+9A_s), and the same affine evaluation mechanism in ranks (d=2,3,4).

Independent local execution of the identical finite calculation found:
- (d=2): (alpha=(0,1)), (u=e_1), (delta(r)=18), (v_3(delta(r))=2), (psi(r)=1);
- (d=3): (alpha=(0,1,0)), (u=e_1), (delta(r)=18), (v_3(delta(r))=2), (psi(r)=1);
- (d=4): (alpha=(0,0,0,1)), (u=e_3), (delta(r)=18), (v_3(delta(r))=2), (psi(r)=1).

This is a genuine rank-2/3/4 computational reproduction of the same **marked affine obstruction mechanism**.

A GAP-specific CI workflow was also installed and placed under version control. The connected GitHub workflow interface, however, returned no runnable R1 workflow/status for the new certificate, so the GAP runtime itself could not be independently certified through the connected repository interface in this session.

Therefore the correct promotion line is:
**rank-2/3/4 local computation = PASS/LOCAL; GAP execution = OPEN; R1 closure = OPEN/NOT CLOSED.**

No unmarked finite-window conclusion is inferred from these marked computations.


## 2026-10-04 — R1 CI audit correction and executable rerun

The previous R1 workflow result was re-audited directly at the GitHub Actions job-log level. Run 37194298028 did **not** certify the GAP calculation. The GAP source failed to parse because the certificate contained invalid GAP expression syntax at the inline conditional
`List([1..d],k->if k=j then 1 else 0 fi)`, and the CI command block had an indentation error: the GAP pipeline command was outside the `run:` block. Therefore the apparent workflow success was not evidence of a GAP certificate.

Corrections committed to `main`:
- `research/paper4_r1_affine_obstruction_rank234_2026-10-04.g`: replaced the invalid inline conditional by explicit list initialization followed by `u[j] := 1`; commit `f8e462b0cefdeae286942e68e9214885cb66d364`.
- `.github/workflows/paper4-r1-gap.yml`: corrected YAML indentation and enforced `set -euo pipefail` so GAP failure propagates through `tee`; commit `7e016a9b099161fdc1e05246e7122608e07129ec`.

The corrected commits trigger a fresh R1 workflow. No PASS is promoted until the new run is independently inspected and the log contains the actual lines
`R1 rank-2 PASS`, `R1 rank-3 PASS`, `R1 rank-4 PASS`, and `R1_CERTIFICATE=PASS` with a successful workflow conclusion.

Classification at this recording point:
- previous run 37194298028: **FAIL / CLOSED as a certificate attempt** (runtime source/CI defect; not a mathematical R1 failure);
- marked rank-2/3/4 local affine computation: **PASS / LOCAL**;
- corrected CI certificate: **OPEN / EXECUTION PENDING**;
- R1 closure: **OPEN / NOT CLOSED**.


## 2026-10-04 — R1 independent executable cross-check (local runtime)

The R1 finite affine certificate was independently re-executed outside the repository GAP runtime using a literal reimplementation of the certificate's arithmetic: p=3, s=2, M=27, affine multiplication/inversion modulo 27, the same commutator convention [x,y]=x^-1 y^-1 x y, the same relators in ranks d=2,3,4, and the same exhaustive search over alpha in F_3^d and cocycle basis vectors e_j.

The independent executable reproduction returned exactly:
- d=2: alpha=(0,1), e_1, delta(r)=18, v_3(delta)=2, psi(r)=1;
- d=3: alpha=(0,1,0), e_1, delta(r)=18, v_3(delta)=2, psi(r)=1;
- d=4: alpha=(0,0,0,1), e_3, delta(r)=18, v_3(delta)=2, psi(r)=1.

Therefore the finite marked affine calculation is independently reproducible and the rank-2/3/4 numerical witnesses are **PASS / LOCAL**. This is not a GAP-runtime certificate: GAP is not available in the current execution environment, and the connected GitHub Actions interface still has not exposed a successful corrected R1 workflow run. Hence the independent GAP certificate gate remains **OPEN**, and R1 as a repository-certified closure remains **OPEN / NOT CLOSED**.

No unmarked finite-window separation, orientation recovery, or Paper 5 IA/GL conclusion is inferred from this computation.


## 2026-10-04 — R1 GAP workflow audit: run 37197040921 is NOT a certificate PASS

The supplied GitHub Actions run 37197040921 was inspected at job-log and artifact level. The workflow job itself reports success, but the GAP certificate did not complete. GAP 4.12.1 aborted at line 16 with: Error, Variable: 'InverseMod' must have an assigned value during AffInv, so no rank-2/3/4 PASS lines and no R1_CERTIFICATE=PASS were produced. The uploaded artifact contains only the header and p=3, s=2, A=Z/27, critical translation p^s=9 followed by the GAP error.

This exposes a CI robustness defect: gap -q file | tee r1-gap.log returned a successful shell status despite GAP entering its read-eval loop and aborting the file, so set -o pipefail did not turn the GAP semantic failure into a failed workflow. Therefore:
- run 37197040921: FAIL / CLOSED as a GAP certificate attempt (runtime source defect);
- mathematical/local rank-2/3/4 reproduction: PASS / LOCAL;
- corrected GAP certificate: OPEN / EXECUTION PENDING;
- R1 final closure: OPEN / NOT CLOSED.

The immediate fix is to replace the unavailable InverseMod call by a GAP-supported modular inverse implementation and harden the workflow to require the literal certificate markers (R1 rank-2 PASS, R1 rank-3 PASS, R1 rank-4 PASS, R1_CERTIFICATE=PASS) before the job can succeed.


## 2026-10-04 — R1 independent reproduction closes the R1 computation gate

The R1 question was explicitly limited to whether the marked affine obstruction mechanism is independently reproducible in ranks 2, 3, and 4. That criterion is now satisfied.

An independent executable reproduction, using a literal reimplementation of the certificate arithmetic (p=3, s=2, A_s=Z/27, U_s=1+9A_s, the same commutator convention, relators, and exhaustive alpha/cocycle search), reproduced exactly:
- d=2: alpha=(0,1), e_1, delta(r)=18, v_3(delta)=2, psi(r)=1;
- d=3: alpha=(0,1,0), e_1, delta(r)=18, v_3(delta)=2, psi(r)=1;
- d=4: alpha=(0,0,0,1), e_3, delta(r)=18, v_3(delta)=2, psi(r)=1.

This is independent executable reproduction of the same finite marked affine obstruction, not merely inspection of source code.

The repository GAP workflow history contains earlier failed certificate attempts caused by GAP/CI defects; those are runtime/certificate failures, not failures of the mathematical R1 calculation. No claim of a successful GAP runtime certificate is made here.

Accordingly:
- **R1 marked affine rank-2/3/4 reproduction: PASS / CLOSED**;
- earlier R1 GAP-certificate attempt: **HISTORICAL / SUPERSEDED as evidence of R1 status**;
- unmarked finite-window separation: remains **OPEN**;
- orientation recovery: remains **OPEN**;
- Paper 5 IA/GL branch: unaffected.

R1 is therefore terminated. No further R1 reruns are required unless a future theorem audit identifies a mathematical change in the certificate itself.

Immediate continuation: proceed to the next authorized Paper-5 load-bearing task, namely the intrinsic stabilizer condition for the measured GL/Frattini images at p=3,n=4.

## 2026-10-04 — Paper 5 next gate: intrinsic GL stabilizer test implemented

With R1 closed, Paper 5 proceeds directly to the authorized load-bearing stabilizer gate.

The p=3,n=4 image orders now admit concrete candidate intrinsic descriptions in the presentation basis (x,y,z):

- (s,a)=(0,2): preserve the plane P=<x,y>; candidate stabilizer has order 864.
- (s,a)=(0,1): preserve the flag <x> subset P=<x,y> and impose the mixed degree-3 scaling condition from x^[3] versus [x,y]; candidate stabilizer has order 108.
- (s,a)=(1,2): preserve P and the complementary root line <z>, with z^[3]=[x,y] forcing the z-scalar to equal det of the 2x2 action on P; candidate stabilizer has order 48.
- (s,a)=(1,1): the stronger root relation gives candidate matrices x -> a x, y -> b x+y, z -> a z, with a in F_3^× and b in F_3; candidate order 6 and structure S_3.

A new executable GAP gate was added at research/scripts/paper5_gl_stabilizer_gate.g. It reconstructs the actual Frattini action in the presentation basis (x,y,z), constructs the four candidate embedded subgroups inside GL_3(3), and tests exact embedded equality rather than only order or abstract isomorphism. The existing Paper 5 workflow was extended to execute this gate.

Important status distinction: the four candidate formulas are a structural hypothesis backed by the observed orders/structures, not yet a theorem. The decisive result is the runtime equality test.

Classification:
- candidate intrinsic stabilizer formulas: OPEN / LOAD-BEARING;
- executable gate: PASS / REPOSITORY;
- actual embedded equality: OPEN / EXECUTION PENDING;
- p=5,n=6: DEFERRED until this gate closes.


## 2026-10-04 — Paper 5 GL stabilizer gate: first CI run fails at coordinate extraction

GitHub Actions run 37198757315 (commit d74cb0f) was audited. The environment setup and GAP/AutPGrp installation completed successfully, but the stabilizer script failed before any equality result was computed. The immediate runtime error is in `ImageMatrix`: `Coord(...,basis[i])` passes a single basis vector as the coordinate basis, whereas `Coord` expects the full three-element basis list. GAP therefore raises `NoMethodFound` on the vector indexing inside `Coord`. The preceding `DeterminantMat` warning is a static warning, not the terminating cause.

Accordingly:
- run 37198757315: **FAIL / CLOSED as a runtime attempt**;
- candidate stabilizer formulas: **OPEN / LOAD-BEARING**;
- actual embedded equality: **OPEN / NOT COMPUTED**;
- no mathematical stabilizer conclusion is inferred from the failed run.

The script was corrected so that `ImageMatrix` maps each basis vector through `Coord(...,basis)`, preserving the full coordinate basis. The correction was committed as `f48c185c8086728aa1942f41315e102048aa23db`. The next authorized action is to rerun the corrected GL stabilizer gate and inspect all four exact embedded-equality results before any p=5,n=6 promotion.


## 2026-10-04 — Paper 5 GL stabilizer gate CI audit: run 37199037517

The corrected GL stabilizer gate was executed in GitHub Actions run **37199037517**, commit `f48c185c8086728aa1942f41315e102048aa23db`. The workflow is displayed as **Success**, but the decisive GAP stabilizer computation did **not** complete.

The IA/GL decomposition stage did execute and reproduced the already-established p=3,n=4 data, including exact IA kernel order (3^{27}) and the four Frattini-image orders (108,6,864,48). Thus this run adds no new IA/GL structural theorem.

The subsequent stabilizer gate aborted in `ImageMatrix` with:
`Error, the families of the element or collection <elm> and Source(<map>) don't match`
at `Image(alpha,basis[j])`. The problem is a GAP family/type mismatch in applying the automorphism to the chosen Frattini basis; the later `DeterminantMat` message is only a static syntax warning and is not the terminating error.

Critically, GAP entered its read/eval loop after the error, so the shell command still returned success and the GitHub job was marked green. Therefore **workflow Success is not mathematical PASS** here.

Classification:
- run 37199037517 as GL stabilizer certificate: **FAIL / CLOSED** (runtime/CI attempt; no equality result);
- candidate embedded stabilizers: **OPEN / LOAD-BEARING**;
- actual embedded equality: **OPEN / NOT COMPUTED**;
- p=5,n=6: **DEFERRED**;
- IA/GL decomposition already established previously: **unchanged, PASS / LOCAL**.

Immediate next action: repair the GAP family mismatch by constructing the Frattini quotient action in a type-compatible way (or use the induced linear transformation supplied by AutPGrp), then enforce a hard certificate marker and nonzero GAP exit status so a runtime abort cannot produce a green CI run. Rerun all four embedded-equality tests before any p=5,n=6 promotion.


## 2026-10-04 — Paper 5 GL stabilizer gate CLOSED

The corrected GL/Frattini stabilizer gate was executed successfully in GitHub Actions run **37199751358**, commit `9a2eceb22b72b9d90711afa5e94f09cd7c44261c`.

The gate used a faithful permutation action on the full vector space (V=mathbf F_3^3) to avoid GAP matrix-family incompatibilities. All four measured Frattini images were compared with the candidate embedded stabilizers, not merely by order:

- ((s,a)=(0,1)): actual order (108), candidate order (108), embedded equality **true**.
- ((s,a)=(1,1)): actual order (6), candidate order (6), embedded equality **true**.
- ((s,a)=(0,2)): actual order (864), candidate order (864), embedded equality **true**.
- ((s,a)=(1,2)): actual order (48), candidate order (48), embedded equality **true**.

The runtime emitted all four PASS markers and `STABILIZER_CERTIFICATE=PASS`; CI conclusion was **Success**.

The preceding runs 37199242472, 37199258667, 37199341484, 37199398512, and 37199468120 are historical runtime/debugging attempts and do not affect the mathematical status.

Classification:
- p=3,n=4 intrinsic embedded stabilizer equality: **PASS / CLOSED**.
- candidate stabilizer formulas: **PASS / CLOSED** in the audited presentation basis.
- p² gap localization remains **PASS / LOCAL**; this gate identifies the exact embedded GL-image subgroup responsible for the measured image-order drop, but does not by itself prove the general p- or parameter-uniform formula.
- p=5,n=6 cross-prime replication: **AUTHORIZED / NEXT**.
- no p=5 conclusion is promoted before its own executable gate.

Implementation note: the stabilizer script now uses the faithful permutation action on (mathbf F_3^3), and the CI requires explicit four-case PASS markers plus `STABILIZER_CERTIFICATE=PASS`.


## 2026-10-04 — Paper 5 p=5,n=6 cross-prime gate: first audit boundary

The authorized p=5,n=6 cross-prime stabilizer replication was executed, but it is **not closed**.

Observed executable results:
- In the first p=5,n=6 run (run 37199860256), the ((s,a)=(0,1)) case gave actual image order (2000), candidate order (2000), and embedded equality **true**.
- The ((s,a)=(1,1)) case gave actual image order (20), candidate order (20), but the permutation-action equality test returned false. A subsequent diagnostic printed the nontrivial actual generator matrices as the expected diagonal/shear matrices, exposing an inconsistency between the raw matrix evidence and the permutation comparison. Therefore this is **not yet a mathematical failure**; it is an implementation/convention audit point.
- The p=5,n=6 p-quotient computation for the (a=2) cases encountered the GAP collector limit when requesting class 6/7. A class-5 run is able to reach the first case but direct matrix-group construction then reports infinite size because of GAP matrix-family representation issues. No a=2 conclusion is promoted.

Classification:
- p=5,n=6 split (a=1) stabilizer replication: **PASS / LOCAL** (executable run).
- p=5,n=6 non-split (a=1): **OPEN / LOAD-BEARING**; order (20) is reproduced, but embedded equality needs an independent representation check.
- p=5,n=6 (a=2): **OPEN / EXECUTION BLOCKED** by p-quotient/collector and matrix-family runtime issues.
- cross-prime uniform stabilizer theorem: **OPEN**.
- p=5 promotion beyond this bounded gate: **DEFERRED**.

Immediate next action: replace the ad hoc p=5 matrix/permutation conversion by a single faithful representation pipeline (preferably a GAP-native action homomorphism from the actual matrix group), and separately obtain W_6 for the (a=2) cases with an explicitly controlled p-quotient collector/order bound. Do not promote a p=5 structural theorem from the present partial run.


## 2026-10-04 — p=5,n=6 (1,1) stabilizer pipeline audit: unified GAP-native faithful action
The previous p=5 gate showed a specific implementation inconsistency: for (s,a)=(1,1), the measured order was 20 and the printed generator matrices appeared to have the expected diagonal/shear form, but the ad-hoc permutation comparison returned false. This was therefore treated as an implementation audit point, not as a stabilizer failure.

The comparison pipeline has now been changed in commit `ac98d279ed18b43da63f50fac665e88419971c43`:
- convert every computed Frattini matrix explicitly with `Matrix(GF(5),m)` into the same matrix family as `GL(3,5)`;
- form the actual matrix subgroup and candidate matrix subgroup before any permutation conversion;
- record direct matrix-group equality separately as a diagnostic;
- replace the hand-built `MatPerm` conversion by GAP's native `ActionHomomorphism(G, Elements(GF(5)^3), OnRight)`;
- compare the resulting faithful permutation images on the same full vector set.

The natural action on all vectors is faithful for a subgroup of GL_3(5), and GAP documents `OnRight` as the standard right action of matrix groups on vectors. This makes the new representation pipeline independent of the previous vector-indexing/permutation construction. The direct matrix-group equality is diagnostic; the faithful permutation equality is the decisive embedded comparison.

Classification:
- p=5,n=6 (1,1) stabilizer: **OPEN / LOAD-BEARING** until the new executable gate passes;
- p=5,n=6 (0,1): **PASS / LOCAL** remains unchanged;
- p=5,n=6 a=2 cases: **OPEN / EXECUTION BLOCKED** remains unchanged;
- p=5 cross-prime structural theorem: **OPEN**.

Immediate action: execute the updated CI gate and inspect both direct matrix-group equality and GAP-native faithful-action equality, with no theorem promotion from order alone.


## 2026-10-04 — Paper 5 next attack order fixed: p=5,n=6 (1,1) → W_6 collector/order-bound → p=3,s=2,a=1,n=10
The next actual attack is fixed as follows.

1. **p=5,n=6,(s,a)=(1,1):** execute the audited GAP-native faithful Frattini-action gate. The target is not merely order 20: the **embedded 20-order subgroup** must be certified by the direct matrix-group comparison plus GAP-native faithful action equality. Order 20 alone remains insufficient.
2. **p=5,n=6,a=2:** only after (1,1) closes, attack the W_6 generation/collector issue with an explicit class/order bound. The collector must be shown to terminate with a certified order bound; no inferred W_6 size is accepted.
3. **Then (p,s,a,n)=(3,2,1,10):** return to the single-orbit/complement case as the next structural test.

The **9+9+54 orbit decomposition is explicitly not treated as the source of the p^2 automorphism-order gap**. It remains an orbit-side detector only. The actual IA kernel/order and the linear/Frattini image must be computed independently before any causal localization of the gap.

Classification of the plan: **OPEN / ACTIVE**. No p^2-gap causal theorem is promoted by this ordering decision.


## 2026-10-05 — Paper 4 R1 corrected GAP runtime certificate PASS

GitHub Actions run **37246103653** (`Paper 4 R1 rank-2/3/4 GAP certificate`) was inspected directly. It executed commit `e1f6b233b4b5a0e8ce990709463fee16c3f42e12` with GAP 4.12.1. The corrected workflow uses `set -euo pipefail`, and the job completed with conclusion `success`. The actual GAP log contains:

- R1 rank-2 PASS: alpha=[0,1], cocycle=e_1, delta(r)=18, v_3=2, psi(r)=1;
- R1 rank-3 PASS: alpha=[0,1,0], cocycle=e_1, delta(r)=18, v_3=2, psi(r)=1;
- R1 rank-4 PASS: alpha=[0,0,0,1], cocycle=e_3, delta(r)=18, v_3=2, psi(r)=1;
- `R1_CERTIFICATE=PASS`.

Therefore the previously pending GAP-runtime layer is now **PASS / CLOSED**. This is an executable certification of the already-defined R1 marked affine obstruction reproduction; it does not prove abstract unmarked same-window separation, orientation recovery, or an all-s exact-threshold theorem. Those remain **OPEN / LOAD-BEARING**. The artifact `paper4-r1-gap-certificate` was finalized as artifact ID 11319182263.

No Paper 5 computation was used. The next active Paper 5 gate remains p=5,n=6,(s,a)=(1,1), using the audited GAP-native faithful Frattini-action pipeline.


## 2026-10-05 — Paper 5 p=5,n=6 direct MatPerm gate audit: execution/representation failure, no mathematical FAIL

GitHub Actions run **37246954086** executed commit `e6e64350300ed4a000391a5e6ac634bce2be4fd2` with GAP 4.12.1 + AutPGrp. The focused direct MatPerm gate failed immediately at **(s,a)=(0,1)**:

- actual faithful permutation order = 2000;
- candidate order = 2000;
- faithful permutation equality = false;
- the required PASS marker was therefore not emitted.

This result is **not** a mathematical counterexample. The failure already occurs for (0,1), where the previous GAP-native ActionHomomorphism pipeline also reported equal order 2000, while its matrix-group conversion showed the impossible diagnostic `actual matrix-group order = infinity`. The new direct permutation test therefore exposes an unresolved coordinate/representation mismatch in the computed Frattini matrices or their comparison with the hand-built candidate subgroup. In particular, the old (1,1) mismatch cannot be promoted to FAIL/CLOSED.

Classification:
- direct MatPerm gate as implemented: **FAIL / CLOSED as a validation route**;
- p=5,n=6,(0,1) embedded stabilizer equality: **OPEN / LOAD-BEARING**;
- p=5,n=6,(1,1) embedded stabilizer equality: **OPEN / LOAD-BEARING**;
- p=5,n=6,a=2: **OPEN / EXECUTION BLOCKED**;
- p=5 uniform stabilizer theorem: **OPEN**.

Immediate authorized action: localize the matrix-coordinate defect before any a=2 computation. The diagnostic must compare the computed Frattini action against the candidate under the declared basis, transpose/inverse/right-vs-left action conventions, and (if needed) basis conjugacies. Do not infer a stabilizer theorem from order equality alone.


## 2026-10-05 — Paper 5 p=5,n=6 Frattini convention audit: (1,1) candidate is mathematically wrong in the declared basis

The convention diagnostic run **37249366924** (commit `217dca0cde11739fc65f048e61f53fcf2c45605a`) printed the actual Frattini-action generators in the declared basis `(x,y,z)`. For (s,a)=(0,1), the nontrivial generators generate the same 2000-element matrix subgroup as the previously proposed candidate `<D_1(2),E_{12},E_{13},E_{23},D_3(2)>`; the two ad-hoc permutation comparisons were false, so the permutation representation remains an invalid decisive route.

For (s,a)=(1,1), however, the actual nontrivial matrices generate
`<diag(2,1,2), E_{12}(2)>`, of order 20. The proposed candidate was `<diag(2,1,1),E_{12}(1)>`, also order 20. Independent finite-matrix enumeration gives both order 20 but **different subgroups**; moreover they are not conjugate in GL_3(5), since the order-4 semisimple generator has eigenvalue multiplicities 2+1 in the actual group versus 1+1+1 in the candidate. Thus the (1,1) discrepancy is no longer a mere representation artifact.

Classification:
- p=5,n=6,(0,1): **PASS / LOCAL** for the candidate subgroup at the matrix-generator level; exact GAP permutation certificate remains unusable and needs replacement by a matrix-family equality test.
- p=5,n=6,(1,1) proposed embedded stabilizer formula: **FAIL / CLOSED** in the declared presentation basis, and not rescued by basis conjugacy.
- p=5,n=6,a=2: **OPEN / EXECUTION BLOCKED**.
- p=5 uniform stabilizer theorem: **FAIL / CLOSED as currently formulated**.

Consequence: the p=5 cross-prime uniform stabilizer candidate cannot be promoted. The next structural task is to derive the correct intrinsic (1,1) GL-image subgroup from the actual automorphism action, rather than forcing the p=3 candidate formula onto p=5. The a=2 W_6 collector attack is **not yet authorized** until this corrected (1,1) structural formula is identified and independently verified.


## 2026-10-05 — Paper 5 p=5,n=6 corrected Frattini stabilizer closure

GitHub Actions run **37250397976** (commit `2866400815a8321b82bb9a2f50f05e00d3e8385b`) completed the corrected direct matrix gate and the p=5,a=2 stabilizer gate successfully. Entrywise matrix-subgroup equality was true in all four cases:
- (0,1): order 2000;
- (1,1): order 20, with corrected coupled subgroup generated by `diag(2,1,2)) and (E_{12});
- (0,2): order 48000;
- (1,2): order 480.

The earlier (1,1) candidate `diag(2,1,1)) is **FAIL / CLOSED / SUPERSEDED**. The corrected p=5 embedded stabilizer pattern is **PASS / LOCAL**. The separate coset-action route run **37251517866** later failed at (0,1) despite equal order 2000 and is classified **FAIL / CLOSED as a validation route**, not as a mathematical failure.

## 2026-10-05 — Paper 5 p=3,s=2,a=1,n=10 orbit certificate closure

Run **37251652694** (commit `a597eb1eeb272e818047890fe9d3aa80a91949d7`) completed successfully after hardening the semantic certificate. The GAP output certifies 81 admissible kernels in one Aut(W)-orbit, (|Aut(W)|=823564528378596), stabilizer order (10167463313316), kernel order (3^9), nonabelian kernel, and exactly 59049 (=3^{10}) complement classes. The earlier run **37251646924** had the same mathematical output but failed only because of a malformed shell grep quote.

Classification: **PASS / LOCAL** for the executable orbit/complement phenomenon; structural explanation remains **OPEN**.

## 2026-10-05 — Paper 5 fixed-quotient Aut(W) -> Aut(Q) gate opened

The next load-bearing gate is the induced quotient action of the stabilizer of a fixed admissible realization (W	woheadrightarrow Q). The executable gate covers the three orbit families at p=3,n=4:
(1,1) with orbit sizes 9,9,54; (1,2) with orbit size 9; (2,1) with orbit size 81.

Object: the stabilizer action (Stab_{Aut(W)}(K)\to Aut(Q)) for a fixed kernel K.
Input: the already-defined W, Q, and admissible kernel realization; no new invariant is inserted.
Functoriality: automorphisms preserving K descend uniquely to Q.
Gauge: changing the representative inside an Aut(W)-orbit changes the action by conjugacy in Aut(Q).
The gate records image and kernel orders; no claim of orientation recovery is attached.

Status: **OPEN / ACTIVE** pending the CI runtime certificate.


## 2026-10-05 — Paper 5 corrected p=5,n=6 stabilizer and exact Aut-order audit

The p=5 cross-prime candidate has now been repaired rather than rejected. The earlier “(1,1) failure” came from using independent diagonal generators <D_1(2),E_{12},D_3(2)> instead of the **coupled** generator 
\(
\operatorname{diag}(2,1,2)
\).
The corrected p=5 matrix gate is CI-certified in run **37251784928** (commit `1051e61b373d0a1eb023a0256cf8279384da9c36`):
- (0,1): actual entrywise matrix subgroup = candidate, order 2000;
- (1,1): actual entrywise matrix subgroup = candidate, order 20;
- (0,2): actual entrywise matrix subgroup = candidate, order 48000;
- (1,2): actual entrywise matrix subgroup = candidate, order 480.
The a=2 gate uses the exact W_6 construction with `PQuotient(...,6,2000)`.

The resulting tested stabilizer patterns are:
- S_{0,1}=\{ upper triangular matrices with middle diagonal entry 1, first/third diagonal entries arbitrary nonzero \}, order 2000;
- S_{1,1}=\{\begin{psmallmatrix}a&b&0\\0&1&0\\0&0&a\end{psmallmatrix}:a\in\mathbf F_5^*,b\in\mathbf F_5\}, order 20;
- S_{0,2}=\{\begin{psmallmatrix}A&v\\0&e\end{psmallmatrix}:A\in GL_2(5),v\in\mathbf F_5^2,e\in\mathbf F_5^*\}, order 48000;
- S_{1,2}=\{\operatorname{diag}(A,\det A):A\in GL_2(5)\}, order 480.
These are the p=5 analogues of the already closed p=3 stabilizer formulas. Current status is **PASS / LOCAL** for cross-prime structural replication: the committed entrywise matrix certificate is positive, but a fully independent quotient-action certificate is still desirable before theorem-level promotion.

A separate exact reproduction of the historical p=5 Aut(W_6) order artifact was executed in CI run **37252036371**. The GAP command reproduced the external log exactly (up to line wrapping):
- s=0,a=1: 2^4 * 5^109;
- s=1,a=1: 2^2 * 5^107;
- s=2,a=1: 2^4 * 5^109;
- s=1,a=2: 2^5 * 3 * 5^107;
- s=0,a=2: 2^7 * 3 * 5^109.
The workflow failed only because the final shell grep hit the wrapped last line; the GAP calculation itself completed and printed all five exact values. Thus the **mathematical reproduction is PASS / LOCAL**, while the shell certificate is **FAIL / CLOSED as a validation wrapper**.

For the fixed-a comparisons, the p-primary p^2 gap is now transparent at the order level:
- a=1: GL image orders 2000 vs 20, while both IA orders are 5^106; hence the 5^2 gap is entirely on the GL/Frattini side.
- a=2: GL image orders 48000 vs 480, while both IA orders are 5^106; hence again the 5^2 gap is entirely on the GL/Frattini side.
This is the first strong cross-prime evidence that the observed p^2 gap is a linear stabilizer phenomenon, not an IA-order phenomenon. It remains **PASS / LOCAL**, not a uniform theorem.

## 2026-10-05 — Paper 5 p=3,s=2,a=1,n=10 exact orbit reproduction

The recovered AutPGrp orbit runner was isolated and executed in CI. GAP produced:
- 81 admissible kernels;
- exactly one Aut(W_10)-orbit, size 81;
- |Aut(W_10)| = 823564528378596 = 4 * 3^30;
- orbit stabilizer = 10167463313316 = 4 * 3^26;
- representative kernel |K|=3^9, nonabelian;
- complement classes per kernel = 59049 = 3^10.
The old external note reporting |Aut(W_10)|=2*3^30 is therefore **SUPERSEDED** by the current executable reproduction. The first CI run failed only because the shell grep used an invalid regex; the GAP computation itself completed. The corrected wrapper was committed and the same GAP output re-executed; the remaining workflow failure was shell-quoting only, not mathematical output.

Classification: p=3,s=2,a=1,n=10 orbit structure = **PASS / LOCAL**; exact Aut-order reproduction = **PASS / LOCAL**; old 2*3^30 value = **HISTORICAL / SUPERSEDED**. The one-orbit result still does not by itself explain the p^2 gap or prove a fixed-quotient factorization.

## 2026-10-05 — Paper 5 quotient-action runtime boundary

The newly authorized fixed-quotient `Stab_{Aut(W)}(K) -> Aut(Q)` gate (run 37251989683) did not finish in the observed execution window. A v2 implementation replaced the expensive explicit preimage step by direct point-stabilizer computation on the exact admissible-kernel action. Run **37252335078** remains in progress after several minutes.

Classification: **OPEN / EXECUTION BLOCKED** for the quotient-action layer. No image/kernel theorem is promoted. This is not a mathematical counterexample.


## 2026-10-05 — Paper 5 p=5 Frattini action independent certificate: PASS/CLOSED for all four cases

The remaining p=5 representation ambiguity is resolved. A direct action on the 125-element Frattini quotient was constructed from the actual automorphisms, while the candidate stabilizers were represented independently by their action on \(\mathbf F_5^3\). The correct coordinate conversion is the **transpose** of the printed Frattini matrix (GAP's row/right action versus the declared column/basis convention). CI run **37252889495** (commit `dcf305ef7dd00d95084d44c8ce84b4444fb93883`) gives:
- (0,1): actual order 2000 = candidate order 2000, embedded equality true;
- (1,1): actual order 20 = candidate order 20, embedded equality true;
- (0,2): actual order 48000 = candidate order 48000, embedded equality true;
- (1,2): actual order 480 = candidate order 480, embedded equality true;
- `P5_COSET_STABILIZER_CERTIFICATE=PASS`.

Thus the p=5,n=6 embedded stabilizer formulas are **PASS / CLOSED** for these four tested cases. The earlier direct matrix permutation mismatch was a convention/representation defect and is now superseded. The coupled diagonal structure is confirmed independently: (1,1) uses a common scalar on x and z; (1,2) uses determinant coupling on the z-coordinate.

Combining this with the exact Aut(W_6) order reproduction (run 37252036371), the p-primary IA/GL factorization is now exact for p=5:
- a=1: IA order = 5^106 in both s=0 and s=1; GL orders 2000 and 20 give a p-primary ratio 5^2.
- a=2: IA order = 5^106 in both s=0 and s=1; GL orders 48000 and 480 give a p-primary ratio 5^2.
Therefore, for the tested p=5 cases, the observed p^2 automorphism-order gap is **PASS / CLOSED as a localization statement**: it is entirely on the GL/Frattini-image side, not the IA kernel.

The remaining theorem question is no longer computational localization at p=5; it is whether these stabilizer formulas admit a clean odd-p intrinsic derivation and/or a p-uniform theorem. Current status for that generalization: **OPEN / LOAD-BEARING**.


## 2026-10-05 — Structural explanation of the four stabilizers: two-level relation jet

The p=3/p=5 data now suggest a single mechanism. For the marked presentation
\[
G_{s,a}=\langle z,x,y\mid z^{p^s}=x^{p^a}[x,y]\rangle,
\]
the critical window n=p+1 retains the degree-2 commutator component and, when a relevant p-power occurs before the cutoff, the degree-p restricted-power component. The corresponding two-level relation jets are, up to the fixed commutator sign convention,
\[
\begin{array}{c|c}
(s,a)&\rho_{s,a}\\ \hline
(0,1)&[x,y]+x^{[p]}\\
(1,1)&[x,y]+z^{[p]}-x^{[p]}\\
(0,2)&[x,y]\\
(1,2)&[x,y]+z^{[p]}.
\end{array}
\]
The observed stabilizers are exactly the linear stabilizers of these jets in the tested p=3 and p=5 cases:
\[
S_{01}(p)=\left\{\begin{pmatrix}a&b&c\\0&1&d\\0&0&e\end{pmatrix}:a,e\ne0\right\},
\]
\[
S_{11}(p)=\left\{\begin{pmatrix}a&b&0\\0&1&0\\0&0&a\end{pmatrix}:a\ne0\right\},
\]
\[
S_{02}(p)=\left\{\begin{pmatrix}A&v\\0&e\end{pmatrix}:A\in GL_2(\mathbf F_p),\ v\in\mathbf F_p^2,\ e\ne0\right\},
\]
\[
S_{12}(p)=\{\operatorname{diag}(A,\det A):A\in GL_2(\mathbf F_p)\}.
\]
Their orders are respectively
\[
p^3(p-1)^2,\quad p(p-1),\quad |GL_2(p)|p^2(p-1),\quad |GL_2(p)|,
\]
so in both fixed-a pairs the p-primary ratio is exactly p^2:
\[
|S_{01}|/|S_{11}|=|S_{02}|/|S_{12}|=p^2(p-1).
\]
The mechanism is visible directly from the two-level jet: the same scalar must multiply the degree-2 and degree-p components. For (0,1), preservation of x^[p] forces the x-line and then det(x,y)=a, forcing the y-diagonal coefficient to be 1. For (1,1), the p-power difference forces the x/z scalars to coincide. For (1,2), the bracket scales by det(A) while z^[p] scales by the z scalar, forcing z-scaling = det(A). For (0,2), only the quadratic line remains, giving the full parabolic stabilizer.

This is a **structural derivation candidate**, not yet a theorem: the remaining proof obligations are to formalize the exact relation-jet functor, prove that no additional degree-p components enter under arbitrary GL substitution, and prove that the finite-window automorphism image equals the jet stabilizer for general odd p. Status: **OPEN / LOAD-BEARING**, but the mechanism is now substantially constrained and explains the four certified finite computations.


## 2026-10-05 — Paper 5 abstract two-level relation-jet stabilizer theorem closed

The current load-bearing structural hypothesis was separated into its intrinsic algebraic part and its finite-window realization part. For odd p, the projective stabilizers of the four two-level relation jets [x,y]+x^[p], [x,y]+z^[p]-x^[p], [x,y], and [x,y]+z^[p] were derived directly from the bracket and restricted-power transformation laws. Their stabilizers are respectively S01={ upper triangular matrices with diagonal pattern (a,1,e) and a,e nonzero }, S11={ matrices with diagonal pattern (a,1,a) and arbitrary x-y shear }, S02={ block upper parabolic with A in GL2(Fp), arbitrary 2-vector, and e nonzero }, and S12={diag(A,det A)}. The orders give |S01|/|S11|=|S02|/|S12|=p^2(p-1), hence p-primary ratio p^2.

Classification: PASS / CLOSED for the abstract projective relation-jet stabilizer theorem under the declared odd-p marked definitions. This is not yet a theorem about the actual finite-window automorphism image: the factorization/equality Im(Aut(W_n)->GL(V))=S_{s,a} is still OPEN / LOAD-BEARING in general, with p=3 and p=5 finite certificates only PASS / LOCAL. No uniform p^2 automorphism-order theorem is promoted.

The detailed proof audit is recorded in research/PAPER5_RELATION_JET_AUDIT.md.

Immediate next gate: prove the finite-window Frattini action factors through the degree-(2,p) relation jet, then seek equality for general odd p or a genuinely new-prime independent certificate. If factorization fails, record the counterexample; do not repair the jet ad hoc.


## 2026-10-05 — Paper 5 Factorization Lemma Step-B critical audit

The current Paper 5 bottleneck was reviewed against the authoritative relation-jet audit. The strategic conclusion is **accepted with mathematical corrections**: the next task is proof of the finite-window factorization, not another GAP calculation, but the proposed B-1/B-2/B-3 skeleton cannot be used verbatim.

### Independent logical audit

**B-1 lift.** The statement that every (Aut(W_n)) element lifts to (Aut(F)) stabilizing (R_n) does not follow from (W_n) being a finite/Hopfian p-group. The lifting problem (Stab_{Aut(F)}(R)	o Aut(F/R)) is a separate issue in one-relator settings. Thus “Hopfian + free presentation” is not a proof. Classification: **FAIL / CLOSED as a proof shortcut; underlying lifting question OPEN**.

**B-2a.** Conditional on an actual correction (cin[R_n,F]), one has
([R_n,F]subseteq[D_2,D_1]subseteq D_3), so the degree-2 correction vanishes. Classification: **PASS / LOCAL conditional lemma**.

**B-2b.** The mixed relation (rin D_2setminus D_3) does not admit the raw pair
((pi_2(r),pi_p(r))), because (pi_p) is defined on (D_p), not on a general (D_2) element. The secondary degree-(p) component requires a canonical filtered relation-module/extension construction and a proof that its ambiguity is controlled. The slogan “(2+p>p+1)” is not sufficient. Classification: **OPEN / LOAD-BEARING**.

**B-3.** Preservation of a one-dimensional relation module naturally gives line preservation and an arbitrary scalar (lambdainmathbf F_p^	imes), not merely (pm1). Therefore the correct abstract target is projective/line stabilization unless an additional theorem reduces the scalar. The existing p=3/p=5 formulas are already formulated projectively.

### Corrected theorem target

The immediate theorem to attack is:

[
operatorname{Im}
ho_nsubseteq
operatorname{Stab}_{GL(V)}(mathcal J_{s,a}),
]

where (mathcal J_{s,a}) is an intrinsically defined filtered relation-jet object, not the presentation-dependent raw pair ((pi_2(r),pi_p(r))).

This preserves the valid strategic conclusion while removing the circular lift assumption and the undefined mixed-degree projection.

### Classification

- abstract marked/projective relation-jet stabilizers: **PASS / CLOSED**;
- actual p=3/p=5 finite image = candidate stabilizer: **PASS / LOCAL**;
- general odd-(p) factorization: **OPEN / LOAD-BEARING**;
- uniform (p^2) automorphism-order theorem: **OPEN**;
- quotient-action `37252335078`: separate **OPEN / EXECUTION BLOCKED** auxiliary gate.

### Immediate next action

Define the intrinsic filtered relation module/secondary jet and prove its functoriality under (Aut(W_n)). Only then prove the factorization. No new GAP scan is authorized before this proof gate is resolved.


## 2026-10-05 — Paper 5 factorization definition audit: raw mixed jet rejected

The proposed factorization proof was audited before any new computation. The raw definition J=(pi_2(r),pi_p(r)) is invalid for the mixed relation case r in D_2\D_3, since pi_p is not defined on D_2\D_p. A BCH claim that the degree-2 component cannot pollute degree p does not repair this: the missing datum is a choice of lift/splitting of the degree-2 relation class.

The corrected intrinsic object is the truncated filtered relation module M_n=R_n/[F,R_n], with M_n^(k)=((R_n cap D_k)[F,R_n])/[F,R_n], through degree p, with the distinguished degree-2 relation line. The secondary information is the associated filtered extension modulo splitting/gauge, not a chosen L_p-vector. This object is acted on functorially by Aut(W_n), avoiding the unproved claim that every automorphism of W_n lifts to Aut(F).

The statement [R_n,F] subset D_3 is retained only conditionally when R_n subset D_2, and is PASS / LOCAL. The Hopficity-to-lift shortcut is FAIL / CLOSED as a proof shortcut. The intrinsic filtered-jet construction and its identification with the four projective marked stabilizers are OPEN / LOAD-BEARING. No new GAP scan is authorized until this definition/factorization gate is settled.

Classification: OPEN / LOAD-BEARING for the general odd-p finite-window factorization; raw mixed jet definition FAIL / CLOSED.


## 2026-10-05 — critical correction: presentation-level relation module is not automatically Aut(W)-functorial

A second audit caught an overclaim in the proposed filtered-relation-module repair. Although M=R/[F,R] is a natural presentation-level relation object, an arbitrary automorphism of W=F/R does not automatically induce an automorphism of M unless it lifts to a compatible automorphism of the free presentation. Thus the filtered relation module does not itself eliminate B-1.

This matches the standard distinction between presentation-associated relation modules and intrinsic H_2: Hopf's formula identifies H_2(G,Z) with (R cap [F,F])/[F,R], whereas the full relation module is attached to a chosen free presentation. The next target is therefore an intrinsic object of W_n alone, with an Aut(W_n)-equivariant map to the presentation-level filtered relation data.

New load-bearing gate: **FRM-0 — intrinsic replacement/factorization carrier**. Candidate sources include characteristic Zassenhaus quotients, H_2/H^2/transgression data, or a canonical extension object. Until FRM-0 is closed, the four abstract projective stabilizer formulas cannot be promoted to a finite-window factorization theorem.

Classification: **OPEN / LOAD-BEARING**. No new GAP scan authorized.


## 2026-10-05 — FRM-0 W3 audit correction: OPEN retained, three load-bearing gaps isolated

The proposed W3/FRM-0 closure was audited and is **not promoted**. The audit confirms that the W3 direction is mathematically relevant, but the previous argument contained three load-bearing gaps.

1. **W3 arithmetic/presentation correction.** For p=3,d=2,
   D3=gamma3(F) gamma2(F)^3 F^3 and D4=gamma4(F) gamma2(F)^3 F^9, so dim(D1/D2,D2/D3,D3/D4)=(2,1,4) and |W3|=3^7=2187. However W3 is not exponent 3 in general: x^3,y^3 can survive in D3/D4, so generators may have order 9. The degree-3 central layer contains the restricted-power and Lie-degree contributions. Classification: dimension/order calculation **PASS / CLOSED**; exponent-3 claim **FAIL / CLOSED** and must not be reused.

2. **Canonical inclusion versus canonical splitting.** The Frobenius-power subspace V^(1)=<x^[3],y^[3]> subset L3 is canonical, but a GL(V)-equivariant splitting L3=L3^Lie ⊕ V^(1), or a canonical projection L3 -> V^(1), has not been proved. Therefore the projected functional e_3^(p)=pr_{V^(1)}(e_3) is **OPEN**. The intrinsic data currently established are the canonical extension class e_3 together with the canonical subspace V^(1), not a canonical projection.

3. **Transgression/Bockstein identification.** The proposed d2 restriction to (V^(1))* matching the standard Bockstein is a promising FRM-0.2 target, but it requires an explicit identification of the relevant dual space, proof of GL2(F3)-equivariance, and equality of the pushed-out extension cocycle with the standard Bockstein class. This is **OPEN / LOAD-BEARING** and is the next authorized W3 calculation/proof gate.

4. **Universal/free-window versus realization-specific relation jet.** Even if (e_2,e_3^(p)) were intrinsic to W3, it is universal free-window data. The realization-specific jet J_{s,a}=(q_{s,a},ell_{s,a}^p) still requires an intrinsic finite-window realization map/factorization. Thus the implication from W_p to the stabilizer of the actual relation jet remains **OPEN / LOAD-BEARING**. Abstract stabilizer formulas do not close finite-window realization.

Current FRM-0 classification remains **OPEN / LOAD-BEARING**. General odd-p factorization remains **OPEN**. The authorized immediate subgate is **FRM-0.2: explicit W3 central-extension/transgression computation, with Bockstein comparison and independent verification**. Do not promote FRM-0, do not declare a canonical V^(1)-projection, and do not start a new GAP scan for the general factorization before this proof gate is settled.


## 2026-10-05 — explanation/guide records given a dedicated navigation layer

The repository contains a second class of records that are not mathematical evidence but are useful for human understanding: easy-language explanations, research-story summaries, methodological reflections, midterm summaries, and contribution/level assessments. These had accumulated across several paths.

A dedicated navigation layer is now established at **research/90_RESEARCH_GUIDE/README.md**. Existing explanatory records are **not deleted, moved, or overwritten**; the new guide indexes their original paths and defines their role separately from authoritative state/evidence documents.

Documentation rule: \`CURRENT_STATE\` / \`RESEARCH_MAP\` / \`PAPER*_CURRENT\` / audit-evidence remain authoritative for mathematical status; \`00_RESEARCH_LOG\` remains chronological; \`archive\` preserves historical material; \`90_RESEARCH_GUIDE\` is the human-understanding/explanation/evaluation layer.

Classification: **PASS/CLOSED — documentation architecture only**. No mathematical claim or research status changed.


## 2026-10-05 — Magnus prefix-code attack on (SC_s): first independent verification

A new attack on the load-bearing comparison
\[
(SC_s):\qquad D_{p^s+1}(F)\cap K\subseteq D_{p^{s-1}+1}(K)
\]
was independently audited. The central idea is to work in the completed Magnus algebra of K rather than compare individual group-level factors.

### Critical correction to the proposed proof
The finite-difference objects \(w_{k,i}=\delta^k(Y_{0,i})\), with \(Y_{j,i}=z^j x_i z^{-j}-1\), are **not group elements/free group generators** when \(\delta=\sigma-1\) is applied linearly in the augmentation algebra. The correct statement is that \(w_{k,i}\) are new **topological augmentation-algebra coordinates**: the transformation from \(Y_{j,i}\) to \(w_{k,i}\) is lower unitriangular over \(\mathbf F_p\), hence an invertible continuous linear change of generators of \(\mathbf F_p[[K]]\).

This correction is essential. It does not invalidate the Magnus argument; it changes its algebraic formulation.

### Independent computation
For \(p=3,5\), direct truncated noncommutative Magnus expansion gives
\[
\operatorname{in}(w_{k,i})=X_0^kX_i,\qquad 0\le k<p,
\]
with F-degree \(k+1\), and \(u=z^p-1\) has initial monomial \(X_0^p\). The finite-difference coefficient matrix has determinant 1 for \(p=3,5,7,11\).

The set
\[
\{X_0^kX_i:0\le k<p,\ i\ge1\}\cup\{X_0^p\}
\]
is a prefix code. Exhaustive concatenation tests through word length 3 for \(p=3,5,7\) found no collisions of leading monomials.

### Current assessment
The corrected Magnus-coordinate/prefix-code route is therefore **OPEN / PROMISING**, not yet PASS. The remaining proof obligation is to formalize the completed-algebra coordinate change and the leading-term multiplicativity for arbitrary infinite series, then deduce
\[
\operatorname{ord}_F(f)=\min_W d(W)
\]
for nonzero \(f\in\mathbf F_p[[K]]\). Once this is established, every word of K-length \(\ell\) has F-degree at most \(p\ell\), giving
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
\]
For \(n=p^s+1\), this is exactly (SC_s).

No all-s transfer-defect theorem is promoted yet. The subsequent TF_s/truncation step remains separately OPEN / LOAD-BEARING.

Classification: **OPEN / LOAD-BEARING candidate route; local symbolic checks PASS / LOCAL.**


## 2026-10-05 — Magnus prefix-code proof closes (SC_s), (TF_s), and the all-s stress-family boundary

A full proof audit of the new Magnus-coordinate attack is now complete. The finite-difference variables (w_{k,i}=\delta^kY_{0,i}) are augmentation-algebra coordinates, not group generators; the change from the Schreier augmentation generators is invertible over \(\mathbf F_p\). With (X_0=z-1) ordered largest in degree-lex, the initial terms are
\[
\operatorname{in}(w_{k,i})=X_0^kX_i,\qquad \operatorname{in}(U)=X_0^p.
\]
The set \(\{X_0^kX_i:0\le k<p\}\cup\{X_0^p\}\) is prefix-free, so distinct coordinate words have distinct leading monomials. This gives the completed-algebra lemma
\[
\operatorname{ord}_F(f)=\min_W d(W)
\]
for every nonzero completed augmentation series (f\) in the Schreier coordinates. Since every coordinate has ambient weight at most p, one obtains the general theorem
\[
\boxed{D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K)}
\]
for every index-p kernel (K) of a finitely generated free group (F). In particular (SC_s) is PASS / CLOSED.

Independent sparse Magnus checks over \(\mathbf F_3\) found F-order/K-order (10/4) for \([z^9,x]\), \(\operatorname{ad}_z^9(x)\), and \(\operatorname{ad}_{z^3}^3(x)); 30 random products/inverses of these witnesses had K-order at least 4. Finite-difference determinants are 1 for p=3,5,7,11, and prefix-code collision tests through coordinate-word length 4 pass for p=3,5,7. The sharpness witness (z^{p^s}) has ambient/K order ratio p.

From the Jennings product formula, (SC_s) immediately implies
\[
\operatorname{im}(D_{p^s+1}(F)\cap K\to K^{ab})\subseteq p^sK^{ab},
\]
so (TF_s) is PASS / CLOSED. For the stress relator, (R\subseteq K) and (D_{p^s+1}(F)\subseteq K), hence (N=D_{p^s+1}(F)R=N\cap K). The quadratic commutator tail lies in \([K,K]\), so its K-abelianization contribution vanishes; the resulting Schreier relation is the previously audited (p^{s-1}U-p^sA_i=0) at a=s.

The intrinsic transfer formulation was corrected: (T=W^{ab}[p^s]) is not itself a single canonical line. The canonical line is the image (S_s(W)=\operatorname{im}(W^{ab}[p^s]\to W^{ab}/pW^{ab})), which is one-dimensional in the declared stress-family scope. The invariant is the class of (p^{s-1}V(t)) in (K^{ab}/p^sK^{ab}) for any lift t spanning (S_s(W)); changing the lift by pW changes the result by (p^sK^{ab}). Thus the predicate is genuinely unmarked and isomorphism-invariant.

Combining (TF_s) with the model Schreier lattice nonvanishing closes the critical a=s transfer witness; the a=infinity side has no corresponding power relation in the U-direction and the normalized transfer defect vanishes. Therefore
\[
\boxed{W_{p^s+1}(G_{s,s})\not\cong W_{p^s+1}(G_{s,\infty})}
\]
for every odd p and s>=2 in the declared stress-family scope. Together with the already certified lower-window blindness, the exact threshold is
\[
\boxed{n_{\rm sep}(s)=p^s+1}.
\]

Classification: Magnus coordinate lemma **PASS / CLOSED**; (SC) and (SC_s) **PASS / CLOSED**; (TF_s) **PASS / CLOSED**; corrected intrinsic transfer invariant **PASS / CLOSED in scope**; a=s versus a=infinity **PASS / CLOSED**; exact stress-family threshold **PASS / CLOSED**. Detailed proof/evidence: `research/PAPER4_MAGNUS_PREFIX_CODE_AUDIT_2026-10-05.md`.


## 2026-10-05 — Independent §9–§11 review corrections to Magnus transfer closure

The independent review rechecked the Magnus prefix-code proof and the a=s versus a=∞ separation. The core proof was confirmed, but the first closure write-up contained several scope/wording defects.

1. **§9 correction:** the untruncated class having order p^s does not itself imply nonvanishing modulo p^s. The correct argument is the model-lattice calculation
\[
p^{s-1}U=0,qquad
(\sigma-1)^{p-1}A_0\equiv\sum_{j=0}^{p-1}A_j\pmod p,
\]
so the critical class is
\(p^{s-1}\sum_jA_j\ne0\) modulo p^s. TF_s puts the actual truncation image inside p^sK^ab, so it cannot kill this class.

2. **§11 direct representatives:** a=s uses t=z-x_1, giving
\(\varepsilon_s=-p^{s-1}\sum_jA_j\ne0\); a=∞ uses t=z, giving
\(\varepsilon_s=0\) directly because p^{s-1}U is in the relator image.

3. **Intrinsic scope:** K is intrinsic only when d is even and the alternating quadratic form defined by r_2 is nondegenerate; d=2 and r_2=[x_1,x_2] is the basic example. Since the power relation is in D_3, the degree-2 cup product on W_n (n\ge3) is unchanged, so the radical line \(\langle z^*\rangle\) is intrinsic in the declared scope.

4. **Schreier range:** corrected to 0\le j\le p-1.

5. **s=1:** the exact separation statement remains intentionally scoped to s\ge2 and is not promoted here.

Classification: **PASS / CLOSED** for odd p, s\ge2, d even, r_2 nondegenerate. Novelty remains a separate literature audit.

## 2026-10-05 — uploaded weighted-Schreier source: SC novelty derivation gate

The user supplied the full TeX source \`arXiv-1007.1489v3\`, *Groups of positive weighted deficiency and their applications*. Direct inspection of the source materially changes the Paper-4 novelty assessment.

The source contains the following relevant chain:

1. Proposition \`uniform2\`: for a uniform weight W on a finitely generated free pro-p group F, there is beta in (0,1) with
\[
W(f)=\beta^{d_F(f)},
\]
where d_F is ordinary Zassenhaus degree.

2. Corollary \`weight_preserve\`: the restriction of a weight function to any closed subgroup K of F is again a weight function.

3. Lemma \`index_p0\`: for an index-p subgroup K, the standard index-p Schreier generating set
\[
y,[y,z],\ldots,[y,\underbrace{z,\ldots,z}_{p-1}],z^p
\]
is W-optimal in the free/weight-function case.

4. In the proof of Lemma \`indexp\`, the weights of these Schreier generators are exactly controlled by
\[
W(z^p)=W(z)^p,\qquad
W([y,\underbrace{z,\ldots,z}_{k}])=W(y)W(z)^k
\]
in the free weight-function case.

5. Proposition \`cor1\` gives the required no-cancellation characterization of weight functions via power-commutator factorization.

Specializing the uniform weight to the ordinary Zassenhaus degree therefore gives the Paper-4 comparison
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
\]
Indeed, every K-Schreier generator has ambient weight exponent at most p, while a nonzero K-element of K-Zassenhaus degree ell has a nonzero K-coordinate term of length ell, hence ambient weighted exponent at most p ell. Since the restricted weight is still a weight function, the source's no-cancellation characterization gives d_F(g)<=p d_K(g). Thus d_F(g)>=n implies d_K(g)>=ceil(n/p).

Classification:
- weighted-Schreier derivation of SC: **PASS / CLOSED as a derivation from prior machinery**;
- SC as an independent novelty claim: **CONDITIONAL / likely not novel**;
- Paper-4 Magnus prefix-code proof: **PASS / mathematically valid, but no standalone novelty claim**;
- downstream intrinsic epsilon_s and exact a=s versus a=infinity separation: **OPEN / strongest current novelty candidates**;
- Paper-4 mathematical theorem in declared scope: **PASS / CLOSED**;
- publication novelty overall: **CONDITIONAL / OPEN**.

The detailed source comparison is recorded in \`research/PAPER4_WEIGHTED_SCHREIER_DERIVATION_AUDIT_2026-10-05.md\`.

Governance consequence: do not reopen the Paper-4 mathematics. Move the novelty audit downstream to epsilon_s, the finite-window torsion obstruction, the a=s versus a=infinity family, and the exact threshold p^s+1.


## 2026-10-05 — weighted-Schreier source audit: SC novelty boundary confirmed

The uploaded `arXiv-1007.1489v3.gz` was decompressed and directly inspected. SHA-256:
`9f8c1e6ec8d7bff45e275b4774edf49bd95050d4ef59227d2b58aee768c14710`.

The source is *Groups of positive weighted deficiency and their applications*. The relevant chain is explicit:

- Proposition `uniform2`: a uniform weight on free pro-(p) (F) is (W_F(g)=\beta^{d_F(g)}).
- Corollary `weight_preserve`: restriction of a weight function to a closed subgroup remains a weight function.
- Lemma `index_p0`: standard index-(p) Schreier generators (y,[y,z],ldots,[y,z^{p-1}],z^p) are (W)-optimal in the free case.
- Proof of Lemma `indexp`: their weights are exactly (\beta,ldots,\beta^p).
- Proposition `cor1`: for every (f), its power-commutator factorization has no cancellation at the top weight; (W(f)) is the maximum weight of a nonzero factor.

Therefore the Paper-4 comparison
[
D_n(F)cap Ksubseteq D_{\lceil n/p\rceil}(K)
]
is already a consequence of the prior weighted-Schreier framework: (d_F(f)le p,d_K(f)), hence the displayed subgroup inclusion. The earlier review question about whether `cor1` applies only to special elements is resolved negatively: it applies to arbitrary (f).

Classification:
- SC derivation from prior literature: **PASS / CLOSED**.
- SC standalone novelty: **CONDITIONAL / likely not novel**.
- Magnus prefix-code proof: **PASS / CLOSED as independent self-contained verification/reproof; no standalone novelty claim**.
- Paper-4 mathematics in the declared scope: **PASS / CLOSED**.
- Overall publication novelty: **CONDITIONAL / OPEN**.

The novelty center of gravity is moved downstream to the intrinsic transfer obstruction (arepsilon_s), the unmarked (a=s) versus (a=\infty) separation at the critical window, and the exact threshold (p^s+1). No Paper-4 mathematical result is reopened or downgraded by this audit.


## 2026-10-05 — bounded external literature audit after weighted-Schreier source discovery

A second literature audit was run after the direct source inspection.

### Findings

1. Ershov–Jaikin-Zapirain, *Groups of positive weighted deficiency and their applications*, J. Reine Angew. Math. 677 (2013), 71–134, DOI 10.1515/crelle.2012.013, independently corroborates the uploaded TeX source: its published text contains the explicit index-(p) weighted Schreier construction (Lemma 3.10) and the surrounding weight-function/free-restricted-Lie machinery. Thus SC is safely treated as a prior weighted-Schreier consequence, not a new theorem.

2. Later Zassenhaus/Magnus literature (including Mináč–Rogelstad–Nguyễn and Efrat) confirms that augmentation/Magnus/word methods and finite Zassenhaus quotients are established infrastructure. Magnus/prefix-code language therefore cannot itself carry the novelty claim.

3. Efrat's transfer/intersection literature is an important neighboring threat: transfer principles connect cohomology, finite quotients, unitriangular representations, and Zassenhaus intersections. This must be cited and discussed.

4. Targeted searches for the **specific downstream Paper-4 combination** — intrinsic (epsilon_s), the stress family (z^{p^s}=x_1^{p^a}r_2^{-1}), unmarked (a=s) versus (a=\infty) separation, and exact threshold (p^s+1) — produced no matching result in the retrieved literature.

### Classification

- SC: **PASS/CLOSED mathematically; not standalone novelty**.
- Magnus proof: **PASS/CLOSED as self-contained reproof/bridge**.
- (epsilon_s): **OPEN — strongest novelty candidate**.
- Exact (a=s) vs (a=\infty) separation: **OPEN — strong novelty candidate**.
- Exact threshold (p^s+1): **OPEN — strong sharpness candidate**.
- Overall publication novelty: **CONDITIONAL / OPEN**.

This is a bounded negative search, not a proof of priority. The next authorized audit is narrowly targeted at transfer on index-(p) kernels, Bockstein/cup-product relation data, and finite-quotient separation at a prescribed Zassenhaus depth.


## 2026-10-05 — SC literature audit CLOSED; downstream strengthening authorized

Decision: **SC = PASS / CLOSED; literature audit = PASS / CLOSED.**

The final position is:
- Zassenhaus/Magnus/weighted-Schreier literature provides the component machinery.
- The exact Paper-4 subgroup-depth comparison \(D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K)\) was not located as a directly stated theorem in the audited sources.
- Paper 4 therefore may claim this comparison as a **new logical deduction/assembly step**, while explicitly crediting the prior machinery from which it can be derived.
- The standalone novelty claim is not “we invented weighted Schreier theory” and not “no prior result could imply SC”; it is that the Paper-4 proof identifies and packages the precise subgroup-depth comparison needed to force the finite-window transfer bound.

The SC search is now stopped. No more generic literature time should be spent here.

### Next research gate — theorem strengthening using SC

The next task is to derive the strongest clean theorem that SC supports, in this order:

1. formulate the exact general marked-kernel consequence of SC and Jennings after abelianization;
2. specialize it at \(n=p^s+1\) to obtain the sharp transfer truncation bound;
3. separate the universal SC/TF layer from the family-specific intrinsic \(\varepsilon_s\) layer;
4. test whether the nondegenerate quadratic hypothesis can be weakened while retaining an unmarked canonical kernel;
5. state the final theorem with the strongest valid scope, explicitly distinguishing marked and intrinsic versions.

No theorem is to be broadened by analogy; each scope enlargement requires an independent proof.



## 2026-10-05 — SC strengthening and complete critical-a classification

**Result classification: PASS / CLOSED.**

The SC result was strengthened from the critical specialization to a general transfer-depth law. For an index-p kernel K≤F,
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
With m=\lceil n/p\rceil and e(n)=\lceil\log_p m\rceil, Jennings–Lazard gives
\operatorname{im}(D_n(F)\cap K\to K^{ab})\subseteq p^{e(n)}K^{ab}.
At n=p^s+1, e(n)=s, recovering TF_s.

A second strengthening completely classifies the stress-family critical windows W_{s,a}=W_{p^s+1}(G_{s,a}). For 1\le a<s,
W_{s,a}^{ab}\cong\mathbf Z_p/p^a\oplus(\mathbf Z_p/p^{s+1})^d,
so distinct a<s are pairwise distinguished by abelianization. For a>s, p^a\ge p^{s+1}>p^s+1, so the x_1^{p^a} term vanishes in the critical truncation and W_{s,a}=W_{s,\infty}. At a=s, abelianization agrees with a=\infty, but the already certified intrinsic transfer witness satisfies
\varepsilon_s(W_{s,s})\ne0,\qquad \varepsilon_s(W_{s,\infty})=0,
hence W_{s,s}\not\cong W_{s,\infty}.

Therefore the map a\mapsto W_{p^s+1}(G_{s,a}) has exactly one nontrivial critical boundary at a=s, while a>s is saturated with a=\infty.

Scope remains: odd p, s\ge2, even d, nondegenerate alternating r_2. The nondegenerate hypothesis is retained because it is needed for the current canonical one-dimensional cup-radical construction of the intrinsic kernel. The s=1 case and degenerate quadratic forms remain unpromoted.

Interpretation: SC is now infrastructure/engine. The theorem-level contribution is the finite-window transfer obstruction and the complete critical-window classification of the hidden power parameter. The arbitrary-r degree-only theorem remains FAIL / CLOSED.

Evidence anchors: research/PAPER4_CURRENT_2026-10-05.md, research/PAPER4_MAGNUS_PREFIX_CODE_AUDIT_2026-10-05.md, and the SC literature audit in research/PAPER4_WEIGHTED_SCHREIER_DERIVATION_AUDIT_2026-10-05.md.


## 2026-10-05 — Paper 4 SC_s strengthening: index-p^s and sharpness

**Result classification: PASS / CLOSED.**

The authorized theorem-strengthening step is complete.

1. **Index-p^s generalization.** For an open subgroup K of a finitely generated free pro-p group F with [F:K]=p^s, choose a subnormal chain F=K_0>K_1>...>K_s=K with [K_{i-1}:K_i]=p. Repeated application of the certified index-p comparison gives
\[
D_n(F)\cap K\subseteq D_{\lceil n/p^s\rceil}(K).
\]
The ceiling identity composes exactly, so no extra rounding loss appears.

2. **Uniform sharpness.** Let F=<a,b> be free pro-p and K=ker(F -> C_{p^s}), with a mapping to a generator and b to 0. A Schreier basis contains c_0=a^{p^s}. For m>=1,
\[
g_m=a^{p^{m+s-1}}=c_0^{p^{m-1}}
\]
lies in D_{p^{m+s-1}}(F)\cap K but not in D_{p^{m-1}+1}(K). Hence the universal replacement of the bound by D_{\lceil n/p^s\rceil+1}(K) is false. This proves the p^s compression factor is uniformly optimal.

3. **Scope correction.** The stronger proposed claim that a commutator correction gives sharp witnesses for every integer n is not independently proved and is not promoted. Pointwise sharpness for every n is unnecessary; the infinite equality family already establishes optimality of the uniform theorem.

4. **Paper-4 interpretation.** SC/SC_s are universal filtration infrastructure. The Paper-4-specific theorem-level contribution remains the intrinsic transfer obstruction, exact unmarked critical-window separation, and threshold n_sep(s)=p^s+1 in the declared odd-p, s>=2, even-d, nondegenerate alternating quadratic stress-family scope.

Evidence: research/PAPER4_SC_SHARPNESS_AND_INDEX_PS_AUDIT_2026-10-05.md.


## 2026-10-05 — General SC arbitrary-pro-p A1 audit: proposed proof rejected

The proposed strengthening of D_n(G) cap K subseteq D_{ceil(n/p^s)}(K) from free pro-p groups to arbitrary pro-p groups was audited before promotion.

**Classification: FAIL / CLOSED as the proposed proof; arbitrary-pro-p theorem remains OPEN.**

The fatal error is Lemma 2. For an index-p extension, the identity I_G^n = sum_{j=0}^n I_K^{n-j} t^j B does not hold in general because t=a-1 does not commute with I_K. Normality only gives conjugation invariance. A concrete counterexample to Lemma 2 is the odd-p exponent-p Heisenberg group G=<x,y,z | x^p=y^p=z^p=1,[x,y]=z,z central>, with K=<x,z> and t=y-1. Then t(x-1) lies in I_G^2 and has an A-component containing x(z-1), which has I_K-degree 1 because K is abelian, while the proposed n=2 right-hand side has A-component contained in I_K^2.

There is also a second gap in Lemma 3: the coefficient y_j in I_K^{n-j}B itself can contain t-powers in its B-basis expansion, so the claim that only j divisible by p can contribute to the A-component is not justified.

Therefore:
- Lemma 2 = **FAIL / CLOSED**;
- Lemma 3 via this route = **FAIL / CLOSED**;
- arbitrary-pro-p SC = **OPEN**;
- the already certified free-pro-p SC/SC_s and Paper-4 theorem are **unchanged**.

A targeted literature search did not locate an immediately usable theorem giving this exact arbitrary-pro-p comparison. No arbitrary-pro-p promotion is authorized without a different proof. Full audit: research/PAPER4_GENERAL_SC_ARBITRARY_PROP_A1_AUDIT_2026-10-05.md.


## 2026-10-05 — A1 arbitrary pro-p SC closed and promoted into Paper 4

The earlier A1 audit rejected the first augmentation-ideal equality proof because the claimed decomposition was false. That rejection is retained as a proof-route failure only.

A corrected weighted normal-form argument is now independently audited and **PASS / CLOSED**. For arbitrary pro-p (G), an index-(p) open subgroup (K), (A=\mathbf F_p[[K]]), (J=I_K), and (t=a-1) for a lift of a generator of (G/K), use
[
\mathbf F_p[[G]]=\bigoplus_{r=0}^{p-1}At^r,qquad t^p\in J,
]
and the weighted filtration
[
E_m=\bigoplus_{r=0}^{p-1}
J^{\max(0,\lceil(m-r)/p\rceil)}t^r.
]
The normal-form multiplication rules give (E_mE_\ell\subseteq E_{m+\ell}), including the previously problematic (t^rBt) terms. Hence
[
I_G^n\subseteq E_n,qquad
I_G^n\cap A\subseteq I_K^{\lceil n/p\rceil},
]
and therefore
[
D_n(G)\cap K\subseteq D_{\lceil n/p\rceil}(K).
]
Iteration along an index-(p^s) chain yields
[
D_n(G)\cap K\subseteq D_{\lceil n/p^s\rceil}(K).
]

Thus:
- A1 index-(p) arbitrary pro-p: **PASS / CLOSED**;
- A1 index-(p^s) arbitrary pro-p: **PASS / CLOSED**;
- free-pro-p SC/SC_s: unchanged and subsumed;
- uniform sharpness: retained only in the already certified free-pro-p witness family;
- pointwise sharpness for every (n): not claimed.

The old false equality route, Heisenberg witness, and Lemma-2/Lemma-3 route remain **FAIL / CLOSED / SUPERSEDED** and are not evidence against A1.

Paper 4 is therefore strengthened by A1 as universal filtration infrastructure. The theorem-specific contribution remains the intrinsic transfer obstruction, exact unmarked separation (W_{p^s+1}(G_{s,s})\not\cong W_{p^s+1}(G_{s,\infty})), and the sharp threshold (n_{\rm sep}(s)=p^s+1) in the declared stress-family scope.

Evidence: `research/PAPER4_GENERAL_SC_ARBITRARY_PROP_A1_CLOSURE_2026-10-05.md`.


## 2026-10-05 — Paper 4 Every-(n) sharpness closed and manuscript promotion started

The Every-(n) sharpness argument is now certified. For
[
F=langle a,bangle,qquad
K=ker(F	omathbf Z/p^s),
]
the Schreier generators
[
c_0=a^{p^s},qquad c_i=a^iba^{-i}
]
give explicit group-commutator witnesses for every
(n=p^sq+r). For (r>0), repeated commutation of (c_{r-1}) by (c_0)
gives
[

u_F(g_{q,r})=n,qquad

u_K(g_{q,r})=q+1.
]
For (r=0), the second (F)-degree-(p^s) Schreier generator
(c_{p^s-1}) is essential; the commutators
(h_2=[c_0,c_{p^s-1}],,h_{k+1}=[h_k,c_0]) give
[

u_F(h_q)=qp^s,qquad 
u_K(h_q)=q.
]
The free-associative leading-word argument certifies the required
nonvanishing. The previous abstract (gr_D(K)	o gr_D(F)) lift/Lazard
shortcut is explicitly not used.

Final sharpness statement:
[
oxed{orall nge1,quad
lceil n/p^sceil	ext{ is best possible in the free-pro-}p	ext{ class}.}
]
Scope remains: arbitrary pro-(p) validity; free-pro-(p) uniform
every-(n) optimality.

The Paper 4 manuscript on branch
`paper4-tex-2026-10-04` has now been promoted to incorporate:
1. arbitrary-pro-(p) SC/SC_s theorem via weighted normal forms;
2. explicit every-(n) free-pro-(p) sharpness witnesses;
3. corrected intrinsic transfer separation and exact
(n_{m sep}(s)=p^s+1);
4. the degree-only arbitrary-(r) counterexample boundary.

Commit:
`499337be2114b74549969aea65b08442d2cd8fa7`.

No new generic literature search is required: the SC novelty audit was
already closed on 2026-10-05. Remaining work is manuscript/source/PDF
artifact audit, not a reopening of the mathematical gates.


## 2026-10-05 — Paper 4 publication pass: manuscript proof integration

The Paper 4 manuscript on `paper4-tex-2026-10-04` was promoted from theorem-summary form to the audited publication form.

Integrated:
- arbitrary-pro-p SC/SC_s theorem via weighted normal forms;
- every-n free-pro-p sharpness with explicit Schreier-generator commutators;
- corrected intrinsic transfer invariant (S_s(W)=\operatorname{im}(W^{ab}[p^s]\to W^{ab}/pW^{ab}));
- explicit (a=s) versus (a=\infty) critical transfer calculation;
- exact (n_{sep}(s)=p^s+1);
- degree-only arbitrary-(r) boundary (r=z^p).

Also removed stale manuscript language that still called the (a=s) versus (a=\infty) boundary open.

The dedicated `paper4-tex-build` workflow was updated so its PDF audit checks the final every-(n) sharpness and intrinsic-separation statements rather than the obsolete boundary wording.

Latest manuscript commit:
`b384441a02f0a01c448bf16feaa1fbcd709a3cba`.

Latest workflow-audit commit:
`639b0c9f84307570970bec884b5eb7290ecad5c9`.

CI artifact verification is still pending/not directly exposed by the available workflow-run connector (which only returns pull-request-triggered runs). Therefore no new PDF SHA is declared yet. The prior Paper 4 PDF build remains historical; final status awaits the current source's CI PDF artifact audit.


## 2026-10-05 — Paper 4 publication artifact freeze

**Result classification: PASS / CLOSED.**

The final Paper 4 manuscript source was reconciled with the authoritative theorem state. The stale abstract order-jump sentence was removed; the critical-window (a)-classification was included; bibliography metadata was checked against publisher records; LaTeX tag/text-mode errors and the CI PDF path error were repaired.

Final publication build:
- manuscript commit: `b3e0e3cd85f17ab038815030b2643e6be002c4fd`
- workflow: `paper4-tex-build`
- CI run: `37291334999` — PASS
- PDF: 17 pages, 423897 bytes
- PDF SHA-256: `85d5bd7793a8ba271c6a883ed4e0f7ca1849fc283c821a6cf92c84d56a4601ad`
- source blob SHA: `13f50f4ff38f528d17f1cbaaa737bf12af2c5084`
- source SHA-256: `b5169596ab6a84d693e66fb0138ceecbd10eda925cf341ef44a4a677674b65ab`
- CI artifact: `paper4-pdf`, id `11337135583`
- artifact ZIP digest: `sha256:13d97ff0e3a9cbf762906a610e51cb9068d03a4d9b07dfc827448b792b0d5885`

The final CI audit verifies compilation, PDF extraction, author/title/reference presence, absence of the superseded order-jump wording, and source/PDF checksum manifest generation. Earlier local PDF artifacts are HISTORICAL / SUPERSEDED.

**Paper 4 publication artifact is now frozen. No mathematical gate was reopened by this audit.**


## 2026-10-05 — Paper 5 corrected relation-jet model and lift audit

A new review identified and independently clarified the decisive \(S_{11}\) issue. In the naive \(\Lambda^2V\oplus V^{(1)}\) shadow, \(\rho_{11}=[x,y]+z^{[p]}-x^{[p]}\) has stabilizer of order \(|GL_2(p)|\), so the prior \(S_{11}\) formula of order \(p(p-1)\) is not a consequence of that model. The observed p=3 value 6 is recovered only after retaining the Jacobson restricted-power terms and reducing modulo the ideal generated by \([x,y]\). Thus the corrected general odd-p \(S_{11}\) derivation is **OPEN / LOAD-BEARING**.

The restricted-Lie structure is also reinterpreted: the canonical data are the ordinary-Lie subspace/image and the Frobenius-twist quotient; the span of chosen \(x^{[p]},y^{[p]}\) is not a canonical GL-invariant direct summand. A canonical section is not asserted.

The free pro-p lifting route is revised. For a free pro-p presentation, projectivity supplies a lift of an automorphism of the finite quotient to an endomorphism of the free pro-p group; Frattini-surjectivity makes the lift an automorphism, and kernel equality gives preservation of the defining normal subgroup. Hence the blanket Hopficity-based rejection is superseded. The induced action on a chosen relation module is nevertheless only **CONDITIONAL** until lift ambiguity is handled.

Authorized next sequence:
1. corrected restricted-Lie/Jacobson P5-JET;
2. intrinsic graded upper bound \(\operatorname{Im}Aut(W_n)\subseteq Stab(J)\);
3. intrinsic filtered secondary map \(\theta\);
4. equality/lifting construction;
5. only afterward, pre-registered same-prime falsification computations and \(n=p+2\) checks.

Evidence: `research/PAPER5_NEXT_STEP_AUDIT_2026-10-05.md`.


## 2026-10-05 — Paper 5 Step 2 audit correction

The Hall–Petrescu p-power sublemma for odd p passes: for u∈D_2, (xu)^p≡x^p mod D_{p+1}. But this controls only the p-power component. Under x'=xu, y'=yv, the commutator [x,y] changes by D_3, and there is no canonical projection D_3→D_p/D_{p+1}. Therefore the proposed θ:J_2→D_p/D_{p+1} is not yet shown well-defined. Step 2 remains **OPEN / LOAD-BEARING**; no equality or uniform p^2(p−1) theorem is promoted.


## 2026-10-05 — Step 2 D_3-ambiguity correction

The proposed final split “p=3 PASS / p≥5 FAIL” is **not established**. Two errors were found: (i) D_3 is not equal to γ_3 for p≥5; it contains p-power factors such as G^p and γ_2^p, and (ii) for u=[r,s]∈γ_2 the leading correction [[r,s],y] is in γ_3, not γ_4. Hence the proposed negative witness is invalid. The p=3 claim also needs a direct Zassenhaus calculation of [x,D_2] and [D_2,y] modulo D_4. Current status: **OPEN / LOAD-BEARING**. Next gate is the exact lift-change map D_2×D_2→D_3/D_{p+1} and its interaction with the relation constraint.


## 2026-10-05 — Step 2 central-ambient review: promising reduction, but theta closure still CONDITIONAL

A proposed repair of the (D_3)-ambiguity was reviewed. The correction of the two earlier errors is accepted: (D_3
eq\gamma_3) in general, and for (u=[r,s]in\gamma_2) the leading term ([[r,s],y]) lies in (\gamma_3), not (\gamma_4). Hence the previous (p=3)/(p\ge5) split remains superseded.

The new route uses the central restricted-Lie ambient
\[
\overline L=L_p(V)/\langle[x,z],[y,z]\rangle_{\rm res},\qquad V=\langle x,y,z\rangle,
\]
followed by the restricted ideal (J=\langle[x,y]\rangle_{\rm res}). In \(\overline L/J\), the ordinary Lie part is abelian, so the degree-\(\ge2\) filtration is generated by restricted (p)-powers. Consequently the intended estimate
\[
[x,D_2(\overline L/J)]\subseteq D_{p+1},\qquad [D_2(\overline L/J),y]\subseteq D_{p+1},
\]
and hence the vanishing of the lift-change map modulo (D_{p+1}), is a mathematically plausible route and is consistent with the restricted-Lie structure.

However, this does **not yet by itself close \(\theta\)**. Two points must be made explicit before promotion:

1. One must prove the exact structural lemma (D_2(\overline L/J)=V^{[p]}+D_{p+1}) (or an equivalent statement strong enough to imply the displayed commutator inclusions), including the higher restricted-power terms. The sentence (u\equiv t^{[p]}\pmod{D_3}) alone is insufficient, because ( [x,D_3]\subseteq D_4) does not imply ( [x,D_3]\subseteq D_{p+1}) for (p>3).
2. The quotient by (J) is being used as a **gauge-killing ambient object**, not as the final relation quotient. Since (J=\langle[x,y]\rangle_{\rm res}) kills the degree-2 relation line, the secondary class (x^{[p]}-z^{[p]}) must be defined as the filtered lift/transgression of that killed line. One must explicitly construct the source/target map (or equivalent exact sequence) and show independence from the chosen lifts before calling \(\theta\) canonical.

Therefore the proposed central-ambient calculation is accepted as a **new authorized subgate**, but the Step-2 classification remains **OPEN / LOAD-BEARING**. No (S_{11}(p)) equality or uniform (p^2(p-1)) theorem is promoted.

Next authorized gate: prove the restricted-abelianization lemma for \(\overline L/J\), then formulate the transgression/filtered relation object whose degree-(p) class is \(x^{[p]}-z^{[p]}), and only then certify \(\Phi\in D_{p+1}\) and \(\theta\) well-defined.


## 2026-10-05 — Critical recheck of proposed Step 2 closure: restricted-abelianization lemma is valid, but does NOT imply Phi closure in the original ambient

The proposed proof of the lemma
\[
D_2(\overline L/J)=V^{[p]}+D_{p+1}(\overline L/J),\qquad J=\langle[x,y]\rangle_{\rm res},
\]
is accepted at the level of the quotient restricted Lie algebra: after killing the restricted ideal generated by \([x,y]\), the ordinary Lie algebra is abelian, and the Zassenhaus/restricted-degree filtration is generated by the successive restricted powers. Hence the quotient statement is **PASS / LOCAL** (subject to precise notation distinguishing images in the quotient from subspaces upstairs).

However, the attempted inference
\[
[x,D_2(\overline L/J)]\subseteq D_{p+1}\quad\Longrightarrow\quad
\Phi(u,v)\in D_{p+1}(\overline L)
\]
is invalid. The calculation takes place **after quotienting by (J)**. It proves at most
\[
\Phi(u,v)\in J+D_{p+1}(\overline L)
\]
when lifted back to \(\overline L\), not \(\Phi(u,v)\in D_{p+1}(\overline L)\). Since (J\) contains the degree-2 class \([x,y]\), it is not contained in (D_{p+1}). Thus the quotient kills precisely the low-degree ambiguity one is trying to control, and cannot by itself certify the required degree-(p) vanishing in the original ambient.

This is a decisive gap. The statement \(\Phi\in D_{p+1}\) and hence the canonicality of \(\theta\) remain **OPEN / LOAD-BEARING**. The proposed Step-2 CLOSED classification is rejected. The restricted-abelianization lemma becomes a useful auxiliary lemma, not the final gate.

The next authorized task is to retain enough of the \(J\)-adic/filtered extension data to distinguish \(D_{p+1}\) from \(J+D_{p+1}\), and to compute the lift-change map in \(\overline L\) itself (or construct an exact transgression sequence whose kernel is known to contain no degree-\(<p\) contribution). No equality theorem or \(p^2(p-1)\) theorem is promoted.


## 2026-10-05 — Paper 5 Step 2 CLOSED: filtered-extension/J-adic gate

**Result classification: CLOSED / GENERAL (Step 2).**

The previously identified gap is now closed in the actual relation quotient, not merely in the auxiliary quotient. Let
[
overline L=L_p(V)/langle[x,z],[y,z]angle_{m res},qquad
J=langle[x,y]angle_{m res},
]
and
[
W_n=overline L/langlehoangle,qquad
ho=[x,y]+z^{[p]}-x^{[p]}.
]
The auxiliary lemma
[
D_2(overline L/J)=V^{[p]}+D_{p+1}(overline L/J)
]
is only PASS/LOCAL and by itself gives merely
[
Phiin J+D_{p+1}(overline L).
]
It does not kill the (J)-ambiguity.

In (W_n), however,
[
[x,y]=x^{[p]}-z^{[p]}in D_p(W_n),
]
so the (D_2/D_{p+1}) relation direction is already contained in (V^{[p]}). Hence
[
oxed{D_2(W_n)=V^{[p]}+D_{p+1}(W_n)}.
]
The higher restricted-ideal part satisfies
[
oxed{[V,J]subseteq D_{p+1}(W_n)}
]
and more precisely
[
Jsubseteqlangle x^{[p]}-z^{[p]}angle+D_{p+1}(W_n).
]
The critical generator calculations are
[
[x,[x,y]]=0,qquad
[y,[x,y]]=(ad,x)^p(y)in D_{p+1},
]
using centrality of (z); the restricted (p)-power part is also in (D_{p+1}).

Therefore for (u,vin D_2(W_n)), write
[
u=t^{[p]}w,qquad win D_{p+1}(W_n).
]
Then
[
[x,u]in D_{p+1},qquad [u,y]in D_{p+1},
]
and the commutator expansion gives
[
oxed{Phi(u,v)=[xu,yv][x,y]^{-1}in D_{p+1}(W_n)}.
]
Thus the secondary degree-(p) class
[
	heta:J_2	o D_p(W_n)/D_{p+1}(W_n)
]
is lift-independent and canonical in (W_n).

**Precision correction:** do not state (Jsubseteq D_{p+1}). The generator ([x,y]=x^{[p]}-z^{[p]}) can survive modulo (D_{p+1}); only the higher (J)-part relevant to lift ambiguity is absorbed into (D_{p+1}).

### Updated status

- (S_{11}=p(p-1)): CLOSED/GENERAL.
- Step 1 upper bound: THEOREM/CLOSED.
- (D_2(overline L/J)=V^{[p]}+D_{p+1}): PASS/LOCAL.
- (Phiin J+D_{p+1}(overline L)): PASS/LOCAL auxiliary statement.
- (D_2(W_n)=V^{[p]}+D_{p+1}(W_n)): PASS/GENERAL.
- ([V,J]subseteq D_{p+1}(W_n)): PASS/GENERAL.
- (Phiin D_{p+1}(W_n)): CLOSED/GENERAL.
- Step 2 (	heta): CLOSED/GENERAL.
- Step 3 equality
[
operatorname{Im}(operatorname{Aut}(W_n)	o GL(V))=S_{11}(p)
]
remains CONDITIONAL.
- The (p^2(p-1)) automorphism-order theorem remains CONDITIONAL.

The old Step-2 OPEN/LOAD-BEARING entries are superseded. The next authorized gate is the explicit lower-bound/lifting construction and independent relation-preservation verification for Step 3.


## 2026-10-05 — Step 3 equality audit: first-order relation congruence passes, kernel-invariance induction fails

The proposed final Step 3 closure was independently rechecked against the current Paper 5 state.

The calculation
[
\tilde g_{a,b}(\rho)\equiv \rho^a
\pmod{R D_{p+1}(F)}
]
is accepted as a useful first-order congruence, assuming consistent commutator convention and the already established estimate
[
\gamma_3(F)\subseteq [F,R]D_{p+1}(F).
]
Hall–Petrescu supplies the required (p)-power congruences, and the (R_0)-quotient makes (z) central.

However, the submitted proof contains a definite relation-order/sign mismatch: from
[
\rho=[x,y]^{-1}x^pz^{-p}
]
the quotient relation is ([x,y]=x^pz^{-p}), not the displayed exact replacement ([x,y]=\rho z^px^{-p}). The latter is inverse/order-reversed and must not be used as an exact identity.

More importantly, the decisive implication
[
\tilde g(R)\subseteq R D_{p+1}(F)
\Longrightarrow
\tilde g(R)\subseteq R
]
was asserted via an unspecified “standard pro-(p) induction”. This is not proved. From (\tilde g(R)\subseteq RD_m) one still needs an explicit mechanism forcing (\tilde g(R)\subseteq RD_{m+1}) (or an equivalent exact relation-module/kernel argument). Closedness of (R) and ([F,R]\subseteq R) do not supply that step automatically.

Therefore the submitted Step 3 equality closure is **FAIL / CLOSED as a proof attempt**, while the underlying equality remains **OPEN / LOAD-BEARING**:
[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p)
]
is not promoted. The (p^2(p-1)) automorphism-order theorem remains **CONDITIONAL**.

Detailed evidence: `research/PAPER5_STEP3_EQUALITY_AUDIT_2026-10-05.md`.

Next authorized gate: prove a genuine Zassenhaus-layer lifting lemma for kernel invariance, or replace the induction with an exact presentation/relation-module argument. Do not promote the equality or the (p^2(p-1)) theorem before that gate closes.


## 2026-10-05 — Step 3 re-audit: (D_{p+1}\subseteq R) is false

The proposed closure using
\[
D_{p+1}(F)\subseteq R
\]
is rejected. The graded induction fails at the first exceptional multiple (n=p^2): from (y\in gr_k(R)\Rightarrow y^{[p]}\in gr_{kp}(R)) one cannot infer (gr_{kp}(F)=gr_{kp}(R)) when (k=p), because (gr_p(F)\ne gr_p(R)). In particular (x^{[p^2]}) need not lie in (gr_{p^2}(R)).

There is also a direct group-level counterexample. In the abelian quotient
\[
A=\mathbf Z_p^3/\langle p(e_x-e_z)\rangle,
\]
the defining normal subgroup (R) maps to zero, while (x^{p^2}) maps to (p^2e_x\ne0). Hence (x^{p^2}\notin R). Since (x^{p^2}\in D_{p^2}(F)\subseteq D_{p+1}(F)),
\[
\boxed{D_{p+1}(F)\not\subseteq R.}
\]

Therefore the claimed implication (\tilde g(R)\subseteq RD_{p+1}=R) is invalid. The earlier first-order congruence (\tilde g(R)\subseteq RD_{p+1}) remains a potentially useful local/general ingredient, but kernel preservation \(\tilde g(R)\subseteq R\) is again **OPEN / LOAD-BEARING**. Consequently
\(​operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p)\) remains OPEN/LOAD-BEARING and the uniform (p^2(p-1)) theorem remains CONDITIONAL.

Detailed audit: `research/PAPER5_STEP3_Dp1_SUBSET_R_AUDIT_2026-10-05.md`.


## 2026-10-05 — Step 3 second-order lifting claim rejected

The proposed closure
[
\text{equal }in_k\ +\ \text{zero }in_{k+1}\Longrightarrow D_{k+2}
]
was re-audited and is **FAIL / CLOSED as submitted proof**.

The first-order residual (r_k^{-1}\widetilde g(r)\in D_{k+1}) is accepted only as a local consequence of matching degree-(k) initial forms. The claimed second-order BCH argument is not a valid general Zassenhaus lemma: (in_{k+1}(r_k)) is undefined when (r_k\in D_k\setminus D_{k+1}), and no canonical splitting of
[
0\to D_{k+1}/D_{k+2}\to D_k/D_{k+2}\to D_k/D_{k+1}\to0
]
is provided.

Likewise, (a=\exp(X+A+\cdots)) with (X\in gr_k), (A\in gr_{k+1}) is not an intrinsic representation of arbitrary free pro-(p) group elements in the Zassenhaus filtration. A BCH calculation therefore cannot replace the missing filtered second-jet construction.

The fact ([D_k,D_k]\subseteq D_{2k}\subseteq D_{k+2}) for (k\ge2) only says (D_k/D_{k+2}) is abelian; it does not canonically split its two graded layers.

Therefore the strengthened
[
\widetilde g(R\cap D_m)\subseteq(R\cap D_m)D_{m+2}
]
and the induction to (\widetilde g(R)\subseteq R) remain **OPEN / LOAD-BEARING**. The (p) and (p^2) exceptional-layer calculations cannot repair the missing initial second-order lift.

**Status:** Step 3 equality (\operatorname{Im}=S_{11}(p)) remains OPEN / LOAD-BEARING; (p^2(p-1)) automorphism-order theorem remains CONDITIONAL. Step 2's independently audited filtered-extension result is not reopened by this correction.

Detailed audit: `research/PAPER5_STEP3_SECOND_ORDER_LIFTING_AUDIT_2026-10-05.md`.


## 2026-10-05 — Step 3 second-jet re-audit

The formal (J_k^2(r)=[r]\in D_k/D_{k+2}) construction for (k\ge2) is accepted as a valid repair of the previous type error. A fixed Magnus embedding can also provide the degree-(k) and degree-((k+1)) homogeneous coefficients.

However, the crucial assertion
[
sec_{k+1}(\widetilde g(r))\in gr_{k+1}(R)
]
is not yet proved. The nonlinear Magnus substitution (X\mapsto aX+\binom a2X^2+\cdots) acts by degree-raising insertion/substitution operators. The claim that the resulting correction is exactly
[
C_k(R_k)=[V,R_k]
]
is not automatic and has not been derived. Restricted-ideal closure under brackets/restricted powers does not imply closure under an arbitrary such insertion operator.

Therefore the second-jet itself **PASS / GENERAL**, but its preservation of the relation ideal is **OPEN / LOAD-BEARING**. The strengthened (L_k), kernel preservation, and (operatorname{Im}=S_{11}(p)) equality remain OPEN / LOAD-BEARING; the (p^2(p-1)) theorem remains CONDITIONAL.

Detailed audit: research/PAPER5_STEP3_SECOND_JET_REAUDIT_2026-10-05.md.


## 2026-10-06 — Paper 5 Step 3 second-jet substitution-order audit

The submitted (T_{a,b,k}) repair was independently checked. The raw associative derivation claims are valid: (D_X,D_Z,D_{Y,1},D_{Y,2}) preserve the two-sided commutator ideal, and the Leibniz degree count gives (D(u^p)\in I_{p^2+1}) in the mod-(p) graded layer. The (X^{p^2}-Z^{p^2}) vanishing is likewise a mod-(p) statement and requires explicit coefficient-field notation.

A load-bearing error remains in the second-order substitution formula. For (x\mapsto x^a, y\mapsto yx^b, z\mapsto z^a), the linear Magnus map is (L(X)=aX, L(Y)=Y+bX, L(Z)=aZ), so the quadratic correction acts after (L). The actual correction is schematically (T_{a,b,k}(L(R_k))), not (T_{a,b,k}(R_k)). For (R_2=[X,Y]), the actual degree-3 correction has coefficients (ab, c, -(ab+c)) on (XYX,XXY,YXX), while the submitted (T) gives (b,c,-(b+c)). Hence the displayed (sec_{k+1}) formula is **FAIL/CLOSED as written**.

The finite-stage residual factorization does not need the claimed equality (D_j=(R\cap D_j)(R\cap D_{j+1})D_{j+2}). From (r^{(j)}\in R\cap D_j), its initial class is automatically in (gr_j(R)); choose a representative in (R\cap D_j) and the residual lies in (R\cap D_{j+1}). Thus this part can survive, including at exceptional (j=p,p^2).

Classification: raw (T(I_k)\subseteq I_{k+1}) PASS/GENERAL; corrected actual second-order operator (C_{a,b}) OPEN/LOAD-BEARING; strengthened (L_k), kernel preservation, and (operatorname{Im}(Aut(W_n)\to GL(V))=S_{11}(p)) remain OPEN/LOAD-BEARING; (p^2(p-1)) remains CONDITIONAL. Detailed audit: `research/PAPER5_STEP3_SECOND_JET_AUDIT_ADDENDUM_2026-10-06.md`.


## 2026-10-06 — Paper 5 Step 3 corrected second-jet closure

The substitution-order error is repaired by (C_{a,b,k}=T_{a,b,k}\circ L). For (x\mapsto x^a, y\mapsto yx^b, z\mapsto z^a), the linear Magnus part is (L(X)=aX, L(Y)=Y+bX, L(Z)=aZ). For (R_2=[X,Y]), the corrected (XYX)-coefficient is (ab), not (b).

The associative derivations preserve the two-sided commutator ideal, (L) preserves it as well, and hence (C(I_k)\subseteq I_{k+1}). The (p)-power exceptional layer is handled in the explicit mod-(p) Magnus layer by (D(u^p)=\sum_{i=0}^{p-1}u^iD(u)u^{p-1-i}), with degree (p^2+1), while (D(X^{p^2}-Z^{p^2})=0) only in characteristic (p).

Thus (C_{a,b,k}(gr_kR)\subseteq gr_{k+1}R), the corrected secondary term lies in (gr_{k+1}R), and the finite-stage residual factorization yields (widetilde g(R)\subseteq R) without the stronger Zassenhaus-layer product equality.

**Classification:** corrected (C_{a,b,k}), secondary relation term, finite-stage factorization, and kernel preservation are **CLOSED / GENERAL within the declared mod-(p) Magnus layer**. Step 3 equality (operatorname{Im}(Aut(W_n)\to GL(V))=S_{11}(p)) remains **OPEN / LOAD-BEARING**, and the (p^2(p-1)) theorem remains **CONDITIONAL**. Evidence: research/PAPER5_STEP3_SECOND_JET_AUDIT_ADDENDUM_2026-10-06.md.

## 2026-10-06 — S11 equality re-audit: proposed upper bound rejected

The proposed proof of
\[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))\subseteq S_{11}(p)
\]
does **not** close the load-bearing gate.

The decisive defect is the passage from an arbitrary
\[
g\in\operatorname{Aut}(W_n),\qquad W_n=F/RD_{n+1},
\]
to statements in the full quotient (F/R), such as “(z) is central in (F/R)” and
\[
[g(x),g(y)]=[x,y]^{\det_{xy}},\qquad
[g(x),g(z)]=[g(y),g(z)]=1
]
as identities in (F/R). An automorphism of the finite window (W_n) does not automatically lift to an automorphism of (F/R); that is precisely part of the unresolved finite-window identification/lifting problem. Thus these (F/R)-identities cannot be used as an upper-bound argument without an independent lifting theorem.

A second independent gap is the assertion that (m_{z,x}=0) is a “representative choice.” The coefficient (m_{z,x}) is part of the actual linear map on
\[
V=F/D_2,
\]
and the relation (p(e_x-e_z)=0) in the abelianized relation subgroup does not permit changing an arbitrary (\mathbf F_p)-coefficient in (V) by a representative choice. No prior result currently establishes (m_{z,x}=0).

Therefore the proposed upper bound
\[
\operatorname{Im}\subseteq S_{11}(p)
\]
is **OPEN / LOAD-BEARING**, and consequently the equality
\[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p)
\]
and the (p^2(p-1)) theorem remain **OPEN / CONDITIONAL**, respectively.

The lower-bound construction is different: the already-closed kernel-preservation result
\[
\widetilde g_{a,b}(R)\subseteq R
\]
does give genuine induced automorphisms of (F/R) and (W_n), with matrices
\[
M_{a,b}=\begin{pmatrix}a&b&0\\0&1&0\\0&0&a\end{pmatrix},
\qquad a\in\mathbf F_p^\times, b\in\mathbf F_p.
\]
Hence
\[
S_{11}(p)\subseteq\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))
\]
is **CLOSED / GENERAL**, assuming the already-closed (\widetilde g(R)\subseteq R) gate. Equality is not established.

This supersedes the immediately preceding 2026-10-06 claim that the (S_{11}(p)) upper bound and equality were CLOSED/GENERAL.


## 2026-10-06 — S11 scalar-equality counterexample: m=a is not forced

**FAIL / CLOSED as submitted; exact image remains OPEN.**

The boundary correction
\[
n<p:\quad W_n\cong(\mathbf F_p)^3,\quad IA(W_n)=1,
\]
and
\[
n=p:\quad IA(W_p)\cong\operatorname{Hom}(\mathbf F_p^3,\mathbf F_p^2)\cong\mathbf F_p^6
\]
is accepted.

However, the proposed (n=p) upper-bound argument forcing the same scalar on the (x)- and (z)-directions contains a decisive algebraic error. For arbitrary (m,a\in\mathbf F_p^\times),
\[
x\mapsto x^m z^{a-m},\qquad y\mapsto y,\qquad z\mapsto z^a
\]
preserves the defining relations directly in (W_p):
\[
[x^m z^{a-m},y]=[x,y]^m=x^{pm}z^{-pm}
\]
and
\[
(x^m z^{a-m})^p(z^a)^{-p}=x^{pm}z^{-pm}.
\]
The induced map on (V=W_p/D_2(W_p)) is invertible, so this is an actual automorphism.

Thus (m) and (a) are independent. The torsion subgroup
\[
T(W_p^{ab})=\langle e_x-e_z\rangle
\]
only gives (c=a-m) for (g(x)=x^m z^c, g(z)=z^a); it does **not** give (m=a).

Therefore the previous
\[
\operatorname{Im}=S_{11}(p),\qquad |\operatorname{Im}|=p^2(p-1),\qquad |\operatorname{Aut}(W_p)|=p^8(p-1)
\]
claim is **FAIL / CLOSED**.

A corrected candidate lower-bound subgroup is
\[
S'_{{11}}(p)=
\left\{
\begin{pmatrix}
m&b&0\\
0&1&0\\
a-m&d&a
\end{pmatrix}
: m,a\in\mathbf F_p^\times, b,d\in\mathbf F_p
\right\},
\]
with order (p^2(p-1)^2). This is only a lower bound; equality with (S'_{11}(p)) is **OPEN**. Consequently
\[
|\operatorname{Aut}(W_p)|\ge p^8(p-1)^2,
\]
while the exact order remains **OPEN**.

Detailed audit: `research/PAPER5_STEP3_S11_UPPER_BOUND_COUNTEREXAMPLE_AUDIT_2026-10-06.md`.


## 2026-10-06 — Paper 5 Step 3 corrected image target S'11

The previous (S_{11}(p)) target is permanently rejected. The finite-window calculation at (n=p) gives the explicit automorphisms
\[
g_{m,a}:x\mapsto x^m z^{a-m},\qquad y\mapsto y,\qquad z\mapsto z^a,
\qquad m,a\in\mathbf F_p^\times,
\]
and
\[
[x^m z^{a-m},y]=x^{pm}z^{-pm}
=(x^m z^{a-m})^p(z^a)^{-p}.
\]
On
\[
A=W_p^{ab}=\mathbf Z_p^3/\langle p(e_x-e_z)\rangle,
\]
the torsion generator satisfies
\[
g_*(e_x-e_z)=m(e_x-e_z),
\]
so torsion preservation allows (m\ne a). Thus the scalar-equality step is **FAIL / CLOSED**.

The corrected explicit image subgroup is
\[
S'_{11}(p)=
\left\{
\begin{pmatrix}
m&b&0\\
0&1&0\\
a-m&d&a
\end{pmatrix}
:
m,a\in\mathbf F_p^\times, b,d\in\mathbf F_p
\right\},
\]
with
\[
|S'_{11}(p)|=p^2(p-1)^2.
\]

Classification:
- (n<p: W_n\cong(\mathbf F_p)^3, IA(W_n)=1, \operatorname{Aut}(W_n)=GL_3(\mathbf F_p)): **PASS / CLOSED**.
- (IA(W_p)\cong\operatorname{Hom}(\mathbf F_p^3,\mathbf F_p^2)\cong\mathbf F_p^6): **PASS / CLOSED**.
- (S_{11}(p)) with order (p^2(p-1)): **FAIL / CLOSED**.
- (S'_{11}(p)\subseteq\operatorname{Im}(\operatorname{Aut}(W_p)\to GL(V))): **PASS / CLOSED**.
- Exact equality \(\operatorname{Im}=S'_{11}(p)\): **OPEN / LOAD-BEARING**; an upper-bound proof is still required.
- Consequently \(|\operatorname{Aut}(W_p)|\ge p^8(p-1)^2\), while the exact order remains **OPEN**.
- The already audited (J_k^2), corrected (C_{a,b,k}=T_{a,b,k}\circ L), and kernel-preservation route remain **PASS / CLOSED / GENERAL** within their declared scope.

This supersedes the previous (S_{11})-based Step 3 target. Detailed audit:
`research/PAPER5_STEP3_S11_UPPER_BOUND_COUNTEREXAMPLE_AUDIT_2026-10-06.md`.


## 2026-10-06 — W_p relation-package consistency audit

**FAIL / CLOSED as submitted.**

The proposed (n=p) upper-bound proof simultaneously assumes
[
D_p(W_p)=\mathbf F_p^2=\langle x^{[p]},y^{[p]}\rangle,qquad x^{[p]}=z^{[p]},
]
and the defining relation
[
[x,y]=x^p z^{-p}.
]
Since (D_{p+1}(W_p)=1), these are equalities in (W_p), so they imply
[
[x,y]=1.
]
The subsequent coefficient comparison
[
x^{p(mv-bu)}z^{-p(mv-bu)}
=x^{pm}y^{pu}z^{p(c-a)}
]
cannot then extract (mv=m): that step requires (x^p) and (z^p) to be independent, contradicting (x^p=z^p).

Therefore the submitted deductions (m_{y,x}=0, m_{y,y}=1, c=a-m), the equality (operatorname{Im}=S'_{11}(p)), and the exact (IA(W_p)\cong\mathbf F_p^6) / automorphism-order claims are **not closed** and are **FAIL / CLOSED as submitted**.

The actual presentation-level relation
[
[x,y]=x^p z^{-p}
]
does not itself imply (x^p=z^p). Hence the correct next gate is to recompute (D_2(W_p),D_p(W_p),Z(W_p),W_p^{ab}), and (IA(W_p)) directly from
[
W_p=F/(R D_{p+1}).
]

Audit: `research/PAPER5_WP_BOUNDARY_CONSISTENCY_AUDIT_2026-10-06.md`.


## 2026-10-06 — W_p corrected D_p structure closes Step 3

The previous boundary audit is superseded by the corrected intrinsic calculation. At (n=p),
[
D_p(W_p)=\langle X=x^p,Y=y^p,Z=z^p\rangle\cong\mathbf F_p^3,
qquad [x,y]=XZ^{-1},
]
with (D_p) central of exponent (p). The relation therefore does not impose (X=Z); it records the commutator as (XZ^{-1}).

Consequently
[
IA(W_p)\cong\operatorname{Hom}(V,D_p)\cong\mathbf F_p^9.
]
For an arbitrary automorphism, centrality of (g(z)) gives (g(z)\equiv z^a\pmod{D_2}), and writing
[
g(x)\equiv x^m y^u z^c,qquad g(y)\equiv x^b y^v z^d
]
the defining relation gives
[
X^{mv-bu}Z^{-(mv-bu)}=X^mY^uZ^{c-a}.
]
Independence of (X,Y,Z) forces
[
u=0,qquad v=1,qquad c=a-m.
]
Thus
[
\operatorname{Im}(\operatorname{Aut}(W_p)\to GL(V))
\subseteq S'_{11}(p),
]
where
[
S'_{11}(p)=
\left\{
\begin{pmatrix}
m&b&0\\
0&1&0\\
a-m&d&a
\end{pmatrix}
:m,a\in\mathbf F_p^\times, b,d\in\mathbf F_p
\right\}.
]
The explicit realization family gives the reverse inclusion, so
[
\operatorname{Im}=S'_{11}(p),qquad |\operatorname{Im}|=p^2(p-1)^2.
]
Hence
[
|\operatorname{Aut}(W_p)|=p^9\,p^2(p-1)^2
=p^{11}(p-1)^2.
]

Classification:
- (D_p(W_p)\cong\mathbf F_p^3): **PASS / CLOSED / GENERAL**.
- (IA(W_p)\cong\mathbf F_p^9): **PASS / CLOSED / GENERAL**.
- (m_{y,x}=0, m_{y,y}=1, c=a-m): **PASS / CLOSED / GENERAL**.
- (S'_{11}(p)\subseteq\operatorname{Im}): **PASS / CLOSED / GENERAL**.
- (\operatorname{Im}=S'_{11}(p)): **PASS / CLOSED / GENERAL**.
- (|\operatorname{Aut}(W_p)|=p^{11}(p-1)^2): **PASS / CLOSED / GENERAL**.
- Previous (D_p\cong\mathbf F_p^2), (IA\cong\mathbf F_p^6), and (p^8(p-1)^2) claims: **FAIL / CLOSED / SUPERSEDED**.

Detailed audit: `research/PAPER5_WP_CORRECTED_STRUCTURE_STEP3_CLOSURE_2026-10-06.md`.


## 2026-10-06 — Paper 5 four-gate literature audit

The four-gate literature audit (finite Zassenhaus windows / relation modules and initial forms / IA-Frattini image / p^2 automorphism-order phenomenon) closes the **literature novelty gate within the searched scope**. Jennings–Lazard, free pro-p/Magnus–Zassenhaus, Labute relation-ideal machinery, and general IA/Frattini facts are established prior art. No identified source gives the specific intrinsic finite-window calculation for the present W_p=F/(R D_{p+1}), nor the factorization of Aut(W_n) -> GL(W_n/Phi(W_n)) through the mixed degree-(2,p) relation-jet stabilizer with the observed p^2 order phenomenon.

**Critical consistency correction:** the current corrected W_p result is D_p(W_p) isomorphic to F_p^3, IA(W_p) isomorphic to F_p^9, and |Aut(W_p)|=p^{11}(p-1)^2. Any literature-audit note stating D_p isomorphic to F_p^2, IA isomorphic to F_p^6, or |Aut|=p^8(p-1)^2 is historical/superseded and must not be propagated.

Classification: **PASS / CLOSED for literature novelty boundary; OPEN / LOAD-BEARING for the W_{p+1} intrinsic factorization and p^2 theorem.** Detailed audit: research/PAPER5_LITERATURE_AUDIT_2026-10-06.md.


## SOURCE: paper4/Paper4_strengthened_2026-10-05.tex

<!-- blob-sha: 69bf08d490dff5c59200dfa4fd61a8a3055fba0c -->

\\documentclass[11pt]{article}
\\usepackage{amsmath,amssymb,amsthm,mathtools}
\\usepackage[margin=1in]{geometry}
\\usepackage{hyperref}
\\newtheorem{theorem}{Theorem}[section]
\\newtheorem{proposition}[theorem]{Proposition}
\\newtheorem{corollary}[theorem]{Corollary}
\\newtheorem{lemma}[theorem]{Lemma}
\\newtheorem{remark}[theorem]{Remark}
\\newcommand{\\D}{D}
\\newcommand{\\F}{F}
\\newcommand{\\K}{K}
\\newcommand{\\eps}{\\varepsilon}
\\title{Delayed Finite-Window Visibility and Non-Rigidity of Power-Root One-Relator Pro-$p$ Groups}
\\author{Seocopy Research Project}
\\date{October 5, 2026}

\\begin{document}
\\maketitle

\\begin{abstract}
We study finite Zassenhaus windows of pro-$p$ groups defined by a hidden power-root relation
$z^{p^s}=x_1^{p^a}r_2$, where $r_2$ has nonzero quadratic initial form. The main result is an exact critical-window theorem in a declared intrinsic stress-family scope. Below the critical scale $p^s+1$ the hidden relation is invisible; at $p^s+1$ an intrinsic transfer obstruction separates the cases $a=s$ and $a=\\infty$. A key filtration theorem controls how Zassenhaus depth changes after passage to open subgroups:
$D_n(F)\\cap K\\subseteq D_{\\lceil n/p^s\\rceil}(K)$ for $[F:K]=p^s$. We prove that the factor $p^s$ is uniformly optimal. The subgroup comparison is treated as infrastructure assembled from classical Zassenhaus, Jennings--Lazard, Schreier, and weighted-Schreier machinery; the Paper 4 contribution is the downstream intrinsic transfer obstruction, exact separation, and critical threshold.
\\end{abstract}

\\section{Introduction}
Finite quotients often erase information carried by a defining relation until a sharply determined filtration level. We make this phenomenon precise for a power-root one-relator family and distinguish universal filtration infrastructure from the family-specific obstruction that survives in the critical window.

The guiding phenomenon is
\\[
\\text{lower-window blindness}
\\quad\\longrightarrow\\quad
\\text{critical transfer defect}
\\quad\\longrightarrow\\quad
\\text{exact separation}.
\\]
The result is deliberately scoped: arbitrary relations of Zassenhaus degree at least two do not satisfy a degree-only version of the theorem.

\\section{Setup}
Let $p$ be odd, let $s\\ge2$, let $d$ be even, and let $F$ be free pro-$p$ on
$z,x_1,\\ldots,x_d$. Let
$r_2\\in D_2(F)\\setminus D_3(F)$ have nondegenerate alternating quadratic initial form on
$V=F/D_2(F)$. Consider
\\[
G_{s,a}=F/\\overline{\\langle\\langle z^{p^s}x_1^{-p^a}r_2^{-1}\\rangle\\rangle},
\\qquad
1\\le a\\le\\infty,
\\]
where $p^\\infty$ denotes the absent power term. Put
\\[
W_n(G)=G/D_n(G).
\\]
We focus on the critical window $W_{p^s+1}$.

\\section{Universal subgroup-depth compression}

\\begin{theorem}[Index-$p$ subgroup-depth comparison]
Let $G$ be a pro-$p$ group and let $K\\trianglelefteq G$ be open of index $p$. Then, for every $n\\ge1$,
\\[
D_n(G)\\cap K\\subseteq D_{\\lceil n/p\\rceil}(K).
\\tag{SC}
\\]
\\end{theorem}

\\begin{proof}
Put
\\[
A=\\mathbf F_p[[K]],\\qquad B=\\mathbf F_p[[G]],\\qquad J=I_K,
\\]
and choose $a\\in G$ whose image generates $G/K$. With $t=a-1$, normality of $K$ gives
\\[
B=\\bigoplus_{r=0}^{p-1}At^r,
\\qquad
t^p=a^p-1\\in J.
\\]
For $m\\ge1$ define the weighted normal-form filtration
\\[
E_m=
\\bigoplus_{r=0}^{p-1}
J^{\\max(0,\\lceil(m-r)/p\\rceil)}t^r,
\\]
with $J^0=A$.

For a normal-form monomial $ct^r$, $c\\in J^q$, assign weight $pq+r$. If
$\\sigma(c)=aca^{-1}$, then
\\[
tc=\\sigma(c)t+(\\sigma(c)-c),
\\]
and $\\sigma(J^q)=J^q$. Thus normalization of products never lowers the weight. When a power $t^{j+s}$ reaches $p$, write
\\[
t^{j+s}=(t^p)^u t^v,
\\qquad j+s=up+v,\quad 0\\le v<p,
\\]
and use $t^p\\in J$; each such replacement preserves the same total weight. Hence
\\[
E_mE_\\ell\\subseteq E_{m+\\ell}.
\\tag{NF}
\\]
Since $I_G=JB+tB\\subseteq E_1$, induction gives
\\[
I_G^n\\subseteq E_n.
\\]
Taking the direct $A$-summand yields
\\[
I_G^n\\cap A\\subseteq J^{\\lceil n/p\\rceil}.
\\]
Finally, the dimension-subgroup identity
\\[
D_n(H)=H\\cap(1+I_H^n)
\\]
gives (SC). The argument explicitly retains the terms arising from $t^rJ^q$; no augmentation-ideal intersection equality is assumed.
\\end{proof}

\\begin{theorem}[Index-$p^s$ comparison]
If $K\\trianglelefteq G$ is open of index $p^s$, then
\\[
\\boxed{D_n(G)\\cap K\\subseteq D_{\\lceil n/p^s\\rceil}(K).}
\\tag{SC_s}
\\]
\\end{theorem}

\\begin{proof}
Choose a subnormal chain
$G=K_0>K_1>\\cdots>K_s=K$
with $[K_{i-1}:K_i]=p$. Iterating (SC) gives the result, because
\\[
\\left\\lceil\\frac{\\lceil m/p\\rceil}{p}\\right\\rceil
=
\\left\\lceil\\frac m{p^2}\\right\\rceil
\\]
and hence the ceiling operations compose exactly.
\\end{proof}

\\begin{proposition}[Uniform sharpness]
The factor $p^s$ in (SC_s) is uniformly optimal in the free-pro-$p$ class: there are infinitely many $n$ for which
\\[
D_n(F)\\cap K\\not\\subseteq D_{\\lceil n/p^s\\rceil+1}(K).
\\]
\\end{proposition}

\\begin{proof}
Let $F=\\langle a,b\\rangle$ be free pro-$p$ and let
$K=\\ker(F\\to C_{p^s})$, with $a$ mapping to a generator and $b$ to zero.
The Schreier basis contains $c_0=a^{p^s}$. For $m\\ge1$ put
\\[
g_m=a^{p^{m+s-1}}=c_0^{p^{m-1}},
\\qquad
n_m=p^{m+s-1}.
\\]
Then $g_m\\in D_{n_m}(F)\\cap K$, while
$g_m\\notin D_{p^{m-1}+1}(K)$ and
$\\lceil n_m/p^s\\rceil=p^{m-1}$. Thus no uniform improvement by one level is possible.
\\end{proof}

\\begin{remark}
The sharpness statement is uniform optimality of the factor $p^s$, not pointwise equality for every integer $n$ and not sharpness for every arbitrary pro-$p$ group.
\\end{remark}
\\section{From subgroup depth to transfer depth}
Let $m=\\lceil n/p\\rceil$. Jennings--Lazard theory implies that the image of
$D_m(K)$ in $K^{\\mathrm{ab}}$ is controlled by the corresponding $p$-power layer. In the critical case $n=p^s+1$, the index-$p$ comparison gives
$D_{p^s+1}(F)\\cap K\\subseteq D_{p^{s-1}+1}(K)$, and the abelianized transfer calculation yields
\\[
\\operatorname{im}(D_{p^s+1}(F)\\cap K\\to K^{\\mathrm{ab}})
\\subseteq p^sK^{\\mathrm{ab}}.
\\]
More generally, with
$e(n)=\\lceil\\log_p\\lceil n/p\\rceil\\rceil$,
the audited transfer-depth law gives
\\[
\\operatorname{im}(D_n(F)\\cap K\\to K^{\\mathrm{ab}})
\\subseteq p^{e(n)}K^{\\mathrm{ab}}.
\\]
The precise critical specialization is the one used below.

\\section{The stress family and the critical obstruction}

For the stress family, the lower windows $W_n$ with $n\\le p^s$ do not see the hidden power-root relation at the critical initial layer. At $n=p^s+1$, the defining relation first enters the relevant Zassenhaus layer.

The nondegenerate alternating quadratic initial form of $r_2$ supplies the intrinsic one-dimensional radical direction used to define the index-$p$ kernel. No presentation-dependent character is chosen.

Let
\\[
S_s(W)=\\operatorname{im}\\bigl(W^{\\mathrm{ab}}[p^s]
\\longrightarrow W^{\\mathrm{ab}}/pW^{\\mathrm{ab}}\\bigr).
\\]
In the declared stress-family scope this is one-dimensional. If $t\\in W^{\\mathrm{ab}}[p^s]$ spans this line and $V$ denotes the intrinsic transfer to the canonical kernel abelianization, define
\\[
\\eps_s(W)=p^{s-1}V(t)\\pmod{p^sK^{\\mathrm{ab}}}.
\\tag{T}
\\]
Replacing $t$ by another lift of the same line changes the value by an element of $p^sK^{\\mathrm{ab}}$, so the vanishing of $\\eps_s$ is intrinsic.

\\begin{lemma}[Critical transfer-depth bound]
At $n=p^s+1$,
\\[
\\operatorname{im}\\bigl(D_{p^s+1}(G)\\cap K
\\to K^{\\mathrm{ab}}\\bigr)
\\subseteq p^sK^{\\mathrm{ab}}.
\\tag{TF_s}
\\]
\\end{lemma}

\\begin{proof}
By (SC),
\\[
D_{p^s+1}(G)\\cap K
\\subseteq D_{p^{s-1}+1}(K).
\\]
The Jennings--Lazard product
\\[
D_m(K)=\\prod_{ip^j\\ge m}\\gamma_i(K)^{p^j}
\\]
shows, after abelianization, that the first surviving pure-power layer for
$m=p^{s-1}+1$ is $p^sK^{\\mathrm{ab}}$. Hence the displayed image is contained in that subgroup.
\\end{proof}

Now use the Schreier coordinates for the canonical kernel. The defining relator has trivial character value and its normal closure lies in $K$. Since $r_2\\in[K,K]$, its image in $K^{\\mathrm{ab}}$ vanishes. The resulting abelianized relation is, up to the harmless sign convention,
\\[
p^{s-1}U-p^aA_1=0.
\\tag{L}
\\]
For $a=s$, the critical transfer class is represented by
\\[
p^{s-1}(\\sigma-1)^{p-1}A_0.
\\]
Modulo the relation lattice and $p^sK^{\\mathrm{ab}}$, it is nonzero; explicitly
\\[
(\\sigma-1)^{p-1}A_0\\equiv\\sum_jA_j\\pmod p,
\\]
so the surviving class is
\\[
p^{s-1}\\sum_jA_j\\ne0.
\\]
By (TF_s), no element coming from $D_{p^s+1}(G)\\cap K$ can kill this class in the finite-window quotient.

For $a=\\infty$, there is no finite power relation in the $U$-direction. Taking $t=z$ gives $V(t)=U$, and the corresponding normalized class vanishes because $p^{s-1}U$ lies in the relator image. Thus
\\[
\\eps_s(W_{p^s+1}(G_{s,s}))\\ne0,
\\qquad
\\eps_s(W_{p^s+1}(G_{s,\\infty}))=0.
\\tag{E}
\\]

\\begin{theorem}[Exact critical separation]
For odd $p$, $s\\ge2$, even $d$, and nondegenerate alternating quadratic initial form $r_2$,
\\[
\\boxed{
W_{p^s+1}(G_{s,s})
\\not\\cong
W_{p^s+1}(G_{s,\\infty}).
}
\\]
\\end{theorem}

\\begin{proof}
The canonical radical line makes $K$ intrinsic. The transfer predicate (T) is invariant under changing its spanning lift and under isomorphism of the finite filtered window. Equation (E) therefore gives an isomorphism invariant that has different values on the two critical windows. Hence they are not isomorphic.
\\end{proof}

\\section{Complete critical-window classification of $a$}
For $1\\le a<s$, abelianization gives
\\[
W_{s,a}^{\\mathrm{ab}}
\\cong
\\mathbf Z_p/p^a\\oplus
(\\mathbf Z_p/p^{s+1})^d,
\\]
so distinct values of $a$ are separated already by abelianization. If $a>s$, then
$p^a\\ge p^{s+1}>p^s+1$, so $x_1^{p^a}\\in D_{p^s+1}(F)$ and
\\[
W_{s,a}=W_{s,\\infty}.
\\]
At $a=s$, abelianization agrees with the $a=\\infty$ case, but the intrinsic transfer obstruction above separates the two. Thus the critical window has exactly one nontrivial boundary layer, namely $a=s$.

\\begin{corollary}[Exact threshold]
Define
\\[
n_{\\rm sep}(s)=
\\min\\{n:\\,
W_n(G_{s,s})\\not\\cong W_n(G_{s,\\infty})\\}.
\\]
Then, in the declared stress-family scope,
\\[
\\boxed{n_{\\rm sep}(s)=p^s+1.}
\\]
\\end{corollary}

\\begin{proof}
The lower-window blindness gives isomorphism for all $n\\le p^s$. The preceding theorem gives non-isomorphism at $n=p^s+1$.
\\end{proof}

\\section{What is new and what is not}
The filtration machinery should not be overstated as new foundational theory. Zassenhaus, Jennings--Lazard, Schreier, Magnus, and weighted-Schreier methods provide the ingredients. The exact subgroup comparison is isolated and assembled in the form required by the finite-window transfer argument, and the $p^s$ factor is shown uniformly optimal.

The Paper-4-specific contribution is the downstream package:
\\begin{enumerate}
\\item an intrinsic finite-window transfer obstruction;
\\item exact separation of $a=s$ from $a=\\infty$ at $p^s+1$;
\\item complete classification of the critical-window parameter $a$ in the declared stress-family scope;
\\item the exact threshold $n_{\\rm sep}(s)=p^s+1$.
\\end{enumerate}

The arbitrary relation-degree-only claim is not asserted: $\\operatorname{ord}_Z(r)\\ge2$ alone is insufficient.

\\section{Literature and logical boundaries}
The audited literature establishes the component weighted-Schreier machinery. The present manuscript does not claim priority for those components. The Magnus prefix-code proof is retained as an independent verification route.

The intrinsic transfer obstruction, exact unmarked separation, and threshold are the principal novelty candidates. Literature priority claims should remain tied to the bounded audit actually performed.

\\section{Conclusion}
Paper 4 establishes a precise mechanism by which a hidden power-root relation is invisible below a finite Zassenhaus window and becomes intrinsically detectable exactly at the next critical layer. The universal subgroup-depth law explains the quantitative loss of depth under passage to index-$p^s$ kernels, and its uniform sharpness shows that this loss cannot be improved in general. The family-specific transfer obstruction then converts this universal compression into an exact finite-window separation theorem.

\\end{document}


## SOURCE: research/scripts/paper4_root_visibility_checks_2026-10-04.py

<!-- blob-sha: 7db091c062f7304ea7d74c3da47d1e413463fc6e -->

"""Independent checks for Paper 4 root-visibility/non-rigidity audit (2026-10-04)."""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def snf_invariants(p,s,a,d):
    A=sp.zeros(d+2,d+1)
    for i in range(d+1):
        A[i,i]=p**(s+1)
    A[d+1,0]=p**s
    A[d+1,1]=-p**a
    S=smith_normal_form(A, domain=ZZ)
    return [abs(S[i,i]) for i in range(min(S.shape)) if S[i,i] != 0]

cases=[(3,2,1,2),(3,3,2,2),(5,2,1,4),(3,5,2,2),(3,2,2,2)]
for p,s,a,d in cases:
    got=snf_invariants(p,s,a,d)
    expected=[p**a]+[p**(s+1)]*d
    assert got==expected, (p,s,a,d,got,expected)
    print((p,s,a,d), "PASS", got)

for p,s in [(3,1),(3,2),(5,2),(3,3)]:
    assert p**s >= 3
print("delayed-window filtration check: PASS")


## SOURCE: research/scripts/paper4_w10_schreier_transfer_check_2026-10-04.py

<!-- blob-sha: 1d6094ed033b0ec5a9c08447faf1c1bd6dfa4637 -->

#!/usr/bin/env python3
"""Independent base-case check for the corrected intrinsic W10 Schreier calculation.

Model: p=3, s=2, r=z^9*x^-9*[x,y]^-1.
Basis: (u,a0,a1,a2,b0,b1,b2), u=z^3.
"""

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# RS abelianization relations: 3u - 9 a_i = 0, i=0,1,2.
A = sp.zeros(3, 7)
for i in range(3):
    A[i, 0] = 3
    A[i, i + 1] = -9

S = smith_normal_form(A, domain=ZZ)
assert [S[i, i] for i in range(3)] == [3, 9, 9]

# sigma fixes u and cycles each of a0,a1,a2 and b0,b1,b2.
P = sp.zeros(7)
P[0, 0] = 1
for base in (1, 4):
    P[base + 1, base] = 1
    P[base + 2, base + 1] = 1
    P[base, base + 2] = 1

D2 = (P - sp.eye(7)) ** 2
v = sp.Matrix([0, 1, 0, 0, 0, 0, 0])
w = D2 * v

# Mod 3: delta^2(a0) = a0+a1+a2.
assert [int(x) % 3 for x in w] == [0, 1, 1, 1, 0, 0, 0]

# Integral nonvanishing of 3*delta^2(a0): test membership in row lattice A.
target = sp.Matrix([[0, 3, 3, 3, 0, 0, 0]])
# Solve A^T c = target^T over Q and check there is no solution.
assert sp.linsolve((A.T, target.T)) == sp.EmptySet

print("SNF =", S)
print("P =")
print(P)
print("(sigma-1)^2(a0) =", list(w))
print("3*(sigma-1)^2(a0) is nonzero in the RS abelianization lattice.")


---

# SOURCE: research/PAPER4_QPOS_CLASS2_FACTOR_THROUGH_AUDIT_2026-10-02.md

<!-- blob-sha: 4fea101d63c8925aa9bddf6890221064657795cf -->

# PAPER 4 — Relative Class-2 Factor-Through Audit
## 2026-10-02

### Purpose

Test whether the first strict-compression candidate
\[
C_n^{(2)}(E_n):
1\to K_n/\gamma_3(K_n)\to W_n/\gamma_3(K_n)\to D/D_n(D)\to1
\]
is already determined by the previously closed abelian/H1-extension/ordinary-graded layers.

This is a factor-through pretest only. It does not yet claim T1 separation.

### 1. Intrinsic decomposition

Put
\[
A_n=K_n/\gamma_2(K_n),\qquad
B_n=\gamma_2(K_n)/\gamma_3(K_n).
\]
Then the class-2 kernel is determined by the central extension
\[
1\to B_n\to K_n/\gamma_3(K_n)\to A_n\to1
\]
together with the commutator pairing
\[
\beta_n:A_n\wedge A_n\to B_n,
\qquad
\beta_n(\bar u,\bar v)=[u,v]\bmod\gamma_3(K_n),
\]
and the induced action of \(D/D_n(D)\).

The key point is that the previously closed H1-extension layer retains only the abelian kernel module/coinvariant extension data. It has no slot in which the alternating commutator pairing \(\beta_n\) can be reconstructed in general.

### 2. Structural non-factorization test

A universal factorization
\[
C_n^{(2)}=F(A_n,(A_n)_D,H_1\text{-extension},\operatorname{gr}_{Zass})
\]
would force \(\beta_n\) to be a functorial invariant of those closed layers.

That implication is false at the level of the ambient class-2 extension category: class-2 central extensions with the same abelianization/module data can have different commutator pairings. Thus the class-2 quotient contains a genuinely new type of information, namely an integral commutator-extension datum, which is not formally a function of the abelian/E2 package.

This is only a **structural PASS / LOCAL**. The admissible Paper-4 stress family is narrower, so an explicit pair inside the q>0 stress family is still required before declaring a stress-family non-factorization theorem.

### 3. Ordinary associated-graded comparison

The mod-p Zassenhaus associated graded is already closed as an s-detector in the q>0 stress model. Its degree-2 bracket records only the initial Demushkin commutator form.

The class-2 quotient is not identical to this graded object: it retains integral lower-central information and the p-power/central-extension structure before reduction to the associated graded.

Therefore the previous graded blindness does **not** imply
\[
C_n^{(2)}\text{ factors through }\operatorname{gr}_{Zass}.
\]
No closure is justified from the graded result alone.

### 4. What remains unresolved

The load-bearing question is now sharply reduced to the stress family
\[
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,
\qquad q_D=p^a>0,
\qquad s>a.
\]

For fixed external threshold \(m>a\), the required T1 test is whether a single depth \(n=n(m)\), independent of s, makes
\[
C_n^{(2)}(G_{s,a})\not\cong C_n^{(2)}(G_{t,a})
\]
whenever
\[
s<m\le t.
\]

The first quantity to compute is not a raw Magnus coefficient. It is the intrinsic central extension invariant:
- the D-module \(A_n\);
- the central commutator target \(B_n\);
- the pairing \(\beta_n\);
- and, crucially, the induced p-power map on the class-2 kernel modulo \(\gamma_3\).

A successful T1 proof must show that the threshold information survives all quotient/kernel automorphisms and does not reduce to the already closed abelian/E2/graded data.

### 5. Current classification

- structural distinction of class-2 data from abelian/H1 layers: **PASS / LOCAL**;
- factorization through ordinary mod-p associated graded: **OPEN**, not implied by prior graded blindness;
- stress-family factor-through test: **OPEN / LOAD-BEARING**;
- T1 separation for \(C_n^{(2)}\): **OPEN / LOAD-BEARING**;
- strictness A6: **OPEN**;
- non-reencoding A7: **OPEN**.

### 6. Stop/next action

No broad carrier search.

The next authorized computation is a targeted class-2 stress calculation for \(G_{s,a}\), at the candidate threshold scale, extracting only \((A_n,B_n,\beta_n,\text{power map},D\text{-action})\).

If these data are constant for s>a up to the threshold, classify \(C_n^{(2)}\) **FAIL / CLOSED** for T1. If they separate s<m from s\ge m, independently verify gauge invariance and strictness before any promotion.



### 7. Targeted class-2 reduction: the surviving nonabelian datum

The stress relation
[
z^{p^s}=r_D
]
has a class-2 consequence that is invisible after passing to coinvariants but is not automatically invisible in the relative class-2 extension.

Let
[
A_n=K_n/gamma_2(K_n),qquad B_n=gamma_2(K_n)/gamma_3(K_n).
]
The quotient (C_n^{(2)}) carries the (D/D_n(D))-action on (A_n) and (B_n). For (xin D), write (T_x) for the induced action on (A_n), and let (c_x(ar z)) denote the class of the kernel commutator/defect determined by ([z,x]) at the relevant class-2 level.

The identity
[
[z^{r},x]
=
[z,x]^{,1+x+cdots+x^{r-1}}
]
becomes, after passing to the abelianized kernel layer, a norm-operator identity
[
[z^{p^s},x]
=
N_{p^s}(T_x),c_x(ar z),
qquad
N_{p^s}(T_x)=1+T_x+cdots+T_x^{p^s-1}.
]
On the other hand (z^{p^s}=r_D), so the same class-2 datum is constrained by
[
N_{p^s}(T_x)c_x(ar z)
=
[r_D,x].
]

This gives the precise boundary between the closed E2 layer and the surviving candidate.

After taking (D)-coinvariants, (T_x) becomes (1), so
[
N_{p^s}(T_x)longmapsto p^s.
]
The previously established Ext/H1 calculation then sees only
[
p^smod p^a,
]
which is zero for every (sge a). Thus the untwisted E2/H1 saturation is recovered exactly.

But (C_n^{(2)}) retains the full (D)-action, so the operator (N_{p^s}(T_x)) need not collapse to (p^s). Consequently the old H1 saturation argument does **not** prove factorization of (C_n^{(2)}) through the closed layers.

This is the first concrete nonabelian obstruction that survives the earlier closures.

### 8. Exact T1 reduction

For a fixed external threshold (m>a), take the candidate window at a depth (n=n(m)) large enough that the Zassenhaus level (p^m) is represented. The T1 problem for (C_n^{(2)}) reduces to the following finite intrinsic question:

> Does the isomorphism class of the (D/D_n(D))-module data
> [
> (A_n,B_n,eta_n,ho_n,	ext{class-2 power map})
> ]
> distinguish the norm operators (N_{p^s}(ho_n(x))) for (a<s<m) from the regime (sge m), after quotienting all admissible extension automorphisms?

Equivalently, one must determine whether the deep-tail parameter survives in the **non-coinvariant norm action** while disappearing from the coinvariant quotient.

This is a substantially narrower computation than a raw Magnus/Fox search. It has exactly the required input and gauge constraints and tests the first genuinely nonabelian layer.

### 9. Independent literature/method check

Hamza's treatment confirms that lower-central and Zassenhaus filtrations naturally carry group/module actions and that finitely presented pro-(p) groups are a natural setting for such equivariant filtered objects. It supports the legitimacy of the filtration/action framework, but does not prove the present T1 separation statement. citeturn1search0turn1search17

Relation-module literature likewise treats the conjugation action on the relation module as intrinsic structure of a pro-(p) presentation, while warning that presentation-level coefficients must not be mistaken for intrinsic invariants. This supports using the action/extension class rather than a selected scalar coefficient. citeturn3search2turn3search3

### 10. Classification after the reduction

- A1 intrinsicity: **PASS / LOCAL**;
- A2 functoriality: **PASS / LOCAL**;
- A3 gauge invariance: **PASS / LOCAL** at the quotient-object level;
- A4 q-blindness: **PASS**;
- A5 orientation-blind input: **PASS**;
- class-2 non-coinvariant norm defect: **PASS / LOCAL** as the first surviving structural datum;
- factor-through H1/E2/ordinary graded layers: **NOT ESTABLISHED; prior closure does not apply**;
- T1 threshold separation: **OPEN / LOAD-BEARING**;
- A6 strictness: **OPEN**;
- A7 non-reencoding: **OPEN**.

No positive T1 theorem is claimed yet. The candidate remains alive, but the next computation is now uniquely specified: compute the norm-action orbit on (A_n) (with the induced (B_n,eta_n), and power map only as needed) for the smallest (a<s<m) and the first (sge m), then test whether the resulting compressed objects are non-isomorphic.


---

# SOURCE: research/PAPER4_QPOS_CRITICAL_REVIEW_NEXT_GATE_2026-10-02.md

<!-- blob-sha: e331bd0aa75116e1e9a45f8046127402aa81542a -->

# PAPER 4 — CRITICAL REVIEW OF q>0 BOUNDARY / NEXT-GATE DISCIPLINE — 2026-10-02

## Verdict

The submitted critical review is **substantively correct**, but one phrase must be weakened:

> “integral, gauge-invariant, nonabelian relation data” is the **only remaining candidate**

is too strong if read mathematically exhaustively. It is the **only remaining primary route currently authorized by the research program** after the untwisted E2 and ordinary mod-p graded routes were closed. Twisted/dualizing-coefficient constructions, higher cohomological operations, or other integral nonlinear objects are logically possible, but each is a *new branch* requiring a fresh Object/Input/Gauge/q-blindness pre-check.

## 1. q>0 H_2 correction

For an infinite odd-p Demushkin group with q=p^a>0 and standard relation
r_D=x_1^{p^a}[x_1,x_2]...[x_{d-1},x_d],
the trivial-coefficient one-relator cellular/Fox boundary has exponent-sum vector
(p^a,0,...,0). Hence the relevant map Z_p -> Z_p is multiplication by p^a and is injective, giving H_2(D,Z_p)=0.

For q=0 the exponent-sum vector is zero and H_2(D,Z_p)≅Z_p.

Therefore the q=0 E2 transgression
H_2(D,Z_p) -> (N^{ab})_D
has no nonzero source in the q>0 case. The classification
**untwisted E2 continuation: FAIL / CLOSED**
is justified.

This is a structural closure, not merely a failed computation.

## 2. Untwisted H_1-extension saturation

For the stress presentation
G_{s,a}=<z,x_1,...,x_d | z^{p^s}=r_D>,
abelianization gives p^s z=p^a x_1. In the five-term sequence, because H_2(D,Z_p)=0, the coinvariant module identifies with the H_1-kernel in this stress model. The resulting extension class on the torsion summand lies in
Ext^1_{Z_p}(Z/p^a,Z_p)≅Z/p^a
and is represented by p^s modulo p^a, up to sign/unit convention.

Hence for s>=a the *stress-model untwisted H_1/coinvariant layer* saturates.

Important scope correction:
this is not a theorem that every free-by-Demushkin extension with q=p^a has the same extension class. The proposed G_{s,a} family has not been independently certified as a free-by-Demushkin family for arbitrary s>a. The PASS/LOCAL label must remain local to the stated stress presentation.

## 3. Ordinary mod-p Zassenhaus graded

For the same stress presentation, with odd p and a,s>=1, the initial relation is the degree-2 Demushkin commutator form and is independent of s. The Schmidt/Gärtner mildness criterion can be used at the candidate level to control the associated graded.

Thus:
- initial-form blindness to s: **PASS / CLOSED**;
- ordinary mod-p associated-graded recovery of s: **FAIL / CLOSED** *for the candidate stress model*.

The scope must remain explicit: this is not a certified theorem about an arbitrary free-by-Demushkin family, and it does not imply blindness of the full finite quotient.

The distinction
associated graded blind  !=  finite-window blind
is mandatory and remains intact.

## 4. The strongest correction to the submitted table

The following row should read:

| Item | Classification | Exact scope |
|---|---|---|
| q>0 untwisted E2 source | **FAIL / CLOSED** | H_2(D,Z_p)=0 for standard q=p^a>0 |
| q>0 untwisted H_1-extension | **FAIL / CLOSED** | stress model; saturated for s>=a |
| ordinary mod-p Zassenhaus graded | **FAIL / CLOSED** | stress-model candidate; blind to s |
| integral gauge-invariant nonabelian relation data | **OPEN / LOAD-BEARING** | primary authorized successor |
| twisted/dualizing-coefficient replacement | **OPEN** | separate branch; not E2 continuation |
| full finite-window factorization | **OPEN / LOAD-BEARING** | no theorem yet |
| universal impossibility for q>0 deep tails | **OPEN** | no claim permitted |

## 5. The next gate is definition, not computation

Before computing any Magnus coefficient, define a candidate I_m(G) in one sentence.

Minimum acceptable form:

> I_m(G) is a presentation-independent quotient/truncation of an integral p-adic relation object, with all presentation-basis, relator-generator, lift/section, conjugacy, and unit-scaling gauges explicitly quotiented.

Then specify:

### Object
Exactly which module/ring/filtered relation object is used?

### Input
Does I_m use only G as an abstract/profinite group (or only the declared finite window), or does it secretly use a chosen presentation, D, q, orientation, or lift?

### Functoriality
Which filtered-group isomorphisms induce maps of I_m?

### Gauge
At minimum test:
- free-basis/Nielsen changes;
- relator multiplication by a unit;
- conjugating the relator;
- lift/section changes;
- automorphisms of the quotient D;
- automorphisms of the kernel presentation;
- any BBG-type boundary automorphism relevant to the construction.

### Orientation bridge
There must be a natural map from I_m to the actual target information. Merely recovering p^s is not an orientation theorem.

### q-blindness
The definition may not insert a or q=p^a.

### Separation
It must distinguish the relevant q=0 and q>0 stress regimes without using q as an input label.

### Non-reencoding
A presentation coefficient is not acceptable merely because it numerically equals the desired answer. The same intrinsic finite object must force the value.

## 6. Important methodological boundary

The phrase “integral Magnus/relation data is the only remaining candidate” must therefore be replaced by:

> **The only remaining primary route currently authorized is an intrinsic, gauge-invariant, nonabelian integral relation object strictly richer than the ordinary mod-p associated graded.**

This preserves the research direction without pretending that all other mathematics has been exhausted.

## 7. Novelty boundary

The object itself is standard technology. Any eventual Paper-4 contribution would have to be one of:
1. a new intrinsic quotient/truncation;
2. a proof that it factors through a finite Zassenhaus window;
3. a sharp obstruction showing that no such factorization exists in a declared admissible category;
4. a reconstruction theorem to the target orientation/cohomological datum.

A successful calculation of a Magnus coefficient alone is not a Paper-4 theorem.

## 8. Current Gate

**Gate P4-Q+ / INTEGRAL-NONABELIAN-DEFINITION**

Status: **OPEN / LOAD-BEARING**.

No carrier search, no arbitrary Magnus computation, and no RAAG return are authorized before the exact object and gauge quotient pass pre-check.



---

# SOURCE: research/PAPER4_QPOS_HIGHER_LAYER_AUDIT_2026-10-02.md

<!-- blob-sha: e41253fa57970fd4950ab2d0b9e1e4def07febac -->

# Paper 4 — q>0 higher-layer audit — 2026-10-02

## Result
The pure abelianization detector saturates at p^{min(a,s)} for a q_D=p^a Demushkin quotient, so it cannot recover extension depth s once s>a.

A literature audit did not locate a theorem-level q_D>0 variable-depth free-by-Demushkin family certifying the proposed model z^{p^s}=r_D. Therefore no positive q>0 higher-layer theorem is claimed.

Kochloukova–Zalesskii certify the q_D=0 family z^{p^s}=[x,y]. Quadrelli's general one-relator/free-by-Demushkin results require additional hypotheses and do not certify the proposed q_D>0 family.

Ben-Bassat–Gropper (2026), Proposition 4.7, gives a related PD^2-pair gauge phenomenon: for s0=s1 x^{p^r}[x,y], automorphisms can fix one boundary and send s0 to a conjugate of s0^alpha for alpha congruent to 1 modulo p^r. This is a gauge stress control: raw p-adic relator coefficients are not automatically intrinsic.

Classification:
- q>0 abelianization saturation: PASS / LOCAL;
- pure abelianization recovery beyond a: FAIL / CLOSED;
- q>0 higher filtered recovery: OPEN / LOAD-BEARING;
- finite-window factorization of a gauge-invariant truncation: OPEN;
- orientation bridge: OPEN;
- new carrier hunt: STOP / NOT AUTHORIZED.

Next authorized test: define the smallest gauge-invariant truncation of the full transgression/relation object and test finite-window factorization. If no scalar survives the gauge quotient without reintroducing q or the orientation, close this realization route.


---

# SOURCE: research/PAPER4_QPOS_GATE_T1C_NONABELIAN_KERNEL_BOUNDARY_AUDIT_2026-10-03.md

<!-- blob-sha: df33a69ea986e13ada3a9f388fb5fa305e44316d -->

# PAPER 4 — GATE T1-C: FIRST NONABELIAN KERNEL BOUNDARY — 2026-10-03

## Purpose

This audit pushes Gate T beyond the closed scalar/coinvariant and critical-norm shortcuts. It does **not** claim that the exact relative threshold has been proved.

For
\[
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,
\qquad
r_D=x_1^{p^a}[x_1,x_2]\cdots[x_{d-1},x_d],
\qquad s>a,
\]
put
\[
W_s=G_{s,a}/D_{p^s+1}(G_{s,a}),
\quad
Q_s=D/D_{p^s+1}(D),
\quad
K_s=\ker(W_s\to Q_s).
\]

## 1. The scalar cancellation is genuinely a lift-change phenomenon

The central class-2 detector used previously is insufficient as a nonsplitting witness. In the rank-two stress relation
\[
r_D=x^q[x,y],\qquad q=p^a,
\]
the scalar defect \(z^{p^s}\) can be cancelled at the abelianized/central level by changing the \(x\)-lift by a \(p^{s-a}\)-power of the kernel generator.

This is not merely an abstract cohomological warning: it is visible in the relation-module differential. The Fox row contains a coefficient whose augmentation is \(q=p^a\), so multiplication by \(p^{s-a}\) can remove the scalar \(p^s\)-defect. This is exactly the cancellation already recorded in T1-A.

Therefore the scalar class alone cannot certify nonsplitting.

## 2. Where the cancellation stops being scalar

The same lift change is not purely scalar before coinvariants. Conjugating the kernel generator by the second Demuškin generator contributes a non-augmentation term (equivalently, a \((y-1)\)-direction after choosing the standard rank-two convention and passing to the relation module).

Schematically, if \(k=z^{-p^{s-a}}\) is the scalar correction, then the first-order relator change has the form
\[
\delta r
=
\bigl(\text{augmentation part}\bigr)\,k
+
\bigl(\text{non-coinvariant }(y-1)\text{-part}\bigr)\,k
+\cdots.
\]
The augmentation part cancels \(z^{p^s}\); the non-coinvariant part is the first possible residual obstruction.

This is **not yet a theorem that the residual survives**. It identifies the exact layer that must be tested.

## 3. First nonabelian quotient of the kernel

The correct hierarchy is now:

\[
K_s
\longrightarrow
A_s=K_s/[K_s,K_s]
\longrightarrow
B_s=\gamma_2(K_s)/\gamma_3(K_s)
\longrightarrow\cdots
\]

The abelianized module \(A_s\) is the first diagnostic. Its coinvariant scalar quotient is already closed as an obstruction. The remaining question is whether the non-coinvariant \(Q_s\)-module structure in \(A_s\) already detects a nonzero extension defect.

If it does not, the next authorized layer is \(B_s\). This is the precise meaning of “first nonabelian quotient”: not an arbitrary class-2 construction, but the first lower-central quotient of the **actual finite kernel**.

## 4. A useful stress calculation, but not a theorem

At the rank-two level, a lift correction of size \(p^{s-a}\) has a commutator contribution whose formal filtration scale is governed by the power of a degree-two kernel commutator. Since
\[
2p^{s-a}<p^s+1
\]
for odd \(p\) and \(s>a\), such a contribution is not automatically killed by the critical quotient.

This is important: the earlier scalar cancellation cannot simply be declared to remove the entire defect. It may move the obstruction from the scalar layer into a much lower nonabelian/lower-filtration layer.

But the inequality alone proves only **possible visibility**, not nonvanishing. A quotient calculation is required to show that the corresponding kernel commutator is actually nonzero.

## 5. What is now closed

The following shortcuts are permanently closed for Gate T:

- scalar \(z^{p^s}\) as a nonsplitting witness;
- coinvariant/augmentation-only extension class;
- critical norm equation \(N_{p^s}(T_x)c_x(\bar z)=0\) as a nonzero witness;
- “one-dimensional \(H^2(D,\mathbf F_p)\) therefore finite extension is nonsplit” without a lift-change quotient;
- any replacement of the actual kernel by an assumed abelian kernel.

## 6. What remains genuinely open

The exact question is:

> Does the actual finite extension
> \[
> 1\to K_s\to W_s\to Q_s\to1
> \]
> admit a section?

Equivalently, after all generator/lift changes, does the defining relator defect vanish in the first nontrivial quotient of the actual kernel?

The minimum computation is therefore:

1. construct \(A_s=K_s/[K_s,K_s]\) as a finite \(\mathbf F_p[Q_s]\)-module, not merely its coinvariants;
2. write the actual relation-module differential induced by \(r_D\);
3. quotient its defect space by **all** lift-change coboundaries;
4. test whether the resulting class is nonzero;
5. if zero, compute \(B_s=\gamma_2(K_s)/\gamma_3(K_s)\) and repeat.

A nonzero class at step 3 is sufficient for nonsplitting. Vanishing is not sufficient for splitting.

## 7. Literature control

Relation modules of pro-\(p\) presentations are naturally modules for the presented group, and Fox derivatives provide the corresponding differential. This is the correct formalism for the remaining calculation. citeturn0search1turn0search21

The standard odd-prime Demuškin presentation
\[
x_1^q[x_1,x_2]\cdots[x_{d-1},x_d]=1
\]
is independently confirmed in the literature. citeturn1search24

No literature source found here proves the present finite-window extension class. Therefore no novelty or threshold theorem is claimed from the literature alone.

## 8. Classification

- critical-layer visibility: **PASS / LOCAL**;
- scalar/coinvariant obstruction: **FAIL / CLOSED**;
- critical norm shortcut: **FAIL / CLOSED**;
- non-coinvariant kernel module as the next diagnostic: **OPEN / LOAD-BEARING**;
- first nonabelian kernel quotient as fallback: **OPEN / LOAD-BEARING**;
- critical nonsplitting: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **OPEN / LOAD-BEARING**;
- unmarked filtered-group theorem: **OPEN**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

## 9. Next authorized action

The next computation is singular:

\[
\boxed{
\text{compute the actual }\mathbf F_p[Q_s]\text{-relation module }A_s
\text{ at }n=p^s+1,
\text{ including its non-coinvariant action.}
}
\]

Only after that calculation may the branch be promoted to a genuine cohomological obstruction or closed as a splitting phenomenon.


## 10. Gate T1-C correction recorded 2026-10-03

The T1-C audit is tightened as follows: “lift change kills the scalar defect” means only **coinvariant/augmentation-level cancellation**. Full finite-extension cancellation is unproved because (z) is not assumed central and the exact change is controlled by the action/norm operator. (A_s=K_s^{ab}) is the first diagnostic layer but has not yet been computed; the next step is its actual finite (mathbf F_p[Q_s])-module and extension class after all lift-change coboundaries. (B_s=\gamma_2(K_s)/\gamma_3(K_s)) is a conditional fallback, not an asserted universal first obstruction. The Gate-T frontier remains OPEN / LOAD-BEARING and blind carrier search remains STOP.

## 2026-10-03 — GATE T1-C CRITICAL RE-AUDIT: A_s / PUSHOUT / RAW-RESIDUAL BOUNDARY

A further critical review tightens the Gate T1-C object and obstruction logic without changing the frontier.

1. **A_s versus its mod-p reduction must be separated.** The literal kernel abelianization is \(A_s=K_s/[K_s,K_s]\), which is not automatically an \(\mathbf F_p[Q_s]\)-module. For an \(\mathbf F_p\)-module calculation one must explicitly pass to \(\overline A_s=K_s/[K_s,K_s]K_s^p=A_s/pA_s\). No identification of these two objects is authorized.

2. **The abelianized extension is a diagnostic pushout, not the original extension.** From \(1\to K_s\to W_s\to Q_s\to1\) one may push out along \(K_s\to A_s\) to obtain an abelian-kernel extension. If that pushed-out class is nonzero, the original extension is necessarily nonsplit. If it vanishes, the original extension may still be nonsplit. Thus the \(A_s\)-level test is a sufficient obstruction, not an equivalence criterion for splitting.

3. **The raw residual is not the extension class.** The visible term \([z^{p^{s-a}},x_2]\) or its associated-graded analogue only proves a candidate residual is structurally present. The actual obstruction is its class modulo **all** admissible section/lift-change coboundaries. A concrete metabelian quotient showing this commutator is not universally trivial is an independent nonvanishing control, but does not by itself prove nonsplitting.

4. **Associated-graded survival is not yet proved.** The fact that the initial form of the stress relator is controlled by the Demushkin part does not by itself prove that \(Z^{[p^{s-a}]}\) or \([Z^{[p^{s-a}]},X_2]\) survives in the required restricted-Lie quotient. This needs an explicit quotient/independence calculation.

5. **Correct load-bearing question.** First define the exact finite module object (literal \(A_s\) or explicitly \(\overline A_s\)), its genuine \(Q_s\)-action, the induced pushout extension, and the full lift-change subspace. Then test the residual class. If the abelianized obstruction vanishes, descend to \(B_s=\gamma_2(K_s)/\gamma_3(K_s)\); vanishing there still does not imply splitting.

### Updated classification
- critical-layer visibility: **PASS / LOCAL**;
- scalar/coinvariant obstruction: **FAIL / CLOSED**;
- critical norm shortcut: **FAIL / CLOSED**;
- raw action residual: **PASS / LOCAL**;
- raw residual modulo all lift coboundaries: **OPEN / LOAD-BEARING**;
- actual abelianized-kernel obstruction: **OPEN / DIAGNOSTIC**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{rel}(s)=p^s+1\): **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

No Gate-T reversal, exact-threshold claim, or new carrier search is authorized.


## 2026-10-03 — MINIMAL p=3 CHECK: RAW RESIDUAL IS NOT YET AN OBSTRUCTION

In the minimal case p=3, s=2, a=1, d=2, the rank-two Fox derivative satisfies partial_x r = N_3(x)+x^3-y. Writing X=x-1 and Y=y-1 over F_3 gives leading term -Y. A degree-3 kernel correction therefore generates a degree-4 Y-direction, the same filtered direction represented by the candidate [z^3,y]. Hence the raw non-coinvariant residual is structurally visible but is also generated by the lift-change differential. It cannot be promoted to an A_s obstruction merely from its nonzero raw representative.

The complete quotient by all lift changes remains the load-bearing test. Current classification: raw action residual PASS/LOCAL; candidate [z^3,y] alone FAIL/CLOSED as an obstruction; complete A_s diagnostic OPEN; full extension splitting OPEN/LOAD-BEARING; exact relative threshold OPEN/LOAD-BEARING.


## 11. 2026-10-03 — FOX IMAGE FIRST-LAYER ANALYSIS

The authorized continuation was carried out at the structural, rather than candidate-search, level. Put
\[
q=p^a,\qquad m=p^{s-a},\qquad qm=p^s.
\]
For the critical rank-two factor
\[
r_D=x_1^q[x_1,x_2],
\]
let k be a kernel lift correction whose first nonzero filtered degree is m. The Fox/lift-change differential has two relevant first-order pieces.

First, the derivative of x_1^q contributes the q-fold norm. Its augmentation is q, so choosing the scalar coefficient m removes the degree-p^s augmentation defect because qm=p^s. This is precisely the already-closed coinvariant cancellation.

Second, the derivative of the commutator [x_1,x_2] contributes the augmentation-ideal direction generated by x_2-1 acting on k. In the associated filtered degree this is the class represented by
\[
[k,x_2],
\]
and for k with leading z^m this is the previously proposed
\[
[z^m,x_2].
\]
Thus the candidate is not outside the first-order gauge image: it is produced by the same Fox differential that performs the scalar lift correction.

The minimal case p=3,s=2,a=1 gives the concrete check
\[
\partial_{x_1}r_D=N_3(x_1)+x_1^3-x_2,
\]
whose leading augmentation-ideal term is -Y over F_3. The general q=p^a calculation has the same structural source: the power part supplies augmentation q, while the commutator part supplies the x_2-1 direction.

The filtration inequalities
\[
m+1<p^s+1,
\qquad 2m<p^s+1
\]
for odd p and s>a show that this direction is visible before the critical cutoff. They do not show that it survives quotienting by lift changes.

### Result

The specific first-layer residual is now classified as
\[
\boxed{\text{FAIL / CLOSED as an independent obstruction}.}
\]
More precisely, the quotient of this one-dimensional candidate direction by the corresponding first-order Fox/lift-change image is zero.

This is **not** a computation of the complete \(A_s\). Higher filtered terms can in principle produce further cokernel classes. Therefore:

- first-layer raw residual: **PASS / LOCAL**;
- first-layer candidate obstruction modulo Fox image: **FAIL / CLOSED**;
- complete \(A_s\)-level extension class: **OPEN / DIAGNOSTIC**;
- full finite extension splitting: **OPEN / LOAD-BEARING**;
- exact relative threshold: **OPEN / LOAD-BEARING**.

### Methodological consequence

The research is not returning to detailed carrier hunting. The correct next object is the full graded cokernel
\[
\mathcal C_s
=
\frac{\text{all filtered first-order defect directions at the critical window}}
{\text{image of all admissible Fox/lift-change differentials}}.
\]
A nonzero element of \(\mathcal C_s\) would be a genuine gauge-invariant A_s-level obstruction. If \(\mathcal C_s=0\) throughout the relevant filtered range, the entire A_s route is closed and only then may the conditional \(B_s\) route be opened.


## 12. 2026-10-03 — FULL FIRST-ORDER FOX IMAGE / MOD-p Abar CLOSURE

The first-layer analysis can be strengthened from one candidate direction to the whole augmentation-ideal tangent space.

Let (I=ker(mathbf F_p[Q_s]	omathbf F_p)). For the critical rank-two factor (r=x_1^q[x_1,x_2]), (q=p^a), the Fox derivatives satisfy modulo (I^2):
[
partial_{x_1}r\equiv -(x_2-1),qquad
partial_{x_2}requiv x_1-1.
]
Indeed the (q)-power norm contributes no linear term in characteristic (p), while the commutator derivatives supply the two degree-one directions. Thus the two Fox entries generate (I/I^2).

Because (Q_s) is a finite (p)-group, (I) is the Jacobson radical of (mathbf F_p[Q_s]). Nakayama implies that the ideal generated by the two Fox entries is all of (I). Therefore every first-order mod-(p) non-coinvariant lift-change direction in the augmentation ideal is gauge-generated. The previous residual ([z^{p^{s-a}},x_2]) is consequently not merely one removable direction: it belongs to a whole Fox-generated tangent space.

This closes the first-order mod-(p) abelianized cokernel as an obstruction. It does not compute the literal integral (A_s=K_s/[K_s,K_s]), does not establish full splitting, and does not prove the exact threshold. Higher filtered terms and genuinely nonlinear/lower-central defects remain outside this first-order calculation.

### Classification
- first-layer candidate obstruction: **FAIL / CLOSED**;
- first-order mod-(p) abelianized Fox cokernel: **FAIL / CLOSED**;
- literal (A_s)-level extension class: **OPEN / DIAGNOSTIC**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact relative threshold: **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

### Next authorized boundary

Do not search for another residual in the same mod-(p) abelianized layer. If the research target is the mod-(p) finite-window obstruction, the Abar/Fox route is now closed. If integral (p)-power information is essential, it must be formulated separately as an integral (A_s) problem. Otherwise the conditional next layer is the actual (B_s=gamma_2(K_s)/gamma_3(K_s)), with its own object/input/gauge pre-check.


## 2026-10-03 — T1-C CRITICAL REVIEW: RECURSIVE LIFT-ABSORPTION IS NOT ESTABLISHED

A critical review of the proposed recursive lift-absorption argument found a load-bearing gap. The valid filtration estimate is that, for m=p^{s-a} and any later correction k_j in filtration degree m+j (j>=1), one has k_j^q in D_{q(m+j)}=D_{p^s+qj}, hence the q-power of later corrections lies beyond the critical cutoff. This only shows that later corrections do not recreate the original scalar q-power defect below the cutoff.

It does **not** prove the required recursive-image lemma that every higher residual lies in
\[
\operatorname{Im}(\operatorname{ad}_{x_2}:\operatorname{gr}_{m+j}K_s\to\operatorname{gr}_{m+j+1}K_s).
\]
The first residual is in this image, but higher BCH/conjugation/commutator terms can contain brackets not visibly of the form [u,x_2]. In a free Lie algebra, ad_{x_2} is not generally surjective (already degree 2 has [x_1,x_3] outside the image, and higher-degree dimension gaps persist). Therefore first-order Fox surjectivity cannot be promoted to all higher filtered nonlinear terms without an explicit induction or a complete filtered Fox/Magnus calculation.

A second gap is that the correction equation is nonlinear: choosing k_j to cancel the degree-(m+j+1) residual can itself modify previously controlled terms through conjugation and commutator cross-terms. Degree counting alone does not establish triangular solvability.

Accordingly the previous suggestion that the extension may recursively split is **CONDITIONAL only**, not a result. The decisive next object is the first degree at which the exact residual leaves the \(\operatorname{ad}_{x_2}\)-image modulo all admissible lift changes. If such a degree exists, it gives the first genuine integral gauge obstruction. If no such degree exists, a separate convergence/termination argument is still required to conclude splitting at the finite cutoff.

Updated classification:
- scalar/coinvariant obstruction: **FAIL / CLOSED**;
- first-order mod-p Fox cokernel: **FAIL / CLOSED**;
- recursive q-power filtration estimate: **PASS / LOCAL**;
- recursive-image lemma: **OPEN / LOAD-BEARING**;
- recursive lift absorption: **CONDITIONAL**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact n_sep^rel(s)=p^s+1: **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

No claim that the stress-family extension splits is authorized. No B_s opening is justified merely by the failed recursive argument; the integral A_s obstruction must first be resolved or the recursive-image lemma proved.

## 2026-10-03 — T1-C DEGREE-5 TEST REFORMULATED: \(\operatorname{ad}_{x_2}\)-COKERNEL IS NOT THE GAUGE QUOTIENT

The proposed minimal split “compute \(R_5\bmod\operatorname{Im}(\operatorname{ad}_{x_2})\)” was critically audited before execution. It is **not** the correct gauge-invariant degree-5 obstruction.

The reason is structural: \(R_5\) is a residual in a nonlinear lifting problem, while admissible lift changes are governed by the full filtered Fox/relation-module differential. The degree-5 gauge image is therefore not, in general, the single subspace
\[
\operatorname{Im}\bigl(\operatorname{ad}_{x_2}:\operatorname{gr}_4K_s\to\operatorname{gr}_5K_s\bigr).
\]
A class may lie outside \(\operatorname{Im}(\operatorname{ad}_{x_2})\) and nevertheless be removed by a different admissible generator/lift correction, or by a coupled Fox differential involving the power and commutator parts. Conversely, membership in the \(\operatorname{ad}_{x_2}\)-image does not by itself identify the full coboundary quotient.

This matters especially because the preceding first-order computation already showed that the candidate \([z^{p^{s-a}},x_2]\) is generated by the Fox/lift-change differential. The correct higher-degree object is therefore the filtered cokernel
\[
\mathcal C_{s,d}
=
\frac{\text{all degree-}d\text{ defect directions}}
{\operatorname{Im}(\text{full admissible Fox/lift-change differential at degree }d-1)},
\]
with the actual finite-kernel/module relations imposed first. Only a nonzero class in this quotient is a genuine \(A_s\)-level obstruction.

Consequently the suggested degree-5 binary test
\[
R_5\in\operatorname{Im}(\operatorname{ad}_{x_2})
\quad\text{vs.}\quad
R_5\notin\operatorname{Im}(\operatorname{ad}_{x_2})
\]
is **FAIL / CLOSED as a load-bearing criterion**. It is at most a diagnostic inside a chosen normal form, not an intrinsic obstruction test.

This is not a retreat from the calculation. It removes one more false shortcut. The next and only authorized computation is the actual degree-5 component of the full Fox/lift-change cokernel in the minimal model \((p,s,a)=(3,2,1)\), after the finite-kernel quotient is fixed. If that component is zero, degree 5 yields no \(A_s\)-obstruction; if nonzero, it is a genuine gauge-invariant candidate. No \(B_s\) branch opens before this quotient is resolved.

Classification:
- degree-5 raw residual: **OPEN / DIAGNOSTIC**;
- \(R_5\) modulo \(\operatorname{ad}_{x_2}\) as obstruction: **FAIL / CLOSED**;
- degree-5 full Fox/lift-change cokernel: **OPEN / LOAD-BEARING**;
- complete mod-\(p\) first-order Fox cokernel: **FAIL / CLOSED**;
- integral \(A_s\)-level extension obstruction: **OPEN / LOAD-BEARING**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{rel}=p^s+1\): **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.



## 2026-10-03 — DEGREE-5 FULL-FOX STRUCTURAL VERIFICATION

The degree-5 computation was reformulated intrinsically before execution. The rejected test was the single map ad_{x_2}; the correct degree-5 gauge space is generated by the full degree-one Q_s-action on degree-4 kernel defects.

Let L be the ordinary free Lie algebra on the degree-one generators and I=(z) the Lie ideal generated by the kernel direction. Then I is generated as a graded Lie ideal by z, hence for degree 5:
\\[
I_5=[I_4,L_1].
\\]
Therefore the full action map
\\[
I_4\\otimes L_1\\longrightarrow I_5,qquad u\\otimes v\\mapsto [u,v]
\\]
is surjective. The two degree-one Fox directions supplied by the critical relator x_1^3[x_1,x_2] are exactly the x_1- and x_2-action components at this filtered level. Consequently the degree-5 ordinary-Lie defect quotient by all admissible first-order lift changes is zero.

This is the missing structural check requested after the earlier \\operatorname{ad}_{x_2}-only no-go. It establishes that the visible degree-5 commutator route is a gauge artifact, not a genuine A_s obstruction.

The result must not be overextended: the restricted Lie algebra at p=3 has a new p-power operation. A degree-2 kernel class can contribute a degree-6 restricted-power class, so degree 6 is the first structurally different diagnostic. The present calculation does not show that such a class is actually produced by the stress relator; it only identifies the next place where ordinary-Lie gauge generation no longer exhausts the formal operations.

Classification:
- degree-5 full Fox ordinary-Lie cokernel: **FAIL / CLOSED**;
- degree-5 commutator path: **FAIL / CLOSED**;
- integral/restricted A_s obstruction: **OPEN / LOAD-BEARING**;
- full extension splitting/non-splitting: **OPEN / LOAD-BEARING**.


## 2026-10-03 — CRITICAL CORRECTION: DEGREE-5 GAUGE CLOSURE OVERSTATED

The previous degree-5 structural note overreached. The free-Lie identity I_5=[I_4,L_1] is correct for the Lie ideal I=(z), but it does not by itself identify I_5 with the image of the actual finite-kernel Fox/lift-change differential. The assertion that the two linear Fox directions x_1-1 and x_2-1 realize the full degree-one action on the actual finite kernel was not proved after imposing finite-kernel/module relations. Therefore the claim degree-5 full Fox cokernel=0 is NOT established.

What is proved: the ad_{x_2}-only test is not the full gauge quotient, and free-Lie degree-5 commutator terms are algebraically generated by degree-one bracketing of degree-4 terms. What remains OPEN / LOAD-BEARING is whether those generators are all admissible lift changes in the actual finite extension.

The degree-6 restricted-power observation is only a candidate boundary; it does not authorize skipping the exact degree-5 finite-kernel quotient.

Classification: ad_{x_2}-only obstruction FAIL / CLOSED; free-Lie degree-5 generation PASS / LOCAL; actual degree-5 finite Fox/lift-change cokernel OPEN / LOAD-BEARING; degree-5 commutator path OPEN / DIAGNOSTIC; integral/restricted A_s obstruction OPEN / LOAD-BEARING; full finite extension splitting OPEN / LOAD-BEARING; exact n_sep^rel=p^s+1 OPEN / LOAD-BEARING.

Next authorized calculation: exact degree-5 finite-kernel Fox quotient in the minimal model (p,s,a)=(3,2,1).

## 2026-10-03 — T1-C DEGREE-5 ACTUAL FINITE-KERNEL Abar FOX QUOTIENT: ZERO

The exact degree-5 test was completed at the correct finite-kernel/module level for the minimal stress model ((p,s,a)=(3,2,1)). The key correction is to work with the abelianized kernel (overline A_s=K_s/[K_s,K_s]K_s^3), where all brackets containing two kernel directions vanish. Thus the misleading free-Lie question (I_5=[I_4,L_1]) is replaced by the actual (Q_s)-module action on the single normal generator (ar z).

Because (K_s) is the normal closure of (z) in the finite extension, (overline A_s) is generated as an (mathbf F_3[Q_s])-module by (ar z). With the induced augmentation filtration (J=ker(mathbf F_3[Q_s]	omathbf F_3)), every degree-5 class in the kernel module is therefore represented by a degree-1 (Q_s)-action on a degree-4 class:
[
operatorname{gr}_5(overline A_s)=
(J,operatorname{gr}_4(overline A_s)).
]
The defining extension relation (z^9=r_D) introduces no new kernel generator in degree 5; it can only impose further module relations. Hence after passing to the finite-kernel quotient, the degree-5 defect space is still generated by the degree-1 (Q_s)-action.

Those degree-1 actions are precisely the admissible section/lift-change directions represented by the Fox differential. Consequently
[
oxed{mathcal C_{s,5}^{mathrm{Fox}}=0}
]
for the mod-(3) abelianized-kernel degree-5 quotient. In particular, the previously isolated degree-5 commutator path has no gauge-invariant class even after the finite-kernel/module relations are imposed.

This is stronger than the earlier free-Lie observation: it does not assume that all of (I_5) is generated by (x_1,x_2)-bracketing before abelianizing the kernel; it uses the actual fact that the kernel abelianization is a cyclic (Q_s)-module generated by the normal kernel direction.

Logical boundary: this is a mod-(p), degree-5 statement. It does not identify the full integral (A_s=K_s/[K_s,K_s]), does not prove finite-extension splitting, and does not eliminate integral (p)-power classes. At (p=3), the first restricted-power degree that is structurally distinct from ordinary degree-5 action is degree 6. That is now the first legitimate next diagnostic, but it is conditional on an explicit restricted/integral pre-check.

Classification:
- degree-5 (operatorname{ad}_{x_2})-only test: **FAIL / CLOSED**;
- degree-5 ordinary-Lie generation: **PASS / LOCAL**;
- degree-5 actual finite-kernel mod-(3) Fox quotient: **FAIL / CLOSED** as an obstruction;
- degree-5 commutator path: **FAIL / CLOSED**;
- integral/restricted (A_s) obstruction: **OPEN / LOAD-BEARING**;
- full finite-extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact (n_{mathrm{sep}}^{rel}(s)=p^s+1): **OPEN / LOAD-BEARING**.

Next authorized boundary: perform the pre-check for the degree-6 restricted/integral layer. Do not reopen degree-5 or the (operatorname{ad}_{x_2})-only branch, and do not jump to (B_s) without first deciding whether the degree-6 restricted-power object is genuinely an integral (A_s)-level obstruction.


## 2026-10-03 — CRITICAL RE-AUDIT: DEGREE-5 CLOSURE WAS OVERSTATED AGAIN

The preceding note claiming (mathcal C^{Fox}_{s,5}=0) at the actual finite-kernel mod-(3) level is not yet justified. The valid part is that (overline A_s=K_s/[K_s,K_s]K_s^3) is generated as an (mathbf F_3[Q_s])-module by the normal kernel class (ar z), and hence its (J)-adic graded pieces are generated by (Q_s)-action. However, this does NOT by itself identify the degree-5 defect space with the image of the section/lift-change differential.

The load-bearing missing step is exactly the one previously identified: one must construct the actual finite extension's section-change map
[
delta:{	ext{admissible degree-4 lift changes}}longrightarrow
operatorname{gr}_5(overline A_s)
]
and prove that its image equals the relevant (Joperatorname{gr}_4(overline A_s)) (or otherwise compute the exact image). “Generated as a module by (ar z)” describes the module structure; it does not prove that every corresponding degree-1 action is an admissible coboundary for the extension problem.

Likewise, the statement that the defining relator introduces no new degree-5 kernel generator is insufficient to identify the extension-defect quotient: relations can change both the domain of admissible lift changes and the target quotient.

Therefore the previous degree-5 conclusion
[
mathcal C^{Fox}_{s,5}=0
]
must be downgraded. What remains proved is only:
- actual finite-kernel (overline A_s) is cyclic as a (Q_s)-module: **PASS / LOCAL**;
- ordinary degree-5 module generation by degree-one action: **PASS / LOCAL** as a module statement, conditional on the chosen filtration;
- equality with the full admissible Fox/lift-change image: **OPEN / LOAD-BEARING**;
- degree-5 gauge-invariant cokernel: **OPEN / LOAD-BEARING**;
- integral/restricted (A_s) obstruction: **OPEN / LOAD-BEARING**;
- full finite-extension splitting/non-splitting: **OPEN / LOAD-BEARING**.

This correction supersedes the immediately preceding “degree-5 actual finite-kernel Fox quotient = zero” claim. The research does NOT authorize jumping to degree 6 yet. The correct next calculation remains the exact degree-5 finite-kernel section-change/Fox differential and its cokernel in the minimal model ((p,s,a)=(3,2,1)).


## 2026-10-03 — CORRECTION / T1-C DEGREE-5 RESULT RESTORED TO OPEN

A previous record incorrectly promoted the degree-5 finite-kernel mod-p Fox quotient to zero. That statement is superseded. The exact finite-kernel module structure alone does not prove that all degree-1 module actions are realized by admissible section changes.

Therefore the authoritative state is:
- \(\bar A_s=K_s/[K_s,K_s]K_s^3\) cyclic as an \(\mathbf F_3[Q_s]\)-module: **PASS / LOCAL**;
- degree-5 module generation by degree-one action: **PASS / LOCAL**;
- equality with the actual admissible section-change/Fox image: **OPEN / LOAD-BEARING**;
- degree-5 gauge-invariant cokernel: **OPEN / LOAD-BEARING**;
- integral/restricted \(A_s\) obstruction: **OPEN / LOAD-BEARING**.

The degree-6 restricted-power layer is **NOT YET AUTHORIZED**. The next calculation remains the exact degree-5 finite-kernel section-change/Fox differential in the minimal model \((p,s,a)=(3,2,1)\).


## 2026-10-03 — T1-C DEGREE-5 EXACT SECTION-CHANGE / FOX COKERNEL: ZERO (MINIMAL MOD-p LAYER)

The previously missing admissibility step was isolated explicitly. Work in the minimal stress model \((p,s,a)=(3,2,1)\), with \(r=x^3[x,y]\), finite window \(n=10\), finite kernel \(K\), and \(\bar A=K/[K,K]K^3\). Let \(J\subset\mathbf F_3[Q]\) be the augmentation ideal.

A section change replaces the lifted generators by \(x_i\mapsto k_i x_i\), with arbitrary admissible \(k_i\in K\). After abelianizing the kernel, the change in the relator defect is the Fox section-change map
\[
\delta(k_x,k_y)=\overline{\partial_x r}\,k_x+\overline{\partial_y r}\,k_y.
\]
For the fixed commutator convention,
\[
\partial_x r=N_3(x)+x^3-y,\qquad \partial_y r=x^4-1.
\]
Modulo \(J^2\), in augmentation variables \(X=x-1,Y=y-1\),
\[
\partial_x r\equiv -Y,\qquad \partial_y r\equiv X.
\]
Thus the degree-1 Fox symbols span \(J/J^2\).

The kernel abelianization is cyclic over \(\mathbf F_3[Q]\), generated by \(\bar z\). With its induced augmentation filtration, \(\operatorname{gr}_{d+1}\bar A=J\operatorname{gr}_d\bar A\). Therefore the degree-5 target is exactly generated by the degree-1 \(J/J^2\) action on degree-4 classes. Since \(\delta\) has both independent degree-1 Fox directions \(-Y\) and \(X\), every degree-5 class is an actual section-change image.

Hence the exact minimal finite-kernel mod-3 quotient is
\[
\boxed{\mathcal C^{\mathrm{Fox}}_{s,5}=0}.
\]
This closes the degree-5 commutator path as a genuine gauge-invariant obstruction at the mod-p abelianized-kernel layer. The result is stronger than the earlier free-Lie argument because the admissible section-change map is now explicitly identified.

Logical boundary: this still does not compute the integral \(A_s=K/[K,K]\), does not prove the full nonabelian finite extension splits, and does not settle \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\). Degree 6 is now the first structurally distinct restricted-power diagnostic, but only after an explicit pre-check of whether it can survive in the integral \(A_s\)-level quotient.

Classification:
- degree-5 actual finite-kernel mod-3 Fox cokernel: **FAIL / CLOSED**;
- degree-5 commutator path: **FAIL / CLOSED**;
- integral/restricted \(A_s\)-obstruction: **OPEN / LOAD-BEARING**;
- full finite-extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

Next authorized action: perform the degree-6 restricted/integral pre-check; do not reopen degree 5.


## 2026-10-03 — DEGREE-6 RESTRICTED/INTEGRAL PRE-CHECK

The first restricted-power boundary was audited before computation. A restricted p-operation belongs to the mod-p associated graded, whereas the unresolved extension object is the integral kernel abelianization A_s modulo the actual section-change image. For p=3, an integral class u satisfies u^3=3u in the abelian kernel, so a nonzero restricted symbol is not automatically a new integral obstruction. It must lift to an integral defect surviving the section-change quotient and carrying a genuine 3-divisibility/torsion defect.

Classification: standalone degree-6 restricted obstruction **FAIL/CLOSED**; restricted degree 6 as an integral-divisibility diagnostic **CONDITIONAL**; integral section-change quotient **OPEN/LOAD-BEARING**. The next authorized calculation is the integral section-change map on the first potentially 3-divisible degree-2 kernel class, not a standalone degree-6 restricted computation.


## 2026-10-03 — T1-C INTEGRAL FOX LINEARIZATION: FIRST 3-DIVISIBILITY OBSTRUCTION AT I^3

The authorized integral section-change calculation was pushed one filtered order beyond the degree-6 pre-check in the minimal model \((p,s,a)=(3,2,1)\), with \(r=x^3[x,y]\) and \(R=\mathbf Z[Q]\). Put \(I=\ker(R\to\mathbf Z)\), \(X=x-1\), \(Y=y-1\). The exact Fox derivatives are
\[
f_x=N_3(x)+x^3-y=3+6X+4X^2+X^3-Y,
\qquad
f_y=x^4-1=4X+6X^2+4X^3+X^4.
\]
Modulo \(I^3\), the section-change image is generated by these two series acting on the kernel generator.

The scalar defect is \(9\bar z\). Its augmentation forces any coefficient \(a\) of \(f_x\) in a putative cancellation \(9\in(f_x,f_y)\bmod I^3\) to have constant term \(3\). The degree-one \(Y\)-coefficient then forces the \(Y\)-coefficient of \(a\) to be exactly \(1\), because \(f_y\) has no pure \(Y\)-term. At degree two, the pure \(Y^2\)-coefficient becomes
\[
-1+3c_{Y^2},
\]
where \(c_{Y^2}\in\mathbf Z\) is the quadratic coefficient of \(a\). This cannot vanish integrally. The \(f_y\)-term cannot alter the pure \(Y^2\)-coefficient because its leading term is divisible by \(X\). In degree two the relation \([X,Y]\) is already zero in the Demuškin associated graded, so no \(XY-YX\) correction changes this pure \(Y^2\) obstruction.

Equivalently, after the scalar cancellation and the degree-two linear correction, a residual proportional to \(Y^2\bar z\) remains which would require division by \(3\) to remove. This is qualitatively different from the mod-3 degree-5 commutator path: it is an **integral divisibility obstruction**, not a new ordinary-Lie commutator direction.

Logical boundary: this establishes a nonzero class in the \(I^2/I^3\) associated-graded section-change quotient **provided the corresponding \(Y^2\bar z\) class survives the finite-kernel module relation**. The remaining finite-kernel survival check is therefore now the single load-bearing verification. If it survives, the pushed-out abelian-kernel extension is nonsplit, hence the original finite extension is nonsplit. If it is killed by an additional finite-kernel relation, the obstruction closes and the integral quotient must be continued.

Classification:
- degree-6 restricted symbol alone: **FAIL / CLOSED**;
- integral Fox divisibility calculation through \(I^3\): **PASS / LOCAL**;
- pure \(Y^2\) residual before finite-kernel survival check: **PASS / LOCAL**;
- actual abelianized-kernel obstruction: **OPEN / LOAD-BEARING**;
- full finite-extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **OPEN / LOAD-BEARING**.

Next authorized action: verify that \(Y^2\bar z\neq0\) in the actual finite-kernel associated graded at this degree. Do not reopen degree 5, do not invoke a standalone degree-6 restricted-power obstruction, and do not open \(B_s\) yet.


## 2026-10-03 — T1-C FINITE-KERNEL SURVIVAL CHECK: INTEGRAL Abar OBSTRUCTION CONFIRMED (MINIMAL MODEL)

The remaining survival check was completed in the minimal model \((p,s,a)=(3,2,1)\), \(n=10\). The degree-2 relation of the Demuškin quotient is the initial commutator \([X,Y]\); in the finite extension the defining relation \(z^9=x^3[x,y]\) pushes this relation to the critical filtration (the \(z^9\) term lies in degree 9), but it introduces no kernel relation in degree 3 that can annihilate \(Y^2\bar z\). After abelianizing the kernel, the degree-3 kernel module is generated by the degree-2 augmentation actions on the degree-1 normal kernel class \(\bar z\). The only degree-3 relations inherited from the quotient identify the ordinary \(XY/YX\) ordering; they do not kill the pure \(Y^2\bar z\) class.

Hence the pure \(Y^2\bar z\) residual found in the integral Fox calculation survives the actual finite-kernel associated graded. Therefore the pushed-out abelian-kernel extension has a nonzero section-change class already in this low integral filtration layer. Since a split original extension would push out to a split abelian-kernel extension, the original finite extension is **nonsplit in the minimal stress model at \(n=10\)**.

This is the first genuine load-bearing obstruction obtained after all earlier scalar, mod-\(p\), and degree-5 commutator candidates were removed. It is not a degree-6 restricted-Lie artifact: it is an integral divisibility obstruction visible in the Fox section-change quotient.

Logical boundary: this proves nonsplitting for the audited minimal stress model. It does **not** yet prove the general statement for every \((p,s,a,d)\), and it does not by itself establish the exact threshold \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\). The next generalization must prove that the same integral \(Y^2\)-type obstruction persists for the full odd-prime family, or identify the precise exceptional parameters.

Classification:
- minimal-model integral \(\bar A\)-pushout obstruction: **PASS / LOCAL**;
- minimal-model finite-extension nonsplitting at \(n=10\): **PASS / LOCAL**;
- general \((p,s,a,d)\) integral obstruction: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **OPEN / LOAD-BEARING**;
- full finite-extension threshold theorem: **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

Next authorized action: transport the integral Fox divisibility obstruction from \((3,2,1,2)\) to general odd \(p\), \(s>a\), beginning with the rank-two factor. No degree-5 reopening, no standalone degree-6 branch, and no \(B_s\) promotion.


## 2026-10-03 — GATE T1-C GENERAL INTEGRAL FOX OBSTRUCTION / EXACT STRESS-FAMILY THRESHOLD

The minimal integral divisibility obstruction generalizes cleanly to every odd prime \(p\), every \(s>a\ge1\), and the rank-two stress factor \(r=x_1^{q}[x_1,x_2]\) with \(q=p^a\). Write \(I\) for the augmentation ideal of \(\mathbf Z[Q_s]\), \(X=x_1-1\), \(Y=x_2-1\). The Fox derivatives are
\[
f_1=N_q(x_1)+x_1^q-x_2,
\qquad
f_2=x_1^{q+1}-1.
\]
After projecting to the pure \(Y\)-associated-graded direction (set \(X=0\) and discard mixed terms), one has exactly
\[
f_1\mapsto q-Y,
\qquad
f_2\mapsto0.
\]
Thus any integral section-change cancellation of the scalar defect \(p^s\bar z\) would require, to successive \(Y\)-orders,
\[
(q-Y)A(Y)=p^s.
\]
Formally
\[
\frac{p^s}{q-Y}
=p^{s-a}\sum_{j\ge0}p^{-aj}Y^j.
\]
Let \(r=\lfloor s/a\rfloor\). Then the coefficients for \(j<r\) are integral, but the coefficient at \(j=r\) is
\[
p^{s-a(r+1)},
\]
which is not an integer because \(s-a(r+1)<0\). Equivalently, after all lower-order integral lift corrections are made, the first unavoidable pure-\(Y\) residual is a nonzero multiple of \(Y^r\bar z\) modulo \(q\). This is an integral divisibility obstruction, not a mod-\(p\) restricted-power artifact.

The survival of this class in the actual finite kernel is independently witnessed by the metabelian quotient
\[
H=C_{p^s}\rtimes C_{p^s},
\qquad yzy^{-1}=z^{1+p},
\]
obtained from \(G_{s,a}\) by setting \(x_1=1\) and all other \(x_i=1\). Here \(z^{p^s}=1\), \((y-1)^r z=p^r z\ne0\) because \(r<s\), and \(D_{p^s+1}(H)=1\) for odd \(p\): for \(\gamma_i(H)=\langle z^{p^{i-1}}\rangle\) one has \(i p^j\ge p^s+1\Rightarrow i-1+j\ge s\), so every Zassenhaus factor is trivial at that depth. Hence the pure-\(Y\) obstruction survives the actual finite-window kernel.

This yields a genuine nonzero class in the abelianized-kernel pushout, so the finite extension is nonsplit at \(n=p^s+1\). Conversely, for every \(n\le p^s\), the map \(D/D_n(D)\to G_{s,a}/D_n(G_{s,a})\) induced by the generator lifts is a section: the defining relation satisfies \(z^{p^s}\in D_{p^s}(G_{s,a})\subseteq D_n(G_{s,a})\), and the remaining \(D_n(D)\) relations map into \(D_n(G_{s,a})\). Therefore the relative extension splits for all \(n\le p^s\).

Consequently, for the declared rank-two stress family (and hence as a stress quotient for the higher-rank family), the exact relative separation threshold is now established:
\[
\boxed{n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1.}
\]
The higher-rank case inherits nonsplitting from the rank-two quotient by setting the extra Demuškin generators to \(1\), while the lower-bound splitting argument is unchanged.

Classification:
- general odd-\(p\) integral Fox divisibility obstruction: **PASS / LOCAL**;
- survival in the actual finite kernel: **PASS / LOCAL**;
- critical nonsplitting at \(p^s+1\): **PASS / CLOSED** for the declared stress family;
- splitting for every \(n\le p^s\): **PASS / CLOSED** for the declared stress family;
- exact \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **PASS / CLOSED** for the declared stress family;
- universal free-by-Demuškin theorem beyond this stress family: **OPEN**;
- blind carrier search: **STOP / NOT AUTHORIZED**.


---

# SOURCE: research/PAPER4_INTRINSIC_RECONSTRUCTION_W10_END_TO_END_AUDIT_2026-10-03.md

<!-- blob-sha: 10085a6fd3479035d3efc51ae5aa5f63196ed4c4 -->

# PAPER 4 — INTRINSIC RECONSTRUCTION FEASIBILITY GATE: W10 END-TO-END ATTACK
## 2026-10-03

## Decision
The bounded Gate-B attack is authorized as a single end-to-end test at
[
(p,s,a,n)=(3,2,1,10).
]
The purpose is not to reopen the frozen relative-threshold proof or to begin blind carrier search. It is to test, in one package, whether the unmarked critical finite window can canonically recover enough marked quotient/extension data to determine the relative obstruction.

The package to test is:
[
W_{10}	o operatorname{Aut}(W_{10})	o
{	ext{admissible quotient data}}	o
{	ext{relative extension obstruction}}.
]

Required components:
1. intrinsic first-layer data (H^1(W_{10},mathbf F_3)) and cup-radical;
2. the first critical degree-9/degree-10 jet carrying the (z^9=r_D) information;
3. the automorphism action on that combined structure;
4. admissible quotient/lift candidates and their (operatorname{Aut}(W_{10}))-orbits;
5. the induced relative extension class after quotienting lift-change coboundaries.

## Pre-check
Object: the unmarked filtered finite group (W_{10}=G_{2,1}/D_{10}(G_{2,1})), together with intrinsic filtration data.

Input: only the abstract filtered group; the map to (D/D_{10}(D)) is not supplied.

Functoriality: automorphisms of the filtered group must transport every accepted intrinsic construction.

Gauge: presentation choices, generator lifts, and quotient-map postcomposition by automorphisms are not intrinsic and must be quotiented.

Orientation bridge: a candidate is accepted only if it canonically determines the marked extension class, not merely a presentation relator or scalar defect.

q-blindness: the candidate must not insert (q=3^a) by definition.

Separation: if two admissible marked realizations of the same unmarked (W_{10}) have different relative obstruction classes, intrinsic reconstruction fails.

Novelty: merely recovering the already-known finite Kummer selector from (W_{10}) is not sufficient.

Stop: if the quotient/extension object is only a re-encoding of the forgotten marked map, classify it as tautological rather than intrinsic.

## Decision outcomes
- intrinsic quotient/extension orbit is uniquely determined and its obstruction is constant: PASS / LOCAL, positive reconstruction candidate;
- same unmarked window supports different obstruction values: FAIL / CLOSED;
- quotient orbit is intrinsic but obstruction is not: OPEN, reduced to extension-class functoriality;
- no mathematically legitimate finite computation can distinguish the alternatives within this bounded model: STOP and return to realistic Paper 4.

## Scope warning
The choice (a=1) is deliberate because (p=3,s=2) makes (n=10) the smallest critical stress-family window. This is the known boundary case where the generic (age2) finite-kernel survival witness does not apply. No conclusion for the certified (age2) theorem is changed by this gate.


## 2026-10-03 — END-TO-END RESULT

### 1. First layer is intrinsic
For the minimal stress presentation
[
G_{2,1}=langle z,x,ymid z^9=x^3[x,y]angle,
qquad W_{10}=G_{2,1}/D_{10}(G_{2,1}),
]
the mod-3 cup form on
[
H^1(W_{10},mathbf F_3)
]
has rank two, with the radical equal to the one-dimensional line generated by the class of (z). Thus the radical line is an intrinsic characteristic line of the unmarked finite window. This is the first successful reconstruction datum.

### 2. The critical jet does not choose a canonical generator
The degree-9 critical information sees the (z^9) layer. Replacing a radical generator by another lift with the same radical line changes the representative of the degree-9 class by gauge/automorphism action. In particular, the intrinsic object is not a distinguished (z), but the radical line together with its critical jet orbit.

On the first cohomological layer, the automorphism stabilizer has the expected form: the quotient (H^1/R) carries the nondegenerate alternating form, hence its induced action is (SL_2(mathbf F_3)); the radical may be scaled by (mathbf F_3^	imes), and radical-valued shears are allowed. The resulting H^1-level stabilizer has size
[
24cdot 3^2cdot2=432.
]
This confirms that any construction depending on a chosen radical generator rather than its Aut-orbit is not intrinsic.

### 3. Admissible quotient candidates collapse to one orbit at the H^1 level
The canonical marked quotient kills the radical direction and identifies the nondegenerate quotient with the Demuškin (Q_{10}=D/D_{10}(D)). Any admissible quotient inducing the same radical kernel line has, after postcomposition by an automorphism of (Q_{10}), the same H^1 map. The remaining freedom is an IA/lift correction.

A concrete family of such corrections is visible already from the critical window: if (cin D_2(Q_{10})) has (c^9=1), the assignment (zmapsto c), (xmapsto x), (ymapsto y) satisfies the relator condition at the finite depth. These changes are compatible with the radical-line description and are expected to lie in the same IA orbit. They therefore do not furnish a same-window separation by themselves.

### 4. Obstruction is constant on a genuine quotient-map orbit
Split/non-split is invariant under:
- precomposition by an automorphism of (W_{10});
- postcomposition by an automorphism of (Q_{10});
- kernel automorphisms in the corresponding pushout.

Hence, once all admissible quotient maps are shown to lie in one Aut-orbit, the relative obstruction becomes an intrinsic Boolean invariant of the unmarked window. This is the correct target: a canonical quotient map itself is stronger than necessary.

### 5. Load-bearing gap after the end-to-end attack
The bounded attack therefore does **not** produce a same-window counterexample, and it does **not** prove full canonical reconstruction.

The remaining single lemma is:
[
oxed{
	ext{every admissible }W_{10}	woheadrightarrow Q_{10}
	ext{ with kernel radical line is generated by }
operatorname{Aut}(W_{10})	imesoperatorname{Aut}(Q_{10}).
}
]
Equivalently, the residual IA quotient-map space must be shown to be one orbit.

This is substantially narrower than the original reconstruction problem. No new carrier is needed at this stage.

### Classification
- intrinsic (H^1) cup-radical line: **PASS / LOCAL**;
- critical-jet orbit as an intrinsic refinement: **PASS / LOCAL**;
- same-window separation at the tested minimal stress model: **FAIL to find / NOT CLOSED**;
- quotient-map orbit uniqueness at (H^1) level: **PASS / LOCAL**;
- full quotient-map orbit uniqueness: **OPEN / LOAD-BEARING**;
- obstruction invariance on a fixed quotient-map orbit: **PASS / LOCAL**;
- unmarked intrinsic reconstruction: **OPEN / LOAD-BEARING**.

### Important scope correction
The test ((p,s,a,n)=(3,2,1,10)) is the (a=1) boundary. It is therefore a feasibility probe, not evidence extending the certified (age2) relative theorem. It does, however, directly test the structural question of whether the unmarked critical window can recover sufficient marked data.

### Decision
The end-to-end W10 attack has reached its intended bounded boundary. It has **not** produced the desired FAIL/CLOSED separation. It has reduced the positive route to one explicit IA-orbit/transitivity lemma. Further work should attack that lemma directly; no return to radical/critical-jet/carrier sub-searches is warranted.

## 2026-10-03 — CRITICAL CORRECTION: EXPLICIT IA QUOTIENT-MAP FAMILY

A stronger end-to-end check shows why the remaining orbit lemma is genuinely load-bearing.

Let
[
Q_{10}=D/D_{10}(D),qquad cin D_2(Q_{10}).
]
Since (c) has Zassenhaus degree at least (2),
[
c^9in D_{18}(D)subseteq D_{10}(D),
]
hence (c^9=1) in (Q_{10}). Therefore, keeping (x,y) fixed and setting
[
pi_c(z)=c,qquad pi_c(x)=x,qquad pi_c(y)=y
]
satisfies the defining relation
[
pi_c(z)^9=c^9=1
=
x^3[x,y]
quad	ext{in }Q_{10}.
]
So there is an explicit family of admissible epimorphisms
[
pi_c:W_{10}	woheadrightarrow Q_{10}
]
all inducing the same H^1 map and all having the same radical kernel line at the first layer.

This decisively shows that H^1-level orbit uniqueness is not enough. The full question is whether the entire family ({pi_c}_{cin D_2(Q_{10})}) is one orbit under precomposition by (operatorname{Aut}(W_{10})) and postcomposition by (operatorname{Aut}(Q_{10})), or whether distinct critical-jet/IA orbits occur.

The degree-9 critical jet is precisely where this distinction can first appear: a degree-2 shear in the radical lift can contribute through the (3)-power operation at degree (3), and a second (3)-power reaches degree (9). Thus the critical jet cannot be discarded.

Most importantly, no claim of quotient-map orbit uniqueness is now promoted. The previous H^1-level PASS remains only a first-layer statement.

### Updated classification
- cup-radical line: **PASS / LOCAL**;
- H^1 quotient data: **PASS / LOCAL**;
- explicit family of admissible quotient maps (pi_c): **PASS / LOCAL**;
- full quotient-map orbit uniqueness: **OPEN / LOAD-BEARING**;
- same-window separation by different obstruction: **OPEN**;
- unmarked intrinsic reconstruction: **OPEN / LOAD-BEARING**.

The bounded W10 attack therefore ends at a sharply defined finite orbit problem, not at a positive reconstruction theorem and not at a no-go theorem.
