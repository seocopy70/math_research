# HA61-B3 — GENERAL A_2-LIFT GAUGE TEST — 2026-09-20

## Status

**HA61-B3: PASS / CLOSED.**

The A_2-lift gauge
\[
z \mapsto z+d_{A_2}\phi
\]
cannot change the secondary connecting obstruction. This is not merely a q=3/q=9 numerical observation: it follows formally from the connecting-map construction.

## 1. Setup

Consider
\[
0\to \mathbf F_3\to A_3\xrightarrow{\pi}A_2\to0,
\]
and let \(z\in Z^1(G,A_2)\). Choose an arbitrary cochain lift
\(\widetilde z\in C^1(G,A_3)\), so \(\pi(\widetilde z)=z\).

The secondary obstruction is represented by
\[
d_{A_3}\widetilde z\in Z^2(G,\mathbf F_3),
\]
after identifying the kernel \(\ker\pi\cong\mathbf F_3\).

## 2. Gauge transformation

Let \(\phi\in C^0(G,A_2)\) and replace
\[
z' = z+d_{A_2}\phi.
\]

Choose any lift \(\widetilde\phi\in C^0(G,A_3)\) with
\(\pi(\widetilde\phi)=\phi\), and use the compatible lift
\[
\widetilde z'
=
\widetilde z+d_{A_3}\widetilde\phi.
\]

Then
\[
d_{A_3}\widetilde z'
=
d_{A_3}\widetilde z+d_{A_3}^2\widetilde\phi
=
d_{A_3}\widetilde z.
\]

Hence the obstruction cocycle is unchanged **already at cochain level**.

Therefore
\[
\boxed{\delta_3([z'])=\delta_3([z])}.
\]

No residual term can acquire a nonzero change merely from changing the A_2 cocycle representative by a coboundary.

## 3. Consequence for B_{rho_2}

Suppose a crossed-word expansion is written schematically as
\[
\delta_3(z)
=
[f(t_2)+B_{\rho_2}(z)+(\mu\wedge f)(R)+E_{\ge4}(z)]\omega.
\]

The total expression is gauge-invariant. Therefore any apparent variation of
\(B_{\rho_2}\) under
\(z\mapsto z+d\phi\) must be cancelled by another displayed term or must itself be zero in the obstruction class.

Thus:

- a genuinely gauge-dependent \(B_{\rho_2}\) cannot be an intrinsic secondary invariant;
- the B3 gauge test cannot by itself prove \(B_{\rho_2}=0\);
- it does prove that any surviving \(B_{\rho_2}\) must be a function of the cohomology-level input, not of the arbitrary cocycle representative.

This is the exact logical correction required after the earlier overclaim.

## 4. Stronger distinction: representative gauge vs. lift-class ambiguity

B3 closes only **representative gauge**.

It does not identify all A_2-valued cohomology lifts of the same
\(f\in H^1(G,\mathbf F_3)\). If \(\delta_2(f)=0\), the set of lifts of \(f\) is generally a torsor under the kernel contributed by
\(H^1(G,\mathbf F_3)\). Therefore one must not silently replace “gauge independence” by “independence of the chosen A_2 lift class.”

That remaining ambiguity is exactly where a nontrivial secondary datum could still hide.

## 5. B4 target sharpened

The next question is therefore:

> After quotienting by coboundary gauge, does the non-\mu part of the secondary obstruction define a canonical linear functional
> \[
> H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3)
> \]
> represented by the intrinsic next filtered residual \(t_2\)?

Equivalently, for a fixed primary-zero \(f\), determine whether every admissible A_2 lift gives
\[
\delta_3(z)- (\mu\wedge f)(R)
=
f(t_2)\,\omega
\]
with the same intrinsic \(t_2\), rather than an additional lift-class parameter.

No claim of B4 closure is made here.

## Decision

\[
\boxed{\text{HA61-B3 = PASS / CLOSED}}
\]

\[
\boxed{\text{HA61-B4 = OPEN / LOAD-BEARING}}
\]

B5 remains unopened until the B4 source is isolated.
