# HA61-B5/B6 — Degree-3 Gauge Group and Secondary Affine Action Preflight — 2026-09-20

## Purpose

This record freezes the corrected boundary after the critical audit of HA61-B5. The affine law is an obstruction-preserving compensator law, not yet a proven canonical gauge action.

## Current verified facts

1. The proposed secondary quotient D4/D5 is **FAIL / CLOSED**: g^9 lies in D9 subset D5, while z(g^9)/9 mod 3 can detect f(g), so division by 9 does not descend from D4/D5.
2. The relevant finite information window is the lower-3-central quotient G/P4, with D10 as the corresponding Zassenhaus threshold on the standard comparison family. This is **PASS / LOCAL**, not a universal orientation-recognition theorem.
3. The gamma_2^3 contribution satisfies
   z([g,h]^3)/9 = (lambda wedge f)([g,h]),
   so it supplies no independently detected new functional. Classification: **FAIL / CLOSED as an independent new functional**. Universal gauge absorption remains OPEN.
4. For the cubic relator-gauge source [v,R],
   T_{lambda,f}([v,R]) = -lambda(v)(lambda wedge f)(R).
   On the primary-zero locus this becomes lambda(v) f(p), giving the verified shift of the obstruction by the old p-direction.
5. Consequently the formal obstruction-preserving compensator
   (t2,mu) -> (t2 + a p, mu + a lambda), a=lambda(v),
   is algebraically correct.
6. This does NOT yet prove that an actual allowed presentation/lift/gauge transformation induces that diagonal action on the pair.

## Critical boundary

The following are distinct and must not be conflated:

- an obstruction-preserving compensator;
- an actual gauge-induced transformation of the secondary data;
- a homomorphism/crossed action from the full degree-3 gauge group;
- a canonical affine/torsor quotient.

The current state proves only the first for the audited [v,R] source.

## Next authorized attack

Define, before computation, the actual admissible degree-3 gauge group Gamma_3^gauge including all permitted sources relevant at this stage:

- relator conjugation;
- relation-generator/unit changes, if they act at the relevant order;
- generator IA/lift changes;
- choice of section/lift;
- P3/P4 representative changes;
- V^(2) representative changes.

For each source, determine its induced change on the secondary data. Do not assume that every source is represented by [v,R].

Then verify in order:

1. **Object:** admissible secondary pairs (t2,mu), with V^(2) versus V^(1) typing explicit.
2. **Input:** only declared filtered/relation/coefficient-extension data; no q or chi.
3. **Legitimacy:** actual gauge transformation, not merely an obstruction-preserving compensator.
4. **Composition:** successive gauges induce the same law as the group product; determine whether the scalar a is additive or a crossed 1-cocycle.
5. **Kernel:** compute the subgroup acting trivially on the actual pair.
6. **Orbit:** compute the resulting orbit relation without presupposing a linear quotient.
7. **Canonicality:** test invariance under change of presentation/cover/lift.
8. **Only then:** decide whether the orbit space is an affine torsor, a vector-space quotient, or something else.

## Explicit stop conditions

Stop and classify **OPEN / LOAD-BEARING** if:
- a permitted gauge source produces a transformation not factoring through the diagonal law;
- the scalar a fails to compose additively/crossedly;
- mu's actual gauge law differs from the compensator;
- V^(2) -> V^(1) identification is being used without an explicit canonical Frobenius identification;
- the admissible pair space is not canonically affine.

A surviving independent orbit parameter keeps HA61-B OPEN. No HA61-C/all-digit induction is authorized merely from the formal compensator.

## Current classification

- D4/D5 secondary quotient: FAIL / CLOSED.
- G/P4 and D10 information window: PASS / LOCAL.
- gamma_2^3 independent functional: FAIL / CLOSED.
- cubic [v,R] calculation: PASS / LOCAL.
- raw t2 intrinsicity: FAIL / CLOSED.
- formal shift t2 -> t2+a p: PASS / LOCAL.
- obstruction-preserving mu compensator: PASS / LOCAL.
- actual gauge-induced mu action: OPEN / LOAD-BEARING.
- full degree-3 gauge-group action: OPEN / LOAD-BEARING.
- canonical affine quotient/torsor: OPEN / LOAD-BEARING.
- HA61-B: OPEN / LOAD-BEARING.
- HA61-C: not opened.

This record supersedes any wording that treats the combined affine secondary carrier or its quotient as already canonical.
