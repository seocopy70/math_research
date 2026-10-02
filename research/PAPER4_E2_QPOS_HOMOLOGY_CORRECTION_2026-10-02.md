# PAPER 4 — E2 q>0 HOMOLOGICAL CARRIER CORRECTION — 2026-10-02

## Critical correction

The previous gate treated q>0 as if the q=0 E2 transgression source H_2(D,Z_p) remained available. That is not correct.

For an infinite Demushkin group with q=p^a>0 and standard odd-p relation
r_D=x_1^{p^a}[x_1,x_2]...[x_{d-1},x_d],
the one-relator Fox/cellular boundary after tensoring with the trivial Z_p-module is the exponent-sum vector
(p^a,0,...,0). Multiplication by p^a on Z_p is injective. Hence
H_2(D,Z_p)=0.
For q=0 the exponent-sum vector is zero and the same calculation gives H_2(D,Z_p)≅Z_p.

Therefore the E2 transgression class
H_2(D,Z_p) -> (N^{ab})_D
that carried the K–Z q=0 depth signal has no nonzero source in q>0.

## Intrinsic abelian extension check

For the stress presentation
G_{s,a}=<z,x_1,...,x_d | z^{p^s}=r_D>,
the abelianized relation is
p^s z=p^a x_1.
The quotient map G_{s,a}->D induces a surjection on H_1. Its kernel contains the free rank-one z-direction; the untwisted five-term sequence now starts with H_2(D,Z_p)=0, so
(N^{ab})_D -> ker(H_1(G)->H_1(D))
is an isomorphism.

The resulting short exact sequence of Z_p-modules
0 -> Z_p -> H_1(G) -> H_1(D) -> 0
is classified on the torsion summand by an Ext^1 class in
Ext^1_Zp(Z/p^a,Z_p) ≅ Z/p^a.
The relation p^s z=p^a x_1 represents the class p^s mod p^a (up to sign/unit convention). Hence for s>=a the abelian homological extension class is already zero and cannot distinguish s>a.

This is stronger than the earlier statement 'abelianization saturates': the entire untwisted H_1/coinvariant extension layer is saturated at q-depth a.

## Consequence

The previous 'q>0 higher filtered E2' target must be split:

- untwisted E2 homological/transgression object: **FAIL / CLOSED for s>a**;
- pure abelianization detector: **FAIL / CLOSED**;
- abelian H_1-extension class: **FAIL / CLOSED for s>a**;
- BBG-type gauge warning: **PASS / LOCAL stress control only**;
- genuinely nonabelian higher relation data: **OPEN / LOAD-BEARING**;
- twisted/dualizing-coefficient replacement: **OPEN / NOT YET DEFINED**, but it is a different object and cannot be called E2 continuation without a new pre-check;
- finite-window factorization of a new nonabelian object: **OPEN**.

## Methodological consequence

Do NOT continue searching for a 'higher filtered truncation of E2' in the untwisted Z_p homology. That route is structurally exhausted for q>0 beyond a.

The only legitimate successor is a genuinely nonabelian relation object (e.g. relation-module/Magnus/Zassenhaus layer) whose definition is intrinsic and whose finite-window factorization is proved. A twisted coefficient construction may be investigated separately, but it must first pass Object/Input/Gauge/q-blindness and must not smuggle the quotient orientation into the input.

## Sources

Demushkin standard q>0 relations and orientation: Labute classification / Souza–Zalesskii 2026.
Pro-p Fox/relation-module calculus: NSW-style relation module and Fox derivative framework.
PD^2 dualizing-module framework: Ben-Bassat–Gropper 2026.
