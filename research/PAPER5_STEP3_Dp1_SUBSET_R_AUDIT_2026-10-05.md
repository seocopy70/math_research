# Paper 5 Step 3 — Audit of the claimed (D_{p+1}\subseteq R) closure (2026-10-05)

## Classification

**FAIL / CLOSED as a proof route.** The claimed inclusion (D_{p+1}(F)\subseteq R) is false for the stated
\[
R=\langle[x,z],[y,z]\rangle^F\,\langle\rho\rangle^F,
\qquad \rho=[x,y]^{-1}x^pz^{-p}.
\]
Consequently the proposed one-line closure (RD_{p+1}=R) and the resulting Step 3 equality do not follow.

## Decisive graded obstruction

The proposed argument correctly observes that the ordinary Lie bracket part is killed from degree (2) onward, except for restricted-power contributions at degrees divisible by (p). The fatal point is the treatment of those restricted-power contributions.

At degree (n=kp), the restricted graded piece contains (p)-th powers of elements of degree (k). From
\[
y\in gr_k(R)\quad\Longrightarrow\quad y^{[p]}\in gr_{kp}(R)
\]
one may infer inclusion in the forward direction, but **not the converse**.

In particular (gr_p(F)\ne gr_p(R)): the degree-(p) restricted-power directions represented by (x^{[p]},y^{[p]},z^{[p]}) are not all in (gr_p(R)). Therefore at the next multiple,
\[
x^{[p^2]}=(x^{[p]})^{[p]}\in gr_{p^2}(F),
\]
there is no basis for putting this class in (gr_{p^2}(R)). The sentence “if (k\ge p+1), then …” only handles (k\) in the already-closed range and misses the exceptional case (k=p), which is exactly the obstruction at (n=p^2).

Thus the asserted induction
\[
gr_n(F)=gr_n(R)\quad(n\ge p+1)
\]
fails already at (n=p^2) (for every odd (p\ge3)).

## Concrete group-level witness

Pass to the abelian quotient
\[
A=\mathbf Z_p^3/\langle p(e_x-e_z)\rangle,
\]
with (x,y,z) mapped to (e_x,e_y,e_z). The generators of (R_0) vanish in the abelianization, while (ho) imposes exactly (p(e_x-e_z)=0). Hence (F/R) maps to (A).

The image of (x^{p^2}) is (p^2e_x\), which is nonzero in (A). Therefore
\[
x^{p^2}\notin R.
\]
But (x^{p^2}\in D_{p^2}(F)\subseteq D_{p+1}(F)). Hence
\[
\boxed{D_{p+1}(F)\not\subseteq R.}
\]

This is an independent group-level disproof, not merely a grading-convention objection.

## Consequence for Step 3

The proposed chain
\[
\tilde g(R)\subseteq RD_{p+1}=R
\]
cannot be used. The earlier audit remains controlling: the first-order congruence
\[
\tilde g(R)\subseteq RD_{p+1}
\]
may still be useful, but a genuine kernel-invariance mechanism is still required.

The correct unresolved problem is therefore to prove
\[
\tilde g(R)\subseteq R
\]
directly, or to replace it with an exact relation-module/presentation argument, or to construct a valid filtered induction whose residual terms are known to lie in the relevant graded relation subspaces.

## Status update

- \(D_{p+1}\subseteq R\): **FAIL / CLOSED**.
- \(gr_n(F)=gr_n(R)\) for all \(n\ge p+1\): **FAIL / CLOSED** as stated.
- \(\tilde g(R)\subseteq RD_{p+1}\): **PASS / LOCAL-GENERAL SUPPORT**, subject to the separate first-order audit.
- \(\tilde g(R)\subseteq R\): **OPEN / LOAD-BEARING**.
- \(\operatorname{Im}(\operatorname{Aut}(W_n)\to GL(V))=S_{11}(p)\): **OPEN / LOAD-BEARING**.
- uniform (p^2(p-1)) automorphism-order theorem: **CONDITIONAL**.

This audit supersedes the 2026-10-05 Step 3 closure claim based on (D_{p+1}\subseteq R).
