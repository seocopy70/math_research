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
