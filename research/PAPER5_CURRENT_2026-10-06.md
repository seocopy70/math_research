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
