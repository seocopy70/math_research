# Paper 4 — s=3 boundary quotient audit — 2026-10-04

## Scope

Paper 4 remains **FROZEN as a manuscript artifact**, but the freeze is understood as a publication/production freeze caused by the unresolved truncation boundary, not as a prohibition on a bounded mathematical boundary audit. A small, load-bearing breakthrough may justify reopening the manuscript later if it materially strengthens the mathematics.

This audit is a continuation of the existing \\(p,s)=(3,3)\\), \\(n=28\\) local witness, not a reopening of the failed arbitrary-degree theorem, the superseded order-jump argument, or the general E_\\psi branch.

## Existing evidence

The model Schreier calculation establishes
\\[
\\gamma=9(\\sigma-1)^2a_0
=9(a_0-2a_1+a_2)\\neq0
\\]
in the untruncated Schreier abelianization model. Modulo 3,
\\[
(\\sigma-1)^2a_0\\equiv a_0+a_1+a_2=:N_a.
\\]
Thus \\(\\gamma=9N_a\\) at the relevant mod-3 norm-direction level.

The actual finite-window statement still requires control of
\\[
\\operatorname{im}(D_{28}(F)\\cap K\\to K^{ab}).
\\]

## Critical correction to the proposed S3-Gate

The originally proposed map
\\[
\\lambda:K^{ab}\\to C_3,
\\qquad \\lambda(\\gamma)\\neq0,
\\]
is impossible because \\(\\gamma=9N_a\\) and every homomorphism to \\(C_3\\) kills \\(3K^{ab}\\), hence in particular kills \\(9N_a\\).

Therefore the **C3 target formulation is FAIL / CLOSED as stated**. This is a logical correction, not evidence against the transfer-defect mechanism.

The correct one-dimensional quotient must retain the 9-layer. A minimal corrected formulation is
\\[
\\bar\\lambda:
K^{ab}/27K^{ab}\\longrightarrow C_{27},
\\qquad
\\bar\\lambda(N_a)=1,
\\]
so that
\\[
\\bar\\lambda(\\gamma)=\\bar\\lambda(9N_a)=9\\neq0
\\quad\text{in }C_{27}.
\\]

Equivalently, one may work only on the layer
\\[
9K^{ab}/27K^{ab}
\\]
and use its \\(C_3\\)-valued quotient after dividing the layer by the common factor 9. But that C3 functional is **not** a homomorphism defined on all of \\(K^{ab}\\).

## Corrected S3 Gate

The next bounded target is therefore:

1. Construct the norm-direction functional at the 9-layer, equivalently a map \\(K^{ab}/27K^{ab}\\to C_{27}\\) detecting \\(9N_a\\).
2. Compute or prove the image of \\(D_{28}(F)\\cap K\\) under this functional.
3. If the image is zero while \\(\\bar\\lambda(\\gamma)\\neq0\\), the actual \\(W_{28}\\) witness survives.
4. If this fails, classify the obstruction rather than promoting a separator.

This is strictly weaker than proving the full subgroup comparison
\\[
D_{28}(F)\\cap K\\subseteq D_{10}(K),
\\]
and it is also weaker than proving the full
\\[
\\operatorname{im}(D_{28}(F)\\cap K\\to K^{ab})\\subseteq27K^{ab}
\\]
if only the single norm-direction projection is needed.

## Status

- s=3 model Schreier nonvanishing: **PASS / LOCAL**.
- C3 functional on all \\(K^{ab}\\) detecting \\(9N_a\\): **FAIL / CLOSED as stated**.
- Corrected 9-layer / C27 projection gate: **OPEN / LOAD-BEARING**.
- Actual \\(W_{28}\\) separation: **OPEN / LOAD-BEARING**.
- General \\(SC_s\\) and \\(TF_s\\): **OPEN / LOAD-BEARING**.
- Paper 4 manuscript artifact: **PASS / CLOSED — FROZEN**.
- Paper 4 mathematical freeze: **reopenable only through a bounded, load-bearing boundary result; no automatic manuscript reopening**.

## Stop condition

Do not infer an s=3 theorem from the model lattice or from the existence of a formal projection. If the corrected projection cannot be shown to annihilate the actual truncation image, stop and record the obstruction.

