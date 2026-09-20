# KUMMER HARD ATTACK 36 — SELECTOR-ONLY COHERENCE AND THE REAL ENDGAME
## 2026-09-20

### 1. Objective

After Hard Attack 35, the raw finite coker carriers do not automatically form a strict inverse system, but the unique finite selectors are compatible under PD² verification. This attack asks whether compatibility can be characterized intrinsically from the selector predicates themselves, without manufacturing maps M_{k+1}->M_k.

### 2. Selector sets

Define, at each k,
S_k(G) = { rho in Hom(G,U_k) : |coker(delta_{k,rho})| = 3^k }.

The finite recognition theorem gives:
S_k(G) = { chi mod 3^k}
for PD²/Demuškin G in the admissible setting.

Therefore each S_k(G) is a singleton, and the reduction map
Hom(G,U_{k+1}) -> Hom(G,U_k)
restricts to a map S_{k+1}(G)->S_k(G), because reduction of the unique selector is chi mod 3^k.

This reduction does NOT require a map between M_{k+1} and M_k. It is induced by the ordinary coefficient reduction on candidate characters, together with the theorem that the selector predicate at each level is exactly the canonical orientation condition.

### 3. Attack on circularity

Potential objection: saying "the selector reduces because it equals chi" may be tautological if the goal is to reconstruct chi intrinsically.

Resolution:
- For the finite-level theorem, equality S_k={chi mod 3^k} is established by an independent PD² orientation theorem.
- The finite carrier itself contains no chi.
- Thus the result is a recognition theorem: an intrinsic finite predicate happens to have the unique solution equal to the independently characterized canonical orientation.
- However, the selector-only coherence statement is NOT a new carrier-internal naturality theorem. It remains a verified consequence of the external PD² characterization.

Hence:
selector coherence for the mathematical reconstruction = PASS / LOCAL;
intrinsic carrier-only coherence = OPEN.

### 4. Stronger formulation

The actual reconstructed object can be defined without a raw inverse limit of carriers:
S(G) = { (rho_k)_k : rho_k in S_k(G), rho_{k+1} mod 3^k = rho_k }.

Because each S_k is a singleton and the selected elements are compatible, S(G) is a singleton.

The unique element is the orientation character chi in the inverse limit:
S(G) = {chi_filt}.

This gives a clean theorem schema:

**Finite Recognition + Coherence Theorem.**
For an admissible pro-3 PD²/Demuškin group G, the finite intrinsic coker predicates S_k select exactly one candidate rho_k at every k, and these selectors are compatible. Consequently the inverse-limit selector set S(G) is a singleton, canonically identified with chi_filt.

### 5. Remaining logical boundary

This does NOT prove:
- that P_{k+1} is minimal;
- that the raw carrier tower is a strict inverse system;
- that the construction is universal among all conceivable finite invariants;
- that the same theorem holds outside the declared PD²/Demuškin class;
- that the admissibility/naturality framework can be weakened without changing the statement.

These remain OPEN.

### 6. New stop test

The research should NOT continue indefinitely merely to make the raw carriers functorial if the actual reconstruction theorem is already obtained through compatible selector predicates.

A further attack is justified only if it can improve one of:
1. remove dependence on the external PD² orientation characterization from coherence;
2. prove minimality of P_{k+1} in a precisely defined carrier category;
3. establish strict carrier-level naturality;
4. broaden the admissible category.

Otherwise, the finite recognition + coherence theorem is a legitimate endpoint for the current main branch, with minimality and universality explicitly separated as future questions.

### 7. Status

- selector-only coherence: PASS / LOCAL under PD² verification;
- finite recognition + coherence theorem: PASS / LOCAL;
- intrinsic carrier-only coherence: OPEN;
- strict carrier tower: OPEN;
- minimality: OPEN;
- universal no-go/minimality: OPEN.

No numerical computation required.
