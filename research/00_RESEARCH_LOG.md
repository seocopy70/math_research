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



## 2026-09-20 — CRITICAL REVIEW OF LOWER 3-CENTRAL BOUNDARY / LOGICAL LIMIT

The first-stage result was attacked before advancing to Kummer recognition.

The algebraic threshold argument survives: for the lower 3-central series P_{n+1}=P_n^3[P_n,G], the standard product formula gives x_1^{3^s} weight s+1, and the abelianization at n=s+2 gives a sharp separation. The quotient-isomorphism statement therefore remains PASS / LOCAL.

Three precision limits are binding:

1. “χ mod 3^k is determined by G/P_{k+1}” is valid only as a standard-family/classification-level information statement. Pairwise separation of the finite q-layers follows from the first abelianized invariant, but this does not yet provide a canonical selector/natural transformation from an arbitrary quotient object to the pointed orientation.

2. The lower-3-central filtration itself is functorial, but a twisted Kummer condition using coefficients Z/3^k(ρ) cannot simply be declared a predicate of G/P_{k+1}: the coefficient action is part of the unknown ρ. The next proof must define the recognition predicate without circularly supplying χ, or else prove that the relevant variable action/semidirect-product data factors through the finite quotient in the required sense.

3. The linear threshold is an information-boundary comparison, not evidence that P_{k+1} is intrinsically “better” or a compressed orientation carrier. In particular, quotient-level automorphisms may still destroy pointedness even when the isomorphism class separates the standard q-layers.

The rank-two computation is a sanity check, not an independent proof of the general theorem; the essential proof remains the lower p-central product formula plus functoriality and abelianization.

Decision: first-stage threshold theorem remains PASS / LOCAL. No new gate is introduced. The single next theorem remains the finite Kummer-recognition/factorization statement, with circularity and pointedness treated inside its proof rather than as separate gates.


## 2026-09-20 — FIRST-STAGE LOWER 3-CENTRAL INFORMATION BOUNDARY

A theorem draft was completed comparing the Zassenhaus filtration D_n and lower 3-central series P_n for the standard family G_{3^s} and power-free control G_∞.

Using Jennings' formula for D_n and the standard product formula P_n=∏_{i+j≥n}γ_i^{3^j}, the power term x_1^{3^s} has D-weight 3^s but P-weight s+1. Hence
G_{3^s}/D_N ≅ G_∞/D_N iff N≤3^s,
and
G_{3^s}/P_n ≅ G_∞/P_n iff n≤s+1,
with sharpness at the next levels detected already after abelianization. The same sharpness mechanism was checked conceptually in the rank-two analogue <x,y | x^{3^s}[x,y]>.

Consequently, within the standard family and using the known orientation formula χ_{3^s}(x_2)=(1-3^s)^{-1}, the information boundary for χ mod 3^k is D_{3^{k-1}+1} on the Zassenhaus scale versus P_{k+1} on the lower-3-central scale; mod 27 gives D_10 versus P_4.

Logical boundary: this is an isomorphism-class information-boundary result, dependent on the standard-family classification/orientation formula. It is not a pointed naturality theorem and does not yet prove a q-blind intrinsic Kummer recognition criterion on G/P_{k+1}.

Status:
- Zassenhaus threshold: PASS / LOCAL.
- Lower 3-central threshold: PASS / LOCAL, subject to the standard P_n product formula.
- Sharpness by abelianization: PASS / LOCAL.
- Rank-two sanity check: PASS / LOCAL.
- Linear information boundary for χ mod 3^k: PASS / LOCAL, standard-family/classification dependent.
- Kummer recognition from G/P_{k+1}: OPEN.

Detailed note: research/LOWER_3_CENTRAL_INFORMATION_BOUNDARY_2026-09-20.md
## 2026-09-20 — CRITICAL CORRECTION: Zassenhaus threshold wording + mixed m-adic reopening

A review correction was independently checked.

The threshold claim was never that (G/D_N(G)) itself is abelian. The correct calculation is
[
(G/D_NG)^{ab}=G/(D_NG').
]
For (G_{3^s}), Jennings' formula shows that at (N=3^s+1)
[
(G_{3^s}/D_N)^{ab}cong mathbf Z/3^s	imes(mathbf Z/3^{s+1})^3,
]
whereas the power-free control has ((mathbf Z/3^{s+1})^4). For (Nle3^s), (x_1^{3^s}in D_N(F)), so the relator (x_1^{3^s}c) reduces to (c) modulo (D_N(F)), yielding
[
G_{3^s}/D_Ncong G_infty/D_N.
]
Thus (D_{3^{n-1}+1}) is sufficient and (D_{3^{n-1}}) insufficient to distinguish the standard-family cases relevant to (chimod3^n), with classification/orientation formula dependence explicitly retained. For (n=2,3), the thresholds are D_4 and D_10.

The second correction concerns HARD ATTACK 10. Its negative result is specifically the failure of the ordinary presentation-independent local degree-(le3) Fox truncation. It does not establish a no-go for finite mixed ((3,I))-adic carriers.

A new definitional branch is therefore authorized:
[
mathfrak m=(3,I),qquad J_n^{mix}=I_{mathrm{Fox}}+mathfrak m^n,
]
subject first to definition, Nielsen covariance, relator gauge/unit/conjugation invariance, finite-level well-definedness, and an orientation bridge. No numerical scan is authorized before these gates pass.

The existence gate and the non-tautology/compression gate are now explicitly separated: Fox-derived finite objects are not excluded from existence, while any claim of genuine compression/independence is tested later.

Load-bearing warning: for (r'=grg^{-1}), Fox differentiation contains an additional term
[
g,partial r+(1-grg^{-1})partial g,
]
so the relation/augmentation ideal must be defined to control this term. This is the first naturality obstacle.

Decision:
- Zassenhaus threshold on standard family: **PASS / LOCAL**;
- ordinary degree-3 Fox truncation no-go: **PASS / CLOSED**;
- mixed m-adic carrier: **OPEN / REAUTHORIZED FOR DEFINITIONAL ATTACK ONLY**;
- relator-gauge naturality: **OPEN / LOAD-BEARING**.

Record: `research/CRITICAL_CORRECTION_MIXED_MADIC_AND_ZASSENHAUSZ_THRESHOLD_2026-09-20.md`

## 2026-09-20 — HARD ATTACK 14: no nontrivial quotient of the exact local Fox carrier

The remaining quotient-based loophole was attacked directly.

For the frozen (q=3) relation, write
[
A=1+u_1,quad B=1+u_2,quad C=1+u_3,quad D=1+u_4.
]
The exact Fox equations are
[
F_1=B(1+A)+A^2,quad F_2=A-1,quad F_3=D-1,quad F_4=C-1.
]
Thus
[
F_2=u_1,quad F_3=u_4,quad F_4=u_3,
]
and after quotienting by these,
[
F_1=2u_2+3.
]
Therefore
[
mathcal A_{mathrm{Fox}}
=
mathbf Z_3[[u_1,u_2,u_3,u_4]]/(u_1,u_3,u_4,2u_2+3)
congmathbf Z_3.
]

The exact local Fox obstruction scheme is already a reduced characteristic-zero point:
[
(A,B,C,D)=(1,-1/2,1,1).
]

Hence a proper unital quotient of this local coefficient algebra either has finite (3)-power characteristic and loses higher (3)-adic digits, or collapses the point. There is no proper quotient-based compression preserving the full orientation.

This closes a specific class of “compress the Fox scheme itself” proposals. It does **not** prove that no different, non-quotient intrinsic exact extension object can exist. Such an object would have to be defined independently of Fox and then factor naturally into the exact Fox carrier.

Decision:
- **quotient-of-local-Fox-scheme compression: FAIL / CLOSED;**
- **exact local Fox carrier minimal under full-(3)-adic-preserving quotients: PASS / CLOSED;**
- **independent intrinsic non-quotient exact compression: OPEN.**

Record:
research/ORIENTATION_FOX_LOCAL_QUOTIENT_MINIMALITY_HARD_ATTACK_2026-09-20.md

## 2026-09-20 — HARD ATTACK 13: full associated-graded no-go and minimal extension lower bound

The previous attack only established that bounded associated-graded windows cannot recover the full orientation. A stronger question was attacked: perhaps the entire infinite mod-3 Zassenhaus graded object could still encode (q) and hence (chi).

The literature boundary closes this loophole for the present odd-prime Demuškin setting. Mináč–Pasini–Quadrelli–Tân identify, for Demuškin groups, the complete graded group algebra
[
\operatorname{gr}\mathbf F_p[[G]]\cong U(L(G))
]
with the quadratic/PBW Demuškin graded algebra. For odd (p), its defining relation is the quadratic symplectic relation
[
[X_1,X_2]+[X_3,X_4]+\cdots,
]
independent of the Demuškin (q)-invariant. Thus the full mod-3 associated-graded object is (q)-blind, not merely finite truncations.

Consequently the rank-four family
[
G_{3^s}=\langle x_i\mid x_1^{3^s}[x_1,x_2][x_3,x_4]\rangle,
qquad
G_\infty=\langle x_i\mid [x_1,x_2][x_3,x_4]\rangle
]
has the same mod-3 graded Demuškin object while
[
\chi_{3^s}(x_2)=(1-3^s)^{-1}
]
varies with (s), and (\chi_\infty(x_2)=1).

This is a genuine project-specific lower bound:

[
\boxed{
\text{full mod-3 associated graded data}
\not\Rightarrow
q
\not\Rightarrow
\chi.
}
]

Therefore any successful q-blind carrier must add non-graded filtered/characteristic-zero extension information. At the first nontrivial level, the projective degree-3 power component (P_3) coupled to the quadratic relation (R_2) supplies such information and recovers (chi\bmod9).

A further precision was added: it would be false to infer that every higher (3)-adic digit requires a new independent extension class. For fixed (q=3), the exact equation (1+2B=0) compresses all digits into one exact (\mathbf Z_3)-coefficient equation. Thus the remaining question is not “how many digits/classes?” but whether this exact extension information admits a canonical intrinsic representation strictly smaller than the universal projective Fox obstruction scheme.

Decision:
- **full mod-3 associated-graded (	o q,chi): FAIL / CLOSED;**
- **minimal non-graded extension lower bound for mod-9: PASS / LOCAL;**
- **intrinsic exact intermediate carrier: OPEN.**

Record:
research/ORIENTATION_FULL_GRADED_NO_GO_MINIMAL_EXTENSION_2026-09-20.md

## 2026-09-20 — HARD ATTACK 10: degree-3 Fox truncation FAIL / CLOSED under Nielsen change

A concrete Nielsen-equivalent presentation was used to attack the remaining idea that the fixed q=3 degree-3 Fox compression might itself be intrinsic.

Take
\[
x_1=y_1y_2,\quad x_2=y_2,\quad x_3=y_3,\quad x_4=y_4.
\]
The exact transformed Fox row is
\[
J'_1=Y_1^2Y_2+Y_1Y_2+1,
\]
\[
J'_2=Y_1(Y_1^2Y_2^2+Y_1^2Y_2+1),
\]
with the remaining rows rational in \(Y_3,Y_4\).

The transported canonical point is
\[
(Y_1,Y_2,Y_3,Y_4)=(-2,-1/2,1,1),
\]
which lies in the same \(1+3\mathbf Z_3\) neighborhood.

After writing \(Y_i=1+v_i\) and truncating to total degree \(\le3\), the second row evaluates at
\[
(v_1,v_2,v_3,v_4)=(-3,-3/2,0,0)
\]
to
\[
-243/2\neq0,
\]
although the full exact Fox row vanishes there.

Decision:
- full Fox scheme Nielsen covariance: PASS/CLOSED;
- fixed-normal-form degree-3 Fox compression: PASS/CLOSED;
- presentation-independent degree-3 Fox truncation: **FAIL/CLOSED**;
- intrinsic exact degree-(2,3) filtered carrier by another construction: **OPEN**.

This is a concrete counterexample to using the local degree bound of the frozen normal form as an intrinsic exact truncation theorem.

Record:
research/ORIENTATION_FOX_DEGREE3_NIELSEN_HARD_ATTACK_2026-09-20.md

## 2026-09-20 — HARD ATTACK 9: naive integral augmentation jet FAIL / CLOSED

The proposed next object \(\langle r-1\rangle\subset I^2/I^4\) in \(\mathbf Z_3[[F]]\), with ordinary augmentation ideal \(I\), was attacked before any computation.

For \(r=x_1^3[x_1,x_2][x_3,x_4]\) and \(X_i=x_i-1\),
\[
x_1^3-1=3X_1+3X_1^2+X_1^3.
\]
The commutator product begins in degree 2, so
\[
r-1=3X_1+[X_1,X_2]+[X_3,X_4]+O(I^3),
\]
and therefore \(r-1\notin I^2\).

This kills the proposed plain \(\mathbf Z_3\)-augmentation jet at the definition level. It is not a matter of missing gauge proof.

The correct distinction is:
- standard mod-3 Zassenhaus filtration: uses the completed \(\mathbf F_3[[F]]\) augmentation ideal and yields the degree-(2,3) restricted-Lie relation jet;
- ordinary \(\mathbf Z_3[[F]]\) augmentation filtration: is different and does not place the Demushkin relator in \(I^2\);
- mixed p-adic/Zassenhaus weighted filtrations: a legitimate possible direction, but finite associated graded pieces are residue-layer objects and do not automatically carry the full exact scalar \(-1/2\in\mathbf Z_3^\times\).

This is an independent structural confirmation of the previously closed “naive \(\mathbf Z_3\) restricted-Lie scalar extension” route.

Decision:
- plain \(\mathbf Z_3\)-augmentation \(I^2/I^4\) carrier: **FAIL / CLOSED**;
- mod-3 Zassenhaus degree-(2,3) carrier: **PASS / CLOSED**;
- mixed integral weighted jet: **OPEN**, but cannot be assumed to contain full 3-adic information;
- exact universal Fox scheme: **PASS / CLOSED** under the stated standard hypotheses;
- intrinsic exact two-component filtered compression: **OPEN**.

Literature check: standard Zassenhaus definitions use the augmentation ideal of \(\mathbf F_p[[G]]\), consistent with Jennings/Lazard and modern Demushkin/Koszul references.

Record:
research/ORIENTATION_INTEGRAL_AUGMENTATION_JET_HARD_ATTACK_2026-09-20.md



## 2026-09-19 — HARD ATTACK 2: exact Z_3 carrier identification reopened

A second theorem-level weakness was found. The fixed q=3 crossed-derivation calculation is algebraically sound, but the later claim that a concrete projective degree-(2,3) relation jet with exact Z_3 coefficients is itself an established carrier is too strong.

The mod-3 restricted Lie object uses a characteristic-3 p-operation. It cannot simply be scalar-extended to Z_3 as the same restricted-Lie structure. Therefore the exact pair (R,P_3) over Z_3 has not been independently defined in the required sense.

Correct status: fixed full relation + exact crossed derivation = PASS/CLOSED; intrinsic mod-9 projective degree-(2,3) carrier = PASS/CLOSED; concrete exact two-component degree-(2,3) carrier => full chi = OPEN; naive Z_3 restricted-Lie scalar extension = FAIL/CLOSED.

Detailed audit: research/ORIENTATION_EXACT_Z3_CARRIER_HARD_AUDIT_2026-09-19.md.


## 2026-09-19 — HARD ATTACK 3: universal exact Fox obstruction carrier

The exact-carrier search was reopened with a genuinely different object type rather than a scalar extension of the characteristic-3 restricted Lie carrier. For a fixed minimal one-relator presentation, define the universal Laurent coefficient ring A=Z_3[T_1^{±1},...,T_d^{±1}] and the unevaluated twisted Fox-Jacobian row J_r=(tau(partial r/partial x_i)), tau(x_i)=T_i. The carrier is defined independently of any candidate orientation; a character is recovered only after evaluating T_i at its values and solving J_r=0.

For r=x_1^3[x_1,x_2][x_3,x_4], the row is J_1=1+A+A^2/B, J_2=A^2(A-1)/B, J_3=A^3(D^{-1}-1)/C, J_4=A^3(1-C^{-1})/D. On 1+3Z_3 the zero locus is uniquely A=C=D=1, B=-1/2. Thus a fixed-presentation finite exact algebraic carrier recovering the full orientation has been obtained.

This does not yet solve intrinsicity: arbitrary minimal free-basis changes must be shown to induce the corresponding Laurent-torus coordinate change and transform the obstruction ideal covariantly. Relator conjugation/unit changes must also be checked. The object is not finite information; it contains exact 3-adic coefficient data in a finitely generated algebraic presentation.

Decision:
- fixed-presentation universal Fox carrier: PASS/CLOSED;
- non-circular input definition: PASS/CLOSED;
- q=3 full-orientation recovery: PASS/CLOSED;
- presentation-independent/intrinsic carrier: OPEN;
- two-component degree-(2,3) compression: OPEN.

Detailed record: research/ORIENTATION_EXACT_UNIVERSAL_FOX_CARRIER_AUDIT_2026-09-19.md.


## 2026-09-19 — HARD ATTACK 4: universal Fox carrier covariance CLOSED

The new universal exact Fox carrier was subjected to the presentation-change attack. The carrier is formulated over the completed local coefficient ring A=Z_3[[U_1,...,U_d]], T_i=1+U_i, and is projective under multiplication by units.

Relator conjugation gives J_{uru^{-1}}=tau(u)J_r, so the zero locus is unchanged. Relation-generator changes act by completed coefficient-ring units, conditional on the standard cyclic one-relator relation-module structure. A free-basis change is controlled by Fox's chain rule: the row transforms by induced formal torus substitution followed by an invertible evaluated Fox Jacobian. Hence the universal obstruction scheme is presentation-covariant and its character zero locus is preserved.

For the frozen q=3 relation the unique point in 1+3Z_3 is (1,-1/2,1,1). Therefore the exact carrier branch has a new positive endpoint:
- non-tautological exact characteristic-zero carrier in universal projective Fox-scheme form: PASS/CLOSED;
- presentation covariance: PASS/CLOSED at the universal Fox-calculus level, conditional on standard one-relator relation-module facts;
- fixed q=3 recovery: PASS/CLOSED;
- two-component degree-(2,3) compression: OPEN;
- bounded finite-information universal carrier: FAIL/CLOSED.

The research question is now sharpened: can the universal Fox obstruction scheme be compressed intrinsically to a smaller filtered object, ideally degree (2,3), without reintroducing the earlier circularity?

Detailed records: research/ORIENTATION_EXACT_UNIVERSAL_FOX_CARRIER_AUDIT_2026-09-19.md and research/ORIENTATION_EXACT_UNIVERSAL_FOX_COVARIANCE_AUDIT_2026-09-19.md.


## 2026-09-19 — HARD ATTACK 5: exact Fox degree-3 compression

A further structural reduction was found. In local coordinates T_i=1+u_i, the fixed q=3 universal Fox obstruction ideal is exactly equivalent on the 1+3Z_3 neighbourhood to
F_1=3+3u_1+u_1^2+u_1u_2+2u_2,
F_2=u_1,
F_3=u_4,
F_4=u_3.
Hence the zero locus is u_1=u_3=u_4=0 and 2u_2+3=0, giving chi(x_2)=-1/2. The unreduced second Fox coefficient has degree 3, so the full fixed-normal-form row has local degree at most 3.

The power-free control has projective ideal equivalent to (B-1,A-1,D-1,C-1), giving the trivial 1+3Z_3 character locus. Thus the exact carrier separates q=3 from the power-free control without using q as an input label.

Decision:
- fixed-normal-form degree-3 polynomial compression: PASS/CLOSED;
- intrinsic degree-3 truncation under arbitrary presentation change: OPEN;
- exact two-component (R,p)-type compression: OPEN.

Detailed record: research/ORIENTATION_EXACT_FOX_DEGREE3_COMPRESSION_AUDIT_2026-09-19.md.


## 2026-09-20 — HARD ATTACK 11: higher Bockstein / p-adic digit tower

The proposed Bockstein/higher-obstruction bridge was attacked at the definition level. Candidate-dependent twisted coefficient criteria are exact orientation tests, but they cannot be the desired q-blind filtered input because the coefficient system already depends on the unknown character. Higher Bocksteins can detect p-power lifting depth, but their existence does not supply a canonical map to the next character digit. In the frozen q=3 Fox equations, after the mod-9 layer is fixed, all higher digits are forced recursively by the exact unit equation 1+2B=0; no independent higher geometric obstruction appears in that presentation.

Decision: **OPEN / STRUCTURAL** for a genuine higher-obstruction bridge; **FAIL / CLOSED** for the inference “higher Bockstein tower alone reconstructs full chi.”

Next attack: distinguish full filtered extension data from the bare associated graded tower, and test whether the former canonically reconstructs the exact Fox obstruction ideal. If not, seek an explicit same-graded/different-lift obstruction pair.

Record: `research/ORIENTATION_HIGHER_BOCKSTEIN_HARD_ATTACK_2026-09-20.md`.


## 2026-09-20 — HARD ATTACK 12: filtered extension vs associated graded

The phrase “full filtered tower” was split into (A) the full associated-graded tower and (B) an actual compatible tower of filtered extension quotients. (A) does not retain extension/gluing data; the $q=3^s$ family gives the finite-window obstruction to full $\chi$. (B), if it literally retains compatible residues of the relation in a complete separated filtration, reconstructs the completed relation by inverse limit, and completed Fox calculus then applies by continuity. This is mathematically valid but largely formal and does not by itself provide a smaller intrinsic carrier.

Decision: associated-graded full-$\chi$ claim **FAIL / CLOSED**; full filtered-extension-to-Fox implication **PASS / LOCAL**; genuine intermediate compression **OPEN**.

Record: `research/ORIENTATION_FILTERED_EXTENSION_VS_GRADED_HARD_ATTACK_2026-09-20.md`.


## 2026-09-20 — CONSOLIDATED RESEARCH PROGRAM SYNTHESIS / MOD-27 GATE

A full-state synthesis was frozen in research/RESEARCH_PROGRAM_SYNTHESIS_2026-09-20.md to prevent local branch results from obscuring the main mathematical question.

The refined objective is to determine the exact information boundary for recovering the canonical 3-adic orientation: what the full mod-3 associated graded loses; what the first filtered extension layer adds; whether higher finite 3-adic digits admit intrinsic finite-level carriers; and whether a compatible tower yields full chi while remaining genuinely smaller than exact Fox/presentation data.

### Established
- Complete mod-3 associated graded is q-blind: **FAIL/CLOSED** for recovering q or chi.
- overline J_3=[(R,p)] recovers chi mod 9: **PASS/CLOSED** under the audited standard transgression/Bockstein convention.
- A literal compatible full filtered extension tower reconstructs the completed relation and hence chi by inverse-limit + continuous Fox: **PASS/LOCAL**, but this is not a compression result.
- Universal exact Fox carrier recovers full chi: **PASS/CLOSED** under the audited hypotheses.
- Exact local Fox algebra is already reduced and isomorphic to Z_3: quotient compression preserving all 3-adic information is **CLOSED**.

### Explicitly excluded
Naive Z_3 augmentation jet; naive Z_3 restricted-Lie scalar extension; intrinsic fixed degree-3 Fox truncation; higher-Bockstein-alone reconstruction; full associated-graded tower reconstruction; bounded-degree + bounded-precision universal recovery; quotient compression of the exact local Fox algebra.

### Still open
P_3 information-theoretic minimality; absolute carrier minimality outside the explicitly defined quotient-observable category; intrinsic J_27; compatible higher J_(3^n); strict intrinsic compression of the full Fox carrier; non-tautological filtered-extension -> exact-Fox factorization.

### NEXT GATE
The next task is **not** another broad scan. It is the existence/no-go test for an intrinsic mod-27 carrier
\[
J_{27}(G)\Rightarrow\chi\bmod27.
\]
The candidate must be independent of the unknown chi, presentation/Nielsen/relator-gauge invariant, separating at mod 27, naturally reduce to the established mod-9 carrier, and not be a relabeled Fox-equation modulo 27. Any failure at definition/invariance/separation closes that branch immediately.

This is the current authoritative continuation point.

 
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


## 2026-09-20 — HARD ATTACK 15: MOD-27 CATEGORY ADEQUACY / TRIVIAL-INTRINSICITY LOOP

Before constructing a higher obstruction, the admissible input category itself was attacked. The PRE-MOD27 gate allowed the group G together with filtered relation data, but if arbitrary intrinsic constructions of the full group G are admitted, then the canonical dualizing module/action already contains the canonical orientation. Likewise, the Demuškin classification identifies q as a group invariant and recovers the canonical orientation from q in the standard presentation. Hence an unrestricted group-only J_27 exists trivially, but this is not a new filtered/relation carrier.

This forces a sharper definition-level distinction: “q is not literally supplied” is not enough for q-blindness. A legitimate new J_27 must be constructed from the declared filtered/relation-information functor itself, without first extracting the dualizing action, q (or an equivalent complete classification invariant) and repackaging it as the carrier.

The mod-27 problem is therefore split into: (A) unrestricted group-intrinsic reconstruction — known/tautological for this program; (B) filtered/relation-data reconstruction — still OPEN; (C) mod-3 associated-graded/cohomological data — already insufficient; (D) full compatible filtered extension tower — sufficient but essentially retains the completed relation.

Decision: **CATEGORY-ADEQUACY CORRECTION: PASS / CLOSED.** This closes a methodological loophole, not the existence/no-go question for a genuine filtered J_27.

Record: research/MOD27_CATEGORY_ADEQUACY_HARD_ATTACK_2026-09-20.md


## 2026-09-20 — HARD ATTACK 16: COEFFICIENT-9 BOCKSTEIN EXTENSION CARRIER CANDIDATE

A genuinely new mod-27 candidate survived the definition-level attack:
\[
\mathcal B_{27}(G)=\bigl(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9\bigr),
\]
with \(\beta_9\) the connecting map for \(0\to\mathbf F_3\to\mathbf Z/27\to\mathbf Z/9\to0\). This is intrinsic coefficient-extension data, functorial, q-blind, and visibly reduces to the audited mod-9 cup+Bockstein carrier.

For the standard family, direct relator lifting gives \(\beta_9(f)=qf(x_1)/9\) in the H² line. Naturality gives \(\beta_9\circ\iota=\beta_1\). Hence the first two coefficient-extension layers distinguish q=3, q=9, and q divisible by 27 without inserting q.

A critical correction was made during the attack: the orientation digit must be expressed by the p-adic logarithm
\[
\lambda_{27}=\frac13\log\chi\pmod9,
\]
not by \((\chi-1)/3\), which is not additive mod 9. For the standard family, \(\lambda_{27}=e_2\) at q=3, \(3e_2\) at q=9, and 0 at q divisible by 27, giving \(\chi(x_2)=13,10,1\pmod{27}\) after exponentiation.

This produces the first serious intrinsic J_27 candidate. However, the orientation bridge is not yet theorem-level: one must prove naturally, without a chosen standard presentation, that the cup-dual of the relevant Bockstein layer equals the corresponding coefficient of \(\frac13\log\chi\). Gauge/morphism naturality of this bridge is the remaining load-bearing step.

Decision: **MOD-27 BOCKSTEIN-EXTENSION CARRIER: OPEN / STRONG CANDIDATE.**

Substatus: definition PASS; q-blindness PASS; functoriality structural PASS; reduction to J9 PASS; separation PASS/LOCAL; orientation bridge OPEN; compression below Fox OPEN.

Record: research/MOD27_BOCKSTEIN_EXTENSION_CARRIER_HARD_ATTACK_2026-09-20.md


## 2026-09-20 — HARD ATTACK 17: BOCKSTEIN CARRIER MAY ONLY REPACKAGE q-VALUATION

The apparent mod-27 orientation bridge was attacked at the non-tautology level. The coefficient-extension package \(\mathcal B_{27}\) separates the standard family by \(v_3(q)=1,2,\ge3\), while the proposed logarithmic orientation values \(1,3,0\pmod9\) are already a known function of that q-class through the Demuškin orientation formula. Thus the current evidence is equally explained by \(\mathcal B_{27}\to v_3(q)\text{-class}\to q\text{-class}\to\chi\), which is forbidden classification/repackaging under the revised gate.

Therefore the package remains an intrinsic q-information detector, but its status as a new orientation carrier is downgraded. Decision: **CONDITIONAL / NOT YET ADMISSIBLE**. To recover admissibility, one needs a presentation-free universal identity or independent universal property producing \(\frac13\log\chi\) directly, without first extracting q/classification data. If no such factorization exists, close the candidate as an orientation carrier while retaining the detector result.

Record: research/MOD27_BOCKSTEIN_EXTENSION_CARRIER_HARD_ATTACK_2026-09-20.md


## 2026-09-20 — HARD ATTACK 18: internal-automorphism no-go for the mod-27 Bockstein carrier

The coefficient-extension candidate
\[
\mathcal B_{27}=(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9)
\]
was attacked by the automorphism group of the carrier itself.

For the frozen \(q=3\) relation, \(a_1\in3\mathbf Z/9\) and \(a_2,a_3,a_4\) are unrestricted. The map
\[
S(a_1,a_2,a_3,a_4)=(a_1,4a_2,a_3,a_4)
\]
is \(\mathbf Z/9\)-linear, fixes reduction and \(\iota(H^1(G,\mathbf F_3))\), preserves the cup product, and preserves \(\beta_9\), since \(\beta_9\) sees only the \(a_1\)-component in the frozen relation.

Thus the full declared carrier has an internal symmetry acting trivially on the mod-3 direction but nontrivially on its characteristic-zero lift. The required \(q=3\) logarithmic orientation digit
\[
\lambda_{27}=\frac13\log\chi\equiv e_2\pmod9
\]
therefore cannot be canonically selected from the declared carrier.

Decision:
- **\(\mathcal B_{27}\) as a mod-27 orientation carrier: FAIL / CLOSED;**
- intrinsic coefficient-extension/q-layer detector: **PASS / LOCAL;**
- a different mod-27 carrier with additional rigidifying structure: **OPEN.**

This supersedes HARD ATTACK 17's CONDITIONAL status. No further Bockstein-only scan is authorized.


## 2026-09-20 — HARD ATTACK 20: Bockstein package closes as a new non-tautological mod-27 carrier

Hard Attack 19 corrected the logical gap in Hard Attack 18: the internal map S on H^1(G,Z/9) is an abstract carrier automorphism, not yet an admissible group-induced morphism. Therefore S alone cannot prove a naturality no-go in the project's real input category.

A stronger independent attack was then made at the factorization level. On the rank-four Demuškin family, the entire declared package B_27 has exactly the three coefficient-extension types determined by v_3(q)=1,2,>=3: beta_1 nonzero; beta_1=0 with descended beta_9 nonzero; both zero. The known mod-27 orientation reduction has exactly the corresponding three classes 13,10,1. Thus the present package's successful orientation values are extensionally a function of the same finite q-valuation/classification partition.

No independent chain-level identity, universal property, or finer invariant has been produced inside B_27 that distinguishes orientations while the q-class is held fixed. Therefore the package fails the PRE-MOD27 operational non-tautology criterion as a **new orientation carrier**, even though it remains a valid intrinsic finite q-layer detector.

Decision:
- B_27 q-layer detector: **PASS / LOCAL**;
- B_27 as new non-tautological mod-27 orientation carrier: **FAIL / CLOSED**;
- Hard Attack 18 absolute symmetry no-go: **HISTORICAL / SUPERSEDED**;
- successor carrier with genuinely new q-blind rigidification: **OPEN**.

Stop consequence: no further beta_1/beta_9 scans on the same family are authorized. A successor must add genuinely new structure or an independent universal property, and must first pass the same object/category/q-blindness gate.## 2026-09-20 — CRITICAL REVIEW OF HARD ATTACK 20

Hard Attack 20's closure of the mod-27 Bockstein carrier was overstrong. The argument established only that the **observed Bockstein layers** on the tested Demuškin family form three q-valuation cases. It did not prove that the full structured carrier \((H^1(F_3),H^1(Z/9),red,iota,cup,beta_1,beta_9)\) has exactly three isomorphism types, nor that every natural bridge on the full admissible category factors through q/classification.

This distinction is load-bearing: agreement with the known q->chi formula on a test family is evidence against novelty, but not a universal no-go theorem. The candidate therefore returns to **CONDITIONAL / OPEN** as an orientation carrier.

Decision:
- q-layer detection: **PASS / LOCAL**;
- q-factorization on tested family: **PASS / LOCAL**;
- Bockstein orientation carrier: **CONDITIONAL / OPEN**;
- same-family numerical scans: STOP.

Next authorized attack: prove the structured-carrier classification/factorization universally, or produce an admissible same-carrier/different-orientation counterexample.


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


## AUTHORITATIVE UPDATE — HARD ATTACK 24 — 2026-09-20

Hard Attack 24 tightened the lower-3-central Kummer factorization proof and separated the complete finite Kummer carrier from the recognition problem.

For
\[
A_k=\mathbf Z/3^k,\quad U_k=1+3A_k,\quad H_k=A_k\rtimes U_k,
\]
a direct induction proves
\[
P_n(H_k)\subseteq 3^{n-1}A_k\rtimes(1+3^nA_k),
\]
hence
\[
P_{k+1}(H_k)=1.
\]
Therefore every candidate pair \((\rho,f)\), with \(\rho:G\to U_k\) and \(f\in Z^1(G,A_k(\rho))\), factors through \(Q_k=G/P_{k+1}(G)\).

This is now a clean **PASS / LOCAL** factorization theorem.

The correct complete finite bookkeeping object is
\[
\mathcal K_k(Q)=\coprod_{\rho\in\operatorname{Hom}(Q,U_k)} Z^1(Q,A_k(\rho)).
\]
The canonical-orientation problem is therefore a finite selection problem: one must construct a q-blind, functorial subobject/predicate selecting exactly \(\rho=\chi\bmod3^k\). The naive condition \(\exists f\) is vacuous because \(f=0\) always exists; \(\exists f\ne0\) is not known to be a unique orientation selector and risks merely restating duality if strengthened by known orientation data.

Decision:
- exact \(P_{k+1}(H_k)=1\): **PASS / LOCAL**;
- candidate Kummer factorization through \(G/P_{k+1}\): **PASS / LOCAL**;
- complete finite Kummer carrier \(\mathcal K_k\): **PASS / LOCAL** as the correct bookkeeping object;
- naive crossed-homomorphism existence selector: **FAIL / CLOSED**;
- canonical q-blind selector from \(Q_k\): **OPEN**;
- universal same-carrier/different-orientation no-go: **OPEN**.

Record: `research/KUMMER_RECOGNITION_LOWER_3_CENTRAL_HARD_ATTACK_24_2026-09-20.md`.

No further numerical scan is authorized until a concrete selector predicate or admissible counterexample construction is available.


## AUTHORITATIVE UPDATE — HARD ATTACK 25 — 2026-09-20 — NONZERO KUMMER COCYCLE SELECTOR CLOSED

The obvious repair of the vacuous crossed-homomorphism criterion was attacked structurally.

For a fixed candidate \(\rho:G\to U_k\), a crossed homomorphism on the rank-four free group is determined by four values in \(A_k\). Imposing the single Demuškin relator gives one additive obstruction
\[
\mathrm{Obs}_\rho:A_k^4\to A_k.
\]
Hence
\[
Z^1(G,A_k(\rho))=\ker(\mathrm{Obs}_\rho)
\]
has cardinality at least \(|A_k|^3\), for every candidate \(\rho\). In particular, nonzero crossed homomorphisms exist for every candidate action, not only for the canonical orientation.

Thus:
- \(\exists f\): **FAIL / CLOSED**;
- \(\exists f\ne0\): **FAIL / CLOSED** on the standard one-relator family;
- Boolean nonvanishing of \(H^1(G,A_k(\rho))\): **FAIL / CLOSED** as an orientation selector;
- richer twisted-cohomological interaction with additional finite group structure: **OPEN**.

The missing ingredient must therefore encode an interaction between the candidate coefficient action and additional intrinsic finite group/extension structure. Mere Kummer existence or nontriviality cannot provide the selector.

Record: `research/KUMMER_RECOGNITION_NONZERO_COCYCLE_HARD_ATTACK_25_2026-09-20.md`.


## METHODOLOGICAL UPDATE — 2026-09-20 — DISCOVERY/ATTACK DUAL TRACK

The recent Kummer branch exposed a process-level risk: repeated hard attacks are excellent for preventing false claims but can become locally exhaustive without generating the conceptual construction needed to reach the target.

Binding methodological correction:

1. **Attack track** remains mandatory for definition, naturality, q-blindness, separation, non-tautology, and proof verification.
2. **Discovery track** is now an equally explicit research phase. It is not a relaxation of rigor; it is where candidate mechanisms are generated before being attacked.
3. Every OPEN bottleneck must therefore be accompanied by a finite **idea search matrix**, not only another obstruction test.
4. Candidate mechanisms should be generated from the target's structural fingerprints:
   - orientation is a coefficient action / character;
   - mod-9 success required the degree-(2,3) relation jet;
   - lower-3-central depth compresses q-information dramatically;
   - Kummer data naturally couples a character with a twisted extension/cocycle;
   - the missing selector must therefore plausibly arise from an interaction between the finite quotient's extension structure and the candidate coefficient action.
5. Literature is to be mined by reusable mechanism, not by matching theorem names: object → input → invariance → obstruction → verification → logical boundary → possible factorization.
6. Before closing an OPEN branch, ask separately:
   **(a) What is false? (b) What structure is missing? (c) What known mathematical mechanism produces exactly that structure?**
7. The next Kummer phase should therefore not be “more Kummer variants” blindly. It should run a structured discovery pass over candidate mechanisms such as twisted extension classes, transgression/fundamental-class pairings, Bockstein–Kummer compatibility, duality-type pairings, and finite nilpotent/central extensions, then submit each candidate to the existing hard gates.

This is a process correction, not a mathematical result. It does not weaken any PASS/FAIL classification.


## 2026-09-20 — HARD ATTACK 27: FINITE EXTENSION CARRIER DEFINITION AND SUFFICIENCY BOUNDARY

After Hard Attack 26, the vague extension/2-cell candidate was made precise. With N=P_{k+1}(G), define M_k=N/(N^{3^k}[N,N]) and E_k=G/(N^{3^k}[N,N]); the subgroup is characteristic, N is open/finitely generated, and the resulting extension is finite. This is an intrinsic q-blind candidate J_k^ext=(Q_k,M_k,E_k), and H^1(N,A_k(rho)) is determined by M_k for every candidate rho.

The hard attack then checked sufficiency rather than assuming it. The Hochschild-Serre total-degree-two structure contains H^0(Q_k,H^2(N,A_k(rho))), so the finite relation-module extension does not automatically determine H^2(G,A_k(rho)). Adding H^2(N,A_k(rho)) directly risks importing the Demushkin duality/orientation object and is therefore circular unless independently reconstructed from filtered extension data.

Classification: definition PASS / LOCAL; automatic H^2 reconstruction FAIL / CLOSED as an inference; universal carrier OPEN; genuine finite 2-cell obstruction OPEN. No numerical scan authorized.

Detailed record: research/KUMMER_FINITE_EXTENSION_CARRIER_HARD_ATTACK_27_2026-09-20.md


## 2026-09-20 — HARD ATTACK 28: CANONICAL FINITE 2-CELL EXTENSION CLASS

The extension branch was sharpened from a finite quotient to its canonical extension class e_k in H^2(Q_k,M_k). This yields a functorial finite transgression map for every candidate twisted coefficient action. The attack found the next logical boundary: e_k alone has no distinguished four-generator/2-cell evaluation, so it does not automatically reproduce the standard twisted obstruction row. Adding a fundamental/duality class directly risks circularly importing orientation.

Classification: e_k PASS / LOCAL; transgression PASS / LOCAL; automatic row recovery FAIL / CLOSED as an inference; zero-map selector FAIL / CLOSED; nonzero selector OPEN; intrinsic reconstruction of the missing 2-cell evaluation OPEN / decisive. No numerical scan authorized.

Detailed record: research/KUMMER_2CELL_OBSTRUCTION_HARD_ATTACK_28_2026-09-20.md


## 2026-09-20 — HARD ATTACK 29: PD2 TOP-CLASS RIGIDIFIER

The obvious way to supply the missing 2-cell evaluation—adjoining H^2(P_{k+1}(G),F_3) or its Z/3^k lift—was attacked. Its quotient action is already the orientation-bearing duality action, so it is not an independently derived filtered carrier. This closes the direct top-class enrichment as a non-tautological solution, while leaving open a genuinely derived finite chain-level obstruction T_k.

Classification: direct top-class enrichment FAIL / CLOSED for the stated objective; independent T_k OPEN / decisive. No further oriented-cohomology enrichment authorized.


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


## 2026-09-20 — DEFERRED RESEARCH IDEAS RECORDED AFTER COKER BREAKTHROUGH

Following the review of the new proposal set, promising but non-immediate directions were preserved in `research/NEXT_RESEARCH_IDEA_BACKLOG_2026-09-20.md`.

The recorded candidates are:
- compare one-relator finite Fox relation residue against the intrinsic finite extension class/transgression, first determining whether the Fox residue adds information or is only a coordinate realization;
- elevate the finite Kummer result to a unique-selector theorem, with canonical chi recovered as a corollary;
- treat coker cardinality as a maximality-selector reformulation;
- defer mixed m-adic/bi-filtered constructions until precise intrinsicity and relator-gauge naturality are established;
- develop filtration-dependent information-transfer efficiency as a higher-level synthesis;
- postpone P_{k+1} minimality until the admissible carrier category and inverse-limit theorem are settled.

These are **OPEN / DEFERRED**, not closed. The active main line remains finite-coker strengthening followed by a hard attack on (k\to k+1) compatibility/naturality. No deferred branch is to be resurrected without a new structural reason or comparison map.


## 2026-09-20 — HARD ATTACK 35: INVERSE-SYSTEM COMPATIBILITY AUDIT

The next attack separated carrier-level naturality from output compatibility.

For Q_{k+1}->Q_k and E_{k+1}->E_k, the relation modules nevertheless change kernels:
M_{k+1} is built from P_{k+2}, whereas M_k is built from P_{k+1}. The natural inclusion-induced map lands only in a generally proper submodule of M_k. Consequently no automatic map of Hom sources, transgressions, or coker carriers exists. Direct strict inverse-system structure of the raw coker carriers is therefore FAIL / CLOSED as an inference.

A weaker and sufficient statement survives: if rho_{k+1} is the unique level-(k+1) coker selector, then its reduction is the unique level-k selector. The PD² duality criterion identifies maximal top-cohomology size with triviality of chi*rho^{-1}; triviality modulo 3^{k+1} implies triviality modulo 3^k. Hence selected outputs form a compatible family.

Classification:
- carrier-level direct reduction: FAIL / CLOSED as an inference;
- carrier tower naturality: OPEN / load-bearing;
- selector compatibility: PASS / LOCAL under PD² verification;
- practical inverse-limit reconstruction: PASS / LOCAL subject to the declared PD² framework;
- carrier-only inverse-system functoriality: OPEN.

Record: research/KUMMER_HARD_ATTACK_35_INVERSE_SYSTEM_COMPATIBILITY_AUDIT_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 36: SELECTOR-ONLY COHERENCE

Hard Attack 36 asked whether the practical inverse-limit reconstruction requires the raw coker carriers to form an inverse system. It does not.

Define S_k(G) by the finite coker maximality predicate. The finite recognition theorem identifies S_k(G) with the singleton {chi mod 3^k}. Reduction of candidate characters therefore restricts to compatible maps between the singleton selector sets. Thus the inverse-limit selector set is a singleton, giving chi_filt.

This is PASS / LOCAL under the PD² framework. It is a recognition/coherence theorem, not a carrier-only naturality theorem. Raw carrier tower functoriality remains OPEN; so do minimality and universal category-independent claims.

The practical endpoint of the current main branch is therefore:
finite intrinsic carrier -> transgression coker -> unique finite selector -> selector coherence -> chi_filt.

Do not force strict carrier-level inverse maps without a new structural reason.
Record: research/KUMMER_HARD_ATTACK_36_SELECTOR_COHERENCE_ENDGAME_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 37
PD²-independent selector uniqueness was attacked. No valid finite-input reconstruction theorem and no admissible no-go were obtained. Status remains OPEN. The coker selector and selector coherence remain PASS / LOCAL only under the PD² framework. Direct reuse of the known one-relator/Fox obstruction row as an intrinsic proof shortcut is FAIL / CLOSED. The exact load-bearing target is an intrinsic evaluation of the finite extension's 2-cell transgression from (Q_k,M_k,E_k,rho). Detailed record: `research/KUMMER_HARD_ATTACK_37_PD2_INDEPENDENT_SELECTOR_2026-09-20.md`.

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


## 2026-09-20 — HARD ATTACK 39: YONEDA / RESTRICTED COEFFICIENT-PROFILE COMPLETENESS

Hard Attack 39 attacked the proposed equivalence between the extension class e_k and its transgression profile.

For the full category of Q_k-modules, define T_e(A)(phi)=phi_*(e). The profile recovers e by taking A=M_k and phi=id_{M_k}; conversely e determines the entire profile. Hence full coefficient-category completeness is PASS / CLOSED, but only at a Yoneda-level information-theoretic level.

For the actual Kummer family A_k(rho)=Z/3^k, define the restricted observation map Phi_k(e)=(phi_*(e))_{rho,phi} with kernel K_k=intersection ker(phi_*). The restricted family is information-complete iff K_k=0. No faithfulness theorem is available, and the full Yoneda argument does not establish it.

The selector is weaker than full e_k-recovery: it only requires the finite observation function rho -> |coker[Hom_Q(M_k,A_k(rho)) -> H^2(Q_k,A_k(rho))]| for the specific Demushkin e_k to have a unique maximizer, equal to the canonical orientation residue. This remains OPEN / DECISIVE without PD².

Coordinate comparison with the Fox row is now legitimate only as a secondary computation: one must construct a cocycle for e_k, push it out along phi, and identify the resulting H^2 class with the Fox/crossed-word obstruction, including section/presentation independence.

Classification:
- full coefficient-category profile completeness: PASS / CLOSED (Yoneda-complete, not a selector theorem);
- restricted Kummer profile completeness: OPEN;
- restricted profile -> unique orientation without PD²: OPEN / DECISIVE;
- Fox row as coordinate realization: OPEN;
- PD²-based finite selector: PASS / LOCAL;
- carrier minimality: OPEN;
- strict carrier-tower naturality: OPEN.

Record: research/KUMMER_HARD_ATTACK_39_YONEDA_COEFFICIENT_PROFILE_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 40: RANK-ONE COEFFICIENT / SPECTRAL-BLINDNESS AUDIT

Hard Attack 40 identifies the exact representation-theoretic content of the restricted Kummer profile. For A_k(rho)=Z/3^k, every equivariant phi:M_k->A_k(rho) satisfies phi(gm)=rho(g)phi(m), so phi factors through the twisted scalar specialization M_{k,rho}=M_k/<gm-rho(g)m>. Therefore the push-forward/coker profile of e_k is a scalar-character spectroscopy of the extension class.

This yields a structural factorization **PASS / CLOSED**, but not a generic no-go: K_k may or may not be nonzero on the actual Demushkin e_k. A proof of non-faithfulness would require an explicit invisible class or a theorem about the representation structure of e_k.

The remaining selector theorem is that rho -> |coker[Hom_{Z/3^k}(M_{k,rho},A_k(rho)) -> H^2(Q_k,A_k(rho))]| must have a unique maximizer at chi mod 3^k, without PD².

Classification: scalar-character factorization **PASS / CLOSED**; faithfulness on e_k **OPEN / DECISIVE**; unique scalar-character maximizer without PD² **OPEN / DECISIVE**; Fox row as coordinate realization **OPEN**; PD²-based selector **PASS / LOCAL**; carrier minimality and strict tower naturality **OPEN**.

Record: research/KUMMER_HARD_ATTACK_40_RANK_ONE_SPECTRAL_BLINDNESS_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 40 CRITICAL REVIEW / REVISED GATE

The self-critique of Hard Attack 40 was audited against the authoritative research state.

Accepted corrections:
- A_k(rho)=Z/3^k is rank-one, but M_{k,rho} need not be one-dimensional. The safe terminology is rank-one coefficient / scalar-character specialization.
- Hom_{Q_k}(M_k,A_k(rho)) ≅ Hom_{Z/3^k}(M_{k,rho},Z/3^k) is a formal twisted-coinvariant reformulation, not a new obstruction theorem.
- K_k=0 is auxiliary, not the decisive selector criterion. The decisive PD^2-independent target remains the unique maximizer of rho |-> |C_k(rho)|.
- PD^2-based finite selection remains PASS / LOCAL; its removal is a separate theorem problem.

Critical correction to a proposed new interpretation:
calling maximal coker "complete filling" of H^2 is backwards. Since C_k(rho)=H^2/im(delta), larger coker means smaller transgression image when the ambient group is fixed; equality |C_k|=|H^2| means im(delta)=0. Therefore the useful qualitative notions are transgression invisibility, defect maximality, or vanishing, not filling.

Additional audit:
- "response curve/spectroscopy" is heuristic language until a precise invariant is defined.
- the twisted coinvariant is safely described as a scalar specialization; no unproved induced/coinduced analogy is to be used.
- Fitting/determinant machinery is only a candidate. It is initially a repackaging of a cokernel unless it yields a new basis-independent rho-dependent theorem.
- information-theoretic analogies do not constitute novelty.

Revised active gate:
(A) prove a scalar-visibility/vanishing theorem for the specific Demushkin extension push-forward delta_{k,rho};
(B) at k=2, compare delta_{2,rho} intrinsically with the already closed cup+Bockstein / degree-(2,3) obstruction;
(C) if ambient H^2 size remains uncontrolled, stop and record the exact PD^2 boundary rather than claiming selector uniqueness.

Classification:
- Hard Attack 40 scalar-character factorization: PASS / CLOSED.
- Hard Attack 40 as a new obstruction theorem: HISTORICAL / SUPERSEDED; reformulation only.
- restricted Kummer faithfulness K_k=0: OPEN / AUXILIARY.
- scalar-character visibility of e_k: OPEN / DECISIVE.
- unique coker maximality without PD^2: OPEN / DECISIVE.
- Fox row as coordinate realization: OPEN.
- Fitting/determinant: OPEN / DEFERRED pending non-tautology.
- PD^2 finite selector: PASS / LOCAL.
- carrier minimality: OPEN.
- strict tower naturality: OPEN.

Detailed record: research/HARD_ATTACK_40_CRITICAL_REVIEW_AND_NEXT_GATE_2026-09-20.md.


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
