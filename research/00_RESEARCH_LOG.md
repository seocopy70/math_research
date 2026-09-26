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
