# POST-PAPER-3 CRITICAL REVIEW OF EXTERNAL LEDGER INTERPRETATION — 2026-10-02

## Scope

This audit critically evaluates the proposed interpretation of the 2026-10-02 external-verification ledger. The proposal is largely sound as a methodological review, but several suggested next steps are stale, too strong, or mis-formulated relative to the current authoritative state.

## 1. O_k categorical interpretation

### Accepted

If objects are pairs (C, omega_C) with omega_C:H^2(Q,F_p)->C annihilating im(tra), and morphisms commute with the obstruction maps, then O_k=H^2(Q,F_p)/im(tra) is initial. The factorization O_k->C is exactly the quotient universal property.

The direct-sum example C=O_k⊕O_k with diagonal obstruction map does refute a terminal-style unique C->O_k statement, provided the proposed category contains that direct-sum object and the two projections as morphisms.

### Required correction

The statement "the category should be changed to admissible carriers" is only a programmatic suggestion, not a theorem. The proposed adjectives separating/gauge-independent/q-blind/presentation-independent do not define a category until:
1. objects are specified;
2. morphisms are specified;
3. composition/identity are specified;
4. admissibility is stable under those morphisms;
5. O_k is shown to be an object if a universal property for O_k is claimed.

Therefore this is not the immediate next research step. It is a possible future categorical formalization.

Classification:
- O_k quotient universal property: PASS/CLOSED.
- terminal uniqueness: FAIL/CLOSED.
- general admissible-carrier category: OPEN, but not currently load-bearing.

## 2. Mixed Fox: the proposed "direct Fox -> chi" next step is stale

The proposal says the next step should be to search for a q-free direct Fox-jet -> chi formula.

This has already been achieved at the declared standard-family local scope in the finite mixed-bridge audit. The Fox equations give A=C=D=1 and B=(1-q)^(-1) modulo the required precision, without inserting chi into the carrier definition. Thus the direct orientation bridge itself is PASS/LOCAL.

What later closed the branch was not failure of the direct bridge. The closure was the category-relative non-redundancy result: after finite-pair descent, the standard-family mixed carrier does not yield a recognition theorem beyond the already established q-regime/Kummer selector at the declared scope.

Therefore the proposal should NOT be used to reopen or extend the Mixed Fox branch.

Classification:
- direct mixed Fox -> chi bridge on standard Demuškin family: PASS/LOCAL.
- Mixed Fox as new recognition carrier: FAIL/CLOSED — REDUNDANT.
- a genuinely new Fox-to-chi theorem outside the closed scope: OPEN, but this would be a new branch, not continuation of the same Mixed Fox gate.

## 3. q-blindness proposal: reject as stated

The suggested definition compares a carrier for E_k with a carrier obtained by replacing q by 0 in the relator. This is not a sound general definition of q-blindness.

Problems:
- q=0 is itself a special Demuškin regime, not a formal "q erased" version of an arbitrary q.
- replacing q by 0 can change the group, admissibility class, extension window, and target.
- a carrier can be q-blind by definition while still producing q-sensitive output through the allowed finite input; definition-independence and output-insensitivity must be separated.
- q-blindness is primarily a restriction on the construction's allowed input, not an assertion that all q-values yield isomorphic carriers.

A better gate is:
"q-blind at input" means q is not supplied as a parameter and no presentation normal form containing q is used in the definition. Then separately test:
(1) input invariance;
(2) whether the resulting carrier separates q-regimes;
(3) whether the orientation bridge factors through q/classification.

If a stronger notion is desired, define it as invariance under a specified equivalence relation on admissible inputs, not by the ad hoc substitution q->0.

Classification:
- proposed q->0 definition: FAIL/CLOSED as a general definition.
- intrinsic q-blind input condition: PASS/LOCAL as a methodological gate.
- formal q-blindness equivalence relation: OPEN.

## 4. Non-standard Demuškin extension

The suggestion to reopen q=0, p=2, and non-standard Demuškin forms is not authorized as the next move.

p=2 is structurally non-adjacent because the classification has additional cases and normal forms. q=0 is already part of the odd-p standard family and is not an omitted case. Reopening these regimes without a new carrier or a new obstruction would violate the current stop boundary.

This can become a future stress-test after a genuinely new finite-input carrier survives the current object/input/functoriality/gauge/orientation/separation gates.

Classification:
- q=0 omission claim: FAIL/CLOSED.
- p=2/non-standard extension as future stress test: OPEN/CONDITIONAL.
- as immediate next task: NOT AUTHORIZED.

## 5. Evidence-type enforcement: accept with one correction

The proposal to require every gate to point to equation, counterexample, literature theorem, or reproducible computation is excellent and consistent with the repository protocol.

But "status label 금지" should not mean removing status labels. The protocol explicitly requires PASS/CLOSED, PASS/LOCAL, FAIL/CLOSED, OPEN, CONDITIONAL, HISTORICAL/SUPERSEDED.

Correct rule:
> A status label may summarize a result only after the underlying evidence type and exact scope are stated; a label can never substitute for evidence.

This is a methodological improvement worth incorporating into future audits.

## 6. The actual next research target

The proposed review does not overturn the current active gate.

The current state remains:
- Paper 3: FROZEN/COMPLETE.
- O_k quotient carrier: PASS/CLOSED; proposed terminal minimality FAIL/CLOSED.
- arbitrary (Q,A)->E descent: FAIL/CLOSED.
- Demuškin restricted pair->extension-window reconstruction: PASS/CLOSED at isomorphism-class scope.
- finite-pair -> Mixed Fox object: PASS/LOCAL.
- Mixed Fox as new recognition carrier: FAIL/CLOSED — REDUNDANT.
- genuinely new finite-input carrier: OPEN.

The correct next attack is therefore not another Fox calculation, not q-blindness by q->0 substitution, and not a p=2 reopening.

The load-bearing search is:
1. identify a genuinely different finite-input carrier;
2. define its exact input before construction;
3. prove intrinsicity/functoriality/gauge independence;
4. establish a direct orientation bridge;
5. test q-blindness at the input-definition level;
6. establish separation and non-redundancy;
7. stop immediately if any structural gate fails.

The earlier discovery-ladder idea of "smallest invisible deformation -> weakest intrinsic rigidity condition -> nearest broader class" remains useful as a meta-strategy, but it should be applied only to a new carrier or to the extension-fiber problem itself, not used to revive Mixed Fox.

## Final classification

- External ledger methodological quality: PASS/LOCAL.
- O_k categorical diagnosis: PASS/LOCAL, with category-definition caveat.
- Proposed admissible-carrier category as an immediate theorem target: OPEN / NOT LOAD-BEARING.
- Direct Fox->chi as next Mixed Fox task: HISTORICAL/SUPERSEDED.
- q->0 definition of q-blindness: FAIL/CLOSED.
- p=2/non-standard Demuškin expansion now: NOT AUTHORIZED / CONDITIONAL future stress test.
- evidence-type gate: PASS/LOCAL.
- genuinely new carrier search: OPEN / LOAD-BEARING.
