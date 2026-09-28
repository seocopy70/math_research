# Paper 1 / Paper 2 / Paper 3 artifact audit — 2026-09-28

## Purpose
Reconcile the publication manuscripts with the authoritative research state after the Paper 3 source/PDF synchronization failure.

## Paper 1
- Manuscript source audited: `paper/main.tex` on `successor-publication-candidate-2026-09-26`.
- Mathematical scope: fixed rank-4, q=3 Demushkin group.
- Main theorem: finite-window Kummer recognition  
  `K_k(Q_k,rho) <=> rho = chi mod 3^k`, k>=2.
- The manuscript explicitly keeps canonical orientation as classical prior art, treats q-blindness correctly, and does not claim minimality of P_{k+1}.
- U1-U5 proof architecture in the audited source matches the frozen theorem boundary: arbitrary-candidate factorization, finite Fox criterion, base-level identification, coefficient-variation/PD^2 uniqueness.
- No stale revival of the superseded H^0/socle shortcut was found in the audited source.
- Classification: **PASS / CLOSED** for the mathematical manuscript at its declared scope; publication novelty remains **CONDITIONAL**.

## Paper 2
- Publication source audited: `paper/successor_main.tex` on `paper2-paper3-merged-2026-09-26`.
- Main theorem: exact affine factorization depth `n_aff(k)=p^{k-1}+1` in the stated crossed-cocycle representation category.
- Rank-two sharpness, finite-depth f-collapse, finite free-product extension, and blockwise q=3 rank-four Kummer application are explicitly scoped.
- Absolute intrinsic-carrier minimality and broader elementary-type uniformity are explicitly not claimed.
- Merged CI run **36215909243** passed compilation, manuscript verification, and PDF upload.
- Classification: **PASS / CLOSED** at the declared manuscript scope; publication novelty remains **CONDITIONAL**.

## Paper 3
- Authoritative source: `paper/main.tex` on `main`, source blob SHA `f37cdbf94140d4a0168419dd8c71868958f0de2e`.
- The latest source repair commit is `dc73b0365be4020545e73ec768dbea5fed889b0e`; the current `main` branch is three documentation-only commits ahead, with no changes to `paper/main.tex`.
- Therefore the prior PDF from CI run **36363508628** (head `3acf4d551f66b21df7ed0528164ef76c690cbc13`) is **not authoritative for the current source**, because that CI head predates the source repair.
- Required gate: rebuild current `main` source in CI, independently verify PDF text/content, then record the new commit/PDF hash/artifact identity before restoring manuscript-finalization CLOSED.
- Mathematical classifications remain unchanged: finite-window recognition PASS/CLOSED; selector threshold PASS/CLOSED at declared scope; one-dimensional cup-line carrier/minimality PASS/CLOSED in the declared linear selector-carrier category; stronger finite-pair canonical functional OPEN/NOT LOAD-BEARING; publication novelty OPEN/CONDITIONAL.

## Process correction
A manuscript may not be called FINAL merely because a previous PDF passed CI. The final identity is the tuple:
**authoritative source commit + source blob(s) + CI PASS on that exact commit + independent PDF/content audit + PDF checksum + recorded artifact manifest**.
