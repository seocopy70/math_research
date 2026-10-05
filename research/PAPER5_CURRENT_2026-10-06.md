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
