# HARD ATTACK 34 — COKER DUALITY/NORM AUDIT

## 2026-09-20

Hard Attack 33 was independently audited at the level of the PD^2 duality bridge, coefficient twist, finite norm, and finite-carrier realization.

### 1. Dualizing-module correction
The notation in Hard Attack 33 must be made precise. For pro-p duality with finite p-primary coefficients, the relevant dualizing module is the discrete torsion module I_G (for a PD^2/Poincare pro-p group, abstractly Q_3/Z_3 with G-action via the orientation character), not the torsion-free Z_3 dualizing line. Then
B = Hom(A_k(rho), I_G)
 is finite of exponent 3^k and carries the action chi*rho^{-1}. This is the coefficient module appearing in the top-degree duality
H^2(G,A_k(rho))^* ≅ H^0(G,B).

### 2. Restriction/corestriction bridge survives
For N=P_{k+1}(G), an open subgroup, the dualizing module for N is the restriction of I_G. Hence the PD^2 duality pairings identify the Pontryagin dual of
res:H^2(G,A)->H^2(N,A)
with
cor:H^0(N,B)->H^0(G,B).
This is the standard restriction/corestriction compatibility for Poincare/duality groups. No top class is inserted into the finite carrier.

### 3. N-triviality of B
Both rho mod 3^k and chi mod 3^k factor through Q_k=G/P_{k+1}(G). Therefore N acts trivially on B. Thus H^0(N,B)=B and corestriction is the finite norm
N_Q(b)=sum_{q in Q}q.b.

### 4. Norm estimate
The quotient Q_k has abelianization containing (Z/3^k)^3 from x_2,x_3,x_4, so v_3(|Q_k|)>=3k. The image C of delta=chi*rho^{-1} in U_k has order 3^m with m<=k-1. Writing Q->C with kernel K gives N_Q=|K|N_C. For nontrivial C, if u generates C then LTE/geometric-series valuation gives v_3(1+u+...+u^{3^m-1})>=m; hence v_3(|K|N_C)>=3k. For trivial C, N_Q is multiplication by |Q| and is zero on exponent-3^k B. Therefore cor=0.

### 5. Consequence
Duality gives res=0, so inflation H^2(Q,A)->H^2(G,A) is surjective. LHS five-term exactness gives
coker(delta_rho) = im(inf) = H^2(G,A_k(rho)).
Therefore the finite coker size equals the full twisted top-cohomology size.

### 6. Orientation recognition
Using the standard PD^2/Demuškin criterion
rho=chi mod 3^k iff |H^2(G,A_k(rho))|=3^k,
we obtain
rho=chi mod 3^k iff |coker(delta_rho)|=3^k.

### 7. Critical boundary
The argument survives. The only correction is the precise torsion dualizing-module formulation. The coker itself remains a finite object determined by the extension
1 -> M_k -> E_k -> Q_k -> 1
and rho; H^2(G,A) is used only in the independent theorem proving what the coker computes.

Status:
- Hard Attack 33 core coker theorem: PASS / LOCAL after this correction.
- finite Kummer recognition at level k for PD^2/Demuškin G: PASS / LOCAL.
- inverse-limit reconstruction: OPEN pending a separate compatibility/naturality theorem.
- minimality of P_{k+1}: OPEN.
- universal category-independent minimality/no-go: OPEN.

This audit does not claim that the carrier is minimal or that the global research goal is complete.
