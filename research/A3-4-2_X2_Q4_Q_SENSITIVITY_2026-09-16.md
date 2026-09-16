# A3-4-2 — X2-bracket detects the q=3 p-power contribution in Q4

## 1. Purpose

This experiment tests the structural correction identified after A3-3:

- bracketing the degree-3 class with X1 kills the restricted-power term because
  [X1^[3], X1] = 0;
- bracketing with X2 should instead expose
  [X1^[3], X2] = ad(X1)^3(X2).

The q=3 and q=infinity representatives are taken from the existing Track B record, in the same Magnus/conjugation convention.

## 2. Existing degree-3 representatives

The repository record gives

s3 = X1^[3] + 2[[X3,X4],X1] + 2[[X3,X4],X2],

sinf = 2[[X3,X4],X1] + 2[[X3,X4],X2].

Hence

s3 - sinf = X1^[3].

This is not reconstructed independently in this experiment; the existing Track B definition is reused so that both classes remain in one convention.

## 3. Restricted-Lie sanity check

The code represents X1^[3] in the degree-3 truncated associative algebra by X1^3. It then checks independently that

[X1^[3],X2] = [X1,[X1,[X1,X2]]].

The assertion passes and the common value is nonzero.

Therefore the p-power contribution is not being treated as an arbitrary monomial: it is exactly the restricted-Lie element prescribed by

ad(X1^[3]) = ad(X1)^3.

## 4. A3-4-2 comparison

Define

d3_x2 = [s3,X2],

dinf_x2 = [sinf,X2].

The calculation verifies exactly

d3_x2 - dinf_x2 = [X1^[3],X2]
                  = [X1,[X1,[X1,X2]]].

The common quadratic relation is

R = [X1,X2] + [X3,X4],

and the same degree-4 quotient

Q4 = L4/(R)_4

used in Phase 2-1 is used here.

## 5. Exact rank certificate

Over F3:

- rank((R)_4) = 5;
- rank((R)_4 + [X1^[3],X2]) = 6.

Therefore

[X1^[3],X2] != 0 in Q4.

Consequently

[s3,X2] != [sinf,X2] in Q4.

The q=3 and q=infinity controls are thus separated in degree 4 by the X2-bracket.

## 6. Interpretation

This establishes detection of the presence of the p-power contribution in the degree-4 quotient. It does NOT establish recovery of the exact numerical parameter q.

In particular, q=3 versus q=infinity can be separated already in this degree window, while q=3 versus q=9 remains a different question: x1^9 first enters the Zassenhaus filtration at degree 9, so degree <=4 cannot distinguish those numerical parameters merely from the defining p-power term.

The result therefore changes the immediate research direction: there is no reason to repeat the X1-bracket as a q-sensitivity probe. The next structural question is whether the nonzero class [X1^[3],X2] has an intrinsic module-theoretic characterization, and separately how the exact q-image can be recovered at degree 9.

## 7. Reproducibility

Script:

`research/phase2_15_A3_4_2_X2_q_sensitivity_2026-09-16.py`

The script imports the previously certified Phase 2-1 Q4/W45 infrastructure rather than rebuilding the quotient with a second convention.

## Status

**Computational certificate established.**

The restricted-Lie sanity check and the Q4 nonvanishing rank test are explicit assertions in the committed script.
