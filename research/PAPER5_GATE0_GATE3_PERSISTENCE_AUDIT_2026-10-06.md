# Paper 5 — Gate 0/1/3 Persistence Audit — 2026-10-06

## Classification

- **Gate 0 (central b-convention): PASS / LOCAL certificate**
- **Central model uniform image at n=p+1 and n=p^2+1 for p=3: PASS / LOCAL**
- **Actual G_{1,1} persistence through the tested windows: PASS / LOCAL**
- **Old central-model claim G_{p^2} < G_p via b:x->xy: FAIL / CLOSED / SUPERSEDED**
- **General actual-model persistence for all n>=p+1: OPEN / LOAD-BEARING**
- **p=5,n=7 exact scan: OPEN / COMPUTATIONAL LIMIT**, not a mathematical failure.

## Gate 0 — exact b certificate

The repository's corrected boundary matrices use the presentation basis (x,y,z) and the b-parameter in the y-column. The explicit finite-window map with (m,a,b,d)=(1,1,1,0) is

[
xmapsto x,qquad ymapsto xy,qquad zmapsto z.
]

The GAP certificate constructs this map directly on the finite central windows and verifies bijectivity. Thus the b-unipotent in the central model is **y -> xy**, not x -> xy.

This is a runtime certificate, not an inference from matrix convention.

## Gate 1 — central model

For
[
G_{m cen}=langle z,x,ymid [x,z]=[y,z]=1, [x,y]=x^p z^{-p}angle
]
at p=3, the 36 explicit maps
[
zmapsto z^a,quad
xmapsto x^m z^{a-m},quad
ymapsto x^b y z^d
]
with m,a in F_3^*, b,d in F_3 were tested directly on:

- n=4=p+1: |W_4|=3^6=729;
- n=10=p^2+1: |W_{10}|=3^9=19683.

All 36 maps induce automorphisms at both levels.

Together with the already-closed n=p upper bound
[
operatorname{Im}Aut(W_p)subseteq S'_{11}(p),
qquad |S'_{11}(3)|=36,
]
this gives the finite-level equality
[
operatorname{Im}Aut(W_4)=operatorname{Im}Aut(W_{10})=S'_{11}(3)
]
for this tested central tower. It independently confirms the analytic-model uniform-image prediction.

It does **not** by itself prove the all-odd-p central theorem; that theorem is supplied by the explicit semidirect-product decomposition and should remain separately scoped.

## Gate 3 — actual G_{1,1}

For
[
G_{1,1}=langle z,x,ymid z^p=x^p[x,y]angle
]
the exact finite-window automorphism groups were computed.

### p=3

[
egin{array}{c|c|c|c}
n&|W_n|&|operatorname{Aut}(W_n)|&|operatorname{Im}_n|\
hline
3&3^5&629856&864\
4&3^{13}&45753584909922&6\
5&3^{23}&159532886153745019726722&6
end{array}
]

Thus the first transition occurs at n=p+1=4, and the image remains 6 at n=5.

### p=5

[
egin{array}{c|c}
n&|operatorname{Im}_n|\
hline
5&48000\
6&20
end{array}
]

The n=6 result independently reproduces the existing p=5,n=6 certificate. The first transition again occurs at n=p+1.

The values are exactly
[
p(p-1)=6, 20.
]

## Cohomological stabilizer calculation

Take
[
omega=x^*wedge y^*,
qquad
eta(lambda)=(lambda(x)-lambda(z))eta.
]

Let A be the induced matrix on V in the (x,y,z) basis. Preservation of the line F_pomega forces A to preserve the plane <x,y>. If its top-left block is B, the induced scalar on H^2 is det(B)^{-1}. Naturality of beta then gives
[
A(e_x-e_z)=det(B)(e_x-e_z).
]
Writing
[
A=egin{pmatrix}B&u\0&a_{33}end{pmatrix}
]
forces
[
B=egin{pmatrix}a&b\0&1end{pmatrix},
qquad
a_{33}=a,
qquad
u=0.
]
Hence
[
operatorname{Stab}(omega,eta)
=
left{
egin{pmatrix}
a&b&0\
0&1&0\
0&0&a
end{pmatrix}
:ain F_p^	imes, bin F_p
ight},
]
and therefore
[
|operatorname{Stab}(omega,eta)|=p(p-1).
]

This agrees exactly with the actual p=3,n=4,5 and p=5,n=6 image orders. The cohomological formulas still require a direct relator/Fox derivation before being promoted to a theorem.

## Superseded central strict-shrinkage narrative

The old log entry claiming
[
b:xmapsto xy,qquad bin G_psetminus G_{p^2}
]
in the central model is invalid. The direct certificate shows that the corresponding central automorphism is
[
xmapsto x,quad ymapsto xy,quad zmapsto z
]
and it survives both tested finite windows.

This does **not** invalidate the separate denominator theorem
[
RD_{p^2+1}subsetneq RD_{p+1}.
]
The denominator chain and the automorphism-image chain are distinct statements.

The previous central (G_{p^2}subsetneq G_p) entry is therefore **HISTORICAL / SUPERSEDED** as a statement about the central model. The actual (G_{1,1}) image behavior must be studied independently.

## Remaining load-bearing question

The tested data now support the much cleaner conjectural shape
[
operatorname{Im}_n
=
operatorname{Stab}(omega,eta)
qquad(nge p+1)
]
for the actual (1,1)-family.

What is not yet proved is the reverse inclusion uniformly for all odd p and all n>=p+1.

The p=5,n=7 computation could not be completed with the standard GAP p-quotient collector: the collector stops at class 6. This is a computational limitation, not evidence of image shrinkage.

## Reproducibility

Certificate branch:
`paper5-gate0-gate3-20261006`

Successful final certificate run:
- workflow: Paper 5 Gate 0/1/3 certificate
- run: 37404099935

The later p=5,n=7 attempts failed only because the GAP collector could not construct the requested next class; the successful n<=6 outputs above are unaffected.
