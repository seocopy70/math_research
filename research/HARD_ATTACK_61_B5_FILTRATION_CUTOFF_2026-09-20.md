# HA61-B5 — FILTRATION CUTOFF / HIGHER-TERM AUDIT — 2026-09-20

## Status

**HA61-B5: OPEN / LOAD-BEARING.**

The requested naive cutoff “all E_{>=4} terms vanish modulo 27 after division by 9” is false in general. The correct B5 target is therefore not total vanishing of the D_4 sector, but isolation of its surviving /9 residual and proof that this residual is exactly the next filtered datum t_2 rather than an independent coefficient-action invariant.

## 1. Pre-check

- **Object:** the secondary connecting obstruction for
  0 -> F_3 -> A_3=Z/27(rho_3) -> A_2=Z/9(rho_2) -> 0.
- **Input:** the primary-zero A_2 lift, the degree-(2,3) relation data already audited, and the D_4/higher relation error.
- **Excluded:** q, the known canonical orientation, and any presentation-specific numerical normalization.
- **Gate:** determine the exact contribution of E_{>=4} after division by 9 mod 3.

## 2. The first hard obstruction to a blanket cutoff

The earlier mod-9 theorem used D_4 membership successfully because the trivial-action contribution of a D_4 error has exponent sum divisible by 9, hence becomes zero after division by 3 and reduction mod 3.

At the mod-27 secondary stage we divide by 9 instead. The same argument no longer kills the D_4 sector.

Indeed, for a generator g and any crossed cocycle z reducing to f,

  z(g^9) = (1 + rho(g) + ... + rho(g)^8) z(g).

With rho(g)=1+3a mod 27, the coefficient satisfies

  1 + rho(g) + ... + rho(g)^8 = 9 mod 27,

because the terms linear in 3a and quadratic in 3a are already multiples of 27. Hence

  z(g^9)/9 = f(g) mod 3.

But g^9 lies in D_4(F). Therefore

  D_4-error does NOT imply zero after the /9 secondary normalization.

This is a proof-level reason that the old mod-9 D_4 cutoff cannot simply be recycled one level higher.

## 3. What survives from D_4

The surviving D_4 contribution is not arbitrary.

The Zassenhaus description
  D_4 = product_{3^j i >= 4} gamma_i(F)^{3^j}
shows that the first potentially visible /9 contributions arise from the next p-power / lower-3-central layer. In particular, the gamma_1^9 component already gives the explicit residual above.

Other D_4 generators are subject to additional divisibility because:
- commutator values of a mod-3 cocycle lift are already constrained by the primary coefficient-extension structure;
- p-th powers of elements whose cocycle value is already divisible by 3 acquire an additional factor of 3;
- higher commutator layers have zero ordinary exponent sum and can only enter through the twisted correction terms.

Thus B5 cannot legitimately label the whole D_4 sector “zero”; it must decompose it by source and valuation.

## 4. Corrected B5 decomposition

Write

  E_{>=4} = E_{P_4} + E_{>P_4},

where E_{P_4} is the first lower-3-central / power-relation residual and E_{>P_4} is deeper.

The authorized question is now:

1. prove that E_{P_4}/9 is the canonical next residual t_2 (up to the already fixed projective/common H^2 gauge);
2. prove that E_{>P_4}/9 = 0 in the secondary quotient, or factors through the same t_2 datum;
3. prove that no independent rho_2-action scalar survives in these terms.

This is exactly the “source -> valuation -> filtration -> quotient” audit required by the continuity protocol.

## 5. Relation to HA58/HA59

HA58 already established, on the standard family, that the P_4 residual is nonzero for q=9 and zero for 27|q, while being directionally aligned with the mod-9 orientation line. HA59 identified the coker/obstruction quotient as the natural place where gauge directions should be removed.

B5 now supplies the missing logical boundary:

- HA58's residual is plausibly the first surviving part of E_{>=4};
- this does NOT yet prove that every higher term is absorbed by t_2;
- therefore HA61-C cannot yet be opened.

## 6. Important negative result

The statement

  “r' = r mod D_4  =>  secondary obstruction unchanged mod 27”

is **FALSE without an additional quotient/vanishing hypothesis**.

The counter-mechanism is the D_4 element g^9, whose divided secondary evaluation is f(g).

Thus D_4 is exactly the correct cutoff for the first mod-9 obstruction, but not for the second mod-27 obstruction.

This is a genuine filtration-depth boundary, not a technical nuisance.

## 7. Current decision

- **Blanket E_{>=4} vanishing at mod 27:** FAIL / CLOSED.
- **D_4 membership as sufficient cutoff:** FAIL / CLOSED.
- **Identification of the surviving D_4/P_4 residual with intrinsic t_2:** OPEN / LOAD-BEARING.
- **Vanishing/factorization of deeper-than-P_4 terms:** OPEN.
- **Independent old-rho_2 term:** still OPEN until the corrected source decomposition is completed.
- **HA61-B overall:** OPEN / LOAD-BEARING.
- **HA61-C:** not opened.

## 8. Next authorized attack

Do not perform a broad scan.

Compute the secondary evaluation on the generators of the first residual layer explicitly:
- g^9-type power terms;
- gamma_2^3-type terms;
- the corresponding P_3/P_4 relation-power generators.

Then quotient by the already established mod-9 gauge image and test whether all surviving classes define one linear functional f -> f(t_2).

Only if that quotient is one-dimensional in the required sense, with presentation/gauge naturality, may HA61-C begin.
