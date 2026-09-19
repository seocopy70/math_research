# E1 RELATION-MODULE STRUCTURAL LEMMA — 2026-09-19

## Objective

Test the candidate relation-module container
\[
\mathcal R_F=R/[F,R]
\]
more rigorously before attempting the degree-(2,3) jet.

No finite scan was used or authorized.

## 1. What is actually canonical

Start with a minimal free pro-3 presentation
\[
1\to R\to F\xrightarrow{\pi}G\to1,
\qquad F\cong F_4.
\]

The quotient \(R/[F,R]\) is the coinvariant relation module for the chosen free cover. It kills the relator-conjugation ambiguity found in E1:
\[
uru^{-1}\equiv r\pmod{[F,R]}.
\]

Thus the passage from a chosen relator to its class in \(R/[F,R]\) is strictly stronger than the earlier projective-jet quotient.

## 2. Five-term control

For the extension above, the continuous homology five-term sequence contains
\[
H_2(G,\mathbf Z_3)\longrightarrow
R/[F,R]\longrightarrow
F_{ab}\longrightarrow
G_{ab}\longrightarrow0.
\]

Minimality means
\[
F_{ab}\xrightarrow{\sim}G_{ab},
\]
so the transgression map
\[
R/[F,R]\to F_{ab}
\]
is zero.

This proves an important structural point: the relation-module class is not being selected by its image in degree one; its degree-(2,3) information has to be extracted from the filtered free cover.

**Do not identify \(R/[F,R]\) with \(H_2(G,\mathbf Z_3)\) solely from the five-term sequence.** The sequence only gives the injection of the homological term into the relation module when the degree-one map is an isomorphism.

## 3. Consequence for the jet problem

The candidate map
\[
\operatorname{Jet}_{2,3}(\mathcal R_F)
\longrightarrow L_2(F)\oplus L_3^{res}(F)
\]
cannot be declared canonical merely because \(R/[F,R]\) is a natural quotient for a fixed cover.

There are two distinct invariance problems:

1. **Internal relation-module gauge:** handled by passing from \(R\) to \(R/[F,R]\).
2. **Change of minimal free cover:** an isomorphism
\[
F\to F'
\]
lifting \(\mathrm{id}_G\) must induce a filtered identification of the relevant degree-(2,3) jet.

The second statement is not automatic and is the real E1 obstruction.

## 4. What can be proved immediately

For a fixed minimal free cover, the following is now legitimate:

- the defining relator determines a class in \(R/[F,R]\);
- all conjugate choices of that relator give the same class;
- any proposed degree-(2,3) extraction must be defined from this class together with the Zassenhaus filtration;
- the resulting object must then be tested under a change of minimal free cover.

No claim is made that \(R/[F,R]\), or its filtered jet, is already an invariant of the abstract group.

## 5. New sharper E1 gate

The next proof target is now precise:

> **Cover-change lemma:** given two minimal free pro-3 presentations of the same \(G\), determine whether the defining relation-module classes and their degree-(2,3) filtered jets are canonically identified, at least up to the gauge that leaves \(\Theta\) unchanged.

If the answer is yes, E1 can be upgraded from a candidate container to an intrinsic relation-jet object. If not, the replacement must be a presentation-free extension/transgression invariant.

## Status

- E1-local conjugation gauge: **PASS**.
- \(R/[F,R]\) as fixed-cover relation-module container: **PASS / structurally justified**.
- Identification with \(H_2(G,\mathbf Z_3)\): **NOT CLAIMED**.
- Degree-(2,3) jet extraction: **OPEN**.
- Change of minimal free cover: **OPEN**.
- E1 full intrinsicness: **OPEN**.

No finite scan is authorized.
