# HARD ATTACK 51 — THE EXTERIOR FIBER SECTOR CONTRIBUTES AT LEAST 36 TO d2

Date: 2026-09-20

## Target

HA50 proved
\[
10\le \dim E_3^{2,1}\le55.
\]
The next question is the rank of
\[
d_2^{0,2}:H^2(W,\mathbf F_3)\to H^2(V,\mathbf F_3)\otimes W^*.
\]
Split
\[
H^2(W)=\Lambda^2W^*\oplus\beta_W(W^*).
\]

## Exterior sector

Choose a basis \(w_1^*,\dots,w_9^*\) of \(W^*\), and write
\[
c_i=d_2(w_i^*)\in H^2(V,\mathbf F_3).
\]
HA45 identifies \(d_2:W^*\to H^2(V)\) with the inclusion of the 9-dimensional hyperplane
\[
K\subset H^2(V),
\]
so \(c_1,\dots,c_9\) are linearly independent.

By multiplicativity/Leibniz for the LHS differential,
\[
d_2(w_i^*w_j^*)=c_i\otimes w_j^*-c_j\otimes w_i^*
\]
(up to the common sign convention).

Consider a linear combination
\[
\sum_{i<j}a_{ij}d_2(w_i^*w_j^*).
\]
The coefficient of \(w_j^*\) is a linear combination of the independent vectors \(c_i\). Hence vanishing of the total output forces every \(a_{ij}=0\).

Therefore
\[
\boxed{
d_2|_{\Lambda^2W^*}\text{ is injective, hence has rank }36.
}
\]

This is a theorem-level consequence of the already closed rank-nine transgression; no rho-scan is involved.

## Immediate dimension consequence

Since the full source \(H^2(W)\) has dimension 45,
\[
36\le \operatorname{rank}d_2^{0,2}\le45.
\]
Combining with HA50,
\[
\boxed{
10\le \dim E_3^{2,1}\le19.
}
\]

Thus the previous lower bound 10 is sharpened to a 10--19 dimensional window.

## Bockstein sector boundary

The remaining nine-dimensional source is \(\beta_W(W^*)\). A standard transgression/Bockstein compatibility heuristic suggests that the fiber Bockstein generators may first contribute at the next differential (analogous to the familiar d_3/Bockstein-of-extension phenomenon), but this has NOT been promoted to a theorem here. In particular, we do not yet claim
\[
d_2(\beta_W(W^*))=0.
\]

If that equality is proved, then rank \(d_2^{0,2}=36\) and
\[
\dim E_3^{2,1}=19.
\]
If the Bockstein sector contributes rank r\in\{1,\dots,9\}, then
\[
\dim E_3^{2,1}=19-r.
\]

## Decision

- \(d_2|_{\Lambda^2W^*}\) injective/rank 36: **PASS / CLOSED**.
- \(10\le\dim E_3^{2,1}\le19\): **PASS / CLOSED**.
- \(d_2(\beta_W(W^*))=0\): **OPEN**.
- exact \(\dim E_3^{2,1}\): **OPEN / LOAD-BEARING**.
- H-module structure and higher-differential survival: **OPEN**.
- full \(\beta_\rho^2\): **OPEN / LOAD-BEARING**.

## Next authorized attack

Resolve the Bockstein-sector differential directly, preferably by a cochain/transgression calculation or a precise spectral-sequence compatibility theorem. Do not infer it merely from analogy.
