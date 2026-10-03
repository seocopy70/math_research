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
