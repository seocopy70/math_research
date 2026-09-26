# Paper 3 status — 2026-09-26

## Title
Finite-Window Applications to Free Products of Demuškin Blocks

## Role in the three-paper program
- Paper 1: finite-window Kummer recognition for the fixed rank-four q=3 Demuškin group.
- Paper 2: sharp affine factorization depth n_aff(k)=p^(k-1)+1.
- Paper 3: application of Papers 1–2 to explicit finite free pro-p products of standard Demuškin blocks.

## Current manuscript
- Source: paper3/main.tex
- Initial manuscript commit: 19c3c5e375ef3afaf9c08cfb182a6076aa379dfa
- CI workflow: .github/workflows/paper3-build.yml
- CI run: 36213977187

## Mathematical scope
Closed/supported:
1. Uniform affine factorization through G/P_{p^(k-1)+1}(G).
2. Free-product truncation via the reflector T_n(G)=G/P_n(G).
3. No extra mixed-commutator depth.
4. Finite-depth f-collapse: f>=k becomes invisible in the power relation; f<k remains visible in abelianization.
5. Explicit heterogeneous-block example.
6. Blockwise Kummer recognition for products whose factors are in the already-proved Paper 1 recognition class.

Not claimed:
- absolute minimality of the quotient as an intrinsic carrier;
- the full standard ET_p class;
- a new classification of Demuškin orientations;
- a uniform Kummer selector for arbitrary q or arbitrary Demuškin blocks;
- publication priority for the application formulation.

## Publication status
Mathematical application manuscript: WORKING / PASS pending independent referee audit.
Exact publication novelty: OPEN / CONDITIONAL.
CI build: pending run 36213977187.

## Required next gates
1. Clean CI compile and PDF verification.
2. Independent referee audit of every application theorem, especially H^1 decomposition after finite truncation and the f-collapse statement.
3. Literature/novelty audit against free-product Kummerian results.
4. If no mathematical gap is found, prepare a publication candidate package; otherwise repair only the affected claims.
