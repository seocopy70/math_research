## 2026-09-20 — HA61-B5-12: CANONICAL t2 NO-GO

A same-group relator-conjugation witness now kills the proposed single presentation-independent vector t2. For q=3, p!=0 and lambda=e2*, while the audited conjugation law shifts the coordinate residual by lambda(v)p. Choosing v with lambda(v)=1 changes t2 by p, although all intrinsic input data and the exact connecting-obstruction family remain unchanged. Thus raw t2 is not an intrinsic natural transformation. The quotient t2/<p> is invariant but insufficient because f(t2) does not descend: primary-zero gives f(p)+(lambda wedge f)(R)=0, not f(p)=0. The diagonal (t2,mu) quotient was already rejected because it identifies distinct coefficient actions. Therefore the single-vector P4/t2 compression route is FAIL/CLOSED. The intrinsic delta3 family remains PASS/CLOSED; alternative richer secondary compression is OPEN/DECISIVE; HA61-C via t2 is not opened.

Record: research/HA61_B5_12_NO_GO_CANONICAL_T2_2026-09-20.md

## 2026-09-20 — HA61-B5-10: INTRINSIC SECONDARY FAMILY + PURE-CONJUGATION CANCELLATION

The intrinsic secondary object is now the function-valued family of connecting maps indexed by coefficient characters rho_3 lifting rho_2. It is presentation/lift natural by construction. The previously proposed diagonal quotient (t_2,mu)/F_3(p,lambda) is ruled out as an orientation carrier because pure relator conjugation fixes intrinsic rho_3/mu, and quotienting mu would identify distinct candidate next-digit coefficient actions. Exact crossed-word algebra for r' = v r v^{-1} gives complete cancellation, so the isolated [v,R] term cannot by itself define a gauge shift of t_2.

Decision: intrinsic secondary family PASS/CLOSED; pure conjugation invariance PASS/CLOSED; diagonal affine quotient FAIL/CLOSED; P_4 residual -> intrinsic t_2 OPEN/LOAD-BEARING; E_{>P_4} factorization OPEN/LOAD-BEARING; HA61-B OPEN/LOAD-BEARING; HA61-C not opened.

Record: research/HA61_B5_10_INTRINSIC_SECONDARY_FAMILY_AND_CONJUGATION_2026-09-20.md

## 2026-09-20 — HA61-B5-3: COMBINED AFFINE SECONDARY QUOTIENT

B5-2 was sharpened to an explicit affine action. On the primary-zero locus, the gauge shift (t_2mapsto t_2+a p) is exactly compensated by (mumapstomu+alambda), because (f(p)=-(lambdawedge f)(R)). Thus the natural secondary object is the quotient/torsor ([(t_2,mu)]in(V^{(2)}oplus V^*)/mathbf F_3(p,lambda)) when (lambda
e0); for (lambda=0) this affine ambiguity disappears.

Decision: combined affine action PASS / LOCAL; raw (t_2) intrinsicity FAIL / CLOSED; no independent cubic-bracket functional PASS / LOCAL; universal affine carrier OPEN / LOAD-BEARING; deeper-than-(P_4) factorization OPEN / LOAD-BEARING; HA61-B OPEN / LOAD-BEARING; HA61-C not opened.

Record: research/HARD_ATTACK_61_B5_3_COMBINED_AFFINE_SECONDARY_QUOTIENT_2026-09-20.md.



## 2026-09-20 — HARD ATTACK 54: PERMANENT 19-DIMENSIONAL QUOTIENT IS NOW FIXED

HA53 was critically reviewed against HA52. The generic cyclic-kernel d3/Bockstein phenomenon cited in HA52 cannot affect the specific LHS bidegree (2,1): all r>=3 outgoing targets have negative fiber degree, and all incoming sources have negative base degree. Therefore E_3^{2,1}=E_infinity^{2,1} and the 19-dimensional sector is permanent.

The authoritative object is now the quotient
S = ker(H^2(V,F_3) tensor K -> H^4(V,F_3)) / im(d2:H^2(W,F_3)->H^2(V,F_3) tensor W^*),
with dim S=19 and K=im(d2:W^*->H^2(V,F_3)), dim K=9.

This is a genuine associated-graded filtration piece of H^3(Q_2,F_3). It is not yet an orientation carrier, and no decomposition is inferred from the dimension 19.

Decision: permanent 19D LHS piece PASS / CLOSED; HA52 d3 warning HISTORICAL / SUPERSEDED; H-module structure OPEN / LOAD-BEARING; twisted beta_rho^2 action OPEN / LOAD-BEARING; orientation-selector interpretation OPEN / DECISIVE.

Record: research/KUMMER_HARD_ATTACK_54_CRITICAL_CORRECTION_AND_19_QUOTIENT_2026-09-20.md
## 2026-09-20 — ACTIVE KUMMER BOTTLENECK AFTER HARD ATTACK 26

The automatic implication
P_{k+1}(A_k⋊U_k)=1 => H^2(G,A_k(rho)) factors through Q_k=G/P_{k+1}
is closed. The missing information is the extension/2-cell data of the discarded deep kernel. The next principal candidate is therefore a finite extension-obstruction carrier (Q_k,E_k), not the bare quotient alone.

## 2026-09-20 — NEXT KUMMER BOTTLENECK: TWISTED TOP-COHOMOLOGY RECOGNITION

Discovery Pass 1 identified the first concrete selector mechanism beyond shallow cocycle existence/nonvanishing:
candidate rho + twisted top-degree obstruction / Kummer lifting.

On the standard rank-4 family, the finite twisted obstruction row vanishes uniquely at rho=chi mod 3^k. The next gate is not another numerical scan: determine whether this obstruction can be reconstructed functorially from Q_k=G/P_{k+1}, with presentation/relator-gauge independence and without importing the canonical dualizing action.



## 2026-09-20 — LOWER 3-CENTRAL LINEAR INFORMATION BOUNDARY

The program now records a parallel lower-3-central comparison. The standard family has sharp thresholds G_{3^s}/D_N ≅ G_∞/D_N iff N≤3^s and G_{3^s}/P_n ≅ G_∞/P_n iff n≤s+1. This supports a linear-vs-exponential information-scale comparison, not yet an orientation-carrier theorem. The next step is a single finite-recognition theorem attempt on G/P_{k+1}, without opening additional gates.
## AUTHORITATIVE UPDATE — 2026-09-20 — CRITICAL CORRECTION: ZASSENHAUSZ THRESHOLD + MIXED m-ADIC REOPENING

The earlier review has been corrected at one precise point: the threshold argument concerns
[
(G/D_N(G))^{ab},
]
not an identification (G/D_N(G)=G^{ab}/3^{s+1}). Using Jennings' formula, the abelianized finite quotients separate (G_{3^s}) from the power-free control at (N=3^s+1), while for (Nle3^s) the relation (x_1^{3^s}) lies in (D_N(F)), so
[
G_{3^s}/D_Ncong G_infty/D_N.
]
Hence (D_{3^{n-1}+1}) versus (D_{3^{n-1}}) gives a **PASS / LOCAL** sharp information boundary for (chimod3^n) on the standard Demushkin family, with explicit classification dependence and without claiming a pointed natural carrier theorem.

Separately, HARD ATTACK 10 remains correctly closed only for ordinary presentation-independent degree-(le3) Fox truncation. A mixed ((3,I))-adic finite carrier
[
J_n^{mix}=I_{mathrm{Fox}}+mathfrak m^n,qquad mathfrak m=(3,I),
]
is re-opened as an admissible candidate. The existence gate now permits Fox-derived finite constructions; compression/non-tautology is a separate later gate. The first load-bearing task is the precise definition and relator-gauge/naturality proof.

Record: `research/CRITICAL_CORRECTION_MIXED_MADIC_AND_ZASSENHAUSZ_THRESHOLD_2026-09-20.md`

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 16: MOD-27 BOCKSTEIN-EXTENSION CARRIER

A first serious intrinsic mod-27 candidate now survives the definition gate:
\[
\mathcal B_{27}=(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9).
\]
It uses only functorial coefficient-extension/cohomological data, contains the established mod-9 carrier, and is independent of Fox coordinates.

The correct additive orientation target is \(\lambda_{27}=\frac13\log\chi\pmod9\), not \((\chi-1)/3\). On the standard family the two Bockstein layers give \(e_2\) for q=3, \(3e_2\) for q=9, and 0 for q divisible by 27, yielding the correct residues 13, 10, 1 mod 27.

The candidate remains OPEN because the orientation bridge must still be proved naturally, independently of the standard presentation and without inserting q or the known orientation formula.

Decision: **MOD-27 BOCKSTEIN-EXTENSION CARRIER: OPEN / STRONG CANDIDATE.**

Record: research/MOD27_BOCKSTEIN_EXTENSION_CARRIER_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 15: MOD-27 CATEGORY ADEQUACY

A category-level loophole was closed before any higher mod-27 computation. If unrestricted full-group constructions are admitted, the dualizing module/action already contains the canonical orientation, and the Demuškin classification supplies q as an intrinsic invariant from which the standard orientation formula recovers chi. That is a known group-intrinsic reconstruction, not the intended filtered-carrier result.

The PRE-MOD27 gate is therefore sharpened: q-blindness excludes first extracting q, the dualizing action, or an equivalent complete classification invariant and repackaging it. A genuine J_27 must be built directly from the declared filtered/relation-information input and must not factor through a pre-existing canonical-orientation object without an independent obstruction construction.

Decision:
- unrestricted group-only J_27 as a new carrier: **HISTORICAL / SUPERSEDED**;
- category-adequacy correction: **PASS / CLOSED**;
- genuine filtered/relation J_27: **OPEN**.

Record: research/MOD27_CATEGORY_ADEQUACY_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 14: FOX LOCAL QUOTIENT MINIMALITY

A second structural boundary is now closed. In the frozen (q=3) model, the exact local Fox obstruction algebra is
[
mathbf Z_3[[u_1,u_2,u_3,u_4]]/(u_1,u_3,u_4,2u_2+3)congmathbf Z_3.
]
Hence the local exact Fox scheme is already a reduced characteristic-zero point. No proper unital quotient can preserve the full (3)-adic point: finite-characteristic quotients lose higher digits, while the zero quotient loses the point.

Therefore there is no nontrivial quotient-based compression of the local Fox carrier preserving the full orientation.

Decision:
- quotient-of-local-Fox-scheme compression: **FAIL / CLOSED**;
- exact local Fox carrier minimal under full-(3)-adic-preserving quotients: **PASS / CLOSED**;
- independent intrinsic non-quotient exact compression: **OPEN**.

Record:
research/ORIENTATION_FOX_LOCAL_QUOTIENT_MINIMALITY_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 13: FULL ASSOCIATED-GRADED NO-GO / EXTENSION LOWER BOUND

A literature-backed structural strengthening has been established. For infinite Demuškin pro-(3) groups of fixed rank, the full graded group algebra associated to the complete (3)-Zassenhaus filtration is the quadratic/PBW Demuškin graded algebra determined by the quadratic symplectic relation, independently of the Demuškin (q)-invariant. Hence the full mod-3 associated-graded object is (q)-blind, not merely every bounded graded window.

Therefore, in the rank-four family (G_{3^s}) and (G_infty), the full mod-3 associated-graded object cannot recover (q), and hence cannot recover the canonical (mathbf Z_3^	imes)-valued orientation (chi), even though
[
chi_{3^s}(x_2)=(1-3^s)^{-1},qquad chi_infty(x_2)=1.
]

This yields a genuine lower bound: any successful carrier must contain information not present in the full mod-3 graded object. At mod 9 the projective degree-3 power component (P_3) coupled to (R_2) is a sufficient first extension datum.

The lower bound is not an absolute category-independent minimality theorem. Also, the infinitely many higher (3)-adic digits need not correspond to infinitely many independent extension classes: for fixed (q=3), the exact relation (1+2B=0) compresses all digits into one exact characteristic-zero coefficient equation.

Decision:
- full mod-3 associated graded (Rightarrow q,chi): **FAIL / CLOSED**;
- first non-graded extension datum for mod-9 recovery: **PASS / LOCAL**;
- intrinsic exact intermediate compression below universal Fox: **OPEN**.

Detailed audit:
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

## AUTHORITATIVE UPDATE — 2026-09-20 — INTEGRAL AUGMENTATION JET DEFINITION GATE CLOSED

The proposed next branch \(\langle r-1\rangle\subset I^2/I^4\) over ordinary \(\mathbf Z_3[[F]]\) has been falsified at the definition level:
\[
x_1^3-1=3X_1+3X_1^2+X_1^3
\]
implies
\[
r-1=3X_1+R+O(I^3),
\qquad
R=[X_1,X_2]+[X_3,X_4],
\]
so \(r-1\notin I^2\).

Decision: **FAIL / CLOSED** for the plain integral augmentation carrier.

This sharpens the exact-carrier boundary: the mod-3 Zassenhaus jet is genuinely characteristic-3, while exact \(\mathbf Z_3\)-coefficient recovery lives naturally in the Fox/crossed-derivation side or requires a new mixed filtered construction. A mixed p-adic/Zassenhaus weighted filtration is the only remaining nearby filtered direction, but its finite graded pieces do not automatically contain the full 3-adic digits.

Next authorized structural target:
\[
\text{intrinsic filtered tower}
\to
\text{exact Fox orientation locus},
\]
with the source of the infinitely many 3-adic digits explicitly identified.

Record:
research/ORIENTATION_INTEGRAL_AUGMENTATION_JET_HARD_ATTACK_2026-09-20.md

## AUTHORITATIVE UPDATE — 2026-09-19 — TWISTED DEGREE-(2,3) LIFTING-OBSTRUCTION THEOREM CLOSED

The previously open twisted degree-(2,3) structural bridge is now closed at the first mod-9 level.

A proof-level calculation establishes:
[
delta_
ho(f)=igl[f(p(P))+(lambdawedge f)(R)igr]omega
]
for a minimal one-relator pro-3 presentation with relation jet (r=(R,P)+O(D_4)), where (
ho=1+3lambdapmod9).

The proof has four load-bearing parts:
1. the coefficient exact sequence (0	o3A_2	o A_2	o A_1	o0) identifies the cohomological lifting obstruction;
2. the exact crossed-word formula modulo 9 shows the twisted deformation term sees only degree 2;
3. the Zassenhaus formula (D_4=prod_{3^jige4}gamma_i^{3^j}) shows the divided trivial-action term is unchanged modulo 3 by a (D_4)-error;
4. the degree-one evaluation kills the bracket component of (P), leaving only (p(P)in V^{(1)}).

Presentation/gauge naturality is then obtained intrinsically from the connecting maps (delta_
ho): the family in ((lambda,f)) is presentation-independent, and the map ((R,p)mapsto[f(p)+(lambdawedge f)(R)]) is injective. Thus the projective carrier ([(R,p)]) is forced by the intrinsic first twisted obstruction family, without selecting a preferred IA lift.

For the frozen relation (x_1^3[x_1,x_2][x_3,x_4]), this gives uniquely
[
chimod9=(1,4,1,1).
]

Decision:
- twisted cohomological obstruction: **PASS / CLOSED**;
- degree-(2,3) truncation: **PASS / CLOSED**;
- bracket-part elimination (Pmapsto p(P)): **PASS / CLOSED**;
- projective presentation/gauge naturality at mod-9 level: **PASS / CLOSED**;
- recovery (chimod9): **PASS / CLOSED**;
- bare graded (Rightarrow) carrier: **OPEN**;
- higher 3-adic digits: **OPEN / separate program**.

Detailed proof:
`research/TWISTED_DEGREE3_LIFTING_OBSTRUCTION_THEOREM_2026-09-19.md`.

No broad scan is authorized.

## AUTHORITATIVE UPDATE — 2026-09-19 — BOCKSTEIN–RELATION-JET IDENTIFICATION GATE CLOSED

A critical audit tightened the load-bearing identification
\\[
\\beta\\longleftrightarrow p(P_3)
\\]
The previous wording “direct cochain/transgression calculation proves the identification” was too strong. The defensible statement is:

- the **standard one-relator transgression/relation–Bockstein formula** gives the general identification of the Bockstein with the restricted p-power coefficient vector, up to the convention-dependent global sign/unit of the chosen H² generator;
- for the frozen relator, this is **independently checked by a direct \\(\\mathbf Z/9\\)-lifting obstruction calculation**;
- the cup-product and Bockstein signs must be synchronized in the **same transgression/fundamental-class convention**. In that convention both carry the same global sign, so
\\[
\\operatorname{tr}(\\chi_i\\cup\\chi_j)=-a_{ij},
\\qquad
\\operatorname{tr}(\\beta\\chi_i)=-a_i,
\\]
rather than treating the Bockstein sign as an independent projective gauge.

For the frozen relator
\\[
r_3=x_1^3[x_1,x_2][x_3,x_4],
\\]
the direct lift gives
\\[
\\frac{\\widetilde f_1(r_3)}3\\equiv1\\pmod3,
\\qquad
\\frac{\\widetilde f_i(r_3)}3\\equiv0\\pmod3\\ (i=2,3,4),
\\]
because the commutator factors have zero exponent sum. Hence the Bockstein power vector is \\(p\\sim X_1^{(1)}\\), independently checking the standard formula in this presentation.

The restricted-cube coefficient naturally lies in \\(V^{(1)}\\); over \\(\\mathbf F_3\\), Frobenius is the identity, so \\(V^{(1)}\\cong V\\) canonically for the present calculation.

For the control relation, do not use “q=∞” as a literal group parameter in the final manuscript: the precise object is the **power-free control**
\\[
r_0=[x_1,x_2][x_3,x_4],
\\]
for which the first Bockstein/power component is zero. Thus \\((R,p)=(R,0)\\), distinct from the q=3 carrier.

With
\\[
R=[X_1,X_2]+[X_3,X_4],\\qquad p=X_1^{(1)},
\\]
the already audited recovery functional has unique zero \\(\\lambda=e_2^*\\), yielding
\\[
\\chi\\bmod9=(1,4,1,1).
\\]

Decision:
- intrinsic cup+Bockstein projective carrier: **PASS / CLOSED**;
- \\(\\beta\\leftrightarrow p(P_3)\\): **PASS / CLOSED**, under the standard one-relator transgression/Bockstein formula, with the common sign convention explicitly synchronized and independently checked for the frozen relator;
- absolute H² normalization: **CONDITIONAL / gauge-dependent**;
- projective carrier → \\(\\chi\\bmod9\\): **PASS / CLOSED** at the stated degree-(2,3) level;
- higher 3-adic digits and equality with the Pál–Quick A3/Hochschild invariant remain outside this Gate;
- no broad scan authorized.

Record: research/BOCKSTEIN_RELATION_JET_IDENTIFICATION_AUDIT_2026-09-19.md
## AUTHORITATIVE UPDATE — 2026-09-19 — M3 LITERATURE COMPARISON BOUNDARY

The intrinsic cup+Bockstein carrier has now been compared structurally with Pál–Quick's A_3/Hochschild canonical class.

Result:
- **PASS / LOCAL:** both detect the q=3 first power layer in the standard p=3 Demushkin family: nonzero first Bockstein / nonzero A_3 class at q=3, versus vanishing first Bockstein / vanishing A_3 obstruction for q=3^f, f≥2;
- **OPEN:** no natural factorization from the projective carrier [(R,p)] to the full Hochschild canonical class has been constructed;
- **STOP:** no U_4/Hochschild scan is justified before a target map is defined.

This strengthens the methodological position: the current carrier has an independent literature-level detection cross-check, but equality with the Pál–Quick invariant is not claimed.

Record:
research/M3_CUP_BOCKSTEIN_TO_PAL_QUICK_COMPARISON_AUDIT_2026-09-19.md

## AUTHORITATIVE UPDATE — 2026-09-19 — MOD-9 INTRINSIC CARRIER IDENTIFIED

The μ–χ bridge is narrowed, not fully identified: μ is an intrinsic mod-3 automorphism/duality-line shadow, μ alone cannot recover χ mod 9, and a μ-alone homomorphic lift to 1+3Z_3 is impossible. Additional-data relations remain open, with μ-only scans stopped.

The standalone Bockstein route is closed, but the combined intrinsic pair
\[
(\text{cup product},\beta)
\]
now supplies the missing mod-9 carrier.

With V=H^1(G,F_3)^* and dim H^2=1, temporarily choose ω∈H^2\setminus{0} and write
\[
f\smile g=(f\wedge g)(R)\omega,
\qquad
\beta(f)=f(p)\omega.
\]
Changing ω rescales R and p by the same inverse unit, so
\[
\boxed{\overline J_3(G)=[(R,p)]}
\]
is intrinsic. This agrees with the coarsest filtered degree-(2,3) relation carrier: R is the quadratic relation and p is the restricted-cubic/power component.

The resulting natural functional
\[
\overline\Theta(\lambda)(f)=f(p)+(\lambda\wedge f)(R)
\]
has unique zero λ=e_2^* for q=3 and λ=0 for q=∞. Hence it recovers χ mod 9 and separates the two cases without inserting q.

Decision:
- standalone Bockstein: FAIL/CLOSED;
- cup + Bockstein intrinsic carrier: PASS/CLOSED at mod-9 level, under the stated standard transgression/Bockstein identification;
- M1 intrinsic carrier functor: PASS/CLOSED at mod-9 level, under the standard transgression/Bockstein identification, under the stated standard transgression/Bockstein identification;
- M2 mod-9 orientation factorization: PASS/CLOSED at the stated degree-(2,3) level;
- next authorized structural target: M3 comparison/obstruction relative to the Pál–Quick A3/Hochschild canonical class.

Record:
research/ORIENTATION_MOD9_INTRINSIC_CUP_BOCKSTEIN_CARRIER_2026-09-19.md

No broad scan is authorized.
 
## AUTHORITATIVE UPDATE — 2026-09-19 — EXACT CARRIER BRANCH CLOSED AT STRUCTURAL BOUNDARY

The exact q=3 branch is now separated into:
1. exact filtered relation/evaluation carrier -> full \\(\\chi\\): PASS/CLOSED;
2. mod-3 compressed relation carrier -> \\(\\chi\\bmod9\\): PASS/CLOSED, with coarsest quotient \\(([R],p(P))\\) in the defined linear-evaluation category;
3. exact characteristic-zero concrete compression analogous to \\(([R],p(P))\\): NOT PROVED;
4. naive Z_3 restricted-Lie scalar extension: FAIL/CLOSED.

The canonical exact evaluation quotient is valid only as the coarsest quotient for the independently prescribed coefficient-evaluation family; treating it as “whatever is needed to recover chi” would be tautological.

No further computational scan is authorized for this branch. Any continuation requires a new structural theorem/invariant.

## 0C.2. EXACT Z_3 DEGREE-3 FULL-CHI CLOSURE — 2026-09-19

For the fixed q=3 normal form, the projective degree-(2,3) relation jet can be retained over exact Z_3-coefficients. The exact crossed-derivation equations are
[

ho(x_1)=
ho(x_3)=
ho(x_4)=1,qquad 1+2
ho(x_2)=0,
]
so one bounded-degree exact filtered carrier determines
[
chi(x_2)=-1/2=(1-3)^{-1}inmathbf Z_3^	imes.
]

The degree-<=3 presentation/gauge change has
[
(R,P)mapsto(uR,uP+[v,R]),
]
and the recovery zero set is unchanged because degree-one functionals kill [v,R].

Record: research/ORIENTATION_EXACT_PROJECTIVE_DEGREE3_FULL_CHI_CLOSURE_2026-09-19.md

Boundary: this is fixed q=3 and exact filtered data. It is not a universal bounded-degree theorem over q=3^s, and it is not the bare F_3 associated graded object.

# Research Map — Rank-4 pro-3 Demuškin Group / Intrinsic Orientation Recovery

> **Purpose:** Current state/map document. Read this first in a new session. Chronology belongs in `research/00_RESEARCH_LOG.md`.

## 0. One-sentence research question

\[
\boxed{\text{Can the canonical orientation character }\chi:G\to\mathbb Z_3^\times\text{ be recovered intrinsically from filtered/graded data?}}
\]

The strategy is to determine whether intrinsic filtration information survives in a symmetry-compatible structure strongly enough to distinguish the relevant cases and eventually recover \(\chi\).

---

## 0A. CANONICAL CURRENT STATUS — 2026-09-19

**This block is authoritative for new-session restoration. Later sections are historical chronology; stale OPEN/PENDING labels below do not override this block.**

### Latest conclusion
The structured quotient defect Delta_q(g) = [F_g(X1^3)-X1^3]_3 is algebraically the coboundary g.(X1^3)-X1^3.

The script now checks this identity independently for all 9 structured representatives. CI run 35420266538, commit bd53311cf45dfc930599c3c24b60df8572c155cc, job 105836490226: SUCCESS.

Therefore the previously verified cocycle law is an automatic coboundary identity. The structured-family and implementation PASS results are retained as implementation/convention verification only. They are not evidence for a new q-sensitive invariant or nontrivial H1 class.

### Decision
Delta_q coboundary track: CLOSED / NO NEW INFORMATION.

The proposed broader rank-4 scan for this same cocycle is CANCELLED.

### Current authorized gates
1. Non-coboundary q-sensitive datum definition gate: define an object without pre-inserting q=3 versus q=infinity, prove lift/IA and coordinate legitimacy, and establish it is not a universal p-layer shadow or a coboundary.
2. Orientation-character bridge audit: independently test what, if anything, the condition g e1 = mu(g)e1 says about the target orientation character chi. No implication is assumed without proof.

### Existing closed routes
Original linear-only rank-4 lift observable, preferred-lift repair, naive q=9 relation-space route, artificial H-closure, Q3/Q9 S9 orbit route, and D9-OBS universal p-layer candidate remain closed.

## 0B. CURRENT AUTHORIZED FOLLOW-UP — 2026-09-19

### Rank-2 relator-unit digit definition gate — OPEN / DEFINITION ONLY

After the Delta_q coboundary closure, a new gate is registered: plans/RANK2_UNIT_DIGIT_DEFINITION_GATE_2026-09-19.md.

The candidate datum is the first mod-9 digit of a relator unit u(phi) in Z_3^times attached to an actual automorphism phi in Aut(G_q^(2)), with the primary lift-dependence test restricted to the kernel of the induced GL_2(F_3) action.

Required before computation:
1. exact definition of u(phi) in R/[R,F];
2. proof of multiplicativity/crossed law;
3. smallest filtration level determining u mod 9;
4. proof that the datum is not a function of g alone;
5. q=3 versus q=infinity hand derivation with q absent from the datum definition.

The existing rank-2 D4 lifting control is retained as a low-cost implementation control only. The connection between the relator unit and the canonical orientation character is EXTERNAL / TO VERIFY, not assumed.

No rank-2 finite scan and no rank-4 scan is currently authorized by this gate.

## 0C.1. BOUNDED-DEGREE FULL-χ OBSTRUCTION — 2026-09-19

The stronger question has been split by information model.

**Closed:** no universal carrier with fixed finite Zassenhaus-degree bound and finite 3-adic coefficient precision can recover the full (chi). For
[
G_{3^s}=langle x_imid x_1^{3^s}[x_1,x_2][x_3,x_4]
angle
]
the q-power term first appears in degree (3^s), while
[
chi_{3^s}(x_2)=(1-3^s)^{-1}
eq1=chi_infty(x_2).
]
Thus sufficiently large (s) defeats every fixed degree/precision bound.

**Still open:** a bounded-filtration-degree carrier with exact (mathbf Z_3)-coefficients. Such an object is not finite-information because exact 3-adic coefficients contain infinitely many digits. For fixed q=3 it may recover the full character and requires a separate intrinsic/projective definition.

Record:
`research/ORIENTATION_BOUNDED_DEGREE_FINITE_INFORMATION_OBSTRUCTION_2026-09-19.md`

## 0C. ORIENTATION RECONSTRUCTION CURRENT GATE — 2026-09-19

The finite-level factorization/inverse-limit theorem is now closed at the stated information level.

For the compatible projective filtered relation-jet tower \(J_n\),
\[
J_n\mapsto\chi_n:G\to(\mathbf Z/3^n)^\times
\]
is uniquely determined by the finite-level crossed-derivation equations. For the frozen q=3 relation,
\[
\chi_n(x_1)=\chi_n(x_3)=\chi_n(x_4)=1,
\qquad
\chi_n(x_2)=(-2)^{-1}\pmod{3^n}.
\]
The reductions are compatible and\[\mathbf Z_3^\times\cong\varprojlim_n(\mathbf Z/3^n)^\times\]
gives the unique full \(\chi\).

Record:
\`research/ORIENTATION_FINITE_LEVEL_FACTORISATION_THEOREM_2026-09-19.md\`

Decision: **finite-level factorization / inverse-limit theorem PASS / CLOSED**.

The next minimality audit then established a relative lower bound: any quotient carrier through which mod-9 recovery factors must preserve enough information to distinguish different \(\Theta\)-zero sets. Hence the bare graded forgetful factor is impossible. Absolute categorical minimality of \(J_3\) remains OPEN because the admissible carrier category, morphisms, and quotient/factorization notion are not yet fixed.

Record:
\`research/ORIENTATION_MOD9_RELATIVE_MINIMALITY_AUDIT_2026-09-19.md\`

### Current authorized orientation work

1. Define the smallest defensible category of projective degree-(2,3) relation carriers and test whether \(J_3\) has a genuine universal/minimal property.
2. Determine whether any finite bounded-degree carrier can recover the full 3-adic \(\chi\); if not, seek an obstruction theorem.

No broad finite scan is authorized.

---

## 1. Mathematical setting

\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle,
\qquad
R=[X_1,X_2]+[X_3,X_4],
\]

with degree-4 probe
\[
T=[[[X_3,X_4],X_1],X_1],
\]
and \(H=Sp_4(\mathbb F_3)\).

---

## 2. Global research chain

```text
Demuškin group
  ↓
Zassenhaus filtration / graded Lie structure
  ↓
quadratic relation R
  ↓
degree-4 probe T
  ↓
H-orbit module W (dim 45)
  ↓
internal H-module structure + filtration intersection
  ↓
I = W ∩ W_d = ker(N), dim 35
  ↓
canonical intertwiner τ
  ↓
bracket compatibility test
  ↓
rank-10 stacked obstruction O
  ↓
O2-3: O ≅ W/I ≅ U = im(N)
  ↓
CURRENT: determine whether this 10-dim module is filtration-intrinsic
  ↓
then test q=3 vs q=∞
  ↓
connect any successful invariant back to χ
```

---

## 3. Frozen structural results

### Phase 1 — single probe

- Single degree-4 probe \(T\) is not canonical under the relevant symplectic action.
- Single-probe strategy: **REJECTED / FROZEN**.

### Phase 2 — orbit/module structure

\[
\dim W=45,
\qquad
0\subset U_{10}\subset K_{35}\subset W_{45}.
\]

\[
U\cong\operatorname{Sym}^2(V),
\qquad
\dim(K/U)=25,
\qquad
W\cong\Lambda^2(\operatorname{Sym}^2(V)).
\]

\[
0\to M_{25}\to E_{35}=W/U\to\operatorname{Sym}^2(V)_{10}\to0
\]
is the non-split extension; the candidate \(E\cong\operatorname{Sym}^4(V)\) was rejected.

Track B A2:
\[
HP_4((uv)^{-3})=-T=2T\ne0.
\]

### Phase 2-3 — endomorphism algebra

Authoritative script: `research/phase2_3_endH_optimized_2026-09-15.py`.

\[
\dim\operatorname{End}_H(W)=2,
\quad
N^2=0,
\quad
\operatorname{rank}N=10,
\quad
\dim\ker N=35.
\]

Hence
\[
\operatorname{End}_H(W)\cong\mathbb F_3[\varepsilon]/(\varepsilon^2).
\]

### A3-4 — filtration intersection

\[
I=W\cap W_d,
\qquad
\dim I=35,
\qquad
\boxed{I=\ker N}.
\]
This is frozen.

### A3-4 provenance/repair audit

Audit run `35242896521`; corrected commit `62886877f97e58e87d59b0075d45e38be6176410`; corrected run `35245280405`.

The audit established exact equality of the selected \(W\) basis, all five generator action matrices, \(B=A_2+A_3+A_4+A_5\), and Krylov rank. The earlier apparent Krylov-rank-2 result came from an incorrect old quotient-action extraction. The repaired computation reproduced all frozen structural results.

**A3-4 computational/provenance audit is CLOSED.**

---

## 4. O2-2 — transported obstruction action: COMPLETE / VERIFIED

Record: `research/O2-2_RESULT_2026-09-18.md`  
Run `35278644641`, job `105395199074`.

- O2-2R: **PASS**
- O2-2S: **PASS**
- O2-2T: **PASS**

For all five generators, the independently solved 16-parameter action satisfies exactly
\[
\boxed{T_g=g^{-T}}
\]
over \(\mathbb F_3\), with generator-pair multiplicativity also verified.

Therefore
\[
D_{\rm stack}A_W(g)
=(g^{-T}\otimes A_5(g))D_{\rm stack},
\]
so
\[
\boxed{O=\operatorname{im}D_{\rm stack}\text{ is an }H\text{-submodule}.}
\]

### Final pre-O2-3 action identity check

**PASS:** the \(A_W(g)\) used in O2-2 is the same mathematical action used to define \(N\). The authoritative Phase 2-3 script loads `action_matrices` from Phase 2-1; Phase 2-1 and the corrected A3-4 pipeline use the same `apply_linear_map` and the same five `gens` construction, with column convention
\[
e_j\mapsto\sum_i g_{ij}e_i.
\]
Thus there is no coordinate/convention mismatch between the representation defining \(N\) and the \(A_W\) used in O2-2.

### Legacy convention archaeology

**⚪ NOT YET DETERMINED.** A historical hard-coded matrix numerically equal to \(g^{-T}\) was found, but it was a separate sanity-check object, not evidence that a legacy tuple-action implementation used that convention. This does not block the mathematical pipeline.

---

## 5. O2-3 — rank-10 obstruction identified: PASS / COMPLETE

Record: `research/O2-3_RESULT_2026-09-18.md`  
Run `35279936962`, job `105399291836`  
Final code commit: `3cf1608e26f0ef15ee6610ab8ae25a7f9237b951`

### Verified facts

\[
D_{\rm stack}\in\operatorname{Hom}(W,\mathbb F_3^{4096}),
\qquad
\operatorname{rank}D_{\rm stack}=10,
\qquad
\dim\ker D_{\rm stack}=35.
\]

Directly verified:
\[
D_{\rm stack}|_I=0,
\qquad
\boxed{\ker D_{\rm stack}=I=\ker N}.
\]

Therefore
\[
\bar D_{\rm stack}:W/I\xrightarrow{\sim}O
\]
is an isomorphism.

The nilpotent map gives
\[
N:W/I\xrightarrow{\sim}U=\operatorname{im}N.
\]
Combining them yields
\[
\boxed{U\xrightarrow{\sim}O}
\]
with rank 10.

The generator traces are identical:
\[
\operatorname{tr}(U)=[1,1,1,1,1],
\qquad
\operatorname{tr}(O)=[1,1,1,1,1],
\]
and the induced \(U\to O\) map was directly verified to be \(H\)-equivariant for all five generators. No independent 10x10 solve was needed.

### Mathematical interpretation

The rank-10 obstruction is **not merely a dimension coincidence** within the verified pipeline:
\[
\boxed{O\cong W/I\cong U=\operatorname{im}N}
\]
as an \(H\)-module via the induced map coming from \(D_{\rm stack}\) and \(N\).

This does **not yet** prove that the module is filtration-intrinsic, does not distinguish \(q=3\) from \(q=\infty\), and does not recover \(\chi\).

### Important distinction

The older A3-4-11 `OBSTRUCTION_MODULE` calculation concerns a different obstruction in `Hom(V,L_5/(R)_5)` and has a 45-dimensional image. It must not be conflated with the present O2-2/O2-3 stacked obstruction, whose image is the 10-dimensional \(O\).

---

## 6. O2 transport branch — HISTORICAL / CLOSED

The O2 transport branch is retained as chronology. It is not the current mathematical gate.

The concrete 20D transport-independent route was closed after the transport dependence could not be removed without introducing an unsupported new object. The subsequent q=3 versus q=infinity p-layer routes were also closed as universal p-layer shadows.

**Do not restore this section's historical OPEN labels as current state. The canonical current state is §0A and CURRENT_STATE.md.**

## 6A. O2-4 — absolute transport-independence: FAIL / COMPLETE

Record: `research/O2-4_RESULT_2026-09-18.md`  
Run `35281594800`.

For the exact B1-admissible normalized family
[
	au_b=	au(I+bN),qquad b=0,1,2,
]
each obstruction image has rank 10, but the three images are distinct. Their pairwise join ranks are 20:
[
operatorname{rank}(O_b+O_c)=20quad(b
e c).
]
Hence
[
oxed{O_0,O_1,O_2	ext{ are not equal}.}
]

**Interpretation:** the absolute obstruction image (O_	au=operatorname{Im}D_	au) is transport-dependent. This is a localized failure of canonicality, not a failure of the fixed-(	au) O2-3 module calculation.

The earlier scalar rescaling idea (a	au) is **not an admissible transport freedom** under the B1 pointwise condition (	au|_I=I_{W_d}); it must not be used as an O2-4/O2-5 test.

---

## 6B. O2-5 — affine transport variation: PASS / COMPLETE

Record: `research/O2-5_RESULT_2026-09-18.md`  
Run `35283099072`, job `105409292646`  
Final code commit: `5ab1e41befeb2c425ec0ad478de9665e78e3af9f`.

The corrected implementation first resolved a coordinate-system issue: the 256-dimensional vectors are degree-4 ambient coordinates, not 45-dimensional (W)-coordinates. The final B1 audit compares both sides in the same 256-dimensional ambient coordinate system via
[
I_{W,mathrm{coeff}}=Q_{W45}^{-1}I_{mathrm{coord}},
qquad
T_b^{mathrm{amb}}=W_d	au_bQ_{W45}^{-1}.
]

All final workflow assertions passed.

### Verified checkpoints

- B1 admissibility of the exact (b=0,1,2) family: **PASS**.
- Affine obstruction identity
[
D_b=D_0+bDelta D,qquad Delta D=D_1-D_0
]
: **PASS**.
- Variation rank:
[
oxed{operatorname{rank}Delta D=10}
]
: **PASS**.
- H-stability of
[
Delta O=operatorname{Im}Delta D
]
under the same transported target action used in O2-2: **PASS**.

Therefore
[
oxed{dimDelta O=10,qquad Delta O	ext{ is an }H	ext{-submodule}.}
]

### O2-6 — basepoint-independence: PASS / COMPLETE

Record: research/O2-6_RESULT_2026-09-18.md  
Run 35284130822, job 105412565419.

The complete frozen B1 family was tested by comparing the actual finite-difference maps:
\\[
D_1-D_0,\\qquad D_2-D_1,\\qquad D_0-D_2.
\\]
All three maps have rank 10 and are exactly equal. Hence the affine variation direction, and therefore \\(\\Delta O=\\operatorname{Im}\\Delta D\\), is independent of the basepoint within the complete verified B1 admissible family.

This closes the basepoint-dependence loophole left by O2-5. It still does not provide a transport-free formula solely in filtered/graded terms, nor does it establish \\(\\Delta O\\cong U\\) canonically, q=3 versus q=infinity, or recovery of \\(\\chi\\).

### Critical logical boundary

O2-5 does **not** prove that (Delta O) is canonical under a change of base transport, nor that it is determined by filtration data alone. It establishes a 10-dimensional H-stable **transport-variation module** within the fixed B1 affine family.

It also does not prove a canonical isomorphism (Delta Ocong U), distinguish (q=3) from (q=infty), or recover (chi).

The next gate is therefore:
[
oxed{	ext{Is the variation module }Delta O	ext{ itself independent of the remaining admissible choices?}}
]

Only after this gate should the project move to the explicit (q=3) versus (q=infty) comparison.


## 6C. O2-7 — q-control of transport variation: CORRECTED / PASS FOR ORBIT CLOSURE

Record: `research/O2-7_RESULT_2026-09-18.md`  
Original run: `35284838948`; original final code commit `988f61c04f3c659db2b4bff285f8f0809d4e7f4f`.

### Critical correction

The earlier claim
\[
\dim\langle HN(d)\rangle=9
\]
was an **implementation artifact**. The original O2-7 H-span routine propagated only the most recently appended orbit vector, rather than closing the span under every accumulated basis vector.

O2-8 used a complete closure routine and exposed this discrepancy. The 9D claim, the proposed 1D quotient, and all interpretations based on them are deprecated.

### Corrected result

For \(d=[X_1^{[3]},X_2]\):

- \(\dim\langle H\cdot d\rangle=45=\dim W\).
- \(\operatorname{rank}N(d)=1\).
- Complete orbit closure gives \(\boxed{\dim\langle HN(d)\rangle=10}\).
- Since \(\langle HN(d)\rangle\subseteq U=\operatorname{im}N\) and \(\dim U=10\), \(\boxed{\langle HN(d)\rangle=U}\).

Thus
\[
d\in W,\quad \langle Hd\rangle=W,\quad N(d)\in U,\quad \langle HN(d)\rangle=U.
\]

### Consequence

The previously proposed quotient \(U/\langle HN(d)\rangle\) is zero, not one-dimensional. The local q=∞ control \(d_\infty=0\) remains only a local suppression of the p-power contribution; it is not a full q=∞ recomputation.

### Current status

O2-7 supports the exact statement that the q=3 p-power class has a full 10-dimensional nilpotent shadow equal to U. It does **not** yet prove that this equality is filtration-intrinsic, does not provide a full q=3 versus q=∞ comparison, and does not recover \(\chi\).


## 6D. O2-9(pre) — Phi0/F compatibility: PASS / COMPLETE

Record: Actions run `35320678550`; corrected script commit `bcdfa2ebeeaee8a12d6e3c7e9e9db7421959d5`.

The coordinate-representation bug in the first O2-9(pre) attempt was repaired. The final computation used the 10-dimensional coordinate matrix of
[
\Psi=\Phi_0\circ F:\operatorname{Im}N\to U.
]

Verified:
- (dim\operatorname{Hom}_H(\Delta O,U)=1).
- (Psi) is exactly (10\times10).
- Full matrix comparison gives (Psi=I_{10}) exactly.
- All ten diagonal entries are 1.- Every off-diagonal entry is zero.
- (Psi=2I_{10}) is false.
Hence[
\boxed{\Phi_0\circ F=I_U}.
]

This is a coordinate-level compatibility check between the O2-7 and O2-8 identifications. It does not by itself prove transport-free canonicality.

## 6E. O2-9 — full (operatorname{Aut}_H(W)) transport coverage: HISTORICAL / SUPERSEDED

The remaining transport family must be exhausted before claiming canonicality.

Since
[
\operatorname{End}_H(W)=\mathbb F_3[I,N],qquad N^2=0,
]
its units are exactly
[
aI+bN,qquad a\in\mathbb F_3^\times=\{1,2\},quad b\in\mathbb F_3,
]
so there are exactly six units.

The experiment `research/O2_9_full_transport_invariance_2026-09-18.py` therefore enumerates all six
[
\tau_{a,b}=\tau\circ(aI+bN).
]

A subtle algebraic correction is frozen in the experiment protocol: for the affine obstruction
[
D(S)=D_{\rm linear}(S)-D_{\rm linear}(I),
]
the exact general identity is
[
D_{a,b}=aD_0+b\Delta D+(a-1)D_{\rm linear}(I).
]
Thus (D_{a,b}=aD_0+b\Delta D) is an additional simplification to be tested, not an identity to assume. In particular, the (a=2) case cannot be interpreted using the (a=1) affine formula without checking the extra term.

The experiment explicitly verifies:
1. (dim\operatorname{Hom}_H(W,W_d)=2) via composition with the verified (H)-isomorphism (	au), matching (dim\operatorname{End}_H(W)=2);
2. all six units and the corresponding six transports;
3. H-equivariance of all six transports;
4. the exact affine identity above;
5. the six resulting obstruction images and their total span relative to (O_0+\Delta O).

The canonicality decision is based on the exhausted six-element transport family, not merely on the three previously tested (a=1) transports.

## 6F. O2-9 — full transport / extension structure: COMPLETE / VERIFIED

Record: Actions run `35328765416`; final G-2 implementation commit `45256230c0fc7a866bc246cf13280df946bd3036`.

The six-element transport family was exhausted. The absolute 10-dimensional obstruction is **not** transport-independent: the `a=1` family has rank-10 images, while the `a=2` family has rank 45. Thus the original claim that all admissible transports preserve the same 20-dimensional obstruction space is **REJECTED**.

Nevertheless, the O2-9 structural investigation produced the following verified facts:

- `rank(C)=45`, where `C=D_linear(I)`.
- `dim(V20 intersection Im(C))=10`, with
  \[
  V20\cap\operatorname{Im}C=\Delta O,
  \qquad
  \operatorname{Im}C\cap O_\tau=0.
  \]
- `dim V55=55` for \(V55=V20+\operatorname{Im}C\), and \(V55\) is H-stable under all five generators.
- For \(G=D_{\rm linear}\circ\tau|_{\ker N}\):
  \[
  \operatorname{rank}G=35,
  \qquad
  V20\cap\operatorname{Im}G=\Delta O,
  \qquad
  \operatorname{Im}G\subseteq V55.
  \]
- `dim(V20 + Im G)=45`, and this 45-dimensional space is H-stable.
- Exact matrix-level H-equivariance of \(G\) was verified for all five generators.
- Therefore the induced quotient map is an H-module isomorphism:
  \[
  \boxed{\ker N/\operatorname{Im}N\cong_H (V20+\operatorname{Im}G)/V20},
  \]
  both sides having dimension 25. The injectivity follows from `rank(G)=35` and \(V20\cap\operatorname{Im}G=G(\operatorname{Im}N)=\Delta O\); surjectivity follows by the dimension count.

The optional side check also found
\[
\dim\operatorname{Im}D_{\rm linear}(\tau)=45,
\qquad
\dim(V45+\operatorname{Im}D_{\rm linear}(\tau))=55,
\]
so \(V45\neq\operatorname{Im}D_{\rm linear}(\tau)\), with a 35-dimensional intersection. This is recorded as an optional structural observation, not as part of the O2-9 gate.

The `all_rank10` assertion remains red because the `a=2` transports have rank 45. This is an outcome of the full transport experiment, not an implementation failure.

**O2-9 canonicality consequence:** the 10-dimensional absolute obstruction is not canonical under the exhausted transport family. The surviving structural statement is the verified 20-dimensional \(V20\) plus 25-dimensional quotient structure above. This does not by itself distinguish \(q=3\) from \(q=\infty\) or recover \(\chi\).

## 6G. O2-9 B1 — V20 image equality FAIL / CLOSED

Record: \`research/O2-9_B1_V20_IMAGE_EQUALITY_RESULT_2026-09-18.md\`  
Actions run: \`35359895308\`; job \`105648285525\`.  
Clean execution commit: \`721c6866fbf6ff4282f9e187c37951b1fea7eb71\`.

For the exact B1-admissible family
\[
\tau_b=\tau(I+bN),\qquad b=0,1,2,
\]
let
\[
A_b=\operatorname{Im}D_{(1,b)}.
\]

Verified:
- \(\dim A_0=\dim A_1=\dim A_2=10\);
- every pairwise join has dimension 20;
- hence every pairwise intersection has dimension
  \[
  \dim(A_i\cap A_j)=10+10-20=0;
  \]
- the three-way span has dimension 20.

Therefore
\[
\boxed{A_0,A_1,A_2\text{ are distinct 10-dimensional subspaces with pairwise-zero intersections}}
\]
and
\[
\boxed{\dim(A_0+A_1+A_2)=20}.
\]

The specific proposition that the absolute image is transport-independent within B1 is **FAIL**. The concrete-subspace \(V_{20}\) candidate is therefore **not promoted**.

Define, only as a B1-family observation,
\[
W_{B1}:=A_0+A_1+A_2,\qquad \dim W_{B1}=20.
\]
This does not establish that \(W_{B1}\) is filtration-intrinsic or canonical, and it must not be conflated with a canonical \(V_{20}\).

This result is strictly scoped to the B1 transport family. It does not invalidate the fixed-\(\tau\) O2-3 identification \(O\cong U\), does not decide filtration-intrinsicity in general, and does not decide q=3 versus q=\(\infty\) or recovery of \(\chi\).

## 6G. Q3/Q∞-J — CLOSED / vector-orbit distinction verified

Record: `research/Q3_QINF_INDEPENDENCE_PROTOCOL_2026-09-18.md`; `research/Q3_QINF_zero_case_prereg_2026-09-18.md`  
Actions run: `35350310816`; head commit: `88c90e2a05dab34ef6bac2d9f5545731263850b9`.

The preregistered vector-orbit invariant
\[
J(v)=|H_U\cdot v|
\]
was computed with the fixed N, U, H-action and exact F3 arithmetic.

Verified:
- \(J(N(d_3))=40\);
- \(d_\infty=0\), \(N(d_\infty)=0\), and \(J(N(d_\infty))=1\) as the analytically determined zero-case sanity check;
- \(|\ker(H\to GL(U))|=2\);
- \(|H_U|=25920\);
- \(|\operatorname{Stab}_H(N(d_3))|=1296\);
- \(|\operatorname{Stab}_{H_U}(N(d_3))|=648\);
- first-isomorphism and orbit-stabilizer checks both PASS.

Therefore the substantive local criterion
\[
\boxed{J(N(d_3))\ne J(N(d_\infty))}
\]
passes: this specified N/J probe distinguishes q=3 from the fixed q=∞ baseline.

**Scope boundary:** this does not establish that the canonical 3-adic orientation \(\chi\) is recovered, nor that the distinction is intrinsic to the entire Zassenhaus filtration.

The Q3/Q∞ gate is now **CLOSED**.

## 6H. Q3/Q9 — Gate A d9 definition PASS / CLOSED

Protocol: `research/Q3_Q9_PROTOCOL_2026-09-18.md`; independent derivation commit `392e6134b11308b8219538d4b38fd241c98817fc`; CI workflow commit `5ed9ca9a9280344fa3340a22122a815d5551b320`.

The q=9 source was independently derived from
\[
G_9=\langle x_1,x_2,x_3,x_4\mid x_1^9[x_1,x_2][x_3,x_4]=1\rangle.
\]

Actions run `35352242909` verified:
- \(\operatorname{in}_3(x_1^9)=0\);
- \(\operatorname{in}_3(s_9)=\operatorname{in}_3(s_\infty)\);
- \(\Delta_3(9)=0\);
- \(\boxed{d_9=0}\).

The Gate-A computation is self-contained and does not import the q=3 research script or downstream N/J computation. Gate A is therefore **PASS / CLOSED**.

Q3/Q9 Gate B (N/J comparison) remains **BLOCKED / NOT OPENED**. The fact that \(d_9=0\) is now a verified definition result; it does not by itself authorize a downstream N/J interpretation or imply any q-distinction/conclusion.

## 7. What is NOT the current task

- Do **not** redo the A3-4 provenance audit.
- Do **not** rebuild the historical Phase 2 representation without contradiction.
- Do **not** treat \(O\cong U\) as already proving \(q=3\) versus \(q=\infty\).
- Do **not** claim orientation recovery yet.
- Do **not** block progress on unresolved historical tuple-action archaeology.

---

## 8. New-chat / new-window protocol

> **수학증명 프로젝트 이어가기. 먼저 `RESEARCH_MAP.md`를 기준으로 현재 상태를 복원해줘. A3-4 audit는 완료·동결, O2-2는 PASS, O2-3도 PASS이며 현재 본 연구 단계는 `U = im(N) ≅ O = im(D_stack)`라는 식별이 transport-독립적이고 filtration-intrinsic인지 확인하는 것이다. 새 계산 전에 global position / purpose / dependency / pass-fail consequence를 먼저 정리하고 corrected artifact를 우선 사용하자.**

### Session safety rules

- **Map first.**
- **Authority hierarchy:** Map → Conventions → active Plan → Result/Run evidence.
- **One fact, one authority:** do not create parallel current-state/protocol documents.

- **Frozen means frozen.**
- **Artifact first.**
- **Contradiction first.**
- **Experiment gate:** before execution state purpose, dependency, expected interpretation, and pass/fail consequence.
- **History/state separation:** chronology in `research/00_RESEARCH_LOG.md`; current state here.

---

## 9. Research-record architecture and authority hierarchy

Use one authority for each kind of fact:

| Role | Authority |
|---|---|
| Current mathematical state | `RESEARCH_MAP.md` |
| Mathematical/computational conventions and operating rules | `research/03_CONVENTIONS_AND_IMPLEMENTATION.md` |
| Current O2 research question and experiment sequence | `plans/PLAN-O2-TRANSPORT-INTRINSIC.md` |
| Evidence for a specific result | `research/*_RESULT_*.md` + exact Actions run/job |
| Chronology and historical context | `research/00_RESEARCH_LOG.md` |
| Failure history / recurrence prevention | `ANTIPATTERNS.md` |

`AI_CONTEXT_BRIEF.md` is a bootstrap document for new sessions, not an independent authority for current mathematical status. Parallel q=3/q=∞ work remains separate from the O2 plan unless explicitly promoted into the map.

Existing historical protocol documents are reference/history only; they do not override the three current authorities above.

- O2-2 record: `research/O2-2_RESULT_2026-09-18.md`
- O2-3 record: `research/O2-3_RESULT_2026-09-18.md`

---

## 10. Status legend

- 🟢 **FROZEN / VERIFIED** — safe downstream input.
- 🟡 **OPEN** — mathematically meaningful but unsettled.
- 🔴 **REJECTED** — ruled out for the stated purpose.
- ⚪ **BACKGROUND / NOT YET DETERMINED** — unresolved historical/contextual issue, not a current mathematical gate.

| Item | Status |
|---|---|
| Single probe \(T\) canonicality | 🔴 Rejected |
| \(W\) orbit module, dim 45 | 🟢 Frozen |
| \(\dim End_H(W)=2\) | 🟢 Frozen |
| \(N^2=0\), rank \(N=10\) | 🟢 Frozen |
| \(I=W\cap W_d\), dim 35 | 🟢 Frozen |
| \(I=\ker N\) | 🟢 Frozen |
| rank-45 intertwiner \(\tau\) | 🟢 Verified |
| A3-4 provenance audit | 🟢 Closed |
| bracket discrepancy rank 10 | 🟢 Verified |
| O2-2R/S/T | 🟢 PASS |
| \(T_g=g^{-T}\) | 🟢 Exact / verified |
| \(O=\operatorname{im}D_{\rm stack}\) is an \(H\)-submodule | 🟢 Verified |
| \(A_W\) identity with action defining \(N\) | 🟢 Verified |
| \(\ker D_{\rm stack}=I\) | 🟢 PASS |
| \(\dim O=10\) | 🟢 PASS |
| \(U\cong O\) as \(H\)-modules | 🟢 PASS |
| absolute transport-independence of O_tau | 🔴 Failed in O2-4 |\n| variation-module basepoint independence within B1 family | 🟢 O2-6 PASS |\n| O2-7 raw p-power orbit = U | 🔴 False (orbit dimension 45) |
| O2-7 H.N(d) inside U, dim 10 and equals U | 🟢 Corrected / verified |
| O2-9 full transport canonicality | 🔴 Failed / exhausted |\n| O2-9 20+25 quotient structure | 🟢 Verified |\n| O2-9 B1 absolute image equality / concrete V20 | 🔴 Failed / not promoted |\n| B1 three-image span dimension 20 | 🟢 Verified observation |\n| B1 concrete 20D span transport-free characterization from frozen data | 🔴 Not obtained / current route closed |\n| full filtration-intrinsic characterization of Delta O | 🟡 Open |\n| concrete target-side 20D-space route | 🔴 Closed at current frozen-data level |
| legacy tuple-action archaeology | ⚪ Not yet determined |
| q=3 vs q=∞ distinction | 🟡 Open |
| intrinsic recovery of \(\chi\) | 🟡 Open |

---

## 11. O2 concrete 20D route — HISTORICAL / CLOSED

The B1 family gives three distinct 10D images with pairwise-zero intersections and a common 20D span. Existing affine identities identify this span with Im(D0) + Delta O, but D0 remains transport-dependent. Existing relations involving G = D_linear o tau|ker(N) likewise use the chosen transport.

This closes the concrete 20D-space route for the present construction. It does not prove that no intrinsic 20D object can ever exist. No new V20, quotient, or invariant should be introduced merely to rescue this route.

Q3/Q-infinity remains logically separate.
## 12. Immediate next checkpoint

Do not ask whether O2-3 is "good" or "bad". It has passed.

Ask instead:

\[
\boxed{\text{What makes the 10-dimensional module }U\cong O\text{ canonical?}}
\]

The critical issue is **transport dependence**: the current \(O\) was produced from the specific canonical intertwiner \(\tau\) already fixed by the A3-4 construction. We must determine whether the resulting 10-dimensional module/map is forced by the filtered structure, or merely an artifact of that transport choice.

Only after this gate:
\[
\boxed{q=3\;\text{vs}\;q=\infty}
\]
and eventually
\[
\boxed{\chi\text{ recovery}}.
\]


## 6I. Q3/Q9 — degree-3 probe degenerate; Gate C OPEN

Gate A is CLOSED with independently verified d9=0 (Actions run 35352242909). Consequently the frozen degree-3 N/J probe has only N(0)=0, J(0)=1; it is recorded as a degenerate probe, not as a mathematical failure and not as evidence that q=3 and q=9 filtrations coincide.

The next controlled question is Gate C: determine the first filtration degree at which the q=9 power term can contribute to the baseline-relative source. Over F_3, (1+X_1)^9 has no terms in degrees 1–8, so degree 9 is the first possible contribution from the power term. The degree-9 leading term of the full baseline-relative control remains to be derived independently; no Delta_9(9), source, or new invariant is assumed.

Gate C must be completed before any new q=9 probe is designed. O2 and Q3/Q9 remain logically separate tracks.

## 13. 2026-09-19 — methodological decision after O2 transport failure

The proposed alternative route was critically reviewed against the frozen O2/Q3/Q9 state.

### Adopted

- The research target is narrowed from the broad phrase “recover q/orientation from the Zassenhaus graded object” to the more precise question of whether a **prescribed weak filtered/graded structure** can canonically distinguish q=3 from q=∞.
- Orientation recovery \\(\\chi\\) remains a downstream goal and is not identified with q-distinction.
- A **rank-2 control track** is adopted as a low-cost validation layer for relator-preservation/lifting machinery before any large degree-9 rank-4 computation.
- The proposed lifting observable \\(A_n(q)\\) is retained only as a **provisional diagnostic** until its definition is audited.
- GAP/ANUPQ remains a possible independent verification layer, not a replacement for the current mathematical route.

### Deferred / rejected for now

- Do not replace the current Zassenhaus track by the p-descending central series merely for dimension reduction.
- Do not open a new Massey/A∞ main track at this stage.
- Do not introduce a new canonical 20-dimensional target-space object to rescue the failed O2 concrete-subspace route.
- Do not treat the full finite quotient \\(G/D_n\\) as automatically “weak data”: its abstract group structure may already expose q through abelianization.

### New immediate task

Before implementing \\(A_n(q)\\), perform a definition audit:

1. specify exactly what a lift of \\(g\\in Sp(V)\\) means;
2. specify whether relator preservation is equality or preservation of the normal closure modulo \\(D_n\\);
3. specify the filtration and the induced action;
4. separate information explicitly allowed to the invariant from information that would trivially reveal q;
5. choose the smallest nontrivial filtration level.

Then run the rank-2 control specified in `plans/PLAN-RANK2-CONTROL-AND-LIFTING.md`.

This is a **new validation/diagnostic track**, not a replacement for the existing O2 or Q3/Q9 tracks. The O2 transport-independentity question remains closed at the current concrete 20D level, and the Q3/Q9 Gate C status is unchanged.


## 14. 2026-09-19 — C-2c-1 restricted ambient certificate

Record: `research/C-2C-1_RESULT_2026-09-19.md`  
Implementation: `research/C-2C-1_restricted_ambient_certificate_2026-09-19.py`  
Implementation commit: `0feb39f511569b799231d8d67259ece7a39af666`  
Result-record commit: `025570350fe5f19a4e67c64b8b1aa94ae3f1b9f5`

The rank-2 tensor-algebra control was independently constructed over \(\mathbf F_3\) using exact Gaussian elimination. It gives
\[
\operatorname{rank}L_9=56,
\qquad
\operatorname{rank}L_3^{[3]}=2,
\qquad
\operatorname{rank}L_1^{[9]}=2,
\]
and
\[
\boxed{\operatorname{rank}(L_9+L_3^{[3]}+L_1^{[9]})=60=56+2+2.}
\]

This closes the **small-rank ambient restricted-structure check**: in the 2-generator tensor realization, the degree-9 free-Lie part and the two restricted p-power layers are independent.

For four generators the corresponding dimension count is
\[
29120+20+4=29144,
\]
but this remains a formal dimension prediction, not a full rank-4 degree-9 tensor certificate.

**Scope:** this does not define or validate \(R_9\), \(\mathrm{gr}_9(G)\), H-stability, \(S_9=X_1^{[9]}\), or any degree-9 q-invariant. No downstream degree-9 computation is authorized from this result alone.

**Next gate:** audit the repository's existing lower-degree relation-space convention and define the degree-9 restricted relation space \(R_9\) before any H-stability computation.


## 6J. S9-A — ambient admissibility: PASS / CLOSED

Record: `research/Q3_Q9_S9_A_AMBIENT_ADMISSIBILITY_RESULT_2026-09-19.md`  
Gate record commit: `f8bc39c03eec6a9ba88116c5b46f29eefe3276f2`.

The ambient gate is now formally closed.

Using the already verified C-2a restricted-power identification,
[
X_1^{[3]}=X_1^3,qquad (X_1^{[3]})^{[3]}=X_1^9,
]
the Magnus source
[
S_9=Delta_9(9)=X_1^9
]
may now be represented in the restricted degree-9 ambient as
[
oxed{S_9=X_1^{[9]}}.
]

This is only an **ambient** admissibility result. It does not assert quotient survival and does not test (S_9in I_{infty,9}).

The frozen baseline remains
[
oxed{dim I_{infty,9}=13524},
]
and no (S_9) contribution has been inserted into that baseline.
### Next gate

The next controlled computation is **S9-B — quotient survival**:[
oxed{[S_9]
eq0	ext{ in }L_9^{mathrm{res}}/I_{infty,9}}]
equivalently
[
oxed{S_9
otin I_{infty,9}}.
]

Only after S9-B is resolved may (S_9) be used in any (q=9) ideal construction. H-stability and (D_9) remain blocked.


## 6K. S9-B — quotient survival: PASS / CLOSED

Record: `research/Q3_Q9_S9_B_QUOTIENT_SURVIVAL_RESULT_2026-09-19.md`.

The previous S9-B PASS was retracted during audit, and has now been legitimately restored after the missing structural lemma was independently verified.

Record: `research/Q3_Q9_S9_B_STRUCTURAL_LEMMA_RESULT_2026-09-19.md`.

The structural restricted-ideal recursion gives
[
(I_infty)_9=(I^{ord})_9oplus I_3^{[3]},
]
because all bracket descendants are in the ordinary ideal, the only degree-9 p-power source is degree 3, and ((I_infty)_1=0) eliminates any (L_1^{[9]}) source. Hence
[
(I_infty)_9cap L_1^{[9]}=0.
]

Together with S9-A,
[
S_9=X_1^{[9]}in L_1^{[9]},quad S_9
e0,
]
this proves
[
oxed{S_9
otin I_{infty,9}}.
]

### Current consequence

- S9-A ambient admissibility: **PASS / CLOSED**.
- S9-B quotient survival: **PASS / CLOSED**.
- Baseline (dim I_{infty,9}=13524): **FROZEN**.
- S9 is excluded from the baseline.
- The next authorized step is the separate q=9 relation-space construction (I_9=langle R_2,S_9
angle_{res}).
- H-stability and (D_9) remain downstream gates.

## 6H. Q3/Q9 S9 — q=9 degree-9 relation-space gate: PASS / CLOSED

Record: `research/Q3_Q9_S9_q9_degree9_relation_space_RESULT_2026-09-19.md`.

After S9-A and S9-B were closed, the q=9 restricted ideal was defined by
\[
I_9=\langle R_2,S_9\rangle_{res},\qquad S_9=X_1^{[9]}.
\]

Since S9 has degree 9, its brackets have degree at least 10 and its restricted powers degree 27. Hence
\[
(I_9)_9=(I_\infty)_9+\langle S_9\rangle.
\]
The S9-B structural lemma gives zero intersection of the baseline with (L_1^{[9]}), while S9 is nonzero in that layer. Therefore
\[
\boxed{(I_9)_9=(I_\infty)_9\oplus\langle S_9\rangle},
\qquad
\boxed{\dim (I_9)_9=13525}.
\]

The exact F3 audit verifies the new S9 direction has rank 1. The frozen q=∞ baseline remains 13524.

This gate does **not** establish H-stability, gr9 quotient identification, D9, q=9 invariant detection, or orientation recovery.

**Next gate:** H-stability of ((I_9)_9) under the fixed (H=Sp_4(\mathbb F_3)) action.

## 6I. Q3/Q9 S9 — H-stability gate: FAIL / CLOSED

Record: research/Q3_Q9_S9_H_STABILITY_RESULT_2026-09-19.md.

For the naive q=9 degree-9 relation space
\[
(I_9)_9=(I_\infty)_9\oplus\langle S_9\rangle,
\]
the fixed transvection \(t_{e_2}\) satisfies
\[
t_{e_2}(e_1)=e_1+e_2,
\qquad
t_{e_2}(S_9)=S_9+X_2^{[9]}.
\]
Because the frozen S9-B structural lemma gives
\[
(I_\infty)_9\cap L_1^{[9]}=0,
\]
the transformed vector is outside the q=9 degree-9 space. Exact F3 ranks give rank(<S9>)=1 and rank(<S9,t_e2 S9>)=2.

Therefore
\[
\boxed{(I_9)_9\text{ is not H-stable}.}
\]

The first audit draft had a sign error in the witness; it was detected and corrected before accepting the result. The original attempt is classified INVALID TEST, not mathematical evidence.

**Consequence:** do not proceed to gr9 quotient identification or D9 using the naive I_9,9 as an H-module. The next gate is a critical redesign: determine whether an H-closed replacement is mathematically legitimate and compatible with the presentation-derived q=9 relation.


## 6L. Q3/Q9 S9 — H-closure redesign gate C3.1–C3.3: CLOSED

Record: `research/Q3_Q9_S9_C3_H_closure_redesign_RESULT_2026-09-19.md`  
Implementation commits: `df802e0cc3116a311a39dc8b764c46b5d6dc633d`, `fb328fb502616fd4c8475185fe2aa25a0b10adf3`, `551632894cdf6fce5e22c9dec10c1ece3bd7fb94`.

The complete exact \\(H\\)-orbit closure of \\(S_9=X_1^{[9]}\\) was computed in the natural \\(L_1^{[9]}\\) layer:

\\[
\\boxed{\\dim\\langle H\\cdot S_9\\rangle=4},
\\qquad
\\boxed{\\langle H\\cdot S_9\\rangle=L_1^{[9]}}.
\\]

Thus **C3.1 = PASS**.

However the fixed-presentation relation space has only the line \\(\\langle S_9\\rangle\\) in this layer. The already verified witness
\\[
t_{e_2}(S_9)=S_9+X_2^{[9]}
\\]
shows that the H-closure contains a direction which is not a relation of the fixed q=9 presentation. Therefore promotion of the H-closure as an equivalent q=9 relation space fails:

\\[
\\boxed{\\text{C3.2 = FAIL}}.
\\]

The frozen S9-B structural lemma also gives
\\[
\\boxed{\\langle H\\cdot S_9\\rangle\\cap(I_\\infty)_9=0},
\\]
so **C3.3 = PASS**.

### Consequence

The H-closure rescue route is **CLOSED / NOT PROMOTED**. The tempting dimension
\\[
13524+4=13528
\\]
is only the dimension of a different H-closed relation enlargement; it is **not** the degree-9 relation dimension of the fixed q=9 group and must not be used as such.

Do not proceed to \\(gr_9\\) or \\(D_9\\) using either the naive q=9 space or this artificial H-closed enlargement.

### Next authorized Q3/Q9 checkpoint

Return to the already-open **Gate C**: independently derive the first nonzero baseline-relative degree-9 contribution of the full q=9 presentation from the presentation/Magnus expansion, without assuming H-stability. No new H-closed q=9 relation object is to be introduced merely to rescue the failed route.


## 6M. Q3/Q9 — Gate C: first nonzero degree-9 source CLOSED

Record: `research/Q3_Q9_GATE_C_DEGREE9_SOURCE_RESULT_2026-09-19.md`  

The frozen Gate-C Magnus conventions were applied to the full q=9 control and the q=infinity baseline, independently of the previous q=3 source. Through degree 9,

\\[
\\Delta_d(9)=0\\quad(1\\le d\\le8),
\\]

while the exact degree-9 component is

\\[
\\boxed{\\Delta_9(9)=X_1^9}.
\\]

The characteristic-3 power identity gives
\\[
(1+X_1)^9=1+X_1^9,
\\]
consistent with the computation. Together with the already closed S9-A ambient identity, this identifies the source in the one-generator restricted realization as
\\[
\\boxed{\\Delta_9(9)=X_1^{[9]}=S_9}.
\\]

This closes only the **source-location/derivation** part of Gate C. It does not define a degree-9 quotient invariant, prove H-stability, or authorize D9. The previous H-stability FAIL and the C3 H-closure provenance FAIL remain in force.

### Next authorized gate

Define and audit a **degree-9 source map** from this presentation-derived source. Do not reuse the frozen degree-3 N/J map by analogy, and do not treat S9 as an H-submodule. The map's target, quotient conventions, and H-action must be derived before any new invariant is computed.


## 6N. Q3/Q9 — S9 degree-9 source-map definition gate CLOSED / PASS

Plan: `plans/Q3_Q9_S9_SOURCE_MAP_GATE.md`

The target/action audit was completed before any orbit computation.

For the complete 80 nonzero-vector symplectic transvections over F3,
\[
g^T J g=J.
\]
The quadratic relation R_2 has coefficient matrix J, so every H-generator fixes R_2. Since the frozen baseline ideal I_infty is the restricted ideal generated by R_2,
\[
h(I_\\infty)=I_\\infty
\]
for all h in H. Hence the baseline quotient
\[
Q_9^\\infty=L_9^{res}/(I_\\infty)_9
\]
has a well-defined induced H-action.

S9-B supplies S9 not in the baseline, so
\[
\\phi_9:\langle S_9\\rangle_{\\mathbf F_3}\to Q_9^\\infty,
\qquad S_9\\mapsto[S_9]
\]
is well-defined and nonzero.

No q=9 relation insertion, artificial H-closure, or inherited degree-3 N/J object is used.

### Gate status

- target well-definedness: **PASS**
- baseline H-stability: **PASS**
- coordinate/provenance compatibility: **PASS**
- source nonzero: **PASS** via S9-B
- hidden q=9 insertion: **PASS (none)**
- degree-3 N/J reuse: **PASS (none)**

\[
\\boxed{\\text{S9 source-map definition gate: PASS / CLOSED}}
\]

The next authorized computation is the target-side orbit span
\[
\\mathcal O_9=\\langle H\\cdot[S_9]\\rangle\\subseteq Q_9^\\infty.
\]

This remains only a target-side H-module construction. It is not the fixed q=9 relation space, and no q=3/q=\\infty distinction or orientation conclusion is yet authorized.


## 6O. Q3/Q9 S9 — target-side orbit span PASS

Record: research/Q3_Q9_S9_TARGET_ORBIT_SPAN_RESULT_2026-09-19.md

The source-map target is
\[
Q_9^\\infty=L_9^{res}/(I_\\infty)_9.
\]
S9-B gives
\[
(I_\\infty)_9\\cap L_1^{[9]}=0,
\]
so the quotient map is injective on the p-layer \(L_1^{[9]}\).

C3.1 already established
\[
\\langle H\\cdot S_9\\rangle=L_1^{[9]},
\qquad \\dim L_1^{[9]}=4.
\]
Therefore the target-side orbit satisfies
\[
\\boxed{\\mathcal O_9=\\langle H\\cdot[S_9]\\rangle
\\cong L_1^{[9]},\\qquad \\dim\\mathcal O_9=4.}
\]

This is a quotient-side H-module, not the q=9 relation space and not an H-closed replacement for it.

### Boundary

No q=3/q=\\infty distinction, canonical q-invariant, or orientation conclusion is established by this 4-dimensional orbit alone.

### Next gate

Determine whether the 4-dimensional target-side module gives a legitimate comparison observable between the q=3 and q=\\infty presentations, rather than merely reproducing the natural p-layer representation.


## 6P. Q3/Q9 S9 — explicit baseline H-stability action bridge: PASS / CLOSED

Record:
research/Q3_Q9_S9_SOURCE_MAP_H_STABILITY_ACTION_BRIDGE_RESULT_2026-09-19.md

The previous target-action audit verified \\(g^T Jg=J\\) for all 80 nonzero-vector
symplectic transvections and used the frozen coefficient-matrix convention to
infer \\(g(R_2)=R_2\\). A dedicated implementation bridge audit was added because
the latter implication had not itself been executed by the authoritative action.

Using the repository's authoritative five generators and authoritative
associative substitution action, the audit directly checked

\\[
\\boxed{g\\cdot R_2=R_2}
\\]

for every generator. It also passed multiplicativity and first restricted-power
compatibility on the same action.

Therefore the target-action chain is now explicitly closed:

\\[
g^T Jg=J
\\Rightarrow gR_2=R_2
\\Rightarrow h(I_\\infty)=I_\\infty
\\Rightarrow Q_9^\\infty\\text{ carries an induced H-action}.
\\]

CI run 35414448355, job 105820186019: **SUCCESS**.

This strengthens the source-map target-action status to **structural + explicit
implementation-bridge PASS**. It does not change any downstream q=9 H-stability
failure.

## 6Q. Q3/Q9 S9 — D9-OBS definition gate: OPEN

The target-side orbit remains

\\[
\\boxed{
\\mathcal O_9=\\langle H\\cdot[S_9]\\rangle
\\cong L_1^{[9]},
\\qquad
\\dim\\mathcal O_9=4.
}
\\]

This 4-dimensional object is now considered structurally closed, but its
dimension is not treated as a q-dependent invariant.

The next authorized task is **definition before computation**:

\\[
\\boxed{
\\text{Can a natural q-dependent observable be derived from }\\mathcal O_9?
}
\\]

A candidate must arise from the presentation-derived source and frozen target
construction. Do not manufacture a statistic from the number 4, and do not
reuse the degree-3 N/J construction by analogy.

### Consequence

- PASS: define a natural target-side q-comparison observable before computing it.
- FAIL: establish that \\(\\mathcal O_9\\) is only the natural p-layer shadow and
  close this route without inventing a q-invariant.
- INCONCLUSIVE: the observable depends on an arbitrary transport, coordinate,
  presentation, or noncanonical identification.

No D9 or orientation conclusion is authorized at this stage.


## 6R. Q3/Q9 S9 — D9-OBS natural p-layer candidate: FAIL / CLOSED

Record:
research/Q3_Q9_S9_D9_OBS_DEFINITION_RESULT_2026-09-19.md

The natural candidate was to compare the degree-9 target-side p-layer shadow
of the already verified q=3 source with the q=9 source.

The frozen q=3 source is
\\[
\\Delta_3(3)=X_1^{[3]}.
\\]
Applying the natural restricted p-map gives
\\[
(\\Delta_3(3))^{[3]}=X_1^{[9]}.
\\]
Gate C gives
\\[
\\Delta_9(9)=S_9=X_1^{[9]}.
\\]
Therefore in the common baseline target,
\\[
\\boxed{
[(\\Delta_3(3))^{[3]}]=[S_9]
}
\\]
and hence their H-orbit spans are identical:
\\[
\\boxed{
\\langle H\\cdot[(\\Delta_3(3))^{[3]}]\\rangle
=
\\langle H\\cdot[S_9]\\rangle
=
\\mathcal O_9.
}
\\]

Thus the 4-dimensional orbit is a universal p-layer shadow, not a q=3/q=9
observable. The candidate is closed as **FAIL / CLOSED**.

### Next authorized question

Do not invent another statistic from the same 4D module.

The next search must identify a presentation-derived structure that retains
information lost by the universal p-layer map, while respecting the frozen
boundary that the naive q=9 relation space is not H-stable and its artificial
H-closure is not a valid presentation object.


## 6S. Q3/Q9 S9 — post-D9 presentation-derived structure census: CLOSED
Record: `research/Q3_Q9_S9_D9_OBS_STRUCTURE_CENSUS_2026-09-19.md`

After closing the natural p-layer observable, the authoritative Q3/Q9 records and the relevant earlier q-control/roadmap records were audited for an already-defined presentation-derived structure that survives beyond (L_1^{[9]}).
No such already-authorized q-sensitive object was found.

In particular:
- Gate-C's (Delta_9(9)=X_1^{[9]}) is exactly the universal p-layer shadow.- The fixed q=9 degree-9 relation space is not H-stable.
- Its artificial H-closure is not a valid presentation relation object.
- The existing O2-7 transport-variation module is a degree-4 q=3/q=infty construction and its own boundary excludes using it as a q=3/q=9 degree-9 object.
- The roadmap currently points to broader Track-B/group-level or higher-operation structures, but none is already defined as a Q3/Q9 D9 object.

Decision:
[
oxed{	ext{current Q3/Q9 S9 orbit route = CLOSED at the definition level}.}
]

This is not a proof that no future q=9 invariant exists. Any continuation requires a genuinely new object with its own definition/legitimacy gate, preferably from full filtered/Magnus data, a rigorously defined higher operation/extension datum, or a q-common Track-B construction. No statistic is to be manufactured from (dimmathcal O_9=4).

## 7. Rank-2 lifting control — PASS / CLOSED

Following the closure of the Q3/Q9 S9 orbit branch, the provisional relator-preservation/lifting pipeline was validated on the rank-2 control G_q^(2)=<x1,x2 | x1^q[x1,x2]=1> at D4.

Selected representative results:
- q=3: identity and the vector-fixing unipotent pass;
- q=3: -I and a selected line-moving transvection fail;
- q=infinity: all four selected representatives pass.

The result is control validation only. It does not establish the full A4(q), a line-stabilizer characterization, or any rank-4 theorem.

Result: research/RANK2_D4_LIFTING_CONTROL_RESULT_2026-09-19.md
CI: run 35415080640, job 105822020636.

### Current continuation gate

Before any rank-4 lifting computation, freeze a rank-4 A_n^rel-type definition:
1. exact filtration level;
2. allowed free pro-3 lift class;
3. relator-normal-closure / relator-unit criterion;
4. weak-data input boundary;
5. GSp versus Sp ambient convention.

Only then execute a small rank-4 control.
## 8. Rank-4 D4 lifting definition gate — OPEN

The rank-2 control passed, so a rank-4 candidate was formally drafted at D4.

Candidate:
A_4^rel(q) = {g in GSp_4(F3): an allowed lift preserves the relator up to a unit modulo D4}.

For q=3, the degree-2 relation fixes the unit to the GSp multiplier mu(g). After the required degree-3 normal-closure separation, the candidate q=3 condition is g e1 = mu(g)e1.

This is not yet a theorem or PASS. The next gate is an independent definition/implementation audit of the D4 equivalence, degree-3 correction span, restricted p-layer separation, lift-independence, and GSp/Sp convention.

Definition record: plans/RANK4_D4_LIFTING_DEFINITION_GATE_2026-09-19.md

No rank-4 computation is authorized before this gate closes.
## 9. Rank-4 D4 lifting definition gate — FAIL / CLOSED

The candidate rank-4 relator-lifting observable was audited for lift-independence before any rank-4 q-comparison.

Two lifts inducing the same identity action on V were tested:
- identity lift;
- x1 -> x1[x1,x2], with the other generators fixed.

The first is admissible; the second is not. Its degree-3 difference lies outside the ordinary conjugation correction span.

Therefore the candidate A_4^rel(q) subset GSp_4(F3) is not intrinsic to the linear map under the current lift definition.

Decision: rank-4 D4 lifting definition = FAIL / CLOSED.

This is a genuine mathematical negative result, not a setup failure. No rank-4 q-comparison is authorized from this candidate.

The failure identifies IA/lift data as active degree-3 information. A future lifting route must retain that finer filtered/extension data or provide a canonical invariance/quotient mechanism. A hand-picked lift convention must not be treated as intrinsic.

Result: research/RANK4_D4_LIFT_INDEPENDENCE_AUDIT_RESULT_2026-09-19.md
CI: run 35415237341, job 105822474022.

## 10. Rank-4 D4 — IA / filtered extension datum gate OPEN

The rank-4 D4 lifting candidate is **FAIL / CLOSED** because admissibility is not determined by the induced linear action on V: identity and an IA-modified lift of the same identity map give different degree-3 outcomes.

The failed object must not be repaired by choosing a preferred Nielsen lift. A new definition gate is opened in `plans/RANK4_D4_IA_EXTENSION_DATUM_GATE_2026-09-19.md`.

The next authorized task is a small IA defect-action audit: define the degree-3 defect target, determine the lift-fibre/IA change law, and test whether a canonical quotient, orbit/torsor, or extension datum can retain q-sensitive information. No rank-4 q-comparison is authorized before this gate closes.


## 11. Rank-4 D4 IA extension datum — current continuation after covariance and representative control

The admissible-category covariance audit is now CI-verified: run `35416804953`, commit `c620ce5a962031cfff90d49aa8500ea39cc16dc1`.

Within the admissible category H_adm of size 1296, the spaces C3, Delta_IA, and G3=C3+Delta_IA are invariant, with ranks 4, 20, 20, and the candidate quotient has dimension 44. The q-sensitive source transforms by the multiplier and the -I q=3/q=infinity defect remains nonzero.

A subsequent small representative audit was executed and CI-verified: run `35416952791`, commit `12805fe1a2486a4ba234b2607bf197468cd48a7a`.

The representatives identity, -I, e1 -> e1+e2, and diag(2,1,2,1) were tested using both L_c=phi_c o g and L_c=g o phi_c. For all cases: first-layer IA variation rank = 20; q=3/q=infinity change laws agree exactly; all 276 first-layer composition pairs have zero defect modulo C3; the quotient remains 44-dimensional; every non-identity tested representative has a q-sensitive defect surviving Q3.

This promotes the degree-3 object to a locally verified filtered quotient datum in the frozen convention. It does not yet establish arbitrary free-group coordinate naturality.

### Current gate

The next authorized gate is the quotient-valued defect transformation/composition law on the admissible category, with the GSp multiplier convention explicit.

Do not perform a full rank-4 scan before that law is defined and audited.

The failed linear-only observable, the artificial q=9 H-closure, and preferred-lift repairs remain permanently excluded.


## 12. Quotient-valued q-defect composition law — LOCAL PASS

The absolute normalized relator defect [F_g(R3)-mu(g)R3]_deg3 failed the tested composition law on all 16 controlled ordered pairs and is not promoted.

The q-sensitive object is
Delta_q(g) = [delta_3(g)-delta_infinity(g)] = [F_g(X1^3)-X1^3]_deg3.

For F_(gh)=F_g o F_h, the candidate quotient law is
Delta_q(gh)=Delta_q(g)+g·Delta_q(h)
in Q3=A3/(C3+Delta_IA).

CI run 35417325110: PASS.
- gauge rank 20;
- dim Q3=44;
- 16 ordered pairs tested across identity, -I, standard transvection, and multiplier-2 diagonal;
- candidate-law failures modulo Q3 = 0;
- raw candidate-law failures = 16;
- all 16 composed q-defect classes nonzero.

The reversed action/order diagnostic also passes modulo Q3 on this four-representative set, so uniqueness of the action/order convention is not established by this control.

Current status: the q-sensitive quotient-valued cocycle law is a **local PASS**, not a theorem-level canonicality result.

Next gate: independently fix the action/order convention, extend to a broader structured representative family, verify multiplier-2 GSp compatibility, then consider broad rank-4 coverage. No full rank-4 scan yet.


## 13. Corrected quotient-valued q-defect cocycle audit

The earlier run 35417325110 is INVALIDATED because its defect helper had the reference-relator sign reversed. It must not be cited as evidence.

Corrected run 35418122079, commit bb39ed1a7191aeae0da07813e40abe47695d292a: candidate Delta_q(gh)=Delta_q(g)+g·Delta_q(h) passes for all 16 ordered pairs of the four controlled representatives in Q3. Gauge rank 20, Q3 dimension 44, candidate failures modulo Q3 0, raw failures 0. The reversed diagnostic has 2 failures modulo Q3, so the action/order convention is distinguished on this control set. 11 composed q-defect classes survive Q3.

Current gate: broader structured representative-family audit of the fixed convention and multiplier behavior. No unrestricted full rank-4 scan yet.


## 18A. Broader structured quotient-defect audit — HISTORICAL / EXECUTED

Following the corrected local PASS, a broader but still structured representative family was defined before any unrestricted scan. The family has 9 representatives: identity, -I, two powers of the first hyperbolic-pair shear, two powers of the second hyperbolic-pair shear, a symplectic pair-swap, and two multiplier-2 diagonal GSp representatives. Each matrix is independently checked against g^T J g = mu(g), and the free lift is checked against the intended degree-1 matrix.

The planned audit covers all 81 ordered pairs for the corrected law Delta_q(gh)=Delta_q(g)+g·Delta_q(h) in Q3, plus the reversed convention as a diagnostic.

Script: research/rank4_D4_ia_structured_defect_composition_audit_2026-09-19.py
Workflow: .github/workflows/rank4-d4-ia-structured-defect-composition.yml

Status: PREPARED / EXECUTION PENDING. This is not a PASS and does not authorize a full scan yet.


## 18B. Broader structured quotient-defect audit — HISTORICAL / PASS AS IMPLEMENTATION CHECK

CI run 35418319144, run #3, head commit dc28f6756c74ea57ae97735bcc96ec3cd1c74a35, workflow .github/workflows/rank4-d4-ia-structured-defect-composition.yml.

The 9-representative structured family was executed over all 9^2=81 ordered pairs. The audit independently checked the stated GSp multipliers and lift degree-1 matrices.

Exact output:
- family size = 9;
- pairs tested = 81;
- matrix GSp checks = 9;
- gauge rank = 20;
- dim Q3 = 44;
- candidate law: Delta_q(gh)=Delta_q(g)+g·Delta_q(h);
- candidate-law failures modulo Q3 = 0;
- candidate-law raw failures = 0;
- reversed diagnostic failures modulo Q3 = 18 (raw = 18);
- nonzero composed defect classes = 60;
- multiplier-2 representatives included and reported with multiplier 2.

Therefore the structured-family gate PASSES / CI VERIFIED for the frozen action/order convention. The reversed diagnostic is nonzero on 18 pairs, providing additional evidence that the chosen convention is not merely coincidentally reproduced by the tested family.

Scope remains explicit: this does not establish full GSp4 covariance, arbitrary free-group coordinate naturality, or canonicality of the quotient datum. It authorizes consideration of a still-broader rank-4 scan only after critical review of the implementation and conventions. The unrestricted full scan is not itself recorded as completed here.


## 18C. Critical implementation/convention audit — HISTORICAL / CLOSED AS IMPLEMENTATION CHECK

Final CI run 35418900971, head 0c4a3d7e454ad9d5b04df2e9b3650872b90d943b.

The pre-scan audit verified 9/9 GSp identities, every matrix_to_lift degree-1 matrix, and all 81 ordered pairs under the frozen column composition convention. Gauge rank 20, Q3 dimension 44, frozen raw Delta_q cocycle failures 0 raw / 0 modulo Q3, reversed diagnostic failures 18, and 60 surviving composed classes were confirmed.

Temporary multiplier-factor and normalized-cocycle variants failed and were rejected. The frozen raw law remains authoritative.

Decision: critical implementation/convention audit PASS / CLOSED. This does not establish full GSp4 covariance or canonicality. A broader scan may now be considered only with explicit scope and PASS/FAIL consequence.


## 0C. Rank-2 relator-unit closure scope correction — 2026-09-19

The previous Rank-2 closure wording is narrowed by critical review. The explicit lift-kernel witness proves failure of the **specific proposed relator-unit scalar construction** on the natural canonical abelianized rank-one quotient
\[
Q=(R/[R,F])/H_2(G_3,\mathbf Z_3)\cong3\mathbf Z_3e_1.
\]
It does **not** prove that every possible construction from the full relation module \(R/[R,F]\), or every other filtered relation-module quotient, is impossible.

Authoritative scope:
- proposed scalar construction: **FAIL / CLOSED**;
- natural quotient repair: **FAIL / CLOSED**;
- broader relation-module strategy: **NOT DISPROVED**, and may be reconsidered only through a fresh intrinsic definition gate.

No finite scan is authorized for the failed scalar construction. The next authorized branch is the independent bridge audit between
\[
ge_1=\mu(g)e_1
\]
and the canonical orientation character \(\chi\). No equality or recovery statement is assumed.


## 2026-09-19 — Critical correction: relation-module rank-one objection withdrawn

A further literature/structural audit found that the preceding “R/[R,F] is not rank-one because H_2(G,Z_3) contributes an extra component” argument was incorrect for this one-relator pro-p presentation. Standard Demushkin deformation literature explicitly uses that when the relation subgroup is normally generated by one relator, the relation module R/[R,F] is Z_p, and in the q != 0 case it maps into F^ab with index q. Thus for r_3=x_1^3[x_1,x_2], the map R/[R,F] -> F_ab sends a chosen generator to 3e_1 and is injective.

Accordingly:
- the earlier claim that the q=3 relation module itself has an unavoidable extra H_2 component is **WITHDRAWN**;
- the natural quotient Q=M/H_2(G_3,Z_3) is not needed for the argument and should not be treated as the canonical object;
- the explicit lift-kernel witness is stronger in the corrected setting: because M is already rank one and its image is 3e_1, the stabilizing lift alpha_{r_3} acts by 4 on M itself (mod 9), not merely on an auxiliary quotient.

The lift-independence FAIL therefore remains, and indeed becomes cleaner: the proposed scalar attached to a chosen stabilizing free lift does not descend to Aut(G_3). No mod-9/IA scan is authorized for this construction.

This correction supersedes the immediately preceding “non-rank-one relation module” discussion, but does not reopen the failed lift-independent scalar route.


## 0D. Orientation bridge audit — 2026-09-19

A hand derivation now separates the project’s \(\mu\) condition from the canonical orientation \(\chi\). For q=3, the torsion subgroup of \(G^{ab}\cong\mathbf Z_3^3\oplus\mathbf Z/3\) gives a canonical line whose Frattini image is the frozen \(e_1\)-line. For actual automorphisms, functoriality of \(\chi\) forces the x2 diagonal coefficient to be 1 mod 3. Under the frozen generator-side GSp convention this makes the GSp multiplier equal to the scalar on the torsion line.

This gives a conditional intrinsic interpretation of \(\mu\) on the actual automorphism image, but **does not identify \(\mu\) with \(\chi\)**. The domains differ, and q=3 has \(\chi(G)\subset1+3\mathbf Z_3\), hence trivial reduction mod 3.

Status: **PASS for the type/domain separation and conditional intrinsic interpretation; OPEN for the recovery bridge \(\mu\to\chi\).** No finite scan yet.


## 0E. MU-CHI bridge definition gate — 2026-09-19

Manual proof completed.

- **PASS:** the \(e_1\)-line is intrinsic as the Frattini image of \(\operatorname{Tor}(G^{ab})\cong\mathbf Z/3\).
- **PASS:** actual automorphisms preserve the line and define \(\mu_{\mathrm{int}}:\operatorname{Aut}(G)\to\mathbf F_3^\times\).
- **PASS:** under the frozen matrix/pairing convention, \(\mu_{\mathrm{int}}\) equals the degree-one GSp multiplier on the actual automorphism image.
- **FAIL:** direct \(\mu=\chi\) and \(\mu=\chi\bmod3\).
- **OPEN:** existence of a deeper dualizing-module construction relating \(\chi\) plus additional canonical data to \(\mu_{\mathrm{int}}\).

No finite scan is authorized at this stage. Next hand task: inspect the dualizing module for a canonical finite quotient carrying \(\mu_{\mathrm{int}}\), or prove that no such canonical quotient arises from \(\chi\) alone.


## 2026-09-19 — Dualizing top-line convention audit

Frozen (g) is on the generator/(H_1) side. Hence the induced (H^1) action is (g^{-T}), and the induced (H^2) scalar is (
u(g)^{-1}). For (p=3), (mathbf F_3^	imes={pm1}), so inversion is identical: (mu_{H^2}=mu_{
m int}) as (mathbf F_3^	imes)-valued characters, although conceptually the cohomological action is inverse. This does **not** identify (mu) with the full orientation (chi:G	omathbf Z_3^	imes); (chimod3) is trivial. The MU-CHI bridge is therefore conceptually resolved: (mu) is a canonical automorphism-of-duality-line shadow, not the orientation character. No finite scan is authorized. Next work should target filtered/graded data retaining the (1+3mathbf Z_3) orientation layer.

## 0B. 2026-09-19 — Mod-9 Bockstein candidate: FAIL / CLOSED

The explicit hand audit is recorded in `research/ORIENTATION_MOD9_BOCKSTEIN_AUDIT_2026-09-19.md`.

The canonical coefficient sequence
\[
0\to\mathbf F_3\xrightarrow{3}\mathbf Z/9\to\mathbf F_3\to0
\]
gives an intrinsic Bockstein
\[
\beta:H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3).
\]
For the frozen relation \(x_1^3[x_1,x_2][x_3,x_4]\), the Bockstein detects the unique power-term direction: \(\beta(\gamma_1)\neq0\) and \(\beta(\gamma_i)=0\) for \(i=2,3,4\), up to the fixed top-class convention.

This passes intrinsicity: no preferred free lift is used, and the map itself is invariant under coefficient-coordinate choices. However, its invariant content is the q=3 power/torsion shadow. A scalar coordinate depends on the choice of generator of the one-dimensional \(H^2\) target, and the Bockstein contains no canonical value corresponding to
\[
\chi(x_2)\equiv4\pmod9.
\]

Therefore:
- M9-A (canonical object): **PASS**
- M9-B (intrinsicity): **PASS**
- M9-C (canonical recovery of the first orientation digit): **FAIL**
- M9-D (comparison with \(\chi\bmod9\)): **CLOSED for this candidate**

This is not a universal impossibility result for all finite-coefficient constructions. It closes only the ordinary mod-9 Bockstein candidate as a recovery mechanism. No finite scan is authorized.

## 0C. 2026-09-19 — Twisted mod-9 orientation carrier: PASS / factorization OPEN

The first genuinely successful orientation carrier has now been identified.

For \(\rho:G\to1+3\mathbf Z/9\), write
\[
\rho(x_i)=1+3a_i.
\]
The canonical finite-level condition is surjectivity of
\[
H^1(G,I_2(\rho))\to H^1(G,I_1(\rho)).
\]
For the frozen relation, the twisted cocycle calculation yields the necessary and sufficient condition
\[
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4=0
\]
for every mod-3 cocycle vector. Thus surjectivity holds uniquely for
\[
(a_1,a_2,a_3,a_4)=(0,1,0,0),
\]
so
\[
\rho(x_2)=4\pmod9.
\]

This is a **PASS for intrinsic twisted-coefficient recovery of \(\chi\bmod9\)**.

It is **not yet a PASS for recovery from filtered/graded data**. The new gate is whether the twisted-surjectivity object factors through the prescribed weak filtered/graded datum without importing the full presentation/group structure.

No finite scan is authorized.

## 0D. 2026-09-19 — Twisted orientation factorization gate OPEN

The first successful orientation carrier is the twisted H^1 surjectivity criterion, which uniquely recovers
\[
\chi(x_2)\equiv4\pmod9.
\]

The remaining task is not another numerical computation. It is a factorization/intrinsicity problem.

Write
\[
\rho=1+3\lambda\pmod9,
\qquad \lambda\in H^1(G,\mathbf F_3).
\]
The frozen cocycle calculation gives the first-order obstruction
\[
B_\lambda(f)=(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]
The canonical \(\lambda\) is the unique zero.

The candidate filtered carrier is the first restricted/Zassenhaus layer containing:
- degree-one \(V\);
- the degree-two Demuškin pairing;
- the q=3 degree-three power contribution;
- the induced first-order twisted derivation obstruction.

Gate requirements F1–F5: intrinsic definition, presentation/lift independence, automorphism naturality, uniqueness, and factorization through the allowed filtered/graded datum.

No finite scan is authorized until F1–F5 are hand-proved.

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

The next F5 hand audit is recorded in `research/ORIENTATION_MOD9_FILTERED_FACTOR_F5_AUDIT_2026-09-19.md`.

A key correction was established from the repository's independent q=3 versus q=infinity degree-3 calculation:
[
operatorname{in}_3(s_3)-operatorname{in}_3(s_\infty)=X_1^{[3]}.
]
Hence the q=3 power information is already present in restricted/Zassenhaus degree 3. The earlier claim that it necessarily disappears upon passing to the associated graded restricted object is withdrawn/narrowed.

The minimal plausible carrier is
[
D_3=(V,R_2,P_3),
]
where (V) is degree one, (R_2=[X_1,X_2]+[X_3,X_4]) is the degree-two Demuškin relation, and (P_3) is the degree-three restricted-power contribution.

Decision:
- **F5-A carrier existence: PASS.**
- **F5 canonical obstruction reconstruction: OPEN.**

The remaining issue is genuinely structural: construct (operatorname{Defect}(P_3)) and (operatorname{Twist}_\lambda(R_2)) intrinsically on (D_3), prove their sum is the verified
[
B_\lambda(f)=(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4,
]
and establish presentation/isomorphism naturality and uniqueness.

No finite scan is authorized.

## 0E. 2026-09-19 — F5 structural reconstruction: PASS for enriched relation jet

The open structural reconstruction is resolved at the exact carrier level. Let
\[
J_3=\langle(R_2,P_3)\rangle\subset L_2\oplus L_3^{res}\]
be the degree-3 relation jet, with common scalar ambiguity retained. The intrinsic obstruction is
\[
\Theta_{R_2,P_3}(\lambda)(f)=f(P_3)+(\lambda\wedge f)(R_2).
\]This is exactly the verified B_\lambda in frozen coordinates. Common rescaling changes only the scalar representative, not the zero set. Automorphism/isomorphism naturality follows from evaluation and exterior-power functoriality. Since R_2 is nondegenerate, the zero is unique and equals \(\lambda_\chi=(0,1,0,0)\), hence \(\rho=(1,4,1,1)\bmod9\).

Decision:
- **F5 structural factorization through enriched relation jet \(D_3=(V,J_3)\): PASS.**
- **Bare unmarked associated graded object:** no claim yet that it canonically reconstructs the distinguished relation jet. This is now the only remaining structural boundary of this branch.

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

The remaining bare-graded identification question is closed without computation. Compare the q=3 and q=infinity rank-4 Demushkin groups. Their defining relators have the same p-Zassenhaus initial form R_2=[X_1,X_2]+[X_3,X_4], because x_1^3 has degree 3 whereas the commutators have degree 2. Standard graded-presentation results therefore give the same bare associated graded restricted Lie object in the two cases.

But chi_3(x_2)=4 mod 9 and chi_infinity(x_2)=1 mod 9. Hence no invariant of the bare associated graded restricted Lie object can recover chi mod 9 in this class. The marked degree-3 relation jet J_3=< (R_2,P_3) > contains extra coupling information that the bare graded object does not retain.

This sharpens F5-A rather than contradicting it: P_3=X_1^[3] exists in the ambient degree-3 restricted layer, but the bare graded object does not canonically mark it as the higher component of the same defining relation as R_2.

Final status of this branch: F5-marked PASS; F5-bare FAIL / CLOSED. The original recovery theorem is therefore false for the bare associated graded restricted Lie object. Recovery remains valid for a richer filtered/graded datum carrying the relation-jet coupling (or an equivalent extension invariant).

Detailed audit: research/ORIENTATION_MOD9_FILTERED_FACTOR_F5_BARE_OBSTRUCTION_2026-09-19.md.
No finite scan is authorized.


## 2026-09-19 — Minimal enriched carrier: projective relation jet

After closing F5-bare, the next task is to identify the weakest natural enrichment that can still recover chi mod 9. The candidate is the projective degree-3 relation jet J_3=< (R,P) > in L_2 direct-sum L_3^res, retaining the coupling between the quadratic relation R and its degree-3 filtered component P while forgetting common scalar normalization.

The construction Theta_J(lambda)(f)=f(P)+(lambda wedge f)(R) is sufficient: for nondegenerate R it has a unique zero, and in frozen coordinates R=[X_1,X_2]+[X_3,X_4], P=X_1^[3] gives lambda_chi=e_2^*. The q=3 versus q=infinity obstruction proves that some information beyond the bare graded object is necessary.

Important boundary: sufficiency is established conditional on J_3 being supplied. Intrinsicness/presentation-independence of J_3 is the new E1-E5 structural gate. Do not call J_3 mathematically minimal yet; only the weaker necessary lower bound is justified.

Detailed plan: research/ORIENTATION_MOD9_MINIMAL_ENRICHED_CARRIER_2026-09-19.md.
No finite scan is authorized.


## 2026-09-19 — E1 relator-gauge audit: local PASS / full intrinsicness OPEN

A no-scan structural audit exposed a necessary correction to the projective relation-jet proposal. Relator conjugation changes the degree-3 component by P -> P+[V,R], so projectivization alone does not establish presentation independence. However the twisted recovery functional is insensitive to this change because degree-one f annihilates ordinary brackets: f([v,R])=0. Thus Theta and its zero set survive conjugation.

Status: E1-local gauge compatibility PASS; E1-full intrinsic definition OPEN. The projective jet must be replaced, if necessary, by its complete relation-gauge class. The next gate is to identify the canonical relation-module object that captures all legitimate relator changes.


## 2026-09-19 — E1 relation-module candidate

To absorb all relator-conjugation gauge at the source, the next candidate carrier is the filtered relation module R/[F,R] for a minimal free presentation 1 -> R -> F -> G -> 1. The degree-(2,3) relation jet should be obtained from its filtered image in L_2(F) direct-sum L_3^res(F).

Status remains OPEN: this is not yet an abstract-group invariant because presentation-independence has not been proved. E2/E3 are therefore not closed.


## 2026-09-19 — CURRENT GATE UPDATE: E1–E5 mod-9 recovery CLOSED / PASS

The degree-(2,3) enriched relation-jet route has now been closed by a no-scan hand audit. The invariant needed for recovery is the projective/gauge class as seen by
\\[
\\Theta_J(\\lambda)(f)=f(P)+(\\lambda\\wedge f)(R).
\\]
Under minimal-cover/lift changes the jet changes only by common unit scaling and the gauge [v,R], which is annihilated by degree-one evaluation. Thus the zero set is intrinsic, conditional on standard minimal one-relator pro-3 presentation facts and the frozen filtered convention. Automorphism naturality, q=3/q=infinity separation, and recovery of chi mod 9 are all PASS.

This is a substantive endpoint: the projective degree-(2,3) enriched carrier recovers \\(\\chi\\bmod9\\) without putting q into the datum definition. The bare associated graded restricted Lie object remains impossible for this task. Full chi and higher mod-3^n reconstruction remain OPEN; no finite scan is authorized.

Detailed audit: research/ORIENTATION_MOD9_E1_E5_CLOSURE_HAND_AUDIT_2026-09-19.md.


## 2026-09-19 — Full 3-adic orientation: hand derivation PASS

The mod-9 result was pushed further by a no-scan exact crossed-derivation calculation using the standard commutator convention [x,y]=x^{-1}y^{-1}xy. For rho:G->1+3Z_3, evaluating a rho-crossed derivation on r=x_1^3[x_1,x_2][x_3,x_4] forces r_1=r_3=r_4=1 and then 1+2r_2=0. Hence
\\[
\\boxed{\\chi(x_2)=(1-3)^{-1},\\quad \\chi(x_i)=1\;(i\\ne2).}
\\]
Modulo 3^n this gives the complete tower rho_n(x_2)=(-2)^{-1} mod 3^n; e.g. 4 mod 9, 13 mod 27, 40 mod 81, 121 mod 243.

The key distinction is now fixed: the degree-(2,3) projective relation jet recovers the first nontrivial digit mod 9, while the compatible full filtered relation-jet tower recovers the entire 3-adic character. No new independent higher obstruction is needed for this q=3 normal form. The bare associated graded object remains insufficient, and finite-jet minimality remains open.

The exact hand derivation uses the standard intrinsic crossed-derivation characterization of the canonical Demushkin orientation. External classification/orientation references confirm the standard formula chi(x_2)=(1-q)^(-1) for the q-power normal form. Detailed audit: research/ORIENTATION_FULL_3ADIC_HAND_DERIVATION_2026-09-19.md. No finite scan was used.


## Carrier-category endpoint — 2026-09-19

The categorical minimality branch has been resolved at the natural quotient level. Degree-(2,3) relation carriers are taken modulo projective/gauge equivalence, with the full degree-one evaluation family Theta required to factor. The canonical quotient
\[
L^{res}_3(V)/[V,L_2(V)]\cong V^{(1)}
\]
removes exactly the degree-3 information invisible to Theta. The compressed carrier
\[
\overline J_3=[(R,p(P))]
\]
is terminal/coarsest among functorial quotient carriers preserving all Theta observables. Therefore the raw J_3 is not minimal in this category. Absolute minimality among arbitrary non-quotient carriers remains undefined without additional independent category axioms.

Record: research/ORIENTATION_MOD9_CARRIER_CATEGORY_COARSEST_QUOTIENT_2026-09-19.md


## Exact Z_3 carrier boundary — 2026-09-19

The fixed-q=3 exact branch was audited for a direct analogue of the mod-3 coarsest carrier. The characteristic-3 restricted-Lie quotient cannot be naively transported to Z_3. The exact natural object is instead the filtered relation carrier together with its coefficient-level crossed-derivation evaluation family. Exact projective/gauge invariance remains valid, and full chi recovery remains closed.

The remaining exact categorical question is whether that coefficient-evaluation quotient has a concrete non-tautological finite description analogous to the mod-3 pair ([R],p(P)).

Record: research/ORIENTATION_EXACT_Z3_COMPRESSED_CARRIER_AUDIT_2026-09-19.md


## AUTHORITATIVE UPDATE — 2026-09-19 — METHODOLOGY SUFFICIENCY / MISSING-TOOL GATE

The current methodology is sufficient for a bounded theorem program, but not yet sufficient for the stronger intrinsic-minimal-carrier objective without three structural bridges:

- **M1:** intrinsic carrier functor from filtered/augmentation-relation data;
- **M2:** non-tautological natural factorization from that carrier to finite-level crossed-derivation/orientation data;
- **M3:** independent comparison map/factorization, or obstruction, relating the carrier to the Pál–Quick A3/Hochschild invariant.

This is now an explicit gate against blind computation. Pál–Quick's process demonstrates the safer order canonical object -> obstruction -> computation; branches in this project must not reverse this into computation -> hoped-for interpretation.

The IA/filtered-extension and W/U/O branches are subordinate: local PASS results do not authorize further scans unless they produce a bridge to M1/M2/M3. The required pre-computation tests are object, input, functoriality, gauge, orientation, q-blindness, separation, novelty, and stop-on-failure.

Record: `research/METHODOLOGY_SUFFICIENCY_AND_MISSING_TOOLS_AUDIT_2026-09-19.md`.


## AUTHORITATIVE UPDATE — 2026-09-19 — RESEARCH CONTINUITY PROTOCOL

The project now has an explicit cross-chat continuity contract:
`research/RESEARCH_CONTINUITY_PROTOCOL.md`.

The protocol freezes the restoration order (RESEARCH_MAP -> CURRENT_STATE -> RESEARCH_LOG -> relevant stage document), the pre-computation tests, theorem-quality thresholds, PASS/FAIL/OPEN/CONDITIONAL/HISTORICAL classification, publication-discipline test, and the rule that literature papers contribute reusable methodology only after object/input/invariance/verification/logical-boundary transfer is explicitly recorded.

This is a methodological control, not a new mathematical result. It exists to ensure that future sessions cannot silently change definitions, revive closed branches, confuse validation with novelty, or lose the stage-specific PASS/FAIL consequences.

The current principal program remains D0 definition -> D1 intrinsicity -> D2 orientation bridge -> D3 carrier/coarseness -> D4 independent comparison. No broad scan is authorized merely by opening a new chat.


## AUTHORITATIVE UPDATE — 2026-09-20 — HIGHER BOCKSTEIN / P-ADIC DIGIT TOWER HARD ATTACK

The next proposed cohomological lift was attacked before computation. Higher Bocksteins are retained as a possible obstruction language, but their existence does not by itself provide a q-blind character-valued factorization. Candidate-twisted coefficient systems already contain the unknown orientation and therefore cannot be used as the sought filtered input. For the frozen q=3 case, exact Fox lifting shows the higher digits are recursively forced by the same unit equation after the first mod-9 digit; this does not identify an intrinsic filtered source of those digits.

Current target remains: prove or disprove a non-circular functorial reconstruction from full filtered relation extension data to the exact Fox obstruction tower. If the input is only associated-graded data, an extension-data obstruction is expected and must be tested explicitly. Detailed audit: `research/ORIENTATION_HIGHER_BOCKSTEIN_HARD_ATTACK_2026-09-20.md`.


## AUTHORITATIVE UPDATE — 2026-09-20 — FILTERED EXTENSION VS ASSOCIATED GRADED BOUNDARY

The phrase “full filtered tower” is now split into two non-equivalent notions. The associated-graded tower loses extension/gluing data and cannot be claimed to recover the exact Fox coefficients. An actual compatible filtered-quotient tower can reconstruct the completed relation by inverse limit, after which Fox reconstruction is formal/continuous; this is not yet a nontrivial compression result. The research target is therefore an intermediate q-blind, presentation-natural carrier retaining enough extension data for all $3$-adic digits but strictly less than the full completed Fox/presentation object.


## AUTHORITATIVE UPDATE — 2026-09-20 — CONSOLIDATED PROGRAM / CURRENT GATE

The complete refined research map is frozen in research/RESEARCH_PROGRAM_SYNTHESIS_2026-09-20.md.

The logical spine is now explicitly:
\[
\operatorname{gr}_3G\;\text{(q-blind)}\;\Rightarrow\;\text{FAIL},
\]
\[
\overline J_3=[(R,p)]\Rightarrow\chi\bmod9\;\text{PASS},
\]
\[
J_{27}\Rightarrow\chi\bmod27\;\text{OPEN / NEXT},
\]
\[
\{J_{3^n}\}_{n\ge2}\Rightarrow\chi\;\text{OPEN},
\]
while the literal full filtered extension tower recovers chi by inverse limit only in a formal/non-compression sense, and the exact Fox carrier recovers chi directly.

The target is therefore an intermediate intrinsic extension carrier: q-blind, presentation-natural, non-circular, sufficient for the relevant finite 3-adic digit, and genuinely smaller than the completed Fox/presentation object if it is claimed as a compression.

Important negative boundaries already closed: naive Z_3 augmentation jet; naive Z_3 restricted-Lie scalar extension; intrinsic degree-3 Fox truncation; higher-Bockstein-alone reconstruction; full associated-graded reconstruction; bounded-degree + bounded-precision universal recovery; quotient compression of the exact local Fox algebra.

Important claims NOT made: P_3 is information-theoretically minimal; full Fox is categorically/absolutely minimal; full orientation universally requires characteristic-zero data in every possible carrier category.

### NEXT GATE — MOD 27

Construct or rule out an intrinsic J_27 satisfying: q-blind independent input; presentation/Nielsen/relator-gauge invariance; separation of chi mod 27; natural reduction to J_9; non-tautological definition; and genuine compression if advertised.

No broad scan is authorized before these object-level gates are passed.

 
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


## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 18: MOD-27 BOCKSTEIN CARRIER CLOSED BY INTERNAL SYMMETRY

The coefficient-extension candidate
\[
\mathcal B_{27}=(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),\mathrm{red},\iota,\smile,\beta_1,\beta_9)
\]
fails the carrier-level automorphism test. For the frozen \(q=3\) object,
\[
(a_1,a_2,a_3,a_4)\mapsto(a_1,4a_2,a_3,a_4)
\]
preserves all declared structure but changes the characteristic-zero lift of the mod-3 \(e_2\) direction. Since the desired logarithmic digit is \(e_2\pmod9\), the carrier lacks the rigidification required for a natural mod-27 bridge.

Decision:
- **MOD-27 Bockstein-extension carrier as orientation carrier: FAIL / CLOSED;**
- intrinsic coefficient-extension/q-layer detector: **PASS / LOCAL;**
- a new mod-27 carrier with additional rigidifying structure: **OPEN.**

This supersedes HARD ATTACK 17. No further numerical scan of the same Bockstein package is authorized.


## AUTHORITATIVE UPDATE — 2026-09-20 — HARD ATTACK 19: CATEGORICAL CORRECTION / REALIZABILITY GATE

Hard Attack 18's unconditional Bockstein no-go is superseded. Its symmetry
\[
S(a_1,a_2,a_3,a_4)=(a_1,4a_2,a_3,a_4)
\]
is an automorphism of the abstract declared carrier, but admissibility as a morphism induced by the group-level input was not proved. An abstract carrier automorphism only yields a naturality obstruction if the bridge is required to be natural for that morphism.

The next gate therefore separates:

1. \(\mathcal C_{27}^{\mathrm{abs}}\): abstract structured carriers and all structure-preserving isomorphisms;
2. \(\mathcal C_{27}^{\mathrm{real}}\): carriers with morphisms actually induced by admissible group isomorphisms/gauges of the declared filtered/relation input.

Decision:
- Hard Attack 18 absolute no-go: **HISTORICAL / SUPERSEDED**;
- S as abstract-carrier symmetry: **PASS / LOCAL**;
- Bockstein q-layer detector: **PASS / LOCAL**;
- Bockstein mod-27 orientation carrier: **CONDITIONAL / OPEN**.

Hard Attack 19 target: determine whether S is realizable. If realizable, test its action against the intrinsic orientation and close the carrier. If not realizable, identify the precise q-blind datum preventing realization; reject it as a new rigidifier if it is equivalent to hidden q/chi/classification/Fox information. No further numerical scan is authorized before this gate is resolved.


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


## 2026-09-20 — ACTIVE: FINITE EXTENSION / 2-CELL CARRIER REFINED

The extension-carrier branch is now precise. For N=P_{k+1}(G), Q_k=G/N, the first finite extension datum is M_k=N/(N^{3^k}[N,N]) together with E_k=G/(N^{3^k}[N,N]). This is q-blind and intrinsic and captures the kernel data relevant to H^1(N,A_k(rho)).

Hard Attack 27 closes the naive inference that this finite extension already determines twisted H^2: the Hochschild-Serre degree-two terms include H^2(N,A_k(rho)). The next target is therefore not a larger arbitrary carrier, but a finite q-blind 2-cell obstruction T_k naturally extracted from the extension and capable of reproducing the one-relator twisted obstruction without importing the canonical dualizing action.


## 2026-09-20 — ACTIVE: 2-CELL EVALUATION GATE

The finite extension branch now has a canonical class e_k in H^2(Q_k,M_k) and an induced twisted transgression map. The remaining decisive problem is not more quotient depth but whether a distinguished 2-cell evaluation functional can be reconstructed from the finite filtered extension data without importing the Demushkin dualizing/orientation action. This is the current orientation-bridge gate.


## 2026-09-20 — ACTIVE: CHAIN-LEVEL 2-CELL RECONSTRUCTION GATE

The extension branch has reached a sharper boundary. Bare Q_k, kernel extension M_k, canonical extension class e_k, and direct top-class action have all been separated: the first three do not automatically yield the desired orientation, while the last already contains it. The remaining legitimate program is to derive a finite chain-level/extension-level 2-cell invariant T_k from the q-blind filtered extension and prove an independent PD^2 identity to the canonical orientation action. Otherwise a separation counterexample must establish the impossibility within the admissible category.


## 2026-09-20 — DISCOVERY PASS 30: FINITE DERIVED 2-CELL / FITTING CANDIDATE

Hard Attack 29 closed direct top-class enrichment as non-tautological. A new discovery candidate is therefore opened inside the finite extension data itself. For N=P_{k+1}, Q=G/N, M=N/(N^{3^k}[N,N]), E=G/(N^{3^k}[N,N]), and candidate rho:Q→U_k, seek a basis-free finite derived/transgression complex whose kernel/cokernel, Fitting ideal, annihilator, or determinant-line defect supplies the missing 2-cell rigidification. The point is to avoid choosing a generator/evaluation in Hom_Q(M,A_k(rho)).

Immediate attack: a raw scalar Reidemeister/determinant invariant is not canonical because chain bases and coefficient-module scalings change it by units. Thus scalar torsion selector FAIL / CLOSED. A basis-free finite derived/Fitting/annihilator object T_k remains OPEN / decisive. Its identification with the twisted PD^2 obstruction is not established and must not be assumed. No numerical scan is authorized before canonical definition + bridge.

Record: research/KUMMER_FINITE_DERIVED_2CELL_DISCOVERY_PASS_30_2026-09-20.md.


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


## 2026-09-20 — DEFERRED RESEARCH IDEA BACKLOG AFTER COKER BREAKTHROUGH

The recent proposal set was reviewed and recorded separately so that promising directions are preserved without displacing the active main line. Deferred candidates are:
1. compare finite Fox relation residue with the intrinsic extension class/transgression data, first testing whether Fox residue is additional or merely a coordinate realization;
2. formulate the positive result primarily as a finite-level unique-selector theorem, with chi as a PD² corollary;
3. reinterpret coker cardinality as a finite maximality selector;
4. revisit mixed m-adic/bi-filtered constructions only at the definition/naturality level;
5. develop information-transfer efficiency as a higher-level synthesis;
6. postpone minimality of P_{k+1} until an admissible carrier category and the main compatibility theorem are fixed.

Detailed backlog: `research/NEXT_RESEARCH_IDEA_BACKLOG_2026-09-20.md`.

**Immediate main line is unchanged:** strengthen the finite coker theorem and attack k→k+1 compatibility/naturality. Deferred ideas must not be reopened without a new structural reason.


## 2026-09-20 — HARD ATTACK 35: INVERSE-SYSTEM COMPATIBILITY AUDIT

The next attack separates two notions that had been conflated. The finite coker selector is compatible across k at the level of its selected output: under the PD² selector criterion, a level-(k+1) maximal selector reduces to the unique level-k selector. Thus practical inverse-limit reconstruction is PASS / LOCAL under the declared PD² framework.

However, the coker carriers themselves do not automatically form a strict inverse system. Q_{k+1}->Q_k and E_{k+1}->E_k are natural, but M_{k+1} is based on the changing kernel P_{k+2}, while M_k is based on P_{k+1}; the induced map lands only in a generally proper submodule of M_k. Hence no automatic map between the Hom sources, transgressions, or cokernels follows.

Classification:
- naive direct coker-carrier reduction: FAIL / CLOSED as an inference;
- carrier-tower naturality: OPEN / load-bearing;
- finite selector compatibility: PASS / LOCAL under PD² verification;
- practical inverse-limit reconstruction: PASS / LOCAL subject to PD² framework;
- carrier-only inverse-system functoriality: OPEN.

Detailed audit: research/KUMMER_HARD_ATTACK_35_INVERSE_SYSTEM_COMPATIBILITY_AUDIT_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 36: MAIN-BRANCH ENDGAME

The main Kummer branch now has a clean theorem schema:
1. At each finite k, the intrinsic finite extension/transgression coker predicate selects exactly one rho_k.
2. The selected rho_k are compatible under coefficient reduction.
3. Hence the inverse-limit selector set is a singleton, identified with chi_filt.

The strict inverse-system structure of raw carriers is not required for this reconstruction and remains OPEN. Minimality and universal category-independent claims remain OPEN and are explicitly separated from the main theorem.

Stop criterion: do not continue merely to force raw carrier functoriality. Continue only if a new attack can remove PD² dependence from coherence, prove minimality in a defined category, prove strict carrier naturality, or broaden the admissible class.


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


## 2026-09-20 — HARD ATTACK 39: PROFILE COMPLETENESS BOUNDARY

Hard Attack 39 resolves an information-theoretic ambiguity in the phrase "extension class <-> transgression profile". Over the full Q_k-module category, the profile is complete by evaluation at (M_k,id), so no new theorem is hidden there. Over the actual Kummer coefficient family A_k(rho), completeness is a separate faithfulness problem with kernel K_k = intersection_{rho,phi} ker(phi_*).

The active main gate is therefore not recovery of e_k itself, but whether the restricted push-forward/coker profile of e_k has a unique orientation maximizer without PD². This preserves the intended q-blind finite-input problem and sharpens the boundary; no numerical scan is authorized before the restricted-profile theorem is addressed.

Record: research/KUMMER_HARD_ATTACK_39_YONEDA_COEFFICIENT_PROFILE_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 40: SCALAR-CHARACTER SPECTRAL BOUNDARY

The Kummer coefficient family does not probe arbitrary Q_k-module structure. Its equivariant maps factor through twisted coinvariant specializations M_{k,rho}. Hence the finite coker profile is a scalar-character spectroscopy of e_k.

This is a genuine structural boundary but not yet a no-go for the Demushkin extension: the special e_k might be completely visible to these scalar specializations. The active theorem target is therefore a Demushkin-specific scalar-visibility/unique-maximizer result, not generic representation-theoretic faithfulness.

Record: research/KUMMER_HARD_ATTACK_40_RANK_ONE_SPECTRAL_BLINDNESS_2026-09-20.md.


## 2026-09-20 — HARD ATTACK 40 CRITICAL REVIEW / SCALAR-VISIBILITY GATE

The Hard Attack 40 reformulation has been critically audited. Its genuine content is the scalar-character factorization of the restricted Kummer profile through M_{k,rho}; it is not a new obstruction theorem. The Kummer coefficient is rank-one, but M_{k,rho} need not be one-dimensional.

The proposed "maximality as complete filling" interpretation is rejected: C_k(rho)=H^2/im(delta), so larger coker means smaller transgression image (for fixed ambient H^2), and |C_k|=|H^2| means im(delta)=0.

The active next gate is:
intrinsic finite extension -> scalar-character push-forward -> visibility/vanishing criterion -> selector.
At k=2, the first comparison target is the already closed cup+Bockstein degree-(2,3) obstruction. Fitting/determinant machinery remains deferred until it proves genuinely new basis-independent control.

Classification:
- scalar-character factorization: PASS / CLOSED;
- Hard Attack 40 as novelty: HISTORICAL / SUPERSEDED;
- scalar-character visibility of e_k: OPEN / DECISIVE;
- unique scalar-character coker maximizer without PD^2: OPEN / DECISIVE;
- restricted Kummer faithfulness: OPEN / AUXILIARY;
- PD^2-based selector: PASS / LOCAL;
- Fox coordinate realization: OPEN;
- Fitting/determinant: OPEN / DEFERRED;
- carrier minimality and strict tower naturality: OPEN.

Record: research/HARD_ATTACK_40_CRITICAL_REVIEW_AND_NEXT_GATE_2026-09-20.md.


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

The Strategic Reset tests were executed.

1. Information-depth boundary. On the standard family G_{3^s} versus G_infty, the sharp comparison thresholds are D_{3^s+1} for the Zassenhaus filtration and P_{s+2} for the lower-3-central filtration. Consequently, for χ mod 3^n in the worst case s=n−1, the family-level boundaries are D_{3^{n−1}+1} and P_{n+1}; mod 27 gives D_10 and P_4. Classification: PASS / LOCAL. This is not yet a universal pointed orientation-recognition theorem.

2. Layer-B tower reuse. The mod-9 carrier [(R,p)] remains PASS / CLOSED. No theorem currently proves that this fixed carrier recursively generates all higher 3-adic digits. The mod-27 Bockstein-extension package is a finite q-layer detector, but its independent orientation bridge remains unresolved. Classification: tower reuse OPEN / DECISIVE; Bockstein package as all-digit carrier CONDITIONAL / OPEN.

3. Strategic consequence. The 19D permanent LHS piece is not yet justified as the first genuinely new orientation layer. The next authorized target is the mod-27 threshold residual: finite extension data at P_4 or D_10 modulo the already established Layer-B information. If the residual vanishes, this supports collapse/reuse; if nonzero and it admits a natural orientation bridge, it identifies the first genuinely new layer.

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


## 2026-09-20 — HARD ATTACK 59: COKER REINTERPRETED AS UNIVERSAL OBSTRUCTION QUOTIENT

The “why coker?” conceptual attack was executed. The critical correction is that the coker itself is not the orientation invariant. Its structural role is the universal quotient that removes gauge/lift directions before an intrinsic obstruction is evaluated.

For a raw deformation/obstruction space C and gauge image im(d), the quotient C/im(d)=coker(d) is universal for maps annihilating im(d). At mod 9, the established twisted degree-(2,3) obstruction family is precisely of this type: presentation/lift changes are invisible, so the obstruction factors through the quotient, while the orientation is selected by the zero/lifting condition of the resulting functional.

Thus the correct conceptual chain is
\[
\text{raw relation/power data}\to\text{gauge quotient/coker}\to\text{intrinsic obstruction carrier}\to\text{orientation selector}.
\]

This explains the coker structurally without claiming that “coker = orientation.” The latter interpretation is rejected as overstrong.

The same pattern suggests a precise successive-obstruction hypothesis for P_4: a next raw extension datum should have its own gauge image, intrinsic quotient, and twisted coefficient-extension obstruction, with a reduction map to the established mod-9 obstruction. If such a diagram commutes, the P_4 scalar may be forced by functorial compatibility rather than imported from q or the known orientation formula.

A decisive negative test is also identified: if the same intrinsic P_4 projective residual admits two scalar normalizations compatible with all allowed gauge changes and with the same mod-9 reduction, then the P_4 filtered data plus Layer B cannot determine the normalized digit.

Decisions:
- coker as universal gauge-obstruction quotient: **PASS / LOCAL**;
- coker itself as orientation carrier: **FAIL / CLOSED**;
- mod-9 carrier as obstruction quotient + natural functional: **PASS / CLOSED** under the established twisted degree-(2,3) theorem;
- successive obstruction tower: **OPEN / DECISIVE**;
- P_4 reduction-compatibility with mod-9 obstruction: **OPEN / DECISIVE**;
- P_4 scalar normalization from compatibility alone: **OPEN / DECISIVE**.

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


## 2026-09-20 — HA61-B5-14: GLOBAL ZERO-MAP QUANTIFIER CORRECTION

The B5-13 fixed-(f) 27-point argument is superseded as a no-go for the actual selector problem. The target is a lift (ho_3) for which the entire connecting map (delta_{3,ho_3}) vanishes. Conditional on the universal variation identity and surjectivity of the mod-9-to-mod-3 (H^1) reduction, Demuškin cup nondegeneracy implies **global zero-map uniqueness: PASS / LOCAL (conditional)**. This does not prove existence or finite filtered factorization. The active decisive gates are universal variation, finite filtered/relation existence, factorization through (G/P_4\) / (D_{10}), and Serre/Kummer novelty separation. The (t_2), (t_2/\langle p\rangle), and diagonal ((t_2,\mu)) routes remain FAIL/CLOSED; HA61-C remains unopened.

Record: research/HA61_B5_14_GLOBAL_ZERO_MAP_QUANTIFIER_CORRECTION_2026-09-20.md
