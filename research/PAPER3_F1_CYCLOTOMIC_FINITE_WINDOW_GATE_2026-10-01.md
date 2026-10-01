# PAPER 3 — F1 Cyclotomic Finite-Window Generalization Gate

Date: 2026-10-01
Status: ACTIVE / MOST-AGGRESSIVE GENERALIZATION CANDIDATE

## 0. Decision

The next research branch deliberately leaves the torsion-free Demushkin category.

The target is not merely the sharpness of the Blumer–Quadrelli F1 Massey bound. Instead, F1 is used as an adversarial near-Demushkin class to test the broader finite-window recognition program:

> At what finite Zassenhaus depth, if any, can the window distinguish a 1-cyclotomic/Kummerian Demushkin group from a non-1-cyclotomic F1 variation with the same coarse low-degree structure?

The primary binary target is
T_cyc(G) = “G admits a 1-cyclotomic orientation”,
with the Kummerian obstruction used as the concrete verification mechanism.

This is intentionally more ambitious than Gate D. Gate D already proves the finite Kummer selector uniformly for torsion-free Demushkin pro-p groups of even rank, odd p, all allowed q, and all k>=2. The present branch asks whether the finite-window theory survives when the category itself is enlarged to include Demushkin-like non-1-cyclotomic groups.

## 1. Candidate category

For the first stress test, fix odd p, even rank d>=2, and an admissible finite parameter q.

Let C_F1(p,d,q) contain:
- the corresponding torsion-free Demushkin group D(p,d,q);
- the corresponding F1 variation F1(p,d,q).

A later enlargement may include F2, but F2 is deliberately deferred because arXiv:2609.00253 is a separate two-relator branch with its own higher-Massey obstruction analysis.

The category is marked by its actual group isomorphism class, not by a presentation.

## 2. Target

Define
T_cyc(G) in {0,1}
by:
T_cyc(G)=1 iff G admits an orientation into 1+p Z_p for which (G,theta) is 1-cyclotomic/Kummerian.

This is an intrinsic group-level property.

No chosen orientation is supplied as input.

## 3. Finite input

Use the Zassenhaus window
W_n(G)=(G/D_n(G),D_1/D_n,...,D_{n-1}/D_n)
with the same marked filtration structure used by the finite-window program.

The recognition threshold sought is
r_cyc(C;D_bullet)
= min{n : W_n(G) ~= W_n(H) => T_cyc(G)=T_cyc(H) for all G,H in C},
with infinity if no such n exists.

This is a recognition threshold, not a factorization threshold.

## 4. Mandatory pre-check

### Object
W_n and the binary target T_cyc are well-defined.

### Input
Only finite filtered group data W_n are allowed. q, a presentation, and a preselected orientation are not inserted into the selector.

### Functoriality
Filtered group isomorphisms induce isomorphisms of W_n and preserve existence/nonexistence of a 1-cyclotomic orientation.

### Gauge
Presentation generators, relator representatives, and orientation choices are not part of the target. Any obstruction used in the proof must descend to a presentation-independent class or quotient.

### Orientation bridge
A successful branch must produce an explicit implication
W_n(G) -> O_n(G) -> Kummerian obstruction
or a finite carrier whose vanishing/nonvanishing decides T_cyc on the declared category.

### q-blindness
The definition of W_n and T_cyc contains no q. q may appear only in a theorem describing the resulting threshold or in a family used for separation.

### Separation
The decisive first construction is a pair D,F1 with
W_n(D) ~= W_n(F1)
but
T_cyc(D) != T_cyc(F1).
No separation pair may be assumed from the similarity of presentations.

### Novelty
The targeted 2026 literature audit found the F1 sufficient Massey bound n<=q, and verified that Blumer–Quadrelli prove F1 is not 1-cyclotomic. No exact finite-Zassenhaus recognition theorem for 1-cyclotomicity in this Demushkin/F1 pair was identified. This is a targeted audit, not an absolute priority claim.

### Stop
No large computation is authorized until the finite pair, the exact filtration depth, and the finite obstruction carrier are all explicitly defined.

## 5. First decisive gate X1

For the smallest nontrivial case
(p,d,q)=(3,2,3),
determine whether there exists a minimal n for which the Demushkin/F1 pair is separated by W_n with respect to T_cyc.

The preferred outcome is a theorem-level statement of the form:
- W_m(D) ~= W_m(F1) for m <= m0;
- W_{m0+1}(D) not ~= W_{m0+1}(F1);
- the first separating datum has a natural Kummerian/cyclotomic interpretation.

A failure to separate at every finite n would itself be mathematically important and would imply r_cyc=infinity on that pair/class.

## 6. Relation to the existing F1 Massey branch

The Blumer–Quadrelli result gives a parameter-dependent sufficient strong Massey-vanishing range n<=q for F1, while Demushkin groups satisfy strong n-fold Massey vanishing for all n>=3. The recent Palaisti F2 paper does not resolve F1 sharpness.

Therefore the Massey branch is retained as a supporting obstruction/comparison layer, not promoted to the main target.

The main target is 1-cyclotomicity because the F1 examples were constructed precisely to separate that property from several cohomological tests.

## 7. Promotion criterion

Promote this branch only if it yields at least one of:
1. a finite-window separation theorem for D versus F1;
2. a sharp recognition threshold for T_cyc on the declared category;
3. a no-go theorem showing finite Zassenhaus windows cannot recognize T_cyc in the enlarged class;
4. a reusable carrier theorem that survives a further category enlargement.

A single finite computation is PASS / LOCAL evidence only.

## 8. Current classification

- Gate D Demushkin finite Kummer selector: PASS / CLOSED.
- F1 sufficient Massey bound n<=q: PASS / CLOSED as literature fact.
- F1 Massey sharpness: OPEN / LOAD-BEARING.
- Post-2026 targeted F1 sharpness audit: PASS / LOCAL (no exact converse located).
- F1 finite-window 1-cyclotomic recognition: OPEN / DECISIVE.
- Universal carrier/minimality theory: OPEN / CONDITIONAL.
- Publication novelty: OPEN / CONDITIONAL.

## 9. Immediate authorized action

Do not launch a large computation.

First construct the exact (p,d,q)=(3,2,3) Demushkin/F1 pair at the presentation level, determine the first Zassenhaus degree at which their defining relations can differ, and test whether that difference can be converted into an intrinsic finite-window Kummerian obstruction.

Any computation must be independently reproduced and classified before promotion.


## 10. Forward generalization roadmap (recorded 2026-10-01)

This is a roadmap, not a theorem claim.

### Phase A — F1 pair, smallest case
Determine the exact finite-window behavior of D(p,d,q) versus F1(p,d,q), beginning with (p,d,q)=(3,2,3). No large computation before the intrinsic finite obstruction/carrier is defined.

### Phase B — F1 parameter uniformity
If Phase A succeeds, extend to the allowed parameter range (p,d,q). Seek a recognition/separation threshold r_cyc(p,d,q), or rigorous lower/upper bounds. A single example remains PASS/LOCAL.

### Phase C — category enlargement
Only after F1 uniformity or a reusable carrier mechanism is established, test a genuinely different non-1-cyclotomic family; F2 is the first deferred candidate. This tests whether the mechanism is structural rather than family-specific.

### Phase D — property enlargement
If the mechanism survives more than one family, enlarge the target beyond T_cyc to a family of global properties T, seeking an intrinsic functorial form W_n(G) -> O_n(G) -> T(G).

### Phase E — general finite-window recognition theory
The long-term target is the category-relative recognition threshold r_T(C;D_bullet), together with existence/nonexistence, sharp bounds, intrinsic carriers, functorial factorization, and information-theoretic obstructions.

### Promotion / stop rules
Promote only theorem-level finite separation, sharp threshold, no-go theorem, or reusable carrier results. Stop/escalate only after Object/Input/Functoriality/Gauge/Orientation bridge/q-blindness/Separation are explicit. Do not revive the closed F1 Massey route without new evidence. Do not claim priority or that the field is waiting for this exact result.

The strategic purpose is to test whether the finite-recognition program developed in Papers 1–3 survives deliberate enlargement beyond the Demushkin category. Success justifies the next phase; failure may yield a structural no-go result.
