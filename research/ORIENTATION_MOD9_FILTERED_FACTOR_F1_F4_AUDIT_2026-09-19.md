# ORIENTATION MOD-9 FILTERED FACTOR — F1/F2/F3 HAND AUDIT — 2026-09-19

## Scope

This audit tests whether the twisted mod-9 lifting obstruction can be defined from a canonical finite **filtered quotient** of the group, without choosing a free presentation or preferred free lift.

It does **not** yet prove factorization through the associated graded object alone.

## 1. Intrinsic finite filtered carrier

Let G_1=G and G_n denote the frozen Zassenhaus/p-central filtration used by the project. Put

C_3 := G/G_4.

The quotient C_3 is canonical from the filtered group. Its multiplication and the induced quotients G_i/G_4 are therefore independent of a minimal presentation.

Every candidate first orientation digit is
rho=1+3 lambda mod 9,
lambda in V^*=H^1(G,F_3), V=G/G_2.

Because rho has abelian image, rho factors through V and hence through C_3.

## 2. Intrinsic lifting-obstruction definition

For lambda in V^*, let A_2(lambda)=Z/9 with C_3-action through rho=1+3lambda, and let A_1=F_3 with the induced trivial action.

For f in V^*=H^1(G,F_3), define the lifting obstruction intrinsically as the obstruction to lifting the corresponding first-order cocycle through the short exact coefficient sequence

0 -> 3A_2(lambda) -> A_2(lambda) -> A_1 -> 0

in the category of C_3-cocycles, with the filtered class represented in C_3.

Equivalently, on the canonical filtered quotient, this is the obstruction class of the extension of the twisted derivation problem from F_3 to Z/9. No free generator, Magnus expansion, Nielsen lift, or chosen relator is part of the definition.

The important point is that this is an obstruction **attached to the filtered quotient and coefficient action**, not the ordinary Bockstein: the coefficient action depends on lambda.

## 3. Frozen-coordinate evaluation

When C_3 is presented by the frozen minimal presentation, evaluating the intrinsic obstruction in the generator coordinates gives

B_lambda(f)
 = (1-a_2)f_1 + a_1f_2 - a_4f_3 + a_3f_4.

This agrees with the previously verified group-level twisted H^1 calculation.

Thus the coordinate formula is an evaluation of the intrinsic lifting problem, rather than its definition.

## 4. Presentation/lift independence

A change of minimal presentation induces an isomorphism of the corresponding canonical filtered quotients C_3 and identifies V and the coefficient modules functorially.

Therefore the obstruction zero condition is transported by the induced maps on V^*.

No preferred free lift is required.

**F1: PASS at the filtered-quotient level.**

**F2: PASS at the filtered-quotient level.**

This does not yet imply invariance under arbitrary changes that preserve only the associated graded object.

## 5. Automorphism naturality

Every automorphism of G preserves the Zassenhaus filtration and hence induces an automorphism of C_3. The twisted coefficient module and the cocycle-lifting obstruction are functorial under this induced automorphism.

Therefore the zero set

Z = { lambda in V^* : B_lambda = 0 }

is intrinsic as a subset of the first-character space, up to the natural action.

**F3: PASS at the filtered-quotient level.**

## 6. Uniqueness in frozen coordinates

The condition B_lambda=0 for every f in V is equivalent to the four coefficient equations

a_1=0, a_2=1, a_3=0, a_4=0.

Hence the zero set is the singleton

lambda_chi=(0,1,0,0),

and

rho_chi=(1,4,1,1) mod 9.

**F4: PASS.**

## 7. Critical boundary: associated graded versus filtered quotient

The above construction uses the multiplication/extension data of C_3=G/G_4, not merely the associated graded vector spaces and their brackets.

In particular, the q=3 term x_1^3 lies in the first non-quadratic filtered layer. Its information is invisible if one discards the extension data and keeps only the initial quadratic graded relation.

Therefore the present audit establishes:

- intrinsic recovery from the canonical finite filtered quotient C_3: PASS;
- recovery from the associated graded restricted Lie object alone: NOT ESTABLISHED;
- recovery from the full prescribed filtered/graded package: OPEN until the package is formally defined and shown to contain C_3 (or an equivalent extension datum).

## 8. Decision

The factorization problem is narrowed but not closed.

F1/F2/F3: PASS for the canonical finite filtered quotient formulation.
F4: PASS.
F5: OPEN.

No finite scan is authorized.

The next required task is to formalize exactly what the project means by the allowed filtered/graded datum and prove whether it determines the relevant filtered extension class C_3, or else construct a pair with the same associated graded object but different mod-9 orientation digit.
