# Paper 5 — Two-Level Relation-Jet Stabilizer Audit

Date: 2026-10-05

## Scope
For the marked family
\[
G_{s,a}=\langle z,x,y\mid z^{p^s}=x^{p^a}[x,y]\rangle,
\]
with odd prime p, the finite window at the first relevant cutoff carries a degree-2 commutator component and, when visible, a degree-p restricted-power component. The four audited cases are represented by the projective relation jets

- (0,1): \(\rho=[x,y]+x^{[p]}\),
- (1,1): \(\rho=[x,y]+z^{[p]}-x^{[p]}\),
- (0,2): \(\rho=[x,y]\),
- (1,2): \(\rho=[x,y]+z^{[p]}\).

The relevant linear stabilizer is the stabilizer of the **line** spanned by \(\rho\), not of a fixed representative. This distinction is essential and explains the coupled diagonal scalars.

## Algebraic stabilizer calculation
Write a linear substitution on \(V=\langle x,y,z\rangle\). Because p is odd and Frobenius is the identity on \(\mathbf F_p\), \((a v)^{[p]}=a v^{[p]}\) for \(a\in\mathbf F_p\), while the bracket transforms by the determinant on its two-plane.

1. \(\rho_{01}=[x,y]+x^{[p]}\). Preservation of the pure restricted-power line forces \(x\mapsto ax\). Preservation of the quadratic support then forces \(y\mapsto bx+y\) and forbids a z-component in the image of y. The z-column is free modulo invertibility. Both displayed components scale by a, so the relation line is preserved. Hence
\[
S_{01}(p)=\left\{\begin{pmatrix}a&b&c\\0&1&d\\0&0&e\end{pmatrix}:a,e\ne0\right\}.
\]
Its order is \(p^3(p-1)^2\).

2. \(\rho_{11}=[x,y]+z^{[p]}-x^{[p]}\). The two pure-power support lines force x and z to remain on their respective lines; the quadratic term forbids a z-component in y and the relation-line condition forces the x- and z-scalars to agree. The remaining y-shear is free. Thus
\[
S_{11}(p)=\left\{\begin{pmatrix}a&b&0\\0&1&0\\0&0&a\end{pmatrix}:a\ne0\right\},
\]
with order \(p(p-1)\).

3. \(\rho_{02}=[x,y]\). The stabilizer is the parabolic preserving the two-plane \(\langle x,y\rangle\). Therefore
\[
S_{02}(p)=\left\{\begin{pmatrix}A&v\\0&e\end{pmatrix}:A\in GL_2(\mathbf F_p),\ v\in\mathbf F_p^2,\ e\ne0\right\},
\]
with order \(|GL_2(p)|p^2(p-1)\).

4. \(\rho_{12}=[x,y]+z^{[p]}\). The bracket scales by \(\det A\) for \(A\) on \(\langle x,y\rangle\), while z^{[p]} scales by the z-scalar. Preservation of the relation line therefore forces the z-scalar to equal \(\det A\), with no x/y-to-z mixing. Hence
\[
S_{12}(p)=\{\operatorname{diag}(A,\det A):A\in GL_2(\mathbf F_p)\},
\]
with order \(|GL_2(p)|\).

Consequently
\[
|S_{01}|/|S_{11}|=|S_{02}|/|S_{12}|=p^2(p-1),
\]
so the p-primary ratio is exactly \(p^2\).

## What this closes
The **abstract GL stabilizer theorem for the four two-level relation jets** is PASS / CLOSED for every odd prime p, under the stated marked/projective-jet definitions. The proof is presentation-independent at the level of the declared vector space and its bracket/restricted-power operations.

This is stronger than the p=3 and p=5 finite computations: those computations independently certify that the actual Frattini images equal these candidate groups in the tested cases.

## What remains open
The load-bearing missing implication is the finite-window factorization
\[
\operatorname{Im}(Aut(W_n)\to GL(V))\subseteq Stab_{GL(V)}(\rho_{s,a})
\]
and, for the strongest result, equality with that stabilizer for general odd p and the relevant parameters. The current p=3/p=5 certificates establish equality only in the audited finite cases.

Therefore **no uniform automorphism-order-gap theorem is promoted**. The structural localization is:

- abstract jet stabilizer formulas: PASS / CLOSED;
- actual finite-window image = jet stabilizer in audited p=3,p=5 cases: PASS / LOCAL;
- general odd-p factorization/equality: OPEN / LOAD-BEARING;
- p^2 gap as a general theorem: OPEN.

## Next authorized gate
Prove the factorization from the finite-window automorphism action to the degree-(2,p) relation jet without inserting presentation-dependent data, then test equality for a new odd prime (or derive a general lifting theorem). If factorization fails, record the counterexample rather than repairing the jet ad hoc.
