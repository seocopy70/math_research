# Track B — revised comparison: q=3 vs q=∞

## Reason for revision
At Zassenhaus degree <= 4, q=9 cannot contribute its defining p-power term x1^9 because x1^9 lies in D9. Thus a degree-4 q=3 vs q=9 experiment cannot distinguish the numerical values 3 and 9; it only tests whether a p-power relation has entered the observed degree window.

## Primary experiment
Compare

G_3 = <x1,x2,x3,x4 | x1^3 [x1,x2][x3,x4] = 1>

with the q=∞ / pure-commutator control

G_∞ = <x1,x2,x3,x4 | [x1,x2][x3,x4] = 1>.

The common quadratic initial form is
R = [X1,X2] + [X3,X4].

Therefore Q4 and the ordinary Sp4(F3)-module W45 provide a common control. The comparison targets the restricted/Zassenhaus refinement.

## Expected degree locations
For G3, x1^3 first appears in D3/D4 and can induce degree-4 corrections through brackets/conjugations. This is exactly the mechanism detected in A3.

For G∞, there is no x1^q p-power term at all, so the corresponding p-power contribution is absent in every finite degree. Any degree-3/4 difference is therefore a clean test for the presence of the p-power relation, not for the numerical distinction 3 vs 9.

## Required invariants
Do not compare raw coordinates. Compare:
1. restricted/Zassenhaus degree-3 classes modulo the common ordinary Lie part;
2. induced degree-4 classes in Q4;
3. whether the induced class is zero/nonzero in Q4;
4. its location relative to W45 and Q4/W45;
5. if necessary, Sp4(F3)-module intertwiners between the resulting subspaces.

## Interpretation discipline
- If G3 and G∞ differ at degree 3 or 4, this establishes detection of the presence of the p-power relation in that filtration window.
- It does NOT yet establish recovery of the exact orientation-image parameter q.
- To distinguish q=3 from q=9, the first unavoidable window is degree 9, where x1^9 can enter.

## Secondary experiment
Only after the primary experiment is settled, estimate the computational cost of a degree-9 q=3 vs q=9 comparison. The dimension of the degree-9 free Lie component on 4 generators is given by the Witt formula

l_9 = (1/9)(4^9 - 4^3) = 29,120.

Thus a naive ambient degree-9 linear-algebra computation is substantially larger than the degree-4 calculation and should be designed around certificates/symmetry rather than brute-force full matrices.

## Sign convention
All coefficients are in F3, so 2 = -1. In particular

d4 = 2T + 2[[[X3,X4],X2],X1]

may equivalently be written

d4 = -(T + [[[X3,X4],X2],X1]).

The computational record retains coefficient 2 to match the exact F3 output; the equivalence 2=-1 should be stated whenever sign interpretation matters.

## Status
This revised design supersedes the degree-4 q=3 vs q=9 comparison design. Actual q=3 vs q=∞ computation remains to be executed and independently verified.
