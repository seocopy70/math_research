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
