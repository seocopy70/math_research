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
