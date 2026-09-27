
## 2026-09-27 — PAPER 3 T_beta FACTORIZATION AUDIT CRITICAL CORRECTION

Critical review of the same-target Bockstein factorization audit identified two boundary conditions that must be explicit.

1. Target convention is locked as the **linear-map isomorphism class**
\[
T_\beta(G)=[\beta_G],\qquad \beta_G:H^1(G,\mathbf F_p)\to H^2(G,\mathbf F_p).
\]
The source and target are allowed independent linear isomorphisms. Only under this convention does rank determine the target when \(\dim H^2=1\). The basis-dependent actual map is not determined by rank.

2. The S1/S2 lower-bound pair \(G_p,G_{p^2}\) is explicitly used under the same Paper 3 fixed odd-p fixed-rank Demushkin category and the same **unmarked Zassenhaus-window** convention. No marked structure or presentation coordinates are part of the window comparison.

The mathematical conclusion survives:
\[
\boxed{f_{T_\beta}=r_{T_\beta}=p+1}.
\]
The threshold equality is mathematically **PASS / CLOSED** under the locked conventions. However, this does **not** close the literature novelty question. The factorization mechanism and related Bockstein/finite-quotient observations may have prior antecedents, so exact novelty remains **OPEN / NOT YET AUDITED**.

Corrected classification:
- target convention: **LOCKED / PASS**
- \(W_{p+1}\Rightarrow G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}\): **PASS / CLOSED**
- \(G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}\Rightarrow[\beta]\): **PASS / CLOSED under target convention**
- \(f_{T_\beta}\le p+1\): **PASS / CLOSED**
- S1/S2 lower-bound pair under Paper 3 conventions: **PASS / CLOSED**
- \(f_{T_\beta}>p\): **PASS / CLOSED**
- \(f_{T_\beta}=p+1\): **PASS / CLOSED**
- same-target T_beta separation: **FAIL / CLOSED**
- novelty of the threshold/equality: **OPEN / NOT YET AUDITED**

Detailed audit: research/PAPER3_T_BETA_FACTORIZATION_THRESHOLD_AUDIT_2026-09-27.md, corrected commit `0ac32319db372c8e420173a5c9904ca6227e0649`.
