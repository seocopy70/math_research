# Open Problems and Next Steps

## A. Primary-source literature verification

1. Verify the canonical orientation theorem directly from the primary literature.
2. Determine exactly what level of Zassenhaus data can or cannot recover orientation information.
3. Read the recent pro-3, \(q=3\), Demuškin higher-structure/formality work and compare its obstruction with the present degree-4 calculation.

## B. Degree-4 module structure

Given the computed 45-dimensional \(Sp_4(\mathbb F_3)\)-module \(W\), determine:

\[
\operatorname{soc}(W),
\qquad
\operatorname{rad}(W),
\qquad
W/\operatorname{rad}(W),
\]

and its composition factors and extension structure.

The previous result

\[
W^{Sp_4(\mathbb F_3)}=0,
\qquad
W_{Sp_4(\mathbb F_3)}=0
\]

must be retained as a constraint, not interpreted as failure of the overall research program.

## C. Group-level interpretation

Make the passage from the free-Lie calculation to the relevant Zassenhaus quotient completely explicit, including all hypotheses used from mildness/Demuškin theory.

## D. Orientation reconstruction

Investigate whether the following implication can hold in any precise sense:

\[
\text{full filtered structure}
\Longrightarrow
\chi_G:G\to\mathbb Z_3^\times.
\]

If the associated graded mod-3 object is insufficient, identify the smallest additional datum that restores the missing 3-adic information.

## E. Higher operations

Test whether \(T\) can be identified with or related to a higher cohomological operation, Massey product, \(A_\infty\)-multiplication, or another obstruction appearing in the pro-3 Demuškin literature.

## F. Novelty control

No statement should be promoted to “new theorem” until a primary-source search has ruled out an existing equivalent formulation. Computations should remain clearly separated from externally established facts.


## 2026-09-27 — HA58/P4/D10 audit update

The HA58/P4/D10 route is now fully audited. The following are no longer open questions in their original form:

- canonical single-vector \(t_2\) realization: **COUNTEREXAMPLE**
- \(t_2/\langle p\rangle\) as a scalar obstruction carrier: **COUNTEREXAMPLE**
- diagonal \((t_2,\mu)\) quotient as the repair: **COUNTEREXAMPLE**

The finite-depth source classification is also settled at the audited D_4/mod-27 depth: \(F^9\) and the old \(\gamma_2^3\) sector are the surviving source types; \(\gamma_3^3\) and \(\gamma_4\) do not survive the /9 mod-3 normalization.

The remaining load-bearing questions are therefore narrower:

1. **Intrinsic definition:** Can the surviving secondary obstruction family be defined as a canonical function-valued/affine object without choosing a relation representative?
2. **Transport:** What is the exact functorial category in which
   \[
   \rho_3\mapsto\delta_{3,\rho_3}
   \]
   transports naturally?
3. **Compression:** Does that family admit a richer affine/torsor-valued carrier preserving coefficient-lift dependence?
4. **Recognition:** Can a coarser target \(\chi\bmod 27\) factor through such a richer carrier even though the single-vector \(t_2\) route fails?
5. **Finite-depth orientation:** Can the higher connecting family be linked to the already established mod-9 obstruction by an intrinsic coefficient-extension diagram?

Do not reopen the single-vector P_4/\(t_2\) route unless a new mathematical mechanism avoids the conjugation counterexample.


## 2026-09-27 — HA58 NEXT GATE REFINED AFTER SECOND CRITICAL REVIEW

The surviving δ_3 family is scope-locked as follows:
- cohomological definition/naturality: PROVED;
- nonemptiness for the known canonical ρ_2: EXTERNAL;
- finite filtered factorization W_n → {δ_{3,ρ_3}}: OPEN;
- orientation reconstruction from the family: OPEN.

The q=3 rank-four t_2 conjugation witness is a genuine COUNTEREXAMPLE to a universal canonical single-vector claim; no general statement about the q=9 or 27|q coordinate formula is inferred.

The full-torsor zero-selector uniqueness mechanism is COUNTEREXAMPLE / CLOSED in rank 4. The variation formula, filtered existence, and a canonical one-dimensional lift restriction remain OPEN.

Do not treat “torsor-valued carrier” as an established object. It is a candidate compression strategy. Do not reopen the single-vector P_4/t_2 route.


## 2026-09-27 — HA58 OPEN-PROBLEM SCOPE CORRECTION #3

- δ_3 lift-family cohomological definition/naturality: PROVED at fixed (G,ρ_2) cohomological-object level.
- Intrinsic variation formula under ρ_3↦ρ_3(1+9ν): OPEN.
- Fixed-f 27-fold zero-set consequence: PROVED CONDITIONALLY on the variation formula and rank-four Demuškin cup structure.
- Unconditional singleton zero-selector failure: OPEN unless an independent counterexample is supplied.
- Mod-9 projective degree-(2,3) recovery is already audited at PASS/CLOSED level; do not reopen it merely to manufacture a Gate A.
- Remaining load-bearing gates: finite filtered access to L(ρ_2), finite factorization to the δ_3 family, and χ mod 27 reconstruction/compression.
