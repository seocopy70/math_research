# FOLLOW-UP MERGED AUDIT — 2026-09-26

## Scope
Audited the uploaded `followup_merged.tex` only. The frozen publication manuscript was not modified.

## Authoritative continuity state
The repository baseline was restored from RESEARCH_MAP.md, CURRENT_STATE.md, research/00_RESEARCH_LOG.md, and RESEARCH_CONTINUITY_PROTOCOL.md. The current successor-paper gate is sharpness + q-collapse + ET_p obstruction/uniformity; the mixed-commutator issue is explicitly load-bearing.

## Findings

### 1. LaTeX build
The uploaded file does not compile as supplied:
- line 74 uses `\Fp`, but no macro `\Fp` is defined.
- Direct `pdflatex -halt-on-error` stops with `Undefined control sequence`.
- After a temporary, non-source modification defining `\Fp := \mathbb F_p`, three pdflatex passes succeed.
- Final temporary test PDF: 3 pages.
- One harmless overfull hbox (~55.97pt) remains around lines 22--23.

Classification: **FAIL/CLOSED (source syntax defect)**; easy repair, not mathematical.

### 2. Section I — finite-window recognition
The corrected crossed-cocycle commutator formula is algebraically consistent:
z([a,b]) = rho(a)^(-1) rho(b)^(-1) ((1-rho(b))z(a)+(rho(a)-1)z(b)).
For r_f=x_1^(p^f) product of paired commutators, the displayed F_1/F_2 formulas agree with direct substitution; later-pair formulas should nevertheless be written explicitly in the final paper rather than “similar”.

Solving F_i=0 gives a_1=1, all a_i=1 except a_2, and a_2=(1-p^f)^(-1) mod p^k. For p=3,f=1 the residues are 4 mod 9, 13 mod 27, 40 mod 81.

Classification: **PASS/LOCAL** for the displayed algebra; publication theorem remains conditional on the stated Demushkin/Kummerian hypotheses and the previously proved finite-depth factorization.

### 3. Section II — sharpness
A real proof error occurs in line 43:
for f>1 and f<k, the canonical orientation has rho(x_2)=(1-p^f)^(-1) in U_f, so it is generally NOT surjective onto U_{1,k}. The parenthetical “choose a_2=1+p ... while F_i=0 still holds by adjusting” is false: F_i=0 forces the canonical a_2.

This does NOT kill sharpness. Repair:
- for f<k, use the canonical rho (surjectivity unnecessary) and the cocycle z(x_1)=1, z(x_i)=0 otherwise; F_i=0 gives a valid cocycle, and z(x_1^(p^(k-1)))=p^(k-1) != 0 mod p^k.
- for f>=k, the existing x_3 witness with rho(x_2)=1+p and z(x_3)=1, z(x_1)=0 is valid; F_3=0 and the relation obstruction vanishes.

Thus the d>=4 sharpness theorem is salvageable, but the written proof must be corrected.

Classification: **FAIL/CLOSED for the written proof; theorem OPEN pending this local repair**.

### 4. Section III — free pro-p obstruction
For F_2, H^2(F_2,A)=0, so every orientation is Kummerian; this is consistent with the literature. The count |Hom(Q_k,U_{1,k})|=p^{2(k-1)} is also consistent because Q_k^ab has exponent p^k while U_{1,k} has order p^(k-1).

However, “no predicate depending only on Q_k” is too broad. The correct impossibility statement must quantify **isomorphism-natural / functorial, q-blind selectors on the bare abstract quotient**. Otherwise an arbitrary non-natural choice function is not ruled out.

Classification: **PASS/LOCAL after narrowing the logical quantifier**.

### 5. Section IV — q-collapse
The structural statement is sound:
x_1 in P_1(F)\P_2(F) implies x_1^(p^f) in P_{p^f}(F)\P_{p^f+1}(F) for free pro-p F.
Hence x_1^(p^f) dies in Q_k exactly when f>=k, and for f>=k the relation r_f has the same image as the q=infinity relation. The abelianization separates f<k from f>=k.

The lemma should cite the free restricted-Lie/Jennings-Lazard initial-form argument, not be left unsupported.

Classification: **PASS/LOCAL**.

### 6. Section V — mixed commutator gate
The current text treats the key statement as open:
N subset P_n(Q_k(G_1)*_p Q_k(G_2)).
A stronger categorical argument closes this for arbitrary pro-p G_1,G_2.

Let T_n(G)=G/P_n(G). The functor T_n is left adjoint to the inclusion of the full subcategory of pro-p groups H satisfying P_n(H)=1: every homomorphism G->H kills P_n(G) by functoriality. Since free pro-p product is a coproduct,
T_n(G_1 *_p G_2) is canonically isomorphic to
T_n(G_1) *_p T_n(G_2) / P_n(T_n(G_1) *_p T_n(G_2)).
Equivalently, with H=Q_n(G_1)*_p Q_n(G_2), the kernel N of H -> Q_n(G_1*_pG_2) is exactly P_n(H), not merely a vaguely described mixed subgroup.

Zassenhaus commutator functoriality gives [P_i(H),P_j(H)] subset P_{i+j}(H), so the genuinely mixed generators of N occur only at total Zassenhaus weight >= n. This is the correct rigorous replacement for the current “Kurosh+verbal” sentence.

For the requested small test D_1 *_p D_2 at k=2, n=4: N=P_4(Q_2(D_1)*_pQ_2(D_2)); mixed terms such as [P_1(D_1),P_3(D_2)] and [P_2(D_1),P_2(D_2)] have total weight >=4. Since P_4(S_2)=1, every affine map to S_2 kills N. The same argument works for all k.

Therefore the mixed-commutator factorization sub-gate is **PASS/CLOSED**, once stated with the categorical truncation lemma.

### 7. Section V — uniqueness / “rigid ET_p”
The present definition “each *_p factor contains a Demushkin block” is too vague to support the claimed blockwise uniqueness. A clean theorem is available for a narrower class: finite free pro-p products of Demushkin groups with their canonical orientations. Kummerianity is preserved under free products, and restriction/quotient arguments force a Kummerian candidate on each Demushkin factor to equal its unique canonical orientation.

Thus:
- pure free products of Demushkin blocks: uniform window n(k)=p^(k-1)+1 is supported;
- arbitrary recursively defined “rigid ET_p” with semidirect/fibre-product operations: **OPEN** until the class and induction are specified;
- the current Newton/J=diag(...) algorithmic claim should be removed or separated from the structural theorem unless an explicit algorithmic input model is defined.

Classification: **PASS/CLOSED for the pure free-product subclass; OPEN for the broader current ET_p^rig wording**.

## Overall gate classification
- I recognition: **PASS/LOCAL**
- II sharpness theorem: **OPEN** after correcting a false surjectivity step
- III free-pro-p obstruction: **PASS/LOCAL** after naturality qualification
- IV q-collapse: **PASS/LOCAL**
- V mixed commutator factorization: **PASS/CLOSED**
- V pure Demushkin free-product uniformity: **PASS/CLOSED**
- V broad ET_p^rig uniformity: **OPEN**
- LaTeX source: **FAIL/CLOSED**, trivial macro repair
- Publication novelty: **OPEN/CONDITIONAL**

## Next authorized action
Do not modify the frozen main paper. For the successor paper, first patch the sharpness witness, replace the mixed-commutator paragraph by the truncation/coproduct lemma, narrow the impossibility theorem to natural bare-Q selectors, and define the positive rigid subclass as a precise free-product class before making any broader uniformity claim.
