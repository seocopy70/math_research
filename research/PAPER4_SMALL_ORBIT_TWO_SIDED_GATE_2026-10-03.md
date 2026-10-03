# PAPER 4 — SMALL ORBIT / TWO-SIDED GATE-B COMPRESSION TEST
## 2026-10-03

### Question
Can one finite orbit computation simultaneously compress the positive reconstruction route and the negative same-window separation route?

### Exact decision object
For the minimal critical model W_10 at (p,s,a,n)=(3,2,1,10), let A be the set of admissible epimorphisms pi:W_10 -> Q_10 whose induced H^1-kernel is the intrinsic cup-radical line. Let H=Aut(W_10) x Aut(Q_10) act on A. Attach to each orbit its relative split/non-split obstruction.

The decisive finite test is the labelled orbit set
  A/H -> {split, nonsplit}.

It gives a genuine two-sided decision procedure:
- one orbit (or several orbits with one common obstruction value) gives intrinsic determination of the Boolean obstruction;
- two or more orbits with different obstruction values gives a same-window separation and hence FAIL/CLOSED for intrinsic reconstruction;
- multiple orbits with the same obstruction value still give intrinsic Boolean determination, although not canonical quotient-map reconstruction;
- unresolved orbit decomposition leaves the Gate OPEN.

Thus the compression idea is mathematically legitimate. The orbit calculation must include the obstruction label; orbit multiplicity alone is not a negative theorem.

### Computation actually completed
The authoritative W10 family contains explicit maps
  pi_c(z)=c, pi_c(x)=x, pi_c(y)=y,   c in D_2(Q_10),
which are epimorphisms because c^9=1 in Q_10. They all have the same H^1 data and radical kernel line.

A reduced Magnus/augmentation-algebra check was also run as a diagnostic: replacing the radical lift z by z*c with c of augmentation degree >=2 produces no difference in the degree <10 part of the naive free associative p^2-power shadow. This confirms that the first-layer orbit cannot see these corrections and that the critical obstruction must be tested in the relation-quotient, not in the free shadow.

This diagnostic is NOT promoted to a theorem: the Demushkin relation x^3[x,y]=1 must be imposed in the truncated relation algebra, and the critical degree-9 relation terms are exactly where the residual IA action can survive.

### What this settles
1. The proposed “one orbit computation for both directions” is not a conceptual shortcut or category mistake. It is a valid finite decision architecture.
2. It strictly dominates running positive reconstruction and separation as unrelated searches: the same orbit space carries both the positive uniqueness question and the negative separation witness.
3. The current explicit pi_c family cannot itself be counted as a separation pair merely because the maps are distinct; postcomposition/precomposition orbit equivalence and obstruction invariance must be checked.
4. H^1-level orbit collapse is insufficient. The critical IA/degree-9 layer remains load-bearing.

### Remaining single mathematical computation
Compute the relation-aware action of the radical-preserving IA stabilizer on the family pi_c, first on D_3(Q_10)/D_4(Q_10), then propagate to the degree-9 obstruction. The output must be the labelled orbit set, not merely a list of quotient maps.

### Classification
- two-sided orbit-decision principle: PASS / LOCAL;
- explicit pi_c admissible family: PASS / LOCAL;
- free Magnus shadow diagnostic: PASS / LOCAL;
- relation-aware full orbit decomposition: OPEN / LOAD-BEARING;
- same-window separation: OPEN;
- unmarked intrinsic reconstruction: OPEN / LOAD-BEARING.

### Stop boundary
No carrier search, threshold recomputation, degree-5 reopening, scalar/norm shortcut, or RAAG orientation branch is authorized by this calculation.
