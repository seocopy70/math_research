# Paper 5 Gate B — p=3, a=2 corrected group-level lift D3-D6

Date: 2026-10-07

## Status
**PASS / LOCAL.** This record captures a corrected group-level finite-window realization result supplied after the earlier homogeneous/full-ideal distinction audit. It does **not** close Gate B.

## Correction boundary
The earlier seed calculation with the fixed choice W=z^2 is not being reopened or reclassified. The authoritative log records that the zero-correction seed fails the full non-homogeneous ideal test already at T=4. The present result instead uses a corrected parameterization of the images of x,y,z by actual group elements (products of basic commutators), so the group-like condition is automatic and the higher corrections are solved at the group level.

Target order is **cx**. The earlier D3-D9 J-membership test and the derived claim E_2 in ND_10 are withdrawn as insufficient for the corrected filtered-ideal problem.

## Computation reported
For p=3, a=2, with linear part diag(2,1,2):

- D3, D4, D5: no obstruction in the corrected group-level parameterization.
- Weight 4 parameters were exhaustively checked in the stated finite slices.
- D3 weight-2 solution space: 729 candidates.
- D4 survivors: 81.
- D5 survivors: 27.
- A corrected D6 computation constructs explicit solutions from five D5 candidates (indices 3,4,5,8,14).
- For index 3, a separate slower dictionary-algebra implementation re-evaluates the construction and gives zero residual at N=3,4,5,6.

The result is therefore stronger than the old fixed seed W=z^2 calculation: it demonstrates finite-degree relation preservation with genuine group elements after higher corrections.

## What it proves
It proves a **finite local realization through D6** for p=3, a=2, within the explicitly searched parameterization.

It does not prove:
- existence of a compatible lift for all n;
- existence of an actual pro-3 automorphism with linear part diag(2,1,2);
- Gate B closure;
- the result for arbitrary a or arbitrary odd p.

The 4,782,969-solution quadratic-enumeration output from the intermediate script is explicitly excluded from the evidence base because it conflicts with the direct verification and was not trusted.

## Gate classification
- Corrected p=3,a=2 group-level D3-D6 finite realization: **PASS / LOCAL**.
- p=3,a=2 compatible pro-3 lift: **OPEN / LOAD-BEARING**.
- Gate B: **OPEN / LOAD-BEARING**.

## Next mathematical gate
Do not return to the fixed W=z^2 seed or the obsolete homogeneous J-membership argument. The useful next question is whether the five D6 solutions reveal a stable correction pattern. Compare their weight-2 and weight-3 parameters first; only if a structural pattern emerges should D7/D8 be used as a targeted continuation. The ultimate proof obligation remains an all-degree compatible lift.

## Independent verification status
The reported index-3 D6 solution was checked with a separate slower dictionary-algebra implementation. Repository-independent reproduction of the entire search has not yet been performed in this record.
