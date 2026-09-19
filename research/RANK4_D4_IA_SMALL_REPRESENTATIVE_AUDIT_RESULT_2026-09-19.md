# Rank-4 D4 IA Small Representative Audit — 2026-09-19

## Status
**PASS / LOCAL**

## CI
- Run: 35416952791
- Commit: 12805fe1a2486a4ba234b2607bf197468cd48a7a
- Workflow: rank4-d4-ia-small-representative

## Scope

This is a controlled representative computation after the full admissible-category covariance audit. It does **not** scan all of GSp_4(F3).

The tested representatives are:
1. identity;
2. -I;
3. the line-fixing transvection e1 -> e1+e2;
4. multiplier-2 diagonal representative diag(2,1,2,1).

For each representative, both first-layer fibre parameterizations
\[
L_c=\phi_c\circ g,\qquad L_c=g\circ\phi_c
\]
were tested.

## Exact results

For every representative and both parameterizations:

\[
\operatorname{rank}(\Delta_{IA})=20,
\]
\[
\operatorname{rank}(C_3+\Delta_{IA})=20,
\]
so
\[
\boxed{\dim Q_3=64-20=44}.
\]

The q=3 and q=infinity IA change maps agree exactly.

All 276 unordered first-layer IA composition pairs have
\[
\boxed{\text{composition failure modulo }C_3=0}.
\]

The q-sensitive base defect survives the quotient for every non-identity representative tested:
\[
\boxed{[\delta_3(g)-\delta_\infty(g)]\ne0\quad\text{in }Q_3}.
\]

The identity case is the expected zero-defect control.

## Interpretation

The controlled representative test is consistent with the quotient datum
\[
Q_3=A_3/(C_3+\Delta_{IA})
\]
being independent of first-layer lift perturbations under both natural fibre parameterizations, while retaining the tested q=3/q=infinity signal.

This is **not** a proof of arbitrary free-group coordinate naturality, nor a full rank-4 theorem. It is a local representative control following the complete admissible-category covariance audit.

## Consequence

The next authorized task is to formulate the quotient-valued defect transformation/composition law on the admissible category, including the GSp multiplier convention, before any broad representative scan.
