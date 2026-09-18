# Q3/Q∞ — Independent-definition gate for d∞
# Date: 2026-09-18

## Global position

Q3-2A-R structural census is complete for the authoritative q=3 object d3 and its H-orbit. The observed size-40 vector/projective orbit is not promoted to a q-detector. The zero-case convention J(0)=1 is pre-registered, but its mathematical status is explicitly treated as a convention to be audited, not as evidence for q-distinction.

The next task is therefore **definition before computation**:

\[
\boxed{\text{define }d_\infty\text{ independently, then derive }N(d_\infty).}
\]

No Q3/Q∞ comparison is permitted before this gate is frozen.

## Purpose

Construct a mathematically justified q=∞ input object without choosing it to force separation from q=3, and specify exactly how the existing map N is applied afterward.

The goal is not yet to compare orbit sizes. The goal is to establish that the two sides of the later comparison are independently and reproducibly defined.

## Dependencies

Frozen inputs:

- Current research map: `RESEARCH_MAP.md`.
- Mathematical/computational conventions: `research/03_CONVENTIONS_AND_IMPLEMENTATION.md`.
- Q3 zero-case pre-registration: `research/Q3_QINF_zero_case_prereg_2026-09-18.md`.
- Q3-2A-R robustness audit: Actions run `35345371915`, head `ded57a8dd0605f48db2b04f7b7718fff40ffdc6f`.
- The q=3 local object and N construction must be taken from the already-authoritative pipeline, not reconstructed ad hoc for the comparison.

## Independence criteria for d∞

Before any numerical calculation, the q=∞ definition must satisfy all of the following.

1. **Mathematical source is fixed first.**
   The definition must come from the q=∞ group/presentation or the corresponding local graded construction, not from the observed value of J(N(d3)).

2. **No target-value selection.**
   The choice of representative, normalization, basis, or local model may not depend on whether it makes N(d∞) equal to 0, nonzero, or a desired orbit size.

3. **No Q3 representative cloning.**
   A q=∞ object may not be defined merely by taking d3 and deleting/changing a term because that produces the desired comparison. Any relation between the two objects must be derived from the underlying mathematical definitions.

4. **Local data are explicit.**
   The protocol must state exactly which local/graded input determines d∞, including the presentation/relation and the degree/multidegree in which the object lives.

5. **N is fixed before evaluation.**
   Once d∞ is defined, apply the already-authoritative N without modifying its formula, basis convention, H-action, or normalization for the q=∞ case.

6. **Zero is a derived outcome, not an input.**
   If the independent construction gives d∞=0 or N(d∞)=0, record that as a mathematical consequence. It must not be imposed to obtain separation.

7. **Same invariant on both sides.**
   After N(d∞) is derived, use the pre-registered vector-orbit invariant
   \[
   J(v)=|H_U\cdot v|
   \]
   for both q=3 and q=∞, with J(0)=1 only as the already-fixed vector-orbit convention.

8. **Convention audit.**
   Before interpreting a zero/nonzero result, explicitly check whether J(0)=1 is a natural consequence of the linear H-action or merely an auxiliary convention. If it is merely conventional, the final interpretation must say so and must not claim that the numerical value itself is a canonical extension of the projective invariant.

## Required mathematical derivation

The first deliverable is a short derivation of:

\[
d_\infty := \text{(independently defined q=∞ local/graded object)}
\]

followed by

\[
N(d_\infty)
\]

using the fixed N.

The derivation must identify:

- the underlying q=∞ presentation/local model;
- the exact degree and multidegree of d∞;
- why that object is the appropriate q=∞ counterpart of d3;
- whether d∞ is zero before N is applied;
- if nonzero, its explicit coordinates;
- the exact route from the mathematical definition to the computed vector.

## No execution gate

Do **not** create or run Q3/Q∞-2 yet.

Execution becomes admissible only after this document is amended or superseded by a mathematically explicit d∞ definition satisfying the independence criteria above.

## Decision consequences

### DEFINITION ACCEPTED

The q=∞ object is mathematically specified independently, its derivation is reproducible, and no post-hoc target selection is involved.

Then proceed to the smallest possible computation:

\[
N(d_\infty)\quad\text{and}\quad J(N(d_3)),J(N(d_\infty)).
\]

### DEFINITION REJECTED / INSUFFICIENT

If d∞ is selected by reference to the observed q=3 orbit/invariant, or if its mathematical source cannot be stated unambiguously, do not run the comparison. Repair the definition first.

### INVALID TEST

If a later computation mixes coordinate systems, uses a stale N/action, changes normalization between q=3 and q=∞, or silently substitutes a zero case, discard the computation as invalid rather than interpreting it mathematically.

## Current status

The q=3 size-40 stability observation is recorded as:

> **H-EQUIVALENT STABILITY OBSERVED (inside H·d3; no q-claim).**

The q=∞ object remains **OPEN**. No q=3 versus q=∞ conclusion has been drawn.
