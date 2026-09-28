# Paper 3 manuscript manifest — 2026-09-28 (current-source verified)

## Authoritative identity
- Main branch commit: `22f821acdbee5a68513272c70056b7f97a559df5`
- Manuscript source: `paper/main.tex`
- Git blob SHA: `599b5d2b19f3e256ab25535a6aebc1beea907fa2`
- Source SHA-256: `b0fef874507e4f2eef249296d5aca83000a954b0c15c2bf0abfc69664de7b0ac`

## CI verification
- Workflow: **Build paper PDF**
- Run: **36367519607**
- Job: **108756783355**
- Result: **PASS / CLOSED**
- Compile, PDF verification, submission-package generation, and all artifact uploads: PASS

## Current PDF
- Artifact ID: **10947718917**
- PDF SHA-256: `2907598169954f6388d764d3596cbe0fad680165c6397a99fcd67efd669b4a6e`
- PDF size: **412,490 bytes**
- Pages: **16**

## Full submission artifact
- Artifact ID: **10948425435**
- Artifact ZIP digest: `sha256:eb11307dcfd02ade4576328d882b713c498cd8a96950667c0d3fd75f3430af1e`
- Internal `SHA256SUMS.txt` independently checked: source and PDF both **OK**

## Independent post-CI PDF audit
- Extracted PDF text: **PASS**
- Main theorem, D2 transgression quotient, D3 finite cup-line, D4 exact selector depth, fixed-scope minimality boundary, and conditional novelty wording all present.
- Forbidden stale manuscript claims checked: no “first in the literature”, no absolute-priority claim, no obsolete application-only framing.
- No stale “minimality remains open” statement was found in the PDF; the remaining OPEN statements concern stronger/absolute carrier questions as intended.

## Final classification
- Mathematical theorem: **PASS / CLOSED**
- Selector threshold (n_{\mathrm{selector}}(k)=3^{k-1}+1): **PASS / CLOSED** at fixed rank-4, (q=3) scope
- 1D cup-line carrier/minimality: **PASS / CLOSED** in the declared linear selector-carrier category
- Stronger canonical functional from (E_k\to Q_k) alone: **OPEN / NOT LOAD-BEARING**
- Publication novelty: **OPEN / CONDITIONAL**
- Manuscript artifact gate: **PASS / CLOSED**

The prior PDF from run 36363508628 is superseded because it was built before the final source repair. This manifest identifies the replacement artifact by exact source commit, source blob, CI run, PDF checksum, and artifact ID.
