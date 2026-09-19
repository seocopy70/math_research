# HARD ATTACK — EXACT Z_3 DEGREE-(2,3) CARRIER AUDIT — 2026-09-19

## Finding

A second theorem-level weak link was found in the claim that a “projective degree-(2,3) relation jet with exact Z_3 coefficients” is a concrete finite-degree carrier for the full orientation.

The fixed-presentation exact crossed-derivation calculation is correct. The problem is the **carrier identification**.

## 1. Characteristic mismatch

The mod-3 object uses the restricted Lie structure

\[
L_3^{res}(V),
\]

which is intrinsically characteristic 3.

There is no literal scalar extension of this restricted-Lie structure to Z_3 that preserves the same p-operation formalism. Therefore notation such as

\[
\langle(R,P_3)\rangle^{proj}_{\mathbf Z_3}
\]

cannot by itself define a mathematically established exact carrier.

The repository already contains this warning in ORIENTATION_EXACT_Z3_COMPRESSED_CARRIER_AUDIT, but the later “fixed-q=3 exact bounded-degree closure” still states the exact pair too literally.

## 2. The real exact object

What is actually established is:

\[
\text{filtered relation/evaluation data over }\mathbf Z_3
\Longrightarrow
\text{exact crossed-derivation equations}
\Longrightarrow
\chi.
\]

What is not established is:

\[
\text{a concrete two-component exact }(R,P_3)\text{ carrier}
\Longrightarrow
\text{those exact equations}.
\]

The exact coefficient-evaluation quotient is a legitimate candidate, but its concrete finite description is explicitly still OPEN.

## 3. Why this matters

The exact equation

\[
1+2\rho(x_2)=0
\]

comes from evaluating the **full defining relation** under a Z_3-valued crossed derivation. It is not obtained merely by replacing the F_3 coefficient field in the mod-3 restricted jet by Z_3.

Thus the statement “degree 3 is enough” is currently true for the **fixed full relation/evaluation mechanism**, but not yet proved as a theorem about an independently defined exact degree-(2,3) carrier.

## 4. Corrected status

- Fixed q=3 full defining relation + exact crossed derivation: **PASS / CLOSED**.
- Mod-3 projective degree-(2,3) carrier -> chi mod 9: **PASS / CLOSED** at the audited scope.
- Concrete exact Z_3 two-component degree-(2,3) carrier -> full chi: **OPEN**.
- Exact coefficient-evaluation quotient -> full chi: **CONDITIONAL / CLOSED only after the evaluation family is independently supplied**.
- Naive Z_3 restricted-Lie scalar extension: **FAIL / CLOSED**.

## 5. Required repair

To promote the exact bounded-degree claim, construct an exact filtered algebraic object independently of the desired orientation evaluation, then prove that the crossed-derivation coefficient maps factor through it and that presentation/gauge changes preserve it.

Until then, “exact degree-(2,3) carrier” must be replaced by “exact filtered relation/evaluation data” in theorem-level prose.

This is a genuine definition gap, not an algebraic error in the recovered value \(-1/2\).
