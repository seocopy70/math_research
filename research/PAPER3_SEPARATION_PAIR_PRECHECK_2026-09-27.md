# PAPER 3 — SEPARATION PAIR PRE-CHECK: RANK-2 DEMUSHKIN q=p vs q=p^2

Date: 2026-09-27

## Status
**OPEN / LOAD-BEARING**

This note records the first explicit separation-pair attempt after the F1–F4 factorization-vs-recognition audit.

## Candidate pair

For fixed odd p, consider the rank-2 Demushkin-type presentations

G_p = <x1,x2 | x1^p [x1,x2] = 1>

G_p2 = <x1,x2 | x1^(p^2) [x1,x2] = 1>.

Candidate filtration: Zassenhaus p-filtration.
Candidate target: Bockstein beta_G : H^1(G,F_p) -> H^2(G,F_p), or the weaker target Im(beta_G).

## Critical correction before execution

The naive argument

x^p in D_p and x^p not in D_{p+1}
therefore the two presentations first differ at degree p

is **not valid in the quotient Demushkin relation**. In G_p the relation identifies x1^p with [x1,x2]^{-1}, whose leading contribution is degree 2. Free-group p-power degree cannot be transferred directly to the quotient relation without checking the induced filtered relation.

Therefore this naive Step-1 justification is classified **FAIL / CLOSED** and must not be reused.

## Surviving candidate

The window-isomorphism claim

W_p(G_p) ~= W_p(G_p2)

remains **OPEN / LOAD-BEARING**, but must be checked from the actual Zassenhaus/Demuškin filtered structure (or an established q-blindness theorem), not from the naive p-power argument.

The target difference

beta_Gp != beta_Gp2
(or Im(beta_Gp) != Im(beta_Gp2))

is also **OPEN / LOAD-BEARING** and must be computed intrinsically after the window question is settled.

## Correct execution order

S1. Fix the exact meaning of W_p: graded pieces vs truncated filtered quotient vs marked/functorial window.

S2. Verify W_p(G_p) ~= W_p(G_p2).

S3. Independently compute/verify the Bockstein target difference.

S4. If S2 and S3 both pass, conclude only the lower bound r_Tbeta >= p+1 (with the project's threshold convention). Do not claim equality yet.

S5. Treat the upper bound r_Tbeta <= p+1 as a separate theorem.

## Logical boundary

Even a successful Bockstein separation pair does not by itself prove f_T != r_T unless the factorization and recognition thresholds are defined for the **same target T**. Paper 2's affine/orientation factorization threshold cannot simply be compared numerically with r_Tbeta.

## Current classification

- Candidate pair: PASS / LOCAL
- Naive degree-p argument: FAIL / CLOSED
- Window isomorphism: OPEN / LOAD-BEARING
- Bockstein difference: OPEN / LOAD-BEARING
- Recognition lower bound: OPEN
- Exact threshold p+1: OPEN
- Factorization-vs-recognition separation for same T: OPEN / LOAD-BEARING

## Next Gate

Do not start Bockstein computation yet. First fix W_p and test the window isomorphism. If it fails, close this pair and log the negative result.
