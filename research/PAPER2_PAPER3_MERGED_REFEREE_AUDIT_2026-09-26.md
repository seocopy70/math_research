# Paper 2 + Paper 3 merged — independent referee audit — 2026-09-26

## Scope

Independent referee-style audit of the merged successor manuscript
`paper/successor_main.tex` on branch `paper2-paper3-merged-2026-09-26`.
The purpose is to test whether the Paper 3 application corpus can be absorbed
without weakening the central Paper 2 theorem, introducing circularity, or
creating a redundant second paper.

Controlling sources:
- `RESEARCH_MAP.md`
- `research/CURRENT_STATE.md`
- `research/00_RESEARCH_LOG.md`
- `research/SUCCESSOR_INDEPENDENT_REFEREE_AUDIT_2026-09-26.md`
- `research/SUCCESSOR_TWO_REMAINING_PROBLEMS_CLOSURE_2026-09-26.md`
- `paper/successor_main.tex`
- `paper3/main.tex`

## 1. Core theorem

The central theorem remains unchanged:
[
n_{\mathrm{aff}}(k)=p^{k-1}+1
]
for the category of all continuous crossed-cocycle representations into
(A_k\rtimes U_{1,k}), for odd (p), (f\ge1), and even (d\ge2).

The Paper 3 material does not enter the proof of the central upper bound or
the two sharpness witnesses. Therefore the logical dependency of the core
theorem remains intact.

**PASS / CLOSED.**

## 2. Mixed-commutator/free-product extension

The merged manuscript retains the reflector argument
(T_n(G)=G/P_n(G)) and its preservation of finite free pro-(p)
coproducts after reflection. The application theorem consequently uses the
same depth (p^{k-1}+1) for mixed words.

The argument is category-theoretic and does not require a new computation
for mixed commutators. This matches the already closed mixed-commutator
audit.

**PASS / CLOSED.**

## 3. Finite-depth parameter collapse

The Paper 3 parameter-profile result is retained, but its proof was tightened
in the merge.

For (D_{f,d}^{\mathrm{ab}}cong\mathbb Z_p^{d-1}\oplus\mathbb Z/p^f),
the Jennings--Lazard product implies that the image of (P_n) in
abelianization is contained in (p^{\lceil\log_p n\rceil}D_{f,d}^{\mathrm{ab}}).
At (n=p^{k-1}+1), this is contained in (p^kD_{f,d}^{\mathrm{ab}}).
Hence for (f<k) the order-(p^f) torsion class survives, while for
(f\ge k) the power relation lies beyond the retained window.

**PASS / CLOSED after repair.**

## 4. Heterogeneous example

The example
[
D_{1,4}*_pD_{3,2}*_pD_{7,4}
]
at (k=4) is used only as an application illustration. It does not carry
the proof of sharpness; sharpness was proved earlier for the full standard
family. This avoids circularity and keeps the example in the correct role.

**PASS / CLOSED.**

## 5. Blockwise Kummer recognition

The positive recognition statement is explicitly restricted to finite free
pro-3 products of rank-four (q=3) Demuškin blocks, exactly the class for
which Paper 1 supplies the selector theorem.

The proof uses:
1. finite-window factorization for arbitrary candidates;
2. the free-product degree-one cohomology decomposition;
3. surjectivity of a direct sum iff each summand is surjective;
4. the Paper 1 factor selector.

The manuscript explicitly states that this does not give a new classification
of orientations of arbitrary free products and does not claim that the free
product itself is Demuškin.

**PASS / CLOSED, subject only to the literature wording remaining modest.**

## 6. Presentation dependence

The upper-bound/free-product factorization is intrinsic. The parameter-collapse
and sharpness examples use standard presentations only for concrete witnesses
and marked finite quotients. The manuscript distinguishes these roles.

**PASS / CLOSED.**

## 7. Absolute minimality boundary

The merged text repeatedly states that (p^{k-1}+1) is sharp in the affine
crossed-cocycle category, not absolutely minimal among arbitrary intrinsic
carriers. This preserves the earlier category-relative boundary.

**PASS / CLOSED.**

## 8. Potential referee objections

No new load-bearing mathematical defect was found in the merged application
material. Remaining issues are expository rather than theorem-level:

- the title's word "Recognition" is defensible because the paper contains a
  positive blockwise application, but the introduction should continue to
  identify sharp affine factorization as the principal theorem;
- the free-product Kummer theorem should remain visibly restricted to the
  rank-four (q=3) class;
- the novelty claim must remain conditional and must not say "first" or
  "previously unknown";
- the parameter-profile language should not be read as classification of
  bare abstract finite quotients.

These boundaries are already stated in the merged manuscript.

## Final referee classification

- Mathematical core: **PASS / CLOSED**
- Affine sharpness: **PASS / CLOSED**
- Free-product extension: **PASS / CLOSED**
- Heterogeneous parameter application: **PASS / CLOSED**
- Blockwise Kummer application: **PASS / CLOSED within stated class**
- Absolute carrier minimality: **not claimed**
- Publication novelty: **CONDITIONAL / defensible**
- Need for further mathematical repair: **none identified**
