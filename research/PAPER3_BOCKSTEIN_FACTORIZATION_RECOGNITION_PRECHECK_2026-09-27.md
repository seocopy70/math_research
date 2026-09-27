# PAPER 3 — FACTORIZATION vs RECOGNITION FOR BOCKSTEIN — PRECHECK — 2026-09-27

## Motivation

The exact recognition threshold for the Bockstein target is now closed:
[
r_{T_\beta}(\mathcal C_{\mathrm{Dem}};D_\bullet)=p+1
]
for odd (p) and fixed-rank Demuškin groups.

The next load-bearing question is whether the corresponding factorization threshold
[
f_{T_\beta}(\mathcal C_{\mathrm{Dem}};D_\bullet)
]
differs from (r_{T_\beta}).

## Critical distinction

Recognition asks only that
[
W_n(G)\cong W_n(H)\Longrightarrow T(G)\cong T(H).
]

Factorization requires a natural/functorial construction of the target from the truncated filtered object:
[
T \cong \widetilde T_n\circ W_n.
]

Thus (f_T\le r_T) is not automatic. In general factorization is a stronger structural requirement because it must specify the target-valued map, not merely its isomorphism class.

## Pre-check

- **Object:** (T_\beta(G)=[\beta_G]), with explicit choice whether the target is the Bockstein map itself or its isomorphism class.
- **Input:** unmarked truncated filtered object (W_n(G)).
- **Functoriality:** must specify the morphisms/isomorphisms under which the factorization is required.
- **Gauge:** basis changes in (H^1,H^2) must be quotiented if the target is an isomorphism class.
- **Orientation bridge:** Bockstein is defined intrinsically by the coefficient exact sequence; no Demuškin orientation should be inserted into the carrier.
- **q-blindness:** no presentation parameter (q) may be supplied.
- **Separation:** S1/S2 already provide (W_p)-indistinguishability with different Bockstein targets, so (f_{T_\beta}>p).
- **Novelty:** factorization of cohomological data through finite quotients is known in the literature; the potential novelty is specifically whether the *same target* has a factorization threshold strictly different from its recognition threshold.
- **Stop condition:** do not claim (f_T=r_T) merely because (W_{p+1}) recognizes the target. A natural target reconstruction must be constructed and checked.

## Active question

Determine the smallest (n) for which there exists a presentation-independent natural factorization
[
\beta_G \quad\text{or}\quad [\beta_G]
\]
through (W_n(G)), and compare it with
[
r_{T_\beta}=p+1.
]

## Classification

**OPEN — LOAD-BEARING.**

## Execution order

1. Fix the exact target category: full Bockstein map versus isomorphism class.
2. Test whether the intrinsic liftability construction from (G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}) yields a factorization through (W_{p+1}).
3. Test whether a smaller (W_p) can admit any natural factorization.
4. If (f_{T_\beta}=p+1), record equality and determine whether the recognition/factorization distinction remains conceptually useful.
5. If (f_{T_\beta}>p+1), this would give a genuine separation for the same target.
