# HARD ATTACK 46 — TWISTED BOCKSTEIN THROUGH THE LHS SPECTRAL SEQUENCE

Date: 2026-09-20

## Target

After HA45, the base LHS transgression is closed:
W=P_2/P_3 has dimension 9, d_2:W^* -> H^2(V,F_3) has rank 9, and E_3^{2,0}=E_∞^{2,0} is the one-dimensional relation-jet line <(R,p)>.

The next question is whether the coefficient-extension Bockstein
d_lambda = beta + lambda cup(-)
on H^*(Q_2,F_3)
is forced by this one line.

## 1. First compatibility theorem

The short exact coefficient sequence
0 -> F_3 -> A_2(rho) -> F_3 -> 0
is Q_2-equivariant. The LHS filtration is functorial in the coefficient module. Therefore its connecting homomorphism beta_rho induces a morphism between the corresponding LHS spectral sequences.

Consequently, beta_rho^2 cannot be studied solely on the quotient
E_∞^{2,0}=<(R,p)>.
It receives contributions from every filtration piece of total degree 2:
E_∞^{2,0}, E_∞^{1,1}, E_∞^{0,2},
and its target has total degree 3:
E_∞^{3,0}, E_∞^{2,1}, E_∞^{1,2}, E_∞^{0,3}.

Thus any claim that beta_rho^2 is automatically a function only of (R,p) is stronger than the HA45 result and requires additional vanishing or compatibility.

## 2. The crucial new observation: the fiber Bockstein is nontrivial

Although W is central and elementary abelian, H^*(W,F_3) is not concentrated in degree 0 or 1. For W=(F_3)^9,

H^*(W,F_3) ~= Lambda(W^*) tensor Sym(beta W^*)

as a graded algebra.

Hence the coefficient Bockstein acts nontrivially already on the fiber:
beta_W: W^* -> H^2(W,F_3),
and its extension to the polynomial/exterior algebra is nonzero.

Therefore the LHS Bockstein is not merely the Bockstein on the base V applied to the surviving relation line. The fiber rows can contribute to beta_rho^2 after the spectral-sequence differentials are taken into account.

This is a genuine structural reason that the old shortcut
"beta_rho^2 is determined by Theta_(R,p)"
cannot be accepted without proof.

## 3. What remains controlled by (R,p)

The filtration-(2,0) component is controlled.

On the base row j=0, the LHS coefficient map reduces to the ordinary twisted Bockstein on H^*(V,F_3):

d_lambda^V = beta_V + lambda cup(-).

The class represented by the relation jet survives from E_3^{2,0}. Its image in the associated graded target is therefore determined by d_lambda^V applied to that one-dimensional class, provided the resulting class survives the target-side LHS differentials.

This gives a definite partial answer:

- the (2,0) -> (3,0) graded component is a function of (R,p,lambda);
- the full beta_rho^2 may have additional (1,1), (0,2), or extension-induced components.

## 4. New minimal target for the next calculation

The problem has now split cleanly into two pieces.

### A. Base component

Compute d_lambda^V on the one-dimensional relation quotient in H^2(V,F_3), and determine whether its class survives in E_∞^{3,0}.

This is a finite-dimensional exterior/polynomial calculation on V=F_3^4.

### B. Fiber/extension components

Determine the first possible contributions from
E_∞^{1,1} and E_∞^{0,2},
and their images in
E_∞^{2,1}, E_∞^{1,2}, E_∞^{0,3}.

Because the central extension class is the source of d_2 on W^*, these terms are not arbitrary: their first differential is controlled by the same nine-dimensional hyperplane and its relation-jet quotient.

The key question is whether all extra pieces cancel or reduce to a finite additional invariant of e_2.

## 5. Important correction to the selector strategy

HA45 proves a one-dimensional survivor in one filtration layer, not one-dimensional total H^2(Q_2,F_3).

Therefore the phrase "the unique H^2 survivor" must henceforth mean specifically:

"the unique survivor in the base filtration quotient E_∞^{2,0}."

It must NOT be interpreted as dim H^2(Q_2,F_3)=1.

This distinction is load-bearing for the ambient H^2(rho) problem.

## 6. Three possible outcomes

The next calculation can now genuinely distinguish:

1. **Collapse:** all fiber/extension contributions to beta_rho^2 vanish or are determined by the same relation line. Then (R,p) controls the ambient second layer.

2. **Controlled enrichment:** beta_rho^2 requires one or more additional finite low-degree invariants coming from the fiber rows, but these invariants are canonical functions of e_2. Then the true intrinsic carrier is slightly richer than (R,p).

3. **Independent layer:** beta_rho^2 contains information not compressed by the low-degree extension shadow used at mod 9. Then the selector needs a genuinely higher carrier.

The second outcome is now especially plausible structurally, but no outcome is asserted.

## Decision

- LHS functoriality of the coefficient Bockstein: **PASS / CLOSED**.
- Nontrivial fiber Bockstein as an obstruction to the naive collapse: **PASS / CLOSED**.
- (2,0) graded component controlled by (R,p,lambda): **PASS / STRUCTURAL**, subject to target-side survival.
- Full beta_rho^2 determined by (R,p): **OPEN / LOAD-BEARING**.
- Total H^2(Q_2,F_3) being one-dimensional: **NOT CLAIMED / explicitly separated**.
- Next gate: compute the minimal LHS terms in total degrees 2 and 3, beginning with the (2,0)->(3,0) component and the first fiber-row correction.

No broad rho-scan.
