# Paper 3 — T_beta Factorization Threshold Audit

Date: 2026-09-27
Status: **PASS / CLOSED**

## Scope

This audit independently determines the factorization threshold for the same target
\[
T_\beta(G)=[\beta_G],\qquad
\beta_G:H^1(G,\mathbf F_p)\to H^2(G,\mathbf F_p),
\]
in the fixed odd-p fixed-rank Demushkin category with the declared Zassenhaus-window convention.

The result \(r_{T_\beta}=p+1\) is not used as evidence for the factorization threshold.

## Definition

\[
f_{T_\beta}(\mathcal C;D_\bullet)
=
\min\{n:T_\beta\text{ factors through }W_n\}.
\]

Thus factorization at level n means that there is a well-defined assignment from the n-window to the Bockstein target isomorphism class.

## Upper bound: direct factorization through W_{p+1}

For every pro-p group,
\[
D_{p+1}(G)\subseteq G^{p^2}[G,G].
\]

Hence the quotient
\[
G/[G^{p^2}[G,G]]
\cong G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}
\]
is functorially recoverable from \(G/D_{p+1}(G)\), because the image of
\(G^{p^2}[G,G]\) is
\[
(G/D_{p+1})^{p^2}[(G/D_{p+1}),(G/D_{p+1})].
\]

For
\[
0\to\mathbf F_p\to\mathbf Z/p^2\to\mathbf F_p\to0,
\]
the long exact sequence gives
\[
\ker\beta_G=
\operatorname{im}\left[
\operatorname{Hom}(G,\mathbf Z/p^2)
\to
\operatorname{Hom}(G,\mathbf F_p)
\right].
\]

All \(\mathbf Z/p^2\)-valued characters factor through
\(G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}\). Therefore \(W_{p+1}\) determines \(\ker\beta_G\), hence \(\operatorname{rank}\beta_G\).

In the fixed-rank Demushkin category,
\[
\dim H^2(G,\mathbf F_p)=1.
\]
So the isomorphism class of the linear map
\[
\beta_G:\mathbf F_p^d\to\mathbf F_p
\]
is determined by its rank.

Thus there is a well-defined factorization
\[
W_{p+1}\longmapsto[\beta_G],
\]
and
\[
f_{T_\beta}\le p+1.
\]

## Lower bound: W_p does not determine T_beta

Use the independently verified pair
\[
G_p=\langle x,y\mid x^p[x,y]=1\rangle,
\qquad
G_{p^2}=\langle x,y\mid x^{p^2}[x,y]=1\rangle.
\]

S1 gives
\[
W_p(G_p)\cong W_p(G_{p^2})
\]
for the declared unmarked Zassenhaus window.

Independently, S2 gives
\[
\operatorname{rank}\beta_{G_p}=1,
\qquad
\operatorname{rank}\beta_{G_{p^2}}=0.
\]
Hence
\[
T_\beta(G_p)\not\cong T_\beta(G_{p^2}).
\]

Therefore no function of \(W_p\) alone can determine \(T_\beta\), so
\[
f_{T_\beta}>p.
\]

This lower bound is independent of the recognition equality.

## Conclusion

The two direct bounds are
\[
p<f_{T_\beta}\le p+1.
\]
Therefore
\[
\boxed{f_{T_\beta}=p+1}.
\]

Combined with the separately proved recognition result, this yields
\[
\boxed{f_{T_\beta}=r_{T_\beta}=p+1}
\]
for the declared category, filtration and window convention.

This is an equality result, not a separation result.

## Logical boundary

The general distinction between factorization and recognition remains meaningful. What is now closed is only the proposed same-target Bockstein separation in this particular category/window.

Any future separation search must vary at least one of the target, category, or filtration/window structure. No universal equality theorem is claimed.

## Classification

- factorization definition: **PASS / CLOSED**
- \(f_{T_\beta}\le p+1\): **PASS / CLOSED**
- \(f_{T_\beta}>p\): **PASS / CLOSED**
- \(f_{T_\beta}=p+1\): **PASS / CLOSED**
- same-target \(T_\beta\) separation: **FAIL / CLOSED**
- general factorization-vs-recognition separation program: **OPEN / LOAD-BEARING**

Detailed evidence:
- S1: \(W_p(G_p)\cong W_p(G_{p^2})\)
- S2: \(T_\beta(G_p)\not\cong T_\beta(G_{p^2})\)
- T_beta upper-bound audit: \(W_{p+1}\Rightarrow G_{\mathrm{ab}}/p^2G_{\mathrm{ab}}\Rightarrow[\beta_G]\)
