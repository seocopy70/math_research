# Paper 5 — Addendum 2: p^2 gap comparison-window audit — 2026-10-06

## Classification

**OPEN / LOAD-BEARING. The proposed p^2 quotient-kernel decomposition is NOT CLOSED as submitted.**

The intrinsic W_p relation-jet stabilizer result remains CLOSED:
[
W_{p+1}=W_p,qquad
operatorname{Stab}(mathcal J_p)=S'_{11}(p),qquad
operatorname{Im}(operatorname{Aut}(W_p)	o GL(V))=S'_{11}(p).
]

However, the proposed final identification
[
|operatorname{Aut}(W_p)|/|operatorname{Aut}(U_p)|=p^2,
qquad U_p=W_p/L,
]
cannot yet be recorded as CLOSED.

## 1. Quotient-definition obstruction

The intrinsic line
[
L=Z(W_p)D_2(W_p)/D_2(W_p)
]
is a one-dimensional subspace of
[
V=W_p/D_2(W_p),
]
not itself a subgroup of (W_p). Therefore the notation (W_p/L) is not defined without specifying a canonical subgroup lift.

A possible lift is the central subgroup (langle zangle), but replacing (L) by (langle zangle) is an additional definition and must be audited. It is not formally the same object as the line (Lsubset V).

## 2. The quotient changes the window data

If one defines instead
[
U_p:=W_p/langle zangle,
]
then (U_p) is a two-generator quotient and its Frattini quotient has dimension (2), not (3). Consequently its (GL(V))-image, IA kernel, and relation package cannot simply be assumed to have the same (S'_{11}) quotient or a kernel of order (p^7).

Thus the assertions
[
1	o K_p^U	ooperatorname{Aut}(U_p)	o S'_{11}	o1,
qquad |K_p^U|=p^7
]
require independent computation. They do not follow from the CLOSED W_p calculation.

## 3. Domain/type obstruction in the proposed relation equation

The established commutator map has type
[
b:wedge^2Vlongrightarrow D_p.
]
But the proposed expression
[
b(pi(x),y)
]
is not defined, because (pi(x)in D_p), whereas the first input of (b) must lie in (V). A new action/pairing or derivation-level cocycle must be defined before a relation such as
[
b(pi(x),y)+b(x,pi(y))=(a-m)ell
]
can be used.

Therefore the claimed dimension reduction
[
dimoperatorname{Hom}(V,L)=3
quadLongrightarrowquad
dim Z^1_{mathcal J_p}(V,L)=2
]
is presently a **candidate**, not a proof.

## 4. What remains valid

The following remain CLOSED and are not affected:

- (W_{p+1}=W_p): PASS/CLOSED/GENERAL.
- Intrinsic relation package (mathcal J_p=(V,D_p,pi,b,L,mathrm{relation})): PASS/CLOSED/GENERAL.
- (operatorname{Stab}(mathcal J_p)=S'_{11}(p)): PASS/CLOSED/GENERAL.
- (operatorname{Im}(operatorname{Aut}(W_p)	o GL(V))=S'_{11}(p)): PASS/CLOSED/GENERAL.
- (|S'_{11}(p)|=p^2(p-1)^2): PASS/CLOSED.
- (IA(W_p)congmathbf F_p^9) and (|operatorname{Aut}(W_p)|=p^{11}(p-1)^2): PASS/CLOSED.
- Raw (GL_3/S'_{11}) has p-primary part (p), not (p^2).

## 5. Correct next gate

The actual remaining load-bearing task is:

1. Define a genuine subgroup (Cle Z(W_p)) corresponding to the intended central quotient.
2. Compute (U_p=W_p/C) from its presentation.
3. Compute (V_U), (D_p(U_p)), its intrinsic relation package, and (operatorname{Aut}(U_p)) independently.
4. Define the restriction/extension kernel comparing automorphisms of (W_p) and (U_p).
5. Only then test whether the relevant kernel is canonically a 2-dimensional (mathbf F_p)-space.

Until these are done,
[
|operatorname{Aut}(W_p)|/|operatorname{Aut}(U_p)|=p^2
]
is **OPEN**, not CLOSED.

The previous proposed CLOSED claim is therefore rejected as submitted; it does not supersede the existing OPEN/load-bearing status of the exact p^2 comparison theorem.


## Addendum 3 — reverse-π proposal rejected; IA kernel cannot supply the second p

The proposed replacement \(\pi:D_p\to V\), with \(\pi(d_{z1})=v_z\), is **FAIL / CLOSED as a construction from the W_p p-power structure**.

The intrinsic p-power map already fixed in the W_p audit has type \(\pi_0:V\to D_p\), \(\pi_0(\bar g)=g^p\). There is no canonical reverse map \(D_p\to V\) induced by Hall–Petrescu, Witt, or the p-power operation. Since \(D_p(W_p)^p\subseteq D_{p^2}(W_p)=1\), the p-power operation on \(D_p\) cannot produce a nonzero class in \(V\). The assignment \(d_{z1}\mapsto v_z\) is therefore additional structure, not a consequence of the presentation.

More decisively, the proposed kernel cut cannot work even if an arbitrary reverse map were artificially supplied. For \(f\in\operatorname{Hom}(V,D_p)\), the corresponding IA modification changes a lift \(g\) to \(g f(\bar g)\). Since \(D_p\le Z(W_p)\) and \(D_p^p=1\), \((gd)^p=g^p\) and commutators with \(D_p\) are unchanged. Hence IA acts trivially on the established intrinsic data \(\pi_0:V\to D_p\), \(b:\wedge^2V\to D_p\), and the relation package. Thus preservation of \(\mathcal J_p\) does not impose \(f(v_z)\in\ker(\text{reverse-}\pi)\), and no \(3\to2\) cut of \(\operatorname{Hom}(L,D_p)\) follows.

Consequently \(|K_b:K_{\mathcal J}|=p\) is **FAIL / CLOSED for this mechanism**. The proposed \(p^2=p\cdot p\) comparison via \(\operatorname{Aut}_b/\operatorname{Aut}_{\mathcal J}\) is rejected. The exact observed \(p^2\) automorphism-order gap remains **OPEN / LOAD-BEARING** and must be sought in a different comparison object or a higher filtered/extension-level action genuinely visible to IA.

## 2026-10-06 — Addendum 4: model-identity correction

The previous discussion implicitly identified two different groups. This is rejected.

The central Step-3 model is [x,z]=[y,z]=1, [x,y]=x^p z^{-p}, whereas the actual GAP model used in the certified p=3,n=4 calculation is G=<z,x,y | z^3=x^3[x,y]>, with no centrality relations for z. Consequently the central-model S'_{11}(p), D_p-centrality, and its IA-blind no-go do not directly address the observed p=3,n=4 p^2 gap.

Classification: model identification = **FAIL / CLOSED / SUPERSEDED**; actual p=3,n=4 p^2 gap mechanism = **OPEN / LOAD-BEARING**; actual gap remains locally a Frattini/GL-image defect, not an IA defect, by certified runtime.

Next gate: audit the actual mkG(s,a) window, beginning with (s,a)=(1,1), and derive its intrinsic embedded stabilizer in GL_3(3).
