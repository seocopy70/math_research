# HARD ATTACK — Kummer recognition through the lower 3-central quotient — 2026-09-20

## Purpose

Test the proposed second-stage claim that the level-(3^k) orientation can be recognized from
[
Q_k=G/P_{k+1}
]
by a q-blind Kummer/crossed-homomorphism condition.

The attack is deliberately split into two questions:

1. **Factorization:** if a candidate orientation character (ho) and a crossed homomorphism are given, does the relevant semidirect-product data factor through (Q_k)?
2. **Recognition:** does (Q_k) itself contain a non-circular condition that selects the canonical (ho) uniquely?

The first can be proved. The second is the load-bearing theorem and is not yet established.

## 1. Finite semidirect target

Put
[
A_k=mathbf Z/3^k,qquad U_k=1+3A_ksubset A_k^	imes,
]
and
[
H_k=A_ktimes U_k
]
with (U_k) acting on (A_k) by multiplication.

A pair
[
(ho,f),qquad
ho:G	o U_k,quad
f:G	o A_k
]
with
[
f(gh)=f(g)+ho(g)f(h)
]
is equivalent to a homomorphism
[
Phi_{ho,f}:G	o H_k,qquad
gmapsto(f(g),ho(g)).
]

This removes one apparent circularity: (ho) may be treated as a variable candidate, rather than being supplied as the answer.

## 2. Factorization lemma

The lower 3-central series of (H_k) satisfies
[
P_{k+1}(H_k)=1.
]

Reason: if (t=(1,1)) denotes the translation generator and (u) a generator of (U_k), then (t) has order (3^k), (u) has order dividing (3^{k-1}), and
[
[t,u]in 3A_k,
]
with each successive commutator/power step increasing the 3-adic divisibility of the translation part. Equivalently,
[
P_n(H_k)subseteq 3^{,n-1}A_k	imes(1+3^nA_k),
]
so (P_{k+1}(H_k)=1).

Therefore every homomorphism
[
Phi:G	o H_k
]
kills (P_{k+1}(G)). In particular, every pair ((ho,f)) of the above kind factors through
[
Q_k=G/P_{k+1}(G).
]

Thus the proposed quotient depth is sufficient for **finite semidirect Kummer data once the candidate (ho) is included as a variable**.

## 3. The critical obstruction

This does **not** prove
[
chimod 3^k	ext{ is determined by }Q_k.
]

The missing statement is a genuine recognition theorem:

> There must exist a predicate (mathsf K_k(Q,ho)), defined solely from the finite group (Q), the candidate character (ho:Q	o U_k), and declared q-blind finite structure, such that for every admissible Demuškin object:
> [
> mathsf K_k(Q_k,ho)iff ho=chimod3^k,
> ]
> with uniqueness among all candidate (ho).

The factorization lemma only says that crossed-homomorphism data can be evaluated on (Q_k). It does not produce (mathsf K_k).

## 4. Why the naive Kummer condition is insufficient

If the condition is merely
[
exists f:G	o A_k(ho)
]
with (f) a crossed homomorphism, it is vacuous: (f=0) works for every candidate (ho).

If one requires (f
eq0), this is still not a canonical selector without an additional distinguished class, normalization, obstruction, or universal property. Such additional data is exactly what must be shown to be intrinsic and q-blind.

If instead the condition is expressed as a Demuškin duality condition characterizing the orientation module, then it may select (chi), but this risks simply reintroducing the already-known canonical dualizing action/classification theorem rather than extracting orientation from the intended finite filtered input.

Hence the phrase “Kummer recognition” cannot be used as a theorem until the actual predicate is written down and proved to have the required uniqueness.

## 5. Candidate-character space is genuinely nontrivial

On (Q_k), candidate characters
[
ho:Q_k	o U_k
]
are generally plentiful. Since (U_k) is abelian, every such character factors through (Q_k^{ab}). In the standard family, the abelianized finite quotient has several independent cyclic directions, so the quotient does not itself single out the (x_2)-direction.

Therefore uniqueness cannot come from the existence of a character alone. It must come from an additional q-blind finite obstruction.

This is precisely where the earlier mod-9 projective carrier succeeded: the cup+Bockstein relation functional supplied a distinguished finite obstruction. No analogous level-(k) obstruction has yet been defined from (Q_k) alone.

## 6. Sharp logical boundary

The current result is therefore:

- (P_{k+1}) is **sufficient as a factorization depth for candidate semidirect/Kummer data**.
- (P_{k+1}) is **not yet proved to be an orientation-recognition carrier**.
- The statement “(chimod3^k) is determined by (G/P_{k+1})” remains too strong until a q-blind unique recognition predicate is constructed.
- The information-boundary theorem remains valid only at the standard-family finite-quotient/isomorphism-class level.

This is not a failure of the lower-central threshold theorem. It is the exact boundary between **finite information sufficiency for candidate data** and **canonical orientation recognition**.

## 7. Decision

**Kummer factorization through (G/P_{k+1}): PASS / LOCAL.**

**Finite Kummer recognition theorem (Q_kRightarrowchimod3^k): OPEN.**

No numerical scan is authorized until an explicit predicate (mathsf K_k) is defined. The next attack must either:

1. construct such a predicate from genuinely q-blind finite filtered data and prove uniqueness/naturality; or
2. prove a no-go by producing admissible objects with the same allowed finite carrier but different orientation data.

In particular, no claim of a canonical orientation selector from (G/P_{k+1}) should be made at this stage.
