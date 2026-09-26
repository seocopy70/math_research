# SUCCESSOR PUBLICATION CANDIDATE AUDIT — 2026-09-26

## Scope
This branch contains a new successor manuscript source, paper/successor_main.tex, constructed from the authoritative successor audits after the exact uploaded followup_merged.tex source could not be recovered from the repository or indexed conversation files. It is therefore a new working publication candidate, not a byte-for-byte repair of the uploaded source.

The frozen preceding manuscript paper/main.tex is untouched.

## Mathematical gates

### 1. Affine factorization depth
For
\[
S_k=A_k\rtimes U_{1,k},\qquad A_k=\mathbf Z/p^k\mathbf Z,
\]
the Zassenhaus calculation gives
\[
P_n(S_k)=p^{\lceil\log_p n\rceil}A_k\rtimes U_{\lceil\log_p n\rceil+1},
\]
hence
\[
P_{p^{k-1}}(S_k)\ne1,\qquad P_{p^{k-1}+1}(S_k)=1.
\]
Classification: PASS / CLOSED.

### 2. Arbitrary-candidate factorization
Every crossed cocycle defines a homomorphism to S_k; functoriality kills P_{p^{k-1}+1}. Classification: PASS / CLOSED.

### 3. Sharpness
- f < k: canonical orientation plus z(x_1)=1.
- f >= k: rho(x_2)=1+p, z(x_2)=1, using LTE.
- The second witness uses only x_1,x_2, so d=2 is included.
- No surjectivity of the orientation component is assumed.
Classification: PASS / CLOSED.

Thus
\[
n_{\mathrm{aff}}(k)=p^{k-1}+1
\]
is sharp for all odd p, all f>=1, and all even d>=2 in the specified affine crossed-cocycle category.

### 4. q-collapse
For f>=k, x_1^{p^f} dies in the finite quotient because it lies in P_{p^f} and p^f>p^{k-1}+1. The canonical orientation also reduces to the trivial principal-unit character at level p^k. Classification: PASS / LOCAL.

### 5. Recognition versus factorization
The free pro-p example is deliberately limited to the statement that the Kummer predicate itself does not force uniqueness, since cd_p(F_d)=1 makes every finite-level lifting map surjective. It is not presented as a universal impossibility theorem for every natural selector. Classification: PASS / LOCAL.

### 6. Free-product uniformity
The truncation functor T_n(G)=G/P_n(G) is a reflector onto the P_n=1 subcategory and preserves pro-p coproducts. This closes the mixed-commutator factorization issue for finite free products of Demushkin blocks. Classification: PASS / CLOSED.

Broader recursively defined elementary-type classes remain outside scope.

## Publication gates
- Preceding manuscript preservation: PASS / CLOSED.
- Successor source syntax: PASS / LOCAL static audit; exact GitHub CI result is not exposed by the available workflow-run status endpoint.
- Independent CI build: CONFIGURED / awaiting externally reported Actions result.
- Literature novelty: OPEN / CONDITIONAL.
- Absolute minimality beyond the affine category: OPEN / category-dependent.
- Broad ET_p uniformity: OPEN.

## Required next gate
Run the successor CI build from the exact branch commit, then perform a source-level audit of the CI-built manuscript. Do not promote this branch to a final submission package until CI and the independent audit both pass.


## 2026-09-26 — EXACT CI GATE PASSED

The successor branch was checked at the exact head commit
`730b1bf815e0c30cd46d0803cf1b72482df970a8`.

The first CI attempt on the initial successor source exposed a real LaTeX defect in the bibliography: the phrase `pro-\\ell` was outside math mode. This was corrected to `pro-$\\ell$` in the successor source only. No mathematical statement or proof was changed.

Independent GitHub Actions verification then passed on the corrected exact commit:
- Build successor manuscript, run 10: **PASS**
- LaTeX compile: **PASS**
- PDF existence/output check: **PASS**
- final log check for `undefined`, `LaTeX Warning`, or `Error:`: **PASS / CLEAN**
- artifact `successor-manuscript-pdf`: **PASS**
- artifact ID: `10895855568`
- artifact size: 340066 bytes
- artifact SHA-256: `9e4126ef05ccdcd5078d26677217b9779e103187e461fc8122c5420fa51985c9`

Two identical successful CI runs were observed for the corrected commit (PR and branch-push triggers). The earlier failed runs are historical and are explained by the now-corrected bibliography syntax defect.

The branch comparison against current `main` still shows exactly three successor-only files:
1. `.github/workflows/successor-build.yml`
2. `paper/successor_main.tex`
3. `research/SUCCESSOR_PUBLICATION_CANDIDATE_AUDIT_2026-09-26.md`

`paper/main.tex` is not modified by this successor branch diff.

### Updated publication classification

- affine factorization theorem: **PASS / CLOSED**
- sharpness including d=2 and non-surjective affine orientation: **PASS / CLOSED**
- finite-depth f-collapse: **PASS / LOCAL**
- recognition/factorization separation: **PASS / LOCAL**
- finite free-product uniformity: **PASS / CLOSED**
- exact successor CI build: **PASS / CLOSED**
- publication-candidate source: **PASS / CLOSED**
- preceding manuscript preservation: **PASS / CLOSED**
- absolute minimality beyond affine category: **OPEN / category-dependent**
- broader ET_p uniformity: **OPEN**
- literature novelty: **OPEN / CONDITIONAL**

The successor branch has therefore cleared the technical publication-candidate build gate. It must not yet be described as a novel published result or as an absolute-minimality theorem.


## FINAL MATHEMATICAL REFEREE + PRIOR-ART AUDIT — 2026-09-26

### Referee pass

The successor manuscript was re-read theorem-by-theorem after the exact CI gate had already passed. The audit separates mathematical correctness, scope, and novelty.

#### R1. Definition and continuity boundary — PASS / CLOSED
The manuscript now explicitly restricts affine representations, orientations, cocycles, and candidate maps to continuous maps where the profinite topology matters. This removes an otherwise implicit gap: arbitrary abstract homomorphisms from a profinite group to a finite group need not be continuous.

#### R2. Target filtration — PASS / CLOSED
For
[
S_k=A_ktimes U_{1,k},qquad A_k=mathbf Z/p^k,quad U_{1,k}=1+pA_k,
]
the formula
[
P_n(S_k)=p^{e(n)}A_ktimes U_{e(n)+1},
qquad e(n)=lceillog_p nceil,
]
was checked against the Jennings--Lazard product. The endpoint identities
[
P_{p^{k-1}}(S_k)=p^{k-1}A_k
e1,qquad
P_{p^{k-1}+1}(S_k)=1
]
are correct for odd (p).

Independent integer arithmetic checks for (p=3,5,7) and (k=2,3,4) confirmed the endpoint logarithmic transitions.

#### R3. Functorial factorization — PASS / CLOSED
The upper bound is a direct consequence of continuous functoriality of the Zassenhaus filtration and the triviality of (P_{p^{k-1}+1}(S_k)). This is standard background rather than a claimed new functorial principle. Efrat's representation-theoretic treatment of the Zassenhaus filtration and Mináč--Rogelstad--Tân's work on Zassenhaus dimensions are now cited explicitly.

#### R4. Sharpness, (f<k) — PASS / CLOSED
The canonical orientation and cocycle witness satisfy the relator. With
[
a=(1-p^f)^{-1},
]
the cocycle contribution of the power--commutator part is
[
p^f+a^{-1}(1-a)=0,
]
while (z(x_1^{p^{k-1}})=p^{k-1}
otequiv0pmod{p^k}).

#### R5. Sharpness, (fge k), including (d=2) — PASS / CLOSED
The witness
[
ho(x_2)=1+p,qquad z(x_2)=1,qquad ho(x_1)=1,quad z(x_1)=0
]
satisfies the relator at level (p^k), and
[
z(x_2^{p^{k-1}})
=rac{(1+p)^{p^{k-1}}-1}{p}
]
has (p)-adic valuation (k-1) by LTE. The witness uses only two generators, so the rank-two boundary is genuinely covered.

#### R6. Surjectivity — PASS / CLOSED
The lower-bound proof does not require (ho(G)=U_{1,k}). For (f<k), the canonical orientation can have proper image while the translation component still detects the terminal layer. The manuscript now states this as a property of the proof rather than as an extra hypothesis.

#### R7. Category-relative minimality — PASS / CLOSED
The lower and upper bounds match exactly in the declared category:
[
n_{mathrm{aff}}(k)=p^{k-1}+1.
]
The manuscript correctly avoids the stronger and unjustified phrase "absolute minimality".

#### R8. Finite-depth (f)-collapse — PASS / LOCAL
For (fge k), the power relation lies beyond the retained Zassenhaus window, so the finite quotient identifies the (f)-parameters at that depth. This is a genuine information-loss statement at the specified carrier level. It does not assert isomorphism of the full infinite Demushkin groups.

#### R9. Factorization versus recognition — PASS / LOCAL
The logical distinction is sound. The factorization theorem is representation-theoretic; uniqueness of an orientation selected by a finite cohomological predicate is a separate recognition property.

#### R10. Free pro-(p) counterexample — PASS / LOCAL
For free pro-(p) groups, (operatorname{cd}_p=1) gives the finite-level lifting surjectivity. The manuscript correctly limits the conclusion to the stated Kummer predicate and explicitly refuses to claim impossibility of every conceivable natural selector.

#### R11. Finite free products — PASS / CLOSED
The truncation identity follows from the universal property of the pro-(p) coproduct and the fact that the Zassenhaus quotient is universal among quotients with (P_n=1). The uniform upper bound is therefore inherited functorially; the sharp lower bound is inherited from a standard Demushkin factor.

#### R12. Scope boundary — PASS / CLOSED
The manuscript does not extend the theorem to amalgamated/fibre-product elementary-type constructions. This is important because current literature shows that amalgamated Demushkin constructions can have substantially different 1-cyclotomic behavior.

### Prior-art audit

The audit covered the manuscript's cited literature plus targeted searches for the exact combination of:
- Zassenhaus depth;
- affine/semidirect targets;
- crossed cocycles;
- finite coefficient levels;
- Demushkin groups;
- Kummerian orientations;
- finite-window/factorization language.

Relevant established literature includes:

1. Labute's classification of Demushkin groups and the canonical orientation framework.
2. Efrat--Quadrelli (2019), which develops the Kummerian property, cocycle characterization, and the Demushkin canonical orientation.
3. Efrat (2014), which connects Zassenhaus filtration depth to finite-dimensional representation theory.
4. Mináč--Rogelstad--Tân (2016), which computes Zassenhaus graded dimensions for free, Demushkin, and free-product families.
5. Quadrelli--Weigel (2022), which develops oriented pro-(ell) groups and Kummerian/Bogomolov--Positselski phenomena.
6. Quadrelli (2024), which treats 1-cyclotomic obstructions for constructions involving Demushkin groups and explicitly distinguishes free products from pro-(p)-cyclic amalgams.

The audit did **not** locate a prior theorem stated with all of the following simultaneously:
[
S_k=(mathbf Z/p^k)times(1+pmathbf Z/p^k),
quad
n=p^{k-1}+1,
]
all continuous affine crossed-cocycle representations, and a matching sharp lower bound for the standard Demushkin family including (d=2) and without orientation-surjectivity.

This is **not** an absolute priority claim. The correct publication wording is therefore:

> "To the best of our literature search, we did not find a theorem in the literature stated in this exact affine representation category with this exact sharp depth and lower-bound formulation."

The manuscript now uses this conditional boundary rather than asserting priority.

### Important novelty boundary

The following ingredients are individually not claimed as new:
- Zassenhaus functoriality;
- Jennings--Lazard filtration formulae;
- Kummerianity of free pro-(p) groups;
- canonical Demushkin orientation;
- general Zassenhaus information on Demushkin/free-product families.

The potentially publishable composite result is the **sharp finite affine representation window**
[
oxed{n_{mathrm{aff}}(k)=p^{k-1}+1},
]
together with its rank-two/surjectivity-independent sharpness, finite-depth (f)-collapse, and explicit factorization/recognition separation.

### Final referee classification

- Mathematical correctness of core theorem: **PASS / CLOSED**
- Proof completeness within declared category: **PASS / CLOSED**
- Scope discipline: **PASS / CLOSED**
- Technical source quality: **PASS / CLOSED**
- Exact CI build: **PASS / CLOSED**
- Prior-art separation: **PASS / CONDITIONAL**
- Novelty: **OPEN / CONDITIONAL**
- Absolute minimality outside affine category: **OPEN / category-dependent**
- Broader elementary-type extension: **OPEN**

### Recommendation for submission state

The manuscript is now suitable to be treated as a **publication candidate** from the mathematical-structure and reproducibility standpoint. It should not yet be described as having established priority or unconditional novelty. The remaining uncertainty is external scholarly validation of novelty, not an identified mathematical defect in the present theorem/proof package.
