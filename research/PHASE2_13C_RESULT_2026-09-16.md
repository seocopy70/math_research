# Phase 2-13C Result — 2026-09-16

## Status

**FAILED at implementation-level normalization check; no torus-character result is certified yet.**

Latest GitHub Actions run: `35014992864`, job `104536066444`, head `00b5a79c113ab1aa7ff4ed3b63a32ed0f6149e2d`.

The computation successfully reconstructed the earlier certificates:
- dim L4 = 60
- dim (R)_4 = 5
- dim Q4 = 55
- generated Sp4(F3) order = 51840
- dim W = 45
- dim E = 35
- dim E^{U^+(F3)} = 1

For the four split-torus elements, all were verified symplectic and the unique fixed line was preserved. However, the script's explicit subgroup-normalization test returned `False` for the three nonidentity torus elements `(a,b)=(1,2),(2,1),(2,2)`, causing the assertion to fail before the character table was certified.

This is **not** a mathematical conclusion that the torus fails to normalize U+. The failure is in the current implementation/convention check and must be debugged before extracting the character.

## Required next step

Audit the explicit construction of U^+(F3), the C2 basis permutation, torus matrices, and the finite-field inverse/conjugation test. In particular, verify the root subgroup parameterization under conjugation by the torus rather than relying only on the current matrix-membership check. Then rerun Phase 2-13C.

## Interpretation safeguard

Even after a successful finite-field torus-character computation, F3^× has order 2, so the result records only parity/sign information. It must not by itself be promoted to a full algebraic highest-weight identification.
