# E1 RESIDUAL-GAUGE RE-AUDIT — CRITICAL CORRECTION — 2026-09-19

## Finding

The apparent closure of the degree-(2,3) residual-gauge lemma is **not valid as written**. The previous argument correctly controls the degree-2 correction \(Q_i=c_iR_2\), but it contains a gap in the treatment of the degree-3 restricted-power component \(P_3\).

The sentence “replacing a degree-1 variable by a degree-2 correction inside a degree-3 expression raises degree to at least 4” is valid for an ordinary homogeneous Lie monomial, but it is **not automatically valid for a restricted cubic / group-cube contribution**. In characteristic 3, the restricted cube of a sum has cross terms, and when one summand has filtered degree 1 and the other degree 2, those cross terms can occur already in filtered degree 3.

Thus from
\[
\alpha(X_i)=X_i+c_iR_2+O(3)
\]
one cannot yet conclude that \(P_3\) is unchanged modulo \([V,R_2]\). One must explicitly compute the degree-3 cross-term of the restricted cube and prove that its total contribution is in \([V,R_2]\) (or otherwise characterize the extra gauge and show that \(\Theta\) annihilates it).

## Consequence

The correct status is reverted to:

- degree-2 correction line \(Q_i\in\langle R_2\rangle\): **PASS**;
- induced change of \(R_2\) is a bracket gauge \([v,R_2]\): **PASS**;
- induced change of \(P_3\) has no extra degree-3 term: **OPEN**;
- projective degree-(2,3) cover-change naturality: **OPEN**;
- twisted mod-9 recovery in a frozen presentation: **PASS / CLOSED**;
- coarsest carrier statements conditional on naturality: **CONDITIONAL**;
- full tower result: must not be used to retroactively certify mod-9 presentation independence unless each finite-level naturality gate is separately closed.

## Exact next calculation

For the identity-on-G lift with
\[
Q_i=c_iR_2,
\]
compute the degree-3 part of
\[
(X_i+Q_i)^{[3]}-X_i^{[3]}
\]
using the fixed Magnus/Zassenhaus convention, then sum over the actual degree-3 restricted-power contribution of the relator. The target is an explicit identity of the form
\[
\Delta P_3=[v,R_2]
\quad\text{or, more generally,}\quad
\Delta P_3=[v,R_2]+E,
\]
where \(E\) must be tested directly against every degree-one evaluation \(f\) entering \(\Theta\).

No finite scan is authorized. This is now the highest-priority mod-9 proof obligation before any claim of intrinsic carrier closure.

## Literature caution

The literature confirms the one-relator/minimal-presentation and relation-module framework, but it does not by itself supply this exact degree-3 restricted-power calculation. In particular, one-relator pro-p relation modules are structurally well controlled, while the present residual-gauge identity remains a project-specific filtered calculation.
