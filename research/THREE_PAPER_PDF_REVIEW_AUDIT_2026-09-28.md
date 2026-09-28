# THREE-PAPER PDF REVIEW AUDIT — 2026-09-28

## Scope

An external three-paper review was checked against the exact PDFs previously delivered in this session and against the authoritative manuscript commits used to build them.

### Artifact identities checked

- Paper 1 (affine theorem): workflow run 36212215849, head commit 73001ba0611e4f4aa7db8c733ee01d67542e16eb, PDF /mnt/data/Paper1_FINAL_2026-09-26.pdf, 8 pages, SHA-256 09d67cbb88c647e4b7bb92bb91b2d46fe6b9b2c4b32959b7cebd7e468a554eda.
- Paper 2 (finite-window Kummer recognition): workflow run 36216012111, head commit 0194e01176ae1c21fc70858be3797eeb1a3e7c18, PDF /mnt/data/Paper2_FINAL_2026-09-26.pdf, 13 pages, SHA-256 af14b4b7ab971d8ed2d8cac84daae3ff6422ed389cec92b690cc3e184dde1aee.
- Paper 3 (selector minimality): workflow run 36368630643, head commit 2b4ccb849e93af840ca216b06c06c72a36c84dd8, latest repaired PDF /mnt/data/Paper3_FINAL_2026-09-28_latest.pdf, 17 pages, SHA-256 00a4ee8deba65eb7c08a9b703d3c19b50801ffdde2c13cab0155186c247bb4e3.

## Findings

### 1. Paper 2 alleged page-3 print corruption

FAIL / CLOSED as an objection to the delivered artifact.

The exact delivered Paper 2 PDF was rendered independently at page 3. It is normal LaTeX output containing the continuation of Lemma 2.1 and Lemma 2.2. There is no grid of repeated 1 glyphs and no missing proof block.

Text extraction from page 3 is coherent, and visual rendering confirms normal equations, prose, lemma statement, proof, and page number.

Therefore no recompile is authorized solely on the basis of this allegation. If a different PDF shows the 1 1 1 grid, that file is not the exact artifact identified above and must be identified by filename/hash before diagnosis.

### 2. Paper 1 review items

The supplied review appears to have been written against a different/older manuscript mapping.

The delivered Paper 1 is the affine factorization paper. Its source explicitly contains:
- the finite-depth q-collapse section using parameters p,f,k, with no undefined q variable;
- the relation with the preceding finite-window recognition paper;
- the relevant Zassenhaus references, including Efrat 2014.

Accordingly the proposed q-definition and companion-paper fixes are not missing from this artifact in the form alleged. They should not be applied mechanically.

Classification: PASS / CLOSED at the audited manuscript scope; no source edit authorized from these objections alone.

### 3. Paper 3 alleged x3 -> x2 typo

FAIL / CLOSED as an objection.

The current authoritative paper/main.tex at commit 2b4ccb849e93af840ca216b06c06c72a36c84dd8 contains x_2^{3^e} in the shallow-range argument, consistently with chi_G(x_2). The latest PDF was built from that source. No x3 typo remains.

### 4. Paper 3 C_k / iota / inflation typing

PASS / CLOSED.

The current source explicitly distinguishes:
- C_k subset H^2(Q_k,F_3);
- the coefficient connecting map target H^2(Q_k,A_{k-1}(rho_{k-1}));
- the coefficient inclusion iota_*;
- the inflation of the finite cup-line into H^2(G,F_3);
- the fact that C_k is the finite carrier of the surviving first-order cup variation, not the target of the entire connecting map.

The source also explicitly proves dim C_k=1 and injectivity of inflation by relation-module/cup-product duality.

### 5. Paper 3 O_k / C_k relationship

PASS / CLOSED at manuscript-detail level.

The source introduces O_k as a proof carrier and later states the cup-line as the intrinsic one-dimensional carrier. It explicitly says that O_k is not claimed to be the final one-dimensional carrier and that no canonical functional O_k -> F_3 from E_k -> Q_k alone is claimed. The logical distinction is deliberate rather than omitted.

### 6. Labute Theorem 4

PASS / CLOSED.

The attribution was independently checked in the earlier primary-source audit. The manuscript statement is within the audited scope: Labute's Theorem 4 supplies the relevant existence/uniqueness orientation criterion; the project record already records the verification. No replacement citation is required merely because the theorem number is named.

### 7. Paper 3 Fox coefficient F_1

PASS / CLOSED.

The source displays F_1=(1+a_1+a_1^2)+a_1^3(1-a_2)/(a_1a_2)=(a_1^2+a_1a_2+a_2)/a_2, so the alleged sign/algebra discrepancy is not present.

### 8. Paper 3 commutator Fox formula

PASS / CLOSED mathematically; presentation may be strengthened later.

The displayed formula z([x,y])=((1-b)/(ab))X+((a-1)/(ab))Y is consistent with the stated cocycle and commutator conventions and with the independently checked source derivation. The current appendix gives the inverse-cocycle identity and the resulting formula. Adding every intermediate multiplication step would be a stylistic strengthening, not a correction of a mathematical defect.

## Overall publication status after this audit

- Paper 1: PASS / CLOSED at declared manuscript scope; novelty remains conditional.
- Paper 2: PASS / CLOSED at declared manuscript scope and delivered artifact; the alleged p.3 corruption is not present in the exact artifact.
- Paper 3: PASS / CLOSED at declared mathematical/manuscript scope; the alleged x3 typo and typing omission are already repaired/absent in the current source. Novelty remains conditional.

No mathematical branch is reopened. No PDF rebuild is authorized by this review alone.

## Process note

This audit is evidence that filename-based review can silently become a version/mapping problem. Future three-paper audits must bind each paper to (title, source commit, workflow run, PDF SHA-256) before accepting page-level objections.