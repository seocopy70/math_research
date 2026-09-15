# PHASE 2-13C RESULT — TORUS CHARACTER SANITY RECHECK

Date: 2026-09-16
Status: **REOPENED / CHARACTER TABLE INVALIDATED**

## 1. Previous result under review

The previous Phase 2-13C run verified:

- |U^+(F_3)| = 81
- dim E = 35
- dim E^{U^+(F_3)} = 1
- the split torus preserves the unique U^+-fixed line
- exact finite-field inversion/conjugation was used

However, it also printed the table

    (1,1) -> 2
    (1,2) -> 1
    (2,1) -> 1
    (2,2) -> 2

This table cannot be a character of the torus.

## 2. Mathematical sanity check

The split torus is

    T(F_3) = F_3^* x F_3^*

with identity (1,1). Therefore any genuine one-dimensional representation must satisfy

    chi(1,1) = 1.

Also

    (2,2) = (2,1)(1,2),

so multiplicativity requires

    chi(2,2) = chi(2,1) chi(1,2).

The previous values violate both identities:

    chi(1,1) = 2 != 1,

and

    chi(2,1) chi(1,2) = 1 != 2 = chi(2,2).

Therefore the four numerical values are **not certified torus-character data** and must not be used for highest-weight identification.

## 3. What remains valid

The following Phase 2-13B/13C structural results remain separate from the invalid character extraction:

- |U^+(F_3)| = 81
- dim E = 35
- dim E^{U^+(F_3)} = 1
- every tested split torus element is symplectic
- every tested split torus element normalizes U^+
- the unique fixed line is preserved

The existence and torus-stability of the one-dimensional fixed line are therefore retained provisionally, while the scalar character is reopened for exact verification.

## 4. Required next verification

Before Phase 2-14, implement explicit representation-law sanity checks:

1. Verify t(1,1) = I_4 exactly over F_3.
2. Verify rho(t(1,1)) = I_35 exactly.
3. For all t1,t2 in T(F_3), verify

       rho(t1*t2) = rho(t1) rho(t2).

4. Verify directly on the fixed line that

       chi(1,1) = 1.

5. Verify

       chi(2,1) chi(1,2) = chi(2,2).

6. Ensure the fixed-line basis is handled canonically enough that the extracted scalar is an actual eigenvalue, not a basis-dependent ratio artifact.

7. Add hard assertions for the identity and multiplicativity tests. A failure must stop the workflow and mark the character computation invalid.

## 5. Interpretation rule

No torus character, parity pattern, or highest-weight information will be promoted from this phase until all representation-law sanity checks pass.

Phase 2-14 is therefore **BLOCKED** pending this recheck.

## 6. Research-method lesson

This is an example of the project's core safeguard:

    computation -> explicit certificate -> mathematical explanation -> independent sanity check

A basic group-law identity caught an implementation-level inconsistency before the finite-field character data could contaminate the highest-weight analysis.
