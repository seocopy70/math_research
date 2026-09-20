# HARD ATTACK 48 — TARGET-SIDE CORRECTION: THE BASE H^3 ROW IS ALREADY KILLED AT d_2

Date: 2026-09-20

## Target

Hard Attack 47 computed a nonzero raw base-row value
d_lambda^V(z_R) in H^3(V,F_3) and then incorrectly identified the only possible incoming differential to (3,0) after d_2 as d_3:E_3^{0,2}->E_3^{3,0}.

This is false. There is already an incoming
d_2:E_2^{1,1}->E_2^{3,0}.

The present attack computes that d_2 image. The result is stronger and cleaner than the HA47 target: the entire H^3(V,F_3) is hit. Hence
E_3^{3,0}=0,
so the raw base-row term from HA47 has no E_infinity^{3,0} survivor at all.

## 1. Correct LHS differential

For the central extension
1 -> W -> Q_2 -> V -> 1
with W central, write
K=im(d_2:W^*->H^2(V,F_3)).
By HA45, K is the 9-dimensional hyperplane in H^2(V,F_3) annihilating the relation-jet
z_R=b_1+e_1e_2+e_3e_4.

On
E_2^{1,1}=H^1(V,F_3)\otimes W^*,
the LHS d_2 is the derivation determined by the transgression:
d_2(f\otimes\phi)=f\cup d_2(\phi)
(up to the same harmless global sign).

Therefore
im(d_2:E_2^{1,1}->E_2^{3,0})
=
V^*\cup K
\subseteq H^3(V,F_3).

The question is whether V^* K fills H^3(V,F_3).

## 2. Explicit linear-algebra proof

Use
H^*(V,F_3)=Lambda(e_1,e_2,e_3,e_4)\otimes F_3[b_1,b_2,b_3,b_4].

A basis of H^3(V,F_3) is
{e_i e_j e_k}_{i<j<k}
union
{e_i b_j}_{1<=i,j<=4},
so dim H^3(V,F_3)=4+16=20.

The hyperplane K is defined by
a_{b_1}+a_{e_1e_2}+a_{e_3e_4}=0.

In particular K contains:
- b_2,b_3,b_4;
- e_{13},e_{14},e_{23},e_{24};
- b_1-e_{12};
- b_1-e_{34}.

From these generators:

1. All e_i b_j with j=2,3,4 lie in V^* K immediately.

2. For j=1,
e_i(b_1-e_{12}) = e_i b_1 - e_i e_{12},
and the exterior term e_i e_{12} is either zero or one of the exterior cubic basis vectors already generated below. Hence all e_i b_1 also lie in V^* K.

3. All exterior cubic classes are generated:
- e_1e_2e_3 = e_1 e_{23};
- e_1e_2e_4 = e_1 e_{24};
- e_1e_3e_4 = -e_1(e_{12}-e_{34});
- e_2e_3e_4 = -e_2(e_{12}-e_{34}).

Thus every basis element of H^3(V,F_3) belongs to V^*K.

Therefore
\[
\boxed{V^*\cup K=H^3(V,F_3).}
\]

As an independent finite-dimensional verification, the 36 products obtained from a basis of K and the four e_i have rank 20 over F_3.

## 3. Consequence

Hence
\[
E_3^{3,0}
=
E_2^{3,0}/im(d_2:E_2^{1,1}->E_2^{3,0})
=0.
\]

Therefore automatically
\[
E_\infty^{3,0}=0.
\]

This completely disposes of the HA47 base-target survival question. There is no need to compute d_3^{0,2} for this particular target: its target E_3^{3,0} is already zero.

In particular, the explicit nonzero class
d_{e_2}^V(z_R)
=
2b_1e_2-e_1b_2+b_3e_4-e_3b_4+e_2e_3e_4
from HA47 is killed in the LHS spectral sequence at the d_2 target stage.

The important point is that this is not a mysterious cancellation and does not depend on the special choice lambda=e_2. The target filtration quotient itself vanishes.

## 4. Critical correction to HA47

HA47 stated:

"the only possible incoming LHS differential to (3,0) after d_2 is d_3:E_3^{0,2}->E_3^{3,0}."

That statement was wrong because d_2:E_2^{1,1}->E_2^{3,0} is also present.

The corrected logical chain is:

E_2^{1,1} --d_2--> E_2^{3,0},
with image V^*K=H^3(V,F_3),
so E_3^{3,0}=0,
hence E_infinity^{3,0}=0.

This correction is load-bearing and supersedes the HA47 "next gate = d_3^{0,2}" formulation.

## 5. Research significance

This attack does NOT solve beta_rho^2.

It does establish a sharp negative result for one tempting route:

**the base-filtration contribution of beta_rho^2 cannot survive into E_infinity^{3,0}.**

Thus the second Bockstein layer, if it affects the ambient H^2 size, must be detected through the remaining LHS filtration pieces:
- source E_infinity^{1,1} and E_infinity^{0,2};
- target pieces E_infinity^{2,1}, E_infinity^{1,2}, E_infinity^{0,3}.

This is useful because it removes the entire (3,0) target row from the load-bearing problem.

It also shows that the raw nonzero calculation in HA47 was not itself evidence for a new ambient obstruction: it was an E_2-page artifact that is killed by the universal central-extension transgression geometry.

## 6. Next gate

The next authorized calculation should therefore move to the first genuinely surviving target filtration:

\[
E_\infty^{2,1}
\]

and the source component

\[
E_\infty^{1,1}
\]

for beta_rho^2.

The d_2 maps on these rows are still determined by the same extension class K. The question is whether the induced twisted Bockstein on these surviving rows is:
1. forced by the relation line (R,p);
2. determined by a finite additional shadow of e_2;
3. or genuinely independent.

No rho-scan is authorized.

## Decision

- correction of HA47 target differential: **PASS / CLOSED**;
- V^* cup K = H^3(V,F_3): **PASS / CLOSED**;
- E_3^{3,0}=0 and hence E_infinity^{3,0}=0: **PASS / CLOSED**;
- HA47 "d_3 is the first possible incoming differential" claim: **FAIL / CLOSED / SUPERSEDED**;
- base-filtration contribution to E_infinity^{3,0}: **CLOSED / NO SURVIVOR**;
- full beta_rho^2 determination: **OPEN / LOAD-BEARING**;
- unique coker maximizer without PD^2: **OPEN / DECISIVE**.

Record immediately in CURRENT_STATE.md, RESEARCH_MAP.md, and research/00_RESEARCH_LOG.md.
