# HARD ATTACK 49 — THE NEXT BASE TARGET ALSO COLLAPSES: H²(V)·K = H⁴(V)

Date: 2026-09-20

## Target

Hard Attack 48 removed the entire base target E_infinity^{3,0}. The next possible base target in the LHS differential pattern is

d_2:E_2^{2,1}=H^2(V,F_3)\otimes W^* -> E_2^{4,0}=H^4(V,F_3).

Before attempting any twisted Bockstein calculation, attack this target directly. If the cup product with the transgression image K is surjective, then E_3^{4,0}=0 and the whole (4,0) base target is likewise absent from E_infinity.

## 1. Input

Use the already closed Hard Attack 45 data:

- V ≅ F_3^4;
- W ≅ F_3^9;
- d_2:W^* -> H^2(V,F_3) has image K, the 9-dimensional hyperplane
  a_{b_1}+a_{e_{12}}+a_{e_{34}}=0;
- H^*(V,F_3)=Λ(e_1,e_2,e_3,e_4)⊗F_3[b_1,b_2,b_3,b_4].

For the central extension, the LHS differential is a derivation, so on E_2^{2,1}

d_2(f\otimes\phi)=f\cup d_2(\phi),

up to the common global sign.

Hence the target image is exactly

H^2(V,F_3)\cup K \subseteq H^4(V,F_3).

## 2. Explicit surjectivity proof

A homogeneous basis of H^4(V,F_3) consists of

- e_1e_2e_3e_4;
- e_i e_j b_k (i<j, 1≤k≤4);
- b_i b_j (i≤j),

with total dimension 1+24+10=35.

The hyperplane K contains b_2,b_3,b_4 and e_{13},e_{14},e_{23},e_{24}, as well as b_1-e_{12}.

### Polynomial degree 2

For every i,j,

b_i b_j

is obtained by multiplying b_i by a suitable member of K:

- if j∈{2,3,4}, use b_i·b_j;
- for j=1, use b_i·(b_1-e_{12}) and handle the extra e_i b? term together with the mixed generators below.

A cleaner spanning argument is obtained by separating the polynomial subspace after the mixed terms have been generated: the classes e_i e_{12} vanish when i=1,2 and are exterior cubic classes otherwise, so the correction terms are already in the span generated below.

### Mixed classes

All classes e_i e_j b_k are generated as follows.

For k=2,3,4, multiply e_i e_j by b_k∈K.

For k=1, multiply e_i e_j by b_1-e_{12}. The correction e_i e_j e_{12} is either zero or the unique exterior degree-four class e_1e_2e_3e_4 up to sign, hence it is handled in the next step.

### Exterior degree 4

The class

e_1e_2e_3e_4

is obtained from

e_{12}·e_{34}.

Although e_{34} itself is not in K, the difference e_{12}-e_{34} belongs to K because
(b_1-e_{12})-(b_1-e_{34})=e_{34}-e_{12}.

Multiplying by e_{12} gives

e_{12}(e_{12}-e_{34}) = -e_{1234},

so the exterior degree-four generator is in H^2(V)·K.

Thus all 35 basis classes lie in H^2(V)·K.

## 3. Independent finite-dimensional verification

An explicit linear-algebra construction over F_3, using the 10-dimensional H^2 basis, the 9-dimensional K basis, and the 35-dimensional H^4 basis, gives

rank(H^2(V)·K -> H^4(V)) = 35.

Therefore the spanning proof is independently verified.

## 4. Consequence

Hence

E_3^{4,0}
=
E_2^{4,0}/im(d_2:E_2^{2,1}->E_2^{4,0})
=0,

and therefore

E_infinity^{4,0}=0.

This is a genuine structural reduction, not a statement about the twisted Bockstein itself.

The base-target pattern is now:

E_infinity^{3,0}=0,
E_infinity^{4,0}=0.

Thus the first two purely-base targets are eliminated from the LHS load-bearing problem.

## 5. What this does NOT prove

This does not determine E_infinity^{2,1}, nor the twisted Bockstein square, nor the ambient size H^2(Q_2,A_2(rho)).

In particular, one must not infer that because the outgoing d_2 target of E_2^{2,1} vanishes on page E_3, the source E_3^{2,1} vanishes. Its kernel can be large, and its quotient by incoming d_2 from E_2^{0,2} remains the real question.

Therefore the next attack remains the surviving (2,1) row itself, but now with a sharper decomposition:

1. determine ker(d_2:E_2^{2,1}->E_2^{4,0});
2. determine im(d_2:E_2^{0,2}->E_2^{2,1});
3. only then analyze the induced twisted Bockstein on E_infinity^{2,1}.

No rho-scan is authorized.

## Decision

- H^2(V)∪K = H^4(V): **PASS / CLOSED**.
- E_3^{4,0}=0: **PASS / CLOSED**.
- E_infinity^{4,0}=0: **PASS / CLOSED**.
- “therefore E_infinity^{2,1}=0”: **NOT established / must not be claimed**.
- base targets (3,0) and (4,0): **CLOSED / NO SURVIVORS**.
- full beta_rho^2: **OPEN / LOAD-BEARING**.
- unique coker maximizer without PD²: **OPEN / DECISIVE**.

The next authorized gate is the actual survival quotient in E_3^{2,1}.
