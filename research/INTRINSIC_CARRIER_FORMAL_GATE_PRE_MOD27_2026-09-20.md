# INTRINSIC CARRIER FORMAL GATE — PRE-MOD27 — 2026-09-20

## Purpose

Before any search for a mod-27 carrier, fix the admissible mathematical category. This prevents "intrinsic", "non-tautological", and "smaller" from becoming post-hoc labels.

## 1. Admissible input category

An admissible carrier is not defined from a chosen presentation alone. The input must be a functorial filtered relation datum attached to the group in the chosen class.

At minimum the admissible input category must specify:

- objects: the relevant pro-3 one-relator/Demuškin groups together with the filtered relation datum actually allowed;
- morphisms: continuous group isomorphisms together with the induced maps on the allowed filtered/relation data;
- gauge morphisms: free-basis/Nielsen changes, relator multiplication by a unit/conjugation, and any auxiliary normalization explicitly declared;
- coefficient category: the target algebra/module/projective category in which the carrier lives.

A proposed J_27 is admissible only if it is a functor (or pseudofunctor, if unavoidable and explicitly controlled) on this category.

## 2. q-blindness and category adequacy

q-blindness is a definition-level condition, not a test performed after construction. The admissible input must be the declared filtered/relation-information functor, not the unrestricted full group together with arbitrary intrinsic constructions.

The construction of J_27 may use only the declared filtered/relation input and universal structural operations. It may not use:

- the unknown canonical character chi or its finite reductions;
- q as a supplied parameter;
- the dualizing-module action when that action is the target orientation;
- an equivalent complete Demuškin classification invariant used only to reconstruct chi by the known classification formula;
- an equation obtained by first solving for chi and then encoding the answer;
- any factorization through an already-known canonical-orientation object without an independent obstruction construction.

A group-only construction is therefore not automatically admissible merely because it is functorial. If it first extracts q, the dualizing action, or an equivalent complete orientation invariant and then repackages it, it is classified as a tautological/classification reconstruction rather than a new filtered carrier.

This restriction is necessary because infinite Demuškin groups already possess a canonical dualizing module/action and a canonical orientation; allowing arbitrary group-intrinsic constructions would make J_27 exist trivially and would collapse the intended information-boundary problem.

A q=3 example may be used for verification, but not for definition.

## 3. Intrinsicity

Intrinsicity means: for every admissible isomorphism/gauge transformation g, there is a canonically induced isomorphism

J_27(X) -> J_27(gX)

and these induced maps satisfy identity and composition laws.

"Nielsen invariant by calculation" is insufficient unless the calculation exhibits the induced functorial map.

## 4. Orientation bridge

There must be an explicit natural map/evaluation

Phi_27 : J_27 -> O_27

into the finite-level orientation datum, with

Phi_27(J_27(G)) = chi mod 27

in the frozen q=3 test case and naturally under admissible morphisms.

The bridge cannot be defined by inserting chi as an argument.

## 5. Separation

The carrier must distinguish the relevant control family without q being supplied.

At minimum, the q=3 and q=9/27-relevant controls must be separated whenever their canonical orientation residues differ modulo 27.

A single frozen q=3 computation is therefore not enough to establish separation.

## 6. Compatibility

There must be a natural reduction

rho_27,9 : J_27 -> J_9

whose orientation bridge commutes with reduction:

J_27 --Phi_27--> O_27
 | rho              | mod 9
 v                  v
J_9  --Phi_9-----> O_9.

The bottom object is the already audited mod-9 carrier, not a newly redefined substitute.

## 7. Operational non-tautology

"Non-tautological" is replaced by a structural test.

A candidate is NOT accepted as a new carrier merely because Fox equations are renamed, repackaged, or transported.

For acceptance, at least one of the following must be exhibited:

(A) an independent construction of J_27 from filtered/relation/cohomological data that does not first construct the exact Fox obstruction;

or

(B) a factorization
J_27 -> O_Fox,27
through a target whose defining generators/relations are strictly fewer or structurally coarser than the Fox obstruction, together with a proof that the Fox obstruction is not reconstructible from J_27 alone as an object;

or

(C) an independently defined universal property characterizing J_27 without reference to Fox calculus.

A map into Fox by itself does NOT establish novelty or compression.

## 8. "Smaller" is relative, not absolute

No absolute information-theoretic size claim is allowed.

If compression is claimed, the comparison category and invariant must be declared first, for example:

- quotient category;
- number/rank of independent generators;
- algebraic dimension/embedding dimension;
- universal-property strength;
- factorization preorder.

Only after the category is fixed may one state "strictly smaller/coarser".

## 9. Success and failure classification

### PASS / CLOSED
All definition, functoriality, gauge, orientation bridge, separation, and compatibility conditions are proved, and non-tautology is established under a declared comparison category.

### PASS / LOCAL
A legitimate candidate or map is verified, but one structural theorem remains open.

### FAIL / CLOSED
Definition is circular; functoriality fails; gauge invariance fails; separation fails; or the object is demonstrably only a Fox re-encoding.

### OPEN
A candidate survives the pre-check but a required theorem is unresolved.

## 10. Mandatory pre-computation checklist

Before any mod-27 calculation:

1. exact input object;
2. object category and morphisms;
3. allowed gauge transformations;
4. q-blind definition;
5. exact target orientation datum;
6. natural orientation bridge;
7. reduction to J_9;
8. operational non-tautology criterion;
9. declared comparison notion for "smaller";
10. literature comparison status;
11. stop consequence for each failed item.

No broad computation is authorized until items 1–8 are fixed.

## 11. Literature comparison

The M3 branch remains parallel and must not be conflated with novelty.

Before promoting a surviving J_27 candidate, compare its object/input/invariance/obstruction/factorization structure with the relevant Demuškin orientation, Hochschild/cohomological, and Pál–Quick/A3 methodology. The comparison must identify what is genuinely transferred, what is already known, and what remains different.

## 12. Main methodological correction

The project does NOT currently claim:

- P_3 is absolutely minimal;
- J_3 is absolutely minimal;
- full Fox is absolutely minimal;
- characteristic-zero data is necessary in every possible carrier category.

The current claim is narrower:

> Certain information layers and compression routes have been closed, while the existence of a higher intrinsic finite-level carrier remains an open categorical/functorial question.

This document is the mandatory gate before the mod-27 branch.
