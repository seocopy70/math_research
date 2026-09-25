# THEOREM ASSEMBLY ATTACK — CORRECTED ZASSENHAUS WINDOW

Date: 2026-09-25

## Purpose

This record authorizes the next proof-audit stage after the independent U1–U5 audit. It is **not** a repetition of the individual U1–U5 audits. The target is the assembled main theorem under the corrected Zassenhaus finite window.

## Controlling finite window

For the actual Zassenhaus filtration,
\[
Q_k = G/P_{3^{k-1}+1}(G).
\]
Any occurrence of \(G/P_{k+1}\) in older research/manuscript text is superseded unless it is explicitly referring to the former lower-3-central formulation.

## Attack target

Audit the complete implication
\[
\mathsf K_k(Q_k,\rho)\Longleftrightarrow \rho=\chi_G\bmod 3^k,
\qquad k\ge2,
\]
for the fixed rank-4, q=3 Demuškin group, without treating the theorem-level PASS as publication-level closure.

## Assembly attack checklist

1. **U1 → U2:** verify that the corrected Zassenhaus calculation really applies to every semidirect target \(A_k\rtimes U_1\), and that killing \(P_{3^{k-1}+1}\) is sufficient for every candidate \(\rho\), not only the canonical candidate.
2. **U2 → U3:** verify that factorization of crossed cocycles through \(Q_k\) is exactly the hypothesis needed for the finite Kummer predicate, with no hidden lift or presentation assumption.
3. **U3 → U4:** verify that the finite Fox criterion is used only as a proof device for identification, that its hypotheses hold for every candidate under consideration, and that no presentation-dependent statement is silently promoted to an intrinsic statement.
4. **U4 → U5:** verify that the standard-presentation calculation supplies only the k=2 base case / canonical branch identification required by the intrinsic induction, and that no all-k coordinate formula is being imported into U5.
5. **U5 internal assembly:** verify the coefficient-extension variation identity, PD^2 socle-map injectivity, cup-product nondegeneracy, and induction indices as one chain; explicitly search for circular use of the canonical orientation or of the Kummerian property being characterized.
6. **Existence vs uniqueness:** keep existence of \(\chi_G\) as classical prior input, while proving uniqueness among arbitrary finite candidates intrinsically. Ensure existence on \(Q_k\) follows from U1–U2 rather than being assumed from the conclusion.
7. **Predicate input boundary:** verify that \(\mathsf K_k(Q_k,\rho)\) contains no hidden q, presentation, relator, dualizing-module, or pre-supplied orientation input.
8. **Depth/index consistency:** audit every occurrence of \(P_{k+1}\), \(P_{3^{k-1}+1}\), and the indexing convention. No mixed filtration notation may survive in the assembled theorem.
9. **Quantifier audit:** check order of \(k\), candidate \(\rho\), lifts, cocycles, and induction hypotheses. In particular, no statement for the canonical branch may be used before the arbitrary-candidate uniqueness step permits it.
10. **Novelty boundary:** distinguish the mathematical theorem from classical global orientation/Kummerian results and from the still-conditional publication novelty claim.

## Expected outputs

- A dependency DAG for U1–U5 and the main theorem.
- A list of every hidden hypothesis discovered.
- Any circular dependency, if present, classified as fatal / repairable / harmless.
- Exact repaired theorem/proof wording where needed.
- Updated research log and current state only after the assembly attack is actually completed.

## Status

**NEXT AUTHORIZED GATE / OPEN — ASSEMBLY ATTACK NOT YET EXECUTED.**

No theorem-level PASS is upgraded merely by this authorization record.
