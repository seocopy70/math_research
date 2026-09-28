# PAPER 3 — D2 REPAIR: TRANSgression-QUOTIENT FINITE CARRIER

Date: 2026-09-28

## Status

**PASS / CLOSED at the declared finite-selector scope, replacing the false bare-Q_k H^2-inflation argument.**

The previous claim that
\[
H^2(Q_k,\mathbf F_p)\to H^2(G,\mathbf F_p)
\]
is injective is false and remains rejected.

The repair does not try to remove the transient kernel. Instead it quotients it out using the canonical one-step extension.

## 1. Finite window

Let
\[
N_k=p^{k-1},\qquad Q_k=W_{N_k+1}=G/D_{N_k+1},
\]
and let
\[
E_k=W_{N_k+2}=G/D_{N_k+2}.
\]

Set
\[
K_k=D_{N_k+1}/D_{N_k+2}.
\]

By the Zassenhaus commutator property
\[
[D_i(G),G]\subseteq D_{i+1}(G),
\]
the kernel K_k is central in E_k. Hence there is an intrinsic central extension
\[
1\to K_k\to E_k\to Q_k\to1.
\]

## 2. The correct finite obstruction quotient

Since K_k\subseteq\Phi(E_k), inflation
\[
H^1(Q_k,\mathbf F_p)\to H^1(E_k,\mathbf F_p)
\]
is an isomorphism. Therefore the restriction term in the five-term sequence is zero and the transgression
\[
\operatorname{tra}_k:H^1(K_k,\mathbf F_p)^{Q_k}\to H^2(Q_k,\mathbf F_p)
\]
is injective.

Exactness gives
\[
\ker\bigl(H^2(Q_k,\mathbf F_p)\to H^2(E_k,\mathbf F_p)\bigr)
=
\operatorname{im}(\operatorname{tra}_k).
\]

Define the finite obstruction carrier
\[
\boxed{
\mathcal O_k(G):=
H^2(Q_k,\mathbf F_p)/
\operatorname{im}(\operatorname{tra}_k).
}
\]

This is intrinsic to the finite extension
\[
E_k\twoheadrightarrow Q_k.
\]

No canonical orientation, presentation, relator, q, or Fox coordinate is inserted.

## 3. Why this repairs D2

The crucial point is that the selector does **not** require
\[
H^2(Q_k)\hookrightarrow H^2(G).
\]

For every class \alpha\in H^2(Q_k) with nonzero global inflation,
\[
\inf_{Q_k}^G(\alpha)\neq0,
\]
we automatically have
\[
\alpha\notin\ker(H^2(Q_k)\to H^2(E_k))
=
\operatorname{im}(\operatorname{tra}_k).
\]

Therefore
\[
[\alpha]\neq0\quad\text{in }\mathcal O_k(G).
\]

Thus \mathcal O_k retains exactly the part of finite H^2 that survives the first deeper window; it need not equal the full stable image in H^2(G).

## 4. Canonical branch

For the canonical lift \chi_k, classical Kummerianity gives a global lift of every mod-p cohomology class. By the finite crossed-cocycle factorization through Q_k, that lift already factors through Q_k.

Hence the finite connecting map itself vanishes:
\[
\delta_{k,\chi_k}=0
\quad\text{in }H^2(Q_k,\mathbf F_p),
\]
and therefore also in \mathcal O_k(G).

This is stronger than merely saying its global image vanishes.

## 5. False branch

Let
\[
\rho_k'=\rho_k(1+p^{k-1}\nu),
\qquad
0\neq\nu\in H^1(G,\mathbf F_p).
\]

The audited coefficient-extension variation identity gives
\[
\delta_{k,\rho_k'}(f)-\delta_{k,\rho_k}(f)
=
\iota_*(\nu\smile\bar f).
\]

Along the canonical branch \delta_{k,\rho_k}=0. Demuškin cup nondegeneracy gives
\[
\exists a\in H^1(G,\mathbf F_p):
\quad \nu\smile a\neq0.
\]

The reduction map supplies f with \bar f=a.

The finite factorization theorem gives a representative
\[
\alpha_k\in H^2(Q_k,\mathbf F_p)
\]
whose inflation to G is, by the same variation identity,
\[
\inf_{Q_k}^G(\alpha_k)=\nu\smile a\neq0.
\]

Consequently
\[
\alpha_k\notin\operatorname{im}(\operatorname{tra}_k),
\]
and hence
\[
\boxed{
[\alpha_k]\neq0\in\mathcal O_k(G).
}
\]

Therefore every false lift has a nonzero finite obstruction output in \mathcal O_k.

## 6. Selector theorem

The finite selector can therefore be defined using the induced connecting map
\[
\bar\delta_{k,\rho_k}:
H^1(Q_k,\mathbf Z/p^{k-1}(\rho_{k-1}))
\longrightarrow
\mathcal O_k(G).
\]

Then
\[
\boxed{
\bar\delta_{k,\rho_k}=0
\iff
\rho_k=\chi_G\pmod{p^k}
}
\]
at the declared Demuškin scope, assuming the previously audited arbitrary-candidate factorization and global variation/PD² uniqueness inputs.

The forward direction is the false-lift separation argument above; the reverse direction is canonical Kummerianity plus finite factorization.

## 7. What is and is not proved

### CLOSED

- The bare-Q_k H^2-inflation injectivity claim is permanently rejected.
- The one-step transgression quotient \mathcal O_k is a valid finite intrinsic carrier.
- The canonical branch has zero finite obstruction map.
- Every false lift has some nonzero finite obstruction output.
- The full finite selector can be formulated on \mathcal O_k without computing a stable kernel or finding an unknown deeper m_0.
- The repair is q-blind at the selector-definition level.

### NOT CLAIMED

- \mathcal O_k\cong H^2(G,\mathbf F_p).
- \mathcal O_k is one-dimensional.
- \mathcal O_k is absolutely minimal among all finite carriers.
- The full finite H^2 kernel equals the one-step transgression kernel.
- Publication novelty is unconditional.

## 8. Important conceptual consequence

The earlier deeper-window problem asked for the smallest m such that finite H^2 becomes globally faithful. That is stronger than necessary.

For recognition, it is enough to quotient out the **first transient sector** and prove that every false variation has a globally nonzero output. Thus:

\[
\boxed{
\text{recognition does not require stable H^2 reconstruction.}
}
\]

This removes the need for an unknown uniform stabilization bound m_0.

## 9. Fixed p=3, rank 4, k=2 specialization

Here
\[
Q_2=W_4,\qquad E_2=W_5,
\]
and
\[
K_2=P_4/P_5,
\qquad
\dim_{\mathbf F_3}K_2=45.
\]

The previous hand calculation gives
\[
\ker(H^2(W_4)\to H^2(W_5))
=
\operatorname{im}(\operatorname{tra}_2),
\]
of dimension 45, so
\[
\mathcal O_2
=
H^2(W_4,\mathbf F_3)/
\operatorname{im}(\operatorname{tra}_2).
\]

The new point is that no 45-dimensional delta-family intersection calculation is needed. The false-lift witness has nonzero global inflation and therefore cannot lie in the transgression sector.

## 10. Final classification

- Previous bare-Q_k H^2-inflation injectivity: **FAIL / CLOSED**.
- Continuity/stable-kernel argument: **PASS / LOCAL but no longer load-bearing**.
- One-step transgression quotient carrier \mathcal O_k: **PASS / CLOSED**.
- Finite canonical zero map on \mathcal O_k: **PASS / CLOSED**.
- False-lift separating output on \mathcal O_k: **PASS / CLOSED**.
- Corrected arbitrary-(p,d,q,k) D2 finite reconstruction: **PASS / CLOSED**, conditional only on the already-audited factorization and global Demuškin variation inputs.
- D3 uniqueness: **PASS / LOCAL -> promoted to finite-selector scope via D2 repair**.
- D4 LTE threshold: **PASS / LOCAL -> combined with repaired D2 for the selector theorem**.
- Absolute carrier minimality: **OPEN / NOT CLAIMED**.
- Publication novelty: **OPEN / CONDITIONAL**.

## Core statement

\[
\boxed{
\begin{gathered}
Q_k=W_{p^{k-1}+1},\quad
E_k=W_{p^{k-1}+2},\\
\mathcal O_k=
H^2(Q_k,\mathbf F_p)/
\operatorname{im}\operatorname{tra}
\end{gathered}
}
\]

is sufficient to replace the false bare-Q_k H^2-injectivity step.

The key methodological shift is:

\[
\boxed{
\text{do not reconstruct global }H^2;
\quad
\text{quotient the finite transient obstruction that can hide it.}
}
\]
