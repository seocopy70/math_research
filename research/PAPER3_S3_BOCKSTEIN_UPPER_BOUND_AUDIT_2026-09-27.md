# PAPER 3 — S3 BOCKSTEIN UPPER-BOUND AUDIT — 2026-09-27

## Status at entry

S1 and S2 are already independently closed:
- S1: (W_p(G_p)\cong W_p(G_{p^2})) for the declared unmarked truncated filtered-object definition.
- S2: (eta_{G_p}\not\congeta_{G_{p^2}}) and (operatorname{Im}eta_{G_p}\neoperatorname{Im}eta_{G_{p^2}}).
- Consequently (r_{T_\beta}(\mathcal C;D_\bullet)\ge p+1) is established as a **PASS / LOCAL** lower bound.

## Active gate

**S3: upper bound**
[
r_{T_\beta}(\mathcal C;D_\bullet)\le p+1.
]

The target claim is:
[
W_{p+1}(G)\cong W_{p+1}(H)
\Longrightarrow
\beta_G\cong\beta_H
]
for the explicitly declared fixed-rank Demuškin category.

If proved under the stated category and isomorphism notion, this closes
[
r_{T_\beta}=p+1.
]

## Proposed proof route — NOT YET VALIDATED

1. Identify exactly which (p)-power operation is functorially encoded by the truncated filtered group (W_{p+1}(G)), rather than assuming that the associated graded data alone suffices.
2. Audit whether the Bockstein (eta_G) is intrinsically recoverable from that operation for the entire declared Demuškin category, including basis-free/isomorphism-natural formulation.
3. Use the one-relator/Bockstein formula only as an independent verification of the intrinsic reconstruction, not as a substitute for proving that (W_{p+1}) carries the required information.
4. Verify the implication under arbitrary filtered-object isomorphism (W_{p+1}(G)\cong W_{p+1}(H)).
5. Check the boundary cases (p=2) separately; the current S1/S2 candidate and Bockstein formula were developed for odd (p).

## Critical caution

The sentence “the (p)-power map (D_1/D_2\to D_p/D_{p+1}) is part of (W_{p+1})” must be proved as a **canonical operation of the truncated group/filtration**, not merely inferred from a chosen presentation.

Likewise, “the Demuškin Bockstein is exactly the dual of that (p)-power map” requires a precise natural statement, including the target/source identifications and any dualizing-orientation dependence. A presentation-specific coefficient formula alone does not establish the upper bound.

## S3 proof

Assume (p) is odd and (mathcal C) is the fixed-rank Demuškin category used in S1/S2.

### Lemma 1 — the (p+1) Zassenhaus quotient determines abelianization mod (p^2)

By Lazard's formula
[
D_n(G)=prod_{ip^jge n}gamma_i(G)^{p^j}.
]
For (n=p+1), every factor is either:
- (jge2), hence contained in (G^{p^2}); or
- (j=1) with (ige2), hence contained in ([G,G]); or
- (j=0) with (ige p+1), hence contained in ([G,G]).

Therefore
[
D_{p+1}(G)subseteq G^{p^2}[G,G].
]
Hence, writing (Q=G/D_{p+1}(G)),
[
Q_{mathrm{ab}}/p^2Q_{mathrm{ab}}
cong
G/(G^{p^2}[G,G])
=
G_{mathrm{ab}}/p^2G_{mathrm{ab}}.
]
Thus the underlying group (G/D_{p+1}), and therefore (W_{p+1}(G)), canonically determines the abelianization modulo (p^2).

### Lemma 2 — Bockstein rank is determined by abelianization mod (p^2)

The Bockstein is the connecting map of
[
0	omathbf F_p	omathbf Z/p^2	omathbf F_p	o0.
]
For (chiin H^1(G,mathbf F_p)=operatorname{Hom}_{m cont}(G,mathbf F_p)),
[
eta_G(chi)=0
]
if and only if (chi) lifts to a continuous homomorphism
[
G	omathbf Z/p^2.
]
This liftability depends only on
[
G_{mathrm{ab}}/p^2G_{mathrm{ab}}.
]
Consequently (W_{p+1}(G)) determines (dim_{mathbf F_p}kereta_G), hence (operatorname{rank}eta_G).

### Lemma 3 — in fixed-rank Demuškin category, rank determines the isomorphism class of (eta)

For a fixed rank (d) Demuškin group,
[
dim H^1(G,mathbf F_p)=d,qquad dim H^2(G,mathbf F_p)=1.
]
Two linear maps (mathbf F_p^d	omathbf F_p) are isomorphic under changes of bases in source and target exactly when they have the same rank. Therefore the rank determined in Lemma 2 determines the isomorphism class of the whole Bockstein map (T_eta(G)=eta_G).

### Upper-bound conclusion

If
[
W_{p+1}(G)cong W_{p+1}(H)
]
for fixed-rank Demuškin groups (G,H), then their abelianizations modulo (p^2) are isomorphic, hence
[
operatorname{rank}eta_G=operatorname{rank}eta_H,
]
and therefore
[
eta_Gcongeta_H.
]
Thus
[
oxed{r_{T_eta}(mathcal C;D_ullet)le p+1}.
]

Combined with S1/S2:
[
oxed{r_{T_eta}(mathcal C;D_ullet)=p+1}
]
for the declared fixed-rank Demuškin category and odd prime (p).

### Independent presentation-formula check

For a minimal one-relator presentation with quadratic initial form
[
requiv prod_j x_j^{pa_j}prod_{k<l}[x_k,x_l]^{a_{kl}}
pmod{F_3},
]
the NSW/Labute formula identifies the Bockstein coefficients with the (a_j). For the standard odd-(p) Demuškin relation (x_1^q[x_1,x_2]cdots), the coefficient is (q/pmod p). Hence (q=p) gives rank (1), while (qge p^2) or (q=0) gives rank (0), agreeing with the intrinsic liftability argument. The formula is used here only as an independent check, not as the upper-bound proof.

## Logical boundary

- The proof uses **odd (p)**.
- It uses **fixed rank** so that equal Bockstein rank implies isomorphic maps.
- It proves recognition of the **Bockstein map up to isomorphism**, not a canonical coordinate-level identification.
- It does not prove that (W_p) suffices; S1/S2 supply the matching lower bound.
- It does not establish any general-pro-(p) or (p=2) version.

## Classification

**PASS / CLOSED — S3 upper bound established.**

Therefore the exact threshold is **PASS / CLOSED**:
[
oxed{r_{T_eta}(mathcal C;D_ullet)=p+1}.

## Next verification order

**pre-check → precise truncated-operation definition → literature/formula audit → intrinsic reconstruction lemma → arbitrary-isomorphism implication → independent presentation check → classify → immediately record.**
