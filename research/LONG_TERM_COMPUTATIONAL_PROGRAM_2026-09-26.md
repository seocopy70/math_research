# LONG-TERM COMPUTATIONAL RESEARCH PROGRAM — 2026-09-26

## Purpose

This document records a long-term, implementation-oriented research program for the successor-paper branch. The program is explicitly downstream of the two established theoretical results:

1. the finite-window affine/Kummer factorization through the corrected Zassenhaus quotient at depth
   [
   n_{mathrm{aff}}(k)=p^{k-1}+1;
   ]
2. sharpness of that depth in the admissible category of affine crossed-cocycle representations
   [
   S_k=A_ktimes U_{1,k},qquad A_k=mathbf Z/p^k,
   ]
   for every standard Demuškin parameter (fge1) and rank (dge2).

The existing publication manuscript is frozen. This program belongs to the successor branch and must not modify the frozen paper unless a later explicit publication decision authorizes it.

## Governing research protocol

Every task follows the repository's continuity protocol:

**pre-check → define object/input → justify legitimacy → execute → independent verification → classify → record immediately.**

Before any substantial computation, explicitly check:

- Object
- Input
- Functoriality
- Gauge
- Orientation bridge
- q-blindness
- Separation
- Novelty
- Stop conditions

A computational success is evidence, not by itself a new theorem. In particular, recovering a known canonical orientation in a chosen presentation is not a novelty claim.

## Task 1 — Explicit sharpness-witness computation

### Objective

Directly computationally verify the affine sharpness witnesses at small ((p,k,f,d)), confirming that the relevant affine crossed cocycle survives at
[
P_{p^{k-1}}
]
but is killed at
[
P_{p^{k-1}+1}.
]

### Initial test set

- (p=3, k=2,3);
- (p=5, k=2);
- several (f) values straddling (f<k) and (fge k);
- begin with (d=2), then repeat with unused coordinates added for (d>2).

### Witnesses

For (f<k), use the canonical candidate
[
ho(x_1)=1,qquad
ho(x_2)=(1-p^f)^{-1}pmod{p^k},
]
with
[
z(x_1)=1,qquad z(x_i)=0 (i>1).
]
The relation equation is satisfied, while
[
z(x_1^{p^{k-1}})=p^{k-1}
otequiv0pmod{p^k}.
]

For (fge k), use
[
ho(x_1)=1,qquad ho(x_2)=1+p,
]
with
[
z(x_1)=0,qquad z(x_2)=1,
]
and verify via LTE that
[
v_p!left(
rac{(1+p)^{p^{k-1}}-1}{p}
ight)=k-1.
]

### Implementation target

Implement the affine crossed-cocycle law and relator evaluation independently of the manuscript's coordinate formulas where possible. Then compare:

1. symbolic valuation prediction;
2. direct finite-ring computation;
3. filtration-membership prediction;
4. actual nonzero/zero image.

### Deliverable

A reproducible table of ((p,k,f,d)), witness type, valuation, image in (A_k), and survival/death at the two adjacent Zassenhaus depths.

Potential paper use: computational appendix / verification supplement, not automatically a theorem of independent novelty.

### Classification target

**OPEN** until independently implemented and checked.

---

## Task 2 — Finite-window recognition prototype on concrete Demuškin groups / local fields

### Objective

Implement the finite-window recognition mechanism and test it on concrete examples whose maximal pro-(p) Galois groups are known Demuškin groups.

### Candidate examples

Start with examples such as
[
mathbf Q_3(zeta_3),quad
mathbf Q_5(zeta_5),quad
mathbf Q_3(zeta_9),
]
subject to a preliminary verification of the precise (G_K(p)) presentation, Demuškin parameter, and orientation conventions for each field.

Rank-2 examples should be preferred initially to minimize quotient/presentation complexity.

### Required pre-check

Before implementation, verify independently:

- the exact Demuškin presentation or a suitable finite quotient model;
- the relevant (q)-parameter;
- the canonical orientation convention;
- how (Q_k=G/P_{p^{k-1}+1}) is represented computationally;
- what data are genuinely supplied to the recognition algorithm.

Do not silently identify a local-field presentation with the standard frozen presentation.

### Prototype

For a finite quotient (Q_k), implement the candidate predicate
[
mathsf K_k(Q_k,ho):
H^1(Q_k,mathbf Z/p^k(ho))
longrightarrow H^1(Q_k,mathbf F_p)
]
being surjective, together with the finite-depth crossed-cocycle realization used in the successor theory.

Test:

1. candidate orientation residues;
2. existence of lifts;
3. uniqueness among candidates;
4. factorization through (Q_k);
5. disappearance of information below the sharp depth.

### Deliverable

A reproducible success/failure matrix by field, (p), (k), quotient depth, candidate (ho), and recovered orientation residue.

### Important boundary

This is an application/implementation experiment. It does not establish a new theorem merely by reproducing the canonical orientation already known from Demuškin theory.

### Classification target

**OPEN** until the concrete finite quotient model and recognition implementation are independently validated.

---

## Task 3 — Numerical measurement of q-collapse / information loss

### Objective

Measure directly how the finite quotient loses information about the Demuškin parameter (q=p^f), especially across the threshold (f=k).

### Initial experiment

For fixed small (p,k), construct the standard family
[
G_f=langle x_1,ldots,x_dmid
x_1^{p^f}[x_1,x_2][x_3,x_4]cdots=1angle
]
for
[
f=1,2,ldots,k+1.
]

Compute finite quotients at the sharp window and, where useful, one step shallower.

### Measurements

At minimum record:

- abelianization of the finite quotient;
- invariant factors;
- images of the power relation;
- candidate orientation residues modulo (p^k);
- whether (q=p^f) remains distinguishable.

The expected structural transition to test is the (f<k) versus (fge k) collapse in the abelianized finite quotient.

### Deliverable

A table indexed by ((p,k,f)) showing the abelianization structure and the exact collapse threshold, plus a separate table for orientation-residue behavior.

### Logical boundary

q-collapse is an information-loss/separation result. It is not, by itself, a proof that no structured or marked finite carrier can recover the lost information.

### Classification target

**PASS / LOCAL** only after direct computation agrees with the theoretical formula; otherwise classify the discrepancy explicitly.

---

## Task 4 — Compare Zassenhaus depth with other natural filtrations

### Objective

Determine experimentally how the sharp affine factorization depth compares with lower (p)-central and related natural filtrations.

### Candidate comparison

For the same affine recognition problem, measure the first truncation depth at which all relevant crossed cocycles factor through:

- Zassenhaus filtration;
- lower (p)-central filtration;
- other explicitly defined dimension-series variants, if computationally accessible.

### Required discipline

The filtration must be defined precisely before comparing depths. Do not transfer a Zassenhaus result to lower (p)-central notation; the 2026 manuscript audit already established that confusing these filtrations caused a substantive error.

### Deliverable

A filtration-by-filtration depth table and a proof-oriented explanation of any observed difference.

### Classification target

**OPEN**. Computation may suggest a comparison theorem but does not establish optimality without a structural argument.

---

## Recommended execution order

1. **Task 1 — explicit sharpness witnesses**
2. **Task 3 — q-collapse / information loss**
3. **Task 2 — concrete recognition prototype**
4. **Task 4 — filtration comparison**

This order minimizes implementation risk and keeps each experiment tied to an already established theorem.

## Long-term success criterion

The program is successful if it produces a reproducible computational layer that:

- verifies the sharpness witnesses independently;
- visualizes the (f<k) / (fge k) information boundary;
- demonstrates finite-window recognition on at least one independently validated concrete Demuškin example;
- clarifies whether other filtrations exhibit a different factorization depth.

Any stronger mathematical conclusion requires a separate proof gate and literature audit.

## Status

**LONG-TERM PROGRAM: OPEN / AUTHORIZED FOR STAGED IMPLEMENTATION**

No computation is implied by this record. Each task must pass its own pre-check before execution.
