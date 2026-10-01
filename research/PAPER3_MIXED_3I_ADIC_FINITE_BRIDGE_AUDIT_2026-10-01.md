# MIXED (3,I)-ADIC FOX CARRIER — FINITE-LEVEL FACTORIZATION / ORIENTATION-BRIDGE ATTACK — 2026-10-01

## Result

The mixed candidate survives a stronger standard-family attack.

For
\[
r_q=x_1^q[x_1,x_2][x_3,x_4],
\qquad q=3^s \text{ or }q=0,
\]
the projective Fox row has the form
\[
J_1=\sum_{i=0}^{q-1}A^i+A^q(B^{-1}-1),
\]
\[
J_2=A^q(A-1)B^{-1},
\qquad
J_3=A^q(1-D)(CD)^{-1},
\qquad
J_4=A^q(C-1)(CD)^{-1},
\]
with the evident limiting interpretation for q=0.

At the canonical solution,
\[
A=C=D=1,
\qquad
B=(1-q)^{-1}.
\]

The mixed maximal ideal is
\[
\mathfrak m=(3,A-1,B-1,C-1,D-1).
\]

## 1. Finite level needed for mod 3^k

The finite mixed carrier is taken at
\[
\mathcal M_k:=\mathfrak m/\mathfrak m^{k+1}
\]
or equivalently the projective Fox obstruction ideal/scheme over the finite ring
\[
A/\mathfrak m^{k+1}.
\]

The exponent q enters the power term with mixed order
\[
\operatorname{ord}_{\mathfrak m}(3^s(A-1))=s+1.
\]
Hence the first q-layer that affects \(\chi\bmod 3^k\) occurs at mixed order \(k\), while terms for \(v_3(q)\ge k\) disappear beyond the required precision. This is the mixed-filtration analogue of the previously established Zassenhaus threshold, but it is a characteristic-zero filtered statement rather than a Zassenhaus statement.

## 2. Standard-family factorization

For the standard family, the finite mixed jet at level \(k+1\) depends on the power parameter only through the residue information visible modulo \(3^k\). In particular, if
\[
q\equiv q'\pmod{3^k},
\]
then the relevant finite coefficient equations agree to the precision needed for \(\chi\bmod3^k\).

For \(q=3^s\), the mixed order of the leading power contribution is \(s+1\). Thus the cases \(s\ge k\) collapse at the \(k\)-digit target, while \(s<k\) remain visible.

This establishes:

\[
\boxed{
\text{finite mixed Fox factorization: PASS / LOCAL on the standard Demushkin family}
}
\]

It does **not** yet establish a functorial theorem for every admissible finite pair in the project's larger category.

## 3. Direct orientation bridge

The bridge is now genuinely direct at the standard-family level.

From
\[
J_2=0,\quad J_3=0,\quad J_4=0
\]
and the fact that \(A,B,C,D\in1+3\mathbf Z_3\), the finite equations force
\[
A=C=D=1
\]
at the relevant finite precision.

The remaining equation is
\[
q-1+B^{-1}=0
\]
to the corresponding mixed order. Therefore
\[
B=(1-q)^{-1}\pmod{3^k}.
\]

Since B is the coordinate value of the canonical character in the intrinsic Fox character locus, this gives
\[
\boxed{
\mathcal M_k\longrightarrow\chi\pmod{3^k}
}
\]
without inserting \(\chi\) into the carrier definition.

The bridge uses the Fox equation itself, not the two-step route
\[
\mathcal M_k\to q\text{-class}\to\text{known orientation formula}.
\]

That distinction is important for the project's non-tautology gate.

## 4. Why this does not revive the closed degree-3 truncation

The earlier Nielsen attack showed that a fixed ordinary total-degree-3 truncation of the exact Fox row is not presentation invariant.

The present carrier truncates the **intrinsic mixed maximal ideal**
\[
(3,U_1,\ldots,U_d),
\]
not ordinary polynomial degree in a selected coordinate system.

Because admissible free-basis changes preserve this maximal ideal and transform the Fox row projectively by an invertible Jacobian, the finite mixed scheme is not the previously rejected degree-3 object.

## 5. Non-redundancy against C_k

The one-dimensional cup-line \(C_k\) is sufficient for the already-closed finite recognition result, but it does not contain the higher 3-adic digits represented by the mixed Fox equations.

The mixed carrier therefore contains strictly more finite information than \(C_k\) on the standard family.

However, “strictly more information” is not by itself a universal minimality theorem. The project must not repeat the closed \(O_k\) argument.

Current status:

\[
\boxed{
\text{non-redundancy: PASS / LOCAL}
}
\]

## 6. Remaining global gap

The unresolved point is now sharply isolated:

> Does the finite mixed Fox scheme \(\mathcal M_k\) descend functorially from the project's abstract finite-pair category, independently of the standard normal form?

There are two possible outcomes.

### A. Global descent theorem

Prove that the projective mixed Fox construction modulo \(\mathfrak m^{k+1}\) is a functor of the finite filtered pair, with all presentation/gauge choices eliminated.

Then the carrier becomes a genuine new finite-pair carrier and the branch can be promoted toward PASS/CLOSED.

### B. Same-pair counterexample

Find two admissible inputs with isomorphic finite pairs but non-isomorphic mixed finite Fox schemes. Then the mixed branch is immediately **FAIL/CLOSED**.

No broader computation is justified before this dichotomy is settled.

## 7. Literature boundary

The standard background is consistent with this construction: Demushkin groups have a canonical orientation and one-relator minimal presentations; completed Fox calculus gives the relation-module differential; the Zassenhaus filtration is tied specifically to the complete \(\mathbf F_3[[G]]\) augmentation filtration. The mixed \((3,I)\)-adic characteristic-zero truncation is an additional construction and is not supplied as a theorem by these references.

Relevant background: Labute's classification and modern cohomological expositions; Mináč–Pasini–Quadrelli–Tân on complete group algebras/Zassenhaus; completed Fox calculus in the pro-p relation-module setting.

## Decision

- completed projective intrinsicity: **PASS / LOCAL**;
- finite mixed carrier on standard family: **PASS / LOCAL**;
- finite-pair factorization globally: **OPEN / LOAD-BEARING**;
- direct orientation bridge on standard family: **PASS / LOCAL**;
- non-redundancy against C_k: **PASS / LOCAL**;
- universal/global carrier theorem: **OPEN**.

The next authorized attack is the global finite-pair descent theorem versus same-pair counterexample. No new Bockstein scan, ordinary degree-3 Fox scan, or O_k scan is authorized.
