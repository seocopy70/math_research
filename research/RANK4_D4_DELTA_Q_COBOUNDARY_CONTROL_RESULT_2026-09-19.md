# A-1 Delta_q coboundary control — RESULT — 2026-09-19

## Execution

- Workflow: rank4-d4-delta-q-coboundary-control
- Run: 35420831517 (run #3)
- Final diagnostic commit: c1ac93d673af3aefb9d1c4e3df139e31f6ab56ec
- Job: 105838085431
- CI conclusion: SUCCESS (the script executed and reported mathematical test outcomes without assertion-crash)

## T1

Result:
- T1 failures: none
- T1 pass: TRUE
- Across all 9 structured representatives, the implemented Delta_q(g) agrees with g.[X1^3]-[X1^3].

This is computational confirmation on the frozen 9-representative family, not by itself a theorem for all admissible g.

## T2

Result:
- X1^3: 0 failures
- X2^3: 0 failures
- X1X2X1: 5 failures
- arbitrary tensor: 5 failures

The failures are an IMPLEMENTATION / MODEL-LEVEL CONTROL FAILURE, not evidence of a non-coboundary component.

Diagnosis: the existing frozen evaluator ev evaluates free-group words in the truncated group algebra. It is not a direct evaluator for an arbitrary homogeneous degree-3 tensor w under a Lie/Magnus substitution Xi -> F_g(Xi). The special object X1^3 is exceptional because in characteristic 3, (1+X1)^3=1+X1^3. A mixed word such as X1 X2 X1 does not have this property: evaluating it as a group word includes lower-degree/group-algebra terms, so comparing that output with the homogeneous tensor action is not the registered T2 test.

Therefore T2, as implemented, is not an admissible independent q-blind control of the intended mathematical statement.

No PASS-NONTRIVIAL conclusion is allowed from T2.

## T3

The strengthened direct vector test passes:
- direct vector failures over all 81 ordered pairs: 0
- expected nonzero composed classes: 60
- observed nonzero composed classes: 60
- count match: TRUE

Thus T3 is fully consistent with the T1 coboundary identity on the structured family.

## Other setup checks

- GSp checks: 9/9
- gauge rank: 20
- Q3 dimension: 44
- candidate composition law failures modulo Q3: 0
- raw failures: 0
- reversed diagnostic failures: 18
- surviving composed classes: 60

## Decision

A-1 is not yet CLOSED as a three-test experiment, because T2 was shown to be an invalid independent control implementation.

However, the execution established an important methodological point: the special X1^3 identity is exactly why the current Delta_q construction can collapse to the linear coboundary, whereas arbitrary homogeneous tensors cannot be tested through the same ev path without first defining a legitimate pure Magnus/Lie substitution.

The next action is not a broader scan. First either:
1. replace T2 with a mathematically legitimate independent control using an explicitly defined homogeneous Magnus/Lie substitution, or
2. close A-1 using the algebraic three-line argument plus T1/T3 as implementation checks, explicitly dropping the invalid T2 rather than retrofitting it.

No broader rank-4 scan is authorized.
