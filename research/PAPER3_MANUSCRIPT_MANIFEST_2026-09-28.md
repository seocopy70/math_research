# PAPER 3 MANUSCRIPT MANIFEST — FINALIZATION GATE

Status: **FINALIZATION IN PROGRESS — NOT FINAL**

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

## Artifact record

Pending CI build. Do not infer FINAL from a dated filename.
