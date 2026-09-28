# PAPER 3 MANUSCRIPT MANIFEST — FINALIZATION GATE

Status: **FINAL / CLOSED**

This manifest is the publication synchronization contract for the theorem-paper
manuscript at \`paper/main.tex\`. A PDF is not FINAL unless the source commit,
CI result, PDF content audit, checksum, and this manifest are mutually
consistent.

## Load-bearing research → manuscript map

| Research result | Authoritative source | Manuscript location | Required status |
|---|---|---|---|
| D1: exact arbitrary-candidate finite factorization through \(Q_k=G/P_{3^{k-1}+1}\) | \`research/THEOREM_ASSEMBLY_ATTACK_RESULT_2026-09-25.md\` | §2, Lemmas U1–U2 | PASS / CLOSED |
| Base \(k=2\) selector | authoritative research log / Paper 3 base audit | §4 | PASS / CLOSED |
| U5 reduction + coefficient variation + \(PD^2\) socle injection + uniqueness | \`research/THEOREM_ASSEMBLY_ATTACK_RESULT_2026-09-25.md\` and current state | §5 | PASS / CLOSED |
| Finite-window recognition theorem | current authoritative state | §6 | PASS / CLOSED |
| Intrinsic finite cup line \(C_k\), \(\dim C_k=1\) | \`research/PAPER3_FINITE_CUP_LINE_COMPRESSION_2026-09-28.md\` | §7 | PASS / CLOSED |
| Selector minimality \(n_{\mathrm{selector}}(k)=3^{k-1}+1\), fixed rank-4 \(q=3\) | \`research/PAPER3_FINAL_FRONTIER_AUDIT_2026-09-28.md\` | §8 | PASS / CLOSED |
| Canonical functional from \(E_k\to Q_k\) alone | same frontier audit | Scope/boundary sections | OPEN / NOT LOAD-BEARING |
| Publication novelty | same frontier audit | §9–§10 | OPEN / CONDITIONAL |

## Stale-claim rejection

The final source must not claim:
- selector minimality is OPEN;
- the one-dimensional cup line is unproved;
- the manuscript is merely an applications/synthesis paper;
- absolute publication priority;
- injectivity of the full \(H^2(Q_k,\mathbf F_3)\to H^2(G,\mathbf F_3)\).

## Finalization sequence

1. Source-level line audit complete.
2. Clean LaTeX compile PASS.
3. CI verification PASS, including positive and stale-claim-negative markers.
4. PDF text/content audit PASS against this manifest.
5. Artifact ID + PDF SHA-256 + source commit captured.
6. Immediate update of \`CURRENT_STATE.md\`, \`RESEARCH_MAP.md\`, and \`research/00_RESEARCH_LOG.md\`.
7. Only then status changes from NOT FINAL to FINAL.

## Final artifact record

- Manuscript source path: \`paper/main.tex\`
- Main-branch manuscript blob SHA: \`c82e6c5277dd7aa21d3bc4ab9d5490d25cf6c694\`
- CI validation commit: \`3acf4d551f66b21df7ed0528164ef76c690cbc13\`
- CI workflow: **Build paper PDF**, run **36363508628**, conclusion **success**
- Independent shell-pipeline audit: run **36363508467**, conclusion **success**
- Citation hygiene: run **36363508580**, conclusion **success**
- PDF artifact ID: **10946925073**
- Full submission artifact ID: **10945849160**
- PDF SHA-256: \`813fda4840783c3b37002828ccfbe092ccffed6ad189f46430222e5e930a56b0\`
- Submission source SHA-256: \`759476d1003fe2d106cfeae5d82f12f8d866afabfddbdd4a3d063cc0d90e7af0\`
- PDF: **14 pages**, **405,622 bytes**
- PDF content audit: **PASS** — extracted text contains the finite-window theorem, D3 cup-line, D4 selector depth, conditional novelty boundary, and no stale application-only/minimality-open wording.
- Artifact identity is the CI commit plus checksum; the dated filename alone is not authoritative.

Finalization sequence completed:
1. source-level audit;
2. compile-failure diagnosis and repair;
3. CI compile + PDF verification;
4. independent PDF extraction/content audit;
5. artifact checksum capture;
6. immediate research-state synchronization.

The temporary validation PR #5 was closed without merge after its CI validation completed.
