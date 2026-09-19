# Methodology Sufficiency and Missing-Tool Audit — 2026-09-19

## Question

Can the current methodology realistically reach the research target, or are we accumulating calculations without the structural tools needed to connect them to intrinsic cyclotomic orientation?

## Executive conclusion

The methodology is **sufficient for a sharply bounded theorem program**, but **not yet sufficient for the stronger claim of an intrinsic minimal carrier** unless three missing structural bridges are supplied.

The current positive results are real:
- bare quadratic/associated-graded data does not recover chi mod 9;
- the projective degree-(2,3) relation carrier recovers chi mod 9;
- for fixed q=3 with exact Z_3 coefficients, the degree-(2,3) filtered relation/evaluation carrier recovers the full chi;
- a compatible finite-level tower gives the inverse-limit character.

The danger is therefore no longer "we have no method." The danger is **continuing to compute objects whose only established property is higher-order structure, without a functorial map to the orientation-recovery functional**.

## What the literature shows about process, not only results

### Pál–Quick

Their q=3 A_3-formality result proceeds through a canonical higher cohomological object (Benson–Krause–Schwede canonical class), then an explicit lifting computation (including Dwyer U_4(F_3)), and finally a cohomological obstruction. The important methodological pattern is:

canonical object -> functorial obstruction -> explicit computation.

Our relation-jet work currently has the reverse risk:

explicit filtered object -> successful calculation -> seek the intrinsic/canonical interpretation.

This is the main methodological asymmetry.

### Blumer–Quadrelli

Their near-Demuškin examples use group/orientation properties and subgroup/cohomological tests to distinguish structures even when the quadratic graded shadow is similar. Methodologically this reinforces that a useful invariant must be defined at the level of an intrinsic structure, not merely a convenient presentation coordinate.

## Three missing structural tools

### M1. A genuinely intrinsic carrier functor

We need a definition of the degree-(2,3) carrier from the filtered group/augmentation-relation data itself:

G -> J_3(G)

with:
- no chosen Nielsen/free-group lift;
- no inserted q;
- explicit behavior under isomorphisms;
- a precise projective/gauge quotient.

The existing E1-E3 audit is strong evidence at the recovery-functional level, but the theorem should expose the construction as an object/functor, not only as a zero-set calculation.

### M2. The orientation bridge must be a theorem, not a recognition

We currently have the exact crossed-derivation characterization and the recovered value (1-q)^(-1). The missing theorem-level statement is a natural factorization

J_n(G) -> admissible coefficient-evaluation data -> Hom(G,(Z/3^n)^times)

whose unique solution is the canonical cyclotomic orientation.

The critical point is to prove that the coefficient-evaluation family is independently specified. If it is defined as "whatever recovers chi", the construction is tautological.

### M3. A comparison map to an independent higher invariant

Pál–Quick gives a natural independent target: the A_3/Hochschild canonical class. We do not need equality. A map, factorization, or rigorous obstruction to a map would tell us whether our relation jet is detecting the same q-sensitive information through a genuinely different route.

This is a cross-check, not a substitute for M1/M2.

## What we do NOT need

The literature does not justify:
- a broader W/U/O scan;
- a larger rank-4 representative scan;
- more degree-9 brute force;
- a new q-family computation without a pre-defined observable.

Those activities are methodologically unjustified until they produce one of M1-M3.

## Anti-time-waste protocol

Every future branch must pass these gates before computation:

1. **Object test:** What exact intrinsic object is being constructed?
2. **Input test:** What information is allowed? What is explicitly excluded?
3. **Functoriality test:** What maps induce maps of the candidate object?
4. **Gauge test:** Which lift/presentation changes are quotiented, and why?
5. **Orientation test:** Where is the precise map to the crossed-derivation/orientation functional?
6. **q-blindness test:** Is q absent from the definition?
7. **Separating test:** Can q=3 and q=infinity be separated without using q in the definition?
8. **Novelty test:** Does the construction prove something not already implied by the standard Demuškin orientation theorem?
9. **Stop test:** If the branch fails any of 1-5, stop computation and return to definitions.

## Immediate authorized program

### A. Finish the degree-(2,3) theorem chain

Formalize M1 and M2 at the exact level already supported by the audits. No new scan.

### B. Define the carrier category precisely

Retain the proven mod-3 coarsest carrier result ([R], p(P)) as a relative/universal statement in its explicitly defined linear-evaluation category. Do not call it absolute minimality.

### C. Treat the IA branch as subordinate

The IA/filtered-extension candidate is not a main result merely because local equivariance and basepoint audits pass. It becomes worth continuing only if its 44-dimensional quotient can be mapped naturally to the existing orientation-recovery carrier or to M1/M2.

Otherwise it is a separate structural curiosity and should be frozen.

### D. Then perform the Pál–Quick comparison

Construct a precise candidate map/factorization to the A_3 canonical class, or prove a structural obstruction to such a map. Do not claim identity.

## Decision rule

The research is **not currently in a "blind computation" state** because the relation-jet branch has a proven orientation link. However, the IA/W/U/O branches can become blind-computation traps unless every new calculation is required to feed M1, M2, or M3.

The strongest near-term deliverable is therefore not another scan. It is a theorem package establishing:

intrinsic filtered input -> coarsest defensible carrier -> natural coefficient functional -> unique finite-level orientation -> inverse limit,

with the literature comparison as an independent validation layer.
