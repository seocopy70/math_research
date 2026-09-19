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


## Critical review — 2026-09-19

The preceding PASS must be narrowed. The formula
\[
\Theta_{R,P}(\lambda)(f)=f(P)+(\lambda\wedge f)(R)
\]
is mathematically correct once a relation jet \(J_3=\langle(R,P)\rangle\) is already supplied. But the audit did not prove that the required \(J_3\) is canonically determined by the originally prescribed bare filtered/graded datum.

### 1. Main issue: F5 was partly made tautological

If \(P_3\) is explicitly included as a distinguished element of the input datum, then defining \(f(P_3)\) is immediate. Likewise, once \(R_2\) is distinguished, \((\lambda\wedge f)(R_2)\) is canonical. Thus the result proves a conditional factorization:
\[
(V,J_3)\Longrightarrow B_\lambda,
\]
not yet the desired intrinsic recovery from the bare associated graded object.

### 2. Presentation/lift independence was asserted too quickly

The statement that any other presentation/lift inducing the same relation jet changes only the common scalar has not been independently proved. In particular, one must show that all allowed changes of defining relation preserve the coupled pair \((R_2,P_3)\) up to one common unit and do not introduce additional degree-3 terms that alter the functional \(f(P_3)\).

### 3. Automorphism naturality is conditional

Naturality of evaluation and exterior powers is straightforward for an isomorphism that already preserves the marked relation jet. What remains unproved is that every intrinsic automorphism of the bare graded/restricted object canonically preserves or reconstructs the distinguished \(J_3\). Hence the audit proves naturality of the marked object, not naturality of an unmarked reconstruction.

### 4. The 'minimal carrier' claim is not proved

\(D_3=(V,R_2,P_3)\) is a plausible sufficient carrier, but no minimality theorem was established. It should not be called the smallest carrier without a separate information-loss argument.

### 5. Unique zero is solid only after fixing the carrier

The nondegenerate symplectic calculation proving a unique \(\lambda\) is sound. It proves uniqueness conditional on the supplied \((R_2,P_3)\). It does not prove that the corresponding \(\lambda\) is recoverable from the bare graded object.

### Corrected status

The defensible conclusion is:

- F1–F4: PASS for the canonical finite-filtered quotient construction.
- F5-A: PASS for existence of a q-sensitive degree-3 carrier.
- **F5-marked: PASS as a formal factorization through the enriched relation jet \(J_3\).**
- **F5-bare: OPEN.** It remains to prove that the originally allowed bare filtered/graded datum canonically determines the distinguished relation jet \(J_3\), or else to prove that an equivalent unmarked construction exists.

Therefore the previous wording 'F5 structural factorization PASS' must not be read as closure of the original recovery theorem. No finite scan is authorized.
