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
