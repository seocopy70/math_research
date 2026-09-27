# PAPER 3 — Gate C result: delta_3 family -> chi mod 27

Date: 2026-09-28
Status: PASS / CLOSED

## Target

Given the full finite family
F = { delta_{3,rho_3} : rho_3 in L(rho_2) },
determine whether it contains a unique distinguished coefficient lift.

## Existence

For the canonical Demushkin orientation chi_3 = chi mod 27, classical Kummerian/1-cyclotomic theory gives the lifting property: every class in H^1(G,Z/9(chi_2)) lifts to H^1(G,Z/27(chi_3)). Equivalently,
delta_{3,chi_3}=0
as a homomorphism.

This is external/classical existence, not the new finite-window claim.

## Uniqueness from the variation formula

Every other lift has the form
rho_3' = rho_3(1+9 nu),
with nu in H^1(G,F_3).

The audited cochain calculation gives
delta_{3,rho_3'}(f) - delta_{3,rho_3}(f)
= nu cup bar(f)
(up to the fixed global sign convention).

Suppose two lifts rho_3 and rho_3' both give the zero connecting map. Then
nu cup bar(f)=0
for every f in H^1(G,Z/9(rho_2)).

Reduction modulo 3 is surjective on H^1 in the audited coefficient extension, so bar(f) ranges over H^1(G,F_3). Hence
nu cup a = 0
for every a in H^1(G,F_3).

The Demushkin cup pairing is nondegenerate. Therefore nu=0, hence rho_3'=rho_3.

Thus the zero connecting map occurs for exactly one lift:
rho_3 = chi_3.

## Important correction to the earlier zero-set discussion

For a fixed f with nonzero bar(f), the zero set across the 81-element lift torsor can indeed be empty or an affine hyperplane of size 27. That does not contradict the present result.

Gate C asks for a lift whose entire connecting homomorphism is zero for every f. The intersection over all f is a singleton because the cup pairing is nondegenerate.

## Intrinsic selector

The finite family therefore carries the canonical selector
rho_3^* = the unique element of L(rho_2) such that delta_{3,rho_3^*}=0 as a map.

By the existence and uniqueness argument,
rho_3^* = chi mod 27.

No presentation coordinate or q value is used in the selector.

## Classification

Gate C = PASS / CLOSED for the fixed rank-four Demushkin category at mod 27.

The combined finite-window recognition statement is now:
W_10(G) -> L(rho_2) -> {delta_{3,rho_3}} -> chi mod 27,
with all arrows intrinsic at the declared scope.

Gate D remains: determine what survives for arbitrary rank/prime and general k, and whether the threshold law generalizes.
