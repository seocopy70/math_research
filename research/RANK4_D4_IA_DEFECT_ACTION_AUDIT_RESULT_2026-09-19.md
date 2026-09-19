# Rank-4 D4 IA Defect-Action Audit Result — 2026-09-19

## Status

**LOCAL SUB-GATE PASS / MAIN DEFINITION GATE REMAINS OPEN**

The first-layer IA defect-action audit was executed on the frozen degree-3 Magnus model. It does not authorize a rank-4 representative scan.

## 1. Frozen target and correction space

The degree-3 associative Magnus target is
[
A_3 cong mathbf F_3^{4\otimes 3},
qquad dim A_3=64.
]

The ordinary degree-3 normal-closure/conjugation correction space is
[
C_3=operatorname{span}{[X_i,R_2]:1le ile4},
qquad dim C_3=4.
]

These are the same frozen conventions used in the preceding rank-4 lift-independence audit.

## 2. First IA layer

The degree-2 IA parameters are
[
operatorname{Hom}(V,L_2),
qquad
dim V=4,quad dim L_2=6,
]
hence dimension 24.

The audit used the 24 elementary parameters
[
x_imapsto x_i[x_j,x_k],
qquad 1le j<kle4,
]
as a basis of the first IA layer.

No full (GSp_4(mathbf F_3)) scan was performed.

## 3. Defect-change law

For each of three fixed linear-action representatives
- identity;
- (-I);
- the standard transvection (e_1mapsto e_1+e_2),

the degree-3 defect change under the 24 IA directions was computed for both
[
r_3=x_1^3[x_1,x_2][x_3,x_4]
]
and
[
r_infty=[x_1,x_2][x_3,x_4].
]

For all three representatives:

[
oxed{operatorname{rank}(Delta_{mathrm{IA}})=20}
]

for both q=3 and q=infinity, and the two variation maps agree exactly.

Pairwise additivity over all 24 IA basis directions was also checked exactly. Thus, at this degree and for the tested representatives, the IA defect-change law is linear in the first IA-layer parameter and is independent of the chosen basepoint at the tested tangent level.

## 4. Candidate gauge quotient

The combined gauge span is

[
C_3+Delta_{mathrm{IA}},
qquad
dim(C_3+Delta_{mathrm{IA}})=20.
]

Hence the candidate quotient of the degree-3 target has dimension

[
oxed{64-20=44}.
]

This is a **candidate** quotient object only. Its global canonicity and compatibility under change of linear representative have not yet been proved.

## 5. q-sensitive nontriviality test

Let
[
p_g
=
operatorname{def}_{q=3}(g)-operatorname{def}_{q=infty}(g).
]

For the identity representative,
[
p_g=0.
]

For both (-I) and the standard transvection,
[
p_g
e0
]
and, critically,

[
oxed{
p_g
otin C_3+Delta_{mathrm{IA}}.
}
]

Therefore the q=3 restricted-power defect survives the tested IA gauge quotient.

This is the required nontriviality check: the first IA quotient does **not** automatically erase the q-sensitive degree-3 signal.

## 6. Interpretation

The negative result from the previous lift-independence audit is therefore sharpened, not reversed:

- the raw degree-3 defect is genuinely lift-dependent;
- the first IA change law has a finite-dimensional, linear degree-3 shadow;
- quotienting by the ordinary correction space together with this IA variation space is a mathematically viable **candidate** mechanism for removing first-layer lift dependence;
- the q=3 restricted-power signal survives this candidate quotient for the two nontrivial test representatives.

This is not yet a theorem of canonicality.

In particular, the audit does **not** establish:
1. that the 44-dimensional quotient is independent of the chosen free-group coordinates;
2. that the quotient construction is equivariant/functorial under the relevant (GSp_4(mathbf F_3)) action;
3. that the same quotient can be assembled into an intrinsic observable on linear maps;
4. any full rank-4 q=3 versus q=infinity classification;
5. recovery of the 3-adic orientation character.

## 7. Gate consequence

The main gate remains **OPEN**.

The next authorized task is a **quotient-legitimacy / equivariance audit**:

- prove that the first IA variation subspace is canonically defined from the frozen filtered data, rather than from a selected basis of IA directions;
- verify its transformation law under a change of linear representative;
- determine whether the 44-dimensional quotient carries the required compatible action;
- only then consider a small number of q-comparison representatives.

No full rank-4 scan is authorized yet.

## 8. Execution

Script:
`research/rank4_D4_ia_extension_audit_2026-09-19.py`

The exact audit logic was independently executed during this gate. The repository also contains:
`.github/workflows/rank4-d4-ia-extension-audit.yml`

The workflow is configured for push/manual execution; the available GitHub workflow-run reader exposes PR-triggered runs only, so no claim about a push-run CI result is made here.
