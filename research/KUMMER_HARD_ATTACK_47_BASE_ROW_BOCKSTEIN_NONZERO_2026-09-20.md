# HARD ATTACK 47 — BASE-ROW TWISTED BOCKSTEIN IS NONZERO

Date: 2026-09-20

## Target

HA46 reduced the next gate to the filtration-(2,0) component of the LHS coefficient Bockstein. The purpose here is to compute that component explicitly before touching fiber rows.

We work with V=F_3^4 and the standard presentation
H^*(V,F_3) = Lambda(e_1,e_2,e_3,e_4) tensor F_3[b_1,b_2,b_3,b_4],
where deg(e_i)=1, deg(b_i)=2 and beta(e_i)=b_i, beta(b_i)=0. Signs are with the usual graded Leibniz convention. The relation-jet survivor is represented, up to the already isolated common normalization/sign convention, by

z_R = b_1 + e_1 e_2 + e_3 e_4.

This identification is used only as the coordinate realization of the already intrinsic line <(R,p)>; it is not a new presentation-dependent definition.

## 1. General base-row formula

For lambda in V^*=H^1(V,F_3), the twisted Bockstein on the base row is

d_lambda^V = beta_V + lambda cup (-).

Therefore

d_lambda^V(z_R)
= b_1 e_2 - e_1 b_2 + b_3 e_4 - e_3 b_4
  + lambda b_1 + lambda e_1e_2 + lambda e_3e_4,

where the displayed expression is interpreted in H^3(V,F_3) and lambda b_1 means the degree-3 product.

Thus the base-row image is not identically zero as a formal consequence of the relation-jet line. The naive possibility that the second Bockstein automatically vanishes on the surviving line is already ruled out at the base-row level.

## 2. The q=3 candidate lambda=e_2

The already established mod-9 selector for q=3 is lambda=e_2^* (written e_2 in the base cohomology notation). Substitution gives

d_{e_2}^V(z_R)
= 2 b_1 e_2 - e_1 b_2 + b_3 e_4 - e_3 b_4 + e_2e_3e_4.

The five displayed monomials lie in distinct basis directions of H^3(V,F_3): four polynomial-exterior monomials and one exterior cubic. Hence

d_{e_2}^V(z_R) != 0.

This is an actual structural calculation, not a numerical rho-scan.

## 3. What this proves — and what it does not

The calculation proves:

1. The base filtration component of beta_rho^2 on the relation-jet line is generally nonzero.
2. In particular, at the known q=3 mod-9 character lambda=e_2, the raw (2,0)->(3,0) base-row contribution is nonzero.
3. Therefore any eventual vanishing/rank cancellation relevant to beta_rho^2 cannot come from the base Bockstein alone; it must involve target-side LHS structure and/or fiber/extension corrections.

It does NOT yet prove that the class survives to E_infinity^{3,0}. A later LHS differential, most importantly an incoming differential into (3,0), can kill it. Consequently we must not identify this nonzero E_2-base-row calculation with a nonzero class in the associated graded target.

This distinction is load-bearing.

## 4. A useful conceptual consequence

The old three-way split can now be sharpened.

- Pure Collapse in the strongest sense ("beta_rho^2 is zero/determined solely by the raw base relation line with no target/fiber correction") is incompatible with the explicit base calculation.
- A weaker Collapse remains logically possible if the nonzero base-row term is canonically killed by the LHS target differential in a way already forced by (R,p).
- Controlled Enrichment becomes a concrete possibility if that killing requires an additional finite shadow of the central extension class.
- Independent Layer remains possible if the surviving correction cannot be compressed into the low-degree e_2 data.

Thus the next question is no longer whether the base row is interesting: it is exactly which LHS differential controls the fate of the displayed H^3(V) class.

## 5. Next gate: target-side E_infinity^{3,0}

For the central extension 1 -> W -> Q_2 -> V -> 1, the only possible incoming LHS differential to (3,0) after d_2 is

d_3: E_3^{0,2} -> E_3^{3,0}.

There is no outgoing differential from (3,0) because the fiber degree is already 0. Therefore

E_infinity^{3,0} = E_4^{3,0} = E_3^{3,0}/im(d_3^{0,2}).

The immediate task is consequently to compute the class of d_{e_2}^V(z_R) modulo im(d_3^{0,2}). This is the first genuinely decisive target-side calculation.

The source E_3^{0,2} is controlled by the central fiber W and by the same extension class whose d_2 on W^* has rank 9. No broad rho-scan is needed.

## Decision

- explicit base-row formula d_lambda^V(z_R): **PASS / CLOSED** under standard cohomology normalization;
- nonzero raw base-row value at lambda=e_2: **PASS / CLOSED**;
- nonzero E_infinity^{3,0} value: **OPEN / LOAD-BEARING**;
- determination of beta_rho^2 from (R,p): **OPEN / LOAD-BEARING**;
- unique coker maximizer without PD^2: **OPEN / DECISIVE**;
- no broad rho-scan authorized.
