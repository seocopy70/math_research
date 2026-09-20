## 2026-09-20 — HA61-B5-1/B5-2: CORRECT SECONDARY WINDOW; AFFINE t_2 OBSTRUCTION

B5 source audit corrected the proposed D_4/D_5 quotient. It is not a valid secondary quotient because g^9 lies in D_9 subset D_5 but evaluates nontrivially after /9. The relevant mod-27 finite-information threshold is G/P_4, corresponding to the D_10 information window already established for the standard family.

The new P_3/P_4 power residual gives the genuine ninth-power functional. The gamma_2^3 sector reproduces the old lambda wedge f contribution. A cubic bracket gauge change P -> P+[v,R] gives
T([v,R])=-lambda(v)(lambda wedge f)(R)=lambda(v)f(p)
on the primary-zero locus. Hence the raw t_2 shifts by lambda(v)p.

The total secondary functional is preserved by the paired affine change
(t_2,mu) -> (t_2+a p, mu+a lambda).
Thus raw t_2 is not intrinsic; the natural secondary object is a combined affine/torsor class. A universal presentation-free proof that all degree-three bracket terms are exactly absorbed by this quotient remains open.

Decisions:
- D_4/D_5 factorization: FAIL / CLOSED;
- corrected P_4/D_10 threshold: PASS / LOCAL;
- raw t_2 intrinsicity: FAIL / CLOSED;
- combined affine secondary carrier: OPEN / LOAD-BEARING;
- HA61-B: OPEN / LOAD-BEARING;
- HA61-C: not opened.

Records: research/HARD_ATTACK_61_B5_1_SOURCE_QUOTIENT_CORRECTION_2026-09-20.md; research/HARD_ATTACK_61_B5_2_AFFINE_T2_GAUGE_2026-09-20.md.
## 2026-09-20 — HA61-B5: D_4 CUTOFF FAILS AT MOD-27; P_4 RESIDUAL OPEN

HA61-B5 establishes a sharp correction. The mod-9 argument “D_4-errors vanish after division by 3” cannot be reused at mod 27 after division by 9. The explicit D_4 element g^9 gives
\[
z(g^9)/9\equiv f(g)\pmod3
\]
for rho(g)=1+3a mod 27, so D_4-membership alone does not kill the secondary contribution.

The correct source decomposition is
\[
E_{\ge4}=E_{P_4}+E_{>P_4}.
\]
The P_4 component is now the first forced candidate for the intrinsic t_2 residual; deeper terms must be separately killed or shown to factor through the same datum.

Decision:
- blanket E_{>=4} vanishing mod 27: **FAIL / CLOSED**;
- D_4 as sufficient secondary cutoff: **FAIL / CLOSED**;
- P_4 residual -> intrinsic t_2: **OPEN / LOAD-BEARING**;
- deeper-than-P_4 factorization/vanishing: **OPEN**;
- HA61-B: **OPEN / LOAD-BEARING**;
- HA61-C: **not opened**.

Record: research/HARD_ATTACK_61_B5_FILTRATION_CUTOFF_2026-09-20.md (commit d563edad1f5e690ab70c2e13ac28cacb76bc1318).



## 2026-09-20 — HA61-B4 PASS/LOCAL; B5 OPEN

HA61-B4 is **PASS / LOCAL**. Distinct A_2 lift classes over the same mod-3 class differ by 3c, and naturality of the coefficient-extension pullback gives
\(\delta_3(z+3c)-\delta_3(z)=\delta_2(c)\). This exposes the exact obstruction to lift-class independence rather than assuming it.

For both frozen standard branches q=3 and q=9, direct primary crossed-word evaluation gives \(\delta_2\equiv0\), so the secondary obstruction is independent of the A_2 lift class. This agrees with the direct mod-27 formulas.

Boundary: the universal statement is still open. An arbitrary admissible input with nonzero \(\delta_2\) would produce a secondary obstruction on a lift torsor, not a function of f alone. Therefore the next attack is B5: filtration cutoff/source audit, not HA61-C.

Record: research/HARD_ATTACK_61_B4_LIFT_CLASS_INDEPENDENCE_2026-09-20.md.


## 2026-09-20 — HA61-B3 CLOSED / B4 OPEN

HA61-B3 is now **PASS / CLOSED**. The A_2 representative gauge z→z+dφ cannot change the secondary connecting obstruction: after lifting φ to A_3, the compatible lift changes by dφ~, and d^2=0 gives exact equality of the obstruction cocycles. Therefore no genuinely gauge-dependent B_{rho_2} can be an intrinsic secondary invariant.

This does NOT close the old-action question completely. Distinct A_2-valued cohomology lifts over the same primary-zero f can still differ by non-gauge data. The decisive next question is HA61-B4: whether the remaining non-mu secondary contribution is canonically represented by the next filtered residual t_2, or whether an additional lift-class parameter survives.

Current order remains: B1 → B2 → **B3 PASS/CLOSED** → **B4 OPEN/LOAD-BEARING** → B5. No HA61-C and no all-n induction yet.

Record: research/HARD_ATTACK_61_B3_GENERAL_A2_LIFT_GAUGE_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 54: HA53 SUPERCEDES THE HA52 d3 WARNING

A critical review of HA52–53 was recorded. HA52 correctly established dim E_3^{2,1}=19 but left a generic warning that a later d3-Bockstein phenomenon might remove the sector. HA53 closes that concern completely: for (p,q)=(2,1), every r>=3 has zero outgoing target E_r^{2+r,2-r}, and every incoming source E_r^{2-r,r} has negative first index. Hence E_3^{2,1}=E_infinity^{2,1}, with dimension 19. The generic cyclic-kernel d3-Bockstein phenomenon remains valid elsewhere, but cannot act on this bidegree.

The permanent piece is now treated as the canonical quotient S=ker(H^2(V) tensor K -> H^4(V))/im(d2:H^2(W)->H^2(V) tensor W^*), with dim S=19, rather than as an isolated dimension count.

Decision:
- HA52 d2 calculation: PASS / CLOSED;
- HA53 permanence: PASS / CLOSED;
- HA52 warning that d3 may remove the 19D sector: HISTORICAL / SUPERSEDED;
- canonical 19D LHS filtration piece S: PASS / CLOSED;
- H-module structure: OPEN / LOAD-BEARING;
- twisted beta_rho^2 on S: OPEN / LOAD-BEARING;
- orientation-selector interpretation: OPEN / DECISIVE.

Record: research/KUMMER_HARD_ATTACK_54_CRITICAL_CORRECTION_AND_19_QUOTIENT_2026-09-20.md

Next authorized attack: construct the induced H-action on S from the central extension functorially; no dimension-based module identification is permitted.
## 2026-09-20 — HARD ATTACK 26: TOP-COHOMOLOGY DOES NOT AUTOMATICALLY FACTOR THROUGH Q_k

The next Kummer gate was attacked directly. If N=P_{k+1}(G) and Q_k=G/N, then A_k(rho) is N-trivial because rho factors through Q_k. However the Hochschild–Serre five-term sequence contains

0 -> H^1(Q,A) -> H^1(G,A) -> H^1(N,A)^Q -> H^2(Q,A) -> H^2(G,A) -> H^1(Q,H^1(N,A)).

Thus P_{k+1}(A_k⋊U_k)=1 proves factorization of candidate rho and Z^1 data, but does not imply factorization of H^2(G,A_k(rho)) through the abstract quotient Q_k. The missing datum is the extension/2-cell information carried by 1 -> P_{k+1}(G) -> G -> Q_k -> 1.

Decision:
- H^2-factorization through Q_k as an automatic inference: **FAIL / CLOSED**.
- Q-only intrinsic Kummer selector: **OPEN**; not universally disproved inside the restricted Demushkin category.
- finite extension/2-cell enriched carrier (Q_k,E_k): **OPEN / new principal candidate**.
- no numerical scan authorized.

Record: `research/KUMMER_TOP_COHOMOLOGY_HARD_ATTACK_26_2026-09-20.md`

## 2026-09-20 — DISCOVERY PASS: TWISTED KUMMER / TOP-COHOMOLOGY SELECTOR

A new positive mechanism was identified after Hard Attacks 24–25 closed the shallow crossed-cocycle selectors.

For a candidate finite orientation rho:G->U_k, with A_k=Z/3^k and A_k(rho) the twisted module, the PD^2/Kummer literature supplies a stronger selector: the top-degree twisted obstruction. At the full PD^2 level, the canonical orientation is characterized by maximal top cohomology |H^2(G,A_k(rho))|=3^k (equivalently, by the Kummer lifting property). This is not merely existence of a cocycle.

For the standard rank-4 one-relator family
G_q=<x1,x2,x3,x4 | x1^q[x1,x2][x3,x4]>,
the crossed-derivation/top obstruction row was independently expanded:
d1=q+u2^{-1}-1, d2=0,
d3=-(u4-1)/(u3u4), d4=(u3-1)/(u3u4),
after rho(r)=1 forces u1=1 in U_k.
Hence the full row vanishes iff
u2=(1-q)^{-1}, u3=u4=1,
which is exactly chi mod 3^k on the standard family. Therefore the twisted top-cohomology/Kummer mechanism gives a unique finite-level selector on the standard family.

Critical boundary: this does NOT yet prove that the selector is a functor of Q_k=G/P_{k+1}. Although rho and crossed cocycles factor through Q_k because P_{k+1}(A_k⋊U_k)=1, H^2(G,A_k(rho)) is not automatically determined by an arbitrary finite quotient. Presentation/relator-gauge independence and non-tautological filtered realization remain load-bearing.

Decision:
- twisted Kummer/top-cohomology selector as a mechanism: **PASS / LOCAL**;
- unique finite-level selector on standard one-relator family: **PASS / LOCAL**;
- intrinsic q-blind selector on Q_k: **OPEN**;
- universal factorization through G/P_{k+1}: **OPEN**;
- non-tautological filtered realization: **OPEN**.

Record: `research/KUMMER_TWISTED_TOP_COHOMOLOGY_DISCOVERY_PASS_2026-09-20.md`



## 2026-09-20 — FIRST-STAGE LOWER 3-CENTRAL INFORMATION BOUNDARY

The first-stage theorem draft is recorded in research/LOWER_3_CENTRAL_INFORMATION_BOUNDARY_2026-09-20.md. For the standard family G_{3^s} versus G_∞, the sharp finite-quotient thresholds are D_N: N≤3^s and P_n: n≤s+1, with sharp separation at the next level by abelianization. Thus the q-information scale is exponential in Zassenhaus depth but linear in lower-3-central depth. With the known standard-family orientation formula, χ mod 3^k has information boundary D_{3^{k-1}+1} versus P_{k+1}; mod 27 gives D_10 versus P_4.

Status: Zassenhaus threshold PASS / LOCAL; lower-3-central threshold PASS / LOCAL subject to the standard P_n product formula; linear χ-information boundary PASS / LOCAL under standard-family/classification dependence. This is not yet an intrinsic pointed Kummer-recognition theorem. Next substantive task is to test whether the relevant q-blind Kummer condition factors through G/P_{k+1}. No new gate is introduced.
## AUTHORITATIVE UPDATE — 2026-09-20 — CRITICAL CORRECTION: MIXED m-ADIC GATE + ZASSENHAUSZ THRESHOLD

A review correction was audited and accepted.

First, the previously discussed Zassenhaus threshold argument did **not** identify (G/D_N(G)) with its abelianization. The precise statement is
[
(G/D_N(G))^{ab}=G/(D_NG').
]
For (G_{3^s}) and (N=3^s+1), the Jennings formula gives
[
(G_{3^s}/D_N)^{ab}cong mathbf Z/3^s	imes(mathbf Z/3^{s+1})^3,
]
while the power-free control has
[
(G_infty/D_N)^{ab}cong(mathbf Z/3^{s+1})^4.
]
For (Nle3^s), (x_1^{3^s}in D_N(F)), so the defining relation becomes (c=[x_1,x_2][x_3,x_4]=1) modulo (D_N(F)), giving
[
G_{3^s}/D_Ncong G_infty/D_N.
]
Thus the threshold (D_{3^{n-1}+1}) versus (D_{3^{n-1}}) is a valid **PASS / LOCAL** information boundary for (chimod3^n) within the standard Demushkin family, with the classification/orientation formula explicitly identified as an external dependence. It is not a universal pointed naturality theorem.

Second, HARD ATTACK 10 is confirmed to close only the ordinary presentation-independent local degree-(le3) Fox truncation. It does not close a mixed
[
mathfrak m=(3,I)
]
finite carrier. The candidate
[
J_n^{mix}=I_{mathrm{Fox}}+mathfrak m^n
]
is therefore **OPEN / reauthorized for definitional attack only**.

The existence and non-tautology gates are separated: Fox-derived finite constructions are not excluded at the existence stage; genuine compression/independence is tested only after intrinsicity and the orientation bridge are established.

The load-bearing new issue is relator-gauge naturality. For (r'=grg^{-1}), the Fox derivative acquires the additional term
[
g,partial r+(1-grg^{-1})partial g.
]
The mixed carrier definition must therefore specify the relation/augmentation ideal precisely before naturality can be claimed.

Decision:
- corrected Zassenhaus threshold: **PASS / LOCAL**;
- ordinary degree-3 Fox truncation no-go: **PASS / CLOSED**;
- mixed m-adic finite carrier: **OPEN / REAUTHORIZED FOR DEFINITIONAL ATTACK ONLY**;
- mixed-carrier relator-gauge naturality: **OPEN / LOAD-BEARING**;
- no numerical mixed-jet scan until definition + gauge naturality are passed.

Record: `research/CRITICAL_CORRECTION_MIXED_MADIC_AND_ZASSENHAUSZ_THRESHOLD_2026-09-20.md`

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 17: BOCKSTEIN NON-TAUTOLOGY

The apparent mod-27 orientation bridge was attacked more strongly. The coefficient-extension carrier \(\mathcal B_{27}\) separates the standard family exactly by the q 3-adic valuation class, while the proposed logarithmic orientation digit has the corresponding values as a known function of q. Therefore the present evidence is compatible with forbidden classification repackaging: \(\mathcal B_{27}\to v_3(q)\text{-class}\to q\text{-class}\to\chi\).

Decision: the coefficient-extension package remains **PASS / LOCAL as an intrinsic q-information detector**, but as a new orientation carrier it is **CONDITIONAL / NOT YET ADMISSIBLE**. A genuine carrier requires a presentation-free universal identity or independent universal property producing \(\frac13\log\chi\) directly, not by first recovering q/classification data.

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 16: MOD-27 BOCKSTEIN-EXTENSION CARRIER

A new intrinsic finite-level candidate survives the definition gate:
\[
\mathcal B_{27}=(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9),
\]
where \(\beta_9\) comes from \(0\to\mathbf F_3\to\mathbf Z/27\to\mathbf Z/9\to0\). It is q-blind, functorial, independent of Fox coordinates, and naturally contains the established mod-9 carrier.

For the standard Demuškin family, direct relator lifting gives the expected q=3/q=9/q≥27 separation. The correct additive target is the logarithmic orientation digit \(\lambda_{27}=\frac13\log\chi\pmod9\). The frozen-family values are \(e_2,3e_2,0\), which exponentiate to \(\chi(x_2)=13,10,1\pmod{27}\).

Critical boundary: the intrinsic orientation bridge has not yet been proved independently of the standard presentation. In particular, it must be shown that the cup-dual of the relevant Bockstein layer is naturally the corresponding coefficient of \(\frac13\log\chi\), with no hidden use of q or the known orientation formula.

Decision:
- mod-27 Bockstein-extension candidate: **OPEN / STRONG CANDIDATE**;
- definition/q-blindness/reduction: **PASS**;
- separation: **PASS / LOCAL**;
- orientation bridge: **OPEN / load-bearing**;
- strict compression below Fox: **OPEN**.

Record: research/MOD27_BOCKSTEIN_EXTENSION_CARRIER_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 15: MOD-27 CATEGORY ADEQUACY

A definition-level loophole in the PRE-MOD27 gate has been closed. If the full group G is allowed as an unrestricted input with arbitrary intrinsic constructions, then the canonical dualizing module/action already contains chi, and the Demuškin classification identifies q as a group invariant from which the canonical orientation is recovered. Such a group-only J_27 is therefore known/tautological relative to the intended filtered-information problem, not a new carrier.

The gate has been tightened: q-blindness now excludes not only explicit q/chi, but also first extracting q, the dualizing action, or an equivalent complete classification invariant and repackaging it as J_27. A surviving carrier must be constructed directly from the declared filtered/relation-information functor and must not factor through an already-known canonical-orientation object without an independent obstruction construction.

Decision:
- unrestricted group-intrinsic J_27: **HISTORICAL / SUPERSEDED as a new-carrier candidate**;
- category-adequacy correction: **PASS / CLOSED**;
- genuine filtered/relation J_27: **OPEN**;
- no numerical mod-27 scan authorized until the revised input category is frozen.

Record: research/MOD27_CATEGORY_ADEQUACY_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 14: FOX LOCAL QUOTIENT COMPRESSION CLOSED

The frozen (q=3) exact local Fox obstruction algebra was reduced explicitly:
[
mathcal A_{mathrm{Fox}}
=
mathbf Z_3[[u_1,u_2,u_3,u_4]]
/
(u_1,u_3,u_4,2u_2+3)
congmathbf Z_3.
]

Thus the local Fox obstruction scheme on (1+3mathbf Z_3) is already a reduced characteristic-zero point,
[
(1,-1/2,1,1).
]

Consequently, any proper unital quotient of this local coefficient algebra either loses characteristic-zero (3)-adic information or collapses the point. Therefore there is no strictly smaller quotient of the exact local Fox carrier that still retains the full (3)-adic orientation.

Decision:
- quotient-of-local-Fox-scheme compression: **FAIL / CLOSED**;
- exact local Fox carrier minimal under full-(3)-adic-preserving quotients: **PASS / CLOSED**;
- independently defined intrinsic non-quotient exact compression: **OPEN**.

Record:
research/ORIENTATION_FOX_LOCAL_QUOTIENT_MINIMALITY_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 13: FULL ASSOCIATED-GRADED NO-GO

A stronger negative boundary has now been established.

For infinite Demuškin pro-(3) groups of fixed rank, the full graded group algebra
[
operatorname{gr}mathbf F_3[[G]]cong U(L(G))
]
coming from the complete (3)-Zassenhaus filtration is the quadratic/PBW Demuškin graded algebra determined by
[
[X_1,X_2]+[X_3,X_4]+cdots,
]
independently of the Demuškin (q)-invariant. Thus the full mod-3 associated-graded object is (q)-blind, not merely every bounded truncation.

In the rank-four family
[
G_{3^s}=langle x_imid x_1^{3^s}[x_1,x_2][x_3,x_4]
angle,
qquad
G_infty=langle x_imid [x_1,x_2][x_3,x_4]
angle,
]
the graded object is therefore unable to distinguish the groups at the mod-3 graded level, while
[
chi_{3^s}(x_2)=(1-3^s)^{-1}
]
varies with (s), and (chi_infty(x_2)=1).

This upgrades the previous finite-window obstruction to a full associated-graded no-go.

Decision:
- **full mod-3 associated graded (Rightarrow q) or full (chi): FAIL / CLOSED;**
- any successful carrier must contain non-graded filtered/characteristic-zero extension information;
- the first sufficient extension datum at mod-9 is the degree-3 power component (P_3) coupled to (R_2);
- this is a genuine lower bound, but not an absolute category-independent minimality theorem.

Important precision: the full (3)-adic digits do not necessarily require infinitely many independent extension classes. For fixed (q=3), the exact equation (1+2B=0) compresses all digits into one exact (mathbf Z_3)-coefficient relation. Hence the remaining question is specifically whether such exact extension information admits a canonical intrinsic compression smaller than the universal Fox obstruction scheme.

Record:
research/ORIENTATION_FULL_GRADED_NO_GO_MINIMAL_EXTENSION_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-20 — DEGREE-3 FOX TRUNCATION FAILS UNDER NIELSEN CHANGE

A concrete Nielsen-equivalent presentation
\[
x_1=y_1y_2,\quad x_2=y_2,\quad x_3=y_3,\quad x_4=y_4
\]
was used to test whether the fixed-normal-form degree-3 Fox compression is intrinsic.

The transformed exact Fox row contains higher local degrees. After truncation to degree \(\le3\) around \(Y_i=1\), the second row evaluates at the transported canonical point \((-2,-1/2,1,1)\) to
\[
-243/2\neq0,
\]
while the full row vanishes exactly.

Decision:
\[
\boxed{\text{presentation-independent degree-3 Fox truncation = FAIL / CLOSED}.}
\]

This does not rule out a different intrinsic exact filtered carrier; it rules out the naive identification of that carrier with the degree-3 truncation of the universal Fox row.

Record:
research/ORIENTATION_FOX_DEGREE3_NIELSEN_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 9: NAIVE INTEGRAL AUGMENTATION JET CLOSED

The proposed next object
\[
\mathcal R_3^{\mathbf Z_3}=\langle r-1\rangle\subset I^2/I^4,
\qquad I=\ker(\mathbf Z_3[[F]]\to\mathbf Z_3),
\]
is **not defined as stated** for the frozen relation
\[
r=x_1^3[x_1,x_2][x_3,x_4].
\]

Writing \(X_i=x_i-1\),
\[
x_1^3-1=3X_1+3X_1^2+X_1^3,
\]
while the commutator product begins in ordinary augmentation degree 2. Hence
\[
r-1=3X_1+[X_1,X_2]+[X_3,X_4]+O(I^3),
\]
so
\[
\boxed{r-1\notin I^2}.
\]

Therefore the plain \(\mathbf Z_3\)-augmentation quotient \(I^2/I^4\) cannot be the sought integral analogue of the mod-3 Zassenhaus degree-(2,3) jet. This is a **FAIL / CLOSED** definition-level result.

The structural reason is that the Zassenhaus filtration is naturally obtained from the completed \(\mathbf F_3[[F]]\) augmentation ideal; replacing \(\mathbf F_3\) by \(\mathbf Z_3\) changes the filtration and retains the mixed p-adic terms \(3X_1\), \(3X_1^2\). The earlier rejection of naive \(\mathbf Z_3\)-scalar extension of the restricted-Lie carrier is independently confirmed.

A mixed p-adic/Zassenhaus weighted filtration remains **OPEN**, but its finite associated graded pieces retain residue-layer information rather than an unrestricted exact 3-adic scalar. Thus it does not by itself evade the already closed bounded-degree + finite-precision obstruction.

The exact universal Fox obstruction scheme remains the correct characteristic-zero comparison object. The remaining structural target is now:
\[
\boxed{
\text{intrinsic filtered jet tower}
\;\stackrel{?}{\longrightarrow}\;
\text{exact Fox orientation locus}
}
\]
with an explicit account of where the infinitely many 3-adic digits enter. No further plain \(I^2/I^4\) computation is authorized.

Detailed audit:
research/ORIENTATION_INTEGRAL_AUGMENTATION_JET_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-19 — BOCKSTEIN–RELATION-JET IDENTIFICATION GATE CLOSED

The load-bearing identification
\[
\beta\longleftrightarrow p(P_3)
\]
has been audited. A direct cochain/transgression calculation shows that the Bockstein of a mod-3 generator is obtained by lifting it to \(\mathbf Z/9\), evaluating the lift on the relator, and dividing the resulting obstruction by 3. Commutator terms contribute no exponent sum; the restricted-cubic power term \(X_i^{[3]}\) contributes exactly its coefficient. Thus the Bockstein vector is projectively the same power-direction vector \(p(P_3)\), with only the common transgression/fundamental-class sign/unit left as gauge.

For q=3, \(P_3=X_1^{[3]}\), so \(p\sim X_1^{(1)}\). For q=∞, \(p=0\). Therefore the previously established projective recovery functional applies intrinsically and gives \(\chi\bmod9=(1,4,1,1)\) for q=3.

Decision:
- Bockstein–relation-jet projective identification: **PASS / CLOSED** under the standard one-relator transgression convention;
- absolute sign/normalization of the H² generator: **CONDITIONAL / gauge-dependent**, irrelevant to the projective carrier;
- intrinsic cup+Bockstein carrier → \(\chi\bmod9\): **PASS / CLOSED**;
- no higher-digit conclusion and no broad scan.

Record: research/BOCKSTEIN_RELATION_JET_IDENTIFICATION_AUDIT_2026-09-19.md

## AUTHORITATIVE UPDATE — 2026-09-19 — M3 COMPARISON BOUNDARY

The intrinsic mod-9 carrier [(R,p)] was compared with Pál–Quick's A_3/Hochschild canonical class.

A genuine **PASS / LOCAL** detection-level compatibility is established for the standard p=3 Demushkin family:
- q=3: first Bockstein/power direction is nonzero and Pál–Quick's canonical A_3 class is nonzero;
- q=3^f, f≥2: first Bockstein layer vanishes and the Pál–Quick A_3 obstruction vanishes in their theorem range.

This is a common q=3 power-layer detection, not an equality theorem.

The stronger map/factorization
\[
[(R,p)]\longrightarrow\gamma_{A_3}
\]
remains **OPEN** because the two objects have different targets and constructions: the former is the cup/Bockstein carrier, while the latter is a Hochschild/cochain obstruction computed via higher tensor data and Dwyer U_4 lifting.

No U_4/Hochschild scan is authorized. A future M3 continuation must first define a natural target map and prove its functoriality and gauge compatibility.

Detailed record:
research/M3_CUP_BOCKSTEIN_TO_PAL_QUICK_COMPARISON_AUDIT_2026-09-19.md

## AUTHORITATIVE UPDATE — 2026-09-19 — INTRINSIC MOD-9 CARRIER VIA CUP + BOCKSTEIN

The μ–χ bridge was critically narrowed: μ is an intrinsic mod-3 automorphism/duality-line shadow, but μ alone does not determine χ mod 9 and admits no simple homomorphic lift into 1+3Z_3. A deeper μ + additional-data bridge remains conceptually open; no μ-only scan is authorized.

The standalone Bockstein candidate is also CLOSED as an orientation carrier: β alone detects the q=3 power direction but not the scalar 4 mod 9.

A new structural result now closes M1 at the mod-9 level.

For
\[
V=H^1(G,\mathbf F_3)^*
\]
and the intrinsic maps
\[
\smile:H^1\times H^1\to H^2,
\qquad
\beta:H^1\to H^2
\]
with dim H^2=1, choose temporarily ω≠0 in H^2 and define
\[
f\smile g=(f\wedge g)(R)\omega,
\qquad
\beta(f)=f(p)\omega.
\]
Changing ω to uω rescales both R and p by u^{-1}; therefore
\[
\boxed{\overline J_3(G)=[(R,p)]}
\]
is canonical. In the minimal one-relator model, R is the quadratic relation and p is the restricted-cubic/power component of the degree-3 relation jet.

The intrinsic carrier therefore has the factorization
\[
(H^1,H^2,\smile,\beta)
\longmapsto
[(R,p)]
\longmapsto
\overline\Theta(\lambda)(f)=f(p)+(\lambda\wedge f)(R)
\longmapsto
\chi\bmod9.
\]

For q=3, p=e_1^{(1)} and the unique zero is λ=e_2^*, giving (1,4,1,1) mod 9. For q=∞, p=0 and the zero is λ=0.

Decision:
- standalone Bockstein: FAIL/CLOSED;
- cup + Bockstein intrinsic carrier: PASS/CLOSED at mod-9 level, under the stated standard transgression/Bockstein identification;
- M1 intrinsic carrier functor: PASS/CLOSED at mod-9 level, under the standard transgression/Bockstein identification, under the stated standard transgression/Bockstein identification;
- M2 orientation factorization: PASS/CLOSED for the stated projective degree-(2,3) mod-9 functional, with beta ↔ p(P3) supplied by the standard transgression/Bockstein formula;
- M3 independent comparison with Pál–Quick A3/Hochschild class: NEXT AUTHORIZED TARGET;
- no broad computational scan is authorized.

Detailed record:
research/ORIENTATION_MOD9_INTRINSIC_CUP_BOCKSTEIN_CARRIER_2026-09-19.md

## LATEST MANUSCRIPT CONSOLIDATION — 2026-09-19

A unified manuscript draft has been created:
`research/ORIENTATION_RECONSTRUCTION_MANUSCRIPT_DRAFT_2026-09-19.md`

The paper is organized around one central question:
[
	ext{How much filtered relation information is necessary and sufficient to recover the canonical }3	ext{-adic orientation?}
]

The consolidated logical spine is:
1. bare quadratic graded data loses (chimod9);
2. the projective degree-(2,3) relation jet recovers (chimod9);
3. its coarsest natural quotient is (overline J_3=[(R,p(P))]);
4. a compatible finite-level filtered relation-jet tower recovers the full (chi) by inverse limit;
5. bounded degree plus finite coefficient precision cannot universally recover full (chi);
6. fixed (q=3) exact (mathbf Z_3)-coefficient relation/evaluation data does recover full (chi), but no non-tautological finite characteristic-zero compression analogous to (overline J_3) has been proved.

This manuscript is a structural consolidation, not yet a publication-ready literature-complete paper. Claims are intentionally restricted to the audited hypotheses and boundaries.

---

## LATEST AUTHORITATIVE UPDATE — 2026-09-19 — EXACT Z_3 CARRIER BRANCH ENDPOINT

The remaining exact-carrier branch has now been pushed to its structural boundary and closed.

New record:
`research/ORIENTATION_EXACT_Z3_CARRIER_BRANCH_ENDPOINT_2026-09-19.md`

The target was a non-tautological finite/concrete exact \\(\\mathbf Z_3\\)-carrier analogous to the mod-3 compressed carrier \\(([R],p(P))\\).

Final status:
- fixed q=3 exact filtered relation/evaluation data -> full \\(\\chi\\): **PASS / CLOSED**;
- compatible full filtered tower -> full \\(\\chi\\): **PASS / CLOSED**;
- naive characteristic-zero “restricted Lie” lift of the mod-3 quotient: **FAIL / CLOSED**;
- canonical quotient by the independently fixed crossed-derivation evaluation family: **PASS as a universal quotient**, but this is not yet a non-tautological finite compression;
- non-tautological finite/concrete exact compression analogous to \\(([R],p(P))\\): **OPEN / NOT PROVED**, and no further scan is warranted;
- universal bounded-degree + finite-precision carrier across q=3^s: **FAIL / CLOSED**.

Critical correction: an exact finite augmentation truncation is a legitimate object, but no proof was obtained that it alone factors the full exact crossed-derivation coefficient law under the frozen convention. Do not silently promote this to a theorem.

This closes the current exact-carrier search at the structural boundary. A future continuation would require a genuinely new characteristic-zero invariant or a new factorization theorem, not another scan of the already audited candidates.

## Latest exact-Z_3 bounded-degree result — 2026-09-19

The fixed-q=3 branch has reached its natural endpoint.

A single projective degree-(2,3) exact filtered relation jet over Z_3 determines the full orientation for the frozen q=3 normal form:
[
mathbb J^{ex}_3 Longrightarrow 
ho(x_1)=
ho(x_3)=
ho(x_4)=1,quad 1+2
ho(x_2)=0,
]
hence
[
chi(x_2)=-1/2=(1-3)^{-1}inmathbf Z_3^	imes.
]

The presentation-change calculation has the same residual gauge
[
(R,P)mapsto(uR,uP+[v,R])
]
at degree <=3, and degree-one functionals annihilate [v,R], so the recovery zero set is unchanged. This closes the fixed-q=3 exact-carrier branch at the same conditional standard minimal one-relator pro-3 facts used by the mod-9 E1-E5 audit.

This does NOT contradict the universal bounded-degree obstruction: that obstruction varies q=3^s, and for every fixed degree d one can choose 3^s>d. The exact q=3 carrier is therefore a fixed-group exact-filtered result, not a universal finite-information carrier.

Record: research/ORIENTATION_EXACT_PROJECTIVE_DEGREE3_FULL_CHI_CLOSURE_2026-09-19.md

Decision:
- fixed q=3 exact projective bounded-degree carrier -> full chi: PASS / CLOSED
- universal finite-information bounded-degree carrier -> full chi: FAIL / CLOSED
- bare F_3 graded carrier -> full chi: FAIL / CLOSED

## Latest bounded-degree obstruction — 2026-09-19

The stronger branch was pushed without a scan.

A new no-go result is recorded in
`research/ORIENTATION_BOUNDED_DEGREE_FINITE_INFORMATION_OBSTRUCTION_2026-09-19.md`.

For the family
[
G_{3^s}=langle x_imid x_1^{3^s}[x_1,x_2][x_3,x_4]
angle
]
and (G_infty), the quadratic initial relation is identical, while
[
chi_{3^s}(x_2)=(1-3^s)^{-1}
e1=chi_infty(x_2).
]
The power term (x_1^{3^s}) first appears in Zassenhaus degree (3^s). Hence every fixed degree bound (d) misses the q-dependent term for sufficiently large (s). If finite coefficient precision modulo (3^N) is also imposed, choosing (sge N) makes the same carrier indistinguishable modulo (3^N), while the full 3-adic characters remain different.

Decision:
**PASS / CLOSED:** no universal finite-information carrier with both bounded filtration degree and bounded 3-adic precision can recover the full (chi).

Important loophole:
a bounded-degree carrier with exact (mathbf Z_3)-coefficients has infinitely many 3-adic digits and is therefore not a finite-information carrier. For the fixed q=3 presentation, such an exact coefficient-level carrier may recover the full (chi); that separate intrinsic/projective formulation remains OPEN.

This distinction now replaces the undifferentiated “finite bounded-degree jet” OPEN label.

---

# CURRENT STATE — 2026-09-19

> **Authoritative update:** this header supersedes stale branch labels later in this file. Detailed chronology remains in `research/00_RESEARCH_LOG.md`; the consolidated midterm assessment is `MIDTERM_RESEARCH_ASSESSMENT_2026-09-19.md`.

## Latest theorem closure — 2026-09-19

The finite-level factorization / inverse-limit gap has now been written explicitly in
\`research/ORIENTATION_FINITE_LEVEL_FACTORISATION_THEOREM_2026-09-19.md\`.

For the compatible projective filtered relation-jet tower \(J_n\), the theorem-level map is
\[
J_n\longmapsto\chi_n:G\to(\mathbf Z/3^n)^\times,
\]
where \(\chi_n\) is the unique zero of the finite-level crossed-derivation coefficient condition. The frozen q=3 calculation gives
\[
\chi_n(x_1)=\chi_n(x_3)=\chi_n(x_4)=1,\qquad
\chi_n(x_2)=(-2)^{-1}\pmod{3^n}.
\]
Reduction modulo \(3^n\) makes the finite-level solutions compatible, and
\[
\mathbf Z_3^\times\cong\varprojlim_n(\mathbf Z/3^n)^\times
\]
gives the unique inverse-limit character \(\chi\).

Decision: **finite-level factorization / inverse-limit theorem PASS / CLOSED at the stated information level**.
Important boundary: this closes only\[\text{full compatible tower}\Rightarrow\{\chi_n\}_n\Rightarrow\chi.
\]
It does not prove that \(J_3\) alone determines all higher digits, nor categorical minimality, nor existence of a bounded-degree carrier for the full character.

### Next authorized work

1. **Categorical minimality of the projective degree-(2,3) jet.**
2. **Finite bounded-degree jet \(\Rightarrow\) full \(\chi\)** — determine whether possible; if not, prove an obstruction.

No broad finite scan is authorized.

A relative minimality lower bound has been closed; absolute categorical minimality remains OPEN pending an explicit carrier category. See `research/ORIENTATION_MOD9_RELATIVE_MINIMALITY_AUDIT_2026-09-19.md`.

---

## Current research question
Can the canonical orientation character
\[
\chi:G\to\mathbf Z_3^\times
\]
be recovered intrinsically from filtered/graded data?

## Current mathematical position — 2026-09-19

| Datum | Status |
|---|---|
| bare associated graded restricted Lie object | **FAIL / CLOSED** for \(\chi\bmod9\) |
| projective degree-(2,3) relation jet | **PASS / CLOSED** for \(\chi\bmod9\) |
| compatible full filtered relation-jet tower | **PASS** as a full-\(\chi\) reconstruction mechanism |
| finite-level factorization \(J_n\to\chi\bmod3^n\) | **OPEN as an explicit theorem/lemma formulation** |
| one finite bounded-degree jet \(\Rightarrow\) full \(\chi\) | **OPEN** |
| categorical absolute minimality of projective jet | **OPEN** |

### Latest substantive conclusion

The 2026-09-19 hand derivation using
\[
[x,y]=x^{-1}y^{-1}xy
\]
gives, for the standard q=3 Demuškin relation,
\[
\rho(x_1)=\rho(x_3)=\rho(x_4)=1,
\qquad
1+2\rho(x_2)=0,
\]
hence
\[
\boxed{\chi(x_2)=(1-3)^{-1},\quad \chi(x_i)=1\;(i\ne2).}
\]
Thus
\[
\chi(x_2)=4\pmod9,\ 13\pmod{27},\ 40\pmod{81},\ 121\pmod{243},\ldots
\]

The same relation works at every 3-adic level. The projective degree-(2,3) relation jet recovers the first nontrivial digit \(\chi\bmod9\); the compatible full filtered relation-jet tower recovers the full character.

### Critical logical boundary

The hand derivation directly proves the character from the full defining relation via the intrinsic crossed-derivation characterization. To state a theorem specifically as
\[
\text{compatible full relation-jet tower}\Rightarrow\chi
\]
the finite-level maps
\[
J_n\mapsto\chi_n=\chi\bmod3^n
\]
and their compatibility
\[
\chi_{n+1}\equiv\chi_n\pmod{3^n}
\]
should be written explicitly, followed by
\[
\chi=\varprojlim_n\chi_n.
\]
Do not claim this finite-level factorization theorem is already separately proved.

### Information boundary

For
\[
G_3=\langle x_i\mid x_1^3[x_1,x_2][x_3,x_4]\rangle,
\qquad
G_\infty=\langle x_i\mid [x_1,x_2][x_3,x_4]\rangle,
\]
the bare graded restricted Lie object has the same initial quadratic relation, while
\[
\chi_3(x_2)=4\pmod9,\qquad \chi_\infty(x_2)=1\pmod9.
\]
Therefore bare graded data cannot recover \(\chi\bmod9\). The missing information is the coupling between the quadratic relation and its degree-3 filtered component.

The projective jet
\[
J_3=\langle(R_2,P_3)\rangle
\subset L_2\oplus L_3^{res}
\]
supplies this coupling. Its recovery functional
\[
\Theta_J(\lambda)(f)=f(P_3)+(\lambda\wedge f)(R_2)
\]
has the unique q=3 zero \(\lambda=e_2^*\), giving \(\chi\bmod9\).

Presentation/lift/gauge analysis gives
\[
(R,P)\mapsto(uR,uP+[v,R]),
\]
and the bracket term is invisible to degree-one functionals. Hence the recovery zero set is invariant at the stated degree-(2,3) level, conditional on the standard minimal one-relator pro-3 facts and frozen convention.

### Research decision

The core reconstruction question is now **positively resolved at the enriched-data level**, but the stronger minimality question remains open. The next work should therefore focus on:

1. explicit finite-level factorization/inverse-limit theorem;
2. categorical minimality of the projective degree-(2,3) jet;
3. whether any finite bounded-degree jet can determine the full 3-adic character.

No new broad finite scan is authorized merely to revisit the already closed branches.

---


## Authoritative current question
Can the canonical orientation character chi:G -> Z_3^times be recovered intrinsically from filtered/graded data?

## Authoritative branch
**Rank-4 D4 IA / filtered extension datum.**

## Latest mathematical conclusion — 2026-09-19

The quotient-valued object
Delta_q(g) = [F_g(X_1^3)-X_1^3]_3
is **not a new q-sensitive invariant**.

Indeed, with the frozen convention F_(gh)=F_g o F_h and
F_g(X_1)=g.X_1 + terms of degree >=2,
the degree-3 part satisfies
Delta_q(g) = g.(X_1^3) - X_1^3.

This was independently verified in the structured CI on all 9 representatives after adding the explicit coboundary check:
CI run 35420266538, head bd53311cf45dfc930599c3c24b60df8572c155cc, job 105836490226 — SUCCESS.

Therefore
Delta_q(gh)=Delta_q(g)+g.Delta_q(h)
is the ordinary coboundary identity. Modulo Q3 it represents the zero H^1 class whenever [X_1^3] is viewed as a fixed Q3 vector:
Delta_q(g)=g.[X_1^3]-[X_1^3].

### Consequence

The earlier structured cocycle passes remain valid as **implementation/convention checks only**. They do not constitute evidence for a new q-observable, canonical cocycle, or nontrivial H^1 class.

The broader rank-4 scan proposed after the structured audit is **CANCELLED**. No scan whose only purpose is to re-test this cocycle law is authorized.

## Frozen negative / closed routes

- Original linear-only rank-4 D4 lifting observable: FAIL/CLOSED due to lift-independence failure.
- Preferred Nielsen lifts: permanently prohibited as repair.
- Naive q=9 degree-9 relation space: not H-stable.
- Artificial H-closure of the q=9 relation space: invalid as a presentation relation object.
- Q3/Q9 S9 orbit route: CLOSED at definition level.
- D9-OBS natural p-layer candidate: FAIL/CLOSED as a universal p-layer shadow.
- Quotient-valued Delta_q cocycle: CLOSED as **coboundary / no new information**.

## What remains genuinely open

### Gate A — non-coboundary q-sensitive datum definition

A new candidate must satisfy all of the following before computation:

1. **Definition boundary:** its input may not already contain q=3 versus q=infinity as an explicit label or subtraction.
2. **Non-coboundary test:** it must not reduce to g.v-v for a fixed v in a pre-existing representation.
3. **Intrinsicity:** it must survive allowed IA/lift changes without choosing a preferred lift.
4. **Presentation/coordinate legitimacy:** its definition must be independent of arbitrary free-group coordinates, or the precise quotient/torsor mechanism must be proved.
5. **Nontriviality:** there must be a concrete witness showing the datum is not identically zero or a universal p-layer shadow.
6. **q-separation:** only after the datum is defined from admissible weak data may q=3 and q=infinity be compared.

A candidate failing (1) or (2) is closed immediately; no broad scan is warranted.

### Gate B — relation to the orientation character

The rank-4 D4 condition
g e_1 = mu(g)e_1
was previously used as a candidate admissibility condition, but its connection to the target orientation character chi has not been independently established.

This must be tested as a separate mathematical statement. In particular, do not assume that the line/eigenvector condition recovers chi merely because mu is visible in the ambient GSp action.

## Current authorized work

1. Audit/define a genuinely non-coboundary datum, preferably using the retained filtered/extension structure rather than Delta_q.
2. Independently analyze the exact relation between g e1 = mu(g)e1 and chi.
3. Only after a definition gate passes may a new small CI control be designed.

No unrestricted rank-4 scan is currently authorized.

## Latest implementation result

Structured cocycle audit with explicit coboundary check:
- run: 35420266538
- commit: bd53311cf45dfc930599c3c24b60df8572c155cc
- job: 105836490226
- conclusion: SUCCESS

This verifies the hand derivation against the script; it does not create a new invariant.


## A-1 coboundary control — REGISTERED / EXECUTION PENDING

The pre-registered A-1 control has been added before any broader scan.

Plan: plans/RANK4_D4_DELTA_Q_COBOUNDARY_CONTROL_2026-09-19.md
Script: research/rank4_D4_delta_q_coboundary_control_2026-09-19.py
Workflow: .github/workflows/rank4-d4-delta-q-coboundary-control.yml

T1 directly checks Delta_q(g)=g.[X1^3]-[X1^3] for all 9 structured representatives. T2 uses q-blind controls X2^3, X1X2X1, and a fixed non-monomial degree-3 tensor. T3 compares the 81-pair nonzero quotient-class count with the direct coboundary prediction.

The historical H_adm=1296 enumeration is not reconstructed in this gate because no separately reusable authoritative implementation was found in the frozen structured script; no new enumeration is invented.

No mathematical PASS/FAIL is recorded until CI execution is independently checked.


## A-1 execution result — T1 PASS / T2 CONTROL INVALID / T3 PASS

CI run 35420831517, diagnostic commit c1ac93d673af3aefb9d1c4e3df139e31f6ab56ec, job 105838085431: workflow SUCCESS.

T1: zero failures on all 9 representatives for Delta_q(g)=g.[X1^3]-[X1^3].
T3: zero direct vector failures on all 81 ordered pairs; observed and predicted nonzero class count both 60.

T2 produced 0 failures for X1^3 and X2^3 but 5 failures for X1X2X1 and 5 for the arbitrary tensor. This is classified as a control-model/implementation failure, not a non-coboundary result: the frozen evaluator is a truncated free-group/group-algebra evaluator, not a direct homogeneous Magnus/Lie substitution evaluator. X1^3 is exceptional in characteristic 3 because (1+X1)^3=1+X1^3.

Therefore A-1 is NOT yet closed as a three-test experiment. No broader scan is authorized. Next step is either a legitimate pure Magnus/Lie control definition or closure by the algebraic proof plus T1/T3, with the invalid T2 explicitly removed.


## New gate — Rank-2 relator-unit digit (definition only)

A new definition gate has been opened after the Delta_q coboundary closure:
`plans/RANK2_UNIT_DIGIT_DEFINITION_GATE_2026-09-19.md`.

Target: determine whether the first mod-9 digit of the relator unit u(phi) for actual automorphisms of the rank-2 Demushkin model can carry lift-dependent information invisible in the induced g in GL_2(F_3). The candidate is required to be q-blind at definition time and must not use a preferred lift.

The gate is **OPEN / DEFINITION ONLY**. No computation is authorized yet. The next step is a hand derivation of the exact relator-unit normalization and composition law, followed by q=infinity and q=3 mod-9 constraints. The identification of this unit with the canonical orientation is explicitly not assumed; it is EXTERNAL / TO VERIFY.


## Rank-2 unit-digit hand derivation checkpoint — 2026-09-19

A critical review of the earlier hand derivation found that lift-independence of the relator scalar was asserted too strongly. The prior statement is withdrawn.

Corrected status:
- (R/[R,F]) and the scalar action for a **chosen stabilizing free lift** remain the object under study, subject to the relation-module normalization.
- Multiplicativity is valid at the lift level, but does not yet descend to \\(\\operatorname{Aut}(G_q)\\) until lift-independence is proved.
- q=infinity: the determinant calculation remains a control derivation, not a closure of D1.
- q=3: the orientation/abelianization constraint remains auxiliary support only; it does not determine (u\\bmod9).
- The previously suggested formal IA substitution (x_1\\mapsto x_1[x_1,x_2]) is **not** admissible as a free lift witness until its status as a free-group automorphism is proved.

The key missing lemma is now explicit: determine the action on (R/[R,F]) of
\\[
\\ker(\\operatorname{Stab}(R)\\to\\operatorname{Aut}(G_q)).
\\]
If this kernel acts trivially, D1 can be closed; if not, the lift-independent (u(\\phi)) definition fails and the gate must be redesigned.

Therefore the Rank-2 unit-digit gate remains **OPEN / INCONCLUSIVE / HAND-DERIVATION CONTINUING**. No finite scan is authorized.

Next exact task: analyze the stabilizer-to-(\\operatorname{Aut}(G_q)) kernel before any (K_3) scan or mod-9 computation.



## 2026-09-19 — Rank-2 unit-digit structural correction

A further hand audit found a more fundamental problem with the proposed relator-unit definition. The earlier assumption (R/[R,F]\cong\mathbf Z_3) for q=3 is not established and conflicts with the standard five-term/Hopf exact sequence
\[
H_2(G,\mathbf Z_3)\to R/[R,F]\to F_{ab}\to G_{ab}\to0.
\]
For (G_3^{(2)}), (F_{ab}\cong\mathbf Z_3^2) and (G_{ab}\cong\mathbf Z_3\oplus\mathbf Z/3), so (R/[R,F]) has the rank-one abelianized-relation contribution; together with (H_2(G,\mathbf Z_3)\cong\mathbf Z_3) for the infinite Demushkin group, the module is not justified as a single relator line. Thus the scalar equation (	ilde\phi([r_3])=u[r_3]) is not intrinsically defined without an additional quotient/projection.

The Rank-2 relator-unit gate is therefore **OPEN / INCONCLUSIVE at a deeper definition failure**, not merely awaiting lift-kernel analysis. No mod-9 or IA scan is authorized. Next task: determine whether a canonical quotient of (R/[R,F]) exists whose automorphism action supplies the intended scalar; otherwise close/redesign this route.


## 2026-09-19 — Rank-2 relator-unit route CLOSED by explicit lift-kernel witness

The definition-level analysis is now complete enough to close this route; no finite computation is warranted.

For q=3, the five-term/Hopf sequence gives 0 -> H2(G3,Z3) -> M:=R/[R,F] -> F_ab -> G3_ab -> 0. Since F_ab is Z3^2 and G3_ab is Z3 ⊕ Z/3, the natural rank-one quotient is Q:=M/H2(G3,Z3) ≅ ker(F_ab -> G3_ab)=3 Z3 e1.

This quotient nevertheless fails lift-independence. For any r in R, alpha_r(x1)=x1 r, alpha_r(x2)=x2 induces the identity on F/Phi(F), hence is an automorphism of the free pro-3 group; since r=1 in G3 it induces id_G3 and lies in the stabilizer-to-Aut(G3) kernel. Taking r=r3 gives [r3]_F_ab=3e1, so alpha_r3 sends e1 to 4e1 and 3e1 to 4(3e1). Thus the same group automorphism id_G3 has two stabilizing free lifts whose actions on Q differ by the unit 4, already nontrivially modulo 9.

Decision: Rank-2 relator-unit digit route = FAIL / CLOSED. This is a definition-level lift-independence failure, not a computational failure. The full R/[R,F] also contains the H2 component, so there is no canonical single relator line to rescue the scalar construction. No mod-9, K3, IA, or q-comparison scan is authorized for this route.

The next authorized task returns to the independent bridge between g e1=mu(g)e1 and the canonical orientation chi; no implication is assumed.


## 2026-09-19 — Rank-2 route scope correction after critical review

The prior wording “Rank-2 relator-unit digit route = FAIL / CLOSED” was too broad. The explicit witness proves a narrower statement:

- **FAIL:** the proposed relator-unit scalar construction on the natural canonical abelianized rank-one quotient
  \(Q=M/H_2(G_3,\mathbf Z_3)\cong3\mathbf Z_3e_1\) is not lift-independent.
- **FAIL:** therefore that specific scalar cannot descend to \(\operatorname{Aut}(G_3)\), even modulo 9.
- **NOT PROVED:** every possible construction using the full relation module \(R/[R,F]\), or every possible filtered relation-module quotient, is impossible.

Accordingly, the broader “entire relator-module strategy is closed” claim is withdrawn. Any genuinely different intrinsic construction would require its own definition gate and independent proof of lift-independence/naturality.

The next authorized branch remains the independent bridge audit:
\[
ge_1=\mu(g)e_1\quad\text{versus}\quad\chi.
\]
No implication between \(\mu\) and \(\chi\) is assumed.


## 2026-09-19 — Critical correction: relation-module rank-one objection withdrawn

A further literature/structural audit found that the preceding “R/[R,F] is not rank-one because H_2(G,Z_3) contributes an extra component” argument was incorrect for this one-relator pro-p presentation. Standard Demushkin deformation literature explicitly uses that when the relation subgroup is normally generated by one relator, the relation module R/[R,F] is Z_p, and in the q != 0 case it maps into F^ab with index q. Thus for r_3=x_1^3[x_1,x_2], the map R/[R,F] -> F_ab sends a chosen generator to 3e_1 and is injective.

Accordingly:
- the earlier claim that the q=3 relation module itself has an unavoidable extra H_2 component is **WITHDRAWN**;
- the natural quotient Q=M/H_2(G_3,Z_3) is not needed for the argument and should not be treated as the canonical object;
- the explicit lift-kernel witness is stronger in the corrected setting: because M is already rank one and its image is 3e_1, the stabilizing lift alpha_{r_3} acts by 4 on M itself (mod 9), not merely on an auxiliary quotient.

The lift-independence FAIL therefore remains, and indeed becomes cleaner: the proposed scalar attached to a chosen stabilizing free lift does not descend to Aut(G_3). No mod-9/IA scan is authorized for this construction.

This correction supersedes the immediately preceding “non-rank-one relation module” discussion, but does not reopen the failed lift-independent scalar route.


## 2026-09-19 — Orientation bridge hand audit: mu versus chi

A new hand-derivation checkpoint was completed in \`research/ORIENTATION_MU_BRIDGE_HAND_AUDIT_2026-09-19.md\`.

Established:
- \(\chi:G\to\mathbf Z_3^\times\) and \(\mu\) on the degree-one automorphism side have different domains and coefficient groups.
- For q=3, \(G^{ab}\cong\mathbf Z_3^3\oplus\mathbf Z/3\), and the torsion subgroup gives a canonical one-dimensional line whose Frattini image is the project’s \(e_1\)-line under the frozen identification.
- Canonical orientation is automorphism-invariant: \(\chi\circ\phi=\chi\). In the standard presentation this forces the x2 coefficient of \(\phi(x_2)\) to be 1 mod 3.
- Therefore, for an actual automorphism whose degree-one matrix satisfies \(ge_1=a e_1\) and \(g^T Jg=\nu(g)J\), the frozen generator-side convention gives \(\nu(g)=a\) mod 3.

Not established:
- \(\mu=\chi\) or any direct recovery of \(\chi\) from \(\mu\).
- \(\mu\) is not the mod-3 reduction of \(\chi\): for q=3, \(\chi(G)\subset1+3\mathbf Z_3\), while \(\mu\) may be nontrivial in \(\mathbf F_3^\times\).

Gate consequence: **PASS for type/domain separation and the conditional intrinsic interpretation of \(\mu\); OPEN for any actual recovery bridge to \(\chi\).** No finite scan yet.


## 2026-09-19 — MU-CHI bridge definition gate: manual proof

The manual proof is now recorded in \`plans/MU_CHI_BRIDGE_DEFINITION_GATE_2026-09-19.md\`.

Results:
- **PASS:** the frozen \(e_1\)-line is intrinsic: it is the Frattini image of \(\operatorname{Tor}(G^{ab})\cong\mathbf Z/3\).
- **PASS:** actual automorphisms preserve this line, giving a genuine character \(\mu_{\mathrm{int}}:\operatorname{Aut}(G)\to\mathbf F_3^\times\).
- **PASS:** under the frozen matrix/pairing convention, \(\mu_{\mathrm{int}}\) equals the degree-one GSp multiplier on the actual automorphism image.
- **FAIL:** \(\mu\) is not \(\chi\), and is not \(\chi\bmod3\); for \(q=3\), \(\chi(G)\subset1+3\mathbf Z_3\), so its mod-3 reduction is trivial.
- **OPEN:** a deeper dualizing-module construction might relate \(\chi\) plus additional canonical structure to \(\mu_{\mathrm{int}}\). No such construction is currently established.

No finite scan is authorized or needed.


## 2026-09-19 — Dualizing top-line convention audit

Frozen (g) is on the generator/(H_1) side. Hence the induced (H^1) action is (g^{-T}), and the induced (H^2) scalar is (
u(g)^{-1}). For (p=3), (mathbf F_3^	imes={pm1}), so inversion is identical: (mu_{H^2}=mu_{
m int}) as (mathbf F_3^	imes)-valued characters, although conceptually the cohomological action is inverse. This does **not** identify (mu) with the full orientation (chi:G	omathbf Z_3^	imes); (chimod3) is trivial. The MU-CHI bridge is therefore conceptually resolved: (mu) is a canonical automorphism-of-duality-line shadow, not the orientation character. No finite scan is authorized. Next work should target filtered/graded data retaining the (1+3mathbf Z_3) orientation layer.

## 2026-09-19 — Orientation mod-9 recovery gate OPEN

The MU-CHI branch is now conceptually closed: mu is the canonical F3^times character on the torsion/top-duality line, while chi is the Z3^times-valued group orientation. They are not the same object and mu carries no higher 3-adic information.

Next target is the first nontrivial orientation layer chi mod 9. A new gate requires a canonical mod-9 cohomological/Bockstein/first-lift construction and explicitly forbids reuse of the failed lift-dependent relator-unit scalar. No finite scan is authorized until the mod-9 object is hand-defined and its ambiguity is proved harmless.

## 2026-09-19 — Critical correction to mod-9 orientation gate

The first formulation overstated what mod-9 cup data could prove. The corrected status is:

- **Established:** finite-coefficient cup-product data sees the \(q=3\) power contribution; for the frozen relation its mod-9 matrix is, up to convention, \(\begin{pmatrix}6&1\\-1&0\end{pmatrix}\oplus\begin{pmatrix}0&1\\-1&0\end{pmatrix}\).
- **Not established:** this matrix recovers \(\chi(x_2)\equiv4\pmod9\).
- **Critical ambiguity:** \(H^2\)-valued pairing needs a generator/trivialization before a scalar can be extracted; basis/presentation invariance must also be proved.
- **Gate remains OPEN:** test an explicit Bockstein/finite-coefficient invariant. If it retains only q=3 and loses the value 4, close the route.

No finite scan.


## 2026-09-19 — Explicit Bockstein audit: candidate FAIL / CLOSED

The authorized hand task was completed in `research/ORIENTATION_MOD9_BOCKSTEIN_AUDIT_2026-09-19.md`.

For
\[
0\to\mathbf F_3\xrightarrow{3}\mathbf Z/9\to\mathbf F_3\to0
\]
the intrinsic connecting map
\[
\beta:H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3)
\]
was analyzed for
\[
r=x_1^3[x_1,x_2][x_3,x_4].
\]

The Bockstein detects the power-term direction: up to the fixed top-class/sign convention,
\[
\beta(\gamma_1)\neq0,\qquad
\beta(\gamma_2)=\beta(\gamma_3)=\beta(\gamma_4)=0.
\]
Classical Demushkin formulas identify this Bockstein with the power coefficients of the defining relation. This independently confirms that the finite-coefficient operation sees the q=3 power contribution.
Critical result: the intrinsic object is the map \(\beta\), not a canonically normalized scalar in \(\mathbf F_3\). Changing the generator of the one-dimensional \(H^2\) target rescales any displayed scalar. More importantly, \(\beta\) retains only the q=3 power/torsion shadow and does not retain the required first 3-adic orientation value
\[\chi(x_2)\equiv4\pmod9.
\]
Gate decision:
- **M9-A PASS:** canonical Bockstein object defined.
- **M9-B PASS:** intrinsic as a cohomological connecting map; no preferred free lift.
- **M9-C FAIL:** no canonical recovery of the value 4 from this object.
- **M9-D CLOSED for this Bockstein candidate.**

This is a candidate-level closure, not a proof that every possible finite-coefficient construction is impossible. No finite scan is authorized.

Next route, if opened, must retain additional \(1+3\mathbf Z_3\)-valued/twisted-dualizing information rather than reinterpreting the Bockstein's q=3 signal as orientation.

## 2026-09-19 — Twisted mod-9 orientation recovery: PASS / filtered-graded factorization OPEN

The ordinary Bockstein candidate was closed, so the next authorized route was the canonical twisted-coefficient surjectivity criterion.

For a candidate
\[
\rho:G\to1+3\mathbf Z/9,\qquad \rho(x_i)=1+3a_i,
\]
the reduction
\[
H^1(G,I_2(\rho))\to H^1(G,I_1(\rho))
\]
is surjective exactly when every mod-3 cocycle lifts.

Direct cocycle evaluation on
\[
r=x_1^3[x_1,x_2][x_3,x_4]
\]
gives the lift condition
\[
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4=0
\quad(\bmod 3).
\]
Since the four \(f_i\) are independent in \(H^1(G,\mathbf F_3)\), surjectivity is equivalent to
\[
(a_1,a_2,a_3,a_4)=(0,1,0,0).
\]
Hence
\[
\rho(x_2)=4\pmod9,
\]
exactly the frozen canonical orientation.

This is a substantive PASS: unlike the trivial-coefficient Bockstein, the twisted action itself carries the missing first 3-adic digit.

Gate status:
- T9-A canonical twisted finite-level object: **PASS**
- T9-B unique mod-9 recovery: **PASS**
- T9-C explicit recovery of \(\chi\bmod9\): **PASS**
- T9-D factorization through the prescribed filtered/graded data: **OPEN**

Critical limitation: this proves intrinsic recovery from twisted cohomology/full group data, not yet from the Zassenhaus graded object alone. No finite scan is authorized until that factorization question is formally defined and audited.

Detailed derivation: `research/ORIENTATION_MOD9_TWISTED_SURJECTIVITY_GATE_2026-09-19.md`.

## 2026-09-19 — New filtered-factorization gate for twisted orientation

The twisted mod-9 calculation gives a genuine PASS for intrinsic group-level recovery:
\[
\rho:G\to1+3\mathbf Z/9
\]
is uniquely selected by surjectivity of
\[
H^1(G,I_2(\rho))\to H^1(G,I_1(\rho)),
\]
and the frozen presentation yields
\[
\rho(x_2)=4\pmod9.
\]

The remaining question is now sharply isolated. Writing
\[
\rho=1+3\lambda\pmod9,
\qquad \lambda\in H^1(G,\mathbf F_3),
\]
the explicit lift obstruction is
\[
B_\lambda(f)=(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]
The canonical \(\lambda\) is the unique zero of this obstruction.

A new gate asks whether \(B_\lambda\) and its zero set can be defined intrinsically from the prescribed first restricted/Zassenhaus layers, rather than from a full presentation or preferred free lift.

Status:
- F0 candidate carrier: **PASS / strong candidate**
- F1 definition: **OPEN**
- F2 presentation/lift independence: **OPEN**
- F3 automorphism naturality: **OPEN**
- F4 uniqueness: **OPEN** at the intrinsic-object level
- F5 filtered/graded factorization: **OPEN**

No finite scan is authorized. Detailed gate: `plans/ORIENTATION_MOD9_FILTERED_FACTOR_GATE_2026-09-19.md`.

## 2026-09-19 — F1-F4 filtered-quotient audit: PASS, F5 OPEN

A new hand audit is recorded in `research/ORIENTATION_MOD9_FILTERED_FACTOR_F1_F4_AUDIT_2026-09-19.md`.

The twisted mod-9 obstruction can be formulated without a chosen free presentation or preferred free lift as a canonical twisted cocycle-lifting obstruction on the finite filtered quotient
[
C_3=G/G_4
]
of the frozen Zassenhaus/p-central filtration. The coefficient action is through
[

ho=1+3lambdapmod9,qquad lambdain H^1(G,mathbf F_3).
]
In frozen coordinates, evaluation of this intrinsic lifting problem reproduces
[
B_lambda(f)=(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
]

Status:
- **F1 definition:** PASS at the canonical finite-filtered-quotient level.
- **F2 presentation/lift independence:** PASS at that level.
- **F3 automorphism naturality:** PASS at that level.
- **F4 uniqueness:** PASS; the zero set is the singleton ((0,1,0,0)).
- **F5 factorization through the prescribed filtered/graded datum:** OPEN.

Critical boundary: this construction uses filtered extension/multiplication data of (G/G_4), not merely the associated graded vector spaces and initial quadratic relation. The q=3 power term lies in the first non-quadratic filtered layer, so discarding extension data can erase the information needed for (chimod9).

Therefore the project must not yet claim recovery from the associated graded restricted Lie object alone. The next task is to formalize exactly what counts as the allowed filtered/graded datum and determine whether it contains (G/G_4), or an equivalent extension class. No finite scan is authorized.


## 2026-09-19 — F5-A restricted graded carrier audit: PASS / F5 OPEN

A hand audit is recorded in `research/ORIENTATION_MOD9_FILTERED_FACTOR_F5_AUDIT_2026-09-19.md`.

The q-sensitive carrier is already visible in restricted/Zassenhaus degree 3: the independent q=3 versus q=infinity calculation gives
[
operatorname{in}_3(s_3)-operatorname{in}_3(s_\infty)=X_1^{[3]}.
]
Therefore the earlier wording that the q=3 power information is necessarily invisible to the associated graded restricted object is too strong and is corrected.

The minimal plausible graded carrier is
[
D_3=(V,R_2,P_3),
]
with degree-one (V), the quadratic Demuškin relation (R_2), and the degree-three restricted-power contribution (P_3).

Status:
- **F5-A carrier existence:** PASS.
- **F5 canonical obstruction reconstruction:** OPEN.

What remains is to define presentation-free operations
[
operatorname{Defect}(P_3),qquad operatorname{Twist}_\lambda(R_2)
]
whose sum is exactly (B_\lambda), and prove functoriality and uniqueness on (D_3).

Thus the project still must not claim full filtered/graded recovery. No finite scan is authorized.


## 2026-09-19 — F5 structural reconstruction: PASS for enriched degree-3 relation jet

The structural F5 task is closed at the precise enriched-carrier level. The correct carrier is the degree-3 relation jet
\[
J_3=\langle(R_2,P_3)\rangle\subset L_2\oplus L_3^{res},
\]
not two independently rescalable classes. Define, intrinsically,
\[
\operatorname{Defect}_{P_3}(f)=f(P_3),\qquad
\operatorname{Twist}_{\lambda,R_2}(f)=(\lambda\wedge f)(R_2).
\]
Then
\[
\Theta_{R_2,P_3}(\lambda)(f)=f(P_3)+(\lambda\wedge f)(R_2).
\]
In frozen coordinates this is exactly
\[
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4=B_\lambda(f).
\]
Common rescaling of the relation-jet generator rescales \(\Theta\) but leaves its zero set unchanged. Nondegeneracy of \(R_2\) makes the zero set a singleton; \(\lambda_\chi=(0,1,0,0)\), hence \(\rho=(1,4,1,1)\bmod9\).

Decision:
- **F5 structural factorization through enriched relation jet \(D_3=(V,J_3)\): PASS.**
- **Bare associated-graded object with no distinguished relation jet:** not claimed; recovery of \(J_3\) itself is a separate structural gate.

Detailed audit: research/ORIENTATION_MOD9_FILTERED_FACTOR_F5_STRUCTURAL_2026-09-19.md.
No finite scan is authorized.

## 2026-09-19 — Critical review of F5 structural PASS

The previous F5 PASS is narrowed. The formula Theta_{R,P}(lambda)(f)=f(P)+(lambda wedge f)(R) is correct once the marked degree-3 relation jet J_3=< (R,P) > is supplied, but this makes the factorization through the enriched carrier partly formal. Presentation/lift independence and naturality were stated too quickly for the unmarked problem, and minimality of D_3 was not proved.

Correct status:
- F1-F4: PASS at canonical finite-filtered-quotient level.
- F5-A: PASS for q-sensitive degree-3 carrier existence.
- F5-marked: PASS, conditional on the enriched relation jet J_3 being part of the datum.
- **F5-bare: OPEN.** The remaining substantive problem is whether the originally allowed bare filtered/graded datum canonically determines the distinguished relation jet J_3, or admits an equivalent unmarked reconstruction.

No finite scan is authorized.

## 2026-09-19 — F5-bare structural obstruction: FAIL / CLOSED

The remaining bare-graded identification question is now closed structurally, without a finite scan.

Compare
G_3 = <x_1,x_2,x_3,x_4 | x_1^3[x_1,x_2][x_3,x_4]>
with
G_infinity = <x_1,x_2,x_3,x_4 | [x_1,x_2][x_3,x_4]>.

At p=3, the power term x_1^3 has Zassenhaus degree 3 while the commutator terms have degree 2. Hence both defining relators have the same initial quadratic form R_2=[X_1,X_2]+[X_3,X_4]. Standard Demushkin graded-presentation results identify the bare associated graded restricted Lie object from this initial relation, so the q=3 and q=infinity cases have the same bare graded object.

Nevertheless their orientations differ already mod 9:
chi_3(x_2)=4 mod 9, while chi_infinity(x_2)=1 mod 9.

Therefore the bare associated graded restricted Lie object cannot determine chi mod 9, and in particular cannot canonically reconstruct the marked coupling J_3=< (R_2,P_3) >.

Important correction to F5-A: P_3=X_1^[3] exists in the ambient degree-3 restricted layer, but its being the degree-3 component of the same filtered defining relation as R_2 is extra marking/coupling data. The bare graded object does not retain that coupling.

Final branch status:
- F1-F4: PASS at the canonical finite-filtered-quotient level.
- F5-A: PASS only for existence of a q-sensitive ambient degree-3 carrier.
- F5-marked: PASS, conditional on J_3 being supplied.
- F5-bare: FAIL / CLOSED.

This is an information-level obstruction, not a failed implementation. No finite scan is authorized for reopening this route.

Detailed audit: research/ORIENTATION_MOD9_FILTERED_FACTOR_F5_BARE_OBSTRUCTION_2026-09-19.md.


## 2026-09-19 — Minimal enriched carrier: projective relation jet

After closing F5-bare, the next task is to identify the weakest natural enrichment that can still recover chi mod 9. The candidate is the projective degree-3 relation jet J_3=< (R,P) > in L_2 direct-sum L_3^res, retaining the coupling between the quadratic relation R and its degree-3 filtered component P while forgetting common scalar normalization.

The construction Theta_J(lambda)(f)=f(P)+(lambda wedge f)(R) is sufficient: for nondegenerate R it has a unique zero, and in frozen coordinates R=[X_1,X_2]+[X_3,X_4], P=X_1^[3] gives lambda_chi=e_2^*. The q=3 versus q=infinity obstruction proves that some information beyond the bare graded object is necessary.

Important boundary: sufficiency is established conditional on J_3 being supplied. Intrinsicness/presentation-independence of J_3 is the new E1-E5 structural gate. Do not call J_3 mathematically minimal yet; only the weaker necessary lower bound is justified.

Detailed plan: research/ORIENTATION_MOD9_MINIMAL_ENRICHED_CARRIER_2026-09-19.md.
No finite scan is authorized.


## 2026-09-19 — E1 relator-gauge audit: local PASS / full intrinsicness OPEN

A critical no-scan audit tested the candidate projective degree-3 relation jet against relator conjugation. If a filtered relator has degree-(2,3) terms (R,P), replacing it by u r u^{-1} with degree-one term v leaves R unchanged and changes the degree-3 ordinary Lie component by P -> P+[v,R] (up to convention/sign). Therefore common scaling alone is not a sufficient presentation-independence argument.

The recovery functional nevertheless descends through this gauge: for f in V*=H^1(G,F_3), f([v,R])=0, so f(P+[v,R])=f(P), while (lambda wedge f)(R) is unchanged. Hence Theta_{R,P} and its zero set are invariant under relator conjugation.

Decision:
- **E1-local gauge compatibility: PASS.**
- **E1-full intrinsic definition: OPEN.**

The next task is to identify the canonical relation-module quotient containing all legitimate relator changes. In particular, [V,R] is a necessary gauge quotient but is not yet proved to be the complete gauge group. The projective relation jet remains a candidate sufficient carrier, not an intrinsic invariant yet. No finite scan is authorized.

Detailed audit: research/ORIENTATION_MOD9_E1_RELATOR_GAUGE_AUDIT_2026-09-19.md.


## 2026-09-19 — E1 relation-module candidate

The next structural step is to replace the chosen-relator jet by a relation-module container. For a minimal free presentation 1 -> R -> F -> G -> 1, the natural candidate is R/[F,R], which kills relator conjugation automatically. The desired degree-(2,3) jet should be extracted from its Zassenhaus-filtered image into L_2(F) direct-sum L_3^res(F).

This is only a candidate: R/[F,R] is relative to a chosen free presentation, and the degree-(2,3) jet map plus independence under changing minimal free presentation remain OPEN. Therefore E1 full intrinsicness is not PASS. No finite scan is authorized.

Detailed candidate audit: research/ORIENTATION_MOD9_E1_RELATION_MODULE_CANDIDATE_2026-09-19.md.


## 2026-09-19 — E1 relation-module structural lemma

A no-scan structural audit sharpened the relation-module candidate. For a minimal free pro-3 presentation 1 -> R -> F -> G -> 1, the quotient R/[F,R] is a valid fixed-cover container for the defining relation and kills relator conjugation. The continuous homology five-term sequence gives H2(G,Z3) -> R/[F,R] -> F_ab -> G_ab -> 0; minimality makes F_ab -> G_ab an isomorphism, so the middle map is zero. This does NOT justify identifying R/[F,R] with H2(G,Z3), and no such identification is claimed.

The remaining E1 problem is therefore sharply separated: internal relator-conjugation gauge is handled, but change of minimal free cover and the induced degree-(2,3) jet remain unproved. See research/ORIENTATION_MOD9_E1_RELATION_MODULE_LEMMA_2026-09-19.md.

Status: E1-local conjugation gauge PASS; R/[F,R] fixed-cover container PASS / structurally justified; degree-(2,3) jet extraction OPEN; change of minimal free cover OPEN; E1 full intrinsicness OPEN. No finite scan authorized.


## 2026-09-19 — E1 cover-change audit

The change-of-cover problem was reduced to free isomorphisms/lifts lying over id_G. The explicit stabilizing lift from the earlier rank-2 analysis shows that full relation-module cover-independence is false: the relation generator can be multiplied by 4 mod 9. Therefore R/[F,R] must not be declared an intrinsic generator-level object.

The relevant weaker target is projective-jet invariance. Conditional on the standard cyclic one-relator relation-module structure and a residual degree-(2,3) gauge lemma, a cover change would act by (R,P) -> (uR,uP+[v,R]); then Theta scales by u and its zero set is unchanged. This residual-gauge lemma is not yet proved.

Status: full relation-module cover-independence FAIL; projective-jet cover-independence OPEN; Theta invariance under common scaling/conjugation gauge PASS. No finite scan authorized. Detailed audit: research/ORIENTATION_MOD9_E1_COVER_CHANGE_AUDIT_2026-09-19.md.


## 2026-09-19 — E1 residual-gauge lemma PASS

A no-scan degree-(2,3) derivation closes the remaining residual-gauge question relevant to Theta. For a free automorphism inducing id_G, minimality and the one-relator initial relation imply alpha(X_i)=X_i+c_i R_2+O(3). Applying alpha to R_2 gives the degree-3 correction [R_2,v], where v=c_1X_2-c_2X_1+c_3X_4-c_4X_3. The relation-module class may additionally acquire a common unit factor u, so the jet transforms as (R,P) -> (uR,uP+[v,R]). Since f([v,R])=0 for f in V*, Theta scales by u and its zero set is unchanged.

Decision: E1 residual-gauge lemma PASS at the degree-(2,3) level relevant to Theta. Full relation-module generator invariance remains FAIL, but projective degree-(2,3) jet invariance relevant to Theta is PASS, conditional on the standard minimal one-relator facts and frozen filtered convention. Detailed proof: research/ORIENTATION_MOD9_E1_RESIDUAL_GAUGE_LEMMA_2026-09-19.md. No finite scan authorized.


## 2026-09-19 — E1–E5 closure: intrinsic mod-9 recovery PASS

A full no-scan hand audit was completed after the residual-gauge lemma. The remaining presentation issue was separated from the false generator-level relation-module invariance.

For a minimal free pro-3 presentation, the degree-(2,3) relation jet transforms under a change of minimal cover by
\\[
(R,P)\\mapsto(uR,uP+[v,R]),
\\]
with common unit scaling u and the residual conjugation gauge [v,R]. Degree-one functionals annihilate the bracket term, so the recovery functional
\\[
\\Theta_J(\\lambda)(f)=f(P)+(\\lambda\\wedge f)(R)
\\]
is multiplied only by u. Its zero set is therefore intrinsic under presentation, lift, relator-gauge, and normalization changes, conditional on the standard minimal one-relator pro-3 presentation facts and frozen filtered convention.

Automorphism naturality follows from functoriality of evaluation/exterior powers and the same gauge cancellation. For q=3 the unique zero is \\(\\lambda=e_2^*\\); for q=infinity it is \\(\\lambda=0\\). Thus the enriched carrier separates the two cases and recovers
\\[
\\boxed{\\chi\\pmod 9}
\\]
without inserting q into the definition.

Decision:
- E1 Definition: PASS (at the recovery-functional/projective-gauge level).
- E2 Presentation/lift independence: PASS at degree (2,3), conditional on standard minimal one-relator facts.
- E3 Functoriality: PASS at the same level.
- E4 q=3 versus q=infinity separation: PASS.
- E5 recovery of \\(\\chi\\bmod9\\): PASS.

The raw relation-module generator remains non-invariant; this is not a defect for the zero-set construction. Mathematical minimality of the projective jet is not proved. The bare associated graded restricted Lie object remains FAIL/CLOSED. Full \\(\\mathbb Z_3^\\times\\)-valued \\(\\chi\\) and higher mod-\\(3^n\\) reconstruction remain open.

Detailed audit: research/ORIENTATION_MOD9_E1_E5_CLOSURE_HAND_AUDIT_2026-09-19.md. No finite scan was used or authorized.


## 2026-09-19 — Full 3-adic orientation: hand derivation PASS

The mod-9 result was pushed further by a no-scan exact crossed-derivation calculation using the standard commutator convention [x,y]=x^{-1}y^{-1}xy. For rho:G->1+3Z_3, evaluating a rho-crossed derivation on r=x_1^3[x_1,x_2][x_3,x_4] forces r_1=r_3=r_4=1 and then 1+2r_2=0. Hence
\\[
\\boxed{\\chi(x_2)=(1-3)^{-1},\\quad \\chi(x_i)=1\;(i\\ne2).}
\\]
Modulo 3^n this gives the complete tower rho_n(x_2)=(-2)^{-1} mod 3^n; e.g. 4 mod 9, 13 mod 27, 40 mod 81, 121 mod 243.

The key distinction is now fixed: the degree-(2,3) projective relation jet recovers the first nontrivial digit mod 9, while the compatible full filtered relation-jet tower recovers the entire 3-adic character. No new independent higher obstruction is needed for this q=3 normal form. The bare associated graded object remains insufficient, and finite-jet minimality remains open.

The exact hand derivation uses the standard intrinsic crossed-derivation characterization of the canonical Demushkin orientation. External classification/orientation references confirm the standard formula chi(x_2)=(1-q)^(-1) for the q-power normal form. Detailed audit: research/ORIENTATION_FULL_3ADIC_HAND_DERIVATION_2026-09-19.md. No finite scan was used.


## 2026-09-19 — Carrier category result: raw J_3 is not minimal; coarsest natural quotient identified

The categorical branch was pushed without literature or finite scan. A natural degree-(2,3) carrier category was fixed using filtered relation jets and the full degree-one evaluation family Theta. The canonical quotient
\[
L^{res}_3(V)\twoheadrightarrow L^{res}_3(V)/[V,L_2(V)]\cong V^{(1)}
\]
removes exactly the degree-3 bracket/gauge part invisible to degree-one evaluation. Writing p(P) for the image of P gives the compressed projective carrier
\[
\overline J_3=[(R,p(P))].
\]
Any functorial quotient of J_3 preserving all degree-one Theta observables must retain [R] and p(P), hence factors uniquely through \overline J_3. Thus \overline J_3 is terminal/coarsest in the natural quotient category.

Important correction: the raw projective jet J_3 is NOT minimal in this natural category. The unrestricted claim of minimality among arbitrary alternative carriers remains ill-posed without an independently fixed larger category. The recovery-only zero-set carrier can be compressed further to the recovered covector, but that is tautological rather than an independent relation carrier.

Record: research/ORIENTATION_MOD9_CARRIER_CATEGORY_COARSEST_QUOTIENT_2026-09-19.md
Decision: carrier-category/coarsest-quotient branch PASS; raw J_3 minimality FAIL/CLOSED within the natural quotient category; unrestricted absolute minimality OPEN/ill-posed.


## 2026-09-19 — Exact Z_3 compression audit: characteristic-0 boundary found

The proposed exact analogue of the mod-3 compressed carrier was pushed to its structural endpoint. A naive replacement of the characteristic-3 restricted-Lie quotient by a Z_3-restricted Lie object is invalid: restricted Lie algebras are characteristic-p structures, so the mod-3 quotient cannot simply be scalar-extended to Z_3. The correct exact carrier must instead be defined from the filtered relation module together with coefficient-level crossed-derivation evaluations C_n. The projective/gauge mechanism survives, and the fixed q=3 exact calculation still gives rho(x_1)=rho(x_3)=rho(x_4)=1 and 1+2rho(x_2)=0, hence chi(x_2)=-1/2.

The exact coefficient condition is nonlinear in the orientation values, so the simple mod-3 linear Theta cannot simply be reused over Z_3. A canonical exact evaluation quotient can be defined using all natural coefficient evaluations C_n, but a non-tautological finite two-component description analogous to ([R],p(P)) is not yet proved.

Record: research/ORIENTATION_EXACT_Z3_COMPRESSED_CARRIER_AUDIT_2026-09-19.md
Decision: exact full-chi recovery PASS/CLOSED; naive Z_3 restricted-Lie compression FAIL/CLOSED; exact concrete compression OPEN.


## 2026-09-19 — Methodology sufficiency gate

A dedicated methodology audit was completed after comparison with the process used in Pál–Quick and Blumer–Quadrelli. The relation-jet branch has enough machinery for a bounded theorem program, but the intrinsic-minimality objective still requires three structural bridges:

1. **M1 — intrinsic carrier functor:** define the degree-(2,3) carrier directly from filtered/augmentation-relation data, independent of chosen lifts and without inserting q.
2. **M2 — orientation factorization:** prove a natural, non-tautological map from the carrier to the finite-level crossed-derivation coefficient data whose unique solution is the canonical orientation.
3. **M3 — independent comparison:** obtain a natural map/factorization, or a rigorous obstruction to one, between the carrier and Pál–Quick's A3/Hochschild canonical class.

Methodological warning: Pál–Quick's process is canonical object -> obstruction -> explicit computation; our failed/risky branches can invert this into computed object -> hoped-for interpretation. New computation must therefore pass object/input/functoriality/gauge/orientation/q-blindness/separation/novelty tests first.

The IA/filtered-extension and W/U/O branches are subordinate to this gate. Local computational PASS results do not authorize expansion unless they produce a bridge to M1, M2, or M3. No broad scan is authorized merely because higher-order structure exists.

Record: research/METHODOLOGY_SUFFICIENCY_AND_MISSING_TOOLS_AUDIT_2026-09-19.md


## AUTHORITATIVE UPDATE — 2026-09-19 — RESEARCH CONTINUITY PROTOCOL

The project now has an explicit cross-chat continuity contract:
`research/RESEARCH_CONTINUITY_PROTOCOL.md`.

The protocol freezes the restoration order (RESEARCH_MAP -> CURRENT_STATE -> RESEARCH_LOG -> relevant stage document), the pre-computation tests, theorem-quality thresholds, PASS/FAIL/OPEN/CONDITIONAL/HISTORICAL classification, publication-discipline test, and the rule that literature papers contribute reusable methodology only after object/input/invariance/verification/logical-boundary transfer is explicitly recorded.

This is a methodological control, not a new mathematical result. It exists to ensure that future sessions cannot silently change definitions, revive closed branches, confuse validation with novelty, or lose the stage-specific PASS/FAIL consequences.

The current principal program remains D0 definition -> D1 intrinsicity -> D2 orientation bridge -> D3 carrier/coarseness -> D4 independent comparison. No broad scan is authorized merely by opening a new chat.


## AUTHORITATIVE UPDATE — 2026-09-19 — FOX ROW IDENTIFICATION GATE CLOSED

The load-bearing Fox logical gap has been attacked directly rather than by further presentation scans.

A standard characterization of the canonical Demuškin orientation (Labute/Serre) says that a character chi is the canonical orientation exactly when every chi-crossed derivation of the free pro-p presentation descends through the defining relator, i.e. kills the relator. Modern explicit Demuškin calculations use precisely this characterization: arbitrary generator values are assigned to the crossed derivation and the relator equation is expanded coefficient-by-coefficient. citeturn2search0turn2search3

Fox calculus gives, for arbitrary generator values d_i,
D(r)=J_r(chi)d,
where J_r(chi) is the evaluated Fox row used throughout this branch (up to the fixed left/right convention, which does not affect the zero locus). Since the free-generator values d_i are arbitrary,
D(r)=0 for all crossed derivations iff J_r(chi)=0.

Therefore
[canonical Demuškin orientation] iff [universal crossed-derivation descent] iff [J_r(chi)=0].
For r=x_1^3[x_1,x_2][x_3,x_4], the exact row-zero equations on (1+3 Z_3)^4 give
chi(x_1)=chi(x_3)=chi(x_4)=1,chi(x_2)=-1/2=(1-3)^(-1).

This closes the previous A/B/C logical gap: ker J != 0 was too weak, but the canonical criterion quantifies over all crossed derivations, which is exactly row vanishing.
The Nielsen stress test already established exact coordinate covariance for two nontrivial presentation changes; the general Fox chain rule supplies the mechanism.

Decision:
- Fox row = crossed-derivation coefficient row: PASS / CLOSED.
- canonical orientation = universal crossed-derivation descent: PASS / CLOSED under the standard Demuškin orientation theorem.
- canonical orientation = Fox row-zero: PASS / CLOSED.
- Nielsen covariance: PASS / CLOSED.
- exact fixed-q=3 Fox carrier: PASS / CLOSED.
- intrinsic filtered realization of the exact Fox carrier: OPEN.
- exact Fox carrier → intrinsic mod-9/projective relation jet comparison: NEXT TARGET.

Detailed record: research/ORIENTATION_FOX_ROW_IDENTIFICATION_THEOREM_2026-09-19.md


## AUTHORITATIVE UPDATE — 2026-09-19 — FOX → MOD-9 COMPATIBILITY GATE

The exact Fox carrier was compared directly with the independently constructed intrinsic degree-(2,3) mod-9 relation-jet carrier.

Write
A=1+3a, B=1+3b, C=1+3c, D=1+3d.
For the exact Fox zero ideal,
F1=B(1+A)+A^2, F2=A-1, F3=D-1, F4=C-1.
Then
F1/3 = 1+2b mod 3,
F2/3=a, F3/3=d, F4/3=c.
Hence the exact Fox condition modulo 9 is
a1=a3=a4=0 and a2=1 mod 3,
i.e. chi ≡ (1,4,1,1) mod 9.

Independently, the intrinsic projective relation-jet carrier [(R,p(P3))] with
R=[X1,X2]+[X3,X4], p(P3)=X1^(1)
has the unique recovery covector lambda=e2*, which gives exactly the same first character digit.

Decision:
- exact Fox row = canonical orientation: PASS / CLOSED;
- first normalized Fox obstruction mod 9 = intrinsic relation-jet recovery: PASS / CLOSED for the frozen q=3 carrier and tested coordinate changes;
- general natural identification of the full exact Fox coefficient tower with the intrinsic filtered tower: OPEN;
- full filtered-to-Fox factorization at every 3-adic level: NEXT TARGET.

Detailed record: research/ORIENTATION_FOX_TO_MOD9_CARRIER_COMPATIBILITY_2026-09-19.md


## AUTHORITATIVE UPDATE — 2026-09-20 — HIGHER BOCKSTEIN / P-ADIC DIGIT TOWER HARD ATTACK

The proposed next bridge was attacked at the definition level. Candidate-dependent twisted coefficient/Bockstein criteria are exact orientation tests but cannot serve as the desired filtered input without importing the unknown character. Higher Bocksteins may detect q-adic depth, but no character-valued, presentation-natural reconstruction map follows from their existence alone. For the frozen q=3 Fox equations, once the mod-9 digit is fixed, all higher digits are recursively forced by the exact unit equation 1+2B=0; no independent higher geometric obstruction was found. Therefore the substantive unresolved map remains
\[
\text{intrinsic filtered relation extension}\to\text{exact Fox coefficient tower},
\]
without defining the former from the latter.

Decision: **HIGHER BOCKSTEIN BRIDGE OPEN / STRUCTURAL**. Stronger no-go: “higher Bocksteins recover q, therefore full chi” is not an established implication. Detailed audit: `research/ORIENTATION_HIGHER_BOCKSTEIN_HARD_ATTACK_2026-09-20.md`.


## AUTHORITATIVE UPDATE — 2026-09-20 — FILTERED EXTENSION VS ASSOCIATED GRADED BOUNDARY

A further structural distinction is now closed. A fixed or finite associated-graded Zassenhaus window cannot recover full $3$-adic orientation; the family $q=3^s$ moves the power term beyond any prescribed finite degree while changing $\chi$. By contrast, an actual compatible inverse system of filtered relation residues determines the completed relator by completeness, and continuity of completed Fox calculus then gives the exact obstruction. This is PASS / LOCAL, not yet a new compression theorem: such a tower is essentially the completed filtered relation itself. The only remaining substantive carrier problem is an intermediate q-blind intrinsic object that retains extension data sufficient for all digits while being genuinely smaller than the full completed Fox/presentation object.

Detailed audit: `research/ORIENTATION_FILTERED_EXTENSION_VS_GRADED_HARD_ATTACK_2026-09-20.md`.


## AUTHORITATIVE UPDATE — 2026-09-20 — RESEARCH PROGRAM SYNTHESIS / MOD-27 GATE

A consolidated research map has been frozen in research/RESEARCH_PROGRAM_SYNTHESIS_2026-09-20.md.

### Refined central question
The project is not merely to compute the canonical orientation. The target is to determine **how much filtered/relation information is necessary and sufficient** to recover
\[
\chi:G\to\mathbf Z_3^\times,
\]
and whether the required non-graded extension information admits a presentation-natural, q-blind, non-tautological carrier strictly smaller than the completed characteristic-zero Fox/presentation object.

### Established boundary
- full mod-3 Zassenhaus associated graded: **FAIL / CLOSED** for q and full chi; the complete graded Demuškin object is q-blind in the present odd-prime fixed-rank setting;
- projective degree-(2,3) carrier overline J_3=[(R,p)]: **PASS / CLOSED** for chi mod 9 under the audited standard transgression/Bockstein convention;
- compatible full filtered extension tower -> full chi: **PASS / LOCAL**, by inverse-limit reconstruction of the completed relation followed by continuous Fox calculus, but this is not a compression theorem;
- exact universal Fox carrier: **PASS / CLOSED** for full chi under the audited hypotheses;
- exact local Fox algebra is already Z_3, so quotienting it cannot produce a smaller full-3-adic-preserving carrier: **PASS / CLOSED** for quotient compression;
- independent intrinsic non-quotient exact compression: **OPEN**.

### Explicitly ruled out
Naive Z_3 augmentation jet; naive Z_3 scalar extension of the characteristic-3 restricted-Lie carrier; intrinsic fixed degree-3 Fox truncation; higher-Bockstein-alone reconstruction; full associated-graded tower reconstruction; universal bounded-degree + bounded-precision recovery; quotient compression of the exact local Fox algebra.

### Still OPEN
Information-theoretic minimality of P_3; absolute minimality of overline J_3 outside the defined quotient-observable category; existence of an intrinsic finite-level J_27; compatibility J_(3^{n+1}) -> J_(3^n); an intrinsic inverse-limit carrier strictly smaller than full Fox; and a non-tautological natural factorization from intrinsic filtered extension data to the exact Fox coefficient tower.

### NEXT AUTHORIZED GATE: intrinsic mod-27 carrier
The first decisive next question is
\[
\boxed{J_{27}(G)\Rightarrow\chi\bmod27?}
\]
with all six requirements: (1) q-blind input independent of unknown chi; (2) presentation/Nielsen/relator-gauge intrinsicity; (3) separation of chi mod 27; (4) natural reduction to the established mod-9 carrier; (5) non-tautology—not merely Fox equations modulo 27 under a new name; (6) genuine structural compression if compression is claimed.

Stop rule: definition failure -> FAIL/CLOSED; invariance failure -> FAIL/CLOSED; failure to separate mod 27 -> FAIL/CLOSED. Only a surviving candidate advances to higher levels.

The full program is summarized in research/RESEARCH_PROGRAM_SYNTHESIS_2026-09-20.md.

 
## 2026-09-20 — CRITICAL REVIEW: FORMALIZE INTRINSIC CARRIER BEFORE MOD-27

The consolidated synthesis was attacked again. The main surviving weakness was not a mathematical counterexample but a methodological ambiguity: "intrinsic", "non-tautological", and "strictly smaller" were not yet operational enough to serve as hard Gate conditions.

Binding correction:
- formalize the admissible category, morphisms, gauge transformations, coefficient/target category, and functoriality before any mod-27 computation;
- define q-blindness at construction time, excluding chi/q from the input;
- require an explicit natural orientation bridge and a commuting reduction J_27 -> J_9;
- replace the informal non-tautology condition by the operational criteria in research/INTRINSIC_CARRIER_FORMAL_GATE_PRE_MOD27_2026-09-20.md;
- treat "smaller" only relative to an explicitly declared comparison category/invariant;
- do not require compression to prove existence of a legitimate J_27; an intrinsic separating candidate with unresolved compression is PASS / LOCAL or OPEN;
- treat the full filtered inverse-limit route as formal sufficiency, not as substantive compression evidence;
- keep M3 literature comparison parallel to any novelty claim.

This correction prevents a self-imposed overstrong Gate from turning failure of a chosen definition into a false mathematical no-go result.

The mod-27 branch remains the next substantive target, but only after this formal gate is accepted.


## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 18: MOD-27 BOCKSTEIN CARRIER SYMMETRY NO-GO

The proposed coefficient-extension carrier was attacked at the level of its own automorphism group. In the frozen \(q=3\) case,
\[
S(a_1,a_2,a_3,a_4)=(a_1,4a_2,a_3,a_4)
\]
preserves reduction, the inclusion \(\iota\), cup product, and \(\beta_9\), while acting nontrivially on the missing \(\mathbf Z/9\)-lift of the mod-3 \(e_2\) direction. Therefore the declared carrier cannot canonically select
\[
\lambda_{27}=\frac13\log\chi\equiv e_2\pmod9.
\]

Decision:
- **\(\mathcal B_{27}\) as a mod-27 orientation carrier: FAIL / CLOSED;**
- coefficient-extension package as intrinsic q/valuation-layer detector: **PASS / LOCAL;**
- a different mod-27 carrier with genuinely additional rigidifying structure: **OPEN.**

This supersedes HARD ATTACK 17. No further numerical Bockstein-only scan is authorized.


## AUTHORITATIVE UPDATE — 2026-09-20 — CORRECTION TO HARD ATTACK 18 + HARD ATTACK 19

Hard Attack 18 was critically audited and found to overstate its conclusion. The map
\[
S(a_1,a_2,a_3,a_4)=(a_1,4a_2,a_3,a_4)
\]
is an automorphism of the **abstract declared coefficient carrier**, but it was not shown to be induced by an admissible group isomorphism/gauge morphism. The formal PRE-MOD27 gate requires naturality only for the declared admissible input morphisms. Therefore the previous unconditional **FAIL/CLOSED** conclusion is superseded.

Binding correction:
- Hard Attack 18 absolute no-go: **HISTORICAL / SUPERSEDED**;
- abstract-carrier symmetry S: **PASS / LOCAL**;
- Bockstein package as q-layer detector: **PASS / LOCAL**;
- Bockstein package as a mod-27 orientation carrier: **CONDITIONAL / OPEN**.

Hard Attack 19 now freezes the missing issue as a category question. Define the abstract structure-preserving carrier category and the realizable group-induced subcategory separately. Test whether S is realizable by an admissible group automorphism/gauge. If yes, establish the true no-go. If not, identify exactly what q-blind filtered/extension structure blocks S and whether that structure is legitimate new rigidifying information or merely hidden orientation/classification/Fox data.

No further numerical scan is authorized until this realizability test is resolved.


## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 20: BOCKSTEIN NOVELTY CLOSED

Hard Attack 19 established that the abstract carrier symmetry S is not automatically an admissible group morphism, so the previous unconditional symmetry no-go is superseded. A stronger factorization attack now closes the candidate under the project's operational non-tautology gate.

On the rank-four Demuškin test family, the full declared Bockstein package has exactly three finite carrier types, determined by v_3(q)=1, 2, or >=3. The mod-27 orientation reduction on the same family has exactly the corresponding three classes. No finer q-blind invariant, independent chain-level identity, or universal property has been exhibited inside the package that distinguishes orientation lifts at fixed q-class.

Therefore:
- Bockstein package as finite q-layer detector: **PASS / LOCAL**;
- Hard Attack 18 absolute symmetry no-go: **HISTORICAL / SUPERSEDED**;
- Bockstein package as a **new non-tautological mod-27 orientation carrier: FAIL / CLOSED**;
- genuinely different successor carrier: **OPEN**.

No further beta_1/beta_9 scan on the same family is authorized. Any successor must add genuinely new q-blind rigidifying structure or an independently characterized universal property.


## AUTHORITATIVE UPDATE — 2026-09-20 — CRITICAL REVIEW OF HARD ATTACK 20

Hard Attack 20 was re-audited and its final FAIL/CLOSED was found too strong. The three observed Bockstein cases do not by themselves prove that the **entire** structured carrier \(\mathcal B_{27}\) has exactly three isomorphism types; explicit carrier isomorphisms/classification are still missing. Moreover, factorization on the tested q-family does not prove that every natural bridge on the full admissible category factors through q/classification.

Corrected status:
- Bockstein q-layer detector: **PASS / LOCAL**;
- q-factorization evidence on the tested family: **PASS / LOCAL**;
- Hard Attack 18 unconditional symmetry no-go: **HISTORICAL / SUPERSEDED**;
- Bockstein package as a non-tautological mod-27 orientation carrier: **CONDITIONAL / OPEN**.

The next decisive attack is universal/categorical, not numerical: either prove classification of the full structured carrier by the q-valuation quotient and then prove all natural bridges factor through it, or construct two admissible objects with isomorphic \(\mathcal B_{27}\) but distinct \(\chi\bmod27\). No further same-family Bockstein scan is authorized.


## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 21: FULL B27 CARRIER CLASSIFICATION ON STANDARD FAMILY

Hard Attack 21 repairs Gap 1 of Hard Attack 20 at the exact structured-object level. For the standard rank-four family and A=Z/9,
\[
H^1(G_q,A)=\{(a_1,a_2,a_3,a_4):qa_1=0\},
\]
so W_q=3A×A^3 for v_3(q)=1 and W_q=A^4 for v_3(q)≥2. The audited transgression convention gives the three full normal forms for (W_q,beta_1,beta_9), with the common mod-3 cup pairing. Hence the entire declared carrier, not merely visible Bockstein ranks, has exactly three isomorphism types on the standard q-family, indexed by v_3(q)=1,2,≥3.

This is **PASS / CLOSED** for full structured-carrier classification on the standard family and **PASS / CLOSED** for q-valuation factorization on that family.

It is deliberately NOT promoted to a universal no-go: this does not prove that every natural bridge on the full admissible filtered/relation category factors through q/classification. The B27 orientation-carrier status therefore remains **CONDITIONAL / OPEN**.

Stop: no further same-family beta_1/beta_9 scans. Next attack must be universal/categorical: prove universal factorization/no-go, or construct an independent chain-level orientation bridge.

## CRITICAL REVIEW OF HARD ATTACK 21 — 2026-09-20

Hard Attack 21 correctly repairs the principal Gap 1 from Hard Attack 20 on the standard rank-four family, but the record still contains three precision issues that must be fixed before the next universal attack.

### 1. What is actually proved
For (G_q=\langle x_1,x_2,x_3,x_4\mid x_1^q[x_1,x_2][x_3,x_4]\rangle), the calculation
\[
H^1(G_q,\mathbf Z/9)=\{(a_1,a_2,a_3,a_4)\in(\mathbf Z/9)^4:q a_1=0\}
\]
gives (3A\times A^3) for (q=3) and (A^4) for (q\ge9). Together with the displayed Bockstein normal forms this does establish the three structured-carrier isomorphism types on this standard family: class (v_3(q)=1), class (v_3(q)=2), and class (v_3(q)\ge3). The converse distinctions are also structural: the underlying (W_q) differs between (q=3) and (q\ge9), while (\beta_9\) distinguishes (q=9) from (q\ge27).

### 2. Terminology correction
The phrase “canonical normal-form identifications” is too strong. The coordinates (a_i) and the displayed models depend on a chosen standard presentation. The proved statement is: **explicit structure-preserving model isomorphisms exist in a chosen standard presentation, and the resulting abstract structured carrier has exactly three isomorphism types on this family.** No canonical basis or canonical coordinate identification is claimed.

### 3. Target formalization remains load-bearing
The notation (O_{27}) must now be fixed before any bridge theorem is claimed. It should not be treated informally as “the character”. The natural target should be defined basis-free as the appropriate orientation torsor/object together with its mod-27 logarithmic datum, so that a statement
\[
\Phi_{27}:\mathcal B_{27}\to O_{27}
\]
means an actual natural transformation in the declared category. In particular, the quantity (\lambda_{27}=\frac13\log\chi\pmod9) is an additive coordinate only after the target object and its natural action are specified; it is not itself a basis-free vector without that structure.

### 4. Universal no-go is still not proved
The standard-family classification does **not** imply
\[
\text{every natural }\mathcal B_{27}\to O_{27}\text{ factors through }q\text{-classification}.
\]
Nor does it produce the desired independent bridge. Thus the carrier remains **CONDITIONAL / OPEN**. The next decisive attacks are categorical, not numerical.

### 5. Binding next gate
Before further calculation:
- define (O_{27}) intrinsically and basis-free;
- formalize the induced action of admissible morphisms on (O_{27});
- test whether there exist admissible objects (G,G') with isomorphic full (\mathcal B_{27}) but non-isomorphic (O_{27}). Such a pair is a genuine no-go and closes the carrier;
- if no such pair can be produced, attack the universal factorization statement or construct an independent chain-level identity for (\lambda_{27}) without extracting (q), the dualizing action, or the known classification formula.

**Status after this review:**
- full structured-carrier classification on the standard family: **PASS / CLOSED**;
- q-valuation factorization on that family: **PASS / CLOSED**;
- Bockstein finite q-layer detector: **PASS / LOCAL**;
- Hard Attack 18 unconditional symmetry no-go: **HISTORICAL / SUPERSEDED**;
- universal factorization/no-go: **OPEN**;
- independent orientation bridge: **OPEN**;
- Bockstein orientation carrier: **CONDITIONAL / OPEN**.

No further same-family Bockstein scan is authorized.

## AUTHORITATIVE UPDATE — HARD ATTACK 22 — 2026-09-20

The mod-27 target is now formalized basis-free:
\[
\lambda_{27}(G)=\frac13\log\chi_G\pmod9\in H^1(G,\mathbf Z/9),
\]
and \(O_{27}(G)\) is the distinguished-orientation singleton/subfunctor selecting this class. This removes the previous ambiguity in the target notation.

The abstract carrier category has a genuine symmetry \(S\) preventing a natural selector of \(\lambda_{27}\), but \(S\) is not an admissible group/gauge morphism; indeed canonical orientation naturality itself blocks such a realization. Thus the abstract no-go is valid only in \(\mathcal C_{27}^{abs}\), not in the project's admissible category.

The decisive admissible counterexample pair
\[
\mathcal B_{27}(G)\cong\mathcal B_{27}(G'),\qquad
O_{27}(G)\not\cong O_{27}(G')
\]
has not been found. The standard Demushkin family cannot supply one because its full carrier types already separate the valuation classes.

**Binding status:** target formalization PASS/CLOSED; abstract-carrier no-go PASS/CLOSED; admissible counterexample OPEN/NOT FOUND; universal factorization OPEN; independent bridge OPEN; Bockstein orientation carrier CONDITIONAL/OPEN.

No further same-family Bockstein computation is authorized. The next branch must add genuinely new q-blind rigidifying structure or prove a universal factorization theorem. A cohomological Mackey/transfer enrichment across open subgroups is recorded as a candidate, not yet accepted.

## AUTHORITATIVE UPDATE — HARD ATTACK 23 — 2026-09-20

A proposed successor based on restriction/corestriction/conjugation over open subgroups was attacked. The entire Mackey/transfer-enriched trivial-coefficient Bockstein system retains a global coefficient symmetry
\[
T_c:a\mapsto ca,\qquad c\equiv1\pmod3,
\]
which commutes with reduction, \(\iota\), both Bocksteins, cup product, restriction, corestriction, and conjugation. It moves the desired logarithmic orientation lift \(\lambda_{27}\).

Therefore Mackey/transfer enrichment alone does not remove the missing lift ambiguity.

This is not a group-level universal no-go because \(T_c\) is a coefficient-system automorphism, not an admissible group automorphism. It is nevertheless a decisive stop for this successor: more bookkeeping of the same trivial-coefficient Bockstein data cannot supply the missing characteristic-zero rigidification.

**Status:** Mackey/transfer enrichment as abstract coefficient-functor carrier **FAIL / CLOSED**; global group-level no-go **OPEN**; independent orientation bridge **OPEN**. The next meaningful branch must add genuinely group-sensitive filtered extension information.


## 2026-09-20 — HARD ATTACK: KUMMER FACTORIZATION VS RECOGNITION

The proposed second-stage claim through the lower 3-central quotient was split into two distinct statements.

For
[
A_k=mathbf Z/3^k,quad U_k=1+3A_k,quad H_k=A_ktimes U_k,
]
a candidate character (ho:G	o U_k) and crossed homomorphism (f:G	o A_k(ho)) combine into
[
Phi(g)=(f(g),ho(g))in H_k.
]
The finite semidirect target satisfies (P_{k+1}(H_k)=1), so every such pair factors through
[
Q_k=G/P_{k+1}(G).
]

This proves a genuine factorization lemma: **candidate finite Kummer data is visible at (P_{k+1}).**

However, this does not yet prove that (Q_k) recognizes the canonical orientation. The missing theorem is a q-blind predicate
[
mathsf K_k(Q_k,ho)
]
with a unique solution (ho=chimod3^k), natural under admissible morphisms and independent of q/presentation/known orientation data.

The naive condition “there exists a crossed homomorphism” is vacuous because (f=0) works for every candidate (ho). Requiring (f
eq0) still does not supply a canonical selector. A stronger duality condition risks simply repackaging the already-known orientation module/classification.

Candidate characters (Q_k	o U_k) are plentiful, so uniqueness must come from an additional finite obstruction. No such higher-level obstruction has yet been constructed from (Q_k) alone.

Decision:
- finite semidirect/Kummer factorization through (G/P_{k+1}): **PASS / LOCAL**;
- finite q-blind Kummer recognition (G/P_{k+1}Rightarrowchimod3^k): **OPEN**;
- no numerical scan authorized until the recognition predicate is explicitly defined.

Record: `research/KUMMER_RECOGNITION_LOWER_3_CENTRAL_HARD_ATTACK_2026-09-20.md`


## AUTHORITATIVE UPDATE — HARD ATTACK 24 — 2026-09-20 — KUMMER FACTORIZATION/RECOGNITION BOUNDARY

The lower-3-central Kummer branch was tightened at definition level.

For \(A_k=\mathbf Z/3^k\), \(U_k=1+3A_k\), \(H_k=A_k\rtimes U_k\), an induction gives
\[
P_n(H_k)\subseteq3^{n-1}A_k\rtimes(1+3^nA_k),
\]
hence \(P_{k+1}(H_k)=1\). Therefore every candidate finite orientation/crossed-homomorphism pair \((\rho,f)\) factors through
\[
Q_k=G/P_{k+1}(G).
\]

The strongest justified conclusion is consequently:
**candidate finite Kummer data is visible at \(G/P_{k+1}\)**.

The complete finite bookkeeping carrier is
\[
\mathcal K_k(Q)=\coprod_{\rho\in\operatorname{Hom}(Q,U_k)}Z^1(Q,A_k(\rho)).
\]
But this carrier contains all candidate coefficient actions; it does not itself provide a canonical selector. The naive condition \(\exists f\) is vacuous, while \(\exists f\ne0\) has no established uniqueness and any stronger duality condition risks repackaging known orientation data.

Current binding status:
- exact semidirect-target nilpotence: **PASS / LOCAL**;
- Kummer factorization through \(G/P_{k+1}\): **PASS / LOCAL**;
- complete finite Kummer carrier: **PASS / LOCAL**;
- naive crossed-homomorphism selector: **FAIL / CLOSED**;
- q-blind unique orientation recognition from \(Q_k\): **OPEN**;
- admissible same-carrier/different-orientation no-go: **OPEN**.

This confirms the earlier distinction between information sufficiency for candidate data and actual canonical orientation recognition. No numerical scan is authorized until a concrete selector predicate or admissible counterexample is available.

Record: `research/KUMMER_RECOGNITION_LOWER_3_CENTRAL_HARD_ATTACK_24_2026-09-20.md`.


## AUTHORITATIVE UPDATE — HARD ATTACK 25 — 2026-09-20 — NONZERO KUMMER COCYCLE ROUTE CLOSED

The nonzero-cocycle repair was closed structurally. For every candidate \(\rho:G\to U_k\) on the rank-four one-relator family, the four generator values of a crossed homomorphism satisfy only one additive relator obstruction \(A_k^4\to A_k\). Hence
\[
|Z^1(G,A_k(\rho))|\ge |A_k|^3,
\]
so nonzero crossed homomorphisms exist for every candidate \(\rho\).

Therefore nonzero Kummer-cocycle existence cannot select the canonical orientation.

Binding status:
- \(\exists f\): **FAIL / CLOSED**;
- \(\exists f\ne0\): **FAIL / CLOSED**;
- Boolean nonvanishing of \(H^1(G,A_k(\rho))\): **FAIL / CLOSED** as a selector;
- richer twisted cohomological interaction with additional group structure: **OPEN**;
- genuinely group-sensitive finite selector: **OPEN**.

This strengthens the factorization/recognition boundary: \(G/P_{k+1}\) carries candidate Kummer data, but the selector cannot come from Kummer existence alone. The next meaningful branch must combine the candidate coefficient action with additional intrinsic filtered extension structure, or produce an admissible same-carrier/different-orientation no-go.

Record: `research/KUMMER_RECOGNITION_NONZERO_COCYCLE_HARD_ATTACK_25_2026-09-20.md`.


## METHODOLOGICAL CORRECTION — 2026-09-20 — DISCOVERY MUST RUN IN PARALLEL WITH ATTACK

The recent Kummer work revealed a process-level imbalance: hard attacks reliably eliminate invalid constructions but do not by themselves generate the conceptual mechanism needed to cross an OPEN recognition gap.

The research workflow is therefore explicitly dual-track:
- **Attack:** verify definitions, functoriality, gauge/orientation bridge, q-blindness, separation, non-tautology, and logical validity.
- **Discovery:** generate candidate mechanisms from the structural fingerprints of the target and from literature-derived reusable methods.

For every OPEN bottleneck, the next step should include both:
\[
\text{obstruction question} \quad + \quad \text{idea-generation question}.
\]
In the current Kummer branch, the discovery question is: **what intrinsic finite structure naturally couples a candidate coefficient action \(\rho\) to the relation/extension data strongly enough to select \(\chi\)?**

Candidate mechanism families to investigate include twisted extension classes, transgression/fundamental-class pairings, Bockstein–Kummer compatibility, duality-type pairings, and finite nilpotent/central extensions. These are hypotheses only and must pass the existing hard gates.

This is a methodological correction, not a change to any mathematical result.


## 2026-09-20 — HARD ATTACK 27: FINITE EXTENSION CARRIER DEFINITION AND SUFFICIENCY BOUNDARY

A precise finite candidate was defined after Hard Attack 26. For N=P_{k+1}(G), Q_k=G/N, set M_k=N/(N^{3^k}[N,N]) and E_k=G/(N^{3^k}[N,N]). Since N is characteristic and open in the finitely generated pro-3 group G, this gives a finite intrinsic extension 1->M_k->E_k->Q_k->1. The candidate carrier is J_k^ext=(Q_k,M_k,E_k). It is q-blind at construction level and contains the finite kernel data controlling H^1(N,A_k(rho)).

Critical attack: J_k^ext does not automatically determine H^2(G,A_k(rho)). The total-degree-two Hochschild-Serre terms also contain H^0(Q_k,H^2(N,A_k(rho))), which is not determined by M_k. Thus the naive relation-module extension is a legitimate finite extension datum but not yet a top-cohomology carrier. This is a sufficiency failure of the proof route, not a counterexample to the carrier itself.

Decision:
- finite extension carrier definition: PASS / LOCAL;
- automatic H^2 reconstruction from (Q_k,M_k,E_k): FAIL / CLOSED as an inference;
- universal orientation carrier: OPEN;
- direct addition of H^2(N,A_k(rho)): CONDITIONAL / circularity risk;
- genuine finite 2-cell obstruction inside the extension data: OPEN / next target.

Record: research/KUMMER_FINITE_EXTENSION_CARRIER_HARD_ATTACK_27_2026-09-20.md


## 2026-09-20 — HARD ATTACK 28: CANONICAL FINITE 2-CELL EXTENSION CLASS

The finite extension carrier from Hard Attack 27 has a canonical extension class e_k(G) in H^2(Q_k,M_k), Q_k=G/P_{k+1}, M_k=P_{k+1}/(P_{k+1}^{3^k}[P_{k+1},P_{k+1}]). For every candidate rho and A_k(rho), Q-equivariant maps M_k->A_k push e_k to a canonical transgression/connecting map Hom_Q(M_k,A_k(rho))->H^2(Q_k,A_k(rho)). This is a genuine finite q-blind 2-cell construction.

Hard attack: e_k alone does not canonically reproduce the standard four-generator twisted obstruction row. Recovering that row requires a distinguished evaluation functional/basis or equivalent 2-cell rigidification, which is presentation-dependent unless independently reconstructed. Directly adding a Demushkin fundamental/duality class risks importing the desired orientation.

Decision: extension class e_k PASS / LOCAL; transgression map PASS / LOCAL; automatic recovery of the one-relator obstruction row FAIL / CLOSED as an inference; zero-map annihilation selector FAIL / CLOSED; nonzero transgression selector OPEN; intrinsic recovery of the distinguished 2-cell evaluation OPEN / decisive.

Record: research/KUMMER_2CELL_OBSTRUCTION_HARD_ATTACK_28_2026-09-20.md


## 2026-09-20 — HARD ATTACK 29: PD2 TOP-CLASS RIGIDIFIER

The obvious missing 2-cell rigidifier was tested: add the top cohomology module of N=P_{k+1}(G). For the Demushkin/PD^2 setting, this top class carries the quotient action through the orientation character. Thus adding H^2(N,F_3), or its Z/3^k lift, does provide the desired character action, but only because it imports the duality/orientation-bearing object itself.

Decision: top-class module as group object PASS / LOCAL; its use as a direct orientation carrier FAIL / CLOSED for the present non-tautological filtered objective; independently derived finite chain-level T_k OPEN / decisive; universal no-go OPEN. No further enrichment by already-oriented top cohomology is authorized.

Record: research/KUMMER_PD2_TOP_CLASS_RIGIDIFIER_HARD_ATTACK_29_2026-09-20.md


## 2026-09-20 — DISCOVERY PASS 30: FINITE DERIVED 2-CELL / FITTING CANDIDATE

Current bottleneck after Hard Attack 29: derive, rather than append, the missing 2-cell rigidifier from (Q_k,M_k,E_k). Candidate T_k is a basis-free finite derived/transgression complex or its Fitting/annihilator/determinant-line defect, depending functorially on the candidate rho. It is intended to retain secondary extension information without choosing a generator or importing the dualizing module.

Hard attack already closes the raw scalar Reidemeister/determinant version: chain bases and coefficient-module scalings change a scalar by units, so no canonical scalar selector is defined. The basis-free Fitting/annihilator/derived-line version remains OPEN / decisive. No identification with H^2(G,A_k(rho)) is assumed; such a bridge must be independently proved. No numerical scan is authorized until the object and bridge are explicit.

Record: research/KUMMER_FINITE_DERIVED_2CELL_DISCOVERY_PASS_30_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 31: TRANSgression DEFECT TOO SHALLOW

The first concrete Fitting candidate was attacked. For C_rho: Hom_Q(M,A_k(rho)) -> H^2(Q,A_k(rho)), the LHS edge sequence gives coker(delta) = im(inflation H^2(Q,A)->H^2(G,A)). For the canonical PD^2 coefficient, the fundamental/top class restricts nontrivially to the open subgroup N, while any inflated quotient class restricts trivially; hence the inflation image is zero. Therefore coker(delta) and any Fitting/annihilator invariant depending only on it cannot select the canonical orientation. This closes the naive coker route. It does not close every invariant of the full two-term complex: ker(delta) and genuinely higher derived combinations remain open. The structural boundary is sharper: quotient transgression sees the q=0 spectral-sequence row, while the desired orientation lies in the q=2 top row.

Record: research/KUMMER_HARD_ATTACK_31_TRANSgression_DEFECT_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 32: LHS MIDDLE-ROW SURVIVOR IS THE ONLY NON-TAUTOLOGICAL SPECTRAL CANDIDATE

Hard Attack 31 is confirmed, but its boundary is sharpened. The closed cokernel/Fitting defect is exactly the quotient-inflation contribution in the LHS filtration, hence the q=0 row. The remaining spectral candidates split into the middle term E_infty^{1,1} and the top term E_infty^{0,2}/d_3^{0,2}.

The top-row route is not a legitimate new carrier if H^2(N,A) and its Q-action are imported, because for an open PD^2 subgroup N that action is already orientation-bearing. Thus raw d_3^{0,2} is FAIL / CLOSED as a non-tautological input route.

The only remaining potentially non-tautological spectral candidate is
T_k^mid(G,rho)=E_infty^{1,1}\subset H^1(Q_k,H^1(N,A_k(rho))).
Since H^1(N,A) is determined by M_k, this is the first candidate that may retain secondary extension information without adjoining H^2(N,A). However, finiteness of its source does NOT prove that d_2^{1,1} is determined by the truncated finite extension (Q_k,M_k,E_k). That finite-input reconstruction is itself a load-bearing theorem and must be proved before any scan.

For the canonical coefficient action, Hard Attack 31 gives E_infty^{2,0}=0, while PD^2 top cohomology has size 3^k and the top class survives. Hence E_infty^{1,1}(G,chi)=0. This is only a necessary condition; the converse is OPEN.

Status:
- Hard Attack 31 coker/Fitting route: FAIL / CLOSED;
- direct top-class/top-row enrichment: FAIL / CLOSED for non-tautological filtered input;
- raw d_3 route: FAIL / CLOSED as an imported top-row carrier;
- finite reconstruction of d_2^{1,1}: OPEN / load-bearing;
- T_k^mid=E_infty^{1,1}: OPEN / decisive;
- selector T_k^mid=0 iff rho=chi: OPEN;
- universal no-go: OPEN.

Record: research/KUMMER_HARD_ATTACK_32_EINFTY11_D3_2026-09-20.md. No numerical scan authorized until the finite-input and selector gates are passed.


## CRITICAL CORRECTION — 2026-09-20 — HARD ATTACK 31 REOPENED AFTER TOP-CLASS RESTRICTION AUDIT

A decisive error was found in Hard Attack 31. The claim that the canonical PD^2 top class for A_k(chi) restricts nontrivially to N=P_{k+1}(G) is not valid. Already at k=1, A_1(chi)=F_3 because chi mod 3 is trivial, and for a proper open subgroup of p-power index the mod-p degree-two fundamental class can restrict to zero. Standard surface/Demuškin duality sources explicitly record vanishing of Res:H^2(G,F_p)->H^2(L,F_p) for proper open subgroups of index divisible by p.

Therefore the inference “top class restricts nontrivially, hence inflation image is zero” is invalid. The exact identity
coker(delta)=im(inflation H^2(Q,A)->H^2(G,A)) remains correct, but its use as an orientation no-go is reopened.

Consequences:
- Hard Attack 31 coker/Fitting selector closure: HISTORICAL / SUPERSEDED;
- coker-based orientation selector: OPEN;
- Fitting/annihilator of coker: OPEN;
- claim that the canonical class lies in E_infty^{0,2}: UNJUSTIFIED;
- claim E_infty^{1,1}(G,chi)=0 from that placement: UNJUSTIFIED;
- raw d3/top-row enrichment remains closed if H^2(N,A) is imported as orientation-bearing input.

The next binding attack is now the actual LHS filtration placement of H^2(G,A_k(chi)): compute inflation image, E_infty^{1,1}, and top-row restriction/edge behavior before classifying any derived selector. No numerical scan is authorized until this filtration audit is complete.

Detailed correction: research/CRITICAL_CORRECTION_HARD_ATTACK_31_RESTRICTION_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 33: COKER ROUTE REOPENS AND SURVIVES VIA NORM-ZERO DUALITY

The restriction audit overturned Hard Attack 31's closure. The exact coker identity remains
coker(delta_rho)=im(inflation)=ker(res:H^2(G,A)->H^2(N,A)).
Using PD^2 duality, the dual of restriction is corestriction on H^0 of the dual coefficient module B=Hom(A,I). Because N=P_{k+1} acts trivially on B, corestriction is the finite norm from Q_k. The abelianization of Q_k contains the three independent classes x_2,x_3,x_4 modulo 3^k, so |Q_k| is divisible by 3^{3k}. The candidate character delta=chi*rho^{-1} has image of order at most 3^{k-1}; decomposing Q into kernel and cyclic image gives a norm coefficient divisible by a sufficiently high power of 3, hence zero on B=Z/3^k. Therefore restriction is zero for every candidate rho, not just the canonical one.

Consequently inflation is surjective for every candidate rho and
coker(delta_rho) ≅ H^2(G,A_k(rho)).
PD^2 duality then gives the exact finite selector
rho=chi mod 3^k iff |coker(delta_rho)|=3^k.

This is a qualitatively new positive result: the finite carrier is constructed solely from (Q_k,M_k,E_k,rho); H^2(G,A) is not input, and the orientation formula is not used in the construction. The bridge is an independent PD^2 duality plus norm-zero theorem.

Status: finite transgression coker carrier OPEN / STRONG; inflation-surjectivity OPEN / decisive; coker-size selector OPEN / decisive pending three independent checks: |Q_k| divisibility, exact cyclic norm valuation, and twisted PD^2 duality/restriction-corestriction compatibility. Hard Attack 31 coker closure is HISTORICAL / SUPERSEDED. No numerical scan needed.
Record: research/KUMMER_HARD_ATTACK_33_COKER_REOPENS_AND_SURVIVES_2026-09-20.md.


## 2026-09-20 — VERIFICATION OF HARD ATTACK 33: FINITE COKER SELECTOR SURVIVES

The three load-bearing checks were independently verified.

(1) |Q_k| is divisible by 3^{3k}: in the abelianization, P_{k+1} maps to 3^k G_ab, while x_2,x_3,x_4 have independent infinite Z_3 directions. Hence Q_k has an abelian quotient containing (Z/3^k)^3.

(2) Norm-zero: for delta=chi*rho^{-1}:Q_k->U_k with image C of order 3^m, write Q_k=K⋊(coset count) at the level of the norm sum. The cyclic geometric sum over C is divisible by 3^m; multiplying by |K| gives total 3-adic valuation at least v_3(|Q_k|)≥3k, hence the norm is zero on every module of exponent 3^k. The trivial-image case is multiplication by |Q_k| and is also zero.

(3) PD^2 duality identifies the dual of restriction H^2(G,A)->H^2(N,A) with corestriction H^0(N,Hom(A,I))->H^0(G,Hom(A,I)); since the latter norm is zero, restriction is zero for every candidate rho.

Therefore inflation H^2(Q_k,A)->H^2(G,A) is surjective and
coker(delta_rho) ≅ H^2(G,A_k(rho))
for every candidate rho.

Using the standard PD^2 orientation criterion |H^2(G,I_k(rho))|=3^k iff rho=chi mod 3^k, equivalently in the dual finite coefficient convention, the finite coker cardinality gives a unique selector of chi mod 3^k. The carrier itself contains only (Q_k,M_k,E_k,rho), not H^2(G,A), H^2(N,A), the dualizing module, q, or a presentation.

Classification:
- finite coker carrier: **PASS / LOCAL**;
- inflation-surjectivity/norm-zero theorem: **PASS / LOCAL**;
- unique Kummer recognition at every finite level k for PD^2/Demuškin G: **PASS / LOCAL**;
- passage to the compatible inverse system chi_filt: **PASS / LOCAL** subject to the declared PD^2 existence/naturality framework;
- universal category-independent minimality/no-go: **OPEN** (not needed for existence of this construction).

Important correction: Hard Attack 31's coker closure is **HISTORICAL / SUPERSEDED**. The actual obstruction was the false nonzero-restriction claim; once corrected, the same coker becomes the successful carrier.

Record: research/KUMMER_HARD_ATTACK_33_COKER_REOPENS_AND_SURVIVES_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 34: COKER DUALITY/NORM AUDIT SURVIVES

An independent audit found one notation-level correction in Hard Attack 33: the dualizing module used for finite p-primary PD^2 duality is the discrete torsion dualizing module I_G (abstractly Q_3/Z_3 with orientation action), so B=Hom(A_k(rho),I_G) is finite of exponent 3^k. With this correction, the argument is sound: B has action chi*rho^{-1}; for N=P_{k+1}, both rho and chi mod 3^k are N-trivial; PD^2 restriction/corestriction duality identifies res:H^2(G,A)->H^2(N,A) with the dual of cor:H^0(N,B)->H^0(G,B); the latter is the finite Q_k-norm. Since v_3(|Q_k|)>=3k from the (Z/3^k)^3 abelianization quotient and |im(chi*rho^{-1})|<=3^{k-1}, the cyclic geometric norm has total 3-adic valuation >=3k and is zero on B. Thus res=0, inflation is surjective, and coker(delta_rho) ≅ H^2(G,A_k(rho)). Combined with the PD^2 criterion |H^2(G,A_k(rho))|=3^k iff rho=chi mod 3^k, this yields finite Kummer recognition at each k.

Decision:
- Hard Attack 33 core theorem: **PASS / LOCAL**, corrected and independently audited.
- finite Kummer recognition at each level k for PD^2/Demuškin G: **PASS / LOCAL**.
- inverse-limit compatibility/naturality: **OPEN**.
- minimality of P_{k+1}: **OPEN**.
- universal category-independent minimality/no-go: **OPEN**.

Detailed audit: research/KUMMER_HARD_ATTACK_34_COKER_DUALITY_AUDIT_2026-09-20.md


## 2026-09-20 — DEFERRED IDEA BACKLOG RECORDED; MAIN LINE PRESERVED

The creative proposal set from the latest review has been recorded in `research/NEXT_RESEARCH_IDEA_BACKLOG_2026-09-20.md`. These are explicitly deferred, not closed:
- finite Fox-residue versus intrinsic extension-class comparison;
- selector-theorem formulation;
- maximality-selector interpretation;
- mixed m-adic/bi-filtered direction;
- information-transfer efficiency synthesis;
- eventual minimality/admissible-category program.

The immediate task remains the finite coker branch: independently strengthen the construction and attack the inverse-system compatibility/naturality (k\to k+1). No deferred branch should displace this without new evidence.


## 2026-09-20 — HARD ATTACK 35: CARRIER TOWER VS SELECTOR TOWER

A hard compatibility audit was completed. The level-k coker selectors do not automatically define a strict inverse system of carriers because M_k changes with the kernel P_{k+1}; there is no canonical reduction M_{k+1}->M_k, only a natural map into a generally proper submodule. Therefore direct reduction of transgression cokernels is FAIL / CLOSED as an inference.

Separately, the selected outputs are compatible: the PD² finite-level maximality criterion forces a level-(k+1) selector to reduce to the unique level-k selector. Thus the inverse-limit character exists as a compatible family of unique finite selectors, PASS / LOCAL under the declared PD² framework.

The next structural question is no longer "can we force M_{k+1}->M_k?" but whether a universal property of the finite selector can make compatibility intrinsic without requiring a strict inverse system of the raw coker carriers.

Detailed audit: research/KUMMER_HARD_ATTACK_35_INVERSE_SYSTEM_COMPATIBILITY_AUDIT_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 36: SELECTOR-ONLY COHERENCE ENDGAME

A further attack shows that the practical reconstruction problem does not require a strict inverse system of the raw finite coker carriers. Define
S_k(G) = {rho in Hom(G,U_k): |coker(delta_{k,rho})|=3^k}.
The finite recognition theorem gives S_k(G)={chi mod 3^k}. Reduction of candidate characters therefore restricts to compatible maps S_{k+1}->S_k. The inverse-limit selector set
S(G)={(rho_k): rho_k in S_k, rho_{k+1} mod 3^k=rho_k}
is a singleton, canonically identified with chi_filt.

This is PASS / LOCAL under the declared PD² verification framework. It is not a carrier-only naturality theorem: raw carrier maps remain OPEN, as does strict carrier-tower functoriality.

The practical main branch therefore has a clean endpoint: finite recognition + selector coherence + inverse-limit reconstruction. Further work is justified only to remove external PD² dependence from coherence, prove minimality in a specified carrier category, establish strict carrier naturality, or broaden the admissible class.

Detailed record: research/KUMMER_HARD_ATTACK_36_SELECTOR_COHERENCE_ENDGAME_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 37: PD²-INDEPENDENT SELECTOR UNIQUENESS

The strongest remaining finite-level question was attacked: whether the uniqueness of the coker selector |coker(delta_{k,rho})|=3^k can be proved from (Q_k,M_k,E_k,rho) without invoking the external PD² orientation criterion. The coker itself is intrinsic at fixed k, but a PD²-independent proof requires a finite-input reconstruction theorem identifying the transgression image with an intrinsically evaluable twisted 2-cell obstruction. Reusing the standard one-relator/Fox row would be presentation-dependent unless that identification is first derived from the finite extension itself.

Result: no valid finite-input reconstruction proof and no admissible no-go were obtained. Therefore PD²-independent selector uniqueness remains OPEN. The PD²-based finite selector remains PASS / LOCAL; selector coherence remains PASS / LOCAL under the PD² framework; carrier-only coherence remains OPEN. Direct reuse of the known relator row as an intrinsic proof shortcut is FAIL / CLOSED.

The exact remaining load-bearing theorem is:
\[
\boxed{\text{finite extension data}\Longrightarrow\text{intrinsic evaluation of its 2-cell transgression}.}
\]

Record: `research/KUMMER_HARD_ATTACK_37_PD2_INDEPENDENT_SELECTOR_2026-09-20.md`.


## 2026-09-20 — HARD ATTACK 38: EXTENSION-CLASS TRANSGRESSION MADE BASIS-FREE

Hard Attack 38 resolves the precise definitional gap left by Hard Attack 37. For the intrinsic finite extension 1 -> M_k -> E_k -> Q_k -> 1, with e_k=[E_k] in H^2(Q_k,M_k), and candidate coefficient module A_k(rho), the LHS transgression delta_{k,rho}: Hom_{Q_k}(M_k,A_k(rho)) -> H^2(Q_k,A_k(rho)) is canonically the push-forward of the extension class: delta_{k,rho}(phi)=phi_*(e_k), up to the conventional global sign of the spectral-sequence differential.

Thus the finite coker is intrinsically C_k(rho)=H^2(Q_k,A_k(rho))/{phi_*(e_k)}, and can be viewed as the natural transgression profile of e_k over coefficient modules. No presentation, relator, Fox coordinates, q, chi, H^2(G,A), or dualizing module is needed to define this map. Gauge independence follows because only the cohomology class e_k and functorial push-forward are used.

This closes the narrower logical gap “finite extension data -> intrinsic evaluation of its 2-cell transgression” at the level of definition and cohomological interpretation.

It does NOT close PD²-independent selector uniqueness. The remaining theorem is whether the coefficient-module dependence of this intrinsic push-forward profile forces a unique maximal-coker candidate without invoking the external PD² orientation criterion. The known Fox row is now legitimately a coordinate-comparison target, not a definition shortcut.

New structural warning: (Q_k,M_k,E_k) contains the complete finite extension class, so no minimality claim is justified merely from this success.

Classification:
- basis-free finite transgression from e_k: PASS / CLOSED;
- intrinsic/gauge-independent coker construction: PASS / CLOSED;
- Fox row as coordinate realization: OPEN;
- PD²-independent selector uniqueness: OPEN / decisive;
- PD²-based finite selector: PASS / LOCAL;
- carrier minimality and strict tower naturality: OPEN.

Detailed record: research/KUMMER_HARD_ATTACK_38_EXTENSION_CLASS_TRANSGRESSION_2026-09-20.md.

Next authorized attack: compare the known twisted Fox row with the intrinsic push-forward phi_*(e_k), then attack the finite coefficient-module dependence structurally. No broad numerical scan is authorized yet.


## 2026-09-20 — HARD ATTACK 39: YONEDA COMPLETENESS VS RESTRICTED KUMMER PROFILE

Hard Attack 39 separates two statements that had been conflated by the notation e_k <-> T_{e_k}.

For the full category of Q_k-modules A, the profile T_e(A): Hom_Q(M_k,A) -> H^2(Q_k,A), phi |-> phi_*(e), recovers e itself by evaluating at A=M_k and phi=id_{M_k}. Thus full coefficient-category profile completeness is PASS / CLOSED, but this is a Yoneda-level tautology, not a selector theorem.

For the actual Kummer family A_k(rho)=Z/3^k with rank-one twisted Q_k-action, define K_k = intersection_{rho,phi} ker(phi_*), where phi ranges over Hom_Q(M_k,A_k(rho)). The restricted profile is faithful exactly when K_k=0. No such faithfulness theorem is currently proved, and it does not follow from the Yoneda identity because M_k is not part of the restricted coefficient family in general.

Therefore the precise remaining gate is sharper:
- e_k -> full coefficient profile: PASS / CLOSED (information-complete but tautological);
- e_k -> restricted Kummer profile: OPEN;
- restricted profile -> unique orientation without PD²: OPEN / DECISIVE;
- Fox row as coordinate realization of phi_*(e_k): OPEN;
- PD²-based finite selector: PASS / LOCAL;
- carrier minimality and strict tower naturality: OPEN.

The selector need not reconstruct all of e_k. It only needs the restricted observation function rho |-> |coker T_{e_k}(A_k(rho))| to have a unique maximizer. This is now the exact finite, q-blind theorem target. No broad numerical scan is authorized until a structural theorem about the restricted profile is established.

Record: research/KUMMER_HARD_ATTACK_39_YONEDA_COEFFICIENT_PROFILE_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 40: RANK-ONE COEFFICIENT / SPECTRAL-BLINDNESS AUDIT

The restricted Kummer coefficient family A_k(rho)=Z/3^k only probes scalar-character specializations of the Q_k-module M_k. For fixed rho, equivariant maps satisfy phi(gm)=rho(g)phi(m), hence factor through M_{k,rho}=M_k/<gm-rho(g)m>. Thus the restricted push-forward profile of e_k is a scalar-character spectroscopy of the extension class.

This is a structural factorization theorem, not yet a no-go: it does not prove that the actual Demushkin e_k has invisible components. Therefore scalar-character factorization is **PASS / CLOSED**; faithfulness on the actual e_k is **OPEN / DECISIVE**; unique scalar-character maximizer without PD² is **OPEN / DECISIVE**; Fox row as coordinate realization is **OPEN**; PD²-based selector is **PASS / LOCAL**; carrier minimality and strict tower naturality remain **OPEN**.

No broad scan is authorized. The next attack must determine whether the Demushkin extension class has a special scalar-character visibility theorem strong enough to force a unique maximizer.

Record: research/KUMMER_HARD_ATTACK_40_RANK_ONE_SPECTRAL_BLINDNESS_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 40 CRITICAL REVIEW / NEXT GATE CORRECTION

A critical audit confirms that Hard Attack 40 is a structural scalar-specialization reformulation, not a new obstruction theorem. The Kummer coefficient A_k(rho)=Z/3^k is rank-one, while M_{k,rho} need not be one-dimensional. K_k=0 is auxiliary rather than decisive.

Important correction: maximality of |C_k(rho)| must not be described as "complete filling" of H^2. Since C_k=H^2/im(delta), maximal coker corresponds to minimal transgression image; in the established equality |C_k|=|H^2| the image of delta vanishes.

The next authorized gate is therefore the scalar-character visibility/vanishing structure of delta_{k,rho} for the specific Demushkin extension, beginning with an intrinsic comparison at k=2 to the already closed cup+Bockstein degree-(2,3) obstruction. Fitting/determinant constructions are deferred unless they demonstrably add a new basis-independent control theorem.

Current classification:
- scalar-character factorization: PASS / CLOSED;
- Hard Attack 40 as novelty: HISTORICAL / SUPERSEDED;
- scalar-character visibility: OPEN / DECISIVE;
- unique coker maximality without PD^2: OPEN / DECISIVE;
- restricted faithfulness K_k=0: OPEN / AUXILIARY;
- PD^2 finite selector: PASS / LOCAL;
- Fox coordinate realization: OPEN;
- Fitting/determinant: OPEN / DEFERRED;
- carrier minimality: OPEN;
- strict tower naturality: OPEN.

Record: research/HARD_ATTACK_40_CRITICAL_REVIEW_AND_NEXT_GATE_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 42: AMBIENT H^2 AUDIT — STRUCTURAL REDUCTION

The ambient numerator in the finite coker selector was attacked without a rho-scan. For A_2(rho)=Z/9 with rho mod 3 trivial, the coefficient sequence
0 -> F_3 -> A_2(rho) -> F_3 -> 0
has twisted Bockstein connecting maps beta_rho^i. The long exact sequence gives the exact formula
log_3 |H^2(Q_2,A_2(rho))| = 2 dim H^2(Q_2,F_3) - rank(beta_rho^1) - rank(beta_rho^2).

The degree-one map beta_rho^1 is exactly the already closed mod-9 intrinsic obstruction Theta_(R,p), up to the synchronized H^2 normalization/sign convention. Thus the same relation-jet that is the scalar shadow of the finite extension class also controls one of the two ambient-cohomology terms.

This separates the remaining rho-dependence into two sources: (A) ordinary finite-group coefficient cohomology through beta_rho^1,beta_rho^2, and (B) extension-class transgression visibility. No cancellation may be assumed.

Decision:
- coefficient-sequence reduction of ambient H^2: PASS / CLOSED;
- beta_rho^1 = intrinsic mod-9 obstruction: PASS / CLOSED;
- constancy/variation of |H^2(Q_2,A_2(rho))|: OPEN / LOAD-BEARING;
- structural control of beta_rho^2: OPEN / LOAD-BEARING;
- unique coker maximizer without PD^2: OPEN / DECISIVE;
- no broad rho-scan authorized.

Record: research/KUMMER_HARD_ATTACK_42_AMBIENT_H2_AUDIT_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 43: SECOND BOCKSTEIN LAYER BOUNDARY

Hard Attack 43 tested whether the second connecting map beta_rho^2 is forced by the already closed degree-one map beta_rho^1 / intrinsic carrier (R,p).

For 0 -> F_3 -> A_2(rho) -> F_3 -> F_3, both maps are instances of the same twisted coefficient-extension Bockstein beta_rho^i(z)=beta(z)+lambda cup z, up to the common convention, with lambda=(rho-1)/3 mod 3. Thus the same character parameter enters both layers.

However, this does NOT give beta_rho^2=F(beta_rho^1). The maps act on different cohomological degrees and require the actual H^*(Q_2,F_3) algebra in degrees 2 and 3. The original pro-3 PD^2 property cannot be transferred to Q_2 to force the missing relation without reintroducing the external PD^2 input.

Decision: common twisted-Bockstein mechanism PASS/CLOSED; determination of beta_rho^2 from beta_rho^1 OPEN/NOT ESTABLISHED; finite-quotient PD^2 shortcut FAIL/CLOSED as an inference; ambient H^2 constancy/variation OPEN/LOAD-BEARING; unique coker maximizer without PD^2 OPEN/DECISIVE.

Next narrow attack: derive H^*(Q_2,F_3) through degree 3 from the class-2/central-extension structure of Q_2, then determine rank behavior of beta_rho^2. No broad rho-scan authorized.

Record: research/KUMMER_HARD_ATTACK_43_SECOND_BOCKSTEIN_LAYER_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 44: Q_2 AS A CENTRAL EXTENSION — FIRST DEEP REDUCTION

Hard Attack 44 pushed beyond the abstract warning and rewrote Q_2 through its lower-3-central central extension. Let V=G/P_2 ≅ F_3^4 and W=P_2/P_3. In the class-2 quotient Q_2, W is central. The degree-two extension data consists of the six commutator directions together with four cube directions, subject to the single frozen relation t_1+c_{12}+c_{34}=0; hence the natural presentation-level model has dim_F3 W=9. This gives |Q_2|=3^{4+9}=3^{13} at the frozen q=3 level.

The LHS spectral sequence has E_2^{i,j}=H^i(V,H^j(W,F_3)), with trivial V-action because W is central. The transgression d_2:H^1(W,F_3)->H^2(V,F_3) is evaluation on the central extension class. Since dim H^1(W)=9 while dim H^2(V)=dim(Λ^2 V^*)+dim(V^*)=6+4=10, the extension class has at most a codimension-one obstruction space. The expected rank-nine statement is equivalent to linear independence of the nine commutator/cube components of the Q_2 extension class; this must still be proved from the actual finite presentation before being promoted to PASS.

This is a substantially sharper target: the degree-(2,3) Demushkin relation jet appears as the unique potential surviving line in H^2(V) after the central extension transgression, but this identification is not yet proved at the Q_2 cohomology level. If rank d_2=9 is established, the LHS page isolates a one-dimensional E_3^{2,0} and gives a concrete place where the intrinsic (R,p) shadow may reappear.

The twisted Bockstein is d_lambda=beta+lambda cup(-), with beta(lambda)=0 for admissible lambda and lambda cup lambda=0 at p=3, so d_lambda^2=0. The remaining problem is now localized: track this differential through the LHS spectral sequence and determine its action on the surviving degree-two and degree-three classes. This is the first genuinely promising route to beta_rho^2 without a rho-scan.

Decision: central-extension reduction PASS; dim W=9 model / d_2 rank-nine identification OPEN pending direct proof; surviving H^2 line = (R,p) shadow OPEN; beta_rho^2 structural control OPEN/LOAD-BEARING. No selector claim and no broad rho-scan authorized.

Record: research/KUMMER_HARD_ATTACK_44_Q2_LOW_DEGREE_COHOMOLOGY_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 45: W=9 AND RANK d_2=9 CLOSED

Hard Attack 45 completed the two hypotheses left open by HA44.

For the free rank-4 pro-3 group, the degree-two lower 3-central quotient has the 10-dimensional basis consisting of 4 cube directions and 6 commutator directions. The defining relator has initial form \(\rho_2=t_1+c_{12}+c_{34}\), which is nonzero. Passing to the one-relator quotient removes exactly the one-dimensional initial-relation line at this degree, so \(W=P_2/P_3\cong L_2(F)/\langle\rho_2\rangle\) and \(\dim W=9\).

For the central extension \(1\to W\to Q_2\to V\to1\), the LHS transgression \(d_2:W^*=H^1(W,\mathbf F_3)\to H^2(V,\mathbf F_3)\) is evaluation on the extension class. Since \(H^2(V,\mathbf F_3)\cong \beta(V^*)\oplus\Lambda^2V^*\) has dimension 10, and \(W^*\) identifies with the hyperplane of degree-two functionals annihilating \(\rho_2\), the transgression is the inclusion of a 9-dimensional hyperplane. Therefore \(\operatorname{rank}d_2=9\) and \(\dim\operatorname{coker}d_2=1\).

The surviving line is canonically represented by the relation-jet \(\rho_2\), i.e. by the already established intrinsic pair \((R,p)\) after the common duality/H² normalization. Thus the HA44 picture of a unique degree-two survivor is now proved rather than hypothesized.

Critical boundary: this is the base untwisted LHS transgression statement. It does not determine \(\beta_\rho^2\), nor the full twisted \(H^2(Q_2,\mathbf Z/9(\rho))\), nor the coker selector. The next gate is to propagate \(d_\lambda=\beta+\lambda\cup(-)\) through the LHS page and determine whether the degree-three ambient contribution is forced by the same surviving line or requires an enriched shadow of \(e_2\).

Decision:
- \(\dim W=9\): **PASS / CLOSED at q=3**;
- \(\operatorname{rank}d_2=9\): **PASS / CLOSED at q=3**;
- unique untwisted H² survivor \(\cong\langle(R,p)\rangle\): **PASS / CLOSED at q=3**;
- \(\beta_\rho^2\) structural control: **OPEN / LOAD-BEARING**;
- ambient \(H^2(\rho)\) control: **OPEN / LOAD-BEARING**;
- unique coker maximizer without PD²: **OPEN / DECISIVE**.

Record: research/KUMMER_HARD_ATTACK_45_W9_AND_D2_RANK9_2026-09-20.md (commit c8e22374a1a08840b011bc1ecc33f7e113fff90a).


## 2026-09-20 — HARD ATTACK 46: TWISTED BOCKSTEIN / LHS COMPATIBILITY

HA46 pushed the new bottleneck directly into the LHS spectral sequence. The coefficient extension 0 -> F3 -> A2(rho) -> F3 -> 0 is Q2-equivariant, so its Bockstein is filtration-compatible and induces a map of LHS spectral sequences.

A critical structural correction follows: HA45's one-dimensional survivor is only the base-filtration piece E_infinity^{2,0}, not the total group H2(Q2,F3). The full degree-two source also has possible E_infinity^{1,1} and E_infinity^{0,2} pieces, while the target degree three has E_infinity^{3,0}, E_infinity^{2,1}, E_infinity^{1,2}, E_infinity^{0,3}.

Moreover W=(F3)^9 has H*(W,F3)=Lambda(W*) tensor Sym(beta W*), so the fiber Bockstein is already nontrivial. Therefore beta_rho^2 is not automatically determined by the base relation line (R,p). This is a genuine obstruction to the naive collapse, not a numerical failure.

What remains controlled is the filtration-(2,0) component: on the base row the differential is d_lambda^V=beta_V+lambda cup(-), so its action on the relation-jet line is a finite calculation depending only on (R,p,lambda), subject to survival in the target LHS page.

The problem is now cleanly split into a base component and the first fiber/extension corrections. Three outcomes remain open: collapse to (R,p); controlled enrichment by a finite additional intrinsic shadow of e2; or an independent higher layer.

Decision:
- coefficient-Bockstein/LHS functoriality: PASS / CLOSED;
- nontrivial fiber-Bockstein obstruction: PASS / CLOSED;
- (2,0) graded component controlled by (R,p,lambda): PASS / STRUCTURAL;
- full beta_rho^2 from (R,p): OPEN / LOAD-BEARING;
- total H2(Q2,F3) one-dimensional: explicitly NOT CLAIMED;
- next gate: minimal LHS calculation in total degrees 2 and 3, starting with (2,0)->(3,0) and first fiber-row correction.

Record: research/KUMMER_HARD_ATTACK_46_TWISTED_BOCKSTEIN_LHS_COMPATIBILITY_2026-09-20.md (commit 519230a3c1ebf1a6c4db76904692d0a529351cf5).


## 2026-09-20 — HARD ATTACK 47: BASE-ROW TWISTED BOCKSTEIN IS NONZERO

HA47 carried the HA46 base-row calculation through explicitly. With the standard normalization
H^*(V,F_3)=Lambda(e_1,e_2,e_3,e_4) tensor F_3[b_1,b_2,b_3,b_4], beta(e_i)=b_i, and relation-jet representative
z_R=b_1+e_1e_2+e_3e_4,
the filtration-(2,0) twisted Bockstein is

d_lambda^V(z_R)=beta(z_R)+lambda cup z_R.

For the already established q=3 mod-9 candidate lambda=e_2 this gives

d_{e_2}^V(z_R)=2b_1e_2-e_1b_2+b_3e_4-e_3b_4+e_2e_3e_4,
which is nonzero in H^3(V,F_3), since the displayed monomials occupy distinct basis directions.

This is a genuine structural result, not a rho-scan: the raw (2,0)->(3,0) contribution does not vanish. Therefore any eventual cancellation relevant to beta_rho^2 must come from target-side LHS differentials and/or fiber/extension corrections.

Critical boundary: this nonzero E_2 base-row value is NOT yet a nonzero E_infinity^{3,0} class. For the central extension, the decisive target quotient is
E_infinity^{3,0}=E_3^{3,0}/im(d_3:E_3^{0,2}->E_3^{3,0}),
after the already established d_2 stage. Hence the next attack is to compute d_3^{0,2} and determine whether it kills the displayed class.

A precision correction is also recorded: HA45's phrase “unique one-dimensional LHS H^2 survivor” is henceforth interpreted strictly as the unique E_infinity^{2,0} base-filtration survivor, not total H^2(Q_2,F_3).

Decision:
- explicit base-row formula: PASS / CLOSED;
- nonzero raw base-row value at lambda=e_2: PASS / CLOSED;
- nonzero E_infinity^{3,0}: OPEN / LOAD-BEARING;
- beta_rho^2 from (R,p): OPEN / LOAD-BEARING;
- unique coker maximizer without PD^2: OPEN / DECISIVE.

Record: research/KUMMER_HARD_ATTACK_47_BASE_ROW_BOCKSTEIN_NONZERO_2026-09-20.md (commit 69a0d208162531731ff3649d4e39a3e6fa56ea0f).


## 2026-09-20 — HARD ATTACK 48: BASE H^3 TARGET IS KILLED ALREADY AT d_2

HA48 corrected a load-bearing error in HA47. The claim that the only incoming differential to (3,0) after the d_2 stage was d_3:E_3^{0,2}->E_3^{3,0} was false: there is already d_2:E_2^{1,1}->E_2^{3,0}.

Let K=im(d_2:W^*->H^2(V,F_3)). By HA45, K is the 9-dimensional hyperplane annihilating the relation-jet z_R=b_1+e_1e_2+e_3e_4. Since the LHS d_2 is a derivation,

d_2:E_2^{1,1}=V^*\\otimes W^* -> E_2^{3,0}=H^3(V,F_3)

has image V^*\\cup K. A direct basis argument shows

V^*\\cup K = H^3(V,F_3),

using b_2,b_3,b_4, e_{13},e_{14},e_{23},e_{24}, b_1-e_{12}, and b_1-e_{34} as generators of K. An independent finite-dimensional F_3 rank check gives rank 20, equal to dim H^3(V,F_3)=20.

Therefore

E_3^{3,0}=0,

and hence E_infinity^{3,0}=0. The nonzero raw base-row class computed in HA47 is consequently killed at the d_2 target stage; no d_3^{0,2} calculation is needed for this target.

This is a genuine negative refinement: the base-filtration output of beta_rho^2 has no surviving (3,0) component. The second Bockstein problem must move to the surviving filtration pieces (2,1), (1,2), (0,3) and their source-side counterparts.

Decision:
- HA47 target-differential correction: **PASS / CLOSED**;
- V^*\\cup K=H^3(V,F_3): **PASS / CLOSED**;
- E_infinity^{3,0}=0: **PASS / CLOSED**;
- HA47 “first possible incoming differential is d_3^{0,2}”: **FAIL / CLOSED / SUPERSEDED**;
- beta_rho^2 from (R,p): **OPEN / LOAD-BEARING**;
- unique coker maximizer without PD²: **OPEN / DECISIVE**.

Record: research/KUMMER_HARD_ATTACK_48_BASE_TARGET_KILLED_AT_D2_2026-09-20.md (commit 2a8e5ec4ec9b8fbed7b501387f5a0becdd5d6222).


## 2026-09-20 — HARD ATTACK 49: BASE H^4 TARGET ALSO KILLED AT d_2

Hard Attack 48 closed E_infinity^{3,0}=0. The next base target was attacked directly. For the central extension 1 -> W -> Q_2 -> V -> 1, the LHS derivation gives d_2:H^2(V,F_3)⊗W^* -> H^4(V,F_3) with image H^2(V,F_3)∪K, where K=im(d_2:W^*->H^2(V,F_3)) is the 9-dimensional hyperplane from Hard Attack 45. An explicit spanning argument, independently checked by finite-dimensional rank computation, gives H^2(V,F_3)∪K=H^4(V,F_3) (dimension 35). Hence E_3^{4,0}=0 and E_infinity^{4,0}=0.

This removes the second purely-base target. It does NOT imply E_infinity^{2,1}=0: the kernel of d_2 on E_2^{2,1} can be large, and the quotient by incoming d_2 from E_2^{0,2} is still load-bearing. The next gate is therefore the actual survival quotient E_3^{2,1}=ker(d_2:E_2^{2,1}->E_2^{4,0})/im(d_2:E_2^{0,2}->E_2^{2,1}), followed only then by the twisted Bockstein analysis.

Decision:
- H^2(V)∪K=H^4(V): **PASS / CLOSED**;
- E_3^{4,0}=0 and E_infinity^{4,0}=0: **PASS / CLOSED**;
- inference E_infinity^{2,1}=0: **NOT ESTABLISHED**;
- base targets (3,0),(4,0): **CLOSED / NO SURVIVORS**;
- full beta_rho^2: **OPEN / LOAD-BEARING**;
- unique coker maximizer without PD²: **OPEN / DECISIVE**.

Record: research/KUMMER_HARD_ATTACK_49_BASE_TARGET_H4_KILLED_AT_D2_2026-09-20.md

## 2026-09-20 — HARD ATTACK 50: DIMENSIONAL OBSTRUCTION FOR THE (2,1) SURVIVOR

HA50 makes the next bottleneck strictly sharper. From HA49, dim E_2^{2,1}=90 and rank d_2^{2,1}=35, so dim ker d_2^{2,1}=55. Since W is F_3^9 elementary abelian, dim E_2^{0,2}=dim H^2(W,F_3)=C(9,2)+9=45. Therefore dim E_3^{2,1}=55-rank(d_2^{0,2}) >=10. Hence E_3^{2,1} is forced nonzero by dimension alone: incoming d_2 can never kill the entire (2,1) sector. The target is therefore no longer to test whether E_3^{2,1}=0, but to identify the forced survivor subquotient and its H-action. The decomposition H^2(W)=Lambda^2 W^* plus beta_W(W^*) must be retained.

Decision:
- dim E_3^{2,1} >= 10: PASS / CLOSED;
- E_3^{2,1} != 0: PASS / CLOSED;
- exact dimension/module structure: OPEN / LOAD-BEARING;
- survival to E_infinity: OPEN;
- full beta_rho^2: OPEN / LOAD-BEARING;
- unique coker maximizer without PD^2: OPEN / DECISIVE.

Record: KUMMER_HARD_ATTACK_50_21_SURVIVOR_DIMENSION_OBSTRUCTION_2026-09-20.md (commit a8617b69289d4cfa16922903b50639e8a6059ecf).


## 2026-09-20 — HARD ATTACK 51: EXTERIOR FIBER SECTOR RANK 36

HA51 sharpens HA50. Writing c_i=d_2(w_i^*) for a basis of W^*, HA45 gives c_1,...,c_9 linearly independent. By the LHS Leibniz rule,
d_2(w_i^*w_j^*)=c_i\otimes w_j^*-c_j\otimes w_i^*.
Hence d_2 restricted to Lambda^2 W^* is injective, with rank 36. Since dim H^2(W)=45,
36 <= rank(d_2^{0,2}) <=45,
so
10 <= dim E_3^{2,1} <=19.
The remaining uncertainty is exactly the 9-dimensional fiber-Bockstein summand beta_W(W^*). The tempting statement d_2(beta_W(W^*))=0 is not yet promoted; it requires a direct transgression/Bockstein theorem or cochain proof.

Decision:
- d_2|_{Lambda^2 W^*} rank 36: PASS / CLOSED;
- 10 <= dim E_3^{2,1} <= 19: PASS / CLOSED;
- Bockstein-sector d_2: OPEN;
- exact E_3^{2,1} and H-action: OPEN / LOAD-BEARING;
- higher-differential survival: OPEN;
- full beta_rho^2: OPEN / LOAD-BEARING.

Record: KUMMER_HARD_ATTACK_51_EXTERIOR_SECTOR_RANK36_2026-09-20.md (commit 51454b5276e9120dabb8f52bbba4342c5437acd0).


## 2026-09-20 — HARD ATTACK 52: BOCKSTEIN FIBER SECTOR IS d2-CLOSED

HA52 resolves the nine-dimensional uncertainty left by HA51. For any linear functional phi:W->F3, push out the central extension along phi to a cyclic-kernel central extension 1->F3->E_phi->V->1. Naturality of the LHS spectral sequence sends the cyclic fiber Bockstein beta(u) to beta_W(phi). The standard odd-prime cyclic-kernel calculation has d2(beta(u))=0 (the Bockstein-of-extension-class phenomenon occurs one page later). Therefore d2(beta_W(phi))=0 for every phi, and hence d2 vanishes on the entire beta_W(W*) summand.

Combining with HA51's rank-36 injection on Lambda^2 W*, rank d2^{0,2}=36 exactly. Since ker(d2^{2,1}) has dimension 55,
\[
\boxed{\dim E_3^{2,1}=55-36=19.}
\]
This is an exact E3 result, not merely a lower bound. The 19-dimensional survivor is not yet identified as an H-module and need not survive to E_infinity; the next load-bearing target is the first higher differential, especially the d3/Bockstein mechanism.

Decision:
- d2(beta_W(W*))=0: PASS / CLOSED under the standard cyclic-kernel LHS calculation plus pushout naturality;
- rank d2^{0,2}=36: PASS / CLOSED;
- dim E3^{2,1}=19: PASS / CLOSED;
- H-module structure: OPEN / LOAD-BEARING;
- higher d3/higher survival: OPEN / LOAD-BEARING;
- full beta_rho^2: OPEN / LOAD-BEARING;
- unique coker maximizer without PD2: OPEN / DECISIVE.

Record: KUMMER_HARD_ATTACK_52_BOCKSTEIN_SECTOR_D2_CLOSED_2026-09-20.md (commit 4407d8dfc1206ade4384462014b2146c215d558d).


## 2026-09-20 — HARD ATTACK 53: THE 19-DIMENSIONAL (2,1) SURVIVOR IS PERMANENT

HA53 observes a pure bidegree obstruction. Since d_r has bidegree (r,1-r), any outgoing d_r from E_r^{2,1} with r>=3 lands in negative second degree, and any incoming d_r would originate at negative first degree. Hence no higher differential can touch E_3^{2,1}. Combining with HA52 gives
\[
\boxed{E_3^{2,1}=E_\infty^{2,1},\quad \dim E_\infty^{2,1}=19.}
\]
Thus the 19-dimensional sector is a genuine permanent LHS filtration piece, not a transient page-3 artifact.

Decision:
- E_3^{2,1}=E_infinity^{2,1}: PASS / CLOSED;
- dim E_infinity^{2,1}=19: PASS / CLOSED;
- H-module structure: OPEN / LOAD-BEARING;
- twisted beta_rho^2 on this sector: OPEN / LOAD-BEARING;
- unique coker maximizer without PD2: OPEN / DECISIVE.

Record: KUMMER_HARD_ATTACK_53_21_PERMANENT_SURVIVOR_2026-09-20.md (commit 20f4ba10bc744d5ae02e6c656cc6c55d8b216f5b).


## 2026-09-20 — HARD ATTACK 55: CRITICAL REVIEW OF HA54 AND H-LIFT PRE-CHECK

HA54 was critically re-audited before advancing to the representation-theoretic branch.

### Confirmed
The permanent LHS piece remains
\[
E_3^{2,1}=E_\infty^{2,1},\qquad \dim=19,
\]
and the concrete quotient
\[
\mathcal S=\frac{\ker(H^2(V,\mathbf F_3)\otimes K\to H^4(V,\mathbf F_3))}{\operatorname{im}(d_2:H^2(W,\mathbf F_3)\to H^2(V,\mathbf F_3)\otimes W^*)}
\]
has dimension 19. This is a genuine LHS associated-graded filtration piece. No orientation interpretation follows from permanence alone.

### Critical correction / pre-check
The existence of the previously computed \(H\)-action on the filtered degree-one object (and its image \(PSp_4(3)\)) does **not** by itself imply an action of \(H\) on
\[
1\to W\to Q_2\to V\to1.
\]
Before treating \(\mathcal S\) as an \(H\)-module, one must prove that the relevant \(H\)-action lifts to the central extension, equivalently that the extension class is preserved with the required induced action on \(W\), or construct the corresponding extension automorphisms directly.

If this lift fails, that failure is itself a meaningful boundary and the \(H\)-module branch must be closed. If it succeeds, only then may one prove functorially that \(K\), \(\ker\mu\), \(\operatorname{im}d_2\), and \(\mathcal S\) are \(H\)-stable.

### Input-category audit
The objects \(V,W,Q_2\) are finite filtered/extension data, but their admissibility as the declared intrinsic input category must remain explicit. No presentation, classification, known \(\chi\), or PD^2 orientation data may be silently imported into the construction of the \(H\)-action or the interpretation of \(\mathcal S\).

### q=3 boundary
The numerical result \(\dim\mathcal S=19\) is a frozen \(q=3\) local structural result unless a general-q theorem is supplied. It must not be promoted to a universal dimension statement.

### Strategic boundary
The three possible interpretations remain open:
1. **Collapse:** the 19D sector is controlled by already established \((R,p)\) data;
2. **Controlled Enrichment:** it adds a finite, functorially determined correction needed for \(\beta_\rho^2\);
3. **Independent Layer:** it carries genuinely new \(\rho\)-visibility.

No one of these is currently selected.

### Decisions
- permanent 19D LHS filtration piece: **PASS / CLOSED**;
- \(H\)-action lift to \(Q_2\): **OPEN / LOAD-BEARING**;
- \(H\)-module structure of \(\mathcal S\): **OPEN / LOAD-BEARING**;
- twisted \(\beta_\rho^2\) on \(\mathcal S\): **OPEN / LOAD-BEARING**;
- orientation-selector role: **OPEN / DECISIVE**;
- PD^2-free unique coker maximality: **OPEN / DECISIVE**;
- q-universality of the 19D numerical result: **OPEN**.

### Next authorized attack
First search the repository for an already established lift of the filtered \(H\)-action to \(Q_2\) or its central extension. If none exists, attack extension-class invariance/lift directly. Only after that may the actual \(H\)-module structure of \(\mathcal S\) be computed. No dimension-based module identification is authorized.


## 2026-09-20 — HARD ATTACK 56: FULL SP4 LIFT KILLED BY INTRINSIC TORSION LINE

HA55's load-bearing H-lift gate was attacked directly. The full ambient symplectic group used in the degree-4 representation track cannot act through actual automorphisms of the frozen q=3 Demuškin group.

The intrinsic degree-one audit already establishes
\[
G^{ab}\cong \mathbf Z_3^3\oplus\mathbf Z/3,
\]
with the Frattini image of \operatorname{Tor}(G^{ab}) a distinguished line \(\ell=\langle e_1\rangle\subset V\). Every actual automorphism preserves torsion in abelianization, hence preserves \(\ell\).

But the authoritative symplectic convention has \(t_v=I+v(Jv)^T\). For \(v=e_2\), \(Je_2=e_1\), so
\[
t_{e_2}e_1=e_1+e_2,
\]
which does not preserve \(\ell\). Therefore this element of \(Sp_4(\mathbf F_3)\) cannot arise from an actual automorphism of \(G\), and the full ambient symplectic action cannot lift to \(Q_2\).

Decision:
- full \(Sp_4(\mathbf F_3)\) lift to \(Q_2\): **FAIL / CLOSED**;
- intrinsic full-Sp4 module interpretation of \(\mathcal S\): **FAIL / CLOSED**;
- actual automorphism image versus line stabilizer: **OPEN / LOAD-BEARING**;
- lift of actual automorphism image to \(Q_2\): **OPEN / LOAD-BEARING**;
- \(\mathcal S\) under the actual automorphism image: **OPEN / LOAD-BEARING**;
- twisted \(\beta_\rho^2|_{\mathcal S}\): **OPEN / LOAD-BEARING**;
- orientation-selector role of \(\mathcal S\): **OPEN / DECISIVE**.

Interpretation: the earlier full \(Sp_4\) symmetry is an ambient graded symmetry, not the actual automorphism symmetry of the frozen q=3 group. The next authorized branch is the actual degree-one automorphism image, expected to lie in the stabilizer of the intrinsic torsion line. No full-Sp4 decomposition of \(\mathcal S\) should be treated as an intrinsic result.

Record: research/KUMMER_HARD_ATTACK_56_FULL_SP4_LIFT_KILLED_BY_TORSION_LINE_2026-09-20.md


## 2026-09-20 — STRATEGIC RESET: INFORMATION-LAYER PROGRAM

After HA48–56, the project has enough local negative boundaries that continued one-by-one candidate closure risks becoming the dominant activity. The common structural question is now elevated:

> What is the minimum kind of non-graded information required to distinguish the canonical orientation, and how does that information propagate through the filtration tower?

Three layers are fixed for the next strategic pass:
- Layer A: full mod-3 associated graded — q-blind, cannot recover the Z_3-valued orientation (PASS / CLOSED).
- Layer B: intrinsic projective relation-jet/cup+Bockstein carrier [(R,p)] — recovers chi mod 9 under the stated hypotheses (PASS / CLOSED).
- Layer C: deeper finite extension/cohomology data — includes the permanent 19D LHS piece at frozen q=3, but its orientation role is unresolved (OPEN). The full ambient Sp4 action is now closed as an intrinsic symmetry by HA56.

The next high-value program is therefore not to compute every Layer-C module. It is to prove/test an information-layer theorem:
1. formulate the sharp filtration-depth threshold as an explicit information theorem;
2. determine whether the Layer-B relation/power tower canonically propagates to higher 3-adic digits;
3. identify the first digit/layer at which genuinely new information appears, if any;
4. require every Layer-C candidate to pass q-blindness, functoriality, explicit orientation-bridge, non-redundancy, and q=3/control separation before representation computation.

The actual automorphism-image/lift branch remains OPEN/LOAD-BEARING but is subordinate unless it supplies the required functorial mechanism.

Stop rule: no broad representation scan, no full 19D module computation, and no new spectral scan until Test I (digit-depth theorem) or Test II (tower reuse) produces a concrete structural target.

Record: research/STRATEGIC_RESET_INFORMATION_LAYERS_2026-09-20.md (commit da2cd7ec3fae76106033580a1cc98e2cb2984316).

## 2026-09-20 — HARD ATTACK 57: INFORMATION-DEPTH BOUNDARY + LAYER-B TOWER REUSE

HA57 executes the two tests authorized by the Strategic Reset.

### Test I — sharp finite-information depth

For the standard family G_{3^s} versus the power-free control G_infty, the audited thresholds give
- Zassenhaus: G_{3^s}/D_N ≅ G_infty/D_N for N≤3^s, with separation at D_{3^s+1};
- lower-3-central: G_{3^s}/P_n ≅ G_infty/P_n for n≤s+1, with separation at P_{s+2}.

Since χ_{3^s} differs from the control modulo 3^n exactly in the worst case s=n−1, the corresponding family-level information boundaries are D_{3^{n−1}+1} and P_{n+1}. In particular mod 27 gives D_10 and P_4.

This is an information-depth theorem only for the standard comparison family; it is not yet a universal pointed orientation-recognition theorem.

Decision:
- sharp Zassenhaus depth: PASS / LOCAL;
- sharp lower-3-central depth: PASS / LOCAL.

### Test II — reuse of the Layer-B carrier

The mod-9 projective carrier [(R,p)] is already PASS / CLOSED for χ mod 9. HA57 tests whether the same relation/power mechanism canonically propagates all higher digits.

The result is negative only in the sense of proof status: no all-digit tower-reuse theorem has been established. The mod-27 coefficient-extension package detects the next q-layers but, on the evidence audited so far, does not supply the missing presentation-free rigidifying orientation bridge. Test I also shows that deeper non-graded information enters at increasing filtration depth.

Therefore:
- fixed Layer-B carrier -> all digits: OPEN / DECISIVE;
- Bockstein package as finite q-layer detector: PASS / LOCAL;
- Bockstein package as all-digit orientation carrier: CONDITIONAL / OPEN.

### Next authorized target

Do not reopen the 19D representation branch yet. Construct the mod-27 threshold residual: finite extension data at P_4 or D_10 modulo the information already contained in Layer B, then test whether the residual is zero (collapse) or nonzero with a natural orientation bridge (first genuinely new layer).

Record: research/HARD_ATTACK_57_INFORMATION_DEPTH_AND_LAYER_B_TOWER_2026-09-20.md

## 2026-09-20 — HARD ATTACK 58: MOD-27 THRESHOLD RESIDUAL IDENTIFIED

HA58 executed the authorized mod-27 threshold residual attack. The first new finite filtered information beyond the mod-9 Layer-B carrier appears at the next lower-3-central power/relation layer, at the P_4 threshold (equivalently within the D_10 information window on the Zassenhaus scale).

For the standard family q=3^s:
- q=3: the first power/relation contribution is already absorbed by Layer B;
- q=9: a new nonzero restricted-power/relation class appears in P_3/P_4;
- 27|q: that degree-three residual vanishes modulo P_4.

Thus the residual strictly separates q=9 from 27|q even though both have the same mod-9 orientation value. It is genuinely beyond the fixed Layer-B carrier.

The intrinsic residual is naturally projective: the degree-one torsion line and the symplectic commutator pairing identify its direction with the same orientation direction used at Layer B. What is not yet proved is the scalar normalization that identifies it with the exact second logarithmic digit 3e_2 in H^1(G,Z/9), or a universal natural transformation to chi mod 27.

This means the first new higher information is now a simpler filtered extension datum, not the 19D LHS sector. The 19D branch is superseded as strategic priority, not mathematically disproved.

Decisions:
- higher P_4 power/relation residual exists and detects q=9 vs 27|q: PASS / LOCAL;
- strict separation from Layer B: PASS / LOCAL;
- projective orientation-direction identification: CONDITIONAL / LOCAL;
- normalized mod-27 orientation bridge: OPEN / DECISIVE;
- 19D S as first new layer: HISTORICAL / SUPERSEDED as strategic priority;
- all-digit finite filtered orientation tower: OPEN / DECISIVE.

Next authorized target: P_4 normalization/transport theorem — prove or kill the canonical scalar bridge from the higher power residual to the already normalized mod-9 orientation direction.

Record: research/HARD_ATTACK_58_MOD27_THRESHOLD_RESIDUAL_2026-09-20.md


## 2026-09-20 — HARD ATTACK 59: COKER AS OBSTRUCTION QUOTIENT — CONCEPTUAL RESET

The “why coker?” attack sharpened the current program. The coker is not itself the orientation carrier. Its structural meaning is the universal quotient that removes gauge/lift directions before an intrinsic obstruction functional is evaluated.

For raw deformation data C and gauge image im(d), coker(d)=C/im(d) is the universal target for maps that kill im(d). The established mod-9 twisted obstruction factors through this quotient; the orientation is then selected by the vanishing/lifting condition of the resulting functional.

Therefore the correct pattern is
\[
\text{raw relation/power data}\to\text{coker/gauge quotient}\to\text{intrinsic obstruction}\to\text{orientation selector}.
\]

This rejects the overstrong slogan “coker = orientation” and provides a concrete conceptual basis for the appearance of coker.

The next decisive target is now narrower: construct the coefficient-extension diagram for the P_4 obstruction and test whether its obstruction functional reduces to the already normalized mod-9 family. If it does, the P_4 scalar may be forced by functorial compatibility; if it does not, a genuine normalization boundary may be proved.

Decisions:
- coker as universal obstruction quotient: **PASS / LOCAL**;
- coker itself as orientation carrier: **FAIL / CLOSED**;
- P_4 reduction-compatibility: **OPEN / DECISIVE**;
- successive obstruction tower: **OPEN / DECISIVE**.

Record: research/HARD_ATTACK_59_COKERNEL_AS_OBSTRUCTION_QUOTIENT_2026-09-20.md


## 2026-09-20 — HARD ATTACK 61-B: STRUCTURAL CANCELLATION OF OLD COEFFICIENT ACTION

HA61-B attacked whether the q=3/q=9 cancellation found in HA61-A is an accident of the frozen normal forms or is forced by the two-stage coefficient-extension mechanism.

Result: the feared old-action contribution does not survive as an independent secondary invariant once the (A_2)-valued cocycle lies on the primary obstruction zero locus. Terms coming from the old ρ_2 action belong to the already-satisfied first lifting obstruction / lift-gauge sector. The genuinely new coefficient-extension contribution is the derivative term ((μ∧f)(R)), while the new filtered information enters through the next residual (f(t_2)).

Thus, conditional on an intrinsic definition of (t_2), the secondary obstruction has the structural form

delta_3(f) = [f(t_2) + (mu wedge f)(R)] omega.

This explains why HA61-A gives the same new-parameter slope in the q=3 branch (nontrivial ρ_2) and q=9 branch (trivial ρ_2). It is stronger than a frozen-word numerical cancellation, but it does not yet prove a presentation-free construction of (t_2).

Decision:
- HA61-B: **PASS / LOCAL**;
- independent additive (B_{ρ_2}) at the secondary stage: **FAIL / CLOSED** as a separate invariant term;
- secondary obstruction shape conditional on intrinsic (t_2): **PASS / LOCAL**;
- presentation-free/gauge-independent (t_2): **OPEN / LOAD-BEARING**;
- all-digit induction: **OPEN / DECISIVE**.

Next authorized target: HA61-C — intrinsic definition and gauge-independence of (t_2), before any all-n induction. Record: research/HARD_ATTACK_61_B_STRUCTURAL_CANCELLATION_2026-09-20.md (commit 365c5241ba21707119a40090bd5a8cb20bc56366).


## 2026-09-20 — HA61-B SCOPE CORRECTION

Critical review accepted only in part. The q=3/q=9 calculations do establish a strong LOCAL constraint: no independent additive B_rho2 is visible in the audited frozen standard-family branches. However, the earlier claim that delta_2(f)=0 structurally forces every old-rho2 contribution to disappear was too strong. A general secondary term may depend on the A_2 lift z, and its vanishing/absorption requires an explicit full expansion, primary-zero reduction, lift-gauge test, independence test against t_2, and filtration cutoff.

Therefore HA61-B is corrected to **OPEN / LOAD-BEARING**. HA61-A remains **PASS / LOCAL**. The correct next order is B1 origin -> B2 primary-zero reduction -> B3 A_2-lift gauge test -> B4 test whether any survivor is canonically t_2-data -> B5 explicit filtration cutoff. Only then may HA61-C begin. No all-n induction.

Record: research/HARD_ATTACK_61_B_CORRECTION_2026-09-20.md (commit e2d719c7f8e14f4d60a69bfd704dcc2d368e36ae).


## 2026-09-20 — HA61-B3: A_2-LIFT GAUGE ATTACK — SCOPE CORRECTION

HA61-B3 was re-audited at the general cohomological level. For
\[
0\to\mathbf F_3\to A_3=\mathbf Z/27(\rho_3)\to A_2=\mathbf Z/9(\rho_2)\to0,
\]
an \(A_2\)-valued cocycle representative may be changed within its cohomology class by the exact gauge
\[
z\mapsto z+d_{\rho_2}(3\phi).
\]
The connecting homomorphism \(\delta_3:H^1(G,A_2)\to H^2(G,\mathbf F_3)\) is well-defined on cohomology classes, so the **full secondary obstruction** is invariant under this lift-representative gauge:
\[
\Delta_\phi\delta_3=0.
\]
This closes the gauge-dependence question at the level of the total obstruction.

However, this does **not** imply that a decomposition term \(B_{\rho_2}(z)\) vanishes individually. Cancellation with other representative-dependent pieces remains logically possible. In particular, the statement in the earlier HA61-B structural document that the primary-zero condition by itself eliminates every old-action contribution was too strong unless the full source expansion and filtration cutoff are supplied.

The exact current source ledger is:
1. old \(\rho_2\)-action / \(A_2\)-lift terms;
2. new \(\mu\)-prefix × lift terms;
3. relation/power jet terms;
4. the \(P_3/P_4\) residual \(t_2\);
5. lift-gauge cross terms;
6. \(D_4\)/higher-filtration terms.

Primary-zero \(\delta_2(f)=0\) is a **domain condition for the existence of an \(A_2\)-lift**, not by itself a proof that source (1) is absent from every chosen expansion. Therefore the independent-term question remains open until B4/B5 complete the source-by-source independence and filtration audit.

### Decision
- **B3 lift-gauge invariance of the total secondary connecting obstruction: PASS / CLOSED.**
- **B3 old-action elimination / \(B_{\rho_2}=0\): OPEN / LOAD-BEARING.**
- **HA61-B overall: OPEN / LOAD-BEARING.**
- **B4:** test whether any surviving old-action contribution factors canonically through a presentation-free \(t_2\).
- **B5:** explicit coefficient-valuation + filtration cutoff; membership in \(D_4\) alone is not sufficient.
- **HA61-C remains closed/not opened** until B4/B5 are resolved.

This supersedes the stronger HA61-B wording that classified the independent \(B_{\rho_2}\) term as FAIL/CLOSED. The earlier claim is retained only as historical/superseded text; it must not control the current state.
