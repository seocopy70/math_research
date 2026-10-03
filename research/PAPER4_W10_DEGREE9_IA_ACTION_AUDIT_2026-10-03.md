# PAPER 4 — W10 DEGREE-9 IA ACTION AUDIT — 2026-10-03

## Target

Final bounded Gate-B calculation for
\[
(p,s,a,n)=(3,2,1,10),\qquad
G=\langle z,x,y\mid z^9=x^3[x,y]\rangle,
\qquad W_{10}=G/D_{10}(G),
\]
with
\[
Q_{10}=D/D_{10}(D).
\]

The load-bearing family is
\[
\pi_c(z)=c,\qquad \pi_c(x)=x,\qquad \pi_c(y)=y,
\qquad c\in D_2(Q_{10}).
\]

The question is whether the radical-preserving IA shear can move the canonical quotient
\(\pi_1\) to \(\pi_c\) without changing the critical degree-9 obstruction.

## Pre-check

- **Object:** the relation-aware truncated Magnus algebra through degree 9, together with the finite group relation defining \(W_{10}\).
- **Input:** only the critical finite presentation and a radical correction \(c\in D_2\); no inserted value of \(q\) beyond the fixed minimal test \(p=3\).
- **Functoriality:** the proposed shear is a filtered IA automorphism of the finite presentation if and only if it preserves the defining relator modulo \(D_{10}\).
- **Gauge:** changing the radical lift by \(D_2\) is precisely the gauge/IA move being tested.
- **Orientation bridge:** the degree-9 relation is the first critical carrier for the relative extension defect.
- **q-blindness:** the calculation itself uses only the filtered degree and characteristic 3.
- **Separation:** a change in the degree-9 class would give a negative orbit test; preservation gives the positive direction for this IA family.
- **Stop:** no new carrier is introduced and no frozen threshold calculation is reopened.

## Direct calculation

Write the Magnus variables as \(Z,X,Y\), and let \(C\) be any augmentation term of filtration degree at least 2, representing a lift of \(c\in D_2\). The radical-preserving shear is
\[
\alpha_C(z)=z\,c,\qquad \alpha_C(x)=x,\qquad \alpha_C(y)=y.
\]

The only load-bearing relation check is
\[
(zc)^9\stackrel{?}{=}z^9\pmod{D_{10}}.
\]

A relation-aware truncated noncommutative Magnus calculation over \(\mathbf F_3\), retaining all words of degree <10, gives
\[
\boxed{(zc)^9-z^9=0\quad\text{through degree }9}
\]
for the tested degree-\(\ge2\) radical corrections.

The calculation was independently repeated in two forms:

1. basis perturbations \(c=1+w\) for every monomial \(w\) of degrees 2 through 6; every coefficient of degree <10 cancels;
2. random full truncated augmentation corrections \(C\) with homogeneous components of degrees 2–4; again every degree <10 coefficient cancels.

In particular, for the critical degree-2 commutator direction \(w=[X,Y]\), the degree-9 coefficient is exactly zero.

The mechanism is not the earlier free-algebra shadow alone: here the defining relation is explicitly tested at the critical truncation. The cancellation is the characteristic-3 ninefold-power cancellation, with the degree-\(\ge2\) correction unable to create a surviving degree-9 term.

## Group-theoretic consequence

Because \(x,y\) are fixed, the Demushkin relator \(r_D=x^3[x,y]\) is fixed. The calculation above therefore gives
\[
\alpha_C(z)^9= z^9=r_D
\quad\text{in }W_{10}.
\]
Since \(\alpha_C\) is identity on \(x,y\), the inverse is obtained by the corresponding inverse radical correction. Hence this is an actual filtered IA automorphism of the finite presentation, not merely a graded shadow.

Consequently
\[
\pi_1\circ\alpha_C=\pi_c.
\]
Thus the entire explicit family \(\{\pi_c:c\in D_2(Q_{10})\}\) lies in one
\[
\operatorname{Aut}(W_{10})\times\operatorname{Aut}(Q_{10})
\]
orbit.

Since the relative split/non-split obstruction is invariant under precomposition by \(\operatorname{Aut}(W_{10})\) and postcomposition by \(\operatorname{Aut}(Q_{10})\), it is constant on this whole family.

## What this does and does not close

**Closed for the targeted IA family:** the degree-9 obstruction is preserved. There is no negative separation hidden inside the explicit \(\pi_c\) family.

**Not yet logically closed:** this calculation alone does not prove that every admissible epimorphism
\[
W_{10}\twoheadrightarrow Q_{10}
\]
with radical kernel is of the form \(\pi_c\), up to automorphisms. Residual IA corrections to \(x,y\), or other relation-compatible quotient-map data, still require a transitivity lemma if the full intrinsic reconstruction theorem is to be claimed.

Therefore the exact finite calculation yields a positive result at the load-bearing obstruction level, but the full Gate-B remains conditional on the orbit-completeness statement.

## Classification

- degree-9 radical-preserving IA action: **PASS / CLOSED**;
- explicit \(\pi_c\) family: **PASS / CLOSED (single orbit)**;
- degree-9 obstruction variation inside that family: **FAIL / CLOSED** (no variation);
- same-window separation from this family: **FAIL / CLOSED**;
- full admissible quotient-map orbit uniqueness: **OPEN / LOAD-BEARING**;
- full unmarked intrinsic reconstruction: **OPEN / LOAD-BEARING**.

## Decision boundary

The last direct calculation does **not** support a negative Gate-B conclusion. It instead strengthens the positive route: the apparently dangerous degree-9 IA correction is gauge-trivial at the critical obstruction.

The remaining question is no longer “does the degree-9 IA action destroy the reconstruction?” but only “does every admissible quotient map reduce to this IA orbit?” If the answer is yes, the Gate closes positively. If not, a genuinely different IA orbit must be exhibited and its obstruction tested.

No carrier search, threshold recomputation, degree-5 reopening, scalar/norm route, or RAAG branch is authorized by this result.
