# E1 RELATION-MODULE CANDIDATE — 2026-09-19

## Objective

Replace the incomplete projective-jet quotient by a canonical object that automatically kills relator conjugation and other relation-kernel gauge changes.

No finite scan was used or authorized.

## 1. Candidate canonical container

For a minimal free pro-3 presentation
\[
1\to R\to F\to G\to1,
\]
the natural relation-module candidate is
\[
\mathcal R_F:=R/[F,R].
\]

The key advantage over a chosen relator is immediate: replacing a defining relator by a conjugate changes it by an element of \([F,R]\), so its class in \(\mathcal R_F\) is unchanged.

For a one-relator Demushkin presentation, the class of the defining relator therefore has a canonical home relative to the chosen free cover, before taking its filtered degree-(2,3) image.

## 2. Filtered jet candidate

Equip \(F\) with the fixed Zassenhaus filtration and \(R\) with the induced filtration. The next object to define is the degree-(2,3) image of the relator class in \(\mathcal R_F\), schematically
\[
\operatorname{Jet}_{2,3}(\mathcal R_F)
\longrightarrow L_2(F)\oplus L_3^{res}(F).
\]

The desired output should be the class represented by
\[
(R,P),
\]
but now modulo all changes already killed in \(R/[F,R]\), not merely modulo common scaling and the visible conjugation gauge \([V,R]\).

This is a candidate construction only. The map and its presentation-independence still require proof.

## 3. Why this is the correct direction

The previous E1 audit found
\[
P\mapsto P+[v,R]
\]
under relator conjugation. The quotient \(R/[F,R]\) kills exactly this source of ambiguity before passing to the associated filtered jet.

This matches the standard relation-module framework used in filtered one-relator/mild pro-p theory: initial forms of relators generate the graded relation ideal, while relation modules package dependence on defining relations. Labute-type mild-presentation results use relation modules of the form \(r/[r,r]\) for the graded ideal; the group-level analogue \(R/[F,R]\) is the natural object to test here. External literature confirms this relation-module framework, but does not by itself prove the present degree-(2,3) intrinsic jet statement.

## 4. Critical caveat

\[
R/[F,R]
\]
is canonical only relative to a chosen free presentation/cover. It is therefore NOT yet legitimate to call the resulting degree-(2,3) jet an invariant of the abstract group.

The remaining question is whether minimal free presentations of the same G induce canonically isomorphic filtered relation modules, or whether the correct invariant must instead be formulated in terms of a universal/free-cover category.

Thus:

\[
\boxed{\text{E1 candidate: relation-module formulation}}
\]

but NOT yet

\[
\boxed{\text{E1 full intrinsicness: PASS}}.
\]

## 5. Current gate status

- E1-local relator-gauge compatibility: PASS.
- Relation-module container \(R/[F,R]\): structurally well-motivated candidate.
- Degree-(2,3) jet map: OPEN.
- Independence under change of minimal free presentation: OPEN.
- E2/E3: not yet authorized as closed.

The next task is to determine whether the filtered degree-(2,3) class of the canonical relation-module element is presentation-independent, or whether a presentation-free extension invariant is required.

No finite scan is authorized.
