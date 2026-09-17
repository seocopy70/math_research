# Gate 0-B — q=3 / q=∞ A3-4 structure constructibility

Date: 2026-09-17

## Provenance of the specification

### Confirmed from the repository

1. Gate 0-A has now been independently verified: q=3 and q=∞ have the same degree-2 relation, both produce 45-dimensional `Q4/W45`, and independently constructed 5-generator 45×45 modules admit an invertible intertwiner.
2. The existing A3-4 construction for q=3 uses the degree-3 restricted-power class `X1^[3] = X1^3`, sets `d = [X1^3, X2]`, takes its H-orbit, obtains a 45-dimensional `Wd`, and then constructs the 35-dimensional intersection `I = W45 ∩ Wd` and `K = ker(N)` with the previously verified H-module identifications.
3. The independent Track-B calculation in the repository verifies
   `in_3(s_3) - in_3(s_infty) = X1^[3]` and `[X1^[3],X1]=0`.

### Agreed in prior conversation

1. Gate 0-B must precede any total Ext^1 calculation in A3-4-21.
2. The first question is whether the q=∞ analogues of the q=3 A3-4 objects `d`, `B/A`, and `K` actually exist naturally and are computationally constructible.
3. If the q=∞ analogue does not naturally exist, this is not to be recorded merely as a failed test. It may itself be a q-sensitive signal and must be recorded as such, without overclaiming before the calculation.

### Fixed in this cycle

For the Gate 0-B constructibility test, the q=∞ analogue of the q=3 degree-3 source is defined by the same relation-derived comparison used in the independent Track-B calculation. Thus the q-sensitive degree-3 source is `X1^[3]` for q=3 and `0` for q=∞. The test then asks whether the downstream A3-4 construction can produce the same kind of nonzero 45-dimensional `Wd`, 35-dimensional intersection, and 35-dimensional `K`.

This is deliberately a constructibility gate, not yet an Ext calculation and not yet a claim that nonexistence alone proves a complete q=3/q=∞ classification theorem.

## Gate 0-B checks

1. Independently recompute the q=3/q=∞ degree-3 source difference.
2. Construct `d_3=[X1^3,X2]` and the natural `d_infty=0`.
3. Compute the H-orbit span dimensions of both.
4. For q=3, confirm the existing downstream construction remains 45D/35D/35D and is executable.
5. For q=∞, do not force a 35D analogue by reusing q=3 data. Report whether the natural construction has a nonzero 45D source and hence whether A3-4-style `B/A,K` can be constructed by the same relation-derived mechanism.

## Interpretation rule

- q=3: expected PASS if the independently reconstructed source and existing downstream dimensions agree.
- q=∞: `NO_NATURAL_A3_4_SOURCE` is a meaningful result if the natural source is zero; it is not labelled a software failure.
- Only after this gate is resolved should A3-4-21 Ext^1 calculations be attempted.
