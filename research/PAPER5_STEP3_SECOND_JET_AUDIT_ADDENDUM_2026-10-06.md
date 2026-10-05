# Paper 5 — Step 3 Second-Jet Audit Addendum
Date: 2026-10-06

## Classification

**FAIL / CLOSED as submitted proof; Step 3 equality remains OPEN / LOAD-BEARING.**

The 2026-10-06 proposed (T_{a,b,k}) repair correctly identifies associative derivations that preserve the commutator ideal, and the (p^2+1) degree count is valid after coefficient reduction to (mathbf F_p). However, the displayed second-order formula applies the operator to (R_k) rather than to the linearly transformed first-order term. This is a load-bearing substitution-order error.

For the specified lift
[
xmapsto x^a,qquad ymapsto yx^b,qquad zmapsto z^a,
]
the Magnus substitution has
[
L(X)=aX,quad L(Y)=Y+bX,quad L(Z)=aZ,
]
and quadratic part
[
Q(X)=inom a2X^2,quad
Q(Y)=bYX+inom b2X^2,quad
Q(Z)=inom a2Z^2.
]
For a homogeneous (R_k), the degree-((k+1)) contribution is the quadratic insertion operator evaluated after the linear substitution, schematically
[
C_{a,b}(R_k)=T_{a,b,k}(L(R_k)),
]
not (T_{a,b,k}(R_k)), unless (T) is redefined to incorporate this linear substitution.

A concrete degree-2 check detects the mismatch. Put (c=inom a2) and take (R_2=[X,Y]). The actual degree-3 correction contains
[
ab,XYX+c,XXY-(ab+c)YXX,
]
whereas the submitted (T([X,Y])) gives
[
b,XYX+c,XXY-(b+c)YXX.
]
These differ for general (a) whenever (b
e0). Thus
[
sec_{k+1}(	ilde g(r))
=gr(	ilde g)(R_{k+1})+T_{a,b,k}(R_k)
]
is false with the submitted (T) in general.

## What survives

1. (D_X,D_Z,D_{Y,1},D_{Y,2}) are degree-(+1) associative derivations.
2. Each preserves the two-sided commutator ideal (I); hence the raw operator satisfies (T(I_k)subseteq I_{k+1}).
3. For (uin I_p), the associative Leibniz sum gives (D(u^p)in I_{p^2+1}) in the mod-(p) Magnus algebra. The coefficient/characteristic convention must be explicit because the earlier ambient (mathbf Z_planglelangle X,Y,Zangleangle) does not have (p^2=0).
4. The (X^{p^2}-Z^{p^2}) calculation is likewise a mod-(p) calculation and belongs in the corresponding (mathbf F_p)-graded/restricted-Lie layer.
5. The finite-stage residual-factorization idea can work without the displayed equality
[
D_j=(Rcap D_j)(Rcap D_{j+1})D_{j+2}.
]
If (r^{(j)}in Rcap D_j), then its initial class is by definition in (gr_j(R)). Choose (r_jin Rcap D_j) representing that class; then
[
r^{(j+1)}=r_j^{-1}r^{(j)}in Rcap D_{j+1}.
]
No assumption (gr_j(R)=gr_j(F)) is needed, including at the exceptional layers (j=p,p^2).

## Remaining load-bearing gap

Even after the above repairs, one must define the **actual** degree-((k+1)) operator (C_{a,b}) induced by the full Magnus substitution and prove that it preserves (gr_{k+1}(R)). The raw statement (T(I_k)subseteq I_{k+1}) is not enough because the actual correction acts after the linear substitution. Only then can the strengthened (L_k) be derived.

## Updated status

- (D_k/D_{k+2}) abelian, (kge2): **PASS / GENERAL**.
- (J_k^2(r)=[r]in D_k/D_{k+2}): **PASS / GENERAL**.
- Raw derivation/commutator-ideal preservation (T(I_k)subseteq I_{k+1}): **PASS / GENERAL**.
- (D(u^p)in I_{p^2+1}) for (uin I_p): **PASS / GENERAL after explicit mod-(p) formulation**.
- (X^{p^2}-Z^{p^2}mapsto0): **PASS / GENERAL in the mod-(p) graded layer**.
- Displayed formula (sec_{k+1}=gr(	ilde g)(R_{k+1})+T(R_k)): **FAIL / CLOSED as written**.
- Corrected actual second-order operator (C_{a,b}): **OPEN / LOAD-BEARING**.
- Strengthened (L_k): **OPEN / LOAD-BEARING**.
- (	ilde g(R)subseteq R): **OPEN / LOAD-BEARING**.
- (operatorname{Im}(Aut(W_n)	o GL(V))=S_{11}(p)): **OPEN / LOAD-BEARING**.
- (p^2(p-1)) theorem: **CONDITIONAL**.

This supersedes/refines the immediately preceding second-jet audit by locating the specific substitution-order obstruction. Step 2 remains independently CLOSED/GENERAL.
