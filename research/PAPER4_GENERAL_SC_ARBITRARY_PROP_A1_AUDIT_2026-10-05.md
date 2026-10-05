# Paper 4 — General SC arbitrary pro-p audit (2026-10-05)

## Claim under audit

For every pro-p group G, every open K<=G with [G:K]=p^s,
D_n(G) cap K <= D_{ceil(n/p^s)}(K).

The proposed proof reduces to index p and uses three augmentation-ideal lemmas.

## Verdict

**FAIL / CLOSED as a proof.**

The proposed Lemma 2 is false in general. Consequently Lemma 3 does not follow, and the claimed arbitrary-pro-p theorem remains **OPEN** unless a different proof is supplied.

This audit does **not** invalidate the already certified free-pro-p SC/SC_s result used by Paper 4.

## Fatal point: Lemma 2

The asserted identity
I_G^n = sum_{j=0}^n I_K^{n-j} t^j B
is not valid for a general index-p extension.

The problem is that t=a-1 does not commute with I_K. Normality of K only gives conjugation invariance of I_K. In general,
t x = (a x a^{-1}-x) + (a x a^{-1})t,
and the first term need only lie in I_K, not in I_K^2.

### Concrete witness

Let p be odd and let G be the exponent-p Heisenberg group
G=<x,y,z | x^p=y^p=z^p=1, [x,y]=z, z central>.
Put K=<x,z>, so K is normal of index p and K is abelian. Let a=y and t=y-1.

Then
t(x-1) = (y-1)(x-1) = x(z-1) + (xz-1)t
(up to the harmless convention for the commutator orientation; the key A-component is x(z-1)).

Because K is abelian, z-1 is in I_K but not in I_K^2. Hence the A-component of t(x-1) has I_K-degree 1.

But the proposed n=2 right-hand side is
I_K^2 B + I_K t B + t^2 B.
In the A=K basis decomposition B=A direct-sum A t (for p=2) / A-basis 1,t,...,t^{p-1} in general, its A-component is contained in I_K^2. Therefore t(x-1) belongs to I_G^2 but not to the proposed right-hand side.

Thus Lemma 2 fails.

## Consequence for Lemma 3

The proof of Lemma 3 also contains a second independent gap: it analyzes the t^j factor while treating y_j as though its A-basis expansion could not contribute additional t-powers. But y_j is an element of I_K^{n-j}B, not merely an element of I_K^{n-j}. Its B-coordinate expansion can contain t^k terms, and combinations with j can return to the A-component.

Therefore the statement that only j divisible by p can contribute to the A-component is unjustified.

## Status

- Lemma 1 (finite-index freeness / triangular basis): **PASS / LOCAL/standard**, subject to the chosen completed group-algebra formulation.
- Lemma 2 as stated: **FAIL / CLOSED**.
- Lemma 3 as derived from Lemma 2: **FAIL / CLOSED as this proof route**.
- Arbitrary-pro-p SC: **OPEN**.
- Free-pro-p SC/SC_s used by Paper 4: **unchanged, PASS / CLOSED**.
- No Paper-4 core theorem is weakened by this audit.

## Literature check

A targeted search did not locate, in the searched sources, an immediately usable theorem proving this exact arbitrary-pro-p subgroup-depth comparison. General dimension-subgroup/Jennings-Lazard properties are standard, but they do not by themselves certify this intersection estimate.

Therefore no arbitrary-pro-p promotion is made.

## Authorized next step

If this generalization is pursued, first seek a genuinely functorial dimension-subgroup argument (or a published theorem stated at this exact level). Do not repair Lemma 2 by assuming commutation of I_K with t; that would silently reintroduce a false hypothesis.

