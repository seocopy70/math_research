# Manuscript construction status — 2026-09-25

## Current manuscript

The first publication-style manuscript now exists at:

- `paper/main.tex`
- `paper/references.bib`

The manuscript is deliberately narrower than the research history. It presents the finite-window recognition theorem and keeps the canonical Demuškin orientation as classical prior art.

## What has been transferred from the research project

1. The finite coefficient semidirect-product filtration.
2. Arbitrary-candidate factorization through (Q_k=G/P_{k+1}).
3. The finite Kummer lifting / twisted Fox criterion.
4. Standard-presentation identification
   [
   ho(x_2)=(1-3)^{-1}pmod{3^k}.
   ]
5. Intrinsic uniqueness via coefficient-extension variation, PD² duality, and cup-product nondegeneracy.
6. The assembled theorem
   [
   mathsf K_k(Q_k,ho)iffho=chi_Gmod3^k.
   ]

## What is explicitly not claimed

- discovery of the canonical orientation;
- novelty of the global Kummerian criterion;
- uniformity over all Demuškin parameters (q);
- minimality of (P_{k+1});
- absolute/world-first publication priority.

## Publication-critical verification still required

The manuscript is a **first mathematical draft**, not yet submission-ready. The following are the remaining load-bearing checks:

### A. U1 filtration
Write the lower-3-central recursion explicitly and verify both inclusions
[
P_j(A_ktimes U_1)=3^{j-1}A_ktimes(1+3^jA_k).
]

### B. U3 Kummer/Fox criterion
Replace the compressed Nakayama paragraph with the full finite lifting argument, including:
- the exact relation between generator-value lifting and (H^1)-surjectivity;
- the precise twisted Fox evaluation convention;
- the iterative correction step;
- the converse direction.

### C. U5 variation lemma
Give a complete Yoneda/coefficient-extension proof of
[
delta_{ho_k'}-delta_{ho_k}
=iota_{k-1}circ(
usmile-).
]

### D. U5 PD² lemma
State the exact dualizing module convention and the finite coefficient dual. Verify that the dual of the socle inclusion is the reduction map on (H^0).

### E. Induction
State explicitly why a level-(k) solution reduces to a level-((k-1)) solution, and why the canonical orientation supplies existence at every level.

### F. Literature boundary
Before submission, recheck the exact finite-window statement against additional literature and possible equivalent formulations. The current novelty statement remains conditional.

## Important manuscript rule

Do not turn the research log into the paper. The research log records failed routes, computational audits, superseded arguments, and gate decisions. The paper should contain only the cleaned logical proof chain.

## Current status

- Mathematical theorem: **PASS / CLOSED**
- Manuscript first draft: **OPEN / WORKING**
- Publication-level proof audit: **OPEN**
- Exact publication novelty: **OPEN / STRONG CANDIDATE**
- Minimality: **OPEN**
