# Rank-4 D4 Relator-Lifting Definition Gate — 2026-09-19

## Status
**DEFINITION DRAFT / NOT YET EXECUTED**

This document defines the next candidate object after the PASS of the rank-2 D4 control. No rank-4 computation is authorized until this definition is independently audited.

## 1. Fixed rank-4 presentations
Let
G_3=<x1,x2,x3,x4 | r_3=x1^3[x1,x2][x3,x4]=1>
and let the q=infinity baseline be
G_inf=<x1,x2,x3,x4 | r_inf=[x1,x2][x3,x4]=1>.

Write V=F3^4 with symplectic form J determined by R2=[X1,X2]+[X3,X4].

## 2. First filtration level
Use the standard p-Zassenhaus filtration and n=4.
The q=3 power term x1^3 first appears in degree 3, so D4 is the smallest level at which the q=3 source can affect relator preservation beyond the common quadratic relation.

## 3. Ambient linear group
The candidate ambient group is GSp_4(F3), not Sp_4(F3) by default.
For g in GSp_4(F3), define its multiplier mu(g) by g^T J g = mu(g) J.
Sp_4(F3) is the multiplier-1 subgroup.

## 4. Lift class
A lift of g is a specified free pro-3 automorphism tilde-g of F=<x1,...,x4> inducing g on F/Phi(F)=V.
The first implementation will use explicitly specified Nielsen-type lifts for selected representatives. The existence, choice-dependence, and exact admissibility equivalence must be audited before treating the resulting set as intrinsic.

## 5. Relator-unit preservation condition
At level D4, the candidate admissibility condition is:
there exists a unit u in F3^times such that tilde-g(r_3) is congruent to r_3^u modulo the closed normal closure of r_3 together with D4(F).
For the baseline q=infinity relation, the same condition is imposed with r_inf.

The unit is not an independent free parameter once the degree-2 relation is nonzero: the degree-2 class forces u=mu(g). This implication is part of the definition audit and must be checked in the implementation.

## 6. Degree-3 reduction to be audited
Modulo D4, the degree-3 change coming from conjugating the quadratic relator is contained in
span_F3{[X1,R2],[X2,R2],[X3,R2],[X4,R2]}.
The q=3 relator has the additional p-layer source X1^[3].
Because the p-layer V^[3] is distinct from the ordinary degree-3 Lie layer in the frozen restricted convention, the candidate q=3 admissibility condition reduces to
(g X1)^[3] = mu(g) X1^[3],
equivalently, at the F3 vector level,
g e1 = mu(g) e1.

For q=infinity there is no degree-3 p-layer source, so the corresponding p-layer constraint is absent.

**Important:** the reduction above is a candidate structural lemma, not yet a PASS. The exact normal-closure calculation and lift-independence must be verified.

## 7. Candidate observable
Define, only after the audit passes,
A_4^rel(q) = { g in GSp_4(F3) : an allowed lift of g satisfies the relator-unit condition modulo D4 }.
This is not yet called a weak-data invariant. The allowed input must exclude the full abstract quotient G_q/D4.

## 8. Required audit before execution
1. Independently reconstruct D4 through Magnus degree 3.
2. Verify the degree-2 multiplier/unit identity.
3. Verify the degree-3 normal-closure correction span has the expected rank.
4. Verify the restricted p-layer separation used in the reduction.
5. Test lift-independence on at least two admissible lifts of the same linear representative where available.
6. Keep GSp and Sp conventions separate.
7. Only then test selected rank-4 representatives.

## 9. Gate consequence
PASS: the object and its finite-level equivalence are well-defined under the frozen conventions, and the implementation reproduces the structural reduction.
FAIL: the proposed A_4^rel definition is not legitimate at D4; stop before any rank-4 q-comparison.
INCONCLUSIVE: lift choice, unit extraction, or weak-data boundary remains unresolved.

## 10. Boundary
This gate does not claim q-recovery, orientation recovery, or canonicity. It is a definition/legitimacy gate for a small rank-4 control only.