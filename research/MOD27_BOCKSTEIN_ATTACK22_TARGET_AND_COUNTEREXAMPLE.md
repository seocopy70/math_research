# HARD ATTACK 22 — FORMAL MOD-27 TARGET AND COUNTEREXAMPLE TEST — 2026-09-20

## 0. Purpose

Hard Attack 21 repaired the standard-family classification gap but left the decisive universal question open. This attack first formalizes the target \(O_{27}\), then attempts the strongest available counterexample test before any new carrier is invented.

## 1. Basis-free target \(O_{27}\)

For an infinite pro-3 Demushkin group \(G\), the canonical orientation is the intrinsic character
\[
\chi_G:G\to 1+3\mathbf Z_3.
\]
This is not a chosen basis vector. It is the character coming from the action on the dualizing module; literature also characterizes it as the unique orientation making \(G\) 1-cyclotomic.

Reduce modulo \(27\):
\[
\chi_{27}:G\to (1+3\mathbf Z_3)/(1+27\mathbf Z_3).
\]
On \(1+3\mathbf Z_3\), the truncated logarithm gives a canonical group isomorphism
\[
\frac13\log:
(1+3\mathbf Z_3)/(1+27\mathbf Z_3)
\;\xrightarrow{\sim}\;
\mathbf Z/9.
\]
Therefore the additive logarithmic orientation
\[
\lambda_{27}(G):=\frac13\log\chi_G\pmod9
\]
is itself a basis-free element of
\[
H^1(G,\mathbf Z/9)=\operatorname{Hom}_{\mathrm{cont}}(G,\mathbf Z/9).
\]

Define \(O_{27}(G)\) to be the singleton distinguished-orientation object
\[
O_{27}(G)=\{\lambda_{27}(G)\},
\]
with morphisms transported by pullback along admissible group isomorphisms. Equivalently, the target can be regarded as the natural subfunctor of \(H^1(-,\mathbf Z/9)\) selecting the canonical logarithmic orientation class.

This removes the previous ambiguity in the notation \(O_{27}\). The desired bridge is an actual natural transformation
\[
\Phi_{27}:\mathcal B_{27}\Longrightarrow O_{27},
\]
not merely a coordinate formula for \(e_2\).

## 2. Immediate structural observation

The target class \(\lambda_{27}\) lies in the underlying module
\[
W=H^1(G,\mathbf Z/9)
\]
already present in \(\mathcal B_{27}\).

For \(q=3\), however, the carrier structure determines the mod-3 reduction of the distinguished direction but does not, at the abstract-module level, distinguish its characteristic-zero lift. Explicitly, if \(e_2\) denotes the mod-3 direction selected by the cup pairing and \(\beta_1\), then
\[
e_2,\quad 4e_2,\quad 7e_2,\quad \ldots
\]
represent different lifts in \(W\) with the same reduction whenever they differ by multiplication by a unit congruent to \(1\pmod3\). The map
\[
S(a_1,a_2,a_3,a_4)=(a_1,4a_2,a_3,a_4)
\]
is an automorphism of the abstract structured carrier.

Thus there is **no natural transformation from the abstract carrier category** \(\mathcal C_{27}^{abs}\) to \(O_{27}\) that selects \(\lambda_{27}\): S fixes every declared carrier datum while moving the desired lift.

This is a genuine theorem about the abstract carrier category.

## 3. Why this is not yet a theorem in the project's admissible category

The project's input morphisms are induced by continuous group isomorphisms and declared presentation/gauge transformations. S has not been shown to be induced by such a morphism.

Indeed, if a group automorphism \(\alpha\) of \(G_3\) induced S on \(H^1(G_3,\mathbf Z/9)\), naturality of the canonical orientation would force
\[
\lambda_{27}\circ\alpha=\lambda_{27}.
\]
But S sends the \(x_2\)-coordinate to \(4\) times itself, whereas
\[
\lambda_{27}(x_2)=1\pmod9.
\]
Hence S cannot be induced by an admissible group automorphism of \(G_3\).

This proves the opposite of the desired realizability: the abstract symmetry is specifically blocked by the canonical orientation itself.

That is important evidence, but it is not a counterexample pair. It says the missing rigidity is precisely group-level information that the declared carrier has forgotten.

## 4. Counterexample-pair test

The decisive no-go would be admissible \(G,G'\) such that
\[
\mathcal B_{27}(G)\cong\mathcal B_{27}(G')
\]
while
\[
O_{27}(G)\not\cong O_{27}(G').
\]

### Standard Demushkin family

This test fails to produce such a pair:

- \(v_3(q)=1,2,\ge3\) give three distinct full carrier types.
- Within each valuation class in the standard family, the mod-27 logarithmic orientation has the corresponding fixed class:
  \[
  e_2,\quad 3e_2,\quad 0
  \]
  after the standard model identifications.
- Since the only admissible q-values in the odd-prime standard classification are the powers \(3^s\) (plus the power-free \(q=0\) case), there is no second standard-family object with the same full carrier type but a different \(\lambda_{27}\).

Therefore no genuine admissible counterexample pair has been found.

## 5. Literature boundary

The canonical orientation is known independently as the action on the dualizing module, and for infinite Demushkin groups it is the unique orientation giving the relevant 1-cyclotomic structure. The standard presentation then gives
\[
\chi(x_2)=(1-3^s)^{-1},\qquad \chi(x_i)=1\;(i\ne2).
\]
These facts validate the target definition and explain why an admissible automorphism cannot realize S. They do not provide the desired factorization through \(\mathcal B_{27}\).

## 6. Decision

- basis-free \(O_{27}\) target formalization: **PASS / CLOSED**;
- abstract-carrier no-go under all structure-preserving carrier isomorphisms: **PASS / CLOSED**;
- realizability of the symmetry S as an admissible group/gauge morphism: **FAIL / CLOSED** (S is blocked by the intrinsic orientation);
- admissible counterexample pair: **OPEN / NOT FOUND**;
- universal factorization \(\mathcal B_{27}\to O_{27}\) through q/classification: **OPEN**;
- independent chain-level bridge: **OPEN**;
- Bockstein package as a genuine non-tautological orientation carrier: **CONDITIONAL / OPEN**.

## 7. Consequence: the branch has reached its real boundary

The Bockstein package is not disproved as an admissible carrier, but its only demonstrated orientation information is the finite q-layer partition, while its abstract internal symmetry shows that coefficient-extension data alone does not contain the required 3-adic lift.

Therefore:

1. no more same-family Bockstein calculations;
2. do not promote the abstract S obstruction to a group-level no-go;
3. do not claim a positive orientation bridge;
4. the next admissible branch must add genuinely new q-blind rigidifying information, or prove a universal factorization theorem.

A natural candidate for the next structural attack is **cohomological Mackey/transfer data across open subgroups**, because it can constrain the lift of \(H^1(G,\mathbf Z/9)\) without inserting \(\chi\) into the definition. This is only a candidate, not yet an authorized carrier.

## Classification

\[
\boxed{\text{Bockstein orientation carrier: CONDITIONAL / OPEN}}
\]

The branch is now closed against numerical elaboration and open only at the universal categorical/rigidification level.
