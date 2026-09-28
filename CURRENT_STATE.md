
## 2026-09-28 — PAPER 3 ARTIFACT GATE CLOSED

The repaired source commit `dd3d2e69c4e320129a3d0025c853747dabe744e4` successfully completed the `Build paper PDF` workflow (run `36393007041`). The CI-built submission bundle was independently unpacked and checked.

The packaged `main.tex` has Git blob SHA `0a71fab5f2227b7f4659d5f10fca3e555c7add8b`, matching the authoritative current `paper/main.tex`. The CI PDF is 17 pages. The repaired §8 typed cohomology chain and the subsequent Lemma 5.2 comparison were verified in the extracted PDF text, and pages 9–10 were visually inspected.

CI submission PDF checksum: `2ab01035bb42a16b36b2f1efafa66cafda9c73b041c5a3c5c5aa2c9ca5a8e697`.

Classification:
- artifact gate: **PASS / CLOSED**
- overall Paper 3: **INTERNAL REVIEW PASSED**
- publication novelty: **OPEN / CONDITIONAL**

## 2026-09-28 — PAPER 3 §8 CUP-LINE TYPE REPAIR

The authoritative `paper/main.tex` was repaired at commit `dd3d2e69c4e320129a3d0025c853747dabe744e4`.

The previous §8 sentence incorrectly described the image of \\(\iota_*\\) as still lying in \\(H^2(G,\\mathbb F_3)\\). It is now written with the explicit typed chain
\\[
C_k\xrightarrow{\operatorname{infl}}H^2(G,\mathbb F_3)
\xrightarrow{\iota_*}H^2(G,A_{k-1}(\chi_{k-1})),
\\]
followed by Lemma U5b's identification with the connecting-map variation.

Primary-source verification against Mináč–Pasini–Quadrelli–Tân (Adv. Math. 380 (2021), §7):
- Proposition 7.1: relation initial forms and cup-product evaluation form a commutative pairing diagram.
- Proposition 7.2: for odd p, the relevant degree-two pairing is perfect on the alternating part \\(\Lambda^2(V)\\).
- The present p=3 rank-four relation has one-dimensional degree-two initial-form span, so the §8 finite cup carrier has rank one.

Classification:
- §8 type repair: **PASS / CLOSED**.
- §8 rank-one primary-source compatibility: **PASS / LOCAL**.
- Publication artifact gate: **OPEN / PENDING exact-source CI + PDF/content audit + checksum**.
- Publication novelty: **OPEN / CONDITIONAL**.

The mathematical frontier is unchanged; this is a source-detail repair and independent literature verification.

## 2026-09-28 — PAPER 3 DETAIL REPAIR / LITERATURE AUDIT CURRENT STATE

The authoritative Paper 3 source changed at commit `470d06e34088db2b101acac7ad3bf4b0eaa1bb02`.

Applied:
- §9 lower-bound wording corrected to distinguish (m\le3^{k-2}) (outside (mathcal D_{k,m})) from (3^{k-2}<m\le3^{k-1}) (inside domain, selector fails).
- U5c final sentence now explicitly derives injectivity of (iota_*) from surjectivity of its dual.
- Literature audit wording records only searches actually performed: arXiv and general web searches on 2026-09-28; MathSciNet/zbMATH Open are not claimed.

Targeted literature result:
- Efrat–Quadrelli 2019 confirms prior art for Kummerianity/cohomological and 1-cocycle lifting.
- Mináč–Pasini–Quadrelli–Tân 2021 confirms the minimal-presentation relation/cup-product pairing used here.
- No exact theorem combining the present bare-(Q_k), arbitrary-candidate, finite Kummer recognition, and fixed-scope sharp selector-depth package was identified in the targeted search.

Classification:
- mathematical frontier: unchanged, PASS / CLOSED at declared scope;
- literature audit: PASS / LOCAL;
- publication artifact gate: OPEN / PENDING exact-source CI + PDF/content audit + checksum.

## 2026-09-28 — THREE-PAPER MATHEMATICAL CONTRIBUTION ASSESSMENT RECORDED

For future research continuity, the researcher-facing synthesis is frozen in:
`research/THREE_PAPER_MATHEMATICAL_CONTRIBUTION_ASSESSMENT_2026-09-28.md`.

The three-paper arc is recorded as:
**Paper 1 = finite recognition/factorization → Paper 2 = sharp affine threshold (p^{k-1}+1) → Paper 3 = recognition at the sharp scale, with fixed rank-4 (p=3) selector threshold (3^{k-1}+1) and 1D linear selector-carrier minimality.**

Overall mathematical assessment: **research-level coherent finite-recognition program at the declared scopes**.
Publication novelty: **OPEN / CONDITIONAL**; no priority claim.

This is an explanatory synthesis only; authoritative mathematical classifications remain in the individual Gate/audit records.



## 2026-09-28 — PAPER 3 EXACT-SOURCE ARTIFACT GATE CLOSED

The repaired `paper/main.tex` has now passed the exact-source CI/PDF gate and independent artifact audit.

Authoritative source: `ac53cc2e753fc7b8fb0eb4b78a0085ccfdbc5a89`; blob `3f0bc48ac532d0ed72bcfe876a8283bed178dfbc`; source SHA-256 `bc951dce61717ed184e8763118a3ffef310615b09b95b8fd6ae7ca0a83e42a49`.
CI run **36374270475** and PDF verification: **PASS / CLOSED**. PDF artifact **10950077812**, SHA-256 `d38c63bd1b453482217c7876d818ff7b50e48cbde7f219552953d8a5e36d56c0`, 17 pages. Independent PDF/content audit: **PASS / CLOSED**.

The publication artifact gate is therefore **PASS / CLOSED**. No earlier PDF remains authoritative.
## 2026-09-28 — PAPER 3 REFEREE DETAIL REPAIR 2 / ARTIFACT GATE

The authoritative manuscript source was repaired in commit `2ab97e7d11f5238f6586aa435c9da36d62781d91`. The source-level repair is complete and rechecked. The exact commit triggered Build paper PDF run `36373920812`, currently **IN PROGRESS**.

The publication artifact remains **OPEN / PENDING** until CI compilation, PDF verification, and independent artifact/content audit complete. No prior PDF is authoritative for this source revision.

The mathematical classifications remain unchanged: finite-window recognition PASS/CLOSED; fixed-scope selector threshold PASS/CLOSED; 1D cup-line carrier/minimality PASS/CLOSED in the declared linear selector-carrier category; stronger finite-pair functional OPEN/NOT LOAD-BEARING; novelty OPEN/CONDITIONAL.

## 2026-09-28 — THREE-PAPER PDF REVIEW AUDIT / VERSION-MAPPING CORRECTION

The externally supplied three-paper review was checked against the exact artifacts previously delivered in this session.

- Paper 1 artifact: affine factorization paper, run 36212215849, commit 73001ba0611e4f4aa7db8c733ee01d67542e16eb, 8 pages, SHA-256 09d67cbb88c647e4b7bb92bb91b2d46fe6b9b2c4b32959b7cebd7e468a554eda.
- Paper 2 artifact: finite-window Kummer recognition paper, run 36216012111, commit 0194e01176ae1c21fc70858be3797eeb1a3e7c18, 13 pages, SHA-256 af14b4b7ab971d8ed2d8cac84daae3ff6422ed389cec92b690cc3e184dde1aee.
- Paper 3 artifact: selector-minimality paper, run 36368630643, commit 2b4ccb849e93af840ca216b06c06c72a36c84dd8, 17 pages, SHA-256 00a4ee8deba65eb7c08a9b703d3c19b50801ffdde2c13cab0155186c247bb4e3.

Critical correction:
- The alleged Paper 2 page-3 grid of repeated 1 glyphs is NOT present in the exact delivered Paper 2 artifact. Independent text extraction and visual rendering of page 3 show a normal proof page. No rebuild is authorized from that objection alone.
- The supplied Paper 1 objections correspond to a different/older manuscript mapping; the delivered Paper 1 already uses p,f,k rather than an undefined q and contains the relation with the preceding recognition paper.
- The alleged Paper 3 x3 typo is absent: current source uses x_2^{3^e}.
- The alleged Paper 3 C_k/iota/inflation omission is already explicitly handled in the current source.
- The F_1 algebra and commutator formula are correct under the stated conventions.
- Labute Theorem 4 attribution was already independently verified.

Classification:
- Paper 1: PASS / CLOSED at declared manuscript scope.
- Paper 2: PASS / CLOSED at declared manuscript scope and delivered artifact.
- Paper 3: PASS / CLOSED at declared manuscript scope.
- Publication novelty for all three remains CONDITIONAL/OPEN as already recorded.

No mathematical branch is reopened. Detailed audit: research/THREE_PAPER_PDF_REVIEW_AUDIT_2026-09-28.md.

## 2026-09-28 — PAPER 3 REFEREE DETAIL REPAIR / CI GATE REOPENED

A referee-style adversarial review of the repaired theorem manuscript identified ten detail objections (M1–M10). Primary-source checking and source inspection show that M1, M3, M4, M8, and M9 were legitimate presentation/proof-detail omissions and have now been repaired in paper/main.tex. M2, M5, and M10 were already substantively satisfied; their wording was checked. M6 (Labute Theorem 4) was verified against the primary source and is accurately attributed. M7's alleged rank inconsistency is not a mathematical error: because r in Phi(F), H/Phi(H) is isomorphic to F/Phi(F), so rank(F)=dim H^1(H,F_3). The manuscript now states this explicitly.

- Source repair commit: f686fef1bfbab0b566d2cd424aa097955a2c61ec.
- Referee detail audit: research/PAPER3_REFEREE_DETAIL_REPAIR_2026-09-28.md.
- Mathematical scope/classifications unchanged: finite-window recognition PASS/CLOSED; selector threshold PASS/CLOSED at fixed rank-4 q=3 scope; 1D cup-line carrier/minimality PASS/CLOSED in the declared linear selector-carrier category; stronger finite-pair functional OPEN/NOT LOAD-BEARING; novelty OPEN/CONDITIONAL.
- Manuscript artifact status: OPEN/PENDING exact CI build + independent PDF/package audit.

The previous final PDF remains superseded. No new FINAL artifact may be declared from the prior run.

## 2026-09-28 — PAPER 3 CURRENT-SOURCE ARTIFACT VERIFIED

The final Paper 3 source/PDF synchronization gate is now closed against the exact current source.

- Authoritative main commit: `22f821acdbee5a68513272c70056b7f97a559df5`.
- `paper/main.tex` blob: `599b5d2b19f3e256ab25535a6aebc1beea907fa2`.
- Source SHA-256: `b0fef874507e4f2eef249296d5aca83000a954b0c15c2bf0abfc69664de7b0ac`.
- CI run **36367519607**: **PASS / CLOSED**; compile, verification, package generation and uploads all passed.
- Current PDF: artifact **10947718917**, 16 pages, 412,490 bytes, SHA-256 `2907598169954f6388d764d3596cbe0fad680165c6397a99fcd67efd669b4a6e`.
- Full submission artifact: **10948425435**; internal source/PDF checksums independently verified.
- Independent PDF text/content audit: **PASS / CLOSED**.
- The previous PDF from run 36363508628 is superseded because its head predates the final source repair.
- Paper 1 and Paper 2 artifact audits are recorded in `research/PAPER_ARTIFACT_AUDIT_2026-09-28.md`.

**Manuscript-finalization identity is now:** source commit + source blob + CI PASS on that exact source + independent PDF audit + checksum + artifact manifest.

## 2026-09-28 — PAPER 3 MANUSCRIPT RESYNCHRONIZATION REOPENED FOR VERIFICATION

The prior manuscript-finalization closure is superseded because the adversarial source audit identified proof-detail omissions in `paper/main.tex`. The underlying research results remain closed; only the publication artifact gate is reopened.

- U2 inflation/coefficient-triviality chain: **REPAIRED**.
- U3 minimal one-relator hypothesis: **REPAIRED**.
- D2 transgression quotient \(\mathcal O_k\): **ADDED** as a proof carrier, with no absolute-minimality claim.
- D3 finite cup-line proof: **REPAIRED**, with Mináč–Pasini–Quadrelli–Tân Proposition 7.1 explicitly identified.
- D4 shallow-range non-factorization: **REPAIRED** by direct valuation calculation.
- D4 LTE: **REPAIRED**, using \(v_3(u-1)=1\) and \(v_3(S_N(u))=k-1\).
- Recognition theorem: explicit cross-reference label added.
- Source revision commit: `dc73b0365be4020545e73ec768dbea5fed889b0e` (accidental cleanup typo corrected immediately).
- CI compilation/PDF verification for this revision: **PENDING**.
- Publication novelty: **OPEN / CONDITIONAL**.

The mathematical classifications are unchanged:
- finite-window recognition: **PASS / CLOSED** at the declared fixed rank-4, \(q=3\) Demuškin scope;
- selector threshold \(n_{\mathrm{selector}}(k)=3^{k-1}+1\): **PASS / CLOSED** at that scope;
- one-dimensional cup-line carrier/minimality: **PASS / CLOSED** in the declared linear selector-carrier category;
- canonical \(\mathcal O_k\to\mathbf F_3\) reconstructed from \(E_k\to Q_k\) alone: **OPEN / NOT LOAD-BEARING**;
- publication novelty: **OPEN / CONDITIONAL**.

Next authorized action: CI compile → independent PDF text/content audit → final artifact/hash update → only then restore manuscript-finalization CLOSED.

## 2026-09-28 — PAPER 3 MANUSCRIPT FINALIZATION CLOSED

The manuscript synchronization failure has been corrected and the publication artifact gate is now closed.

- The theorem-paper source is \`paper/main.tex\`; the stale application-only \`paper3/main.tex\` is not the final manuscript.
- Source-level line audit: **PASS / CLOSED**.
- Compile failure identified and repaired: unmatched math delimiter in U5a (“modulo \(3^{k-1}\)”).
- CI **Build paper PDF** run **36363508628**: **PASS / CLOSED**.
- Independent workflow shell audit run **36363508467**: **PASS / CLOSED**.
- Citation hygiene run **36363508580**: **PASS / CLOSED**.
- PDF artifact **10946925073**; full submission artifact **10945849160**.
- PDF SHA-256: \`813fda4840783c3b37002828ccfbe092ccffed6ad189f46430222e5e930a56b0\`.
- Submission-source SHA-256: \`759476d1003fe2d106cfeae5d82f12f8d866afabfddbdd4a3d063cc0d90e7af0\`.
- PDF: **14 pages, 405,622 bytes**.
- Independent PDF text/content audit: **PASS / CLOSED**; theorem, D3 cup-line, D4 selector threshold, conditional novelty boundary, and stale-claim rejection markers were verified.
- Citation-artifact PUA/cite-token contamination found by CI in three research notes was cleaned and citation hygiene subsequently passed.
- Temporary validation PR #5 was closed without merge after successful validation.

Final manuscript synchronization manifest:
\`research/PAPER3_MANUSCRIPT_MANIFEST_2026-09-28.md\`.

Publication novelty remains **OPEN / CONDITIONAL**. The stronger canonical functional from \(E_k\\to Q_k\) alone remains **OPEN / NOT LOAD-BEARING**.

**Next authorized action:** none for manuscript finalization. Do not reopen closed D1/D2/D3/D4 or selector-minimality branches merely to modify the final artifact. Future work is a separate research branch.

## 2026-09-28 — FINAL FRONTIER AUDIT / SELECTOR MINIMALITY CLOSED

The post-recognition frontier has been audited end-to-end.

- Selector minimality for the fixed rank-4, q=3 pro-3 Demuškin group is **PASS / CLOSED**:
  n_selector(k)=3^{k-1}+1.
  The proof uses the two correct shallow ranges: m <= 3^{k-2} where chi_k does not factor, and 3^{k-2}<m<=3^{k-1} where it factors but Kummer lifting fails by the S_N(u) valuation obstruction.
- The finite cup-line carrier C_k=im(H^1(Q_k,F_3) tensor H^1(Q_k,F_3) -> H^2(Q_k,F_3)) is **PASS / CLOSED**, dim C_k=1, using relation-module/cup-product duality rather than bare finite-to-global H^2 injectivity.
- Therefore 1D finite selector-carrier minimality is **PASS / CLOSED** in the declared linear selector-carrier category.
- The stronger canonical functional O_k -> F_p reconstructed solely from E_k -> Q_k remains **OPEN / NOT LOAD-BEARING**.
- Publication novelty remains **OPEN / CONDITIONAL**. The narrow candidate novelty boundary is the finite-factorization/finite-recognition assembly; canonical Kummerian orientation is classical.

Authoritative detailed audit: research/PAPER3_FINAL_FRONTIER_AUDIT_2026-09-28.md, commit b86f332c472cf946902a4e898a597d094fae1b72.

**Next authorized action:** final line-by-line audit of D1/D2, stale manuscript wording cleanup, generalized-q scope reconciliation, then independent LaTeX compilation. Do not reopen the closed selector-minimality or cup-line branches.

---

## 2026-09-28 — P-1 DEGREE-3 STATUS FROZEN / CURRENT FRONTIER GATE D

P-1 is retained as a verified presentation-level baseline, not as the active carrier route.

- (L_3(F)=L_3^{\mathrm{Lie}}(F)\oplus V^{[3]}), (\dim=24): **PASS / CLOSED**.
- (\operatorname{in}_3(r)=X_1^{[3]}): **PASS / CLOSED**, presentation-level.
- (\dim[R_2,V]=4): **PASS / CLOSED**.
- (\operatorname{gr}_3(I_r)=[R_2,V]\oplus\mathbf F_3X_1^{[3]}), (\dim=5): **PASS / CLOSED**.
- (\dim L_3(G)=19): **PASS / CLOSED**.
- (\ker P_G=\mathbf F_3X_1): **PASS / CLOSED — presentation-level only**.
- Canonical line from degree 3 alone: **OPEN**, explicitly not required for the current carrier.

The controlling filtration fact is (F_{(2)}F_{(2)}\subseteq F_{(4)}); the previous incorrect (F_{(2)}F_{(2)}\subseteq F_{(3)}) statement is superseded.

The active finite-window path remains:
\[
W_{10}\to L_{10}(\rho_2)\to\{\delta_{3,\rho_3}\}\to\chi\bmod27,
\]
with Gate A, Gate B, and Gate C recorded as PASS/CLOSED at their declared scopes. No degree-3 canonical-line revival is authorized.

**Current authorized frontier: Gate D.** Test the construction for arbitrary prime/rank/parameter/level \((p,d,q,k)\), and separate formal steps from those requiring Demuškin (PD^2), finite p-group cohomology, and the specific sharp Zassenhaus depth. Absolute carrier minimality and publication novelty remain unclaimed/conditional unless separately established.

---

## 2026-09-28 — U1–U5 VS KUMMERIAN PRIOR-ART BOUNDARY

The four-layer Kummerian/1-cyclotomic audit was compared directly with the U1–U5 proof architecture.

The boundary is now precise:
- **Classical / KNOWN:** canonical Demuškin orientation and its uniqueness as Kummerian/1-cyclotomic; finite coefficient-lifting criteria; cocycle realization and full-group existence.
- **U5 uniqueness mechanism:** conceptually overlaps the classical uniqueness theorem, so it is not itself a novelty claim. Its value in Paper 3 is to make uniqueness compatible with the finite candidate-selector architecture.
- **U1–U2:** the genuinely finite-data bridge: arbitrary twisted crossed cocycles for arbitrary candidate rho factor through the specific finite quotient (Q_k=G/P_{k+1}) via the finite semidirect-product filtration. The audited Kummerian literature does not state this exact bare-(Q_k), arbitrary-candidate factorization theorem.
- **U3:** converts finite Kummer lifting into a finite twisted Fox obstruction. This is the explicit recognition mechanism; its ingredients are classical, but the finite-window assembly remains distinct unless an equivalent theorem is found.
- **U4:** presentation-local identification only; not novelty-bearing.
- **U5:** intrinsic uniqueness/induction; classical uniqueness content, but needed to remove presentation dependence after the finite factorization step.

Therefore the current novelty gate is sharply localized at the finite-factorization/assembly layer, not at “discovering Kummerianity” or “discovering canonical orientation.”

Classification: **PASS / LOCAL** for the prior-art boundary. The mathematical finite-window theorem remains **PASS / CLOSED** in the research record; publication novelty remains **OPEN / CONDITIONAL**.

Next authorized action: no new carrier computation. First perform the final source-level comparison of U1–U3 (especially the semidirect finite-depth factorization) against any equivalent finite-coefficient quotient theorem; only then decide whether the finite-window theorem can be treated as genuinely distinct.

## 2026-09-28 — KUMMERIAN / 1-CYCLOTOMIC FOUR-LAYER PRIOR-ART AUDIT

The authorized narrower literature audit was completed before any new carrier computation.

Primary/near-primary sources checked: Efrat–Quadrelli (2019), Quadrelli–Weigel (2022), and Quadrelli (2024). These sources confirm the classical Kummerian/1-cyclotomic framework: finite coefficient-lifting maps H^1(G,Z_p(theta)/p^n) -> H^1(G,F_p), equivalent cocycle criteria, and uniqueness of the canonical orientation for Demushkin groups.

Four-layer result:
1. L(rho_2): formal lift space is a standard first-order character torsor when nonempty, but no bare-Q_k intrinsic construction was found. **PASS / LOCAL**.
2. {delta_{3,rho_3}}: the underlying coefficient-lift obstruction mechanism is known once an orientation is supplied, but the exact project family is not presented as an orientation-free finite-input object. **PASS / LOCAL**.
3. Exact variation delta_{rho_3(1+9nu)}-delta_{rho_3}=nu cup f-bar: no matching theorem was located. **OPEN / NOT VERIFIED**.
4. Reconstruction from bare Q_k=G/P_{k+1} without importing orientation: no direct theorem was found. **OPEN / LOAD-BEARING**.

Therefore the classical Kummerian theory does not by itself collapse the present finite-window problem. The only potentially non-classical part remains the natural finite-window reconstruction/factorization, not canonical orientation or Kummerianity itself.

Detailed audit: research/PAPER3_DELTA3_MAZUR_MASSEY_PRIOR_ART_AUDIT_2026-09-28.md, Addendum 3.
Next authorized action: compare this four-layer boundary against U1–U5 and isolate exactly which finite-factorization statements require independent proof. No new carrier computation yet.

## 2026-09-28 — δ3 FAMILY-LEVEL VARIATION AUDIT

The prior-art audit was extended from individual \(\delta_{3,\rho_3}\) to the load-bearing family
\[
L(\rho_2)\ni\rho_3\mapsto\delta_{3,\rho_3},
\qquad
\delta_{3,\rho_3(1+9\nu)}(f)-\delta_{3,\rho_3}(f)=\nu\cup\bar f.
\]

Bellaïche's *Pseudodeformations* confirms strong prior art for the surrounding deformation-theoretic pattern: obstruction classes in a cokernel of a degree-2/Yoneda-product map, with extension spaces controlled by cup/Yoneda products.

But the targeted audit did **not** establish that Bellaïche identifies the present coefficient-lift torsor \(L(\rho_2)\) with such a deformation-parameter torsor, nor that his results contain the exact translation law \(\nu\mapsto\nu\cup\bar f\) for this family. It also did not find a finite-Zassenhaus reconstruction theorem for the family without importing the canonical orientation.

Classification:
- parameterized obstruction + H^2/Yoneda/cup framework: **PASS / CLOSED — KNOWN**
- Bellaïche package = exact present \(L(\rho_2),\delta_3\) family: **FAIL / CLOSED — not established**
- exact \(\delta\)-variation formula as Bellaïche theorem: **OPEN / NOT VERIFIED**
- finite-window reconstruction \(W_n\to\{\delta_{3,\rho_3}\}\): **OPEN / NOT FOUND**

The next Kummerian/1-cyclotomic audit must therefore check four items separately: (i) lift torsor, (ii) obstruction family, (iii) translation/variation law, and (iv) finite-window reconstruction.

Detailed addendum: research/PAPER3_DELTA3_MAZUR_MASSEY_PRIOR_ART_AUDIT_2026-09-28.md.
Status: **PASS / LOCAL**.

## 2026-09-28 — PAPER 3 δ3 / MAZUR / MASSEY PRIOR-ART AUDIT

A novelty-first audit was completed before any new carrier computation. The surviving cohomological family is
[
ho_3mapstodelta_{3,ho_3},qquad
delta_{3,ho_3}:H^1(G,mathbf Z/9(ho_2))	o H^2(G,mathbf F_3),
]
from
[
0	omathbf F_3	omathbf Z/27(ho_3)	omathbf Z/9(ho_2)	o0.
]

Key distinction:
- Mazur deformation theory supplies the same **general small-extension / H^2-obstruction mechanism**, but (delta_{3,ho_3}) is not literally the obstruction to lifting (ho_2) to (ho_3). Here (ho_3) is already fixed, and (delta) obstructs lifting a cohomology class (fin H^1(G,mathbf Z/9(ho_2))).
- Efrat's Zassenhaus/Massey/U_n embedding-problem machinery has the same abstract obstruction pattern, but its lifted object is a unipotent representation/defining system, not the twisted coefficient 1-cocycle (f). Therefore (delta_3) is not literally the U_4/Massey obstruction.
- Strong Massey vanishing for Demuškin groups is known, so a fixed-category Massey-vanishing target remains CLOSED as trivial/constant. It does not imply that the full coefficient-extension family ({delta_{3,ho_3}}) is zero.
- Pál–Quick A_3-formality gives independent q-sensitive higher-cohomological information, but its DGA/Hochschild canonical-class input is not the finite Zassenhaus window nor the (delta_3) family.

Classification:
- general H^2 obstruction mechanism: **KNOWN / PASS-CLOSED**
- (delta_3) = Mazur deformation obstruction: **FAIL / CLOSED**
- (delta_3) = Efrat U_4/Massey embedding obstruction: **FAIL / CLOSED**
- strong Demuškin Massey vanishing: **PASS / CLOSED**
- strong Massey vanishing (Rightarrowdelta_3=0): **NOT ESTABLISHED; do not infer**
- A_3-formality = (delta_3): **OPEN / not found**
- finite filtered factorization (W_n	o{delta_{3,ho_3}}): **OPEN / LOAD-BEARING**
- novelty of the finite-window factorization theorem: **OPEN / CONDITIONAL**

Detailed audit: `research/PAPER3_DELTA3_MAZUR_MASSEY_PRIOR_ART_AUDIT_2026-09-28.md`, commit `3c6c0eac5e91fe5ee3c36ae66487e3e087f0522d`.

Next authorized action: a narrower Kummerian/1-cyclotomic prior-art comparison asking whether existing theorems construct the coefficient-lift torsor or equivalent connecting-map family from a finite quotient/Zassenhaus data **without assuming the canonical orientation**. No new carrier computation is authorized before that comparison.



## 2026-09-27 — PAPER 3 MIDPOINT SUMMARY / CURRENT MASTER CONTEXT

Paper 3 is now at a major conceptual checkpoint.

**Original goal:** determine whether canonical Demushkin orientation \(\chi:G\to\mathbf Z_p^\times\), or \(\chi\bmod p^k\), can be recovered from a finite unmarked Zassenhaus window
\[
W_n(G)=(G/D_n;D_1/D_n,\ldots,D_{n-1}/D_n).
\]

**First correction:** no universal threshold such as \(r_{\chi\bmod p^k}=p^{k-1}+1\) is to be asserted. Recognition depth is target/category/filtration dependent:
\[
r_T(\mathcal C;D_\bullet).
\]
Status: universal formula **CLOSED**.

**Second correction:** the attempted same-target factorization/recognition separation was definitionally invalid. If \(f_T\) means the least \(n\) such that \(T\) factors through \(W_n\), and \(r_T\) means the least \(n\) such that \(W_n\) determines \(T\), they express the same information condition. Status:
- same-target \(f_T\neq r_T\): **INVALID / CLOSED — DEFINITIONAL IDENTITY**
- genuine separation: richer carrier \(O\) versus coarser target \(T=\Phi(O)\), comparing \(f_O\) with \(r_T\): **OPEN / LOAD-BEARING**.

**Bockstein target:** 
\[
T_\beta(G)=[\beta_G],\qquad \beta_G:H^1(G,\mathbf F_p)\to H^2(G,\mathbf F_p)
\]
from \(0\to\mathbf F_p\to\mathbf Z/p^2\to\mathbf F_p\to0\). Target convention is locked to the isomorphism class of the linear map, with independent source/target isomorphisms. In fixed-rank Demushkin, \(\dim H^2=1\), so rank determines this target; basis-dependent map is not claimed to be determined.

**Bockstein theorem:** the lower-bound pair
\[
G_p=\langle x,y\mid x^p[x,y]=1\rangle,\quad
G_{p^2}=\langle x,y\mid x^{p^2}[x,y]=1\rangle
\]
has isomorphic \(W_p\) but different \(T_\beta\). For the upper bound,
\[
D_{p+1}(G)\subseteq G^{p^2}[G,G],
\]
so \(W_{p+1}\) determines
\[
G/[G^{p^2}[G,G]]\cong G_{\rm ab}/p^2G_{\rm ab}.
\]
The Bockstein kernel is exactly the mod-\(p\) characters liftable to \(\mathbf Z/p^2\):
\[
\ker\beta_G=
\operatorname{im}\bigl[\operatorname{Hom}(G,\mathbf Z/p^2)\to\operatorname{Hom}(G,\mathbf F_p)\bigr].
\]
Thus \(W_{p+1}\) determines the Bockstein rank and, under the locked target convention, \([\beta]\). Combined with the lower bound:
\[
\boxed{f_{T_\beta}=r_{T_\beta}=p+1}.
\]
Status: **PASS / CLOSED**. This is a consistency theorem, not a separation result.

**Bockstein limitation:** \(T_\beta\) compresses \(q=p^2,p^3,\ldots\) into the rank-zero class and therefore is not by itself a carrier for full canonical orientation.

**Candidate B:** 
\[
\mathcal B_{27}=
(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\beta_1,\beta_9).
\]
Exact object/functoriality: **PASS / CLOSED**. On
\[
G_q=\langle x_1,x_2,x_3,x_4\mid x_1^q[x_1,x_2][x_3,x_4]\rangle,\quad q=3^s,
\]
the carrier detects the three valuation classes \(v_3(q)=1,2,\ge3\):
\[
v_3(q)=1:\beta_1\ne0;\quad
v_3(q)=2:\beta_1=0,\bar\beta_9\ne0;\quad
v_3(q)\ge3:\beta_1=0,\bar\beta_9=0,
\]
with \(\beta_9\circ\iota=\beta_1\). Therefore finite \(q\)-layer detection is **PASS / LOCAL**.

The line-by-line literature audit found strong prior art: Simons (1989) already uses Bockstein constructions for Demushkin tower level subgroups; Efrat–Quadrelli and later 1-cyclotomic/Kummerian work connect coefficient-lift structures to canonical orientation; generalized/higher Bockstein ideas are also established. Hence:
- new mod-27 orientation carrier: **FAIL / CLOSED**
- coefficient-extension/Bockstein novelty: **FAIL / CLOSED**
- no further trivial-coefficient \(\beta_1,\beta_9\) scan authorized.

**Other branches:** F1 Level A = **PASS / CLOSED**, retained but not load-bearing; F1 Level B/Massey sharpness = **OPEN / DEFERRED / NOT LOAD-BEARING**; fixed-rank Demushkin triple-Massey target = **FAIL / CLOSED** because constant; \(T_\cup\) = **FAIL / CLOSED — TRIVIAL TARGET**.

**Current architecture:**
\[
\boxed{W_n(G)\longrightarrow O(G)\overset{\Phi}{\longrightarrow}T(G)}
\]
where \(O\) is richer intrinsic carrier and \(T\) is a coarser target. The load-bearing question is now the carrier-vs-target separation, not same-target factorization vs recognition.

**Next decisive target:** the intrinsic \(P_4/D_{10}\) higher power/relation residual observed in HA58 to distinguish \(q=9\) from \(27\mid q\). The computation alone is not sufficient. Four gates are mandatory:
1. intrinsic definition independent of presentation coordinates;
2. transport/functoriality under the declared morphisms/isomorphisms;
3. intrinsic projective direction \([R_G]\);
4. canonical scalar normalization, or a proof that scalar ambiguity is intrinsic.
Scalar normalization is currently the sharpest attack point.

**New ultimate goal:** not merely “can a finite window recover orientation?” but
\[
\boxed{\text{When, how much, and in what form does finite intrinsic filtered data determine the canonical \(p\)-adic orientation?}}
\]
More concretely:
\[
\boxed{W_n(G)\to O(G)\to\chi_G\bmod p^k}
\]
and a quantitative theory of necessary and sufficient filtered relation information. Final guiding question:
\[
\boxed{\text{How much filtered relation information is necessary and sufficient to recover the canonical \(p\)-adic orientation?}}
\]

Paper 1–2 supply the finite-window, sharpness/obstruction, affine/Kummer, and explicit witness toolkit; Paper 3 is now the abstraction asking how the required information depth depends on the object being reconstructed.

**Current final state:** orientation reconstruction theorem not yet obtained, but the invalid definitions and nonproductive carriers have been substantially eliminated. The load-bearing problem is now sharply localized at intrinsic filtered relation residual \(\to\) canonical orientation, with the four tests above. Next authorized action: full intrinsic definition/transport/projective-direction/scalar-normalization audit of the \(P_4/D_{10}\) residual.


## 2026-09-27 — PAPER 3 T_beta FACTORIZATION AUDIT CRITICAL CORRECTION

The T_beta factorization audit was critically reviewed and the record was tightened. The mathematical threshold remains closed, but the earlier audit overstated closure in two places.

Locked target convention:
\[
T_\beta(G)=[\beta_G]
\]
means the **isomorphism class of the linear map** \(\beta_G:H^1(G,\mathbf F_p)\to H^2(G,\mathbf F_p)\), with independent linear isomorphisms on source and target. Only under this convention does rank determine the target in the fixed-rank Demushkin category (\(\dim H^2=1\)). The actual basis-dependent map is not determined by rank.

The lower-bound pair \(G_p,G_{p^2}\) is explicitly locked to the same Paper 3 category and the same unmarked Zassenhaus-window convention; no marked/presentation structure is used in the separation argument.

Corrected classification:
- target convention: **LOCKED / PASS**
- \(W_{p+1}\Rightarrow G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}\): **PASS / CLOSED**
- \(G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}\Rightarrow[\beta]\): **PASS / CLOSED under target convention**
- \(f_{T_\beta}\le p+1\): **PASS / CLOSED**
- S1/S2 lower-bound pair under Paper 3 conventions: **PASS / CLOSED**
- \(f_{T_\beta}>p\): **PASS / CLOSED**
- \(f_{T_\beta}=p+1\): **PASS / CLOSED**
- same-target T_beta separation: **FAIL / CLOSED**
- novelty of the threshold/equality: **OPEN / NOT YET AUDITED**

Thus the mathematical equality
\[
\boxed{f_{T_\beta}=r_{T_\beta}=p+1}
\]
is retained under the declared conventions, but no novelty claim is attached to it until the exact literature antecedents are checked.

Detailed audit: research/PAPER3_T_BETA_FACTORIZATION_THRESHOLD_AUDIT_2026-09-27.md (corrected commit 0ac32319db372c8e420173a5c9904ca6227e0649).

## 2026-09-27 — PAPER 3 SEPARATION AXIS CORRECTION

A structural correction closes a definitional ambiguity in the factorization-vs-recognition program. If both quantities are defined for the same target T by "T factors through W_n" versus "W_n determines T", then they are the same information condition and cannot furnish a genuine numerical separation. Therefore the load-bearing separation problem must use a richer carrier/observation O and a coarser target T=Phi(O): compare f_O with r_T.

Status:
- same-target f_T versus r_T separation: **INVALID / CLOSED — DEFINITIONAL IDENTITY**
- richer-carrier O versus coarser-target T separation: **OPEN / LOAD-BEARING**
- T_beta branch: **CLOSED** as a consistency check, not a separation example
- next authorized gate: candidate carrier/target pair novelty + non-redundancy audit before computation

The finite Kummer/affine orientation carrier versus a coarser target remains the first candidate family, but no target is promoted until its compression map and independent thresholds are explicit.

## 2026-09-27 — CANDIDATE B MOD-27 BOCKSTEIN CARRIER CLOSED

Mathematical and literature audit complete. B_27 is retained as a finite q-layer detector: PASS/LOCAL. As a new non-tautological mod-27 orientation carrier: FAIL/CLOSED.

The full structured carrier is classified into the three valuation classes on the standard family; no independent orientation-sensitive rigidifier has been exhibited; and direct prior-art overlap exists with Bockstein-based Demushkin level constructions and the Kummerian/canonical-orientation framework. The earlier abstract-symmetry no-go is not used because group-realizability was not established.

No further trivial-coefficient Bockstein scan. Next decisive target: intrinsic P_4/D_10 higher power/relation residual and its scalar normalization/transport theorem.


## 2026-09-27 — PAPER 3 HA58 P4/D10 FULL INTRINSICITY AUDIT

The HA58/P4/D10 route has now been audited end-to-end in the required order: definition -> coordinate dependence -> transport -> projective direction -> scalar normalization.

Authoritative audit:
\`research/PAPER3_HA58_P4_D10_FULL_INTRINSICITY_AUDIT_2026-09-27.md\`
commit: \`e0db79240aa54d181399cda5ae9b3430cb948c97\`.

Final classifications:

- lower-3-central filtration definition: **PROVED**
- q=9 standard-family residual existence: **COMPUTED**
- q=9 versus 27|q detection pattern: **COMPUTED**
- degree-3 q=9 difference = 0: **COMPUTED**
- finite D_4 source classification at mod 27: **PROVED / COMPUTED**
- intrinsic residual definition as HA58 intended: **OPEN**
- residual transport/functoriality: **OPEN**
- standard-family projective direction: **COMPUTED**
- canonical projective map from the intrinsic torsion line: **OPEN**
- frozen standard-family scalar normalization: **COMPUTED**
- canonical scalar normalization: **OPEN**
- intrinsic single-vector \(t_2\) route: **COUNTEREXAMPLE**
- single presentation-independent residual vector: **COUNTEREXAMPLE**
- intrinsic connecting-obstruction family \(\rho_3\mapsto\delta_{3,\rho_3}\): **PROVED**
- richer secondary carrier beyond \(t_2\): **OPEN**

Decisive correction: HA61-B5-12 supplies a same-abstract-group / different-relation-coordinate witness under \(r\mapsto vrv^{-1}\) for which the putative \(t_2\) changes by \(p\) while the intrinsic connecting-obstruction family is unchanged. Therefore the proposed canonical single vector \(t_2\) cannot exist in the intended presentation-independent form. The quotient \(t_2/\langle p\rangle\) is also insufficient because the secondary obstruction evaluates \(f(t_2)\) while the primary-zero condition does not force \(f(p)=0\).

The finite-depth source ledger is now exhausted: after division by 9 mod 3, \(F^9\) and the old \(\gamma_2^3\) sector survive; \(\gamma_3^3\) and \(\gamma_4\) do not. Thus the remaining problem is not an unknown higher-term computation but the intrinsic compression of the surviving secondary obstruction family.

Strategic consequence: **do not resurrect the single-vector P_4 residual route.** The next authorized Paper 3 problem is to determine whether the intrinsic function-valued secondary obstruction family can be compressed to a richer affine/torsor-valued carrier while retaining coefficient-lift dependence.

This strengthens the main Paper 3 architecture \(W_n(G)\to O(G)\to T(G)\): the HA58 case is now a concrete example where a finite filtered computation contains genuine new information but a natural-looking vector compression is non-intrinsic.


## 2026-09-27 — CRITICAL REVIEW CORRECTION OF HA58/P4/D10 AUDIT

The subsequent critical review was itself audited against the repository source chain. Two distinctions are now locked.

1. The review is correct that the original report was not self-contained enough: the proof basis for the intrinsic cohomological family and the exact t_2 counterexample should have been reproduced.
2. The review is not correct that the repository lacks those proofs/definitions. HA61-B5-8/B5-10 explicitly define
\[
L(\rho_2)=\{\rho_3\bmod 9=\rho_2\}
\]
and the coefficient sequence
\[
0\to\mathbf F_3\to\mathbf Z/27(\rho_3)\to\mathbf Z/9(\rho_2)\to0,
\]
with the connecting family
\[
\rho_3\mapsto\delta_{3,\rho_3}.
\]
Naturality of connecting homomorphisms proves the intrinsic cohomological object. Thus this remains **PROVED**, but only at the cohomological-object level.

Likewise HA61-B5-12 supplies the explicit same-group relator-conjugation witness:
\[
r\mapsto vrv^{-1},\qquad t_2\mapsto t_2+\lambda(v)p
\]
with q=3 frozen branch \(\lambda=e_2^*,p=e_1\ne0\). The full intrinsic obstruction family is unchanged. Therefore the single-vector \(t_2\) claim is genuinely **COUNTEREXAMPLE**, not merely OPEN.

The corrected scope is:
\[
\text{intrinsic }\delta_3\text{ family}=\mathbf{PROVED},
\]
but
\[
W_n(G)\to\{\delta_{3,\rho_3}\}_{\rho_3}=\mathbf{OPEN},
\qquad
\{\delta_{3,\rho_3}\}_{\rho_3}\to\chi\bmod27=\mathbf{OPEN}.
\]

The phrase “끝까지 진행했다” is narrowed: the authorized audit procedure was completed; the orientation-reconstruction problem itself remains OPEN.

The detailed correction is recorded in
research/PAPER3_HA58_P4_D10_FULL_INTRINSICITY_AUDIT_2026-09-27.md
at commit 471321c973de05c6c5ac407f3944b3a12017b331.


## 2026-09-27 — HA58 SECOND CRITICAL REVIEW: δ_3 / t_2 SCOPE LOCK

- Each δ_{3,ρ_3}, and the full lift-indexed family L(ρ_2) → δ_{3,ρ_3}, are PROVED at the cohomological-object/naturality level once ρ_2 is fixed.
- Finite filtered factorization W_n → {δ_{3,ρ_3}} is OPEN.
- If ρ_2 is the known canonical mod-9 orientation, L(ρ_2) nonempty is EXTERNAL by established canonical-orientation existence. Non-circular finite-filtered recovery remains OPEN.
- The t_2 no-go is a genuine COUNTEREXAMPLE in the q=3 rank-four branch, sufficient to rule out a universal canonical single-vector theorem. No identical formula is claimed for every q-branch.
- Full-torsor zero-selector uniqueness is COUNTEREXAMPLE / CLOSED in rank 4: a nonzero cup functional has 3-dimensional kernel, so a zero, if it exists, leaves up to 27 lifts.
- The variation formula, finite-filtered existence, and any canonical one-dimensional lift restriction are OPEN.
- “Torsor-valued carrier” is a candidate architecture, not an established result.

Next authorized gate:
W_n(G) → {δ_{3,ρ_3}}_{ρ_3∈L(ρ_2)}
with an explicit category and no importation of the canonical orientation into the factorization proof.


## 2026-09-27 — HA58 THIRD CRITICAL REVIEW: VARIATION / GATE SCOPE LOCK

Two corrections are now locked.

1. The intrinsic variation formula δ_{3,ρ_3(1+9ν)}(f)−δ_{3,ρ_3}(f)=±(ν∪f) remains **OPEN**. Therefore the statement that the full rank-four zero-selector is already a COUNTEREXAMPLE/CLOSED is too strong. What is proved is only the conditional consequence: if the variation formula holds and is nonzero, then fixed-f zeros form an affine hyperplane of size 27. Unconditional singleton failure remains OPEN unless an independent counterexample is supplied.

2. Gate A must not reopen the already-audited mod-9 result. The projective degree-(2,3) carrier recovering χ mod 9 is already recorded as PASS/CLOSED at the declared audited level. The unresolved HA61 gates are: finite-input construction of L(ρ_2) without importing higher orientation data; finite-input factorization to the δ_3 family; and reconstruction/compression of χ mod 27.

Terminology: “cohomological-object level” now explicitly means well-defined/functorial for fixed G and fixed ρ_2, not D_•-intrinsic or finite-window-determined. When nonempty, L(ρ_2) is an H^1(G,F_3)-torsor algebraically; this does not establish a finite filtered torsor-valued carrier.


## 2026-09-27 — HA58 CRITICAL REVIEW #4: VARIATION FORMULA PROVED, FINITE ACCESS REMAINS OPEN

Direct cochain calculation proves, for rho_3'=rho_3(1+9nu) and f in H^1(G,Z/9(rho_2)),

**delta_{3,rho_3'}(f)-delta_{3,rho_3}(f)=nu cup bar(f)**,

where bar(f) is the mod-3 reduction, under the standard inhomogeneous differential convention (up to overall sign under the opposite connecting-map convention).

The earlier Ext argument is withdrawn: multiplication by 3 on Z/9(rho_2) is not injective, so the displayed sequence was not exact. The variation theorem survives independently by the explicit cochain proof.

For fixed f with bar(f) != 0, Demushkin cup nondegeneracy makes the variation a nonzero functional on rank-4 H^1(G,F_3). Hence any nonempty zero-set is an affine hyperplane of size 27. But nu=0 is a zero only when delta_{3,rho_3}(f)=0; finite-filtered zero existence remains OPEN. If bar(f)=0, the zero-set is either empty or all 81 lifts.

Updated status: variation formula **PROVED**; fixed-f 27-fold zero-set **PROVED CONDITIONALLY**; finite-filtered access to L(rho_2) and the full delta_3 family **OPEN**; family-to-chi mod 27 recognition **OPEN**. The q=3 rank-four t_2 no-go remains a genuine COUNTEREXAMPLE.

Next load-bearing task: construct or refute a finite-filtered carrier realizing the lift torsor/family without importing chi mod 27.


## 2026-09-27 — HA58 ZERO-EXISTENCE REVIEW: DEMUSHKIN CASE CAN BE CLOSED AT THEOREM LEVEL

A further distinction is required. For fixed-rank Demushkin G, the standard Demushkin duality theorem gives dim H^2(G,F_3)=1 and a nondegenerate cup-product pairing H^1(G,F_3) x H^1(G,F_3) -> H^2(G,F_3). Therefore, for bar(f) != 0, the functional nu -> nu cup bar(f) is surjective onto H^2(G,F_3). Hence the equation

nu cup bar(f) = -delta_{3,rho_3}(f)

always has a solution, and the fixed-f zero-set is an affine 3-dimensional hyperplane of size 27 in rank 4.

Thus the zero-existence issue is not an intrinsic open problem once the standard Demushkin duality theorem is admitted. Its status should be recorded as **EXTERNAL/PROVED UNDER DEMUSHKIN DUALITY**, not OPEN. What remains open is the finite-filtered construction/access of the torsor and the delta-family, and the special case bar(f)=0 is not resolved by this surjectivity argument (variation is then identically zero, so the zero-set is either empty or all 81).

This does not change the next load-bearing gate: W_n(G) -> L(rho_2) or equivalently an appropriate finite-data realization of the full lift-indexed delta-family without importing chi mod 27.


## 2026-09-28 — FINAL U1–U3 PRIOR-ART COMPARISON

The final source-level comparison was completed before new carrier computation.

- U1 semidirect finite-depth calculation uses standard twisted-cocycle/semidirect ingredients, but no audited source states the exact packaged theorem that arbitrary candidate orientations factor through the specific finite quotient Q_k=G/P_{k+1} via this finite semidirect filtration. **OPEN / NOT FOUND as prior-art identity.**
- U2 is a formal consequence of U1 and gives H^1(Q_k,A_k(\bar\rho)) ≅ H^1(G,A_k(\rho)). Existing Kummerian quotient-inheritance results assume an oriented pair and additional hypotheses; they do not identify with this arbitrary-candidate factorization. **PASS / CLOSED for U2; FAIL / CLOSED as literature identity.**
- U3's twisted cocycle, prescribed-generator, and relation-obstruction ingredients are classical, but the exact finite-window twisted-Fox recognition assembly on Q_k was not found. **OPEN / NOT FOUND.**

Final boundary: possible novelty remains localized at finite factorization/assembly, not canonical orientation or Kummerianity. Publication novelty remains **OPEN / CONDITIONAL**.

Next authorized action: carrier computation may resume under the U1–U3 theorem chain; no absolute novelty claim is permitted.


## 2026-09-28 — Citation hygiene correction

The prior hygiene detector had a false-negative condition caused by invisible citation delimiters. Fifteen affected files were cleaned. The hardened workflow now rejects Private Use Area characters and known citation-artifact patterns; run 36331775297 passed. Current hygiene status: **PASS / CLOSED**. No mathematical conclusion changed.


## 2026-09-28 — PAPER 3 ZASSENHAUSZ WINDOW SHARPNESS CLOSED

The authorized carrier computation now yields a sharpness theorem for the finite Kummer selector. Let (N=3^{k-1}). U1–U3 prove sufficiency of (Q=G/P_{N+1}). For the canonical candidate (chi_k(x_2)=(1-3)^{-1}) and the mod-3 class (f(x_2)=1), every twisted cocycle lift satisfies
[
z(x_2^N)=left(sum_{j=0}^{N-1}chi_k(x_2)^jight)z(x_2).
]
LTE gives valuation (k-1) for the geometric sum, so (z(x_2^N)
eq0pmod{3^k}). Since (x_2^Nin P_N), the canonical lifting problem does not factor through (G/P_N). Thus the preceding window fails.

Therefore the exact Zassenhaus-window threshold of the declared Kummer selector is
[
\boxed{n_k^{\mathrm{Kum}}=3^{k-1}+1}.
]
In particular (n_2=4) and (n_3=10). This is selector sharpness, not absolute minimality among arbitrary carriers.

Classification:
- preceding-window obstruction: **PASS / CLOSED**
- sharp selector threshold: **PASS / CLOSED**
- absolute carrier minimality: **OPEN / NOT CLAIMED**
- publication novelty: **OPEN / CONDITIONAL**

Detailed audit: `research/PAPER3_ZASSENHAUSZ_WINDOW_MINIMALITY_AUDIT_2026-09-28.md`.
Next authorized target: richer-carrier (O\to T) separation; do not reopen the already-sharp selector window.


## 2026-09-28 — Critical review correction: predecessor-window descent

 Critical-review correction: the sharpness proof is sound, but the audit must explicitly establish descent of the canonical action to G/P_N. This follows from Zassenhaus functoriality and D_N(1+3Z_3)=1+3^kZ_3 for N=3^{k-1}. The witness then proves failure of the Kummer predicate on the preceding quotient itself. The independent modular table is k=2..6; all-k validity comes from LTE. Classification remains PASS/CLOSED for selector sharpness.
Detailed audit correction: `research/PAPER3_ZASSENHAUSZ_WINDOW_MINIMALITY_AUDIT_2026-09-28.md` (commit `c25eb982fc8ff4280098b44e4c4992ed6f86e563d`).

## 2026-09-28 — PAPER 3 GATE D REOPENED: D2 H^2 INFLATION OBJECTION

The previous Gate D CLOSED label is superseded. A critical five-term Hochschild–Serre audit shows that for N=P_{p^{k-1}+1}(G),
\\[
\ker(H^2(Q_k,F_p)\to H^2(G,F_p))\cong H^1(N,F_p)^{Q_k},
\\]
because H^1(Q_k,F_p)->H^1(G,F_p) is surjective and hence the transgression is injective. Since N is a nontrivial open pro-p subgroup and Q_k is a finite p-group, the fixed-point space is nonzero. Thus the asserted H^2 inflation injectivity, and hence the bare-Q_k D2 reconstruction, fails.

Classification:
- Gate D architecture: **PASS / LOCAL**.
- D2 bare-Q_k H^2 argument: **FAIL / CLOSED**.
- D2 replacement extension/transgression carrier: **OPEN / LOAD-BEARING**.
- D3 global uniqueness mechanism: **PASS / LOCAL**, finite reconstruction conditional on D2.
- D4 LTE sharpness: **PASS / LOCAL**.
- full arbitrary-(p,d,q,k) Gate D: **CONDITIONAL / OPEN**.
- Gates A-C fixed (p=3,d=4,q=3): **PASS / CLOSED**.
- absolute carrier minimality: **OPEN / NOT CLAIMED**.
- publication novelty: **OPEN / CONDITIONAL**.

Next authorized action: repair D2 using extension/transgression data or a precisely identified quotient-level obstruction subspace. Do not treat Gate D as closed.

## 2026-09-28 — LIVE GATE D2 REPAIR: DEEPER-WINDOW COHOMOLOGY

The rejected bare-Q_k H^2-injectivity argument is replaced by a weaker continuity statement. For Q_k=G/P_{p^{k-1}+1}, every H^2(Q_k,F_p) class that dies in H^2(G,F_p) dies after some deeper finite Zassenhaus quotient W_{p^{k-1}+1+m}. Finite-dimensionality of H^2(Q_k,F_p) implies stabilization at some finite m_0. This is an existence theorem only: no explicit or uniform bound for m_0 is known, and m=1 is not established.

Current D2 frontier:
- continuity/stabilization existence: **PASS / LOCAL**;
- m=1 sufficiency: **OPEN**;
- uniform computable m-bound: **OPEN / LOAD-BEARING**;
- finite delta-family reconstruction at corrected depth: **OPEN / LOAD-BEARING**.

For k=2, p=3, d=4, the first concrete audit is W_4 -> W_5, with extension kernel P_4/P_5. The required calculation is the W_5-fixed subspace of H^1(P_4/P_5,F_3), its transgression image in H^2(W_4,F_3), and then the position of the actual delta-family relative to that kernel. No claim is made that the nonzero full kernel contains the canonical delta class.


## 2026-09-28 — D2 FIRST HAND CALCULATION COMPLETED

The first corrected deeper-window computation for p=3,d=4,k=2 is now complete. For the central extension
\[
1\to P_4/P_5\to W_5\to W_4\to1,
\]
MRT gives dim_F3(P_4/P_5)=45. Since [P_4,G]⊂P_5, W_5 acts trivially on the fiber, so H^1(P_4/P_5,F_3)^{W_5} has dimension 45. Frattini containment makes H^1(W_4,F_3)->H^1(W_5,F_3) an isomorphism; hence transgression is injective and the one-step inflation kernel H^2(W_4,F_3)->H^2(W_5,F_3) has dimension 45.

The canonical delta branch is outside this kernel because its image in H^2(G,F_3) is nonzero. Thus m=1 does not kill the canonical branch. The remaining load-bearing question is whether every false candidate is also outside this 45-dimensional kernel; exact delta-family/kernel intersection remains OPEN.

Classification:
- m=1 kernel structure: **PASS / CLOSED**;
- canonical branch survives m=1: **PASS / LOCAL**;
- m=1 full selector: **OPEN / LOAD-BEARING**;
- exact delta/kernel intersection: **OPEN / LOAD-BEARING**;
- uniform m-bound: **OPEN / LOAD-BEARING**.

Detailed calculation: research/PAPER3_D2_P4_P5_HAND_CALC_2026-09-28.md


## 2026-09-28 — PAPER 1 ↔ PAPER 3 Q4 / P4-P5 BRIDGE AUDIT

A dedicated side investigation resolved the previously noted 45-dimensional coincidence.

For the verified Paper 1 construction,
\[
Q_4=L_4(F)/(R)_4,\quad \dim Q_4=45,
\]
and the orbit span satisfies \(\dim W_{45}=45\), hence
\[
\boxed{W_{45}=Q_4}.
\]

For the rank-4 p=3 Demuškin group, the free restricted-Lie/mild Zassenhaus presentation identifies the degree-4 Zassenhaus graded piece with the same quadratic degree-4 quotient:
\[
\boxed{P_4/P_5\cong Q_4\cong W_{45}}.
\]
This is a structural identification, not a dimension-only inference.

The corrected D2 one-step extension
\[
1\to P_4/P_5\to W_5\to W_4\to1
\]
has transgression image
\[
\ker(H^2(W_4,\mathbf F_3)\to H^2(W_5,\mathbf F_3))
\cong H^1(P_4/P_5,\mathbf F_3)
\cong Q_4^*
\cong W_{45}^*,
\]
with dimension 45.

Thus the old Paper 1 45-dimensional object is precisely the degree-4 Zassenhaus fiber, while the corrected Paper 3 D2 one-step cohomological ambiguity is its dual. This does not revive the old orientation-carrier route.

Classification:
- W45=Q4: PASS / CLOSED
- Q4 isomorphic to P4/P5: PASS / CLOSED at the declared rank-4 p=3 Demuškin scope
- D2 one-step kernel isomorphic to Q4*: PASS / CLOSED
- delta-family / Q4* intersection: OPEN / LOAD-BEARING
- m=1 full D2 selector: OPEN / LOAD-BEARING
- Paper 1 orientation-carrier route: HISTORICAL / SUPERSEDED

Detailed record: research/PAPER1_PAPER3_Q4_P4P5_BRIDGE_AUDIT_2026-09-28.md.

Next authorized side action: test the delta-variation family against the Q4* transgression sector; do not restart the old search for an orientation vector inside W45.

## 2026-09-28 — CRITICAL REFINEMENT: D2 / Q4* COMPARISON TYPE

The proposed direct comparison “delta-family ∩ Q4*” is now corrected as INVALID / CLOSED — type mismatch.

The delta-family consists of connecting homomorphisms into H^2, whereas Q4* is identified by transgression with a 45-dimensional subspace of H^2(W4,F3). Thus the correct comparison is output-class-wise:
delta_{3,rho3}(f) in tra(Q4*) = ker(H^2(W4)->H^2(W5)).

For every false lift rho3'=rho3(1+9nu), nu nonzero, the global variation formula and Demushkin cup nondegeneracy give some f with nonzero variation. Since a class in the one-step kernel maps to zero in H^2(G), that separating global variation class cannot be in the one-step kernel. This is PASS / LOCAL, conditional on the finite representative/factorization needed at W4.

The load-bearing finite question is:
for every nu nonzero, does there exist f whose finite representative of nu cup fbar survives W4 -> W5?

The Paper 1 10-25-10 structure remains potentially useful only after dualizing Q4 and proving the induced Sp4(F3)-module convention. It is not a decomposition of the delta-family itself.

Detailed correction: research/PAPER1_PAPER3_Q4_P4P5_BRIDGE_AUDIT_2026-09-28.md.


## 2026-09-28 — D2-A / D2-B CLOSED: FINITE REPRESENTATIVE AND SURVIVAL

The declared D2 load-bearing implication is now proved for the fixed rank-four pro-3 Demushkin case.

For any false lift rho_3'=rho_3(1+9nu), 0 != nu in H^1(G,F_3), the audited variation identity and canonical Kummerian existence give delta_{rho_3'}(f)=nu cup fbar. Demushkin cup nondegeneracy supplies a in H^1(G,F_3) with nu cup a != 0, and the audited reduction map supplies f with fbar=a.

Because P_4 is contained in Phi(G)=P_2, both nu and a factor through W_4=G/P_4. Thus alpha_4=nu_4 cup a_4 in H^2(W_4,F_3) inflates to the nonzero global separating class delta_{rho_3'}(f). Hence alpha_4 cannot die under W_4 -> W_5: if it did, functoriality would force its image in H^2(G,F_3) to vanish.

Therefore:
global separation => finite W4 representative => W4 -> W5 survival.

This closes the exact D2-A and D2-B statements. The previously proposed literal "delta-family intersect Q4*" calculation is not required: the 45-dimensional transgression kernel consists of classes with zero image in global H^2, while the separating variation class has nonzero global image.

Logical boundary: this does not claim that the entire delta-family is reconstructible as a map-valued object from W4 alone. It proves the existence-of-a-separating-output criterion that D2 actually requires.

Classification:
- D2-A finite representative: PASS / CLOSED
- D2-B W4 -> W5 survival: PASS / CLOSED
- m=1 full separation at the stated existence-of-a-separating-output criterion: PASS / CLOSED
- exact delta-family / Q4* intersection: NOT REQUIRED / SUPERSEDED
- full W4 reconstruction of the entire delta-family: SEPARATE / NOT CLAIMED

Detailed record: research/PAPER3_D2_FINITE_REPRESENTATIVE_SURVIVAL_RESULT_2026-09-28.md.


## CRITICAL AUDIT — 2026-09-28 — D2 PARAMETER-SPACE TYPE ERROR

A critical type error was found in the newly written D2-A/D2-B record. The line
\[
0\ne\nu\in Q_4^*\cong H^1(G,\mathbf F_3)
\]
is false: in the fixed rank-four p=3 case, \(\dim Q_4^*=45\), whereas \(\dim H^1(G,\mathbf F_3)=4\). The variation parameter \(\nu\) in
\[
\rho_3'=\rho_3(1+9\nu)
\]
must lie in \(H^1(G,\mathbf F_3)\), not in \(Q_4^*\).

Thus the literal earlier D2 formula with \(\forall 0\ne\nu\in Q_4^*\) is **INVALID / TYPE ERROR**. The corrected load-bearing statement is the same existence-of-separating-output assertion with
\[
\forall\,0\ne\nu\in H^1(G,\mathbf F_3).
\]
For that corrected statement, the D2-A/D2-B proof remains valid: choose \(a\) by Demushkin cup nondegeneracy, lift \(a\) to \(f\), form \(\alpha_4=\nu_4\smile a_4\), and use functoriality to prove survival.

This correction does not affect the identification
\[
\ker(H^2(W_4)\to H^2(W_5))\cong Q_4^*;
\]
that is a separate output/kernel statement. It does mean that \(Q_4^*\) is the transient cohomological obstruction space, not the parameter space of coefficient-lift variations.

Classification:
- literal D2 statement with \(\nu\in Q_4^*\): **INVALID / CLOSED**;
- corrected D2-A finite representative for \(\nu\in H^1(G,\mathbf F_3)\): **PASS / CLOSED**;
- corrected D2-B W4 -> W5 survival: **PASS / CLOSED**;
- identification of \(Q_4^*\) as the one-step kernel: **PASS / CLOSED**;
- delta-family / \(Q_4^*\) direct intersection: **SUPERSEDED / NOT LOAD-BEARING**.


## 2026-09-28 — PAPER 3 D2 REPAIR CLOSED: TRANSGRESSION-QUOTIENT CARRIER

The false bare-Q_k H^2-inflation injectivity step is replaced by a finite extension/transgression quotient.

Let N_k=p^{k-1}, Q_k=W_{N_k+1}, E_k=W_{N_k+2}, and K_k=D_{N_k+1}/D_{N_k+2}. Since [D_i,G]⊂D_{i+1}, K_k is central in E_k and
\[
1\to K_k\to E_k\to Q_k\to1
\]
is an intrinsic finite central extension. Because K_k⊂Φ(E_k), H^1(Q_k,F_p)→H^1(E_k,F_p) is an isomorphism. The five-term sequence therefore gives
\[
\ker(H^2(Q_k,F_p)\to H^2(E_k,F_p))=\operatorname{im}(\operatorname{tra}_k).
\]
Define
\[
\mathcal O_k(G)=H^2(Q_k,F_p)/\operatorname{im}(\operatorname{tra}_k).
\]

This quotient, not H^2(Q_k) itself, is the corrected finite obstruction carrier. It is intrinsic to the finite extension E_k→Q_k and does not require identifying H^2(Q_k) with global H^2(G).

For the canonical lift, finite crossed-cocycle factorization plus global Kummerianity gives a finite lift, hence the finite connecting map is already zero in H^2(Q_k), and therefore in O_k. For any false lift rho_k'=rho_k(1+p^{k-1}nu), nu≠0 in H^1(G,F_p), Demushkin cup nondegeneracy and the audited reduction-surjectivity provide f with nonzero global variation nu cup fbar. Its finite representative alpha_k has nonzero inflation to H^2(G), so it cannot lie in im(tra_k), which is killed already in H^2(E_k). Thus its class in O_k is nonzero.

Therefore the induced finite connecting map
\[
\bar\delta_{k,rho_k}:H^1(Q_k,Z/p^{k-1}(rho_{k-1}))\to O_k(G)
\]
is identically zero exactly for the canonical lift, at the declared Demushkin scope, subject only to the already-audited arbitrary-candidate factorization and global variation/PD^2 inputs.

Classification:
- bare-Q_k H^2-inflation injectivity: **FAIL / CLOSED** permanently;
- stable-kernel continuity: **PASS / LOCAL**, no longer load-bearing;
- transgression-quotient carrier O_k: **PASS / CLOSED**;
- finite canonical zero map: **PASS / CLOSED**;
- false-lift finite separation in O_k: **PASS / CLOSED**;
- arbitrary-(p,d,q,k) D2 repair: **PASS / CLOSED** at the declared selector scope;
- D3 finite selector: **PASS / LOCAL -> promoted conditional on the audited D1/global inputs**;
- D4 sharp threshold: **PASS / LOCAL -> compatible with repaired selector**;
- absolute carrier minimality: **OPEN / NOT CLAIMED**;
- publication novelty: **OPEN / CONDITIONAL**.

The deeper-window search for a uniform stabilization bound is no longer required for recognition. The key shift is: recognition only needs the finite transient obstruction sector to be quotiented out, not full stable reconstruction of H^2(G).

Detailed proof: research/PAPER3_D2_TRANSGRESSION_QUOTIENT_CARRIER_RESULT_2026-09-28.md


## 2026-09-28 — D3 FINITE SELECTOR PROMOTED; D4 CATEGORY BOUNDARY FIXED

D3 is now **PASS / CLOSED** at the declared fixed rank-4, p=3, q=3 scope. The induction is: arbitrary-candidate factorization transfers K_k from Q_k to G; reduction/descent transfers it to level k-1; induction identifies rho_{k-1}=chi mod p^{k-1}; hence rho_k=chi_k(1+p^{k-1}nu) with nu in H^1(G,F_p). If nu != 0, the repaired D2 transgression-quotient separation produces a finite nonzero obstruction, contradicting K_k. Thus nu=0. Canonical Kummerianity gives existence.

**Critical dependency correction:** D2 does NOT require arbitrary-candidate surjectivity H^1(G,A_k(rho_k))->H^1(G,F_p). That would be circular because surjectivity is essentially the Kummer predicate. The required reduction-surjectivity is for the canonical lower-level module H^1(G,A_{k-1}(chi_{k-1})) -> H^1(G,F_p), supplied by classical Kummerianity of chi_G. This distinction is load-bearing and must remain explicit.

D4 is **PASS / CLOSED only in the affine crossed-cocycle representation category**: n_aff(k)=p^{k-1}+1 is sharp there by the already audited LTE witnesses, including rank-two. This does not prove minimality of the intrinsic Kummer selector window, nor absolute minimality of O_k.

q-status: selector is q-blind at the fixed project scope (q absent from selector input), but no uniform-in-q theorem is claimed. q-family uniformity and q-recovery remain separate/open.

Remaining frontiers: (1) absolute carrier minimality, after fixing a carrier category; (2) minimal selector window below P_{p^{k-1}+1}; (3) uniform-in-q recognition; (4) publication novelty audit.

Detailed record: research/PAPER3_D3_SELECTOR_PROMOTION_D4_BOUNDARY_2026-09-28.md


## 2026-09-28 — CARRIER MINIMALITY FORMALIZED AS A CATEGORY QUESTION

“Absolute minimality of O_k” is not yet a well-posed numerical problem. Without fixing the allowed carrier category, arbitrary recognition carriers can be nonlinear/Boolean and dimension is meaningless; even among linear quotients, minimum-dimension quotients need not be unique. The meaningful next target is a specified category of finite F_p-linear functorial carriers built from the canonical finite extension E_k→Q_k, and a universal quotient/factorization theorem for O_k.

Current classification: O_k is a sufficient canonical carrier PASS/CLOSED; absolute minimality NOT WELL-POSED until category fixed; linear quotient minimality OPEN; functorial universal minimality OPEN. Do not revive large 45-dimensional computations before this categorical target is fixed.

Detailed record: research/PAPER3_CARRIER_MINIMALITY_BOUNDARY_2026-09-28.md


## 2026-09-28 — GATE D GENERALIZATION CLOSED AFTER D2 TRANSGRESSION-QUOTIENT REPAIR

The Gate D generalization has now been re-derived with the corrected D2 carrier and independently checked against the earlier failure mode.

Scope:
- torsion-free Demuškin pro-p groups;
- odd prime p;
- even rank d>=2;
- q in {0,p,p^2,...};
- every k>=2.

The false statement
H^2(Q_k,F_p) -> H^2(G,F_p) injective
remains FAIL/CLOSED. It is not used anywhere in the corrected proof.

Instead:
Q_k=G/D_{p^{k-1}+1},
E_k=G/D_{p^{k-1}+2},
K_k=D_{p^{k-1}+1}/D_{p^{k-1}+2},
and
O_k=H^2(Q_k,F_p)/im(tra_k).

The proof is now:

1. D1: every candidate crossed cocycle factors through Q_k by the uniform odd-p affine semidirect filtration.
2. Canonical branch: global Kummerianity gives a global lift; D1 forces that lift to factor through Q_k, so the finite connecting map is zero directly. No H^2 inflation injectivity is needed.
3. False branch: rho_k'=chi_k(1+p^{k-1}nu), nu!=0. PD^2 cup nondegeneracy and canonical lower-level Kummerianity provide f with nonzero global variation nu cup fbar. Its finite representative alpha_k cannot lie in im(tra_k), because transgression classes die already in H^2(E_k), while alpha_k has nonzero global inflation. Hence [alpha_k] is nonzero in O_k.
4. D3 induction then gives uniqueness at every k.
5. D4 LTE gives the exact predecessor obstruction at D_{p^{k-1}}, hence the declared selector threshold p^{k-1}+1.

Critical non-circularity condition:
the proof uses only canonical lower-level reduction-surjectivity, not arbitrary-candidate Kummer surjectivity.

Classification:
- Gate D architecture: PASS/CLOSED;
- D1 arbitrary odd-p factorization: PASS/CLOSED;
- corrected D2 carrier: PASS/CLOSED;
- D3 arbitrary-k finite selector: PASS/CLOSED;
- D4 exact selector threshold: PASS/CLOSED;
- uniform-in-q within the declared torsion-free Demuškin class: PASS/CLOSED;
- arbitrary pro-p groups: NOT CLAIMED;
- absolute/functorial carrier minimality: OPEN;
- publication novelty: OPEN/CONDITIONAL.

Authoritative proof: research/PAPER3_GATE_D_GENERAL_ODD_P_RANK_Q_K_RESULT_2026-09-28.md, commit 99bbbeb2d6072b8f435ada806e08e48781f5d381.


## 2026-09-28 — CARRIER MINIMALITY CRITICAL CORRECTION

The first linear-carrier reduction was critically rechecked. The statement “minimum carrier dimension equals the span dimension of all false-lift outputs” was too strong: recognition only requires at least one surviving obstruction per false candidate, not preservation of every linear combination.

Correct formulation: for a quotient pi:O_k -> C, detection requires ker(pi) to avoid the actual obstruction set for every false candidate. The unrestricted linear problem is therefore a finite subspace-avoidance problem. The span S_k of all obstruction outputs gives an exact lower bound only in the stronger category that requires every nonzero vector of S_k to remain detectable.

Thus:
- corrected recognition-minimality formulation: PASS/CLOSED;
- D2 nonempty false-obstruction set: PASS/CLOSED;
- exact minimal dimension in the original quotient-recognition category: OPEN;
- span-complete minimality: OPEN;
- functorial minimality: OPEN.

No 45-dimensional recomputation is authorized yet. Next target is the intrinsic/functorial structure of the false-obstruction set.

Authoritative correction: research/PAPER3_CARRIER_SPAN_REDUCTION_2026-09-28.md, commit cc50379a53fc295a0e830537f7c35846d696d3d6.


## 2026-09-28 — CARRIER FRONTIER REFINED: GLOBAL SHADOW VS FINITE-PAIR CARRIER

The carrier-minimality attack produced a useful categorical split.

The transgression quotient O_k has a canonical global map
lambda_k: O_k -> H^2(G,F_p), because transgression classes die already in E_k and hence have zero global inflation. D2 proves every false-lift obstruction has nonzero image under lambda_k. Since Demushkin H^2 is one-dimensional, this gives a one-dimensional detector if global inflation is allowed.

Therefore absolute minimality of O_k is not a meaningful target: in a global category, a 1-dimensional detector already exists. The genuine Paper 3 problem is the finite-pair intrinsic category built only from E_k -> Q_k.

New load-bearing question:
Can lambda_k, or any equivalent nonzero functional on every false-obstruction set, be reconstructed functorially from the finite pair E_k -> Q_k alone?

If yes, the intrinsic carrier collapses to dimension 1. If no, the failure identifies the extra finite filtered-relation information that must be retained.

The 45-dimensional calculation remains deferred; it is relevant only if the finite-pair obstruction-set/module question cannot be resolved abstractly.

Authoritative analysis: research/PAPER3_CARRIER_SPAN_REDUCTION_2026-09-28.md, commit 9fbca468daaa0d2ef363e48524d766ad3b4fb610.


## 2026-09-28 — CRITICAL REVIEW: GLOBAL-SHADOW CLAIM NARROWED

A load-bearing overstatement in the carrier-minimality note was corrected. D2 proves that for every false candidate there exists at least one witness with nonzero global inflation; it does NOT prove that every finite obstruction output from every witness has nonzero global shadow.

Correct detector statement:
for every rho != chi_k, there exists f such that lambda_k(delta_{k,rho}(f)) != 0.
Thus lambda_k is still a 1-dimensional detector in the global category, but only at the existential-per-candidate level.

The finite-pair question remains OPEN: whether E_k -> Q_k canonically determines an equivalent nonzero functional on the witness family. Non-recoverability is NOT claimed.

Authoritative correction: research/PAPER3_CARRIER_SPAN_REDUCTION_2026-09-28.md, commit 948ad02cff8d2c9dfa226b7fbaba17055b9d46f0.


## 2026-09-28 — PAPER 3 MIDPOINT CHECKPOINT / RECOGNITION CLOSED, CARRIER COMPRESSION FRONTIER

A formal midpoint checkpoint was recorded in `research/PAPER3_MIDPOINT_SUMMARY_2026-09-28.md`.

The large-scale state is now frozen as follows:
- D1 finite factorization through Q_k: PASS/CLOSED at the declared torsion-free Demushkin scope;
- corrected D2 transgression-quotient separation: PASS/CLOSED;
- D3 finite Kummer selector: PASS/CLOSED;
- D4 affine depth p^{k-1}+1: PASS/CLOSED in the declared affine category;
- bare-Q_k H^2 inflation injectivity: FAIL/CLOSED;
- absolute carrier minimality: OPEN and category-dependent;
- finite-pair intrinsic 1D reconstruction from E_k -> Q_k: OPEN/LOAD-BEARING.

The correct global detector is existential per false candidate:
for every rho != chi_k there exists f with lambda_k(delta_{k,rho}(f)) != 0. No claim is made that every finite obstruction output survives globally.

Next authorized attack is abstract finite-pair reconstruction. The 45-dimensional rank-4 p=3 calculation remains deferred unless the abstract route cannot decide the question.

Authoritative midpoint note: research/PAPER3_MIDPOINT_SUMMARY_2026-09-28.md.


## 2026-09-28 — PAPER 3 MIDPOINT CHECKPOINT / RECOGNITION CLOSED, CARRIER COMPRESSION FRONTIER

Formal midpoint checkpoint: `research/PAPER3_MIDPOINT_SUMMARY_2026-09-28.md`.

- D1 finite factorization: PASS/CLOSED at the declared torsion-free Demushkin scope.
- Corrected D2 transgression-quotient separation: PASS/CLOSED.
- D3 finite Kummer selector: PASS/CLOSED.
- D4 affine depth p^{k-1}+1: PASS/CLOSED in the declared affine category.
- Bare-Q_k H^2 inflation injectivity: FAIL/CLOSED.
- Global one-dimensional detector: PASS/CLOSED, existential per false candidate.
- Finite-pair intrinsic one-dimensional reconstruction from E_k -> Q_k: OPEN/LOAD-BEARING.
- Absolute/functorial carrier minimality: OPEN.
- 45-dimensional rank-4 p=3 calculation: DEFERRED.
- Publication novelty: OPEN/CONDITIONAL.

Next authorized attack: determine whether the finite central extension E_k -> Q_k canonically yields an equivalent nonzero functional on the D2 witness family. No non-recoverability claim is made.


## 2026-09-28 — PAPER 3 FINITE CUP-LINE COMPRESSION / 1D SELECTOR CARRIER CLOSED

The abstract finite-pair functional reconstruction was attacked directly. A stronger recognition-level compression is available.

For
\[
Q_k=G/D_{p^{k-1}+1},
\]
define the intrinsic cup-product image
\[
C_k=\operatorname{im}\bigl(H^1(Q_k,\mathbf F_p)^{\otimes2}\xrightarrow{\cup}H^2(Q_k,\mathbf F_p)\bigr).
\]

Because the quotient kernel lies in \(D_3\) for odd \(p\), the quadratic initial relation is unchanged from the Demuškin group. Standard relation/cup duality therefore gives
\[
\dim_{\mathbf F_p}C_k=1.
\]

On the canonical lower-level branch,
\[
\rho_k=\chi_k(1+p^{k-1}\nu),
\]
and the audited variation formula gives
\[
\delta_{k,\rho_k}(f)-\delta_{k,\chi_k}(f)=\nu\smile\bar f.
\]
Since the canonical connecting map is zero, every false-branch finite obstruction output lies in \(C_k\). D2 supplies, for every \(\nu\ne0\), at least one witness with nonzero global inflation; hence that witness is nonzero already in \(C_k\).

Therefore the finite selector can be compressed to the one-dimensional intrinsic target \(C_k\):
\[
\delta^\cup_{k,\rho_k}:H^1(Q_k,A_{k-1}(\rho_{k-1}))\to C_k,
\]
with
\[
\delta^\cup_{k,\rho_k}=0
\iff
\rho_k=\chi_k
\]
after the closed lower-level induction step.

This yields a genuine minimality statement in the newly specified linear selector-carrier category: dimension 0 cannot recognize a false candidate, while \(C_k\) has dimension 1.

Important distinction:
- the stronger projection/functional \(O_k\to\mathbf F_p\) reconstructed solely from \(E_k\to Q_k\) remains OPEN;
- it is no longer load-bearing for recognition;
- \(O_k\) is retained as the proof carrier used by D2 to establish survival against the transient transgression sector;
- the final recognition carrier is the intrinsic one-dimensional cup line.

Authoritative detailed record: research/PAPER3_FINITE_CUP_LINE_COMPRESSION_2026-09-28.md, commit 3daed93e34cb872ea7008a3ddb34d2b62778857e.


## 2026-09-28 — CRITICAL REVIEW: 1D CUP-LINE COMPRESSION CLAIM DOWNGRADED

A substantive error was found in the newly proposed finite cup-line compression.

The claim
\[
\dim C_k=1,\qquad
C_k=\operatorname{im}(H^1(Q_k,\mathbf F_p)^{\otimes2}\to H^2(Q_k,\mathbf F_p))
\]
does not follow merely from the fact that the Demuškin cup image in \(H^2(G,\mathbf F_p)\) is one-dimensional.

Naturality proves only that
\[
C_k\to H^2(G,\mathbf F_p)
\]
has one-dimensional image. The finite map may have a nontrivial kernel. The assertion that the degree-two initial relation is unchanged modulo \(D_3\) is a graded statement and does not by itself eliminate higher finite \(H^2\) cup-product classes that inflate trivially.

Accordingly:
- finite cup-line dimension 1: OPEN;
- embedding \(C_k\hookrightarrow O_k\): OPEN;
- 1D finite selector carrier: OPEN;
- minimality = 1: OPEN;
- D2's cup-product variation identity and existential false-candidate separation remain valid;
- D1/D2/D3/D4 remain unaffected.

New load-bearing target:
\[
\ker(C_k\to H^2(G,\mathbf F_p)).
\]
Either prove this kernel is zero for the actual \(Q_k\), or characterize it intrinsically. Do not claim one-dimensional finite compression until this is settled.

Authoritative correction is appended to the finite cup-line compression record, commit f99a4b38de1bd5becb8b4f3d8307b628708745ef.


## 2026-09-28 — PAPER 3 FINITE CUP-LINE KERNEL CLOSED

The active kernel question for C_k = im(H^1(Q_k,F_p)^{⊗2} -> H^2(Q_k,F_p)) is now resolved abstractly.

For a minimal free pro-p presentation G=F/R, Q_k=G/D_{p^{k-1}+1}=F/R_k with R_k=R D_{p^{k-1}+1}(F). Because p is odd and p^{k-1}+1>=3, the added quotient relators lie in D_3(F). Hence the image of R_k in D_2(F)/D_3(F) is exactly the one-dimensional span of the Demushkin relator's nonzero quadratic initial form.

Standard relation-module/cup-product duality identifies the dual of the finite cup map with this degree-two initial-form map. Therefore dim_Fp C_k=1. This is the missing proof: it does not use finite-to-global H^2 injectivity. The resulting nonzero one-dimensional C_k -> H^2(G) is therefore injective.

Consequences:
- ker(C_k -> H^2(G))=0: PASS/CLOSED;
- C_k embeds in O_k: PASS/CLOSED;
- every D2 false-branch witness lies in the intrinsic one-dimensional cup line, and every false candidate has a nonzero such witness: PASS/CLOSED;
- 1D intrinsic finite selector carrier: PASS/CLOSED;
- linear selector-carrier minimality = 1: PASS/CLOSED;
- 45-dimensional calculation: DEFERRED / NOT REQUIRED;
- stronger canonical functional O_k -> F_p determined from E_k -> Q_k alone: OPEN / NOT LOAD-BEARING.

Primary detailed proof: research/PAPER3_FINITE_CUP_LINE_COMPRESSION_2026-09-28.md, commit c5aa630f7b49eca16ac7696c0989c9a6da1df7eb. The relation/cup compatibility is standard and documented in the cited literature audit.


## 2026-09-28 — PAPER 3 REFEREE GAP CLOSURE: FREE-PRODUCT TWISTED-H1

The load-bearing referee objection in the application manuscript has been repaired and independently rechecked at the proof-structure level.

- Candidate-dependent coefficient module is now explicit: M_rho=Z/p^k(rho), with M_rho_i the restriction to G_i.
- The degree-one free-product decomposition is stated together with the natural commutative coefficient-reduction diagram.
- For N=P_{p^{k-1}+1}(G), the factor intersection N cap G_i=P_{p^{k-1}+1}(G_i) is justified by functoriality plus the canonical retraction G to G_i.
- Paper 2 arbitrary-candidate factorization therefore transports the finite twisted H^1 problem to the free factors, and the global Kummer predicate is exactly the direct sum of the factor predicates.
- The truncation/coproduct lemma was rewritten with an explicit universal-property proof.
- The selected-depth abelianization calculation was tightened to D_{p^{k-1}+1}(D_{f,d}^{ab})=p^k Z_p^{d-1} plus zero torsion component.
- Scope wording corrected: Paper 1 recognition is rank-four q=3, while heterogeneous f_i is used only for the broader affine application.

Classification:
- free-product twisted-H^1 gap: PASS / CLOSED
- truncation lemma: PASS / CLOSED
- parameter-collapse wording/proof: PASS / CLOSED
- scope consistency: PASS / CLOSED
- publication novelty: OPEN / CONDITIONAL

Detailed closure record: research/PAPER3_REFEREE_GAP_CLOSURE_2026-09-28.md.

Build: commit f97b9f04dd873fd2d0123d325443032c4840d086 triggered Paper 3 CI run 36361479679; at record time it was queued, so compilation is not yet classified.


## 2026-09-28 — FINAL D1/D2 SOURCE AUDIT: STALE FORMULAS CORRECTED

The final line-by-line attack found two stale formulas in general Gate D documentation and corrected them before finalization.

- D1: the Zassenhaus filtration is logarithmic in n; the false shorthand P_j(S_k)=T_j for every integer j was replaced by P_n(S_k)=p^{ceil(log_p n)}A_k semidirect U_{ceil(log_p n)+1}. The endpoint P_{p^{k-1}+1}=1 and nontrivial predecessor remain unchanged.
- D2: the transgression-carrier variation identity has common target H^2(G,F_p), so the correct formula is directly delta_{rho'}-delta_{chi}=nu cup f-bar. The auxiliary iota formulation is not used in this typed statement.

Classification:
- D1 endpoint/factorization: PASS / CLOSED after correction;
- D2 variation target typing: PASS / CLOSED after correction;
- stale historical formulas: HISTORICAL / SUPERSEDED;
- no new selector counterexample found.

The final proof audit therefore closes the previously authorized D1/D2 source-level attack. The remaining blocker is compilation plus final manuscript/novelty positioning, not a new mathematical branch.


## 2026-09-28 — FINAL PAPER 3 CI BUILD / PDF VERIFIED

The final manuscript source at commit f97b9f04dd873fd2d0123d325443032c4840d086 was compiled by GitHub Actions workflow **Build Paper 3**, run **36361479679**.

- LaTeX compilation: **PASS / CLOSED**
- PDF verification step: **PASS / CLOSED**
- Artifact: `paper3-pdf` (artifact 10946385056)
- PDF: 10 pages, 370,375 bytes
- SHA-256: `adf76e22672184f5c022bc268bfcdc932cb575b5151b0adca215293dcab132ba`
- No LaTeX error/undefined-reference/warning failure was reported by the workflow verification step.

This build is the manuscript corresponding to the repaired free-product twisted-H^1 proof and corrected scope. Subsequent commits after f97b9f04dd873fd2d0123d325443032c4840d086 only update research/audit records; they do not alter `paper3/main.tex`. Therefore this artifact is the current final manuscript PDF.

Publication novelty remains **OPEN / CONDITIONAL**; no priority claim is made.


## 2026-09-28 — AUTHORITATIVE PAPER 3 SYNCHRONIZATION STATUS

The research frontier and the publication artifact are now treated as separate states with an explicit synchronization gate.

Current mathematical frontier: D1/D2/D3/D4, one-dimensional cup carrier, and category-relative selector minimality are PASS/CLOSED according to the research audit.

Current manuscript/PDF status: **OPEN / LOAD-BEARING**, not yet final. The first attempted synchronization commit `a334cefff5fe90c15cfe86984d2dc3331d6c4838` failed LaTeX compilation, so no PDF from that run is authoritative.

FINAL requires all of:
- research state checked against authoritative files;
- manuscript manifest complete;
- main.tex contains every load-bearing result and no superseded conclusion;
- independent CI LaTeX compile PASS;
- PDF content verification PASS;
- generated artifact tied to the exact commit SHA and checksum;
- immediate research-log entry recording the final artifact identity.
