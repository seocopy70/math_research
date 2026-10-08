# Paper 5 — Current State Addendum — 2026-10-06

## Active classification

**OPEN / LOAD-BEARING** for the uniform (p^2) automorphism-order-gap theorem.

## Step-3 boundary gate now CLOSED

For the stabilized boundary window (W_{p+1}=W_p), the intrinsic relation package
[
mathcal J_p=(V,D_p,pi,b,L,mathrm{relation})
]
with (V=W_p/D_2(W_p)), (D_p=D_p(W_p)), p-power map (pi), commutator map (b), and canonical central line
[
L=Z(W_p)D_2(W_p)/D_2(W_p)
]
has stabilizer
[
operatorname{Stab}(mathcal J_p)=S'_{11}(p)
=left{egin{pmatrix}m&b&0\0&1&0\a-m&d&aend{pmatrix}:m,a
e0, b,dinmathbf F_pight}.
]
Thus
[
|S'_{11}(p)|=p^2(p-1)^2.
]

The explicit family
[
xmapsto x^m z^{a-m},quad ymapsto x^b y z^d,quad zmapsto z^a
]
realizes every stabilizer element, so
[
operatorname{Im}(operatorname{Aut}(W_p)	o GL(V))=S'_{11}(p).
]
With (IA(W_p)congmathbf F_p^9),
[
|operatorname{Aut}(W_p)|=p^{11}(p-1)^2.
]

### Precision correction

[
rac{|GL_3(mathbf F_p)|}{|S'_{11}(p)|}
=p(p-1)(p+1)(p^2+p+1).
]
Therefore the raw (GL_3)-index does **not** itself give a (p^2) deficit; its p-primary part is only (p). The intrinsic result establishes two free additive parameters (b,d), not yet the exact (p^2) order ratio of the previously observed comparison.

## Next load-bearing gate

Identify the exact comparison family/windows whose automorphism orders differ by (p^2), and prove that the intrinsic relation-jet restriction above accounts for that ratio.

Evidence: research/PAPER5_WP_INTRINSIC_RELATION_JET_AUDIT_2026-10-06.md.


## 2026-10-06 — Addendum 2: proposed p^2 comparison window rejected as submitted

The proposed identification \(U_p=W_p/L\) and the conclusion
\[
|\operatorname{Aut}(W_p)|/|\operatorname{Aut}(U_p)|=p^2
\]
were audited and are **NOT CLOSED**. The intrinsic line \(L=Z(W_p)D_2/D_2\) is a subspace of \(V=W_p/D_2\), not itself a subgroup of \(W_p\), so \(W_p/L\) requires a separately specified subgroup lift. If one uses \(\langle z\rangle\), the quotient has a 2-dimensional Frattini quotient and therefore cannot simply inherit the same \(S'_{11}\) image or a \(p^7\) IA kernel.

A second type error occurs in the proposed relation condition \(b(\pi(x),y)\): the established \(b\) has type \(b:\wedge^2V\to D_p\), while \(\pi(x)\in D_p\), so this expression is undefined without introducing a new action/pairing. Consequently the claimed \(3\to2\) dimension cut and \(Z^1_{\mathcal J_p}(V,L)\cong\mathbf F_p^2\) remain **OPEN / LOAD-BEARING**.

The CLOSED \(W_p\) intrinsic stabilizer result is unchanged. Detailed audit: research/PAPER5_P2_GAP_COMPARISON_WINDOW_AUDIT_2026-10-06.md.


## 2026-10-06 — Addendum 3: reverse-pi/kernel-cut mechanism rejected

The proposed reverse map \(\pi:D_p\to V\) and the resulting \(3\to2\) IA-kernel cut are **FAIL / CLOSED as a mechanism**. The authoritative intrinsic p-power map is \(\pi_0:V\to D_p\). No canonical reverse map is induced by the p-power operation; moreover \(D_p\) is central of exponent \(p\), so the assignment \(d_{z1}\mapsto v_z\) is extra structure.

There is a stronger obstruction to the proposed second factor \(p\): every IA modification by \(f:V\to D_p\) is invisible to the established intrinsic jet data. If \(d\in D_p\), then \((gd)^p=g^p\) and \([gd,h]=[g,h]\), because \(D_p\le Z(W_p)\) and \(D_p^p=1\). Hence preserving \(\pi_0\), \(b\), \(L\), and the relation cannot cut \(\operatorname{Hom}(V,D_p)\) from dimension 9 to dimension 8.

Therefore \(K_b/K_{\mathcal J}\cong\mathbf F_p\) and the resulting \(p^2\) decomposition are **FAIL / CLOSED for this proposed mechanism**. The exact \(p^2\) automorphism-order theorem remains **OPEN / LOAD-BEARING**. No new CLOSED comparison window has been identified.

## 2026-10-06 — Addendum 4: model-identity correction

A decisive consistency audit found that the current closed W_p calculation and the earlier observed p^2 GAP computation are **not calculations on the same finite group**.

The closed boundary model used in the Step-3 calculation is presented by
\[
[x,z]=[y,z]=1,\qquad [x,y]=x^p z^{-p},
\]
so z is central. In contrast, the authoritative GAP artifact aut_common.g defines, for the actual (s,a)=(1,1),
\[
G=\langle z,x,y\mid z^3=x^3[x,y]\rangle
\]
(and then takes its Zassenhaus window W=G/D_5); there are no defining relations [z,x]=[z,y]=1. Thus the two groups must not be identified merely because their displayed power-commutator relation can be algebraically rearranged.

This resolves the apparent conflict with the certified p=3,n=4 Frattini-image computation, where the actual non-split image has order 6, while the central-model candidate S'_{11}(3) has order 36. The former concerns the actual GAP model; the latter concerns the separately defined central boundary model.

### Classification
- Centralized boundary model W_p: its internal Step-3 results remain valid within that declared presentation scope, subject to their own audits.
- Identification of that model with the actual GAP W producing the observed p^2 gap: **FAIL / CLOSED / SUPERSEDED AS AN ASSUMPTION**.
- Using the central-model J_p no-go to locate the observed p^2 gap: **INVALID / SUPERSEDED**.
- Actual observed p^2 gap mechanism: **OPEN / LOAD-BEARING**.

### Correct next gate
Return to the actual GAP presentation G=<z,x,y | z^3=x^3[x,y]> (and its general p,s,a analogue), reconstruct its finite-window intrinsic relation jet, and identify the embedded Frattini stabilizer that changes from order 108 to 6 in the certified p=3,n=4 split/non-split comparison. The previously proposed central-model IA no-go does not settle this actual problem.


## 2026-10-06 — Addendum 5: proposed actual-model 108→6 stabilizer derivation rejected

The proposed closure via the matrix condition M(R) in <R> is FAIL / CLOSED as a derivation, and the exact actual-model p^2 mechanism remains OPEN / LOAD-BEARING.

Two independent defects were found.

1. The split comparison was misstated. The authoritative research/external/paper5_aut/aut_common.g defines s=0 by G_{0,a}=<z,x,y | x^(p^a)[x,y]=1>, not a relation-free G_{0,0}. The certified split case is (s,a)=(0,1), hence it already has the relation x^p[x,y]=1.

2. The induced action on the degree-p power layer was linearized incorrectly. From an arbitrary M in GL(V), one cannot in general substitute M(d_z)=a d_z+b d_x+c d_y for the image of z^p. If a lift has initial form z -> az+bx+cy, its restricted p-power contains Jacobson/polarization cross terms; v -> v^[p] is not an ordinary linear map V -> <d_z,d_x,d_y>. Therefore the displayed equations c=f, fg=di, dh=eg, etc. have not been established as the actual finite-window automorphism conditions.

The additional assertion that the presentation occurrence of z intrinsically forces b=c=0 is also not a proof: an intrinsic distinguished line in V must be identified from the finite group/window, not from the chosen presentation alone.

### Current classification

- actual GAP data |L_{0,1}|=108, |L_{1,1}|=6, and |IA|=3^27: PASS / LOCAL;
- model mismatch with the centralized boundary model: PASS / CLOSED;
- proposed M(R) derivation of the actual stabilizer: FAIL / CLOSED;
- p^2 gap localized to the Frattini/GL image: PASS / LOCAL;
- exact intrinsic stabilizer for the actual G_{1,1}/D_5: OPEN / LOAD-BEARING.

### Authorized next gate

Reconstruct the actual induced action on V=W/Phi(W) from the certified GAP automorphism generators, express the defining relation as the correct restricted-Lie/Jacobson degree-p relation jet, and only then identify the embedded subgroup of GL_3(3). No 108→6 theorem or Paper 5 END classification is authorized yet.


## 2026-10-06 — Addendum 6: p=3 Jacobson absorption is partial, intrinsic line remains open

For p=3, R=z^[3]-x^[3]-[x,y] is filtered-inhomogeneous in W=G_{1,1}/D_4. Bracketing R with x and y kills the p-power bracket terms in D_4 and forces the surviving degree-3 terms [[x,y],x] and [[x,y],y] to vanish. Thus the Jacobson polarization terms in the p=3 cube expansion are absorbed in the relation quotient. This repairs the specific p=3 restricted-power linearization defect, subject to checking the exact Jacobson convention and signs.

This does not prove that the z-line in V is intrinsically Aut(W)-invariant. Presentation support alone is insufficient. The b=c=0 restriction and exact nonsplit embedded stabilizer therefore remain OPEN until either an intrinsic characterization is proved or the actual six GAP Frattini matrices are extracted and matched directly.

The p=3 absorption argument is not a general odd-p theorem: for p>3 the relevant degree bookkeeping differs.

Classification: p=3 Jacobson absorption = PASS / LOCAL; exact intrinsic stabilizer = OPEN / LOAD-BEARING; p^2 structural theorem = OPEN / LOAD-BEARING; Paper 5 END = NOT AUTHORIZED.


## 2026-10-06 — Final actual-model Gate execution correction

The authoritative p=3 stabilizer gate was audited against CI run 37199037517. The run installed GAP/AutPGrp successfully but the stabilizer calculation aborted before computing the six matrices because Image(alpha,basis[j]) used incompatible GAP source families. The gate has now been corrected to recover Frattini basis elements through PreImagesRepresentative(frnat,v) before applying the automorphism.

The corrected gate also tests the intrinsic line candidate Z(W)D_2/D_2 directly and compares the actual embedded image against both the repository candidate and the user's proposed (z,x,y) subgroup after basis conversion.

Current status: the correction is committed, but post-correction runtime output has not yet been independently recovered. Therefore the exact embedded subgroup and intrinsic z-line remain OPEN / LOAD-BEARING. No Paper 5 END classification is authorized.


## 2026-10-06 — Explicit-R audit correction

The concrete relation subgroup is explicit, and its full degree-two initial layer closes the one-step boundary \(W_{p+1}=W_p\). The proposed reduction of all-n stabilization to \(F^p\subseteq R\) is rejected because the Zassenhaus graded object has restricted p-power contributions; \(L_{k+1}=[L_k,L_1]\) is not a general identity. All-n stabilization remains **OPEN / LOAD-BEARING**.


## Addendum 7 — Gate 0/1/3 persistence certificate

The central-model b-direction and actual (1,1)-family persistence were independently rechecked.

- Central model, p=3: all 36 explicit S'_11(3) automorphisms survive at n=4 and n=10. In particular the b=1 element is x -> x, y -> xy, z -> z.
- Therefore the historical central-model claim G_{p^2} subsetneq G_p via b:x -> xy is FAIL / CLOSED / SUPERSEDED. The denominator strictness RD_{p^2+1} subsetneq RD_{p+1} remains valid and is logically separate.
- Actual G_{1,1}: p=3 gives GL-image orders 864,6,6 at n=3,4,5; p=5 gives 48000,20 at n=5,6.
- The first observed transition is n=p+1, and the next tested window remains at p(p-1).
- The candidate cohomological stabilizer Stab(omega,beta) has order p(p-1), matching these actual values. Uniform equality remains OPEN / LOAD-BEARING until the relator-derived (omega,beta) theorem and reverse realization are closed.
- p=5,n=7 is not yet computed: GAP's p-quotient collector stops at class 6. This is a computational limitation, not a mathematical failure.

Detailed certificate: research/PAPER5_GATE0_GATE3_PERSISTENCE_AUDIT_2026-10-06.md.


## 2026-10-07 — P5-MODEL-1 / P5-COH-1 correction

### Indexing fixed
The GAP window is G/D_n. The free-presentation notation W_m=F/(RD_{m+1}) therefore satisfies W_m=G/D_{m+1}. Thus the relation-jet window called W_p is the GAP window n=p+1. The observed 864->6->6 (p=3) and 48000->20 (p=5) contains the transition G/D_p -> G/D_{p+1}=W_p; it is not evidence for a sequence of distinct post-W_p windows.

### Cohomological gate closed
For r=z^p x^{-p}[x,y]^{-1}, the minimal-presentation relation formula gives, for odd p, omega=x* wedge y* and beta(lambda)=(lambda(x)-lambda(z)) eta, up to the simultaneous sign choice of eta in H^2(G,F_p). Hence the intrinsic stabilizer is S_coh(p)={ [[a,b,0],[0,1,0],[0,0,a]] : a in F_p^*, b in F_p }, with order p(p-1). Naturality of cup product and Bockstein gives Im(Aut(G)->GL(H^1(G,F_p))) subseteq S_coh(p). Classification: PASS / CLOSED / GENERAL for the global upper bound.

### n=p maximal-parabolic interpretation
The local values satisfy |GL_3(F_3)|/864=13=3^2+3+1 and |GL_3(F_5)|/48000=31=5^2+5+1. Thus the observed n=p images have order p^3(p-1)^3(p+1), the stabilizer order of a point/line in P^2(F_p). This remains PASS / LOCAL; an embedded-equality certificate with the canonical <x,y> plane is still a separate subgate.

### Remaining load-bearing gates
The global upper bound does not imply the finite-window upper bound because a finite-window automorphism need not lift to G. The remaining targets are: (1) finite W_p intrinsic upper bound, proved directly from the degree-2 and degree-p relation jet; (2) diagonal realization of every diag(a,1,a) in Aut(G). The b-unipotent realization is already closed. A finite p=3 extraction attempt is not promoted because of coordinate/AutPGrp representation issues.

If both gates close, monotonicity gives the all-window theorem without further n-by-n scanning.

Detailed audit: research/PAPER5_P5_COH1_MODEL_INDEX_AUDIT_2026-10-07.md.


## 2026-10-07 — A2 residual-jet correction

A2 remains OPEN / LOAD-BEARING. The original relator has initial Zassenhaus form r2=[x,y] in degree 2; the degree-p residual jet is therefore defined only after quotienting by J=(r2)_res. The old notation rp in Dp/Dp+1 for the original relator is superseded.

The Jacobson projection to multidegrees (1,0,p-1) and (0,1,p-1) gives ad(z)^(p-1)(u_x) and ad(z)^(p-1)(u_y), respectively. This is consistent with p=3 but still requires a formal residual-jet/no-cancellation proof.

The proposed Hilbert lower bound from cd(G)=2 and H2=1 is FAIL / CLOSED as a proof route. The p=3 values 3,2,8,10 are PASS / LOCAL checks only and are not the coefficients of (1-3t+t^2)^(-1), whose coefficients begin 1,3,8,21,55. The correct route is strongly-free [x,y] -> Labute mildness -> graded presentation, followed by Jennings-Lazard/Jacobson translation.

No A2 CLOSED or p^2 theorem promotion is authorized until the residual-jet projection lemma is rigorously completed.


## 2026-10-07 — A2 hand proof closes the finite-window upper bound

A direct Magnus-algebra proof closes the A2 upper-bound gate, without invoking mildness. Set T=F_p<<xi,eta,zeta>> and I=(r-1), with r=z^p x^(-p)[x,y]^(-1). Every monomial of r-1 either contains eta or has at least p occurrences in the xi/zeta alphabet. Hence I has zero components in multidegrees (1,0,p-1) and (0,1,p-1).

For an automorphism of W_p, choose a free-pro-p lift g~. Since g~(r) lies in R D_(p+1), its Magnus expansion satisfies g~(r)-1 in I+T_(>=p+1). A1 supplies the strong invariant g(<x,y>)=<x,y>, so g~(x),g~(y) have no zeta terms; consequently the commutator factor contributes no zeta multidegrees. The degree-p projections therefore come only from zeta'^p. Writing zeta'=chi zeta+(a-chi)xi+c eta+O(2), the (1,0,p-1) and (0,1,p-1) coefficients are chi^(p-1)(a-chi) and chi^(p-1)c, so a=chi and c=0. With chi=det(g|P)=ad, d=1.

The pure (p,0,0) and (0,0,p) components are not zero in I; they identify the scalar multiple of the degree-p generator and reproduce the beta-compatible coefficient relations. Thus the earlier apparent coefficient ambiguity is resolved.

Classification: **A2 finite-window upper bound = PASS / CLOSED**, assuming the already-closed A1 invariant and standard completed-group-algebra lift/Magnus facts. Gate B diagonal realization remains **OPEN / LOAD-BEARING**; the full Paper 5 p^2 theorem remains **OPEN / LOAD-BEARING**.


## 2026-10-07 — authoritative A2 closure / Gate B handoff

The latest audited hand proof supersedes the earlier same-day A2-OPEN entries in this current file. The finite-window higher-jet upper bound is now **PASS / CLOSED** under the already-closed A1 invariant and standard completed-group-algebra/Magnus lift facts.

Precisely, for an automorphism of the relation-jet window, the strong A1 invariant g(<x,y>)=<x,y> removes all zeta-containing Magnus terms from the x,y images. In the degree-p Magnus projection of the lifted relation, the critical multidegrees (1,0,p-1) and (0,1,p-1) therefore receive contribution only from the p-power of the zeta image. Their coefficients force a=chi and c=0, and the determinant identity chi=ad gives d=1. The pure degree-p components are not zero; they determine the scalar multiple of the relation generator and are compatible with the same beta constraint.

The proof is not being promoted beyond the stated hypotheses; the remaining standard Magnus/completed-group-algebra conventions are to be cited explicitly in the manuscript. This is nevertheless sufficient to close the finite-window A2 upper-bound gate.

### Active Gate B

The only load-bearing research gate is now the **pro-p diagonal realization**: for every a in F_p^*, diag(a,1,a) must lie in the image of Aut(G) on H^1. The b-unipotent direction is already realized. The generic C_n^* / new-dual-space branch is not authorized because A2 already supplies the successful functional/detector layer.

The first Gate-B test must not assume the naive substitution x->x^a, z->z^a, y->y preserves the relator. Treat it only as a seed and solve the relation-preservation equation with higher pro-p corrections. The exact requirement is that a free-pro-p lift Phi_a with linear part diag(a,1,a) satisfy Phi_a(r) in the normal closure of r. A single finite-level lift is PASS / LOCAL, not Gate-B closure; compatible lifting to the pro-p group is required.

### Current classification

| Item | Classification |
|---|---|
| P5-COH-1 global cohomological scalar stabilizer | PASS / CLOSED / GENERAL |
| A2 finite-window higher-jet upper bound | **PASS / CLOSED** |
| A2 residual-jet/no-cancellation | **PASS / CLOSED** as part of the audited Magnus proof |
| diagonal diag(a,1,a) realization in pro-p G | **OPEN / LOAD-BEARING** |
| full p^2 automorphism theorem | **OPEN / LOAD-BEARING** |

Historical same-day entries claiming A2 remained OPEN are retained above for traceability but are HISTORICAL / SUPERSEDED by this closure entry.

## 2026-10-07 — Gate B B1 D4 obstruction vanishes

The first explicit Magnus test for E_a=x^{ap}[x^a,y]z^{-ap} is now recorded. For p>=5, the degree-4 class vanishes in the associated graded quotient by the relation ideal: the p-power factors contribute nothing in degree 4 mod p, and the remaining [x^a,y] component is killed by the degree-2 initial relation ideal. A direct p=5 word-space membership check confirms this.

Classification: B1 D4 vanishing = PASS / LOCAL. The tentative B3 degree-4 obstruction and the map L_2 -> L_3 are therefore not the relevant next gate. The next authorized layer is the first nonzero residual class, beginning at D_5/D_6 for p>=5. Gate B remains OPEN / LOAD-BEARING.

Detailed audit: research/PAPER5_GATE_B_B1_D4_MAGNUS_AUDIT_2026-10-07.md.


## 2026-10-07 — Gate B B4 p=3 Hensel pre-check correction

The proposed p=3 (U\in I^2/I^3) Hensel search was audited before execution. The suggested standalone degree-6 equation is not yet sufficient: if the degree-4 target is solved by (U=0), then a nonzero (U_2) changes degree 4 through (Z^2U_2+ZU_2Z+U_2Z^2). Hence the claim (U=XX) cancels the degree-6 remainder cannot be accepted without solving the coupled degree-4/5/6 equations. The correct object is (W=Z+U_2+U_3+\cdots), solved layer-by-layer in the same truncated Magnus quotient.

The p>=5 “all higher layers cancel by (R^p)” argument is also not yet a proof: D4 vanishing is established, but the first restricted p-power layer remains load-bearing. Therefore no PASS/CLOSED promotion is made from the new hand argument.

Classification: p=3 Hensel correction = **OPEN / LOAD-BEARING**; (U=XX) claim = **CONDITIONAL / UNVERIFIED**; p>=5 full pro-p diagonal realization = **OPEN / LOAD-BEARING**. Existing D4 result remains **PASS / LOCAL**.

Detailed audit: `research/PAPER5_GATE_B_B4_P3_HENSEL_AUDIT_2026-10-07.md`.


## 2026-10-07 — Gate B B4 p=3 coupled Magnus result through D6

Two solver implementation errors were found and corrected before classification. Run 37565779239 was superseded because its D4 equation used W^4 rather than W^3. Run 37565922146 was superseded because its D5/D6 perturbation columns used W^5/W^6 rather than the actual W^3 equation.

Final commit `d6673a4ade78cba4be39bb72491d5f7083bda331`, Actions run 37566134673: D4-compatible U2 = 81; D5-compatible pairs = 81; D6-compatible coupled lifts = 27. The first lift has U2=U3=0, and an independent implementation gives U4=0 as well. Thus the exact truncated associative Magnus quotient used here admits the uncorrected path W=Z through degree 6.

Independent verification by a separately implemented F3 algebra/rank calculation reproduces all three counts and the zero path.

Classification: **PASS / LOCAL through D6**. This is not pro-p closure and does not close Gate B. The remaining load-bearing issue is extension beyond the finite D6 calculation, in particular the first restricted p-power layer / all-higher-layer compatibility.


## 2026-10-07 — Gate B B4 correction: the load-bearing p=3 test is a=2, not a=1

A parameter-consistency audit found that the earlier coupled script tested a=1, where W=Z is the identity path and the defining relation itself gives the target. That computation is retained as PASS / LOCAL through D6, but it is not the nontrivial realization test for diag(a,1,a).

For p=3, the nontrivial scalar is a=2. The correct seed is W=z^2, with target X_2=x^6[x^2,y]. A new exact full two-sided ideal membership calculation was therefore run for the zero-correction path W=z^2, degree by degree D4 through D9. The computation used exact associative Magnus algebra over F_3, all left/right contexts of every homogeneous component of r-1, and Gaussian elimination encoded by packed ternary rows. A second pivot convention independently reproduced every result.

Actions run 37568611185 (commit e6c866093810fb8f0407d942488e60b29a4f02ad) gives:

| degree | ideal rank | generators | target terms | membership |
|---|---:|---:|---:|---|
| D4 | 32 | 34 | 8 | TRUE |
| D5 | 124 | 142 | 10 | TRUE |
| D6 | 441 | 547 | 14 | TRUE |
| D7 | 1491 | 2005 | 16 | TRUE |
| D8 | 4880 | 7108 | 16 | TRUE |
| D9 | 15624 | 24604 | 16 | TRUE |

Thus the nontrivial p=3 scalar a=2 has the uncorrected seed W=z^2 passing the full two-sided ideal membership test through D9. This supersedes the proposed a=1 D9 target as the relevant Gate-B diagnostic, not as historical provenance.

### Classification
- p=3, a=1, coupled D4-D6: PASS / LOCAL, but non-load-bearing identity case.
- p=3, a=2, W=z^2 full ideal membership D4-D9: PASS / LOCAL.
- p=3 pro-p diagonal realization: OPEN / LOAD-BEARING.
- Gate B: OPEN / LOAD-BEARING.

### Important notation correction
At D9 the relevant equation is the degree-9 homogeneous component of the cubic relation-preservation equation
(W^3-X_a)_9 ≡ 0 mod I_9,
not a literal ninth-power equation W^9=X_a^(9). The restricted p^2-power layer is reflected in the degree-9 Magnus component of W^3. The next calculation must therefore continue the nontrivial a=2 path toward higher restricted layers / compatible pro-3 lifting, rather than reinterpret the D9 test as a literal ninth-power identity.

Detailed script: research/PAPER5_B4_P3_A2_D9_MAGNUS_2026-10-07.py.


## 2026-10-07 — Exact-identity candidate audit: centralization does not imply the required conjugation identity

The proposed structural shortcut from the D4-D9 result was audited before any D10 computation. Let c=[x,y]. From r=z^p x^{-p}c^{-1}=1 one indeed gets c=z^p x^{-p}, hence x^{-p}cx^p=c and therefore [c,x^p]=1. However, for the nontrivial p=3,a=2 case, [x^2,y]=c^x c, so the desired equality [x^2,y]=c^2 requires c^x=c. The established identity [c,x^3]=1 does not imply this: conjugation by x may have order 3 on c.

The Hall–Petresco/Magnus observations in the proposal likewise give filtered/power-level information (for example [[x,y],x] lying in a p-power layer), not the exact equality [[x,y],x]=1. Thus the proposed deduction z^{ap}=x^{ap}[x^a,y] is **not established**. An exact normal-closure factorization of E_2=z^6x^{-6}[x^2,y]^{-1} remains **OPEN / LOAD-BEARING**.

This does not alter the strongest local evidence: the nontrivial p=3,a=2 seed W=z^2 passed full two-sided Magnus ideal membership through D9 in Actions run 37568611185. That result remains **PASS / LOCAL**. The exact-identity shortcut is **FAIL / CLOSED as a logical implication**, while the existence of some independent exact factorization remains **OPEN / LOAD-BEARING**.

Detailed audit: research/PAPER5_GATE_B_EXACT_IDENTITY_AUDIT_2026-10-07.md (commit 17c59dc63bf3a9ce64122f4d4c9b35582d114569).

Strategic consequence: do not run D10 merely because this shortcut failed. The next authorized route is a direct exact-factorization/normal-closure construction or an all-degree restricted-power lifting lemma. Gate B remains **OPEN / LOAD-BEARING**.


## 2026-10-07 — B4 D3-D9 full-ideal audit correction

A definition-level and independent D4 audit was performed after a review questioned whether the B4 script was checking only a homogeneous ideal J rather than the filtered ideal I+Delta^{T+1}, and reported an a=2 failure already at T=4.

The authoritative B4 definitions are
\[
p=3,\quad r=z^3x^{-3}[x,y]^{-1},\quad [x,y]=x^{-1}y^{-1}xy,
\]
\[
W=z^2,\qquad X_2=x^6[x^2,y].
\]
These agree with the current Gate-B record.

An independent associative Magnus calculation over F_3 at D4 gives ideal rank 32 and augmented rank 32, hence
\[
(W^3-X_2)_4\in I_4.
\]
Therefore the reported a=2 failure at T=4 is incompatible with the authoritative definitions.

The existing script's use of every homogeneous component (r-1)_d with all left/right contexts is also not, by itself, a weakening to an irrelevant ideal for the truncated test. Degree by degree, it computes the degree-N component of the filtered ideal generated by r-1; checking the relevant degrees through D9 yields the stated finite truncation
\[
W^3-X_2\in I+\Delta^{10}.
\]
This still does not prove exact normal-closure membership E_2\in N.

For a=1, the exact relation gives z^3=x^3[x,y] in the quotient, so any correct full-ideal implementation with the same conventions must pass the identity path at every truncation order. A reported a=1 failure therefore indicates a convention/target/membership mismatch until the alternative script is inspected.

Classification:
- authoritative definitions: PASS / CLOSED / DEFINITIONAL;
- independent D4 filtered-ideal check for a=2: PASS / LOCAL;
- existing a=2 D3-D9 result: PASS / LOCAL;
- reported a=2 T4 failure under the same definitions: FAIL / CLOSED / incompatible with authoritative definitions;
- reported “J-membership only” objection: FAIL / CLOSED / too coarse;
- exact E_2 in N: OPEN / LOAD-BEARING;
- Gate B: OPEN / LOAD-BEARING.

Do not rerun D10 merely because of this audit. The next load-bearing target remains exact normal-closure factorization or a rigorous all-degree restricted-power lifting mechanism.


## 2026-10-07 — Superseding correction: full non-homogeneous ideal check

The preceding audit in this file is **HISTORICAL / SUPERSEDED**. A supplied independent script was executed verbatim and its membership semantics were inspected.

The script tests the actual two-sided ideal
\[
I=\langle r-1\rangle
\]
in the truncated associative Magnus algebra, using the full non-homogeneous element \(r-1\), not its homogeneous components independently.

For p=3, a=2, W=z^2, X_2=x^6[x^2,y], the reproduced results are:

| T | xc | cx |
|---|---|---|
| 2 | True | True |
| 3 | True | True |
| 4 | **False** | **False** |
| 5 | False | False |
| 6 | False | False |
| 7 | False | False |

The sanity path a=1, ORDER=cx is True for every tested T=2,...,7.

### Why the previous D4 argument was wrong

The previous audit conflated two different membership problems.

The existing D9 script independently checks
\[
(q_N)\in J_N,
\qquad
J=\langle (r-1)_2,(r-1)_3,\ldots\rangle,
\]
degree by degree.

The supplied full-ideal script checks
\[
q\in I+\Delta^{T+1},
\qquad
I=\langle r-1\rangle.
\]

Although \(J\) contains \(I\), the degree components of an element of I are **coupled**: the same left/right context coefficients multiply the entire non-homogeneous element \(r-1\), hence simultaneously constrain its degree-2, degree-3, degree-4, ... contributions.

Membership of each \(q_N\) separately in \(J_N\) does not imply existence of one common linear combination of the full generators \(u(r-1)v\) whose total truncated expansion equals q.

This is exactly why the old D4 rank-32 calculation can pass while the full T=4 calculation fails.

### Correct finite-window consequence

For a=2 the strongest currently established local statement is the homogeneous/J certificate
\[
(q_N)\in J_N,\quad 3\le N\le9,
\]
not
\[
q\in I+\Delta^{10}.
\]

The previously recorded claim
\[
E_2\in ND_{10}
\]
is therefore **not established** by D3-D9 and must be withdrawn.

The full non-homogeneous test gives instead
\[
E_2\notin ND_5
\]
under the stated conventions, because T=4 already fails. This is a genuine finite-window obstruction to the zero-correction seed W=z^2, not a proof that no higher correction W=z^2+U_2+\cdots can exist.

### Classification

- Existing homogeneous D3-D9 J-membership: **PASS / LOCAL**, but weaker than filtered-ideal membership.
- Full non-homogeneous ideal membership for a=2, T=2,3: **PASS / LOCAL**.
- Full non-homogeneous ideal membership for a=2, T=4: **FAIL / LOCAL**.
- Zero-correction seed W=z^2 satisfying the relation through D4: **FAIL / CLOSED for the seed**.
- Claim E_2 in ND_10 from the previous D3-D9 record: **FAIL / CLOSED / SUPERSEDED**.
- Existence of a corrected pro-3 lift W=z^2+U_2+...: **OPEN / LOAD-BEARING**.
- Gate B: **OPEN / LOAD-BEARING**.

### Authorized next action

Do not run D10 on the zero-correction seed as if the D4 obstruction were absent.

The correct next question is the coupled correction problem:
\[
W=z^2+U_2+U_3+\cdots
\]
with
\[
W^3-X_2\in I+\Delta^{T+1}
\]
tested using the **full non-homogeneous ideal** I. Solve the coupled equations beginning at the first failed degree T=4. A finite corrected solution remains PASS / LOCAL until compatible all-degree pro-3 lifting is proved.


## 2026-10-07 — D6 five-solution structure gate: data-extraction boundary

The next authorized mathematical step is the structural comparison of the five nontrivial p=3, a=2 D6 lifts (indices 3,4,5,8,14), before any D7/D8 expansion.

The authoritative D6 audit records only the candidate indices and the finite counts (729 -> 81 -> 27 -> 5); it does **not** record the actual weight-2/weight-3 coefficient tuples or the explicit corrected images Phi(x), Phi(y), Phi(z) for those five solutions. The repository therefore does not yet contain enough data to perform the requested five-way structural comparison without inventing coefficients.

This is a **data-extraction blocker, not a mathematical failure**. The comparison target is fixed:
1. normalize each of the five lifts in the same commutator basis and order;
2. extract the complete weight-2 correction U_2 and weight-3 correction U_3;
3. quotient by any explicitly proven gauge/conjugation redundancy before comparing;
4. compute pairwise differences U_2(i)-U_2(j) and U_3(i)-U_3(j);
5. test whether the five solutions lie on an affine family, a common kernel/coset, or satisfy a low-degree polynomial relation;
6. compare the D6 residual/Jacobian constraints to identify which parameter is genuinely selected at D6;
7. only if a stable law is visible, derive the D7/D8 equations from that law rather than rerunning a blind search.

No D7/D8 calculation is authorized until this comparison is completed.

Classification:
- D3-D6 finite group-level realization: **PASS / LOCAL** (unchanged).
- Five-solution structural law: **OPEN / LOAD-BEARING**.
- D7/D8 continuation: **CONDITIONAL / NOT YET AUTHORIZED**.
- Gate B: **OPEN / LOAD-BEARING**.

Evidence: research/PAPER5_GATE_B_P3_A2_GROUP_LEVEL_D6_AUDIT_2026-10-07.md.


## 2026-10-08 — Gate B exact free-group identity closes the a=-1 branch

The previous p=3,a=2 D6 structural route is now supplemented by an exact free-group identity.

With [u,v]=u^{-1}v^{-1}uv and
r=z^p x^{-p}[x,y]^{-1}, define
Phi(x)=x^{-1}, Phi(y)=x^{-(p+1)}yx^{p+1}, Phi(z)=z^{-1}.
For c=[x,y],
Phi(c)^{-1}=x^{-p}cx^p, hence
Phi(r)=z^{-p}r^{-1}z^p.

Therefore Phi preserves the relator normal closure and induces a continuous endomorphism of G. Its Frattini-quotient linear part is diag(-1,1,-1), so it is surjective; finite generation plus Hopf gives an automorphism.

Classification:
- odd p, a=-1 realization: **PROVED**;
- p=3 diag(a,1,a)-type diagonal torus: **PROVED**;
- general a with ord(a)>2: **OPEN / LOAD-BEARING**;
- full Paper 5 p^2 theorem: **OPEN / LOAD-BEARING**.

This supersedes the need to complete the D6-to-all-degree lift proof for the p=3,a=2 branch as the proof route, while retaining its finite computations as PASS / LOCAL discovery evidence.

### Corrected D6 discovery chronology

The earlier wording that Phi_0 itself passes through T<=9 was incorrect and is superseded.

The correct discovery chain is:
gauge structure -> Phi_0 -> correction pattern -> x^{-4} y x^4 -> exact identity.

Here k=1 (Phi_0) passes through D5 but fails at D6. One weight-4 correction repairs D6 and one further weight-5 correction closes D7. The coefficients agree with binom(4,j) mod 3 = (1,0,1,1), pointing to k=4=p+1. The Magnus T<=9 evidence concerns k=4, not k=1.

The affine/gauge counts 729 -> 81 -> 27 and 27 -> 3 -> 1 remain discovery evidence only. The earlier five-way D6 structural selection was a solver/gauge-representative artifact and is **HISTORICAL / SUPERSEDED**.

### Withdrawn routes

The old J-membership test, old xc-order route, and the statement “E_2 in ND_10 PASS” are **HISTORICAL / SUPERSEDED** as Gate-B evidence. The corrected group-level D6 result remains **PASS / LOCAL**.

### Reproduction note

The free-group check is associated with the local script name PAPER5_GATE_B_EXACT_IDENTITY_FREE_GROUP_CHECK.py; that script is not currently present in the GitHub repository and is therefore not claimed as a repository artifact. The reported word checks cover p=3,5,7,11,13. Magnus evidence is k=4 through T<=9 with k=1 failing at D6.

### Next authorized gate

For p=5,a=2, Gate B requires only Phi(r) to lie in the relator normal closure. A conjugate-of-a-power representation is merely a sufficient route. The earlier claim that a weight-(p+2) error must be cancelled by a weight-(p+1) correction is **CONJECTURE / UNVERIFIED**.

Proceed first with the smallest finite filtered correction and its gauge quotient; only a structural pattern should trigger an all-degree factorization/lifting attempt. Blind D7/D8 continuation is not authorized.


## 2026-10-08 — Gate B p=5,a=2 validation design / source-recovery gate

The next authorized Gate-B computation is a narrowly scoped validation harness for p=5,a=2:

- p=3 regression: reproduce D3/D4/D5 = 729→81→27 using the existing solver parameterization; do not encode the superseded 27→5 interpretation. D6 remains a separate corrected finite-realization check.
- p=5 D3/D4: independently expose variable count, equation count, F5 rank, nullity, and 5^nullity rather than accepting 3125 by cardinality alone.
- gauge action: compute the actual gauge-group order, action closure, orbit-stabilizer consistency, orbit-size histogram, and orbit count; do not assume |G|=125, 25 orbits, or orbit size 125.

The harness deliberately excludes p=5 D5/D6/D7. Those stages remain unauthorized until the rank/action audit passes.

**Source-reuse gate:** repository search did not locate a committed copy of the earlier p=3 solver (`gateB_stage.py`, `gateB_fast.py`, or an equivalent group-level implementation). The authoritative D6 audit also records that the solver coefficient data are not repository-visible. Therefore no new validation script is created yet: first recover the exact solver artifact and fix its parameterization/coordinate system as a repository-visible source; then create `research/scripts/paper5_gateB_p5_a2_validation.py` as a caller/auditor, not a reimplementation.

Classification:
- validation design: **PASS / CLOSED**;
- solver-source recovery: **OPEN**;
- p=5 D3/D4 rank + gauge-action audit: **OPEN / LOAD-BEARING**;
- p=5 D5/D6/D7 continuation: **CONDITIONAL / NOT AUTHORIZED**.


## 2026-10-09 — Gate B Labute exact-equality claim corrected

A proposed closure via Labute Theorem 2 was rechecked against the original 1967 paper. The earlier statement that Theorem 2 directly gives
\[
\exists\psi\in\operatorname{Aut}(F),\qquad \psi(r)=r'
\]
is **incorrect**.

The original paper states the weaker conclusion: if the closed normal subgroups satisfy \((r)=(r')\) and \(F/(r)\) is Demushkin, then there is an automorphism of \(F\) **sending \(r\) into \(r'\)**. The wording is explicitly “sending \(r\) into \(r'\)”, not equality or conjugate-of-power equality. See Labute, *Classification of Demushkin Groups*, p.108, Corollary immediately following Theorem 2.

Therefore the proposed substitution \(r=w_0=x^p[x,y],\ r'=r^\alpha\) does establish \((r)=(r')\), but Labute alone does **not** establish \(\psi(w_0)=w_0^\alpha\) or even \(\psi(w_0)=g w_0^\alpha g^{-1}\).

This is load-bearing because the root-extension lift requires an exact relation-level equality (or a separately proved sufficient conjugate-of-power form). Mere membership in the normal closure is insufficient for the stated construction.

The earlier proposed “prescribed Frattini shape follows from exact equality” argument is consequently **NOT a proof**. Its initial restricted-layer coefficient calculation remains a useful conditional calculation: if an exact equality \(\psi(w_0)=w_0^\alpha\) is independently obtained, comparison of the \(x^{[p]},y^{[p]},[x,y]\) components gives the expected constraints \(c=0,a=\alpha,d=1\). It does not produce the missing exact equality.

Classification:
- Labute as relevant relator-equivalence methodology: **PASS / LOCAL**.
- Labute direct exact-power realization: **FAIL / CLOSED as the proposed route**.
- Exact-power/conjugate-of-power realization for ord(\alpha)>2: **OPEN / LOAD-BEARING**.
- Hensel/Magnus p=5, \alpha=2 test: **REOPENED as an authorized fallback**; no D5/D6/D7 computation before the existing validation/source-recovery gate is satisfied.
- Full Gate B: **OPEN / LOAD-BEARING**.

This supersedes the immediately preceding internal claim that Labute Theorem 2 had closed the general torus lift.


## 2026-10-09 — First restricted-layer lemma audit

The Gate-B hand-proof repair closes the first restricted-layer **lemma**, but not the lift problem. The corrected degree separation is accepted, and
\[
L_p/[L_{p-1},L_1]\cong\mathbf F_pX^{[p]}\oplus\mathbf F_pY^{[p]}
\]
is recorded as **PASS / LOCAL**. Under the conditional filtered equality \(\psi(w_0)\equiv w_0^{\tilde\alpha}\pmod{D_{p+1}}\), the residual projection is
\[
\pi_{\rm res}(E_p)=(a^p-\tilde\alpha)X^{[p]}+c^pY^{[p]},
\]
forcing \(a^p=\tilde\alpha,c=0\); with Teichmuller normalization this gives \(a=\tilde\alpha,d=1\).

This does **not** establish exact-power/conjugate-of-power realization, all-degree pro-p lifting, or Gate-B closure. The group-to-restricted-Lie passage and filtered degree-p projection should be formalized before manuscript promotion.

Classification: first restricted-layer quotient/residual = **PASS / LOCAL**; exact lift = **OPEN / LOAD-BEARING**; Gate B = **OPEN / LOAD-BEARING**.

Evidence: `research/PAPER5_GATE_B_FIRST_RESTRICTED_LAYER_AUDIT_2026-10-09.md`.


## 2026-10-09 — Gate B all-degree Hensel proposal: corrected load-bearing boundary

The proposed Lemma A/B/C route was audited as a candidate replacement for degree-by-degree D_{p^k} computation.

The strategic reduction is accepted: the goal is **not** to brute-force infinitely many Zassenhaus layers, but to prove a universal restricted-power obstruction lemma and then use pro-p completeness. The ordinary correction map
\[
d\Phi_m(u,v)=[u,Y]+[X,v]
\]
targets the ordinary bracket part, while the restricted quotient at \(n=p^k\) is the only possible new obstruction.

However, the submitted all-k Lemma C is **not yet proved**. In particular, the statements that \(\psi([x,y])\) contributes trivially to the restricted projection and that
\[
\pi_{\rm res}^{(k)}(w_0^{\tilde\alpha})=\tilde\alpha X^{[p^k]}
\]
cannot be inferred merely from \(\psi([x,y])\in\gamma_2\) or from a generic Hall–Petresco slogan. The lower-degree components of
\(w_0=x^p[x,y]\)
are coupled, and the residual must first be known to lie in \(D_{p^k}\) before its \(L_{p^k}\)-class is projected.

The required universal lemma is therefore:

\[
Q_n:=L_n/[L_{n-1},L_1],\qquad
Q_n=0\ (n\ne p^k),\qquad
Q_{p^k}\cong\mathbf F_pX^{[p^k]}\oplus\mathbf F_pY^{[p^k]},
\]
together with a rigorous filtered-power formula showing that every cross-term in the relation-preservation residual lies in \([L_{p^k-1},L_1]\), so that the restricted projection is genuinely
\[
(a^{p^k}-\tilde\alpha)X^{[p^k]}+c^{p^k}Y^{[p^k]}.
\]

If this universal formula is proved, the Teichmuller normalization
\(a=\tilde\alpha,\ c=0\)
would kill all restricted obstructions simultaneously because
\(\tilde\alpha^{p^k}=\tilde\alpha\).
Only then would pro-p completeness yield the exact lift.

Classification:
- ordinary/restricted separation: **PASS / LOCAL**;
- first restricted quotient and first-layer residual: **PASS / LOCAL**;
- all-k restricted-power formula (Lemma C): **OPEN / LOAD-BEARING**;
- exact-power/conjugate-of-power lift: **OPEN / LOAD-BEARING**;
- Gate B: **OPEN / LOAD-BEARING**.

Authorized next action: prove the universal restricted-quotient power lemma. Do **not** replace this by blind D_5/D_6/D_{p^k} computation. Finite computations may be used only as independent diagnostics after the structural lemma is formulated.
