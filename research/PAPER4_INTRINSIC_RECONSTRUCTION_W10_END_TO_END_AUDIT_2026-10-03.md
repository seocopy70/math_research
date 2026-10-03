# PAPER 4 — INTRINSIC RECONSTRUCTION FEASIBILITY GATE: W10 END-TO-END ATTACK
## 2026-10-03

## Decision
The bounded Gate-B attack is authorized as a single end-to-end test at
[
(p,s,a,n)=(3,2,1,10).
]
The purpose is not to reopen the frozen relative-threshold proof or to begin blind carrier search. It is to test, in one package, whether the unmarked critical finite window can canonically recover enough marked quotient/extension data to determine the relative obstruction.

The package to test is:
[
W_{10}	o operatorname{Aut}(W_{10})	o
{	ext{admissible quotient data}}	o
{	ext{relative extension obstruction}}.
]

Required components:
1. intrinsic first-layer data (H^1(W_{10},mathbf F_3)) and cup-radical;
2. the first critical degree-9/degree-10 jet carrying the (z^9=r_D) information;
3. the automorphism action on that combined structure;
4. admissible quotient/lift candidates and their (operatorname{Aut}(W_{10}))-orbits;
5. the induced relative extension class after quotienting lift-change coboundaries.

## Pre-check
Object: the unmarked filtered finite group (W_{10}=G_{2,1}/D_{10}(G_{2,1})), together with intrinsic filtration data.

Input: only the abstract filtered group; the map to (D/D_{10}(D)) is not supplied.

Functoriality: automorphisms of the filtered group must transport every accepted intrinsic construction.

Gauge: presentation choices, generator lifts, and quotient-map postcomposition by automorphisms are not intrinsic and must be quotiented.

Orientation bridge: a candidate is accepted only if it canonically determines the marked extension class, not merely a presentation relator or scalar defect.

q-blindness: the candidate must not insert (q=3^a) by definition.

Separation: if two admissible marked realizations of the same unmarked (W_{10}) have different relative obstruction classes, intrinsic reconstruction fails.

Novelty: merely recovering the already-known finite Kummer selector from (W_{10}) is not sufficient.

Stop: if the quotient/extension object is only a re-encoding of the forgotten marked map, classify it as tautological rather than intrinsic.

## Decision outcomes
- intrinsic quotient/extension orbit is uniquely determined and its obstruction is constant: PASS / LOCAL, positive reconstruction candidate;
- same unmarked window supports different obstruction values: FAIL / CLOSED;
- quotient orbit is intrinsic but obstruction is not: OPEN, reduced to extension-class functoriality;
- no mathematically legitimate finite computation can distinguish the alternatives within this bounded model: STOP and return to realistic Paper 4.

## Scope warning
The choice (a=1) is deliberate because (p=3,s=2) makes (n=10) the smallest critical stress-family window. This is the known boundary case where the generic (age2) finite-kernel survival witness does not apply. No conclusion for the certified (age2) theorem is changed by this gate.

