# PAPER 3 — CARRIER MINIMALITY: CORRECTED LINEAR-QUOTIENT REDUCTION — 2026-09-28

## Status

A first carrier-minimality reduction was critically rechecked. The earlier claim that the minimum carrier dimension equals the dimension of the span of all false-lift outputs was **too strong**: recognition only needs to preserve each actual false obstruction, not every linear combination of false obstructions.

The corrected result is an exact kernel-avoidance formulation.

## 1. Fixed finite carrier

For
\[
Q_k=G/D_{p^{k-1}+1},\qquad
E_k=G/D_{p^{k-1}+2},
\]
define
\[
\mathcal O_k
=
H^2(Q_k,\mathbf F_p)/\operatorname{im}(\operatorname{tra}_k).
\]

Let
\[
\mathscr F_k\subset\mathcal O_k\setminus\{0\}
\]
be the set of all finite obstruction classes produced by false first-order lifts and their witnesses:
\[
\mathscr F_k
=
\{\, [\delta_{k,\rho}(f)]:
\rho\ne\chi_k,\ f\text{ a witness}\,\}.
\]

D2 proves
\[
\boxed{\mathscr F_k\ne\varnothing}
\]
and, more strongly, every false candidate has at least one nonzero element of \mathscr F_k associated with it.

Let
\[
\mathscr S_k=\operatorname{span}(\mathscr F_k).
\]

## 2. Exact criterion for a linear quotient carrier

Take a linear quotient carrier
\[
\pi:\mathcal O_k\twoheadrightarrow C.
\]

The carrier detects every false candidate exactly when, for every false candidate \rho, at least one of its obstruction witnesses remains nonzero:
\[
\boxed{
\forall \rho\ne\chi_k,\quad
\exists f\quad
\pi([\delta_{k,\rho}(f)])\ne0.
}
\]

Equivalently,
\[
\ker\pi
\]
must avoid the obstruction set belonging to each false candidate.

This is weaker than
\[
\ker\pi\cap\mathscr S_k=\{0\}.
\]

The latter is a sufficient condition, but in general is not necessary, because a nonzero linear combination of individually detectable obstruction classes may lie in the kernel without causing any actual false candidate to become undetectable.

### Concrete warning

Over \(\mathbf F_3\), a set such as
\[
\{e_1,e_2,e_1+e_2\}
\]
spans a 2-dimensional space, yet the 1-dimensional functional
\[
(x,y)\mapsto x+y
\]
is nonzero on all three listed vectors. Thus “carrier dimension = span dimension” is not a valid recognition theorem.

This correction is now authoritative.

## 3. Correct minimality invariant

The unrestricted linear-quotient problem is therefore:

\[
\boxed{
\min_{\pi:\mathcal O_k\twoheadrightarrow C}
\dim C
\quad\text{subject to}\quad
\ker\pi\cap\mathscr F_\rho=\varnothing
\text{ for every false candidate }\rho,
}
\]
where \(\mathscr F_\rho\) is the set of obstruction outputs available for that candidate.

Equivalently, if \(K\le\mathcal O_k\) is the kernel of a quotient, then
\[
K\cap\mathscr F_\rho=\varnothing
\quad\text{for every false }\rho,
\]
and
\[
\dim C=\dim\mathcal O_k-\dim K.
\]

So the problem is a finite linear-algebraic **subspace-avoidance problem**, not a span-dimension problem.

## 4. What the span still tells us

The span
\[
\mathscr S_k=\operatorname{span}(\mathscr F_k)
\]
remains useful.

If one imposes the stronger carrier requirement that **every nonzero vector of \mathscr S_k** must remain detectable, then
\[
\ker\pi\cap\mathscr S_k=\{0\}
\]
is necessary and sufficient, and hence
\[
\dim C\ge\dim\mathscr S_k.
\]

Thus
\[
\dim\mathscr S_k
\]
is an exact minimum only for the stronger “detect every nonzero vector in the obstruction span” category, not automatically for the original recognition problem.

D2 still gives
\[
\mathscr S_k\ne0.
\]

## 5. Consequences for \mathcal O_k

The correct questions are now:

### Recognition-minimality
Does there exist a proper quotient
\[
\mathcal O_k\twoheadrightarrow C
\]
whose kernel avoids every actual false-candidate obstruction set?

### Span-complete minimality
Is
\[
\mathscr S_k=\mathcal O_k?
\]
If so, \mathcal O_k is minimal in the stronger span-complete category.

### Functorial minimality
Is there a canonical quotient of \mathcal O_k that is minimal and functorial under isomorphisms of the finite filtered pair
\[
E_k\to Q_k?
\]

The first is the true recognition problem; the second is a useful stronger problem; the third is the strongest categorical target.

All three remain OPEN.

## 6. 45-dimensional calculation: exact role

The old rank-4, p=3 calculation
\[
\dim(P_4/P_5)=45,\qquad
\ker(H^2(W_4)\to H^2(W_5))\cong Q_4^*
\]
is not required for the corrected D2 theorem.

It becomes relevant only if we try to determine:
- the actual obstruction set \mathscr F_2;
- its span or module structure;
- or the existence of a proper functorial quotient of \mathcal O_2.

Therefore the previous decision stands:

\[
\boxed{
\text{do not restart the 45-dimensional computation yet.}
}
\]

First identify the intrinsic structure of the obstruction set and its functorial symmetries.

## 7. Classification

- corrected recognition-carrier formulation: **PASS / CLOSED**;
- D2 nonempty false-obstruction set: **PASS / CLOSED**;
- exact minimal dimension in unrestricted quotient category: **OPEN**;
- span-complete lower bound: **PASS / CLOSED as a conditional statement**;
- \mathcal O_k minimality: **OPEN**;
- functorial universal minimality: **OPEN**;
- 45-dimensional computation as current recognition input: **NOT REQUIRED**;
- 45-dimensional computation as later minimality/module input: **DEFERRED / CONDITIONAL**.

## Next target

The sharp next question is:

\[
\boxed{
\text{What is the intrinsic/functorial structure of the false-obstruction set }\mathscr F_k?
}
\]

In particular, determine whether automorphisms of the finite filtered pair force \mathscr F_k to contain sufficiently many directions that every proper functorial quotient kills some false candidate.

Only after this symmetry/obstruction-set analysis should a concrete rank-4 module calculation be reopened.
