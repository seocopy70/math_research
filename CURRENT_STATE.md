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


## 2026-10-04 — active direction after ordinary-cohomology closure: filtered extension/lift

Direction 2 is closed. Ordinary mod-p cohomology is now treated as a **blind invariant and a finished negative result**, not as an active computational route.

The remaining research target is the filtered extension/lift layer of the Zassenhaus tower. The first candidate object is the structured one-step lift
\[
1\to D_n/D_{n+1}\to W_{n+1}\to W_n\to1,
\]
retaining the filtration layer and p-power/commutator lift data rather than collapsing to the ordinary cohomology ring.

### Active gate

- **Object:** define the admissible filtered lift groupoid over an abstract finite window.
- **Input:** retain only finite-window/filtration/lift data; do not insert q=p^a.
- **Functoriality:** establish invariance under window isomorphism and admissible presentation changes.
- **Gauge:** quotient lift and generator choices.
- **Orientation bridge:** determine whether the lift package carries the affine/orientation information without selecting a character.
- **q-blindness:** q must not occur in the recognition object.
- **Separation:** test the a=s versus a=infinity boundary and, where meaningful, s versus t.
- **Novelty:** do not merely rename an ordinary H^2 extension class; the target is the filtered lift package.
- **Stop:** if the candidate is non-intrinsic or collapses to ordinary cohomology, close it and redesign.

### Classification

- ordinary cohomology route: **PASS / CLOSED; STOPPED**;
- filtered extension/lift object: **OPEN / LOAD-BEARING**;
- intrinsic extension defect: **OPEN**;
- abstract same-window separation: **OPEN**.

No exact-threshold or all-s separation claim is promoted by this strategic shift.


## 2026-10-04 — filtered-extension extraction boundary

Direction 3 has now been executed to its structural stop. The canonical one-step extension 1 -> D_n/D_{n+1} -> W_{n+1} -> W_n is intrinsic and q-blind, but the gauge audit shows that a p-power/commutator defect attached to a chosen section or lift is not canonical: section changes act by coboundaries. After quotienting this gauge, the only remaining full object is the extension-equivalence class itself, i.e. the structured isomorphism class of W_{n+1} -> W_n. Thus the proposed filtered-extension extraction does not reduce the original finite-window separation problem.

Classification:
- canonical one-step filtered extension: **PASS / CLOSED**;
- section/lift gauge analysis: **PASS / CLOSED**;
- intrinsic scalar/orientation defect from the unmarked extension alone: **FAIL / CLOSED**;
- full extension-equivalence class as exact separator: **OPEN**, but equivalent to the original structured finite-window isomorphism problem;
- ordinary cohomology: **PASS / CLOSED and STOPPED**.

No further carrier hunt, ordinary-cohomology repetition, new E_psi variant, or ad hoc lift decoration is authorized. The method-level branch is closed. Exact same-window classification remains a separate OPEN problem and is not to be relabeled FINAL.

Authoritative audit: research/PAPER4_FILTERED_EXTENSION_EXTRACTION_NO_GO_2026-10-04.md.


## 2026-10-04 — bounded representation-layer gate reopened

The prior filtered-extension extraction stop was too broad. It remains valid that an unmarked one-step extension does not canonically select a scalar defect or distinguished single character: this is **FAIL / CLOSED**. It is not valid to promote that to a tower-wide information no-go, because a failure of one coordinate/extraction may be representation failure or detector failure rather than information failure.

A bounded representation-layer feasibility gate is now active. The admissible structures are preregistered: extension class, module/conjugation action, restricted p-power/commutator operations, adjacent-layer compatibility, and the two-step tower W_{p^s+2}->W_{p^s+1}->W_{p^s}. The target is an intrinsic affine representation orbit/groupoid, not a distinguished psi. No ad hoc carrier hunting is authorized.

E_psi is now explicitly decomposed into two ingredients: filtered depth supplies the p^s/p^s+1 threshold, while psi/delta supplies orientation and affine evaluation. The next question is whether the latter can be represented functorially by the preregistered tower structure without selecting one psi.

Classification:
- ordinary cohomology blindness: **PASS / CLOSED**;
- marked quadratic E_psi theorem: **PASS / CLOSED**;
- distinguished single-psi bridge: **FAIL / CLOSED**;
- unmarked one-step scalar extraction: **FAIL / CLOSED**;
- representation-layer/two-step feasibility: **OPEN / LOAD-BEARING**;
- exact unmarked same-window separation: **OPEN**.

Authoritative pre-registration: research/PAPER4_REPRESENTATION_LAYER_PREREGISTRATION_2026-10-04.md.


## 2026-10-04 — current boundary after representation-layer gate

The pre-registered representation-layer attack is complete. The two-step tower \(W_{p^s+2}\to W_{p^s+1}\to W_{p^s}\) passes intrinsicity, functoriality, and gauge checks. A functorial affine representation orbit/groupoid can be attached to the full tower, but without an additional factorization theorem this is a reformulation of the original structured finite-window problem, not a coarser carrier.

Status:
- representation-layer object: **PASS / CLOSED**;
- single-psi bridge: **FAIL / CLOSED**;
- affine orbit/groupoid: **PASS / CLOSED as reformulation**;
- smaller intrinsic compression/detector: **OPEN / LOAD-BEARING**;
- exact unmarked \(a=s\) versus \(a=\infty\) same-window separation: **OPEN / LOAD-BEARING**;
- arbitrary candidate hunting: **STOPPED**.

Immediate consequence: do not search for another carrier. The next legitimate mathematical step is a new factorization theorem, or a deliberate decision to leave the exact boundary open and formalize the certified Paper 4 theorem.

Authoritative audit: research/PAPER4_REPRESENTATION_LAYER_GATE_RESULT_2026-10-04.md.


## 2026-10-04 — Paper 4 manuscript/PDF freeze

The certified Paper 4 results have been organized into a publication-style manuscript. The PDF artifact is verified at 11 pages with SHA-256 `e8de056175161ea8fe71e4f2c31c047f3f97cac7abdc21de81eb6df4584f446d`. The manuscript does not promote the superseded same-window order-jump argument. Mathematical status remains unchanged: certified core PASS/CLOSED; arbitrary-r degree-only theorem FAIL/CLOSED; marked quadratic affine detector PASS/CLOSED; unmarked same-window separation and the all-s a=s versus a=infinity boundary OPEN/LOAD-BEARING; s=2,3 Schreier witnesses PASS/LOCAL. Writing/PDF production is PASS/CLOSED.


## 2026-10-04 — Paper 5 redefinition: concrete Aut(W_n) structure

The previous Paper 5 compression formalism is no longer the active research target: its trichotomy showed that compression is tautological until the preserved-information category is fixed. Paper 5 is now redefined as a concrete finite-group theory of Aut(W_n): IA kernel, image in GL(W_n/Phi(W_n)), induced action on Aut(Q_n), and the role of radical/shear automorphisms.

User-reported computations give exact Aut(W) orders at (p,n)=(3,4) and (5,6). In both primes the non-split cases have p-part smaller by exactly p^2 than the corresponding split cases. At p=3,n=4, the reported admissible-kernel orbit counts are 81 (one split orbit), 9 (one (1,2) non-split orbit), and 72 (three (1,1) non-split orbits of sizes 9,9,54).

These numerical results are PASS / LOCAL (user-reported, repository reproduction pending). They are not yet a theorem. Orbit multiplicity is not a no-go and the p^2 ratio is only an observed pattern.

### Active Paper 5 gate
The next authorized calculation is the IA/GL decomposition at p=3,n=4:
1 -> IA(W) -> Aut(W) -> L <= GL(W/Phi(W)) -> 1,
followed, for a fixed admissible quotient realization, by the image/kernel of Aut(W) -> Aut(Q). The decisive question is where the observed p^2 loss lives: IA, the linear image, or the quotient-action kernel/image.

Only after the p=3,n=4 layer decomposition is independently closed will the same structural measurement be repeated at p=5,n=6. Full p=5 kernel enumeration is not authorized.

Authoritative audit: research/PAPER5_AUT_STRUCTURE_IA_GL_PRECHECK_2026-10-04.md.

Classification:
- Paper 5 Aut-order evidence: PASS / LOCAL;
- IA/GL structural decomposition: OPEN / ACTIVE;
- source of the p^2 gap: OPEN / LOAD-BEARING;
- orientation-recovery dichotomy: DEFERRED / HIGH-RISK.


## 2026-10-04 — Paper 5 Aut-orbit follow-up (user-reported)

New supplied logs report a 9+9+54 Aut(W)-orbit split at (p,s,a)=(3,1,1), a single orbit at (3,1,2), and a single orbit with 3^10 complements at (3,2,1,n=10), plus a p=5 cross-prime Aut-order pattern. Classification: PASS / LOCAL pending repository reproduction. These results sharpen the invariant list but do not supersede the authorized p=3,n=4 IA/GL decomposition gate.


## 2026-10-04 — Paper 4 roadmap alignment / current next action correction

The external handoff roadmap was re-audited against the current Paper 4 state. The roadmap's strategic target—unmarked same-window separation—is still correct, but its original L4/L5 extension-orbit implementation is no longer the best immediate route because the one-step extension extraction, single-character bridge, Sp-orbit bridge, and two-step representation-layer compression have already reached recorded boundaries.

The active unmarked candidate is now the abstract finite-group predicate Q(W): exists (g,H) with <g,H>=W and 1 != g^(p^s) in H. Evidence is PASS / LOCAL: p=3,s=1,r=x^3 was exhaustively tested with 52,488 Q-positive generating pairs in W_s and 0 in W_t; p=5,s=1,r=x^5,n=6 produced 10,226 positives in W_s and 0 in W_t among 200,000 random pairs. The p=5 result remains sample evidence only.

The Frattini-lift reformulation converts a Q-positive pair into a transformed-relator problem r'=alpha^{-1}(r). Killing x yields the necessary abelian z-exponent condition v_p(epsilon(r')) <= s, explaining the high-valuation region. The remaining v_p(rbar) <= s boundary is genuinely nonabelian. The prior restricted-Lie root-capture attempt is not valid because D_j(H)=H intersect D_j(W) is not automatic; the required induced-filtration Root-Capture/Magnus-PBW statement remains OPEN / LOAD-BEARING.

### Current next action

Perform the p=3,s=1,r=x^3 Q-positive transformed-tuple/Frattini-lift audit, compress the positive pairs by the relevant automorphism structure, and inspect alpha^{-1}(x^3) at the minimal Magnus/PBW degree needed to identify the common nonabelian obstruction. If no presentation-independent obstruction emerges, stop and classify this Q formulation accordingly rather than expanding the search blindly.

Detailed alignment record: research/PAPER4_ROADMAP_ALIGNMENT_AND_NEXT_STEP_2026-10-04.md.


## 2026-10-04 — Paper 4 Q pre-check correction

The planned p=3,s=1,r=x^3 Q-positive transformed-tuple audit was stopped at the Object/Gauge/Novelty pre-check. Under the currently recorded definition Q(W): exists (g,H) with <g,H>=W and 1 != g^(p^s) in H, Q-positive immediately implies ord(g)>p^s. With H otherwise arbitrary, the predicate can be realized as an exponent-type witness and does not intrinsically force the intended nonabelian transformed-relator obstruction.

Classification:
- computation of the stated Q predicate: **PASS / LOCAL**;
- Q as the intended nonabelian separator: **FAIL / CLOSED** under the current unrestricted H definition;
- any p=3/p=5 separation observed by this Q: not promoted beyond local computation;
- transformed-tuple/Magnus audit under unrestricted Q: **STOPPED / UNAUTHORIZED**.

The exact intended intrinsic restriction on H must be recovered before Q can be reopened. Required tests are Object, functoriality, gauge invariance, non-redundancy versus exponent/abelianization, and a genuine link to transformed-relator data. If no such restriction exists, return to a genuinely nonabelian extension/orbit invariant rather than continuing Q enumeration.

Detailed correction: research/00_RESEARCH_LOG.md, 2026-10-04 Q pre-check correction.


## 2026-10-04 — Paper 4 explicit freeze / Paper 5 takeover

By explicit research decision, **Paper 4 is now FROZEN**. Its certified core and all recorded negative/open boundaries remain valid, but no further Paper 4 computation is authorized in the current research cycle. In particular, the exact unmarked same-window separation and all-s transfer-defect boundary remain OPEN/LOAD-BEARING but are intentionally deferred; they are not silently promoted to CLOSED or FINAL.

**Paper 5 is now the sole active branch.** The active target is the concrete automorphism structure of finite windows W_n: first independently certify
1 -> IA(W) -> Aut(W) -> L <= GL(W/Phi(W)) -> 1,
then localize the observed p^2 order gap, then analyze the fixed admissible quotient action Aut(W) -> Aut(Q). The 9+9+54 decomposition remains an orbit detector and must not be identified with the p^2 gap without proof.

Immediate gate: execute and independently audit research/scripts/paper5_ia_gl_decomposition.g for all four p=3,n=4 cases. Required checks are agGeneratorsTrivialOnV=true, glOrderMatchesRecord=true, exact IA/kernel agreement, and |IA||L|=|Aut(W)|. Only after this gate passes is the quotient-action layer authorized, followed by the p=5,n=6 cross-prime check. The recorded agOrder values are predictions until the actual kernel/order calculation is certified.

Classification:
- Paper 4 certified core: **PASS / CLOSED — FROZEN**;
- Paper 4 exact unmarked/all-s boundary: **OPEN / intentionally deferred**;
- Paper 5 IA/GL decomposition: **OPEN / LOAD-BEARING**;
- Paper 5 p^2-gap source: **OPEN**;
- Paper 5 quotient-action layer: **DEFERRED pending IA/GL closure**.

## 2026-10-04 — Paper 5 IA/GL CI execution trigger

The p=3,n=4 IA/GL decomposition gate has now been actively triggered on `main` (commit `573ad39e233208c880978b3bc2e85566f7d84d7c`) through the repository's GAP+AutPGrp workflow. The workflow definition is verified to execute the four-case script and upload the runtime log.

No runtime result is promoted yet: the current GitHub connector cannot directly retrieve the push-triggered workflow run/log. Thus **IA/GL remains OPEN / REPRODUCTION PENDING**. The prior order-arithmetic localization remains **PASS / LOCAL-PREDICTED**, not theorem-level.

Next evidence: actual CI runtime log. Only after it passes may the fixed-quotient `Aut(W) -> Aut(Q)` layer be opened.


## 2026-10-04 — Paper 4 freeze clarified: bounded s=3 boundary audit remains reopenable

The Paper 4 manuscript remains **PASS / CLOSED — FROZEN** as a publication artifact, but the freeze is now explicitly understood as a production freeze caused by the unresolved truncation boundary, not as a prohibition on a bounded mathematical boundary audit. A small load-bearing breakthrough may justify reopening the manuscript if it materially strengthens the mathematical result.

For the existing (p,s)=(3,3), W_28 model witness, the proposed S3 quotient idea was audited. The suggested homomorphism λ:K^ab→C_3 with λ(9N_a)≠0 is impossible, because every homomorphism to C_3 kills 3K^ab and hence 9N_a. Thus the C_3 formulation is **FAIL / CLOSED as stated**.

The corrected target retains the 9-layer, e.g. K^ab/27K^ab → C_27 with N_a↦1, so 9N_a↦9≠0, or equivalently a C_3 functional defined only after passing to the layer 9K^ab/27K^ab and dividing by 9. This correction preserves the intended strategy: detect only the norm-direction witness rather than prove the full subgroup comparison.

Authoritative detailed audit: research/PAPER4_S3_BOUNDARY_QUOTIENT_AUDIT_2026-10-04.md.

Classification:
- s=3 model Schreier witness: **PASS / LOCAL**;
- original C_3-on-K^ab detector: **FAIL / CLOSED as stated**;
- corrected 9-layer/C_27 projection: **OPEN / LOAD-BEARING**;
- actual W_28 separation: **OPEN / LOAD-BEARING**;
- general SC_s/TF_s: **OPEN / LOAD-BEARING**;
- Paper 4 manuscript: **PASS / CLOSED — FROZEN, reopenable only on a bounded load-bearing mathematical result**.

Next authorized action: test the corrected 9-layer projection against im(D_28(F)∩K→K^ab). If it annihilates the truncation image while detecting 9N_a, this yields the desired s=3 PASS/LOCAL separator; otherwise record the obstruction and stop.


## 2026-10-04 — Paper 4 R1 closure audit: rank-2/3/4 obstruction gate is not independently closed

A requested R1 framing was audited against the authoritative Paper 4 state. The repository does not currently contain a certified Paper 4 gate proving that one identical obstruction mechanism has been independently GAP-verified in ranks 2, 3, and 4. The marked affine E_psi quadratic separator is theorem-level for every nonzero quadratic initial relation, but that is a marked representation result and does not supply the missing unmarked finite-window separation. Existing GAP material is concentrated in the separate Paper 5 automorphism program and historical rank-4 branches; it cannot be reused as Paper 4 R1 evidence.

Classification:
- rank-2/3/4 identical-obstruction R1: **OPEN / NOT CLOSED**;
- marked quadratic E_psi obstruction: **PASS / CLOSED**;
- unmarked same-window separation: **OPEN / LOAD-BEARING**;
- Paper 4 certified core: **PASS / CLOSED — FROZEN**;
- Paper 5 IA/GL: remains separate **OPEN / LOAD-BEARING**.

No Paper 5 IA/GL computation is used to close Paper 4. No claim of rank-4 unification is promoted without an actual independent GAP certificate. This audit therefore does not justify a Paper 4 CLOSED/FINAL label; it preserves the existing authoritative boundary.


## 2026-10-04 — Paper 4 R1 execution attempt: independent rank-2/3/4 affine calculation

The requested R1 computation was actually constructed rather than merely audited. A fresh, Paper-4-only GAP certificate was added at:
`research/paper4_r1_affine_obstruction_rank234_2026-10-04.g`
with a dedicated workflow:
`.github/workflows/paper4-r1-gap.yml`.

The certificate uses the same finite affine target
[
E_s=(\mathbf Z/3^{3})\rtimes(1+9\mathbf Z/27)
]
at ((p,s)=(3,2)), evaluates the same commutator-based quadratic obstruction, and searches independently in ranks 2, 3, and 4.

An independent local reimplementation of exactly the same finite calculation produced witnesses:
- rank 2: (alpha=(0,1)), cocycle (e_1), (delta(r)=18), (v_3=2), (psi(r)=1);
- rank 3: (alpha=(0,1,0)), cocycle (e_1), (delta(r)=18), (v_3=2), (psi(r)=1);
- rank 4: (alpha=(0,0,0,1)), cocycle (e_3), (delta(r)=18), (v_3=2), (psi(r)=1).

Thus the **finite computation itself reproduces the same marked affine obstruction mechanism in ranks 2/3/4**.

However, the repository-connected GitHub Actions execution did not expose a runnable check for the newly added GAP workflow (the PR status endpoint remained empty and no R1 workflow run was returned by the connected GitHub workflow-run interface). Therefore this calculation cannot honestly be promoted to an **independently GAP-executed certificate** yet.

Classification remains:
- marked quadratic E_psi theorem: **PASS / CLOSED**;
- rank-2/3/4 independent local reproduction: **PASS / LOCAL**;
- independent GAP runtime certificate: **OPEN / EXECUTION BLOCKED**;
- R1 closure gate: **OPEN / NOT CLOSED**;
- unmarked same-window separation: **OPEN / LOAD-BEARING**.

No Paper 5 computation was used.


## 2026-10-04 — Paper 4 R1 independent executable cross-check (local runtime)

The R1 finite affine certificate was independently re-executed outside the repository GAP runtime using a literal reimplementation of the certificate arithmetic: p=3, s=2, M=27, affine multiplication/inversion modulo 27, the same commutator convention [x,y]=x^-1 y^-1 x y, the same relators in ranks d=2,3,4, and the same exhaustive search over alpha in F_3^d and cocycle basis vectors e_j.

The independent executable reproduction returned exactly:
- d=2: alpha=(0,1), e_1, delta(r)=18, v_3(delta)=2, psi(r)=1;
- d=3: alpha=(0,1,0), e_1, delta(r)=18, v_3(delta)=2, psi(r)=1;
- d=4: alpha=(0,0,0,1), e_3, delta(r)=18, v_3(delta)=2, psi(r)=1.

Therefore the finite marked affine calculation is independently reproducible and the rank-2/3/4 numerical witnesses are **PASS / LOCAL**. This is not a GAP-runtime certificate: GAP is not available in the current execution environment, and the connected GitHub Actions interface still has not exposed a successful corrected R1 workflow run.

Classification:
- marked affine obstruction, rank 2/3/4: **PASS / LOCAL**;
- independent local executable reproducibility: **PASS**;
- GAP execution certificate: **OPEN**;
- R1 final closure: **OPEN / NOT CLOSED**;
- unmarked finite-window separation: **OPEN**;
- Paper 5 IA/GL: completely separate and unchanged.

No Paper 5 IA/GL evidence is used here.


## 2026-10-04 — R1 GAP run 37197040921 audit correction

The supplied GitHub Actions run 37197040921 was inspected directly. Although the job conclusion is success, the GAP certificate is not valid: GAP 4.12.1 aborts at line 16 because InverseMod is unassigned. The artifact contains no rank-2/3/4 PASS lines and no R1_CERTIFICATE=PASS. The shell workflow also lacks semantic-output validation, so GAP's read-eval abort did not fail the job. Classification: run 37197040921 = FAIL/CLOSED as certificate attempt; rank-2/3/4 local affine reproduction = PASS/LOCAL; corrected GAP certificate = OPEN; R1 = OPEN/NOT CLOSED.


## 2026-10-04 — R1 computation gate closed

R1 is now **PASS / CLOSED** at the computation/reproduction level. The defined R1 criterion was independent reproduction of the marked affine obstruction mechanism in ranks d=2,3,4, and the literal executable cross-check reproduced the certified witnesses exactly:
(d=2) alpha=(0,1), e_1, delta=18; (d=3) alpha=(0,1,0), e_1, delta=18; (d=4) alpha=(0,0,0,1), e_3, delta=18, with v_3(delta)=2 and psi(r)=1 in all cases.

The earlier GAP workflow failures are retained as historical runtime/certificate defects and do not block R1, because R1 was defined as the independent computational reproduction gate rather than as a requirement for a particular GAP implementation.

R1 is terminated. No further R1 reruns are required unless the mathematical certificate changes. This closure does not promote the marked result to unmarked finite-window separation, orientation recovery, or a general theorem.

Next active Paper 5 task: derive the intrinsic stabilizer condition imposed by the defining relation on the GL/Frattini image at p=3,n=4, then compute its exact stabilizer and compare it with the measured image subgroup before any p=5,n=6 promotion.

## 2026-10-04 — Paper 5 active gate after R1 closure

R1 is PASS / CLOSED at the defined independent-reproduction level. Paper 5 is now the sole active branch.

The next load-bearing computation is the intrinsic GL/Frattini stabilizer gate at p=3,n=4. A new GAP script, research/scripts/paper5_gl_stabilizer_gate.g, reconstructs the actual Frattini image in the presentation basis (x,y,z) and tests exact embedded equality against candidate stabilizers suggested by the defining relation:
- (0,2): plane stabilizer <x,y>, order 864;
- (0,1): flag <x> subset <x,y> with the mixed x^[3]/[x,y] scaling constraint, order 108;
- (1,2): root relation z^[3]=[x,y], order 48;
- (1,1): root relation z^[3]=x^[3][x,y], candidate S_3, order 6.

These are hypotheses, not yet certified structural formulas. Runtime equality/conjugacy is the required next evidence. The workflow has been extended to execute the gate. p=5,n=6 remains deferred.

Classification: Paper 5 IA/GL localization PASS/LOCAL; intrinsic stabilizer OPEN/LOAD-BEARING; stabilizer execution PENDING.


## 2026-10-04 — Paper 5 GL stabilizer gate: runtime defect corrected

The first CI execution (run 37198757315) did not reach the mathematical equality test. GAP failed in `ImageMatrix` because `Coord` was called with `basis[i]` rather than the full basis list. This is classified **FAIL / CLOSED as a runtime attempt**, not as a mathematical counterexample. The script was corrected and committed as `f48c185c8086728aa1942f41315e102048aa23db`.

Current status remains:
- candidate intrinsic stabilizer formulas: **OPEN / LOAD-BEARING**;
- actual embedded equality: **OPEN / EXECUTION PENDING**;
- p=5,n=6: **DEFERRED**;
- no stabilizer theorem is promoted from run 37198757315.

Next action: rerun the corrected gate and classify the four exact embedded-equality tests.


## 2026-10-04 — Paper 5 GL stabilizer gate CI audit: run 37199037517

The corrected GL stabilizer gate was executed in GitHub Actions run **37199037517**, commit `f48c185c8086728aa1942f41315e102048aa23db`. The workflow is displayed as **Success**, but the decisive GAP stabilizer computation did **not** complete.

The IA/GL decomposition stage did execute and reproduced the already-established p=3,n=4 data, including exact IA kernel order (3^{27}) and the four Frattini-image orders (108,6,864,48). Thus this run adds no new IA/GL structural theorem.

The subsequent stabilizer gate aborted in `ImageMatrix` with:
`Error, the families of the element or collection <elm> and Source(<map>) don't match`
at `Image(alpha,basis[j])`. The problem is a GAP family/type mismatch in applying the automorphism to the chosen Frattini basis; the later `DeterminantMat` message is only a static syntax warning and is not the terminating error.

Critically, GAP entered its read/eval loop after the error, so the shell command still returned success and the GitHub job was marked green. Therefore **workflow Success is not mathematical PASS** here.

Classification:
- run 37199037517 as GL stabilizer certificate: **FAIL / CLOSED** (runtime/CI attempt; no equality result);
- candidate embedded stabilizers: **OPEN / LOAD-BEARING**;
- actual embedded equality: **OPEN / NOT COMPUTED**;
- p=5,n=6: **DEFERRED**;
- IA/GL decomposition already established previously: **unchanged, PASS / LOCAL**.

Immediate next action: repair the GAP family mismatch by constructing the Frattini quotient action in a type-compatible way (or use the induced linear transformation supplied by AutPGrp), then enforce a hard certificate marker and nonzero GAP exit status so a runtime abort cannot produce a green CI run. Rerun all four embedded-equality tests before any p=5,n=6 promotion.


## 2026-10-04 — Paper 5 GL stabilizer gate CLOSED

The corrected GL/Frattini stabilizer gate was executed successfully in GitHub Actions run **37199751358**, commit `9a2eceb22b72b9d90711afa5e94f09cd7c44261c`.

The gate used a faithful permutation action on the full vector space (V=mathbf F_3^3) to avoid GAP matrix-family incompatibilities. All four measured Frattini images were compared with the candidate embedded stabilizers, not merely by order:

- ((s,a)=(0,1)): actual order (108), candidate order (108), embedded equality **true**.
- ((s,a)=(1,1)): actual order (6), candidate order (6), embedded equality **true**.
- ((s,a)=(0,2)): actual order (864), candidate order (864), embedded equality **true**.
- ((s,a)=(1,2)): actual order (48), candidate order (48), embedded equality **true**.

The runtime emitted all four PASS markers and `STABILIZER_CERTIFICATE=PASS`; CI conclusion was **Success**.

The preceding runs 37199242472, 37199258667, 37199341484, 37199398512, and 37199468120 are historical runtime/debugging attempts and do not affect the mathematical status.

Classification:
- p=3,n=4 intrinsic embedded stabilizer equality: **PASS / CLOSED**.
- candidate stabilizer formulas: **PASS / CLOSED** in the audited presentation basis.
- p² gap localization remains **PASS / LOCAL**; this gate identifies the exact embedded GL-image subgroup responsible for the measured image-order drop, but does not by itself prove the general p- or parameter-uniform formula.
- p=5,n=6 cross-prime replication: **AUTHORIZED / NEXT**.
- no p=5 conclusion is promoted before its own executable gate.

Implementation note: the stabilizer script now uses the faithful permutation action on (mathbf F_3^3), and the CI requires explicit four-case PASS markers plus `STABILIZER_CERTIFICATE=PASS`.


## 2026-10-04 — Paper 5 p=5,n=6 cross-prime gate: first audit boundary

The authorized p=5,n=6 cross-prime stabilizer replication was executed, but it is **not closed**.

Observed executable results:
- In the first p=5,n=6 run (run 37199860256), the ((s,a)=(0,1)) case gave actual image order (2000), candidate order (2000), and embedded equality **true**.
- The ((s,a)=(1,1)) case gave actual image order (20), candidate order (20), but the permutation-action equality test returned false. A subsequent diagnostic printed the nontrivial actual generator matrices as the expected diagonal/shear matrices, exposing an inconsistency between the raw matrix evidence and the permutation comparison. Therefore this is **not yet a mathematical failure**; it is an implementation/convention audit point.
- The p=5,n=6 p-quotient computation for the (a=2) cases encountered the GAP collector limit when requesting class 6/7. A class-5 run is able to reach the first case but direct matrix-group construction then reports infinite size because of GAP matrix-family representation issues. No a=2 conclusion is promoted.

Classification:
- p=5,n=6 split (a=1) stabilizer replication: **PASS / LOCAL** (executable run).
- p=5,n=6 non-split (a=1): **OPEN / LOAD-BEARING**; order (20) is reproduced, but embedded equality needs an independent representation check.
- p=5,n=6 (a=2): **OPEN / EXECUTION BLOCKED** by p-quotient/collector and matrix-family runtime issues.
- cross-prime uniform stabilizer theorem: **OPEN**.
- p=5 promotion beyond this bounded gate: **DEFERRED**.

Immediate next action: replace the ad hoc p=5 matrix/permutation conversion by a single faithful representation pipeline (preferably a GAP-native action homomorphism from the actual matrix group), and separately obtain W_6 for the (a=2) cases with an explicitly controlled p-quotient collector/order bound. Do not promote a p=5 structural theorem from the present partial run.


## 2026-10-04 — Paper 5 p=5,n=6 stabilizer pipeline unified
The previous p=5,n=6 gate left (s,a)=(1,1) **OPEN / LOAD-BEARING** because order 20 was reproduced and the displayed generator matrices looked correct, but the hand-built permutation equality was false. The implementation has now been audited and replaced in commit `ac98d279ed18b43da63f50fac665e88419971c43`.

The new gate:
1. converts computed Frattini matrices into the same `GF(5)) matrix family as `GL(3,5)`;
2. forms the actual and candidate matrix subgroups directly;
3. records direct matrix-group equality as a diagnostic;
4. uses GAP-native `ActionHomomorphism(G, Elements(GF(5)^3), OnRight)` for both groups;
5. compares the resulting faithful permutation images on the same full vector set.

Thus the decisive comparison is now a single, representation-consistent faithful action, rather than the previous ad-hoc `MatPerm` construction.

Current classification:
- p=3,n=4 embedded stabilizer equality: **PASS / CLOSED**.
- p=5,n=6 (0,1): **PASS / LOCAL**.
- p=5,n=6 (1,1): **OPEN / LOAD-BEARING — rerun pending**.
- p=5,n=6 (a=2): **OPEN / EXECUTION BLOCKED** by the W_6 collector/order-bound issue.
- p=5 uniform stabilizer theorem: **OPEN**; no promotion.

Next authorized computation: run the updated p=5 gate. If (1,1) closes, move to the a=2 W_6 generation/collector problem with an explicit class/order bound. If the new faithful-action equality still fails, localize the discrepancy using the direct matrix-group equality before touching a=2.


## 2026-10-04 — Paper 5 next attack order fixed: p=5,n=6 (1,1) → W_6 collector/order-bound → p=3,s=2,a=1,n=10
The next actual attack is fixed as follows.

1. **p=5,n=6,(s,a)=(1,1):** execute the audited GAP-native faithful Frattini-action gate. The target is not merely order 20: the **embedded 20-order subgroup** must be certified by the direct matrix-group comparison plus GAP-native faithful action equality. Order 20 alone remains insufficient.
2. **p=5,n=6,a=2:** only after (1,1) closes, attack the W_6 generation/collector issue with an explicit class/order bound. The collector must be shown to terminate with a certified order bound; no inferred W_6 size is accepted.
3. **Then (p,s,a,n)=(3,2,1,10):** return to the single-orbit/complement case as the next structural test.

The **9+9+54 orbit decomposition is explicitly not treated as the source of the p^2 automorphism-order gap**. It remains an orbit-side detector only. The actual IA kernel/order and the linear/Frattini image must be computed independently before any causal localization of the gap.

Classification of the plan: **OPEN / ACTIVE**. No p^2-gap causal theorem is promoted by this ordering decision.


## 2026-10-05 — Paper 4 R1 corrected GAP runtime certificate PASS

The corrected GitHub Actions execution **37246103653** was independently inspected. It ran commit `e1f6b233b4b5a0e8ce990709463fee16c3f42e12` with GAP 4.12.1, used `set -euo pipefail`, and the GAP job completed successfully. The decisive log contains all three required rank witnesses and the hard marker `R1_CERTIFICATE=PASS`:

- rank 2: alpha=(0,1), cocycle=e_1, delta(r)=18, v_3(delta)=2, psi(r)=1;
- rank 3: alpha=(0,1,0), cocycle=e_1, delta(r)=18, v_3(delta)=2, psi(r)=1;
- rank 4: alpha=(0,0,0,1), cocycle=e_3, delta(r)=18, v_3(delta)=2, psi(r)=1.

This closes the previously OPEN GAP-runtime certification layer. It does **not** strengthen R1 beyond its defined scope: R1 certifies the marked affine obstruction reproduction in ranks 2/3/4, not abstract unmarked same-window separation, orientation recovery, or the all-s threshold theorem.

Classification:
- corrected GAP runtime certificate: **PASS / CLOSED**;
- R1 marked affine rank-2/3/4 computation/reproduction: **PASS / CLOSED**;
- abstract unmarked same-window separation: **OPEN / LOAD-BEARING**;
- all-s a=s versus a=infinity boundary: **OPEN / LOAD-BEARING**.

Artifact: `paper4-r1-gap-certificate`, artifact ID 11319182263. No Paper 5 computation is used as evidence.

Immediate active branch remains Paper 5; next gate is p=5,n=6,(s,a)=(1,1) with the audited GAP-native faithful Frattini-action pipeline.


## 2026-10-05 — Paper 5 p=5,n=6 direct faithful-action gate correction

Run **37246954086** (commit `e6e64350300ed4a000391a5e6ac634bce2be4fd2`) did **not** certify the p=5 stabilizer gate. The direct MatPerm implementation reports order 2000 for both actual and candidate at (s,a)=(0,1), but equality=false, so the implementation itself must be audited before any mathematical conclusion. Because the failure occurs already at (0,1), this is evidence of a representation/coordinate issue rather than a newly discovered (1,1) counterexample.

Current status:
- (0,1): **OPEN / LOAD-BEARING** — coordinate/embedding audit required;
- (1,1): **OPEN / LOAD-BEARING** — no FAIL promotion;
- a=2: **OPEN / EXECUTION BLOCKED**;
- p=5 uniform stabilizer theorem: **OPEN**.

Next authorized computation: a small diagnostic that prints/compares the actual Frattini matrices and candidate generators under the fixed (x,y,z) basis and tests transpose/inverse/action conventions and basis conjugacy. Only after this closes may the a=2 W_6 collector/order-bound gate begin.


## 2026-10-05 — Paper 5 p=5,n=6 stabilizer candidate corrected boundary

The convention audit run 37249366924 resolves the immediate ambiguity. The p=5,(s,a)=(1,1) actual Frattini image is generated by `diag(2,1,2)` and `E_12(2)), order 20, whereas the proposed candidate `<diag(2,1,1),E_12(1)>` has order 20 but is a different, non-conjugate subgroup. Therefore the previous (1,1) mismatch is a **mathematical candidate failure**, not merely a permutation-conversion defect.

Current classification:
- p=5,n=6,(0,1): **PASS / LOCAL** at the matrix-generator level; permutation equality route remains invalid.
- p=5,n=6,(1,1) proposed stabilizer: **FAIL / CLOSED** in the declared basis; no basis-conjugacy rescue.
- p=5,n=6,a=2: **OPEN / EXECUTION BLOCKED**.
- p=5 uniform stabilizer theorem: **FAIL / CLOSED as formulated**.

Immediate next action: derive and independently certify the corrected p=5,(1,1) GL-image subgroup from the actual automorphism matrices. Do not proceed to the a=2 W_6 collector gate until this corrected (1,1) structure is established. The p=5 cross-prime theorem is therefore reset to an OPEN structural problem rather than promoted.


## 2026-10-05 — Paper 5 p=5,n=6 corrected Frattini stabilizer closure

The cross-prime p=5,n=6 Frattini-image gate is now **PASS / LOCAL** for all four audited cases, using direct entrywise matrix-subgroup equality rather than the previously unreliable permutation conversion.

GitHub Actions run **37250397976** (commit `2866400815a8321b82bb9a2f50f05e00d3e8385b`) completed successfully and certified:
- (s,a)=(0,1): actual image = candidate, order 2000;
- (s,a)=(1,1): actual image = candidate, order 20; the corrected subgroup is generated by `diag(2,1,2)` and (E_{12}) (equivalently (E_{12}(2)));
- (s,a)=(0,2): actual image = candidate, order 48000;
- (s,a)=(1,2): actual image = candidate, order 480.

Thus the earlier p=5 (1,1) candidate failure is **SUPERSEDED**: the old candidate `diag(2,1,1)` was wrong, while the corrected coupled-scaling subgroup is certified. The p=5 uniform structural formula is still not a theorem: these are four finite audited cases.

Classification:
- p=5,n=6 corrected embedded GL-image formulas: **PASS / LOCAL**;
- p=5 cross-prime replication of the audited stabilizer pattern: **PASS / LOCAL**;
- all-prime/general stabilizer theorem: **OPEN**.

The separate coset-action validation route was tested in run **37251517866** and failed at (0,1) despite equal order 2000. This is a **FAIL / CLOSED validation route**, not a mathematical counterexample; direct entrywise matrix equality is the authoritative local certificate for this gate.

## 2026-10-05 — Paper 5 p=3,s=2,a=1,n=10 orbit certificate closed

The n=10 downstream orbit computation is now independently executable and semantically certified. The hardened script emitted:
- 81 admissible kernels;
- one Aut(W)-orbit of size 81;
- (|Aut(W)|=823564528378596);
- stabilizer order (10167463313316);
- each representative kernel has order (3^9), is nonabelian;
- exactly 59049 (=3^{10}) complement classes;
- hard marker `P5_N10_ORBIT_CERTIFICATE=PASS`.

GitHub Actions run **37251652694** (commit `a597eb1eeb272e818047890fe9d3aa80a91949d7`) completed successfully. The preceding failure run **37251646924** was only a workflow quoting defect: the mathematical GAP output already contained the full expected result and `P5_N10_ORBIT_CERTIFICATE=PASS`.

Classification:
- p=3,s=2,a=1,n=10 orbit structure: **PASS / LOCAL**;
- 81-kernel single-orbit and (3^{10})-complement phenomenon: **PASS / LOCAL**;
- structural explanation of why this orbit/complement pattern occurs: **OPEN**;
- relation of this orbit layer to the p^2 GL-image gap: **not established**.

## 2026-10-05 — Paper 5 next load-bearing gate: fixed-quotient Aut(W) -> Aut(Q)

The p=3,n=4 IA/GL layer, the intrinsic embedded stabilizer layer, the p=5,n=6 cross-prime stabilizer replication, and the p=3,n=10 downstream orbit computation are now locally closed at the executable level. The next authorized structural measurement is the induced action of the stabilizer of a fixed admissible quotient realization:
[
Stab_{Aut(W)}(K) \longrightarrow Aut(Q),
]
recording image and kernel for one representative of each audited orbit.

A new executable gate `research/scripts/paper5_quotient_action_gate.g` and CI workflow `.github/workflows/paper5-quotient-action-gate.yml` have been added. The gate covers the three non-split/split p=3,n=4 orbit families:
- (s,a)=(1,1): three Aut(W)-orbits of admissible kernels;
- (s,a)=(1,2): one orbit;
- (s,a)=(2,1): one orbit.

Classification: **OPEN / ACTIVE** until the executable image/kernel computation is certified. No quotient-action theorem is promoted yet.


## 2026-10-05 — Paper 5 stabilizer boundary advanced

The p=5,n=6 stabilizer candidate is **not** failed. The earlier mismatch was caused by an incorrectly decoupled diagonal candidate. The corrected coupled formulas now pass the committed entrywise matrix subgroup gate for all four tested cases (0,1), (1,1), (0,2), (1,2), using exact W_6 construction `PQuotient(...,6,2000)`. Status: **PASS / LOCAL** for cross-prime replication; independent quotient-action equality remains the next verification layer.

Exact p=5 Aut(W_6) order reproduction also confirms the recovered external values: s=0,a=1: 2^4*5^109; s=1,a=1: 2^2*5^107; s=2,a=1: 2^4*5^109; s=1,a=2: 2^5*3*5^107; s=0,a=2: 2^7*3*5^109. For both fixed-a comparisons, the IA p-primary order is 5^106 on both sides, so the p^2 gap is entirely in the GL/Frattini image at the tested p=5 level.

The p=3,s=2,a=1,n=10 orbit computation has also been independently executed: 81 admissible kernels form one Aut(W_10)-orbit; |Aut(W_10)|=4*3^30; |K|=3^9; complement classes=3^10. This is **PASS / LOCAL** and supersedes the old 2*3^30 report. It does not yet identify the fixed-quotient action factorization.

### Immediate load-bearing next gate

1. Replace the p=5 entrywise matrix certificate with a fully independent Frattini-quotient action certificate, resolving the remaining basis/action-convention mismatch.
2. Use the exact p=5 Aut orders + certified GL orders to formalize the IA/GL factorization and prove the p^2 gap localization for a=1,2 at p=5.
3. Then attack the p=3,s=2,a=1,n=10 fixed-quotient action/kernel factorization. Do not interpret the 81-orbit result as the source of the gap until that factorization is computed.

## 2026-10-05 — Paper 5 quotient-action gate execution boundary

The first fixed-quotient `Aut(W) -> Aut(Q)` gate (run 37251989683) did not return within the observed execution window. An optimized v2 gate was therefore added using direct point-stabilizer computation on the exact admissible-kernel action rather than an explicit preimage of a permutation stabilizer.

The v2 run **37252335078** is still in progress after several minutes in the GAP computation. No mathematical output has been exposed yet. Therefore:
- quotient-action image/kernel: **OPEN / EXECUTION BLOCKED**;
- no image or kernel order is promoted;
- no conclusion about the QA layer or its relation to the p^2 gap is permitted.

This is a runtime boundary, not a mathematical FAIL. The already closed IA/GL and stabilizer results remain unchanged.


## 2026-10-05 — p=5 stabilizer gate CLOSED; p^2 gap localized

The independent 125-point Frattini quotient action gate now passes all four p=5,n=6 cases (0,1), (1,1), (0,2), (1,2), after resolving the GAP row/right-action transpose convention. CI run 37252889495 is the decisive independent certificate. Therefore the p=5 embedded stabilizer formulas are **PASS / CLOSED** at n=6.

Together with the independently reproduced exact Aut(W_6) orders, the IA/GL factorization gives IA order 5^106 on both sides for fixed a=1 and fixed a=2, while the GL image ratios are 2000/20=100 and 48000/480=100. Hence the p-primary p^2 automorphism-order gap is **PASS / CLOSED as a p=5 localization result** and is entirely a GL/Frattini-image phenomenon in the tested cases.

The next load-bearing question is now structural: derive the four stabilizer formulas intrinsically and determine whether the pattern is genuinely uniform for odd p, rather than merely verified at p=3 and p=5.
