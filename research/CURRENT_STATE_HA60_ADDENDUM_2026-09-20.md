# HA60 CURRENT-STATE ADDENDUM — 2026-09-20

## HARD ATTACK 60 — coefficient-extension diagram

HA60 constructs the correct two-stage coefficient-extension ladder for the mod-27 attack.

The key correction is that the next connecting map does **not** literally reduce to the mod-9 connecting map. Instead:
- delta_2 is the primary obstruction for lifting H^1(G,F_3) to A_2=Z/9(rho_2);
- after delta_2=0 and an A_2-valued lift exists, delta_3 for
  0 -> F_3 -> A_3=Z/27(rho_3) -> A_2 -> 0
  is the secondary obstruction to lifting that A_2 class.

For rho_3=rho_2(1+9mu), the next obstruction has the same quadratic term governed by R and a new power term t_2 from the P_3/P_4 residual:
delta_3(z)=[z_bar(t_2)+(mu wedge z_bar)(R)]omega.

For the standard rank-four family:
- q=9 gives t_2=X_1^(1), and direct mod-27 crossed-word evaluation gives the unique mu=e_2^*;
- q=3 gives the compatible next digit mu=0;
- 27|q gives t_2=0 and mu=0.

Thus the P_4 scalar is fixed by the canonical filtered power map inside the coefficient-extension obstruction, rather than chosen from q or chi.

### Decisions
- coefficient-extension diagram / successive obstruction at mod 27: **PASS / CLOSED**
- P_4 reduction-compatibility with mod-9 mechanism: **PASS / CLOSED** for the audited standard-family two-stage theorem
- P_4 scalar normalization: **PASS / CLOSED** for the mod-27 coefficient-extension construction
- general arbitrary-input presentation-free identification of t_2: **OPEN / LOAD-BEARING**
- all-digit coefficient-extension induction: **OPEN / DECISIVE**
- 19D LHS sector as first new layer: **HISTORICAL / SUPERSEDED strategically**

Record: `research/HARD_ATTACK_60_COEFFICIENT_EXTENSION_DIAGRAM_2026-09-20.md`.
