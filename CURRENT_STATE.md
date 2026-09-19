# CURRENT STATE — 2026-09-19

## Authoritative current question
Can the canonical orientation character chi:G -> Z_3^times be recovered intrinsically from filtered/graded data?

## Authoritative branch
**Rank-4 D4 IA / filtered extension datum.**

## Latest mathematical conclusion — 2026-09-19

The quotient-valued object
Delta_q(g) = [F_g(X_1^3)-X_1^3]_3
is **not a new q-sensitive invariant**.

Indeed, with the frozen convention F_(gh)=F_g o F_h and
F_g(X_1)=g.X_1 + terms of degree >=2,
the degree-3 part satisfies
Delta_q(g) = g.(X_1^3) - X_1^3.

This was independently verified in the structured CI on all 9 representatives after adding the explicit coboundary check:
CI run 35420266538, head bd53311cf45dfc930599c3c24b60df8572c155cc, job 105836490226 — SUCCESS.

Therefore
Delta_q(gh)=Delta_q(g)+g.Delta_q(h)
is the ordinary coboundary identity. Modulo Q3 it represents the zero H^1 class whenever [X_1^3] is viewed as a fixed Q3 vector:
Delta_q(g)=g.[X_1^3]-[X_1^3].

### Consequence

The earlier structured cocycle passes remain valid as **implementation/convention checks only**. They do not constitute evidence for a new q-observable, canonical cocycle, or nontrivial H^1 class.

The broader rank-4 scan proposed after the structured audit is **CANCELLED**. No scan whose only purpose is to re-test this cocycle law is authorized.

## Frozen negative / closed routes

- Original linear-only rank-4 D4 lifting observable: FAIL/CLOSED due to lift-independence failure.
- Preferred Nielsen lifts: permanently prohibited as repair.
- Naive q=9 degree-9 relation space: not H-stable.
- Artificial H-closure of the q=9 relation space: invalid as a presentation relation object.
- Q3/Q9 S9 orbit route: CLOSED at definition level.
- D9-OBS natural p-layer candidate: FAIL/CLOSED as a universal p-layer shadow.
- Quotient-valued Delta_q cocycle: CLOSED as **coboundary / no new information**.

## What remains genuinely open

### Gate A — non-coboundary q-sensitive datum definition

A new candidate must satisfy all of the following before computation:

1. **Definition boundary:** its input may not already contain q=3 versus q=infinity as an explicit label or subtraction.
2. **Non-coboundary test:** it must not reduce to g.v-v for a fixed v in a pre-existing representation.
3. **Intrinsicity:** it must survive allowed IA/lift changes without choosing a preferred lift.
4. **Presentation/coordinate legitimacy:** its definition must be independent of arbitrary free-group coordinates, or the precise quotient/torsor mechanism must be proved.
5. **Nontriviality:** there must be a concrete witness showing the datum is not identically zero or a universal p-layer shadow.
6. **q-separation:** only after the datum is defined from admissible weak data may q=3 and q=infinity be compared.

A candidate failing (1) or (2) is closed immediately; no broad scan is warranted.

### Gate B — relation to the orientation character

The rank-4 D4 condition
g e_1 = mu(g)e_1
was previously used as a candidate admissibility condition, but its connection to the target orientation character chi has not been independently established.

This must be tested as a separate mathematical statement. In particular, do not assume that the line/eigenvector condition recovers chi merely because mu is visible in the ambient GSp action.

## Current authorized work

1. Audit/define a genuinely non-coboundary datum, preferably using the retained filtered/extension structure rather than Delta_q.
2. Independently analyze the exact relation between g e1 = mu(g)e1 and chi.
3. Only after a definition gate passes may a new small CI control be designed.

No unrestricted rank-4 scan is currently authorized.

## Latest implementation result

Structured cocycle audit with explicit coboundary check:
- run: 35420266538
- commit: bd53311cf45dfc930599c3c24b60df8572c155cc
- job: 105836490226
- conclusion: SUCCESS

This verifies the hand derivation against the script; it does not create a new invariant.


## A-1 coboundary control — REGISTERED / EXECUTION PENDING

The pre-registered A-1 control has been added before any broader scan.

Plan: plans/RANK4_D4_DELTA_Q_COBOUNDARY_CONTROL_2026-09-19.md
Script: research/rank4_D4_delta_q_coboundary_control_2026-09-19.py
Workflow: .github/workflows/rank4-d4-delta-q-coboundary-control.yml

T1 directly checks Delta_q(g)=g.[X1^3]-[X1^3] for all 9 structured representatives. T2 uses q-blind controls X2^3, X1X2X1, and a fixed non-monomial degree-3 tensor. T3 compares the 81-pair nonzero quotient-class count with the direct coboundary prediction.

The historical H_adm=1296 enumeration is not reconstructed in this gate because no separately reusable authoritative implementation was found in the frozen structured script; no new enumeration is invented.

No mathematical PASS/FAIL is recorded until CI execution is independently checked.


## A-1 execution result — T1 PASS / T2 CONTROL INVALID / T3 PASS

CI run 35420831517, diagnostic commit c1ac93d673af3aefb9d1c4e3df139e31f6ab56ec, job 105838085431: workflow SUCCESS.

T1: zero failures on all 9 representatives for Delta_q(g)=g.[X1^3]-[X1^3].
T3: zero direct vector failures on all 81 ordered pairs; observed and predicted nonzero class count both 60.

T2 produced 0 failures for X1^3 and X2^3 but 5 failures for X1X2X1 and 5 for the arbitrary tensor. This is classified as a control-model/implementation failure, not a non-coboundary result: the frozen evaluator is a truncated free-group/group-algebra evaluator, not a direct homogeneous Magnus/Lie substitution evaluator. X1^3 is exceptional in characteristic 3 because (1+X1)^3=1+X1^3.

Therefore A-1 is NOT yet closed as a three-test experiment. No broader scan is authorized. Next step is either a legitimate pure Magnus/Lie control definition or closure by the algebraic proof plus T1/T3, with the invalid T2 explicitly removed.
