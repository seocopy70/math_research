## 2026-10-04 — Paper 4 critical same-window correction

- The previously claimed same-window order jump is **FAIL / CLOSED as a proof route**: the defining normal closures are not nested, so no canonical epimorphism follows and the claimed p-factor order jump is false.
- Exact unmarked threshold n_sep(s)=p^s+1 is **OPEN**. The certified lower bound n_sep(s)>=p^s+1 remains **PASS / CLOSED** in the stated scope.
- G_{s,a} not isomorphic to G_{t,a} is **OPEN**. Abelianization, W-critical-window order/abelianization, canonical index-p subgroup abelianization, mod-p cohomology, and gr do not separate s in the checked family.
- Existing (p,s)=(3,2),(3,3) transfer/Schreier results remain **PASS / LOCAL** only; (SC_s)/(TF_s) remains **OPEN / LOAD-BEARING**.
- Paper 4 certified core below this boundary remains **PASS / CLOSED**; no exact-threshold or all-s separation claim may be promoted.

## 2026-10-04 — TF_s / index-p Zassenhaus comparison review correction

The latest direct proof attempt and literature review **do not certify** the subgroup-comparison lemma
\[
(SC_s)\qquad D_{p^s+1}(F)\cap K\subseteq D_{p^{s-1}+1}(K).
\]

- The earlier augmentation-ideal equality \(I_F^n\cap\mathbf F_p[K]=I_K^n\) is **FAIL / CLOSED**; \(F=\mathbf Z, K=p\mathbf Z\) gives a counterexample.
- Likewise \(D_n(F)\cap K\subseteq D_n(K)\) is **FAIL / CLOSED**; the same abelian example shows the necessary degree loss.
- Jennings recursion alone does not prove \((SC_s)\), because \(w_1^p\in K\) does not imply \(w_1\in K\).
- Lazard/Jennings formulas and the induced \(D_{p^{s-1}+1}(K)\to K^{ab}\subseteq p^sK^{ab}\) statement remain **PASS**.
- Shalev Proposition 1.2 was checked as a result about the filtration of a single group; it does **not**, on the evidence currently verified, supply the required index-\(p\) intersection theorem.
- Therefore \((TF_s)\) remains **OPEN / LOAD-BEARING**, not FAILED: the only missing bridge is the subgroup-filtration comparison (or an alternative direct proof of the same \(K^{ab}\)-image bound).
- The \((p,s)=(3,2)\) Schreier/transfer witness remains **PASS / LOCAL** and is not promoted to an all-\(s\) theorem.

**Current Paper 4 boundary:** the exact all-\(s\) \(a=s\) vs. \(a=\infty\) separation is **OPEN / LOAD-BEARING**. Paper 4 is not FINAL. The cleanest current fallback is a **CONDITIONAL** theorem: if \((SC_s)\) (or directly \((TF_s)\)) is certified, the transfer-defect separator closes the remaining boundary.

This supersedes the earlier log entry that labeled the intrinsic transfer-defect boundary "CLOSED"; that earlier label must not control the current state.


## 2026-10-04 — Restricted-Lie TF_s proof audit correction

The newly proposed restricted-Lie induction does **not** certify \((TF_s)\). The lower-central graded object was incorrectly treated as a free restricted Lie algebra; the induction also controls \(\gamma_i(K)\), not the required ambient \(\gamma_i(F)\cap K\), and the Zassenhaus-weight implication used in the reduction is not reversible. Accordingly, the central divisibility bound remains **OPEN / LOAD-BEARING**.

Paper 4 **certified core remains PASS / CLOSED**. The all-\(s\) \(a=s\) versus \(a=\infty\) boundary remains **OPEN / LOAD-BEARING** and is not promoted to FINAL by this attempt.


## 2026-10-04 — next boundary attack: s=3 local witness

The next Paper 4 step is now fixed at the smallest unresolved continuation beyond \((p,s)=(3,2)\): the \((p,s)=(3,3)\), \(W_{28}\) truncation audit. A model Schreier-lattice calculation gives
\[
9(\sigma-1)^2[a_0]\ne0
\]
under the untruncated relations, extending the local transfer-defect pattern. Classification: **PASS / LOCAL** only. The actual \(W_{28}\) statement remains **OPEN / LOAD-BEARING** until the image of \(D_{28}(F)\cap K\) in \(K^{ab}\) is controlled. No all-\(s\) theorem is promoted.

Immediate target: certify or refute the actual truncation effect at \((p,s)=(3,3)\). If it is contained in \(27K^{ab}\), the \(s=3\) separator closes; if not, the transfer-defect mechanism fails at this next test.


## 2026-10-04 — decision: do not start the general E_ψ generator as a Paper 4 step

The proposed replacement of the Demuškin-specific test group E' by a universal twisted-character test family E_ψ is recognized as a potentially useful route toward a broader theorem, but it is **not authorized as the next Paper 4 computation**.

Reason: the current Paper 4 mathematical core is to be treated as complete in its certified scope, while the exact all-s boundary remains an explicitly OPEN/CONDITIONAL extension rather than a publication-blocking task. Building E_ψ would therefore reopen a broader general theorem whose legitimacy, intrinsic definition, and separation mechanism are not yet established. In particular, the existence of a twisted character ψ annihilating a Fox-derivative expression is not by itself a proof that a canonical finite test group E_ψ exists or that it yields n_sep=p^s+1.

Classification:
- Paper 4 certified core: **PASS / CLOSED**.
- all-s transfer-defect / exact-threshold boundary: **OPEN / intentionally left open**.
- universal E_ψ test-group construction: **OPEN / future generalization**, not a Paper 4 dependency.
- Direction 1 generator implementation: **DEFERRED**, not started.

Decision consequence: stop the new general-theorem branch here and move to Paper 4 organization/writing. If later reopened as a separate generalization program, the first task must be a pre-check defining E_ψ intrinsically and proving functoriality/gauge invariance before any large computation.


## 2026-10-04 — decision: bounded test-family generalization challenge

The user has decided that the certified Paper 4 core, while mathematically real, is too narrow relative to the original generalization ambition. Instead of moving directly to organization/writing, a **bounded test-family generalization challenge** is authorized.

This is not a reopening of the closed core and not a return to the failed arbitrary-(r) theorem. The first test family is the narrowest genuinely broader class suggested by the surviving mechanism:

[
G_{s,a}(r_2)=langle z,x_1,ldots,x_dmid z^{p^s}=x_1^{p^a}r_2angle,
qquad s>age2,
]
where (p) is odd and (r_2) is a nonzero quadratic initial relation, with the rank-two stress relation (r_2=[x_1,x_2]) as the control case.

The challenge is to determine whether the critical relative-window mechanism (n=p^s+1) survives when the Demuškin-specific quadratic form is replaced by a broader quadratic class. The test must vary the quadratic input enough to be a real generalization, but remain bounded enough to distinguish a structural mechanism from accidental presentation-specific behavior.

### Pre-check required before computation

- **Object:** relative finite-window extension (W_n(G)	o D/D_n(D)), and its first intrinsic candidate obstruction.
- **Input:** (p,s,a,d) and the quadratic initial form (r_2), with (q=p^a); (q) must not be inserted into the finite-window object itself.
- **Functoriality:** quotient maps and admissible changes of generators must induce the obstruction map.
- **Gauge:** normalize quadratic forms only modulo the explicitly allowed automorphism/gauge action; do not identify non-equivalent forms by presentation convenience.
- **Orientation bridge:** the map from the finite-window data to the relative extension/orientation datum must be stated before testing.
- **q-blindness:** the candidate finite object must be defined without (q=p^a).
- **Separation:** at minimum compare the control stress case against a genuinely different quadratic form in the same parameter range.
- **Novelty:** distinguish a theorem about the broader quadratic class from the already closed Demuškin stress-family threshold.
- **Stop:** if intrinsicity or the orientation bridge fails, stop the generalization rather than enlarging the family.

### PASS/FAIL gate

- **PASS:** the same critical obstruction factors naturally for the broader quadratic test family, with a theorem-level statement and at least one independent non-control example.
- **FAIL:** the mechanism depends essentially on the Demuškin quadratic form, or two admissible quadratic inputs produce incompatible obstruction behavior at the same critical window.
- **CONDITIONAL:** the mechanism survives only under an explicit nondegeneracy condition on (r_2).
- **OPEN:** computation reveals a coherent broader pattern but the intrinsic factorization or general proof is not yet closed.

The existing arbitrary-(r) degree-only generalization remains **FAIL / CLOSED**, and the universal (E_\psi) branch remains deferred. No Paper 5 compression work is reopened.

Immediate next action: perform the pre-check and then use the smallest non-control quadratic test cases before any large computation.


## 2026-10-04 — bounded generalization challenge: execution authorization

The user's proposed broader-testing direction is **ACCEPTED with one governance correction**: the research will pursue a genuinely broader quadratic test family, but the universal arbitrary-(r) E_ψ generator is **not** the first computation. The authoritative active branch is the bounded family already defined above.

### Scope
- Object: relative finite-window extension W_n(G) -> D/D_n(D) and its first intrinsic obstruction.
- Family: G_{s,a}(r_2)=<z,x_1,...,x_d | z^{p^s}=x_1^{p^a}r_2>, odd p, s>a>=2, nonzero quadratic initial form r_2.
- Control: r_2=[x_1,x_2].
- Non-control: a quadratic form genuinely outside the control orbit; the first meaningful comparison should use d>=4, e.g. a rank-4 quadratic form such as [x_1,x_2]+[x_3,x_4], rather than only rank-2 forms that are GL-equivalent in small rank.
- q-blindness: q=p^a is a family parameter, not part of the finite-window object used for recognition/separation.

### Pre-check decision
Before any large computation, certify Object/Functoriality/Gauge/Orientation bridge/q-blindness/Separation/Novelty/Stop. In particular, the obstruction must be defined intrinsically and the bridge to the relative extension/orientation datum must be explicit. If that fails, stop this branch rather than enlarging the family.

### Evidence interpretation
The reported p=3,s=1 experiments are **motivation only**, not evidence closing the new theorem: s=1 lies outside the authorized s>a>=2 family and the n=4 window is too small. The degree-3 example [[x,y],y] is also outside the first quadratic-input family. These experiments therefore do not alter the current classification.

### Relation to E_psi
The universal E_psi construction remains **OPEN / future generalization**. It may be revisited only after the bounded quadratic-family challenge establishes that the obstruction mechanism survives beyond the Demushkin control case and after an intrinsic E_psi object/functoriality pre-check is passed.

### Immediate next action
Execute the pre-check, then construct the smallest non-control quadratic test case and compare it with the control case at the first feasible stress parameters. No s=2 large-window computation is authorized until the pre-check passes.


## 2026-10-04 — strategic correction: universal E_psi challenge explicitly authorized

The prior decision to defer the universal E_psi branch is **superseded as a strategic restriction**. The continuity protocol is a guard against unrecorded scope drift and invalid promotion of exploratory work; it is not a prohibition on deliberately opening a high-risk generalization branch. The user explicitly chooses to pursue the universal E_psi direction as a bold exploratory challenge.

### Status and boundary
- Universal E_psi branch: **OPEN / ACTIVE EXPLORATORY GENERALIZATION**.
- This branch is not silently promoted to the Paper 4 theorem core. Paper 4's certified core remains **PASS / CLOSED**.
- The arbitrary-r degree-only theorem remains **FAIL / CLOSED** and must not be revived in its old form.
- The new target is conditional: determine whether an intrinsically defined twisted-character test object E_psi exists for a broad class of relations r, and whether its critical-window separation mechanism can be proved. Failure is a legitimate research result.

### First gate (mandatory, but not a veto on exploration)
The first task is the E_psi pre-check:
1. Object — define E_psi without circularly inserting the unknown q/orientation into the finite-window object.
2. Input — specify exactly what data from (r,p,s) are allowed.
3. Functoriality — prove or falsify invariance under admissible generator changes/presentation equivalence.
4. Gauge — identify the character/lift normalization and quotient the gauge action explicitly.
5. Orientation bridge — state the exact map from the finite-window obstruction to psi and then to the relation z^(p^s)=r.
6. q-blindness — test whether q can be recovered rather than encoded in E_psi.
7. Separation — first test control cases, then genuinely non-Demushkin relations.
8. Novelty — compare against known Fox/Koch/cyclotomic constructions before calling the mechanism new.
9. Stop/branch rule — if the canonical object fails, record FAIL/CLOSED for this E_psi formulation and redesign; do not quietly substitute a presentation-dependent object.

### Computation policy
No large s=2/3 sweep is required before the pre-check. Once the object survives the pre-check, a minimal finite generator should be implemented and immediately tested at p=3,s=2 and p=3,s=3 on both control and non-control relations. The earlier s=1 experiments remain motivating evidence only.


## 2026-10-04 — E_psi intrinsic-definition attack: first closure and remaining boundary

The universal E_psi branch was attacked from the definition rather than from computation.

### Definition correction

The earlier informal condition “twisted Fox derivative = 0” is not the correct detector for
[
z^{p^s}=r.
]
The correct affine condition is **nonzero critical translation**.

Set
[
A_s=\mathbf Z/p^{s+1}\mathbf Z,qquad U_s=1+pA_s,qquad
E_s=A_s\rtimes U_s.
]
For a character
[
\psi:F\to U_s
]
and a crossed homomorphism
[
\delta:F\to A_s,qquad
\delta(gh)=\delta(g)+\psi(g)\delta(h),
]
the affine representation is
[
\rho_{\psi,\delta}(g)=(\delta(g),\psi(g)).
]

Define the twisted Fox evaluation ideal
[
I_\psi(r)=
\sum_i A_s\,\psi\!\left(\frac{\partial r}{\partial x_i}\right)
=
\{\delta(r):\delta\in Z^1(F,A_{s,\psi})\}.
]

Then the critical relation admits an affine lift with
[
z\mapsto(1,1)
]
iff
[
\psi(r)=1,qquad p^s\in I_\psi(r).
]

This is the correct E_psi object: the finite affine target together with the twisted evaluation ideal. The group alone is not the invariant.

### Definition/gauge/functoriality audit

- **Object:** PASS / CLOSED for the affine test datum.
- **Input:** PASS / CLOSED.
- **Functoriality:** PASS / CLOSED in the marked free-presentation category; individual Fox coordinates change, but the evaluation ideal and affine-lift existence are invariant.
- **Gauge:** PASS / CLOSED when \psi(r)=1; affine translation changes \delta by a coboundary and leaves \delta(r) unchanged, while unit rescaling preserves the valuation condition.
- **q-blindness:** PASS / CLOSED. The target is indexed by the critical window s and does not insert an unknown q into the recognition object.
- **Orientation bridge:** OPEN / LOAD-BEARING for unmarked finite windows. The affine representation has a canonical linear character \psi, but recovering that character intrinsically from the abstract finite window has not been proved.

### Affine target depth

For
[
E_s=A_s\rtimes U_s,
]
one has
[
D_{p^s}(E_s)=p^sA_s\ne1,qquad D_{p^s+1}(E_s)=1.
]
This follows from Lazard's product formula together with
[
[E_s,E_s]=pA_s,qquad
\gamma_i(E_s)=p^{i-1}A_s (i\ge2)
]
until vanishing.

Hence E_s is an exact finite detector for the p^s/p^s+1 boundary.

### General quadratic input

For every tested nonzero quadratic initial relation
[
r\in D_2(F)\setminus D_3(F),
]
there are explicit characters/cocycles producing
[
\psi(r)=1,qquad v_p(\delta(r))\le s.
]
Independent finite-word checks covered:
- p=3,5;
- s=1,2,3;
- random quadratic words in rank 3;
- all 26 nonzero canonical quadratic forms in rank 2 for p=3;
- all 124 nonzero canonical quadratic forms in rank 2 for p=5.

These are **PASS / LOCAL** only.

The formal general lemma still needs a proof with the higher-order contribution audit closed. In particular, in the pure-commutator case the chosen order-p character isolates the quadratic commutator contribution at the p^s scale, but higher Zassenhaus terms must be bounded carefully; if they contribute at lower valuation that only helps, while an exact cancellation at the critical scale must be excluded algebraically.

### Marked separation result

The affine lift gives
[
\rho(z^{p^s})=(p^s,1)=\rho(r)\ne1,
]
while
[
\rho(z^{p^t})=1qquad(t>s).
]
Because
[
D_{p^s+1}(E_s)=1,
]
the representation factors through the marked critical window
[
W_{p^s+1}(G_s(r))
]
but not through the lower window.

Thus the **marked affine/representation critical threshold is a theorem candidate at p^s+1 for arbitrary nonzero quadratic initial relation**.

This does **not** prove
[
W_{p^s+1}(G_s(r))\not\cong W_{p^s+1}(G_t(r))
]
as abstract unmarked finite groups. The missing implication is precisely the intrinsic orientation/character bridge from the abstract window to the affine representation package.

### Classification

- universal arbitrary-degree E_psi theorem: **FAIL / CLOSED** in the old degree-only form;
- affine E_psi definition: **PASS / CLOSED**;
- functorial/gauge/q-blindness pre-check: **PASS / CLOSED** in the marked category;
- quadratic affine separator: **OPEN / LOAD-BEARING theorem candidate**;
- marked critical-window separation: **PASS / LOCAL → theorem candidate**;
- unmarked orientation bridge: **OPEN / LOAD-BEARING**;
- unmarked same-window separation: **OPEN**.

Authoritative detail: `research/EPSI_INTRINSIC_DEFINITION_AUDIT_2026-10-04.md`.


## 2026-10-04 — E_psi quadratic separator CLOSED after second audit

The E_psi branch has now passed the previously load-bearing quadratic proof gate.

### Correction
For odd p,
\[
D_2(F)/D_3(F)\cong\Lambda^2H_1(F,\mathbf F_p),
\]
so the earlier inclusion of \(X_i^{[p]}\) terms in the degree-two initial form was **FAIL / CLOSED** and is superseded.

### Closed lemma
For every
\[
r\in D_2(F)\setminus D_3(F),
\]
write its nonzero quadratic class as
\[
\rho_2(r)=\sum_{i<j}b_{ij}[X_i,X_j],\qquad B\ne0.
\]
With \(A_s=\mathbf Z/p^{s+1}\), choose an order-p character \(\psi_\alpha:F\to1+p^sA_s\) and a crossed homomorphism. The quadratic contribution is
\[
\delta(r_2)\equiv p^sL_B(\alpha,u)\pmod{p^{s+1}},
\]
with \(L_B\) a nonzero linear functional for a suitable \(\alpha\).

The \(D_3\)-tail cannot simply be discarded: its \(\gamma_3\)-part is \(0\pmod{p^{s+1}}\), while its p-power part contributes an \(\alpha\)-independent linear functional at the same normalized \(p^s\)-scale. Varying the character parameter \(\alpha=t e_k\) makes the nonzero quadratic functional avoid cancellation with that fixed tail. Hence there exist \((\psi,\delta)\) with
\[
\psi(r)=1,\qquad v_p(\delta(r))=s,
\]
so \(p^s\in I_\psi(r)\).

Classification: **PASS / CLOSED** for the marked affine quadratic separator. This is strictly narrower than the failed arbitrary-degree theorem; no degree-only generalization is revived.

### Consequence
Because \(D_{p^s+1}(E_s)=1\), the affine representation gives a marked critical-window detector at \(n=p^s+1\), and it does not descend to \(W_{p^s}\). Thus the marked affine critical threshold is now a theorem-level result for all nonzero quadratic initial relations.

### Remaining load-bearing boundary
This still does **not** imply
\[
W_{p^s+1}(G_s(r))\not\cong W_{p^s+1}(G_t(r))
\]
as abstract unmarked finite groups. The sole remaining structural obstacle in this E_psi formulation is the **unmarked orientation/character bridge** from the abstract finite window to the affine representation package.

Do not enlarge to arbitrary Zassenhaus degree. If the orientation bridge fails, the correct endpoint is a PASS/CLOSED marked theorem plus OPEN unmarked reconstruction.


## 2026-10-04 — E_psi orientation-bridge audit

The next load-bearing E_psi gate was attacked directly.

- **Canonical single-character orientation bridge: FAIL / CLOSED.**
- **Orbit/groupoid-valued affine package: OPEN / LOAD-BEARING.**
- **Abstract unmarked same-window separation for general r in D_2\\D_3: OPEN.**

For the rank-two control relation r=[x_1,x_2], determinant-one Nielsen automorphisms preserve the commutator relator up to conjugacy and induce the standard SL_2(F_p)-action on the order-p character space. The successful affine characters form the nonzero orbit. Since SL_2(F_p) is transitive on nonzero vectors, no individual nonzero psi can be canonically recovered from the abstract finite window.

This is a genuine no-go for the route
abstract window -> distinguished psi -> affine separator,
not a failure of the affine E_psi definition itself.

The surviving bridge must therefore be orbit-valued: an automorphism/gauge-invariant set or groupoid of successful affine representations, or an orbit-invariant evaluation/defect functional. The next authorized attack is to construct such an orbit-level defect and test whether it separates s from t. If it cannot be made intrinsic, the E_psi formulation ends at the marked theorem.

Authoritative detail: research/EPSI_ORIENTATION_BRIDGE_AUDIT_2026-10-04.md.


## 2026-10-04 — intrinsic carrier salvage after the single-psi no-go

A canonical replacement for a distinguished psi was found:

\[
\mathcal A(W)=\operatorname{Ann}_{H^1(W,\mathbf F_p)}(\operatorname{Tor}(W^{ab})).
\]

This is intrinsic to the abstract finite window. For the critical quadratic family, the marked separator can be chosen with its character in this subspace: if \bar r=p^k a, choose a nonzero character direction alpha with alpha(a)=0 and with nonzero contraction against the quadratic alternating form B. Such an alpha exists because a nonzero alternating form cannot vanish on all of a^perp.

**PASS / CLOSED:** canonical character carrier \mathcal A(W).

**PASS / CLOSED:** existence of a successful marked affine character inside \mathcal A(W) for r in D_2\\D_3.

**OPEN / LOAD-BEARING:** the carrier does not itself distinguish s from t. The remaining object must be an orbit-invariant extension defect attached to the power relation, not merely a canonical character subspace.

Authoritative detail: research/EPSI_ORIENTATION_BRIDGE_AUDIT_2026-10-04.md.


## 2026-10-04 — critical correction to E_psi carrier proposal

The proposed carrier
\[
\mathcal A(W)=\operatorname{Ann}_{H^1(W,\mathbf F_p)}(\operatorname{Tor}(W^{ab}))
\]
is **FAIL / CLOSED** as stated.

Reason: the finite window W is a finite p-group, so W^{ab} is finite p-primary torsion and therefore Tor(W^{ab})=W^{ab}. Since
\[
H^1(W,\mathbf F_p)\cong\operatorname{Hom}(W^{ab},\mathbf F_p),
\]
the annihilator of all W^{ab} is zero. Thus the earlier PASS/CLOSED claim for a nonzero intrinsic carrier was false.

The marked E_psi theorem and the single-character symmetry no-go remain valid. The replacement intrinsic carrier is now OPEN and must use a genuinely nontrivial filtered/extension/Bockstein structure of W rather than ordinary torsion annihilation.


## 2026-10-04 — correction: Sp-orbit orientation bridge does not close

The proposed PASS/CLOSED conclusion for the abstract E_psi orientation bridge via an Sp-orbit is **superseded and rejected**. Nonzero quadratic initial form does not imply nondegeneracy; rank-4 r_2=[x_1,x_2] is an explicit degenerate counterexample. The exponent s is also unrelated to quadratic-form rank. Even in the nondegenerate symplectic subcase, transitivity only removes representative choice and does not provide an intrinsic extension defect separating s from t, while recovery of B from the abstract finite window remains unproved.

Current status: marked quadratic E_psi separator **PASS / CLOSED**; single-character bridge **FAIL / CLOSED**; Sp-orbit bridge in general D_2\D_3 **FAIL / CLOSED as stated**; nondegenerate symplectic subcase **CONDITIONAL**; intrinsic orbit/groupoid defect **OPEN / LOAD-BEARING**; abstract same-window separation **OPEN**.

Immediate next task: test a genuinely intrinsic filtration/extension object on the degenerate rank-4 example r_2=[x_1,x_2], without importing the presentation-level B or psi.


## 2026-10-04 — critical correction: marked (s) is target-indexed, not an invariant of (r_2)

The proposed next gate “does (v_p(\delta(r))) depend only on (r_2)?” was audited against the actual marked E_\psi construction. That question was ill-posed.

In the closed marked lemma, (s) is fixed **before** constructing the affine target:
\[
A_s=\mathbf Z/p^{s+1}\mathbf Z,qquad E_s=A_s\rtimes(1+p^sA_s).
\]
The lemma then asserts that for every nonzero quadratic initial relation (r\in D_2\setminus D_3), after choosing the order-(p) character and cocycle in that (E_s), one can arrange
\[
\psi(r)=1,qquad v_p(\delta(r))=s.
\]
Thus (s) is not extracted from (r), and there is no single (\delta) whose valuation is an invariant attached to (r_2). The cocycle takes values in the (s)-dependent module (A_s).

For (r_A=[x_1,x_2]), this is explicit for every (s\ge1): take \(\psi(x_1)=1+p^s\), \(\psi(x_i)=1\) for (i>1), and choose the normalized cocycle with (u_2=1) and the other relevant coordinate zero. Then
\[
\delta([x_1,x_2])\equiv p^s\pmod{p^{s+1}},
\]
so the same fixed relation admits a critical affine lift at every target index (s).

Therefore:
- “marked (s) is determined by (r_2)” = **FAIL / CLOSED as a formulation**;
- “same (r_2) implies same marked (s)” = **FAIL / CLOSED**;
- the deduction that marked (s) is not an abstract invariant from that premise is **superseded**;
- the genuine unmarked orientation/orbit-level problem remains **OPEN / LOAD-BEARING**.

This also separates two notions previously conflated: (i) the Zassenhaus degree of a higher tail inserted into a relator, and (ii) the externally indexed critical depth of the affine detector. They are different parameters and must not be identified.

For the exploratory pair (r_A) versus (r_B=r_Ax_1^{p^m}), any separation caused by the added degree-(p^m) tail is therefore a filtered-relator/quotient statement, not evidence that the marked E_\psi exponent parameter is encoded by the quadratic initial form.


## 2026-10-04 — refinement: the higher-jet critical pair is genuinely separated, but is not exponent-same-family separation

For the exploratory pair
\[
r_A=[x_1,x_2],\qquad r_B=[x_1,x_2]x_1^{p^m},
\]
the previously proposed \(\operatorname{Aut}(F)\)-orbit argument is unnecessary and too strong. The separation at the first window where the added tail becomes visible has a direct intrinsic certificate from abelianization.

Indeed, for \(n=p^m\), the added factor \(x_1^{p^m}\) lies in \(D_{p^m}(F)\), so
\[
W_{p^m}(G_A)\cong W_{p^m}(G_B).
\]
At \(n=p^m+1\), the abelianization of the free truncated quotient retains the class of \(x_1^{p^m}\):
\[
W_{p^m+1}(G_A)^{ab}\cong(\mathbf Z/p^{m+1})^4,
\]
whereas the relation for \(G_B\) imposes \(p^m x_1=0\), giving
\[
W_{p^m+1}(G_B)^{ab}\cong
\mathbf Z/p^m\oplus(\mathbf Z/p^{m+1})^3
\]
(up to the displayed choice of basis). Hence
\[
W_{p^m}(G_A)\cong W_{p^m}(G_B),qquad
W_{p^m+1}(G_A)\not\cong W_{p^m+1}(G_B).
\]
This is a valid **PASS / CLOSED Zassenhaus-critical higher-jet separation**.

However, it does not compare \(G_s(r)\) and \(G_t(r)\) for one fixed relation \(r\). It therefore does not close the exact unmarked same-window problem of the control family. Its significance is narrower: a finite window can intrinsically detect a higher filtered tail at its first visible degree, even when the quadratic initial form is unchanged.

The earlier claim that this proves or disproves recovery of the marked E_\psi parameter \(s\) is not valid. The marked parameter is target-indexed; the higher-tail degree \(m\) is a property of the chosen relator.


## 2026-10-04 — E_psi critical-separation audit correction

A proposed closure of the universal E_psi/abstract-separation branch was rejected.

- For (c\in D_3\setminus D_4) and (p^m>3), (D_{p^m}\subset D_3), so (c
otin D_{p^m}) in general. The claim that (r_A=[x_1,x_2]) and (r_B=r_Ac) define isomorphic (W_{p^m}) merely because (cin D_3) is false.
- More generally, (c\in D_k) gives equality of the two relator images modulo (D_k), but does **not** by itself give abstract non-isomorphism at (W_{k+1}).
- The attempted automorphism no-go is invalid: IA automorphisms can alter higher filtered terms while fixing the leading abelianization/graded data. A genuine orbit calculation is required.
- Therefore the proposed generic “(D_k)-jet implies (W_k) same and (W_{k+1}) different” theorem is **FAIL/CLOSED as stated**.
- The claim that the marked E_psi theorem has abstract content exactly equal to the quadratic invariant (B) is also not established. What is established is only markedness and the absence of a current intrinsic single-character bridge.

**Current boundary:** marked quadratic E_psi theorem = **PASS/CLOSED (marked)**; abstract unmarked same-window separation and recovery of (s) = **OPEN/LOAD-BEARING**. This restores the authoritative unresolved boundary and does not reopen the failed arbitrary-degree theorem.


## 2026-10-04 — new closed local result: d=3, p=3 cubic jet

The rank-2 quadratic control case \(r_2=[x_1,x_2]\) was independently audited at the next window.

- \(Q_3(r_2)=L_3/([r_2,V]+\operatorname{im}\Delta)\) has dimension 2, with representatives
  \(c_1=[x_3,[x_1,x_3]]\), \(c_2=[x_3,[x_2,x_3]]\).
- The stabilizer of \(e_1\wedge e_2\) has order 432 and acts on \(Q_3\) with exactly two orbits: zero and nonzero.
- For \(r_A=r_2\) and \(r_B=r_2c_1\),
  \[
  W_3(G_A)\cong W_3(G_B),\qquad
  W_4(G_A)\not\cong W_4(G_B).
  \]
  The \(W_4\) separation is certified by the cubic lower-central layer: dimensions 5 versus 4 over \(\mathbf F_3\).

Correction to the draft proof: \(\gamma_3^3\subseteq\gamma_4\) is false. The argument must be made through the \(D_4\)-quotient / mod-3 cubic layer, not integral \(L_3\).

Classification: **PASS / CLOSED**, but only for this specific \(d=3,p=3\), zero-vs-nonzero cubic-orbit comparison. It does not establish the general statement “distinct \(Q_3\)-orbits imply distinct \(W_4\)-isomorphism classes.”

The broad equivalence
\[
W_n\text{-iso}\iff \operatorname{Aut}(F/D_n)\text{-orbit of the truncated relator}
\]
remains **OPEN** and requires a separate lifting/Nielsen argument.

Immediate next target: generalize the cubic-layer calculation to arbitrary odd \(p\) and rank \(d\), starting with the intrinsic map from \(Q_3(r_2)\) to a \(W_4\)-isomorphism invariant.


## 2026-10-04 — correction: cubic Q3 result remains local; W4 separation reopened

The proposed \(d=3,p=3\) conclusion
\[
W_3(G_A)\cong W_3(G_B),\qquad W_4(G_A)\not\cong W_4(G_B)
\]
for \(r_B=r_2c_1\) was over-promoted.

The \(Q_3(r_2)\) calculation itself remains valid: \(\dim Q_3=2\), with zero/nonzero stabilizer orbits. But the claimed 5-versus-4 cubic lower-central dimensions are not valid because an inhomogeneous relation \(r_2+c_1\) has degree-2 initial form \(r_2\); \(c_1\) cannot simply be counted as an additional independent degree-3 relation.

Status:
- \(Q_3\) dimension/basis: **PASS / LOCAL**.
- non-removable cubic jet directions: **PASS / LOCAL**.
- zero/nonzero cubic orbit gives \(W_4\) non-isomorphism: **OPEN**.
- general \(Q_3\to W_4\)-classification: **OPEN / LOAD-BEARING**.

The next computation must target an invariant sensitive to the filtered extension class rather than the ordinary cubic associated-graded dimension.


## 2026-10-04 — Direction 2 ordinary mod-p cohomology blindness CLOSED

Direction 2 is **PASS / CLOSED** at theorem level for the declared odd-p stress family. For every s>=1, finite a>=1, and a=infinity, the power terms lie in the third p-Zassenhaus term, so the relator has the same quadratic commutator initial form. Quadrelli, arXiv:2011.03233v3, Proposition 2.1 gives the full ordinary mod-p cohomology algebra: it is quadratic, H^k=0 for k>=3, and the H^1 cup product is determined entirely by the common commutator form. Thus ordinary H^bullet(-,F_p) is completely blind to s and a, including the a=s versus a=infinity boundary.

This closes only the ordinary-cohomology route. It does not imply group-level or finite-window isomorphism, nor equality of Massey/Bockstein/A_infinity or filtered extension data. No further ordinary H^* computation is authorized as a route to the remaining finite-window boundary.

Authoritative audit: research/PAPER4_DIRECTION2_COHOMOLOGY_BLINDNESS_CLOSURE_2026-10-04.md.
