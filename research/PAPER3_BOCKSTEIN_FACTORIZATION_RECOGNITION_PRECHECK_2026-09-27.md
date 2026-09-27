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


## F1 — Upper factorization through W_{p+1}

For the isomorphism-class target (T_\beta(G)=[\beta_G]), the S3 argument is stronger than mere recognition. From (W_{p+1}(G)) one canonically obtains the quotient
[
Q=G/D_{p+1}(G)
]
and hence
[
Q_{\mathrm{ab}}/p^2Q_{\mathrm{ab}}\cong G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}.
]
The mod-(p) character space is canonically
[
H^1(G,\mathbf F_p)=\operatorname{Hom}(G_{\mathrm{ab}},\mathbf F_p),
]
and a character lies in (ker\beta_G) exactly when it lifts to a homomorphism (G\to\mathbf Z/p^2). This liftability relation is determined by (G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}).

Thus (W_{p+1}) determines the subspace (ker\beta_G). In the fixed-rank Demuškin category, (H^1) has fixed dimension (d) and (H^2) fixed dimension (1), so the isomorphism class of the Bockstein map is determined by this kernel (equivalently by its rank). This gives a natural factorization of the isomorphism-class target through (W_{p+1}), not merely an existential recognition implication.

## F2 — Lower factorization obstruction at W_p

S1 and S2 give
[
W_p(G_p)\cong W_p(G_{p^2})
]
while
[
[\beta_{G_p}]\ne[\beta_{G_{p^2}}].
]
Therefore no well-defined target-valued factorization through (W_p) can exist for the isomorphism-class target.

Hence, for the declared target and category,
[
f_{T_\beta}\ge p+1.
]
Together with F1,
[
\boxed{f_{T_\beta}=p+1=r_{T_\beta}}.
]

## Boundary / unresolved issue

This equality is established only for the **isomorphism-class Bockstein target**. If the target is the full Bockstein map with a canonical identification of source/target cohomology spaces, then a stronger naturality/gauge specification is required. The present result does not claim such a coordinate-level factorization.

## Classification

**PASS / CLOSED — factorization threshold equals recognition threshold for the declared isomorphism-class target.**

The hoped-for same-target separation (f_{T_\beta}\ne r_{T_\beta}) is therefore **not obtained** from the current Bockstein example. This is a boundary result, not a failure of the recognition theorem.
