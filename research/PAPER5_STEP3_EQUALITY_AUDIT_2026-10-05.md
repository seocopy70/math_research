# Paper 5 — Step 3 Equality Audit (2026-10-05)

## Classification

**FAIL / CLOSED as a proof attempt; Step 3 remains OPEN / LOAD-BEARING.**

The submitted argument does establish several useful congruences, but it does **not** prove the decisive implication
[
\tilde g_{a,b}(R)\subseteq R.
]
Therefore it does not yet establish
[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p).
]

## 1. Valid local calculations

With
[
F=\langle x,y,z\rangle,quad
R_0=\langle[x,z],[y,z]\rangle^F,quad
\rho=[x,y]^{-1}x^pz^{-p},quad R=R_0\langle\rho\rangle^F,
]
the following parts are usable after correcting the relation-order/sign notation.

- In (F/R_0), (z) is central, so commutators with (z^p) vanish there.
- Since (x^p\in D_p(F)), one has ([y,x^p]\in D_{p+1}(F)).
- The degree-(ge3) commutator terms in the Hall collection formula for ([x^a,y]) lie in (gamma_3(F)), and the previously established estimate
  [
  \gamma_3(F)\subseteq [F,R]D_{p+1}(F)
  ]
  is sufficient for the stated congruence modulo ([F,R]D_{p+1}), provided the group commutator convention is kept consistent.
- Hall–Petrescu gives
  [
  (x^a)^p\equiv x^{ap}\pmod{D_{p+1}(F)},qquad
  (z^a)^p\equiv z^{ap}\pmod{D_{p+1}(F)}.
  ]
- Consequently the intended first-order relation calculation
  [
  \tilde g_{a,b}(\rho)\equiv \rho^a
  ]
  modulo (R D_{p+1}(F)) is a plausible and useful congruence.

## 2. Definite notation/sign correction

From
[
\rho=[x,y]^{-1}x^pz^{-p},
]
the defining relation is
[
[x,y]=x^pz^{-p}
]
in the quotient (with the chosen commutator convention). The displayed replacement
[
[x,y]=\rho z^px^{-p}
]
in the submitted proof is not an exact identity and has the inverse/order reversed.

Thus the displayed derivations of ([x,[x,y]]) and ([y,[x,y]]) must be rewritten from the actual defining relation (or explicitly stated only as congruences modulo (R) and the relevant filtration). This is repairable, but it prevents the submitted display from being accepted verbatim as a proof.

## 3. Decisive gap: the pro-p induction is invalid as stated

The submitted argument concludes:

> if (\tilde g(R)\subseteq R D_{p+1}(F)), then a standard pro-(p) induction gives (\tilde g(R)\subseteq R).

This implication is **not established**.

Knowing only
[
\tilde g(R)\subseteq R D_{p+1}
]
shows that (\tilde g) preserves (R) only modulo the first deeper Zassenhaus layer. It does **not** automatically imply
[
\tilde g(R)\subseteq R D_{p+2},
]
and hence cannot be iterated to the limit without an additional contraction/induction mechanism.

In particular, the phrase “(D_{p+1})에서 (R)을 이용해 (D_{p+2})까지 올리고 귀납” omits the actual lemma needed to perform that lift. The facts (R) is closed and ([F,R]subseteq R) do not by themselves supply it.

A valid closure would need one of the following, proved explicitly:

1. a genuine filtered lifting lemma showing
   [
   \tilde g(R)\subseteq R D_m\Longrightarrow
   \tilde g(R)\subseteq R D_{m+1}
   ]
   for every (m\ge p+1); or
2. an independent presentation-theoretic argument that (\tilde g) maps each normal generator of (R) into (R); or
3. an automorphism/lift argument in which the kernel (R) is shown invariant by an exact relation-module calculation.

None is supplied in the submitted Step 3 proof.

## 4. Consequence for equality

The free-pro-(p) Frattini argument can be used **only after** kernel preservation is established. Once an endomorphism descends to (W_n) and induces an invertible map on (V=F/D_2(F)), the Frattini criterion can promote the descended endomorphism to an automorphism. It cannot itself prove that (R) is invariant.

Therefore the chain
[
\tilde g(R)\subseteq R
\Rightarrow
\tilde g\text{ descends to }W_n
\Rightarrow
S_{11}(p)\subseteq\operatorname{Im}
]
is sound in structure, but its first implication remains unproved.

## 5. Result classification

- (\gamma_3(F)\subseteq[F,R]D_{p+1}(F)): **PASS / LOCAL-GENERAL SUPPORT**, subject to a convention-consistent rewrite.
- (\tilde g(\rho)\equiv\rho^a\pmod{R D_{p+1}}): **PASS / LOCAL-GENERAL SUPPORT**, not yet kernel preservation.
- (\tilde g(R)\subseteq R): **FAIL / CLOSED as submitted proof**.
- Step 3 lower-bound equality: **OPEN / LOAD-BEARING**.
- [
  \operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p)
  ]
  : **CONDITIONAL / not promoted**.
- (p^2(p-1)) automorphism-order theorem: **CONDITIONAL / not promoted**.

## 6. Authorized next gate

Do not search for more numerical confirmation of the (S_{11}) formula yet. The next proof gate is specifically the missing **kernel-invariance lifting lemma** for (R\triangleleft F), starting from the congruence
[
\tilde g(\rho)\equiv\rho^a\pmod{R D_{p+1}}.
]
The proof must explicitly control the successive Zassenhaus layers or replace the induction by an exact relation-module argument.

