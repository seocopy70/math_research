# U5 — Intrinsic finite-selector audit and literature comparison — 2026-09-24

## Object

For a pro-3 Demushkin group G and k>=2, let
[
Q_k=G/P_{k+1}(G),qquad U_k=(mathbf Z/3^k)^	imes_1=1+3mathbf Z/3^k.
]
The candidate intrinsic selector is the predicate on pairs (Q_k,ho)
[
mathsf K_k(Q_k,ho):
H^1(Q_k,mathbf Z/3^k(ho))	o H^1(Q_k,mathbf F_3)
	ext{ is surjective}.
]

## Input audit

Allowed input: the finite group Q_k, its lower-3-central filtration inherited intrinsically from G, and a candidate character rho:Q_k->U_k.

Excluded from the predicate: q, a presentation, a chosen relator, Fox coordinates, the canonical orientation chi, and a preferred H^2 generator.

## Functoriality

A group isomorphism Q_k->Q'_k transports candidate characters and twisted modules, and naturality of cohomology transports the lifting map. Thus the predicate itself is functorial.

## Gauge

Presentation changes do not act on the abstract pair (Q_k,rho). The Fox row is only a proof coordinate. The intrinsic object to retain is the surjectivity predicate, equivalently the vanishing of the connecting obstruction family when an exact-sequence formulation is used.

## Orientation bridge

U1-U3 give:
1. every crossed cocycle for rho factors through Q_k;
2. finite H^1 lifting on G and Q_k is equivalent;
3. in a one-relator coordinate presentation, the predicate is equivalent to vanishing of the twisted relation/Fox row, using the corrected valuation-induction proof.

Thus the bridge from the intrinsic predicate to the coordinate obstruction is established, but the uniqueness proof is still presentation-based.

## q-blindness

The definition of K_k contains no q. This is genuine definitional q-blindness. However, proving that K_k has exactly one solution and that solution is chi mod 3^k uniformly over all Demushkin groups still uses the standard presentation/classification in the current proof. Therefore q-blindness of the definition is PASS, while q-uniform intrinsic uniqueness remains OPEN.

## Separation

The standard q=3 calculation gives a unique solution at every audited k and the corrected all-k coefficient calculation gives the local recurrence. Degenerate one-relator stress tests show that uniqueness is not a formal consequence of being one-relator: non-Demushkin relations can have multiple or no finite Kummer candidates. Thus the selector's rigidity is tied to Demushkin structure, not merely to the finite predicate syntax.

## Literature comparison

The audited literature establishes the full-group Kummerian criterion: surjectivity of
[
H^1(G,mathbf Z_p(	heta)/p^n)	o H^1(G,mathbf F_p)
]
for every n is equivalent to Kummerianity, and the canonical orientation of a Demushkin group is the unique orientation with that property. Modern formulations also give equivalent descriptions through K_theta(G), theta-abelian quotients, and related structural conditions.

A later quotient-inheritance result (Proposition 2.10 in the 2024 1-cyclotomicity paper) requires an already Kummerian oriented pair (G,theta), a normal N contained in ker(theta), and surjectivity of
[
H^1(G,mathbf F_p)	o H^1(N,mathbf F_p)^G.
]
This is not the same as the present finite candidate-selector statement on Q_k: here rho is itself a finite candidate, and the required factorization is proved directly through the semidirect finite-depth lemma. In particular, the literature result does not by itself supply the finite-window theorem for N=P_{k+1} without checking its additional restriction hypothesis.

The 2022 Kummerian equivalences similarly characterize the full oriented pair but do not, in the audited statements, give the q-free unique-selector theorem on the bare lower-3-central quotient Q_k.

## Current result

- Object: PASS/CLOSED.
- Functoriality of the predicate: PASS/CLOSED.
- Gauge/presentation independence of the predicate: PASS/CLOSED.
- Orientation bridge to Fox coordinates: PASS/CLOSED, coordinate-level.
- q-blind definition: PASS/CLOSED.
- Uniform intrinsic uniqueness: OPEN/LOAD-BEARING.
- Literature novelty boundary: OPEN/DECISIVE.

## Stop condition

Do not claim U5 closed merely from the fact that the predicate is intrinsic. The load-bearing statement is:
[
orall	ext{ Demushkin }G,quad
mathsf K_k(Q_k,ho)
Longleftrightarrow
ho=chi_Gmod 3^k,
]
with no q or presentation in the input.

The next mathematical attack is therefore not another Fox expansion. It is to prove or disprove this naturality/uniqueness statement from intrinsic Demushkin data, or to identify an existing theorem that already implies it.

## 2026-09-24 — N3–N5 LITERATURE GATE RESULT

N3 is now closed as a novelty source. Labute Proposition 6/Theorem 4 already gives the all-level crossed-derivation characterization and unique Demushkin orientation; Quadrelli's 2024 Lemma 2.9 restates Kummerianity as arbitrary finite-level generator-value lifting, and Example 2.6 identifies the unique canonical Demushkin orientation. Therefore full-group finite-coefficient uniqueness is historical/known, not the proposed contribution.

N4 remains OPEN/LOAD-BEARING. The 2024 quotient-inheritance Proposition 2.10 requires an already Kummerian oriented pair, N subset ker(theta), and surjectivity of H^1(G,F_p) -> H^1(N,F_p)^G. Its proof explicitly uses that restriction hypothesis. This does not state the present finite candidate-recognition theorem for N=P_{k+1}. Our U1-U2 route instead proves direct finite-depth factorization for arbitrary candidate rho through Q_k.

N5 remains OPEN/DECISIVE. No audited source states a q-blind, functorial selector on the bare Q_k=G/P_{k+1} whose unique candidate is chi mod 3^k. Labute's proof forces the character in a standard classification presentation, while modern Kummerian papers retain the already-given orientation as input.

Recent checks: Blumer-Quadrelli (arXiv:2603.15464v2) concerns 1-cyclotomic obstructions for variations of Demushkin groups, not a finite Q_k selector; Pál-Quick (2026) concerns A_3-formality, not the finite Kummer selector.

Decision:
- N3 full-group uniqueness: HISTORICAL / SUPERSEDED as novelty;
- N4 exact G/P_{k+1} factorization: OPEN / LOAD-BEARING;
- N5 q-blind finite selector: OPEN / DECISIVE;
- overall novelty: OPEN / CONDITIONAL.

No new Fox computation is authorized from this gate. The next attack is the intrinsic U5 theorem, with factorization/recognition kept logically separate from the already-known existence and uniqueness of the canonical full-group orientation.
