# Phase 2-13C Result — 2026-09-16

## Status

**CLOSED / VERIFIED.**

The previous normalization failure was an implementation-level failure, not a mathematical result. The script was corrected to use exact F_3 inversion/conjugation rather than floating-point matrix inversion, and the rerun succeeded.

Latest successful GitHub Actions run: `35016071586`, job `104539707314`, head `33dcaaadbebe281a7b879aeae718b17150e2c4c1`.

## Certified reconstruction

- dim L4 = 60
- dim (R)_4 = 5
- dim Q4 = 55
- generated Sp4(F3) order = 51840
- dim W = 45
- dim U = 10
- dim E = 35
- |U+(F3)| = 81
- dim E^{U+(F3)} = 1

## Coarse torus-normalization certificate

For every split-torus element t(a,b)=diag(a,b,a^{-1},b^{-1}), with a,b in F3^×, the computation verified:

- symplectic = True
- normalizes U+ = True
- fixed-line preserved = True

for (a,b)=(1,1),(1,2),(2,1),(2,2).

Therefore the earlier normalize=False results are definitively classified as implementation errors. The finite-group calculation now directly certifies

t U+ t^{-1} = U+

for every split-torus element in T(F3).

## Torus character of the unique fixed line

Since dim E^{U+}=1, the fixed line is a one-dimensional torus module. The exact finite-field character table is:

(a,b)   lambda
(1,1)   2
(1,2)   1
(2,1)   1
(2,2)   2

Equivalently,
chi(1,1)=2, chi(1,2)=1, chi(2,1)=1, chi(2,2)=2.

The computation certifies that the unique U+(F3)-fixed line is preserved by the split torus and carries the above character.

## Interpretation safeguard

This is a finite-field torus character only. Since F3^× is isomorphic to C2, this detects only sign/parity information. It must not by itself be promoted to a full algebraic highest-weight identification.

## Independent verification record

The successful run also re-executed the preceding Phase 2-1 / Phase 2-3 / Phase 2-13B checks before Phase 2-13C, including:

- dim W = 45
- dim End_H(W) = 2
- rank N = 10
- N^2 = 0
- dim E^{U+} = 1

## Next step

Proceed to Phase 2-14: strengthen the finite-field torus-character information and identify the highest-weight candidate using an extension field / explicit weight-space method. The next stage must distinguish clearly between:

1. computationally observed character data;
2. a mathematically identified highest weight;
3. a final module isomorphism certificate.
