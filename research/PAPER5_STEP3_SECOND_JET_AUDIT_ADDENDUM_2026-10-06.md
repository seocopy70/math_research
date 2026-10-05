# Paper 5 — Step 3 Second-Jet Audit Addendum
Date: 2026-10-06

## Classification

**CLOSED / GENERAL for the corrected second-order operator; Step 3 equality remains OPEN / LOAD-BEARING.**

The substitution-order defect is repaired by
\[
C_{a,b,k}:=T_{a,b,k}\circ L.
\]
For (x\mapsto x^a, y\mapsto yx^b, z\mapsto z^a),
\[
L(X)=aX,quad L(Y)=Y+bX,quad L(Z)=aZ.
\]
Hence
\[
\operatorname{sec}_{k+1}(\widetilde g(r))
=\operatorname{gr}(\widetilde g)(R_{k+1})+T_{a,b,k}(L(R_k)).
\]
For (R_2=[X,Y]),
\[
C_{a,b,2}(R_2)
=ab\,XYX+\binom a2XXY-
\left(ab+\binom a2\right)YXX,
\]
so the corrected coefficient is (ab), not (b).

### Verification

Work explicitly in the mod-(p) Magnus/restricted-Lie layer. Let
\[
I=\langle[X,Z],[Y,Z],[X,Y]\rangle_{\rm assoc}.
\]
The associative derivations (D_X,D_Z,D_{Y,1},D_{Y,2}) preserve the two-sided ideal (I), and (L) preserves (I). Thus
\[
T_{a,b,k}(I_k)\subseteq I_{k+1},
\qquad
C_{a,b,k}(I_k)\subseteq I_{k+1}.
\]
For (u\in I_p),
\[
D(u^p)=\sum_{i=0}^{p-1}u^iD(u)u^{p-1-i}\in I_{p^2+1},
\]
because (D(u)\in I_{p+1}). Also (D(X^{p^2}-Z^{p^2})=0) in characteristic (p). These exceptional-layer statements are not literal (mathbf Z_p)-identities.

Combining the ordinary commutator ideal with the exceptional power layers gives
\[
C_{a,b,k}(gr_k(R))\subseteq gr_{k+1}(R),
\]
and therefore
\[
\operatorname{sec}_{k+1}(\widetilde g(r))\in gr_{k+1}(R).
\]

### Finite-stage residual factorization

No strong equality
\[
D_j=(R\cap D_j)(R\cap D_{j+1})D_{j+2}
\]
is required. If (r^{(j)}\in R\cap D_j), then its initial class is by definition in (gr_j(R)). Choose (r_j\in R\cap D_j) representing it; then
\[
r^{(j+1)}=r_j^{-1}r^{(j)}\in R\cap D_{j+1}.
\]
Iteration gives
\[
r=r_kr_{k+1}\cdots r_Nr^{(N+1)},qquad
r^{(N+1)}\in R\cap D_{N+1}.
\]
The corrected second-order statement gives (widetilde g(r_j)\in RD_{j+2}), hence
\[
\widetilde g(r)\in RD_{N+1}
\]
for every (N\ge k). Since (R) is closed and (D_N\to1),
\[
\bigcap_NRD_N=R,
\]
so
\[
\boxed{\widetilde g(R)\subseteq R}.
\]

### Updated status

- (D_k/D_{k+2}) abelian, (k\ge2): **PASS / GENERAL**.
- (J_k^2(r)): **PASS / GENERAL**.
- Raw derivation/commutator-ideal preservation: **PASS / GENERAL**.
- (D(u^p)\in I_{p^2+1}): **PASS / GENERAL in the explicit mod-(p) layer**.
- (X^{p^2}-Z^{p^2}\mapsto0): **PASS / GENERAL in the explicit mod-(p) layer**.
- Corrected (C_{a,b,k}=T_{a,b,k}\circ L): **CLOSED / GENERAL**.
- (C_{a,b,k}(gr_k(R))\subseteq gr_{k+1}(R)): **CLOSED / GENERAL**.
- (operatorname{sec}_{k+1}(\widetilde g(r))\in gr_{k+1}(R)): **CLOSED / GENERAL within the declared mod-(p) Magnus layer**.
- Finite-stage residual factorization: **CLOSED / GENERAL**.
- (widetilde g(R)\subseteq R): **CLOSED / GENERAL**.
- Step 3 equality (operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p)): **OPEN / LOAD-BEARING**.
- (p^2(p-1)) theorem: **CONDITIONAL**.

This supersedes the immediately preceding 2026-10-06 entry that left (C_{a,b,k}) OPEN/LOAD-BEARING. Step 2 remains independently CLOSED/GENERAL.
