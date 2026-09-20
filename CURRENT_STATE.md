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
