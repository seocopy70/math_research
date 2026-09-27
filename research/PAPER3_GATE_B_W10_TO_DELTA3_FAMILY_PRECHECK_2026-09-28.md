# PAPER 3 — Gate B precheck: W_10 -> full delta_3 family

Date: 2026-09-28
Status: OPEN / LOAD-BEARING

## Exact target

After Gate A, the finite input supplies Q_10=G/P_10 and L_10(rho_2) canonically identified with L(rho_2). For each rho_3 in L(rho_2), the target is
delta_{3,rho_3}: H^1(G,Z/9(rho_2)) -> H^2(G,F_3).

The required factorization is stronger than existence of the lift set:
W_10(G) -> {delta_{3,rho_3}}_{rho_3 in L(rho_2)}.

## What U2 gives

For each candidate rho_3, the semidirect-product argument gives finite-depth factorization of the twisted coefficient data. In particular, the coefficient action and twisted H^1 domain can be represented on Q_10.

This closes the domain side. It does not by itself produce the connecting homomorphism.

## What U3 gives

For a fixed minimal one-relator presentation, U3 identifies the lifting predicate with vanishing of a twisted Fox obstruction row. The corrected valuation argument is PASS/CLOSED.

But the Fox row is presentation-level data. U3 therefore gives a realization formula only after a relator/presentation is supplied. It does not by itself prove that the row is a functorial function of the bare filtered object W_10.

## Necessary finite carrier

A successful Gate B proof must construct from W_10 alone a finite target object H_10(W_10), natural maps
O_{rho_3}: H^1(Q_10,Z/9(bar rho_2)) -> H_10(W_10),
and a natural identification H_10(W_10) ~= H^2(G,F_3), or an equivalent target-free formulation, such that the composite equals delta_{3,rho_3} after inflation.

The construction must be independent of presentation, relator representative, free-group lift, coefficient-lift representative, and scalar normalization of H^2.

## Immediate boundary

The finite quotient Q_10 alone does not come equipped with the defining extension 1 -> P_10(G) -> G -> Q_10 -> 1. The connecting map is a cohomology operation of G, while a twisted Fox row is extracted from a chosen presentation of G.

Therefore the naive rule "choose a presentation of Q_10 and run Fox" is not yet legitimate: a presentation of Q_10 need not encode the extension data defining G, and the required value must be shown invariant under all choices.

This is a logical boundary, not yet a counterexample.

## Verdict

Gate B: OPEN / LOAD-BEARING.

Closed subclaims:
- L(rho_2) is finite and W_10-constructible;
- each delta_{3,rho_3} is intrinsically defined once G,rho_2,rho_3 are fixed;
- twisted H^1 factorization through the finite quotient is available;
- the one-relator Fox realization is valid under the minimality hypothesis.

The unresolved theorem is exactly:
finite filtered W_10 -> the full delta_3 family.

## Authorized next attack

Test the strongest plausible intrinsic candidate H_10 = H^2(Q_10,F_3), or its canonical transgression/extension subquotient. Determine whether a natural map from this finite quotient-level obstruction object to H^2(G,F_3) recovers the U3 Fox obstruction for every rho_3.

If this fails, classify the failure precisely: missing extension data, non-injectivity, non-functoriality, or relator-gauge dependence.
