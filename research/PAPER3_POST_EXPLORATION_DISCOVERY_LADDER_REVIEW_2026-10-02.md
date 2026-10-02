# POST-PAPER-3 GENERALIZATION DISCOVERY LEDGER — BOUNDARY TO LADDER REVIEW
Date: 2026-10-02

## 1. Review target

The submitted proposal correctly identifies a missing research-program layer: the existing audits close individual branches but do not yet turn the negative results into a structured search for the nearest broader class.

The governing question is:
\[
W_k(G)\longrightarrow \mathcal C_k^{new}\longrightarrow \chi_G\bmod 3^k
\]
outside the fixed-rank standard Demuškin classification, with the carrier defined without inserting q or chi.

The proposal is accepted as a **research-direction correction**, but several proposed intermediate theorems are too strong or insufficiently intrinsic and must be repaired before authorization.

## 2. What is correct

### 2.1 The arbitrary-extension counterexample is a boundary marker

The examples
\[
Q=C_3^2,\quad A=C_3,
\]
with
\[
E_1=C_9\times C_3
\]
and the exponent-3 Heisenberg extension show that a bare pair \((Q,A)\), even together with the knowledge that it occurs as a central extension, does not determine the extension class.

The correct lesson is not that pair descent is generally impossible and therefore the search ends. The correct lesson is:

> any positive descent theorem must identify a restricted category in which the admissible extension-class fiber is rigid.

This is a legitimate new search axis.

### 2.2 Mixed Fox closure supplies a genuine diagnostic

The Mixed Fox branch is closed as a new recognition theorem because the surviving route factors through q/classification in the audited construction. This should be re-used as a negative test:

> a candidate that only reconstructs the known Demuškin parameter q and then applies the known orientation formula is not a new q-free orientation bridge.

The next carrier must therefore be tested for a direct orientation functional before investing in large computations.

## 3. Corrections to the proposed ladder

### 3.1 S1 rank variation is not yet a substantive new stage

For infinite Demuškin groups in the odd-p standard case, the minimal generator rank d is already an intrinsic invariant:
\[
d=\dim_{\mathbf F_p}H^1(G,\mathbf F_p),
\]
and for the finite quotient \(Q_k\) this H^1 information is already visible. Moreover, in the standard q\ne2 presentation the rank is necessarily even. Thus a proposed T1 asserting that isomorphic windows force d=d' is largely an H^1-level invariant check, not a new finite-recognition theorem.

The q-part of T1 also needs reformulation: q is a discrete p-power invariant in the standard classification, not a freely varying scalar. A statement such as q\equiv q' mod p^{k-1} must be replaced by the actual finite-window equivalence relation on the allowed q-values.

Therefore S1 should be retained only as a **sanity/control stage**, not as the main discovery target.

### 3.2 S2 should not be the next stage

The p=2 Demuškin classification has additional normal forms and orientation cases; odd-rank phenomena occur in special q=2 cases. This is a materially different classification regime, not a simple adjacent extension of the odd-p standard family. It should remain a later branch unless it produces a genuinely new carrier.

### 3.3 The proposed axiom (R) is not yet an intrinsic condition

The phrase “relator is a single element and the components of \(\partial r\) lie in different m-adic degrees” depends on a chosen presentation, generator system, and possibly relation representative. Before it can define a category, one must specify its invariant quotient/formulation under Nielsen transformations, relation-generator gauge, and relator conjugation.

More importantly, even an intrinsic “single-relator + mixed-degree Fox derivative” condition does not by itself imply extension-class uniqueness. The Heisenberg example is only one obstruction pattern; it does not establish that the proposed condition forces rigidity.

Thus T2, as written, is **OPEN and presently unsupported**, not a candidate theorem ready for computation.

### 3.4 T3 is substantially too strong

For mild pro-p groups, the literature gives strong control of the graded algebra from the initial forms of a strongly free set of relations. This does not imply that a shallow Zassenhaus window determines the next extension layer in general.

Mildness is precisely a condition on initial forms and graded structure; it does not by itself eliminate higher-order deformation data. Therefore
\[
W_k(G)\cong W_k(H)\Rightarrow G/D_{N_k+1}\cong H/D_{N_k+1}
\]
cannot be promoted merely from mildness.

The correct S4 question is weaker and more relevant:

> identify a restricted mild/one-relator subclass for which the extension-class fiber over the chosen finite window is rigid, or construct a same-window/different-next-layer counterexample.

This converts T3 into a genuine gate rather than an assumed theorem.

## 4. Revised discovery ladder

The useful ladder is therefore:

### S0 — standard Demuškin
Established control model.
- finite window → extension window: PASS/CLOSED at the declared standard scope;
- orientation recovery exists;
- Mixed Fox adds no non-redundant theorem.

### S0.5 — rigidity invariant extraction
Define the abstract obstruction:
\[
\mathfrak F(W)=\{[E]\;:\;E\text{ is admissible and projects to }W\}.
\]
The decisive property is not “relator-shaped” language but
\[
|\mathfrak F(W)|=1
\]
in the chosen admissible category, up to extension isomorphism.

This is the correct abstraction of what the Demuškin argument actually uses.

### S1 — nearest one-relator / PD2-like extensions
Do not begin with arbitrary rank variation. Instead ask whether the Demuškin rigidity mechanism survives in the nearest class where q is no longer the classifier but the group still has one relation / cd 2 / a controlled relation module.

Gate:
\[
W_k(G)\cong W_k(H)
\Rightarrow
[E_k(G)]\cong[E_k(H)].
\]
If false, record the first deformation parameter invisible to W_k.

### S2 — intrinsic “relator-coupling” condition
Only after identifying the actual invisible deformation should one formulate an invariant condition that kills it. The condition must be stated on the relation module / extension class / filtered cohomology, not on a raw Fox presentation.

### S3 — mild pro-p test bed
Use mild groups as an adversarial class, not as an assumed positive theorem. The literature establishes strong graded consequences of strong freeness, but higher filtered extension data can remain. citeturn0search3turn0search8

Gate:
same W_k + same proposed invariant → does the next extension layer still vary?

### S4 — genuine q-free orientation bridge
Only once a class with finite-window rigidity survives should one search for
\[
\mathcal C_k^{new}\to \chi\bmod 3^k
\]
without passing through q.

## 5. Immediate next authorized experiment

The first attack should therefore be **not a large computation and not T1 as originally stated**.

It should be a symbolic rigidity test on the smallest class strictly beyond the standard Demuškin classifier:

1. Fix odd p=3 and a small even rank where the standard model is explicit.
2. Keep the same finite pair/window \(W_k\).
3. Introduce the smallest admissible higher-order deformation of the one-relator relation that is invisible to the retained window.
4. Determine whether the deformation changes the extension class \(E_k\to Q_k\) or only changes data above the window.
5. If a same-window/different-extension example exists, close that candidate class.
6. If no deformation survives, formulate the resulting rigidity condition intrinsically and only then define a new carrier.

This is the correct “boundary → axiom → adjacent class” workflow.

## 6. Discovery-vs-verification distinction

The project should now maintain two layers:

- **Verification ledger:** records PASS/FAIL/CLOSED claims already established.
- **Discovery ledger:** records boundary observations, candidate classes, deformation parameters, and next falsification tests.

A discovery-stage OPEN must always have:
1. a precise candidate class;
2. a precise obstruction/fiber;
3. a smallest counterexample target;
4. a clear PASS/FAIL consequence.

## 7. Final classification of this review

- “FAIL at arbitrary extensions reveals a useful rigidity boundary”: **PASS / LOCAL**.
- “Mixed Fox closure motivates a q-free bridge search”: **PASS / LOCAL** as a research heuristic, not a theorem.
- S1/T1 exactly as proposed: **CONDITIONAL / REFORMULATE**.
- S2 as immediate next stage: **HISTORICAL / DEFERRED**.
- R/T2 as currently stated: **OPEN / NOT YET INTRINSIC**.
- T3 for all mild pro-p groups: **FAIL / CLOSED as an overstrong target**; weaker mild-subclass rigidity test remains OPEN.
- Revised nearest-class rigidity search: **OPEN / LOAD-BEARING**.
- Genuinely new q-free carrier: **OPEN**.

## 8. Operational consequence

No W_11/W_12, large Fox scan, or Paper 2 reproof is authorized.

The next branch is:

\[
\boxed{
\text{identify the smallest invisible deformation of }E_k
\;\longrightarrow\;
\text{find the weakest intrinsic condition that kills it}
\;\longrightarrow\;
\text{test the nearest broader class}
}
\]

Only after this survives may a new carrier be defined.
