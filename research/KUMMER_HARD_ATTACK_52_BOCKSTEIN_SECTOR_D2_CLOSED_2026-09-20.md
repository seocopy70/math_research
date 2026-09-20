# HARD ATTACK 52 — THE Bockstein FIBER SECTOR IS d2-CLOSED

Date: 2026-09-20

## Target

HA51 reduced the uncertainty to the nine-dimensional fiber-Bockstein summand
\[
\beta_W(W^*)\subset H^2(W,\mathbf F_3).
\]
The question is whether
\[
d_2(\beta_W(W^*))=0.
\]

## Pushout/naturality argument

Let \(\varphi:W\to\mathbf F_3\) be any nonzero linear functional. Push out the central extension
\[
1\to W\to Q_2\to V\to1
\]
along \(\varphi\). This gives a central extension
\[
1\to\mathbf F_3\to E_\varphi\to V\to1.
\]

Let \(u\in H^1(\mathbf F_3,\mathbf F_3)\) be the fiber generator. Under the induced map of LHS spectral sequences,
\[
u\longmapsto\varphi\in H^1(W,\mathbf F_3),
\qquad
\beta(u)\longmapsto\beta_W(\varphi).
\]

For a central extension with cyclic kernel \(C_3\) and odd-prime coefficients, the standard low-degree LHS calculation has
\[
d_2(u)=c_\varphi\in H^2(V,\mathbf F_3),
\qquad
d_2(\beta u)=0,
\]
while the Bockstein of the extension class appears one page later as the corresponding \(d_3\)-phenomenon. This standard pattern is explicitly documented in the literature for cyclic p-kernels; the source used as a methodological cross-check records \(d_2(t)=0\) for the degree-two Bockstein generator and identifies the next Bockstein differential with \(\beta(\alpha)\). See the literature audit used for this step.

By naturality of the LHS spectral sequence under the pushout,
\[
d_2(\beta_W(\varphi))
=
\varphi_*\bigl(d_2(\beta u)\bigr)
=
0.
\]
Since every element of \(\beta_W(W^*)\) arises this way,
\[
\boxed{d_2(\beta_W(W^*))=0.}
\]

This argument does not require a rho-scan and does not assume a particular basis of W.

## Consequence

HA51 proved that
\[
d_2|_{\Lambda^2W^*}
\]
has rank 36. HA52 proves that the remaining 9-dimensional Bockstein summand lies in the kernel. Therefore
\[
\boxed{\operatorname{rank}d_2^{0,2}=36}
\]
and hence
\[
\boxed{\dim E_3^{2,1}=55-36=19.}
\]

So the previous 10--19 uncertainty collapses to an exact 19-dimensional E3 survivor.

## Important boundary

This is only an E3 statement. It does NOT prove that the 19-dimensional sector survives to E_infinity. The Bockstein part is now expected to interact with the next differential; the cyclic-kernel model suggests that its extension-class obstruction first appears through a d3/Bockstein mechanism. That higher differential must still be computed for the rank-9 central extension.

Also, the 19-dimensional space has not yet been identified as an H-module. No identification with a previously known 10-, 14-, 19-, or 25-dimensional module is allowed without an actual representation calculation.

## Decision

- d2 on the fiber-Bockstein summand vanishes: **PASS / CLOSED**, by pushout naturality plus the standard cyclic-kernel LHS calculation.
- rank d2^{0,2}=36: **PASS / CLOSED**.
- dim E3^{2,1}=19: **PASS / CLOSED**.
- exact H-module structure of E3^{2,1}: **OPEN / LOAD-BEARING**.
- higher d3/higher-differential survival: **OPEN / LOAD-BEARING**.
- full beta_rho^2: **OPEN / LOAD-BEARING**.
- unique coker maximizer without PD²: **OPEN / DECISIVE**.

## Next authorized attack

Compute the first higher differential affecting the 19-dimensional survivor, beginning with the Bockstein-originated d3 mechanism, and identify the H-module structure before attempting any selector conclusion.
