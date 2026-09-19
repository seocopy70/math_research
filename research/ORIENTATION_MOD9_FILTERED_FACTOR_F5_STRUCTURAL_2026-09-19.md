# ORIENTATION MOD-9 FILTERED FACTOR — F5 STRUCTURAL RECONSTRUCTION — 2026-09-19

## Scope

This audit closes the structural question left by F5-A, without a finite scan.

The minimal carrier is treated as a **degree-3 relation jet**, not as two independently rescalable classes:
\[
J_3=\langle (R_2,P_3)\rangle\subset L_2\oplus L_3^{res}.
\]
Here
\[
V=L_1,\qquad R_2=[X_1,X_2]+[X_3,X_4],\qquad P_3=X_1^{[3]}
\]
in the frozen coordinates.

The common scalar ambiguity in choosing a generator of the one-dimensional relation jet is essential: the obstruction is defined only up to a common nonzero scalar, which does not change its zero set.

## 1. Intrinsic definitions

Let \(V\) be the degree-one space, let \(R\in\Lambda^2V\) be the quadratic component of a generator of the relation jet, and let \(P\in V^{[3]}\) be its restricted degree-3 component.

For \(f\in V^*\), define

\[
\operatorname{Defect}_P(f)=f(P).
\]

This uses only the canonical evaluation pairing. No free presentation or lift is chosen.

For \(\lambda\in V^*\), define

\[
\operatorname{Twist}_{\lambda,R}(f)
=(\lambda\wedge f)(R).
\]

Here \(\lambda\wedge f\in\Lambda^2V^*\) and evaluation on \(R\in\Lambda^2V\) is canonical. Again, no presentation or preferred lift is involved.

Therefore the intrinsic first-order obstruction attached to the relation jet is

\[
\Theta_{R,P}(\lambda)(f)
=
f(P)+(\lambda\wedge f)(R).
\]

Equivalently,
\[
\Theta_{R,P}(\lambda)
=
\operatorname{ev}_P+\bigl(f\mapsto(\lambda\wedge f)(R)\bigr)
\in V^{**}.
\]

If the generator \((R,P)\) is replaced by \(c(R,P)\), \(c\in\mathbf F_3^\times\), then
\[
\Theta_{cR,cP}=c\,\Theta_{R,P}.
\]
Hence its zero set is independent of the generator. This is the correct intrinsic object when the relation is canonically known only up to a unit.

## 2. Recovery of the verified frozen formula

Take
\[
R=e_1\wedge e_2+e_3\wedge e_4,
\qquad
P=e_1^{[3]},
\]
and write
\[
\lambda=\sum a_i e_i^*,\qquad f=\sum f_i e_i^*.
\]

Then
\[
(\lambda\wedge f)(R)
=
a_1f_2-a_2f_1+a_3f_4-a_4f_3,
\]
while
\[
f(P)=f_1.
\]

Thus
\[
\Theta_{R,P}(\lambda)(f)
=
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4,
\]
which is exactly the previously verified twisted mod-9 lifting obstruction \(B_\lambda(f)\).

So the decomposition from F5-A is not merely schematic:
\[
B_\lambda
=
\operatorname{Defect}(P_3)+\operatorname{Twist}_\lambda(R_2)
\]
is an exact coordinate realization of the intrinsic formula.

## 3. Presentation/lift independence

The construction depends only on the graded/restricted relation jet \(J_3\).

A different free presentation or free lift that induces the same relation jet changes the chosen generator only by the common scalar ambiguity above, and hence changes \(\Theta\) only by a nonzero scalar.

Consequently the canonical datum is the zero set
\[
Z(J_3)=\{\lambda\in V^*:\Theta_{R,P}(\lambda)=0\},
\]
not a particular scalar-valued representative of \(\Theta\).

This is the exact amount of independence needed for orientation recovery.

## 4. Automorphism naturality

Let \(h:V\to V'\) be an isomorphism preserving the restricted structure and carrying the relation jet \(J_3\) to \(J_3'\).

For \(\lambda',f'\in(V')^*\), put
\[
\lambda=h^*\lambda',\qquad f=h^*f'.
\]
Then functoriality of evaluation and exterior powers gives
\[
\Theta_{R',P'}(\lambda')(f')
=
c^{-1}\Theta_{R,P}(h^*\lambda')(h^*f')
\]
for the common scalar \(c\) relating the chosen generators. Therefore
\[
Z(J_3')=(h^*)^{-1}Z(J_3).
\]

Thus the recovered character class is an isomorphism-natural invariant of the relation jet.

## 5. Uniqueness

Assume the quadratic component \(R\) is nondegenerate. Define
\[
\Phi_R:V^*\to V^{**},
\qquad
\Phi_R(\lambda)(f)=(\lambda\wedge f)(R).
\]

For a nondegenerate alternating form, \(\Phi_R\) is an isomorphism: in a symplectic basis it is the usual identification induced by the symplectic form.

The equation
\[
\Theta_{R,P}(\lambda)=0
\]
is therefore
\[
\Phi_R(\lambda)=-\operatorname{ev}_P,
\]
which has exactly one solution.

In the frozen basis,
\[
P=e_1^{[3]}
\]
and the solution is
\[
\lambda_\chi=e_2^*,
\]
because
\[
(e_2^*\wedge f)(e_1\wedge e_2+e_3\wedge e_4)=-f_1.
\]
Hence
\[
\lambda_\chi=(0,1,0,0),
\]
and therefore
\[
\rho(x_1,x_2,x_3,x_4)=(1,4,1,1)\pmod9,
\]
matching the canonical Demuškin orientation modulo 9.

## 6. Boundary and exact meaning of the PASS

This proves the following precise statement:

> The mod-9 twisted orientation obstruction factors through the degree-3 restricted relation jet \(J_3=\langle(R_2,P_3)\rangle\), provided that this relation jet is included as part of the prescribed graded datum.

It does **not** prove that the bare graded restricted Lie algebra \(\operatorname{gr}(G)\) with only its abstract operations automatically reconstructs the distinguished relation jet \(J_3\). That is a separate identification problem.

Accordingly the project should distinguish:
- **F5 structural factorization through the enriched carrier \(D_3=(V,J_3)\): PASS.**
- **Recovery from the bare unmarked associated graded restricted Lie algebra: not claimed.**

This is stronger and more precise than the earlier F5-A status, while avoiding the invalid inference that an abstract graded algebra alone canonically remembers the chosen Demuškin relation jet.

## Decision

\[
\boxed{
F1-F4=PASS,\qquad
F5\text{-A}=PASS,\qquad
F5\text{ (enriched relation-jet factorization)}=PASS.
}
\]

The remaining question, if the target theorem requires the **bare** associated graded object with no distinguished relation jet, is only whether that jet itself is canonically recoverable from that bare object. No finite scan is authorized; this is a separate structural gate.
