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
