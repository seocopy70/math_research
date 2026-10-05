# Research Log — Active/Post-Paper-3 Chronology

> **Scope:** This chronological ledger is for active research after Papers 1–3 were frozen. Papers 1–3 historical provenance is indexed at `research/archive/PAPERS1-3_RESEARCH_HISTORY.md` and remains in their dated proof/audit records. Do not re-copy frozen Paper 1–3 history into this file.

## 2026-10-04 — TF_s literature review and subgroup-comparison correction

A direct re-check was performed after the transfer-defect reduction identified the load-bearing lemma
\[
(TF_s):\quad \operatorname{im}(D_{p^s+1}(F)\cap K\to K^{ab})\subseteq p^sK^{ab},
\]
with the proposed sufficient comparison
\[
(SC_s):\quad D_{p^s+1}(F)\cap K\subseteq D_{p^{s-1}+1}(K).
\]

### Direct-proof audit

1. The augmentation-ideal shortcut \(I_F^n\cap\mathbf F_p[K]=I_K^n\) is **FAIL / CLOSED**. The example \(F=\mathbf Z, K=p\mathbf Z\) gives \(t^p-1\in I_F^p\cap\mathbf F_p[K]\) but \(t^p-1\notin I_K^2\).
2. The stronger-looking inclusion \(D_n(F)\cap K\subseteq D_n(K)\) is also **FAIL / CLOSED** by the same example: \(D_2(F)\cap K\) contains \(t^p\), whereas \(t^p\notin D_2(K)\).
3. Jennings recursion does not close \((SC_s)\): writing an element of \(D_{p^s+1}(F)\cap K\) as a product involving a \(p\)-th power from \(D_{p^{s-1}+1}(F)\) does not imply that the preimage factor lies in K.

### Literature audit

Shalev's Proposition 1.2, as located in the cited 1990 literature, concerns identities built from the filtration of a **single group G**. It does not, on the currently verified evidence, state the required index-\(p\) intersection comparison \(D_{pn}(F)\cap K\subseteq D_n(K)\), nor its special case \((SC_s)\). The Shalev result therefore remains **PASS as a literature fact but NOT DIRECTLY APPLICABLE** to the missing bridge.

The Lazard product formula
\[
D_n(G)=\prod_{ip^j\ge n}\gamma_i(G)^{p^j}
\]
and the corresponding Jennings recursion remain **PASS**. Consequently, once \((SC_s)\) is supplied, the implication
\[
D_{p^s+1}(F)\cap K\subseteq D_{p^{s-1}+1}(K)
\Longrightarrow
\operatorname{im}(D_{p^s+1}(F)\cap K\to K^{ab})\subseteq p^sK^{ab}
\]
is valid.

### Classification

- augmentation-ideal intersection equality: **FAIL / CLOSED**;
- same-index Zassenhaus intersection inclusion: **FAIL / CLOSED**;
- Jennings-only proof of \((SC_s)\): **FAIL / CLOSED as an approach**;
- Shalev Proposition 1.2: **PASS / LOCAL, not directly applicable**;
- \((SC_s)\): **OPEN / LOAD-BEARING**;
- \((TF_s)\): **OPEN / LOAD-BEARING**;
- all-s transfer-defect separation: **OPEN / LOAD-BEARING**;
- Paper 4 final freeze: **BLOCKED** by this missing bridge (or an alternative direct proof of \((TF_s)\).

### Governance correction

An earlier 2026-10-04 log entry labeled the intrinsic transfer-defect boundary "CLOSED". That label is **superseded**. The verified status is only **PASS / LOCAL** for the \((p,s)=(3,2)\) witness and **OPEN / LOAD-BEARING** for the all-s theorem. No all-s claim is to be promoted from the local witness.

The most defensible fallback is now a **CONDITIONAL** Paper 4 statement: if \((SC_s)\) or directly \((TF_s)\) is certified, then the transfer-defect calculation closes the remaining a=s vs. a=∞ boundary.


## 2026-10-04 — Restricted-Lie TF_s proof audit: proposed induction rejected

A new proposed proof of
\[
(TF_s):\quad \operatorname{im}(D_{p^s+1}(F)\cap K\to K^{ab})\subseteq p^sK^{ab}
\]
was audited and is **NOT VALID**. The Paper 4 certified core remains closed, but this argument does **not** close the all-s boundary.

### Independent audit findings

1. **Wrong graded object / restricted structure.** The lower-central-series graded object \(\bigoplus_i\gamma_i(F)/\gamma_{i+1}(F)\) is the ordinary free Lie algebra in the free-group case; the standard free restricted Lie algebra belongs to the Zassenhaus/dimension filtration, not the lower-central grading used in the proposal. Thus the asserted restricted-Lie setup is not legitimate as stated.

2. **Ambient \(\gamma_i(F)\) versus \(\gamma_i(K)\) mismatch.** The target concerns \(c\in\gamma_i(F)\subseteq K\), but the induction actually controls images of \(\gamma_i(K)\) (or its associated graded pieces). These are not the same filtration. In particular \([z,x]\in\gamma_2(F)\cap K\) is generally a Schreier degree-1 generator for \(K\), not an element of \(\gamma_2(K)\). Hence the claimed generation of the relevant \(\gamma_i(F)\)-image by \([z,\mathcal L_{K,i-1}]\), \([x,\mathcal L_{K,i-1}]\), \([y,\mathcal L_{K,i-1}]\) is not a proof of the stated ambient-filtration bound.

3. **Base cases are not enough to repair the mismatch.** The explicit \(i=4,5\) computations may verify particular cyclic-commutator witnesses, but they do not establish the full image of \(\gamma_i(F)\cap K\to K^{ab}\).

4. **The Zassenhaus implication is not reversible in the way used.** From \(c\in\gamma_i(F)\) and \(c^{p^j}\in D_{p^s+1}(F)\), membership in \(D_{p^s+1}\) does not by itself force \(ip^j\ge p^s+1\); an element of \(\gamma_i(F)^{p^j}\) can have strictly larger Zassenhaus weight. The displayed proof therefore cannot use that implication as a general deduction.

5. **Therefore the central bound**
\[
\operatorname{im}(\gamma_i(F)\cap K\to K^{ab})\subseteq p^{\lceil i/p\rceil-1}K^{ab}
\]
remains **UNPROVEN**. The numerical cyclic examples are **PASS / LOCAL**, not an induction theorem.

### Classification

- restricted-Lie induction as written: **FAIL / CLOSED as a proof route**;
- proposed \(\gamma_i(F)\)-to-\(K^{ab}\) divisibility bound: **OPEN / LOAD-BEARING**;
- \((TF_s)\): **OPEN / LOAD-BEARING**;
- all-\(s\) transfer-defect separation: **OPEN / LOAD-BEARING**;
- Paper 4 certified core: **PASS / CLOSED**;
- Paper 4 all-\(s\) boundary: **OPEN**, so no FINAL/all-\(s\) promotion.

This entry supersedes any session-level claim that the restricted-Lie induction had proved \((TF_s)\). No all-\(s\) theorem is to be recorded from this argument.


## 2026-10-04 — s=3 model Schreier transfer witness

The remaining Paper 4 boundary (a=s) versus (a=\infty) was advanced by a bounded ((p,s)=(3,3)), (n=28) Schreier-lattice calculation. With the corrected intrinsic radical character \(\chi(z)=1,\chi(x)=\chi(y)=0\), the untruncated Schreier abelianization has relations \(9u-27a_i=0\). The critical model class
\[
9(\sigma-1)^2a_0=9a_0-18a_1+9a_2
\]
is not in the integral row lattice (SNF \(\operatorname{diag}(9,27,27)\)); hence the model class is nonzero. This extends the \(s=2\) local pattern to \(s=3\).

This is **PASS / LOCAL only**. It does not prove survival in the actual \(K^{ab}\) of \(W_{28}\), because the truncation image \(D_{28}(F)\cap K\to K^{ab}\) is still controlled by the unresolved subgroup-filtration comparison \((SC_s)\) (or a direct replacement). The next authorized attack is therefore the actual truncation image at \((p,s)=(3,3)\), not an all-\(s\) promotion.

Evidence: `research/PAPER4_S3_MODEL_SCHREIER_TRANSFER_2026-10-04.md`, commit `f423bc41f7d41023fdeaf5e8de657229118e338a`.


## 2026-10-04 — same-window order-jump correction / exact-threshold rollback

A direct audit of the previously “CLOSED” same-window order-jump argument found a fatal subgroup-containment error. The proposed canonical epimorphism
\[
W_{p^s+1}(G_s)\twoheadrightarrow W_{p^s+1}(G_t)
\]
was justified by treating the defining normal subgroups as nested, but
\(N_s=D_n\langle\!\langle z^{p^s}r^{-1}\rangle\!\rangle\) and
\(N_t=D_n\langle\!\langle r\rangle\!\rangle\) are not nested in the required direction because \(z^{p^s}\notin D_{p^s+1}\). Hence the claimed order jump \(|W_s|=p|W_t|\) is invalid.

A direct finite computation at the test case reported in the audit gives equal orders for the two compared windows, consistent with the structural objection. Therefore:

- “same-window order jump” = **FAIL / CLOSED as a proof route**;
- exact unmarked threshold \(n_{\mathrm{sep}}(s)=p^s+1\) = **OPEN**;
- certified lower bound \(n_{\mathrm{sep}}(s)\ge p^s+1\) = **PASS / CLOSED in the stated scope**;
- all-s same-window separation = **OPEN / LOAD-BEARING**;
- the existing \((p,s)=(3,2)\) and \((3,3)\) transfer calculations remain **PASS / LOCAL** only;
- a proof that \(G_s\not\cong G_t\) is also not currently certified and must not be inferred from the window calculation.

This supersedes the earlier evidence-index wording that promoted the exact threshold to CLOSED. It does not invalidate the certified Paper 4 core below this boundary.


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

The certified Paper 4 core is mathematically real but judged too narrow relative to the original generalization ambition. A bounded **test-family generalization challenge** is therefore authorized before organization/writing.

This does not reopen the failed arbitrary-(r) degree-only theorem, the frozen core, or Paper 5 compression. The first broader family is
[
G_{s,a}(r_2)=langle z,x_1,ldots,x_dmid z^{p^s}=x_1^{p^a}r_2
angle,
qquad s>age2,
]
with odd (p) and a nonzero quadratic initial relation (r_2). The rank-two stress relation (r_2=[x_1,x_2]) is the control case; at least one genuinely different quadratic form must be tested.

The target is to determine whether the critical relative-window mechanism at (n=p^s+1) is structural beyond the Demuškin-specific quadratic form.

Pre-check obligations before computation:
- Object: relative finite-window extension (W_n(G)	o D/D_n(D)) and its first intrinsic candidate obstruction.
- Input: (p,s,a,d,r_2); (q=p^a) may parameterize the family but must not be inserted into the finite-window object.
- Functoriality: quotient maps and admissible generator changes must induce the obstruction.
- Gauge: quotient only by explicitly justified automorphisms/normalizations.
- Orientation bridge: state the map from finite-window data to the relative extension/orientation datum before testing.
- q-blindness: the candidate finite object is defined without (q).
- Separation: compare the control stress case with a genuinely different quadratic form.
- Novelty: distinguish any broader theorem from the already closed stress-family threshold.
- Stop: if intrinsicity or the orientation bridge fails, stop rather than enlarging the family.

Gate:
- PASS = theorem-level factorization survives for the broader class, with an independent non-control example;
- FAIL = the mechanism is essentially Demuškin-specific or admissible quadratic inputs exhibit incompatible behavior at the same critical window;
- CONDITIONAL = survival requires an explicit nondegeneracy hypothesis on (r_2);
- OPEN = coherent broader pattern appears but intrinsic factorization/general proof remains unresolved.

Immediate next action: perform this pre-check, then test the smallest non-control quadratic cases before any large computation.


## 2026-10-04 — bounded generalization challenge: user proposal reviewed and execution plan fixed

The user proposed replacing the Demushkin-only test group by a universal E_psi generator for arbitrary relations r, motivated by small p=3,s=1 experiments showing split at n=3 and non-split at n=4 for several relations. This proposal was reviewed against the authoritative research state.

### Decision
**ACCEPT the broader research ambition, but do not jump directly to the universal E_psi generator.** The current authorized branch is the bounded quadratic test-family challenge recorded in CURRENT_STATE.md. This is the correct middle ground between the narrow certified Paper 4 core and the previously failed arbitrary-(r), degree-only theorem.

### Why the correction is necessary
The s=1 experiments are too weak for the intended test (the active family requires s>a>=2), and the degree-3 relation [[x,y],y] is not a quadratic initial relation. Thus they cannot by themselves establish that the critical p^s+1 mechanism is structural. The universal claim “psi exists => n_sep=p^s+1” also requires an intrinsic definition of E_psi, functoriality/gauge invariance, and a proved separation mechanism before it can be treated as a theorem program.

### Authorized experiment
Use G_{s,a}(r_2)=<z,x_1,...,x_d | z^{p^s}=x_1^{p^a}r_2>, with odd p and s>a>=2, nonzero quadratic initial r_2. Keep r_2=[x_1,x_2] as the control and test a genuinely non-equivalent quadratic form, preferably first at d>=4 where rank-2 versus rank-4 quadratic forms give a real comparison. The finite-window object must remain q-blind.

### Required pre-check
Object / Input / Functoriality / Gauge / Orientation bridge / q-blindness / Separation / Novelty / Stop must be discharged before substantial computation. If intrinsicity or the orientation bridge fails, the branch stops.

### Classification
- arbitrary-r degree-only theorem: **FAIL / CLOSED**;
- Paper 4 certified core: **PASS / CLOSED**;
- all-s exact-threshold/transfer-defect boundary: **OPEN / intentionally not a blocker for this challenge**;
- bounded quadratic-family generalization: **OPEN — active challenge**;
- universal E_psi generator: **OPEN / future generalization, DEFERRED**.

Immediate next action: pre-check, then smallest genuinely non-control quadratic test case; no large s=2 computation before that gate passes.


## 2026-10-04 — strategic correction: universal E_psi branch reopened deliberately

The user challenged the earlier conservative decision to defer the universal E_psi generator, correctly distinguishing **governance discipline** from **risk aversion**. The repository continuity protocol is intended to prevent silent scope drift, revive superseded proofs, and promote exploratory computations to theorem status without validation. It does not forbid a consciously chosen high-risk generalization challenge.

### Decision
The universal E_psi direction is therefore **REOPENED as an explicit exploratory branch**. This is a deliberate research gamble, not a reclassification of the failed arbitrary-r degree-only theorem.

The target is stronger than the bounded quadratic-family challenge: construct, or prove impossible to construct, an intrinsically defined finite twisted-character test object E_psi for a broad class of relations r, and determine whether the p^s+1 separation mechanism survives.

### Non-negotiable discipline
The branch remains subject to the protocol's pre-check. In particular, E_psi must not be defined by secretly inserting the unknown q/orientation, and the twisted Fox condition must be shown to be presentation/gauge invariant before large computations. A failure of intrinsicity is a valid and potentially useful **FAIL / CLOSED** result for this construction.

### Strategic consequence
The bounded quadratic-family branch is no longer the sole next step. It becomes a control/benchmark family for the universal branch. The research order is now:

**E_psi intrinsic definition → functoriality/gauge audit → minimal generator → p=3,s=2/3 stress tests → separation/factorization attempt → classify → record.**

The Paper 4 certified core remains frozen. The old arbitrary-r degree-only theorem remains FAIL/CLOSED. No result from this exploratory branch may be back-propagated into Paper 4 without a separate theorem audit.


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


## 2026-10-04 — E_psi quadratic separator audit closes the marked theorem

The E_psi branch was subjected to a second, adversarial audit of the proposed quadratic lemma.

### Correction 1: degree-two Zassenhaus piece
The previously used expression
\[
\rho_2(r)=\sum_i a_iX_i^{[p]}+\sum_{i<j}b_{ij}[X_i,X_j]
\]
was wrong for odd-p Zassenhaus filtration. Since F^p is contained in D_p and hence D_3,
\[
D_2/D_3\cong\Lambda^2H_1(F,\mathbf F_p),
\]
and the degree-two initial form is purely alternating.
Classification: FAIL / CLOSED for the p-power-term formulation; superseded.

### Correction 2: higher terms are not automatically negligible
The earlier statement that the D_3-tail is harmless without calculation was also rejected. The p-power part of D_3=gamma_3 F^p contributes at order p before cocycle normalization and therefore at the same normalized p^s-scale. The gamma_3-part, in contrast, contributes only at order p^(2s) and vanishes modulo p^(s+1).

### Closed argument
Let r=r_2 h, h in D_3, and write epsilon=p^s. Use order-p characters
\[
\psi_\alpha(x_i)=1+\varepsilon\alpha_i.
\]
For
\[
r_2=\sum_{i<j}b_{ij}[x_i,x_j],
\]
the crossed-homomorphism calculation gives
\[
\delta(r_2)\equiv p^sL_B(\alpha,u)\pmod{p^{s+1}},
\]
where for a basic commutator
\[
L_{ij}(\alpha,u)=-\alpha_j u_i+\alpha_i u_j.
\]
If B is nonzero, choose a vertex k incident to a nonzero edge. Then L_B(t e_k, dot) is a nonzero linear functional for t nonzero.

After scaling the cocycle by p^(s-1), the p-power part of h contributes an alpha-independent linear functional C_h(u) at the same p^s-scale; the gamma_3-part is zero modulo p^(s+1). Varying t in F_p, at most one value can make C_h+L_B(t e_k, dot) identically zero. Since p is odd, choose another value and then choose u with nonzero total functional.

Hence
\[
\exists(\psi,\delta):\quad \psi(r)=1,\quad v_p(\delta(r))=s,
\]
and therefore p^s is in I_psi(r).

### Classification
- affine E_psi object: PASS / CLOSED;
- marked functoriality/gauge/q-blindness: PASS / CLOSED;
- quadratic affine separator for every r in D_2\D_3: PASS / CLOSED;
- marked critical-window detection at p^s+1: PASS / CLOSED;
- abstract unmarked orientation/character bridge: OPEN / LOAD-BEARING;
- abstract same-window separation: OPEN;
- arbitrary-degree degree-only theorem: FAIL / CLOSED.

### Research boundary
This closes the marked quadratic E_psi theorem candidate without reviving the old arbitrary-degree claim. The next authorized attack is the intrinsic orientation bridge, not another random quadratic sweep or an enlargement of the relation class.

Authoritative detailed audit: research/EPSI_INTRINSIC_DEFINITION_AUDIT_2026-10-04.md.


## 2026-10-04 — E_psi orientation-bridge audit

The single-character orientation bridge was tested by symmetry rather than by further computation. In the control family r=[x_1,x_2] (rank two), determinant-one Nielsen automorphisms preserve the relator up to conjugacy and act as SL_2(F_p) on the nonzero order-p character space. The marked affine separator works for nonzero character directions, so the successful set is a full nonzero orbit. Therefore no individual nonzero psi is canonical.

**FAIL / CLOSED:** distinguished single-psi bridge.

**OPEN / LOAD-BEARING:** orbit/groupoid-valued bridge.

This is not a no-go for unmarked separation itself. It only rules out presentation-independent selection of one character. The next attack must define an orbit-invariant affine defect directly from the abstract finite window.

Authoritative detail: research/EPSI_ORIENTATION_BRIDGE_AUDIT_2026-10-04.md.


## 2026-10-04 — intrinsic character-carrier salvage

After closing the single-character bridge, the intrinsic replacement
\[
\mathcal A(W)=\operatorname{Ann}_{H^1(W,\mathbf F_p)}(\operatorname{Tor}(W^{ab}))
\]
was identified.

For a critical quadratic window, writing \bar r=p^k a, one can choose a nonzero character direction alpha with alpha(a)=0 and B(alpha,-)\ne0, where B is the nonzero alternating degree-two initial form. Hence the marked affine separator may be chosen inside the canonical carrier.

Classification: **PASS / CLOSED** for the carrier and **PASS / CLOSED** for existence of a successful marked character in it. The carrier itself is not a separator; the extension-defect attached to the power relation remains **OPEN / LOAD-BEARING**.


## 2026-10-04 — critical correction: Tor-annihilator carrier was invalid

The proposed intrinsic carrier
\(\operatorname{Ann}_{H^1(W,\mathbf F_p)}(\operatorname{Tor}(W^{ab}))\)
was adversarially checked and found to be zero for finite p-group windows: W^{ab} is itself finite torsion, and H^1(W,F_p)=Hom(W^{ab},F_p). Therefore the claimed PASS/CLOSED carrier is **FAIL/CLOSED** and superseded.

This correction does not affect the marked quadratic E_psi theorem or the single-character symmetry no-go. It reopens only the carrier construction. The next legitimate intrinsic candidate must exploit filtered extension/Bockstein data rather than ordinary torsion of W^{ab}.


## 2026-10-04 — E_psi Sp-orbit closure claim critically rejected

A proposed closure of the unmarked orientation bridge via an Sp-orbit was adversarially audited and is **not valid**. The decisive counterexample is already in rank 4: r_2=[x_1,x_2] is nonzero in D_2/D_3 but defines a rank-2 degenerate alternating form. Its stabilizer preserves the radical, so it is not the full Sp_4(F_p) and does not act transitively on all nonzero character directions. More generally, r in D_2\D_3 does not imply nondegeneracy, and the Zassenhaus exponent s has no reason to equal half the rank of B.

Even if a nondegenerate special case has a transitive symplectic orbit, transitivity does not imply abstract finite-window separation: one still needs an intrinsic defect on the orbit/representation groupoid and a proof that it differs for s and t. Likewise, the assertion that B is recovered from the abstract finite window merely because the window is a quotient of G_s(r) is not a valid intrinsicity argument.

Classification: Sp-orbit bridge for all D_2\D_3: **FAIL / CLOSED as stated**; nondegenerate symplectic subcase: **CONDITIONAL** only; orbit/groupoid-valued intrinsic defect: **OPEN / LOAD-BEARING**; abstract unmarked same-window separation: **OPEN**. This supersedes the proposed PASS/CLOSED Sp-orbit conclusion. The marked E_psi theorem remains PASS/CLOSED.


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


## 2026-10-04 — E_psi / critical-separation audit: proposed closure rejected

A full audit of the session-level claim that the E_psi branch is now closed found a decisive filtration error and an unsupported automorphism-orbit step.

### Decisive correction

For the Zassenhaus filtration, if (c\in D_3\setminus D_4) and (p^m>3), then
[
D_{p^m}\subset D_3,
]
not (D_3\subset D_{p^m}). Hence for
[
r_A=[x_1,x_2],qquad r_B=r_Ac,qquad c\in D_3\setminus D_4,
]
the two relators do **not** have the same image modulo (D_{p^m}). Therefore the assertion that
[
W_{p^m}(G_A)\cong W_{p^m}(G_B)
]
follows from the filtration degree of (c) is false.

What is valid is only the formal low-window statement: if (c\in D_k), then the two defining relators have the same image in (F/D_k(F)), so the corresponding presented quotients have the same presentation modulo (D_k). This does **not** imply non-isomorphism at (k+1); an abstract isomorphism may come from an automorphism of the free quotient.

### Second correction: automorphism argument

The statement “an automorphism preserves degree, therefore it cannot send a degree-2 element to degree-2 plus degree-3” is invalid. IA automorphisms act trivially on abelianization while changing higher filtered terms; Magnus generators include commutator transvections (x_i\mapsto x_i[x_j,x_k]). Thus preservation of the leading graded class does not rule out adding higher Zassenhaus/lower-central terms. Any claimed separation of (r_A) from (r_Ac) therefore requires an actual orbit calculation, not a degree argument.

### Consequence

The proposed general statement
[
c\in D_k\setminus D_{k+1}\Longrightarrow
W_k(G_A)\cong W_k(G_B),W_{k+1}(G_A)\not\cong W_{k+1}(G_B)
]
is **FAIL/CLOSED as stated**. The first implication is presentation-level and valid; the second is not automatic.

The specific pair
[
[x_1,x_2],quad [x_1,x_2][x_1,[x_1,x_2]]
]
does not establish a critical (p^m+1) separation. In particular, for (p^m>3) it is already different modulo (D_{p^m}) at the presentation level, and its abstract orbit under automorphisms remains a separate question.

### E_psi boundary correction

The statement “marked E_psi theorem has abstract content exactly equal to the intrinsic quadratic invariant B” is also too strong. What is established is only:
- the marked theorem depends on a quadratic initial relation and an externally chosen target (E_s);
- (s) is not extracted from (r_2);
- no intrinsic single-character bridge has been constructed;
- therefore the marked theorem does not currently supply an unmarked recovery of (s).

This is **OPEN**, not FAIL/CLOSED. The possibility of an independent abstract invariant of the family (G_s(r)) remains unresolved.

### Current classification after audit

- marked quadratic E_psi theorem: **PASS/CLOSED (marked scope)**;
- single canonical psi bridge: **FAIL/CLOSED**;
- Tor-annihilator carrier: **FAIL/CLOSED**;
- Sp-orbit universal bridge: **FAIL/CLOSED as stated**;
- quadratic kernel-rank separation: **PASS/CLOSED**;
- generic (D_k/D_{k+1}) critical separation theorem: **FAIL/CLOSED as stated**;
- specific (G_s(r)\) vs (G_t(r)) abstract same-window separation: **OPEN/LOAD-BEARING**;
- abstract unmarked shadow of the marked E_psi theorem: **OPEN**.

This correction does not reopen the failed arbitrary-degree theorem. It restores the authoritative boundary that exact unmarked same-window separation is unresolved.


## 2026-10-04 — d=3, p=3 cubic-jet audit: Q3 computation and W4 separation

A direct linear-algebra audit of the proposed rank-2 quadratic control case
\[
F=F(x_1,x_2,x_3),\qquad r_2=[x_1,x_2]
\]
confirms the following.

1. The degree-3 free Lie space has dimension 8 over \(\mathbf F_3\). For
\[
\Delta:L_2\oplus L_2\to L_3,\qquad
\Delta(u_1,u_2)=[u_1,x_2]+[x_1,u_2],
\]
one obtains \(\dim\operatorname{im}\Delta=6\). Moreover
\[
[r_2,V]\subseteq\operatorname{im}\Delta,
\]
so
\[
Q_3(r_2)=L_3/([r_2,V]+\operatorname{im}\Delta)
\]
has dimension 2. A valid quotient basis is represented by
\[
c_1=[x_3,[x_1,x_3]],\qquad c_2=[x_3,[x_2,x_3]].
\]
Independent tensor-model row reduction over \(\mathbf F_3\) gives rank 6 for \(\operatorname{im}\Delta\) and rank 8 after adjoining \(c_1,c_2\).

2. The stabilizer of \(e_1\wedge e_2\) in \(GL_3(\mathbf F_3)\) has order
\[
|SL_2(\mathbf F_3)|\,|\mathbf F_3^\times|\,|\mathbf F_3^2|
=24\cdot2\cdot9=432.
\]
The earlier 432 value is correct; the 864 value would correspond to incorrectly using \(GL_2\) rather than the determinant-one condition forced by fixing \(e_1\wedge e_2\).

3. On \(Q_3\), the unipotent radical and the scalar \(\lambda\in\mathbf F_3^\times\) act trivially, while the \(SL_2\)-part acts naturally on \(\langle c_1,c_2\rangle\cong\mathbf F_3^2\). Hence the stabilizer has exactly two orbits:
\[
\{0\},\qquad Q_3\setminus\{0\}.
\]

4. The proposed \(W_4\)-separation is valid for the specific zero/nonzero comparison, but the original proof contained a filtration error. It is false that
\[
\gamma_3(F)^3\subseteq\gamma_4(F).
\]
The correct statement is
\[
D_4(F)=\gamma_4(F)\,\gamma_2(F)^3\,\gamma_3(F)^3\,F^9,
\]
so the lower-central degree-3 layer of the \(W_4\) quotient is taken modulo the appropriate 3-power relations; equivalently its relevant cubic layer is an \(\mathbf F_3\)-quotient of \(L_3\), not the integral \(L_3\) used in the draft argument.

For
\[
r_A=[x_1,x_2],\qquad
r_B=[x_1,x_2]c_1,
\]
the degree-3 normal-closure contribution is respectively
\[
\langle [[x_1,x_2],x_i]:i=1,2,3\rangle
\]
of dimension 3, and that same 3-space plus \(\langle c_1\rangle\), of dimension 4. Thus the corresponding cubic lower-central quotient has dimensions 5 and 4 (over \(\mathbf F_3\)). Therefore
\[
W_4(G_A)\not\cong W_4(G_B).
\]
At \(W_3\), both relators have the same image modulo the degree-3 tail, so
\[
W_3(G_A)\cong W_3(G_B).
\]

Classification: **PASS / CLOSED (specific \(d=3,p=3\), zero-vs-nonzero cubic orbit separation)**.

Important boundary: this does **not** prove that every pair of distinct \(Q_3\)-orbits gives distinct \(W_4\)-isomorphism classes in general. In the present \(d=3,p=3\) example there are only two stabilizer orbits, and the zero/nonzero pair is separated by the cubic-layer dimension.

The broad criterion
\[
W_n\text{-iso}\iff \operatorname{Aut}(F/D_n)\text{-orbit of the truncated relator}
\]
remains **OPEN**. An isomorphism between two quotient groups does not automatically imply that their defining kernels are conjugate under an automorphism of the universal truncated free group; this is a Nielsen/lifting issue and requires a separate theorem.

Next authorized attack: formulate the general cubic-layer map
\[
Q_3(r_2)\longrightarrow \text{isomorphism invariants of }W_4
\]
carefully, first for arbitrary odd \(p\) and rank \(d\), before attempting the full \(Q_k\) tower.


## 2026-10-04 — correction: the d=3,p=3 cubic W4 separation is NOT certified

The immediately preceding audit over-promoted the pair
\[
r_A=[x_1,x_2],\qquad r_B=[x_1,x_2]c_1,qquad c_1=[x_3,[x_1,x_3]]
\]
to PASS/CLOSED. That promotion is **superseded and withdrawn**.

The error is more fundamental than the earlier \(\gamma_3^3\subseteq\gamma_4\) mistake. For the inhomogeneous relator \(r_B=r_2+c_1\), the leading lower-central term is still \(r_2\) in degree 2. Passing to the associated lower-central graded object therefore initially imposes the degree-2 relation \(r_2\), whose degree-3 consequences are \([r_2,V]\). One cannot simply add \(c_1\) as an independent degree-3 relation in \(\gamma_3(W_4)/\gamma_4(W_4)\).

Equivalently: the fact that the normal closures of \(r_2\) and \(r_2c_1\) are different in the universal truncated presentation does **not** imply that \(c_1\) contributes an additional independent relation to the cubic lower-central layer of the quotient. The relation \(r_2c_1=1\) identifies the degree-2 word \(r_2\) with a degree-3 correction; it does not separately kill \(c_1\).

Therefore the claimed dimensions
\[
\dim \gamma_3(W_4(G_A))/\gamma_4=5,\qquad
\dim \gamma_3(W_4(G_B))/\gamma_4=4
\]
are not established and should not be used.

What remains valid from the computation:
- \(Q_3(r_2)\) has dimension 2 with representatives \(c_1,c_2\);
- the stabilizer of \(e_1\wedge e_2\) has order 432;
- its action on \(Q_3\) has zero and nonzero orbits;
- \(Q_3\) therefore contains genuinely non-removable cubic directions at the presentation/jet level.

What is **not** established:
\[
W_3(G_A)\cong W_3(G_B),\qquad
W_4(G_A)\not\cong W_4(G_B)
\]
for the zero/nonzero cubic pair. The \(W_3\) equality is still presentation-level and safe; the \(W_4\) non-isomorphism is **OPEN**.

The next correct attack is not another dimension count based on the same lower-central layer. It must test an invariant that sees the *extension class/filtered lift* of the cubic jet, e.g. a canonical p-power/commutator extension datum in \(W_4\), or directly compute the full finite 3-group isomorphism type for the smallest case. The \(Q_3\) orbit remains a candidate input, not yet a certified \(W_4\)-classification invariant.

Classification of the cubic result after correction:
- \(Q_3\) computation: **PASS / LOCAL**;
- nonzero cubic directions modulo IA gauge: **PASS / LOCAL**;
- zero-vs-nonzero \(Q_3\) orbit \(\Rightarrow W_4\) non-isomorphism: **OPEN**;
- general \(Q_3\to W_4\)-isomorphism classification: **OPEN / LOAD-BEARING**.


## 2026-10-04 — DIRECTION 2 CLOSED: ordinary mod-p cohomology is s/a-blind

The requested Direction 2 attack was completed to the full ordinary cohomology-ring level rather than stopping at H^1, H^2, or the associated graded.

### Target
For odd p, stress family G_{s,a}=<z,x_1,...,x_d | z^{p^s}=x_1^{p^a}[x_1,x_2][x_3,x_4]...>, with s>=1, finite a>=1, and a=infinity meaning the power term is absent.

### Core proof
Because p^s,p^a>=3, both power terms lie in the third p-Zassenhaus term. Therefore the relator is congruent modulo the third term to the same quadratic commutator product for every s,a.

Quadrelli, arXiv:2011.03233v3, Proposition 2.1, applies directly: the mod-p cohomology algebra is quadratic; H^k(G,F_p)=0 for k>=3; and the cup product in H^1 is exactly the common symplectic commutator form. Thus the complete ordinary graded algebra H^bullet(G_{s,a},F_p) is independent of s and a in the declared family.

### Independent verification
- filtration check: PASS;
- minimal one-relator presentation: PASS;
- complete H^bullet determination: PASS;
- a=s versus a=infinity: PASS;
- q-blindness: PASS.

The literature source is stronger than the earlier internal associated-graded observation: it closes the whole ordinary cohomology ring, not merely gr_Z.

### Boundary
This does **not** prove G_{s,a} isomorphic to G_{t,b}, equality of finite windows, or equality of higher operations such as Massey/Bockstein/A_infinity data. It proves only that ordinary mod-p cohomology cannot recover the hidden s or a in this family.

### Classification
**Direction 2 = PASS / CLOSED.**

The route is closed. The remaining finite-window boundary must use information beyond the ordinary cohomology ring, if it is pursued at all. No repetition of ordinary H^* calculations is authorized.

Authoritative audit: research/PAPER4_DIRECTION2_COHOMOLOGY_BLINDNESS_CLOSURE_2026-10-04.md.


## 2026-10-04 — Direction 3 decision: ordinary cohomology is now discarded; filtered extension/lift becomes the active invariant layer

The completed Direction 2 audit establishes **PASS / CLOSED** for ordinary mod-p cohomology in the declared odd-p stress family: the full ordinary cohomology ring is s/a-blind. Repeating H^*, cup-product, or ordinary quadratic-cohomology calculations is therefore no longer an authorized route to the hidden finite-window parameter.

### Strategic conclusion

**Ordinary cohomology is no longer a research target.** The remaining information must be sought one layer above the ordinary cohomology ring, in the **filtered extension/lift structure** of the finite Zassenhaus tower.

The working object is not a new cohomology ring. The first intrinsic candidate is the filtered extension/lift groupoid over a critical window:
[
mathsf{Lift}_n(W_n)
=
left{
widetilde W	woheadrightarrow W_n:
widetilde W	ext{ is an admissible }(n+1)	ext{-level filtered lift}

ight}/cong,
]
together with the kernel
[
K_n=D_n/D_{n+1}
]
and the induced conjugation/trivial-action data and extension class. Since
([D_n,G]subseteq D_{n+1}), the successive Zassenhaus layer is central; however, the research target is the **actual filtered lift/extension package**, not merely its abstract class in ordinary (H^2).

For the present problem the decisive question is:

> Does the critical filtered lift/extension fiber over (W_{p^s}(G_s)) versus (W_{p^s+1}(G_s)) retain the hidden (p^s)-power relation even though the ordinary cohomology ring does not?

### Required next gate

Before computation, audit:
1. **Object:** define the admissible filtered lift groupoid independently of the hidden q/s parameter.
2. **Input:** specify exactly which filtration/layer/lift data are retained.
3. **Functoriality:** prove invariance under finite-window isomorphism and admissible presentation changes.
4. **Gauge:** quotient lift choices and generator changes correctly.
5. **Orientation bridge:** determine whether the lift package carries the affine/orientation information without choosing a distinguished character.
6. **q-blindness:** the recognition object must not contain q=p^a.
7. **Separation:** test whether the extension/lift package differs for the a=s versus a=infinity boundary or for s versus t at the critical level.
8. **Novelty:** distinguish the actual filtered lift invariant from merely restating an ordinary cohomology extension class.
9. **Stop:** if the lift object collapses to the already-blind ordinary ring or is not intrinsic, close that formulation rather than adding ad hoc decorations.

### Immediate research target

The first concrete construction is the **one-step filtered extension**
[
1	o D_n/D_{n+1}	o W_{n+1}	o W_n	o1
]
viewed as a structured lift, with its p-power/commutator lifting data retained. The next attack should determine whether the hidden relation contributes a nontrivial, gauge-invariant defect to this lift package at (n=p^s).

Classification:
- ordinary cohomology route: **PASS / CLOSED and STOPPED**;
- filtered extension/lift object: **OPEN / LOAD-BEARING**;
- intrinsic extension defect: **OPEN**;
- abstract same-window separation: **OPEN**;
- arbitrary-degree degree-only theorem: **FAIL / CLOSED** and remains closed.

This entry is the controlling decision for the next research branch.


## 2026-10-04 — filtered-extension extraction/no-go boundary CLOSED

The post-cohomology Direction 3 was executed at the structural level rather than by another candidate hunt. The canonical one-step Zassenhaus extension
\[
1\to K_n=D_n/D_{n+1}\to W_{n+1}\to W_n\to1
\]
was fixed as the only active object.

### Gate result
- Object: **PASS / CLOSED**. The extension is canonical, q-blind, and functorial under filtered finite-window isomorphism.
- Input: **PASS / CLOSED**. No hidden q=p^a, marked character, or presentation choice is inserted.
- Gauge: **PASS / CLOSED**. Since [D_n,G]⊂D_{n+1}, the kernel is central. A section produces a 2-cocycle, and changing the section changes it by a coboundary. Hence a defect computed from a selected lift is not intrinsic unless it descends through this gauge action.
- Orientation bridge: **FAIL / CLOSED** for the proposed scalar/carrier extraction. The unmarked extension contains no distinguished character/orientation. The marked E_psi construction does not supply an intrinsic bridge after the marking is forgotten.
- q-blindness: **PASS / CLOSED**.
- Separation: the full extension-equivalence class is not a new lower-level invariant; it is exactly the structured isomorphism class of W_{n+1}->W_n. Thus using the full package to separate the critical cases is equivalent to solving the original finite-window extension-isomorphism problem.

### Independent structural check
Standard central-extension theory identifies section changes with coboundaries and the intrinsic extension with its cohomology class. Zassenhaus layers additionally carry canonical restricted-Lie p-power/commutator operations. These facts validate the gauge analysis, but neither supplies the missing unmarked orientation bridge.

### Classification
**Filtered-extension extraction as a new canonical defect = FAIL / CLOSED.**

This is a method-level no-go, not a proof that the critical a=s and a=infinity windows are isomorphic. The latter remains **OPEN** if one insists on exact finite-window classification. No further candidate hunting is authorized merely to avoid that boundary.

Authoritative audit: research/PAPER4_FILTERED_EXTENSION_EXTRACTION_NO_GO_2026-10-04.md.

### Stop decision
Do not reopen ordinary cohomology, search for another carrier, invent another E_psi variant, or add ad hoc lift decorations. Further progress would require a genuinely new theorem giving a canonical quotient/factorization of the full extension-equivalence class. The current extraction branch is therefore closed at its legitimate boundary.


## 2026-10-04 — correction: filtered-extension no-go was method-level, not tower-wide

Adversarial review identified a real overreach in the immediately preceding stop. The prior result correctly closes the attempt to extract a canonical scalar defect from a chosen section/lift of the **unmarked one-step extension**, because section changes act by coboundaries and no distinguished orientation is present. But that does not justify a blanket no-go for all canonical representations of the same extension, nor for multi-step compatible tower data.

### Corrected failure taxonomy
A negative result must distinguish:
1. **representation failure** — a chosen coordinate cannot expose information present in the fixed structure;
2. **information failure** — the full declared structure itself lacks the target information;
3. **detector failure** — the information may be present, but no functorial extraction operator has yet been found.
Only (2) is a structural no-go for the declared object.

### Pre-registered bounded reopening
The branch is reopened only as a representation-layer feasibility gate, not as candidate hunting. The admissible structure layers are fixed in advance:
- extension class;
- induced module/conjugation structure;
- canonical restricted p-power and commutator operations;
- their adjacent-layer compatibility;
- two-step/full finite tower extension compatibility.

The minimum multi-step object is W_{p^s+2}->W_{p^s+1}->W_{p^s}. No new carrier, character, or ad hoc lift decoration may be introduced merely because one layer fails.

### E_psi mechanism audit
The marked affine detector succeeds through a combination of:
- **filtered depth**: D_{p^s}(E_s) nontrivial but D_{p^s+1}(E_s)=1;
- **orientation/representation**: psi and delta provide the directed affine evaluation of the hidden relation.

Thus the one-step unmarked extension cannot be expected to reproduce the marked detector merely from filtered depth. The intrinsic target, if it exists, should be an affine representation **orbit/groupoid**, not a canonically selected single psi.

Representability will be used only after defining the category of admissible filtered tower structures and the functor to affine representation groupoids; it will not be assumed as a slogan.

### Classification
- one-step scalar defect from unmarked extension: **FAIL / CLOSED**;
- one-step/tower representation-layer feasibility: **OPEN / LOAD-BEARING**;
- exact unmarked same-window separation: **OPEN**;
- no arbitrary candidate hunt authorized.

Authoritative pre-registration: research/PAPER4_REPRESENTATION_LAYER_PREREGISTRATION_2026-10-04.md.


## 2026-10-04 — representation-layer gate reaches its boundary

The pre-registered two-step filtered-tower feasibility gate has now been executed. The intrinsic object is
\(W_{p^s+2}\to W_{p^s+1}\to W_{p^s}\), with central extension classes, induced module structure, restricted p-power/commutator operations, and adjacent-layer compatibility.

- Object/Input/Functoriality/Gauge: **PASS / CLOSED**.
- Distinguished single-character orientation bridge: **FAIL / CLOSED**, consistent with the earlier symmetry no-go.
- An affine representation **groupoid/orbit construction** is legitimate and functorial from the full declared tower, but at this level it is only a canonical reformulation of the structured finite-window problem, not a strictly smaller carrier.
- No comparison theorem currently shows that the groupoids differ for (a=s) versus (a=\infty), and none shows that they coincide.
- Therefore the remaining obstruction is classified as **detector failure / OPEN**, not information failure.

This closes the bounded representation-layer branch at its pre-registered stop rule. No new carrier, character, lift decoration, or ad hoc representation hunt is authorized. The exact unmarked same-window separation remains **OPEN / LOAD-BEARING** and now requires a genuinely new factorization/compression theorem rather than another candidate search.

Authoritative audit: research/PAPER4_REPRESENTATION_LAYER_GATE_RESULT_2026-10-04.md.


## 2026-10-04 — Paper 4 manuscript/PDF final artifact audit

Paper 4 manuscript was finalized from the certified research state and built from
the dedicated `paper4-tex-2026-10-04` branch. The four manuscript corrections
were applied: direct same-window order separation for (1\le a<s<t);
the (a=s) versus (a=\infty), (s\ge2) boundary remains OPEN;
the arbitrary-(r) degree-only generalization is explicitly closed using
the (r=z^p) counterexample; and the Zassenhaus/Jennings--Lazard and
quadratic-cohomology literature boundary was recorded in the manuscript.

Final CI result: `paper4-tex-build` run 37172461426 = PASS.
PDF: 12 pages.
SHA-256: `39937e753368e4cb8c06dfaf2f7808727c3d88e14b75669c937ab0d06520b536`.
GitHub Actions artifact: `paper4-pdf`, id 11292160916.
The local audited PDF is `/mnt/data/Paper4_final_2026-10-04.pdf`.

Classification: **PASS / CLOSED — manuscript artifact complete**.
This closes the writing/PDF-production task only; the mathematical OPEN boundary
(G_{s,s}) versus (G_{s,\infty}) for (s\ge2) remains unchanged.


## 2026-10-04 — Paper 5 redefined around Aut(W_n)

The compression formulation of Paper 5 was judged too tautological to carry the intended mathematical contribution. The active branch is therefore redefined as concrete finite-group structure: Aut(W_n), its IA kernel, its image on W_n/Phi(W_n), induced action on admissible quotients Q_n, and radical/shear effects.

The user supplied completed calculations reporting exact automorphism orders for (p,n)=(3,4) and (5,6). The p-parts exhibit the same factor p^2 deficit from split to non-split cases at both primes. The p=3,n=4 admissible-kernel enumeration reports 81/9/72 kernels with orbit pattern 1/1/3 respectively.

Because the current repository did not yet contain the supplied scripts/logs for these new calculations, the evidence is recorded as PASS / LOCAL, user-reported rather than independently certified. No structural theorem is promoted from the order comparison alone.

The next authorized computation is the IA/GL decomposition for all p=3,n=4 cases, followed by the induced Aut(W) -> Aut(Q) image/kernel. The aim is to identify the exact layer responsible for the p^2 gap. Only after independent closure at p=3 will the same measurement be run at p=5.

Audit: research/PAPER5_AUT_STRUCTURE_IA_GL_PRECHECK_2026-10-04.md.


## 2026-10-04 — Paper 5 Aut-orbit follow-up evidence (user-supplied logs)

The user supplied three computational artifacts/results for the active Aut(W_n) branch (aut_common.g, aut3.log, p5aut.log). The artifacts are not yet committed to the current repository, so the following is recorded as USER-REPORTED / REPRODUCTION PENDING, not theorem-level evidence.

Reported p=3 orbit structure: (3,1,1) has 72 admissible kernels in Aut-orbits 9+9+54; (3,1,2) has 9 kernels in one orbit; (3,2,1), n=10, has 81 kernels in one Aut(W_10)-orbit, with reported |Aut(W_10)|=2*3^30, |K|=3^9, and 3^10 complements per kernel. The two size-9 orbits in (3,1,1) are reported to be distinguished by pi(z) in Phi(Q) versus outside Phi(Q); a complete invariant explanation of 9/9/54 is still open.

Reported p=5,n=6 orders: s=0,a=1 -> 2^2 5^109; s=1,a=1 -> 2^2 5^107; s=2,a=1 -> 2^2 5^109; s=1,a=2 -> 2^5 3 5^107; s=0,a=2 -> 2^7 3 5^109. This reproduces the reported p^2 p-primary split/non-split gap and shows s-dependence in total Aut order, but remains observational pending independent rerun.

Interpretation: Aut-orbit structure is now a strong candidate structural layer, but the authoritative Paper 5 gate still requires the p=3,n=4 IA/GL decomposition and fixed-quotient action analysis before the larger n=10 orbit result is promoted. Classification: PASS / LOCAL candidate evidence; reproduction and structural factorization OPEN. Audit: research/PAPER5_AUT_ORBIT_FOLLOWUP_AUDIT_2026-10-04.md.


## 2026-10-04 — Paper 5 IA/GL decomposition gate advanced

The five Paper 5 external calculation artifacts have now been restored under `research/external/paper5_aut/`: `aut_common.g`, `aut3.g`, `aut3.log`, `p5aut.g`, and `p5aut.log`. The earlier provenance label “user-reported / artifacts not in repository” is superseded.

The recovered p=3,n=4 calculation gives exact reported automorphism orders:
- s=0,a=1: (|Aut(W)|=2^2 3^{30});
- s=1,a=1: (|Aut(W)|=2,3^{28}), with 72 admissible kernels in orbits 9+9+54;
- s=0,a=2: (|Aut(W)|=2^5 3^{30});
- s=1,a=2: (|Aut(W)|=2^4 3^{28}), with one orbit of size 9;
- s=2,a=1: (|Aut(W)|=2^2 3^{30}), one orbit of size 81 and (3^{10}) complements.

Exact order arithmetic gives the following prediction, not yet a certified decomposition:
[
(0,1): (|IA|,|L|)=(3^{27},2^2 3^3),quad
(1,1): (3^{25},2,3^3),
]
[
(0,2): (3^{27},2^5 3^3),quad
(1,2): (3^{25},2^4 3^3).
]
Thus the p-primary (3^2) loss is predicted to lie entirely in the IA layer, while the linear image keeps (3^3) in all four cases.

A new executable audit was added at `research/scripts/paper5_ia_gl_decomposition.g`. It directly checks the Frattini action, the AutPGrp linear-image order, the IA factor from `agOrder`, and the exact factorization (|Aut(W)|=|IA||L|).

The GAP AutPGrp documentation confirms that `glAutos` are the automorphisms acting nontrivially on the Frattini quotient and that `agAutos` generate the normal solvable part, so this script targets the intended IA/GL split rather than introducing an ad hoc layer.

### Classification

- external artifacts: **PASS / REPOSITORY**
- total-order and orbit data: **PASS / REPOSITORY**
- IA-defect localization by order arithmetic: **PASS / LOCAL-PREDICTED**
- executable IA/GL decomposition: **OPEN / REPRODUCTION PENDING**
- quotient-action image/kernel: **OPEN**
- p=5 structural theorem: **DEFERRED until p=3 closure**

Audit: `research/PAPER5_IA_GL_DECOMPOSITION_AUDIT_2026-10-04.md`.


## 2026-10-04 — Paper 5 IA/GL execution gate: runtime boundary

The IA/GL localization was taken to the execution boundary. The repository now contains the five external GAP artifacts and the dedicated decomposition script. A local environment check was performed for GAP; GAP/AutPGrp is not installed in the available runtime, so the new executable gate could not be rerun here.

Accordingly, no IA-kernel equality or full Aut(W) generation claim is promoted. The exact-order arithmetic remains **PASS / LOCAL-PREDICTED**: for p=3,n=4 the split/non-split 3^2 gap is numerically localized to the candidate IA factor while the candidate linear image retains v_3=3 in all four cases.

Required next execution checks remain:
- displayed W generators generate W;
- agAutos act trivially on W/Phi(W);
- glAutos generate a linear image of the recorded order;
- the induced action homomorphism has kernel exactly <agAutos>;
- <glAutos,agAutos>=Aut(W);
- |IA| |L| = |Aut(W)|.

The available runtime cannot certify these until GAP/AutPGrp is executed in a suitable GAP environment. Classification: **OPEN / REPRODUCTION PENDING**. p=5 remains deferred.


## 2026-10-04 — Paper 4 roadmap alignment and Q-direction decision

External handoff roadmap `research/external/GENERAL_THEOREM_ROADMAP_HANDOFF_2026-10-04.md` was compared against `RESEARCH_MAP.md`, `CURRENT_STATE.md`, and the continuity protocol.

- Roadmap-level next target remains correct: **unmarked same-window separation** in the S/hard region, beginning with the smallest control case and then generalization.
- The roadmap's original L4/L5 implementation (extension-class/orbit separation) is no longer the best immediate route. One-step extension extraction, distinguished-single-psi bridge, naive Sp-orbit bridge, and two-step representation compression have already reached their recorded boundaries.
- Current best implementation is the intrinsic finite-group predicate
  \(Q(W):\exists(g,H),\ \langle g,H\rangle=W,\ 1\ne g^{p^s}\in H\).
- Q evidence is **PASS / LOCAL**: p=3,s=1,r=x^3 was exhaustively tested (52,488 positive generating pairs in W_s, 0 in W_t); p=5,s=1,r=x^5,n=6 has 10,226 positives in W_s and 0 in W_t among 200,000 random pairs. The latter is sample evidence, not proof.
- Frattini-lift reformulation gives a natural transformed-relator problem \(r'=\alpha^{-1}(r)\). Killing x yields the necessary abelian z-exponent condition \(v_p(\epsilon(r'))\le s\), reproducing the easy/high-valuation obstruction.
- The remaining hard boundary is nonabelian: rule out all relevant transformed relators in the \(v_p(\bar r)\le s\) region. The earlier restricted-Lie root-capture attempt is invalid without control of the induced filtration \(H\cap D_k(W)\); a Root-Capture lemma or equivalent Magnus/PBW statement is still **OPEN / LOAD-BEARING**.

**Decision:** the roadmap's Theorem-C direction is retained at the strategic level, but its implementation is updated to **Q-invariant → p=3,s=1,r=x^3 transformed-tuple/Frattini-lift audit → nonabelian Magnus/PBW obstruction → general lemma if possible**. Do not restart the already-closed L4/L5 extraction as a standalone carrier hunt.

Detailed alignment record: `research/PAPER4_ROADMAP_ALIGNMENT_AND_NEXT_STEP_2026-10-04.md`.
Classification: Q = **PASS / LOCAL**; Q theorem and nonabelian obstruction = **OPEN / LOAD-BEARING**.

Immediate next authorized action: classify Q-positive p=3,s=1,r=x^3 pairs up to the relevant automorphism/Frattini-lift structure and inspect the transformed relator at the minimal Magnus/PBW degree needed to isolate the common obstruction.


## 2026-10-04 — Paper 4 Q pre-check: current Q definition is too weak

Before executing the planned p=3,s=1,r=x^3 transformed-tuple audit, the current Q definition itself was rechecked under the continuity protocol.

The recorded predicate is:
Q(W): there exist g and H with <g,H>=W and 1 != g^(p^s) in H.

Immediate structural consequence: Q-positive implies ord(g)>p^s. Thus Q necessarily contains an exponent witness. More importantly, if H is allowed to be an arbitrary subgroup subject only to <g,H>=W, then H can be chosen after an element g with nontrivial p^s-th power; the predicate therefore does not by itself encode the intended nonabelian transformed-relator/Frattini-lift obstruction. It is at best an exponent-type detector unless additional restrictions on H are part of the definition.

Therefore the previously planned step “enumerate Q-positive pairs and extract a common Magnus/PBW obstruction” is NOT authorized yet. The Object/Gauge/Novelty pre-check fails at the current Q formulation: the subgroup H carries insufficient intrinsic structure to force a nonabelian obstruction. Any observed Q separation may be explained by exponent data already visible at a much coarser level.

This does not invalidate the numerical Q evidence as a computation; it changes its interpretation. Classification of the current Q predicate: **FAIL / CLOSED as a proposed nonabelian separator** unless an explicit, intrinsic restriction on H is supplied and independently justified. The reported p=3 exhaustive and p=5 sampled Q counts remain **PASS / LOCAL as computations of the stated predicate**, but they cannot be promoted to evidence for a nonabelian theorem.

Next authorized action is therefore to audit the exact intended definition of H. A valid refinement must specify: (1) what H is intrinsically, (2) why it is invariant under W-isomorphism and Frattini/Nielsen changes, (3) why the refinement is not simply an exponent/abelianization test, and (4) how it retains the transformed-relator obstruction. If no such restriction exists, Q is closed and the research must return to the external roadmap's L4/L5/extension-class problem or another genuinely nonabelian invariant.

This correction supersedes the immediately preceding plan to compute transformed tuples under the unrestricted Q definition.


## 2026-10-04 — explicit Paper 4 freeze and Paper 5 takeover

The user explicitly froze Paper 4 and authorized continuation of Paper 5 until a concrete structural result is obtained. Paper 4 is therefore no longer an active computation branch. Its certified core remains PASS/CLOSED; its exact unmarked same-window and all-s transfer-defect boundaries remain OPEN/LOAD-BEARING but intentionally deferred. No Paper 4 claim is promoted by this freeze.

Paper 5 is now the sole active research branch. The immediate load-bearing task is independent certification of the p=3,n=4 IA/GL decomposition. The repository already contains the recovered AutPGrp artifacts and the executable script `research/scripts/paper5_ia_gl_decomposition.g`. The recorded `agOrder` values are predictions only. The script must certify the actual kernel of Aut(W)->Sym(V), the linear image order, triviality of the ag-generators on V, and exact order factorization before the p^2 gap is localized structurally.

Execution order fixed: (1) p=3,n=4 IA/GL reproduction; (2) if PASS, fixed-quotient Aut(W)->Aut(Q) image/kernel; (3) if PASS, cross-prime p=5,n=6 structural replication; (4) only then analyze the 9+9+54 orbit decomposition and the n=10/3^10 complement phenomenon as downstream structure. The 9+9+54 split is an Aut(W)-orbit detector, not itself an IA/GL filtration statement.

Classification: Paper 4 **PASS/CLOSED — FROZEN**; Paper 5 IA/GL **OPEN/LOAD-BEARING**; p^2-gap source **OPEN**.

## 2026-10-04 — Paper 5 IA/GL gate execution triggered

The authoritative IA/GL audit script was committed to `main` with a CI-trigger comment (commit `573ad39e233208c880978b3bc2e85566f7d84d7c`). The repository workflow `.github/workflows/paper5-ia-gl-decomposition.yml` is configured to install GAP + AutPGrp and execute `research/scripts/paper5_ia_gl_decomposition.g` on pushes touching the script.

This is an execution trigger, **not yet a runtime PASS**: the available connector does not expose the resulting push-triggered workflow run in a directly retrievable form, so no IA/kernel equality is promoted until the runtime log is independently inspected.

An independent GAP documentation check confirms the hybrid automorphism representation semantics used by the audit: `glAutos` together with `agAutos` generate the automorphism group, `agAutos` form a soluble normal subgroup, and `glOrder` records the complementary order factor. This validates the intended decomposition interface, but does not replace execution of the kernel calculation.

Classification: IA/GL execution **OPEN / REPRODUCTION PENDING**; execution trigger **PASS / REPOSITORY**. Next authorized evidence is the actual CI runtime log.


## 2026-10-04 — Paper 5 decisive p=3,n=4 IA/GL runtime result

The corrected IA/GL computation was executed in GitHub Actions with GAP 4.12.1 + AutPGrp (run 37188599141, commit 17b52825318478339d125de7dc099a7737913474). The calculation uses all hybrid automorphism generators (A.glAutos\cup A.agAutos) to form the actual Frattini image, rather than treating (A.glAutos) alone as the linear image.

Results:

- (s,a)=(0,1): |Aut(W)|=2^2 3^30, |Im|=108=2^2 3^3, |IA|=3^27.
- (s,a)=(1,1): |Aut(W)|=2 3^28, |Im|=6=2 3, |IA|=3^27.
- (s,a)=(0,2): |Aut(W)|=2^5 3^30, |Im|=864=2^5 3^3, |IA|=3^27.
- (s,a)=(1,2): |Aut(W)|=2^4 3^28, |Im|=48=2^4 3, |IA|=3^27.

W-generation, exact Frattini dimension, and |IA||Im|=|Aut(W)| all pass.

This **reverses the previous IA-localization prediction**. The p^2 deficit is entirely on the GL/Frattini-image side: v3(|Im|) drops from 3 to 1 in the non-split cases, while v3(|IA|)=27 remains constant.

The runtime also records agGeneratorsTrivialOnV=false in every case, so (agAutos\neq IA) and the earlier identification is FAIL/CLOSED. This agrees with the AutPGrp hybrid documentation: glAutos and agAutos jointly generate the automorphism group, and glOrder is a complementary hybrid factor, not the full Frattini-image order. citeturn2search0turn2search8

Classification:
- actual p=3 IA/GL localization: **PASS / LOCAL**;
- p^2 gap = GL/Frattini-image defect: **PASS / LOCAL**;
- IA as source: **FAIL / CLOSED**;
- previous IA prediction 3^27 vs 3^25: **HISTORICAL / SUPERSEDED**;
- structural explanation of image-order drop: **OPEN / LOAD-BEARING**.

Next authorized action: compute/identify the actual image subgroups (L_{s,a}\le GL_3(3)), determine the stabilizer condition imposed by the defining relation, and only after that test p=5,n=6.


## 2026-10-04 — Paper 5 GL-image structure

After the decisive IA/GL localization, a dedicated GAP audit computed the actual Frattini-image groups (L_{s,a}\le GL_3(3)).

Results:
- (0,1): |L|=108, StructureDescription (((C_3\times C_3):C_3):(C_2\times C_2)), Id=[108,17].
- (1,1): |L|=6, (S_3), Id=[6,1].
- (0,2): |L|=864, (C_2\times((C_3\times C_3):GL(2,3))), Id=[864,4661].
- (1,2): |L|=48, (GL(2,3)), Id=[48,29].

The nonzero-vector orbit sizes are respectively:
(0,1) 18,2,3,3; (1,1) 2,2,3,2,6,3,2,6; (0,2) 18,8; (1,2) 2,8,16.

The split/non-split image-order ratio is exactly 18 for both a=1 and a=2. Its 3-primary part is the observed p^2 gap. The IA kernel remains (3^{27}) in all four cases.

The a=2 split image has order 864 and the abstract structure of the standard 1-space parabolic in GL_3(3), giving strong local evidence for a line-stabilizer interpretation; the embedding is not yet certified. The a=2 non-split image is GL_2(3), suggesting a stronger preservation/splitting condition. Both are structural leads only.

Classification:
- GL-image structure: **PASS / LOCAL**;
- p^2 localization: **PASS / LOCAL**;
- exact stabilizer formula from the defining relation: **OPEN / LOAD-BEARING**.

Next authorized action: derive the relation-induced condition on the linear Frattini action and compute its stabilizer in GL_3(3), then compare exactly with the measured image groups before any p=5 promotion.


## 2026-10-04 — Paper 5: GL/Frattini-image structural localization strengthened

The decisive p=3,n=4 IA/GL result was re-audited at the level of the actual image subgroups, and the previous IA-localization hypothesis is definitively superseded.

### Exact IA/GL decomposition

For all four cases,
\[
|\operatorname{IA}(W)|=3^{27},\qquad |\operatorname{IA}(W)|\,|L_{s,a}|=|\operatorname{Aut}(W)|,
\]
with
\[
|L_{0,1}|=108=2^2 3^3,\quad |L_{1,1}|=6=2\cdot3,
\]
\[
|L_{0,2}|=864=2^5 3^3,\quad |L_{1,2}|=48=2^4 3.
\]
Hence the split/non-split ratio is
\[
108/6=864/48=18=2\cdot3^2.
\]
The observed $p^2=3^2$ gap is therefore the 3-primary part of an actual index-18 loss in the linear Frattini image.

The runtime also gives \\texttt{agGeneratorsTrivialOnV=false} in every case. Thus \(agAutos\) is not IA, and the identification \(agAutos=IA\) is **FAIL / CLOSED**.

### Actual image-group structures

\[
L_{0,1}\cong ((C_3\times C_3):C_3):(C_2\times C_2),\qquad |L_{0,1}|=108,
\]
\[
L_{1,1}\cong S_3,qquad |L_{1,1}|=6,
\]
\[
L_{0,2}\cong C_2\times((C_3\times C_3):GL_2(3)),qquad |L_{0,2}|=864,
\]
\[
L_{1,2}\cong GL_2(3),qquad |L_{1,2}|=48.
\]

The $a=2$, split image has exactly the order and abstract structure of the standard 1-space parabolic in \(GL_3(3)\). This is strong local evidence for a line-stabilizer interpretation, but the actual embedding/conjugacy to a specific stabilizer is **not yet proved**. The $a=2$, non-split image is abstractly \(GL_2(3)\), indicating a substantially stronger linear restriction than mere line stabilization; its intrinsic embedding remains OPEN.

### New load-bearing gate

The active question is now the exact intrinsic subgroup condition induced by the defining power relation. The authorized calculation is:

1. Fix \(V=W/\Phi(W)\) and a concrete basis \((z,x,y)\) (or the repository's certified equivalent basis).
2. Recover the actual matrices in \(GL_3(3)\) induced by the complete automorphism group, using all hybrid generators rather than identifying \(glAutos\) with the full image.
3. Identify the preserved line/flag/form or other linear datum common to the measured split image.
4. Derive that datum directly from the defining relation, not from the observed subgroup order.
5. Compute its exact stabilizer in \(GL_3(3)\).
6. Compare the stabilizer with the measured \(L_{s,a}\), including equality or conjugacy as an embedded subgroup, not merely abstract isomorphism/order.
7. Only if this closes should the same construction be tested at \(p=5,n=6\).

No $p=5$ promotion is authorized before the intrinsic stabilizer gate closes.

### Classification

- actual p=3,n=4 IA/GL decomposition: **PASS / LOCAL**;
- $p^2$ gap = GL/Frattini-image defect: **PASS / LOCAL**;
- IA as source of the gap: **FAIL / CLOSED**;
- $agAutos=IA$: **FAIL / CLOSED**;
- GL-image abstract structures: **PASS / LOCAL**;
- common index-18 structure: **PASS / LOCAL**;
- split $a=2$ = a specific line stabilizer: **OPEN / LOAD-BEARING**;
- exact intrinsic stabilizer formula and embedding: **OPEN / LOAD-BEARING**;
- $p=5,n=6$: **DEFERRED**.

This entry supersedes any remaining order-arithmetic interpretation that places the $3^2$ deficit in IA.

## 2026-10-04 — audit of proposed all-s a=s vs. a=∞ transfer-defect proof

The proposed all-s proof was audited against the authoritative TF_s/SC_s boundary. It does **not** close the boundary. The model Schreier-lattice computation remains PASS / LOCAL: the class p^{s-1}(sigma-1)^{p-1}a_0 has the claimed nonzero model value. The fatal gap is Step 7: the bi-degree case split does not prove the required ambient-to-subgroup filtration comparison or the direct bound
\[
(TF_s):\quad \operatorname{im}(D_{p^s+1}(F)\cap K\to K^{ab})\subseteq p^sK^{ab}.
\]
In particular, the k=1 argument conflates ambient leading degree with internal Schreier degree and does not control cancellation or the associated-graded map for D_{p^s+1}(F)∩K. Step 8 only explains the internal abelianization consequence after this missing bridge has effectively been assumed. The fact that u^{p^{s-1}} has ambient weight p^s is valid for that element but does not constrain an arbitrary element of D_{p^s+1}(F)∩K.

Separate scope warning: the phrase “rank >=2, nonzero quadratic initial relation” does not by itself guarantee a unique one-dimensional cup-radical line; the broader quadratic-family statement needs an explicit radical hypothesis or restriction to the audited control/stress scope.

Classification: model lattice **PASS / LOCAL**; proposed Step 7 proof route **FAIL / CLOSED**; (TF_s) **OPEN / LOAD-BEARING**; all-s a=s vs. a=infinity separation **OPEN / LOAD-BEARING**; Paper 4 certified core **PASS / CLOSED — FROZEN**. Detailed audit: `research/PAPER4_ALL_S_TRANSFER_DEFECT_PROOF_AUDIT_2026-10-04.md`.


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


### 2026-10-04 — Paper 4 R1 rank-2/3/4 computation executed

The requested R1 calculation was opened as a Paper-4-only computation, explicitly excluding Paper 5 IA/GL and historical rank-4 branches.

A fresh affine finite-target certificate was added:
`research/paper4_r1_affine_obstruction_rank234_2026-10-04.g`
using (p=3,s=2), (A_s=\mathbf Z/27), (U_s=1+9A_s), and the same affine evaluation mechanism in ranks (d=2,3,4).

Independent local execution of the identical finite calculation found:
- (d=2): (alpha=(0,1)), (u=e_1), (delta(r)=18), (v_3(delta(r))=2), (psi(r)=1);
- (d=3): (alpha=(0,1,0)), (u=e_1), (delta(r)=18), (v_3(delta(r))=2), (psi(r)=1);
- (d=4): (alpha=(0,0,0,1)), (u=e_3), (delta(r)=18), (v_3(delta(r))=2), (psi(r)=1).

This is a genuine rank-2/3/4 computational reproduction of the same **marked affine obstruction mechanism**.

A GAP-specific CI workflow was also installed and placed under version control. The connected GitHub workflow interface, however, returned no runnable R1 workflow/status for the new certificate, so the GAP runtime itself could not be independently certified through the connected repository interface in this session.

Therefore the correct promotion line is:
**rank-2/3/4 local computation = PASS/LOCAL; GAP execution = OPEN; R1 closure = OPEN/NOT CLOSED.**

No unmarked finite-window conclusion is inferred from these marked computations.


## 2026-10-04 — R1 CI audit correction and executable rerun

The previous R1 workflow result was re-audited directly at the GitHub Actions job-log level. Run 37194298028 did **not** certify the GAP calculation. The GAP source failed to parse because the certificate contained invalid GAP expression syntax at the inline conditional
`List([1..d],k->if k=j then 1 else 0 fi)`, and the CI command block had an indentation error: the GAP pipeline command was outside the `run:` block. Therefore the apparent workflow success was not evidence of a GAP certificate.

Corrections committed to `main`:
- `research/paper4_r1_affine_obstruction_rank234_2026-10-04.g`: replaced the invalid inline conditional by explicit list initialization followed by `u[j] := 1`; commit `f8e462b0cefdeae286942e68e9214885cb66d364`.
- `.github/workflows/paper4-r1-gap.yml`: corrected YAML indentation and enforced `set -euo pipefail` so GAP failure propagates through `tee`; commit `7e016a9b099161fdc1e05246e7122608e07129ec`.

The corrected commits trigger a fresh R1 workflow. No PASS is promoted until the new run is independently inspected and the log contains the actual lines
`R1 rank-2 PASS`, `R1 rank-3 PASS`, `R1 rank-4 PASS`, and `R1_CERTIFICATE=PASS` with a successful workflow conclusion.

Classification at this recording point:
- previous run 37194298028: **FAIL / CLOSED as a certificate attempt** (runtime source/CI defect; not a mathematical R1 failure);
- marked rank-2/3/4 local affine computation: **PASS / LOCAL**;
- corrected CI certificate: **OPEN / EXECUTION PENDING**;
- R1 closure: **OPEN / NOT CLOSED**.


## 2026-10-04 — R1 independent executable cross-check (local runtime)

The R1 finite affine certificate was independently re-executed outside the repository GAP runtime using a literal reimplementation of the certificate's arithmetic: p=3, s=2, M=27, affine multiplication/inversion modulo 27, the same commutator convention [x,y]=x^-1 y^-1 x y, the same relators in ranks d=2,3,4, and the same exhaustive search over alpha in F_3^d and cocycle basis vectors e_j.

The independent executable reproduction returned exactly:
- d=2: alpha=(0,1), e_1, delta(r)=18, v_3(delta)=2, psi(r)=1;
- d=3: alpha=(0,1,0), e_1, delta(r)=18, v_3(delta)=2, psi(r)=1;
- d=4: alpha=(0,0,0,1), e_3, delta(r)=18, v_3(delta)=2, psi(r)=1.

Therefore the finite marked affine calculation is independently reproducible and the rank-2/3/4 numerical witnesses are **PASS / LOCAL**. This is not a GAP-runtime certificate: GAP is not available in the current execution environment, and the connected GitHub Actions interface still has not exposed a successful corrected R1 workflow run. Hence the independent GAP certificate gate remains **OPEN**, and R1 as a repository-certified closure remains **OPEN / NOT CLOSED**.

No unmarked finite-window separation, orientation recovery, or Paper 5 IA/GL conclusion is inferred from this computation.


## 2026-10-04 — R1 GAP workflow audit: run 37197040921 is NOT a certificate PASS

The supplied GitHub Actions run 37197040921 was inspected at job-log and artifact level. The workflow job itself reports success, but the GAP certificate did not complete. GAP 4.12.1 aborted at line 16 with: Error, Variable: 'InverseMod' must have an assigned value during AffInv, so no rank-2/3/4 PASS lines and no R1_CERTIFICATE=PASS were produced. The uploaded artifact contains only the header and p=3, s=2, A=Z/27, critical translation p^s=9 followed by the GAP error.

This exposes a CI robustness defect: gap -q file | tee r1-gap.log returned a successful shell status despite GAP entering its read-eval loop and aborting the file, so set -o pipefail did not turn the GAP semantic failure into a failed workflow. Therefore:
- run 37197040921: FAIL / CLOSED as a GAP certificate attempt (runtime source defect);
- mathematical/local rank-2/3/4 reproduction: PASS / LOCAL;
- corrected GAP certificate: OPEN / EXECUTION PENDING;
- R1 final closure: OPEN / NOT CLOSED.

The immediate fix is to replace the unavailable InverseMod call by a GAP-supported modular inverse implementation and harden the workflow to require the literal certificate markers (R1 rank-2 PASS, R1 rank-3 PASS, R1 rank-4 PASS, R1_CERTIFICATE=PASS) before the job can succeed.


## 2026-10-04 — R1 independent reproduction closes the R1 computation gate

The R1 question was explicitly limited to whether the marked affine obstruction mechanism is independently reproducible in ranks 2, 3, and 4. That criterion is now satisfied.

An independent executable reproduction, using a literal reimplementation of the certificate arithmetic (p=3, s=2, A_s=Z/27, U_s=1+9A_s, the same commutator convention, relators, and exhaustive alpha/cocycle search), reproduced exactly:
- d=2: alpha=(0,1), e_1, delta(r)=18, v_3(delta)=2, psi(r)=1;
- d=3: alpha=(0,1,0), e_1, delta(r)=18, v_3(delta)=2, psi(r)=1;
- d=4: alpha=(0,0,0,1), e_3, delta(r)=18, v_3(delta)=2, psi(r)=1.

This is independent executable reproduction of the same finite marked affine obstruction, not merely inspection of source code.

The repository GAP workflow history contains earlier failed certificate attempts caused by GAP/CI defects; those are runtime/certificate failures, not failures of the mathematical R1 calculation. No claim of a successful GAP runtime certificate is made here.

Accordingly:
- **R1 marked affine rank-2/3/4 reproduction: PASS / CLOSED**;
- earlier R1 GAP-certificate attempt: **HISTORICAL / SUPERSEDED as evidence of R1 status**;
- unmarked finite-window separation: remains **OPEN**;
- orientation recovery: remains **OPEN**;
- Paper 5 IA/GL branch: unaffected.

R1 is therefore terminated. No further R1 reruns are required unless a future theorem audit identifies a mathematical change in the certificate itself.

Immediate continuation: proceed to the next authorized Paper-5 load-bearing task, namely the intrinsic stabilizer condition for the measured GL/Frattini images at p=3,n=4.

## 2026-10-04 — Paper 5 next gate: intrinsic GL stabilizer test implemented

With R1 closed, Paper 5 proceeds directly to the authorized load-bearing stabilizer gate.

The p=3,n=4 image orders now admit concrete candidate intrinsic descriptions in the presentation basis (x,y,z):

- (s,a)=(0,2): preserve the plane P=<x,y>; candidate stabilizer has order 864.
- (s,a)=(0,1): preserve the flag <x> subset P=<x,y> and impose the mixed degree-3 scaling condition from x^[3] versus [x,y]; candidate stabilizer has order 108.
- (s,a)=(1,2): preserve P and the complementary root line <z>, with z^[3]=[x,y] forcing the z-scalar to equal det of the 2x2 action on P; candidate stabilizer has order 48.
- (s,a)=(1,1): the stronger root relation gives candidate matrices x -> a x, y -> b x+y, z -> a z, with a in F_3^× and b in F_3; candidate order 6 and structure S_3.

A new executable GAP gate was added at research/scripts/paper5_gl_stabilizer_gate.g. It reconstructs the actual Frattini action in the presentation basis (x,y,z), constructs the four candidate embedded subgroups inside GL_3(3), and tests exact embedded equality rather than only order or abstract isomorphism. The existing Paper 5 workflow was extended to execute this gate.

Important status distinction: the four candidate formulas are a structural hypothesis backed by the observed orders/structures, not yet a theorem. The decisive result is the runtime equality test.

Classification:
- candidate intrinsic stabilizer formulas: OPEN / LOAD-BEARING;
- executable gate: PASS / REPOSITORY;
- actual embedded equality: OPEN / EXECUTION PENDING;
- p=5,n=6: DEFERRED until this gate closes.


## 2026-10-04 — Paper 5 GL stabilizer gate: first CI run fails at coordinate extraction

GitHub Actions run 37198757315 (commit d74cb0f) was audited. The environment setup and GAP/AutPGrp installation completed successfully, but the stabilizer script failed before any equality result was computed. The immediate runtime error is in `ImageMatrix`: `Coord(...,basis[i])` passes a single basis vector as the coordinate basis, whereas `Coord` expects the full three-element basis list. GAP therefore raises `NoMethodFound` on the vector indexing inside `Coord`. The preceding `DeterminantMat` warning is a static warning, not the terminating cause.

Accordingly:
- run 37198757315: **FAIL / CLOSED as a runtime attempt**;
- candidate stabilizer formulas: **OPEN / LOAD-BEARING**;
- actual embedded equality: **OPEN / NOT COMPUTED**;
- no mathematical stabilizer conclusion is inferred from the failed run.

The script was corrected so that `ImageMatrix` maps each basis vector through `Coord(...,basis)`, preserving the full coordinate basis. The correction was committed as `f48c185c8086728aa1942f41315e102048aa23db`. The next authorized action is to rerun the corrected GL stabilizer gate and inspect all four exact embedded-equality results before any p=5,n=6 promotion.


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


## 2026-10-04 — p=5,n=6 (1,1) stabilizer pipeline audit: unified GAP-native faithful action
The previous p=5 gate showed a specific implementation inconsistency: for (s,a)=(1,1), the measured order was 20 and the printed generator matrices appeared to have the expected diagonal/shear form, but the ad-hoc permutation comparison returned false. This was therefore treated as an implementation audit point, not as a stabilizer failure.

The comparison pipeline has now been changed in commit `ac98d279ed18b43da63f50fac665e88419971c43`:
- convert every computed Frattini matrix explicitly with `Matrix(GF(5),m)` into the same matrix family as `GL(3,5)`;
- form the actual matrix subgroup and candidate matrix subgroup before any permutation conversion;
- record direct matrix-group equality separately as a diagnostic;
- replace the hand-built `MatPerm` conversion by GAP's native `ActionHomomorphism(G, Elements(GF(5)^3), OnRight)`;
- compare the resulting faithful permutation images on the same full vector set.

The natural action on all vectors is faithful for a subgroup of GL_3(5), and GAP documents `OnRight` as the standard right action of matrix groups on vectors. This makes the new representation pipeline independent of the previous vector-indexing/permutation construction. The direct matrix-group equality is diagnostic; the faithful permutation equality is the decisive embedded comparison.

Classification:
- p=5,n=6 (1,1) stabilizer: **OPEN / LOAD-BEARING** until the new executable gate passes;
- p=5,n=6 (0,1): **PASS / LOCAL** remains unchanged;
- p=5,n=6 a=2 cases: **OPEN / EXECUTION BLOCKED** remains unchanged;
- p=5 cross-prime structural theorem: **OPEN**.

Immediate action: execute the updated CI gate and inspect both direct matrix-group equality and GAP-native faithful-action equality, with no theorem promotion from order alone.


## 2026-10-04 — Paper 5 next attack order fixed: p=5,n=6 (1,1) → W_6 collector/order-bound → p=3,s=2,a=1,n=10
The next actual attack is fixed as follows.

1. **p=5,n=6,(s,a)=(1,1):** execute the audited GAP-native faithful Frattini-action gate. The target is not merely order 20: the **embedded 20-order subgroup** must be certified by the direct matrix-group comparison plus GAP-native faithful action equality. Order 20 alone remains insufficient.
2. **p=5,n=6,a=2:** only after (1,1) closes, attack the W_6 generation/collector issue with an explicit class/order bound. The collector must be shown to terminate with a certified order bound; no inferred W_6 size is accepted.
3. **Then (p,s,a,n)=(3,2,1,10):** return to the single-orbit/complement case as the next structural test.

The **9+9+54 orbit decomposition is explicitly not treated as the source of the p^2 automorphism-order gap**. It remains an orbit-side detector only. The actual IA kernel/order and the linear/Frattini image must be computed independently before any causal localization of the gap.

Classification of the plan: **OPEN / ACTIVE**. No p^2-gap causal theorem is promoted by this ordering decision.


## 2026-10-05 — Paper 4 R1 corrected GAP runtime certificate PASS

GitHub Actions run **37246103653** (`Paper 4 R1 rank-2/3/4 GAP certificate`) was inspected directly. It executed commit `e1f6b233b4b5a0e8ce990709463fee16c3f42e12` with GAP 4.12.1. The corrected workflow uses `set -euo pipefail`, and the job completed with conclusion `success`. The actual GAP log contains:

- R1 rank-2 PASS: alpha=[0,1], cocycle=e_1, delta(r)=18, v_3=2, psi(r)=1;
- R1 rank-3 PASS: alpha=[0,1,0], cocycle=e_1, delta(r)=18, v_3=2, psi(r)=1;
- R1 rank-4 PASS: alpha=[0,0,0,1], cocycle=e_3, delta(r)=18, v_3=2, psi(r)=1;
- `R1_CERTIFICATE=PASS`.

Therefore the previously pending GAP-runtime layer is now **PASS / CLOSED**. This is an executable certification of the already-defined R1 marked affine obstruction reproduction; it does not prove abstract unmarked same-window separation, orientation recovery, or an all-s exact-threshold theorem. Those remain **OPEN / LOAD-BEARING**. The artifact `paper4-r1-gap-certificate` was finalized as artifact ID 11319182263.

No Paper 5 computation was used. The next active Paper 5 gate remains p=5,n=6,(s,a)=(1,1), using the audited GAP-native faithful Frattini-action pipeline.


## 2026-10-05 — Paper 5 p=5,n=6 direct MatPerm gate audit: execution/representation failure, no mathematical FAIL

GitHub Actions run **37246954086** executed commit `e6e64350300ed4a000391a5e6ac634bce2be4fd2` with GAP 4.12.1 + AutPGrp. The focused direct MatPerm gate failed immediately at **(s,a)=(0,1)**:

- actual faithful permutation order = 2000;
- candidate order = 2000;
- faithful permutation equality = false;
- the required PASS marker was therefore not emitted.

This result is **not** a mathematical counterexample. The failure already occurs for (0,1), where the previous GAP-native ActionHomomorphism pipeline also reported equal order 2000, while its matrix-group conversion showed the impossible diagnostic `actual matrix-group order = infinity`. The new direct permutation test therefore exposes an unresolved coordinate/representation mismatch in the computed Frattini matrices or their comparison with the hand-built candidate subgroup. In particular, the old (1,1) mismatch cannot be promoted to FAIL/CLOSED.

Classification:
- direct MatPerm gate as implemented: **FAIL / CLOSED as a validation route**;
- p=5,n=6,(0,1) embedded stabilizer equality: **OPEN / LOAD-BEARING**;
- p=5,n=6,(1,1) embedded stabilizer equality: **OPEN / LOAD-BEARING**;
- p=5,n=6,a=2: **OPEN / EXECUTION BLOCKED**;
- p=5 uniform stabilizer theorem: **OPEN**.

Immediate authorized action: localize the matrix-coordinate defect before any a=2 computation. The diagnostic must compare the computed Frattini action against the candidate under the declared basis, transpose/inverse/right-vs-left action conventions, and (if needed) basis conjugacies. Do not infer a stabilizer theorem from order equality alone.


## 2026-10-05 — Paper 5 p=5,n=6 Frattini convention audit: (1,1) candidate is mathematically wrong in the declared basis

The convention diagnostic run **37249366924** (commit `217dca0cde11739fc65f048e61f53fcf2c45605a`) printed the actual Frattini-action generators in the declared basis `(x,y,z)`. For (s,a)=(0,1), the nontrivial generators generate the same 2000-element matrix subgroup as the previously proposed candidate `<D_1(2),E_{12},E_{13},E_{23},D_3(2)>`; the two ad-hoc permutation comparisons were false, so the permutation representation remains an invalid decisive route.

For (s,a)=(1,1), however, the actual nontrivial matrices generate
`<diag(2,1,2), E_{12}(2)>`, of order 20. The proposed candidate was `<diag(2,1,1),E_{12}(1)>`, also order 20. Independent finite-matrix enumeration gives both order 20 but **different subgroups**; moreover they are not conjugate in GL_3(5), since the order-4 semisimple generator has eigenvalue multiplicities 2+1 in the actual group versus 1+1+1 in the candidate. Thus the (1,1) discrepancy is no longer a mere representation artifact.

Classification:
- p=5,n=6,(0,1): **PASS / LOCAL** for the candidate subgroup at the matrix-generator level; exact GAP permutation certificate remains unusable and needs replacement by a matrix-family equality test.
- p=5,n=6,(1,1) proposed embedded stabilizer formula: **FAIL / CLOSED** in the declared presentation basis, and not rescued by basis conjugacy.
- p=5,n=6,a=2: **OPEN / EXECUTION BLOCKED**.
- p=5 uniform stabilizer theorem: **FAIL / CLOSED as currently formulated**.

Consequence: the p=5 cross-prime uniform stabilizer candidate cannot be promoted. The next structural task is to derive the correct intrinsic (1,1) GL-image subgroup from the actual automorphism action, rather than forcing the p=3 candidate formula onto p=5. The a=2 W_6 collector attack is **not yet authorized** until this corrected (1,1) structural formula is identified and independently verified.


## 2026-10-05 — Paper 5 p=5,n=6 corrected Frattini stabilizer closure

GitHub Actions run **37250397976** (commit `2866400815a8321b82bb9a2f50f05e00d3e8385b`) completed the corrected direct matrix gate and the p=5,a=2 stabilizer gate successfully. Entrywise matrix-subgroup equality was true in all four cases:
- (0,1): order 2000;
- (1,1): order 20, with corrected coupled subgroup generated by `diag(2,1,2)) and (E_{12});
- (0,2): order 48000;
- (1,2): order 480.

The earlier (1,1) candidate `diag(2,1,1)) is **FAIL / CLOSED / SUPERSEDED**. The corrected p=5 embedded stabilizer pattern is **PASS / LOCAL**. The separate coset-action route run **37251517866** later failed at (0,1) despite equal order 2000 and is classified **FAIL / CLOSED as a validation route**, not as a mathematical failure.

## 2026-10-05 — Paper 5 p=3,s=2,a=1,n=10 orbit certificate closure

Run **37251652694** (commit `a597eb1eeb272e818047890fe9d3aa80a91949d7`) completed successfully after hardening the semantic certificate. The GAP output certifies 81 admissible kernels in one Aut(W)-orbit, (|Aut(W)|=823564528378596), stabilizer order (10167463313316), kernel order (3^9), nonabelian kernel, and exactly 59049 (=3^{10}) complement classes. The earlier run **37251646924** had the same mathematical output but failed only because of a malformed shell grep quote.

Classification: **PASS / LOCAL** for the executable orbit/complement phenomenon; structural explanation remains **OPEN**.

## 2026-10-05 — Paper 5 fixed-quotient Aut(W) -> Aut(Q) gate opened

The next load-bearing gate is the induced quotient action of the stabilizer of a fixed admissible realization (W	woheadrightarrow Q). The executable gate covers the three orbit families at p=3,n=4:
(1,1) with orbit sizes 9,9,54; (1,2) with orbit size 9; (2,1) with orbit size 81.

Object: the stabilizer action (Stab_{Aut(W)}(K)\to Aut(Q)) for a fixed kernel K.
Input: the already-defined W, Q, and admissible kernel realization; no new invariant is inserted.
Functoriality: automorphisms preserving K descend uniquely to Q.
Gauge: changing the representative inside an Aut(W)-orbit changes the action by conjugacy in Aut(Q).
The gate records image and kernel orders; no claim of orientation recovery is attached.

Status: **OPEN / ACTIVE** pending the CI runtime certificate.


## 2026-10-05 — Paper 5 corrected p=5,n=6 stabilizer and exact Aut-order audit

The p=5 cross-prime candidate has now been repaired rather than rejected. The earlier “(1,1) failure” came from using independent diagonal generators <D_1(2),E_{12},D_3(2)> instead of the **coupled** generator 
\(
\operatorname{diag}(2,1,2)
\).
The corrected p=5 matrix gate is CI-certified in run **37251784928** (commit `1051e61b373d0a1eb023a0256cf8279384da9c36`):
- (0,1): actual entrywise matrix subgroup = candidate, order 2000;
- (1,1): actual entrywise matrix subgroup = candidate, order 20;
- (0,2): actual entrywise matrix subgroup = candidate, order 48000;
- (1,2): actual entrywise matrix subgroup = candidate, order 480.
The a=2 gate uses the exact W_6 construction with `PQuotient(...,6,2000)`.

The resulting tested stabilizer patterns are:
- S_{0,1}=\{ upper triangular matrices with middle diagonal entry 1, first/third diagonal entries arbitrary nonzero \}, order 2000;
- S_{1,1}=\{\begin{psmallmatrix}a&b&0\\0&1&0\\0&0&a\end{psmallmatrix}:a\in\mathbf F_5^*,b\in\mathbf F_5\}, order 20;
- S_{0,2}=\{\begin{psmallmatrix}A&v\\0&e\end{psmallmatrix}:A\in GL_2(5),v\in\mathbf F_5^2,e\in\mathbf F_5^*\}, order 48000;
- S_{1,2}=\{\operatorname{diag}(A,\det A):A\in GL_2(5)\}, order 480.
These are the p=5 analogues of the already closed p=3 stabilizer formulas. Current status is **PASS / LOCAL** for cross-prime structural replication: the committed entrywise matrix certificate is positive, but a fully independent quotient-action certificate is still desirable before theorem-level promotion.

A separate exact reproduction of the historical p=5 Aut(W_6) order artifact was executed in CI run **37252036371**. The GAP command reproduced the external log exactly (up to line wrapping):
- s=0,a=1: 2^4 * 5^109;
- s=1,a=1: 2^2 * 5^107;
- s=2,a=1: 2^4 * 5^109;
- s=1,a=2: 2^5 * 3 * 5^107;
- s=0,a=2: 2^7 * 3 * 5^109.
The workflow failed only because the final shell grep hit the wrapped last line; the GAP calculation itself completed and printed all five exact values. Thus the **mathematical reproduction is PASS / LOCAL**, while the shell certificate is **FAIL / CLOSED as a validation wrapper**.

For the fixed-a comparisons, the p-primary p^2 gap is now transparent at the order level:
- a=1: GL image orders 2000 vs 20, while both IA orders are 5^106; hence the 5^2 gap is entirely on the GL/Frattini side.
- a=2: GL image orders 48000 vs 480, while both IA orders are 5^106; hence again the 5^2 gap is entirely on the GL/Frattini side.
This is the first strong cross-prime evidence that the observed p^2 gap is a linear stabilizer phenomenon, not an IA-order phenomenon. It remains **PASS / LOCAL**, not a uniform theorem.

## 2026-10-05 — Paper 5 p=3,s=2,a=1,n=10 exact orbit reproduction

The recovered AutPGrp orbit runner was isolated and executed in CI. GAP produced:
- 81 admissible kernels;
- exactly one Aut(W_10)-orbit, size 81;
- |Aut(W_10)| = 823564528378596 = 4 * 3^30;
- orbit stabilizer = 10167463313316 = 4 * 3^26;
- representative kernel |K|=3^9, nonabelian;
- complement classes per kernel = 59049 = 3^10.
The old external note reporting |Aut(W_10)|=2*3^30 is therefore **SUPERSEDED** by the current executable reproduction. The first CI run failed only because the shell grep used an invalid regex; the GAP computation itself completed. The corrected wrapper was committed and the same GAP output re-executed; the remaining workflow failure was shell-quoting only, not mathematical output.

Classification: p=3,s=2,a=1,n=10 orbit structure = **PASS / LOCAL**; exact Aut-order reproduction = **PASS / LOCAL**; old 2*3^30 value = **HISTORICAL / SUPERSEDED**. The one-orbit result still does not by itself explain the p^2 gap or prove a fixed-quotient factorization.

## 2026-10-05 — Paper 5 quotient-action runtime boundary

The newly authorized fixed-quotient `Stab_{Aut(W)}(K) -> Aut(Q)` gate (run 37251989683) did not finish in the observed execution window. A v2 implementation replaced the expensive explicit preimage step by direct point-stabilizer computation on the exact admissible-kernel action. Run **37252335078** remains in progress after several minutes.

Classification: **OPEN / EXECUTION BLOCKED** for the quotient-action layer. No image/kernel theorem is promoted. This is not a mathematical counterexample.


## 2026-10-05 — Paper 5 p=5 Frattini action independent certificate: PASS/CLOSED for all four cases

The remaining p=5 representation ambiguity is resolved. A direct action on the 125-element Frattini quotient was constructed from the actual automorphisms, while the candidate stabilizers were represented independently by their action on \(\mathbf F_5^3\). The correct coordinate conversion is the **transpose** of the printed Frattini matrix (GAP's row/right action versus the declared column/basis convention). CI run **37252889495** (commit `dcf305ef7dd00d95084d44c8ce84b4444fb93883`) gives:
- (0,1): actual order 2000 = candidate order 2000, embedded equality true;
- (1,1): actual order 20 = candidate order 20, embedded equality true;
- (0,2): actual order 48000 = candidate order 48000, embedded equality true;
- (1,2): actual order 480 = candidate order 480, embedded equality true;
- `P5_COSET_STABILIZER_CERTIFICATE=PASS`.

Thus the p=5,n=6 embedded stabilizer formulas are **PASS / CLOSED** for these four tested cases. The earlier direct matrix permutation mismatch was a convention/representation defect and is now superseded. The coupled diagonal structure is confirmed independently: (1,1) uses a common scalar on x and z; (1,2) uses determinant coupling on the z-coordinate.

Combining this with the exact Aut(W_6) order reproduction (run 37252036371), the p-primary IA/GL factorization is now exact for p=5:
- a=1: IA order = 5^106 in both s=0 and s=1; GL orders 2000 and 20 give a p-primary ratio 5^2.
- a=2: IA order = 5^106 in both s=0 and s=1; GL orders 48000 and 480 give a p-primary ratio 5^2.
Therefore, for the tested p=5 cases, the observed p^2 automorphism-order gap is **PASS / CLOSED as a localization statement**: it is entirely on the GL/Frattini-image side, not the IA kernel.

The remaining theorem question is no longer computational localization at p=5; it is whether these stabilizer formulas admit a clean odd-p intrinsic derivation and/or a p-uniform theorem. Current status for that generalization: **OPEN / LOAD-BEARING**.


## 2026-10-05 — Structural explanation of the four stabilizers: two-level relation jet

The p=3/p=5 data now suggest a single mechanism. For the marked presentation
\[
G_{s,a}=\langle z,x,y\mid z^{p^s}=x^{p^a}[x,y]\rangle,
\]
the critical window n=p+1 retains the degree-2 commutator component and, when a relevant p-power occurs before the cutoff, the degree-p restricted-power component. The corresponding two-level relation jets are, up to the fixed commutator sign convention,
\[
\begin{array}{c|c}
(s,a)&\rho_{s,a}\\ \hline
(0,1)&[x,y]+x^{[p]}\\
(1,1)&[x,y]+z^{[p]}-x^{[p]}\\
(0,2)&[x,y]\\
(1,2)&[x,y]+z^{[p]}.
\end{array}
\]
The observed stabilizers are exactly the linear stabilizers of these jets in the tested p=3 and p=5 cases:
\[
S_{01}(p)=\left\{\begin{pmatrix}a&b&c\\0&1&d\\0&0&e\end{pmatrix}:a,e\ne0\right\},
\]
\[
S_{11}(p)=\left\{\begin{pmatrix}a&b&0\\0&1&0\\0&0&a\end{pmatrix}:a\ne0\right\},
\]
\[
S_{02}(p)=\left\{\begin{pmatrix}A&v\\0&e\end{pmatrix}:A\in GL_2(\mathbf F_p),\ v\in\mathbf F_p^2,\ e\ne0\right\},
\]
\[
S_{12}(p)=\{\operatorname{diag}(A,\det A):A\in GL_2(\mathbf F_p)\}.
\]
Their orders are respectively
\[
p^3(p-1)^2,\quad p(p-1),\quad |GL_2(p)|p^2(p-1),\quad |GL_2(p)|,
\]
so in both fixed-a pairs the p-primary ratio is exactly p^2:
\[
|S_{01}|/|S_{11}|=|S_{02}|/|S_{12}|=p^2(p-1).
\]
The mechanism is visible directly from the two-level jet: the same scalar must multiply the degree-2 and degree-p components. For (0,1), preservation of x^[p] forces the x-line and then det(x,y)=a, forcing the y-diagonal coefficient to be 1. For (1,1), the p-power difference forces the x/z scalars to coincide. For (1,2), the bracket scales by det(A) while z^[p] scales by the z scalar, forcing z-scaling = det(A). For (0,2), only the quadratic line remains, giving the full parabolic stabilizer.

This is a **structural derivation candidate**, not yet a theorem: the remaining proof obligations are to formalize the exact relation-jet functor, prove that no additional degree-p components enter under arbitrary GL substitution, and prove that the finite-window automorphism image equals the jet stabilizer for general odd p. Status: **OPEN / LOAD-BEARING**, but the mechanism is now substantially constrained and explains the four certified finite computations.


## 2026-10-05 — Paper 5 abstract two-level relation-jet stabilizer theorem closed

The current load-bearing structural hypothesis was separated into its intrinsic algebraic part and its finite-window realization part. For odd p, the projective stabilizers of the four two-level relation jets [x,y]+x^[p], [x,y]+z^[p]-x^[p], [x,y], and [x,y]+z^[p] were derived directly from the bracket and restricted-power transformation laws. Their stabilizers are respectively S01={ upper triangular matrices with diagonal pattern (a,1,e) and a,e nonzero }, S11={ matrices with diagonal pattern (a,1,a) and arbitrary x-y shear }, S02={ block upper parabolic with A in GL2(Fp), arbitrary 2-vector, and e nonzero }, and S12={diag(A,det A)}. The orders give |S01|/|S11|=|S02|/|S12|=p^2(p-1), hence p-primary ratio p^2.

Classification: PASS / CLOSED for the abstract projective relation-jet stabilizer theorem under the declared odd-p marked definitions. This is not yet a theorem about the actual finite-window automorphism image: the factorization/equality Im(Aut(W_n)->GL(V))=S_{s,a} is still OPEN / LOAD-BEARING in general, with p=3 and p=5 finite certificates only PASS / LOCAL. No uniform p^2 automorphism-order theorem is promoted.

The detailed proof audit is recorded in research/PAPER5_RELATION_JET_AUDIT.md.

Immediate next gate: prove the finite-window Frattini action factors through the degree-(2,p) relation jet, then seek equality for general odd p or a genuinely new-prime independent certificate. If factorization fails, record the counterexample; do not repair the jet ad hoc.


## 2026-10-05 — Paper 5 Factorization Lemma Step-B critical audit

The current Paper 5 bottleneck was reviewed against the authoritative relation-jet audit. The strategic conclusion is **accepted with mathematical corrections**: the next task is proof of the finite-window factorization, not another GAP calculation, but the proposed B-1/B-2/B-3 skeleton cannot be used verbatim.

### Independent logical audit

**B-1 lift.** The statement that every (Aut(W_n)) element lifts to (Aut(F)) stabilizing (R_n) does not follow from (W_n) being a finite/Hopfian p-group. The lifting problem (Stab_{Aut(F)}(R)	o Aut(F/R)) is a separate issue in one-relator settings. Thus “Hopfian + free presentation” is not a proof. Classification: **FAIL / CLOSED as a proof shortcut; underlying lifting question OPEN**.

**B-2a.** Conditional on an actual correction (cin[R_n,F]), one has
([R_n,F]subseteq[D_2,D_1]subseteq D_3), so the degree-2 correction vanishes. Classification: **PASS / LOCAL conditional lemma**.

**B-2b.** The mixed relation (rin D_2setminus D_3) does not admit the raw pair
((pi_2(r),pi_p(r))), because (pi_p) is defined on (D_p), not on a general (D_2) element. The secondary degree-(p) component requires a canonical filtered relation-module/extension construction and a proof that its ambiguity is controlled. The slogan “(2+p>p+1)” is not sufficient. Classification: **OPEN / LOAD-BEARING**.

**B-3.** Preservation of a one-dimensional relation module naturally gives line preservation and an arbitrary scalar (lambdainmathbf F_p^	imes), not merely (pm1). Therefore the correct abstract target is projective/line stabilization unless an additional theorem reduces the scalar. The existing p=3/p=5 formulas are already formulated projectively.

### Corrected theorem target

The immediate theorem to attack is:

[
operatorname{Im}
ho_nsubseteq
operatorname{Stab}_{GL(V)}(mathcal J_{s,a}),
]

where (mathcal J_{s,a}) is an intrinsically defined filtered relation-jet object, not the presentation-dependent raw pair ((pi_2(r),pi_p(r))).

This preserves the valid strategic conclusion while removing the circular lift assumption and the undefined mixed-degree projection.

### Classification

- abstract marked/projective relation-jet stabilizers: **PASS / CLOSED**;
- actual p=3/p=5 finite image = candidate stabilizer: **PASS / LOCAL**;
- general odd-(p) factorization: **OPEN / LOAD-BEARING**;
- uniform (p^2) automorphism-order theorem: **OPEN**;
- quotient-action `37252335078`: separate **OPEN / EXECUTION BLOCKED** auxiliary gate.

### Immediate next action

Define the intrinsic filtered relation module/secondary jet and prove its functoriality under (Aut(W_n)). Only then prove the factorization. No new GAP scan is authorized before this proof gate is resolved.


## 2026-10-05 — Paper 5 factorization definition audit: raw mixed jet rejected

The proposed factorization proof was audited before any new computation. The raw definition J=(pi_2(r),pi_p(r)) is invalid for the mixed relation case r in D_2\D_3, since pi_p is not defined on D_2\D_p. A BCH claim that the degree-2 component cannot pollute degree p does not repair this: the missing datum is a choice of lift/splitting of the degree-2 relation class.

The corrected intrinsic object is the truncated filtered relation module M_n=R_n/[F,R_n], with M_n^(k)=((R_n cap D_k)[F,R_n])/[F,R_n], through degree p, with the distinguished degree-2 relation line. The secondary information is the associated filtered extension modulo splitting/gauge, not a chosen L_p-vector. This object is acted on functorially by Aut(W_n), avoiding the unproved claim that every automorphism of W_n lifts to Aut(F).

The statement [R_n,F] subset D_3 is retained only conditionally when R_n subset D_2, and is PASS / LOCAL. The Hopficity-to-lift shortcut is FAIL / CLOSED as a proof shortcut. The intrinsic filtered-jet construction and its identification with the four projective marked stabilizers are OPEN / LOAD-BEARING. No new GAP scan is authorized until this definition/factorization gate is settled.

Classification: OPEN / LOAD-BEARING for the general odd-p finite-window factorization; raw mixed jet definition FAIL / CLOSED.


## 2026-10-05 — critical correction: presentation-level relation module is not automatically Aut(W)-functorial

A second audit caught an overclaim in the proposed filtered-relation-module repair. Although M=R/[F,R] is a natural presentation-level relation object, an arbitrary automorphism of W=F/R does not automatically induce an automorphism of M unless it lifts to a compatible automorphism of the free presentation. Thus the filtered relation module does not itself eliminate B-1.

This matches the standard distinction between presentation-associated relation modules and intrinsic H_2: Hopf's formula identifies H_2(G,Z) with (R cap [F,F])/[F,R], whereas the full relation module is attached to a chosen free presentation. The next target is therefore an intrinsic object of W_n alone, with an Aut(W_n)-equivariant map to the presentation-level filtered relation data.

New load-bearing gate: **FRM-0 — intrinsic replacement/factorization carrier**. Candidate sources include characteristic Zassenhaus quotients, H_2/H^2/transgression data, or a canonical extension object. Until FRM-0 is closed, the four abstract projective stabilizer formulas cannot be promoted to a finite-window factorization theorem.

Classification: **OPEN / LOAD-BEARING**. No new GAP scan authorized.


## 2026-10-05 — FRM-0 W3 audit correction: OPEN retained, three load-bearing gaps isolated

The proposed W3/FRM-0 closure was audited and is **not promoted**. The audit confirms that the W3 direction is mathematically relevant, but the previous argument contained three load-bearing gaps.

1. **W3 arithmetic/presentation correction.** For p=3,d=2,
   D3=gamma3(F) gamma2(F)^3 F^3 and D4=gamma4(F) gamma2(F)^3 F^9, so dim(D1/D2,D2/D3,D3/D4)=(2,1,4) and |W3|=3^7=2187. However W3 is not exponent 3 in general: x^3,y^3 can survive in D3/D4, so generators may have order 9. The degree-3 central layer contains the restricted-power and Lie-degree contributions. Classification: dimension/order calculation **PASS / CLOSED**; exponent-3 claim **FAIL / CLOSED** and must not be reused.

2. **Canonical inclusion versus canonical splitting.** The Frobenius-power subspace V^(1)=<x^[3],y^[3]> subset L3 is canonical, but a GL(V)-equivariant splitting L3=L3^Lie ⊕ V^(1), or a canonical projection L3 -> V^(1), has not been proved. Therefore the projected functional e_3^(p)=pr_{V^(1)}(e_3) is **OPEN**. The intrinsic data currently established are the canonical extension class e_3 together with the canonical subspace V^(1), not a canonical projection.

3. **Transgression/Bockstein identification.** The proposed d2 restriction to (V^(1))* matching the standard Bockstein is a promising FRM-0.2 target, but it requires an explicit identification of the relevant dual space, proof of GL2(F3)-equivariance, and equality of the pushed-out extension cocycle with the standard Bockstein class. This is **OPEN / LOAD-BEARING** and is the next authorized W3 calculation/proof gate.

4. **Universal/free-window versus realization-specific relation jet.** Even if (e_2,e_3^(p)) were intrinsic to W3, it is universal free-window data. The realization-specific jet J_{s,a}=(q_{s,a},ell_{s,a}^p) still requires an intrinsic finite-window realization map/factorization. Thus the implication from W_p to the stabilizer of the actual relation jet remains **OPEN / LOAD-BEARING**. Abstract stabilizer formulas do not close finite-window realization.

Current FRM-0 classification remains **OPEN / LOAD-BEARING**. General odd-p factorization remains **OPEN**. The authorized immediate subgate is **FRM-0.2: explicit W3 central-extension/transgression computation, with Bockstein comparison and independent verification**. Do not promote FRM-0, do not declare a canonical V^(1)-projection, and do not start a new GAP scan for the general factorization before this proof gate is settled.


## 2026-10-05 — explanation/guide records given a dedicated navigation layer

The repository contains a second class of records that are not mathematical evidence but are useful for human understanding: easy-language explanations, research-story summaries, methodological reflections, midterm summaries, and contribution/level assessments. These had accumulated across several paths.

A dedicated navigation layer is now established at **research/90_RESEARCH_GUIDE/README.md**. Existing explanatory records are **not deleted, moved, or overwritten**; the new guide indexes their original paths and defines their role separately from authoritative state/evidence documents.

Documentation rule: \`CURRENT_STATE\` / \`RESEARCH_MAP\` / \`PAPER*_CURRENT\` / audit-evidence remain authoritative for mathematical status; \`00_RESEARCH_LOG\` remains chronological; \`archive\` preserves historical material; \`90_RESEARCH_GUIDE\` is the human-understanding/explanation/evaluation layer.

Classification: **PASS/CLOSED — documentation architecture only**. No mathematical claim or research status changed.


## 2026-10-05 — Magnus prefix-code attack on (SC_s): first independent verification

A new attack on the load-bearing comparison
\[
(SC_s):\qquad D_{p^s+1}(F)\cap K\subseteq D_{p^{s-1}+1}(K)
\]
was independently audited. The central idea is to work in the completed Magnus algebra of K rather than compare individual group-level factors.

### Critical correction to the proposed proof
The finite-difference objects \(w_{k,i}=\delta^k(Y_{0,i})\), with \(Y_{j,i}=z^j x_i z^{-j}-1\), are **not group elements/free group generators** when \(\delta=\sigma-1\) is applied linearly in the augmentation algebra. The correct statement is that \(w_{k,i}\) are new **topological augmentation-algebra coordinates**: the transformation from \(Y_{j,i}\) to \(w_{k,i}\) is lower unitriangular over \(\mathbf F_p\), hence an invertible continuous linear change of generators of \(\mathbf F_p[[K]]\).

This correction is essential. It does not invalidate the Magnus argument; it changes its algebraic formulation.

### Independent computation
For \(p=3,5\), direct truncated noncommutative Magnus expansion gives
\[
\operatorname{in}(w_{k,i})=X_0^kX_i,\qquad 0\le k<p,
\]
with F-degree \(k+1\), and \(u=z^p-1\) has initial monomial \(X_0^p\). The finite-difference coefficient matrix has determinant 1 for \(p=3,5,7,11\).

The set
\[
\{X_0^kX_i:0\le k<p,\ i\ge1\}\cup\{X_0^p\}
\]
is a prefix code. Exhaustive concatenation tests through word length 3 for \(p=3,5,7\) found no collisions of leading monomials.

### Current assessment
The corrected Magnus-coordinate/prefix-code route is therefore **OPEN / PROMISING**, not yet PASS. The remaining proof obligation is to formalize the completed-algebra coordinate change and the leading-term multiplicativity for arbitrary infinite series, then deduce
\[
\operatorname{ord}_F(f)=\min_W d(W)
\]
for nonzero \(f\in\mathbf F_p[[K]]\). Once this is established, every word of K-length \(\ell\) has F-degree at most \(p\ell\), giving
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
\]
For \(n=p^s+1\), this is exactly (SC_s).

No all-s transfer-defect theorem is promoted yet. The subsequent TF_s/truncation step remains separately OPEN / LOAD-BEARING.

Classification: **OPEN / LOAD-BEARING candidate route; local symbolic checks PASS / LOCAL.**


## 2026-10-05 — Magnus prefix-code proof closes (SC_s), (TF_s), and the all-s stress-family boundary

A full proof audit of the new Magnus-coordinate attack is now complete. The finite-difference variables (w_{k,i}=\delta^kY_{0,i}) are augmentation-algebra coordinates, not group generators; the change from the Schreier augmentation generators is invertible over \(\mathbf F_p\). With (X_0=z-1) ordered largest in degree-lex, the initial terms are
\[
\operatorname{in}(w_{k,i})=X_0^kX_i,\qquad \operatorname{in}(U)=X_0^p.
\]
The set \(\{X_0^kX_i:0\le k<p\}\cup\{X_0^p\}\) is prefix-free, so distinct coordinate words have distinct leading monomials. This gives the completed-algebra lemma
\[
\operatorname{ord}_F(f)=\min_W d(W)
\]
for every nonzero completed augmentation series (f\) in the Schreier coordinates. Since every coordinate has ambient weight at most p, one obtains the general theorem
\[
\boxed{D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K)}
\]
for every index-p kernel (K) of a finitely generated free group (F). In particular (SC_s) is PASS / CLOSED.

Independent sparse Magnus checks over \(\mathbf F_3\) found F-order/K-order (10/4) for \([z^9,x]\), \(\operatorname{ad}_z^9(x)\), and \(\operatorname{ad}_{z^3}^3(x)); 30 random products/inverses of these witnesses had K-order at least 4. Finite-difference determinants are 1 for p=3,5,7,11, and prefix-code collision tests through coordinate-word length 4 pass for p=3,5,7. The sharpness witness (z^{p^s}) has ambient/K order ratio p.

From the Jennings product formula, (SC_s) immediately implies
\[
\operatorname{im}(D_{p^s+1}(F)\cap K\to K^{ab})\subseteq p^sK^{ab},
\]
so (TF_s) is PASS / CLOSED. For the stress relator, (R\subseteq K) and (D_{p^s+1}(F)\subseteq K), hence (N=D_{p^s+1}(F)R=N\cap K). The quadratic commutator tail lies in \([K,K]\), so its K-abelianization contribution vanishes; the resulting Schreier relation is the previously audited (p^{s-1}U-p^sA_i=0) at a=s.

The intrinsic transfer formulation was corrected: (T=W^{ab}[p^s]) is not itself a single canonical line. The canonical line is the image (S_s(W)=\operatorname{im}(W^{ab}[p^s]\to W^{ab}/pW^{ab})), which is one-dimensional in the declared stress-family scope. The invariant is the class of (p^{s-1}V(t)) in (K^{ab}/p^sK^{ab}) for any lift t spanning (S_s(W)); changing the lift by pW changes the result by (p^sK^{ab}). Thus the predicate is genuinely unmarked and isomorphism-invariant.

Combining (TF_s) with the model Schreier lattice nonvanishing closes the critical a=s transfer witness; the a=infinity side has no corresponding power relation in the U-direction and the normalized transfer defect vanishes. Therefore
\[
\boxed{W_{p^s+1}(G_{s,s})\not\cong W_{p^s+1}(G_{s,\infty})}
\]
for every odd p and s>=2 in the declared stress-family scope. Together with the already certified lower-window blindness, the exact threshold is
\[
\boxed{n_{\rm sep}(s)=p^s+1}.
\]

Classification: Magnus coordinate lemma **PASS / CLOSED**; (SC) and (SC_s) **PASS / CLOSED**; (TF_s) **PASS / CLOSED**; corrected intrinsic transfer invariant **PASS / CLOSED in scope**; a=s versus a=infinity **PASS / CLOSED**; exact stress-family threshold **PASS / CLOSED**. Detailed proof/evidence: `research/PAPER4_MAGNUS_PREFIX_CODE_AUDIT_2026-10-05.md`.


## 2026-10-05 — Independent §9–§11 review corrections to Magnus transfer closure

The independent review rechecked the Magnus prefix-code proof and the a=s versus a=∞ separation. The core proof was confirmed, but the first closure write-up contained several scope/wording defects.

1. **§9 correction:** the untruncated class having order p^s does not itself imply nonvanishing modulo p^s. The correct argument is the model-lattice calculation
\[
p^{s-1}U=0,qquad
(\sigma-1)^{p-1}A_0\equiv\sum_{j=0}^{p-1}A_j\pmod p,
\]
so the critical class is
\(p^{s-1}\sum_jA_j\ne0\) modulo p^s. TF_s puts the actual truncation image inside p^sK^ab, so it cannot kill this class.

2. **§11 direct representatives:** a=s uses t=z-x_1, giving
\(\varepsilon_s=-p^{s-1}\sum_jA_j\ne0\); a=∞ uses t=z, giving
\(\varepsilon_s=0\) directly because p^{s-1}U is in the relator image.

3. **Intrinsic scope:** K is intrinsic only when d is even and the alternating quadratic form defined by r_2 is nondegenerate; d=2 and r_2=[x_1,x_2] is the basic example. Since the power relation is in D_3, the degree-2 cup product on W_n (n\ge3) is unchanged, so the radical line \(\langle z^*\rangle\) is intrinsic in the declared scope.

4. **Schreier range:** corrected to 0\le j\le p-1.

5. **s=1:** the exact separation statement remains intentionally scoped to s\ge2 and is not promoted here.

Classification: **PASS / CLOSED** for odd p, s\ge2, d even, r_2 nondegenerate. Novelty remains a separate literature audit.

## 2026-10-05 — uploaded weighted-Schreier source: SC novelty derivation gate

The user supplied the full TeX source \`arXiv-1007.1489v3\`, *Groups of positive weighted deficiency and their applications*. Direct inspection of the source materially changes the Paper-4 novelty assessment.

The source contains the following relevant chain:

1. Proposition \`uniform2\`: for a uniform weight W on a finitely generated free pro-p group F, there is beta in (0,1) with
\[
W(f)=\beta^{d_F(f)},
\]
where d_F is ordinary Zassenhaus degree.

2. Corollary \`weight_preserve\`: the restriction of a weight function to any closed subgroup K of F is again a weight function.

3. Lemma \`index_p0\`: for an index-p subgroup K, the standard index-p Schreier generating set
\[
y,[y,z],\ldots,[y,\underbrace{z,\ldots,z}_{p-1}],z^p
\]
is W-optimal in the free/weight-function case.

4. In the proof of Lemma \`indexp\`, the weights of these Schreier generators are exactly controlled by
\[
W(z^p)=W(z)^p,\qquad
W([y,\underbrace{z,\ldots,z}_{k}])=W(y)W(z)^k
\]
in the free weight-function case.

5. Proposition \`cor1\` gives the required no-cancellation characterization of weight functions via power-commutator factorization.

Specializing the uniform weight to the ordinary Zassenhaus degree therefore gives the Paper-4 comparison
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
\]
Indeed, every K-Schreier generator has ambient weight exponent at most p, while a nonzero K-element of K-Zassenhaus degree ell has a nonzero K-coordinate term of length ell, hence ambient weighted exponent at most p ell. Since the restricted weight is still a weight function, the source's no-cancellation characterization gives d_F(g)<=p d_K(g). Thus d_F(g)>=n implies d_K(g)>=ceil(n/p).

Classification:
- weighted-Schreier derivation of SC: **PASS / CLOSED as a derivation from prior machinery**;
- SC as an independent novelty claim: **CONDITIONAL / likely not novel**;
- Paper-4 Magnus prefix-code proof: **PASS / mathematically valid, but no standalone novelty claim**;
- downstream intrinsic epsilon_s and exact a=s versus a=infinity separation: **OPEN / strongest current novelty candidates**;
- Paper-4 mathematical theorem in declared scope: **PASS / CLOSED**;
- publication novelty overall: **CONDITIONAL / OPEN**.

The detailed source comparison is recorded in \`research/PAPER4_WEIGHTED_SCHREIER_DERIVATION_AUDIT_2026-10-05.md\`.

Governance consequence: do not reopen the Paper-4 mathematics. Move the novelty audit downstream to epsilon_s, the finite-window torsion obstruction, the a=s versus a=infinity family, and the exact threshold p^s+1.


## 2026-10-05 — weighted-Schreier source audit: SC novelty boundary confirmed

The uploaded `arXiv-1007.1489v3.gz` was decompressed and directly inspected. SHA-256:
`9f8c1e6ec8d7bff45e275b4774edf49bd95050d4ef59227d2b58aee768c14710`.

The source is *Groups of positive weighted deficiency and their applications*. The relevant chain is explicit:

- Proposition `uniform2`: a uniform weight on free pro-(p) (F) is (W_F(g)=\beta^{d_F(g)}).
- Corollary `weight_preserve`: restriction of a weight function to a closed subgroup remains a weight function.
- Lemma `index_p0`: standard index-(p) Schreier generators (y,[y,z],ldots,[y,z^{p-1}],z^p) are (W)-optimal in the free case.
- Proof of Lemma `indexp`: their weights are exactly (\beta,ldots,\beta^p).
- Proposition `cor1`: for every (f), its power-commutator factorization has no cancellation at the top weight; (W(f)) is the maximum weight of a nonzero factor.

Therefore the Paper-4 comparison
[
D_n(F)cap Ksubseteq D_{\lceil n/p\rceil}(K)
]
is already a consequence of the prior weighted-Schreier framework: (d_F(f)le p,d_K(f)), hence the displayed subgroup inclusion. The earlier review question about whether `cor1` applies only to special elements is resolved negatively: it applies to arbitrary (f).

Classification:
- SC derivation from prior literature: **PASS / CLOSED**.
- SC standalone novelty: **CONDITIONAL / likely not novel**.
- Magnus prefix-code proof: **PASS / CLOSED as independent self-contained verification/reproof; no standalone novelty claim**.
- Paper-4 mathematics in the declared scope: **PASS / CLOSED**.
- Overall publication novelty: **CONDITIONAL / OPEN**.

The novelty center of gravity is moved downstream to the intrinsic transfer obstruction (arepsilon_s), the unmarked (a=s) versus (a=\infty) separation at the critical window, and the exact threshold (p^s+1). No Paper-4 mathematical result is reopened or downgraded by this audit.


## 2026-10-05 — bounded external literature audit after weighted-Schreier source discovery

A second literature audit was run after the direct source inspection.

### Findings

1. Ershov–Jaikin-Zapirain, *Groups of positive weighted deficiency and their applications*, J. Reine Angew. Math. 677 (2013), 71–134, DOI 10.1515/crelle.2012.013, independently corroborates the uploaded TeX source: its published text contains the explicit index-(p) weighted Schreier construction (Lemma 3.10) and the surrounding weight-function/free-restricted-Lie machinery. Thus SC is safely treated as a prior weighted-Schreier consequence, not a new theorem.

2. Later Zassenhaus/Magnus literature (including Mináč–Rogelstad–Nguyễn and Efrat) confirms that augmentation/Magnus/word methods and finite Zassenhaus quotients are established infrastructure. Magnus/prefix-code language therefore cannot itself carry the novelty claim.

3. Efrat's transfer/intersection literature is an important neighboring threat: transfer principles connect cohomology, finite quotients, unitriangular representations, and Zassenhaus intersections. This must be cited and discussed.

4. Targeted searches for the **specific downstream Paper-4 combination** — intrinsic (epsilon_s), the stress family (z^{p^s}=x_1^{p^a}r_2^{-1}), unmarked (a=s) versus (a=\infty) separation, and exact threshold (p^s+1) — produced no matching result in the retrieved literature.

### Classification

- SC: **PASS/CLOSED mathematically; not standalone novelty**.
- Magnus proof: **PASS/CLOSED as self-contained reproof/bridge**.
- (epsilon_s): **OPEN — strongest novelty candidate**.
- Exact (a=s) vs (a=\infty) separation: **OPEN — strong novelty candidate**.
- Exact threshold (p^s+1): **OPEN — strong sharpness candidate**.
- Overall publication novelty: **CONDITIONAL / OPEN**.

This is a bounded negative search, not a proof of priority. The next authorized audit is narrowly targeted at transfer on index-(p) kernels, Bockstein/cup-product relation data, and finite-quotient separation at a prescribed Zassenhaus depth.


## 2026-10-05 — SC literature audit CLOSED; downstream strengthening authorized

Decision: **SC = PASS / CLOSED; literature audit = PASS / CLOSED.**

The final position is:
- Zassenhaus/Magnus/weighted-Schreier literature provides the component machinery.
- The exact Paper-4 subgroup-depth comparison \(D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K)\) was not located as a directly stated theorem in the audited sources.
- Paper 4 therefore may claim this comparison as a **new logical deduction/assembly step**, while explicitly crediting the prior machinery from which it can be derived.
- The standalone novelty claim is not “we invented weighted Schreier theory” and not “no prior result could imply SC”; it is that the Paper-4 proof identifies and packages the precise subgroup-depth comparison needed to force the finite-window transfer bound.

The SC search is now stopped. No more generic literature time should be spent here.

### Next research gate — theorem strengthening using SC

The next task is to derive the strongest clean theorem that SC supports, in this order:

1. formulate the exact general marked-kernel consequence of SC and Jennings after abelianization;
2. specialize it at \(n=p^s+1\) to obtain the sharp transfer truncation bound;
3. separate the universal SC/TF layer from the family-specific intrinsic \(\varepsilon_s\) layer;
4. test whether the nondegenerate quadratic hypothesis can be weakened while retaining an unmarked canonical kernel;
5. state the final theorem with the strongest valid scope, explicitly distinguishing marked and intrinsic versions.

No theorem is to be broadened by analogy; each scope enlargement requires an independent proof.



## 2026-10-05 — SC strengthening and complete critical-a classification

**Result classification: PASS / CLOSED.**

The SC result was strengthened from the critical specialization to a general transfer-depth law. For an index-p kernel K≤F,
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
With m=\lceil n/p\rceil and e(n)=\lceil\log_p m\rceil, Jennings–Lazard gives
\operatorname{im}(D_n(F)\cap K\to K^{ab})\subseteq p^{e(n)}K^{ab}.
At n=p^s+1, e(n)=s, recovering TF_s.

A second strengthening completely classifies the stress-family critical windows W_{s,a}=W_{p^s+1}(G_{s,a}). For 1\le a<s,
W_{s,a}^{ab}\cong\mathbf Z_p/p^a\oplus(\mathbf Z_p/p^{s+1})^d,
so distinct a<s are pairwise distinguished by abelianization. For a>s, p^a\ge p^{s+1}>p^s+1, so the x_1^{p^a} term vanishes in the critical truncation and W_{s,a}=W_{s,\infty}. At a=s, abelianization agrees with a=\infty, but the already certified intrinsic transfer witness satisfies
\varepsilon_s(W_{s,s})\ne0,\qquad \varepsilon_s(W_{s,\infty})=0,
hence W_{s,s}\not\cong W_{s,\infty}.

Therefore the map a\mapsto W_{p^s+1}(G_{s,a}) has exactly one nontrivial critical boundary at a=s, while a>s is saturated with a=\infty.

Scope remains: odd p, s\ge2, even d, nondegenerate alternating r_2. The nondegenerate hypothesis is retained because it is needed for the current canonical one-dimensional cup-radical construction of the intrinsic kernel. The s=1 case and degenerate quadratic forms remain unpromoted.

Interpretation: SC is now infrastructure/engine. The theorem-level contribution is the finite-window transfer obstruction and the complete critical-window classification of the hidden power parameter. The arbitrary-r degree-only theorem remains FAIL / CLOSED.

Evidence anchors: research/PAPER4_CURRENT_2026-10-05.md, research/PAPER4_MAGNUS_PREFIX_CODE_AUDIT_2026-10-05.md, and the SC literature audit in research/PAPER4_WEIGHTED_SCHREIER_DERIVATION_AUDIT_2026-10-05.md.


## 2026-10-05 — Paper 4 SC_s strengthening: index-p^s and sharpness

**Result classification: PASS / CLOSED.**

The authorized theorem-strengthening step is complete.

1. **Index-p^s generalization.** For an open subgroup K of a finitely generated free pro-p group F with [F:K]=p^s, choose a subnormal chain F=K_0>K_1>...>K_s=K with [K_{i-1}:K_i]=p. Repeated application of the certified index-p comparison gives
\[
D_n(F)\cap K\subseteq D_{\lceil n/p^s\rceil}(K).
\]
The ceiling identity composes exactly, so no extra rounding loss appears.

2. **Uniform sharpness.** Let F=<a,b> be free pro-p and K=ker(F -> C_{p^s}), with a mapping to a generator and b to 0. A Schreier basis contains c_0=a^{p^s}. For m>=1,
\[
g_m=a^{p^{m+s-1}}=c_0^{p^{m-1}}
\]
lies in D_{p^{m+s-1}}(F)\cap K but not in D_{p^{m-1}+1}(K). Hence the universal replacement of the bound by D_{\lceil n/p^s\rceil+1}(K) is false. This proves the p^s compression factor is uniformly optimal.

3. **Scope correction.** The stronger proposed claim that a commutator correction gives sharp witnesses for every integer n is not independently proved and is not promoted. Pointwise sharpness for every n is unnecessary; the infinite equality family already establishes optimality of the uniform theorem.

4. **Paper-4 interpretation.** SC/SC_s are universal filtration infrastructure. The Paper-4-specific theorem-level contribution remains the intrinsic transfer obstruction, exact unmarked critical-window separation, and threshold n_sep(s)=p^s+1 in the declared odd-p, s>=2, even-d, nondegenerate alternating quadratic stress-family scope.

Evidence: research/PAPER4_SC_SHARPNESS_AND_INDEX_PS_AUDIT_2026-10-05.md.


## 2026-10-05 — General SC arbitrary-pro-p A1 audit: proposed proof rejected

The proposed strengthening of D_n(G) cap K subseteq D_{ceil(n/p^s)}(K) from free pro-p groups to arbitrary pro-p groups was audited before promotion.

**Classification: FAIL / CLOSED as the proposed proof; arbitrary-pro-p theorem remains OPEN.**

The fatal error is Lemma 2. For an index-p extension, the identity I_G^n = sum_{j=0}^n I_K^{n-j} t^j B does not hold in general because t=a-1 does not commute with I_K. Normality only gives conjugation invariance. A concrete counterexample to Lemma 2 is the odd-p exponent-p Heisenberg group G=<x,y,z | x^p=y^p=z^p=1,[x,y]=z,z central>, with K=<x,z> and t=y-1. Then t(x-1) lies in I_G^2 and has an A-component containing x(z-1), which has I_K-degree 1 because K is abelian, while the proposed n=2 right-hand side has A-component contained in I_K^2.

There is also a second gap in Lemma 3: the coefficient y_j in I_K^{n-j}B itself can contain t-powers in its B-basis expansion, so the claim that only j divisible by p can contribute to the A-component is not justified.

Therefore:
- Lemma 2 = **FAIL / CLOSED**;
- Lemma 3 via this route = **FAIL / CLOSED**;
- arbitrary-pro-p SC = **OPEN**;
- the already certified free-pro-p SC/SC_s and Paper-4 theorem are **unchanged**.

A targeted literature search did not locate an immediately usable theorem giving this exact arbitrary-pro-p comparison. No arbitrary-pro-p promotion is authorized without a different proof. Full audit: research/PAPER4_GENERAL_SC_ARBITRARY_PROP_A1_AUDIT_2026-10-05.md.


## 2026-10-05 — A1 arbitrary pro-p SC closed and promoted into Paper 4

The earlier A1 audit rejected the first augmentation-ideal equality proof because the claimed decomposition was false. That rejection is retained as a proof-route failure only.

A corrected weighted normal-form argument is now independently audited and **PASS / CLOSED**. For arbitrary pro-p (G), an index-(p) open subgroup (K), (A=\mathbf F_p[[K]]), (J=I_K), and (t=a-1) for a lift of a generator of (G/K), use
[
\mathbf F_p[[G]]=\bigoplus_{r=0}^{p-1}At^r,qquad t^p\in J,
]
and the weighted filtration
[
E_m=\bigoplus_{r=0}^{p-1}
J^{\max(0,\lceil(m-r)/p\rceil)}t^r.
]
The normal-form multiplication rules give (E_mE_\ell\subseteq E_{m+\ell}), including the previously problematic (t^rBt) terms. Hence
[
I_G^n\subseteq E_n,qquad
I_G^n\cap A\subseteq I_K^{\lceil n/p\rceil},
]
and therefore
[
D_n(G)\cap K\subseteq D_{\lceil n/p\rceil}(K).
]
Iteration along an index-(p^s) chain yields
[
D_n(G)\cap K\subseteq D_{\lceil n/p^s\rceil}(K).
]

Thus:
- A1 index-(p) arbitrary pro-p: **PASS / CLOSED**;
- A1 index-(p^s) arbitrary pro-p: **PASS / CLOSED**;
- free-pro-p SC/SC_s: unchanged and subsumed;
- uniform sharpness: retained only in the already certified free-pro-p witness family;
- pointwise sharpness for every (n): not claimed.

The old false equality route, Heisenberg witness, and Lemma-2/Lemma-3 route remain **FAIL / CLOSED / SUPERSEDED** and are not evidence against A1.

Paper 4 is therefore strengthened by A1 as universal filtration infrastructure. The theorem-specific contribution remains the intrinsic transfer obstruction, exact unmarked separation (W_{p^s+1}(G_{s,s})\not\cong W_{p^s+1}(G_{s,\infty})), and the sharp threshold (n_{\rm sep}(s)=p^s+1) in the declared stress-family scope.

Evidence: `research/PAPER4_GENERAL_SC_ARBITRARY_PROP_A1_CLOSURE_2026-10-05.md`.


## 2026-10-05 — Paper 4 Every-(n) sharpness closed and manuscript promotion started

The Every-(n) sharpness argument is now certified. For
[
F=langle a,bangle,qquad
K=ker(F	omathbf Z/p^s),
]
the Schreier generators
[
c_0=a^{p^s},qquad c_i=a^iba^{-i}
]
give explicit group-commutator witnesses for every
(n=p^sq+r). For (r>0), repeated commutation of (c_{r-1}) by (c_0)
gives
[

u_F(g_{q,r})=n,qquad

u_K(g_{q,r})=q+1.
]
For (r=0), the second (F)-degree-(p^s) Schreier generator
(c_{p^s-1}) is essential; the commutators
(h_2=[c_0,c_{p^s-1}],,h_{k+1}=[h_k,c_0]) give
[

u_F(h_q)=qp^s,qquad 
u_K(h_q)=q.
]
The free-associative leading-word argument certifies the required
nonvanishing. The previous abstract (gr_D(K)	o gr_D(F)) lift/Lazard
shortcut is explicitly not used.

Final sharpness statement:
[
oxed{orall nge1,quad
lceil n/p^sceil	ext{ is best possible in the free-pro-}p	ext{ class}.}
]
Scope remains: arbitrary pro-(p) validity; free-pro-(p) uniform
every-(n) optimality.

The Paper 4 manuscript on branch
`paper4-tex-2026-10-04` has now been promoted to incorporate:
1. arbitrary-pro-(p) SC/SC_s theorem via weighted normal forms;
2. explicit every-(n) free-pro-(p) sharpness witnesses;
3. corrected intrinsic transfer separation and exact
(n_{m sep}(s)=p^s+1);
4. the degree-only arbitrary-(r) counterexample boundary.

Commit:
`499337be2114b74549969aea65b08442d2cd8fa7`.

No new generic literature search is required: the SC novelty audit was
already closed on 2026-10-05. Remaining work is manuscript/source/PDF
artifact audit, not a reopening of the mathematical gates.


## 2026-10-05 — Paper 4 publication pass: manuscript proof integration

The Paper 4 manuscript on `paper4-tex-2026-10-04` was promoted from theorem-summary form to the audited publication form.

Integrated:
- arbitrary-pro-p SC/SC_s theorem via weighted normal forms;
- every-n free-pro-p sharpness with explicit Schreier-generator commutators;
- corrected intrinsic transfer invariant (S_s(W)=\operatorname{im}(W^{ab}[p^s]\to W^{ab}/pW^{ab}));
- explicit (a=s) versus (a=\infty) critical transfer calculation;
- exact (n_{sep}(s)=p^s+1);
- degree-only arbitrary-(r) boundary (r=z^p).

Also removed stale manuscript language that still called the (a=s) versus (a=\infty) boundary open.

The dedicated `paper4-tex-build` workflow was updated so its PDF audit checks the final every-(n) sharpness and intrinsic-separation statements rather than the obsolete boundary wording.

Latest manuscript commit:
`b384441a02f0a01c448bf16feaa1fbcd709a3cba`.

Latest workflow-audit commit:
`639b0c9f84307570970bec884b5eb7290ecad5c9`.

CI artifact verification is still pending/not directly exposed by the available workflow-run connector (which only returns pull-request-triggered runs). Therefore no new PDF SHA is declared yet. The prior Paper 4 PDF build remains historical; final status awaits the current source's CI PDF artifact audit.


## 2026-10-05 — Paper 4 publication artifact freeze

**Result classification: PASS / CLOSED.**

The final Paper 4 manuscript source was reconciled with the authoritative theorem state. The stale abstract order-jump sentence was removed; the critical-window (a)-classification was included; bibliography metadata was checked against publisher records; LaTeX tag/text-mode errors and the CI PDF path error were repaired.

Final publication build:
- manuscript commit: `b3e0e3cd85f17ab038815030b2643e6be002c4fd`
- workflow: `paper4-tex-build`
- CI run: `37291334999` — PASS
- PDF: 17 pages, 423897 bytes
- PDF SHA-256: `85d5bd7793a8ba271c6a883ed4e0f7ca1849fc283c821a6cf92c84d56a4601ad`
- source blob SHA: `13f50f4ff38f528d17f1cbaaa737bf12af2c5084`
- source SHA-256: `b5169596ab6a84d693e66fb0138ceecbd10eda925cf341ef44a4a677674b65ab`
- CI artifact: `paper4-pdf`, id `11337135583`
- artifact ZIP digest: `sha256:13d97ff0e3a9cbf762906a610e51cb9068d03a4d9b07dfc827448b792b0d5885`

The final CI audit verifies compilation, PDF extraction, author/title/reference presence, absence of the superseded order-jump wording, and source/PDF checksum manifest generation. Earlier local PDF artifacts are HISTORICAL / SUPERSEDED.

**Paper 4 publication artifact is now frozen. No mathematical gate was reopened by this audit.**


## 2026-10-05 — Paper 5 corrected relation-jet model and lift audit

A new review identified and independently clarified the decisive \(S_{11}\) issue. In the naive \(\Lambda^2V\oplus V^{(1)}\) shadow, \(\rho_{11}=[x,y]+z^{[p]}-x^{[p]}\) has stabilizer of order \(|GL_2(p)|\), so the prior \(S_{11}\) formula of order \(p(p-1)\) is not a consequence of that model. The observed p=3 value 6 is recovered only after retaining the Jacobson restricted-power terms and reducing modulo the ideal generated by \([x,y]\). Thus the corrected general odd-p \(S_{11}\) derivation is **OPEN / LOAD-BEARING**.

The restricted-Lie structure is also reinterpreted: the canonical data are the ordinary-Lie subspace/image and the Frobenius-twist quotient; the span of chosen \(x^{[p]},y^{[p]}\) is not a canonical GL-invariant direct summand. A canonical section is not asserted.

The free pro-p lifting route is revised. For a free pro-p presentation, projectivity supplies a lift of an automorphism of the finite quotient to an endomorphism of the free pro-p group; Frattini-surjectivity makes the lift an automorphism, and kernel equality gives preservation of the defining normal subgroup. Hence the blanket Hopficity-based rejection is superseded. The induced action on a chosen relation module is nevertheless only **CONDITIONAL** until lift ambiguity is handled.

Authorized next sequence:
1. corrected restricted-Lie/Jacobson P5-JET;
2. intrinsic graded upper bound \(\operatorname{Im}Aut(W_n)\subseteq Stab(J)\);
3. intrinsic filtered secondary map \(\theta\);
4. equality/lifting construction;
5. only afterward, pre-registered same-prime falsification computations and \(n=p+2\) checks.

Evidence: `research/PAPER5_NEXT_STEP_AUDIT_2026-10-05.md`.


## 2026-10-05 — Paper 5 Step 2 audit correction

The Hall–Petrescu p-power sublemma for odd p passes: for u∈D_2, (xu)^p≡x^p mod D_{p+1}. But this controls only the p-power component. Under x'=xu, y'=yv, the commutator [x,y] changes by D_3, and there is no canonical projection D_3→D_p/D_{p+1}. Therefore the proposed θ:J_2→D_p/D_{p+1} is not yet shown well-defined. Step 2 remains **OPEN / LOAD-BEARING**; no equality or uniform p^2(p−1) theorem is promoted.


## 2026-10-05 — Step 2 D_3-ambiguity correction

The proposed final split “p=3 PASS / p≥5 FAIL” is **not established**. Two errors were found: (i) D_3 is not equal to γ_3 for p≥5; it contains p-power factors such as G^p and γ_2^p, and (ii) for u=[r,s]∈γ_2 the leading correction [[r,s],y] is in γ_3, not γ_4. Hence the proposed negative witness is invalid. The p=3 claim also needs a direct Zassenhaus calculation of [x,D_2] and [D_2,y] modulo D_4. Current status: **OPEN / LOAD-BEARING**. Next gate is the exact lift-change map D_2×D_2→D_3/D_{p+1} and its interaction with the relation constraint.


## 2026-10-05 — Step 2 central-ambient review: promising reduction, but theta closure still CONDITIONAL

A proposed repair of the (D_3)-ambiguity was reviewed. The correction of the two earlier errors is accepted: (D_3
eq\gamma_3) in general, and for (u=[r,s]in\gamma_2) the leading term ([[r,s],y]) lies in (\gamma_3), not (\gamma_4). Hence the previous (p=3)/(p\ge5) split remains superseded.

The new route uses the central restricted-Lie ambient
\[
\overline L=L_p(V)/\langle[x,z],[y,z]\rangle_{\rm res},\qquad V=\langle x,y,z\rangle,
\]
followed by the restricted ideal (J=\langle[x,y]\rangle_{\rm res}). In \(\overline L/J\), the ordinary Lie part is abelian, so the degree-\(\ge2\) filtration is generated by restricted (p)-powers. Consequently the intended estimate
\[
[x,D_2(\overline L/J)]\subseteq D_{p+1},\qquad [D_2(\overline L/J),y]\subseteq D_{p+1},
\]
and hence the vanishing of the lift-change map modulo (D_{p+1}), is a mathematically plausible route and is consistent with the restricted-Lie structure.

However, this does **not yet by itself close \(\theta\)**. Two points must be made explicit before promotion:

1. One must prove the exact structural lemma (D_2(\overline L/J)=V^{[p]}+D_{p+1}) (or an equivalent statement strong enough to imply the displayed commutator inclusions), including the higher restricted-power terms. The sentence (u\equiv t^{[p]}\pmod{D_3}) alone is insufficient, because ( [x,D_3]\subseteq D_4) does not imply ( [x,D_3]\subseteq D_{p+1}) for (p>3).
2. The quotient by (J) is being used as a **gauge-killing ambient object**, not as the final relation quotient. Since (J=\langle[x,y]\rangle_{\rm res}) kills the degree-2 relation line, the secondary class (x^{[p]}-z^{[p]}) must be defined as the filtered lift/transgression of that killed line. One must explicitly construct the source/target map (or equivalent exact sequence) and show independence from the chosen lifts before calling \(\theta\) canonical.

Therefore the proposed central-ambient calculation is accepted as a **new authorized subgate**, but the Step-2 classification remains **OPEN / LOAD-BEARING**. No (S_{11}(p)) equality or uniform (p^2(p-1)) theorem is promoted.

Next authorized gate: prove the restricted-abelianization lemma for \(\overline L/J\), then formulate the transgression/filtered relation object whose degree-(p) class is \(x^{[p]}-z^{[p]}), and only then certify \(\Phi\in D_{p+1}\) and \(\theta\) well-defined.


## 2026-10-05 — Critical recheck of proposed Step 2 closure: restricted-abelianization lemma is valid, but does NOT imply Phi closure in the original ambient

The proposed proof of the lemma
\[
D_2(\overline L/J)=V^{[p]}+D_{p+1}(\overline L/J),\qquad J=\langle[x,y]\rangle_{\rm res},
\]
is accepted at the level of the quotient restricted Lie algebra: after killing the restricted ideal generated by \([x,y]\), the ordinary Lie algebra is abelian, and the Zassenhaus/restricted-degree filtration is generated by the successive restricted powers. Hence the quotient statement is **PASS / LOCAL** (subject to precise notation distinguishing images in the quotient from subspaces upstairs).

However, the attempted inference
\[
[x,D_2(\overline L/J)]\subseteq D_{p+1}\quad\Longrightarrow\quad
\Phi(u,v)\in D_{p+1}(\overline L)
\]
is invalid. The calculation takes place **after quotienting by (J)**. It proves at most
\[
\Phi(u,v)\in J+D_{p+1}(\overline L)
\]
when lifted back to \(\overline L\), not \(\Phi(u,v)\in D_{p+1}(\overline L)\). Since (J\) contains the degree-2 class \([x,y]\), it is not contained in (D_{p+1}). Thus the quotient kills precisely the low-degree ambiguity one is trying to control, and cannot by itself certify the required degree-(p) vanishing in the original ambient.

This is a decisive gap. The statement \(\Phi\in D_{p+1}\) and hence the canonicality of \(\theta\) remain **OPEN / LOAD-BEARING**. The proposed Step-2 CLOSED classification is rejected. The restricted-abelianization lemma becomes a useful auxiliary lemma, not the final gate.

The next authorized task is to retain enough of the \(J\)-adic/filtered extension data to distinguish \(D_{p+1}\) from \(J+D_{p+1}\), and to compute the lift-change map in \(\overline L\) itself (or construct an exact transgression sequence whose kernel is known to contain no degree-\(<p\) contribution). No equality theorem or \(p^2(p-1)\) theorem is promoted.


## 2026-10-05 — Paper 5 Step 2 CLOSED: filtered-extension/J-adic gate

**Result classification: CLOSED / GENERAL (Step 2).**

The previously identified gap is now closed in the actual relation quotient, not merely in the auxiliary quotient. Let
[
overline L=L_p(V)/langle[x,z],[y,z]angle_{m res},qquad
J=langle[x,y]angle_{m res},
]
and
[
W_n=overline L/langlehoangle,qquad
ho=[x,y]+z^{[p]}-x^{[p]}.
]
The auxiliary lemma
[
D_2(overline L/J)=V^{[p]}+D_{p+1}(overline L/J)
]
is only PASS/LOCAL and by itself gives merely
[
Phiin J+D_{p+1}(overline L).
]
It does not kill the (J)-ambiguity.

In (W_n), however,
[
[x,y]=x^{[p]}-z^{[p]}in D_p(W_n),
]
so the (D_2/D_{p+1}) relation direction is already contained in (V^{[p]}). Hence
[
oxed{D_2(W_n)=V^{[p]}+D_{p+1}(W_n)}.
]
The higher restricted-ideal part satisfies
[
oxed{[V,J]subseteq D_{p+1}(W_n)}
]
and more precisely
[
Jsubseteqlangle x^{[p]}-z^{[p]}angle+D_{p+1}(W_n).
]
The critical generator calculations are
[
[x,[x,y]]=0,qquad
[y,[x,y]]=(ad,x)^p(y)in D_{p+1},
]
using centrality of (z); the restricted (p)-power part is also in (D_{p+1}).

Therefore for (u,vin D_2(W_n)), write
[
u=t^{[p]}w,qquad win D_{p+1}(W_n).
]
Then
[
[x,u]in D_{p+1},qquad [u,y]in D_{p+1},
]
and the commutator expansion gives
[
oxed{Phi(u,v)=[xu,yv][x,y]^{-1}in D_{p+1}(W_n)}.
]
Thus the secondary degree-(p) class
[
	heta:J_2	o D_p(W_n)/D_{p+1}(W_n)
]
is lift-independent and canonical in (W_n).

**Precision correction:** do not state (Jsubseteq D_{p+1}). The generator ([x,y]=x^{[p]}-z^{[p]}) can survive modulo (D_{p+1}); only the higher (J)-part relevant to lift ambiguity is absorbed into (D_{p+1}).

### Updated status

- (S_{11}=p(p-1)): CLOSED/GENERAL.
- Step 1 upper bound: THEOREM/CLOSED.
- (D_2(overline L/J)=V^{[p]}+D_{p+1}): PASS/LOCAL.
- (Phiin J+D_{p+1}(overline L)): PASS/LOCAL auxiliary statement.
- (D_2(W_n)=V^{[p]}+D_{p+1}(W_n)): PASS/GENERAL.
- ([V,J]subseteq D_{p+1}(W_n)): PASS/GENERAL.
- (Phiin D_{p+1}(W_n)): CLOSED/GENERAL.
- Step 2 (	heta): CLOSED/GENERAL.
- Step 3 equality
[
operatorname{Im}(operatorname{Aut}(W_n)	o GL(V))=S_{11}(p)
]
remains CONDITIONAL.
- The (p^2(p-1)) automorphism-order theorem remains CONDITIONAL.

The old Step-2 OPEN/LOAD-BEARING entries are superseded. The next authorized gate is the explicit lower-bound/lifting construction and independent relation-preservation verification for Step 3.


## 2026-10-05 — Step 3 equality audit: first-order relation congruence passes, kernel-invariance induction fails

The proposed final Step 3 closure was independently rechecked against the current Paper 5 state.

The calculation
[
\tilde g_{a,b}(\rho)\equiv \rho^a
\pmod{R D_{p+1}(F)}
]
is accepted as a useful first-order congruence, assuming consistent commutator convention and the already established estimate
[
\gamma_3(F)\subseteq [F,R]D_{p+1}(F).
]
Hall–Petrescu supplies the required (p)-power congruences, and the (R_0)-quotient makes (z) central.

However, the submitted proof contains a definite relation-order/sign mismatch: from
[
\rho=[x,y]^{-1}x^pz^{-p}
]
the quotient relation is ([x,y]=x^pz^{-p}), not the displayed exact replacement ([x,y]=\rho z^px^{-p}). The latter is inverse/order-reversed and must not be used as an exact identity.

More importantly, the decisive implication
[
\tilde g(R)\subseteq R D_{p+1}(F)
\Longrightarrow
\tilde g(R)\subseteq R
]
was asserted via an unspecified “standard pro-(p) induction”. This is not proved. From (\tilde g(R)\subseteq RD_m) one still needs an explicit mechanism forcing (\tilde g(R)\subseteq RD_{m+1}) (or an equivalent exact relation-module/kernel argument). Closedness of (R) and ([F,R]\subseteq R) do not supply that step automatically.

Therefore the submitted Step 3 equality closure is **FAIL / CLOSED as a proof attempt**, while the underlying equality remains **OPEN / LOAD-BEARING**:
[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p)
]
is not promoted. The (p^2(p-1)) automorphism-order theorem remains **CONDITIONAL**.

Detailed evidence: `research/PAPER5_STEP3_EQUALITY_AUDIT_2026-10-05.md`.

Next authorized gate: prove a genuine Zassenhaus-layer lifting lemma for kernel invariance, or replace the induction with an exact presentation/relation-module argument. Do not promote the equality or the (p^2(p-1)) theorem before that gate closes.


## 2026-10-05 — Step 3 re-audit: (D_{p+1}\subseteq R) is false

The proposed closure using
\[
D_{p+1}(F)\subseteq R
\]
is rejected. The graded induction fails at the first exceptional multiple (n=p^2): from (y\in gr_k(R)\Rightarrow y^{[p]}\in gr_{kp}(R)) one cannot infer (gr_{kp}(F)=gr_{kp}(R)) when (k=p), because (gr_p(F)\ne gr_p(R)). In particular (x^{[p^2]}) need not lie in (gr_{p^2}(R)).

There is also a direct group-level counterexample. In the abelian quotient
\[
A=\mathbf Z_p^3/\langle p(e_x-e_z)\rangle,
\]
the defining normal subgroup (R) maps to zero, while (x^{p^2}) maps to (p^2e_x\ne0). Hence (x^{p^2}\notin R). Since (x^{p^2}\in D_{p^2}(F)\subseteq D_{p+1}(F)),
\[
\boxed{D_{p+1}(F)\not\subseteq R.}
\]

Therefore the claimed implication (\tilde g(R)\subseteq RD_{p+1}=R) is invalid. The earlier first-order congruence (\tilde g(R)\subseteq RD_{p+1}) remains a potentially useful local/general ingredient, but kernel preservation \(\tilde g(R)\subseteq R\) is again **OPEN / LOAD-BEARING**. Consequently
\(​operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p)\) remains OPEN/LOAD-BEARING and the uniform (p^2(p-1)) theorem remains CONDITIONAL.

Detailed audit: `research/PAPER5_STEP3_Dp1_SUBSET_R_AUDIT_2026-10-05.md`.


## 2026-10-05 — Step 3 second-order lifting claim rejected

The proposed closure
[
\text{equal }in_k\ +\ \text{zero }in_{k+1}\Longrightarrow D_{k+2}
]
was re-audited and is **FAIL / CLOSED as submitted proof**.

The first-order residual (r_k^{-1}\widetilde g(r)\in D_{k+1}) is accepted only as a local consequence of matching degree-(k) initial forms. The claimed second-order BCH argument is not a valid general Zassenhaus lemma: (in_{k+1}(r_k)) is undefined when (r_k\in D_k\setminus D_{k+1}), and no canonical splitting of
[
0\to D_{k+1}/D_{k+2}\to D_k/D_{k+2}\to D_k/D_{k+1}\to0
]
is provided.

Likewise, (a=\exp(X+A+\cdots)) with (X\in gr_k), (A\in gr_{k+1}) is not an intrinsic representation of arbitrary free pro-(p) group elements in the Zassenhaus filtration. A BCH calculation therefore cannot replace the missing filtered second-jet construction.

The fact ([D_k,D_k]\subseteq D_{2k}\subseteq D_{k+2}) for (k\ge2) only says (D_k/D_{k+2}) is abelian; it does not canonically split its two graded layers.

Therefore the strengthened
[
\widetilde g(R\cap D_m)\subseteq(R\cap D_m)D_{m+2}
]
and the induction to (\widetilde g(R)\subseteq R) remain **OPEN / LOAD-BEARING**. The (p) and (p^2) exceptional-layer calculations cannot repair the missing initial second-order lift.

**Status:** Step 3 equality (\operatorname{Im}=S_{11}(p)) remains OPEN / LOAD-BEARING; (p^2(p-1)) automorphism-order theorem remains CONDITIONAL. Step 2's independently audited filtered-extension result is not reopened by this correction.

Detailed audit: `research/PAPER5_STEP3_SECOND_ORDER_LIFTING_AUDIT_2026-10-05.md`.


## 2026-10-05 — Step 3 second-jet re-audit

The formal (J_k^2(r)=[r]\in D_k/D_{k+2}) construction for (k\ge2) is accepted as a valid repair of the previous type error. A fixed Magnus embedding can also provide the degree-(k) and degree-((k+1)) homogeneous coefficients.

However, the crucial assertion
[
sec_{k+1}(\widetilde g(r))\in gr_{k+1}(R)
]
is not yet proved. The nonlinear Magnus substitution (X\mapsto aX+\binom a2X^2+\cdots) acts by degree-raising insertion/substitution operators. The claim that the resulting correction is exactly
[
C_k(R_k)=[V,R_k]
]
is not automatic and has not been derived. Restricted-ideal closure under brackets/restricted powers does not imply closure under an arbitrary such insertion operator.

Therefore the second-jet itself **PASS / GENERAL**, but its preservation of the relation ideal is **OPEN / LOAD-BEARING**. The strengthened (L_k), kernel preservation, and (operatorname{Im}=S_{11}(p)) equality remain OPEN / LOAD-BEARING; the (p^2(p-1)) theorem remains CONDITIONAL.

Detailed audit: research/PAPER5_STEP3_SECOND_JET_REAUDIT_2026-10-05.md.


## 2026-10-06 — Paper 5 Step 3 second-jet substitution-order audit

The submitted (T_{a,b,k}) repair was independently checked. The raw associative derivation claims are valid: (D_X,D_Z,D_{Y,1},D_{Y,2}) preserve the two-sided commutator ideal, and the Leibniz degree count gives (D(u^p)\in I_{p^2+1}) in the mod-(p) graded layer. The (X^{p^2}-Z^{p^2}) vanishing is likewise a mod-(p) statement and requires explicit coefficient-field notation.

A load-bearing error remains in the second-order substitution formula. For (x\mapsto x^a, y\mapsto yx^b, z\mapsto z^a), the linear Magnus map is (L(X)=aX, L(Y)=Y+bX, L(Z)=aZ), so the quadratic correction acts after (L). The actual correction is schematically (T_{a,b,k}(L(R_k))), not (T_{a,b,k}(R_k)). For (R_2=[X,Y]), the actual degree-3 correction has coefficients (ab, c, -(ab+c)) on (XYX,XXY,YXX), while the submitted (T) gives (b,c,-(b+c)). Hence the displayed (sec_{k+1}) formula is **FAIL/CLOSED as written**.

The finite-stage residual factorization does not need the claimed equality (D_j=(R\cap D_j)(R\cap D_{j+1})D_{j+2}). From (r^{(j)}\in R\cap D_j), its initial class is automatically in (gr_j(R)); choose a representative in (R\cap D_j) and the residual lies in (R\cap D_{j+1}). Thus this part can survive, including at exceptional (j=p,p^2).

Classification: raw (T(I_k)\subseteq I_{k+1}) PASS/GENERAL; corrected actual second-order operator (C_{a,b}) OPEN/LOAD-BEARING; strengthened (L_k), kernel preservation, and (operatorname{Im}(Aut(W_n)\to GL(V))=S_{11}(p)) remain OPEN/LOAD-BEARING; (p^2(p-1)) remains CONDITIONAL. Detailed audit: `research/PAPER5_STEP3_SECOND_JET_AUDIT_ADDENDUM_2026-10-06.md`.


## 2026-10-06 — Paper 5 Step 3 corrected second-jet closure

The substitution-order error is repaired by (C_{a,b,k}=T_{a,b,k}\circ L). For (x\mapsto x^a, y\mapsto yx^b, z\mapsto z^a), the linear Magnus part is (L(X)=aX, L(Y)=Y+bX, L(Z)=aZ). For (R_2=[X,Y]), the corrected (XYX)-coefficient is (ab), not (b).

The associative derivations preserve the two-sided commutator ideal, (L) preserves it as well, and hence (C(I_k)\subseteq I_{k+1}). The (p)-power exceptional layer is handled in the explicit mod-(p) Magnus layer by (D(u^p)=\sum_{i=0}^{p-1}u^iD(u)u^{p-1-i}), with degree (p^2+1), while (D(X^{p^2}-Z^{p^2})=0) only in characteristic (p).

Thus (C_{a,b,k}(gr_kR)\subseteq gr_{k+1}R), the corrected secondary term lies in (gr_{k+1}R), and the finite-stage residual factorization yields (widetilde g(R)\subseteq R) without the stronger Zassenhaus-layer product equality.

**Classification:** corrected (C_{a,b,k}), secondary relation term, finite-stage factorization, and kernel preservation are **CLOSED / GENERAL within the declared mod-(p) Magnus layer**. Step 3 equality (operatorname{Im}(Aut(W_n)\to GL(V))=S_{11}(p)) remains **OPEN / LOAD-BEARING**, and the (p^2(p-1)) theorem remains **CONDITIONAL**. Evidence: research/PAPER5_STEP3_SECOND_JET_AUDIT_ADDENDUM_2026-10-06.md.

## 2026-10-06 — S11 equality re-audit: proposed upper bound rejected

The proposed proof of
\[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))\subseteq S_{11}(p)
\]
does **not** close the load-bearing gate.

The decisive defect is the passage from an arbitrary
\[
g\in\operatorname{Aut}(W_n),\qquad W_n=F/RD_{n+1},
\]
to statements in the full quotient (F/R), such as “(z) is central in (F/R)” and
\[
[g(x),g(y)]=[x,y]^{\det_{xy}},\qquad
[g(x),g(z)]=[g(y),g(z)]=1
]
as identities in (F/R). An automorphism of the finite window (W_n) does not automatically lift to an automorphism of (F/R); that is precisely part of the unresolved finite-window identification/lifting problem. Thus these (F/R)-identities cannot be used as an upper-bound argument without an independent lifting theorem.

A second independent gap is the assertion that (m_{z,x}=0) is a “representative choice.” The coefficient (m_{z,x}) is part of the actual linear map on
\[
V=F/D_2,
\]
and the relation (p(e_x-e_z)=0) in the abelianized relation subgroup does not permit changing an arbitrary (\mathbf F_p)-coefficient in (V) by a representative choice. No prior result currently establishes (m_{z,x}=0).

Therefore the proposed upper bound
\[
\operatorname{Im}\subseteq S_{11}(p)
\]
is **OPEN / LOAD-BEARING**, and consequently the equality
\[
\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p)
\]
and the (p^2(p-1)) theorem remain **OPEN / CONDITIONAL**, respectively.

The lower-bound construction is different: the already-closed kernel-preservation result
\[
\widetilde g_{a,b}(R)\subseteq R
\]
does give genuine induced automorphisms of (F/R) and (W_n), with matrices
\[
M_{a,b}=\begin{pmatrix}a&b&0\\0&1&0\\0&0&a\end{pmatrix},
\qquad a\in\mathbf F_p^\times, b\in\mathbf F_p.
\]
Hence
\[
S_{11}(p)\subseteq\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))
\]
is **CLOSED / GENERAL**, assuming the already-closed (\widetilde g(R)\subseteq R) gate. Equality is not established.

This supersedes the immediately preceding 2026-10-06 claim that the (S_{11}(p)) upper bound and equality were CLOSED/GENERAL.


## 2026-10-06 — S11 scalar-equality counterexample: m=a is not forced

**FAIL / CLOSED as submitted; exact image remains OPEN.**

The boundary correction
\[
n<p:\quad W_n\cong(\mathbf F_p)^3,\quad IA(W_n)=1,
\]
and
\[
n=p:\quad IA(W_p)\cong\operatorname{Hom}(\mathbf F_p^3,\mathbf F_p^2)\cong\mathbf F_p^6
\]
is accepted.

However, the proposed (n=p) upper-bound argument forcing the same scalar on the (x)- and (z)-directions contains a decisive algebraic error. For arbitrary (m,a\in\mathbf F_p^\times),
\[
x\mapsto x^m z^{a-m},\qquad y\mapsto y,\qquad z\mapsto z^a
\]
preserves the defining relations directly in (W_p):
\[
[x^m z^{a-m},y]=[x,y]^m=x^{pm}z^{-pm}
\]
and
\[
(x^m z^{a-m})^p(z^a)^{-p}=x^{pm}z^{-pm}.
\]
The induced map on (V=W_p/D_2(W_p)) is invertible, so this is an actual automorphism.

Thus (m) and (a) are independent. The torsion subgroup
\[
T(W_p^{ab})=\langle e_x-e_z\rangle
\]
only gives (c=a-m) for (g(x)=x^m z^c, g(z)=z^a); it does **not** give (m=a).

Therefore the previous
\[
\operatorname{Im}=S_{11}(p),\qquad |\operatorname{Im}|=p^2(p-1),\qquad |\operatorname{Aut}(W_p)|=p^8(p-1)
\]
claim is **FAIL / CLOSED**.

A corrected candidate lower-bound subgroup is
\[
S'_{{11}}(p)=
\left\{
\begin{pmatrix}
m&b&0\\
0&1&0\\
a-m&d&a
\end{pmatrix}
: m,a\in\mathbf F_p^\times, b,d\in\mathbf F_p
\right\},
\]
with order (p^2(p-1)^2). This is only a lower bound; equality with (S'_{11}(p)) is **OPEN**. Consequently
\[
|\operatorname{Aut}(W_p)|\ge p^8(p-1)^2,
\]
while the exact order remains **OPEN**.

Detailed audit: `research/PAPER5_STEP3_S11_UPPER_BOUND_COUNTEREXAMPLE_AUDIT_2026-10-06.md`.


## 2026-10-06 — Paper 5 Step 3 corrected image target S'11

The previous (S_{11}(p)) target is permanently rejected. The finite-window calculation at (n=p) gives the explicit automorphisms
\[
g_{m,a}:x\mapsto x^m z^{a-m},\qquad y\mapsto y,\qquad z\mapsto z^a,
\qquad m,a\in\mathbf F_p^\times,
\]
and
\[
[x^m z^{a-m},y]=x^{pm}z^{-pm}
=(x^m z^{a-m})^p(z^a)^{-p}.
\]
On
\[
A=W_p^{ab}=\mathbf Z_p^3/\langle p(e_x-e_z)\rangle,
\]
the torsion generator satisfies
\[
g_*(e_x-e_z)=m(e_x-e_z),
\]
so torsion preservation allows (m\ne a). Thus the scalar-equality step is **FAIL / CLOSED**.

The corrected explicit image subgroup is
\[
S'_{11}(p)=
\left\{
\begin{pmatrix}
m&b&0\\
0&1&0\\
a-m&d&a
\end{pmatrix}
:
m,a\in\mathbf F_p^\times, b,d\in\mathbf F_p
\right\},
\]
with
\[
|S'_{11}(p)|=p^2(p-1)^2.
\]

Classification:
- (n<p: W_n\cong(\mathbf F_p)^3, IA(W_n)=1, \operatorname{Aut}(W_n)=GL_3(\mathbf F_p)): **PASS / CLOSED**.
- (IA(W_p)\cong\operatorname{Hom}(\mathbf F_p^3,\mathbf F_p^2)\cong\mathbf F_p^6): **PASS / CLOSED**.
- (S_{11}(p)) with order (p^2(p-1)): **FAIL / CLOSED**.
- (S'_{11}(p)\subseteq\operatorname{Im}(\operatorname{Aut}(W_p)\to GL(V))): **PASS / CLOSED**.
- Exact equality \(\operatorname{Im}=S'_{11}(p)\): **OPEN / LOAD-BEARING**; an upper-bound proof is still required.
- Consequently \(|\operatorname{Aut}(W_p)|\ge p^8(p-1)^2\), while the exact order remains **OPEN**.
- The already audited (J_k^2), corrected (C_{a,b,k}=T_{a,b,k}\circ L), and kernel-preservation route remain **PASS / CLOSED / GENERAL** within their declared scope.

This supersedes the previous (S_{11})-based Step 3 target. Detailed audit:
`research/PAPER5_STEP3_S11_UPPER_BOUND_COUNTEREXAMPLE_AUDIT_2026-10-06.md`.


## 2026-10-06 — W_p relation-package consistency audit

**FAIL / CLOSED as submitted.**

The proposed (n=p) upper-bound proof simultaneously assumes
[
D_p(W_p)=\mathbf F_p^2=\langle x^{[p]},y^{[p]}\rangle,qquad x^{[p]}=z^{[p]},
]
and the defining relation
[
[x,y]=x^p z^{-p}.
]
Since (D_{p+1}(W_p)=1), these are equalities in (W_p), so they imply
[
[x,y]=1.
]
The subsequent coefficient comparison
[
x^{p(mv-bu)}z^{-p(mv-bu)}
=x^{pm}y^{pu}z^{p(c-a)}
]
cannot then extract (mv=m): that step requires (x^p) and (z^p) to be independent, contradicting (x^p=z^p).

Therefore the submitted deductions (m_{y,x}=0, m_{y,y}=1, c=a-m), the equality (operatorname{Im}=S'_{11}(p)), and the exact (IA(W_p)\cong\mathbf F_p^6) / automorphism-order claims are **not closed** and are **FAIL / CLOSED as submitted**.

The actual presentation-level relation
[
[x,y]=x^p z^{-p}
]
does not itself imply (x^p=z^p). Hence the correct next gate is to recompute (D_2(W_p),D_p(W_p),Z(W_p),W_p^{ab}), and (IA(W_p)) directly from
[
W_p=F/(R D_{p+1}).
]

Audit: `research/PAPER5_WP_BOUNDARY_CONSISTENCY_AUDIT_2026-10-06.md`.


## 2026-10-06 — W_p corrected D_p structure closes Step 3

The previous boundary audit is superseded by the corrected intrinsic calculation. At (n=p),
[
D_p(W_p)=\langle X=x^p,Y=y^p,Z=z^p\rangle\cong\mathbf F_p^3,
qquad [x,y]=XZ^{-1},
]
with (D_p) central of exponent (p). The relation therefore does not impose (X=Z); it records the commutator as (XZ^{-1}).

Consequently
[
IA(W_p)\cong\operatorname{Hom}(V,D_p)\cong\mathbf F_p^9.
]
For an arbitrary automorphism, centrality of (g(z)) gives (g(z)\equiv z^a\pmod{D_2}), and writing
[
g(x)\equiv x^m y^u z^c,qquad g(y)\equiv x^b y^v z^d
]
the defining relation gives
[
X^{mv-bu}Z^{-(mv-bu)}=X^mY^uZ^{c-a}.
]
Independence of (X,Y,Z) forces
[
u=0,qquad v=1,qquad c=a-m.
]
Thus
[
\operatorname{Im}(\operatorname{Aut}(W_p)\to GL(V))
\subseteq S'_{11}(p),
]
where
[
S'_{11}(p)=
\left\{
\begin{pmatrix}
m&b&0\\
0&1&0\\
a-m&d&a
\end{pmatrix}
:m,a\in\mathbf F_p^\times, b,d\in\mathbf F_p
\right\}.
]
The explicit realization family gives the reverse inclusion, so
[
\operatorname{Im}=S'_{11}(p),qquad |\operatorname{Im}|=p^2(p-1)^2.
]
Hence
[
|\operatorname{Aut}(W_p)|=p^9\,p^2(p-1)^2
=p^{11}(p-1)^2.
]

Classification:
- (D_p(W_p)\cong\mathbf F_p^3): **PASS / CLOSED / GENERAL**.
- (IA(W_p)\cong\mathbf F_p^9): **PASS / CLOSED / GENERAL**.
- (m_{y,x}=0, m_{y,y}=1, c=a-m): **PASS / CLOSED / GENERAL**.
- (S'_{11}(p)\subseteq\operatorname{Im}): **PASS / CLOSED / GENERAL**.
- (\operatorname{Im}=S'_{11}(p)): **PASS / CLOSED / GENERAL**.
- (|\operatorname{Aut}(W_p)|=p^{11}(p-1)^2): **PASS / CLOSED / GENERAL**.
- Previous (D_p\cong\mathbf F_p^2), (IA\cong\mathbf F_p^6), and (p^8(p-1)^2) claims: **FAIL / CLOSED / SUPERSEDED**.

Detailed audit: `research/PAPER5_WP_CORRECTED_STRUCTURE_STEP3_CLOSURE_2026-10-06.md`.


## 2026-10-06 — Paper 5 four-gate literature audit

The four-gate literature audit (finite Zassenhaus windows / relation modules and initial forms / IA-Frattini image / p^2 automorphism-order phenomenon) closes the **literature novelty gate within the searched scope**. Jennings–Lazard, free pro-p/Magnus–Zassenhaus, Labute relation-ideal machinery, and general IA/Frattini facts are established prior art. No identified source gives the specific intrinsic finite-window calculation for the present W_p=F/(R D_{p+1}), nor the factorization of Aut(W_n) -> GL(W_n/Phi(W_n)) through the mixed degree-(2,p) relation-jet stabilizer with the observed p^2 order phenomenon.

**Critical consistency correction:** the current corrected W_p result is D_p(W_p) isomorphic to F_p^3, IA(W_p) isomorphic to F_p^9, and |Aut(W_p)|=p^{11}(p-1)^2. Any literature-audit note stating D_p isomorphic to F_p^2, IA isomorphic to F_p^6, or |Aut|=p^8(p-1)^2 is historical/superseded and must not be propagated.

Classification: **PASS / CLOSED for literature novelty boundary; OPEN / LOAD-BEARING for the W_{p+1} intrinsic factorization and p^2 theorem.** Detailed audit: research/PAPER5_LITERATURE_AUDIT_2026-10-06.md.


## 2026-10-06 — Paper 5 W_{p+1}=W_p stabilization claim audit

**FAIL / CLOSED as submitted.** The proposed proof incorrectly evaluates the Jennings–Lazard filtration at n=p+1. The terms (i,j)=(2,1) and (1,2) contribute gamma_2(F)^p and F^{p^2}, so

D_{p+1}(F)=gamma_{p+1}(F) gamma_2(F)^p F^{p^2}

rather than gamma_{p+1}(F). The claimed equality gr_{p+1}(R)=gr_{p+1}(F) is also unsupported: the ideal generated by the present quadratic relation line is not automatically the whole degree-(p+1) free Lie layer.

Therefore W_{p+1}=W_p is not established, and the stabilization-based explanation of the p^2 gap remains OPEN / LOAD-BEARING. This is consistent with the earlier audited fact D_{p+1}(F) is not contained in R. Detailed audit: research/PAPER5_WP1_STABILIZATION_AUDIT_2026-10-06.md.

## 2026-10-06 — W_{p+1}=W_p stabilization corrected and CLOSED

The prior stabilization audit was superseded after re-evaluating the exact Jennings–Lazard product and the full relation subgroup.

For odd p,
D_{p+1}(F)=gamma_{p+1}(F) gamma_2(F)^p F^{p^2}.
The relation subgroup
R=< [x,z], [y,z], [x,y]^{-1}x^p z^{-p} >^F
has the full degree-two initial layer because the first two relators contribute [x,z],[y,z] and the third contributes -[x,y] modulo D_3. Thus gr_2(R)=gr_2(F). Since gr(R) is a restricted Lie ideal, the ordinary Lie component in degree p+1 is contained in gr_{p+1}(R); p+1 is not divisible by p, so no separate p-power component occurs there. Hence gamma_{p+1}(F) subset R D_{p+2}(F).

The exceptional factors satisfy gamma_2(F)^p subset D_{2p}(F) subset D_{p+2}(F) and F^{p^2} subset D_{p^2}(F) subset D_{p+2}(F). Therefore
D_{p+1}(F) subset R D_{p+2}(F),
so R D_{p+1}=R D_{p+2} and W_{p+1}=W_p.

Classification:
- D_{p+1}=gamma_{p+1}: FAIL/CLOSED.
- gr_2(R)=gr_2(F): PASS/CLOSED.
- gr_{p+1}(R)=gr_{p+1}(F): PASS/CLOSED in the declared free-pro-p/Zassenhaus setting.
- D_{p+1} subset R D_{p+2}: PASS/CLOSED.
- W_{p+1}=W_p: PASS/CLOSED/GENERAL.
- D_{p+1} subset R remains FAIL/CLOSED; x^{p^2} is still a counterexample.
- Step-3 equality Im(Aut(W_n)->GL(V))=S_11(p) remains OPEN/LOAD-BEARING.

Detailed audit: research/PAPER5_WP1_STABILIZATION_AUDIT_2026-10-06.md. The earlier 2026-10-06 stabilization FAIL audit is superseded.


## 2026-10-06 — p^2 comparison-window Addendum 2 audit

The proposed final closure
\[
U_p=W_p/L,\qquad |\operatorname{Aut}(W_p)|/|\operatorname{Aut}(U_p)|=p^2
\]
was audited and rejected **as submitted**.

First, \(L=Z(W_p)D_2/D_2\) is a line in \(V=W_p/D_2\), not a subgroup of \(W_p\); hence \(W_p/L\) is undefined until a canonical subgroup lift is specified. If \(C=\langle z\rangle\) is chosen instead, the quotient has a 2-dimensional Frattini quotient and its automorphism image/kernel must be recomputed independently; neither the same \(S'_{11}\) image nor a \(p^7\) kernel follows formally.

Second, the proposed relation condition \(b(\pi(x),y)\) is type-invalid for the already-defined \(b:\wedge^2V\to D_p\), since \(\pi(x)\in D_p\), not \(V\). A new action/pairing or derivation-level construction is required before a \(3\to2\) dimension cut can be proved.

Therefore:
- \(W_{p+1}=W_p\): PASS/CLOSED/GENERAL.
- intrinsic \(W_p\) relation-jet stabilizer \(S'_{11}\): PASS/CLOSED/GENERAL.
- \(\operatorname{Im}(\operatorname{Aut}(W_p)\to GL(V))=S'_{11}\): PASS/CLOSED/GENERAL.
- raw \(GL_3/S'_{11}\) p-primary index: \(p\).
- proposed \(U_p\) quotient comparison and \(Z^1_{\mathcal J_p}(V,L)\cong\mathbf F_p^2\): OPEN/LOAD-BEARING.
- exact \(p^2\) automorphism-order theorem: OPEN/LOAD-BEARING.

Detailed audit: research/PAPER5_P2_GAP_COMPARISON_WINDOW_AUDIT_2026-10-06.md.
