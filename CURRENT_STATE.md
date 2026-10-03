undefined

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
