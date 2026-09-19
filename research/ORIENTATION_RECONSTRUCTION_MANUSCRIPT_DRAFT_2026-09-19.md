# Recovering the 3-adic Orientation of a Demuškin Pro-3 Group from Filtered Relation Jets

**Manuscript draft — 2026-09-19**

## Abstract

We study the extent to which the canonical orientation character
\[
\chi:G\to\mathbf Z_3^\times
\]
of a rank-four Demuškin pro-\(3\) group can be reconstructed from filtered and graded relation data. For the standard presentation
\[
G_3=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle,
\]
the quadratic initial relation
\[
R_2=[X_1,X_2]+[X_3,X_4]
\]
does not retain enough information to distinguish the \(q=3\) orientation from the \(q=\infty\) case. The first useful enrichment is the projective degree-\((2,3)\) relation jet
\[
J_3=[(R_2,P_3)],\qquad P_3=X_1^{[3]}.
\]
From this jet one obtains a natural degree-one crossed-derivation functional
\[
\Theta_J(\lambda)(f)=f(P_3)+(\lambda\wedge f)(R_2).
\]
Its zero set is intrinsic under the relevant presentation, lift, relator-gauge, and normalization changes, and for \(q=3\) it has the unique zero \(\lambda=e_2^*\). Hence \(J_3\) recovers the canonical orientation modulo \(9\).

We then identify the precise information carried by this construction. The raw jet is not minimal in the natural quotient category determined by all degree-one evaluation observables. Its coarsest quotient is
\[
\overline J_3=[(R_2,p(P_3))],
\]
where
\[
p:L_3^{res}(V)\to L_3^{res}(V)/[V,L_2(V)]\cong V^{(1)}.
\]
This quotient is terminal among functorial quotients preserving the full degree-one evaluation family.

For the full \(3\)-adic character, a compatible filtered relation-jet tower \(J_n\) yields unique finite-level characters
\[
\chi_n:G\to(\mathbf Z/3^n)^\times,
\qquad
\chi_n(x_2)=(-2)^{-1}\pmod{3^n},
\]
and hence, by inverse limit,
\[
\chi(x_2)=(1-3)^{-1}.
\]
At the same time, a family
\[
G_{3^s}=\langle x_i\mid x_1^{3^s}[x_1,x_2][x_3,x_4]\rangle
\]
shows that no universal carrier with both bounded filtration degree and finite \(3\)-adic precision can recover the full orientation: the \(q\)-dependent power term first appears in degree \(3^s\). Thus the results establish a sharp information hierarchy rather than a claim that one finite \(\mathbf F_3\)-jet universally contains the whole \(3\)-adic character.

The paper isolates a general reconstruction pattern: when an invariant is invisible in the associated graded object, one should retain the first filtered relation jet in which the hidden parameter couples to the leading relation, and then quotient away exactly the information invisible to the relevant observables.

---

## 1. Introduction

A recurring difficulty in filtered algebraic problems is that passage to an associated graded object can erase extension information that is essential for recovering an invariant of the original object. The graded object records leading terms, but not necessarily how successive filtered pieces are coupled inside an actual relation.

This issue occurs naturally for Demuškin pro-\(p\) groups. Their associated graded restricted Lie algebra is controlled by the quadratic initial form of the defining relation, while the canonical orientation character is a genuinely \(p\)-adic invariant. The question addressed here is:

> **How much filtered relation information is necessary and sufficient to recover the canonical orientation character?**

The answer obtained in the rank-four pro-\(3\) model has three layers.

First, the bare quadratic graded relation is insufficient. The \(q=3\) and \(q=\infty\) presentations have the same quadratic initial relation
\[
R_2=[X_1,X_2]+[X_3,X_4],
\]
but their orientations already differ modulo \(9\).

Second, the missing information appears in the coupling between the quadratic relation and its degree-three restricted-power component. This produces the projective relation jet
\[
J_3=[(R_2,P_3)]
\]
and the intrinsic recovery equation
\[
f(P_3)+(\lambda\wedge f)(R_2)=0.
\]
For the standard \(q=3\) presentation the unique solution is
\[
\lambda=e_2^*,
\]
so
\[
\chi(x_1),\chi(x_2),\chi(x_3),\chi(x_4)
\equiv(1,4,1,1)\pmod9.
\]

Third, the full \(3\)-adic problem separates into two logically different questions. A compatible sequence of finite-level filtered relation jets determines all reductions \(\chi\bmod3^n\), hence the full character by inverse limit. But there is no universal bounded-degree, finite-precision carrier that can do this for the whole family \(q=3^s\). Exact \(\mathbf Z_3\)-coefficients for the fixed \(q=3\) group are different: they contain infinitely many \(3\)-adic digits and can recover the full character at bounded filtration degree.

The purpose of the paper is therefore not to claim an absolute “minimal jet” in every conceivable category. Instead, it identifies a precise coarsest carrier for a natural observable category and establishes sharp positive and negative information results.

---

## 2. The model and conventions

We fix
\[
G_3=
\left\langle
x_1,x_2,x_3,x_4
\mid
r=x_1^3[x_1,x_2][x_3,x_4]=1
\right\rangle
\]
with group commutator
\[
[x,y]=x^{-1}y^{-1}xy.
\]

The corresponding \(q=\infty\) model is
\[
G_\infty=
\left\langle
x_1,x_2,x_3,x_4
\mid
[x_1,x_2][x_3,x_4]=1
\right\rangle.
\]

Let \(V\) denote the degree-one \(\mathbf F_3\)-space. In the standard coordinates,
\[
V=\langle e_1,e_2,e_3,e_4\rangle.
\]

The quadratic initial relation is
\[
R_2=e_1\wedge e_2+e_3\wedge e_4.
\]

For \(q=3\), the degree-three restricted-power contribution of the same filtered relation is
\[
P_3=X_1^{[3]}.
\]
For \(q=\infty\), the corresponding degree-three component is zero.

The canonical orientation is the unique orientation arising from the standard Demuškin crossed-derivation characterization. In the frozen \(q=3\) normal form it satisfies
\[
\chi(x_1)=\chi(x_3)=\chi(x_4)=1,
\qquad
\chi(x_2)=(1-3)^{-1}.
\]

All statements below use the frozen commutator convention above.

---

## 3. Loss of information at the quadratic graded level

The first obstruction is immediate.

For both \(G_3\) and \(G_\infty\), the defining relation has the same degree-two initial term:
\[
R_2=[X_1,X_2]+[X_3,X_4].
\]

The \(x_1^3\) term in the \(q=3\) relation occurs in Zassenhaus degree \(3\), so it is absent from the quadratic initial form.

Nevertheless,
\[
\chi_3(x_2)=4\pmod9,
\qquad
\chi_\infty(x_2)=1\pmod9.
\]

Thus the bare quadratic graded relation cannot determine even \(\chi\bmod9\).

This is not merely a failure of one proposed formula. It is an information-level obstruction: the two groups have the same quadratic relation but different orientation characters.

The missing datum is therefore not another function of \(R_2\) alone. It must retain how the degree-three filtered relation component is coupled to \(R_2\).

---

## 4. The projective degree-\((2,3)\) relation jet

### 4.1 Definition

For a minimal free pro-\(3\) presentation, write the filtered defining relation through degree three as
\[
r=(R_2,P_3)+O(4).
\]

The relevant object is its projective relation jet
\[
J_3=[(R_2,P_3)].
\]

The projectivization is essential. A change of relation generator can multiply both components by a common unit, and a relator conjugation can add a degree-three bracket term.

For \(\lambda,f\in V^*\), define
\[
\Theta_J(\lambda)(f)
=
f(P_3)+(\lambda\wedge f)(R_2).
\]

The canonical orientation modulo \(9\) is encoded by the unique zero of this functional.

### 4.2 Explicit calculation

Write
\[
\lambda=a_1e_1^*+a_2e_2^*+a_3e_3^*+a_4e_4^*
\]
and
\[
f=f_1e_1^*+f_2e_2^*+f_3e_3^*+f_4e_4^*.
\]

For
\[
R_2=e_1\wedge e_2+e_3\wedge e_4,
\qquad
P_3=e_1^{[3]},
\]
the functional becomes
\[
\Theta_J(\lambda)(f)
=
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]

Since this must vanish for every \(f\),
\[
a_1=a_3=a_4=0,
\qquad
a_2=1.
\]

Hence
\[
\boxed{\lambda_\chi=e_2^*.}
\]

Writing
\[
\rho=1+3\lambda\pmod9,
\]
we obtain
\[
\boxed{
\rho(x_1),\rho(x_2),\rho(x_3),\rho(x_4)
=(1,4,1,1)\pmod9.
}
\]

Thus the degree-\((2,3)\) relation jet recovers
\[
\boxed{\chi\pmod9.}
\]

For \(q=\infty\), \(P_3=0\), and nondegeneracy of \(R_2\) gives the unique zero
\[
\lambda=0.
\]
Consequently the same carrier separates \(q=3\) from \(q=\infty\) without inserting \(q\) into the definition.

---

## 5. Intrinsicity: presentation, lift, and gauge changes

A chosen defining relator is not itself canonical. The relevant question is whether the recovery zero set survives the allowed changes.

Let a free automorphism inducing the identity on \(G\) have degree-two corrections
\[
\alpha(X_i)=X_i+Q_i+O(3).
\]
Minimality and the one-dimensional quadratic initial relation imply
\[
Q_i=c_iR_2.
\]

At degree three, the induced change of the relation jet has the form
\[
(R_2,P_3)
\longmapsto
(uR_2,uP_3+[v,R_2]),
\]
where \(u\) is a unit and \(v\in V\).

For every degree-one functional \(f\),
\[
f([v,R_2])=0.
\]

Therefore
\[
\Theta'(\lambda)=u\,\Theta(\lambda).
\]

The scalar \(u\) does not change the zero set. Hence the recovered covector is invariant under the degree-\((2,3)\) presentation/lift/relator gauge relevant to the calculation.

This establishes the following precise statement.

### Proposition 5.1

Under the standard minimal one-relator pro-\(3\) presentation hypotheses and the frozen filtration convention, the zero set
\[
Z(\Theta_J)
=
\{\lambda\in V^*:\Theta_J(\lambda)=0\}
\]
is invariant under the degree-\((2,3)\) presentation and relator gauge.

The statement concerns the recovery observable. It does **not** assert that a chosen generator of the full relation module is itself canonical.

Automorphism naturality follows from the functoriality of the induced action on \(V\), exterior powers, and the same cancellation of the bracket gauge.

---

## 6. The coarsest natural carrier

The raw \(J_3\) contains more information than the recovery functional sees.

There is a canonical quotient
\[
p:
L_3^{res}(V)
\longrightarrow
L_3^{res}(V)/[V,L_2(V)].
\]

In characteristic \(3\), the quotient is the restricted-cube component
\[
V^{(1)}.
\]

For every degree-one \(f\),
\[
f(P_3)=f(p(P_3)),
\]
and
\[
f([v,R_2])=0.
\]

Thus define
\[
\boxed{
\overline J_3=[(R_2,p(P_3))]
\subset
\mathbf P\bigl(\Lambda^2V\oplus V^{(1)}\bigr).
}
\]

For the standard examples,
\[
\overline J_3(3)
=
[(R_2,e_1^{(1)})],
\qquad
\overline J_3(\infty)
=
[(R_2,0)].
\]

### Theorem 6.1 — Coarsest quotient theorem

Consider the category of functorial quotients of the projective degree-\((2,3)\) relation jet that preserve all degree-one observables
\[
\Theta_{R,P}(\lambda)(f)
=
f(P)+(\lambda\wedge f)(R).
\]

Then every such quotient factors uniquely through
\[
J_3\twoheadrightarrow\overline J_3.
\]

Hence \(\overline J_3\) is terminal, equivalently the coarsest admissible quotient, in this category.

#### Proof

If two jets have different \(p(P)\), choose \(f\) with
\[
f(p(P)-p(P'))\neq0.
\]
Then the corresponding observables differ already at \(\lambda=0\), so no quotient preserving all observables can identify them.

Likewise, different projective quadratic relation lines are detected by the nondegenerate pairing
\[
(\lambda,f)\mapsto(\lambda\wedge f)(R).
\]

Thus any admissible quotient must retain \([R]\) and \(p(P)\). Conversely, the full observable family factors through these two pieces because the bracket component is annihilated by degree-one evaluation. Therefore the factorization through \(\overline J_3\) is unique.

\(\square\)

This corrects the stronger but false statement that the raw \(J_3\) is itself categorically minimal.

The result is meaningful because the carrier is obtained by a canonical algebraic quotient of the relation jet; it does not simply store the already recovered orientation covector.

---

## 7. Full 3-adic reconstruction

The mod-\(9\) result is the first nontrivial finite-level recovery. To reconstruct the full character, consider a compatible filtered relation-jet tower
\[
(J_n)_{n\ge2},
\]
where \(J_n\) retains the filtered relation information required for the crossed-derivation calculation modulo \(3^n\), modulo the already identified projective/gauge ambiguity.

For a candidate
\[
\rho:G\to(\mathbf Z/3^n)^\times,
\]
the crossed-derivation condition
\[
D(gh)=D(g)+\rho(g)D(h)
\]
evaluated on the filtered relation gives a coefficient functional
\[
\mathcal C_n(J_n,\rho).
\]

Define
\[
\Phi_n(J_n)
=
\{\rho:\mathcal C_n(J_n,\rho)=0\}.
\]

For the frozen \(q=3\) relation, the coefficient equations force
\[
\rho_n(x_1)=\rho_n(x_3)=\rho_n(x_4)=1
\]
and
\[
1+2\rho_n(x_2)=0\pmod{3^n}.
\]

Since \(2\) is a unit modulo \(3^n\),
\[
\boxed{
\rho_n(x_2)=(-2)^{-1}=(1-3)^{-1}\pmod{3^n}.
}
\]

Thus
\[
\Phi_n(J_n)=\{\chi_n\}.
\]

The reductions are compatible:
\[
\chi_{n+1}\equiv\chi_n\pmod{3^n}.
\]

Since
\[
\mathbf Z_3^\times
\cong
\varprojlim_n(\mathbf Z/3^n)^\times,
\]
the compatible family determines a unique
\[
\boxed{
\chi:G\to\mathbf Z_3^\times.
}
\]

In particular,
\[
\chi(x_2)
=
-\frac12
=
(1-3)^{-1},
\]
with
\[
\chi(x_2)\equiv4\pmod9,\quad
13\pmod{27},\quad
40\pmod{81},\quad
121\pmod{243},\ldots
\]

### Theorem 7.1 — Finite-level factorization and inverse limit

For the frozen rank-four \(q=3\) Demuškin presentation, a compatible projective filtered relation-jet tower determines uniquely the reductions
\[
\chi_n:G\to(\mathbf Z/3^n)^\times
\]
through the finite-level crossed-derivation coefficient equations, and the compatible family \((\chi_n)_n\) determines the full canonical orientation
\[
\chi:G\to\mathbf Z_3^\times.
\]

The theorem does not assert that the mod-\(9\) jet \(J_3\) alone determines all higher digits.

---

## 8. A sharp impossibility result

The preceding positive theorem requires care about what “finite information” means.

Consider
\[
G_{3^s}
=
\left\langle
x_1,x_2,x_3,x_4
\mid
x_1^{3^s}[x_1,x_2][x_3,x_4]=1
\right\rangle
\]
and \(G_\infty\).

All members have the same quadratic initial relation
\[
R_2=[X_1,X_2]+[X_3,X_4].
\]

Their orientations satisfy
\[
\chi_{3^s}(x_2)=(1-3^s)^{-1},
\qquad
\chi_\infty(x_2)=1.
\]

But the power term
\[
x_1^{3^s}
\]
first appears in Zassenhaus degree \(3^s\).

Fix a degree bound \(d\). Choose \(s\) with
\[
3^s>d.
\]

Then the bounded-degree filtered data cannot see the \(q\)-dependent power term, while the full orientations are different.

If finite coefficient precision modulo \(3^N\) is also imposed, choose
\[
s\ge N.
\]
Then
\[
(1-3^s)^{-1}\equiv1\pmod{3^N},
\]
although the full \(3\)-adic units remain unequal.

### Theorem 8.1 — Finite-information obstruction

There is no universal reconstruction procedure from carriers having both a fixed finite Zassenhaus-degree bound and fixed finite \(3\)-adic coefficient precision that recovers the full orientation throughout the family \(q=3^s\).

This is an information obstruction, not merely the failure of a particular candidate construction.

There is no contradiction with the fixed-\(q=3\) exact result. Exact \(\mathbf Z_3\)-coefficients contain infinitely many \(3\)-adic digits and therefore are not finite-information carriers.

---

## 9. The characteristic-zero boundary

The mod-\(3\) compressed carrier suggests the tempting replacement
\[
L_3^{res}(V)/[V,L_2(V)]
\cong V^{(1)}
\]
with \(\mathbf Z_3\) in place of \(\mathbf F_3\).

This is not legitimate.

Restricted Lie algebras are characteristic-\(p\) structures. There is no automatic “restricted Lie algebra over \(\mathbf Z_3\)” obtained by scalar extension of the characteristic-three quotient.

Consequently, the exact full-\(\chi\) construction must be formulated in the filtered relation/augmentation and coefficient-evaluation framework rather than by formally lifting the restricted-Lie quotient.

An exact evaluation quotient can be defined once the crossed-derivation evaluation family
\[
\mathcal C_n
\]
is independently fixed. But a concrete, non-tautological finite exact analogue of
\[
[(R,p(P))]
\]
has not been obtained.

This is a genuine boundary of the present method, not an omitted calculation.

---

## 10. What the results establish

The results can be summarized as an information hierarchy.

\[
\boxed{
\begin{array}{ccl}
\text{bare quadratic graded relation}
&\Longrightarrow&
\text{orientation information lost}
\\[2mm]
\downarrow && \\
\text{projective degree-(2,3) relation jet}
&\Longrightarrow&
\chi\bmod9
\\[2mm]
\downarrow && \\
\text{coarsest natural quotient }[(R,p(P))]
&\Longrightarrow&
\text{same recovery observables}
\\[2mm]
\downarrow && \\
\text{compatible finite-level filtered tower}
&\Longrightarrow&
\chi\bmod3^n\ \forall n
\\[2mm]
\downarrow && \\
\text{inverse limit}
&\Longrightarrow&
\chi:G\to\mathbf Z_3^\times.
\end{array}
}
\]

The corresponding negative boundary is

\[
\boxed{
\text{bounded degree + finite precision}
\not\Longrightarrow
\text{universal full }3\text{-adic orientation}.
}
\]

This separation is essential. It prevents three distinct claims from being conflated:

1. recovery modulo \(9\);
2. recovery from a full compatible tower;
3. recovery of the full character from one bounded finite-information carrier.

Only the first two are established in the stated frameworks; the third is obstructed in the universal finite-information setting.

---

## 11. Relation to a broader reconstruction principle

The calculations suggest a general pattern for filtered algebraic reconstruction.

Suppose an object \(X\) has a filtered relation
\[
r=r_d+r_{d+1}+\cdots
\]
and an invariant \(I(X)\) that is not determined by the leading graded data \(r_d\).

Instead of immediately increasing the entire graded calculation, one can ask:

1. At what first filtration degree does the hidden parameter enter?
2. Does it enter as a component of the same filtered relation?
3. What observable evaluates that component?
4. Which parts of the higher jet are annihilated by every relevant observable?
5. What is the coarsest quotient preserving all such observables?

In the present case:

\[
r_2=R_2,
\qquad
r_3=P_3,
\]
and the relevant observable is the degree-one crossed-derivation evaluation
\[
f(P_3)+(\lambda\wedge f)(R_2).
\]

The resulting carrier is not the entire degree-three Lie component but its observable quotient
\[
[(R_2,p(P_3))].
\]

This suggests a useful research viewpoint:

> **Filtered invariant recovery can be treated as an observability problem: identify the first relation jet at which the hidden invariant becomes visible, then quotient out the information annihilated by the recovery observables.**

The present paper establishes this principle in a concrete Demuškin setting; its validity in broader classes of filtered objects is a question for subsequent work.

---

## 12. Limitations and open directions

The following stronger statements are deliberately not claimed.

### 12.1 Absolute minimality

There is no theorem here saying that \(\overline J_3\) is the smallest possible carrier among all conceivable constructions. Such a statement requires an independently justified larger category of carriers.

What is proved is the coarsest-quotient property inside the natural category of degree-\((2,3)\) relation-jet quotients preserving the full degree-one evaluation family.

### 12.2 Universal exact finite compression

The fixed \(q=3\) exact relation/evaluation data determines the full character, but a concrete finite characteristic-zero carrier analogous to \(\overline J_3\) has not been identified.

### 12.3 Higher rank and general \(q\)

The present proofs are for the frozen rank-four \(q=3\) normal form and the comparison family \(q=3^s\). A general theorem for arbitrary rank and arbitrary \(q\) remains open.

### 12.4 Other filtrations

The argument is tied to the Zassenhaus/restricted-power filtration structure used here. Whether analogous first-informative jets exist for other filtrations is open.

---

## 13. Conclusion

The main result is not that a single small graded object magically contains the full \(3\)-adic orientation.

Rather, the analysis identifies exactly where orientation information is lost and what filtered relation information restores it.

For the rank-four Demuškin pro-\(3\) group:

\[
\boxed{
\text{quadratic graded data}
\;\text{is insufficient;}
}
\]

\[
\boxed{
\text{the projective degree-(2,3) relation jet recovers }\chi\bmod9;
}
\]

\[
\boxed{
\text{a compatible filtered relation-jet tower recovers the full }\chi;
}
\]

and

\[
\boxed{
\text{no universal bounded-degree finite-information carrier can recover the full character.}
}
\]

The associated categorical result is that the raw degree-\((2,3)\) jet contains removable information: after quotienting the degree-three layer by the bracket subspace invisible to degree-one evaluation, one obtains the coarsest natural carrier
\[
\boxed{\overline J_3=[(R,p(P))]}.
\]

The broader methodological message is therefore a precise one:

\[
\boxed{
\text{When graded data loses an invariant, inspect the first filtered relation jet that couples to the hidden parameter.}
}
\]

In this model that principle turns an apparently invisible \(3\)-adic orientation into an explicitly recoverable observable, while also identifying the information-theoretic boundary beyond which bounded finite data cannot suffice.

---

## Appendix A. Core formulas

### A.1 Relation

\[
r=x_1^3[x_1,x_2][x_3,x_4].
\]

### A.2 Quadratic component

\[
R_2=[X_1,X_2]+[X_3,X_4].
\]

### A.3 Degree-three component

\[
P_3=X_1^{[3]}.
\]

### A.4 Recovery functional

\[
\Theta_J(\lambda)(f)
=
f(P_3)+(\lambda\wedge f)(R_2).
\]

### A.5 Coordinate form

\[
\Theta_J(\lambda)(f)
=
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]

### A.6 Recovered mod-\(9\) orientation

\[
\lambda_\chi=e_2^*,
\qquad
\chi\equiv(1,4,1,1)\pmod9.
\]

### A.7 Gauge

\[
(R,P)\mapsto(uR,uP+[v,R]).
\]

### A.8 Coarsest carrier

\[
\overline J_3=[(R,p(P))].
\]

### A.9 Finite-level equation

\[
1+2\rho_n(x_2)=0\pmod{3^n}.
\]

### A.10 Full orientation

\[
\chi(x_2)=(1-3)^{-1},
\qquad
\chi(x_i)=1\quad(i\ne2).
\]

---

## Appendix B. Status ledger for the manuscript

| Claim / branch | Status |
|---|---|
| Bare quadratic graded data recovers \(\chi\bmod9\) | **FAIL / CLOSED** |
| Projective degree-\((2,3)\) jet recovers \(\chi\bmod9\) | **PASS / CLOSED** |
| Presentation/lift/gauge invariance of recovery zero set | **PASS**, under stated standard hypotheses |
| Raw \(J_3\) absolutely minimal | **FAIL / CLOSED** in the natural quotient category |
| \(\overline J_3=[(R,p(P))]\) coarsest natural quotient | **PASS / CLOSED** |
| Compatible finite-level tower recovers full \(\chi\) | **PASS / CLOSED** |
| Fixed \(q=3\), exact \(\mathbf Z_3\) relation/evaluation data recovers full \(\chi\) | **PASS / CLOSED** |
| Universal bounded-degree + finite-precision full-\(\chi\) carrier | **FAIL / CLOSED** |
| Naive \(\mathbf Z_3\) restricted-Lie scalar extension | **FAIL / CLOSED** |
| Concrete non-tautological finite exact compression analogous to \(\overline J_3\) | **OPEN / NOT PROVED** |
| General rank / general \(q\) theorem | **OPEN** |
| Other filtrations | **OPEN** |
