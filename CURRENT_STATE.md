
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

## 2026-09-27 — PAPER 3 SEPARATION AXIS CORRECTION

A structural correction closes a definitional ambiguity in the factorization-vs-recognition program. If both quantities are defined for the same target T by "T factors through W_n" versus "W_n determines T", then they are the same information condition and cannot furnish a genuine numerical separation. Therefore the load-bearing separation problem must use a richer carrier/observation O and a coarser target T=Phi(O): compare f_O with r_T.

Status:
- same-target f_T versus r_T separation: **INVALID / CLOSED — DEFINITIONAL IDENTITY**
- richer-carrier O versus coarser-target T separation: **OPEN / LOAD-BEARING**
- T_beta branch: **CLOSED** as a consistency check, not a separation example
- next authorized gate: candidate carrier/target pair novelty + non-redundancy audit before computation

The finite Kummer/affine orientation carrier versus a coarser target remains the first candidate family, but no target is promoted until its compression map and independent thresholds are explicit.

## 2026-09-27 — CANDIDATE B MOD-27 BOCKSTEIN CARRIER CLOSED

Mathematical and literature audit complete. B_27 is retained as a finite q-layer detector: PASS/LOCAL. As a new non-tautological mod-27 orientation carrier: FAIL/CLOSED.

The full structured carrier is classified into the three valuation classes on the standard family; no independent orientation-sensitive rigidifier has been exhibited; and direct prior-art overlap exists with Bockstein-based Demushkin level constructions and the Kummerian/canonical-orientation framework. The earlier abstract-symmetry no-go is not used because group-realizability was not established.

No further trivial-coefficient Bockstein scan. Next decisive target: intrinsic P_4/D_10 higher power/relation residual and its scalar normalization/transport theorem.
