# Rank-4 D4 Quotient-Valued q-Defect Composition Audit — 2026-09-19

## Status
**PASS / LOCAL**

## CI
- Run: 35417325110
- Commit: 1ee1680f071c77ee3b6042eb1436df507d9f3406
- Workflow: rank4-d4-ia-quotient-defect-composition

## 1. Correct defect object

The first attempted law for the absolute normalized relator defect
[
[F_g(R_3)-mu(g)R_3]_{deg 3}
]
failed on all 16 ordered pairs. This is recorded as a genuine negative diagnostic; that absolute defect is not promoted to the quotient cocycle.

The q-sensitive object is instead the difference of the q=3 and q=infinity defects:
[
Delta_q(g)
=
[delta_3(g)-delta_infty(g)]
=
[F_g(X_1^3)-X_1^3]_{deg 3}.
]

For an admissible lift (F_g) with
[
g e_1=mu(g)e_1,
]
the degree-3 source (X_1^3) transforms by the multiplier (mu(g)). The multiplier therefore belongs in the source transformation convention, but the composition law for the difference (Delta_q) itself is the ordinary cocycle law below.

## 2. Tested composition law

For (F_{gh}=F_gcirc F_h), the candidate law is
[
oxed{
Delta_q(gh)=Delta_q(g)+gcdotDelta_q(h)
}
]
in
[
Q_3=A_3/(C_3+Delta_{mathrm{IA}}).
]

The audit tested all (4	imes4=16) ordered pairs of:
1. identity;
2. (-I);
3. (e_1mapsto e_1+e_2);
4. (operatorname{diag}(2,1,2,1)), multiplier (2).

## 3. Exact results

[
operatorname{rank}(C_3+Delta_{mathrm{IA}})=20,
qquad
dim Q_3=44.
]

For all 16 ordered pairs:
[
oxed{	ext{candidate-law failures modulo }Q_3=0}.
]

The raw ambient equality does not hold:
[
oxed{	ext{raw candidate-law failures}=16}.
]
This is expected at this stage because the quotient removes the verified (C_3+Delta_{mathrm{IA}}) gauge variation.

All 16 composed defects had nonzero quotient classes in this controlled set.

## 4. Important qualification

The reversed diagnostic formula
[
Delta_q(gh)=Delta_q(h)+hcdotDelta_q(g)
]
also had zero failures modulo (Q_3) on this four-representative test set. Therefore the present computation establishes the candidate cocycle law as a valid local law, but **does not by itself prove uniqueness of the transport/order convention** at the quotient level.

The raw failures of both formulas are 16/16.

Thus this gate is a **local PASS for existence/compatibility of the candidate quotient-valued law**, not yet a full canonical action/cocycle theorem.

## 5. Consequence

The previous main gate can now be narrowed from “define the transformation/composition law” to:

[
oxed{
	ext{extend and audit the quotient-valued q-defect cocycle law beyond the four controls,
while fixing the precise action/order convention.}
}
]

No full rank-4 scan is authorized yet.

## 6. Scope boundary

This result does not establish:
- arbitrary free-group coordinate naturality;
- full GSp(_4(mathbf F_3)) cocycle covariance;
- uniqueness of the quotient action convention;
- a canonical class independent of all coordinate choices;
- recovery of (chi).

It does establish a concrete, nontrivial local quotient-valued q-sensitive composition law on the tested admissible representatives.
