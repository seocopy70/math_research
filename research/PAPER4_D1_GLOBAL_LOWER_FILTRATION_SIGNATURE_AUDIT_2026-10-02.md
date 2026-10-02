# PAPER 4 — GATE D1 FORMALIZATION: GLOBAL LOWER-FILTRATION SIGNATURE — 2026-10-02

## Decision

A definition-level D1 candidate survives the intrinsicity pre-check:

\[
\boxed{\Lambda_E(u,x):=
\max\{m\le n+1:\exists\ \tilde u,\tilde x\in Y,
\ \tilde u\mapsto u,\ \tilde x\mapsto x,\ [\tilde u,\tilde x]\in D_m(Y)\}}
\]

for an adjacent finite window
\[
E:\quad 1\to A=D_n/D_{n+1}\to Y=W_{n+1}\xrightarrow{\pi}X=W_n\to1,
\qquad L_1=X/\Phi(X),
\]
with \(u,x\in L_1\). The value \(n+1\) is assigned when the commutator is trivial in \(Y\); equivalently one may regard \(\Lambda_E(u,x)\) as the full set of attainable filtration depths rather than a single maximum.

The associated **global lower-filtration signature** of \(u\) is
\[
\boxed{
\mathcal L_E(u)=\bigl(\Lambda_E(u,x)\bigr)_{x\in L_1},
}
\]
or, without choosing a scalar encoding,
\[
\mathscr R_m(u)=\{x\in L_1:\exists\text{ lifts with }[\tilde u,\tilde x]\in D_m(Y)\},
\qquad
\mathcal L_E(u)=(\mathscr R_m(u))_{m=2}^{n+1}.
\]

This is deliberately a **global signature**, not a distinguished pair \((u,x)\), and not a bilinear map \(L_1\times L_1\to A\).

## 1. Object

The input is only the abstract filtered adjacent pair \((Y\twoheadrightarrow X)\), with its characteristic filtration and the induced degree-one quotient \(L_1=X/\Phi(X)\).

For each \(u\in L_1\), all lifts of \(u\) in \(Y\) are allowed. For each \(x\in L_1\), all lifts are allowed. The signature records which lower-filtration depths can be achieved simultaneously for that pair.

No presentation, generator, section, displayed \(q\), or orientation is part of the definition.

## 2. Why the definition is gauge/lift-independent

The crucial point is the existential quantifier over the **entire lift fiber**.

If an automorphism of the presentation or a change of section replaces a chosen lift by another lift in the same fiber, that new lift is already included in the defining set. Thus \(\mathscr R_m(u)\) is defined by the finite group extension itself, not by a selected representative.

This avoids the false step
\[
[\tilde u,\tilde x]\bmod D_{q+1}
\quad\text{is automatically independent of arbitrary }D_2\text{-lift changes}.
\]
That step was closed in the raw origin-restricted pairing audit.

## 3. Functoriality

A filtered isomorphism of adjacent windows transports:
- the filtration \(D_m\);
- the projection \(Y\to X\);
- the Frattini quotient \(L_1\);
- the complete lift fibers;
- the commutator relation.

Therefore
\[
\mathcal L_E(u)
\longmapsto
\mathcal L_{E'}(f(u))
\]
naturally under filtered isomorphism.

No claim is made yet for arbitrary non-isomorphic graph morphisms.

## 4. q-blindness

The definition contains no distinguished \(q\). It is defined simultaneously at every filtration depth available in the finite window.

The number \(q\) may later appear as the first exceptional depth in a particular target class, but that is an **output interpretation**, not an input to \(\mathcal L_E\).

This satisfies the required q-blindness test at the definition level.

## 5. Relation to the lower-obstruction problem

The previous failed formulation asked whether a particular pair satisfies
\[
[\tilde u,\tilde x]\notin D_q.
\]
That is too local and is unstable as a purported canonical degree-q value.

The present object instead records the entire depth profile
\[
m\longmapsto \mathscr R_m(u)
\]
against **all** degree-one directions simultaneously.

Thus a direction with one lower-degree contaminating origin is not merely assigned a yes/no label; the obstruction is part of its full global signature.

This directly addresses the current D1 requirement.

## 6. Independent model checks

### (a) Rank-two special edge

For
\[
G=\langle v,w\mid wvw^{-1}=v^{1+q}\rangle,
\]
the canonical special direction satisfies
\[
\Lambda_E(\bar w,\bar v)=q,
\]
because the first nontrivial commutator survives in \(D_q/D_{q+1}\).

The same depth is visible in the reverse pair up to the usual convention/sign/inverse:
\[
\Lambda_E(\bar v,\bar w)=q.
\]

This confirms that the signature retains the intended higher-depth defect without introducing \(q\) into its definition.

### (b) Long ordinary-chain contamination

In the audited chain
\[
r_1-r_2-a\to s,
\]
the special direction has q-depth against the relevant origin, whereas an ordinary contaminated direction has a degree-2 obstruction. Hence
\[
\mathcal L_E(\bar s)\neq \mathcal L_E(\bar s+\bar r_1)
\]
already at the lower part of the filtration profile.

This is the precise local phenomenon the scalar q-layer projection lost.

### (c) Separated two-sink model

For
\[
G=\langle a,b,s,t\mid sas^{-1}=a^{1+q},\;
tbt^{-1}=b^{1+q}\rangle,
\]
the signature detects
\[
\Lambda_E(\bar s,\bar a)=q,
\qquad
\Lambda_E(\bar t,\bar b)=q.
\]

However,
\[
\Lambda_E(\bar s+\bar t,\bar a)=q
\]
because the \(t\)-component is invisible to the \(a\)-sector in this model. Therefore D1 does **not** itself imply that q-active directions are literal sink directions.

This is not a failure of D1. It is an explicit warning that D2 must extract a quotient/kernel from the **relations among the full signatures**, rather than declaring the q-active locus to be \(N_q^\perp\).

### (d) Isolated special direction

The isolated-special counterexample remains controlling for the unrestricted class: an isolated special vertex can have orientation value 1 while contributing no special-edge lower-filtration signature. Thus no D1 object built solely from special-edge defects can recover the unrestricted orientation without an additional admissibility restriction or marked input.

D1 therefore does not reopen the already CLOSED unrestricted Gate-D no-go.

## 7. Non-tautology test

The construction does not reference \(\chi\), \(\omega_q\), Kummerianity, or a declared special-vertex set.

It is therefore not a disguised definition of the desired orientation.

The possible objection is different: the signature may be **too rich** because it records a large portion of the filtered multiplication. This is a coarseness/novelty question for D2/D3, not a definition-level failure.

## 8. Precise D1 theorem target

The load-bearing D1 statement is:

> For every admissible adjacent window, the family \(\mathcal L_E(u)\) is an intrinsic, presentation-independent, lift-independent, filtered-isomorphism-covariant global lower-filtration signature of \(u\in L_1\).

This statement is now defensible at the definition level.

What is **not** proved:
1. \(\mathcal L_E\) is linear in \(u\);
2. the sets \(\mathscr R_m(u)\) are always subspaces;
3. \(\mathcal L_E\) alone determines \(\omega_q\);
4. a canonical \(N_q\) can already be extracted;
5. the unrestricted specially oriented class admits positive orientation recovery.

## 9. Classification

- global lower-filtration signature definition \(\mathcal L_E\): **PASS / LOCAL**;
- presentation/lift/gauge independence: **PASS / LOCAL**;
- filtered-isomorphism covariance: **PASS / LOCAL**;
- q-blindness: **PASS / LOCAL**;
- non-tautological definition: **PASS / LOCAL**;
- linearity/subspace structure: **OPEN / LOAD-BEARING**;
- canonical quotient extraction \(N_q\): **OPEN / LOAD-BEARING**;
- orientation bridge \(N_q\to\omega_q\): **OPEN / LOAD-BEARING**;
- unrestricted Gate D: **FAIL / CLOSED** remains controlling;
- Paper 4: **OPEN / LOAD-BEARING** only on a declared restricted admissible class/input.

## 10. Stop rule for the next step

Do **not** immediately define
\[
N_q:=\operatorname{span}\{u:\mathcal L_E(u)\text{ is q-invisible}\}.
\]
The current separated two-sink examples already show why that would be too coarse.

The authorized D2 attack is narrower:

> Determine whether the **relations among the signatures**
> \[
> \{\mathcal L_E(u):u\in L_1\}
> \]
> canonically define a linear quotient \(U/N_q\), without inserting \(q\), \(\omega_q\), a graph, or a chosen basis.

The first test must be the smallest separated two-sink and the chordal-tree controls. If the resulting quotient still admits an orientation-changing automorphism, D2 closes for that signature.

## Final status

\[
\boxed{
\text{D1: intrinsic global lower-filtration signature = PASS / LOCAL}
}
\]

The result is a **definition-level advance**, not yet an orientation theorem. The next legitimate gate is D2, but only through relations among the full signatures, not through a q-visible locus or a pairwise obstruction.
