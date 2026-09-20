# ONE-RELATOR KUMMER SELECTOR STRESS TEST — 2026-09-21

## Scope
Authorized follow-up to the B2 finite Kummer selector branch. This is a scope/generalization experiment, not a proof of the intrinsic \(\bar\delta_4\circ\iota_1\) statement. The present computation uses the already-proved one-relator Fox realization of the Kummer predicate as a diagnostic proxy.

## Pre-check
- Object: one-relator pro-3 group \(G=F/\langle\!\langle r\rangle\!\rangle\).
- Input: relation word, rank, and finite coefficient ring \(\mathbf Z/3^k\); no canonical orientation or q is inserted.
- Functoriality: only the crossed-cocycle/Fox realization already established in B2 is used. No presentation-independence claim is inferred for the raw Fox row.
- Gauge: none is quotiented; this is deliberately a coordinate-level diagnostic.
- Orientation bridge: Kummer predicate iff vanishing of the twisted Fox row.
- q-blindness: yes.
- Separation: compare nondegenerate and degenerate quadratic relation patterns and rank-3 one-relator examples.
- Stop: no interpretation as an intrinsic \(\bar\delta_4\circ\iota_1\) theorem unless separately proved.

## Computational method
A fresh direct Fox evaluator was implemented independently of the unavailable historical step3.py file. For each generator letter it accumulates the scalar character value of the preceding prefix and applies the standard Fox rule for \(x_i\) and \(x_i^{-1}\). Exhaustive enumeration over \(\rho_i\in1+3\mathbf Z/3^k\) checks \(\rho(r)=1\) and all twisted Fox coefficients \(F_i(\rho)=0\pmod{3^k}\). This is an independent implementation/check, not a rerun of the historical script.

## Test family
A. Standard rank-4 Demushkin, q=3: \(r=x_1^3[x_1,x_2][x_3,x_4]\).

B. Rank-4 power-free symplectic control: \(r=[x_1,x_2][x_3,x_4]\).

C. Rank-4 degenerate quadratic relation: \(r=[x_1,x_2][x_2,x_3]\).

D. Rank-3 commutator: \(r=[x_1,x_2]\).

E. Rank-3 power relation: \(r=x_1^3[x_1,x_2]\).

F. Rank-3 degenerate commutator relation: \(r=[x_1,x_2][x_1,x_3]\).

G. Rank-3 power + degenerate quadratic relation: \(r=x_1^3[x_1,x_2][x_1,x_3]\).

H. Rank-4 power + degenerate quadratic relation: \(r=x_1^3[x_1,x_2][x_2,x_3]\).

## Results

| Relation | rank | k=2 (mod 9) | k=3 (mod 27) |
|---|---:|---:|---:|
| \(x_1^3[x_1,x_2][x_3,x_4]\) | 4 | 1 | 1 |
| \([x_1,x_2][x_3,x_4]\) | 4 | 1 | 1 |
| \([x_1,x_2][x_2,x_3]\) | 3 active generators | 3 | 9 |
| \([x_1,x_2]\) | 2 active generators | 1 | 1 |
| \(x_1^3[x_1,x_2]\) | 2 active generators | 1 | 1 |
| \([x_1,x_2][x_1,x_3]\) | 3 | 3 | 9 |
| \(x_1^3[x_1,x_2][x_1,x_3]\) | 3 | 3 | 9 |
| \(x_1^3[x_1,x_2][x_2,x_3]\) | 3 active generators | 0 | 0 |

For the rank-4 standard Demushkin relation the unique solutions are \((1,4,1,1)\pmod9\) and \((1,13,1,1)\pmod{27}\). For the power-free symplectic control the unique solution is the trivial character.

For the degenerate relation \([x_1,x_2][x_2,x_3]\), the solutions at k=2 are \((1,1,1),(4,1,4),(7,1,7)\), and at k=3 there are 9 solutions \((1,1,1),(4,1,4),\ldots,(25,1,25)\), with the same one-parameter pattern. Thus uniqueness fails and the number of solutions grows by a factor of 3 at each additional 3-adic digit.

For \([x_1,x_2][x_1,x_3]\), there are likewise 3 and 9 solutions at k=2,3.

For \(x_1^3[x_1,x_2][x_2,x_3]\), there is no Kummer/Fox solution at either k=2 or k=3.

## Independent analytic sanity checks
The observed multiplicities are structural, not numerical noise. For commutator-only relations, the twisted Fox row is controlled by differences of candidate character values. A degenerate quadratic form leaves a positive-dimensional family of characters satisfying the row equations, explaining the 3, 9, ... growth. Adding a power term to a degenerate quadratic relation can instead make the finite Fox system inconsistent, as in test H.

## What this says about \(\bar\delta_4\circ\iota_1\)
It does not prove or disprove that \(\bar\delta_4\circ\iota_1\) is automatically zero for all one-relator pro-3 groups.

It does establish a useful boundary test:
- the finite Kummer selector is rigid on the standard nondegenerate Demushkin relation;
- degenerating the leading quadratic relation can destroy uniqueness;
- adding the power term to a degenerate quadratic relation can destroy existence altogether.

Therefore a claim that the mod-27/\(\delta_4\) lifting mechanism is automatic for arbitrary one-relator pro-3 groups is not supported by this stress test.

## Classification
**STRESS TEST: PASS / LOCAL.**

This means the authorized computational experiment successfully finds non-Demushkin one-relator examples where the finite Kummer selector loses Demushkin rigidity (non-unique or empty). It is not a theorem about all one-relator groups and is not yet a classification of \(\bar\delta_4\circ\iota_1\).

## Next authorized step
Choose the degenerate relation \(r=[x_1,x_2][x_1,x_3]\), retain all of its finite Kummer characters, and compute the actual coefficient-extension obstruction \(\bar\delta_4\circ\iota_1\) at the first stage where it is defined. This separates:
1. selector non-uniqueness caused only by the primary Kummer equations;
2. a higher obstruction that restores uniqueness;
3. automatic vanishing of the higher obstruction even in the degenerate case.

Until that computation is done, no claim is made about automatic vanishing.
