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


## 2026-10-05 — Factorization Lemma Step-B critical audit

The proposed Step-B proof skeleton is accepted as the correct **load-bearing target**, but it contains several nontrivial assumptions that must not be promoted to lemmas without proof.

### B-1 lift: NOT available from Hopficity

The proposed statement

[
Aut(W_n)	woheadleftarrow N_{Aut(F)}(R_n)/Stab
]

does **not** follow from “(W_n) is a finite/Hopfian p-group with a free presentation.” Hopficity concerns surjective endomorphisms of (W_n); it gives no general lifting theorem for automorphisms of a quotient through a chosen free presentation. The classical formulation of the problem itself treats surjectivity of (Stab_{Aut(F)}(R)	o Aut(F/R)) as a separate and generally difficult question. Therefore B-1 is **OPEN**, not a routine preliminary lemma.

For the present Paper 5 factorization, the preferred route is therefore **not to assume a lift**. Seek an intrinsic formulation through the minimal presentation/relation module and the induced action on the associated graded relation data. A lift may be used only if a separate theorem is proved for this specific (W_n).

### B-2a: degree-2 correction is valid only after the correction class is justified

If one has (cin [R_n,F]) and (R_nsubseteq D_2(F)), then

[
[R_n,F]subseteq[D_2,D_1]subseteq D_3,
]

so the degree-2 class of the correction vanishes. This part is sound.

However, the stronger asserted normal form

[
widetildealpha(r)=r^{pm1}c,qquad
cin [R_n,F]D_{p+2}
]

does **not** follow merely from (widetildealpha(R_n)=R_n). It requires an independent relation-module calculation. Stabilizing the normal closure of (r) does not automatically force the exponent to be (pm1), nor does it automatically eliminate all lower filtered relation-module corrections.

### B-2b: the mixed (D_2/D_p) issue is deeper than BCH bookkeeping

The statement that the (D_2) component “does not pollute” the degree-(p) component is not yet a proved consequence of (2+p>p+1). The problem is not only multiplication of two homogeneous group elements; it is the **choice of a representative/lift of the degree-2 relation class** before extracting a secondary degree-(p) class.

For a relation (rin D_2setminus D_3), the raw map
(pi_p:D_p	o D_p/D_{p+1}) is not even defined on (r) unless (rin D_p). Thus the notation
[
J=(pi_2(r),pi_p(r))
]
for a mixed relation is not intrinsically meaningful as written.

The correct object must instead be a **filtered relation module / extension of the degree-2 relation line**, with a well-defined secondary degree-(p) class modulo the ambiguity generated by the degree-2 relation. Only after this object is defined can a jet-separation lemma be proved.

Accordingly, B-2b is **OPEN / LOAD-BEARING**, and the present “BCH degree separation” sentence is only a heuristic motivation.

### B-3: the scalar ambiguity is projective, not merely (pm1)

For an abstract automorphism preserving a one-dimensional relation module, the natural first conclusion is preservation of the **relation line**, hence multiplication by some scalar (lambdainmathbf F_p^	imes) (or by a unit before reduction), not necessarily only (lambda=pm1).

Therefore the current audit must distinguish:

- fixed-vector stabilizer: (gJ=J);
- projective/line stabilizer: (glangle Jangle=langle Jangle).

The p=3/p=5 finite certificates currently support the **projective/line** stabilizer formulas used in the abstract theorem. A reduction from arbitrary (lambdainmathbf F_p^	imes) to (pm1) would be an additional theorem and is not currently justified.

### Corrected factorization target

The mathematically safe load-bearing statement is therefore:

[
oxed{
operatorname{Im}ho_n
subseteq
operatorname{Stab}_{GL(V)}
igl(mathcal J_{s,a}igr)
}
]

where (mathcal J_{s,a}) is an **intrinsically defined filtered relation-jet object**, preferably a relation-module/graded-extension object, and the stabilizer is interpreted in the appropriate projective sense.

The present concrete formulas for (S_{01},S_{11},S_{02},S_{12}) remain **PASS / CLOSED as abstract marked/projective stabilizer calculations**. What is not closed is the bridge from the finite quotient (W_n) to that abstract jet.

### Decision

- “No new blind GAP calculation now”: **ACCEPTED**.
- “Factorization lemma is the unique load-bearing gate”: **ACCEPTED**, with the corrected intrinsic formulation above.
- B-1 lift lemma as stated: **FAIL / CLOSED as a proof shortcut**; the underlying lifting question remains **OPEN**.
- B-2a degree-2 correction vanishing, conditional on (cin[R,F]): **PASS / LOCAL**.
- B-2b mixed-degree secondary jet: **OPEN / LOAD-BEARING**.
- B-3 (pm1)-only scalar reduction: **FAIL / CLOSED as currently justified**; projective scalar ambiguity remains.
- General odd-(p) finite-window factorization: **OPEN / LOAD-BEARING**.
- Quotient-action run `37252335078`: remains a separate **OPEN / EXECUTION BLOCKED** auxiliary gate and is not the current mathematical bottleneck.

Immediate next proof task: define (mathcal J_{s,a}) intrinsically via the filtered relation module (or prove an equivalent canonical construction), then prove that every finite-window automorphism acts through its projective stabilizer. No new prime sweep is authorized before this definition/factorization proof is settled.
