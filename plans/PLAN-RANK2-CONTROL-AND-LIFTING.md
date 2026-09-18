# Rank-2 Control and Lifting Audit — 2026-09-19

## Status

**PLANNED / NOT YET EXECUTED**

This is a low-cost control track added after the O2 transport-canonicality route failed to produce a transport-free 20-dimensional object.

It is a validation/control experiment, not a replacement for the existing rank-4 research.

## 1. Purpose

Test the basic relator-preservation / lifting pipeline on the rank-2 model

\[
G_q^{(2)}=\langle x_1,x_2\mid x_1^q[x_1,x_2]=1\rangle
\]

before using the same type of lifting question in the rank-4 problem.

The control is intended to detect implementation or convention errors in:

- free-group/free-Lie substitution;
- mod-3 arithmetic;
- filtration degree bookkeeping;
- restricted-power handling;
- relator preservation modulo a finite filtration level;
- induced action on the chosen quotient;
- equivariance conventions.

It must not be used to infer a rank-4 theorem.

## 2. Why rank 2 is the control

The rank-2 presentation is metabelian in the relevant setting and has a substantially smaller graded computation. This makes it suitable as a positive/negative control for the machinery before any large degree-9 rank-4 computation.

The control should reproduce facts that can be established independently from the presentation, rather than merely reproducing a number expected by the implementation.

## 3. Mathematical object to freeze before execution

For a chosen filtration level n, define a lift test only after fixing:

1. the exact filtration D_n;
2. the free-group automorphism model used to lift an element of the linear group on V;
3. the criterion that the lifted automorphism preserves the normal closure of the defining relator modulo D_n;
4. the induced action convention on V;
5. the finite-field convention.

No computation is valid until these are explicit.

## 4. Relation to the proposed A_n(q)

The candidate diagnostic is

\[
A_n(q)=\{g\in H:\text{there exists an admissible lift preserving the relator modulo }D_n\}.
\]

This definition is **provisional**.

It must not yet be called a weak-data invariant, because if the input includes the whole finite quotient G_q/D_n as an abstract group, q may already be recoverable from its abelianization. The intended weak-data version must expose only the prescribed graded/filtered action and relator-preservation information needed for the lift test.

The first task is therefore a definition audit, not a large computation.

## 5. Control cases

At minimum compare:

- q=3;
- q=∞, using the pure-commutator baseline;

and, if the same source construction permits it without additional complexity, q=9 only as a later control.

The q=∞ case must be defined independently as the baseline presentation, not selected after observing an invariant.

## 6. Required outputs

For the first small-degree control, record:

- exact definition of D_n;
- exact lift class being tested;
- representative symmetries preserving the distinguished line \ell=\langle\bar x_1\rangle;
- representative symmetries moving \ell;
- lift outcome for each representative;
- all coordinate/action conventions;
- independent sanity checks.

Do not require the full group A_n(q) in the first run.

## 7. Decision criteria

### PASS

The rank-2 control reproduces the independently justified expected lift behavior for the chosen representatives, with all convention and arithmetic checks passing.

This validates the pipeline sufficiently to proceed to a small rank-4 lifting experiment.

### MATHEMATICAL FAILURE

The implementation is independently validated, but the expected rank-2 mathematical statement is false.

Record the exact counterexample and stop before transferring the pipeline to rank 4.

### INVALID TEST

Any coordinate, filtration, field-arithmetic, stale-artifact, or lift-definition problem occurs.

Repair and rerun; do not interpret the output mathematically.

### SETUP FAILURE

The computation cannot be executed for environmental/toolchain reasons.

## 8. Non-goals

This control does not attempt to:

- prove q-recovery;
- prove orientation recovery;
- replace the Q3/Q∞ track;
- replace O2;
- justify the p-descending filtration;
- introduce Massey/A∞ machinery;
- claim generality beyond the tested rank-2 case.

## 9. Next gate after this document

Before implementation, complete the definition audit of A_n(q) and choose the smallest filtration level for which the lift condition is nontrivial.

Only then write/run the rank-2 computation.

## 10. Preliminary definition audit — 2026-09-19

The standard p-Zassenhaus convention gives
\[
D_n(G)=\prod_{ip^h\ge n}\gamma_i(G)^{p^h},
\]
so the graded contribution of degree 3 is visible in the quotient by \(D_4\), not by \(D_3\). In the rank-2 q=3 model, the commutator term has initial degree 2 while the p-power term \(x_1^3\) has degree 3. Therefore the first quotient that can see the q=3 power contribution is expected to be
\[
G_3^{(2)}/D_4,
\]
with the q=∞ baseline having no corresponding degree-3 power contribution.

This is a **filtration-indexing fact**, not yet a lift computation.

For the linear symmetry group of the rank-2 mod-3 generator space, the natural ambient group is
\[
Sp_2(\mathbf F_3)=SL_2(\mathbf F_3),
\]
which has order 24. The distinguished finite-q torsion direction is the line
\[
\ell=\langle\bar x_1\rangle.
\]
Its line stabilizer has index equal to the number of projective lines in \(\mathbf F_3^2\), namely 4, hence has order 6. This gives a concrete small-group control for the proposed line-stabilizer idea.

### Definition to use for the first control

For \(g\in SL_2(\mathbf F_3)\), a **lift at level n** will mean a specified automorphism \(\tilde g\) of the free pro-3 group on \(x_1,x_2\) whose induced action on \(F/\Phi(F)\cong\mathbf F_3^2\) is g. The admissibility condition is that \(\tilde g\) preserve the normal closure of the defining relator modulo \(D_n(F)\) (equivalently, the relator images agree in the relevant quotient), with the exact equivalence to be checked in the implementation.

The first computational level should therefore be **n=4**, because n=3 cannot see the degree-3 q-sensitive term under the standard descending-filtration convention.

### Weak-data restriction

The experiment must not take the entire abstract finite quotient \(G_q/D_4\) as an input object and then read q from its abelianization. The intended observable is the lift/admissibility behavior of prescribed linear symmetries relative to the fixed presentation/graded data.

The first run should therefore test representative elements in the line stabilizer and representative elements moving \(\ell\), rather than attempt to enumerate all of \(SL_2(\mathbf F_3)\).

### Literature boundary

Recent work of Pál–Quick independently establishes that, for odd-prime Demuškin groups, q=3 is distinguished from q\ne3 by \(A_3\)-formality of the continuous-cochain DGA. This confirms that q=3 can survive in higher structure, but it does not validate the present lifting observable or make the present filtered/graded route redundant. The current project therefore continues to target the weaker-data question. See arXiv:2601.07551. 
