# PAPER 3 — CARRIER MINIMALITY: SPAN REDUCTION THEOREM — 2026-09-28

## Status

**Carrier minimality is now reduced to a precise finite linear-algebra problem in the quotient-carrier category.**

This does not yet prove that the transgression quotient \(\mathcal O_k\) is minimal or universal. It identifies exactly what must be computed to prove such a statement.

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

The corrected D2 theorem gives, for every false first-order lift
\[
\rho_k=\chi_k(1+p^{k-1}\nu),\qquad \nu\ne0,
\]
at least one finite obstruction class
\[
o(\nu,f)\in\mathcal O_k
\]
that is nonzero.

Let
\[
\mathscr S_k
=
\operatorname{span}_{\mathbf F_p}
\{\,o(\nu,f):
\nu\ne0,\ f\text{ is an admissible witness for }\nu\,\}
\subseteq\mathcal O_k.
\]

More invariantly, take the span of the images in \(\mathcal O_k\) of all finite connecting outputs arising from all false candidates.

Then
\[
\mathscr S_k\ne0
\]
by D2.

## 2. Linear quotient-carrier theorem

Restrict first to the category of finite-dimensional \(\mathbf F_p\)-linear quotient carriers:
\[
\pi:\mathcal O_k\twoheadrightarrow C,
\]
with recognition performed by the induced obstruction map.

A carrier C detects every false lift iff
\[
\ker(\pi)\cap\mathscr S_k=\{0\}.
\]

### Proof

If a nonzero
\[
s\in\ker(\pi)\cap\mathscr S_k
\]
is represented by a linear combination of false-lift outputs, the quotient has lost a direction that is load-bearing for the obstruction span. Conversely, if the kernel has zero intersection with \(\mathscr S_k\), every nonzero obstruction direction remains nonzero after projection.

The linear-algebra consequence is
\[
\boxed{\dim C\ge \dim\mathscr S_k.}
\]

Conversely, after choosing a complement
\[
\mathcal O_k=\mathscr S_k\oplus U,
\]
the projection
\[
\mathcal O_k\to\mathscr S_k
\]
is a quotient-carrier of dimension \(\dim\mathscr S_k\) that detects every false obstruction.

Therefore, in the unrestricted linear quotient category,
\[
\boxed{
\min\dim C=\dim\mathscr S_k.
}
\]

This is an exact reduction, not a heuristic.

## 3. What this says about \(\mathcal O_k\)

The transgression quotient is minimal in the linear quotient category iff
\[
\boxed{\mathscr S_k=\mathcal O_k.}
\]

So the old vague question “is \(\mathcal O_k\) minimal?” has been replaced by the concrete spanning question:

\[
\boxed{
\text{Do all of }\mathcal O_k
\text{ arise, linearly, from false-lift obstruction outputs?}
}
\]

If yes, \(\mathcal O_k\) is dimension-minimal among all linear quotient carriers.

If
\[
0<\dim\mathscr S_k<\dim\mathcal O_k,
\]
then \(\mathcal O_k\) contains recognition-inert directions and is not dimension-minimal in that category.

## 4. Immediate lower bound

D2 already proves
\[
\dim\mathscr S_k\ge1.
\]

The global Demuškin pairing alone does **not** determine \(\dim\mathscr S_k\). Globally,
\[
H^2(G,\mathbf F_p)
\]
is one-dimensional, so all separating outputs have the same nonzero global image up to scalar. Distinct finite obstruction directions can therefore differ only by finite information invisible after global inflation.

Hence one cannot infer
\[
\mathscr S_k=\mathcal O_k
\]
from PD^2 nondegeneracy alone.

This is the exact point at which a genuine finite-carrier computation or representation-theoretic argument would become necessary.

## 5. Functorial category remains separate

The projection onto a chosen complement \(\mathscr S_k\) is generally noncanonical. Therefore the preceding theorem does **not** prove functorial minimality.

For the stronger category
\[
\mathcal C_k^{\mathrm{fun}}
=
\{\text{finite }\mathbf F_p\text{-linear carriers functorially attached to }E_k\to Q_k\},
\]
the remaining target is a universal property of \(\mathcal O_k\), for example:

> Every admissible functorial separating carrier receives a canonical factorization from \(\mathcal O_k\), or from a canonical quotient of \(\mathcal O_k\).

That remains **OPEN**.

## 6. 45-dimensional calculation: exact role

The old rank-4, p=3 calculation
\[
\dim(P_4/P_5)=45,\qquad
\ker(H^2(W_4)\to H^2(W_5))\cong Q_4^*
\]
is not required for the definition of \(\mathscr S_2\).

It becomes relevant only if we attempt to compute
\[
\dim\mathscr S_2
\]
or its \(Sp_4(\mathbf F_3)\)-module structure.

Therefore the correct research order is:

\[
\boxed{
\text{define }\mathscr S_k
\to
\text{prove functorial properties}
\to
\text{only then compute its dimension/module structure if needed}.
}
\]

This preserves the previous decision not to restart the 45-dimensional computation prematurely.

## 7. Classification

- exact linear-quotient reduction: **PASS / CLOSED**;
- \(\mathscr S_k\ne0\): **PASS / CLOSED** by D2;
- \(\min\dim C=\dim\mathscr S_k\) in unrestricted linear quotient category: **PASS / CLOSED**;
- \(\mathcal O_k\) minimality: **OPEN**, equivalent to \(\mathscr S_k=\mathcal O_k\);
- functorial universal minimality: **OPEN**;
- 45-dimensional computation as a recognition input: **NOT REQUIRED**;
- 45-dimensional computation as a possible minimality/module input: **DEFERRED / CONDITIONAL**.

## Next target

The next mathematically sharp question is not “calculate 45 again.” It is:

\[
\boxed{
\text{Can }\mathscr S_k\text{ be characterized intrinsically, or bounded below, without coordinates?}
}
\]

A particularly useful first test is whether the functorial span of false-lift outputs is forced to contain a canonical submodule of \(\mathcal O_k\). Only after that should a concrete rank-4 module calculation be reopened.
