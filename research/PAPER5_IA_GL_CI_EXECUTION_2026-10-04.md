# Paper 5 — IA/GL CI execution audit — 2026-10-04

The pre-registered IA/GL decomposition was executed in Ubuntu 24.04 with GAP 4.12.1 and AutPGrp 1.11.

- GAP installation/load: PASS.
- First execution of `paper5_ia_gl_decomposition.g`: IMPLEMENTATION FAILURE at `Group(glperms)`.
- Correction used in the CI rerun: exact `Position(elsV,v)` indexing instead of `PositionSorted`, plus an empty-generator guard.
- Corrected run reached the actual IA/GL computation stage and remained running at the time of this audit.
- No IA-kernel theorem is promoted.
- Existing p^2 localization remains PASS / LOCAL-PREDICTED.
- Quotient action remains OPEN.
- p=5 structural replication remains DEFERRED.

Evidence: GitHub Actions run 37182131149, job 111376644940.

Classification:
- environment: PASS / REPOSITORY
- first script run: IMPLEMENTATION FAILURE
- corrected decomposition: OPEN / REPRODUCTION PENDING
- p^2 IA localization: PASS / LOCAL-PREDICTED
