# PAPER 3 — CARRIER MINIMALITY: CORRECTED LINEAR-QUOTIENT REDUCTION — 2026-09-28

## Status

Carrier minimality has been reduced to an exact kernel-avoidance problem. A second distinction is now locked: a one-dimensional **global** shadow exists, but it is not an intrinsic finite-pair carrier.

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
be the set of all finite obstruction classes produced by false first-order lifts and their witnesses.

D2 proves
\[
\boxed{\mathscr F_k\ne\varnothing}
\]
and every false candidate has at least one nonzero obstruction in this set.

Let
\[
\mathscr S_k=\operatorname{span}(\mathscr F_k).
\]

## 2. Exact criterion for a linear quotient carrier

Take a quotient carrier
\[
\pi:\mathcal O_k\twoheadrightarrow C.
\]

It detects every false candidate exactly when, for every false candidate \rho, at least one of its obstruction witnesses remains nonzero:
\[
\boxed{
\forall \rho\ne\chi_k,\quad
\exists f\quad
\pi([\delta_{k,\rho}(f)])\ne0.
}
\]

Equivalently, the kernel must avoid the obstruction set attached to every false candidate.

This is weaker than
\[
\ker\pi\cap\mathscr S_k=\{0\}.
\]

The latter is sufficient, but generally not necessary.

### Concrete warning

Over \(\mathbf F_3\), the set
\[
\{e_1,e_2,e_1+e_2\}
\]
spans a 2-dimensional space, yet the 1-dimensional functional
\[
(x,y)\mapsto x+y
\]
is nonzero on all three vectors. Therefore “minimum recognition-carrier dimension = span dimension” is false in general.

The previous version of this file made exactly that overstrong inference and is superseded.

## 3. Exact recognition-minimality problem

The unrestricted linear quotient problem is the finite subspace-avoidance problem
\[
\boxed{
\min_{\pi:\mathcal O_k\twoheadrightarrow C}
\dim C
}
\]
subject to
\[
\forall \rho\ne\chi_k,\quad
\exists f:\pi([\delta_{k,\rho}(f)])\ne0.
\]

Equivalently, for a kernel K\le\mathcal O_k,
\[
K\cap\mathscr F_\rho=\varnothing
\]
for every false candidate's obstruction set \mathscr F_\rho, and
\[
\dim C=\dim\mathcal O_k-\dim K.
\]

This is exact.

## 4. The global-shadow theorem

There is nevertheless a canonical one-dimensional detector **after global inflation is allowed**.

Because
\[
\operatorname{im}(\operatorname{tra}_k)
\]
dies already in H^2(E_k) and hence in H^2(G), global inflation factors through the quotient:
\[
\lambda_k:\mathcal O_k\longrightarrow H^2(G,\mathbf F_p).
\]

D2 proves that every false-lift obstruction class has nonzero image:
\[
\boxed{
o\in\mathscr F_k\implies \lambda_k(o)\ne0.
}
\]

For a Demushkin group,
\[
\dim_{\mathbf F_p}H^2(G,\mathbf F_p)=1.
\]
Therefore the global shadow \lambda_k detects every false obstruction.

Hence, in a category that is allowed to use the global inflation map,
\[
\boxed{\text{a 1-dimensional carrier is sufficient.}}
\]

This is not the desired intrinsic finite-data result, because \lambda_k is defined using the map to the full group G. It is precisely the information the finite carrier problem is trying not to import.

This distinction is important:

- **global category:** 1-dimensional recognition is already available;
- **finite-pair intrinsic category:** whether \lambda_k can be reconstructed from E_k\to Q_k is OPEN.

Thus “\mathcal O_k is minimal” cannot be true in an unrestricted category.

## 5. What the finite-pair problem really asks

The relevant category must forbid importing the global map
\[
H^2(Q_k)\to H^2(G).
\]

A natural category is:
\[
\mathcal C_k^{\mathrm{fin}}
=
\{\text{finite }\mathbf F_p\text{-linear carriers constructed functorially from }E_k\to Q_k\}.
\]

The actual question becomes:

\[
\boxed{
\text{Can the global-shadow functional }\lambda_k
\text{ be reconstructed from the finite pair }E_k\to Q_k?
}
\]

If yes, a 1-dimensional finite carrier would suffice.

If no, then the finite-pair carrier necessarily retains additional information, and the minimality problem becomes genuinely nontrivial.

## 6. Relation to the 45-dimensional calculation

The old rank-4, p=3 calculation
\[
\dim(P_4/P_5)=45,\qquad
\ker(H^2(W_4)\to H^2(W_5))\cong Q_4^*
\]
is not needed for the global-shadow theorem and not needed for D2/D3.

It becomes relevant only to the finite-pair question:
whether the non-global directions in \mathcal O_2 can be removed functorially while preserving detection of all false candidates.

So the previous decision remains:

\[
\boxed{\text{do not restart the 45-dimensional computation yet.}}
\]

## 7. Classification

- corrected recognition-minimality formulation: **PASS / CLOSED**;
- D2 nonempty false-obstruction set: **PASS / CLOSED**;
- global 1-dimensional detector: **PASS / CLOSED**;
- finite-pair reconstruction of the global shadow: **OPEN / LOAD-BEARING**;
- \mathcal O_k minimality in an unrestricted category: **FAIL / CLOSED — too strong a question**;
- \mathcal O_k minimality in the finite-pair functorial category: **OPEN**;
- 45-dimensional computation as current recognition input: **NOT REQUIRED**;
- 45-dimensional computation as later finite-pair minimality input: **DEFERRED / CONDITIONAL**.

## Next target

The sharp next test is now:

\[
\boxed{
\text{Is }\lambda_k:\mathcal O_k\to H^2(G,\mathbf F_p)
\text{ recoverable from the finite pair }E_k\to Q_k?
}
\]

If it is, the carrier problem collapses to a one-dimensional intrinsic selector. If it is not, that failure itself identifies exactly what extra finite filtered relation information must be retained.
