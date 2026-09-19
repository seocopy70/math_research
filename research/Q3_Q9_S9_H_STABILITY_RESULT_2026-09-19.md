# Q3/Q9 — S9 degree-9 H-stability result

Date: 2026-09-19

## Status

**FAIL — mathematical failure, after corrected exact F3 verification.**

The q=9 degree-9 relation space
\[
(I_9)_9=(I_\infty)_9\oplus\langle S_9\rangle,
\qquad \dim(I_9)_9=13525
\]
is not stable under the fixed H=Sp_4(F_3) action.

## 1. Exact witness

Use the authoritative symplectic convention
\[
J=\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}
\]
and the fixed transvection
\[
t_{e_2}=I+e_2(Je_2)^T.
\]

Direct exact calculation gives
\[
t_{e_2}(e_1)=e_1+e_2.
\]

Since the restricted ninth-power layer L_1^[9] has the same coefficient action over F_3,
\[
t_{e_2}(S_9)=X_1^{[9]}+X_2^{[9]}=S_9+X_2^{[9]}.
\]

## 2. Why this leaves the q=9 relation space

S9-B established
\[
(I_\infty)_9\cap L_1^{[9]}=0.
\]

The degree-9 q=9 space has L1^[9] projection exactly
\[
\langle S_9\rangle=\langle X_1^{[9]}\rangle.
\]

But
\[
S_9+X_2^{[9]}\notin\langle S_9\rangle.
\]

Exact F3 rank check:
\[
\operatorname{rank}\{S_9\}=1,
\qquad
\operatorname{rank}\{S_9,t_{e_2}S_9\}=2.
\]

Because the baseline has zero L1^[9] projection, it cannot absorb the new X2^[9] component. Hence
\[
t_{e_2}S_9\notin(I_9)_9.
\]

Therefore
\[
\boxed{(I_9)_9\text{ is not }H\text{-stable}.}
\]

## 3. Implementation correction during audit

The first committed draft used the wrong sign for t_{e2}(e1). The authoritative J convention gives Je2=e1, hence
\[
t_{e_2}(e_1)=e_1+e_2,
\]
not e1+2e2.

This was caught by an independent exact local check before accepting the result. The script was corrected in commit
836c3ce4d1382d35545c2998af2addf4a42c7a89.

The original incorrect attempt is classified as INVALID TEST / implementation error, not as mathematical evidence.

## 4. Gate consequence

The q=9 degree-9 relation-space construction itself remains valid:
\[
\dim(I_9)_9=13525.
\]

But it cannot be promoted as an H-stable degree-9 relation submodule.

Thus the planned downstream route
\[
I_{9,9}\longrightarrow gr_9(G_9)\longrightarrow D_9
\]
is blocked at the H-stability gate.

Do not infer a q=9 invariant or orientation recovery from the +1 dimension increment alone.

## Reproducibility

Script:
research/Q3_Q9_S9_H_stability_degree9_2026-09-19.py

Workflow:
.github/workflows/q3-q9-s9-h-stability.yml

The GitHub Actions API available in this session does not expose the push-triggered run, so no CI run identifier is claimed here. The substantive decision rests on the corrected exact local F3 computation plus the structural S9-B certificate.
