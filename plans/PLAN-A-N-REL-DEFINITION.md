# A_n^rel Definition Audit — 2026-09-19

## Status

**DEFINITION DRAFT / NOT YET EXECUTED**

This document freezes the mathematical meaning of the proposed relator-preservation observable before the rank-2 implementation.

The purpose is to prevent three distinct notions from being conflated:

1. exact preservation of a chosen relator;
2. preservation of its normal closure modulo a filtration;
3. preservation of the relator line up to a 3-adic unit.

The third is the intended observable because exact equality would artificially force the orientation multiplier to be 1.

---

## 1. Research target

The present research should not ask whether the full finite quotient G/D_n determines q. That question is too strong for the intended weak-data program: the abelianization of G/D_n already exposes finite q once n is large enough.

The intended question is narrower:

> At what smallest filtered/graded level can the relator-preserving lift behavior distinguish q=3^s (s >= 2) from q=infinity, without using the full abstract finite quotient as input?

The q=3 case remains a control case, not the primary novelty target, because recent A_3-formality results already distinguish q=3 from q != 3.

---

## 2. Ambient linear group

Let V = F_3^4 for the rank-4 problem, equipped with the alternating form induced by the degree-2 initial part of the Demushkin relator.

There are two natural ambient groups:

- Sp(V): multiplier 1;
- GSp(V): arbitrary nonzero multiplier.

For g in GSp(V), write mu(g) in F_3^* for its multiplier.

The definition of A_n^rel should use **GSp(V) as the ambient group** if the observable is intended to retain the possible orientation/H^2 multiplier.

The previously used H = Sp_4(F_3) is then the multiplier-1 subgroup. It must not be silently substituted for GSp_4(F_3).

For the rank-2 control, replace V by F_3^2 and use

GSp_2(F_3) = GL_2(F_3),

with Sp_2(F_3) = SL_2(F_3) as the multiplier-1 subgroup.

---

## 3. Free-group/pro-p setup

Let F be the free pro-3 group on the chosen generators.

Let D_n(F) denote the standard descending 3-Zassenhaus filtration

D_n(F) = product_{i 3^h >= n} gamma_i(F)^{3^h}.

Let r_q be the defining relator.

Examples:

- rank 2, finite q:
  r_q = x_1^q [x_1,x_2];
- rank 2, q = infinity:
  r_infinity = [x_1,x_2];
- rank 4, finite q:
  r_q = x_1^q [x_1,x_2][x_3,x_4];
- rank 4, q = infinity:
  r_infinity = [x_1,x_2][x_3,x_4].

The notation q = infinity is shorthand for the pure-commutator baseline and is not to be treated as a numerical 3-adic value.

---

## 4. Lift class

For a linear map g in the chosen ambient group, a lift is an automorphism

  g~ in Aut(F)

whose induced action on F/Phi(F) is exactly g under the project's fixed coordinate convention.

The lift class must be fixed before computation. In particular:

- the generator images must be explicit;
- row/column convention must be explicit;
- composition order must be explicit;
- the induced action on V must be verified on basis vectors.

A mere matrix action on V is not itself a lift.

---

## 5. Relator-unit preservation

The intended admissibility condition at level n is:

  g~(r_q) belongs to < < r_q > > D_n(F)

where < < r_q > > denotes the closed normal closure in F.

Equivalently, after passing to the relevant quotient, the image of the relator lies in the relator-generated normal subgroup modulo D_n.

However, for the orientation-sensitive formulation we should record the stronger scalar statement whenever it is well-defined:

  g~(r_q) congruent to r_q^{u(g)} modulo the appropriate normal-closure/filtration relation,

where u(g) is a 3-adic unit.

The scalar u(g) is **not to be assumed unique in an arbitrary quotient**. Uniqueness must be checked at the first level where the relator class spans a one-dimensional coefficient/module. If uniqueness fails, only admissibility—not a multiplier—may be recorded.

At mod-3 level, the induced scalar is expected to reduce to the GSp multiplier when the degree-2 symplectic class is the controlling relator class. This is a structural expectation to be tested, not a premise of the computation.

---

## 6. Definition of A_n^rel

For a fixed presentation, filtration level n, and fixed lift convention, define

  A_n^rel(q)
  = { g in GSp(V) :
      there exists an admissible lift g~
      satisfying the relator-unit preservation condition at level n }.

The word "there exists" refers only to lifts within the explicitly fixed lift class. It must not allow an unrestricted search over arbitrary automorphisms that could change the meaning of the observable.

For a multiplier-1 study, define the restricted subgroup

  A_n^Sp(q) = A_n^rel(q) intersect Sp(V).

Do not identify A_n^rel(q) with a line stabilizer before computation.

The first mathematical question is whether A_n^rel(q) is strictly smaller than the ambient group and, if so, what structural feature accounts for the restriction.

---

## 7. Distinguished torsion line

For finite q, the abelianization contains a distinguished finite-q torsion direction generated by the image of x_1.

Let

  ell = < x-bar_1 >.

This line is a candidate source of symmetry breaking.

The following implications are **hypotheses, not definitions**:

  A_n^rel(q) is contained in Stab(ell),

or

  A_n^rel(q) equals Stab(ell).

The second statement is substantially stronger and must never be inferred from the first successful examples.

For q = infinity, there is no corresponding finite-order torsion line coming from x_1^q, so the baseline symmetry behavior must be computed independently.

---

## 8. Weak-data boundary

The full abstract quotient G_q / D_n is excluded as an input to the weak-data observable.

Reason: its abelianization can already reveal q. For q = 3^s, the finite-q contribution appears in the abelianization once n > q, so this gives the essentially tautological threshold n_0(q) = q + 1 under the standard convention.

Therefore:

- allowed: prescribed linear action, fixed graded/filtered pieces, relator class, and the lift/admissibility test;
- excluded: reading q directly from the abstract finite quotient's abelianization;
- excluded: declaring q recovered merely because G_q/D_n are non-isomorphic.

The project is interested in a structural observable, not an isomorphism test for finite quotients.

---

## 9. Rank-2 control

The rank-2 model is a pipeline control only.

It does not contain the rank-4-specific W_45 or degree-4 obstruction geometry. In particular, the rank-2 graded Lie algebra is not a substitute for the rank-4 obstruction problem.

Its purpose is limited to checking:

- restricted powers;
- filtration indexing;
- relator substitution;
- S_9 / degree bookkeeping where used;
- matrix/action conventions;
- relator-unit preservation;
- implementation independence.

For the first q=3 control, use n = 4 under the standard descending Zassenhaus indexing, since the degree-3 power term is invisible modulo D_3 and first visible modulo D_4.

The q=9 case is deferred to the small-degree search rather than folded into the first control.

---

## 10. Primary novelty target

The main target is revised to:

> Determine the smallest filtered/graded level, within the prescribed weak-data observable, at which q = 3^s for s >= 2 can be distinguished from q = infinity.

This target deliberately separates:

- q=3, which is already known to be special in higher cohomological structure;
- q>=9, where the project seeks a lower-level filtered/graded detection mechanism;
- orientation recovery, which remains downstream and is not identified with q-detection.

A successful q=9 or higher detection would therefore be materially more informative for the present program than merely rediscovering the q=3 exceptional case.

---

## 11. Execution gate

Before implementation, freeze the following in code/documentation:

1. exact D_n convention;
2. exact matrix convention;
3. exact lift convention;
4. exact relator-unit criterion;
5. whether the run is in GSp or Sp;
6. how u(g) is extracted, if it is defined;
7. independent sanity checks.

Only after this gate passes should the rank-2 n=4 computation be written or run.

---

## 12. Non-goals

This definition does not:

- prove that A_n^rel is canonical;
- prove that it is presentation-independent;
- prove equality with a line stabilizer;
- prove orientation recovery;
- replace the existing Q3/Q9 or O2 records;
- justify switching to the p-descending filtration;
- introduce Massey/A-infinity machinery.

Those remain separate questions.
