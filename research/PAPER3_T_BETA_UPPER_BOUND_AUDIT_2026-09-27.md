# PAPER 3 — T_beta UPPER-BOUND AUDIT: BOCKSTEIN KERNEL AND RECOGNITION THRESHOLD

Date: 2026-09-27

## Status
**PASS / CLOSED** for the upper-bound theorem in the declared category; combined with the existing S1/S2 lower bound, the exact threshold is **PASS / CLOSED**.

## Target
Let
\[
T_\beta(G)=[\beta_G],\qquad
\beta_G:H^1(G,\mathbf F_p)\to H^2(G,\mathbf F_p)
\]
be the Bockstein for
\[
0\to\mathbf F_p\to\mathbf Z/p^2\to\mathbf F_p\to0.
\]

For the odd-p fixed-rank Demushkin category, \(\dim H^1(G,\mathbf F_p)=d\) and \(\dim H^2(G,\mathbf F_p)=1\).

## Lemma 1 — Bockstein kernel = reduction of p^2-valued characters
The long exact sequence gives
\[
H^1(G,\mathbf Z/p^2)\to H^1(G,\mathbf F_p)
\xrightarrow{\beta_G}H^2(G,\mathbf F_p).
\]
With trivial coefficient action,
\[
\ker\beta_G=
\operatorname{im}\left[
\operatorname{Hom}_{\mathrm{cts}}(G,\mathbf Z/p^2)
\to\operatorname{Hom}_{\mathrm{cts}}(G,\mathbf F_p)
\right].
\]
Thus a mod-p character lies in the Bockstein kernel exactly when it lifts to a \(\mathbf Z/p^2\)-valued character. This is a general pro-p statement.

## Lemma 2 — \(G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}\) determines the Bockstein rank
Every \(\mathbf Z/p^2\)-valued character factors through
\[
G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}.
\]
Hence the reduction image, and therefore \(\ker\beta_G\), is determined functorially by this quotient.

The already closed filtration inclusion
\[
D_{p+1}(G)\subseteq G^{p^2}[G,G]
\]
implies that \(W_{p+1}(G)\) determines \(G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}\). Therefore \(W_{p+1}\) determines \(\ker\beta_G\) and
\[
\operatorname{rank}\beta_G=d-\dim\ker\beta_G.
\]

## Lemma 3 — rank determines the isomorphism class of the Bockstein map
For fixed rank \(d\), Demushkin duality gives
\[
\dim H^1(G,\mathbf F_p)=d,\qquad \dim H^2(G,\mathbf F_p)=1.
\]
Two linear maps \(V\to L\), with \(\dim V=d\) and \(\dim L=1\), are isomorphic under independent automorphisms of \(V,L\) iff they have the same rank. Hence \([\beta_G]\) is determined by \(\operatorname{rank}\beta_G\in\{0,1\}\).

Important precision: this does not say rank determines the Demushkin group or \(q\); it determines only the abstract linear-map isomorphism class of \(\beta\).

## Independent parameter check
For
\[
r_q=x^q[x,y],
\]
the direct relator calculation gives
\[
\beta(\chi_x)=\frac qp\,u,\qquad \beta(\chi_y)=0.
\]
Thus for \(q=p^f\), rank \(\beta=1\) when \(f=1\), and rank \(\beta=0\) when \(f\ge2\), agreeing with the liftability description.

## Upper bound and exact threshold
For every group in the declared fixed-rank odd-p Demushkin category,
\[
W_{p+1}(G)\cong W_{p+1}(H)\Longrightarrow [\beta_G]\cong[\beta_H],
\]
so
\[
r_{T_\beta}\le p+1.
\]
The existing S1/S2 pair gives \(r_{T_\beta}\ge p+1\). Therefore
\[
\boxed{r_{T_\beta}=p+1}
\]
for the declared category containing the full fixed-rank odd-p Demushkin family and the S1/S2 separation pair.

## Logical boundary
This closes the exact Bockstein recognition threshold. It does not prove
\[
f_{T_\beta}\ne r_{T_\beta}.
\]
The factorization threshold for the same target \(T_\beta\) must be defined and tested separately.

## Classification
- Bockstein kernel/liftability lemma: **PASS / CLOSED**
- \(G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}\Rightarrow\ker\beta\): **PASS / CLOSED**
- rank-to-linear-map-isomorphism step: **PASS / CLOSED**
- \(W_{p+1}\Rightarrow T_\beta\): **PASS / CLOSED**
- \(r_{T_\beta}\le p+1\): **PASS / CLOSED**
- \(r_{T_\beta}=p+1\): **PASS / CLOSED** in the declared category
- same-target factorization-vs-recognition separation: **OPEN / LOAD-BEARING**

No new Massey computation is authorized by this result.
