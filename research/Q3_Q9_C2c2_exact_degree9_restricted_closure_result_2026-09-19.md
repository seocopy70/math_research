# C-2c-2 — Exact degree-9 restricted-closure certificate

Date: 2026-09-19

## Status

**PASS — degree-9 baseline restricted closure certificate.**

This closes the pure baseline closure computation for C-2c-2 through degree 9. It does **not** insert S9, does not test H-stability, and does not define D9.

## 1. Exact method

A direct degree-9 tensor-coordinate rank would be unnecessarily large. The same finite-dimensional object can be certified exactly through its restricted universal enveloping algebra.

Let

I = <R2>_res,  R2 = [X1,X2] + [X3,X4],

and let g = L^res / I.

For the associative quotient u(g), the defining relation is

R2 = X1X2 - X2X1 + X3X4 - X4X3.

Choose degree-lex order X1 > X2 > X3 > X4. Its leading word is X1X2. The word X1X2 has no self-overlap, so the single quadratic relation has no critical overlap. Hence the normal words are exactly words avoiding X1X2, giving

Hilb u(g) = 1/(1 - 4t + t^2).

For a graded restricted Lie algebra in characteristic 3, restricted PBW gives

Hilb u(g)
 = product_{n>=1} ((1-t^(3n))/(1-t^n))^{dim g_n}.

Exact coefficient inversion therefore determines every dim g_n through degree 9.

## 2. Dimension certificate

| n | dim L_n | dim L_n^res | dim g_n | dim I_n | restricted increment |
|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 |
| 2 | 6 | 6 | 5 | 1 | 0 |
| 3 | 20 | 24 | 20 | 4 | 0 |
| 4 | 60 | 60 | 45 | 15 | 0 |
| 5 | 204 | 204 | 144 | 60 | 0 |
| 6 | 670 | 676 | 445 | 231 | +1 |
| 7 | 2340 | 2340 | 1440 | 900 | 0 |
| 8 | 8160 | 8160 | 4680 | 3480 | 0 |
| 9 | 29120 | 29144 | 15620 | 13524 | +4 |

The ambient restricted dimensions agree with the project convention:

- L3^res = L3 + L1^[3] = 24
- L6^res = L6 + L2^[3] = 676
- L9^res = L9 + L3^[3] + L1^[9] = 29144

## 3. Relation-layer conclusions

The ordinary relation dimensions are:

- I2^ord = 1
- I3^ord = 4
- I4^ord = 15
- I5^ord = 60
- I6^ord = 230
- I7^ord = 900
- I8^ord = 3480
- I9^ord = 13520

The restricted closure changes these only at degrees 6 and 9:

- degree 6: 230 -> 231, a new +1 dimension;
- degree 7: unchanged;
- degree 8: unchanged;
- degree 9: 13520 -> 13524, a new +4 dimensions.

Thus the exact baseline degree-9 restricted relation space has

**dim I_infty,9 = 13524.**

## 4. Path decomposition

There are only two possible new p-closure sources through degree 9:

1. I2^[3], in degree 6;
2. I3^[3], in degree 9.

The degree-6 p-layer has ambient dimension 6, while the restricted quotient gains only 5 dimensions over the ordinary quotient at degree 6. Therefore exactly one p-direction is absorbed by the relation ideal: the previously directly verified I2^[3] contribution.

Any bracket descendants of I2^[3] at degree 9 are already in the ordinary ideal, because for a restricted Lie algebra

[x^[3],y] = ad(x)^3(y),

and I2 is an ordinary ideal. Therefore they do not create a new degree-9 restricted increment.

At degree 9 the ambient p-layers have dimensions

dim L3^[3] + dim L1^[9] = 20 + 4 = 24.

The restricted quotient gains 20 dimensions over the ordinary quotient (15620 - 15600 = 20), leaving exactly 4 p-directions inside the relation ideal. Since I1=0, the only possible new degree-9 relation p-source is I3^[3]. Hence its contribution is exactly +4.

## 5. Response to the previous critique

### Explicit degree <=5 zero check

The audit now records this directly: there is no new restricted-ideal p contribution in degrees 1–5.

Degree 3 has an ambient p-layer L1^[3], but it contributes no new relation dimension; its bracket with R2 is already in the ordinary relation closure.

### C-2c-2 scope

The gate is now split conceptually into:

1. **closure-interface check:** restricted recursion agrees with the locked ordinary recursion through degree 5;
2. **restricted contribution check:** first new p-closure at degree 6 is +1;
3. **exact degree-9 closure certificate:** I6=231, I7=900, I8=3480, I9=13524, with the only new degree-9 p contribution equal to +4 from I3^[3].

S9 is explicitly outside this baseline closure certificate.

## 6. Scope boundary

Established:

- exact baseline restricted closure through degree 9;
- exact dim I_infty,9 = 13524;
- exact restricted increments: +1 at degree 6 and +4 at degree 9;
- no new restricted relation contribution through degree 5, 7, or 8.

Not established:

- S9 = X1^9 as a restricted-Lie element;
- whether S9 is already in I_infty,9;
- q=9 relation ideal I9,9;
- H-stability;
- D9.

## 7. Reproducibility

Script:
research/Q3_Q9_C2c2_exact_degree9_restricted_closure_2026-09-19.py

GitHub Actions:
35409723512 — success.

The certificate uses exact integer/Fraction arithmetic and exact PBW coefficient inversion; no floating-point rank calculation is used in the degree-9 certificate.
