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

## 2026-09-24 — U5 INTRINSIC UNIQUENESS CLOSED: VARIATION + PD² SOCLE INJECTIVITY

The two load-bearing U5 lemmas are now closed without Fox coordinates.

### Lemma U5-V — coefficient-extension variation

Let \(k\ge2\), let \(\rho_k\) and \(\rho_k'\) be two candidate characters reducing to the same level-\((k-1)\) character \(\rho_{k-1}\), and write
\[
\rho_k'=\rho_k(1+3^{k-1}\nu),\qquad \nu\in H^1(G,\mathbf F_3).
\]
For \(A_j=\mathbf Z/3^j(\rho_j)\), the two coefficient extensions
\[
0\to A_{k-1}(\rho_{k-1})\xrightarrow{\iota_{k-1}}A_k(\rho_k)\to\mathbf F_3\to0
\]
and its \(\rho_k'\)-analogue differ by the Yoneda class represented by \(\nu\). Naturality of connecting homomorphisms therefore gives
\[
\boxed{\;
\delta_{\rho_k'}-\delta_{\rho_k}
=
\iota_{k-1}\circ(\nu\smile -)
\;}
\]
as maps
\[
H^1(G,\mathbf F_3)\longrightarrow H^2(G,A_{k-1}(\rho_{k-1})).
\]
The formula is intrinsic: it uses only the coefficient-extension classes and the cup/Yoneda product. No presentation, Fox derivative, relator, \(q\), or preferred \(H^2\)-generator enters.

### Lemma U5-PD — socle inclusion is injective on \(H^2\)

On the induction branch \(\rho_{k-1}=\chi\bmod3^{k-1}\), the socle inclusion
\[
\iota_{k-1}:\mathbf F_3\hookrightarrow A_{k-1}(\chi_{k-1})
\]
induces an injective map
\[
H^2(G,\mathbf F_3)\hookrightarrow H^2(G,A_{k-1}(\chi_{k-1})).
\]
Indeed, PD² duality identifies \(H^2(G,M)\) with the dual of the appropriate \(H^0\)-group of the dual coefficient module tensored with the dualizing module. For \(M=A_{k-1}(\chi_{k-1})\), the dualizing twist cancels the \(\chi_{k-1}\)-action, so the dual map to \(H^2(\mathbf F_3)\to H^2(A_{k-1})\) is the reduction
\[
H^0(G,A_{k-1})\to H^0(G,\mathbf F_3),
\]
which is surjective. Hence the original \(H^2\)-map is injective.

The canonical dualizing orientation is used only as an internal theorem-proving device in this lemma; it is not part of the definition of the finite selector \(\mathsf K_k\).

### U5 uniqueness theorem

Assume inductively that the unique level-\((k-1)\) selector is \(\chi\bmod3^{k-1}\). If \(\rho_k,\rho_k'\) both satisfy the intrinsic finite Kummer predicate, their connecting maps vanish identically. By Lemma U5-V and Lemma U5-PD,
\[
\nu\smile v=0\qquad\forall v\in H^1(G,\mathbf F_3).
\]
The Demuškin cup pairing is nondegenerate, hence \(\nu=0\), so \(\rho_k=\rho_k'\). The base case \(k=2\) is the established finite-window result. Existence is supplied by the known canonical Kummerian/Demushkin orientation, and U1-U2 show that its finite-level lifting predicate is exactly the predicate on \(Q_k=G/P_{k+1}\).

Therefore
\[
\boxed{
\mathsf K_k(Q_k,\rho)
\Longleftrightarrow
\rho=\chi_G\bmod3^k
}
\]
for every \(k\ge2\), for the finite selector defined intrinsically on \((Q_k,\rho)\).

### Boundary and novelty

This closes the mathematical U5 gate. It does **not** make the canonical orientation itself new: existence/uniqueness of the full-group Kummerian orientation is classical/known. The remaining publication-level gate is whether the exact finite-window formulation above is already an immediate corollary or an equivalent restatement of an existing quotient/inheritance theorem.

Decision:
- coefficient-extension variation lemma: **PASS / CLOSED**;
- PD² socle-injectivity lemma: **PASS / CLOSED**;
- U5 intrinsic uniqueness: **PASS / CLOSED**;
- N4 finite \(G/P_{k+1}\) factorization: **PASS / CLOSED**;
- N5 q-blind finite selector theorem: **PASS / CLOSED**;
- overall novelty: **OPEN / CONDITIONAL**.

No Fox computation was used or reopened.


## 2026-09-24 — CONTROLLING N1–N5 CRITICAL REVIEW

The earlier N3–N5 labels in this audit are superseded by the final critical review.

- N3 full-group finite-level uniqueness: **HISTORICAL / NOT NOVEL**.
- N4 arbitrary-candidate factorization through Q_k=G/P_{k+1}: **MATHEMATICAL PASS / CLOSED**. This is distinct from quotient inheritance, but it is not by itself a novelty verdict.
- N5 exact bare-Q_k selector theorem: **NO exact prior theorem found in the audited corpus; PASS / CONDITIONAL for novelty**.
- Overall publication novelty: **PASS / CONDITIONAL**, not an absolute priority claim.

Scope correction: the theorem currently proved is for the fixed rank-4, q=3 Demuškin group. “q-blind” means q is absent from selector input, not that the theorem is uniform over q.

Depth correction: P_{k+1} is sufficient; minimality remains OPEN.

U5 proof correction: variation is a coefficient-extension/Yoneda identity and PD² injectivity must be written using the exact dual coefficient modules and dual reduction map. Classical Kummerian existence is imported.

This entry is controlling for manuscript wording.


## 2026-09-25 — PROP. 2.10 RESTRICTION-SURJECTIVITY HARD ATTACK / N2 SHARPENED

The proposed second follow-up problem was tested against the exact 2024 Proposition 2.10 statement. That proposition assumes an already Kummerian oriented pair (G,theta), N⊂ker(theta), and surjectivity of
res^1_{G,N}: H^1(G,F_p) -> H^1(N,F_p)^G.
Its proof explicitly uses the dual inclusion
N/N^p[G,N] -> G/Phi(G).

For the present N=P_{k+1}(G), p=3, one has N⊂Phi(G), hence the dual inclusion map is zero. At the same time the relevant relative Frattini quotient is nonzero: P_{k+1}/P_{k+2}≠0, while P_{k+1}^3[P_{k+1},G]⊂P_{k+2}. Therefore
P_{k+1}/P_{k+1}^3[P_{k+1},G] != 0,
so the dual map is not injective and the restriction map is not surjective.

Decision: FAIL / CLOSED for automatic restriction-surjectivity. Consequently Proposition 2.10 cannot be used with N=P_{k+1} as an automatic corollary mechanism for the present finite-window theorem.

This does not itself prove absolute novelty. It removes one concrete quotient-inheritance collapse route. The U1–U5 theorem remains PASS/CLOSED and exact publication novelty remains OPEN/CONDITIONAL.

Record: research/PROP_2_10_RESTRICTION_SURJECTIVITY_HARD_ATTACK_2026-09-25.md (commit 5439b06cf45faa6042225ab3e338997c10f2301a).


## 2026-09-25 — CORRECTION / SCOPE TIGHTENING OF PROP. 2.10 ATTACK

The previous entry stated the nonvanishing of P_{k+1}/P_{k+2} uniformly in k without separately recording the needed graded-dimension argument. That is stronger than necessary and is superseded.

The decisive result needs only k=2:
for the rank-4 p=3 Demushkin group, the published Zassenhaus dimension formula gives
dim_F3(P_3/P_4)=c_3=(4^3-4)/3=20.
Hence P_3/P_4 is nonzero, while P_3^3[P_3,G]⊂P_4. Since P_3⊂Phi(G), the dual inclusion
P_3/P_3^3[P_3,G] -> G/Phi(G)
is zero and has nonzero source. Therefore
H^1(G,F_3) -> H^1(P_3,F_3)^G
is not surjective.

This single k=2 counterexample is sufficient to classify automatic Prop. 2.10 restriction-surjectivity as FAIL/CLOSED. Any all-k nonvanishing strengthening is left unclaimed pending a separate explicit proof.

Record correction: research/PROP_2_10_RESTRICTION_SURJECTIVITY_HARD_ATTACK_2026-09-25.md, commit 70dad1bcab1145590d5a06b125dcf07b9249e7e5.
