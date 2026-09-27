# Paper 3 F1 q=3,n=4 — Level A computation record

## Date
2026-09-27

## Scope

After the original-text audit of Blumer–Quadrelli arXiv:2603.15464v2, the smallest authorized F1 sharpness computation was executed at (p,q,d,n)=(3,3,2,4), U_5(F_3).

The computation is deliberately split from the full Dwyer lift. Level A tests the explicit local obstruction only; it does not decide existence of the full fourfold lift.

## Input

Each alpha_h in H^1(G,F_3) is represented by its values (a_h,b_h,c_h,d_h), with the nonzero classes retained. Hence there are 80^4=40,960,000 ordered nonzero alpha-sequences.

The adjacent cup conditions are c_h d_{h+1}-d_h c_{h+1}=0 mod 3 for h=1,2,3.

## Level A results

| Stage | Count |
|---|---:|
| All ordered nonzero sequences | 40,960,000 |
| Cup-pass sequences | **3,681,856** |
| Level-A local-obstruction pass | **2,546,560** |
| Level-A local-obstruction fail | **1,135,296** |

For the local obstruction L(alpha)=a_2 a_3(a_1 b_4-a_4 b_1) mod 3, the failure count is 1,135,296, so the failure proportion among cup-pass sequences is approximately 30.8348%.

## Mathematical conclusion

The computation establishes: cup-vanishing does not imply the Level-A local condition.

It does not establish that cup-vanishing fails to imply the full fourfold Massey/Dwyer lift. The latter requires the Level-B compensation test involving A_2,B_2.

## Level B boundary

For [A_1,B_1]=I+C and [A_2,B_2]=I+D, the verified structural reduction is T_15=C_15+D_15+(CD)_15.

After the adjacent cup filter, D_13=D_24=D_35=0, and hence (CD)_15=0, so the final central coordinate reduces to T_15=C_15+D_15.

This is a verified reduction, not a claim that compensation always exists.

In particular, the fact that a free coordinate such as w_25 can enter D_15 does not by itself solve the full matrix relation: T_13,T_14,T_24,T_25,T_35 must simultaneously vanish.

## Computational policy

Do not enumerate arbitrary U_5(F_3) matrices for every Level-A failure.

The authorized sequence is: retain the 1,135,296 failure sequences; symbolically reduce the Level-B equations; identify the exceptional/compensation locus; only then perform the smallest necessary enumeration.

## Classification

- Level-A exhaustive enumeration: **PASS / CLOSED**
- cup-vanishing does not imply Level-A local condition: **PASS / CLOSED**
- full F1 q=3,n=4 sharpness: **OPEN / LOAD-BEARING**
- Level-B compensation: **OPEN / LOAD-BEARING**
- “Level-A failure implies full-lift failure”: **NOT ESTABLISHED**
- next authorized action: **Level-B symbolic reduction before exhaustive matrix enumeration**

## Reproducibility note

The Level-A implementation should save the actual failure sequences, not only aggregate counts, because those sequences form the input dataset for the Level-B analysis.