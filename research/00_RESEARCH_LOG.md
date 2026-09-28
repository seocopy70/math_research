## 2026-09-28 — THREE-PAPER AUTHORITATIVE REVISION CHECKLIST EXECUTION

The supplied revision checklist was treated as the authoritative edit list for Paper 1/2/3. No direct edits were made to the previously frozen main-branch artifacts.

Paper 1:
- Revision branch: `paper1-fixes-2026-09-28`.
- The all-(f) lower-bound witness was consolidated into one proposition, and the category-relative minimality/free-product statements were repaired.
- Literature-boundary wording was kept conditional; Mináč–Tân–Trà arXiv:2510.20133 was added as surrounding Zassenhaus literature.
- CI compile: PASS (PDF produced, 8 pages).
- Repository verify step: FAIL only because the workflow's warning-grep rejects unresolved citation warnings in the LaTeX log; no LaTeX compilation error occurred. Therefore Paper 1 artifact gate is OPEN/PENDING citation-hygiene cleanup and re-verification.

Paper 2:
- Revision branch: `paper2-fixes-clean-2026-09-28`.
- U4 was explicitly labeled as the base-level identification proposition.
- U5c was rewritten with the finite-coefficient (PD^2) duality direction and the dual reduction map (A_{k-1}	woheadrightarrowmathbf F_3).
- arXiv:1412.7685 was identified explicitly in the literature boundary/bibliography.
- Clean CI validation branch: `paper2-ci-clean-2026-09-28`, run **36398580257**: PASS.
- No PDF/artifact closure is claimed yet beyond successful clean compilation; exact-source/PDF/hash gate remains pending.

Paper 3:
- Revision branch: `paper3-fixes-2026-09-28`.
- U5c and literature-audit wording were updated within the supplied checklist scope.
- CI runs on the revision branch completed successfully; exact final artifact closure still requires the independent PDF/content/hash gate.

Important process note:
- Several early Paper 2 patch attempts were deliberately discarded after CI exposed malformed section boundaries. The clean Paper 2 branch was rebuilt from the authoritative base commit rather than repairing a corrupted intermediate.
- No failed intermediate branch is authoritative.
- Current classification: Paper 1 OPEN/PENDING citation-hygiene verification; Paper 2 PASS/LOCAL (clean compilation, artifact gate pending); Paper 3 PASS/LOCAL (CI compile/build success, exact artifact gate pending).
- Publication novelty remains OPEN/CONDITIONAL.

## 2026-09-28 — PAPER 3 REFEREE DETAIL REPAIR / ARTIFACT GATE REOPENED

A new adversarial manuscript review raised M1–M10. The source was checked against the authoritative research state and primary literature before editing.

Result:
- M1 D3 relation-module image chain: PASS/CLOSED after explicit R_k -> P_2/P_3 chain.
- M2 D4 shallow range: PASS/CLOSED; existing valuation chain is correct.
- M3 D4 middle range: PASS/CLOSED after explicit x_2^N in G^N subseteq P_N subseteq P_m chain.
- M4 D2 transgression: PASS/CLOSED after explicit P_{N_k+1} subseteq P_2=Phi(G), hence K_k subseteq Phi(E_k).
- M5 C_k typing: PASS/CLOSED; finite cup image and coefficient-extension target are explicitly separated.
- M6 Labute Theorem 4: PASS/CLOSED; primary-source check confirms the existence/uniqueness plus Proposition-6 crossed-homomorphism criterion attribution.
- M7 alleged U3 d inconsistency: FAIL/CLOSED as an objection; r in Phi(F) implies H/Phi(H) ~= F/Phi(F), so rank(F)=dim H^1(H,F_3)=d.
- M8 Fox coefficients: PASS/CLOSED after adding a cochain-level derivation appendix.
- M9 G^{3^e}: PASS/CLOSED after defining the power subgroup and stating G^{3^e} subseteq P_{3^e}.
- M10 Appendix A formatting: PASS/CLOSED.

Source repair commit: f686fef1bfbab0b566d2cd424aa097955a2c61ec.
Detailed audit: research/PAPER3_REFEREE_DETAIL_REPAIR_2026-09-28.md.

Artifact gate is explicitly reopened because the source changed. The next authorized sequence is exact-source CI -> independent PDF/content audit -> checksum/package verification -> final manifest update. No prior PDF is authoritative after this source change.

## 2026-09-28 — MANUSCRIPT SOURCE CLEANUP CORRECTION

The first cleanup commit accidentally introduced repeated-character typos while replacing the reviewer-noted “ogether” typo. This was caught immediately by source inspection and corrected.

- Corrected manuscript commit: `dc73b0365be4020545e73ec768dbea5fed889b0e`.
- `ttogether` / `Ttogether` contamination: **REMOVED**.
- Recognition theorem label, D2 \(\mathcal O_k\) section, U2/U3 repairs, D3 Proposition 7.1 citation, and D4 corrections remain present.
- CI/PDF verification remains **PENDING** for the corrected source.

No mathematical status changes.

## 2026-09-28 — PAPER 3 REFEREE GAP CLOSURE / MANUSCRIPT RESYNCHRONIZATION

The adversarial manuscript review exposed real source-level gaps despite the prior publication artifact closure. The mathematical research frontier was already closed at the relevant scopes, but the manuscript had not faithfully synchronized several load-bearing proof details. This is classified as a **MANUSCRIPT SYNCHRONIZATION DEFECT**, not a reopening of the mathematics.

Corrected in `paper/main.tex`:
- U2 now explicitly states the coefficient-triviality/inflation chain: \(\rho\equiv1\pmod3\), \(P_{3^{k-1}+1}\subseteq P_2=\Phi\), and the kernel acts trivially on \(A_k(\rho)\).
- U3 now states the minimal one-relator hypothesis explicitly, including the free rank \(d=\dim H^1(H,\mathbf F_3)\) and \(r\in\Phi(F)\).
- The finite transgression quotient \(\mathcal O_k=H^2(Q_k,\mathbf F_3)/\operatorname{im}(\operatorname{tra}_k)\) is now included as the D2 proof carrier, while explicitly not claiming it is the final minimal carrier.
- The finite cup-line proof now cites Mináč–Pasini–Quadrelli–Tân, Proposition 7.1 at the actual relation-module/cup pairing step and explains why the added \(P_n(F)\subseteq P_3(F)\) relators contribute no quadratic initial form.
- The selector lower bound for \(m\le3^{k-2}\) now gives the direct valuation calculation showing \(\chi_G\) does not factor through \(W_m\).
- The LTE argument now correctly records \(v_3(u-1)=1\) and derives \(v_3(S_N(u))=k-1\).
- The recognition theorem is given an explicit LaTeX label for cross-reference, and manuscript typos were cleaned.
- The literature boundary now includes \(\mathcal O_k\) as a proof carrier while retaining the conditional novelty wording.

Independent source check:
- Mináč–Pasini–Quadrelli–Tân, Proposition 7.1 was verified directly from the published article: it gives the commutative pairing diagram relating the relation initial-form map to cup-product evaluation. This supports the manuscript's rank-one finite cup-line argument under the stated minimal-presentation hypotheses.
- Labute Theorem 4 was independently checked for existence/uniqueness of the canonical orientation and the value \(\chi(x_2)=(1-q)^{-1}\) in the odd-\(p\) normal form.

Classification:
- mathematical D2/D3/D4 status: **UNCHANGED / PASS-CLOSED at declared scopes**;
- manuscript synchronization: **REPAIR COMMITTED**;
- prior “final artifact” state: **SUPERSEDED by this source revision**;
- CI/PDF verification of commit `7adb6fe8ab43dd924daf282730c0c316757a892a`: **PENDING**;
- publication novelty: **OPEN / CONDITIONAL**.

Next authorized action: independent CI compilation, PDF text/content audit, artifact hash capture, then update the manuscript manifest and final state only after those gates pass.

## 2026-09-28 — FINAL PAPER 3 ARTIFACT / MANUSCRIPT SYNCHRONIZATION CLOSED

The manuscript synchronization gate required after the stale-PDF incident is now fully closed.

Authoritative final source: \`paper/main.tex\`.

Completed checks:
- source line-by-line audit and structural reordering;
- compile-failure diagnosis: unmatched closing math delimiter in U5a;
- repair and successful clean LaTeX compilation;
- Build Paper PDF CI run **36363508628**: PASS/CLOSED;
- workflow shell audit run **36363508467**: PASS/CLOSED;
- citation hygiene run **36363508580**: PASS/CLOSED;
- independent extraction/content audit of the CI PDF: PASS/CLOSED;
- exact artifact checksum capture.

Final artifact:
- PDF artifact ID: **10946925073**
- full submission artifact ID: **10945849160**
- PDF SHA-256: \`813fda4840783c3b37002828ccfbe092ccffed6ad189f46430222e5e930a56b0\`
- source package SHA-256: \`759476d1003fe2d106cfeae5d82f12f8d866afabfddbdd4a3d063cc0d90e7af0\`
- PDF size/pages: **405,622 bytes / 14 pages**
- CI validation commit: \`3acf4d551f66b21df7ed0528164ef76c690cbc13\`
- main-branch manuscript blob: \`c82e6c5277dd7aa21d3bc4ab9d5490d25cf6c694\`

A separate CI audit also found citation-artifact Unicode/tokens in three Paper 3 research notes; these were cleaned, and citation hygiene subsequently passed. This is a repository hygiene correction, not a mathematical change.

The final manuscript now explicitly reflects the closed research frontier: finite-window recognition, U5 uniqueness, intrinsic 1D cup-line carrier, and fixed rank-4 \(q=3\) selector minimality. The stronger finite-pair functional reconstruction remains OPEN/NOT LOAD-BEARING. Publication novelty remains OPEN/CONDITIONAL.

The temporary validation PR #5 was closed without merge after successful validation.

Classification:
- manuscript synchronization: **PASS / CLOSED**
- final PDF artifact: **PASS / CLOSED**
- publication novelty: **OPEN / CONDITIONAL**


## 2026-09-27 — M2 POST-BLUMER–QUADRELLI F1 SHARPNESS AUDIT CLOSED

A targeted post-publication literature audit was completed before computation. Marina Palaisti, arXiv:2609.00253 (submitted 2026-08-31), is explicitly an F2 two-relator paper: it studies the added commuting relator, develops support-block reductions, and proves a five-fold vanishing theorem for the full-interior-support case while reducing remaining support types. It does not treat the F1 one-relator family or prove sharpness/failure for F1 at n>q. Targeted searches for F1 + n>q + Massey/Demuškin likewise found no exact converse or obstruction.

The F2 result is therefore a methodological comparison, not prior art resolving F1. Its one-relator reduction relies on the extra commuting relator/second central defect; no transfer to F1 is assumed.

Classification:
- M2 post-Blumer–Quadrelli prior-art audit: **PASS / CLOSED** (audited negative; not an absolute claim about unindexed/unpublished work).
- F1 proof-mechanism breakpoint at n=q+1: **PASS / CLOSED** from independent hand calculation.
- Actual F1 sharpness/failure at n=q+1: **OPEN / LOAD-BEARING**.
- M3 finite-window recognition: **NOT YET AUTHORIZED**.

Next authorized action: smallest M1 computation (p,q,d,n)=(3,3,2,4), U_5(F_3), with exact admissibility/cup-vanishing/Dwyer-lift conditions and independent verification.

Detailed audit: research/M2_POST_BQ_F1_SHARPNESS_LITERATURE_AUDIT_2026-09-27.md

## 2026-09-27 — PAPER 3 M-GATE: BLUMER–QUADRELLI F1 MASSEY SHARPNESS

The uploaded arXiv-2603.15464v2 source was independently unpacked and checked against the current Paper 3 target discussion.

Verified from the actual source:
- Proposition (2.a): for G in F1 and n <= q, G satisfies a strong variant of n-fold Massey vanishing.
- Example 2(a): ordinary Demuškin groups satisfy strong n-fold Massey vanishing for every n >= 3, with Blumer–Quadrelli citing Pál–Szabó, Theorem 3.5 (arXiv:1811.06192). The earlier Mináč–Tân attribution is corrected.
- For G in F1, the associated graded restricted Lie algebra is explicitly presented by <X1,Y1,...,Xd,Yd | [X2,Y2]+...+[Xd,Yd]=0>, so the F1 branch is structurally compatible with the existing Zassenhaus/initial-form/Magnus-Fox toolkit.