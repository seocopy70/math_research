# Rank-2 D4 Lifting Control Result — 2026-09-19

## Status
**PASS / CONTROL CLOSED**

This is a validation experiment for the proposed relator-preservation/lifting pipeline. It is not evidence for a rank-4 theorem.

## 1. Frozen control
The model is G_q^(2)=<x1,x2 | r_q=x1^q[x1,x2]=1>, with p=3.
The first q-sensitive Zassenhaus level is D4: x1^3 has degree 3, while [x1,x2] starts in degree 2.
The computation uses the free pro-3 Magnus expansion modulo augmentation degree >=4, over F3. It does not supply the abstract finite quotient G_q^(2)/D4 as input.
For a selected free-group lift, relator admissibility is checked by degree-2 equality and then degree-3 difference lying in span{[X1,R2],[X2,R2]}, R2=[X1,X2]. The two degree-3 conjugation directions have exact F3-rank 2.

## 2. Tested representatives
Column convention: e_j maps to sum_i g_ij e_i.

| representative | induced matrix | relation to ell=<x1> | q=3 | q=infinity |
|---|---|---|---|---|
| identity | I | preserves | admissible | admissible |
| unipotent | [[1,1],[0,1]] | preserves ell and fixes x1 | admissible | admissible |
| minus identity | -I | preserves ell, but sends x1 to -x1 | not admissible | admissible |
| transvection | [[1,0],[1,1]] | moves ell | not admissible | admissible |

All four q=infinity representatives pass.
For q=3, the tested admissible representatives are exactly the identity and the chosen unipotent that fixes the distinguished vector x1. The line-stabilizing -I fails, so the tested condition is finer than merely stabilizing the line.

## 3. Structural reading of the control
At degree 2, every tested SL2(F3) representative preserves the symplectic commutator class.
At degree 3, q=3 carries the additional restricted-power contribution X1^[3]. The -I representative changes this contribution by the nontrivial scalar -1, while the moving transvection changes its direction. These changes cannot be absorbed by the degree-3 conjugation span. Hence both fail the q=3 relator-preservation test.
For q=infinity, there is no X1^[3] contribution, and all tested SL2 representatives pass.
This gives a concrete low-cost positive/negative control for the lifting mechanism.

## 4. Gate decision
Rank-2 D4 lifting control = PASS / CLOSED
The PASS means only that the frozen n=4 relator-preservation/lifting implementation behaves as independently expected on the selected rank-2 representatives.
It does not establish a complete description of A4(3), equality with a line stabilizer, a rank-4 theorem, q-recovery from weak filtered data, or orientation recovery.

## 5. Execution certificate
Script: research/rank2_lifting_D4_control_2026-09-19.py
Workflow: .github/workflows/rank2-lifting-d4-control.yml
Commit: 4af11b274b630b422e7fef48d9a6dc53281d55fe
GitHub Actions: run 35415080640; job 105822020636; conclusion SUCCESS.
The workflow output verified all frozen assertions over exact F3 arithmetic.