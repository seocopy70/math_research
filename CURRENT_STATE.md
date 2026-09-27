
## 2026-09-27 — PAPER 3 T_beta FACTORIZATION AUDIT CRITICAL CORRECTION

The T_beta factorization audit was critically reviewed and the record was tightened. The mathematical threshold remains closed, but the earlier audit overstated closure in two places.

Locked target convention:
\[
T_\beta(G)=[\beta_G]
\]
means the **isomorphism class of the linear map** \(\beta_G:H^1(G,\mathbf F_p)\to H^2(G,\mathbf F_p)\), with independent linear isomorphisms on source and target. Only under this convention does rank determine the target in the fixed-rank Demushkin category (\(\dim H^2=1\)). The actual basis-dependent map is not determined by rank.

The lower-bound pair \(G_p,G_{p^2}\) is explicitly locked to the same Paper 3 category and the same unmarked Zassenhaus-window convention; no marked/presentation structure is used in the separation argument.

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

Thus the mathematical equality
\[
\boxed{f_{T_\beta}=r_{T_\beta}=p+1}
\]
is retained under the declared conventions, but no novelty claim is attached to it until the exact literature antecedents are checked.

Detailed audit: research/PAPER3_T_BETA_FACTORIZATION_THRESHOLD_AUDIT_2026-09-27.md (corrected commit 0ac32319db372c8e420173a5c9904ca6227e0649).
