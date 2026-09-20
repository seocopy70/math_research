# HA61-B5-8 — INTRINSIC SECONDARY OBSTRUCTION AS A FUNCTION ON COEFFICIENT LIFTS — 2026-09-20

## Verdict

PASS / CLOSED at the intrinsic cohomological-object level; HA61-B remains OPEN / LOAD-BEARING.

The correct secondary object is not the affine quotient of (t_2,mu). It is the naturally defined family of connecting obstructions indexed by the intrinsic coefficient characters rho_3 lifting a fixed rho_2:

  L(rho_2) = {rho_3 : G -> (Z/27)^× | rho_3 mod 9 = rho_2}.

For each rho_3, the exact sequence

  0 -> F_3 -> Z/27(rho_3) -> Z/9(rho_2) -> 0

defines a canonical connecting map

  delta_{3,rho_3}: H^1(G,Z/9(rho_2)) -> H^2(G,F_3).

Thus the intrinsic secondary object is the function-valued family rho_3 -> delta_{3,rho_3}.

## 1. Object and legitimacy

The definition uses only the intrinsic group G, the intrinsic coefficient character rho_2, and a candidate coefficient character rho_3. No presentation, relator word, Fox coordinate, t_2, or preferred H^2 generator enters.

Because admissible rho_3 are congruent to 1 modulo 3, the kernel 9 Z/27(rho_3) is canonically a trivial F_3-module, so the displayed coefficient sequence is intrinsic.

## 2. Lift-representative gauge

The connecting homomorphism is defined on H^1, not on a chosen cocycle. If z is replaced by z + d_{rho_2} c, its connecting image is unchanged. Hence the A_2 lift-representative gauge is already removed by the cohomological construction.

## 3. Presentation/naturality

For an isomorphism alpha:G' -> G carrying the coefficient data to the corresponding data on G', pullback gives a morphism of the two short exact coefficient sequences. Naturality of connecting homomorphisms gives the commutative relation

  alpha^* delta_{3,rho_3} = delta_{3,rho_3 o alpha} alpha^*.

For a pure relator-conjugation change representing the same abstract group, the intrinsic coefficient character rho_3 is unchanged. Therefore the intrinsic obstruction function is unchanged.

Conclusion: presentation/lift naturality of the function-valued secondary obstruction is PASS / CLOSED at the cohomological-object level.

## 4. Consequence for mu

Writing rho_3 = rho_2(1+9 mu) is a coordinate description of a point of L(rho_2), not a gauge coordinate to be quotiented.

When lambda != 0, mu, mu+lambda, and mu+2 lambda are distinct coefficient characters modulo 27. The obstruction is supposed to distinguish these alternatives.

Therefore the simple quotient (t_2,mu) / F_3(p,lambda) is ruled out as the intrinsic orientation carrier. This strengthens HA61-B5-7.

## 5. Coordinate formula: the new diagnostic

In a chosen presentation, after choosing an H^2 generator omega, one may obtain a coordinate formula of the form

  delta_{3,rho_3}(f) = [ f(t_2) + (mu wedge f)(R) ] omega.

The intrinsic theorem above does NOT prove that t_2 is intrinsic.

Instead it forces a precise consistency condition. Under pure relator gauge, rho_3 and intrinsic mu remain fixed, while the left side remains fixed. Therefore any change in the displayed t_2 term must be cancelled by the remaining representative-level terms.

In particular, the previously computed [v,R] contribution T = lambda(v) f(p) cannot be cancelled by declaring mu -> mu + lambda(v). The full coordinate expansion must contain another compensating contribution, or the present source decomposition is incomplete.

This is a concrete source-audit target, not an assumption.

## 6. Intrinsic zero selector

Define the admissible primary-zero domain as the classes f for which the first obstruction vanishes and an A_2 lift exists. The intrinsic secondary zero locus is

  Z_3 = {rho_3 in L(rho_2) : delta_{3,rho_3}(f)=0 for every admissible primary-zero f}.

Uniqueness of the zero is PASS / LOCAL only on the already audited standard-family normal forms. No universal uniqueness theorem is claimed.

## 7. Exact boundary

Closed:
- intrinsic coefficient-lift domain;
- intrinsic function-valued secondary connecting obstruction;
- lift-representative independence;
- presentation/naturality of that obstruction family;
- affine quotient of (t_2,mu) by (p,lambda) as orientation carrier: FAIL / CLOSED.

Open:
- presentation-free filtered t_2;
- complete coordinate expansion of delta_3;
- P_4 residual -> t_2 identification;
- deeper-than-P_4 factorization/vanishing;
- universal zero uniqueness;
- all-digit induction.

Therefore HA61-B remains OPEN / LOAD-BEARING and HA61-C remains unopened.

## 8. Next authorized attack

Do not open HA61-C and do not perform an all-n induction.

The next attack is a coordinate-completeness/source audit: freeze the intrinsic delta_3; expand it through the P_4 threshold; track separately [v,R], gamma_1^9, gamma_2^3, lift-gauge, and deeper sources; use intrinsic invariance to solve for the missing compensating term under pure relator conjugation; then test whether the surviving quotient is exactly one functional f -> f(t_2).

Only after that may the P_4-to-t_2 identification and deeper-term factorization be promoted.