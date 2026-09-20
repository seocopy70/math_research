# HA61-B5-10 — INTRINSIC SECONDARY FAMILY + PURE-CONJUGATION CANCELLATION — 2026-09-20

## Status

**PASS / CLOSED for the intrinsic cohomological secondary object and pure relator-conjugation invariance; FAIL / CLOSED for the proposed diagonal affine quotient as an orientation carrier; HA61-B remains OPEN / LOAD-BEARING.**

This attack was pushed past the earlier formal affine compensator instead of treating it as a gauge quotient.

### 1. Intrinsic object

For a fixed intrinsic primary coefficient character rho_2, define the intrinsic lift set
L(rho_2) = {rho_3 : G -> (Z/27)^× : rho_3 mod 9 = rho_2}.

For every rho_3 in L(rho_2), the exact sequence
0 -> F_3 -> Z/27(rho_3) -> Z/9(rho_2) -> 0
defines a canonical connecting map
delta_{3,rho_3}: H^1(G,Z/9(rho_2)) -> H^2(G,F_3).

Therefore the secondary object is the function-valued family rho_3 |-> delta_{3,rho_3}. It is defined without q, chi, a presentation, Fox coordinates, t_2, or a preferred H^2 generator.

### 2. Gauge/naturality

Representative changes z -> z + d_{rho_2}c leave the connecting image unchanged. Under group isomorphism, naturality of connecting homomorphisms transports the entire family. Hence presentation/lift naturality is **PASS / CLOSED at the cohomological-object level**.

### 3. The diagonal quotient is not legitimate

The earlier formal law
(t_2,mu) -> (t_2+a p, mu+a lambda)
is only an obstruction-preserving compensator. It is not an actual pure-presentation gauge action: under pure relator conjugation the intrinsic rho_3, hence its lift parameter mu, is fixed.

Moreover mu, mu+lambda, mu+2lambda are distinct rho_3 candidates when lambda != 0. Quotienting by the lambda-direction would identify the very alternatives that the secondary obstruction is supposed to distinguish.

Decision: **(t_2,mu)/F_3(p,lambda) as the orientation carrier = FAIL / CLOSED.**

### 4. Exact pure-relator-conjugation check

For r' = v r v^{-1}, a crossed cocycle satisfies exactly
z(r') = z(v) + rho_3(v)z(r) + rho_3(vr)z(v^{-1}) = 0
when z(r)=0 and rho_3(r)=1.

Thus the full crossed-word evaluation is invariant at every filtration order. The isolated degree-three [v,R] term
T([v,R]) = lambda(v)f(p)
cannot be the complete gauge contribution. Its cancellation must occur with the remaining prefix/suffix representative terms; it cannot be repaired by changing intrinsic mu.

This is an exact algebraic cancellation, independent of q and chi.

### 5. Remaining load-bearing boundary

The intrinsic family is now canonical, but the intended filtered compression has not yet been proved. The unresolved tasks are:

1. expand the full delta_3 coordinate formula through the P_4 threshold;
2. identify the P_4 residual with a presentation-independent filtered datum t_2, or prove that no such single datum exists;
3. show that all E_{>P_4} contributions vanish or factor through the same datum;
4. prove functoriality under the declared filtered input category and fix the remaining common H^2 normalization issue;
5. only then test universal zero uniqueness.

No HA61-C and no all-n induction is authorized yet.

### Classification

- intrinsic coefficient-lift domain: **PASS / CLOSED**;
- intrinsic function-valued secondary connecting obstruction: **PASS / CLOSED**;
- pure relator-conjugation invariance: **PASS / CLOSED**;
- formal diagonal compensator: **PASS / LOCAL**;
- diagonal affine quotient as orientation carrier: **FAIL / CLOSED**;
- P_4 residual -> intrinsic t_2: **OPEN / LOAD-BEARING**;
- E_{>P_4} factorization/vanishing: **OPEN / LOAD-BEARING**;
- HA61-B overall: **OPEN / LOAD-BEARING**;
- HA61-C: **not opened**.

## Immediate next attack

Keep the exact intrinsic delta_3 fixed. Perform the source-complete mod-27 / division-by-9 ledger for the P_4 generators, retaining prefix/suffix terms together with the relation-jet terms. The decisive question is whether the surviving functional on the primary-zero domain has rank one and is represented by a natural filtered datum. A failure closes B negatively; a proof opens the final bridge toward C.

Record: `research/HA61_B5_10_INTRINSIC_SECONDARY_FAMILY_AND_CONJUGATION_2026-09-20.md`.

