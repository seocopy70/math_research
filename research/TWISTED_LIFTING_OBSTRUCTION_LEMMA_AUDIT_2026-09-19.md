# TWISTED LIFTING OBSTRUCTION LEMMA — STRUCTURAL AUDIT / 2026-09-19

## Purpose

This document records the corrected status of the twisted mod-9 branch and pushes the next authorized theorem-level target: an abstract lifting-obstruction lemma for minimal one-relator pro-3 presentations.

It supersedes the overly strong wording in the earlier twisted-recovery audit whenever that wording treated a frozen-coordinate identity as a fully established natural factorization.

## 1. Status correction

The following distinctions are now frozen.

- Direct twisted-surjectivity recovery of the frozen q=3 character modulo 9: **PASS / CLOSED**.
- Exact equality, in the frozen coordinate model, between the twisted obstruction and
  \[
  \Theta_{(R,p)}(\lambda)(f)=f(p)+(\lambda\wedge f)(R):
  \]
  **PASS / CLOSED**.
- Projective/gauge compatibility at the already established degree-(2,3) carrier level: **CONDITIONAL PASS** until the presentation-change action on the twisted cocycle data is formulated abstractly.
- A natural intrinsic factorization
  \[
  \text{intrinsic carrier}\to\text{twisted-surjectivity criterion}
  \]
  for arbitrary minimal one-relator pro-3 presentations: **OPEN**.
- Recovery from the bare Zassenhaus restricted graded object: **OPEN / NOT ESTABLISHED**.
- Higher 3-adic digits: **OPEN / separate program**.

In particular, the earlier statement “factorization through the projective carrier: PASS/CLOSED” is to be read only in the frozen-coordinate/projective model, not as a completed naturality theorem.

## 2. Structural setting

Let
\[
G=F/\overline{\langle r\rangle}
\]
be a minimal one-relator pro-3 presentation with
\[
V=H^1(G,\mathbf F_3)^*.
\]
Assume the standard one-relator transgression identification and write the relation jet through degree 3 as
\[
r=(R,P)+O(4),
\qquad
R\in L_2(V),\quad P\in L^{res}_3(V).
\]
Let
\[
p(P)\in V^{(1)}
\]
denote the restricted-cubic/power projection.

For a rank-one character
\[
\rho:G\to1+3\mathbf F_3\subset(\mathbf Z/9)^\times,
\qquad
\rho(x_i)=1+3a_i,
\]
write \(\lambda=\sum a_i e_i^*\).

Let
\[
A_2=\mathbf Z/9
\]
with G-action through \(\rho\), and let \(A_1=\mathbf F_3\) be the trivial module obtained by reduction.

The reduction map
\[
A_2\twoheadrightarrow A_1
\]
is G-equivariant because \(\rho(g)\equiv1\pmod3\).

## 3. Cohomological lifting statement to prove

For a class \([f]\in H^1(G,A_1)\), lifting it to \(H^1(G,A_2)\) is equivalent to choosing a crossed homomorphism \(z:F\to A_2\) whose reduction is \(f\) and whose relator obstruction vanishes.

Because the mod-3 action is trivial,
\[
H^1(G,A_1)\cong V^*
\]
via generator values. There are no nonzero principal derivations in the trivial coefficient module.

The remaining issue is the twisted coefficient module: principal derivations in \(A_2\) need not vanish. Therefore the proof must formulate the obstruction on cohomology classes, not merely on arbitrary generator-value vectors.

A clean route is the standard one-relator five-term/resolution description: the only obstruction to lifting a mod-3 1-cocycle is the image of the relator under a chosen lifted crossed homomorphism, modulo the corresponding coefficient-module coboundary action.

## 4. Degree-(2,3) obstruction calculation

Fix generator values
\[
z(x_i)\equiv f_i\pmod3.
\]
Using
\[
z(uv)=z(u)+\rho(u)z(v)
\]
and the fixed convention
\[
[x,y]=x^{-1}y^{-1}xy,
\]
expand the relator modulo 9 and divide the obstruction by 3.

The degree-2 commutator contribution is bilinear in \((\lambda,f)\), while the degree-3 restricted-power contribution is linear in \(f\). After reduction modulo 3, the obstruction has the coordinate-free form
\[
\boxed{
\operatorname{Obs}_{(R,p)}(\lambda,f)
=
f(p)+(\lambda\wedge f)(R).
}
\]

For the frozen q=3 relation
\[
R=[X_1,X_2]+[X_3,X_4],
\qquad
p=X_1^{(1)},
\]
this becomes
\[
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]

Hence the lifting map is surjective exactly when this functional vanishes for every \(f\), namely
\[
a_1=a_3=a_4=0,
\qquad
a_2=1.
\]
Therefore
\[
\rho(x_1)=\rho(x_3)=\rho(x_4)=1,
\qquad
\rho(x_2)=4\pmod9.
\]

## 5. What remains for the abstract lemma

The calculation above is not yet a complete intrinsic theorem. Four bridges must be made explicit.

### (A) Resolution/obstruction bridge

Prove that, for a minimal one-relator pro-3 presentation, the relator obstruction computed from a lifted crossed homomorphism represents the complete obstruction to lifting a class in
\[
H^1(G,A_1)
\]
to
\[
H^1(G,A_2).
\]

This should be stated using the standard five-term sequence or an explicit two-term beginning of the one-relator resolution. The proof must account for twisted principal derivations.

### (B) Jet truncation bridge

Show that modulo 3, after dividing the relator obstruction by 3, all terms of filtered degree >=4 vanish and the surviving degree-2/degree-3 terms are exactly
\[
(\lambda\wedge f)(R)+f(p(P)).
\]
This is the precise statement that the obstruction factors through the degree-(2,3) relation jet.

### (C) Naturality/gauge bridge

Under a change of minimal generators and relator representative, establish the induced transformation of
\[
(R,p(P),\lambda,f)
\]
and prove that the zero condition
\[
\operatorname{Obs}_{(R,p)}(\lambda,-)=0
\]
is invariant.

In particular, the previously audited degree-3 gauge
\[
(R,P)\mapsto(uR,uP+[v,R])
\]
must be accompanied by the corresponding transformation of the twisted cocycle coordinates. It is not sufficient to note only that degree-one functionals annihilate \([v,R]\).

### (D) Intrinsic orientation characterization

If the twisted-surjectivity criterion is to be called “canonical orientation characterization” in the theorem, the exact external theorem supplying that characterization must be cited and its hypotheses matched to the present pro-3 Demuškin setting.

The frozen computation itself proves uniqueness for the present relation; it does not by itself prove the general characterization.

## 6. Current theorem target

The desired theorem is therefore the following, subject to proving A–D.

> **Twisted degree-(2,3) lifting-obstruction theorem (target).**
> For a minimal one-relator pro-3 presentation satisfying the stated transgression hypotheses, the first twisted lifting obstruction for
> \[
> H^1(G,\mathbf Z/9(\rho))\to H^1(G,\mathbf F_3)
> \]
> depends only on the projective degree-(2,3) relation carrier
> \[
> \overline J_3=[(R,p(P))],
> \]
> through
> \[
> \operatorname{Obs}_{\overline J_3}(\lambda,f)
> =
> f(p(P))+ (\lambda\wedge f)(R),
> \]
> and the vanishing-for-all-f condition is invariant under the allowed presentation/gauge changes.

This theorem would convert the present frozen calculation into a genuine structural factorization result.

## 7. Stop rule

Do not perform another broad computational scan.

The next work is proof-level:

1. prove the one-relator obstruction lemma including twisted coboundaries;
2. prove the degree-(2,3) truncation formula with the exact commutator sign;
3. prove presentation/gauge naturality;
4. check/cite the general Demuškin twisted-surjectivity characterization.

Only after these are closed should the branch be promoted from “frozen-coordinate factorization” to an intrinsic theorem.

## Decision

**Structural lemma: OPEN / authorized next target.**

The previous twisted recovery remains a genuine independent mod-9 calculation. What is not yet closed is the abstract naturality bridge from the intrinsic carrier to that twisted criterion.
