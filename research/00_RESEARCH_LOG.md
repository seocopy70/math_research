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

Logical correction:
- “Demuškin triple-Massey vanishing” as a target in the fixed Demuškin category is FAIL / CLOSED because the target is constant there.
- The F1 proposition supplies a genuine parameter-dependent sufficient bound n <= q.
- Blumer–Quadrelli do not prove the converse n > q => failure of strong n-fold Massey vanishing. Therefore sharpness is OPEN and is a legitimate M-Gate candidate, subject to a post-publication literature audit.

Paper 3 M-Gate:
M0 category = F1 or minimal enlargement: OPEN.
M1 sharpness of n <= q: OPEN / LOAD-BEARING.
M2 post-Blumer–Quadrelli/Pál–Szabó/Pál–Quick prior-art audit: OPEN / MANDATORY BEFORE COMPUTATION.
M3 finite Zassenhaus recognition threshold: NOT AUTHORIZED until M1/M2.
M4 generalization to p,d,q,n and larger mild/multi-relator classes: DEFERRED.

Smallest proposed stress test, only after M2:
d=2, q=p, n=p+1.

The branch is promoted only if it yields more than a one-off calculation, ideally a clean threshold/structural theorem depending on p,d,q,n and with a mechanism surviving at least one category enlargement.

Detailed audit:
research/PAPER3_F1_MASSEY_SHARPNESS_GATE_2026-09-27.md

Classification:
- fixed Demuškin triple-Massey target: FAIL / CLOSED
- F1 sufficient bound n <= q: PASS / CLOSED (verified literature fact)
- sharpness: OPEN / LOAD-BEARING
- post-publication prior-art audit: OPEN / MANDATORY
- finite-window Massey recognition threshold: OPEN / NOT YET AUTHORIZED
- general threshold theorem: OPEN / CONDITIONAL


## 2026-09-26 — EXTENDED SHARP FINITE-WINDOW DRAFT: CRITICAL AUDIT

The uploaded `sharp_finite_window.tex` was attacked as a proposed successor paper.

A fatal manuscript-level mathematical error was found in the left crossed-cocycle commutator formula. With (z(gh)=z(g)+\rho(g)z(h)) and ([a,b]=a^{-1}b^{-1}ab), the correct identity is
[
z([a,b])=\rho(a)^{-1}\rho(b)^{-1}\bigl((1-\rho(b))z(a)+(\rho(a)-1)z(b)\bigr).
]
The draft omits the prefactor. This propagates into the explicit Fox coefficients and the all-(k) selector.

For the stated normal form (r=x_1^{p^f}[x_1,x_2]\cdots), the corrected zero condition gives
[
\rho(x_2)=(1-p^f)^{-1}\pmod{p^k},
]
the known canonical orientation value, not (1+p^f). The discrepancy first appears at (k=3): for (p=3,f=1), the draft gives (4\pmod{27}), while the canonical value is (13\pmod{27}). Thus the current main theorem/abstract are **FAIL/CLOSED as written** for (k\ge3).

A second independent issue: the draft's "sharp window" theorem proves a universal affine-representation factorization threshold, not recognition minimality among all intrinsic predicates/carriers. The latter remains **OPEN**, consistent with the authoritative research state.

A further flaw in the sharpness proof is that it claims the canonical (chi\bmod p^k) is surjective onto (U_{1,k}) for all (f). This is false for (f\ge k), where (chi\bmod p^k) is trivial.

The Newton algorithm and q-recovery sections inherit the corrected orientation equation and also require a precise distinction between abstract-(Q_k), marked-(Q_k), and normal-form presentation input models.

Detailed audit:
`research/EXTENDED_SHARP_FINITE_WINDOW_CRITICAL_AUDIT_2026-09-26.md`.

Classification:
- crossed-cocycle formula: **FAIL/CLOSED**
- all-k selector as currently written: **FAIL/CLOSED**
- corrected finite-window factorization mechanism: **PASS/CONDITIONAL**
- recognition minimality: **OPEN**
- q-collapse classification: **PASS/LOCAL**
- Newton algorithm: **OPEN/CONDITIONAL**
- publication novelty: **OPEN/CONDITIONAL**

No closed branch is revived. Required next step is repair of the cocycle/Fox equations before any further extension scan.

# 2026-09-25 — EXACT 962be77 BUILD ATTACK: U3 LATEX SYNTAX DEFECT FOUND AND FIXED

## Pre-check

The authoritative state required the exact manuscript commit
`962be77ed62040ed5707e3c59c54de6585a0086d` to be checked out and compiled before
publication preparation could proceed. The source-level U1-U5/theorem audit had already
passed; this was a build-verification gate, not authorization for another mathematical
branch.

## Execution

A disposable GitHub Actions audit checked out exactly `962be77`. The first attempt
failed before compilation because the runner lacked TeX packages. A second audit installed
`texlive-latex-extra` and `poppler-utils`, then reproduced the failure in the first
`pdflatex` pass.

The actual error was:

```
! LaTeX Error: Command \\end{equation*} invalid in math mode.
l.149 \\end{proposition}
! ==> Fatal error occurred, no output PDF file produced!
```

Inspection of the exact source showed the U3 proposition contained an opened display
`\\[` with no matching `\\]` before `\\end{proposition}`. The defect is purely
syntactic. It does not alter any mathematical statement, hypothesis, proof, or reference.

## Correction

The missing `\\]` was inserted immediately before `\\end{proposition}` in
`paper/main.tex`. Corrected main-branch commit:
`058955142df5f831ec09d2b5e46461b0424e65e6`.

The same one-line correction was independently tested first on a disposable branch before
being applied to main.

## Independent verification

GitHub Actions run `36145439668` built the corrected source with TeX dependencies and
performed three `pdflatex` passes.

Result:
- three-pass build: **PASS**
- final-pass warning/error audit: **clean**
- PDF: **10 pages**
- PDF size: **284649 bytes**
- PDF SHA-256:
  `8056c70a42fdf6f32534bf4dc843c6264cc9bb1bdb282ade705c33f9fe64567f`
- uploaded artifact: `fixed-u3-pdf`

The generated PDF was extracted and independently inspected for the final-pass
warning/error condition; no `Undefined`, `LaTeX Warning`, `LaTeX Error`,
`Fatal error`, `Emergency stop`, or `!` matches occurred in build3.log.

## Classification

- exact `962be77` source identity: **PASS / CLOSED**
- exact `962be77` clean build: **FAIL / CLOSED** — manuscript syntax defect
- corrected source build: **PASS / CLOSED**
- mathematical theorem/U1-U5 status: **UNCHANGED**
- novelty: **OPEN / CONDITIONAL**
- Zassenhaus-window minimality: **OPEN**

## Logical boundary

This finding must not be described as a mathematical failure of U3. The U3 proof content
was unchanged. It is a publication-source defect caught by the final build gate.

## Next action

No new mathematical computation is authorized from this event. Proceed to final PDF review,
citation/source consistency review, and publication preparation.

## 2026-09-24 — U5 INTRINSIC UNIQUENESS CLOSED / FINITE-WINDOW SELECTOR THEOREM

The two load-bearing U5 lemmas are now proved intrinsically.

**Variation lemma.** If two level-\(k\) candidate characters reducing to \(\rho_{k-1}\) differ by \(1+3^{k-1}\nu\), \(\nu\in H^1(G,\mathbf F_3)\), then the corresponding coefficient-extension connecting maps satisfy
\[
\delta_{\rho_k'}-\delta_{\rho_k}
=
\iota_{k-1}\circ(\nu\smile-).
\]
This is a Yoneda/coefficient-extension naturality statement and is independent of presentation, Fox coordinates, \(q\), and the choice of \(H^2\)-generator.

**PD² socle-injectivity lemma.** On the canonical induction branch \(\rho_{k-1}=\chi\bmod3^{k-1}\), the socle inclusion
\[
\iota_{k-1}:\mathbf F_3\hookrightarrow \mathbf Z/3^{k-1}(\chi_{k-1})
\]
induces an injection on \(H^2\). PD² duality identifies the dual map with the reduction of invariant sections of the untwisted dual coefficient module, which is surjective.

Hence if two candidate characters both satisfy the global finite Kummer predicate, their connecting maps vanish identically; the variation formula and injectivity imply \(\nu\smile v=0\) for every \(v\in H^1(G,\mathbf F_3)\). Demuškin cup nondegeneracy gives \(\nu=0\). Induction from the established \(k=2\) base case proves intrinsic uniqueness at every \(k\).

Together with U1-U2, which give finite-depth factorization through \(Q_k=G/P_{k+1}\), and the known existence of the canonical Kummerian orientation, this yields
\[
\boxed{\mathsf K_k(Q_k,\rho)\Longleftrightarrow \rho=\chi_G\bmod3^k}
\]
for every \(k\ge2\).

Classification:
- U5 variation lemma: **PASS / CLOSED**
- U5 PD² socle-injectivity: **PASS / CLOSED**
- U5 intrinsic uniqueness: **PASS / CLOSED**
- N4 finite-window factorization: **PASS / CLOSED**
- N5 q-blind finite selector theorem: **PASS / CLOSED**
- overall novelty: **OPEN / CONDITIONAL**

No Fox computation was reopened. The remaining task is the final literature novelty comparison: determine whether this exact bare-\(Q_k\), q-blind selector/factorization statement is an immediate corollary or equivalent reformulation of an existing theorem.

Record: \`research/U5_INTRINSIC_FINITE_SELECTOR_AUDIT_2026-09-24.md\`.

## 2026-09-24 — U5 INTRINSIC UNIQUENESS CLOSED / FINITE-WINDOW SELECTOR THEOREM

The two load-bearing U5 lemmas are now proved intrinsically.

**Variation lemma.** If two level-(k) candidate characters reducing to (
ho_{k-1}) differ by (1+3^{k-1}
u), (
uin H^1(G,mathbf F_3)), then the corresponding coefficient-extension connecting maps satisfy
[
delta_{
ho_k'}-delta_{
ho_k}
=
iota_{k-1}circ(
usmile-).
]
This is a Yoneda/coefficient-extension naturality statement and is independent of presentation, Fox coordinates, (q), and the choice of (H^2)-generator.

**PD² socle-injectivity lemma.** On the canonical induction branch (
ho_{k-1}=chimod3^{k-1}), the socle inclusion
[
iota_{k-1}:mathbf F_3hookrightarrow mathbf Z/3^{k-1}(chi_{k-1})
]
induces an injection on (H^2). PD² duality identifies the dual map with the reduction of invariant sections of the untwisted dual coefficient module, which is surjective.

Hence if two candidate characters both satisfy the global finite Kummer predicate, their connecting maps vanish identically; the variation formula and injectivity imply (
usmile v=0) for every (vin H^1(G,mathbf F_3)). Demuškin cup nondegeneracy gives (
u=0). Induction from the established (k=2) base case proves intrinsic uniqueness at every (k).

Together with U1-U2, which give finite-depth factorization through (Q_k=G/P_{k+1}), and the known existence of the canonical Kummerian orientation, this yields
[
oxed{mathsf K_k(Q_k,
ho)Longleftrightarrow 
ho=chi_Gmod3^k}
]
for every (kge2).

Classification:
- U5 variation lemma: **PASS / CLOSED**
- U5 PD² socle-injectivity: **PASS / CLOSED**
- U5 intrinsic uniqueness: **PASS / CLOSED**
- N4 finite-window factorization: **PASS / CLOSED**
- N5 q-blind finite selector theorem: **PASS / CLOSED**
- overall novelty: **OPEN / CONDITIONAL**

No Fox computation was reopened. The remaining task is the final literature novelty comparison: determine whether this exact bare-(Q_k), q-blind selector/factorization statement is an immediate corollary or equivalent reformulation of an existing theorem.

Record: `research/U5_INTRINSIC_FINITE_SELECTOR_AUDIT_2026-09-24.md` (commit 814c8b9a20f76cde5611c4f2c3698d85c6e5ce6c).

## 2026-09-24 — N3–N5 LITERATURE GATE RESULT

The requested novelty-first audit was completed before any new U5 computation.

**N3 — finite-level uniqueness:** the full-group statement is known. Labute Proposition 6/Theorem 4 gives the all-level crossed-derivation criterion and unique Demushkin orientation; Quadrelli (2024), Lemma 2.9, restates Kummerianity as arbitrary finite-level generator-value lifting. Therefore full-group finite-coefficient uniqueness is **HISTORICAL / SUPERSEDED** as a novelty claim.

**N4 — factorization through Q_k=G/P_{k+1}:** no exact theorem found. Quadrelli (2024), Proposition 2.10, starts with an already Kummerian oriented pair and assumes N subset ker(theta) plus surjectivity of H^1(G,F_p) -> H^1(N,F_p)^G. Its proof uses that hypothesis to construct a cocycle vanishing on N. This is quotient inheritance, not the present finite candidate-recognition theorem. N4 is **OPEN / LOAD-BEARING**.

**N5 — q-blind finite selector:** no exact published theorem was found in the audited corpus stating that the bare finite quotient Q_k carries a functorial predicate whose unique candidate is chi mod 3^k. Labute's proof uses a standard classification presentation; modern papers retain the known orientation as input. N5 is **OPEN / DECISIVE**.

Recent checks of Blumer–Quadrelli, arXiv:2603.15464v2, and Pál–Quick's 2026 A_3-formality papers did not reveal an exact finite Q_k orientation-recognition theorem.

**Consequence:** no new Fox computation is justified. The next authorized attack is the intrinsic U5 theorem, while keeping finite-window factorization/recognition logically separate from the already-known full-group canonical orientation theorem.

Record: research/U5_INTRINSIC_FINITE_SELECTOR_AUDIT_2026-09-24.md.

## 2026-09-24 — U5 PRE-CHECK / LITERATURE COMPARISON

The intrinsic finite predicate is now fixed as
\[
\mathsf K_k(Q_k,\rho):H^1(Q_k,\mathbf Z/3^k(\rho))\to H^1(Q_k,\mathbf F_3)\text{ surjective},
\qquad Q_k=G/P_{k+1}.
\]
Object, functoriality, gauge independence of the predicate, and definitional q-blindness are PASS/CLOSED. U1-U3 provide the factorization/coordinate bridge; U4 remains presentation-local.

A targeted literature comparison was performed. The audited modern literature characterizes full-group Kummerianity by surjectivity of the coefficient-lifting maps for all n and identifies the canonical Demushkin orientation as the unique Kummerian orientation. A quotient-inheritance proposition in the 2024 1-cyclotomicity literature requires an already Kummerian oriented pair, a normal subgroup N contained in ker(theta), and surjectivity of H^1(G,F_p)->H^1(N,F_p)^G. This does not directly establish the present finite candidate-selector on Q_k with N=P_{k+1}; the extra restriction hypothesis and the fact that rho is itself a finite candidate must be checked rather than assumed. The 2022 Kummerian equivalences likewise do not, in the audited statements, supply the bare-Q_k unique-selector theorem.

Therefore U5 remains OPEN/LOAD-BEARING and the novelty gate remains OPEN/DECISIVE. No claim that the finite-window selector is already known, and no claim of novelty, is authorized.

Record: research/U5_INTRINSIC_FINITE_SELECTOR_AUDIT_2026-09-24.md.

## 2026-09-24 — U1–U4 CRITICAL AUDIT: U3 AND U4 CORRECTIONS

The proposed U1–U5 package was independently audited against the continuity protocol. U1 survives and is now CLOSED by the semidirect-product proof: for S_k=A_k⋊U_1 and U_j=1+3^jA_k, P_j(S_k)=3^{j-1}A_k⋊U_j, hence P_{k+1}(S_k)=1. U2 then gives the canonical finite-depth H^1 factorization through Q_k=G/P_{k+1}.

Two corrections are load-bearing.

### U3 correction
The earlier claim “lifting each basis vector gives I⊂3I, hence Nakayama” is not justified. Basis-vector lifting first gives F_i∈3A_k, not F_i∈3I. The correct proof is a valuation induction: if all F_i∈3^mA_k and e_i has a cocycle lift α=e_i+3β with ΣF_jα_j=0, then F_i=−3ΣF_jβ_j∈3^{m+1}A_k. Starting at m=0 and iterating to m=k gives F_i=0. Thus the Fox–Kummer equivalence remains PASS/CLOSED, but the proof mechanism is valuation induction, not the previously stated Nakayama step. This assumes the relevant mod-3 H^1 is represented by arbitrary generator values (as in the standard Demuškin one-relator setting); that hypothesis must be stated explicitly in any general lemma.

### U4 correction
The previously proposed all-k coefficient formula involving c_k=(r_{k-1}-4)/3^{k-2} is false beyond the checked low levels. The exact z_1 coefficient is governed by
\[
2+\rho_k(x_2)^{-1}.
\]
Writing ρ_k(x_2)=r+3^{k-1}a_2 gives
\[
2+ρ_k(x_2)^{-1}\equiv(2+r^{-1})-r^{-2}3^{k-1}a_2\pmod{3^k}.
\]
Since the previous-stage obstruction gives 2+r^{-1}≡0 mod 3^{k-1}, the next digit is determined by the residue of (2+r^{-1})/3^{k-1}; on the canonical branch this forces a_2=1. Hence 1,4,13,40,121,364,… is still recovered, but the former 4−r recurrence is FAIL/CLOSED and must not control the proof.

### Current classification
- U1 finite-depth semidirect lemma: PASS/CLOSED.
- U2 H^1 factorization: PASS/CLOSED.
- U3 Fox–Kummer equivalence: PASS/CLOSED, with corrected valuation-induction proof and explicit mod-3 H^1 hypothesis.
- U4 standard-presentation all-k uniqueness: PASS/LOCAL, using the corrected inverse coefficient; presentation-dependent.
- U5 intrinsic/presentation-free/q-blind selector: OPEN/LOAD-BEARING.
- Overall uniform B2: OPEN/DECISIVE.

The older 2026-09-21 general-k record contains the superseded U3 Nakayama argument and the older recurrence formulation; this entry is the controlling correction. No t_2 route is revived.

Immediate next gate: U5 Object/Input/Functoriality/Gauge/Orientation-bridge audit for the intrinsic finite predicate on (Q_k,ρ), followed by a targeted literature comparison for finite-coefficient quotient inheritance. Do not claim novelty or intrinsic uniqueness until this gate is closed.

## 2026-09-24 — k=3 CRITICAL REVIEW CORRECTION + k=4 GATE

The k=3 document was strengthened after critical audit. Character parameterization, free-group-to-G descent, the hypotheses \(\rho(P_2)=\rho(P_3)=1\) in the valuation steps, and the exact meaning of the 81-case enumeration are now explicit. The phrase “canonical (P_4)-residual” was removed. Scope is corrected: the result is local to the standard rank-four (q=3) presentation; it is not yet a presentation-free or q-uniform theorem. k=3 remains PASS/LOCAL.

The authorized k=4 gate was then executed. With
\[
\rho_4=(1+27a_1,13+27a_2,1+27a_3,1+27a_4),
\]
direct mod-81 crossed-word evaluation gives
\[
z(r)=27((1-a_2)z_1+a_1z_2-a_4z_3+a_3z_4)\pmod{81}.
\]
Universal vanishing forces \((a_1,a_2,a_3,a_4)=(0,1,0,0)\), hence the unique candidate is
\[
\rho_4=(1,40,1,1)\pmod{81}.
\]
Fresh exhaustive enumeration over all 81 compatible lifts confirms the same unique zero.

For the candidate, the direct valuation chain is
\[
z(P_2)\subset3A_4,\quad z(P_3)\subset9A_4,\quad z(P_4)\subset27A_4,\quad z(P_5)=0,
\]
so every mod-3 class lifts and factors through \(Q_4=G/P_5\).

Decision:
- k=4 exact obstruction: **PASS / CLOSED** for the standard family;
- k=4 uniqueness: **PASS / LOCAL**;
- (P_5)-annihilation: **PASS / LOCAL**;
- (Q_4)-factorization: **PASS / LOCAL**;
- presentation-free selector: **OPEN**;
- q-uniformity: **OPEN**;
- all-k theorem: **OPEN / DECISIVE**;
- minimal carrier: **OPEN / LOAD-BEARING**.

The next authorized gate is the uniform finite-depth lemma for \(A_k=\mathbf Z/3^k\) and \(Q_k=G/P_{k+1}\), followed by a literature comparison. No (t_2) route is revived.

Record: `research/KUMMER_B2_K4_FINITE_WINDOW_MOD81_2026-09-24.md` (commit 14947f40075be8fdec9e9b206b2c78a0ecc0b570).


## 2026-09-24 — B2 / k=3 FINITE-WINDOW MOD-27 GATE

The authorized k=3 attack was completed for the standard rank-four q=3 Demushkin group G=<x1,x2,x3,x4 | x1^3[x1,x2][x3,x4]>. By the k=2 result, any K_3 candidate reduces mod 9 to rho_2=(1,4,1,1), so all mod-27 lifts are rho_3=(1+9a1,13+9a2,1+9a3,1+9a4). Exact crossed-word evaluation gives
z(r)=9(-a2 z1+a1 z2-a4 z3+a3 z4) mod 27.
Hence the universal obstruction vanishes iff a1=a2=a3=a4=0, so the unique candidate is rho_3=(1,13,1,1). Independent enumeration of all 3^4=81 lifts confirms exactly one zero obstruction vector.

The load-bearing finite existence gate was then proved directly. For the unique candidate, every mod-3 class f admits an A_3=Z/27(rho_3)-valued crossed cocycle lift on G because z(r)=0 for arbitrary generator lifts. Since z(P_2) is divisible by 3, z(P_3)=P_2^3[P_2,G] evaluates into 9A_3; then z(P_4)=P_3^3[P_3,G]=0 because the cube and commutator contributions are divisible by 27. Thus every lift annihilates P_4 and factors through Q_3=G/P_4. This is a genuine finite-window factorization proof, not an appeal to full-G Kummerianity.

Classification: k=3 exact obstruction PASS/CLOSED for the standard family; k=3 uniqueness PASS/LOCAL; P_4-annihilation PASS/LOCAL; finite Q_3 factorization PASS/LOCAL. Uniform B2 remains OPEN/DECISIVE. Single-vector t_2 remains FAIL/CLOSED. Next authorized gate is k=4, A_3->A_4 and Q_4=G/P_5, with direct finite-depth factorization before any all-k claim.

Record: research/KUMMER_B2_K3_FINITE_WINDOW_MOD27_2026-09-24.md (commit 4023dedb339e178cdf1fa715e8a44eb671d2ed77).

## 2026-09-24 — N1 LITERATURE GATE: KUMMERIAN/CYCLOTOMIC ORIENTATION IS KNOWN; FINITE-WINDOW FACTORIZATION REMAINS OPEN

A four-paper primary-literature audit was completed after restoring RESEARCH_MAP.md, CURRENT_STATE.md, 00_RESEARCH_LOG.md, and RESEARCH_CONTINUITY_PROTOCOL.md. The audited corpus is Labute (1967), Efrat–Quadrelli (2019, arXiv:1707.07018v3), Quadrelli–Weigel (2020, arXiv:1811.02250v3), and Quadrelli–Weigel (2022, arXiv:2103.12438v3). Labute Prop. 6/Thm. 4, Efrat–Quadrelli Thm. 7.1/Prop. 7.3/Thm. 7.6, and the corresponding Quadrelli–Weigel results establish the full-group Kummerian/cyclotomic lifting characterization and uniqueness of the canonical Demushkin orientation. Therefore “canonical orientation = unique Kummerian/cyclotomic orientation” is HISTORICAL / SUPERSEDED as a novelty claim.

The audit did NOT find the stronger statement needed for B2: a q-blind, functorial predicate on the bare finite quotient Q_k=G/P_{k+1} whose unique solution is chi mod 3^k, together with a proof that the full-group lifting obstruction factors through Q_k. The missing finite-depth existence statement is that a mod-3^k lift constructed on G annihilates P_{k+1}; this is not supplied by the full-G Kummerian theorem. Thus the literature boundary is PASS / CLOSED, while finite Q_k reconstruction/factorization remains OPEN / DECISIVE. B2/k=2 remains PASS / LOCAL. The next authorized gate remains k=3, Q_3=G/P_4: direct P_4-annihilation of the mod-27 Kummer lift.

Record: research/N1_LITERATURE_GATE_KUMMERIAN_CYCLOTOMIC_DEMUSHKIN_2026-09-24.md (commit 20064ad894951260bf2a130f9db37bea3a06f092).


## 2026-09-21 — B2 / k=2 FINITE-WINDOW KUMMER TEST

The first concrete B2 finite-window test was completed at k=2, Q_2=G/P_3 for the lower-3-central filtration. Define, for \(\rho:Q_2\to(\mathbf Z/9)^\times\) with \(\rho\equiv1\pmod3\), the finite predicate
\[
\mathsf K_2(\rho): H^1(Q_2,\mathbf Z/9(\rho))\to H^1(Q_2,\mathbf F_3)\text{ is surjective}.
\]
Using the already audited mod-9 obstruction \(\delta_{2,\rho}(f)=[f(p)+(\lambda\wedge f)(R)]\omega\), \(R=[X_1,X_2]+[X_3,X_4]\), \(p=X_1^{(1)}\), the universal-zero condition forces \(\lambda=e_2^*\), hence \(\rho=(1,4,1,1)=\chi\bmod9\).

The finite-window existence gate was then checked directly: for the resulting A_2-valued lift z, reduction gives z(P_2)=0, so z(P_2)\subset3A_2; also \(\rho(P_2)=1\). Therefore z(g^3)=0 for g\in P_2, and the crossed-commutator formula gives z([g,h])=0 for g\in P_2, h\in G. Since P_3=P_2^3[P_2,G], z(P_3)=0. Thus the mod-9 lift factors through Q_2; existence is not being inferred merely from the full group G.

For every other candidate \(\lambda\), the audited obstruction supplies an f with nonzero obstruction in H^2(G,F_3); by naturality of inflation this rules out vanishing of the corresponding Q_2 obstruction. Hence the finite predicate has the desired unique solution in this k=2 test.

Decision:
- B2 finite predicate definition: **PASS / CLOSED**;
- q-blindness/predicate naturality at k=2: **PASS / CLOSED**;
- Q_2 finite-window existence: **PASS / LOCAL**;
- k=2 uniqueness: **PASS / LOCAL**;
- uniform B2 theorem for all k: **OPEN / DECISIVE**;
- next gate: k=3, Q_3=G/P_4; first prove P_4 annihilation of the mod-27 Kummer lift before any higher interpretation.

Record: research/KUMMER_B2_K2_FINITE_WINDOW_MOD9_2026-09-21.md (commit 232f12ef8bf48c808b771739d19eaebd03ff0107).
## 2026-09-20 — HA61-B5-12: CANONICAL t2 NO-GO

A same-group relator-conjugation witness now kills the proposed single presentation-independent vector t2. For q=3, p!=0 and lambda=e2*, while the audited conjugation law shifts the coordinate residual by lambda(v)p. Choosing v with lambda(v)=1 changes t2 by p, although all intrinsic input data and the exact connecting-obstruction family remain unchanged. Thus raw t2 is not an intrinsic natural transformation. The quotient t2/<p> is invariant but insufficient because f(t2) does not descend: primary-zero gives f(p)+(lambda wedge f)(R)=0, not f(p)=0. The diagonal (t2,mu) quotient was already rejected because it identifies distinct coefficient actions. Therefore the single-vector P4/t2 compression route is FAIL/CLOSED. The intrinsic delta3 family remains PASS/CLOSED; alternative richer secondary compression is OPEN/DECISIVE; HA61-C via t2 is not opened.

Record: research/HA61_B5_12_NO_GO_CANONICAL_T2_2026-09-20.md

## 2026-09-20 — HA61-B5-11: FINITE-DEPTH D4 SOURCE LEDGER

The D4 Zassenhaus source list is exhausted at the required finite depth. Using the already established crossed-cocycle valuation z(gamma_2) in 3A3, z(gamma_3) in 9A3, and the finite next-step consequence z(gamma_4) in 27A3, together with rho=1 on commutator subgroups, the /9 mod-3 secondary evaluation has only two surviving source types: F^9 and gamma_2^3. gamma_3^3 and gamma_4 vanish. F^9 gives f(g), while gamma_2^3 gives the old (lambda wedge f) sector. Thus there is no hidden third D4 source, but canonical extraction of the F^9 residual as a filtered t2 remains open.

Decision: D4 finite source classification PASS/LOCAL; gamma3^3/gamma4 zero PASS/LOCAL; intrinsic delta3 family PASS/CLOSED; filtered t2 extraction OPEN/LOAD-BEARING; HA61-B OPEN/LOAD-BEARING; HA61-C not opened.

Record: research/HA61_B5_11_FINITE_DEPTH_SOURCE_LEDGER_2026-09-20.md

# HA61-B5-10 — INTRINSIC SECONDARY FAMILY + PURE-CONJUGATION CANCELLATION — 2026-09-20

## Status

**PASS / CLOSED for the intrinsic cohomological secondary object and pure relator-conjugation invariance; FAIL / CLOSED for the proposed diagonal affine quotient as an orientation carrier; HA61-B remains OPEN / LOAD-BEARING.**

This attack was pushed past the earlier formal affine compensator instead of treating it as a gauge quotient.

### 1. Intrinsic object

For a fixed intrinsic primary coefficient character rho_2, define the intrinsic lift set
L(rho_2) = {rho_3 : G -> (Z/27)^× : rho_3 mod 9 = rho_2}.

For every rho_3 in L(rho_2), the exact sequence
0 -> F_3 -> Z/27(rho_3) -> Z/9(rho_2) -> 0
defines a canonical connecting map
delta_{3,rho_3}: H^1(G,Z/9(rho_2)) -> H^2(G,F_3).

Therefore the secondary object is the function-valued family rho_3 |-> delta_{3,rho_3}. It is defined without q, chi, a presentation, Fox coordinates, t_2, or a preferred H^2 generator.

### 2. Gauge/naturality

Representative changes z -> z + d_{rho_2}c leave the connecting image unchanged. Under group isomorphism, naturality of connecting homomorphisms transports the entire family. Hence presentation/lift naturality is **PASS / CLOSED at the cohomological-object level**.

### 3. The diagonal quotient is not legitimate

The earlier formal law
(t_2,mu) -> (t_2+a p, mu+a lambda)
is only an obstruction-preserving compensator. It is not an actual pure-presentation gauge action: under pure relator conjugation the intrinsic rho_3, hence its lift parameter mu, is fixed.

Moreover mu, mu+lambda, mu+2lambda are distinct rho_3 candidates when lambda != 0. Quotienting by the lambda-direction would identify the very alternatives that the secondary obstruction is supposed to distinguish.

Decision: **(t_2,mu)/F_3(p,lambda) as the orientation carrier = FAIL / CLOSED.**

### 4. Exact pure-relator-conjugation check

For r' = v r v^{-1}, a crossed cocycle satisfies exactly
z(r') = z(v) + rho_3(v)z(r) + rho_3(vr)z(v^{-1}) = 0
when z(r)=0 and rho_3(r)=1.

Thus the full crossed-word evaluation is invariant at every filtration order. The isolated degree-three [v,R] term
T([v,R]) = lambda(v)f(p)
cannot be the complete gauge contribution. Its cancellation must occur with the remaining prefix/suffix representative terms; it cannot be repaired by changing intrinsic mu.

This is an exact algebraic cancellation, independent of q and chi.

### 5. Remaining load-bearing boundary

The intrinsic family is now canonical, but the intended filtered compression has not yet been proved. The unresolved tasks are:

1. expand the full delta_3 coordinate formula through the P_4 threshold;
2. identify the P_4 residual with a presentation-independent filtered datum t_2, or prove that no such single datum exists;
3. show that all E_{>P_4} contributions vanish or factor through the same datum;
4. prove functoriality under the declared filtered input category and fix the remaining common H^2 normalization issue;
5. only then test universal zero uniqueness.

No HA61-C and no all-n induction is authorized yet.

### Classification

- intrinsic coefficient-lift domain: **PASS / CLOSED**;
- intrinsic function-valued secondary connecting obstruction: **PASS / CLOSED**;
- pure relator-conjugation invariance: **PASS / CLOSED**;
- formal diagonal compensator: **PASS / LOCAL**;
- diagonal affine quotient as orientation carrier: **FAIL / CLOSED**;
- P_4 residual -> intrinsic t_2: **OPEN / LOAD-BEARING**;
- E_{>P_4} factorization/vanishing: **OPEN / LOAD-BEARING**;
- HA61-B overall: **OPEN / LOAD-BEARING**;
- HA61-C: **not opened**.

## Immediate next attack

Keep the exact intrinsic delta_3 fixed. Perform the source-complete mod-27 / division-by-9 ledger for the P_4 generators, retaining prefix/suffix terms together with the relation-jet terms. The decisive question is whether the surviving functional on the primary-zero domain has rank one and is represented by a natural filtered datum. A failure closes B negatively; a proof opens the final bridge toward C.

Record: `research/HA61_B5_10_INTRINSIC_SECONDARY_FAMILY_AND_CONJUGATION_2026-09-20.md`.


## 2026-09-20 — HA61-B5-3: COMBINED AFFINE SECONDARY QUOTIENT

B5-2 was sharpened to an explicit affine action. On the primary-zero locus, the gauge shift (t_2mapsto t_2+a p) is exactly compensated by (mumapstomu+alambda), because (f(p)=-(lambdawedge f)(R)). Thus the natural secondary object is the quotient/torsor ([(t_2,mu)]in(V^{(2)}oplus V^*)/mathbf F_3(p,lambda)) when (lambda
e0); for (lambda=0) this affine ambiguity disappears.

Decision: combined affine action PASS / LOCAL; raw (t_2) intrinsicity FAIL / CLOSED; no independent cubic-bracket functional PASS / LOCAL; universal affine carrier OPEN / LOAD-BEARING; deeper-than-(P_4) factorization OPEN / LOAD-BEARING; HA61-B OPEN / LOAD-BEARING; HA61-C not opened.

Record: research/HARD_ATTACK_61_B5_3_COMBINED_AFFINE_SECONDARY_QUOTIENT_2026-09-20.md.

## 2026-09-20 — HA61-B5-1/B5-2: SECONDARY WINDOW CORRECTED; RAW t_2 FAILS INTRINSICITY

A direct source audit found two important corrections.

First, the previously proposed map
\[
D_4/D_5\to (1/9)z(\cdot)\bmod3
\]
is not well-defined: \(g^9\in D_9\subset D_5\) but \(z(g^9)/9=f(g)\). The correct mod-27 finite-information threshold is the lower-3-central quotient \(G/P_4\), equivalently the previously established D_10 information window on the standard family. The new residual is in the retained \(P_3/P_4\) layer.

Second, the degree-three Lie/gauge sector was computed. For \(P\mapsto P+[v,R]\),
\[
T_{\lambda,f}([v,R])=-\lambda(v)(\lambda\wedge f)(R).
\]
On the primary-zero locus,
\[
(\lambda\wedge f)(R)=-f(p),
\]
so the raw secondary residual transforms as
\[
t_2\mapsto t_2+\lambda(v)p.
\]
The compensating coefficient-extension parameter transforms as
\[
\mu\mapsto\mu+\lambda(v)\lambda,
\]
because this leaves
\[
f(t_2)+(\mu\wedge f)(R)
\]
unchanged.

Therefore:
- D_4/D_5 secondary factorization: **FAIL / CLOSED**;
- corrected P_4/D_10 threshold: **PASS / LOCAL**;
- \gamma_2^3 contribution: old \lambda\wedge f sector, not a new independent carrier;
- raw t_2 intrinsicity: **FAIL / CLOSED**;
- combined affine secondary pair \((t_2,\mu)\) modulo the diagonal \((p,\lambda)\)-shift: **OPEN / LOAD-BEARING**;
- universal absorption of all degree-three bracket/gauge terms: **OPEN**;
- HA61-B: **OPEN / LOAD-BEARING**;
- HA61-C: **not opened**.

Records:
- research/HARD_ATTACK_61_B5_1_SOURCE_QUOTIENT_CORRECTION_2026-09-20.md (c4c2869...)
- research/HARD_ATTACK_61_B5_2_AFFINE_T2_GAUGE_2026-09-20.md (d817858...)
## 2026-09-20 — HA61-B5: NAIVE D_4 CUTOFF KILLED; P_4 RESIDUAL IS LOAD-BEARING

HA61-B5 was pushed through the filtration/valuation boundary. The naive claim that every E_{>=4} term vanishes modulo 27 after division by 9 is false.

The decisive test is a D_4 element g^9. For an A_3 crossed cocycle with rho(g)=1+3a mod 27,
\[
1+rho(g)+\cdots+rho(g)^8\equiv9\pmod{27},
\]
so
\[
z(g^9)/9\equiv f(g)\pmod3.
\]
Yet g^9\in D_4. Therefore D_4-membership is sufficient for the first mod-9 cutoff but is NOT sufficient for the second mod-27 cutoff.

The correct B5 decomposition is therefore
\[
E_{\ge4}=E_{P_4}+E_{>P_4},
\]
where the first residual must be identified with the intrinsic next filtered datum t_2, while the deeper sector must be shown to vanish in the secondary quotient or factor through the same t_2.

This is a genuine filtration-depth boundary and strengthens HA58: the P_4 residual is not optional bookkeeping; it is forced by the failure of the old D_4 cutoff.

Decisions:
- blanket E_{>=4} vanishing mod 27: **FAIL / CLOSED**;
- D_4 membership as a sufficient secondary cutoff: **FAIL / CLOSED**;
- P_4 residual = intrinsic t_2: **OPEN / LOAD-BEARING**;
- deeper-than-P_4 terms: **OPEN**;
- HA61-B overall: **OPEN / LOAD-BEARING**;
- HA61-C: **not opened**.

Record: research/HARD_ATTACK_61_B5_FILTRATION_CUTOFF_2026-09-20.md (commit d563edad1f5e690ab70c2e13ac28cacb76bc1318).


## 2026-09-20 — HA61-B4 A2-LIFT CLASS INDEPENDENCE AUDIT

B4 attacked the remaining ambiguity between distinct A_2-valued cohomology lifts over the same mod-3 class f. If z'-z=3c, the pullback of 0→F_3→A_3→A_2→0 along i:F_3→A_2, i(c)=3c, is canonically 0→F_3→A_2→F_3→0. Naturality therefore gives the exact identity

  delta_3(z') - delta_3(z) = delta_2(c).

So lift-class independence is NOT automatic; it is controlled exactly by the first-stage connecting map.

For the frozen q=9 branch, rho_2=1 and direct primary crossed-word evaluation gives delta_2=0 identically. The mod-27 formula z(r_9)=9(1-a)z_1 is also unchanged under z_1→z_1+3c_1.

For the frozen q=3 branch, rho_2(x_2)=4 and the exact primary coefficient is 2+4^{-1}=9≡0 mod 9, with other generator coefficients zero. Hence delta_2=0 identically there as well. The mod-27 coefficient is always divisible by 9, so z→z+3c again leaves delta_3 unchanged.

Thus the lift-class ambiguity is closed for the two audited standard branches, but not universally. The non-mu secondary obstruction is a function of f alone on these branches, supporting the t_2 formula locally. General admissible filtered input still requires a proof that delta_2=0 (or an equivalent canonical mechanism).

Decision: HA61-B4 = PASS / LOCAL. HA61-B5 = OPEN / LOAD-BEARING. HA61-C remains unopened; no all-n induction.

Record: research/HARD_ATTACK_61_B4_LIFT_CLASS_INDEPENDENCE_2026-09-20.md (commit 91797618fff9fa9512c4b30ec08ea96df0d42e02).

## 2026-09-20 — HA61-B3 GENERAL A2-LIFT GAUGE TEST

The general representative-gauge question was settled at the cochain level. For the coefficient extension 0→F_3→A_3→A_2→0, if z is an A_2-valued 1-cocycle and z'=z+d_{A_2}φ, choose any lift φ~ to A_3 and the compatible lift z~=z~+d_{A_3}φ~. Since d^2=0,

  d_{A_3}(z~+dφ~)=d_{A_3}z~.

Thus the secondary connecting obstruction is unchanged already as a representative cocycle, not merely modulo H^2. Therefore an apparent B_{rho_2} variation under z→z+dφ cannot be an intrinsic secondary term.

Important boundary: B3 proves representative-gauge invariance only. It does NOT prove independence of distinct A_2-valued cohomology lifts lying over the same primary-zero f. That remaining lift-class ambiguity is precisely the B4 target.

Decision: HA61-B3 = PASS / CLOSED. HA61-B4 = OPEN / LOAD-BEARING. B5 remains unopened.

Record: research/HARD_ATTACK_61_B3_GENERAL_A2_LIFT_GAUGE_2026-09-20.md (commit a2ad711596b5c44ade458c132b95fc82cbe6b8d1).


## 2026-09-20 — HARD ATTACK 54: PERMANENT 19-DIMENSIONAL QUOTIENT IS NOW FIXED

HA53 was critically reviewed against HA52. The generic cyclic-kernel d3/Bockstein phenomenon cited in HA52 cannot affect the specific LHS bidegree (2,1): all r>=3 outgoing targets have negative fiber degree, and all incoming sources have negative base degree. Therefore E_3^{2,1}=E_infinity^{2,1} and the 19-dimensional sector is permanent.

The authoritative object is now the quotient
S = ker(H^2(V,F_3) tensor K -> H^4(V,F_3)) / im(d2:H^2(W,F_3)->H^2(V,F_3) tensor W^*),
with dim S=19 and K=im(d2:W^*->H^2(V,F_3)), dim K=9.

This is a genuine associated-graded filtration piece of H^3(Q_2,F_3). It is not yet an orientation carrier, and no decomposition is inferred from the dimension 19.

Decision: permanent 19D LHS piece PASS / CLOSED; HA52 d3 warning HISTORICAL / SUPERSEDED; H-module structure OPEN / LOAD-BEARING; twisted beta_rho^2 action OPEN / LOAD-BEARING; orientation-selector interpretation OPEN / DECISIVE.

Record: research/KUMMER_HARD_ATTACK_54_CRITICAL_CORRECTION_AND_19_QUOTIENT_2026-09-20.md
## 2026-09-20 — HARD ATTACK 26: TOP-COHOMOLOGY DOES NOT AUTOMATICALLY FACTOR THROUGH Q_k

The next Kummer gate was attacked directly. If N=P_{k+1}(G) and Q_k=G/N, then A_k(rho) is N-trivial because rho factors through Q_k. However the Hochschild–Serre five-term sequence contains

0 -> H^1(Q,A) -> H^1(G,A) -> H^1(N,A)^Q -> H^2(Q,A) -> H^2(G,A) -> H^1(Q,H^1(N,A)).

Thus P_{k+1}(A_k⋊U_k)=1 proves factorization of candidate rho and Z^1 data, but does not imply factorization of H^2(G,A_k(rho)) through the abstract quotient Q_k. The missing datum is the extension/2-cell information carried by 1 -> P_{k+1}(G) -> G -> Q_k -> 1.

Decision:
- H^2-factorization through Q_k as an automatic inference: **FAIL / CLOSED**.
- Q-only intrinsic Kummer selector: **OPEN**; not universally disproved inside the restricted Demushkin category.
- finite extension/2-cell enriched carrier (Q_k,E_k): **OPEN / new principal candidate**.
- no numerical scan authorized.

Record: `research/KUMMER_TOP_COHOMOLOGY_HARD_ATTACK_26_2026-09-20.md`

## 2026-09-20 — DISCOVERY PASS: TWISTED KUMMER / TOP-COHOMOLOGY SELECTOR

A new positive mechanism was identified after Hard Attacks 24–25 closed the shallow crossed-cocycle selectors.

For a candidate finite orientation rho:G->U_k, with A_k=Z/3^k and A_k(rho) the twisted module, the PD^2/Kummer literature supplies a stronger selector: the top-degree twisted obstruction. At the full PD^2 level, the canonical orientation is characterized by maximal top cohomology |H^2(G,A_k(rho))|=3^k (equivalently, by the Kummer lifting property). This is not merely existence of a cocycle.

For the standard rank-4 one-relator family
G_q=<x1,x2,x3,x4 | x1^q[x1,x2][x3,x4]>,
the crossed-derivation/top obstruction row was independently expanded:
d1=q+u2^{-1}-1, d2=0,
d3=-(u4-1)/(u3u4), d4=(u3-1)/(u3u4),
after rho(r)=1 forces u1=1 in U_k.
Hence the full row vanishes iff
u2=(1-q)^{-1}, u3=u4=1,
which is exactly chi mod 3^k on the standard family. Therefore the twisted top-cohomology/Kummer mechanism gives a unique finite-level selector on the standard family.

Critical boundary: this does NOT yet prove that the selector is a functor of Q_k=G/P_{k+1}. Although rho and crossed cocycles factor through Q_k because P_{k+1}(A_k⋊U_k)=1, H^2(G,A_k(rho)) is not automatically determined by an arbitrary finite quotient. Presentation/relator-gauge independence and non-tautological filtered realization remain load-bearing.

Decision:
- twisted Kummer/top-cohomology selector as a mechanism: **PASS / LOCAL**;
- unique finite-level selector on standard one-relator family: **PASS / LOCAL**;
- intrinsic q-blind selector on Q_k: **OPEN**;
- universal factorization through G/P_{k+1}: **OPEN**;
- non-tautological filtered realization: **OPEN**.

Record: `research/KUMMER_TWISTED_TOP_COHOMOLOGY_DISCOVERY_PASS_2026-09-20.md`



## 2026-09-20 — CRITICAL REVIEW OF LOWER 3-CENTRAL BOUNDARY / LOGICAL LIMIT

The first-stage result was attacked before advancing to Kummer recognition.

The algebraic threshold argument survives: for the lower 3-central series P_{n+1}=P_n^3[P_n,G], the standard product formula gives x_1^{3^s} weight s+1, and the abelianization at n=s+2 gives a sharp separation. The quotient-isomorphism statement therefore remains PASS / LOCAL.

Three precision limits are binding:

1. “χ mod 3^k is determined by G/P_{k+1}” is valid only as a standard-family/classification-level information statement. Pairwise separation of the finite q-layers follows from the first abelianized invariant, but this does not yet provide a canonical selector/natural transformation from an arbitrary quotient object to the pointed orientation.

2. The lower-3-central filtration itself is functorial, but a twisted Kummer condition using coefficients Z/3^k(ρ) cannot simply be declared a predicate of G/P_{k+1}: the coefficient action is part of the unknown ρ. The next proof must define the recognition predicate without circularly supplying χ, or else prove that the relevant variable action/semidirect-product data factors through the finite quotient in the required sense.

3. The linear threshold is an information-boundary comparison, not evidence that P_{k+1} is intrinsically “better” or a compressed orientation carrier. In particular, quotient-level automorphisms may still destroy pointedness even when the isomorphism class separates the standard q-layers.

The rank-two computation is a sanity check, not an independent proof of the general theorem; the essential proof remains the lower p-central product formula plus functoriality and abelianization.

Decision: first-stage threshold theorem remains PASS / LOCAL. No new gate is introduced. The single next theorem remains the finite Kummer-recognition/factorization statement, with circularity and pointedness treated inside its proof rather than as separate gates.


## 2026-09-20 — FIRST-STAGE LOWER 3-CENTRAL INFORMATION BOUNDARY

A theorem draft was completed comparing the Zassenhaus filtration D_n and lower 3-central series P_n for the standard family G_{3^s} and power-free control G_∞.

Using Jennings' formula for D_n and the standard product formula P_n=∏_{i+j≥n}γ_i^{3^j}, the power term x_1^{3^s} has D-weight 3^s but P-weight s+1. Hence
G_{3^s}/D_N ≅ G_∞/D_N iff N≤3^s,
and
G_{3^s}/P_n ≅ G_∞/P_n iff n≤s+1,
with sharpness at the next levels detected already after abelianization. The same sharpness mechanism was checked conceptually in the rank-two analogue <x,y | x^{3^s}[x,y]>.

Consequently, within the standard family and using the known orientation formula χ_{3^s}(x_2)=(1-3^s)^{-1}, the information boundary for χ mod 3^k is D_{3^{k-1}+1} on the Zassenhaus scale versus P_{k+1} on the lower-3-central scale; mod 27 gives D_10 versus P_4.

Logical boundary: this is an isomorphism-class information-boundary result, dependent on the standard-family classification/orientation formula. It is not a pointed naturality theorem and does not yet prove a q-blind intrinsic Kummer recognition criterion on G/P_{k+1}.

Status:
- Zassenhaus threshold: PASS / LOCAL.
- Lower 3-central threshold: PASS / LOCAL, subject to the standard P_n product formula.
- Sharpness by abelianization: PASS / LOCAL.
- Rank-two sanity check: PASS / LOCAL.
- Linear information boundary for χ mod 3^k: PASS / LOCAL, standard-family/classification dependent.
- Kummer recognition from G/P_{k+1}: OPEN.

Detailed note: research/LOWER_3_CENTRAL_INFORMATION_BOUNDARY_2026-09-20.md
## 2026-09-20 — CRITICAL CORRECTION: Zassenhaus threshold wording + mixed m-adic reopening

A review correction was independently checked.

The threshold claim was never that (G/D_N(G)) itself is abelian. The correct calculation is
[
(G/D_NG)^{ab}=G/(D_NG').
]
For (G_{3^s}), Jennings' formula shows that at (N=3^s+1)
[
(G_{3^s}/D_N)^{ab}cong mathbf Z/3^s	imes(mathbf Z/3^{s+1})^3,
]
whereas the power-free control has ((mathbf Z/3^{s+1})^4). For (Nle3^s), (x_1^{3^s}in D_N(F)), so the relator (x_1^{3^s}c) reduces to (c) modulo (D_N(F)), yielding
[
G_{3^s}/D_Ncong G_infty/D_N.
]
Thus (D_{3^{n-1}+1}) is sufficient and (D_{3^{n-1}}) insufficient to distinguish the standard-family cases relevant to (chimod3^n), with classification/orientation formula dependence explicitly retained. For (n=2,3), the thresholds are D_4 and D_10.

The second correction concerns HARD ATTACK 10. Its negative result is specifically the failure of the ordinary presentation-independent local degree-(le3) Fox truncation. It does not establish a no-go for finite mixed ((3,I))-adic carriers.

A new definitional branch is therefore authorized:
[
mathfrak m=(3,I),qquad J_n^{mix}=I_{mathrm{Fox}}+mathfrak m^n,
]
subject first to definition, Nielsen covariance, relator gauge/unit/conjugation invariance, finite-level well-definedness, and an orientation bridge. No numerical scan is authorized before these gates pass.

The existence gate and the non-tautology/compression gate are now explicitly separated: Fox-derived finite objects are not excluded from existence, while any claim of genuine compression/independence is tested later.

Load-bearing warning: for (r'=grg^{-1}), Fox differentiation contains an additional term
[
g,partial r+(1-grg^{-1})partial g,
]
so the relation/augmentation ideal must be defined to control this term. This is the first naturality obstacle.

Decision:
- Zassenhaus threshold on standard family: **PASS / LOCAL**;
- ordinary degree-3 Fox truncation no-go: **PASS / CLOSED**;
- mixed m-adic carrier: **OPEN / REAUTHORIZED FOR DEFINITIONAL ATTACK ONLY**;
- relator-gauge naturality: **OPEN / LOAD-BEARING**.

Record: `research/CRITICAL_CORRECTION_MIXED_MADIC_AND_ZASSENHAUSZ_THRESHOLD_2026-09-20.md`

## 2026-09-20 — HARD ATTACK 14: no nontrivial quotient of the exact local Fox carrier

The remaining quotient-based loophole was attacked directly.

For the frozen (q=3) relation, write
[
A=1+u_1,quad B=1+u_2,quad C=1+u_3,quad D=1+u_4.
]
The exact Fox equations are
[
F_1=B(1+A)+A^2,quad F_2=A-1,quad F_3=D-1,quad F_4=C-1.
]
Thus
[
F_2=u_1,quad F_3=u_4,quad F_4=u_3,
]
and after quotienting by these,
[
F_1=2u_2+3.
]
Therefore
[
mathcal A_{mathrm{Fox}}
=
mathbf Z_3[[u_1,u_2,u_3,u_4]]/(u_1,u_3,u_4,2u_2+3)
congmathbf Z_3.
]

The exact local Fox obstruction scheme is already a reduced characteristic-zero point:
[
(A,B,C,D)=(1,-1/2,1,1).
]

Hence a proper unital quotient of this local coefficient algebra either has finite (3)-power characteristic and loses higher (3)-adic digits, or collapses the point. There is no proper quotient-based compression preserving the full orientation.

This closes a specific class of “compress the Fox scheme itself” proposals. It does **not** prove that no different, non-quotient intrinsic exact extension object can exist. Such an object would have to be defined independently of Fox and then factor naturally into the exact Fox carrier.

Decision:
- **quotient-of-local-Fox-scheme compression: FAIL / CLOSED;**
- **exact local Fox carrier minimal under full-(3)-adic-preserving quotients: PASS / CLOSED;**
- **independent intrinsic non-quotient exact compression: OPEN.**

Record:
research/ORIENTATION_FOX_LOCAL_QUOTIENT_MINIMALITY_HARD_ATTACK_2026-09-20.md

## 2026-09-20 — HARD ATTACK 13: full associated-graded no-go and minimal extension lower bound

The previous attack only established that bounded associated-graded windows cannot recover the full orientation. A stronger question was attacked: perhaps the entire infinite mod-3 Zassenhaus graded object could still encode (q) and hence (chi).

The literature boundary closes this loophole for the present odd-prime Demuškin setting. Mináč–Pasini–Quadrelli–Tân identify, for Demuškin groups, the complete graded group algebra
[
\operatorname{gr}\mathbf F_p[[G]]\cong U(L(G))
]
with the quadratic/PBW Demuškin graded algebra. For odd (p), its defining relation is the quadratic symplectic relation
[
[X_1,X_2]+[X_3,X_4]+\cdots,
]
independent of the Demuškin (q)-invariant. Thus the full mod-3 associated-graded object is (q)-blind, not merely finite truncations.

Consequently the rank-four family
[
G_{3^s}=\langle x_i\mid x_1^{3^s}[x_1,x_2][x_3,x_4]\rangle,
qquad
G_\infty=\langle x_i\mid [x_1,x_2][x_3,x_4]\rangle
]
has the same mod-3 graded Demuškin object while
[
\chi_{3^s}(x_2)=(1-3^s)^{-1}
]
varies with (s), and (\chi_\infty(x_2)=1).

This is a genuine project-specific lower bound:

[
\boxed{
\text{full mod-3 associated graded data}
\not\Rightarrow
q
\not\Rightarrow
\chi.
}
]

Therefore any successful q-blind carrier must add non-graded filtered/characteristic-zero extension information. At the first nontrivial level, the projective degree-3 power component (P_3) coupled to the quadratic relation (R_2) supplies such information and recovers (chi\bmod9).

A further precision was added: it would be false to infer that every higher (3)-adic digit requires a new independent extension class. For fixed (q=3), the exact equation (1+2B=0) compresses all digits into one exact (\mathbf Z_3)-coefficient equation. Thus the remaining question is not “how many digits/classes?” but whether this exact extension information admits a canonical intrinsic representation strictly smaller than the universal projective Fox obstruction scheme.

Decision:
- **full mod-3 associated-graded (	o q,chi): FAIL / CLOSED;**
- **minimal non-graded extension lower bound for mod-9: PASS / LOCAL;**
- **intrinsic exact intermediate carrier: OPEN.**

Record:
research/ORIENTATION_FULL_GRADED_NO_GO_MINIMAL_EXTENSION_2026-09-20.md

## 2026-09-20 — HARD ATTACK 10: degree-3 Fox truncation FAIL / CLOSED under Nielsen change

A concrete Nielsen-equivalent presentation was used to attack the remaining idea that the fixed q=3 degree-3 Fox compression might itself be intrinsic.

Take
\[
x_1=y_1y_2,\quad x_2=y_2,\quad x_3=y_3,\quad x_4=y_4.
\]
The exact transformed Fox row is
\[
J'_1=Y_1^2Y_2+Y_1Y_2+1,
\]
\[
J'_2=Y_1(Y_1^2Y_2^2+Y_1^2Y_2+1),
\]
with the remaining rows rational in \(Y_3,Y_4\).

The transported canonical point is
\[
(Y_1,Y_2,Y_3,Y_4)=(-2,-1/2,1,1),
\]
which lies in the same \(1+3\mathbf Z_3\) neighborhood.

After writing \(Y_i=1+v_i\) and truncating to total degree \(\le3\), the second row evaluates at
\[
(v_1,v_2,v_3,v_4)=(-3,-3/2,0,0)
\]
to
\[
-243/2\neq0,
\]
although the full exact Fox row vanishes there.

Decision:
- full Fox scheme Nielsen covariance: PASS/CLOSED;
- fixed-normal-form degree-3 Fox compression: PASS/CLOSED;
- presentation-independent degree-3 Fox truncation: **FAIL/CLOSED**;
- intrinsic exact degree-(2,3) filtered carrier by another construction: **OPEN**.

This is a concrete counterexample to using the local degree bound of the frozen normal form as an intrinsic exact truncation theorem.

Record:
research/ORIENTATION_FOX_DEGREE3_NIELSEN_HARD_ATTACK_2026-09-20.md## 2026-09-20 — HARD ATTACK 9: naive integral augmentation jet FAIL / CLOSED

The proposed next object \(\langle r-1\rangle\subset I^2/I^4\) in \(\mathbf Z_3[[F]]\), with ordinary augmentation ideal \(I\), was attacked before any computation.

For \(r=x_1^3[x_1,x_2][x_3,x_4]\) and \(X_i=x_i-1\),
\[
x_1^3-1=3X_1+3X_1^2+X_1^3.
\]
The commutator product begins in degree 2, so
\[
r-1=3X_1+[X_1,X_2]+[X_3,X_4]+O(I^3),
\]
and therefore \(r-1\notin I^2\).

This kills the proposed plain \(\mathbf Z_3\)-augmentation jet at the definition level. It is not a matter of missing gauge proof.

The correct distinction is:
- standard mod-3 Zassenhaus filtration: uses the completed \(\mathbf F_3[[F]]\) augmentation ideal and yields the degree-(2,3) restricted-Lie relation jet;
- ordinary \(\mathbf Z_3[[F]]\) augmentation filtration: is different and does not place the Demushkin relator in \(I^2\);
- mixed p-adic/Zassenhaus weighted filtrations: a legitimate possible direction, but finite associated graded pieces are residue-layer objects and do not automatically carry the full exact scalar \(-1/2\in\mathbf Z_3^\times\).

This is an independent structural confirmation of the previously closed “naive \(\mathbf Z_3\) restricted-Lie scalar extension” route.

Decision:
- plain \(\mathbf Z_3\)-augmentation \(I^2/I^4\) carrier: **FAIL / CLOSED**;
- mod-3 Zassenhaus degree-(2,3) carrier: **PASS / CLOSED**;
- mixed integral weighted jet: **OPEN**, but cannot be assumed to contain full 3-adic information;
- exact universal Fox scheme: **PASS / CLOSED** under the stated standard hypotheses;
- intrinsic exact two-component filtered compression: **OPEN**.

Literature check: standard Zassenhaus definitions use the augmentation ideal of \(\mathbf F_p[[G]]\), consistent with Jennings/Lazard and modern Demushkin/Koszul references.

Record:
research/ORIENTATION_INTEGRAL_AUGMENTATION_JET_HARD_ATTACK_2026-09-20.md



## 2026-09-19 — HARD ATTACK 2: exact Z_3 carrier identification reopened

A second theorem-level weakness was found. The fixed q=3 crossed-derivation calculation is algebraically sound, but the later claim that a concrete projective degree-(2,3) relation jet with exact Z_3 coefficients is itself an established carrier is too strong.

The mod-3 restricted Lie object uses a characteristic-3 p-operation. It cannot simply be scalar-extended to Z_3 as the same restricted-Lie structure. Therefore the exact pair (R,P_3) over Z_3 has not been independently defined in the required sense.

Correct status: fixed full relation + exact crossed derivation = PASS/CLOSED; intrinsic mod-9 projective degree-(2,3) carrier = PASS/CLOSED; concrete exact two-component degree-(2,3) carrier => full chi = OPEN; naive Z_3 restricted-Lie scalar extension = FAIL/CLOSED.

Detailed audit: research/ORIENTATION_EXACT_Z3_CARRIER_HARD_AUDIT_2026-09-19.md.


## 2026-09-19 — HARD ATTACK 3: universal exact Fox obstruction carrier

The exact-carrier search was reopened with a genuinely different object type rather than a scalar extension of the characteristic-3 restricted Lie carrier. For a fixed minimal one-relator presentation, define the universal Laurent coefficient ring A=Z_3[T_1^{±1},...,T_d^{±1}] and the unevaluated twisted Fox-Jacobian row J_r=(tau(partial r/partial x_i)), tau(x_i)=T_i. The carrier is defined independently of any candidate orientation; a character is recovered only after evaluating T_i at its values and solving J_r=0.

For r=x_1^3[x_1,x_2][x_3,x_4], the row is J_1=1+A+A^2/B, J_2=A^2(A-1)/B, J_3=A^3(D^{-1}-1)/C, J_4=A^3(1-C^{-1})/D. On 1+3Z_3 the zero locus is uniquely A=C=D=1, B=-1/2. Thus a fixed-presentation finite exact algebraic carrier recovering the full orientation has been obtained.

This does not yet solve intrinsicity: arbitrary minimal free-basis changes must be shown to induce the corresponding Laurent-torus coordinate change and transform the obstruction ideal covariantly. Relator conjugation/unit changes must also be checked. The object is not finite information; it contains exact 3-adic coefficient data in a finitely generated algebraic presentation.

Decision:
- fixed-presentation universal Fox carrier: PASS/CLOSED;
- non-circular input definition: PASS/CLOSED;
- q=3 full-orientation recovery: PASS/CLOSED;
- presentation-independent/intrinsic carrier: OPEN;
- two-component degree-(2,3) compression: OPEN.

Detailed record: research/ORIENTATION_EXACT_UNIVERSAL_FOX_CARRIER_AUDIT_2026-09-19.md.


## 2026-09-19 — HARD ATTACK 4: universal Fox carrier covariance CLOSED

The new universal exact Fox carrier was subjected to the presentation-change attack. The carrier is formulated over the completed local coefficient ring A=Z_3[[U_1,...,U_d]], T_i=1+U_i, and is projective under multiplication by units.

Relator conjugation gives J_{uru^{-1}}=tau(u)J_r, so the zero locus is unchanged. Relation-generator changes act by completed coefficient-ring units, conditional on the standard cyclic one-relator relation-module structure. A free-basis change is controlled by Fox's chain rule: the row transforms by induced formal torus substitution followed by an invertible evaluated Fox Jacobian. Hence the universal obstruction scheme is presentation-covariant and its character zero locus is preserved.

For the frozen q=3 relation the unique point in 1+3Z_3 is (1,-1/2,1,1). Therefore the exact carrier branch has a new positive endpoint:
- non-tautological exact characteristic-zero carrier in universal projective Fox-scheme form: PASS/CLOSED;
- presentation covariance: PASS/CLOSED at the universal Fox-calculus level, conditional on standard one-relator relation-module facts;
- fixed q=3 recovery: PASS/CLOSED;
- two-component degree-(2,3) compression: OPEN;
- bounded finite-information universal carrier: FAIL/CLOSED.

The research question is now sharpened: can the universal Fox obstruction scheme be compressed intrinsically to a smaller filtered object, ideally degree (2,3), without reintroducing the earlier circularity?

Detailed records: research/ORIENTATION_EXACT_UNIVERSAL_FOX_CARRIER_AUDIT_2026-09-19.md and research/ORIENTATION_EXACT_UNIVERSAL_FOX_COVARIANCE_AUDIT_2026-09-19.md.


## 2026-09-19 — HARD ATTACK 5: exact Fox degree-3 compression

A further structural reduction was found. In local coordinates T_i=1+u_i, the fixed q=3 universal Fox obstruction ideal is exactly equivalent on the 1+3Z_3 neighbourhood to
F_1=3+3u_1+u_1^2+u_1u_2+2u_2,
F_2=u_1,
F_3=u_4,
F_4=u_3.
Hence the zero locus is u_1=u_3=u_4=0 and 2u_2+3=0, giving chi(x_2)=-1/2. The unreduced second Fox coefficient has degree 3, so the full fixed-normal-form row has local degree at most 3.

The power-free control has projective ideal equivalent to (B-1,A-1,D-1,C-1), giving the trivial 1+3Z_3 character locus. Thus the exact carrier separates q=3 from the power-free control without using q as an input label.

Decision:
- fixed-normal-form degree-3 polynomial compression: PASS/CLOSED;
- intrinsic degree-3 truncation under arbitrary presentation change: OPEN;
- exact two-component (R,p)-type compression: OPEN.

Detailed record: research/ORIENTATION_EXACT_FOX_DEGREE3_COMPRESSION_AUDIT_2026-09-19.md.


## 2026-09-20 — HARD ATTACK 11: higher Bockstein / p-adic digit tower

The proposed Bockstein/higher-obstruction bridge was attacked at the definition level. Candidate-dependent twisted coefficient criteria are exact orientation tests, but they cannot be the desired q-blind filtered input because the coefficient system already depends on the unknown character. Higher Bocksteins can detect p-power lifting depth, but their existence does not supply a canonical map to the next character digit. In the frozen q=3 Fox equations, after the mod-9 layer is fixed, all higher digits are forced recursively by the exact unit equation 1+2B=0; no independent higher geometric obstruction appears in that presentation.

Decision: **OPEN / STRUCTURAL** for a genuine higher-obstruction bridge; **FAIL / CLOSED** for the inference “higher Bockstein tower alone reconstructs full chi.”

Next attack: distinguish full filtered extension data from the bare associated graded tower, and test whether the former canonically reconstructs the exact Fox obstruction ideal. If not, seek an explicit same-graded/different-lift obstruction pair.

Record: `research/ORIENTATION_HIGHER_BOCKSTEIN_HARD_ATTACK_2026-09-20.md`.


## 2026-09-20 — HARD ATTACK 12: filtered extension vs associated graded

The phrase “full filtered tower” was split into (A) the full associated-graded tower and (B) an actual compatible tower of filtered extension quotients. (A) does not retain extension/gluing data; the $q=3^s$ family gives the finite-window obstruction to full $\chi$. (B), if it literally retains compatible residues of the relation in a complete separated filtration, reconstructs the completed relation by inverse limit, and completed Fox calculus then applies by continuity. This is mathematically valid but largely formal and does not by itself provide a smaller intrinsic carrier.

Decision: associated-graded full-$\chi$ claim **FAIL / CLOSED**; full filtered-extension-to-Fox implication **PASS / LOCAL**; genuine intermediate compression **OPEN**.

Record: `research/ORIENTATION_FILTERED_EXTENSION_VS_GRADED_HARD_ATTACK_2026-09-20.md`.


## 2026-09-20 — CONSOLIDATED RESEARCH PROGRAM SYNTHESIS / MOD-27 GATE

A full-state synthesis was frozen in research/RESEARCH_PROGRAM_SYNTHESIS_2026-09-20.md to prevent local branch results from obscuring the main mathematical question.

The refined objective is to determine the exact information boundary for recovering the canonical 3-adic orientation: what the full mod-3 associated graded loses; what the first filtered extension layer adds; whether higher finite 3-adic digits admit intrinsic finite-level carriers; and whether a compatible tower yields full chi while remaining genuinely smaller than exact Fox/presentation data.

### Established
- Complete mod-3 associated graded is q-blind: **FAIL/CLOSED** for recovering q or chi.
- overline J_3=[(R,p)] recovers chi mod 9: **PASS/CLOSED** under the audited standard transgression/Bockstein convention.
- A literal compatible full filtered extension tower reconstructs the completed relation and hence chi by inverse-limit + continuous Fox: **PASS/LOCAL**, but this is not a compression result.
- Universal exact Fox carrier recovers full chi: **PASS/CLOSED** under the audited hypotheses.
- Exact local Fox algebra is already reduced and isomorphic to Z_3: quotient compression preserving all 3-adic information is **CLOSED**.

### Explicitly excluded
Naive Z_3 augmentation jet; naive Z_3 restricted-Lie scalar extension; intrinsic fixed degree-3 Fox truncation; higher-Bockstein-alone reconstruction; full associated-graded tower reconstruction; bounded-degree + bounded-precision universal recovery; quotient compression of the exact local Fox algebra.

### Still open
P_3 information-theoretic minimality; absolute carrier minimality outside the explicitly defined quotient-observable category; intrinsic J_27; compatible higher J_(3^n); strict intrinsic compression of the full Fox carrier; non-tautological filtered-extension -> exact-Fox factorization.

### NEXT GATE
The next task is **not** another broad scan. It is the existence/no-go test for an intrinsic mod-27 carrier
\[
J_{27}(G)\Rightarrow\chi\bmod27.
\]
The candidate must be independent of the unknown chi, presentation/Nielsen/relator-gauge invariant, separating at mod 27, naturally reduce to the established mod-9 carrier, and not be a relabeled Fox-equation modulo 27. Any failure at definition/invariance/separation closes that branch immediately.

This is the current authoritative continuation point.

 
## 2026-09-20 — CRITICAL REVIEW: FORMALIZE INTRINSIC CARRIER BEFORE MOD-27

The consolidated synthesis was attacked again. The main surviving weakness was not a mathematical counterexample but a methodological ambiguity: "intrinsic", "non-tautological", and "strictly smaller" were not yet operational enough to serve as hard Gate conditions.

Binding correction:
- formalize the admissible category, morphisms, gauge transformations, coefficient/target category, and functoriality before any mod-27 computation;
- define q-blindness at construction time, excluding chi/q from the input;
- require an explicit natural orientation bridge and a commuting reduction J_27 -> J_9;
- replace the informal non-tautology condition by the operational criteria in research/INTRINSIC_CARRIER_FORMAL_GATE_PRE_MOD27_2026-09-20.md;
- treat "smaller" only relative to an explicitly declared comparison category/invariant;
- do not require compression to prove existence of a legitimate J_27; an intrinsic separating candidate with unresolved compression is PASS / LOCAL or OPEN;
- treat the full filtered inverse-limit route as formal sufficiency, not as substantive compression evidence;
- keep M3 literature comparison parallel to any novelty claim.

This correction prevents a self-imposed overstrong Gate from turning failure of a chosen definition into a false mathematical no-go result.

The mod-27 branch remains the next substantive target, but only after this formal gate is accepted.


## 2026-09-20 — HARD ATTACK 15: MOD-27 CATEGORY ADEQUACY / TRIVIAL-INTRINSICITY LOOP

Before constructing a higher obstruction, the admissible input category itself was attacked. The PRE-MOD27 gate allowed the group G together with filtered relation data, but if arbitrary intrinsic constructions of the full group G are admitted, then the canonical dualizing module/action already contains the canonical orientation. Likewise, the Demuškin classification identifies q as a group invariant and recovers the canonical orientation from q in the standard presentation. Hence an unrestricted group-only J_27 exists trivially, but this is not a new filtered/relation carrier.

This forces a sharper definition-level distinction: “q is not literally supplied” is not enough for q-blindness. A legitimate new J_27 must be constructed from the declared filtered/relation-information functor itself, without first extracting the dualizing action, q (or an equivalent complete classification invariant) and repackaging it as the carrier.

The mod-27 problem is therefore split into: (A) unrestricted group-intrinsic reconstruction — known/tautological for this program; (B) filtered/relation-data reconstruction — still OPEN; (C) mod-3 associated-graded/cohomological data — already insufficient; (D) full compatible filtered extension tower — sufficient but essentially retains the completed relation.

Decision: **CATEGORY-ADEQUACY CORRECTION: PASS / CLOSED.** This closes a methodological loophole, not the existence/no-go question for a genuine filtered J_27.

Record: research/MOD27_CATEGORY_ADEQUACY_HARD_ATTACK_2026-09-20.md


## 2026-09-20 — HARD ATTACK 16: COEFFICIENT-9 BOCKSTEIN EXTENSION CARRIER CANDIDATE

A genuinely new mod-27 candidate survived the definition-level attack:
\[
\mathcal B_{27}(G)=\bigl(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9\bigr),
\]
with \(\beta_9\) the connecting map for \(0\to\mathbf F_3\to\mathbf Z/27\to\mathbf Z/9\to0\). This is intrinsic coefficient-extension data, functorial, q-blind, and visibly reduces to the audited mod-9 cup+Bockstein carrier.

For the standard family, direct relator lifting gives \(\beta_9(f)=qf(x_1)/9\) in the H² line. Naturality gives \(\beta_9\circ\iota=\beta_1\). Hence the first two coefficient-extension layers distinguish q=3, q=9, and q divisible by 27 without inserting q.

A critical correction was made during the attack: the orientation digit must be expressed by the p-adic logarithm
\[
\lambda_{27}=\frac13\log\chi\pmod9,
\]
not by \((\chi-1)/3\), which is not additive mod 9. For the standard family, \(\lambda_{27}=e_2\) at q=3, \(3e_2\) at q=9, and 0 at q divisible by 27, giving \(\chi(x_2)=13,10,1\pmod{27}\) after exponentiation.

This produces the first serious intrinsic J_27 candidate. However, the orientation bridge is not yet theorem-level: one must prove naturally, without a chosen standard presentation, that the cup-dual of the relevant Bockstein layer equals the corresponding coefficient of \(\frac13\log\chi\). Gauge/morphism naturality of this bridge is the remaining load-bearing step.

Decision: **MOD-27 BOCKSTEIN-EXTENSION CARRIER: OPEN / STRONG CANDIDATE.**

Substatus: definition PASS; q-blindness PASS; functoriality structural PASS; reduction to J9 PASS; separation PASS/LOCAL; orientation bridge OPEN; compression below Fox OPEN.

Record: research/MOD27_BOCKSTEIN_EXTENSION_CARRIER_HARD_ATTACK_2026-09-20.md


## 2026-09-20 — HARD ATTACK 17: BOCKSTEIN CARRIER MAY ONLY REPACKAGE q-VALUATION

The apparent mod-27 orientation bridge was attacked at the non-tautology level. The coefficient-extension package \(\mathcal B_{27}\) separates the standard family by \(v_3(q)=1,2,\ge3\), while the proposed logarithmic orientation values \(1,3,0\pmod9\) are already a known function of that q-class through the Demuškin orientation formula. Thus the current evidence is equally explained by \(\mathcal B_{27}\to v_3(q)\text{-class}\to q\text{-class}\to\chi\), which is forbidden classification/repackaging under the revised gate.

Therefore the package remains an intrinsic q-information detector, but its status as a new orientation carrier is downgraded. Decision: **CONDITIONAL / NOT YET ADMISSIBLE**. To recover admissibility, one needs a presentation-free universal identity or independent universal property producing \(\frac13\log\chi\) directly, without first extracting q/classification data. If no such factorization exists, close the candidate as an orientation carrier while retaining the detector result.

Record: research/MOD27_BOCKSTEIN_EXTENSION_CARRIER_HARD_ATTACK_2026-09-20.md


## 2026-09-20 — HARD ATTACK 18: internal-automorphism no-go for the mod-27 Bockstein carrier

The coefficient-extension candidate
\[
\mathcal B_{27}=(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9)
\]
was attacked by the automorphism group of the carrier itself.

For the frozen \(q=3\) relation, \(a_1\in3\mathbf Z/9\) and \(a_2,a_3,a_4\) are unrestricted. The map
\[
S(a_1,a_2,a_3,a_4)=(a_1,4a_2,a_3,a_4)
\]
is \(\mathbf Z/9\)-linear, fixes reduction and \(\iota(H^1(G,\mathbf F_3))\), preserves the cup product, and preserves \(\beta_9\), since \(\beta_9\) sees only the \(a_1\)-component in the frozen relation.

Thus the full declared carrier has an internal symmetry acting trivially on the mod-3 direction but nontrivially on its characteristic-zero lift. The required \(q=3\) logarithmic orientation digit
\[
\lambda_{27}=\frac13\log\chi\equiv e_2\pmod9
\]
therefore cannot be canonically selected from the declared carrier.

Decision:
- **\(\mathcal B_{27}\) as a mod-27 orientation carrier: FAIL / CLOSED;**
- intrinsic coefficient-extension/q-layer detector: **PASS / LOCAL;**
- a different mod-27 carrier with additional rigidifying structure: **OPEN.**

This supersedes HARD ATTACK 17's CONDITIONAL status. No further Bockstein-only scan is authorized.


## 2026-09-20 — HARD ATTACK 20: Bockstein package closes as a new non-tautological mod-27 carrier

Hard Attack 19 corrected the logical gap in Hard Attack 18: the internal map S on H^1(G,Z/9) is an abstract carrier automorphism, not yet an admissible group-induced morphism. Therefore S alone cannot prove a naturality no-go in the project's real input category.

A stronger independent attack was then made at the factorization level. On the rank-four Demuškin family, the entire declared package B_27 has exactly the three coefficient-extension types determined by v_3(q)=1,2,>=3: beta_1 nonzero; beta_1=0 with descended beta_9 nonzero; both zero. The known mod-27 orientation reduction has exactly the corresponding three classes 13,10,1. Thus the present package's successful orientation values are extensionally a function of the same finite q-valuation/classification partition.

No independent chain-level identity, universal property, or finer invariant has been produced inside B_27 that distinguishes orientations while the q-class is held fixed. Therefore the package fails the PRE-MOD27 operational non-tautology criterion as a **new orientation carrier**, even though it remains a valid intrinsic finite q-layer detector.

Decision:
- B_27 q-layer detector: **PASS / LOCAL**;
- B_27 as new non-tautological mod-27 orientation carrier: **FAIL / CLOSED**;
- Hard Attack 18 absolute symmetry no-go: **HISTORICAL / SUPERSEDED**;
- successor carrier with genuinely new q-blind rigidification: **OPEN**.

Stop consequence: no further beta_1/beta_9 scans on the same family are authorized. A successor must add genuinely new structure or an independent universal property, and must first pass the same object/category/q-blindness gate.## 2026-09-20 — CRITICAL REVIEW OF HARD ATTACK 20

Hard Attack 20's closure of the mod-27 Bockstein carrier was overstrong. The argument established only that the **observed Bockstein layers** on the tested Demuškin family form three q-valuation cases. It did not prove that the full structured carrier \((H^1(F_3),H^1(Z/9),red,iota,cup,beta_1,beta_9)\) has exactly three isomorphism types, nor that every natural bridge on the full admissible category factors through q/classification.

This distinction is load-bearing: agreement with the known q->chi formula on a test family is evidence against novelty, but not a universal no-go theorem. The candidate therefore returns to **CONDITIONAL / OPEN** as an orientation carrier.

Decision:
- q-layer detection: **PASS / LOCAL**;
- q-factorization on tested family: **PASS / LOCAL**;
- Bockstein orientation carrier: **CONDITIONAL / OPEN**;
- same-family numerical scans: STOP.

Next authorized attack: prove the structured-carrier classification/factorization universally, or produce an admissible same-carrier/different-orientation counterexample.


## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 21: FULL B27 CARRIER CLASSIFICATION ON STANDARD FAMILY

Hard Attack 21 repairs Gap 1 of Hard Attack 20 at the exact structured-object level. For the standard rank-four family and A=Z/9,
\[
H^1(G_q,A)=\{(a_1,a_2,a_3,a_4):qa_1=0\},
\]
so W_q=3A×A^3 for v_3(q)=1 and W_q=A^4 for v_3(q)≥2. The audited transgression convention gives the three full normal forms for (W_q,beta_1,beta_9), with the common mod-3 cup pairing. Hence the entire declared carrier, not merely visible Bockstein ranks, has exactly three isomorphism types on the standard q-family, indexed by v_3(q)=1,2,≥3.

This is **PASS / CLOSED** for full structured-carrier classification on the standard family and **PASS / CLOSED** for q-valuation factorization on that family.

It is deliberately NOT promoted to a universal no-go: this does not prove that every natural bridge on the full admissible filtered/relation category factors through q/classification. The B27 orientation-carrier status therefore remains **CONDITIONAL / OPEN**.

Stop: no further same-family beta_1/beta_9 scans. Next attack must be universal/categorical: prove universal factorization/no-go, or construct an independent chain-level orientation bridge.

## CRITICAL REVIEW OF HARD ATTACK 21 — 2026-09-20

Hard Attack 21 correctly repairs the principal Gap 1 from Hard Attack 20 on the standard rank-four family, but the record still contains three precision issues that must be fixed before the next universal attack.

### 1. What is actually proved
For (G_q=\langle x_1,x_2,x_3,x_4\mid x_1^q[x_1,x_2][x_3,x_4]\rangle), the calculation
\[
H^1(G_q,\mathbf Z/9)=\{(a_1,a_2,a_3,a_4)\in(\mathbf Z/9)^4:q a_1=0\}
\]
gives (3A\times A^3) for (q=3) and (A^4) for (q\ge9). Together with the displayed Bockstein normal forms this does establish the three structured-carrier isomorphism types on this standard family: class (v_3(q)=1), class (v_3(q)=2), and class (v_3(q)\ge3). The converse distinctions are also structural: the underlying (W_q) differs between (q=3) and (q\ge9), while (\beta_9\) distinguishes (q=9) from (q\ge27).

### 2. Terminology correction
The phrase “canonical normal-form identifications” is too strong. The coordinates (a_i) and the displayed models depend on a chosen standard presentation. The proved statement is: **explicit structure-preserving model isomorphisms exist in a chosen standard presentation, and the resulting abstract structured carrier has exactly three isomorphism types on this family.** No canonical basis or canonical coordinate identification is claimed.

### 3. Target formalization remains load-bearing
The notation (O_{27}) must now be fixed before any bridge theorem is claimed. It should not be treated informally as “the character”. The natural target should be defined basis-free as the appropriate orientation torsor/object together with its mod-27 logarithmic datum, so that a statement
\[
\Phi_{27}:\mathcal B_{27}\to O_{27}
\]
means an actual natural transformation in the declared category. In particular, the quantity (\lambda_{27}=\frac13\log\chi\pmod9) is an additive coordinate only after the target object and its natural action are specified; it is not itself a basis-free vector without that structure.

### 4. Universal no-go is still not proved
The standard-family classification does **not** imply
\[
\text{every natural }\mathcal B_{27}\to O_{27}\text{ factors through }q\text{-classification}.
\]
Nor does it produce the desired independent bridge. Thus the carrier remains **CONDITIONAL / OPEN**. The next decisive attacks are categorical, not numerical.

### 5. Binding next gate
Before further calculation:
- define (O_{27}) intrinsically and basis-free;
- formalize the induced action of admissible morphisms on (O_{27});
- test whether there exist admissible objects (G,G') with isomorphic full (\mathcal B_{27}) but non-isomorphic (O_{27}). Such a pair is a genuine no-go and closes the carrier;
- if no such pair can be produced, attack the universal factorization statement or construct an independent chain-level identity for (\lambda_{27}) without extracting (q), the dualizing action, or the known classification formula.

**Status after this review:**
- full structured-carrier classification on the standard family: **PASS / CLOSED**;
- q-valuation factorization on that family: **PASS / CLOSED**;
- Bockstein finite q-layer detector: **PASS / LOCAL**;
- Hard Attack 18 unconditional symmetry no-go: **HISTORICAL / SUPERSEDED**;
- universal factorization/no-go: **OPEN**;
- independent orientation bridge: **OPEN**;
- Bockstein orientation carrier: **CONDITIONAL / OPEN**.

No further same-family Bockstein scan is authorized.

## AUTHORITATIVE UPDATE — HARD ATTACK 22 — 2026-09-20

The mod-27 target is now formalized basis-free:
\[
\lambda_{27}(G)=\frac13\log\chi_G\pmod9\in H^1(G,\mathbf Z/9),
\]
and \(O_{27}(G)\) is the distinguished-orientation singleton/subfunctor selecting this class. This removes the previous ambiguity in the target notation.

The abstract carrier category has a genuine symmetry \(S\) preventing a natural selector of \(\lambda_{27}\), but \(S\) is not an admissible group/gauge morphism; indeed canonical orientation naturality itself blocks such a realization. Thus the abstract no-go is valid only in \(\mathcal C_{27}^{abs}\), not in the project's admissible category.

The decisive admissible counterexample pair
\[
\mathcal B_{27}(G)\cong\mathcal B_{27}(G'),\qquad
O_{27}(G)\not\cong O_{27}(G')
\]
has not been found. The standard Demushkin family cannot supply one because its full carrier types already separate the valuation classes.

**Binding status:** target formalization PASS/CLOSED; abstract-carrier no-go PASS/CLOSED; admissible counterexample OPEN/NOT FOUND; universal factorization OPEN; independent bridge OPEN; Bockstein orientation carrier CONDITIONAL/OPEN.

No further same-family Bockstein computation is authorized. The next branch must add genuinely new q-blind rigidifying structure or prove a universal factorization theorem. A cohomological Mackey/transfer enrichment across open subgroups is recorded as a candidate, not yet accepted.

## AUTHORITATIVE UPDATE — HARD ATTACK 23 — 2026-09-20

A proposed successor based on restriction/corestriction/conjugation over open subgroups was attacked. The entire Mackey/transfer-enriched trivial-coefficient Bockstein system retains a global coefficient symmetry
\[
T_c:a\mapsto ca,\qquad c\equiv1\pmod3,
\]
which commutes with reduction, \(\iota\), both Bocksteins, cup product, restriction, corestriction, and conjugation. It moves the desired logarithmic orientation lift \(\lambda_{27}\).

Therefore Mackey/transfer enrichment alone does not remove the missing lift ambiguity.

This is not a group-level universal no-go because \(T_c\) is a coefficient-system automorphism, not an admissible group automorphism. It is nevertheless a decisive stop for this successor: more bookkeeping of the same trivial-coefficient Bockstein data cannot supply the missing characteristic-zero rigidification.

**Status:** Mackey/transfer enrichment as abstract coefficient-functor carrier **FAIL / CLOSED**; global group-level no-go **OPEN**; independent orientation bridge **OPEN**. The next meaningful branch must add genuinely group-sensitive filtered extension information.


## 2026-09-20 — HARD ATTACK: KUMMER FACTORIZATION VS RECOGNITION

The proposed second-stage claim through the lower 3-central quotient was split into two distinct statements.

For
[
A_k=mathbf Z/3^k,quad U_k=1+3A_k,quad H_k=A_k
times U_k,
]
a candidate character (
ho:G	o U_k) and crossed homomorphism (f:G	o A_k(
ho)) combine into
[
Phi(g)=(f(g),
ho(g))in H_k.
]
The finite semidirect target satisfies (P_{k+1}(H_k)=1), so every such pair factors through
[
Q_k=G/P_{k+1}(G).
]

This proves a genuine factorization lemma: **candidate finite Kummer data is visible at (P_{k+1}).**

However, this does not yet prove that (Q_k) recognizes the canonical orientation. The missing theorem is a q-blind predicate
[
mathsf K_k(Q_k,
ho)
]with a unique solution (
ho=chimod3^k), natural under admissible morphisms and independent of q/presentation/known orientation data.
The naive condition “there exists a crossed homomorphism” is vacuous because (f=0) works for every candidate (
ho). Requiring (f
eq0) still does not supply a canonical selector. A stronger duality condition risks simply repackaging the already-known orientation module/classification.

Candidate characters (Q_k	o U_k) are plentiful, so uniqueness must come from an additional finite obstruction. No such higher-level obstruction has yet been constructed from (Q_k) alone.

Decision:
- finite semidirect/Kummer factorization through (G/P_{k+1}): **PASS / LOCAL**;
- finite q-blind Kummer recognition (G/P_{k+1}Rightarrowchimod3^k): **OPEN**;
- no numerical scan authorized until the recognition predicate is explicitly defined.

Record: `research/KUMMER_RECOGNITION_LOWER_3_CENTRAL_HARD_ATTACK_2026-09-20.md`


## AUTHORITATIVE UPDATE — HARD ATTACK 24 — 2026-09-20

Hard Attack 24 tightened the lower-3-central Kummer factorization proof and separated the complete finite Kummer carrier from the recognition problem.

For
\[
A_k=\mathbf Z/3^k,\quad U_k=1+3A_k,\quad H_k=A_k\rtimes U_k,
\]
a direct induction proves
\[
P_n(H_k)\subseteq 3^{n-1}A_k\rtimes(1+3^nA_k),
\]
hence
\[
P_{k+1}(H_k)=1.
\]
Therefore every candidate pair \((\rho,f)\), with \(\rho:G\to U_k\) and \(f\in Z^1(G,A_k(\rho))\), factors through \(Q_k=G/P_{k+1}(G)\).

This is now a clean **PASS / LOCAL** factorization theorem.

The correct complete finite bookkeeping object is
\[
\mathcal K_k(Q)=\coprod_{\rho\in\operatorname{Hom}(Q,U_k)} Z^1(Q,A_k(\rho)).
\]
The canonical-orientation problem is therefore a finite selection problem: one must construct a q-blind, functorial subobject/predicate selecting exactly \(\rho=\chi\bmod3^k\). The naive condition \(\exists f\) is vacuous because \(f=0\) always exists; \(\exists f\ne0\) is not known to be a unique orientation selector and risks merely restating duality if strengthened by known orientation data.

Decision:
- exact \(P_{k+1}(H_k)=1\): **PASS / LOCAL**;
- candidate Kummer factorization through \(G/P_{k+1}\): **PASS / LOCAL**;
- complete finite Kummer carrier \(\mathcal K_k\): **PASS / LOCAL** as the correct bookkeeping object;
- naive crossed-homomorphism existence selector: **FAIL / CLOSED**;
- canonical q-blind selector from \(Q_k\): **OPEN**;
- universal same-carrier/different-orientation no-go: **OPEN**.

Record: `research/KUMMER_RECOGNITION_LOWER_3_CENTRAL_HARD_ATTACK_24_2026-09-20.md`.

No further numerical scan is authorized until a concrete selector predicate or admissible counterexample construction is available.


## AUTHORITATIVE UPDATE — HARD ATTACK 25 — 2026-09-20 — NONZERO KUMMER COCYCLE SELECTOR CLOSED

The obvious repair of the vacuous crossed-homomorphism criterion was attacked structurally.

For a fixed candidate \(\rho:G\to U_k\), a crossed homomorphism on the rank-four free group is determined by four values in \(A_k\). Imposing the single Demuškin relator gives one additive obstruction
\[
\mathrm{Obs}_\rho:A_k^4\to A_k.
\]
Hence
\[
Z^1(G,A_k(\rho))=\ker(\mathrm{Obs}_\rho)
\]
has cardinality at least \(|A_k|^3\), for every candidate \(\rho\). In particular, nonzero crossed homomorphisms exist for every candidate action, not only for the canonical orientation.

Thus:
- \(\exists f\): **FAIL / CLOSED**;
- \(\exists f\ne0\): **FAIL / CLOSED** on the standard one-relator family;
- Boolean nonvanishing of \(H^1(G,A_k(\rho))\): **FAIL / CLOSED** as an orientation selector;
- richer twisted-cohomological interaction with additional finite group structure: **OPEN**.

The missing ingredient must therefore encode an interaction between the candidate coefficient action and additional intrinsic finite group/extension structure. Mere Kummer existence or nontriviality cannot provide the selector.

Record: `research/KUMMER_RECOGNITION_NONZERO_COCYCLE_HARD_ATTACK_25_2026-09-20.md`.


## METHODOLOGICAL UPDATE — 2026-09-20 — DISCOVERY/ATTACK DUAL TRACK

The recent Kummer branch exposed a process-level risk: repeated hard attacks are excellent for preventing false claims but can become locally exhaustive without generating the conceptual construction needed to reach the target.

Binding methodological correction:

1. **Attack track** remains mandatory for definition, naturality, q-blindness, separation, non-tautology, and proof verification.
2. **Discovery track** is now an equally explicit research phase. It is not a relaxation of rigor; it is where candidate mechanisms are generated before being attacked.
3. Every OPEN bottleneck must therefore be accompanied by a finite **idea search matrix**, not only another obstruction test.
4. Candidate mechanisms should be generated from the target's structural fingerprints:
   - orientation is a coefficient action / character;
   - mod-9 success required the degree-(2,3) relation jet;
   - lower-3-central depth compresses q-information dramatically;
   - Kummer data naturally couples a character with a twisted extension/cocycle;
   - the missing selector must therefore plausibly arise from an interaction between the finite quotient's extension structure and the candidate coefficient action.
5. Literature is to be mined by reusable mechanism, not by matching theorem names: object → input → invariance → obstruction → verification → logical boundary → possible factorization.
6. Before closing an OPEN branch, ask separately:
   **(a) What is false? (b) What structure is missing? (c) What known mathematical mechanism produces exactly that structure?**
7. The next Kummer phase should therefore not be “more Kummer variants” blindly. It should run a structured discovery pass over candidate mechanisms such as twisted extension classes, transgression/fundamental-class pairings, Bockstein–Kummer compatibility, duality-type pairings, and finite nilpotent/central extensions, then submit each candidate to the existing hard gates.

This is a process correction, not a mathematical result. It does not weaken any PASS/FAIL classification.


## 2026-09-20 — HARD ATTACK 27: FINITE EXTENSION CARRIER DEFINITION AND SUFFICIENCY BOUNDARY

After Hard Attack 26, the vague extension/2-cell candidate was made precise. With N=P_{k+1}(G), define M_k=N/(N^{3^k}[N,N]) and E_k=G/(N^{3^k}[N,N]); the subgroup is characteristic, N is open/finitely generated, and the resulting extension is finite. This is an intrinsic q-blind candidate J_k^ext=(Q_k,M_k,E_k), and H^1(N,A_k(rho)) is determined by M_k for every candidate rho.

The hard attack then checked sufficiency rather than assuming it. The Hochschild-Serre total-degree-two structure contains H^0(Q_k,H^2(N,A_k(rho))), so the finite relation-module extension does not automatically determine H^2(G,A_k(rho)). Adding H^2(N,A_k(rho)) directly risks importing the Demushkin duality/orientation object and is therefore circular unless independently reconstructed from filtered extension data.

Classification: definition PASS / LOCAL; automatic H^2 reconstruction FAIL / CLOSED as an inference; universal carrier OPEN; genuine finite 2-cell obstruction OPEN. No numerical scan authorized.

Detailed record: research/KUMMER_FINITE_EXTENSION_CARRIER_HARD_ATTACK_27_2026-09-20.md


## 2026-09-20 — HARD ATTACK 28: CANONICAL FINITE 2-CELL EXTENSION CLASS

The extension branch was sharpened from a finite quotient to its canonical extension class e_k in H^2(Q_k,M_k). This yields a functorial finite transgression map for every candidate twisted coefficient action. The attack found the next logical boundary: e_k alone has no distinguished four-generator/2-cell evaluation, so it does not automatically reproduce the standard twisted obstruction row. Adding a fundamental/duality class directly risks circularly importing orientation.

Classification: e_k PASS / LOCAL; transgression PASS / LOCAL; automatic row recovery FAIL / CLOSED as an inference; zero-map selector FAIL / CLOSED; nonzero selector OPEN; intrinsic reconstruction of the missing 2-cell evaluation OPEN / decisive. No numerical scan authorized.

Detailed record: research/KUMMER_2CELL_OBSTRUCTION_HARD_ATTACK_28_2026-09-20.md


## 2026-09-20 — HARD ATTACK 29: PD2 TOP-CLASS RIGIDIFIER

The obvious way to supply the missing 2-cell evaluation—adjoining H^2(P_{k+1}(G),F_3) or its Z/3^k lift—was attacked. Its quotient action is already the orientation-bearing duality action, so it is not an independently derived filtered carrier. This closes the direct top-class enrichment as a non-tautological solution, while leaving open a genuinely derived finite chain-level obstruction T_k.

Classification: direct top-class enrichment FAIL / CLOSED for the stated objective; independent T_k OPEN / decisive. No further oriented-cohomology enrichment authorized.


## 2026-09-20 — DISCOVERY PASS 30: FINITE DERIVED 2-CELL / FITTING CANDIDATE

Current bottleneck after Hard Attack 29: derive, rather than append, the missing 2-cell rigidifier from (Q_k,M_k,E_k). Candidate T_k is a basis-free finite derived/transgression complex or its Fitting/annihilator/determinant-line defect, depending functorially on the candidate rho. It is intended to retain secondary extension information without choosing a generator or importing the dualizing module.

Hard attack already closes the raw scalar Reidemeister/determinant version: chain bases and coefficient-module scalings change a scalar by units, so no canonical scalar selector is defined. The basis-free Fitting/annihilator/derived-line version remains OPEN / decisive. No identification with H^2(G,A_k(rho)) is assumed; such a bridge must be independently proved. No numerical scan is authorized until the object and bridge are explicit.

Record: research/KUMMER_FINITE_DERIVED_2CELL_DISCOVERY_PASS_30_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 31: TRANSgression DEFECT TOO SHALLOW

The first concrete Fitting candidate was attacked. For C_rho: Hom_Q(M,A_k(rho)) -> H^2(Q,A_k(rho)), the LHS edge sequence gives coker(delta) = im(inflation H^2(Q,A)->H^2(G,A)). For the canonical PD^2 coefficient, the fundamental/top class restricts nontrivially to the open subgroup N, while any inflated quotient class restricts trivially; hence the inflation image is zero. Therefore coker(delta) and any Fitting/annihilator invariant depending only on it cannot select the canonical orientation. This closes the naive coker route. It does not close every invariant of the full two-term complex: ker(delta) and genuinely higher derived combinations remain open. The structural boundary is sharper: quotient transgression sees the q=0 spectral-sequence row, while the desired orientation lies in the q=2 top row.

Record: research/KUMMER_HARD_ATTACK_31_TRANSgression_DEFECT_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 32: LHS MIDDLE-ROW SURVIVOR IS THE ONLY NON-TAUTOLOGICAL SPECTRAL CANDIDATE

Hard Attack 31 is confirmed, but its boundary is sharpened. The closed cokernel/Fitting defect is exactly the quotient-inflation contribution in the LHS filtration, hence the q=0 row. The remaining spectral candidates split into the middle term E_infty^{1,1} and the top term E_infty^{0,2}/d_3^{0,2}.

The top-row route is not a legitimate new carrier if H^2(N,A) and its Q-action are imported, because for an open PD^2 subgroup N that action is already orientation-bearing. Thus raw d_3^{0,2} is FAIL / CLOSED as a non-tautological input route.

The only remaining potentially non-tautological spectral candidate is
T_k^mid(G,rho)=E_infty^{1,1}\subset H^1(Q_k,H^1(N,A_k(rho))).
Since H^1(N,A) is determined by M_k, this is the first candidate that may retain secondary extension information without adjoining H^2(N,A). However, finiteness of its source does NOT prove that d_2^{1,1} is determined by the truncated finite extension (Q_k,M_k,E_k). That finite-input reconstruction is itself a load-bearing theorem and must be proved before any scan.

For the canonical coefficient action, Hard Attack 31 gives E_infty^{2,0}=0, while PD^2 top cohomology has size 3^k and the top class survives. Hence E_infty^{1,1}(G,chi)=0. This is only a necessary condition; the converse is OPEN.

Status:
- Hard Attack 31 coker/Fitting route: FAIL / CLOSED;
- direct top-class/top-row enrichment: FAIL / CLOSED for non-tautological filtered input;
- raw d_3 route: FAIL / CLOSED as an imported top-row carrier;
- finite reconstruction of d_2^{1,1}: OPEN / load-bearing;
- T_k^mid=E_infty^{1,1}: OPEN / decisive;
- selector T_k^mid=0 iff rho=chi: OPEN;
- universal no-go: OPEN.

Record: research/KUMMER_HARD_ATTACK_32_EINFTY11_D3_2026-09-20.md. No numerical scan authorized until the finite-input and selector gates are passed.


## CRITICAL CORRECTION — 2026-09-20 — HARD ATTACK 31 REOPENED AFTER TOP-CLASS RESTRICTION AUDIT

A decisive error was found in Hard Attack 31. The claim that the canonical PD^2 top class for A_k(chi) restricts nontrivially to N=P_{k+1}(G) is not valid. Already at k=1, A_1(chi)=F_3 because chi mod 3 is trivial, and for a proper open subgroup of p-power index the mod-p degree-two fundamental class can restrict to zero. Standard surface/Demuškin duality sources explicitly record vanishing of Res:H^2(G,F_p)->H^2(L,F_p) for proper open subgroups of index divisible by p.

Therefore the inference “top class restricts nontrivially, hence inflation image is zero” is invalid. The exact identity
coker(delta)=im(inflation H^2(Q,A)->H^2(G,A)) remains correct, but its use as an orientation no-go is reopened.

Consequences:
- Hard Attack 31 coker/Fitting selector closure: HISTORICAL / SUPERSEDED;
- coker-based orientation selector: OPEN;
- Fitting/annihilator of coker: OPEN;
- claim that the canonical class lies in E_infty^{0,2}: UNJUSTIFIED;
- claim E_infty^{1,1}(G,chi)=0 from that placement: UNJUSTIFIED;
- raw d3/top-row enrichment remains closed if H^2(N,A) is imported as orientation-bearing input.

The next binding attack is now the actual LHS filtration placement of H^2(G,A_k(chi)): compute inflation image, E_infty^{1,1}, and top-row restriction/edge behavior before classifying any derived selector. No numerical scan is authorized until this filtration audit is complete.

Detailed correction: research/CRITICAL_CORRECTION_HARD_ATTACK_31_RESTRICTION_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 33: COKER ROUTE REOPENS AND SURVIVES VIA NORM-ZERO DUALITY

The restriction audit overturned Hard Attack 31's closure. The exact coker identity remains
coker(delta_rho)=im(inflation)=ker(res:H^2(G,A)->H^2(N,A)).
Using PD^2 duality, the dual of restriction is corestriction on H^0 of the dual coefficient module B=Hom(A,I). Because N=P_{k+1} acts trivially on B, corestriction is the finite norm from Q_k. The abelianization of Q_k contains the three independent classes x_2,x_3,x_4 modulo 3^k, so |Q_k| is divisible by 3^{3k}. The candidate character delta=chi*rho^{-1} has image of order at most 3^{k-1}; decomposing Q into kernel and cyclic image gives a norm coefficient divisible by a sufficiently high power of 3, hence zero on B=Z/3^k. Therefore restriction is zero for every candidate rho, not just the canonical one.

Consequently inflation is surjective for every candidate rho and
coker(delta_rho) ≅ H^2(G,A_k(rho)).
PD^2 duality then gives the exact finite selector
rho=chi mod 3^k iff |coker(delta_rho)|=3^k.

This is a qualitatively new positive result: the finite carrier is constructed solely from (Q_k,M_k,E_k,rho); H^2(G,A) is not input, and the orientation formula is not used in the construction. The bridge is an independent PD^2 duality plus norm-zero theorem.

Status: finite transgression coker carrier OPEN / STRONG; inflation-surjectivity OPEN / decisive; coker-size selector OPEN / decisive pending three independent checks: |Q_k| divisibility, exact cyclic norm valuation, and twisted PD^2 duality/restriction-corestriction compatibility. Hard Attack 31 coker closure is HISTORICAL / SUPERSEDED. No numerical scan needed.
Record: research/KUMMER_HARD_ATTACK_33_COKER_REOPENS_AND_SURVIVES_2026-09-20.md.


## 2026-09-20 — VERIFICATION OF HARD ATTACK 33: FINITE COKER SELECTOR SURVIVES

The three load-bearing checks were independently verified.

(1) |Q_k| is divisible by 3^{3k}: in the abelianization, P_{k+1} maps to 3^k G_ab, while x_2,x_3,x_4 have independent infinite Z_3 directions. Hence Q_k has an abelian quotient containing (Z/3^k)^3.

(2) Norm-zero: for delta=chi*rho^{-1}:Q_k->U_k with image C of order 3^m, write Q_k=K⋊(coset count) at the level of the norm sum. The cyclic geometric sum over C is divisible by 3^m; multiplying by |K| gives total 3-adic valuation at least v_3(|Q_k|)≥3k, hence the norm is zero on every module of exponent 3^k. The trivial-image case is multiplication by |Q_k| and is also zero.

(3) PD^2 duality identifies the dual of restriction H^2(G,A)->H^2(N,A) with corestriction H^0(N,Hom(A,I))->H^0(G,Hom(A,I)); since the latter norm is zero, restriction is zero for every candidate rho.

Therefore inflation H^2(Q_k,A)->H^2(G,A) is surjective and
coker(delta_rho) ≅ H^2(G,A_k(rho))
for every candidate rho.

Using the standard PD^2 orientation criterion |H^2(G,I_k(rho))|=3^k iff rho=chi mod 3^k, equivalently in the dual finite coefficient convention, the finite coker cardinality gives a unique selector of chi mod 3^k. The carrier itself contains only (Q_k,M_k,E_k,rho), not H^2(G,A), H^2(N,A), the dualizing module, q, or a presentation.

Classification:
- finite coker carrier: **PASS / LOCAL**;
- inflation-surjectivity/norm-zero theorem: **PASS / LOCAL**;
- unique Kummer recognition at every finite level k for PD^2/Demuškin G: **PASS / LOCAL**;
- passage to the compatible inverse system chi_filt: **PASS / LOCAL** subject to the declared PD^2 existence/naturality framework;
- universal category-independent minimality/no-go: **OPEN** (not needed for existence of this construction).

Important correction: Hard Attack 31's coker closure is **HISTORICAL / SUPERSEDED**. The actual obstruction was the false nonzero-restriction claim; once corrected, the same coker becomes the successful carrier.

Record: research/KUMMER_HARD_ATTACK_33_COKER_REOPENS_AND_SURVIVES_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 34: COKER DUALITY/NORM AUDIT SURVIVES

An independent audit found one notation-level correction in Hard Attack 33: the dualizing module used for finite p-primary PD^2 duality is the discrete torsion dualizing module I_G (abstractly Q_3/Z_3 with orientation action), so B=Hom(A_k(rho),I_G) is finite of exponent 3^k. With this correction, the argument is sound: B has action chi*rho^{-1}; for N=P_{k+1}, both rho and chi mod 3^k are N-trivial; PD^2 restriction/corestriction duality identifies res:H^2(G,A)->H^2(N,A) with the dual of cor:H^0(N,B)->H^0(G,B); the latter is the finite Q_k-norm. Since v_3(|Q_k|)>=3k from the (Z/3^k)^3 abelianization quotient and |im(chi*rho^{-1})|<=3^{k-1}, the cyclic geometric norm has total 3-adic valuation >=3k and is zero on B. Thus res=0, inflation is surjective, and coker(delta_rho) ≅ H^2(G,A_k(rho)). Combined with the PD^2 criterion |H^2(G,A_k(rho))|=3^k iff rho=chi mod 3^k, this yields finite Kummer recognition at each k.

Decision:
- Hard Attack 33 core theorem: **PASS / LOCAL**, corrected and independently audited.
- finite Kummer recognition at each level k for PD^2/Demuškin G: **PASS / LOCAL**.
- inverse-limit compatibility/naturality: **OPEN**.
- minimality of P_{k+1}: **OPEN**.
- universal category-independent minimality/no-go: **OPEN**.

Detailed audit: research/KUMMER_HARD_ATTACK_34_COKER_DUALITY_AUDIT_2026-09-20.md


## 2026-09-20 — DEFERRED RESEARCH IDEAS RECORDED AFTER COKER BREAKTHROUGH

Following the review of the new proposal set, promising but non-immediate directions were preserved in `research/NEXT_RESEARCH_IDEA_BACKLOG_2026-09-20.md`.

The recorded candidates are:
- compare one-relator finite Fox relation residue against the intrinsic finite extension class/transgression, first determining whether the Fox residue adds information or is only a coordinate realization;
- elevate the finite Kummer result to a unique-selector theorem, with canonical chi recovered as a corollary;
- treat coker cardinality as a maximality-selector reformulation;
- defer mixed m-adic/bi-filtered constructions until precise intrinsicity and relator-gauge naturality are established;
- develop filtration-dependent information-transfer efficiency as a higher-level synthesis;
- postpone P_{k+1} minimality until the admissible carrier category and inverse-limit theorem are settled.

These are **OPEN / DEFERRED**, not closed. The active main line remains finite-coker strengthening followed by a hard attack on (k\to k+1) compatibility/naturality. No deferred branch is to be resurrected without a new structural reason or comparison map.


## 2026-09-20 — HARD ATTACK 35: INVERSE-SYSTEM COMPATIBILITY AUDIT

The next attack separated carrier-level naturality from output compatibility.

For Q_{k+1}->Q_k and E_{k+1}->E_k, the relation modules nevertheless change kernels:
M_{k+1} is built from P_{k+2}, whereas M_k is built from P_{k+1}. The natural inclusion-induced map lands only in a generally proper submodule of M_k. Consequently no automatic map of Hom sources, transgressions, or coker carriers exists. Direct strict inverse-system structure of the raw coker carriers is therefore FAIL / CLOSED as an inference.

A weaker and sufficient statement survives: if rho_{k+1} is the unique level-(k+1) coker selector, then its reduction is the unique level-k selector. The PD² duality criterion identifies maximal top-cohomology size with triviality of chi*rho^{-1}; triviality modulo 3^{k+1} implies triviality modulo 3^k. Hence selected outputs form a compatible family.

Classification:
- carrier-level direct reduction: FAIL / CLOSED as an inference;
- carrier tower naturality: OPEN / load-bearing;
- selector compatibility: PASS / LOCAL under PD² verification;
- practical inverse-limit reconstruction: PASS / LOCAL subject to the declared PD² framework;
- carrier-only inverse-system functoriality: OPEN.

Record: research/KUMMER_HARD_ATTACK_35_INVERSE_SYSTEM_COMPATIBILITY_AUDIT_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 36: SELECTOR-ONLY COHERENCE

Hard Attack 36 asked whether the practical inverse-limit reconstruction requires the raw coker carriers to form an inverse system. It does not.

Define S_k(G) by the finite coker maximality predicate. The finite recognition theorem identifies S_k(G) with the singleton {chi mod 3^k}. Reduction of candidate characters therefore restricts to compatible maps between the singleton selector sets. Thus the inverse-limit selector set is a singleton, giving chi_filt.

This is PASS / LOCAL under the PD² framework. It is a recognition/coherence theorem, not a carrier-only naturality theorem. Raw carrier tower functoriality remains OPEN; so do minimality and universal category-independent claims.

The practical endpoint of the current main branch is therefore:
finite intrinsic carrier -> transgression coker -> unique finite selector -> selector coherence -> chi_filt.

Do not force strict carrier-level inverse maps without a new structural reason.
Record: research/KUMMER_HARD_ATTACK_36_SELECTOR_COHERENCE_ENDGAME_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 37
PD²-independent selector uniqueness was attacked. No valid finite-input reconstruction theorem and no admissible no-go were obtained. Status remains OPEN. The coker selector and selector coherence remain PASS / LOCAL only under the PD² framework. Direct reuse of the known one-relator/Fox obstruction row as an intrinsic proof shortcut is FAIL / CLOSED. The exact load-bearing target is an intrinsic evaluation of the finite extension's 2-cell transgression from (Q_k,M_k,E_k,rho). Detailed record: `research/KUMMER_HARD_ATTACK_37_PD2_INDEPENDENT_SELECTOR_2026-09-20.md`.

## 2026-09-20 — HARD ATTACK 38: EXTENSION-CLASS TRANSGRESSION MADE BASIS-FREE

Hard Attack 38 resolves the precise definitional gap left by Hard Attack 37. For the intrinsic finite extension 1 -> M_k -> E_k -> Q_k -> 1, with e_k=[E_k] in H^2(Q_k,M_k), and candidate coefficient module A_k(rho), the LHS transgression delta_{k,rho}: Hom_{Q_k}(M_k,A_k(rho)) -> H^2(Q_k,A_k(rho)) is canonically the push-forward of the extension class: delta_{k,rho}(phi)=phi_*(e_k), up to the conventional global sign of the spectral-sequence differential.

Thus the finite coker is intrinsically C_k(rho)=H^2(Q_k,A_k(rho))/{phi_*(e_k)}, and can be viewed as the natural transgression profile of e_k over coefficient modules. No presentation, relator, Fox coordinates, q, chi, H^2(G,A), or dualizing module is needed to define this map. Gauge independence follows because only the cohomology class e_k and functorial push-forward are used.

This closes the narrower logical gap “finite extension data -> intrinsic evaluation of its 2-cell transgression” at the level of definition and cohomological interpretation.

It does NOT close PD²-independent selector uniqueness. The remaining theorem is whether the coefficient-module dependence of this intrinsic push-forward profile forces a unique maximal-coker candidate without invoking the external PD² orientation criterion. The known Fox row is now legitimately a coordinate-comparison target, not a definition shortcut.

New structural warning: (Q_k,M_k,E_k) contains the complete finite extension class, so no minimality claim is justified merely from this success.

Classification:
- basis-free finite transgression from e_k: PASS / CLOSED;
- intrinsic/gauge-independent coker construction: PASS / CLOSED;
- Fox row as coordinate realization: OPEN;
- PD²-independent selector uniqueness: OPEN / decisive;
- PD²-based finite selector: PASS / LOCAL;
- carrier minimality and strict tower naturality: OPEN.

Detailed record: research/KUMMER_HARD_ATTACK_38_EXTENSION_CLASS_TRANSGRESSION_2026-09-20.md.

Next authorized attack: compare the known twisted Fox row with the intrinsic push-forward phi_*(e_k), then attack the finite coefficient-module dependence structurally. No broad numerical scan is authorized yet.


## 2026-09-20 — HARD ATTACK 39: YONEDA / RESTRICTED COEFFICIENT-PROFILE COMPLETENESS

Hard Attack 39 attacked the proposed equivalence between the extension class e_k and its transgression profile.

For the full category of Q_k-modules, define T_e(A)(phi)=phi_*(e). The profile recovers e by taking A=M_k and phi=id_{M_k}; conversely e determines the entire profile. Hence full coefficient-category completeness is PASS / CLOSED, but only at a Yoneda-level information-theoretic level.

For the actual Kummer family A_k(rho)=Z/3^k, define the restricted observation map Phi_k(e)=(phi_*(e))_{rho,phi} with kernel K_k=intersection ker(phi_*). The restricted family is information-complete iff K_k=0. No faithfulness theorem is available, and the full Yoneda argument does not establish it.

The selector is weaker than full e_k-recovery: it only requires the finite observation function rho -> |coker[Hom_Q(M_k,A_k(rho)) -> H^2(Q_k,A_k(rho))]| for the specific Demushkin e_k to have a unique maximizer, equal to the canonical orientation residue. This remains OPEN / DECISIVE without PD².

Coordinate comparison with the Fox row is now legitimate only as a secondary computation: one must construct a cocycle for e_k, push it out along phi, and identify the resulting H^2 class with the Fox/crossed-word obstruction, including section/presentation independence.

Classification:
- full coefficient-category profile completeness: PASS / CLOSED (Yoneda-complete, not a selector theorem);
- restricted Kummer profile completeness: OPEN;
- restricted profile -> unique orientation without PD²: OPEN / DECISIVE;
- Fox row as coordinate realization: OPEN;
- PD²-based finite selector: PASS / LOCAL;
- carrier minimality: OPEN;
- strict carrier-tower naturality: OPEN.

Record: research/KUMMER_HARD_ATTACK_39_YONEDA_COEFFICIENT_PROFILE_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 40: RANK-ONE COEFFICIENT / SPECTRAL-BLINDNESS AUDIT

Hard Attack 40 identifies the exact representation-theoretic content of the restricted Kummer profile. For A_k(rho)=Z/3^k, every equivariant phi:M_k->A_k(rho) satisfies phi(gm)=rho(g)phi(m), so phi factors through the twisted scalar specialization M_{k,rho}=M_k/<gm-rho(g)m>. Therefore the push-forward/coker profile of e_k is a scalar-character spectroscopy of the extension class.

This yields a structural factorization **PASS / CLOSED**, but not a generic no-go: K_k may or may not be nonzero on the actual Demushkin e_k. A proof of non-faithfulness would require an explicit invisible class or a theorem about the representation structure of e_k.

The remaining selector theorem is that rho -> |coker[Hom_{Z/3^k}(M_{k,rho},A_k(rho)) -> H^2(Q_k,A_k(rho))]| must have a unique maximizer at chi mod 3^k, without PD².

Classification: scalar-character factorization **PASS / CLOSED**; faithfulness on e_k **OPEN / DECISIVE**; unique scalar-character maximizer without PD² **OPEN / DECISIVE**; Fox row as coordinate realization **OPEN**; PD²-based selector **PASS / LOCAL**; carrier minimality and strict tower naturality **OPEN**.

Record: research/KUMMER_HARD_ATTACK_40_RANK_ONE_SPECTRAL_BLINDNESS_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 40 CRITICAL REVIEW / REVISED GATE

The self-critique of Hard Attack 40 was audited against the authoritative research state.

Accepted corrections:
- A_k(rho)=Z/3^k is rank-one, but M_{k,rho} need not be one-dimensional. The safe terminology is rank-one coefficient / scalar-character specialization.
- Hom_{Q_k}(M_k,A_k(rho)) ≅ Hom_{Z/3^k}(M_{k,rho},Z/3^k) is a formal twisted-coinvariant reformulation, not a new obstruction theorem.
- K_k=0 is auxiliary, not the decisive selector criterion. The decisive PD^2-independent target remains the unique maximizer of rho |-> |C_k(rho)|.
- PD^2-based finite selection remains PASS / LOCAL; its removal is a separate theorem problem.

Critical correction to a proposed new interpretation:
calling maximal coker "complete filling" of H^2 is backwards. Since C_k(rho)=H^2/im(delta), larger coker means smaller transgression image when the ambient group is fixed; equality |C_k|=|H^2| means im(delta)=0. Therefore the useful qualitative notions are transgression invisibility, defect maximality, or vanishing, not filling.

Additional audit:
- "response curve/spectroscopy" is heuristic language until a precise invariant is defined.
- the twisted coinvariant is safely described as a scalar specialization; no unproved induced/coinduced analogy is to be used.
- Fitting/determinant machinery is only a candidate. It is initially a repackaging of a cokernel unless it yields a new basis-independent rho-dependent theorem.
- information-theoretic analogies do not constitute novelty.

Revised active gate:
(A) prove a scalar-visibility/vanishing theorem for the specific Demushkin extension push-forward delta_{k,rho};
(B) at k=2, compare delta_{2,rho} intrinsically with the already closed cup+Bockstein / degree-(2,3) obstruction;
(C) if ambient H^2 size remains uncontrolled, stop and record the exact PD^2 boundary rather than claiming selector uniqueness.

Classification:
- Hard Attack 40 scalar-character factorization: PASS / CLOSED.
- Hard Attack 40 as a new obstruction theorem: HISTORICAL / SUPERSEDED; reformulation only.
- restricted Kummer faithfulness K_k=0: OPEN / AUXILIARY.
- scalar-character visibility of e_k: OPEN / DECISIVE.
- unique coker maximality without PD^2: OPEN / DECISIVE.
- Fox row as coordinate realization: OPEN.
- Fitting/determinant: OPEN / DEFERRED pending non-tautology.
- PD^2 finite selector: PASS / LOCAL.
- carrier minimality: OPEN.
- strict tower naturality: OPEN.
Detailed record: research/HARD_ATTACK_40_CRITICAL_REVIEW_AND_NEXT_GATE_2026-09-20.md.

## 2026-09-20 — HARD ATTACK 48: BASE H^3 TARGET IS KILLED ALREADY AT d_2

HA48 corrected a load-bearing error in HA47. The claim that the only incoming differential to (3,0) after the d_2 stage was d_3:E_3^{0,2}->E_3^{3,0} was false: there is already d_2:E_2^{1,1}->E_2^{3,0}.

Let K=im(d_2:W^*->H^2(V,F_3)). By HA45, K is the 9-dimensional hyperplane annihilating the relation-jet z_R=b_1+e_1e_2+e_3e_4. Since the LHS d_2 is a derivation,

d_2:E_2^{1,1}=V^*\\otimes W^* -> E_2^{3,0}=H^3(V,F_3)

has image V^*\\cup K. A direct basis argument shows

V^*\\cup K = H^3(V,F_3),

using b_2,b_3,b_4, e_{13},e_{14},e_{23},e_{24}, b_1-e_{12}, and b_1-e_{34} as generators of K. An independent finite-dimensional F_3 rank check gives rank 20, equal to dim H^3(V,F_3)=20.

Therefore

E_3^{3,0}=0,

and hence E_infinity^{3,0}=0. The nonzero raw base-row class computed in HA47 is consequently killed at the d_2 target stage; no d_3^{0,2} calculation is needed for this target.

This is a genuine negative refinement: the base-filtration output of beta_rho^2 has no surviving (3,0) component. The second Bockstein problem must move to the surviving filtration pieces (2,1), (1,2), (0,3) and their source-side counterparts.

Decision:
- HA47 target-differential correction: **PASS / CLOSED**;
- V^*\\cup K=H^3(V,F_3): **PASS / CLOSED**;
- E_infinity^{3,0}=0: **PASS / CLOSED**;
- HA47 “first possible incoming differential is d_3^{0,2}”: **FAIL / CLOSED / SUPERSEDED**;
- beta_rho^2 from (R,p): **OPEN / LOAD-BEARING**;
- unique coker maximizer without PD²: **OPEN / DECISIVE**.

Record: research/KUMMER_HARD_ATTACK_48_BASE_TARGET_KILLED_AT_D2_2026-09-20.md (commit 2a8e5ec4ec9b8fbed7b501387f5a0becdd5d6222).


## 2026-09-20 — HARD ATTACK 49: BASE H^4 TARGET ALSO KILLED AT d_2

Hard Attack 48 closed E_infinity^{3,0}=0. The next base target was attacked directly. For the central extension 1 -> W -> Q_2 -> V -> 1, the LHS derivation gives d_2:H^2(V,F_3)⊗W^* -> H^4(V,F_3) with image H^2(V,F_3)∪K, where K=im(d_2:W^*->H^2(V,F_3)) is the 9-dimensional hyperplane from Hard Attack 45. An explicit spanning argument, independently checked by finite-dimensional rank computation, gives H^2(V,F_3)∪K=H^4(V,F_3) (dimension 35). Hence E_3^{4,0}=0 and E_infinity^{4,0}=0.

This removes the second purely-base target. It does NOT imply E_infinity^{2,1}=0: the kernel of d_2 on E_2^{2,1} can be large, and the quotient by incoming d_2 from E_2^{0,2} is still load-bearing. The next gate is therefore the actual survival quotient E_3^{2,1}=ker(d_2:E_2^{2,1}->E_2^{4,0})/im(d_2:E_2^{0,2}->E_2^{2,1}), followed only then by the twisted Bockstein analysis.

Decision:
- H^2(V)∪K=H^4(V): **PASS / CLOSED**;
- E_3^{4,0}=0 and E_infinity^{4,0}=0: **PASS / CLOSED**;
- inference E_infinity^{2,1}=0: **NOT ESTABLISHED**;
- base targets (3,0),(4,0): **CLOSED / NO SURVIVORS**;
- full beta_rho^2: **OPEN / LOAD-BEARING**;
- unique coker maximizer without PD²: **OPEN / DECISIVE**.

Record: research/KUMMER_HARD_ATTACK_49_BASE_TARGET_H4_KILLED_AT_D2_2026-09-20.md

## 2026-09-20 — HARD ATTACK 50: DIMENSIONAL OBSTRUCTION FOR THE (2,1) SURVIVOR

HA50 makes the next bottleneck strictly sharper. From HA49, dim E_2^{2,1}=90 and rank d_2^{2,1}=35, so dim ker d_2^{2,1}=55. Since W is F_3^9 elementary abelian, dim E_2^{0,2}=dim H^2(W,F_3)=C(9,2)+9=45. Therefore dim E_3^{2,1}=55-rank(d_2^{0,2}) >=10. Hence E_3^{2,1} is forced nonzero by dimension alone: incoming d_2 can never kill the entire (2,1) sector. The target is therefore no longer to test whether E_3^{2,1}=0, but to identify the forced survivor subquotient and its H-action. The decomposition H^2(W)=Lambda^2 W^* plus beta_W(W^*) must be retained.

Decision:
- dim E_3^{2,1} >= 10: PASS / CLOSED;
- E_3^{2,1} != 0: PASS / CLOSED;
- exact dimension/module structure: OPEN / LOAD-BEARING;
- survival to E_infinity: OPEN;
- full beta_rho^2: OPEN / LOAD-BEARING;
- unique coker maximizer without PD^2: OPEN / DECISIVE.

Record: KUMMER_HARD_ATTACK_50_21_SURVIVOR_DIMENSION_OBSTRUCTION_2026-09-20.md (commit a8617b69289d4cfa16922903b50639e8a6059ecf).


## 2026-09-20 — HARD ATTACK 51: EXTERIOR FIBER SECTOR RANK 36

HA51 sharpens HA50. Writing c_i=d_2(w_i^*) for a basis of W^*, HA45 gives c_1,...,c_9 linearly independent. By the LHS Leibniz rule,
d_2(w_i^*w_j^*)=c_i\otimes w_j^*-c_j\otimes w_i^*.
Hence d_2 restricted to Lambda^2 W^* is injective, with rank 36. Since dim H^2(W)=45,
36 <= rank(d_2^{0,2}) <=45,
so
10 <= dim E_3^{2,1} <=19.
The remaining uncertainty is exactly the 9-dimensional fiber-Bockstein summand beta_W(W^*). The tempting statement d_2(beta_W(W^*))=0 is not yet promoted; it requires a direct transgression/Bockstein theorem or cochain proof.

Decision:
- d_2|_{Lambda^2 W^*} rank 36: PASS / CLOSED;
- 10 <= dim E_3^{2,1} <= 19: PASS / CLOSED;
- Bockstein-sector d_2: OPEN;
- exact E_3^{2,1} and H-action: OPEN / LOAD-BEARING;
- higher-differential survival: OPEN;
- full beta_rho^2: OPEN / LOAD-BEARING.

Record: KUMMER_HARD_ATTACK_51_EXTERIOR_SECTOR_RANK36_2026-09-20.md (commit 51454b5276e9120dabb8f52bbba4342c5437acd0).


## 2026-09-20 — HARD ATTACK 52: BOCKSTEIN FIBER SECTOR IS d2-CLOSED

HA52 resolves the nine-dimensional uncertainty left by HA51. For any linear functional phi:W->F3, push out the central extension along phi to a cyclic-kernel central extension 1->F3->E_phi->V->1. Naturality of the LHS spectral sequence sends the cyclic fiber Bockstein beta(u) to beta_W(phi). The standard odd-prime cyclic-kernel calculation has d2(beta(u))=0 (the Bockstein-of-extension-class phenomenon occurs one page later). Therefore d2(beta_W(phi))=0 for every phi, and hence d2 vanishes on the entire beta_W(W*) summand.

Combining with HA51's rank-36 injection on Lambda^2 W*, rank d2^{0,2}=36 exactly. Since ker(d2^{2,1}) has dimension 55,
\[
\boxed{\dim E_3^{2,1}=55-36=19.}
\]
This is an exact E3 result, not merely a lower bound. The 19-dimensional survivor is not yet identified as an H-module and need not survive to E_infinity; the next load-bearing target is the first higher differential, especially the d3/Bockstein mechanism.

Decision:
- d2(beta_W(W*))=0: PASS / CLOSED under the standard cyclic-kernel LHS calculation plus pushout naturality;
- rank d2^{0,2}=36: PASS / CLOSED;
- dim E3^{2,1}=19: PASS / CLOSED;
- H-module structure: OPEN / LOAD-BEARING;
- higher d3/higher survival: OPEN / LOAD-BEARING;
- full beta_rho^2: OPEN / LOAD-BEARING;
- unique coker maximizer without PD2: OPEN / DECISIVE.

Record: KUMMER_HARD_ATTACK_52_BOCKSTEIN_SECTOR_D2_CLOSED_2026-09-20.md (commit 4407d8dfc1206ade4384462014b2146c215d558d).


## 2026-09-20 — HARD ATTACK 53: THE 19-DIMENSIONAL (2,1) SURVIVOR IS PERMANENT

HA53 observes a pure bidegree obstruction. Since d_r has bidegree (r,1-r), any outgoing d_r from E_r^{2,1} with r>=3 lands in negative second degree, and any incoming d_r would originate at negative first degree. Hence no higher differential can touch E_3^{2,1}. Combining with HA52 gives
\[
\boxed{E_3^{2,1}=E_\infty^{2,1},\quad \dim E_\infty^{2,1}=19.}
\]
Thus the 19-dimensional sector is a genuine permanent LHS filtration piece, not a transient page-3 artifact.

Decision:
- E_3^{2,1}=E_infinity^{2,1}: PASS / CLOSED;
- dim E_infinity^{2,1}=19: PASS / CLOSED;
- H-module structure: OPEN / LOAD-BEARING;
- twisted beta_rho^2 on this sector: OPEN / LOAD-BEARING;
- unique coker maximizer without PD2: OPEN / DECISIVE.

Record: KUMMER_HARD_ATTACK_53_21_PERMANENT_SURVIVOR_2026-09-20.md (commit 20f4ba10bc744d5ae02e6c656cc6c55d8b216f5b).


## 2026-09-20 — HARD ATTACK 55: CRITICAL REVIEW OF HA54 AND H-LIFT PRE-CHECK

HA54 was critically re-audited before advancing to the representation-theoretic branch.

### Confirmed
The permanent LHS piece remains
\[
E_3^{2,1}=E_\infty^{2,1},\qquad \dim=19,
\]
and the concrete quotient
\[
\mathcal S=\frac{\ker(H^2(V,\mathbf F_3)\otimes K\to H^4(V,\mathbf F_3))}{\operatorname{im}(d_2:H^2(W,\mathbf F_3)\to H^2(V,\mathbf F_3)\otimes W^*)}
\]
has dimension 19. This is a genuine LHS associated-graded filtration piece. No orientation interpretation follows from permanence alone.

### Critical correction / pre-check
The existence of the previously computed \(H\)-action on the filtered degree-one object (and its image \(PSp_4(3)\)) does **not** by itself imply an action of \(H\) on
\[
1\to W\to Q_2\to V\to1.
\]
Before treating \(\mathcal S\) as an \(H\)-module, one must prove that the relevant \(H\)-action lifts to the central extension, equivalently that the extension class is preserved with the required induced action on \(W\), or construct the corresponding extension automorphisms directly.

If this lift fails, that failure is itself a meaningful boundary and the \(H\)-module branch must be closed. If it succeeds, only then may one prove functorially that \(K\), \(\ker\mu\), \(\operatorname{im}d_2\), and \(\mathcal S\) are \(H\)-stable.

### Input-category audit
The objects \(V,W,Q_2\) are finite filtered/extension data, but their admissibility as the declared intrinsic input category must remain explicit. No presentation, classification, known \(\chi\), or PD^2 orientation data may be silently imported into the construction of the \(H\)-action or the interpretation of \(\mathcal S\).

### q=3 boundary
The numerical result \(\dim\mathcal S=19\) is a frozen \(q=3\) local structural result unless a general-q theorem is supplied. It must not be promoted to a universal dimension statement.

### Strategic boundary
The three possible interpretations remain open:
1. **Collapse:** the 19D sector is controlled by already established \((R,p)\) data;
2. **Controlled Enrichment:** it adds a finite, functorially determined correction needed for \(\beta_\rho^2\);
3. **Independent Layer:** it carries genuinely new \(\rho\)-visibility.

No one of these is currently selected.

### Decisions
- permanent 19D LHS filtration piece: **PASS / CLOSED**;
- \(H\)-action lift to \(Q_2\): **OPEN / LOAD-BEARING**;
- \(H\)-module structure of \(\mathcal S\): **OPEN / LOAD-BEARING**;
- twisted \(\beta_\rho^2\) on \(\mathcal S\): **OPEN / LOAD-BEARING**;
- orientation-selector role: **OPEN / DECISIVE**;
- PD^2-free unique coker maximality: **OPEN / DECISIVE**;
- q-universality of the 19D numerical result: **OPEN**.

### Next authorized attack
First search the repository for an already established lift of the filtered \(H\)-action to \(Q_2\) or its central extension. If none exists, attack extension-class invariance/lift directly. Only after that may the actual \(H\)-module structure of \(\mathcal S\) be computed. No dimension-based module identification is authorized.


## 2026-09-20 — HARD ATTACK 56: FULL SP4 LIFT KILLED BY INTRINSIC TORSION LINE

HA55's load-bearing H-lift gate was attacked directly. The full ambient symplectic group used in the degree-4 representation track cannot act through actual automorphisms of the frozen q=3 Demuškin group.

The intrinsic degree-one audit already establishes
\[
G^{ab}\cong \mathbf Z_3^3\oplus\mathbf Z/3,
\]
with the Frattini image of \operatorname{Tor}(G^{ab}) a distinguished line \(\ell=\langle e_1\rangle\subset V\). Every actual automorphism preserves torsion in abelianization, hence preserves \(\ell\).

But the authoritative symplectic convention has \(t_v=I+v(Jv)^T\). For \(v=e_2\), \(Je_2=e_1\), so
\[
t_{e_2}e_1=e_1+e_2,
\]
which does not preserve \(\ell\). Therefore this element of \(Sp_4(\mathbf F_3)\) cannot arise from an actual automorphism of \(G\), and the full ambient symplectic action cannot lift to \(Q_2\).

Decision:
- full \(Sp_4(\mathbf F_3)\) lift to \(Q_2\): **FAIL / CLOSED**;
- intrinsic full-Sp4 module interpretation of \(\mathcal S\): **FAIL / CLOSED**;
- actual automorphism image versus line stabilizer: **OPEN / LOAD-BEARING**;
- lift of actual automorphism image to \(Q_2\): **OPEN / LOAD-BEARING**;
- \(\mathcal S\) under the actual automorphism image: **OPEN / LOAD-BEARING**;
- twisted \(\beta_\rho^2|_{\mathcal S}\): **OPEN / LOAD-BEARING**;
- orientation-selector role of \(\mathcal S\): **OPEN / DECISIVE**.

Interpretation: the earlier full \(Sp_4\) symmetry is an ambient graded symmetry, not the actual automorphism symmetry of the frozen q=3 group. The next authorized branch is the actual degree-one automorphism image, expected to lie in the stabilizer of the intrinsic torsion line. No full-Sp4 decomposition of \(\mathcal S\) should be treated as an intrinsic result.

Record: research/KUMMER_HARD_ATTACK_56_FULL_SP4_LIFT_KILLED_BY_TORSION_LINE_2026-09-20.md


## 2026-09-20 — STRATEGIC RESET: INFORMATION-LAYER PROGRAM

After HA48–56, the project has enough local negative boundaries that continued one-by-one candidate closure risks becoming the dominant activity. The common structural question is now elevated:

> What is the minimum kind of non-graded information required to distinguish the canonical orientation, and how does that information propagate through the filtration tower?

Three layers are fixed for the next strategic pass:
- Layer A: full mod-3 associated graded — q-blind, cannot recover the Z_3-valued orientation (PASS / CLOSED).
- Layer B: intrinsic projective relation-jet/cup+Bockstein carrier [(R,p)] — recovers chi mod 9 under the stated hypotheses (PASS / CLOSED).
- Layer C: deeper finite extension/cohomology data — includes the permanent 19D LHS piece at frozen q=3, but its orientation role is unresolved (OPEN). The full ambient Sp4 action is now closed as an intrinsic symmetry by HA56.

The next high-value program is therefore not to compute every Layer-C module. It is to prove/test an information-layer theorem:
1. formulate the sharp filtration-depth threshold as an explicit information theorem;
2. determine whether the Layer-B relation/power tower canonically propagates to higher 3-adic digits;
3. identify the first digit/layer at which genuinely new information appears, if any;
4. require every Layer-C candidate to pass q-blindness, functoriality, explicit orientation-bridge, non-redundancy, and q=3/control separation before representation computation.

The actual automorphism-image/lift branch remains OPEN/LOAD-BEARING but is subordinate unless it supplies the required functorial mechanism.

Stop rule: no broad representation scan, no full 19D module computation, and no new spectral scan until Test I (digit-depth theorem) or Test II (tower reuse) produces a concrete structural target.

Record: research/STRATEGIC_RESET_INFORMATION_LAYERS_2026-09-20.md (commit da2cd7ec3fae76106033580a1cc98e2cb2984316).

## 2026-09-20 — HARD ATTACK 57: INFORMATION-DEPTH BOUNDARY + LAYER-B TOWER REUSE

The Strategic Reset authorized two tests: a sharp finite-information-depth theorem and a test of whether the mod-9 Layer-B relation/power carrier can be reused for all higher 3-adic digits.

### Test I — information-depth boundary

For the standard family G_{3^s} versus the power-free control G_infty, the audited finite quotient thresholds are:
G_{3^s}/D_N ≅ G_infty/D_N iff N≤3^s, with first separation at D_{3^s+1}, and
G_{3^s}/P_n ≅ G_infty/P_n iff n≤s+1, with first separation at P_{s+2}.

Because the worst case for distinguishing χ mod 3^n from the control is s=n−1, the resulting family-level information boundaries are D_{3^{n-1}+1} and P_{n+1}. Thus mod 27 gives D_10 versus P_4. This is a genuine information-depth result but remains PASS / LOCAL because it is tied to the standard comparison family and uses the known orientation formula only as comparison data.

### Test II — Layer-B tower reuse

The established projective carrier [(R,p)] remains PASS / CLOSED for χ mod 9. The question was whether a canonical recursive tower built from the same relation/power datum can directly generate all higher digits.

The answer at the current theorem level is: not established. The mod-27 coefficient-extension package detects the valuation layers q=3,9,≥27 on the standard family, but the audited bridge is not an independent universal orientation identity. Test I simultaneously shows that deeper non-graded information becomes visible at increasing finite filtration depth.

Therefore no claim is made that fixed Layer-B data generates all digits. The correct classification is:
- fixed Layer-B tower reuse: OPEN / DECISIVE;
- Bockstein package as finite q-layer detector: PASS / LOCAL;
- Bockstein package as all-digit orientation carrier: CONDITIONAL / OPEN.

### Strategic consequence

The 19D permanent LHS sector is not promoted to “the first new orientation layer.” The next authorized attack is the mod-27 threshold residual:
finite extension data at P_4 or D_10 modulo already established Layer-B information.
If this residual vanishes, the evidence supports collapse/reuse. If it is nonzero and has a natural orientation bridge, it identifies the first genuinely new layer.

Record: research/HARD_ATTACK_57_INFORMATION_DEPTH_AND_LAYER_B_TOWER_2026-09-20.md

## 2026-09-20 — HARD ATTACK 58: MOD-27 THRESHOLD RESIDUAL IDENTIFIED

HA58 executed the authorized mod-27 threshold residual attack. The first new finite filtered information beyond the mod-9 Layer-B carrier appears at the next lower-3-central power/relation layer, at the P_4 threshold (equivalently within the D_10 information window on the Zassenhaus scale).

For the standard family q=3^s:
- q=3: the first power/relation contribution is already absorbed by Layer B;
- q=9: a new nonzero restricted-power/relation class appears in P_3/P_4;
- 27|q: that degree-three residual vanishes modulo P_4.

Thus the residual strictly separates q=9 from 27|q even though both have the same mod-9 orientation value. It is genuinely beyond the fixed Layer-B carrier.

The intrinsic residual is naturally projective: the degree-one torsion line and the symplectic commutator pairing identify its direction with the same orientation direction used at Layer B. What is not yet proved is the scalar normalization that identifies it with the exact second logarithmic digit 3e_2 in H^1(G,Z/9), or a universal natural transformation to chi mod 27.

This means the first new higher information is now a simpler filtered extension datum, not the 19D LHS sector. The 19D branch is superseded as strategic priority, not mathematically disproved.

Decisions:
- higher P_4 power/relation residual exists and detects q=9 vs 27|q: PASS / LOCAL;
- strict separation from Layer B: PASS / LOCAL;
- projective orientation-direction identification: CONDITIONAL / LOCAL;
- normalized mod-27 orientation bridge: OPEN / DECISIVE;
- 19D S as first new layer: HISTORICAL / SUPERSEDED as strategic priority;
- all-digit finite filtered orientation tower: OPEN / DECISIVE.

Next authorized target: P_4 normalization/transport theorem — prove or kill the canonical scalar bridge from the higher power residual to the already normalized mod-9 orientation direction.

Record: research/HARD_ATTACK_58_MOD27_THRESHOLD_RESIDUAL_2026-09-20.md


## 2026-09-20 — HARD ATTACK 59: COKER AS UNIVERSAL OBSTRUCTION QUOTIENT

The conceptual “why coker?” attack was completed. The coker is not itself an orientation invariant; it is the universal quotient removing gauge/lift directions before obstruction evaluation. At mod 9, the established twisted degree-(2,3) obstruction is presentation/lift invariant and therefore factors through the relevant quotient, while orientation is selected by the resulting functional's vanishing/lifting condition.

This yields the structural pattern
\[
\text{raw relation/power data}\to\text{gauge quotient/coker}\to\text{intrinsic obstruction carrier}\to\text{orientation selector}.
\]

The key new research hypothesis is a successive obstruction tower: at P_4 there should be a new gauge quotient and coefficient-extension obstruction whose reduction is compatible with the established mod-9 obstruction. Such compatibility could force the scalar normalization of the second digit without using q or the known orientation formula. Conversely, two inequivalent scalar lifts with identical mod-9 reduction would prove a normalization boundary.

Decision:
- coker as universal gauge-obstruction quotient: **PASS / LOCAL**;
- coker itself as orientation carrier: **FAIL / CLOSED**;
- P_4 reduction-compatibility with mod-9 obstruction: **OPEN / DECISIVE**;
- successive obstruction tower: **OPEN / DECISIVE**.

Record: research/HARD_ATTACK_59_COKERNEL_AS_OBSTRUCTION_QUOTIENT_2026-09-20.md


## 2026-09-20 — HARD ATTACK 61-B

HA61-B structural cancellation audit: the feared independent old-coefficient-action term at the secondary coefficient-extension stage does not survive on the primary-obstruction zero locus. The new obstruction has the form f(t_2)+(mu wedge f)(R), conditional on an intrinsic t_2. The result is PASS / LOCAL. Independent B_rho2 term: FAIL / CLOSED as a separate invariant. Presentation-free t_2: OPEN / LOAD-BEARING. All-digit induction: OPEN / DECISIVE. Next: HA61-C intrinsic t_2 and gauge-independence.

Record: research/HARD_ATTACK_61_B_STRUCTURAL_CANCELLATION_2026-09-20.md (commit 365c5241ba21707119a40090bd5a8cb20bc56366).


## 2026-09-20 — HA61-B SCOPE CORRECTION

Critical review accepted only in part. The q=3/q=9 calculations do establish a strong LOCAL constraint: no independent additive B_rho2 is visible in the audited frozen standard-family branches. However, the earlier claim that delta_2(f)=0 structurally forces every old-rho2 contribution to disappear was too strong. A general secondary term may depend on the A_2 lift z, and its vanishing/absorption requires an explicit full expansion, primary-zero reduction, lift-gauge test, independence test against t_2, and filtration cutoff.

Therefore HA61-B is corrected to **OPEN / LOAD-BEARING**. HA61-A remains **PASS / LOCAL**. The correct next order is B1 origin -> B2 primary-zero reduction -> B3 A_2-lift gauge test -> B4 test whether any survivor is canonically t_2-data -> B5 explicit filtration cutoff. Only then may HA61-C begin. No all-n induction.

Record: research/HARD_ATTACK_61_B_CORRECTION_2026-09-20.md (commit e2d719c7f8e14f4d60a69bfd704dcc2d368e36ae).


## 2026-09-20 — HA61-B2: PRIMARY-ZERO REDUCTION AUDIT

HA61-B2 was executed on the two frozen standard branches with exact HA61-A crossed-word expansions. For q=3, with t=13+9a, the exact relation coefficient is 2+t^{-1}=-9a mod 27; hence the primary obstruction is zero mod 9 and the secondary value is -a f_1. For q=9, z(r)=9(1-a)z_1 mod 27, giving secondary value (1-a)f_1. In both branches, changing the tested A_2 lift by z_1 -> z_1+3c leaves the divided mod-3 obstruction unchanged. Thus primary-zero reduction and lift-representative independence are verified locally, and no independent B_{rho_2} survives in these frozen branches.

This does NOT prove the general primary-zero theorem: arbitrary higher relation jets, arbitrary A_2-lift components, relator gauge, and the E_{>=4} filtration cutoff remain uncontrolled.

Decision:
- HA61-B2: **PASS / LOCAL**;
- HA61-B: **OPEN / LOAD-BEARING**;
- next authorized target: HA61-B3 general A_2-lift gauge test; no HA61-C yet.

Record: research/HARD_ATTACK_61_B2_PRIMARY_ZERO_REDUCTION_2026-09-20.md (commit b82e275cc2621763ea735d878546ea661b3c6563).


## 2026-09-20 — HA61-B3: A_2-LIFT GAUGE ATTACK — SCOPE CORRECTION

HA61-B3 was re-audited at the general cohomological level. For
\[
0\to\mathbf F_3\to A_3=\mathbf Z/27(\rho_3)\to A_2=\mathbf Z/9(\rho_2)\to0,
\]
an \(A_2\)-valued cocycle representative may be changed within its cohomology class by the exact gauge
\[
z\mapsto z+d_{\rho_2}(3\phi).
\]
The connecting homomorphism \(\delta_3:H^1(G,A_2)\to H^2(G,\mathbf F_3)\) is well-defined on cohomology classes, so the **full secondary obstruction** is invariant under this lift-representative gauge:
\[
\Delta_\phi\delta_3=0.
\]
This closes the gauge-dependence question at the level of the total obstruction.

However, this does **not** imply that a decomposition term \(B_{\rho_2}(z)\) vanishes individually. Cancellation with other representative-dependent pieces remains logically possible. In particular, the statement in the earlier HA61-B structural document that the primary-zero condition by itself eliminates every old-action contribution was too strong unless the full source expansion and filtration cutoff are supplied.

The exact current source ledger is:
1. old \(\rho_2\)-action / \(A_2\)-lift terms;
2. new \(\mu\)-prefix × lift terms;
3. relation/power jet terms;
4. the \(P_3/P_4\) residual \(t_2\);
5. lift-gauge cross terms;
6. \(D_4\)/higher-filtration terms.

Primary-zero \(\delta_2(f)=0\) is a **domain condition for the existence of an \(A_2\)-lift**, not by itself a proof that source (1) is absent from every chosen expansion. Therefore the independent-term question remains open until B4/B5 complete the source-by-source independence and filtration audit.

### Decision
- **B3 lift-gauge invariance of the total secondary connecting obstruction: PASS / CLOSED.**
- **B3 old-action elimination / \(B_{\rho_2}=0\): OPEN / LOAD-BEARING.**
- **HA61-B overall: OPEN / LOAD-BEARING.**
- **B4:** test whether any surviving old-action contribution factors canonically through a presentation-free \(t_2\).
- **B5:** explicit coefficient-valuation + filtration cutoff; membership in \(D_4\) alone is not sufficient.
- **HA61-C remains closed/not opened** until B4/B5 are resolved.

This supersedes the stronger HA61-B wording that classified the independent \(B_{\rho_2}\) term as FAIL/CLOSED. The earlier claim is retained only as historical/superseded text; it must not control the current state.


## 2026-09-20 — HA61-B5-6: DIAGONAL GAUGE LAW FALSIFIED AS PURE PRESENTATION ACTION

A deeper attack distinguishes pure relator/presentation gauge from coefficient-extension coordinate/trivialization gauge. For r' = v r v^{-1}, the abstract group G and any intrinsic coefficient character rho_2,rho_3 are unchanged; hence the abstract lift parameter mu in rho_3=rho_2(1+9mu) is unchanged. Therefore the previously written diagonal law (t_2,mu) -> (t_2+a p,mu+a lambda) cannot be attributed to pure relator conjugation.

The law remains a valid obstruction-preserving compensator at the representative/formula level, but its second component is not an actual presentation gauge transformation unless an additional coefficient-trivialization/section action is explicitly constructed.

This exposes a possible missing term/source in the decomposition of the secondary obstruction: the gamma_2^3 / [v,R] contribution may be cancelled by a genuine coefficient-coordinate change or by a representative-level old-action/lift term, rather than by quotienting the orientation parameter mu.

Decision:
- formal diagonal compensator: PASS / LOCAL;
- pure presentation -> diagonal action: FAIL / CLOSED;
- gamma_2^3 independent scalar: FAIL / CLOSED only as a separate functional; gauge role OPEN;
- combined presentation+coefficient gauge action: OPEN / LOAD-BEARING;
- canonical affine quotient: OPEN / LOAD-BEARING;
- HA61-B: OPEN / LOAD-BEARING;
- HA61-C remains unopened.

Record: research/HA61_B5_6_HARD_ATTACK_DIAGONAL_GAUGE_FALSIFICATION_2026-09-20.md

## 2026-09-20 — HA61-B5-7: mu-diagonal quotient ruled out as orientation carrier

A stronger conceptual attack shows that quotienting (t2,mu) by the diagonal direction (p,lambda) would identify distinct coefficient characters rho_3=rho_2(1+9mu), precisely the alternatives the secondary obstruction must distinguish. Presentation/section gauge may change coordinate expressions, but cannot identify distinct intrinsic coefficient actions. Therefore the simple affine quotient is FAIL / CLOSED as the orientation carrier. The correct target is an intrinsic function-valued secondary obstruction on the affine space of coefficient lifts, with presentation-independent value; a representative-dependent t2 may appear only as a coordinate expression of that function.
Record: research/HA61_B5_7_HARD_ATTACK_MU_QUOTIENT_DESTROYS_SELECTOR_2026-09-20.md

## 2026-09-20 — HA61-B5-8: INTRINSIC SECONDARY OBSTRUCTION FUNCTION

HA61-B5-8 closes the correct intrinsic object at the cohomological level. For fixed rho_2, each intrinsic rho_3 lift defines 0 -> F_3 -> Z/27(rho_3) -> Z/9(rho_2) -> 0, hence a canonical connecting map delta_{3,rho_3}. Naturality under group isomorphisms/presentation changes and descent from cocycles to cohomology make rho_3 -> delta_{3,rho_3} intrinsic.

This is PASS / CLOSED for intrinsicity of the function-valued secondary obstruction, but not for the filtered realization. The affine quotient of (t_2,mu) remains FAIL / CLOSED as an orientation carrier because it identifies distinct rho_3 actions.

New diagnostic: under pure relator conjugation intrinsic rho_3/mu is fixed. Hence the previously computed [v,R] contribution lambda(v)f(p) cannot be cancelled by changing mu. The full coordinate expansion must contain another compensating source or revise the decomposition. Next target: coordinate completeness/source audit, P_4 residual identification, and deeper-term factorization. HA61-C remains unopened.

Record: research/HA61_B5_8_INTRINSIC_SECONDARY_OBSTRUCTION_FUNCTION_2026-09-20.md.

## 2026-09-20 — HA61-B5-9: PURE RELATOR CONJUGATION EXACT CANCELLATION

The full crossed-cocycle identity was independently checked: for r'=v r v^{-1}, z(r')=0 exactly whenever z(r)=0 and rho_3(r)=1. Hence the intrinsic obstruction is presentation-conjugation invariant at every filtration order. Because rho_3/mu is fixed, the isolated [v,R] contribution lambda(v)f(p) cannot be cancelled by changing mu. It must be cancelled by other representative-level terms from the full conjugated word, including prefix/suffix contributions omitted when only P -> P+[v,R] was tracked.

This is PASS / LOCAL for exact invariance and FAIL / CLOSED for treating [v,R] as the complete gauge contribution. The explicit cancellation partner remains OPEN / LOAD-BEARING and is now the immediate source-level target. HA61-B remains OPEN / LOAD-BEARING; HA61-C unopened.

Record: research/HA61_B5_9_PURE_RELATOR_CONJUGATION_EXACT_CANCELLATION_2026-09-20.md.

## 2026-09-20 — HA61-B5-13: INTRINSIC ZERO-SELECTOR ATTACK

The single-vector t2 route is now closed. The surviving intrinsic family rho_3 -> delta_{3,rho_3} is being attacked directly as a zero-selector on the coefficient-lift torsor L(rho_2), rather than compressed to a presentation-independent vector. For a primary-zero class f, define Z_3(f)={rho_3: delta_{3,rho_3}(f)=0}. The decisive candidate theorem is that two lifts rho_3' = rho_3(1+9 nu) differ intrinsically by the cup-pairing term delta_{3,rho_3'}(f)-delta_{3,rho_3}(f)=nu cup f (up to the already-fixed common H^2 sign convention). If proved, Demushkin cup nondegeneracy gives uniqueness for nonzero f; existence must be proved separately from finite filtered/relation input and without importing the canonical orientation. This is a new OPEN / DECISIVE target, not a resurrection of t2. The novelty gate is explicit: Serre's classical orientation characterization already uses successive H^1 coefficient-lifting surjectivity, so the project must prove a genuine factorization from the declared filtered/relation input to this finite obstruction family rather than merely restating the known orientation definition.

Record: research/HA61_B5_13_INTRINSIC_ZERO_SELECTOR_2026-09-20.md (commit 1c4ecb8c9b8336f9f9fb1e5ae87e156184f16bfb).

## 2026-09-20 — B5-13 CRITICAL CORRECTION

The proposed uniqueness argument for the intrinsic delta3 zero-selector was wrong. A nonzero linear functional nu -> nu cup f on the 4-dimensional H^1(G,F3) is not injective; its kernel has dimension 3. Therefore, if the variation formula holds and one zero exists, the full coefficient-lift torsor has an affine zero set of size 27, not a singleton. B5-13 zero-selector uniqueness is FAIL/CLOSED. The variation identity remains OPEN/DECISIVE. The next legitimate question is whether the filtered data canonically selects a one-dimensional affine lift direction (or another quotient/structure) before zero-selection. Such a restriction cannot be introduced without a fresh Object/Input/Functoriality/Gauge/Novelty audit.


## 2026-09-20 — HA61-B5-14: GLOBAL ZERO-MAP QUANTIFIER CORRECTION

A critical quantifier correction supersedes the fixed-(f) no-go interpretation in B5-13. For fixed (f), the variation (
u\mapsto\nu\smile f) has a 3-dimensional kernel in rank four, so (Z_3(f)) can have 27 points. But the research selector is the stronger condition (delta_{3,
ho_3}\equiv0) as a map on all of (H^1(G,\mathbf Z/9(\rho_2))). If the universal variation identity holds and the reduction (H^1(G,\mathbf Z/9(\rho_2))\to H^1(G,\mathbf F_3)) is surjective, then two global zero maps imply (
u\smile v=0) for every (v\in H^1(G,\mathbf F_3)); Demuškin cup nondegeneracy forces (
u=0). Thus **global zero-map uniqueness is PASS / LOCAL conditional on the variation identity and reduction-surjectivity hypotheses**. The fixed-(f) 27-point argument is **HISTORICAL / SUPERSEDED as a no-go for the global selector**. Universal variation, existence from finite filtered/relation input, finite-window factorization through (G/P_4\) / (D_{10}), and Serre/Kummer novelty separation remain **OPEN / DECISIVE**. The (t_2) and diagonal quotient routes remain closed and are not revived.

Record: research/HA61_B5_14_GLOBAL_ZERO_MAP_QUANTIFIER_CORRECTION_2026-09-20.md


## 2026-09-21 — B2 FINITE KUMMER SELECTOR: GENERAL-k CLOSURE

The previous load-bearing finite-window step is now closed by a direct induction. For A_k=Z/3^k, U_j=1+3^j Z/3^k and S_k=A_k⋊U_1, with T_j=3^{j-1}A_k⋊U_j, one proves P_j(S_k)=T_j for every j. Hence P_{k+1}(S_k)=1 and P_k(S_k)≠1. Any crossed cocycle z together with rho gives psi=(z,rho):G→S_k, and functoriality of the lower 3-central series gives psi(P_{k+1}(G))=1. Thus the crossed cochain problem factors through Q_k=G/P_{k+1}(G), yielding the finite-window H^1 identification. **1-A: PASS.**

The Kummer lifting predicate is equivalent to the vanishing of the twisted Fox row. If I=(F_i(rho)) in R=Z/3^k, surjectivity of H^1(R(rho))→H^1(F_3) gives I⊂3I by lifting each basis vector; Nakayama then gives I=0. The converse is immediate. **Fox–Kummer equivalence: PASS.**

For the standard odd-p Demushkin relation r=x_1^q[x_1,x_2]...[x_{2m-1},x_{2m}], the Fox equations directly force rho_{2i-1}=1, then rho_{2i}=1 for i>1, and finally rho_2=(1-q)^(-1). Thus existence/uniqueness is obtained by direct elimination; Hensel is no longer a proof dependency. Labute classification extends this from the standard presentation to arbitrary odd-p Demushkin groups. **PASS / LOCAL.**

The novelty gate remains OPEN / DECISIVE. Existing literature already characterizes the canonical orientation/Kummerian orientation through surjectivity of H^1(G,Z_p(theta)/p^n)→H^1(G,F_p) for all n. The remaining question is specifically whether the finite-window factorization/recognition formulation on Q_k=G/P_{k+1}, with chi/q/dualizing action absent from the predicate input, is already known or is a genuinely new finite-group formulation. Record: research/B2_FINITE_KUMMER_SELECTOR_GENERAL_K_2026-09-21.md (commit 542b3d8b767a8c65500c92273a3de573112c1367).


## 2026-09-21 — ONE-RELATOR KUMMER SELECTOR STRESS TEST

The authorized scope/generalization experiment was executed outside the standard Demushkin relation. The historical step3.py file was not present in the repository tree, so an independent fresh Fox evaluator was used; this is explicitly a diagnostic implementation, not a rerun of that script.

Exhaustive finite-character enumeration at k=2,3 was performed for standard rank-4 Demushkin, power-free symplectic control, degenerate rank-4/rank-3 commutator relations, and power+degenerate relations. The standard Demushkin relation retains a unique selector: (1,4,1,1) mod 9 and (1,13,1,1) mod 27. The power-free symplectic control has the unique trivial selector. Degenerate relations show selector non-uniqueness: [x1,x2][x2,x3] has 3 solutions at k=2 and 9 at k=3; [x1,x2][x1,x3] has the same 3-to-9 growth. The relation x1^3[x1,x2][x1,x3] also has 3 and 9 solutions, while x1^3[x1,x2][x2,x3] has no solution at either k=2 or k=3.

This is a genuine boundary diagnostic: Demushkin-type nondegeneracy gives rigidity, while degenerate one-relator quadratic data can produce positive-dimensional finite Kummer candidate families or no candidate at all. It does NOT prove or disprove automatic vanishing of the intrinsic higher obstruction \barδ4∘ι1. The next authorized experiment is to compute that actual coefficient-extension obstruction for the multiple-selector relation [x1,x2][x1,x3].

Decision: **ONE-RELATOR STRESS TEST = PASS / LOCAL.** Record: research/ONE_RELATOR_KUMMER_SELECTOR_STRESS_TEST_2026-09-21.md (commit f61d879a6e11bf24a94ea34a0360530e36575224).

## 2026-09-21 — B2 LITERATURE/QUOTIENT CORRECTION

The Kθ-vs-P_{k+1} audit was tightened. Efrat–Quadrelli/Quadrelli quotient inheritance requires conditions such as N⊆Kθ(G) or N⊆ker θ for an already-given infinite orientation. This does not by itself imply the finite-window theorem for N=P_{k+1}. However, it is too strong to say the required inclusions are false: for the finite coefficient character θ mod 3^k, P_{k+1}⊆ker(θ mod 3^k) is in fact true. The unresolved literature gate is specifically whether a finite-coefficient/mod-3^n version with K_{θ mod 3^n} or equivalent quotient inheritance already subsumes the construction.

Therefore the prior statement that the quotient route could be “excluded” is HISTORICAL / SUPERSEDED. Current status: mathematical B2 gates remain PASS; novelty remains **OPEN / LOW-LIKELIHOOD — LITERATURE VERIFICATION REQUIRED** pending this finite-coefficient comparison.


## 2026-09-21 — NOVELTY GATE: CANONICAL ORIENTATION VS FILTRATION-ONLY RECONSTRUCTION

Primary-source literature audit was completed against the uploaded Labute paper (1967, *Classification of Demushkin Groups*) and the uploaded modern oriented/Kummerian Demushkin literature (arXiv:1707.07018v3 and arXiv:2103.12438v3).

### Established by prior literature
- Existence and uniqueness of the canonical/Serre orientation \(\chi:G\to\mathbf Z_p^\times\) for Demushkin groups are classical (Labute, Theorem 4).
- \(\operatorname{Im}\chi\) and the associated \(q(G)\) are invariants; classification by rank and image is classical (Labute).
- Demushkin orientation is already treated in modern cyclotomic/oriented/Kummerian language in the later literature.
- Use of the descending central/Zassenhaus-type filtration and associated graded Lie algebra in Demushkin structure/classification is also not new (Labute §2).

### Exact novelty boundary
The literature checked does NOT, in the audited statements, supply the stronger factorization/reconstruction claim
\[
\operatorname{Fil}_{\mathrm{intr}}(G)\longrightarrow\chi_G
\]
where the input is restricted to an intrinsically defined Zassenhaus/Jennings--Lazard filtered/graded object and no presentation/basis/orientation is supplied. Likewise, a direct theorem that \(G/P_{k+1}\) alone canonically recognizes \(\chi\bmod 3^k\) has not been identified in this audit.

Therefore the original broad claim “recover the canonical orientation of a Demushkin group” is **FAIL / CLOSED as a novelty claim**. The surviving research question is the narrower **filtration-only / finite-window factorization problem**, currently **OPEN / NOVELTY GATE NOT YET CLOSED**.

This does not prove publication-level novelty: the finite-coefficient quotient literature must still be checked against the exact \(G/P_{k+1}\) recognition predicate and the project's non-tautological input category. In particular, existing Kummerian/oriented quotient-inheritance results must not be silently treated as either identical to or distinct from the finite-window theorem until the hypotheses are compared line-by-line.

### Research consequence
Do not describe the project as discovering canonical Demushkin orientation. Describe the candidate contribution, if ultimately proved, as an intrinsic filtered/finite-quotient reconstruction or factorization theorem for the already-known canonical orientation.

Decision:
- classical canonical orientation existence/uniqueness: **FAIL / CLOSED**;
- filtration/graded methods in Demushkin theory: **FAIL / CLOSED as novelty**;
- intrinsic filtration → orientation factorization: **OPEN**;
- finite-window \(G/P_{k+1}\to\chi\bmod 3^k\): **OPEN / LITERATURE VERIFICATION REQUIRED**;
- overall novelty of the present project: **OPEN / CONDITIONAL**.


## 2026-09-24 — U5 INTRINSIC UNIQUENESS ATTACK: INDUCTION THROUGH COEFFICIENT EXTENSIONS

The authorized U5 attack was executed without new Fox expansion. A level-k candidate rho_k reducing to the unique level-(k-1) candidate chi_{k-1} differs from another lift by 1+3^{k-1}nu, nu in H^1(G,F_3). Each lift defines an intrinsic coefficient extension 0 -> A_{k-1}(chi_{k-1}) -> A_k(rho_k) -> F_3 -> 0 and hence a connecting map delta_{rho_k}: H^1(G,F_3) -> H^2(G,A_{k-1}(chi_{k-1})).

The load-bearing variation identity is delta_{rho_k'}-delta_{rho_k} = iota_{k-1} o (nu cup -), where iota_{k-1} is induced by the socle inclusion F_3 -> A_{k-1}(chi_{k-1}). This is a coefficient-extension/Yoneda naturality statement and is presentation/Fox independent.

For a Demushkin group, PD^2 duality with the canonical dualizing orientation should make iota_{k-1} injective on H^2. Therefore two level-k zero connecting maps imply nu cup v=0 for every v in H^1(G,F_3), and cup nondegeneracy gives nu=0. Existence is supplied by the known Kummerian canonical orientation; U1-U2 then factor the finite predicate through Q_k=G/P_{k+1}.

Decision:
- intrinsic induction mechanism: PASS / LOCAL;
- U5 uniqueness: PASS / CONDITIONAL, pending complete proof of the coefficient-extension variation lemma and the PD^2 socle-injectivity lemma;
- finite-window factorization/recognition: OPEN / DECISIVE pending exact literature comparison;
- no Fox route reopened.
Record: research/U5_INTRINSIC_UNIQUENESS_INDUCTION_2026-09-24.md.


## 2026-09-24 — FINAL LITERATURE GATE: FINITE-WINDOW THEOREM NOT IDENTIFIED IN CHECKED LITERATURE

The final literature comparison was completed against Labute (1967), Efrat–Quadrelli (2019), Quadrelli–Weigel (2020, 2022), and the later 2024 oriented/Kummerian treatment.

Established prior art:
- Labute's classical result gives existence/uniqueness of the canonical Demuškin orientation and the cocycle/Kummerian criterion.
- Efrat–Quadrelli and subsequent work formulate Kummerianity by surjectivity of H^1(G,Z_p(theta)/p^n) -> H^1(G,F_p), and give quotient-inheritance results, but with hypotheses involving an already-given orientation and an additional restriction-map condition.
- The checked literature also uses the Zassenhaus filtration and finite quotients for other cohomological/Galois-theoretic purposes.

Exact comparison:
No checked source states, in the required classification-free/q-blind input category, the theorem that for Q_k=G/P_{k+1} the intrinsic predicate
K_k(Q_k,rho): H^1(Q_k,Z/3^k(rho)) -> H^1(Q_k,F_3) is surjective
recognizes exactly rho=chi_G mod 3^k for every k>=2, with the factorization through Q_k proved for arbitrary candidate rho rather than starting from an already-given chi.

The nearest known results therefore do NOT collapse the present theorem by direct citation. In particular, Proposition 2.10-type quotient inheritance cannot simply be invoked: its hypotheses concern a pre-existing oriented Kummerian pair and a surjective restriction map, whereas the present construction's point is to recognize the orientation from the finite quotient without supplying it in advance.

Novelty decision: **PASS / CONDITIONAL — literature-based novelty survives the checked sources, but publication-level novelty must be phrased narrowly and verified against any additional references discovered during peer review.** The broad claim “canonical Demuškin orientation is new” remains closed/non-novel.

The theorem statement is therefore fixed as the finite-window recognition/factorization theorem:
\[
\boxed{\mathsf K_k(G/P_{k+1},\rho)\iff \rho=\chi_G\bmod 3^k,\qquad k\ge2,}
\]
where the predicate is defined intrinsically on Q_k and no presentation coordinate, q, dualizing action, or pre-supplied canonical orientation is part of the selector input. The proof architecture is: (i) arbitrary-candidate crossed-cocycle factorization through Q_k; (ii) Kummerian existence for the canonical orientation; (iii) coefficient-extension variation identity; (iv) PD^2 socle injectivity; (v) cup-product nondegeneracy for uniqueness.

Status after this Gate:
- mathematical theorem: **PASS / CLOSED**
- exact finite-window novelty against checked literature: **PASS / CONDITIONAL**
- theorem statement: **FIXED**
- new computational/math attacks: **CLOSED** unless a referee/literature check identifies a direct prior equivalent theorem.

Key sources checked: Labute 1967; Efrat–Quadrelli 2019; Quadrelli–Weigel 2020 and 2022; Quadrelli 2024.


## 2026-09-24 — PAPER STRUCTURE BASELINE + NOVELTY STATUS CORRECTION

A publication-structure review was completed for the closed U1–U5 program. A dedicated baseline document was created at `paper/PAPER_STRUCTURE_BASELINE.md` (commit 58de6b37e48f8d93f9a5303bfb8a4bfecfb45c41). This document is the working foundation for `paper/main.tex`; it is not itself a novelty claim.

### Publication architecture fixed
The main paper is to be organized around the finite-window recognition theorem, not around the historical sequence of research attacks:
1. Introduction: known global Kummerian/cyclotomic orientation theory; finite-window question; brief information-boundary motivation; main theorem; prior-work/novelty boundary.
2. Finite coefficient extensions and the finite window: U1 lower 3-central filtration of S_k=A_k semidirect U_1 and U2 factorization through Q_k=G/P_{k+1}.
3. Finite Kummer criterion: U3, with the corrected iterative/Nakayama proof of Kummer lifting iff vanishing of the twisted Fox row.
4. Identification in the standard presentation: U4 as a presentation-dependent/local calculation identifying rho(x_2)=(1-q)^(-1); (1,40,1,1) mod 81 is only the k=4 example.
5. Intrinsic uniqueness via PD^2: U5 variation formula, coefficient-extension injectivity, and cup-product nondegeneracy.
6. Main finite-window recognition theorem, assembling U1-U5.
7. Relation to previous work and exact novelty boundary.
8. Brief information-boundary discussion.

### Information-boundary results
The earlier negative results are retained as motivation/lower-bound context, not as a second full contribution in this manuscript: graded data alone do not determine chi mod 9; a single t_2 carrier does not determine chi; the successful object is the function-valued Kummer/lifting obstruction on the finite filtered quotient. Full proofs and the still-open minimal-carrier problem should be reserved for a possible companion paper.

### Appendix policy
Research files research/U1.md–U5.md are audit records and should NOT be pasted verbatim into the paper. Publication appendices should contain rewritten technical details only (semidirect filtration, twisted Fox calculation, PD^2/coefficient-extension details, and optional computational verification).

### Important claim-precision rules
- “q-blind” means q is not an input to the selector; it does not assert a uniform theorem for all q.
- “presentation-free” means the final predicate/theorem is intrinsic; a standard presentation may be used as an intermediate verification device.
- “Q_k suffices” means the relevant twisted H^1/Kummer obstruction factors through Q_k, not that Q_k determines all of G.
- Canonical orientation existence/uniqueness is classical and must not be presented as the novelty.

### Novelty-status correction
The previous 2026-09-24 entry labeled literature novelty “PASS / CONDITIONAL” is now superseded for manuscript purposes. The checked sources establish the classical Kummerian/cyclotomic characterization and related quotient results, but the literature audit was not a complete line-by-line exclusion of every equivalent finite-window formulation. Therefore the defensible current status is:
- mathematical finite-window theorem: PASS / CLOSED;
- exact publication-level novelty: OPEN / STRONG CANDIDATE;
- broad claim of discovering canonical Demuškin orientation: CLOSED / NON-NOVEL.

Before submission, the novelty statement must remain narrow and be tied to source-level comparison, especially the exact depth P_{k+1}, arbitrary candidate rho, absence of pre-supplied chi/q/dualizing action, and the automatic factorization of arbitrary twisted crossed cocycles.

No new mathematical attack is authorized merely to improve the manuscript. The next work is theorem-hypothesis cleanup, publication-style rewriting of U1-U5, and exact source verification where needed.


## 2026-09-24 — N1–N5 CRITICAL REVIEW / MANUSCRIPT-CONTROLLING UPDATE

Before finalizing N5, N1–N4 were rechecked for logical overreach.

**N1:** Kummerian/cyclotomic lifting and canonical Demuškin orientation uniqueness are known. This is prior art.

**N2:** Existing quotient-inheritance results do not automatically imply the present recognition theorem. Their direction starts from an already Kummerian oriented pair; the present problem starts with an arbitrary finite candidate rho.

**N3:** Full-group finite-level uniqueness is historical/non-novel. Labute Proposition 6/Theorem 4 and Efrat–Quadrelli Proposition 7.3/Theorem 7.6 already supply the all-level lifting criterion and unique Demuškin orientation.

**N4:** The mathematical factorization is now PASS/CLOSED: U1–U2 prove that arbitrary rho-twisted crossed cocycles factor through Q_k=G/P_{k+1}. This is a project theorem, but the fact that it is proved does not by itself settle publication novelty.

**N5:** The audited corpus contains no exact theorem stating that the bare finite quotient Q_k carries the functorial predicate K_k(Q_k,rho) whose unique candidate is chi_G mod 3^k, with arbitrary-candidate factorization. Therefore the exact novelty candidate survives **conditionally**. This is not an absolute priority claim.

**Important scope correction:** the current theorem is for the fixed rank-4 q=3 Demuškin group. “q-blind” means q is not an input to the selector, not that the theorem is uniform over all q.

**Depth correction:** P_{k+1} is proved sufficient; minimality is OPEN. Do not use “minimal finite window.”

**U5 proof correction:** variation is a coefficient-extension/Yoneda lemma; PD² injectivity must be presented using exact coefficient duals and the dual reduction map. Classical Kummerian existence is imported.

Decision:
- mathematical theorem: **PASS/CLOSED**;
- exact literature novelty against checked sources: **PASS/CONDITIONAL**;
- broad canonical-orientation novelty: **CLOSED/NON-NOVEL**;
- minimal depth: **OPEN**.

This entry controls manuscript wording over earlier contradictory novelty labels.


## 2026-09-25 — PAPER MANUSCRIPT / LITERATURE MERGE AUDIT

The manuscript `paper/main.tex` was compared against the controlling U5/N1 records and the audited Kummerian/cyclotomic literature. The objective was explicitly to take only supported improvements, not to import unverified claims.

Key manuscript corrections:
- candidate characters are now explicitly principal-unit characters `rho:Q_k -> U_{1,k}=1+3(Z/3^k)`;
- the intrinsic finite Kummer predicate is separated from all presentation/Fox coordinates;
- finite-depth factorization is given its own logical section before the coordinate base-case calculation;
- classical full-group Kummerian/canonical-orientation results are explicitly treated as known background;
- q-blindness is defined as absence of q from selector input, not uniformity over the Demushkin family;
- P_{k+1} is stated as sufficient, with minimality left OPEN;
- novelty wording is restricted to the exact combined bare-Q_k/arbitrary-candidate/factorization formulation and remains conditional on the audited corpus.

No closed branch was revived, no uniform-in-q theorem was claimed, and no recent uploaded paper was treated as proving the finite selector unless supported by the controlling audit.

Classification:
- manuscript finite-window theorem: PASS/CLOSED under the current fixed-group hypotheses and U5 proof;
- classical Kummerian orientation as novelty: HISTORICAL/SUPERSEDED;
- exact publication novelty: PASS/CONDITIONAL;
- minimality: OPEN;
- family-wide generalization: OPEN.

Detailed manuscript audit: `research/PAPER_LITERATURE_MERGE_AUDIT_2026-09-25.md`.
Commit: `46eaa54ccc34ab7eafa1680624e221653ff885de`.


## 2026-09-25 — PROP. 2.10 RESTRICTION-SURJECTIVITY HARD ATTACK / N2 SHARPENED

The proposed second follow-up problem was tested against the exact 2024 Proposition 2.10 statement. That proposition assumes an already Kummerian oriented pair (G,theta), N⊂ker(theta), and surjectivity of
res^1_{G,N}: H^1(G,F_p) -> H^1(N,F_p)^G.
Its proof explicitly uses the dual inclusion
N/N^p[G,N] -> G/Phi(G).

For the present N=P_{k+1}(G), p=3, one has N⊂Phi(G), hence the dual inclusion map is zero. At the same time the relevant relative Frattini quotient is nonzero: P_{k+1}/P_{k+2}≠0, while P_{k+1}^3[P_{k+1},G]⊂P_{k+2}. Therefore
P_{k+1}/P_{k+1}^3[P_{k+1},G] != 0,
so the dual map is not injective and the restriction map is not surjective.

Decision: FAIL / CLOSED for automatic restriction-surjectivity. Consequently Proposition 2.10 cannot be used with N=P_{k+1} as an automatic corollary mechanism for the present finite-window theorem.

This does not itself prove absolute novelty. It removes one concrete quotient-inheritance collapse route. The U1–U5 theorem remains PASS/CLOSED and exact publication novelty remains OPEN/CONDITIONAL.

Record: research/PROP_2_10_RESTRICTION_SURJECTIVITY_HARD_ATTACK_2026-09-25.md (commit 5439b06cf45faa6042225ab3e338997c10f2301a).


## 2026-09-25 — CORRECTION / SCOPE TIGHTENING OF PROP. 2.10 ATTACK

The previous entry stated the nonvanishing of P_{k+1}/P_{k+2} uniformly in k without separately recording the needed graded-dimension argument. That is stronger than necessary and is superseded.

The decisive result needs only k=2:
for the rank-4 p=3 Demushkin group, the published Zassenhaus dimension formula gives
dim_F3(P_3/P_4)=c_3=(4^3-4)/3=20.
Hence P_3/P_4 is nonzero, while P_3^3[P_3,G]⊂P_4. Since P_3⊂Phi(G), the dual inclusion
P_3/P_3^3[P_3,G] -> G/Phi(G)
is zero and has nonzero source. Therefore
H^1(G,F_3) -> H^1(P_3,F_3)^G
is not surjective.

This single k=2 counterexample is sufficient to classify automatic Prop. 2.10 restriction-surjectivity as FAIL/CLOSED. Any all-k nonvanishing strengthening is left unclaimed pending a separate explicit proof.

Record correction: research/PROP_2_10_RESTRICTION_SURJECTIVITY_HARD_ATTACK_2026-09-25.md, commit 70dad1bcab1145590d5a06b125dcf07b9249e7e5.


## 2026-09-25 — PROP. 2.10 PRIMARY-SOURCE VERIFICATION / FINAL SCOPE CORRECTION

Quadrelli (2024) Proposition 2.10 was checked directly. The proposition requires N contained in ker(theta) and surjectivity of H^1(G,F_p) -> H^1(N,F_p)^G. Its proof explicitly uses the dual inclusion N/N^p[G,N] -> G/Phi(G), and the kernel condition again later in the cocycle descent argument.

The Minac–Rogelstad–Nguyen Duy Tan Zassenhaus dimension formula was also checked directly: for a p=3 Demushkin group of rank d, c_3=(d^3-d)/3. Thus for d=4, c_3=20, so P_3/P_4 is nonzero. Since P_3^3[P_3,G] is contained in P_4 and P_3 is contained in Phi(G), the dual inclusion has nonzero source and is zero. Therefore H^1(G,F_3) -> H^1(P_3,F_3)^G is not surjective.

Classification: automatic restriction-surjectivity for N=P_{k+1} is FAIL / CLOSED. This is sufficient to kill the proposed automaticity claim using k=2 only. The all-k nonvanishing statement is not claimed.

Critical scope correction: P_3 itself is not automatically an admissible N for Prop. 2.10 because the proposition separately requires P_3 contained in ker(chi). Therefore the earlier statement that the entire Prop. 2.10 shortcut was closed by the P_3 restriction failure is superseded. An admissible kernel-contained counterexample such as N=P_3 intersect ker(chi) requires a separate proof of nonzero relative Frattini quotient; that branch is OPEN and the tentative x_2^3 modulo 27 argument is not promoted.

Final status: Prop. 2.10 statement/proof PASS / CLOSED; duality PASS / CLOSED; c_3=20 PASS / CLOSED; P_3 restriction nonsurjectivity PASS / CLOSED; automaticity FAIL / CLOSED; admissible kernel-contained counterexample OPEN; Prop. 2.10 as a complete shortcut OPEN / CONDITIONAL; publication novelty OPEN / CONDITIONAL.

Record: research/PROP_2_10_RESTRICTION_SURJECTIVITY_HARD_ATTACK_2026-09-25.md, commit 7147923991ed9960e9019ac465832f3bc90d5a1b.


## 2026-09-25 — KERNEL-CONTAINED PROP. 2.10 COUNTEREXAMPLE CLOSED

The previously OPEN branch N=P_3 intersect ker(chi) is now closed negatively by a cleaner commutator argument. Since chi is abelian-valued, [P_2,G] is contained in ker(chi), and the Zassenhaus commutator rule gives [P_2,G] contained in P_3; hence [P_2,G] is contained in N.

In the associated restricted graded Lie algebra, the initial Demushkin relation is R=[X_1,X_2]+[X_3,X_4] in degree 2. The degree-3 relation space is span{[R,X_i]:1<=i<=4}. Direct coefficient linear algebra over F_3 in the free associative degree-3 space gives rank 4 for these four relation vectors, while adjoining [[X_1,X_2],X_1] gives rank 5. Thus [[X_1,X_2],X_1] survives in degree 3, so [P_2,G] is not contained in P_4.

Therefore N/P_4 is nonzero. Also N^3[N,G] is contained in P_4, while N is contained in Phi(G). Hence N/N^3[N,G] is nonzero and the inclusion-induced map to G/Phi(G) is zero. By Quadrelli Prop. 2.10 duality, H^1(G,F_3) -> H^1(N,F_3)^G is not surjective.

Classification update: N=P_3 intersect ker(chi) admissibility PASS/CLOSED; relative Frattini quotient nonzero PASS/CLOSED; restriction nonsurjectivity PASS/CLOSED; automatic Prop. 2.10 shortcut through this natural kernel-contained N FAIL/CLOSED. This does not assert a universal impossibility for every specially chosen N; that stronger statement is unnecessary.

Record: research/PROP_2_10_RESTRICTION_SURJECTIVITY_HARD_ATTACK_2026-09-25.md, commit 5f6ec4c98d7831ef61a73bb97ea58176d4096df2.

## 2026-09-25 — PROP. 2.10 PRIOR-ART AUDIT / NEGATIVE RESULT SEPARATION

A targeted literature audit was performed for the negative result that, in the rank-4 p=3 Demushkin case, the restriction map H^1(G,F_3) -> H^1(P_3,F_3)^G is not surjective, so Quadrelli (2024) Proposition 2.10 cannot be applied automatically with N=P_3.

The exact source statement was checked line-by-line. Proposition 2.10 assumes an already Kummerian oriented pair, N subset ker(theta), and surjectivity of the restriction map. Its proof explicitly uses the dual injection N/N^p[G,N] -> G/Phi(G). For N=P_3, our k=2 argument gives the opposite: P_3 subset Phi(G), while the source P_3/P_3^3[P_3,G] is nonzero because the published Zassenhaus dimension formula gives dim_F3(P_3/P_4)=c_3=(4^3-4)/3=20, and P_3^3[P_3,G] subset P_4. Hence the dual map is zero on a nonzero source and restriction is not surjective.

Prior-art comparison found the ingredients are known: Proposition 2.10 itself, standard Frattini/Zassenhaus facts, and the Demushkin graded-dimension formula (Mináč–Rogelstad–Tân 2014). Targeted searches did not locate a source explicitly stating this exact composite application to N=P_3 or N=P_{k+1} as a Demushkin obstruction.

Therefore this negative result is not claimed as a new theorem. Its publication value is narrower: it is a PASS / CONDITIONAL prior-art separation lemma showing that one concrete known quotient-inheritance route does not subsume the finite-window theorem. The direct-collapse route through Proposition 2.10 is FAIL / CLOSED.

Record: research/PROP_2_10_PRIOR_ART_AUDIT_2026-09-25.md (commit 0670bf431dcd17fa205ef33c8979d3c055b4263c).


## 2026-09-25 — U1–U5 MANUSCRIPT-ONLY PROOF AUDIT / SECOND PASS

The manuscript was re-audited using the actual current paper/main.tex, rather than relying on earlier research summaries.

### U1–U3
U1 finite-depth semidirect filtration was rechecked at the indexing level. With
\(T_j=3^{j-1}A_k\rtimes U_j\), \(U_j=1+3^jA_k\), one has
\(T_j^3\subseteq3^jA_k\rtimes U_{j+1}\) and
\([T_j,S_k]=3^jA_k\); the commutator with \(4\in U_1\) supplies all of
\(3^jA_k\) because \(4^{-1}-1=-3/4\) is a 3-adic unit times 3.
The induction \(P_j(S_k)=T_j\) is therefore consistent, including the terminal
\(P_{k+1}=1\).

U2 was rechecked as a genuine arbitrary-candidate statement: a crossed cocycle
and its character form a homomorphism into \(S_k\), so functoriality of the
Zassenhaus/lower-3 filtration forces \(P_{k+1}(G)\) into the kernel. Hence both
the candidate and every cocycle factor through \(Q_k\), and the cohomology
identification is not restricted to the canonical orientation.

U3 valuation induction remains valid. The principal-unit hypothesis makes the
residual coefficient action trivial, minimality identifies mod-3 classes with
generator-value vectors, and surjectivity successively forces every twisted Fox
coefficient into \(3^mA_k\) for all \(m\), hence to zero.

### U4 — GAP FOUND AND CLOSED
The earlier manuscript sentence “standard odd-p Demushkin calculation gives”
was judged insufficient as the proof base because U4 is the induction anchor.
It has now been replaced by a self-contained mod-9 twisted-cocycle/Fox
calculation.

For \(a_i=\rho_2(x_i)\in\{1,4,7\}\subset\mathbf Z/9\mathbf Z\), the relation
\(r=x_1^3[x_1,x_2][x_3,x_4]\) gives
\[
F_1=(a_1^2+a_1a_2+a_2)/a_2,\quad
F_2=a_1^2(a_1-1)/a_2,
\]
\[
F_3=-a_1^3(a_4-1)/(a_3a_4),\quad
F_4=a_1^3(a_3-1)/(a_3a_4).
\]
By U3, Kummer lifting is equivalent to \(F_i=0\). Thus
\(F_2=0\Rightarrow a_1=1\), \(F_3=F_4=0\Rightarrow a_3=a_4=1\), and
\(F_1=0\Rightarrow1+2a_2=0\pmod9\Rightarrow a_2=4\).
Therefore the unique level-2 candidate is \((1,4,1,1)\), equal to the canonical
orientation modulo 9. This closes U4 without using the desired theorem
circularly.

### U5b — COCHAIN-LEVEL GAP TIGHTENED
The coefficient extension is now written explicitly as
\[
0\to A_{k-1}(\rho_{k-1})\xrightarrow{j}A_k(\rho_k)\to\mathbf F_3\to0,
\qquad j(a)=3a.
\]
For a common section \(s(1)=1\), the difference of connecting cochains is
computed before passing to cohomology:
\[
d_s'c-d_sc=3^{k-1}(\nu\smile c)
=j(3^{k-2}(\nu\smile c)).
\]
With \(\iota(1)=3^{k-2}\), this yields
\[
\delta_{\rho_k'}-\delta_{\rho_k}=\iota_*(\nu\smile-)
\]
for the convention \((\nu\smile c)(g,h)=\nu(g)c(h)\). The sign is now fixed
rather than hidden under “cocycle identities show”.

### U5c — NATURALITY GAP TIGHTENED
The PD2 duality argument was expanded to identify the dual map explicitly.
For \(M=A_{k-1}(\chi_{k-1})\),
\[
M^\vee\otimes I\cong A_{k-1}
\]
with trivial action. Under the natural duality identification, precomposition
with the socle inclusion \(1\mapsto3^{k-2}\) sends \(a\) to
\(a\,3^{k-2}/3^{k-1}=a/3\), i.e. reduction modulo 3. Therefore the dual of
\(\iota_*\) is the surjective reduction map \(A_{k-1}\twoheadrightarrow\mathbf F_3\),
so \(\iota_*\) is injective.

### U5 status
After these changes, U5 is internally closed at the cochain and duality-map
levels, subject to the standard PD2 duality theorem and the stated convention
that \(\chi\) is the action on the dualizing module. The remaining nondegenerate
cup pairing is exactly the Demushkin defining property.

### LITERATURE CHECK
A fresh targeted search found Quadrelli (2024), Proposition 2.10, explicitly
stating Kummerian quotient inheritance under the restriction-surjectivity
hypothesis. The manuscript's separation from this result is therefore correctly
framed as a failure of that hypothesis for the natural \(N=P_3\), not as a claim
that quotient inheritance is unknown. Searches for finite-level / mod-\(p^n\)
Kummerian recognition of an arbitrary candidate on a Zassenhaus quotient did not
locate an exact theorem matching the present selector statement.

### BUILD CHECK
A three-pass pdflatex compilation of the manuscript state containing the U4
closure and tightened U5b/U5c completed with exit status 0, no undefined-reference
or LaTeX warning/error matches in the final pass, and produced an 8-page PDF.
The compiled PDF is an audit build; the GitHub source update itself is commit
3af1ec738614dbbb92b21e965cd4b7163ee7a664.

Status: U1 PASS/CLOSED; U2 PASS/CLOSED; U3 PASS/CLOSED; U4 PASS/CLOSED;
U5a PASS/CLOSED; U5b PASS/CLOSED after cochain expansion; U5c PASS/CLOSED
after naturality expansion. The proof is now ready for a fresh end-to-end
audit rather than another repetition of the same local checks.


## 2026-09-25 — CRITICAL FILTRATION CORRECTION: ZASSENHAUS VS LOWER 3-CENTRAL

A further end-to-end audit found a substantive indexing error that was not visible in the
earlier U1 local audit.

The manuscript called \(P_i\) the Zassenhaus filtration but defined it by
\[
P_{j+1}=P_j^3[P_j,S],
\]
which is the lower \(3\)-central filtration, not the \(3\)-Zassenhaus/Jennings
filtration. These filtrations agree at the first step but diverge at the
\(3\)-power jumps. Consequently the earlier claim \(P_{k+1}(S_k)=1\) was false
for the Zassenhaus filtration.

For the actual target
\[
S_k=A_k\rtimes U_1,\qquad A_k=\mathbf Z/3^k,\quad U_j=1+3^jA_k,
\]
the corrected Zassenhaus computation is
\[
P_n(S_k)=3^{e(n)}A_k\rtimes U_{e(n)+1},
\qquad e(n)=\lceil\log_3 n\rceil,\ e(1)=0.
\]
Hence
\[
P_{3^{k-1}}(S_k)=3^{k-1}A_k\ne1,
\qquad
P_{3^{k-1}+1}(S_k)=1.
\]
The key point is that the Zassenhaus recursion is
\[
P_n=P_{\lceil n/3\rceil}^3\prod_{i+j=n}[P_i,P_j],
\]
and the cube term supplies exactly the next \(3\)-adic translation and unit
levels; the commutator terms are no deeper than the claimed containment.

Therefore the finite quotient in the theorem has been corrected from
\[
G/P_{k+1}
\quad\text{to}\quad
Q_k=G/P_{3^{k-1}+1}.
\]
U2 has been correspondingly corrected: arbitrary candidate/cocycle maps into
\(S_k\) factor through this actual Zassenhaus quotient by functoriality.

This is a real correction, not cosmetic. In particular, the old \(P_{k+1}\)
factorization cannot be retained for the Zassenhaus filtration. The corrected
window is larger; minimality remains OPEN.

The corrected manuscript is committed as:
26d0180dbf1aece68acf14277da5baa0cf2aed1c.

A fresh three-pass pdflatex compilation of the corrected manuscript state
completed with status 0, 8 pages, and no undefined-reference or LaTeX
warning/error matches in the final pass.

Status update:
- Old U1 formulation: FAIL/CLOSED (terminology + indexing error).
- Correct Zassenhaus U1: PASS/CLOSED.
- U2 after correction: PASS/CLOSED.
- U3: PASS/CLOSED.
- U4: PASS/CLOSED.
- U5a/U5b/U5c: PASS/CLOSED.
- Main theorem: structurally preserved, but with the corrected Zassenhaus
  window \(P_{3^{k-1}+1}\).


## 2026-09-25 — THEOREM ASSEMBLY ATTACK: CORRECTED ZASSENHAUS WINDOW

A full assembly-level attack was performed against the current manuscript after the U1–U5 component audits. The attack did not find a fatal circularity in the U1→U2→U3→U4→U5→theorem chain. Two hidden assembly dependencies were identified and repaired in `paper/main.tex`:

1. **Zassenhaus vs lower-3-central proof separation.** The older research U1 artifact proves the analogous lower-3-central statement (P_{k+1}(S_k)=1), so it cannot by itself justify the corrected Zassenhaus window (G/P_{3^{k-1}+1}). The manuscript proof was therefore replaced by a direct Jennings–Lazard Zassenhaus calculation using 
(P_n=prod_{i3^j\ge n}\gamma_i^{3^j}), together with (gamma_2(S_k)=3A_k), (gamma_i(S_k)=3^{i-1}A_k), and the resulting exact formula (P_n(S_k)=3^{e(n)}A_k\rtimes U_{e(n)+1}). The distinction is now explicit: the old lower-3-central record is historical/superseded for the corrected-window proof.

2. **Trivial-coefficient (H^1) identification.** U2 already gives the twisted (H^1) isomorphism, but the predicate also has target (H^1(-,\mathbf F_3)). The manuscript now explicitly proves (P_{3^{k-1}+1}(G)\subseteq\Phi(G)), hence inflation is an isomorphism on (H^1(-,\mathbf F_3)), and records the commutative square with coefficient reduction. This closes the previously implicit passage between the predicate on (G) and the predicate on (Q_k).

The current main theorem therefore has a coherent dependency chain:
- corrected actual Zassenhaus depth → arbitrary-candidate twisted factorization;
- trivial-coefficient (H^1) identification → equivalence of finite predicates on (G) and (Q_k);
- U3 → finite Fox criterion under explicit minimal one-relator hypotheses;
- U4 → only the (k=2) base selector;
- U5 → intrinsic higher-level uniqueness on the canonical branch;
- classical Kummerianity → independent existence of the canonical candidate.

No circular use of the desired selector theorem was found. In particular, U5 uses the independently known canonical dualizing orientation only inside the PD² injectivity lemma; it does not define the selector using that orientation.

Remaining audit status: **THEOREM ASSEMBLY = PASS / PROVISIONAL**, pending a fresh line-by-line audit of the repaired manuscript and a successful clean LaTeX build. Publication novelty remains **OPEN / CONDITIONAL** and window minimality remains **OPEN**.


## 2026-09-25 — U1 REFEREE-PROOF TIGHTENING + U5c PD² SOURCE ANCHOR

The post-assembly attack did not uncover a new mathematical failure. Two manuscript-level gaps were nevertheless tightened.

**U1:** the Zassenhaus proof in `paper/main.tex` now makes the power valuation explicit. Pure translations satisfy
((a,1)^{3^j}=(3^j a,1)); for (u=1+3^s bin U_s), the binomial/3-adic valuation calculation gives
(u^{3^j}equiv1+3^{s+j}bpmod{3^k}) until the term vanishes. Thus (U_1^{3^j}=U_{j+1}), and the exact identity
(S_k^{3^j}=3^jA_ktimes U_{j+1}) is justified rather than asserted. The commutator generation (gamma_2=3A_k) is also tied explicitly to ([4,a]=3a).

**U5c:** the finite-coefficient PD² duality statement is now anchored to Gareth Wilkes, *Classification of pro-(p) (PD^2) pairs and the pro-(p) curve complex*, Groups, Geometry and Dynamics 14 (2020), §1, which states the orientation-character convention and the finite-module duality used here. The manuscript keeps the explicit dual-map calculation: under (M^eeotimes Icong A_{k-1}), dualizing the socle inclusion (1mapsto3^{k-2}) gives reduction (A_{k-1}	woheadrightarrowmathbf F_3).

Commit: `962be77ed62040ed5707e3c59c54de6585a0086d`.

**Build status:** source-level clean-build verification of this exact commit is still pending; the previous 8-page three-pass build was for the preceding corrected manuscript commit, not this post-tightening commit. No claim of a fresh PDF build is made here.

Classification:
- U1 referee-level explicitness: **PASS / CLOSED**
- U5c literature anchoring: **PASS / CLOSED**
- theorem assembly: **PASS / PROVISIONAL**
- exact publication novelty: **OPEN / CONDITIONAL**
- Zassenhaus window minimality: **OPEN**

## 2026-09-25 — EXACT 962be77 FINAL MANUSCRIPT AUDIT / BUILD GATE

The exact manuscript commit requested for the final gate was independently resolved:
`962be77ed62040ed5707e3c59c54de6585a0086d` (`paper/main.tex`, blob
`4dd8400a0f0d107ec6aa58eaa04ed69c8a0be6af`). The commit is real and its
message is `paper: make U1 valuation proof explicit and source U5c PD2 duality`.

### Source-level end-to-end audit

The exact `paper/main.tex` at this SHA was read in four ranges and checked against
the authoritative U1-U5 state.

- **U1:** the manuscript now uses the actual Jennings--Lazard Zassenhaus product,
  not the lower-3-central recursion. The claimed finite window is
  `P_{3^{k-1}+1}`, and the proof explicitly derives the power valuation and
  `S_k^{3^j}=3^j A_k \rtimes U_{j+1}`.
- **U2:** arbitrary crossed cocycles and arbitrary candidate characters factor
  through the corrected Zassenhaus quotient; the trivial-coefficient H^1 inflation
  step is explicitly included.
- **U3:** the finite Kummer/Fox criterion is stated only under the minimal
  one-relator hypothesis and uses valuation induction rather than the superseded
  informal Nakayama argument.
- **U4:** only the k=2 base selector is used; the coordinate calculation gives
  `(1,4,1,1)` and is not used as an all-k presentation-level uniqueness claim.
- **U5a/U5b/U5c:** reduction, coefficient-extension variation, and PD^2
  socle-injectivity are explicitly stated. The U5b sign convention is fixed at
  cochain level. U5c identifies the dual of the socle inclusion with reduction
  `A_{k-1}->F_3`, with the finite-coefficient PD^2 duality anchored to Wilkes
  (2020), §1.
- **Theorem assembly:** existence is imported only as classical Kummerianity of
  the canonical orientation; uniqueness is obtained by U4 + U5 induction.
  No circular definition of the selector through `chi` was found.
- **Novelty wording:** the manuscript explicitly disclaims novelty for the
  canonical orientation/global Kummerian criterion and keeps the finite-window
  publication claim narrow and conditional.
- **Minimality:** explicitly left OPEN; no unsupported optimal-window claim remains.

### Independent literature spot-check

Wilkes' §1 states the finite-module PD^2 duality and orientation-character
convention used by U5c. Quadrelli (2024), Proposition 2.10, indeed requires
an already Kummerian oriented pair plus the restriction-surjectivity hypothesis;
the manuscript's separation language is therefore appropriately conditional.
The audited sources support the stated classical prior-art boundary.

### Build automation result

A temporary GitHub Actions audit workflow was created on a disposable branch
based exactly on `962be77`, explicitly checking out that SHA, running three
`pdflatex` passes, checking the PDF/logs, and uploading the PDF/log artifact.
The branch was then reset to the exact audited commit to leave no manuscript
change behind. The connector did not expose a workflow run/status for this
push-triggered audit (no run/status was returned), so **no false claim of a
fresh GitHub Actions PDF build is made**.

The local container has `pdflatex` and `latexmk`, but the environment cannot
resolve `github.com`; therefore an exact local checkout could not be performed
from the public repository. The earlier repository record of an 8-page,
three-pass build applies to the preceding corrected commit, not to 962be77.

### Final classification

- Exact source identity: **PASS / CLOSED**
- U1-U5 source consistency: **PASS / CLOSED**
- Theorem assembly / hypothesis-conclusion discipline: **PASS / CLOSED**
- Novelty wording discipline: **PASS / CLOSED / CONDITIONAL**
- Zassenhaus-window minimality: **OPEN**
- Exact fresh PDF build at 962be77: **OPEN / ENVIRONMENTAL VERIFICATION GAP**

No new mathematical branch is opened. The next action is publication preparation
only, unless a genuine build environment becomes available.



## 2026-09-25 — AUTHOR + U5c CITATION + FINAL PDF BUILD

The publication manuscript was updated in `paper/main.tex`:
- author set exactly to **Seo Seongkyo**;
- U5c citation wording tightened to identify Wilkes (2020), §1, specifically the finite-coefficient duality stated immediately before Proposition 1.5, with the same orientation-character convention.

Commit: `4e98bec29ad558f64f314f0897d706c8acd980d1`.

The resulting manuscript was independently rebuilt from the exact GitHub source content at that commit using three consecutive `pdflatex -interaction=nonstopmode -halt-on-error` passes. Final checks:
- exit status: **0**;
- PDF pages: **8**;
- passes 2 and 3: no LaTeX errors, warnings, or undefined-reference matches;
- PDF text confirms author line: **Seo Seongkyo**;
- SHA-256: `202dda263a7dfa1679c0b69a80e50705633b7add8033502f69eb9855dcd110e7`.

The local build is an exact-source-content build of the committed `paper/main.tex`; the container cannot resolve `github.com`, so this is not represented as a fresh GitHub Actions artifact. No mathematical branch was reopened.

Classification:
- author metadata: **PASS / CLOSED**
- U5c citation precision: **PASS / CLOSED**
- final local PDF build: **PASS / CLOSED**
- fresh GitHub Actions artifact: **NOT CLAIMED / ENVIRONMENTAL**
- theorem assembly: **PASS / CLOSED**
- novelty: **OPEN / CONDITIONAL**
- window minimality: **OPEN**


### 2026-09-25 — APPENDIX A–D INSERTION
The manuscript `paper/main.tex` was updated at commit `71d59a39bc142892fdc1dcd38034b49158e6b41a` to include four publication-facing appendices:
- Appendix A: detailed finite-depth Zassenhaus/valuation verification, including the endpoint distinction (P_{3^{k-1}}
eq1) versus (P_{3^{k-1}+1}=1);
- Appendix B: independent (k=2) base-level enumeration (81\to27\to3\to1);
- Appendix C: cochain-level verification of the U5b connecting-map variation and sign convention;
- Appendix D: explicit proof/computation boundary and reproducibility record.

The appendices are deliberately restricted to calculations used by the theorem; broader exploratory computations remain in the research log rather than being presented as proof premises.

A local three-pass PDF rebuild could not be rerun in this environment after this commit because the container has no DNS/network access to GitHub. This is an environment limitation, not a claimed manuscript/build failure. The source update itself was successfully written through the GitHub connector.


### 2026-09-25 — PUBLICATION BIBLIOGRAPHY AUDIT
A source-level bibliography audit was performed against publisher/arXiv records. One concrete metadata error was corrected in `paper/main.tex`: the Mináč–Rogelstad–Tân item was incorrectly titled as “How fast do Zassenhaus filtrations of pro-p-groups descend?”; the cited work is actually emph{Dimensions of Zassenhaus filtration subquotients of some pro-p-groups}, Israel Journal of Mathematics 212 (2016), no. 2, 825–855, DOI 10.1007/s11856-016-1310-0. The U1 text now cites this item explicitly.
The separate unused `paper/references.bib` was removed so the arXiv source package has one authoritative manual bibliography rather than an unused duplicate source.
A minor Appendix A notation typo (`u^{3^j}`) was also corrected.
The manuscript bibliography entries for Labute (1967), Efrat–Quadrelli (2019), Quadrelli–Weigel (2020), Quadrelli–Weigel (2022), Quadrelli (2024), and Wilkes (2020) were cross-checked against publisher/arXiv metadata; their recorded journal/volume/page/article/DOI data are consistent with the audited sources.


### 2026-09-25 — FINAL CI PDF BUILD CLOSED
The publication manuscript at commit `d74bf5f1d40f120c41e4dc4d4c204bfc3794bb77` was compiled by GitHub Actions with the repository TeX environment. Final workflow run `36148729343` completed successfully: LaTeX compilation, manuscript verification, and PDF artifact upload all passed.
The final artifact is 13 pages. SHA-256 of the extracted PDF is `584ee648c8b1e5ff1291b97df742012ab01783a586c045dda676af2e77d05508`.
Independent local inspection of the downloaded artifact confirmed the title/author, theorem, all four Appendix A–D sections, and the corrected Mináč–Rogelstad–Tân bibliography entry. The build log showed no undefined citations/references or LaTeX Warning/Error matches in the final verification pass. One harmless 0.416pt overfull hbox remains in a heading; it does not affect compilation or mathematical content.
The successful PDF artifact is retained by GitHub Actions (artifact id `10869809009`, expiration 2026-12-24).

## 2026-09-26 — FINAL TYPO-FIX CI REBUILD CLOSED

The previously open environmental gap is now closed. The post-typo manuscript commit 455f0426dfdbebd939650f6828eecc0bc630dd7e ("paper: correct Demuskin spelling in abstract") triggered GitHub Actions run 36154558321 for .github/workflows/paper-build.yml.

The run completed successfully. The latex job passed checkout, manuscript compilation, PDF verification, submission-package generation, PDF upload, arXiv-source-package upload, and full-package upload.

Artifacts from this exact source commit:
- PDF artifact: finite-window-kummer-recognition-pdf, id 10872634056
- source package artifact: finite-window-kummer-recognition-source, id 10872693867
- full submission package artifact: finite-window-kummer-recognition-full, id 10872459395

The extracted final PDF is 13 pages and has SHA-256 438bd2c8e88927918f83f5742eae2859da12b9916cb029f7700b34e4b74eab2e.
The full submission package declares the same PDF hash and main.tex hash afc585a76138409e51ffb2d8c8ec609da2cebf250bb7924f9cb39466fe477de1.
The source and full packages contain the same 23,584-byte main.tex content.

Thus the exact requested identity is now established: corrected source -> same CI run -> corrected PDF + packages.

Classification:
- typo correction: PASS / CLOSED
- exact source identity: PASS / CLOSED
- fresh CI PDF build: PASS / CLOSED
- source/PDF/package consistency: PASS / CLOSED
- submission-package generation: PASS / CLOSED
- mathematical theorem status: PASS / CLOSED
- publication novelty: OPEN / CONDITIONAL
- Zassenhaus-window minimality: OPEN

This supersedes the previous "OPEN / ENVIRONMENTAL VERIFICATION GAP" build status.


## 2026-09-26 — FOLLOW-UP PAPER SCOPE: SHARP WINDOW + ET_p OBSTRUCTION/UNIFORMITY

A scope decision was made for the successor-paper program. The existing publication manuscript/paper is **FROZEN** and is not to be modified by this branch.

The successor paper should **combine**, rather than split, the corrected sharp finite-window draft line with the newly developed elementary-type oriented pro-p framework (ET_p). The common research question is the boundary of finite-window recognition: sharp factorization depth, information-theoretic obstructions, q-collapse, and the possible uniformity of the same window on rigid subclasses.

Planned successor-paper architecture:
1. finite-window affine/Kummer factorization and corrected sharpness;
2. abstract-Q_k information loss and q-collapse;
3. strong impossibility on the free pro-p member F_2 = Z_p *_p Z_p of the broad ET_p class, where arbitrary orientations are Kummerian and the abstract finite quotient alone cannot select a unique orientation;
4. weak selector formulation separating the Kummerian candidate set from any additional BP refinement;
5. rigid ET_p/free-product subclass as the next positive uniform-window question.

Important logical boundary: the rigid-subclass claim that the same n(k)=p^(k-1)+1 window works uniformly is **OPEN**, not a theorem. In particular, mixed free-product commutators need an explicit calculation; they cannot be assumed to die at the same Zassenhaus depth merely from factorwise filtration behavior. The first authorized test is a concrete D_1 *_p D_2 calculation for small k, followed by a general proof only if supported.

The abstract-quotient impossibility is to be stated precisely: it rules out recovery from the **isomorphism class of the abstract Q_k alone**. It does not rule out recognition when extra marking, quotient maps, distinguished subgroups, coefficient actions, or other structure are supplied.

Classification:
- successor-paper integration of sharpness + ET_p obstruction program: **PASS / CLOSED (scope decision)**
- free-pro-p/ET_p abstract-Q_k impossibility: **PASS / LOCAL**
- q-collapse as obstruction: **PASS / LOCAL**
- rigid ET_p uniform-window theorem: **OPEN**
- recognition minimality among arbitrary intrinsic carriers: **OPEN**
- successor-paper publication novelty: **OPEN / CONDITIONAL**

No modification of the frozen publication manuscript is authorized by this entry.


## 2026-09-26 — FOLLOW-UP MERGED AUDIT: SHARPNESS REPAIR + MIXED-COMMUTATOR CLOSURE

The uploaded successor draft `followup_merged.tex` was audited without modifying the frozen publication manuscript.

- The source has a LaTeX defect: `\Fp` is undefined. A temporary definition `\Fp=\mathbb F_p` gives a clean three-pass local build (3 pages), with one non-fatal overfull hbox. **FAIL/CLOSED (source syntax)**.
- Section I crossed-cocycle algebra is consistent after the previously recorded prefactor correction; solving the relation gives (a_2=(1-p^f)^{-1}), hence (4,13,40) for (p=3,f=1). **PASS/LOCAL**.
- Section II contains a false step: for (f>1), canonical (a_2=(1-p^f)^{-1}) is not a generator of (U_1), so “choose (a_2=1+p) while (F_i=0)” is invalid. The sharpness theorem is salvageable: for (f<k), canonical (ho) with (z(x_1)=1) already witnesses (x_1^{p^{k-1}}mapsto p^{k-1}
e0); for (fge k), the existing (x_3) witness works. **Written proof FAIL/CLOSED; theorem OPEN pending repair**.
- Section III must restrict “no predicate depending only on (Q_k)” to an **isomorphism-natural/functorial selector on the bare abstract quotient**. Free pro-(p) groups are Kummerian for every orientation, so the obstruction remains genuine.
- Section IV (q)-collapse passes locally: (x_1^{p^f}in P_{p^f}\setminus P_{p^f+1}) gives the exact threshold (fge k). **PASS/LOCAL**.
- Section V mixed commutator gate closes categorically. For (T_n(G)=G/P_n(G)), every map to a pro-(p) group with (P_n=1) factors uniquely through (T_n(G)); hence (T_n) is a reflector. Since free pro-(p) product is a coproduct,
  [
  T_n(G_1*_pG_2)cong T_n(G_1)*_pT_n(G_2)/P_n(T_n(G_1)*_pT_n(G_2)).
  ]
  Thus the kernel (N) is exactly (P_n(H)), (H=Q_n(G_1)*_pQ_n(G_2)), and mixed commutators have total Zassenhaus weight at least (n). At (p=3,k=2,n=4), terms such as ([P_1,P_3]) and ([P_2,P_2]) are therefore killed by (P_4(S_2)=1). **PASS/CLOSED**.
- Positive uniformity is supported for the precise subclass of finite free pro-(p) products of Demushkin groups with canonical orientations; free products preserve Kummerianity and factorwise uniqueness gives the product orientation. The broader current (mathcal{ET}_p^{rig}) wording remains **OPEN** until its recursive class is defined precisely. The Newton/J block-diagonal algorithmic claim should be separated unless an explicit input model is supplied.
- Literature spot-checks support the free-product Zassenhaus/co-product structure and Kummerian free-product facts. 

Audit artifact: `research/FOLLOWUP_MERGED_AUDIT_2026-09-26.md`, commit `e4fca7e63a282d0f4b009299fbf906582270c8ef`.

Current classification: I **PASS/LOCAL**; II **OPEN** pending repair; III **PASS/LOCAL** after naturality qualification; IV **PASS/LOCAL**; V mixed commutator **PASS/CLOSED**; V pure Demushkin free-product uniformity **PASS/CLOSED**; V broad (mathcal{ET}_p^{rig}) **OPEN**; LaTeX source **FAIL/CLOSED**; novelty **OPEN/CONDITIONAL**.


## 2026-09-26 — PAPER/FOLLOWUP TEX DIRECT BUILD AUDIT

Directly inspected the locally uploaded `followup_merged.tex` and compared it with current GitHub `paper/` contents. The repository `paper/` directory currently contains main.tex and audit/status markdowns, but does not contain `followup_merged.tex`, `sharp_factorization_qcollapse.tex`, or `final_audit_report.tex`; therefore only `followup_merged.tex` was directly audited here.

Findings:
- Direct pdflatex build fails at line 74 because `\\Fp` is undefined. Temporary macro definition is sufficient to pass this syntax defect. **FAIL/CLOSED (LaTeX source defect)**.
- The file still contains the previously identified false sharpness sentence at line 43: for (f>1), it says to choose (a_2=1+p) while retaining (F_i=0) “by adjusting”. This contradicts the solved equations, which force (a_2=(1-p^f)^{-1}). **FAIL/CLOSED (proof sentence)**.
- The abstract/theorem text still says (d=2) “fails ... open”. The new computational claim in the user-supplied audit is stronger: (d=2) sharpness holds for (f=1) but fails for (f>1), with explicit (p=3) exhaustive counts. That stronger boundary is NOT yet reflected in the tex. The theorem should be reformulated to distinguish (dge4) all (f) from (d=2,f=1), and state the (d=2,f>1) obstruction precisely.
- Section III still states the overly broad theorem “no predicate depending only on (Q_k)”. This must be narrowed to an isomorphism-natural/functorial selector on the bare quotient; otherwise arbitrary non-natural choice functions are not excluded. **PASS/LOCAL after wording repair**.
- Section V still marks the mixed-commutator gate OPEN. The categorical truncation argument already established in the successor audit closes this gate: (T_n(G)=G/P_n(G)) is the reflector to (P_n=1) pro-(p) groups, hence (T_n(G_1*_pG_2)cong T_n(G_1)*_pT_n(G_2)/P_n(T_n(G_1)*_pT_n(G_2))). Thus the kernel is exactly (P_n) of the free product of factor quotients. **PASS/CLOSED**, so the current Section V is stale.
- Section V's definition “each free-product factor contains a Demushkin block” is too vague for the claimed (H^2), blockwise uniqueness, and Newton algorithm conclusions. The positive result should be restricted to a precisely defined class, e.g. finite free products of Demushkin blocks, unless further closure operations are proved.
- The manuscript has no bibliography environment, bibliography file, or actual citation commands despite naming Labute, Blumer–Quadrelli, Quadrelli–Weigel, etc. The literature section is prose-only. This is **FAIL/publication-critical**.
- The Newton (O(kd)) claim is presented without a defined input model, convergence/uniqueness lemma, or proof that the stated Jacobian remains the relevant invertible block matrix throughout lifting. It should be separated as a computational coordinate realization, not part of the structural theorem, unless proved.
- The (q)-collapse theorem itself is structurally plausible and the abelianization formula distinguishes (f<k) from (fge k); however the “iff” should explicitly state the parameter range (fge1) and the precise free-group/Zassenhaus lemma used for the forward implication.

Classification after direct build/audit:
I **PASS/LOCAL**; II **OPEN** (the theorem boundary can be repaired, but current proof text is false); III **PASS/LOCAL** after naturality qualification; IV **PASS/LOCAL**; V mixed commutator **PASS/CLOSED** but manuscript stale; broad rigid class **OPEN**; bibliography **FAIL/CLOSED**; LaTeX **FAIL/CLOSED**.


## 2026-09-26 — SUCCESSOR TWO REMAINING QUESTIONS: CATEGORY-RELATIVE MINIMALITY CLOSED

A final lower-bound attack was completed on the finite recognition depth. Absolute minimality over arbitrary carriers remains ill-posed without an admissible category, but the natural successor category is the factorization category of all affine crossed-cocycle representations
rho:G -> U_{1,k}, z:G -> A_k(rho).

For the standard Demushkin family G_f and every d>=2, the threshold n_aff(k)=p^(k-1)+1 is sharp.

For f<k, the canonical orientation rho(x_1)=1, rho(x_2)=(1-p^f)^(-1), together with z(x_1)=1 and all other z(x_i)=0, satisfies the relator equation because
p^f + rho(x_2)^(-1)(1-rho(x_2))=0 mod p^k,
while z(x_1^(p^(k-1)))=p^(k-1) != 0 mod p^k.

For f>=k, the d=2 boundary also closes: take rho(x_1)=1, rho(x_2)=1+p, z(x_1)=0, z(x_2)=1. The relator obstruction vanishes modulo p^k, while
z(x_2^(p^(k-1)))=((1+p)^(p^(k-1))-1)/p
has p-adic valuation k-1 and is therefore nonzero modulo p^k. Setting unused coordinates to zero gives the same witness for every d>=2.

Hence:
- affine factorization-depth minimality n_aff(k)=p^(k-1)+1: **PASS / CLOSED** for d>=2, all f>=1;
- absolute minimality among arbitrary intrinsic carriers: **OPEN / category-dependent**;
- the earlier d=2,f>1 sharpness failure claim is **HISTORICAL / SUPERSEDED**.

Detailed audit: research/SUCCESSOR_TWO_REMAINING_PROBLEMS_CLOSURE_2026-09-26.md.

## 2026-09-26 — SUCCESSOR NOVELTY / PRIOR-ART BOUNDARY FINALIZED

A targeted literature audit was completed against Labute's canonical-orientation theorem, Efrat–Quadrelli/Quadrelli Kummerian and 1-cyclotomic criteria, Quadrelli–Weigel's oriented elementary-type results, and the relevant 2026 Blumer–Quadrelli and Pál–Quick papers.

The audit confirms:
- canonical Demushkin orientation and its Kummerian uniqueness are classical: **NON-NOVEL / CLOSED**;
- Kummerianity and 1-cyclotomicity criteria are classical/known: **NON-NOVEL / CLOSED**;
- the present sharp finite-window affine factorization statement at depth p^(k-1)+1 was not located verbatim in the audited corpus;
- the bare abstract-Q_k impossibility must remain restricted to isomorphism-natural/functorial q-blind selectors;
- the q-collapse result is compatible with the finite target orientation residue and is not itself a canonical-orientation novelty;
- Pál–Quick 2026 addresses A_3-formality/canonical Hochschild classes, not the present finite-window affine factorization theorem;
- Blumer–Quadrelli 2026 addresses non-1-cyclotomic examples, not the present recognition theorem.

Accordingly the defensible publication claim is the finite-window/sharp-factorization result and its information-loss boundary, not discovery of the canonical orientation.

Publication novelty remains **OPEN / CONDITIONAL** in the strict sense: a literature search can establish a defensible boundary but cannot prove absence of an equivalent formulation everywhere. No source found in the audited corpus states the exact present theorem.

Detailed audit: research/SUCCESSOR_TWO_REMAINING_PROBLEMS_CLOSURE_2026-09-26.md.


## 2026-09-26 — LONG-TERM COMPUTATIONAL PROGRAM RECORDED

Following the completed successor-paper sharpness/minimality and q-collapse audits, a concrete implementation program was added as `research/LONG_TERM_COMPUTATIONAL_PROGRAM_2026-09-26.md`.

The program deliberately separates computational validation from theorem claims. It begins with direct affine sharpness witnesses, then q-collapse measurements, then a finite-window recognition prototype on independently checked concrete Demuškin/local-field examples, and finally a comparison with other filtrations.

The first task will test the two currently established witness regimes:
- (f<k): canonical (ho(x_2)=(1-p^f)^{-1}), (z(x_1)=1);
- (fge k): (ho(x_2)=1+p), (z(x_2)=1), with the LTE valuation check.

The local-field branch is explicitly conditional on verifying the precise group presentation, (q), orientation convention, and finite quotient model before implementation. The filtration-comparison branch must keep Zassenhaus and lower (p)-central filtrations distinct; the 2025 correction remains controlling.

Recommended execution order: **Task 1 → Task 3 → Task 2 → Task 4**.

Classification: **OPEN / AUTHORIZED FOR STAGED IMPLEMENTATION**. No computation is claimed as completed by this record.

## 2026-09-26 — FINAL INDEPENDENT REFEREE VIEW / PRE-SUBMISSION GATE

실제 투고 직전, 외부 심사자가 공격할 가능성이 높은 지점을 중심으로 후속논문에 대한 마지막 독립 referee 관점 검토를 수행했다. 현재 원고의 수학적 핵심 주장과 증명 연결을 독립적으로 다시 점검한 범위에서는 **즉시 수정해야 할 수학적 오류를 발견하지 않았다**.

이 판정은 다음과 같이 해석한다.
- 수학적 핵심 정리/증명 구조: **PASS / CLOSED** (현재 감사 범위)
- 원고의 최종 투고 적합성: 수학적 오류 부재와 별도로 문헌 novelty, 인용·표현, 최종 PDF/source consistency 등 출판 준비 항목은 별도 확인 대상
- Zassenhaus window의 절대적 최소성: **OPEN**
- exact publication novelty: **OPEN / CONDITIONAL**

따라서 이 검토 결과만으로 novelty 또는 minimality를 CLOSED로 승격하지 않는다. 외부 referee가 제기할 가능성이 높은 공격 지점은 이미 별도 audit에서 추적하고 있으며, 새로운 수학적 오류가 발견되지 않았다는 것은 현재 증명된 범위의 안정성 판정으로 기록한다.

**독립 referee 최종 판정:** 현재 원고에 대해 즉시 수정해야 할 수학적 오류 없음. 다음 단계는 새로운 수학적 가지를 여는 것이 아니라 투고용 최종 source/PDF·참고문헌·novelty 표현의 최종 정합성 확인이다.


## 2026-09-26 — SUCCESSOR EXTERNAL-SUBMISSION GATE CLOSED

The independent-referee repairs were merged into `successor-publication-candidate-2026-09-26` by PR #3, producing candidate commit `73001ba0611e4f4aa7db8c733ee01d67542e16eb`.

Final candidate CI:
- Build successor manuscript: **PASS**
- PDF verification: **PASS**
- warning/error/undefined check: **PASS / CLEAN**
- PDF artifact: **PASS**
- artifact ID: `10896535087`
- artifact digest: `sha256:8abe297080c0c79a7264b92449f9f68c6e41598c7a0e6dc1c54964ed1483a733`

The final submission PDF was extracted from that exact artifact and preserved locally as `successor_submission_final.pdf`; the verified PDF has 8 pages.

The successor manuscript is now **PASS / CLOSED for internal external-submission readiness**. Remaining research classifications are unchanged: novelty remains **OPEN / CONDITIONAL**, absolute carrier minimality remains **OPEN / category-dependent**, and broader elementary-type uniformity remains **OPEN** and unclaimed.

The external submission itself has not been sent; venue selection and the venue-specific submission metadata remain the only external-action steps.


## 2026-09-26 — PAPER 3 FINAL AUDIT / INDEPENDENT NOVELTY GATE

Paper 3 `Finite-Window Applications to Free Products of Demuškin Blocks` was taken through the requested sequence: CI baseline -> independent referee audit -> free-product/Kummer literature audit -> logical redundancy audit -> necessary manuscript repair -> fresh CI trigger -> publication-candidate gate.

Results:
- initial Paper 3 CI run 36213977187 on commit 901fcc6: **PASS / CLOSED**;
- referee audit: **PASS / CLOSED**; no fatal mathematical error, but the blockwise Kummer proof was tightened to explicitly use Paper 2 arbitrary-candidate factorization and the finite H^1 identifications;
- f-collapse wording was narrowed to the marked finite abelianization;
- Efrat--Quadrelli Prop. 7.5 and Quadrelli--Weigel Prop. 5.5 were added as direct prior art for free-product Kummerianity;
- logical redundancy audit: **FAIL / CLOSED** for independent novelty; the principal claims are applications/corollaries of Paper 2 plus known free-product Kummerianity;
- repaired manuscript commit: `55a51dc30579881843658968af2049b0a6dbce8d`;
- fresh Paper 3 CI was triggered by the repaired source; the final run result must be checked from GitHub Actions before any external submission claim;
- Paper 3 classification: **PASS / CLOSED as a mathematically sound application/companion manuscript; FAIL / CLOSED as an independent novelty paper on the current evidence**.

Paper 2 remains untouched. A genuinely independent Paper 3 now requires a new application theorem or obstruction, not further cosmetic expansion of the current free-product synthesis.

## 2026-09-26 — PAPER 2 + PAPER 3 MERGED: FINAL PUBLICATION-TRACK DECISION

Paper 3's current corpus was merged into Paper 2 after the requested sequence:
Paper 2 baseline restoration -> Paper 3 application absorption -> independent referee audit -> novelty/redundancy audit -> manuscript repair -> fresh CI -> publication-candidate gate.

Merged manuscript:
- branch: `paper2-paper3-merged-2026-09-26`
- source: `paper/successor_main.tex`
- publication-candidate status: **PASS / CLOSED internally**, subject to the already stated conditional novelty boundary.

Merged application content:
- finite free pro-p product truncation/coproduct compatibility;
- uniform affine window for mixed commutators;
- heterogeneous `f_i<k` versus `f_i>=k` finite-depth parameter profile;
- explicit composite example `D_{1,4}*_pD_{3,2}*_pD_{7,4}`;
- blockwise Kummer recognition for finite free pro-3 products of rank-four `q=3` blocks.

Referee result:
- mathematical core: PASS/CLOSED;
- affine sharpness: PASS/CLOSED;
- free-product extension: PASS/CLOSED in the stated class;
- finite-depth `f`-collapse: PASS/CLOSED after tightening the abelianization argument;
- blockwise Kummer application: PASS/CLOSED within its stated class;
- no new load-bearing mathematical defect found.

Novelty/redundancy result:
- Paper 3 as an independent publication is **FAIL/CLOSED on current evidence** because its present claims are applications/synthesis of Paper 2 plus the preceding recognition theorem and known free-product machinery.
- This does **not** mean the application material lacks mathematical value.
- The material is retained inside Paper 2, where it strengthens the theorem's concrete scope without competing with the central novelty.
- Publication novelty for Paper 2 remains **CONDITIONAL** and is phrased narrowly; no absolute priority claim is made.

CI:
- final merged manuscript build: **PASS**;
- merged PDF: **11 pages**;
- CI run for the final manuscript commit: `36215909243`;
- earlier failed CI runs were caused by verification-script issues, not manuscript compilation; the final verification and artifact upload passed.

Records:
- `research/PAPER2_PAPER3_MERGED_REFEREE_AUDIT_2026-09-26.md`
- `research/PAPER2_PAPER3_NOVELTY_REDUNDANCY_AUDIT_2026-09-26.md`
- `paper/PAPER2_MERGED_PUBLICATION_CANDIDATE_2026-09-26.md`

Decision:
**Do not submit the former Paper 3 separately in its current form. Treat its present content as the applications/synthesis component of Paper 2.**


## 2026-09-27 — PAPER 3 REOPENED AS NEW RESEARCH PROGRAM: FINITE-WINDOW RECOGNITION THRESHOLDS

The former Paper 3 application/free-product manuscript is now definitively closed as an independent novelty paper and remains absorbed into the Paper 2 publication candidate. Paper 1 and Paper 2 are likewise treated as closed/frozen stages for the next research program; their completed mathematics and publication artifacts remain authoritative and are not reopened merely for variants.

A **new Paper 3** is opened with a different mathematical purpose: define and study the amount of finite filtered information required to recognize a global invariant.

Motivation:
1. Paper 1 showed that finite filtered information can recover a global invariant.
2. Paper 2 established a sharp affine/Kummer factorization depth (n_{\mathrm{aff}}(k)=p^{k-1}+1).
3. The natural next abstraction is to make the required recognition depth itself a category-relative mathematical object.

The new target is
[
r_T(\mathcal C;D_\bullet)
=
\min\{n:W_n(G)\cong W_n(H)\Rightarrow T(G)\cong T(H)
\text{ for all }G,H\in\mathcal C\},
]
with (r_T=\infty) if no such (n) exists. The category is essential: a threshold for one fixed group is trivial/ill-posed because (T(G)) is already fixed.

Factorization and recognition thresholds are explicitly separated. Paper 2's (f_{\mathrm{aff}}(k)=p^{k-1}+1) is a benchmark/bridge and is not automatically identified with a new recognition threshold.

Initial execution plan:
N0 definition -> N1 basic threshold theory -> N2 Paper 2 bridge -> N3 genuinely new target after prior-art audit -> N4 separation/recognition examples -> N5 category/filtration comparison.

Ultimate goal recorded explicitly: develop a general theory of finite-window recognition for filtered algebraic objects, identifying conditions for finite recognizability, sharp thresholds, and information-theoretic obstructions. **The new Paper 3 is the most natural first step toward that ultimate generalization.**

Detailed authoritative plan: `research/PAPER3_FINITE_WINDOW_RECOGNITION_PROGRAM_2026-09-27.md`.

Decision: **Paper 3 new program ACTIVE; Paper 1/2 CLOSED/FROZEN for this research program.**


## 2026-09-27 — PAPER 3 ULTIMATE-GOAL PRIOR-ART AUDIT

Before N3 target selection, the project-level ultimate goal was checked against prior literature rather than assuming that the general framework itself is new.

Key findings:
- finite determinacy / degree of determinacy is established prior art;
- recognition from finite quotients / profinite rigidity is established prior art;
- Efrat–Mináč (TAMS 2017, arXiv:1103.1508) is a particularly close conceptual precedent: it asks how much group-theoretic information is needed to determine a cohomological target and constructs a minimal quotient, with a general cohomological-duality framework;
- Zassenhaus finite-level determination of cohomological data is also established in the Efrat/Massey-product literature;
- finite quotients determining infinite graded/filtered structures occur in other settings as well.

The remaining potentially distinct axis is narrower: a uniform category-relative threshold r_T(C;D_bullet) for a prescribed filtration, treated as a primary mathematical object, with explicit separation from factorization depth, sharp same-window/different-target lower bounds, and systematic category/filtration comparison. No exact theorem containing this full combination was located in the present search.

Decision:
- broad ultimate goal: OPEN / CONDITIONAL, not a novelty claim;
- category-uniform filtration threshold framework: OPEN / LOAD-BEARING;
- Bockstein as first N3 target: NOT SELECTED / HIGH PRIOR-ART RISK;
- N3 framework-level prior-art comparison is now mandatory before substantial target computation.

Detailed audit: research/PAPER3_ULTIMATE_GOAL_PRIOR_ART_AUDIT_2026-09-27.md.


## 2026-09-27 — PAPER 3 EFRAT–MINÁČ / FINITE-DETERMINACY COMPARISON MATRIX

N3 prior-art analysis was refined by rewriting the Efrat–Mináč framework in the project's proposed threshold language and separating verified statements from hypotheses.

### Verified prior-art baseline

Efrat–Mináč, *Galois groups and cohomological functors* (TAMS 2017; arXiv:1103.1508), constructs a canonical quotient (G[3]) for absolute Galois groups containing the relevant roots of unity and proves that it determines the full mod-(q) cohomology ring; Theorem A gives the corresponding minimality condition. For (q=p) odd, the relevant third term agrees with the third Zassenhaus term. Their cohomological-duality framework also includes examples involving cup product and Bockstein together with cup product. This is direct prior art against any broad claim that “finite filtered information determines a cohomological invariant” is itself new.

Efrat 2014, *The Zassenhaus filtration, Massey products, and representations of profinite groups*, supplies a close representation-theoretic precedent: under stated hypotheses, a Zassenhaus term is characterized as an intersection of kernels of upper-triangular unipotent representations. This is prior art for the general bridge between finite-dimensional representation data and Zassenhaus depth.

### Proposed (r_T) recasting — status by item

The project notation
[
r_T(mathcal C;D_ullet)
=
min{n:W_n(G)cong W_n(H)Rightarrow T(G)cong T(H)
	ext{ for all }G,Hinmathcal C}
]
remains useful, but the following distinctions are mandatory.

1. For cup-product/decomposable-cohomology targets, an (n=3) upper bound and a minimal determining quotient are already Efrat–Mináč territory. **NON-NOVEL / CLOSED as a general phenomenon.**

2. For the combined Bockstein + cup target, Efrat–Mináč provide direct prior art. **NON-NOVEL / CLOSED as a general phenomenon.**

3. The statement that a pure Bockstein target (T_eta) has an exact threshold (r_{T_eta}=p+1) is **NOT YET VERIFIED** and must not be treated as an established result. It is only a candidate research question.

4. “Minimal determining quotient” is not automatically identical to the project's (r_T). The Efrat–Mináč theorem concerns a specific cohomological target and category; (r_T) is a category-level indistinguishability threshold for a prescribed filtration. Exact equivalence must be proved, not assumed.

5. The proposed distinction
[
	ext{factorization threshold}
eq	ext{recognition threshold}
]
is conceptually useful, but novelty is **OPEN** until a concrete theorem/example produces a genuine separation.

6. Filtration dependence
[
r_T(mathcal C;D_ullet)
eq r_T(mathcal C;E_ullet)
]
is a candidate axis; no novelty claim is made until an explicit example or comparison theorem survives prior-art checking.

7. Information-loss/separation pairs
[
W_{n-1}(G)cong W_{n-1}(H),qquad T(G)
otcong T(H)
]
are a natural lower-bound language, but explicit constructions must first be checked against existing minimal-determining-quotient results.

### Comparison matrix

| Axis | Existing finite-determinacy / Efrat–Mináč | New Paper 3 program | Current classification |
|---|---|---|---|
| Target | cup/decomposable cohomology; Bockstein+cup variants | arbitrary prescribed target (T) | broad claim **OPEN/CONDITIONAL** |
| Threshold | third-level sufficiency/minimal quotient in specific classes | exact (r_T(mathcal C;D_ullet)) | **OPEN / LOAD-BEARING** |
| Sharp lower bound | minimal determining quotient already gives a form of minimality | explicit same-window separation pair | **OPEN** |
| Factorization vs recognition | not the primary distinction | explicit separate invariants | **OPEN**; must produce nontrivial separation |
| Filtration comparison | mainly fixed canonical filtrations in cited results | compare (D_ullet,E_ullet) | **OPEN** |
| Category dependence | class-specific | ((mathcal C,D_ullet,T)mapsto r_T) | **OPEN** |
| Uniformity | theorem-specific | threshold as category-level object | **OPEN / CONDITIONAL** |
| Information-loss obstruction | implicit/structural minimality exists | explicit obstruction theorem | **OPEN** |

### Research decision

The broad slogan “finite information determines a global invariant” is **not** a novelty claim and is now treated as established background.

Candidate novelty for Paper 3 must instead come from a mathematically nontrivial combination not already supplied by Efrat–Mináč or related finite-determinacy theory, most plausibly:
- a target-independent threshold formalism with precise functorial hypotheses;
- a theorem genuinely separating factorization and recognition thresholds;
- a filtration-comparison theorem;
- or an explicit sharp separation family not reducible to an existing minimal-determining-quotient theorem.

The next mandatory step is **N3 prior-art theorem-by-theorem comparison**, not broad computation. The pure Bockstein (r_{T_eta}=p+1) proposal remains a conjectural test case, not an established result.

Classification: **OPEN / LOAD-BEARING.**


## 2026-09-27 — PAPER 3 FACTORIZATION vs RECOGNITION AUDIT (F1–F4)

The first N3 theorem-by-theorem prior-art audit was completed before any new target computation. The audit compared Efrat–Mináč and related finite-determinacy/Zassenhaus literature against the Paper 3 distinction between factorization and recognition thresholds.

### F1 — Factorization
Existing literature explicitly contains the factorization/determination direction: quotient information such as G/G_(3) determines the relevant cohomological target, equivalently the target is obtained by inflation from a finite quotient. Therefore a factorization threshold by itself is **NON-NOVEL / CLOSED**.

### F2 — Recognition of a quotient from the target
Existing literature also contains results in the reverse information direction, notably statements of the form “the degree ≤2 cohomology determines G_[3].” Thus recognition/reconstruction of a particular quotient from cohomological data is **PARTIALLY COVERED / KNOWN**. This direction is not identical to the Paper 3 recognition threshold, which asks when a finite window determines T.

### F3 — Explicit separation of thresholds
The audited corpus did not identify a theorem that explicitly treats
\[
f_T(\mathcal C;D_\bullet)\quad\text{and}\quad r_T(\mathcal C;D_\bullet)
\]
as separate threshold invariants and studies whether they can differ. Existing work generally states one quotient/target determines another, rather than isolating factorization depth versus recognition depth as distinct numerical objects. Classification: **OPEN / STRONG CANDIDATE**. This is not yet a novelty claim.

### F4 — Separation example
No explicit example was found in the audited corpus exhibiting a genuine numerical separation between factorization and recognition thresholds. In particular, no verified pair has yet been constructed that forces a distinction of the required kind. Classification: **OPEN / LOAD-BEARING**.

### Decision
The next authorized attack is **not** the pure Bockstein threshold. First attempt to construct or rule out a genuine factorization-vs-recognition separation example. Only after this gate is closed should the project move to the pure Bockstein candidate or filtration/category dependence.

Logical boundary: F1 being known does not close F3/F4; F3 being absent from the audited literature does not prove novelty. A concrete theorem or separation construction is required.

Current Paper 3 status:
- Efrat–Mináč Theorem A/B audit: **NON-NOVEL / CLOSED**
- Factorization concept: **NON-NOVEL / CLOSED**
- Factorization vs recognition distinction: **OPEN / STRONG CANDIDATE**
- Explicit separation: **OPEN / LOAD-BEARING**
- Pure Bockstein sharpness: **DEFERRED**
- Ultimate finite-window recognition program: **ACTIVE**


## 2026-09-27 — PAPER 3 S2 BOCKSTEIN SEPARATION AUDIT

The rank-2 candidate pair
\[
G_p=\langle x,y\mid x^p[x,y]=1\rangle,
\qquad
G_{p^2}=\langle x,y\mid x^{p^2}[x,y]=1\rangle
\]
has now passed the independent Bockstein-difference gate.

For the Bockstein
\[
\beta_G:H^1(G,\mathbf F_p)\to H^2(G,\mathbf F_p)
\]
from
\[
0\to\mathbf F_p\to\mathbf Z/p^2\to\mathbf F_p\to0,
\]
the standard one-relator formula reads the mod-p coefficient of the p-power term in the quadratic initial form of the relator. Direct relator-lift evaluation gives the same result.

With \(\chi_x,\chi_y\) dual to \(x,y\):
- for \(G_p\), \(\beta(\chi_x)=\pm u\neq0\), \(\beta(\chi_y)=0\), so \(\operatorname{rank}\beta=1\) and \(\operatorname{Im}\beta=H^2\cong\mathbf F_p\);
- for \(G_{p^2}\), the coefficient is \(p\equiv0\pmod p\), so \(\beta=0\) and \(\operatorname{Im}\beta=0\).

Thus both requested distinctions pass:
1. the whole Bockstein maps are non-isomorphic because their ranks differ;
2. their images differ, one nonzero and one zero.

Together with S1, already PASS/CLOSED with
\[
W_p(G_p)\cong W_p(G_{p^2}),
\]
this yields the concrete recognition lower bound
\[
\boxed{r_{T_\beta}(\mathcal C;D_\bullet)\ge p+1}
\]
for any category containing this pair under the current Zassenhaus-window definition.

This is **PASS / LOCAL** as a lower-bound result. It does not establish the exact equality \(r_{T_\beta}=p+1\), and it does not yet establish \(f_T\ne r_T\) because that comparison must use the same target \(T_\beta\).

Detailed record: research/PAPER3_S2_BOCKSTEIN_SEPARATION_AUDIT_2026-09-27.md.

Next Gate: upper-bound test at \(p+1\), with same-target factorization kept logically separate.


## 2026-09-27 — PAPER 3 S4 TARGET NONTRIVIALITY GATE: T_cup INVALID

The proposed S4 target T_cup(G)=(H^1(G,F_p), cup), viewed as an isomorphism class, has failed the mandatory target-nontriviality pre-check. In the fixed-rank Demuškin category, the cup pairing is a nondegenerate alternating form, and all such forms of the same finite dimension are isomorphic. Hence equal-rank Demuškin groups cannot form a separation pair with different T_cup.

Classification: S4 T_cup = INVALID / TRIVIAL TARGET — CLOSED; rank-4 S4 computation = STOPPED / NOT AUTHORIZED; S4 program = GATE FAILURE / RE-DESIGN REQUIRED; Target Nontriviality Gate = ACTIVE / LOAD-BEARING.

Mandatory target gate for future candidates: TN1 nontriviality; TN2 non-derivability from an already-closed target; TN3 genuine filtration dependence; TN4 prior-art audit. Only targets passing TN1–TN4 may enter concrete separation computation.

Decision: do not perform further S4 rank-4 computation until a replacement target passes the target gate. Detailed audit: research/PAPER3_S4_TARGET_NONTRIVIALITY_GATE_T_CUP_2026-09-27.md.


## 2026-09-27 — PAPER 3 S4 STRUCTURAL CORRECTION: TN2 REVISED

A structural objection was identified and accepted: in the fixed-rank Demuškin category, q is a complete isomorphism invariant. Hence every isomorphism-invariant target T(G) is abstractly a function of q. The previous literal TN2 condition, T != F(chi mod p^k), is therefore too strong as a universal gate and may be structurally impossible or merely a reparameterization distinction.

Revised gate: **TN2' — Non-redundancy / resolution test.** For each candidate target, determine (i) which classification parameters determine T, (ii) what p-adic/finite resolution of those parameters T requires, (iii) whether an existing theorem already supplies the corresponding threshold, and (iv) whether the target yields genuinely new mathematics rather than a repackaging.

Strategic fork recorded:
1. Fixed-rank one-parameter Demuškin category: use the already established family T_k = chi mod p^k and r_{T_k}=n(k)=p^{k-1}+1 as a clean target-dependent threshold family, while classifying it as reinterpretation/generalization unless a new theorem is proved.
2. Expand the category to a multi-parameter class, e.g. free products of several Demuškin blocks already studied in Paper 2, where aggregate versus blockwise targets may yield genuinely richer threshold dependence.

Massey-product and Aut-orbit searches are PAUSED pending this fork; no new computation is authorized yet.
Classification: **OPEN / LOAD-BEARING**.

## 2026-09-27 — CONTINUITY PROTOCOL: AUTOMATIC RECORDING ENABLED

Decision: research-changing evidence is now treated as an automatic repository-write trigger. The assistant must not wait for a separate “기록 반영” request.

Trigger events include:
- material literature/prior-art findings;
- theorem/lemma verification, correction, or falsification;
- PASS/LOCAL, FAIL/CLOSED, OPEN, CONDITIONAL, or HISTORICAL/SUPERSEDED outcomes;
- changes to novelty or logical boundaries;
- opening/freezing/downgrading/promoting/abandoning a branch;
- changes to the next authorized action.

Default recording:
1. research/00_RESEARCH_LOG.md — chronology/evidence;
2. CURRENT_STATE.md — active state and next action when changed;
3. RESEARCH_MAP.md — only for global architecture/status changes;
4. relevant stage/audit document — load-bearing branch details.

The continuity protocol was amended accordingly in commit 399284d86566b3b70c28066db424ee6eb9fb0c58.

Current F1 M2 literature audit remains OPEN / MANDATORY. No Massey computation is authorized until the theorem-by-theorem prior-art audit is completed and classified.



## 2026-09-27 — PAPER 3 F1/q=3,n=4 MASSEY–DWYER ORIGINAL-TEXT AUDIT

Blumer–Quadrelli arXiv:2603.15464v2 원문(main.tex)을 직접 대조하여, 예정된 F1 sharpness computation의 입력·Dwyer convention·lift 조건을 확정했다.

### Confirmed from source
- 각 \(\alpha_h\in H^1(G,\mathbf F_3)\)는 생성자들에 대한 값으로 결정되는 cohomology class이며, 단일 matrix entry가 아니다.
- Dwyer convention은 \((A_i)_{h,h+1}=\alpha_h(x_i)\), \((B_i)_{h,h+1}=\alpha_h(y_i)\)이다. 따라서 \((\alpha_1,\ldots,\alpha_4)\)에서 \(A_1,B_1,A_2,B_2\) 등의 행렬을 구성해야 하며, 역방향 \(A\mapsto(\alpha_h)\)를 기본 정의로 사용할 수 없다.
- fourfold Massey product의 necessary adjacent condition은 \(\alpha_h\smile\alpha_{h+1}=0\)이다.
- \(d=2\)인 F1에서는 이를 \(c_hd_{h+1}-d_hc_{h+1}=0\)로 쓸 수 있다. 여기서 \(c_h=\alpha_h(x_2), d_h=\alpha_h(y_2)\).
- \(q=3,n=4\)에서 full Dwyer relation은 \(A_1^3[A_1,B_1][A_2,B_2]=I_5\)이다.

### Critical logical correction
\([A_1^3,B_1]=1\)은 full fourfold Dwyer lift의 존재와 동치가 아니다. 이는 \(n\le q\) 증명에서 자동으로 확보되는 local step이었으나, \(n=q+1\)에서는 더 이상 자동이 아니며, 이후 \(A_2,B_2\)의 compensation 가능성을 별도로 검사해야 한다.

### Classification
- alpha extraction definition: **PASS / CLOSED**
- Dwyer matrix convention: **PASS / CLOSED**
- adjacent cup condition: **PASS / CLOSED**
- naive \(A\mapsto\alpha\) implementation assumption: **FAIL / CLOSED**
- identifying \([A_1^3,B_1]=1\) with full lift: **FAIL / CLOSED**
- F1 \(q=3,n=4\) local obstruction / sharpness: **OPEN / LOAD-BEARING**

### Computation boundary
Nonzero \(\alpha_h\in H^1(G,\mathbf F_3)\cong\mathbf F_3^4\)만 제한하면 sequence 후보는 \(80^4=40,960,000\)개이다. 다만 즉시 전수계산하지 않고, 먼저 hand-check 가능한 소예와 독립 구현 검증을 거친 뒤 cup filter → \((A_1,B_1)\) realization → \([A_1^3,B_1]\) local test → \((A_2,B_2)\) compensation → full relation 순으로 분리해 계산한다.

Next authorized action: original-text audit 결과를 기준으로 small-example independent verification을 수행한 뒤 exhaustive computation 여부를 결정한다.

## 2026-09-27 — PAPER 3 F1 q=3,n=4 LEVEL A EXHAUSTIVE COMPUTATION CLOSED

The authorized Level-A computation was completed for the smallest F1 sharpness test (p,q,d,n)=(3,3,2,4), using the original Blumer–Quadrelli/Dwyer conventions already audited.

The search space is 80^4=40,960,000 ordered nonzero H^1(G,F_3) sequences. Exact enumeration gives:
- all sequences: **40,960,000**;
- adjacent cup-pass: **3,681,856**;
- Level-A local-obstruction pass: **2,546,560**;
- Level-A local-obstruction fail: **1,135,296**.

Thus, among cup-pass sequences, the explicit Level-A obstruction is nonzero for approximately **30.8348%**. The verified conclusion is: cup-vanishing does not imply the Level-A local condition.

This is **not** yet a sharpness result for the fourfold Massey/Dwyer lift. The full relation is still A_1^3[A_1,B_1][A_2,B_2]=I_5, and Level-B compensation by A_2,B_2 must be tested separately.

The Level-B structural reduction was also recorded: after the adjacent cup filter, D_13=D_24=D_35=0, hence (CD)_15=0 and the central coordinate reduces to T_15=C_15+D_15. This does not imply that compensation always exists, because the other matrix coordinates must vanish simultaneously.

Classification:
- Level-A exhaustive enumeration: **PASS / CLOSED**
- cup-vanishing does not imply Level-A local condition: **PASS / CLOSED**
- full F1 q=3,n=4 sharpness: **OPEN / LOAD-BEARING**
- Level-B compensation: **OPEN / LOAD-BEARING**
- “Level-A failure implies full-lift failure”: **NOT ESTABLISHED**

Detailed record: research/PAPER3_F1_Q3_N4_LEVEL_A_COMPUTATION_2026-09-27.md.

Next authorized action: **Level-B symbolic reduction before any large matrix enumeration**.

## 2026-09-27 — PAPER 3 PRIORITY RESET: F1 MASSEY SHARPNESS COMPUTATION DEFERRED

After re-checking the authoritative Paper 3 program against the current F1 Level-A result, the project decision is to **de-prioritize the q=3,n=4 Massey/Dwyer sharpness branch**. The Level-A computation remains valid and recorded, but it is not required by the core Paper 3 finite-window recognition program unless it yields a structural threshold theorem or separation mechanism.

Reason: the active Paper 3 objective is the category-relative recognition threshold r_T(C;D_bullet), with factorization and recognition explicitly separated. The current F1 Level-A/B calculation addresses a specific n=q+1 Massey-vanishing sharpness question, which is at most an application/case study and is not presently the load-bearing definition, basic theory, or first non-corollary recognition theorem.

Important correction to the proposed alternative: the fixed-rank Demuškin cup target T_cup as an isomorphism class is already CLOSED as trivial/non-discriminating, by the S4 target-nontriviality gate. Therefore no new T_cup rank-4 computation is authorized.

The more coherent active route is the already-open Bockstein target T_beta: S1 gives a finite-window lower-bound pair and S2 gives r_{T_beta} >= p+1 as PASS/LOCAL. The next useful gate is an upper-bound test at p+1, while keeping same-target factorization versus recognition logically separate.

Decision:
- F1 Level-A result: **PASS / CLOSED**, retained as evidence and possible future case study.
- F1 Level-B compensation: **OPEN / DEFERRED**; no further large enumeration authorized now.
- F1 q=3,n=4 Massey sharpness as Paper 3 load-bearing route: **DEFERRED / NOT LOAD-BEARING**.
- T_cup isomorphism-class route: **FAIL / CLOSED — TRIVIAL TARGET**; no computation.
- T_beta recognition threshold: **OPEN / LOAD-BEARING**.

Next authorized action: **Bockstein upper-bound test at p+1**, followed by a same-target comparison with the factorization threshold. No new Massey computation unless a later structural argument shows it is needed.


## 2026-09-27 — PAPER 3 T_beta UPPER-BOUND PRE-CHECK: W_{p+1} ⇒ G_ab/p^2G_ab FIXED

The proposed Bockstein upper-bound route was audited at the key filtration step. A useful correction is required: the earlier statement that W_{p+1} does not generally determine G_ab/p^2G_ab was too weak. In fact, for the Zassenhaus filtration one has the general inclusion

D_{p+1}(G) ⊆ G^{p^2}[G,G].

This follows directly from Lazard's formula D_n=∏_{ip^j≥n} γ_i^{p^j}: at n=p+1, the i=1 contribution begins at G^{p^2}, while every i≥2 contribution lies in [G,G]. Hence, with K=G^{p^2}[G,G],

D_{p+1} ⊆ K,

and therefore the quotient W_{p+1} contains enough information to recover
G/K ≅ G_ab/p^2G_ab:
the image K/D_{p+1} is intrinsically the subgroup
(G/D_{p+1})^{p^2}[(G/D_{p+1}),(G/D_{p+1})]
of the truncated quotient group.

Thus the precise functorial chain is

W_{p+1}(G)
→ G/D_{p+1}(G)
→ G/[G^{p^2}[G,G]]
≅ G_ab/p^2G_ab.

This is stronger than merely reading a p-power map D_1/D_2→D_p/D_{p+1}; the latter can be retained as an equivalent structural interpretation, but it should not be used as the primary proof unless its well-definedness and duality are separately stated.

For the odd-p fixed-rank Demuškin category, the remaining upper-bound step is then:
G_ab/p^2G_ab determines the mod-p^2 liftability kernel of H^1(G,F_p), hence the Bockstein rank; because H^2 has dimension 1, rank β∈{0,1}, and the fixed Demuškin classification identifies the corresponding Bockstein isomorphism class.

Classification:
- W_{p+1} ⇒ G_ab/p^2G_ab: **PASS / CLOSED** (general pro-p filtration fact).
- W_{p+1} ⇒ rank β: **PASS / LOCAL**, pending the explicit Bockstein/liftability lemma and Demuškin parameter check in the chosen odd-p category.
- W_{p+1} ⇒ [β]: **OPEN / LOAD-BEARING** until that lemma is written with exact hypotheses.
- T_beta upper bound r_{T_beta}≤p+1: **OPEN / LOAD-BEARING**.

Next authorized action: write the explicit Bockstein kernel/liftability lemma and then the Demuškin rank-to-isomorphism step; do not claim the full upper bound until both are independently checked.


## 2026-09-27 — PAPER 3 T_beta UPPER BOUND CLOSED

The authorized upper-bound test for the Bockstein target has been completed.

For
\[
0\to\mathbf F_p\to\mathbf Z/p^2\to\mathbf F_p\to0,
\]
the long exact sequence gives
\[
H^1(G,\mathbf Z/p^2)\to H^1(G,\mathbf F_p)
\xrightarrow{\beta_G}H^2(G,\mathbf F_p).
\]
With trivial coefficient action,
\[
\ker\beta_G=
\operatorname{im}\left[
\operatorname{Hom}(G,\mathbf Z/p^2)\to
\operatorname{Hom}(G,\mathbf F_p)
\right].
\]
Thus the Bockstein kernel is exactly the set of mod-p characters liftable to \(\mathbf Z/p^2\).

Every \(\mathbf Z/p^2\)-valued character factors through
\[
G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}.
\]
The already closed inclusion
\[
D_{p+1}(G)\subseteq G^{p^2}[G,G]
\]
implies that \(W_{p+1}\) determines this quotient. Hence \(W_{p+1}\) determines \(\ker\beta_G\), and therefore \(\operatorname{rank}\beta_G\).

For the fixed-rank Demushkin category,
\[
\dim H^1(G,\mathbf F_p)=d,\qquad \dim H^2(G,\mathbf F_p)=1.
\]
Two linear maps \(\mathbf F_p^d\to\mathbf F_p\) are isomorphic iff they have the same rank. Therefore the abstract Bockstein target
\[
T_\beta(G)=[\beta_G]
\]
is determined by \(W_{p+1}(G)\).

Important boundary: this identifies the linear-map isomorphism class, not the Demushkin group or its parameter \(q\). Rank zero does not distinguish \(q=p^2,p^3,\ldots\).

Thus
\[
r_{T_\beta}\le p+1.
\]
Combined with the existing S1/S2 lower bound
\[
r_{T_\beta}\ge p+1,
\]
we obtain
\[
\boxed{r_{T_\beta}=p+1}
\]
in the declared category.

Classification:
- Bockstein kernel/liftability: **PASS / CLOSED**
- \(W_{p+1}\Rightarrow\ker\beta\): **PASS / CLOSED**
- \(W_{p+1}\Rightarrow[\beta]\): **PASS / CLOSED**
- \(r_{T_\beta}\le p+1\): **PASS / CLOSED**
- \(r_{T_\beta}=p+1\): **PASS / CLOSED**
- same-target factorization-vs-recognition separation: **OPEN / LOAD-BEARING**

Detailed audit: research/PAPER3_T_BETA_UPPER_BOUND_AUDIT_2026-09-27.md.

Next authorized action: define/test the same-target factorization threshold \(f_{T_\beta}\); do not infer it from the recognition threshold. No new Massey computation is authorized.



## 2026-09-27 — PAPER 3 T_beta FACTORIZATION THRESHOLD AUDIT CLOSED

The same-target factorization threshold was independently determined for T_beta(G)=[beta_G], without using the recognition equality r_{T_beta}=p+1 as evidence.

Upper bound: D_{p+1}(G) is contained in G^{p^2}[G,G], so W_{p+1} recovers G_ab/p^2G_ab. The Bockstein kernel is the image of Hom(G,Z/p^2) -> Hom(G,F_p), hence is determined by that quotient. Since dim H^2=1 in the fixed-rank Demushkin category, the Bockstein map isomorphism class is determined by its rank. Therefore f_{T_beta} <= p+1.

Lower bound: the independently verified S1/S2 pair has W_p(G_p) isomorphic to W_p(G_{p^2}) but T_beta(G_p) non-isomorphic to T_beta(G_{p^2}), so f_{T_beta}>p.

Therefore f_{T_beta}=p+1. This is a direct factorization proof, not an inference from r_{T_beta}=p+1. Consequently this target gives equality f_{T_beta}=r_{T_beta}=p+1 in the declared category/window, and the same-target separation attempt is FAIL / CLOSED.

Detailed audit: research/PAPER3_T_BETA_FACTORIZATION_THRESHOLD_AUDIT_2026-09-27.md.

Next authorized action: close the T_beta separation branch and return to the general separation search, changing target/category/filtration-window rather than reusing the same Bockstein target.

## 2026-09-27 — PAPER 3 SEPARATION AXIS: FACTORIZATION VS RECOGNITION DEFINITIONAL CORRECTION

A structural correction is now required before any new target computation.

If the factorization invariant is defined for the **same target** T by
\[
f_T=\min\{n:T\text{ factors through }W_n\},
\]
and recognition is defined by
\[
r_T=\min\{n:W_n(G)\cong W_n(H)\Rightarrow T(G)\cong T(H)\text{ for all }G,H\in\mathcal C\},
\]
then these are the same information condition at category level: both say precisely that T is determined by the n-window. Therefore a genuine numerical separation \(f_T\ne r_T\) for the same T cannot be the intended research phenomenon.

The meaningful separation axis is instead:
\[
\boxed{\text{factorization threshold }f_O\text{ of a richer carrier/observation }O
\quad\text{versus recognition threshold }r_T\text{ of a target }T=\Phi(O).}
\]
Here O may retain extension, cocycle, orientation, or other structure that is later compressed to T. Then \(f_O\) and \(r_T\) can legitimately differ because they are thresholds for different objects.

This explains the T_beta outcome more sharply: once O=T_beta, equality with the recognition threshold is forced by definition, not an accidental theorem. The computation \(f_{T_\beta}=r_{T_\beta}=p+1\) is therefore useful as a consistency check, but it cannot be a separation result.

New Paper 3 gate:
- F3 as literal same-target \(f_T\) vs \(r_T\) separation: **INVALID / CLOSED — DEFINITIONAL IDENTITY**.
- F3' richer-carrier vs coarser-target separation: **OPEN / LOAD-BEARING**.
- First task: identify a nontrivial carrier O and a genuine quotient/compression \(\Phi(O)=T\), then determine \(f_O\) and \(r_T\) independently.

Candidate direction retained from earlier work: the finite Kummer/affine orientation carrier O_k versus a coarser target T_k (or a secondary cohomological target), but it must pass a non-redundancy and prior-art screen before computation. The target must not collapse back to the same object O_k.

This correction supersedes any earlier language suggesting that a same-target numerical inequality \(f_T\ne r_T\) itself could be a theorem.

## 2026-09-27 — PAPER 3 CARRIER-TARGET SEPARATION GATE OPENED

The corrected architecture has been operationalized in `research/PAPER3_CARRIER_TARGET_SEPARATION_GATE_2026-09-27.md`.

Candidate A (affine/Kummer carrier -> Bockstein target) is retained as a **control separation**, not a novelty claim: the carrier is deliberately richer than the Bockstein target, so its factorization depth can exceed the target's recognition depth. This validates the corrected carrier-vs-target architecture but does not by itself constitute new mathematics.

Candidate B, the mod-27 Bockstein-extension carrier
\[
\mathcal B_{27}=(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9),
\]
is promoted to the first **strong candidate** because it is coordinate-free and potentially richer than T_beta. Its exact compression to a genuinely coarser target, factorization depth, and prior-art status are not yet closed.

Candidate C (multi-parameter category) remains secondary.

Next authorized action: Candidate B line-by-line non-redundancy/prior-art audit. No large computation is authorized until the carrier, compression map, upper factorization bound, and independent target recognition bound are all explicit.

## 2026-09-27 — CANDIDATE B MOD-27 BOCKSTEIN CARRIER AUDIT COMPLETE

The requested mathematical and literature audit is complete for the mod-27 coefficient-extension carrier.

Final decision: exact object/functoriality PASS/CLOSED; full standard-family structured classification PASS/CLOSED; finite q-layer detection PASS/LOCAL; new non-tautological mod-27 orientation carrier FAIL/CLOSED.

The earlier abstract-symmetry no-go remains HISTORICAL/SUPERSEDED because group-level realizability of that symmetry was not proved and is not used here.

Literature audit found strong direct overlap with Simons (1989), which explicitly constructs characteristic Demushkin tower level subgroups using a Bockstein on H^1(X,Z/q), together with the established Kummerian/canonical-orientation framework of Efrat-Quadrelli and later 1-cyclotomic work. Higher/generalized Bockstein constructions are also established. These sources do not prove identity with the exact proposed carrier, but they block novelty for the coefficient-extension idea alone.

Strategic consequence: no further beta_1,beta_9 scans. The next decisive target is the intrinsic P_4/D_10 higher power/relation residual and its scalar normalization/transport theorem.

Detailed audit: research/PAPER3_MOD27_BOCKSTEIN_CARRIER_LINE_AUDIT_2026-09-27.md (commit 7a3f7d5d56dc261f9d3f80e825fe4c86a741c63b).


## 2026-09-27 — PAPER 3 HA58/P4/D10 FULL INTRINSICITY AUDIT

Audit record:
\`research/PAPER3_HA58_P4_D10_FULL_INTRINSICITY_AUDIT_2026-09-27.md\`

Sequence completed:
1. intrinsic definition;
2. coordinate dependence;
3. transport/functoriality;
4. projective direction;
5. scalar normalization.

Final results:
- standard-family HA58 residual and q=9 versus 27|q detection: **COMPUTED**
- intrinsic HA58 residual definition: **OPEN**
- residual transport/functoriality: **OPEN**
- standard-family projective direction: **COMPUTED**
- canonical projective map: **OPEN**
- frozen scalar normalization: **COMPUTED**
- canonical scalar normalization: **OPEN**
- single-vector \(t_2\) realization: **COUNTEREXAMPLE**
- \(t_2/\langle p\rangle\) repair: **COUNTEREXAMPLE**
- diagonal \((t_2,\mu)\) repair: **COUNTEREXAMPLE**
- intrinsic connecting family \(\rho_3\mapsto\delta_{3,\rho_3}\): **PROVED**

Decisive no-go: relation conjugation \(r\mapsto vrv^{-1}\) can shift the putative \(t_2\) by \(p\) while leaving the intrinsic connecting-obstruction family unchanged. Therefore the proposed canonical single vector cannot be the correct intrinsic carrier.

Finite source ledger: after /9 mod 3, only \(F^9\) and the old \(\gamma_2^3\) sector survive; \(\gamma_3^3,\gamma_4\) vanish at this finite depth.

Strategic reset: stop the single-vector P_4/t_2 route. The next authorized problem is the construction/compression of a richer affine/torsor-valued carrier for the intrinsic secondary obstruction family, preserving coefficient-lift dependence and testing compatibility with the established mod-9 obstruction.


## 2026-09-27 — CRITICAL REVIEW OF HA58/P4/D10 REPORT

The report was critically re-audited against the repository source chain.

Correction:
- original presentation was insufficiently self-contained;
- intrinsic cohomological family \(\rho_3\mapsto\delta_{3,\rho_3}\) is nevertheless genuinely defined and proved at the cohomological-object level in HA61-B5-8/B5-10;
- single-vector \(t_2\) no-go is genuinely supported by HA61-B5-12 through the explicit relator-conjugation witness \(t_2\mapsto t_2+\lambda(v)p\).

Locked distinction:
\[
\text{intrinsic cohomological }\delta_3\text{ family}=\mathbf{PROVED},
\]
while
\[
W_n\to\{\delta_{3,\rho_3}\}=\mathbf{OPEN},
\qquad
\{\delta_{3,\rho_3}\}\to\chi\bmod27=\mathbf{OPEN}.
\]

“Frozen” now means fixed presentation, coefficient-extension convention, basis and transgression normalization; it does not imply intrinsicity.

Literature claim narrowed: Quadrelli 2024 Example 2.6 is retained as external support for canonical Demuškin orientation/Kummer lifting; Mináč–Pasini–Quadrelli–Tân 2021 is retained for Zassenhaus/quadratic-dual background. The previous broad claim about a source proving loss of orientation from Zassenhaus data is withdrawn pending exact primary-source verification.

Audit correction commit: 471321c973de05c6c5ac407f3944b3a12017b331.


## 2026-09-27 — HA58 SECOND CRITICAL REVIEW / SCOPE CORRECTION

The second critical review identified four scope issues and they are now locked.

1. The δ_3 family is PROVED only as a cohomological object/natural family indexed by L(ρ_2). Its derivation from finite filtered data is OPEN.
2. If ρ_2 is the already-known canonical mod-9 orientation, nonemptiness of L(ρ_2) is EXTERNAL; non-circular finite-filtered recovery of the lift information is OPEN.
3. The t_2 conjugation no-go is a genuine COUNTEREXAMPLE in the q=3 rank-four branch and is sufficient to refute a universal single-vector theorem. It is not claimed to cover every q-branch.
4. The full-torsor zero-selector uniqueness route is COUNTEREXAMPLE / CLOSED in rank 4; the variation formula, finite-filtered existence, and any one-dimensional lift-direction construction remain OPEN.

The strategic phrase “torsor-valued carrier” is retained only as a candidate compression architecture. The next load-bearing problem is the intrinsic finite-window factorization W_n → {δ_{3,ρ_3}}, with a precise functorial category and without importing the canonical orientation itself.

Detailed correction: research/PAPER3_HA58_P4_D10_FULL_INTRINSICITY_AUDIT_2026-09-27.md §14.


## 2026-09-27 — HA58 THIRD CRITICAL REVIEW / VARIATION FORMULA CORRECTION

The variation identity for the lift-indexed connecting family remains OPEN in HA61-B5-13. Therefore the rank-4 kernel calculation yields only a conditional no-go for singleton fixed-f zero selection; it does not by itself close the unconditional zero-selector route. The correct status is: variation formula OPEN; conditional 27-element affine-hyperplane consequence PROVED CONDITIONALLY; unconditional singleton zero-selector OPEN.

The next gate is also refined: the mod-9 projective degree-(2,3) carrier/recovery is already audited as PASS/CLOSED at its declared level and should not be reopened. The unresolved sequence is finite-input access to L(ρ_2), finite factorization to the δ_3 family, then χ mod 27 reconstruction/compression.

Detailed correction: research/PAPER3_HA58_P4_D10_FULL_INTRINSICITY_AUDIT_2026-09-27.md §15.


## 2026-09-27 — HA58 CRITICAL REVIEW #4

Direct cochain calculation proves the variation identity for rho_3'=rho_3(1+9nu): delta_{rho_3'}(f)-delta_{rho_3}(f)=nu cup bar(f), where bar(f) is the mod-3 reduction, under the standard convention. The earlier Ext/Yoneda shortcut is withdrawn because multiplication by 3 on Z/9 is not injective. For bar(f) != 0 in rank 4, any nonempty fixed-f zero-set has 27 lifts; nu=0 is not automatically a zero. Finite-filtered access to the lift family remains OPEN. See the HA58 audit Critical Review #4.


## 2026-09-28 — δ3 / MAZUR / MASSEY PRIOR-ART AUDIT

Before any new carrier computation, the surviving family
[
\rho_3\mapsto\delta_{3,\rho_3},qquad
\delta_{3,\rho_3}:H^1(G,\mathbf Z/9(\rho_2))\to H^2(G,\mathbf F_3)
]
was compared with Mazur deformation theory, Efrat's Zassenhaus/Massey/unipotent embedding problems, and recent A_3-formality work.

Findings:
- Mazur supplies the same general small-extension/H^2-obstruction mechanism, but \delta_{3,\rho_3} is **not literally Mazur's deformation obstruction for \rho_2\to\rho_3**: \rho_3 is already fixed and the obstruction concerns lifting a cohomology class f.
- Efrat's U_n/Massey mechanism has the same abstract obstruction pattern, but its lifted object is a unipotent representation/defining system rather than the twisted coefficient 1-cocycle f. Thus **\delta_3 is not literally the U_4/Massey embedding obstruction**.
- Strong Massey vanishing for Demushkin groups is known, so fixed-category Massey vanishing remains a CLOSED constant target; it does **not** imply the whole coefficient-extension \delta_3 family is zero.
- Pál–Quick A_3-formality supplies independent q-sensitive higher-cohomological information, but its DGA/Hochschild canonical-class input is not the finite Zassenhaus window or the \delta_3 family.

Classification:
- general H^2 obstruction mechanism: **KNOWN / PASS-CLOSED**
- \delta_3 = Mazur deformation obstruction: **FAIL / CLOSED**
- \delta_3 = Efrat U_4/Massey obstruction: **FAIL / CLOSED**
- strong Demushkin Massey vanishing: **PASS / CLOSED**
- strong Massey vanishing => \delta_3=0: **NOT ESTABLISHED; do not infer**
- A_3-formality = \delta_3: **OPEN / not found**
- finite filtered factorization W_n -> {\delta_{3,\rho_3}}: **OPEN / LOAD-BEARING**
- novelty of finite-window factorization: **OPEN / CONDITIONAL**

Detailed audit:
research/PAPER3_DELTA3_MAZUR_MASSEY_PRIOR_ART_AUDIT_2026-09-28.md
commit 3c6c0eac5e91fe5ee3c36ae66487e3e087f0522d.

Next authorized action: perform a narrower Kummerian/1-cyclotomic prior-art comparison for whether existing theorems construct the coefficient-lift torsor or equivalent connecting-map family from finite quotient/Zassenhaus data without assuming the canonical orientation. No new carrier computation is authorized before that comparison.


## 2026-09-28 — KUMMERIAN / 1-CYCLOTOMIC FOUR-LAYER PRIOR-ART AUDIT

Completed the authorized literature-first audit before computation. Efrat–Quadrelli (2019), Quadrelli–Weigel (2022), and Quadrelli (2024) confirm the standard Kummerian finite coefficient-lifting and cocycle framework and the classical uniqueness of the canonical Demushkin orientation. The four layers were separated: (i) L(rho_2) is formally a standard lift torsor when nonempty but no bare-Q_k intrinsic construction was found; (ii) individual finite coefficient-lift obstruction machinery is known once orientation is supplied, but the exact project family is not located as an orientation-free finite-input object; (iii) the exact variation law delta_{rho_3(1+9nu)}-delta_{rho_3}=nu cup f-bar was not located as a Kummerian/1-cyclotomic theorem; (iv) no direct theorem reconstructing the full family from bare Q_k=G/P_{k+1} without importing orientation was found.

Classification: (i) PASS / LOCAL; (ii) PASS / LOCAL; (iii) OPEN / NOT VERIFIED; (iv) OPEN / LOAD-BEARING. Classical canonical orientation/Kummerianity remains KNOWN/CLOSED. The finite-window factorization remains the decisive boundary.

Detailed record: research/PAPER3_DELTA3_MAZUR_MASSEY_PRIOR_ART_AUDIT_2026-09-28.md, Addendum 3.
Next authorized action: compare the four-layer result against U1–U5 and isolate the genuinely finite-data statements; no new carrier computation until that comparison is complete.


## 2026-09-28 — U1–U5 VS KUMMERIAN PRIOR-ART BOUNDARY

The Kummerian/1-cyclotomic four-layer audit was compared directly with U1–U5. Canonical orientation, Kummerianity, finite coefficient lifting, and full-group existence are classical. U5 uniqueness overlaps the classical uniqueness content and is not itself the novelty claim. The potentially distinct component is U1–U2: arbitrary-candidate twisted crossed cocycles factor through the specific finite Zassenhaus quotient (Q_k=G/P_{k+1}) via the finite semidirect-product filtration. U3 supplies the finite obstruction realization; U4 is presentation-local. Thus the possible publication novelty is localized at the finite-factorization/assembly layer.

Classification: **PASS / LOCAL** for the boundary localization; publication novelty remains **OPEN / CONDITIONAL**. Next authorized action: final source-level comparison of U1–U3 against equivalent finite-coefficient quotient results; no new carrier computation.


## 2026-09-28 — Citation hygiene structural fix

- Re-audit found residual ChatGPT search citation artifacts in the Paper 3 prior-art audit's Addendum 3 (e.g. concatenated `citeturn...` markers).
- Removed the residual markers from `research/PAPER3_DELTA3_MAZUR_MASSEY_PRIOR_ART_AUDIT_2026-09-28.md` without changing the mathematical conclusions.
- Added `.github/workflows/citation-hygiene.yml`, which scans the repository on every push/PR for ChatGPT citation-artifact markers and fails CI if any are found.
- The first repository-wide run on commit `f1d18af5752afcc297759e0f895bb9af0d1a5834` completed **successfully** (workflow run `36331337426`). Therefore the repository-wide hygiene gate is currently **PASS / CLOSED** for the targeted `citeturn...` artifact pattern.
- Research content status is unchanged: U1–U3 finite-factorization prior-art comparison remains the next authorized mathematical action; no carrier computation is authorized before that comparison.


## 2026-09-28 — FINAL U1–U3 SOURCE-LEVEL PRIOR-ART COMPARISON

Primary/near-primary Kummerian literature was compared directly against U1–U3. Quadrelli (2024) gives the finite-coefficient H^1 lifting criterion, Labute's prescribed-generator cocycle criterion, and a quotient-inheritance result with extra oriented-pair hypotheses. These are genuine prior art for the ingredients, but they do not state the project's arbitrary-candidate finite factorization through Q_k=G/P_{k+1}.

Classification:
- U1 exact packaged semidirect finite-depth factorization as prior art: **OPEN / NOT FOUND**
- U2: **PASS / CLOSED** as a consequence of U1; existing Kummerian quotient theorem is **FAIL / CLOSED** as an identity
- U3 finite-window twisted-Fox assembly: **OPEN / NOT FOUND**
- possible novelty boundary: **OPEN / CONDITIONAL**, localized at finite factorization/assembly

Detailed record: research/PAPER3_DELTA3_MAZUR_MASSEY_PRIOR_ART_AUDIT_2026-09-28.md, Addendum 5.
Next authorized action: resume carrier computation under the independent U1–U3 lemma chain.


## 2026-09-28 — Citation hygiene correction

The previous hygiene CI was found to have a false-negative condition because the repository citation artifacts contain invisible Private Use Area delimiters. GitHub search identified 15 affected files. All 15 were cleaned, and direct post-cleanup reads confirmed zero Private Use Area characters and no visible citation-artifact pattern in those files.

The citation-hygiene workflow was hardened to fail on any Private Use Area character and on visible ChatGPT citation-artifact patterns. Hardened CI run 36331775297 on commit 8102ab49c3e3173bec4bd103cad7aaf07c63654a completed successfully.

The earlier hygiene PASS based on the old detector is superseded. Current repository-wide citation hygiene is **PASS / CLOSED**, based on direct file verification plus the hardened CI run. Mathematical research status is unchanged; U1–U3 prior-art comparison remains complete and carrier computation may resume.


## 2026-09-28 — Sharp Zassenhaus window for the finite Kummer selector

The authorized post-audit carrier computation closed the selector minimality gate. Set (N=3^{k-1}). U1–U3 establish sufficiency of (G/P_{N+1}). For the canonical candidate (chi_k(x_2)=(1-3)^{-1}), take (f(x_2)=1). Every lift has (z(x_2^N)=S_N z(x_2)), where (S_N=sum_{j=0}^{N-1}chi_k(x_2)^j). LTE gives (v_3(S_N)=k-1), hence (z(x_2^N)
eq0pmod{3^k}). Since (x_2^Nin P_N), the canonical lift cannot factor through (G/P_N). Therefore the preceding window fails.

Result: (oxed{n_k^{Kum}=3^{k-1}+1}) for the declared Kummer recognition selector. Explicit checks: (k=2): (z(x_2^3)=3pmod9); (k=3): (z(x_2^9)=9pmod{27}); higher checks agree. Classification: **PASS / CLOSED** for selector sharpness; **OPEN / NOT CLAIMED** for absolute minimality among arbitrary carriers; publication novelty **OPEN / CONDITIONAL**.

Detailed audit: `research/PAPER3_ZASSENHAUSZ_WINDOW_MINIMALITY_AUDIT_2026-09-28.md` (commit `6ba314ae54032ca743a8793b0492709f8118d4a4`).


## 2026-09-28 — Critical review correction: predecessor-window descent

 Critical-review correction: the sharpness proof is sound, but the audit must explicitly establish descent of the canonical action to G/P_N. This follows from Zassenhaus functoriality and D_N(1+3Z_3)=1+3^kZ_3 for N=3^{k-1}. The witness then proves failure of the Kummer predicate on the preceding quotient itself. The independent modular table is k=2..6; all-k validity comes from LTE. Classification remains PASS/CLOSED for selector sharpness.
Detailed audit correction: `research/PAPER3_ZASSENHAUSZ_WINDOW_MINIMALITY_AUDIT_2026-09-28.md` (commit `c25eb982fc8ff4280098b44e4c4992ed6f86e563d`).

## 2026-09-28 — Paper 3 Gate A: W_10 -> L(rho_2)

The first carrier gate after the sharp Kummer window was attacked without reopening the mod-9 problem. Let Q_10=G/P_10(G). The already-audited intrinsic mod-9 carrier is applied to the canonical truncation W_10 -> W_4 to obtain rho_2. Then define
\[
L_{10}(rho_2)=\{\bar rho_3:Q_{10}\to(\mathbf Z/27)^\times:\bar rho_3\bmod9=\bar rho_2\}.
\]
The finite semidirect-product filtration used in U1-U2 implies every full-group mod-27 lift rho_3 of rho_2 kills P_10, so restriction gives L(rho_2) -> L_10(rho_2); inflation gives the inverse. Hence W_10 determines the full lift domain as a finite, functorial, q-blind set, with no use of chi mod 27.

Classification: **PASS / CLOSED for Gate A at the declared category-level scope.** This is a construction result, not a novelty claim: the lift-set/torsor mechanism is standard once rho_2 is supplied. What remains load-bearing is Gate B, construction of the full family of connecting maps from the finite input. The result does not select a rho_3, prove delta-family factorization, or recover chi mod 27.

Detailed record: research/PAPER3_GATE_A_W10_TO_LRHO2_2026-09-28.md
Next authorized action: Gate B — determine whether the family {delta_{3,rho_3}} is reconstructible from W_10 and L_10(rho_2), using U2/U3 but without importing the canonical mod-27 orientation.


## 2026-09-28 — Gate B precheck: finite obstruction assembly is the actual remaining problem

After closing Gate A, the Gate B precheck separated the domain and target issues. U1-U2 give finite factorization of the candidate coefficient action and twisted H^1 domain through Q_10. U3 gives a finite twisted-Fox obstruction only after choosing a minimal one-relator presentation. What is not yet proved is a presentation-independent finite target object H_10(W_10) and natural map whose value agrees with the intrinsic connecting map delta_{3,rho_3} for every rho_3.

The naive replacement H_10=H^2(Q_10,F_3) is therefore promoted only as the next test, not as an assumed solution: Q_10 does not by itself remember the extension 1 -> P_10 -> G -> Q_10 -> 1, and no quotient-level map to H^2(G,F_3) has yet been established that recovers the Fox obstruction.

Classification: **OPEN / LOAD-BEARING**. No failure theorem is claimed yet. Next authorized attack: test H^2(Q_10,F_3) and the canonical transgression/extension subquotient as possible intrinsic finite obstruction carriers; classify any failure exactly.

Detailed record: research/PAPER3_GATE_B_W10_TO_DELTA3_FAMILY_PRECHECK_2026-09-28.md

## 2026-09-28 — Paper 3 Gate B CLOSED and Gate C CLOSED: finite delta-family and mod-27 selector

A new cohomological factorization closes the previously load-bearing finite-family gate. For Q_10=G/P_10, P_10 is contained in Phi(G), so H^1(Q_10,F_3)->H^1(G,F_3) is an isomorphism. The five-term Hochschild-Serre sequence then makes H^2(Q_10,F_3)->H^2(G,F_3) injective. Since Q_10 is a nontrivial finite 3-group, H^2(Q_10,F_3) is nonzero; Demushkinity gives dim H^2(G,F_3)=1. Hence inflation is an isomorphism. Together with U2, coefficient-extension naturality gives a finite quotient-level connecting map for every rho_3 in the finite lift set, and the full family reconstructs the intrinsic G-level family.

Classification: **Gate B PASS / CLOSED**.

The next step also closes Gate C. Classical Kummerianity gives existence of the canonical lift chi mod 27 with delta=0. If rho_3'=rho_3(1+9nu), the proved variation formula gives delta_{rho_3'}(f)-delta_{rho_3}(f)=nu cup bar(f). If two lifts had identically zero connecting maps, then nu cups every element of H^1(G,F_3) to zero. Demushkin cup nondegeneracy forces nu=0. Thus the full delta-family has a unique zero map, and that unique lift is chi mod 27.

Important distinction: fixed-f zero sets may still have 27 elements; Gate C uses the entire homomorphism delta, whose common zero selector is unique.

Classification: **Gate C PASS / CLOSED** for the fixed rank-four Demushkin category at mod 27.

Detailed records:
- research/PAPER3_GATE_B_W10_TO_DELTA3_FAMILY_RESULT_2026-09-28.md
- research/PAPER3_GATE_C_DELTA3_TO_CHI27_RESULT_2026-09-28.md

Current authorized frontier: Gate D — test the argument for arbitrary rank/prime and general k, while separating what is formal from what depends on Demushkin PD^2, finite p-group cohomology, and the specific sharp Zassenhaus depth.


## 2026-09-28 — P-1 DEGREE-3 STATUS FROZEN / FRONTIER RECALIBRATED

The degree-3 P-1 audit was reviewed against the authoritative continuity protocol and current Paper 3 state. The following is frozen:

- (L_3(F)=L_3^{\mathrm{Lie}}(F)\oplus V^{[3]}), dimensions (20+4=24): **PASS / CLOSED**.
- \(\operatorname{in}_3(r)=X_1^{[3]}\) for (r=x_1^3[x_1,x_2][x_3,x_4]): **PASS / CLOSED**, presentation-level.
- \(\dim[R_2,V]=4\): **PASS / CLOSED**.
- \(\operatorname{gr}_3(I_r)=[R_2,V]\oplus\mathbf F_3X_1^{[3]}\), dimension 5: **PASS / CLOSED**.
- \(\dim L_3(G)=19\): **PASS / CLOSED**.
- \(\ker(P_G:V\to L_3(G))=\mathbf F_3X_1\): **PASS / CLOSED — presentation-level only**.
- Canonical/\(\operatorname{Aut}(W_N)\)-invariant line from degree 3 alone: **OPEN**, and not part of the active carrier path.

The corrected filtration product fact \(F_{(2)}F_{(2)}\subseteq F_{(4)}\) is explicitly controlling; the earlier erroneous (F_{(2)}F_{(2)}\subseteq F_{(3)}) statement is superseded and must not be revived.

Research-direction correction: the degree-3 line is not to be promoted to a canonical carrier. The active Paper 3 path has already advanced through Gate A \((W_{10}\to L(\rho_2))\), Gate B (finite \(\delta_3\)-family factorization), and Gate C (unique zero-map selector recovering \(\chi\bmod27\)), all recorded as PASS/CLOSED at their stated scopes. The current frontier is **Gate D: test arbitrary \((p,d,q,k)\) and separate formal ingredients from those depending on Demuškin \(PD^2\), finite p-group cohomology, and the sharp Zassenhaus depth**.

This entry does not claim absolute carrier minimality or publication novelty. It preserves P-1 as a verified baseline computation and prevents reopening the presentation-dependent degree-3 canonical-line route without a genuinely new question.


## 2026-09-28 — PAPER 3 GATE D CLOSED: ARBITRARY ODD p, EVEN RANK d, q, k

Gate D has now been proved at the declared finite-Kummer-selector scope. The fixed rank-four p=3 q=3 calculation is not essential.

For every torsion-free Demushkin pro-p group G of even rank d>=2, odd p, allowed Demushkin parameter q, and k>=2, set N=p^{k-1}. The intrinsic finite selector on W_{N+1}=G/D_{N+1} is defined recursively: at k=2 use the finite Kummer lifting predicate; for k>2 use the full family of connecting maps for all lifts rho_k of the already recovered rho_{k-1}, selecting the unique lift whose entire connecting map is zero.

The arbitrary-p semidirect filtration A_k rt U_{1,k} gives D_{N+1} factorization for every candidate crossed cocycle. Because D_{N+1} is contained in Phi(G), H^1(W_{N+1},F_p) -> H^1(G,F_p) is an isomorphism; the five-term sequence gives injectivity in H^2, while nontrivial finite p-group cohomology and dim H^2(G,F_p)=1 for Demushkin G force H^2 inflation to be an isomorphism. Hence the full delta-family is finite and intrinsic.

The coefficient-extension variation identity and finite-coefficient PD^2 socle injectivity give uniqueness at every k. Classical Kummerianity supplies existence. No presentation-specific U4 calculation is needed for the base k=2 uniqueness.

Sharpness also generalizes. In a standard Demushkin presentation choose f(x_2)=1. For the canonical action a=chi(x_2)=(1-q)^(-1), the witness on x_2^N has geometric factor S_N. For q=0, S_N=N=p^{k-1}; for q!=0, LTE gives v_p(S_N)=k-1. Thus the canonical lift cannot factor through D_N. Therefore the declared finite Kummer selector has exact Zassenhaus threshold
\[
\boxed{n_k^{Kum}=p^{k-1}+1}
\]
for all odd p, even rank d>=2, allowed q, and k>=2.

Classification:
- D0 definition: PASS / CLOSED
- D1 arbitrary-p factorization: PASS / CLOSED
- D2 finite delta-family factorization: PASS / CLOSED
- D3 unique selector: PASS / CLOSED under classical Demushkin PD^2/Kummerian existence
- D4 sharp selector threshold: PASS / CLOSED
- absolute minimality among arbitrary carriers: OPEN / NOT CLAIMED
- publication novelty: OPEN / CONDITIONAL

Detailed proof: research/PAPER3_GATE_D_GENERAL_ODD_P_RANK_Q_K_RESULT_2026-09-28.md.
Next authorized problem: richer intrinsic carrier O versus coarser target T, not another attempt to generalize the already-closed Kummer selector.


## 2026-09-28 — PAPER 3 GATE D D2 CRITICAL CORRECTION: H^2 INFLATION IS NOT INJECTIVE

A line-by-line audit of the Gate D D2 argument identified a concrete logical failure in the five-term Hochschild–Serre step. Let Q_k=G/P_{N_k+1}(G), N=P_{N_k+1}(G). Since N⊂Phi(G), inflation H^1(Q_k,F_p)→H^1(G,F_p) is an isomorphism. Exactness then forces the restriction map to H^1(N,F_p)^{Q_k} to be zero, so the transgression is injective and
\[
\ker\bigl(H^2(Q_k,F_p)\to H^2(G,F_p)\bigr)
=\operatorname{im}(\mathrm{tra})
\cong H^1(N,F_p)^{Q_k}.
\]
Here N is a nontrivial open pro-p subgroup of a Demuškin group, hence H^1(N,F_p)≠0. Since Q_k is a finite p-group acting on a nonzero finite-dimensional F_p-vector space, the fixed-point space is nonzero. Thus the claimed H^2-inflation injectivity is not merely unverified: the current argument implies a nonzero kernel. The conclusion H^2(Q_k,F_p)≅H^2(G,F_p) is therefore rejected.

Impact:
- Gate B/D2 bare-Q_k finite delta-family reconstruction: **FAIL / CLOSED** for this argument.
- Replacement extension/transgression carrier or a precisely identified injective obstruction subspace: **OPEN / LOAD-BEARING**.
- Gate D architecture: **PASS / LOCAL**.
- D3 global uniqueness mechanism: **PASS / LOCAL**, but finite intrinsic reconstruction remains conditional on D2.
- D4 LTE sharpness: **PASS / LOCAL**.
- Fixed p=3 rank-4 q=3 Gates A-C: **PASS / CLOSED** at their recorded scopes.
- Full arbitrary-(p,d,q,k) Gate D: **CONDITIONAL / OPEN**.
- Absolute carrier minimality: **OPEN / NOT CLAIMED**.
- Publication novelty: **OPEN / CONDITIONAL**.

The stale CLOSED labels in CURRENT_STATE.md and RESEARCH_MAP.md were explicitly synchronized downward in the same research update. Next authorized action is D2 repair; no CLOSED Gate D claim is retained.


## 2026-09-28 — GATE D D2 REPAIR: CONTINUITY / DEEPER-WINDOW FORMULATION

The D2 repair direction is now recorded as follows.

For Q_k=G/P_{p^{k-1}+1}(G), let N=P_{p^{k-1}+1}(G). The previous bare-Q_k H^2-injectivity claim is rejected. However, continuous profinite cohomology gives
\[
H^2(G,F_p)\cong \varinjlim_{M\trianglelefteq_o G} H^2(G/M,F_p)
\]
along inflation. Since the Zassenhaus tower W_n=G/P_n is cofinal in the open normal subgroups of a finitely generated residually-p group, every class in H^2(Q_k,F_p) that dies in H^2(G,F_p) dies after some finite deeper window W_{N_k+m}. Because H^2(Q_k,F_p) is finite-dimensional, the ascending chain of kernels stabilizes after some finite m_0. Therefore there exists a finite deeper window that detects exactly the stable kernel of inflation to G.

Important logical boundary: this proves existence of a finite m_0, not a computable or uniform bound m_0(d,p,q,k), and it does not prove that m=1 suffices. It also does not yet prove that the specific delta-family is separated from the transient kernel at a prescribed depth.

### k=2 first obstruction check

For the rank-4 p=3 case, Q_2=W_4 and the next window is W_5. The five-term sequence for
\[
1\to P_4/P_5\to W_4\to W_5\to1
\]
shows that
\[
\ker\bigl(H^2(W_4,F_3)\to H^2(W_5,F_3)\bigr)
\]
contains the image of the transgression from
\[
H^1(P_4/P_5,F_3)^{W_5}.
\]
The kernel cannot be declared zero merely from finite-window depth; the relevant fixed-point space must be computed. More generally, the earlier P_3/P_4=20 record is about the first graded layer and should not be silently substituted for the P_4/P_5 layer appearing in this exact sequence.

Thus the first hand calculation is:
1. compute the W_5-action on P_4/P_5;
2. compute H^1(P_4/P_5,F_3)^{W_5};
3. determine the actual transgression image inside H^2(W_4,F_3);
4. evaluate the concrete delta classes on this kernel.

A nonzero kernel at m=1 does not by itself show that the canonical delta class survives there; it only proves that bare one-step deepening does not automatically make inflation injective on all of H^2(W_4,F_3).

### Revised D2 repair question

The load-bearing question is now:
\[
\boxed{\text{For the delta-family, what is the smallest }m\text{ such that its finite representatives are separated from the stable inflation kernel?}}
\]
A uniform bound in (p,d,q,k), if obtained, would restore a finite explicit selector theorem with a corrected threshold. Without such a bound, the continuity argument remains existence-only and cannot be promoted to a computable Gate D theorem.

Classification:
- continuity/stabilization existence: **PASS / LOCAL**;
- m=1 sufficiency: **OPEN**;
- uniform computable m-bound: **OPEN / LOAD-BEARING**;
- finite delta-family reconstruction at corrected depth: **OPEN / LOAD-BEARING**.


## 2026-09-28 — MRT PRIMARY-SOURCE AUDIT: c4 IS EXPLICIT

Before computing the D2 deeper-window kernel layer P_4/P_5, the Mináč–Rogelstad–Nguyễn Duy Tân source was checked directly rather than extrapolating the previously verified c_3 formula. Their Section 5, Example 5.3 explicitly gives
\[
c_4(G)=\begin{cases}(d^4-5d^2+4)/4,&p\ne2,\\(d^4-3d^2+2d)/4,&p=2.\end{cases}
\]
Thus for p=3,d=4,
\[
\boxed{\dim_{\mathbf F_3}P_4/P_5=45.}
\]
The source also states the general Proposition 5.2 formula for c_n via the w_n sequence. No k->k+1 extrapolation is used.

This closes only the dimension subtask. It does not determine the W_5-action, fixed-point space H^1(P_4/P_5,F_3)^{W_5}, transgression image in H^2(W_4,F_3), or intersection with the delta-family.

Classification:
- MRT explicit c_4 formula: **PASS / CLOSED**;
- p=3,d=4 value c_4=45: **PASS / CLOSED**;
- P_4/P_5 dimension as D2 input: **PASS / LOCAL**;
- module action/fixed points/transgression/delta separation: **OPEN / LOAD-BEARING**.

Audit: research/MRT_C4_PRIMARY_SOURCE_AUDIT_2026-09-28.md


## 2026-09-28 — D2 FIRST HAND CALCULATION COMPLETED: P4/P5 AND m=1 KERNEL

For p=3,d=4,k=2, the correct central extension is
\[
1\to P_4/P_5\to W_5\to W_4\to1.
\]
MRT Example 5.3 gives c_4=45, hence dim_F3(P_4/P_5)=45. Since [P_4,G] is contained in P_5, W_5 acts trivially on P_4/P_5. Therefore
\[
\dim H^1(P_4/P_5,F_3)^{W_5}=45.
\]
Because P_4/P_5 lies in the Frattini kernel, H^1(W_4,F_3)->H^1(W_5,F_3) is an isomorphism, so the five-term transgression is injective. Consequently
\[
\dim\operatorname{im}(tra)=45,
\qquad
\dim\ker(H^2(W_4,F_3)\to H^2(W_5,F_3))=45.
\]

The canonical delta branch is not in this kernel: its image in H^2(G,F_3) is the nonzero Demuškin top class, whereas every class killed already at W5 maps to zero in H^2(G,F_3). Thus one-step deepening does not kill the canonical branch.

However, this does NOT prove m=1 separates every false candidate. The remaining load-bearing object is the intersection of the finite delta-family at W4 with the 45-dimensional one-step inflation kernel. Exact computation of that intersection, and any resulting uniform m-bound, remain OPEN.

Important correction: earlier shorthand wrote the extension in the wrong arrow direction. The authoritative form is 1 -> P4/P5 -> W5 -> W4 -> 1. The dedicated hand-calculation record uses the corrected direction.

Classification:
- P4/P5 dimension 45: PASS / CLOSED;
- W5-action trivial: PASS / CLOSED;
- fixed-point space dimension 45: PASS / CLOSED;
- transgression rank 45: PASS / CLOSED;
- one-step inflation-kernel dimension 45: PASS / CLOSED;
- canonical delta outside the one-step kernel: PASS / LOCAL;
- m=1 full delta-family separation: OPEN / LOAD-BEARING;
- exact delta/kernel intersection: OPEN / LOAD-BEARING;
- uniform m-bound: OPEN / LOAD-BEARING.

Detailed record: research/PAPER3_D2_P4_P5_HAND_CALC_2026-09-28.md


## 2026-09-28 — PAPER 1 ↔ PAPER 3 Q4 / P4-P5 BRIDGE AUDIT

A side investigation was authorized to determine whether the old Paper 1 45-dimensional structure has a genuine relation to the current Paper 3 D2 layer.

Verified Paper 1 facts:
\[
\dim L_4=60,\quad \dim(R)_4=15,\quad \dim Q_4=45,
\]
and the verified orbit span W45 subset Q4 has dimension 45. Therefore
\[
\boxed{W_{45}=Q_4}.
\]

Using the free restricted-Lie description of the p-Zassenhaus graded object and the mild Demuškin quadratic initial relation, the degree-4 restricted graded piece has no independent degree-4 p-power generator beyond the ordinary Lie degree-4 part: X^[3] has degree 3, [X^[3],Y]=ad(X)^3Y is ordinary Lie degree 4, and the next p-power has degree 6. The degree-4 restricted relation ideal is the same quadratic-relator ideal used in Q4. Hence
\[
\boxed{P_4/P_5\cong Q_4\cong W_{45}}.
\]

The independent MRT primary-source audit gives dim P4/P5=45, agreeing with the Paper 1 quotient dimension.

For the corrected D2 extension
\[
1\to P_4/P_5\to W_5\to W_4\to1,
\]
the five-term sequence and the previously verified Frattini/transgression calculation give
\[
\ker(H^2(W_4,F_3)\to H^2(W_5,F_3))
\cong H^1(P_4/P_5,F_3)
\cong Q_4^*\cong W_{45}^*,
\]
dimension 45.

This is the precise bridge: Paper 1's old object is the degree-4 Zassenhaus fiber; Paper 3's one-step D2 ambiguity is its dual. It does not revive the old orientation-carrier route.

New load-bearing question:
\[
\boxed{\text{Does the finite delta-family have a nonzero component in the }Q_4^*\text{ transgression sector?}}
\]
Equivalently, compute the intersection of the finite delta-family with the one-step inflation kernel using the natural degree-4 pairing.

Classification:
- W45=Q4: PASS / CLOSED
- Q4 isomorphic to P4/P5: PASS / CLOSED at rank 4, p=3 Demuškin scope
- D2 one-step kernel isomorphic to Q4*: PASS / CLOSED
- delta-family/kernel intersection: OPEN / LOAD-BEARING
- m=1 full D2 separation: OPEN / LOAD-BEARING
- Paper 1 orientation-carrier route: HISTORICAL / SUPERSEDED

Detailed record: research/PAPER1_PAPER3_Q4_P4P5_BRIDGE_AUDIT_2026-09-28.md.

This branch is a side investigation supporting D2 repair; it is not promoted to the principal Paper 3 theorem until the delta/kernel intersection is independently computed.

## 2026-09-28 — CRITICAL REFINEMENT OF THE PAPER 1 ↔ PAPER 3 BRIDGE

The proposed direct calculation of the finite delta-family intersect Q4* was critically audited and found to be ill-typed. The delta-family is a family of maps into H^2, while Q4* is identified via transgression with a subspace of the finite H^2(W4) target. The correct object-level test is therefore delta_{3,rho3}(f) in tra(Q4*) for individual outputs, not a subspace intersection of the whole family.

A stronger consequence follows from the already-proved global variation formula: for rho3'=rho3(1+9nu), nu nonzero, cup nondegeneracy gives an f with nonzero variation in H^2(G,F3). Any class in the one-step finite kernel maps to zero in H^2(G). Hence the separating global variation output cannot lie in that kernel.

This yields PASS / LOCAL for the existence of a globally separating output outside the one-step kernel, conditional on the missing finite representative/factorization compatibility. It does not yet prove m=1 full selector.

The Paper 1 10-25-10 decomposition can be reused only through the dual Q4* representation after an explicit dual-module audit. It is not itself a decomposition of the delta-family.

Classification:
- literal delta-family intersect Q4*: INVALID / CLOSED — type mismatch;
- output-level transgression-kernel test: OPEN / LOAD-BEARING;
- globally separating false-lift output outside one-step kernel: PASS / LOCAL conditional on finite compatibility;
- Paper 1 10-25-10 dual reuse: OPEN / AUTHORIZED SIDE COMPUTATION;
- m=1 full D2 selector: OPEN / LOAD-BEARING.

Detailed record: research/PAPER1_PAPER3_Q4_P4P5_BRIDGE_AUDIT_2026-09-28.md.


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


## 2026-09-28 — GATE D GENERALIZATION CLOSED AFTER CORRECTED D2

Gate D has been re-derived from the failure of the bare-Q_k H^2 inflation argument rather than patched by assumption.

Scope: torsion-free Demuškin pro-p groups, odd p, even rank d>=2, q in {0,p,p^2,...}, every k>=2.

Core corrected construction:
Q_k=G/D_{p^{k-1}+1}, E_k=G/D_{p^{k-1}+2}, K_k=D_{p^{k-1}+1}/D_{p^{k-1}+2},
O_k=H^2(Q_k,F_p)/im(tra_k).

D1: uniform odd-p affine semidirect filtration gives factorization of every candidate crossed cocycle through Q_k.
D2 canonical branch: global Kummerian lift factors through Q_k, so finite delta is zero directly; no finite-to-global H^2 injectivity is used.
D2 false branch: for rho_k'=chi_k(1+p^{k-1}nu), nu!=0, PD^2 cup nondegeneracy plus canonical lower-level Kummerianity gives f with nonzero global variation. The finite representative cannot be transgression because transgression classes die in E_k while the witness has nonzero global inflation. Thus O_k detects every false first-order lift.
D3: induction gives finite selector uniqueness at every k.
D4: LTE witness gives exact declared selector threshold p^{k-1}+1.

Important non-circularity: arbitrary-candidate Kummer surjectivity is never assumed; only canonical lower-level reduction-surjectivity is used.

Classification:
- Gate D: PASS/CLOSED.
- D1: PASS/CLOSED.
- corrected D2 carrier and separation: PASS/CLOSED.
- D3 all-k selector: PASS/CLOSED.
- D4 threshold: PASS/CLOSED.
- uniform-in-q within the declared torsion-free Demuškin family: PASS/CLOSED.
- arbitrary pro-p generalization: NOT CLAIMED.
- carrier minimality: OPEN.
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


## 2026-09-28 — PAPER 3 MIDPOINT CHECKPOINT

Continuity checkpoint recorded in `research/PAPER3_MIDPOINT_SUMMARY_2026-09-28.md`.

Master status: D1 PASS/CLOSED; corrected D2 PASS/CLOSED; D3 PASS/CLOSED; D4 affine sharpness PASS/CLOSED; bare finite H^2 inflation injectivity FAIL/CLOSED; global one-dimensional detector PASS/CLOSED at the existential-per-false-candidate level; finite-pair intrinsic one-dimensional detector OPEN/LOAD-BEARING; carrier minimality OPEN; 45-dimensional calculation DEFERRED; publication novelty OPEN/CONDITIONAL.

Next attack: abstract reconstruction from the finite central extension E_k -> Q_k, asking whether extension-class/transgression data canonically supplies a nonzero functional on the D2 witness family or forces retention of additional filtered data.


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


## 2026-09-28 — PAPER 3 REFEREE GAP CLOSURE

The authorized referee attack was completed on the load-bearing free-product twisted-H1 step.

Result:
- PASS / CLOSED: candidate-dependent module transport and the commutative coefficient-reduction diagram;
- PASS / CLOSED: N cap G_i=P_n(G_i) via functoriality plus retraction;
- PASS / CLOSED: finite twisted-H1 reduction to factorwise Kummer predicates using Paper 2 arbitrary-candidate factorization;
- PASS / CLOSED: explicit universal-property proof for truncation preserving the free pro-p coproduct after reflection;
- PASS / CLOSED: selected-depth abelianization calculation for the f<k parameter witness;
- PASS / CLOSED: rank-four q=3 recognition scope separated from the broader heterogeneous affine family.

The corresponding manuscript repair is commit f97b9f04dd873fd2d0123d325443032c4840d086.

The strongest previous referee objection is therefore closed. Publication novelty remains OPEN / CONDITIONAL and the Paper 3 application manuscript remains distinct from the theorem-paper track.

Detailed record: research/PAPER3_REFEREE_GAP_CLOSURE_2026-09-28.md.


## 2026-09-28 — FINAL D1/D2 SOURCE AUDIT

The final line-by-line attack found and corrected two stale formulas in general Gate D documentation.

1. The Zassenhaus target filtration uses the logarithmic index ceil(log_p n), not a step-by-one index j. The endpoint required for factorization is unchanged.
2. The D2 transgression-carrier variation identity is typed in H^2(G,F_p), so it is delta_{rho'}-delta_{chi}=nu cup f-bar; the auxiliary iota formulation is not part of that statement.

Classification: D1 endpoint/factorization PASS / CLOSED after correction; D2 variation target typing PASS / CLOSED after correction; stale historical formulas HISTORICAL / SUPERSEDED.

No new selector counterexample was found. The authorized D1/D2 attack is now closed; remaining work is compilation and final manuscript/novelty positioning.


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


## 2026-09-28 — PAPER/RESEARCH SYNCHRONIZATION FAILURE AUDIT + CORRECTIVE GATE

A manuscript synchronization failure was identified after the uploaded `Paper3_FINAL_2026-09-28.pdf` was found to predate the authoritative D2/D3/D4 frontier. The research records had already recorded the newer results, but the publication source/PDF was not automatically required to consume every load-bearing CLOSED result.

Root cause: the existing continuity protocol enforced **research-result logging**, but did not enforce a separate **research → manuscript synchronization gate**. Thus the research state and publication artifact could diverge while each appeared internally consistent.

Classification:
- Research results D2/D3/D4: **PASS/CLOSED** as recorded in the authoritative research state.
- Previous uploaded Paper 3 PDF as a representation of the latest frontier: **FAIL/CLOSED**.
- Current manuscript synchronization: **OPEN / LOAD-BEARING** until clean CI and artifact verification pass.
- Final PDF status: **NOT FINAL** until source, CI PDF, and research-state manifest are cross-verified.

Mandatory corrective process from this point:
1. Every load-bearing PASS/CLOSED result must declare whether it changes the manuscript; if yes, record the exact source path/section that must change.
2. Maintain a Paper 3 manuscript manifest mapping each load-bearing result (D1, D2, D3, D4, selector minimality, cup carrier, novelty boundary) to its manuscript section and status.
3. A paper cannot be labelled FINAL merely because research is PASS/CLOSED. FINAL requires: authoritative-source recheck → manuscript synchronization → independent CI compile → PDF content verification → artifact hash/commit capture → immediate log entry.
4. The dated PDF filename is no longer authoritative by itself; the authoritative identity is the CI commit SHA plus the generated artifact checksum.
5. CI must test both positive markers (all required final results present) and negative stale markers (e.g. 'minimality remains open') before artifact publication.

This audit supersedes the prior assumption that recording a result was sufficient to guarantee manuscript synchronization.

## 2026-09-28 — PAPER 1/2 RE-AUDIT + PAPER 3 CURRENT-SOURCE ARTIFACT CLOSURE

Paper 1 and Paper 2 were rechecked against their authoritative manuscript branches and current research boundaries. Paper 1 remains the fixed rank-4, q=3 finite-window Kummer recognition theorem with classical orientation prior art and no minimality claim. Paper 2 remains the sharp affine factorization theorem with (n_{\mathrm{aff}}(k)=p^{k-1}+1), rank-two sharpness, finite free-product applications, and explicitly bounded claims. Both are **PASS / CLOSED** at their declared manuscript scopes; publication novelty remains conditional.

Paper 3's prior final PDF was found to predate the final source repair. The current source was therefore rebuilt from the exact current main branch and independently audited.

- Main commit: `22f821acdbee5a68513272c70056b7f97a559df5`.
- Source blob: `599b5d2b19f3e256ab25535a6aebc1beea907fa2`.
- Source SHA-256: `b0fef874507e4f2eef249296d5aca83000a954b0c15c2bf0abfc69664de7b0ac`.
- CI run **36367519607**: **PASS / CLOSED**.
- PDF artifact **10947718917**: 16 pages, 412,490 bytes, SHA-256 `2907598169954f6388d764d3596cbe0fad680165c6397a99fcd67efd669b4a6e`.
- Full artifact **10948425435**: SHA-256 digest `eb11307dcfd02ade4576328d882b713c498cd8a96950667c0d3fd75f3430af1e`.
- Independent PDF extraction/content audit: **PASS / CLOSED**.
- Internal full-package SHA256SUMS verification: **PASS**.

Process correction: a prior passing PDF is never authoritative after the source changes. Finality requires exact source identity, CI on that exact source, independent PDF audit, checksum, and manifest.

Classification: Paper 3 manuscript artifact **PASS / CLOSED**; mathematical publication novelty remains **OPEN / CONDITIONAL**; stronger finite-pair canonical functional remains **OPEN / NOT LOAD-BEARING**.


## 2026-09-28 — THREE-PAPER PDF REVIEW AUDIT / VERSION-MAPPING CORRECTION

An external review of Paper 1/2/3 was checked against the exact PDFs delivered in the current session and the exact source commits that built them.

Key result:
- The alleged Paper 2 page-3 print corruption is not present in the delivered artifact. Page 3 was independently text-extracted and visually rendered; it contains normal Lemma 2.1/Lemma 2.2 material. Classification: **FAIL/CLOSED as a review objection**. No rebuild is authorized unless a different PDF is identified by filename/hash.
- The Paper 1 objections appear to target a different/older manuscript mapping. The delivered Paper 1 is the affine factorization paper and already uses p,f,k, includes the preceding-paper relation, and cites Efrat 2014. Classification: **PASS/CLOSED** at declared scope.
- The Paper 3 x3->x2 objection is already absent from the current source; x_2^{3^e} is present. The C_k/iota/inflation typing is already explicit; F_1 algebra is explicitly simplified; the commutator formula is mathematically consistent. Classification: **PASS/CLOSED** at declared scope.
- Labute Theorem 4 attribution remains verified from the earlier primary-source audit.

Artifact bindings:
Paper 1 = run 36212215849 / commit 73001ba0611e4f4aa7db8c733ee01d67542e16eb / SHA 09d67cbb88c647e4b7bb92bb91b2d46fe6b9b2c4b32959b7cebd7e468a554eda.
Paper 2 = run 36216012111 / commit 0194e01176ae1c21fc70858be3797eeb1a3e7c18 / SHA af14b4b7ab971d8ed2d8cac84daae3ff6422ed389cec92b690cc3e184dde1aee.
Paper 3 = run 36368630643 / commit 2b4ccb849e93af840ca216b06c06c72a36c84dd8 / SHA 00a4ee8deba65eb7c08a9b703d3c19b50801ffdde2c13cab0155186c247bb4e3.

Detailed audit: research/THREE_PAPER_PDF_REVIEW_AUDIT_2026-09-28.md.

Decision: **No mathematical branch reopened; no PDF rebuild triggered by this review alone.**


## 2026-09-28 — PAPER 3 REFEREE DETAIL REPAIR 2 / SOURCE SYNCHRONIZATION

The current authoritative `paper/main.tex` was repaired directly from the repository source after the referee-level review. The repair commit is `2ab97e7d11f5238f6586aa435c9da36d62781d91` (source blob `ce6ef7277b34b8e4e600ec6ab3b42862a551a903`).

Applied source changes:
- §6 auxiliary kernel renamed from (K_k) to (J_k), preserving (mathsf K_k) for the Kummer predicate;
- the auxiliary (mathcal O_k) transgression quotient/proof-carrier discussion removed; (C_k) is the explicit carrier used in the manuscript;
- §9 now defines the depth-(m) selector (mathsf K_{k,m}(W_m,ho)) on the actual factor-through domain (mathscr D_{k,m}), and explicitly states that (chi_Gmod3^k) is outside this domain for (mle3^{k-2});
- the convention (chi_G(x_2)=(1-3)^{-1}) is fixed explicitly;
- Lemma 5.3/U5c now states the dualizing-module action, Pontryagin-dual convention, and (PD^2)-naturality of the dual coefficient map;
- the U3 divisibility induction is explicitly described as simultaneous in all Fox coefficients;
- the carrier wording is now “a minimal linear carrier in the declared selector-carrier category”.

Source-level recheck after write: old (K_k) kernel notation absent, (mathcal O_k) absent, selector-domain definition present, convention/naturality wording present.

Classification:
- manuscript source repair: PASS / CLOSED;
- publication artifact gate: OPEN / PENDING exact CI + independent PDF audit;
- mathematical frontier classifications: unchanged;
- publication novelty: OPEN / CONDITIONAL.

The exact source commit has triggered Build paper PDF run 36373920812; no final artifact is declared until that run and the independent PDF/package audit pass.


## 2026-09-28 — PAPER 3 EXACT-SOURCE ARTIFACT GATE CLOSED

The referee-detail repair source was compiled and independently audited.

- Exact manuscript source commit used by CI: `ac53cc2e753fc7b8fb0eb4b78a0085ccfdbc5a89`.
- Source blob SHA: `3f0bc48ac532d0ed72bcfe876a8283bed178dfbc`.
- Source SHA-256: `bc951dce61717ed184e8763118a3ffef310615b09b95b8fd6ae7ca0a83e42a49`.
- Build paper PDF run **36374270475**: **PASS / CLOSED**.
- PDF artifact **10950077812**; PDF SHA-256 `d38c63bd1b453482217c7876d818ff7b50e48cbde7f219552953d8a5e36d56c0`; 17 pages.
- Full artifact **10950097816**; internal SHA256SUMS verified.
- Independent PDF text and visual audit: **PASS / CLOSED**.

A transient LaTeX failure in run 36373920812 was caused solely by the undefined `\\mathscr` selector-domain macro; it was corrected to `\\mathcal`. The subsequent exact-source build passed. The accidental predicate-renaming audit was also corrected before the final successful build; the final PDF consistently uses `\\mathsf K_k` for the Kummer predicate and (J_k) for the auxiliary kernel.

Final classification:
- manuscript artifact: **PASS / CLOSED**;
- mathematical theorem scope: **PASS / CLOSED**;
- selector threshold: **PASS / CLOSED** at fixed rank-4 (q=3) scope;
- 1D cup-line carrier/minimality: **PASS / CLOSED** in the declared linear selector-carrier category;
- stronger canonical finite-pair functional: **OPEN / NOT LOAD-BEARING**;
- publication novelty: **OPEN / CONDITIONAL**.


## 2026-09-28 — META-REFLECTION: WHY THE THREE-PAPER RESULT IS BOTH LUCKY AND RESEARCH-DRIVEN

This entry records a meta-level reflection from the research process itself, rather than a new mathematical theorem.

The project began as a small curiosity-driven experiment. The eventual outcome exceeded the original expectation by a large margin: after repeated computational dead ends, FAIL states, route changes, scope corrections, and attacks on apparently promising arguments, the work nevertheless produced three connected mathematical papers with meaningful results.

The researcher's own role should be recorded as nontrivial even though the AI performed substantial calculations and drafting. In particular, repeated human judgments about whether to continue a calculation, abandon a route, weaken a claim, reformulate a question, or demand an independent verification materially shaped the trajectory. The process repeatedly moved from:
- calculation overload / "what are we even trying to find?" states,
- to explicit FAIL or CLOSED results,
- to a reframed question,
- to a small structural observation,
- to a theorem-level result.

Several such "unexpectedly good result" moments occurred, rather than only one final lucky breakthrough. This is a useful description of the actual research experience: the project could plausibly have ended without any of these moments, yet multiple rounds of failure and reframing produced mutually connected results.

A fair interpretation is therefore:
**substantial effort + research judgment + favorable mathematical structure + good fortune.**
The result should not be described as luck alone. The fortunate openings were repeatedly converted into durable mathematics only through verification, scope restriction, failed-route closure, and reformulation.

### How the original question was partially answered

The original broad question was approximately:

> Can the canonical orientation chi:G -> Z_3^× be recovered intrinsically from finite filtered/graded information, and how much such information is necessary and sufficient?

The three papers do not constitute a complete answer to every possible formulation of that question, and no absolute minimality over all conceivable encodings is claimed. However, their results form a connected partial answer rather than three unrelated pieces.

- **Paper 1 — recognizability:** establishes a finite-window recognition mechanism in the declared rank-4/q=3 Kummer setting. It addresses the "can it be recognized from finite information?" part.
- **Paper 2 — information depth:** determines the sharp factorization depth p^{k-1}+1 in the declared affine crossed-cocycle category. It addresses "how deep must the finite window be for the relevant affine information to survive?"
- **Paper 3 — recognition at the sharp window:** uses the finite quotient at the relevant depth and an intrinsic Kummer/cup-product selector to isolate the canonical orientation in the declared scope. It addresses "does the retained finite information actually suffice to select the canonical candidate?"

Thus the combined architecture is:

  recognizability
       ↓
  information threshold
       ↓
  recognition at the threshold

or, in question form:

  Can we find it?
       ↓
  How much information do we need?
       ↓
  Is that amount actually enough to find it?

The strongest accurate characterization is therefore not "the original question has been completely solved", but:

> The project constructs a substantial, internally connected partial answer to the original question: it shows finite intrinsic recognition in a declared setting, identifies a sharp depth for the relevant affine information, and realizes recognition at that depth via a finite Kummer/cup-product mechanism.

The sharpness and minimality statements remain category-relative:
- Paper 2 sharpness is within the declared affine crossed-cocycle class.
- Paper 3 selector minimality is within the declared linear selector-carrier category.
- Absolute minimality over arbitrary nonlinear finite encodings is not claimed.

This distinction is part of the mathematical contribution and should be preserved in future summaries.

