# C-2c-2 — Restricted closure interface audit result

Date: 2026-09-19

## Status

**PASS — closure-interface preflight only.**

This is not the C-2c-2 definition gate itself. It verifies that the proposed graded restricted-ideal recursion correctly interfaces with the repository's already audited ordinary relation recursion through degree 5, and identifies the first genuinely new restricted contribution.

## 1. Exact ambient checks

Using the standard Lyndon bracketing basis in the tensor algebra over F_3:

- dim L1 = 4
- dim L2 = 6
- dim L3 = 20
- dim L4 = 60
- dim L5 = 204
- dim L6 = 670

Under the project restricted-ambient convention:

- dim L3^res = 20 + 4 = 24
- dim L6^res = 670 + 6 = 676

All ranks were computed by exact F_3 elimination.

## 2. Ordinary relation recursion

With

R2 = [X1,X2] + [X3,X4],

the recursive construction gives:

- dim I2 = 1
- dim I3 = 4
- dim I4 = 15
- dim I5 = 60

These reproduce the locked ordinary relation layers:

(R)_3 = [L1,(R)_2],
(R)_4 = [L1,(R)_3],
(R)_5 = [L1,(R)_4].

The old [L2,R2] shortcut is not used.

## 3. Restricted recursion through degree 5

The audit constructs

I_n = span_i [L_i^res, I_{n-i}]
      + (I_{n/3})^[3] when 3 divides n.

For n=3,4,5, the resulting restricted closure has exactly the same span as the audited ordinary relation layer.

A potentially new degree-3 restricted ambient generator is X_i^[3]. Its bracket with R2 satisfies, in the associative realization,

[X_i^[3],R2] = ad(X_i)^3(R2)
             = [X_i,[X_i,[X_i,R2]]].

Hence these restricted ambient additions introduce no new relation dimension through degree 5.

## 4. First new restricted contribution

At degree 6:

- ordinary bracket closure rank = 230;
- restricted bracket closure rank = 230;
- rank((I2)^[3]) = 1;
- rank(restricted bracket closure + (I2)^[3]) = 231.

Therefore the p-closure term (I2)^[3] is genuinely new at degree 6 and is not redundant.

This is exactly the structural feature that the degree-9 definition must retain: degree 9 cannot be obtained from ordinary relation recursion alone.

## 5. Gate conclusion

### PASS
- The proposed restricted closure recursion is compatible with the locked ordinary recursion through degree 5.
- The first p-closure contribution occurs at degree 6 and is genuinely non-redundant.
- The implementation distinguishes the restricted ambient additions from the ordinary Lie layers.

### NOT YET ESTABLISHED
- full exact restricted closure through degree 9;
- all degree-9 bracket/p-power path redundancies;
- C-2c-2 definition gate as a whole;
- admissibility of S9 = X1^9 as a restricted-Lie source;
- H-stability;
- any D9 definition.

## 6. Reproducibility

Script:
research/Q3_Q9_C2c2_closure_interface_audit_2026-09-19.py

Workflow:
.github/workflows/q3-q9-c2c2-closure-interface-audit.yml

GitHub Actions run:
35409348744 — success.

The initial CI failure was only a missing numpy dependency in the workflow; after adding explicit installation, the same audit completed successfully. No mathematical assertion changed between the two runs.
