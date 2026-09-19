# MINIMAL ENRICHED FILTERED/GRAMMED CARRIER FOR ORIENTATION MOD-9 — 2026-09-19

## Objective

After F5-bare was closed, the next question is not whether the bare associated graded object recovers chi mod 9 (it does not), but:

> What is the weakest natural enrichment of the filtered/graded datum that is sufficient to recover chi mod 9?

No finite scan is authorized.

## 1. Necessary lower bound from the q=3 versus q=infinity obstruction

The bare associated graded restricted Lie object is insufficient because the q=3 and q=infinity Demushkin examples have the same bare graded object but different chi mod 9.

Therefore any successful enriched carrier must retain at least one invariant that distinguishes the degree-3 q=3 contribution from the q=infinity control.

In particular, the carrier must retain not merely the ambient class P_3=X_1^[3], but its coupling to the quadratic relation R_2.

## 2. Candidate minimal enrichment: projective degree-3 relation jet

The natural candidate is the one-dimensional relation line

J_3 = <(R,P)> subset L_2 direct-sum L_3^res,

where:

- R is the degree-2 Demushkin relation;
- P is the degree-3 component of the same filtered defining relation;
- common scaling (R,P) -> c(R,P) is forgotten.

Equivalently, the datum is the projective line [R,P], with nonzero projection to the quadratic relation line.

For the frozen q=3 case:

R = [X_1,X_2]+[X_3,X_4],
P = X_1^[3].

This is strictly richer than the bare graded object and strictly weaker than the full filtered quotient C_3 at the level of explicitly retained relation information.

## 3. Sufficiency calculation

For lambda,f in V^*, define

Theta_J(lambda)(f) = f(P) + (lambda wedge f)(R).

This is invariant under common scaling of (R,P), since scaling multiplies Theta by the same nonzero scalar and therefore does not change its zero set.

For a nondegenerate alternating R, the map

Phi_R: V^* -> V**,
Phi_R(lambda)(f) = (lambda wedge f)(R)

is an isomorphism. Therefore Theta_J(lambda)=0 has a unique solution.

In frozen coordinates,

R=e_1 wedge e_2 + e_3 wedge e_4,
P=e_1^[3],

and the unique solution is

lambda_chi=e_2^*.

Hence the projective relation jet is sufficient for chi mod 9.

## 4. Exact remaining issue: intrinsicness of J_3

The previous F5-marked PASS is conditional: it assumes J_3 is supplied.

The new structural gate must therefore prove one of the following:

A. J_3 is canonically defined from an allowed enriched filtered object, independently of a free presentation;

or

B. an equivalent invariant with exactly the same q=3 versus q=infinity separation and the same Theta zero set can be defined directly.

The following must not be conflated:

- existence of P_3 in the ambient restricted degree-3 space;
- identification of P_3 as part of the same filtered relation as R;
- canonicality of that coupled relation jet.

Only the third item establishes an intrinsic enriched datum.

## 5. Proposed gates

### E1 — Definition

Define the enriched carrier intrinsically as a filtered relation-jet object, not as a chosen relator expansion.

### E2 — Presentation/lift independence

Prove that changing a minimal presentation or free lift induces the natural isomorphism of relation-jet objects and preserves the projective line [R,P].

### E3 — Functoriality

Prove automorphisms/isomorphisms of the enriched filtered object transport J_3 and the zero set of Theta naturally.

### E4 — Separation

Show the carrier distinguishes q=3 from q=infinity. This follows immediately if J_3 contains P_3 nontrivially, while the q=infinity jet has P=0.

### E5 — Recovery

Prove the unique-zero construction recovers lambda_chi and hence chi mod 9.

## 6. Minimality standard

Do NOT claim that J_3 is mathematically minimal merely because it is sufficient.

A defensible minimality statement is only:

> Any carrier sufficient for chi mod 9 in this class must contain information not present in the bare graded object and must distinguish the q=3 and q=infinity filtered relation classes.

The stronger statement that the projective relation jet J_3 is the unique or smallest possible enrichment remains OPEN unless proved.

## 7. Current decision

- Bare graded recovery: FAIL / CLOSED.
- Marked relation-jet recovery: PASS, conditional on J_3 being supplied.
- **New task:** prove intrinsicness of the projective relation jet as an enriched filtered invariant, or replace it with an equivalent canonical extension invariant.

No finite scan is authorized.
