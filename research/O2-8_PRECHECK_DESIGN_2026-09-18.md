# O2-8 PRECHECK — audit of complete H-orbit closure

## Position
O2-7A correctly rejected the naive claim <H.d>=U: the raw q=3 p-power class generates all of W. O2-7B then reported dim <H.N(d)>=9, but that was caused by incomplete orbit closure.

## Purpose
Before interpreting the missing 1D quotient, determine whether the 9D orbit dimension is actually special to the q=3 class d.

## Dependency
Uses only frozen A3-4 artifacts, the verified W action, and N. It does not assume that U/<H.N(d)> has any q-specific meaning.

## Controls
1. The q=3 class d=[X1^[3],X2].
2. Twelve deterministic generic vectors v in W; measure dim <H.N(v)>.
3. Twelve deterministic vectors sampled directly in U=im(N); measure dim <H.u>.
4. Every nonzero column of N as a finite control family.
5. The natural q=3 family ad(X_i)^3(X_j), i != j, where the vector is included only if the authoritative Q4 coordinates embed it into W.

## Primary question
Is dim <H.N(d)>=9 unusually constrained relative to generic/control vectors?

## Interpretation
- If generic/control vectors frequently give 10 while d gives 9, the 9D shadow is evidence of a special position and quotient analysis becomes justified.
- If generic/control vectors also systematically give 9, the 9D phenomenon is likely a generic feature of the U-module and should not be attributed to q=3 without further structure.
- If the q=3 family shows mixed behavior, retain it as an exploratory representation-theoretic pattern; do not infer q-specificity from dimension alone.

## Pass/fail consequence
This is a diagnostic precheck, not a theorem test.
PASS means complete orbit closure is verified and the corrected q=3 shadow has dimension 10.
FAIL means the experiment is invalid or its coordinate/action assumptions break; do not interpret the numerical pattern.

## Required implementation invariant

The H-span routine must close under every currently accumulated basis vector and every generator until no new independent vector appears.

## Critical boundary
Even a positive specialness signal does not prove q=3 vs q=infinity or filtration-intrinsic orientation recovery.
