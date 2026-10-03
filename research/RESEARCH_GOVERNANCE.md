# Research Governance — adaptive audit policy

Last reviewed: 2026-10-04

## Purpose

The repository must preserve proof/audit discipline without turning historical audit rules into permanent search restrictions. Governance is a guardrail, not a research timetable.

## Core principles

1. **No artificial time limit.** OPEN problems have no deadline unless the research programme explicitly chooses one for project management.
2. **Audit is evidence, not a cage.** A dated audit can close a claim or route for its stated scope, but it must not prohibit a genuinely new argument that changes the evidence.
3. **Reopening is allowed when justified.** A CLOSED/FAILED route may be revisited when new mathematics, a new invariant, a corrected hypothesis, new literature, or a new computational method materially changes the premises. The new work must cite the old closure and explain what changed.
4. **No “authorized attack” whitelist.** Research is not restricted to a single pre-approved next step. The current load-bearing OPEN problem is the priority, not an exclusive prohibition on exploratory side routes.
5. **Cheap exploration is permitted.** Small calculations, literature checks, counterexample searches, alternative formulations, and exploratory computations may be run without promoting them to load-bearing status.
6. **Separate discovery from certification.** Exploratory results may be LOCAL or provisional. Promotion to CLOSED/PASS requires the normal evidence standard. This separation should increase exploration rather than suppress it.
7. **Do not confuse stale state with policy.** Historical statements such as “do not reopen X” or “stop if Y” are historical decisions unless repeated in this document or CURRENT_STATE with an explicit current scope.
8. **Prefer bounded scope over permanent prohibition.** A route should be marked “closed as a separator under invariant I in scope S” rather than “never reopen.”
9. **Record material changes.** When a new result invalidates an old restriction or upgrades an OPEN item, update CURRENT_STATE and the evidence index; preserve the older audit for provenance.
10. **No premature manuscript pressure.** “Paper FINAL” is a publication state, not a deadline that constrains mathematical exploration.

## Practical status model

- **CLOSED:** established in stated scope.
- **FAILED:** proposed claim/route has a verified counterexample or decisive obstruction in stated scope.
- **OPEN:** unresolved.
- **LOCAL:** exploratory or limited evidence; not yet certification-grade.
- **LOAD-BEARING:** current priority, not an exclusive research permission.
- **HISTORICAL:** retained for provenance.

A route may move CLOSED -> OPEN only with a documented change in premises/evidence. That is not a governance failure; it is normal mathematical progress.

## Current application to Paper 4

The active mathematical target remains
\[
W_{p^s+1}(G_{s,s})\stackrel{?}{\cong}W_{p^s+1}(G_{s,\infty}),\qquad s\ge2.
\]
This is the priority, but exploratory attacks on adjacent invariants are permitted when they are plausibly informative. Previously closed routes should not be repeated mechanically; they may be reopened if the underlying construction or hypothesis changes.

## Anti-stagnation rule

If repeated attacks produce only the same obstruction, change one of:
- invariant;
- category/functor;
- finite-window presentation;
- family/parameterization;
- literature hypothesis;
- computational model.

Do not interpret repeated failure as a reason to impose an indefinite prohibition.

## Record rule

Every materially new result gets a dated audit or log entry. Current state is updated only after the result is checked against the evidence index. Historical audits remain immutable provenance.
