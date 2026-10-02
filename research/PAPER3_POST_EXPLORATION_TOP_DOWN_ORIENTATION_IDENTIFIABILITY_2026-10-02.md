# TOP-DOWN RESEARCH REFRAME: ORIENTATION IDENTIFIABILITY BEFORE CARRIER SEARCH — 2026-10-02

## 0. Motivation

The post-Paper-3 search has repeatedly approached the problem bottom-up:
finite window -> candidate carrier -> orientation.

This audit proposes a genuinely different direction:
orientation -> finite observability condition -> coarsest sufficient information -> intrinsic realization.

The carrier is no longer the primary unknown. The first unknown is whether the target orientation is identifiable from the declared finite input at all.

## 1. Core inverse problem

Let C_k be the admissible class of oriented filtered pro-p groups, let W_k be the declared finite input/window, and let
chi_k(G)=chi_G mod p^k.

Define the observational equivalence induced by the finite input:
G ~_{W_k} H iff W_k(G) is isomorphic to W_k(H) in the declared input category.

The decisive top-down question is:

  Is chi_k constant on every W_k-equivalence class?

Equivalently, does there exist a well-defined map
  Chi_k : Im(W_k) -> Or_k
such that
  chi_k = Chi_k o W_k ?

If not, then NO carrier constructed solely from W_k can recover chi_k. This is a structural impossibility theorem, independent of carrier design.

If yes, carrier search becomes a secondary realization problem: find an intrinsic finite object C_k obtained from W_k through which Chi_k factors, and determine the coarsest useful realization.

## 2. Why this is different from the old O_k route

This is not the tautological claim that a quotient has a universal property.

The target chi_k is fixed first, and the question is whether it descends through W_k. The negative case gives a genuine no-go:
same finite input + different orientation.

The positive case gives a factorization problem whose object is constrained by a pre-existing target natural transformation.

The carrier is therefore derived from a target-observation problem rather than invented and then tested for usefulness.

## 3. Three top-down gates

### T0 — Identifiability

Search for or prove:
  W_k(G) ≅ W_k(H) but chi_k(G) != chi_k(H).

If such a pair exists:
  FAIL/CLOSED — finite-window orientation identifiability fails at k.

If no such pair can exist and a proof is obtained:
  PASS/CLOSED — chi_k is identifiable from W_k.

This is the decisive gate.

### T1 — Coarsest sufficient information

Assuming T0 passes, define the target kernel on finite inputs:
  w ~_chi w' iff Chi_k(w)=Chi_k(w').

The quotient by this equivalence is the mathematically forced coarsest observable partition for the target.

This quotient is not yet a publishable carrier theorem because it is defined using chi. It is a specification/benchmark, not the final construction.

The research question becomes:
  Can this target-defined quotient be realized without using chi in the construction?

### T2 — Intrinsic realization

Search for an algebraic realization of the T1 quotient using only permitted finite input:
  cohomology, transgression, relation modules, extension classes, deformation spaces, or another intrinsic finite construction.

A successful realization is a genuinely meaningful carrier because its definition is independent of the target it ultimately recovers.

## 4. A stronger dual viewpoint

Instead of constructing C -> chi, start with the natural orientation functional itself.

Ask for the smallest finite level at which every admissible orientation-valued natural transformation is determined by the declared input.

This reframes the threshold as an observability depth:
  d_obs(chi; W) = min{k : chi_k factors through W_k}.

The existing sharp threshold p^{k-1}+1 then becomes not merely a carrier threshold but a candidate theorem about the observability depth of orientation.

This must not be asserted as new mathematics yet: the precise category, target functor, and monotonicity must first be defined.

## 5. A potentially stronger obstruction

The most valuable negative theorem would be:

  There exist G,H in the admissible class with
  W_k(G) ≅ W_k(H)
  but
  chi_G mod p^k != chi_H mod p^k.

This would immediately imply that every carrier C_k functorially constructed only from W_k is incapable of orientation recognition.

This is stronger than showing one proposed carrier fails.

Conversely, if such a counterexample cannot exist because a structural theorem forces orientation rigidity, that theorem itself may be the real result.

## 6. Top-down source of candidate carriers

Only after T0/T1 should one ask what realizes the target quotient.

Possible realizations are not a search list but consequences to test:
- a transgression/extension-class quotient;
- a dual relation-module functional;
- a deformation-theoretic tangent/obstruction quotient;
- a universal coefficient functional;
- a finite representation of the orientation character;
- a derived/cohomological object.

Mixed Fox is then interpreted as one attempted realization, not the object of research.

## 7. Relation to existing branches

This reframing does NOT reopen:
- O_k universal minimality;
- Mixed Fox new-carrier branch;
- q=N_k;
- W_{11}/W_{12};
- Paper 2 reproof;
- p=2 as an immediate target.

The previous results become inputs:
- broad same-pair extension counterexample = evidence that W_k may fail to determine E_k in broad categories;
- Demuškin pair->extension reconstruction = evidence that restricted classes may have rigidity;
- Mixed Fox direct bridge = an example of a realization attempt;
- Mixed Fox redundancy = evidence that a realization can be mathematically valid but fail the novelty/coarseness target.

## 8. Immediate authorized experiment

Do NOT construct a new carrier first.

For the smallest nontrivial target, formulate the finite-input identifiability problem explicitly:

  I_k(C) := { chi_k(G) : G in C, W_k(G) ≅ W }

for a fixed finite window W.

Then ask whether |I_k(C)| can exceed 1.

The first target should be the smallest admissible class enlargement beyond the already rigid standard Demuškin family, because within a class where pair->extension reconstruction is already known, identifiability is partly inherited.

A useful outcome matrix is:

1. |I_k(C)|=1 and proof exists:
   orientation-identifiable; proceed to realization.
2. |I_k(C)|>1 by explicit pair:
   FAIL/CLOSED; no W_k-only carrier can work on C.
3. finite computation suggests singleton but no proof:
   OPEN; do not construct carrier yet.
4. singleton only after adding extra input:
   identify exactly which extra input restores identifiability; this becomes the candidate carrier specification.

## 9. New conceptual target

The research target is therefore shifted from

  "Find a new carrier"

to

  "Determine the finite observability class of orientation."

The desired theorem, if it exists, would have the form:

  finite input W_k determines orientation mod p^k
  iff [intrinsic rigidity condition].

Only after this theorem would a carrier be sought as an algebraic realization of the resulting observable quotient.

## Classification

- top-down identifiability reframing: OPEN / LOAD-BEARING;
- orientation-as-target-first inverse formulation: PASS / LOCAL as a research framework;
- coarsest target quotient: CONDITIONAL / specification, not yet a theorem;
- finite observability depth d_obs: OPEN / definition to formalize;
- new carrier construction before identifiability: NOT AUTHORIZED.

## Stop condition

If a same-W_k/different-chi counterexample is found in the intended generalized class, stop carrier construction for that class immediately and classify the class boundary. If identifiability is proved, only then spend effort on intrinsic carrier realization.
