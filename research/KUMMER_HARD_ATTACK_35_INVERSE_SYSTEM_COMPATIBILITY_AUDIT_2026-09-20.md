# KUMMER HARD ATTACK 35 — INVERSE-SYSTEM COMPATIBILITY AUDIT
## 2026-09-20

### Target

The finite-level theorem is established at each k:
|coker(delta_{k,rho})| = 3^k iff rho = chi mod 3^k,
with the carrier built from
Q_k=G/P_{k+1},
M_k=P_{k+1}/(P_{k+1}^{3^k}[P_{k+1},P_{k+1}]),
E_k=G/(P_{k+1}^{3^k}[P_{k+1},P_{k+1}]).

The next question is whether these finite selectors form a canonical inverse system.

### Attack A — naive carrier-level reduction

There are natural quotient maps
Q_{k+1}->Q_k
and, because the defining denominator for E_{k+1} is contained in that for E_k, a natural map
E_{k+1}->E_k.

However the relation modules are based on different kernels:
M_{k+1}=P_{k+2}/(P_{k+2}^{3^{k+1}}[P_{k+2},P_{k+2}]),
M_k=P_{k+1}/(P_{k+1}^{3^k}[P_{k+1},P_{k+1}]).
The natural map induced by inclusion sends M_{k+1} only into a generally proper submodule of M_k; it is not a canonical quotient M_{k+1}->M_k.

Therefore there is no automatic reduction map
Hom_{Q_{k+1}}(M_{k+1},A_{k+1}(rho_{k+1}))
 -> Hom_{Q_k}(M_k,A_k(rho_k)),
and hence no automatic map of the two transgression cokernels.

Conclusion: the strong claim that the finite coker carriers themselves form an inverse system is NOT established. Any proof that simply reduces E, M, delta and coker from k+1 to k is invalid without an additional extension/restriction construction.

Classification: carrier-level inverse-system functoriality = OPEN / load-bearing; naive direct reduction = FAIL / CLOSED as an inference.

### Attack B — selector compatibility

A weaker statement is enough for reconstruction: if rho_{k+1} is the unique finite selector at level k+1, then its reduction rho_k should be the unique selector at level k.

Using PD^2 duality, for any candidate rho define delta_k=chi*rho^{-1} modulo 3^k. The finite top-cohomology criterion is equivalent to
|H^2(G,A_k(rho))|=3^k iff delta_k is trivial.

If rho_{k+1} is selected at level k+1, then the corresponding top-cohomology group has full size 3^{k+1}. Under the duality description this means the invariant submodule of the dual coefficient module has full size 3^{k+1}, which forces delta_{k+1}=1 modulo 3^{k+1}. Reducing gives delta_k=1, so rho_k=chi mod 3^k and therefore rho_k is the unique level-k selector.

Thus compatibility of the selected characters is a theorem-level consequence of the already established PD^2 selector criterion, although this proof uses the canonical orientation in the verification and is not itself a carrier-only construction.

### Interpretation

This cleanly separates two notions previously conflated:

1. **finite-level recognition:** PASS / LOCAL;
2. **carrier tower naturality:** OPEN;
3. **compatibility of the selected outputs:** PASS / LOCAL under PD^2 duality and the finite-level selector theorem.

The inverse-limit character can therefore be recovered as a compatible family of unique finite selectors at the level of mathematical existence. What remains open is whether the finite carrier construction itself admits a natural transition law independent of the already-known orientation/PD^2 verification.

### New strategic consequence

Do NOT spend the next effort trying to manufacture a canonical map between M_{k+1} and M_k merely because the notation suggests one. The kernel changes with k, and this is a genuine structural obstruction.

The stronger next question is now:

> Can the finite selector be characterized by a compatibility-free universal property, so that the inverse limit is the set of all compatible finite selectors and compatibility is forced by the selector predicate itself?

A successful answer would close the practical reconstruction problem without requiring the individual coker carriers to form a strict inverse system.

### Status

- naive coker-carrier reduction k+1 -> k: **FAIL / CLOSED** as an automatic inference;
- carrier-tower naturality: **OPEN / load-bearing**;
- finite selector compatibility: **PASS / LOCAL** under PD^2 verification;
- practical inverse-limit reconstruction of chi_filt: **PASS / LOCAL** subject to the declared PD^2 framework;
- carrier-only inverse-limit functoriality: **OPEN**;
- minimality of P_{k+1}: **OPEN**.

No numerical scan was needed.
