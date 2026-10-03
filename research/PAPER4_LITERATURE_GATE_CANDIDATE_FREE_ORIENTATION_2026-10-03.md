# PAPER 4 — LITERATURE GATE: CANDIDATE-FREE ORIENTATION / q-RECOVERY — 2026-10-03

## Scope of this audit

This audit evaluates the proposed next step: small finite-window experiments for candidate-free recovery of the Demushkin parameter q/orientation.

The current Paper 4 T1-C target is a different object: the relative extension-depth parameter s in the stress family
G_{s,a}=<z,x_1,...,x_d | z^{p^s}=r_D>.
Therefore a computation that only distinguishes q=3 from q=infinity for ordinary Demushkin groups is not automatically a new Paper 4 result.

## Literature findings

1. Blumer–Quadrelli, *Koszul Lie algebras and their subalgebras*, states that for odd p the p-restrictification of the surface Lie algebra is the Lie algebra associated to the dimension-subgroup series of any 2d-generated Demushkin group. Thus the ordinary mod-p graded Lie object is rank-controlled and does not by itself encode the Demushkin q-parameter.

2. Labute's canonical orientation is not a newly defined target: modern sources explicitly state that every Demushkin group has a unique orientation making it Kummerian/1-cyclotomic, and in the standard odd-p presentation the coordinate formula is theta(y_1)=(1-q)^(-1), with the other standard generators mapped to 1.

3. Efrat's Zassenhaus/Massey/unipotent representation theorem characterizes certain Zassenhaus terms by intersections of kernels of unipotent representations under stated hypotheses. It is a filtration/representation tool, not by itself a theorem of candidate-free Demushkin orientation reconstruction.

4. Palaisti, arXiv:2610.00021 (published 2026-08-31 on the arXiv record), studies free-by-Demushkin extensions and relation-defect classes in topological coinvariants of the free kernel. This is relevant methodology for Gate T, but the abstract does not state candidate-free orientation recovery from an unmarked finite window.

## Project boundary

The repository's Paper 3 top-down closure already establishes, in its declared standard odd-p fixed-rank Demushkin scope, that the canonical finite-level orientation [chi_k] factors through the finite Zassenhaus window W_k. Consequently, re-running q=3 versus q=infinity as a bare Demushkin experiment would be validation/reproduction, not a new theorem.

The potentially new question is instead:

> In the free-by-Demushkin stress family, after forgetting the marked quotient map to D/D_n(D), does an unmarked finite window intrinsically recover any q/a-dependent extension datum, or the canonical base-orientation information needed to reconstruct it?

This is exactly the still-open T1-C unmarked reconstruction problem.

## Pre-check for the proposed computation

Object: an explicitly defined unmarked finite-window observable of the stress family.

Input: W_n alone; no chosen quotient map, presentation, q, a, or orientation.

Functoriality: invariant under abstract finite-group isomorphism.

Gauge: invariant under presentation changes and quotient-map postcomposition.

Orientation bridge: an explicit map from the observable to the relevant canonical orientation/extension class.

q-blindness: the observable definition must not insert q or a.

Separation: test q/a-distinct admissible cases only after the above object is fixed.

Stop: if the proposed experiment merely computes a known selector for ordinary Demushkin groups, classify it as PASS/LOCAL validation and do not promote it.

## Classification

- gr blindness for ordinary Demushkin q: PASS/LOCAL literature-supported; direct source verification still desirable.
- canonical orientation uniqueness: PASS/LOCAL literature-supported; not new.
- Efrat unipotent filtration tool: PASS/LOCAL as methodology; no orientation-reconstruction theorem established.
- Palaisti relation-defect relevance: PASS/LOCAL at abstract level; full-paper transfer remains to be checked.
- candidate-free orientation recovery for the current unmarked free-by-Demushkin finite window: OPEN.
- novelty of a bare q=3 vs q=infinity Demushkin GAP census: CONDITIONAL / likely redundant with the already closed Paper 3 T0 result.
- next authorized computation: only a q-blind, unmarked observable for the free-by-Demushkin family, with same-window separation/reconstruction as the endpoint.

## Sources

- Blumer–Quadrelli, *Koszul Lie algebras and their subalgebras*.
- Labute, *Classification of Demushkin groups*.
- Efrat, *The Zassenhaus filtration, Massey Products, and Representations of Profinite Groups*, arXiv:1301.0896.
- Palaisti, *Detecting Cohomological Dimension Three in Free-by-Demushkin Pro-p Groups*, arXiv:2610.00021.
