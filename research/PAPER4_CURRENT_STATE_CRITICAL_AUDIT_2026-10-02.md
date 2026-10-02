# PAPER 4 CURRENT STATE CRITICAL AUDIT — 2026-10-02

## Decision

Paper 4 is now classified as **OPEN / LOAD-BEARING** at the filtered-extension/generalization stage.

The current research has moved from exploratory carrier search to a structural bottleneck: **does graph-sensitive information survive after the ordinary degree-2 commutator sector is separated/quotiented, in a way that is intrinsic, q-blind, and presentation-independent?**

## What is genuinely established

1. The Grassmannian/special-plane carrier is **FAIL / CLOSED** by the complete 3-vertex counterexample. It must not be reopened.
2. The raw finite central extension
   \[
   1\to A_n=D_n/D_{n+1}\to W_{n+1}\to W_n\to1
   \]
   is a genuine filtered object. The claim that its defect factors through abelianization is **FAIL / CLOSED — FALSE CLAIM**.
3. RP-5 gives a same-abelianization separating pair: two four-vertex specially oriented graphs have isomorphic abelianizations but first-q cross-extension defect ranks 1 and 2. Thus graph-sensitivity criterion B is **PASS / LOCAL**.
4. The literature convention correction is controlling: a special edge (v,w) has ordinary origin v, special terminus w, and wvw^{-1}=v^{1+q}; the q-torsion sector is the origin sector O, not the sinkhole/special sector S. Any origin-to-sinkhole bridge remains a separate theorem.
5. The q-blind adjacent-window Bockstein carrier is **PASS / LOCAL** as a target-relative recognition carrier, but it does not recover full orientation or directed incidence.

## Critical correction to the present strategy

The next gate is not simply “define a canonical quotient W_2^{ord} and hope the defect survives.” That quotient is itself a theorem-bearing construction.

The required gate has four logically separate tests:

### A. Ordinary-sector extraction

Construct an intrinsic degree-2 ordinary relation/commutator sector from the finite window, without presentation labels. Prove exactly what is being quotiented and why it captures all ordinary contamination relevant to the q-defect.

### B. Signal survival

Define the induced q-layer extension defect after quotienting/separating the ordinary sector. The decisive test is whether its image is nonzero and still distinguishes the RP-5 pair. If every admissible quotient kills the rank-1/rank-2 distinction, the present carrier family is a structural no-go.

### C. Intrinsicity and gauge

Show that the quotient, induced defect, and any cross-pairing are invariant under filtered-window isomorphism and lift changes. “Canonical” is not to be used before this is proved.

### D. Generality

After the RP-5 pair survives, test at least:
- 2-generator special edge;
- common-sink with commuting origins;
- noncommuting ordinary-origin sector;
- complete graph;
- a graph with mixed ordinary and special edges.

Only then is an arbitrary-graph incidence statement justified.

## Three possible outcomes

- **PASS / LOCAL:** a nonzero q-defect survives the ordinary-sector separation and still separates explicit same-abelianization pairs, but arbitrary incidence is not yet reconstructed.
- **FAIL / CLOSED:** the natural quotient destroys all graph-sensitive q-information, or the only surviving construction is presentation-dependent/re-encoding.
- **OPEN:** a precise intrinsic quotient/defect exists but survival/generalization remains unresolved.

## Current probability language

No numerical “success probability” is justified. Structurally, RP-5 raises confidence that filtered extension data contain graph information, but it does **not** establish that this information survives a canonical ordinary-sector quotient. That survival question is the decisive unknown.

## Next authorized mathematical target

Do **not** perform a large graph scan. First formalize the ordinary-sector quotient and derive its induced extension class algebraically in the smallest noncommuting-origin model. Then test the same construction on the RP-5 pair. The branch is won or lost at the survival step before any full incidence reconstruction is attempted.

## Paper 4 scope

Paper 4 is the name for this post-Paper-3 generalization research program. Paper 3 remains frozen and unaffected by any failure in Paper 4.
