undefined

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
G_{s,a}(r_2)=langle z,x_1,ldots,x_dmid z^{p^s}=x_1^{p^a}r_2angle,
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
