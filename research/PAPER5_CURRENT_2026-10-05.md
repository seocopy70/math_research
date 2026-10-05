# Paper 5 — Current State (2026-10-05)

## Classification

**OPEN / LOAD-BEARING.**

Paper 5 is currently an automorphism-structure program, not the former compression/trichotomy program.

## What is closed locally

1. For (p=3,n=4), the actual IA kernel has constant order (3^{27}) across the audited split/non-split cases. The observed (3^2) automorphism-order deficit is therefore **not** an IA defect.
2. The deficit is localized to the Frattini/GL image in the audited (p=3,n=4) cases:
   - split (a=1): image order (108), non-split: (6);
   - split (a=2): image order (864), non-split: (48).
3. The corresponding (p=5,n=6) Frattini-image formulas are independently certified for the four audited cases. The fixed-(a) ratios are (2000/20=100) and (48000/480=100), while the IA (5)-primary order is unchanged at the tested level. Thus the (p^2) localization is **PASS / CLOSED as a local p=5 result**.
4. The (p=3,s=2,a=1,n=10) admissible-kernel computation is **PASS / LOCAL**: 81 kernels form one Aut-orbit and each has (3^{10}) complement classes. This does not explain the (p^2) gap.
5. The observed four candidate stabilizer formulas remain **PASS / LOCAL as computational formulas** in the audited p=3,p=5 cases, but the previous general abstract S_11 derivation is superseded by the P5-JET correction audit because it omitted the Jacobson restricted-power terms. The p^2 ratio remains observed locally, not a general theorem.

## What is NOT closed

The key missing theorem is the realization/factorization statement:
[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(W_n/\Phi(W_n)))
=
S_{s,a}
]
(or the correct intrinsic replacement) for general odd (p).

The current relation-jet definition gate is **P5-JET**, followed by the intrinsic-definition gate **FRM-0**. The presentation-level filtered relation module is only **CONDITIONAL**, because an arbitrary automorphism of (W_n) need not lift to the chosen free presentation.

The immediate sub-gates are: (1) close **P5-JET** by deriving S_11 with the Jacobson correction for general odd p; then (2) **FRM-0.2** for the intrinsic W_3 transgression/Bockstein object. No general factorization theorem or uniform (p^2) theorem may be promoted before these gates.

## Superseded/failed routes

- “(p^2) gap comes from IA”: **FAIL / CLOSED / SUPERSEDED**.
- identifying `agAutos` with IA: **FAIL / CLOSED**.
- raw mixed jet ((\pi_2(r),\pi_p(r))) for (r\in D_2\setminus D_3): **FAIL / CLOSED** as an intrinsic definition.
- Hopficity (Rightarrow) lift to the free presentation: **FAIL / CLOSED** as a proof shortcut.
- the old compression/trichotomy formulation: **HISTORICAL / SUPERSEDED** as the main Paper 5 direction.
- the earlier incorrect p=5 stabilizer candidate: **HISTORICAL / SUPERSEDED**.

## Current execution order

1. **P5-JET:** derive the (1,1) S_11 stabilizer from the genuine restricted-Lie/Jacobson model for general odd p.
2. FRM-0.2 (W_3) transgression/Bockstein computation and independent verification.
3. Decide whether an intrinsic Aut((W_n))-equivariant filtered relation jet exists.
4. Prove factorization to the corrected relation-jet stabilizer, or produce a counterexample.
4. Only then pursue a uniform odd-(p) theorem or further prime scans.
5. Quotient-action (\operatorname{Aut}(W)\to\operatorname{Aut}(Q)) remains auxiliary and must not be used to bypass FRM-0.

## Repository anchors

- IA/GL gate: `research/PAPER5_IA_GL_EXECUTION_GATE_2026-10-04.md`
- decisive runtime correction: `research/PAPER5_IA_GL_RUNTIME_CORRECTION_2026-10-04.md`
- IA/GL audit: `research/PAPER5_IA_GL_DECOMPOSITION_AUDIT_2026-10-04.md`
- relation-jet audit: `research/PAPER5_RELATION_JET_AUDIT.md`
- P5-JET correction audit: `research/PAPER5_JET_S11_JACOBSON_CORRECTION_AUDIT_2026-10-05.md`
- filtered relation-module audit: `research/PAPER5_FILTERED_RELATION_MODULE_FACTORIZATION_AUDIT_2026-10-05.md`
- current chronology: `CURRENT_STATE.md` and `research/00_RESEARCH_LOG.md`

**Do not promote the local (p^2) pattern to a uniform theorem.**

**2026-10-05 P5-JET correction:** the numerical S_11 candidates survive locally, but the previous abstract proof is superseded because it treated the restricted-power component too linearly. p=3 independent calculation gives naive stabilizer 48 and corrected Jacobson/ideal stabilizer 6. General odd-p S_11 proof is OPEN / LOAD-BEARING.
