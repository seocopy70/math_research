## 2026-09-25 — POST-ASSEMBLY U1/U5c TIGHTENING

The latest manuscript pass found no new mathematical failure. Two referee-level gaps were tightened in `paper/main.tex`:

- **U1:** the exact power valuation behind (S_k^{3^j}=3^jA_ktimes U_{j+1}) is now written explicitly, including pure translations, (3)-adic unit powering, and the commutator generator ( [4,a]=3a).
- **U5c:** the finite-coefficient PD² duality statement is now explicitly anchored to Wilkes (2020), §1, while retaining the manuscript's explicit dual-map calculation showing that the dual of the socle inclusion is reduction (A_{k-1}	woheadrightarrowmathbf F_3).

Latest manuscript commit: `962be77ed62040ed5707e3c59c54de6585a0086d`.

**Exact-build gate:** a clean local PDF build of this exact post-tightening commit has not yet been independently executed. The earlier 8-page three-pass build belongs to the preceding corrected commit. Therefore the build gate remains OPEN until the exact commit is compiled.

Current status:
- U1: **PASS / CLOSED**
- U2: **PASS / CLOSED**
- U3: **PASS / CLOSED**
- U4: **PASS / CLOSED**
- U5a/U5b/U5c: **PASS / CLOSED**
- theorem assembly: **PASS / PROVISIONAL**
- Zassenhaus window minimality: **OPEN**
- exact publication novelty: **OPEN / CONDITIONAL**

## 2026-09-25 — CRITICAL ZASSENHAUS WINDOW CORRECTION + MANUSCRIPT RE-AUDIT

A second end-to-end audit found and corrected a substantive filtration error in the
publication manuscript.

The manuscript had called \(P_i\) the Zassenhaus filtration but had defined
\(P_{j+1}=P_j^3[P_j,G]\), which is the lower \(3\)-central filtration. Those
filtrations are not equal beyond the first steps. Therefore the previous
factorization claim through \(G/P_{k+1}\) was not valid for the actual Zassenhaus
filtration.

For the finite semidirect target
\[
S_k=A_k\rtimes U_1,\qquad A_k=\mathbf Z/3^k,\quad U_j=1+3^jA_k,
\]
the corrected calculation is
\[
P_n(S_k)=3^{e(n)}A_k\rtimes U_{e(n)+1},
\qquad e(n)=\lceil\log_3 n\rceil,\ e(1)=0.
\]
Hence
\[
P_{3^{k-1}}(S_k)=3^{k-1}A_k\ne1,\qquad
P_{3^{k-1}+1}(S_k)=1.
\]
Thus the actual Zassenhaus finite window is
\[
\boxed{Q_k=G/P_{3^{k-1}+1}},
\]
not \(G/P_{k+1}\). U2 has been corrected accordingly.

This is a genuine mathematical correction. The theorem's recognition mechanism
survives, but the finite window is larger than previously claimed. Minimality of
this corrected window remains OPEN.

Current manuscript status:
- U1 lower-3-central formulation: FAIL/CLOSED (superseded)
- U1 corrected Zassenhaus formulation: PASS/CLOSED
- U2 arbitrary-candidate factorization through corrected \(Q_k\): PASS/CLOSED
- U3 finite Kummer/Fox criterion: PASS/CLOSED
- U4 mod-9 base selector: PASS/CLOSED after explicit Fox calculation
- U5a: PASS/CLOSED
- U5b: PASS/CLOSED after cochain-level expansion
- U5c: PASS/CLOSED after explicit dual-map naturality check
- Main finite-window theorem with corrected \(Q_k\): PASS at the current proof level
- Minimality of the Zassenhaus window: OPEN
- Publication novelty: OPEN / CONDITIONAL

Corrected manuscript commit:
26d0180dbf1aece68acf14277da5baa0cf2aed1c

A three-pass local pdflatex build of the corrected manuscript state completed with
status 0 and produced an 8-page PDF.

## 2026-09-25 — PAPER U1–U5 PROOF AUDIT STARTED

The actual `paper/main.tex` has now been audited against the authoritative U1–U5 research records. The underlying research theorem remains PASS/CLOSED, but the manuscript proof is not yet submission-ready.

Findings:
- U1: research PASS/CLOSED; manuscript underproved because the semidirect filtration induction is only asserted.
- U2: mathematically sound, but the canonical H^1 inflation isomorphism should be stated/proved explicitly.
- U3: OPEN/LOAD-BEARING in manuscript. The current generic one-relator statement is too broad unless minimality is assumed, and the corrected iterative proof is omitted.
- U4: PASS/LOCAL. The manuscript asserts the standard coordinate calculation without showing it; only the k=2 base case is needed for the intrinsic induction.
- U5: OPEN/LOAD-BEARING in manuscript. The variation identity, exact coefficient maps, PD² duality convention, induction reduction, and existence-on-Q_k bridge must be written out.
- The theorem assembly is logically coherent once these lemmas are supplied.

Authoritative audit: `research/PAPER_U1_U5_PROOF_AUDIT_2026-09-25.md`.

No closed research branch was reopened. No new Fox computation was performed.

## 2026-09-25 — PROP. 2.10 PRIOR-ART SEPARATION AUDIT


The negative result for N=P_3 was compared against the primary Proposition 2.10 source and the Zassenhaus-dimension literature. Quadrelli (2024) Proposition 2.10 requires restriction-surjectivity as an explicit hypothesis and uses the dual injection N/N^3[G,N] -> G/Phi(G). For the rank-4 p=3 Demushkin group, P_3 subset Phi(G), while dim_F3(P_3/P_4)=20 and P_3^3[P_3,G] subset P_4. Therefore restriction H^1(G,F_3) -> H^1(P_3,F_3)^G is not surjective.

The exact composite negative statement was not found in the audited literature. Its ingredients are known, so it is not claimed as an independent new theorem. It is recorded as a PASS / CONDITIONAL prior-art separation lemma: Proposition 2.10 cannot automatically collapse the finite-window theorem through N=P_3. Direct Prop. 2.10 collapse route: FAIL / CLOSED. Exact publication novelty of the main finite-window theorem remains OPEN / CONDITIONAL.

Record: research/PROP_2_10_PRIOR_ART_AUDIT_2026-09-25.md.

## 2026-09-24 — U5 INTRINSIC UNIQUENESS CLOSED / FINITE-WINDOW THEOREM ESTABLISHED

The load-bearing U5 gate is now closed at theorem level.

1. **Variation lemma — PASS/CLOSED.** For two level-\(k\) characters reducing to the same \(\rho_{k-1}\), with \(\rho_k'=\rho_k(1+3^{k-1}\nu)\), coefficient-extension/Yoneda naturality gives
\[
\delta_{\rho_k'}-\delta_{\rho_k}
=
\iota_{k-1}\circ(\nu\smile-).
\]
This is intrinsic and presentation/Fox/\(q\) independent.

2. **PD² socle-injectivity lemma — PASS/CLOSED.** On the induction branch \(\rho_{k-1}=\chi\bmod3^{k-1}\), the socle inclusion \(\mathbf F_3\hookrightarrow\mathbf Z/3^{k-1}(\chi_{k-1})\) induces an injection on \(H^2\). PD² duality reduces this to surjectivity of reduction on invariant sections of the untwisted dual coefficient module.

3. **U5 uniqueness — PASS/CLOSED.** If two candidates satisfy the global finite Kummer predicate, their connecting maps vanish. The two lemmas imply \(\nu\smile v=0\) for every \(v\in H^1(G,\mathbf F_3)\); Demuškin cup nondegeneracy gives \(\nu=0\). Induction starts from the established \(k=2\) selector.

4. **Finite-window theorem — PASS/CLOSED.** U1-U2 already prove that the twisted finite lifting problem factors through \(Q_k=G/P_{k+1}\). Existence is supplied by the known canonical Kummerian orientation. Therefore, for every \(k\ge2\),
\[
\boxed{\mathsf K_k(Q_k,\rho)\Longleftrightarrow \rho=\chi_G\bmod3^k.}
\]

Current classification:
- U1: **PASS/CLOSED**
- U2: **PASS/CLOSED**
- U3: **PASS/CLOSED**
- U4: **PASS/LOCAL** (standard-presentation coordinate check only)
- U5: **PASS/CLOSED**
- N3 full-group uniqueness as novelty: **HISTORICAL/SUPERSEDED**
- N4 finite \(G/P_{k+1}\) factorization: **PASS/CLOSED**
- N5 q-blind finite selector: **PASS/CLOSED**
- Uniform B2 mathematical theorem: **PASS/CLOSED**
- Overall novelty: **OPEN / CONDITIONAL**

Important boundary: this does **not** claim that canonical Demuškin orientation is new. Existence/uniqueness of the full-group Kummerian orientation is known. The only remaining publication gate is whether the exact bare-\(Q_k\), q-blind finite-selector/factorization formulation is already an immediate corollary or equivalent reformulation of existing quotient/inheritance results.

No new Fox computation was used or authorized.

Record: \`research/U5_INTRINSIC_FINITE_SELECTOR_AUDIT_2026-09-24.md\`.

## 2026-09-24 — U5 / N3–N5 LITERATURE GATE CLOSED

The targeted literature audit is now sharper. N3 (full-group finite-coefficient uniqueness) is **HISTORICAL / SUPERSEDED** as a novelty source: Labute Proposition 6/Theorem 4 already gives the all-level crossed-derivation criterion and unique Demushkin orientation, and Quadrelli (2024) Lemma 2.9 restates the finite-level generator-value lifting formulation. N4 (exact factorization through Q_k=G/P_{k+1}) remains **OPEN / LOAD-BEARING**. The modern quotient-inheritance result requires an already Kummerian orientation and an extra restriction-surjectivity hypothesis; it does not state the present finite candidate-selector theorem. N5 (q-blind, functorial finite selector on bare Q_k) remains **OPEN / DECISIVE**; no audited source states this exact theorem.

Recent checks of Blumer–Quadrelli (arXiv:2603.15464v2) and Pál–Quick (2026) found no exact finite Q_k selector result. Therefore the efficient next step is the intrinsic U5 proof, with finite-window factorization/recognition kept separate from the already-known full-group canonical orientation theorem. No new Fox computation is authorized.

Active state:
- U1 PASS/CLOSED
- U2 PASS/CLOSED
- U3 PASS/CLOSED
- U4 PASS/LOCAL
- U5 OPEN/LOAD-BEARING
- N3 HISTORICAL/SUPERSEDED
- N4 OPEN/LOAD-BEARING
- N5 OPEN/DECISIVE
- Uniform B2 OPEN/DECISIVE
- Novelty OPEN/CONDITIONAL

Record: research/U5_INTRINSIC_FINITE_SELECTOR_AUDIT_2026-09-24.md.

## 2026-09-24 — U5 PRE-CHECK COMPLETE / U5 OPEN

The intrinsic finite predicate is fixed as
\[
\mathsf K_k(Q_k,\rho):H^1(Q_k,\mathbf Z/3^k(\rho))\to H^1(Q_k,\mathbf F_3)\text{ surjective},
\quad Q_k=G/P_{k+1}.
\]
Object, functoriality, predicate-level gauge independence, and definitional q-blindness are **PASS/CLOSED**. The bridge to Fox coordinates is available through U1-U3, but the all-k uniqueness proof remains presentation-local.

Targeted literature comparison confirms that the known Kummerian/cyclotomic results characterize the full oriented pair and the canonical Demushkin orientation. A quotient-inheritance proposition requires an already Kummerian orientation plus an additional restriction-surjectivity hypothesis; it does not automatically imply the present finite candidate-selector for (P_{k+1}). Thus the exact bare-(Q_k) theorem remains unresolved in the audited corpus.

**Active state:**
- U1: **PASS/CLOSED**
- U2: **PASS/CLOSED**
- U3: **PASS/CLOSED** (valuation-induction proof; prior Nakayama wording superseded)
- U4: **PASS/LOCAL** (corrected inverse coefficient; standard presentation)
- U5: **OPEN/LOAD-BEARING**
- Uniform B2: **OPEN/DECISIVE**
- Novelty: **OPEN/DECISIVE**

Next authorized attack: prove/disprove intrinsic uniform uniqueness of (mathsf K_k) from Demushkin structure without inserting q or a presentation, or identify a literature theorem that directly implies it. No new Fox computation and no (t_2) revival before that gate.

Record: research/U5_INTRINSIC_FINITE_SELECTOR_AUDIT_2026-09-24.md.

## 2026-09-24 — U1–U4 CRITICAL AUDIT / U5 ACTIVE

The uniform finite-depth program has been critically audited. U1 is **PASS/CLOSED** by the independent semidirect-product proof (P_j(A_k\rtimes U_1)=3^{j-1}A_k\rtimes U_j), giving (P_{k+1}=1). U2 is **PASS/CLOSED**: every crossed cocycle factors through (Q_k=G/P_{k+1}), yielding the canonical (H^1) identification.

U3 remains **PASS/CLOSED**, but the proof has been corrected: basis-vector lifting yields (F_i\in3A_k), and repeated lifting/valuation induction yields (F_i\in3^mA_k) for every (m), hence (F_i=0). The previously written (I\subset3I\) Nakayama argument is **HISTORICAL/SUPERSEDED**. The mod-3 (H^1) generator-value hypothesis must be explicit.

U4 remains **PASS/LOCAL** for the standard presentation, but the earlier all-k (4-r_{k-1}) recurrence is **FAIL/CLOSED**. The correct coefficient is (2+\rho_k(x_2)^{-1}); its inverse expansion recovers the next digit on the canonical branch. This does not establish presentation-free uniqueness.

Therefore the active load-bearing gate is
\[
\boxed{U5=\text{intrinsic, presentation-free, q-blind finite selector}}
\]
with Object/Input/Functoriality/Gauge/Orientation-bridge/Separation/Novelty/Stop audit required before further computation.

Current classification:
- U1: **PASS/CLOSED**
- U2: **PASS/CLOSED**
- U3: **PASS/CLOSED** (corrected proof)
- U4: **PASS/LOCAL**
- U5: **OPEN/LOAD-BEARING**
- Uniform B2: **OPEN/DECISIVE**
- No (t_2) route is revived.

Next authorized gate: define the intrinsic finite predicate on ((Q_k,\rho)), prove its naturality, and compare its finite-coefficient quotient inheritance line-by-line with the audited Kummerian/cyclotomic literature.\n\n## 2026-09-24 — B2 / k=4 CLOSED LOCALLY

After critical correction of the k=3 record, the authorized k=4 finite-window gate was executed for the standard rank-four (q=3) Demushkin group. The mod-81 obstruction is
\[
27((1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4),
\]
so the unique compatible candidate is \((1,40,1,1)\pmod{81}\). Independent enumeration of all 81 lifts confirms uniqueness. Direct valuation gives
\[
z(P_2)\subset3A_4,quad z(P_3)\subset9A_4,quad z(P_4)\subset27A_4,quad z(P_5)=0,
\]
hence the lift factors through (Q_4=G/P_5).

Classification: k=4 exact obstruction PASS/CLOSED for the standard family; k=4 uniqueness PASS/LOCAL; (P_5)-annihilation PASS/LOCAL; (Q_4)-factorization PASS/LOCAL. The selector is still presentation-based/local, not yet intrinsic or q-uniform. Uniform B2 remains OPEN/DECISIVE. The next authorized gate is the uniform finite-depth lemma for (A_k=\mathbf Z/3^k), (Q_k=G/P_{k+1}), followed by a literature comparison. No (t_2) route is revived.

Record: research/KUMMER_B2_K4_FINITE_WINDOW_MOD81_2026-09-24.md.


## 2026-09-24 — B2 / k=3 CLOSED LOCALLY

The mod-27 finite-window gate for the standard rank-four q=3 Demushkin group is closed locally. The unique mod-27 candidate reducing to the k=2 solution is (1,13,1,1). The exact relation obstruction is 9(-a2 f1+a1 f2-a4 f3+a3 f4), giving a unique universal-zero lift. Direct valuation gives z(P2)⊂3A3, z(P3)⊂9A3, and z(P4)=0, so all lifts factor through Q3=G/P4. Therefore B2/k=3 is PASS/LOCAL. Uniform B2 is still OPEN/DECISIVE; next authorized gate k=4.

## 2026-09-24 — N1 LITERATURE GATE CLOSED

The four primary references now form the audited literature baseline. The full-group Kummerian/cyclotomic characterization and uniqueness of the Demushkin orientation are known; this part is not the proposed new theorem. The remaining novelty boundary is finite filtered reconstruction: a q-blind natural predicate on Q_k=G/P_{k+1} together with factorization/annihilation of the relevant lift through Q_k. N1 literature boundary: PASS / CLOSED. B2/k=2: PASS / LOCAL. Uniform B2: OPEN / DECISIVE. Next authorized gate: k=3, Q_3=G/P_4, first prove P_4-annihilation of the mod-27 Kummer lift. See research/N1_LITERATURE_GATE_KUMMERIAN_CYCLOTOMIC_DEMUSHKIN_2026-09-24.md.


## 2026-09-21 — B2 K=2 FINITE WINDOW CLOSED LOCALLY

The first finite-window B2 test is complete at Q_2=G/P_3. The predicate “all H^1(Q_2,F_3) classes lift to H^1(Q_2,Z/9(rho))” is q-blind and natural as a predicate of (Q_2,rho). For the standard rank-four Demuškin setting, existence is verified at the quotient level by showing the mod-9 Kummer lift annihilates P_3; uniqueness gives rho=(1,4,1,1). **PASS / LOCAL.**

This does not solve uniform B2. The decisive next gate is k=3, Q_3=G/P_4: prove that the mod-27 Kummer lift annihilates P_4. No all-k induction or classification repackaging is authorized before that gate.

Record: research/KUMMER_B2_K2_FINITE_WINDOW_MOD9_2026-09-21.md.
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
- E_{>P_4} factorization/vanishing: **OPEN / LOAD-BEARING**;- HA61-B overall: **OPEN / LOAD-BEARING**;
- HA61-C: **not opened**.

## Immediate next attack

Keep the exact intrinsic delta_3 fixed. Perform the source-complete mod-27 / division-by-9 ledger for the P_4 generators, retaining prefix/suffix terms together with the relation-jet terms. The decisive question is whether the surviving functional on the primary-zero domain has rank one and is represented by a natural filtered datum. A failure closes B negatively; a proof opens the final bridge toward C.

Record: `research/HA61_B5_10_INTRINSIC_SECONDARY_FAMILY_AND_CONJUGATION_2026-09-20.md`.


## 2026-09-20 — HA61-B5-3: COMBINED AFFINE SECONDARY QUOTIENT

B5-2 was sharpened to an explicit affine action. On the primary-zero locus, the gauge shift (t_2mapsto t_2+a p) is exactly compensated by (mumapstomu+alambda), because (f(p)=-(lambdawedge f)(R)). Thus the natural secondary object is the quotient/torsor ([(t_2,mu)]in(V^{(2)}oplus V^*)/mathbf F_3(p,lambda)) when (lambda
e0); for (lambda=0) this affine ambiguity disappears.

Decision: combined affine action PASS / LOCAL; raw (t_2) intrinsicity FAIL / CLOSED; no independent cubic-bracket functional PASS / LOCAL; universal affine carrier OPEN / LOAD-BEARING; deeper-than-(P_4) factorization OPEN / LOAD-BEARING; HA61-B OPEN / LOAD-BEARING; HA61-C not opened.

Record: research/HARD_ATTACK_61_B5_3_COMBINED_AFFINE_SECONDARY_QUOTIENT_2026-09-20.md.

## 2026-09-20 — HA61-B5-1/B5-2: CORRECT SECONDARY WINDOW; AFFINE t_2 OBSTRUCTION

B5 source audit corrected the proposed D_4/D_5 quotient. It is not a valid secondary quotient because g^9 lies in D_9 subset D_5 but evaluates nontrivially after /9. The relevant mod-27 finite-information threshold is G/P_4, corresponding to the D_10 information window already established for the standard family.

The new P_3/P_4 power residual gives the genuine ninth-power functional. The gamma_2^3 sector reproduces the old lambda wedge f contribution. A cubic bracket gauge change P -> P+[v,R] gives
T([v,R])=-lambda(v)(lambda wedge f)(R)=lambda(v)f(p)
on the primary-zero locus. Hence the raw t_2 shifts by lambda(v)p.

The total secondary functional is preserved by the paired affine change
(t_2,mu) -> (t_2+a p, mu+a lambda).
Thus raw t_2 is not intrinsic; the natural secondary object is a combined affine/torsor class. A universal presentation-free proof that all degree-three bracket terms are exactly absorbed by this quotient remains open.

Decisions:
- D_4/D_5 factorization: FAIL / CLOSED;
- corrected P_4/D_10 threshold: PASS / LOCAL;
- raw t_2 intrinsicity: FAIL / CLOSED;
- combined affine secondary carrier: OPEN / LOAD-BEARING;
- HA61-B: OPEN / LOAD-BEARING;
- HA61-C: not opened.

Records: research/HARD_ATTACK_61_B5_1_SOURCE_QUOTIENT_CORRECTION_2026-09-20.md; research/HARD_ATTACK_61_B5_2_AFFINE_T2_GAUGE_2026-09-20.md.
## 2026-09-20 — HA61-B5: D_4 CUTOFF FAILS AT MOD-27; P_4 RESIDUAL OPEN

HA61-B5 establishes a sharp correction. The mod-9 argument “D_4-errors vanish after division by 3” cannot be reused at mod 27 after division by 9. The explicit D_4 element g^9 gives
\[
z(g^9)/9\equiv f(g)\pmod3
\]
for rho(g)=1+3a mod 27, so D_4-membership alone does not kill the secondary contribution.

The correct source decomposition is
\[
E_{\ge4}=E_{P_4}+E_{>P_4}.
\]
The P_4 component is now the first forced candidate for the intrinsic t_2 residual; deeper terms must be separately killed or shown to factor through the same datum.

Decision:
- blanket E_{>=4} vanishing mod 27: **FAIL / CLOSED**;
- D_4 as sufficient secondary cutoff: **FAIL / CLOSED**;
- P_4 residual -> intrinsic t_2: **OPEN / LOAD-BEARING**;
- deeper-than-P_4 factorization/vanishing: **OPEN**;
- HA61-B: **OPEN / LOAD-BEARING**;
- HA61-C: **not opened**.

Record: research/HARD_ATTACK_61_B5_FILTRATION_CUTOFF_2026-09-20.md (commit d563edad1f5e690ab70c2e13ac28cacb76bc1318).



## 2026-09-20 — HA61-B4 PASS/LOCAL; B5 OPEN

HA61-B4 is **PASS / LOCAL**. Distinct A_2 lift classes over the same mod-3 class differ by 3c, and naturality of the coefficient-extension pullback gives
\(\delta_3(z+3c)-\delta_3(z)=\delta_2(c)\). This exposes the exact obstruction to lift-class independence rather than assuming it.

For both frozen standard branches q=3 and q=9, direct primary crossed-word evaluation gives \(\delta_2\equiv0\), so the secondary obstruction is independent of the A_2 lift class. This agrees with the direct mod-27 formulas.

Boundary: the universal statement is still open. An arbitrary admissible input with nonzero \(\delta_2\) would produce a secondary obstruction on a lift torsor, not a function of f alone. Therefore the next attack is B5: filtration cutoff/source audit, not HA61-C.

Record: research/HARD_ATTACK_61_B4_LIFT_CLASS_INDEPENDENCE_2026-09-20.md.


## 2026-09-20 — HA61-B3 CLOSED / B4 OPEN

HA61-B3 is now **PASS / CLOSED**. The A_2 representative gauge z→z+dφ cannot change the secondary connecting obstruction: after lifting φ to A_3, the compatible lift changes by dφ~, and d^2=0 gives exact equality of the obstruction cocycles. Therefore no genuinely gauge-dependent B_{rho_2} can be an intrinsic secondary invariant.

This does NOT close the old-action question completely. Distinct A_2-valued cohomology lifts over the same primary-zero f can still differ by non-gauge data. The decisive next question is HA61-B4: whether the remaining non-mu secondary contribution is canonically represented by the next filtered residual t_2, or whether an additional lift-class parameter survives.

Current order remains: B1 → B2 → **B3 PASS/CLOSED** → **B4 OPEN/LOAD-BEARING** → B5. No HA61-C and no all-n induction yet.

Record: research/HARD_ATTACK_61_B3_GENERAL_A2_LIFT_GAUGE_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 54: HA53 SUPERCEDES THE HA52 d3 WARNING

A critical review of HA52–53 was recorded. HA52 correctly established dim E_3^{2,1}=19 but left a generic warning that a later d3-Bockstein phenomenon might remove the sector. HA53 closes that concern completely: for (p,q)=(2,1), every r>=3 has zero outgoing target E_r^{2+r,2-r}, and every incoming source E_r^{2-r,r} has negative first index. Hence E_3^{2,1}=E_infinity^{2,1}, with dimension 19. The generic cyclic-kernel d3-Bockstein phenomenon remains valid elsewhere, but cannot act on this bidegree.

The permanent piece is now treated as the canonical quotient S=ker(H^2(V) tensor K -> H^4(V))/im(d2:H^2(W)->H^2(V) tensor W^*), with dim S=19, rather than as an isolated dimension count.

Decision:
- HA52 d2 calculation: PASS / CLOSED;
- HA53 permanence: PASS / CLOSED;
- HA52 warning that d3 may remove the 19D sector: HISTORICAL / SUPERSEDED;
- canonical 19D LHS filtration piece S: PASS / CLOSED;
- H-module structure: OPEN / LOAD-BEARING;
- twisted beta_rho^2 on S: OPEN / LOAD-BEARING;
- orientation-selector interpretation: OPEN / DECISIVE.

Record: research/KUMMER_HARD_ATTACK_54_CRITICAL_CORRECTION_AND_19_QUOTIENT_2026-09-20.md

Next authorized attack: construct the induced H-action on S from the central extension functorially; no dimension-based module identification is permitted.
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



## 2026-09-20 — FIRST-STAGE LOWER 3-CENTRAL INFORMATION BOUNDARY

The first-stage theorem draft is recorded in research/LOWER_3_CENTRAL_INFORMATION_BOUNDARY_2026-09-20.md. For the standard family G_{3^s} versus G_∞, the sharp finite-quotient thresholds are D_N: N≤3^s and P_n: n≤s+1, with sharp separation at the next level by abelianization. Thus the q-information scale is exponential in Zassenhaus depth but linear in lower-3-central depth. With the known standard-family orientation formula, χ mod 3^k has information boundary D_{3^{k-1}+1} versus P_{k+1}; mod 27 gives D_10 versus P_4.

Status: Zassenhaus threshold PASS / LOCAL; lower-3-central threshold PASS / LOCAL subject to the standard P_n product formula; linear χ-information boundary PASS / LOCAL under standard-family/classification dependence. This is not yet an intrinsic pointed Kummer-recognition theorem. Next substantive task is to test whether the relevant q-blind Kummer condition factors through G/P_{k+1}. No new gate is introduced.
## AUTHORITATIVE UPDATE — 2026-09-20 — CRITICAL CORRECTION: MIXED m-ADIC GATE + ZASSENHAUSZ THRESHOLD

A review correction was audited and accepted.

First, the previously discussed Zassenhaus threshold argument did **not** identify (G/D_N(G)) with its abelianization. The precise statement is
[
(G/D_N(G))^{ab}=G/(D_NG').
]
For (G_{3^s}) and (N=3^s+1), the Jennings formula gives
[
(G_{3^s}/D_N)^{ab}cong mathbf Z/3^s	imes(mathbf Z/3^{s+1})^3,
]
while the power-free control has
[
(G_infty/D_N)^{ab}cong(mathbf Z/3^{s+1})^4.
]
For (Nle3^s), (x_1^{3^s}in D_N(F)), so the defining relation becomes (c=[x_1,x_2][x_3,x_4]=1) modulo (D_N(F)), giving
[
G_{3^s}/D_Ncong G_infty/D_N.
]
Thus the threshold (D_{3^{n-1}+1}) versus (D_{3^{n-1}}) is a valid **PASS / LOCAL** information boundary for (chimod3^n) within the standard Demushkin family, with the classification/orientation formula explicitly identified as an external dependence. It is not a universal pointed naturality theorem.

Second, HARD ATTACK 10 is confirmed to close only the ordinary presentation-independent local degree-(le3) Fox truncation. It does not close a mixed
[
mathfrak m=(3,I)
]
finite carrier. The candidate
[
J_n^{mix}=I_{mathrm{Fox}}+mathfrak m^n
]
is therefore **OPEN / reauthorized for definitional attack only**.

The existence and non-tautology gates are separated: Fox-derived finite constructions are not excluded at the existence stage; genuine compression/independence is tested only after intrinsicity and the orientation bridge are established.

The load-bearing new issue is relator-gauge naturality. For (r'=grg^{-1}), the Fox derivative acquires the additional term
[
g,partial r+(1-grg^{-1})partial g.
]
The mixed carrier definition must therefore specify the relation/augmentation ideal precisely before naturality can be claimed.

Decision:
- corrected Zassenhaus threshold: **PASS / LOCAL**;
- ordinary degree-3 Fox truncation no-go: **PASS / CLOSED**;
- mixed m-adic finite carrier: **OPEN / REAUTHORIZED FOR DEFINITIONAL ATTACK ONLY**;
- mixed-carrier relator-gauge naturality: **OPEN / LOAD-BEARING**;
- no numerical mixed-jet scan until definition + gauge naturality are passed.

Record: `research/CRITICAL_CORRECTION_MIXED_MADIC_AND_ZASSENHAUSZ_THRESHOLD_2026-09-20.md`

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 17: BOCKSTEIN NON-TAUTOLOGY

The apparent mod-27 orientation bridge was attacked more strongly. The coefficient-extension carrier \(\mathcal B_{27}\) separates the standard family exactly by the q 3-adic valuation class, while the proposed logarithmic orientation digit has the corresponding values as a known function of q. Therefore the present evidence is compatible with forbidden classification repackaging: \(\mathcal B_{27}\to v_3(q)\text{-class}\to q\text{-class}\to\chi\).

Decision: the coefficient-extension package remains **PASS / LOCAL as an intrinsic q-information detector**, but as a new orientation carrier it is **CONDITIONAL / NOT YET ADMISSIBLE**. A genuine carrier requires a presentation-free universal identity or independent universal property producing \(\frac13\log\chi\) directly, not by first recovering q/classification data.

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 16: MOD-27 BOCKSTEIN-EXTENSION CARRIER

A new intrinsic finite-level candidate survives the definition gate:
\[
\mathcal B_{27}=(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9),
\]
where \(\beta_9\) comes from \(0\to\mathbf F_3\to\mathbf Z/27\to\mathbf Z/9\to0\). It is q-blind, functorial, independent of Fox coordinates, and naturally contains the established mod-9 carrier.

For the standard Demuškin family, direct relator lifting gives the expected q=3/q=9/q≥27 separation. The correct additive target is the logarithmic orientation digit \(\lambda_{27}=\frac13\log\chi\pmod9\). The frozen-family values are \(e_2,3e_2,0\), which exponentiate to \(\chi(x_2)=13,10,1\pmod{27}\).

Critical boundary: the intrinsic orientation bridge has not yet been proved independently of the standard presentation. In particular, it must be shown that the cup-dual of the relevant Bockstein layer is naturally the corresponding coefficient of \(\frac13\log\chi\), with no hidden use of q or the known orientation formula.

Decision:
- mod-27 Bockstein-extension candidate: **OPEN / STRONG CANDIDATE**;
- definition/q-blindness/reduction: **PASS**;
- separation: **PASS / LOCAL**;
- orientation bridge: **OPEN / load-bearing**;
- strict compression below Fox: **OPEN**.

Record: research/MOD27_BOCKSTEIN_EXTENSION_CARRIER_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 15: MOD-27 CATEGORY ADEQUACY

A definition-level loophole in the PRE-MOD27 gate has been closed. If the full group G is allowed as an unrestricted input with arbitrary intrinsic constructions, then the canonical dualizing module/action already contains chi, and the Demuškin classification identifies q as a group invariant from which the canonical orientation is recovered. Such a group-only J_27 is therefore known/tautological relative to the intended filtered-information problem, not a new carrier.

The gate has been tightened: q-blindness now excludes not only explicit q/chi, but also first extracting q, the dualizing action, or an equivalent complete classification invariant and repackaging it as J_27. A surviving carrier must be constructed directly from the declared filtered/relation-information functor and must not factor through an already-known canonical-orientation object without an independent obstruction construction.

Decision:
- unrestricted group-intrinsic J_27: **HISTORICAL / SUPERSEDED as a new-carrier candidate**;
- category-adequacy correction: **PASS / CLOSED**;
- genuine filtered/relation J_27: **OPEN**;
- no numerical mod-27 scan authorized until the revised input category is frozen.

Record: research/MOD27_CATEGORY_ADEQUACY_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 14: FOX LOCAL QUOTIENT COMPRESSION CLOSED

The frozen (q=3) exact local Fox obstruction algebra was reduced explicitly:
[
mathcal A_{mathrm{Fox}}
=
mathbf Z_3[[u_1,u_2,u_3,u_4]]
/
(u_1,u_3,u_4,2u_2+3)
congmathbf Z_3.
]

Thus the local Fox obstruction scheme on (1+3mathbf Z_3) is already a reduced characteristic-zero point,
[
(1,-1/2,1,1).
]

Consequently, any proper unital quotient of this local coefficient algebra either loses characteristic-zero (3)-adic information or collapses the point. Therefore there is no strictly smaller quotient of the exact local Fox carrier that still retains the full (3)-adic orientation.

Decision:
- quotient-of-local-Fox-scheme compression: **FAIL / CLOSED**;
- exact local Fox carrier minimal under full-(3)-adic-preserving quotients: **PASS / CLOSED**;
- independently defined intrinsic non-quotient exact compression: **OPEN**.

Record:
research/ORIENTATION_FOX_LOCAL_QUOTIENT_MINIMALITY_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 13: FULL ASSOCIATED-GRADED NO-GO

A stronger negative boundary has now been established.

For infinite Demuškin pro-(3) groups of fixed rank, the full graded group algebra
[operatorname{gr}mathbf F_3[[G]]cong U(L(G))
]
coming from the complete (3)-Zassenhaus filtration is the quadratic/PBW Demuškin graded algebra determined by
[
[X_1,X_2]+[X_3,X_4]+cdots,
]
independently of the Demuškin (q)-invariant. Thus the full mod-3 associated-graded object is (q)-blind, not merely every bounded truncation.

In the rank-four family
[
G_{3^s}=langle x_imid x_1^{3^s}[x_1,x_2][x_3,x_4]
angle,
qquad
G_infty=langle x_imid [x_1,x_2][x_3,x_4]
angle,
]
the graded object is therefore unable to distinguish the groups at the mod-3 graded level, while
[
chi_{3^s}(x_2)=(1-3^s)^{-1}
]
varies with (s), and (chi_infty(x_2)=1).

This upgrades the previous finite-window obstruction to a full associated-graded no-go.

Decision:
- **full mod-3 associated graded (Rightarrow q) or full (chi): FAIL / CLOSED;**
- any successful carrier must contain non-graded filtered/characteristic-zero extension information;
- the first sufficient extension datum at mod-9 is the degree-3 power component (P_3) coupled to (R_2);
- this is a genuine lower bound, but not an absolute category-independent minimality theorem.

Important precision: the full (3)-adic digits do not necessarily require infinitely many independent extension classes. For fixed (q=3), the exact equation (1+2B=0) compresses all digits into one exact (mathbf Z_3)-coefficient relation. Hence the remaining question is specifically whether such exact extension information admits a canonical intrinsic compression smaller than the universal Fox obstruction scheme.

Record:
research/ORIENTATION_FULL_GRADED_NO_GO_MINIMAL_EXTENSION_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-20 — DEGREE-3 FOX TRUNCATION FAILS UNDER NIELSEN CHANGE

A concrete Nielsen-equivalent presentation
\[
x_1=y_1y_2,\quad x_2=y_2,\quad x_3=y_3,\quad x_4=y_4
\]
was used to test whether the fixed-normal-form degree-3 Fox compression is intrinsic.

The transformed exact Fox row contains higher local degrees. After truncation to degree \(\le3\) around \(Y_i=1\), the second row evaluates at the transported canonical point \((-2,-1/2,1,1)\) to
\[
-243/2\neq0,
\]
while the full row vanishes exactly.

Decision:
\[
\boxed{\text{presentation-independent degree-3 Fox truncation = FAIL / CLOSED}.}
\]

This does not rule out a different intrinsic exact filtered carrier; it rules out the naive identification of that carrier with the degree-3 truncation of the universal Fox row.

Record:
research/ORIENTATION_FOX_DEGREE3_NIELSEN_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 9: NAIVE INTEGRAL AUGMENTATION JET CLOSED

The proposed next object
\[
\mathcal R_3^{\mathbf Z_3}=\langle r-1\rangle\subset I^2/I^4,
\qquad I=\ker(\mathbf Z_3[[F]]\to\mathbf Z_3),
\]
is **not defined as stated** for the frozen relation
\[
r=x_1^3[x_1,x_2][x_3,x_4].
\]

Writing \(X_i=x_i-1\),
\[
x_1^3-1=3X_1+3X_1^2+X_1^3,
\]
while the commutator product begins in ordinary augmentation degree 2. Hence
\[
r-1=3X_1+[X_1,X_2]+[X_3,X_4]+O(I^3),
\]
so
\[
\boxed{r-1\notin I^2}.
\]

Therefore the plain \(\mathbf Z_3\)-augmentation quotient \(I^2/I^4\) cannot be the sought integral analogue of the mod-3 Zassenhaus degree-(2,3) jet. This is a **FAIL / CLOSED** definition-level result.

The structural reason is that the Zassenhaus filtration is naturally obtained from the completed \(\mathbf F_3[[F]]\) augmentation ideal; replacing \(\mathbf F_3\) by \(\mathbf Z_3\) changes the filtration and retains the mixed p-adic terms \(3X_1\), \(3X_1^2\). The earlier rejection of naive \(\mathbf Z_3\)-scalar extension of the restricted-Lie carrier is independently confirmed.

A mixed p-adic/Zassenhaus weighted filtration remains **OPEN**, but its finite associated graded pieces retain residue-layer information rather than an unrestricted exact 3-adic scalar. Thus it does not by itself evade the already closed bounded-degree + finite-precision obstruction.

The exact universal Fox obstruction scheme remains the correct characteristic-zero comparison object. The remaining structural target is now:
\[
\boxed{
\text{intrinsic filtered jet tower}
\;\stackrel{?}{\longrightarrow}\;
\text{exact Fox orientation locus}
}
\]
with an explicit account of where the infinitely many 3-adic digits enter. No further plain \(I^2/I^4\) computation is authorized.

Detailed audit:
research/ORIENTATION_INTEGRAL_AUGMENTATION_JET_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-19 — BOCKSTEIN–RELATION-JET IDENTIFICATION GATE CLOSED

The load-bearing identification
\[
\beta\longleftrightarrow p(P_3)
\]
has been audited. A direct cochain/transgression calculation shows that the Bockstein of a mod-3 generator is obtained by lifting it to \(\mathbf Z/9\), evaluating the lift on the relator, and dividing the resulting obstruction by 3. Commutator terms contribute no exponent sum; the restricted-cubic power term \(X_i^{[3]}\) contributes exactly its coefficient. Thus the Bockstein vector is projectively the same power-direction vector \(p(P_3)\), with only the common transgression/fundamental-class sign/unit left as gauge.

For q=3, \(P_3=X_1^{[3]}\), so \(p\sim X_1^{(1)}\). For q=∞, \(p=0\). Therefore the previously established projective recovery functional applies intrinsically and gives \(\chi\bmod9=(1,4,1,1)\) for q=3.

Decision:
- Bockstein–relation-jet projective identification: **PASS / CLOSED** under the standard one-relator transgression convention;
- absolute sign/normalization of the H² generator: **CONDITIONAL / gauge-dependent**, irrelevant to the projective carrier;
- intrinsic cup+Bockstein carrier → \(\chi\bmod9\): **PASS / CLOSED**;
- no higher-digit conclusion and no broad scan.

Record: research/BOCKSTEIN_RELATION_JET_IDENTIFICATION_AUDIT_2026-09-19.md

## AUTHORITATIVE UPDATE — 2026-09-19 — M3 COMPARISON BOUNDARY

The intrinsic mod-9 carrier [(R,p)] was compared with Pál–Quick's A_3/Hochschild canonical class.

A genuine **PASS / LOCAL** detection-level compatibility is established for the standard p=3 Demushkin family:
- q=3: first Bockstein/power direction is nonzero and Pál–Quick's canonical A_3 class is nonzero;
- q=3^f, f≥2: first Bockstein layer vanishes and the Pál–Quick A_3 obstruction vanishes in their theorem range.

This is a common q=3 power-layer detection, not an equality theorem.The stronger map/factorization
\[
[(R,p)]\longrightarrow\gamma_{A_3}
\]
remains **OPEN** because the two objects have different targets and constructions: the former is the cup/Bockstein carrier, while the latter is a Hochschild/cochain obstruction computed via higher tensor data and Dwyer U_4 lifting.

No U_4/Hochschild scan is authorized. A future M3 continuation must first define a natural target map and prove its functoriality and gauge compatibility.

Detailed record:
research/M3_CUP_BOCKSTEIN_TO_PAL_QUICK_COMPARISON_AUDIT_2026-09-19.md

## AUTHORITATIVE UPDATE — 2026-09-19 — INTRINSIC MOD-9 CARRIER VIA CUP + BOCKSTEIN

The μ–χ bridge was critically narrowed: μ is an intrinsic mod-3 automorphism/duality-line shadow, but μ alone does not determine χ mod 9 and admits no simple homomorphic lift into 1+3Z_3. A deeper μ + additional-data bridge remains conceptually open; no μ-only scan is authorized.

The standalone Bockstein candidate is also CLOSED as an orientation carrier: β alone detects the q=3 power direction but not the scalar 4 mod 9.

A new structural result now closes M1 at the mod-9 level.

For
\[
V=H^1(G,\mathbf F_3)^*
\]
and the intrinsic maps
\[
\smile:H^1\times H^1\to H^2,
\qquad
\beta:H^1\to H^2
\]
with dim H^2=1, choose temporarily ω≠0 in H^2 and define
\[
f\smile g=(f\wedge g)(R)\omega,
\qquad
\beta(f)=f(p)\omega.
\]
Changing ω to uω rescales both R and p by u^{-1}; therefore
\[
\boxed{\overline J_3(G)=[(R,p)]}
\]
is canonical. In the minimal one-relator model, R is the quadratic relation and p is the restricted-cubic/power component of the degree-3 relation jet.

The intrinsic carrier therefore has the factorization
\[
(H^1,H^2,\smile,\beta)
\longmapsto
[(R,p)]
\longmapsto
\overline\Theta(\lambda)(f)=f(p)+(\lambda\wedge f)(R)
\longmapsto
\chi\bmod9.
\]

For q=3, p=e_1^{(1)} and the unique zero is λ=e_2^*, giving (1,4,1,1) mod 9. For q=∞, p=0 and the zero is λ=0.

Decision:
- standalone Bockstein: FAIL/CLOSED;
- cup + Bockstein intrinsic carrier: PASS/CLOSED at mod-9 level, under the stated standard transgression/Bockstein identification;
- M1 intrinsic carrier functor: PASS/CLOSED at mod-9 level, under the standard transgression/Bockstein identification, under the stated standard transgression/Bockstein identification;
- M2 orientation factorization: PASS/CLOSED for the stated projective degree-(2,3) mod-9 functional, with beta ↔ p(P3) supplied by the standard transgression/Bockstein formula;
- M3 independent comparison with Pál–Quick A3/Hochschild class: NEXT AUTHORIZED TARGET;
- no broad computational scan is authorized.

Detailed record:
research/ORIENTATION_MOD9_INTRINSIC_CUP_BOCKSTEIN_CARRIER_2026-09-19.md

## LATEST MANUSCRIPT CONSOLIDATION — 2026-09-19

A unified manuscript draft has been created:
`research/ORIENTATION_RECONSTRUCTION_MANUSCRIPT_DRAFT_2026-09-19.md`

The paper is organized around one central question:
[
	ext{How much filtered relation information is necessary and sufficient to recover the canonical }3	ext{-adic orientation?}
]

The consolidated logical spine is:
1. bare quadratic graded data loses (chimod9);
2. the projective degree-(2,3) relation jet recovers (chimod9);
3. its coarsest natural quotient is (overline J_3=[(R,p(P))]);
4. a compatible finite-level filtered relation-jet tower recovers the full (chi) by inverse limit;
5. bounded degree plus finite coefficient precision cannot universally recover full (chi);
6. fixed (q=3) exact (mathbf Z_3)-coefficient relation/evaluation data does recover full (chi), but no non-tautological finite characteristic-zero compression analogous to (overline J_3) has been proved.

This manuscript is a structural consolidation, not yet a publication-ready literature-complete paper. Claims are intentionally restricted to the audited hypotheses and boundaries.

---

## LATEST AUTHORITATIVE UPDATE — 2026-09-19 — EXACT Z_3 CARRIER BRANCH ENDPOINT

The remaining exact-carrier branch has now been pushed to its structural boundary and closed.

New record:
`research/ORIENTATION_EXACT_Z3_CARRIER_BRANCH_ENDPOINT_2026-09-19.md`

The target was a non-tautological finite/concrete exact \\(\\mathbf Z_3\\)-carrier analogous to the mod-3 compressed carrier \\(([R],p(P))\\).

Final status:
- fixed q=3 exact filtered relation/evaluation data -> full \\(\\chi\\): **PASS / CLOSED**;
- compatible full filtered tower -> full \\(\\chi\\): **PASS / CLOSED**;
- naive characteristic-zero “restricted Lie” lift of the mod-3 quotient: **FAIL / CLOSED**;
- canonical quotient by the independently fixed crossed-derivation evaluation family: **PASS as a universal quotient**, but this is not yet a non-tautological finite compression;
- non-tautological finite/concrete exact compression analogous to \\(([R],p(P))\\): **OPEN / NOT PROVED**, and no further scan is warranted;
- universal bounded-degree + finite-precision carrier across q=3^s: **FAIL / CLOSED**.

Critical correction: an exact finite augmentation truncation is a legitimate object, but no proof was obtained that it alone factors the full exact crossed-derivation coefficient law under the frozen convention. Do not silently promote this to a theorem.

This closes the current exact-carrier search at the structural boundary. A future continuation would require a genuinely new characteristic-zero invariant or a new factorization theorem, not another scan of the already audited candidates.

## Latest exact-Z_3 bounded-degree result — 2026-09-19

The fixed-q=3 branch has reached its natural endpoint.

A single projective degree-(2,3) exact filtered relation jet over Z_3 determines the full orientation for the frozen q=3 normal form:
[
mathbb J^{ex}_3 Longrightarrow 
ho(x_1)=
ho(x_3)=
ho(x_4)=1,quad 1+2
ho(x_2)=0,
]
hence
[
chi(x_2)=-1/2=(1-3)^{-1}inmathbf Z_3^	imes.
]

The presentation-change calculation has the same residual gauge
[
(R,P)mapsto(uR,uP+[v,R])
]
at degree <=3, and degree-one functionals annihilate [v,R], so the recovery zero set is unchanged. This closes the fixed-q=3 exact-carrier branch at the same conditional standard minimal one-relator pro-3 facts used by the mod-9 E1-E5 audit.

This does NOT contradict the universal bounded-degree obstruction: that obstruction varies q=3^s, and for every fixed degree d one can choose 3^s>d. The exact q=3 carrier is therefore a fixed-group exact-filtered result, not a universal finite-information carrier.

Record: research/ORIENTATION_EXACT_PROJECTIVE_DEGREE3_FULL_CHI_CLOSURE_2026-09-19.md

Decision:
- fixed q=3 exact projective bounded-degree carrier -> full chi: PASS / CLOSED
- universal finite-information bounded-degree carrier -> full chi: FAIL / CLOSED
- bare F_3 graded carrier -> full chi: FAIL / CLOSED

## Latest bounded-degree obstruction — 2026-09-19

The stronger branch was pushed without a scan.

A new no-go result is recorded in
`research/ORIENTATION_BOUNDED_DEGREE_FINITE_INFORMATION_OBSTRUCTION_2026-09-19.md`.

For the family
[
G_{3^s}=langle x_imid x_1^{3^s}[x_1,x_2][x_3,x_4]
angle
]
and (G_infty), the quadratic initial relation is identical, while
[
chi_{3^s}(x_2)=(1-3^s)^{-1}
e1=chi_infty(x_2).
]
The power term (x_1^{3^s}) first appears in Zassenhaus degree (3^s). Hence every fixed degree bound (d) misses the q-dependent term for sufficiently large (s). If finite coefficient precision modulo (3^N) is also imposed, choosing (sge N) makes the same carrier indistinguishable modulo (3^N), while the full 3-adic characters remain different.

Decision:
**PASS / CLOSED:** no universal finite-information carrier with both bounded filtration degree and bounded 3-adic precision can recover the full (chi).

Important loophole:
a bounded-degree carrier with exact (mathbf Z_3)-coefficients has infinitely many 3-adic digits and is therefore not a finite-information carrier. For the fixed q=3 presentation, such an exact coefficient-level carrier may recover the full (chi); that separate intrinsic/projective formulation remains OPEN.

This distinction now replaces the undifferentiated “finite bounded-degree jet” OPEN label.

---

# CURRENT STATE — 2026-09-19


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
