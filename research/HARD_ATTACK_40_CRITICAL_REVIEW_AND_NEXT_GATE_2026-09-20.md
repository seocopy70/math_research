# HARD ATTACK 40 — CRITICAL REVIEW AND REVISED NEXT GATE
## 2026-09-20

### Purpose

This audit reviews the proposed self-critique of Hard Attack 40 and records the corrected logical boundaries before the next attack.

## 1. Accepted corrections

The following corrections are confirmed.

1. The coefficient module A_k(rho)=Z/3^k is rank-one, but the twisted coinvariant M_{k,rho} need not be rank-one. The correct phrase is **rank-one coefficient / scalar-character specialization**.
2. The factorization
   Hom_{Q_k}(M_k,A_k(rho)) ≅ Hom_{Z/3^k}(M_{k,rho},Z/3^k)
   is a formal universal-property reformulation, not by itself a new obstruction theorem.
3. K_k=0 is not the decisive selector gate. Full recovery of e_k is stronger than necessary; the decisive object is the scalar-character coker/cardinality function
   rho |-> |C_k(rho)|.
4. The PD^2-based finite selector remains PASS / LOCAL. Removing PD^2 is a separate theorem problem and cannot be inferred merely from the intrinsic definition of C_k(rho).

## 2. Critical correction to the proposed "completeness" idea

The suggestion to reinterpret maximality as "complete filling" is potentially misleading and, in its naive form, backwards.

By definition
C_k(rho)=H^2(Q_k,A_k(rho))/im(delta_{k,rho}).

If the ambient H^2 group is fixed, then larger |C_k(rho)| means **smaller** transgression image, not a more completely filled ambient cohomology group. In the established PD^2 selector,
|C_k(rho)|=|H^2(Q_k,A_k(rho))|
means im(delta_{k,rho})=0.

Therefore the correct qualitative language is not "image fills H^2" but rather one of:
- transgression invisibility / vanishing;
- defect maximality;
- failure of the extension class to be detected by the allowed scalar coefficients.

A qualitative reformulation may still be useful, but it must preserve this direction.

## 3. "Response function" is useful only as a heuristic

The family
rho |-> im(delta_{k,rho})
is a legitimate structural object. However "response curve", "threshold", or "spectroscopy" are explanatory metaphors, not mathematical results. The next theorem must specify an invariant such as:
- image cardinality;
- image filtration/annihilator;
- vanishing/nonvanishing;
- a natural determinant/Fitting invariant,
and prove its functoriality and relation to C_k(rho).

No broad scan is authorized merely to visualize this response.

## 4. Representation-theoretic analogy must be tightened

The twisted coinvariant
M_{k,rho}=M_k / <gm-rho(g)m>
is naturally a tensor/coinvariant construction over the group ring after choosing the rank-one coefficient module. Calling it "the opposite direction of induced/coinduced" is not a theorem and should not be used as a structural claim without an explicit adjunction. The safe representation-theoretic statement is simply that the Kummer family probes rank-one scalar specializations of M_k.

## 5. Fitting ideals are not automatically progress

Because C_k(rho) is already a cokernel, replacing its presentation by a Fitting ideal is initially only a repackaging. A Fitting attack is justified only if it produces a new basis-independent quantity whose rho-dependence can be proved to control the selector, or yields a structural theorem unavailable from the coker definition.

Thus:
**Fitting carrier = OPEN candidate, not yet a next theorem.**

## 6. Information-theoretic language

The "information theory" analogy is useful for intuition but cannot serve as evidence of novelty. The rigorous object is the restricted observation map
Phi_k:e |-> (phi_*(e))_{rho,phi}
with kernel K_k, and the selector-observation function
O_k(e_k)(rho)=coker(delta_{k,rho}).

The exact logical chain is:
full coefficient profile -> Yoneda completeness (PASS/CLOSED);
restricted Kummer profile -> OPEN;
restricted profile -> unique selector without PD^2 -> OPEN/DECISIVE.

## 7. Revised active gate

The next principal question is:

Can the specific Demushkin extension class e_k force a unique scalar-character coker maximizer through a structural theorem about delta_{k,rho}, without invoking PD^2 or the canonical dualizing action?

Before introducing Fitting, determinant, or new representation-theoretic machinery, the first authorized subattack is:

**A. Scalar-visibility theorem.**
Determine whether im(delta_{k,rho}) has a canonical vanishing/nonvanishing criterion expressible from the finite extension data and scalar character rho.

**B. Compare with the already closed mod-9 intrinsic obstruction.**
At k=2, determine whether the intrinsic push-forward delta_{2,rho} specializes to the established cup+Bockstein / degree-(2,3) obstruction, rather than merely agreeing numerically in a presentation.

**C. Stop condition.**
If the scalar-visibility theorem cannot control the ambient H^2 size, do not claim selector uniqueness. Record the exact boundary:
extension-class visibility is solved, but ambient top-cohomology normalization remains PD^2-dependent.

## 8. Classification after this audit

- Hard Attack 40 scalar-character factorization: **PASS / CLOSED**.
- Hard Attack 40 as a new obstruction theorem: **HISTORICAL / SUPERSEDED**; it is a reformulation.
- Restricted Kummer faithfulness K_k=0: **OPEN / AUXILIARY**.
- Scalar-character visibility of the specific e_k: **OPEN / DECISIVE**.
- Unique coker maximality without PD^2: **OPEN / DECISIVE**.
- Fox row as coordinate realization of phi_*(e_k): **OPEN**.
- Fitting/determinant reformulation: **OPEN / DEFERRED until non-tautology is shown**.
- PD^2-based finite selector: **PASS / LOCAL**.
- Carrier minimality: **OPEN**.
- Strict carrier-tower naturality: **OPEN**.

### Bottom line

The proposed self-critique is substantially correct, but one suggested reinterpretation must be rejected: maximal coker is not "complete filling" of H^2. It corresponds to minimal transgression image, and at the PD^2-selected point the established equality means the transgression image vanishes.

The next attack should therefore remain centered on the **scalar-character visibility/vanishing structure of the intrinsic extension push-forward**, with the already closed mod-9 obstruction used as a comparison target. Fitting/determinant machinery is secondary and must earn its place by producing genuinely new, basis-independent control.
