# HARD ATTACK 61-A — FULL n=2 -> 3 CROSSED-WORD DERIVATION — 2026-09-20

## Status
**OPEN / LOAD-BEARING.** HA60 is downgraded to PASS / LOCAL. This attack does not assume the compact HA60 formula.

## Target
For
0 -> F_3 -> A_3=Z/27(rho_3) -> A_2=Z/9(rho_2) -> 0,
with rho_3=rho_2(1+9 mu), derive the secondary connecting obstruction for a general A_2-valued crossed cocycle z lifting f.

The calculation must separate:
1. old rho_2-dependent terms;
2. new extension parameter mu;
3. quadratic R terms;
4. the new P_4/power residual t_2;
5. D_4/P_4 error terms.

The decisive question is whether an additional B_{rho_2}(z) term survives.

## Pre-check
- Object: the actual secondary connecting map delta_3 on the zero locus of the primary obstruction delta_2.
- Input: coefficient extension, finite filtered relation/power data, and the already established mod-9 obstruction; no q/chi/dualizing action.
- Functoriality: connecting maps are intrinsic; the filtered residual must still be proved intrinsic.
- Gauge: crossed-cocycle representatives and H^2 generators are tracked explicitly.
- Orientation bridge: successive Kummer lifting obstruction only.
- q-blindness: q and chi are excluded from the definition.
- Separation: standard q=3, q=9, 27|q are external verification cases.
- Stop condition: if the derived formula depends on an untracked choice of A_2 lift, omega normalization, or relator gauge, stop before defining t_2 intrinsically.

## Exact expansion to derive
For a reduced word w=s_1...s_m,
z(w)=sum_j rho_3(s_1...s_{j-1}) z(s_j),
and rho_3(g)=tilde(rho_2)(g)(1+9 mu(g)) mod 27.

The expansion must retain all terms modulo 27 before division by 9. In particular, terms of the schematic form
9 * (mu(prefix) * f(letter))
and terms coming from the mod-27 lift of rho_2 must not be discarded merely because they disappear modulo 9.

The expected outcome is either

delta_3(z)=[f(t_2)+(mu wedge f)(R)] omega,

or

delta_3(z)=[f(t_2)+B_{rho_2}(z)+(mu wedge f)(R)] omega,

or a more precise equivalent formula with the old-lift contribution absorbed into a canonically transported normalization.

## Current logical boundary
HA60's q=9 calculation cannot decide B_{rho_2}, because rho_2 is trivial there. The q=3 case is therefore the decisive audit case.

No induction n -> n+1 is authorized until this n=2 -> 3 formula is settled.

## Immediate consequence branches
- If B_{rho_2}=0 by a structural cancellation: proceed to HA61-C intrinsic t_2 gate.
- If B_{rho_2} is exactly the transported first-stage normalization: record the corrected formula and proceed.
- If B_{rho_2} survives as genuine extra data: HA60's compact formula is superseded and the exact surviving term becomes the new boundary.
- If the term is gauge-dependent: classify the compact carrier as non-intrinsic at this stage.

## Verification discipline
Any positive cancellation must be checked independently in the frozen q=3 and q=9 normal forms, with the same transgression/fundamental-class convention used in the mod-9 theorem. No known orientation formula may be used to choose the surviving scalar.

## Classification
HA60: **PASS / LOCAL**.
HA61-A: **OPEN / LOAD-BEARING**.
