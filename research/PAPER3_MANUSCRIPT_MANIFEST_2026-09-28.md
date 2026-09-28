# Paper 3 manuscript manifest — 2026-09-28 (current-source verified)

## Authoritative identity
- Manuscript source: `paper/main.tex`
- Source commit used by CI: `ac53cc2e753fc7b8fb0eb4b78a0085ccfdbc5a89`
- Git blob SHA: `3f0bc48ac532d0ed72bcfe876a8283bed178dfbc`
- Source SHA-256: `bc951dce61717ed184e8763118a3ffef310615b09b95b8fd6ae7ca0a83e42a49`

## CI verification
- Workflow: **Build paper PDF**
- Run: **36374270475**
- Job: **108776775979**
- Result: **PASS / CLOSED**
- Compile manuscript: PASS
- PDF verification: PASS
- Submission-package generation: PASS
- PDF/source/full artifact uploads: PASS

## Current PDF
- Artifact ID: **10950077812**
- PDF SHA-256: `d38c63bd1b453482217c7876d818ff7b50e48cbde7f219552953d8a5e36d56c0`
- PDF size: **415,064 bytes**
- Pages: **17**

## Full submission artifact
- Artifact ID: **10950097816**
- Artifact digest: `sha256:4e0ebd4041e31287d3fde877baec52511e164454a2b4b51f156cb996a9115344`
- Internal `SHA256SUMS.txt`: source and PDF both **OK**

## Source artifact
- Artifact ID: **10949833169**
- Internal source SHA-256: `bc951dce61717ed184e8763118a3ffef310615b09b95b8fd6ae7ca0a83e42a49`
- Extracted-source Git blob recomputation: `3f0bc48ac532d0ed72bcfe876a8283bed178dfbc`

## Independent post-CI PDF audit
- Extracted PDF text: **PASS**
- Visual checks of title/abstract, Lemma 5.3, selector domain/D4, and C_k boundary: **PASS**
- Predicate notation consistently uses `\\mathsf K_k`; auxiliary kernel is (J_k).
- `\\mathcal O_k` material is absent.
- `\\mathcal D_{k,m}` and `\\mathsf K_{k,m}` are present, with the shallow-domain exclusion stated.
- Carrier wording is category-relative.
- No stale minimality-open or absolute-priority claim remains.
- Failed run **36373920812** was a LaTeX macro error (`\\mathscr`); corrected to `\\mathcal`. Exact-source run **36374270475** then passed.

## Final classification
- Mathematical theorem: **PASS / CLOSED**
- Selector threshold: **PASS / CLOSED** at fixed rank-4, (q=3) scope
- 1D cup-line carrier/minimality: **PASS / CLOSED** in the declared linear selector-carrier category
- Stronger canonical finite-pair functional: **OPEN / NOT LOAD-BEARING**
- Publication novelty: **OPEN / CONDITIONAL**
- Manuscript artifact gate: **PASS / CLOSED**

This manifest supersedes the previous manifest identity. The authoritative publication artifact is the exact PDF produced from source commit `ac53cc2e753fc7b8fb0eb4b78a0085ccfdbc5a89`.
