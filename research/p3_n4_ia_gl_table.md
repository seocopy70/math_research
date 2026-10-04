# Paper 5 — p=3, n=4 IA/GL + Aut(W)→Aut(Q) invariant table

Status: **OPEN / ACTIVE**  
Purpose: pre-registered diagnostic table for localizing the reported p^2 automorphism-order gap.  
Classification rule: orbit data are **PASS / LOCAL** until source artifacts are committed and independently reproduced.

## Scope

For each admissible-kernel Aut(W)-orbit representative W, record:
1. V=W/Phi(W)
2. L=Im(Aut(W)→GL(V))
3. IA(W)=ker(Aut(W)→GL(V))
4. v3(|IA(W)|), v3(|L|), v3(|Aut(W)|)
5. image/kernel of Aut(W)→Aut(Q)
6. whether pi(z)∈Phi(Q)
7. orbit stabilizer
8. layer tags: GL / IA-SHEAR / QA / STAB

## Orbit table

| Orbit | Representative | dim V | |L| | |IA(W)| | v3(|L|) | v3(|IA|) | v3(|Aut(W)|) | Im Aut(W)→Aut(Q) | Ker Aut(W)→Aut(Q) | pi(z)∈Phi(Q)? | Stabilizer | Layer tag |
|---|---|---:|---:|---:|---:|---:|---:|---|---|---|---:|---|
| O1 | TBD | | | | | | | | | | | |
| O2 | TBD | | | | | | | | | | | | |
| O3 | TBD | | | | | | | | | | | | |
| O4 | TBD | | | | | | | | | | | | |

## Mandatory consistency checks

For every representative:
- v3(|Aut(W)|) = v3(|IA(W)|) + v3(|L|).
- The computed quotient map must be induced by the characteristic quotient fixed by repository governance, not by an ad hoc quotient.
- pi(z)∈Phi(Q) must be checked on the actual reported kernel/realization representative; do not replace it by a generic generating-set heuristic.
- Stabilizer data must use the actual Aut(W)-action on the admissible-kernel realization set. Do not infer stabilizer size from orbit size unless the acting group size is independently certified.

## Interpretation rule

The 9+9+54 decomposition is an **orbit-side invariant**. It is a detector, not itself an automorphism-filtration layer.

The p^2 automorphism-order gap is to be localized independently among:
- **GL**: the linear image L;
- **IA-SHEAR**: IA(W) or its relevant filtration;
- **QA**: image/kernel of Aut(W)→Aut(Q);
- **STAB**: stabilizer contribution when comparing realization orbits.

Do not claim that the orbit decomposition is caused by one of these layers until the calculation establishes the connection.

## Current reported evidence

- p=3,s=1,a=1: 72 admissible kernels, orbit sizes 9+9+54, all reported non-split.
- p=3,s=1,a=2: 9 admissible kernels, one reported orbit, non-split.
- p=3,s=2,a=1,n=10: 81 admissible kernels, one reported Aut(W_10)-orbit; reported |Aut(W_10)|=2·3^30, |K|=3^9, and 3^10 complements/kernel.
- p=5,n=6: reported Aut orders show the p^2 p-primary gap between the relevant split/non-split cases.

These remain **PASS / LOCAL** pending repository reproduction.

## Execution order

1. Complete p=3,n=4 IA/GL decomposition.
2. Localize the p^2 gap.
3. Promote the resulting local statement to a p=3,n=4 structural lemma/theorem if justified.
4. Cross-prime check at p=5,n=6.
5. Analyze the n=10 single-orbit and 3^10-complement phenomena as downstream structural tests.

## GAP interface note

The authoritative external interface has now been recovered at `research/external/paper5_aut/aut_common.g`, with the companion `aut3.g` and `p5aut.g` runners and their logs. The IA/GL decomposition audit is therefore bound to the actual recovered AutPGrp interface rather than invented function names or quotient conventions.

Executable follow-up: `research/scripts/paper5_ia_gl_decomposition.g`.

The table remains OPEN until that script is independently rerun and the four p=3,n=4 decompositions are certified.
