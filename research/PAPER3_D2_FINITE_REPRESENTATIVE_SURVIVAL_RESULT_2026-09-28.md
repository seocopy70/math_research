# PAPER 3 D2-A / D2-B — FINITE REPRESENTATIVE AND SURVIVAL RESULT — 2026-09-28

## Scope

This record resolves the declared D2 load-bearing implication for the fixed rank-four pro-3 Demushkin case
\[
W_4=G/P_4,\qquad W_5=G/P_5,
\]
without attempting to compute the full delta-family as a subspace of \(H^2(W_4,\mathbf F_3)\).

The target is exactly:
\[
\forall,0\ne\nu\in Q_4^*\cong H^1(G,\mathbf F_3)\quad
\exists f
\]
such that the global variation class
\[
[\nu\smile\bar f]\in H^2(G,\mathbf F_3)
\]
has a representative in \(H^2(W_4,\mathbf F_3)\) whose inflation to \(H^2(W_5,\mathbf F_3)\) is nonzero.

## 1. Choose a separating global class

For a false coefficient lift
\[
\rho_3'=\rho_3(1+9\nu),\qquad 0\ne\nu\in H^1(G,\mathbf F_3),
\]
the audited variation identity is
\[
\delta_{\rho_3'}(f)-\delta_{\rho_3}(f)
=
\nu\smile\bar f.
\]

On the canonical branch \(\rho_3=\chi_3\), Kummerianity gives
\[
\delta_{\chi_3}=0.
\]
Hence for a false lift
\[
\delta_{\rho_3'}(f)=\nu\smile\bar f
\]
as a class in \(H^2(G,\mathbf F_3)\).

Demuškin cup nondegeneracy gives, for every \(0\ne\nu\), an
\[
a\in H^1(G,\mathbf F_3)
\]
with
\[
\nu\smile a\ne0.
\]
Reduction
\[
H^1(G,\mathbf Z/9(\rho_2))\to H^1(G,\mathbf F_3)
\]
is surjective in the audited coefficient extension, so choose \(f\) with \(\bar f=a\).

Therefore
\[
\delta_{\rho_3'}(f)=\nu\smile a\ne0.
\]

## 2. The separating class is automatically finite at W4

For a pro-3 group,
\[
P_2=G^3[G,G]=\Phi(G),
\]
and hence
\[
P_4\subseteq\Phi(G).
\]
Therefore every mod-3 character factors through
\[
W_4=G/P_4.
\]

In particular there are unique classes
\[
\nu_4,a_4\in H^1(W_4,\mathbf F_3)
\]
whose inflations are \(\nu,a\).

By naturality of cup products,
\[
\inf_{W_4}^G(\nu_4\smile a_4)
=
\nu\smile a.
\]

Define
\[
\alpha_4:=\nu_4\smile a_4\in H^2(W_4,\mathbf F_3).
\]
Then
\[
\inf_{W_4}^G(\alpha_4)
=
\delta_{\rho_3'}(f)
\ne0.
\]

Thus the required finite representative already exists at W4. No deeper quotient is needed to construct the separating output.

## 3. Survival W4 -> W5

Suppose, for contradiction, that
\[
\inf_{W_4}^{W_5}(\alpha_4)=0.
\]
Functoriality of inflation gives
\[
\inf_{W_4}^{G}
=
\inf_{W_5}^{G}\circ\inf_{W_4}^{W_5},
\]
so then
\[
\inf_{W_4}^{G}(\alpha_4)=0,
\]
contradicting the previous section.

Hence
\[
\boxed{
\inf_{W_4}^{W_5}(\alpha_4)\ne0.
}
\]

This proves the exact D2-B survival statement.

## 4. Why the 45-dimensional kernel does not obstruct D2

The hand calculation established
\[
\dim\ker\bigl(H^2(W_4)\to H^2(W_5)\bigr)=45
\]
and identified this transient sector with the dual degree-4 fiber.

That kernel is irrelevant to the separating witness just constructed: \(\alpha_4\) has nonzero image in \(H^2(G,\mathbf F_3)\), whereas every class in the one-step kernel has zero image in \(H^2(G,\mathbf F_3)\).

Therefore the earlier proposed calculation of a literal
\[
\text{delta-family}\cap Q_4^*
\]
was not merely ill-typed; it is unnecessary for the D2 separation theorem.

The correct comparison is output-wise:
\[
\delta_{\rho_3'}(f)
=
\inf_{W_4}^G(\alpha_4),
\qquad
\alpha_4\notin
\ker\bigl(H^2(W_4)\to H^2(W_5)\bigr).
\]

## 5. Logical boundary

This result proves exactly the declared D2-A/D2-B implication:

\[
\boxed{
\text{global separation}
\Longrightarrow
\text{finite W4 representative}
\Longrightarrow
\text{survival through W5}.
}
\]

It does **not** prove that the entire family
\[
\{\delta_{3,\rho_3}\}_{\rho_3\in L(\rho_2)}
\]
is itself a functorially defined map-valued object determined by W4 alone. That is a different, stronger factorization statement.

Accordingly:

- D2-A finite representative: **PASS / CLOSED**.
- D2-B W4 -> W5 survival: **PASS / CLOSED**.
- m=1 separation of every false lift: **PASS / CLOSED**, at the level of the stated existence-of-a-separating-output criterion.
- Exact delta-family/kernel intersection: **NOT REQUIRED / SUPERSEDED** for this criterion.
- Literal delta-family ∩ Q4*: **INVALID / CLOSED** (type mismatch).
- Full W4 reconstruction of the entire delta-family: **separate question / not claimed**.
- Uniform deeper-window bound for this separation criterion: **not needed**.

## 6. Stronger observation

The argument uses only that \(\nu\) and \(\bar f\) are mod-3 classes. Thus the separating variation class factors through the much shallower quotient W2 already; W4 is sufficient because it is the declared D2 window.

So the sharp statement proved here is stronger than “m=1 works after a 45-dimensional kernel computation”: the surviving separating class is born in the ordinary mod-3 cup product and therefore cannot be killed by any deeper inflation once its global image is nonzero.

The degree-4 transgression sector remains important for understanding the full finite H2 target, but it is not load-bearing for separation of false coefficient lifts.


## CRITICAL AUDIT — 2026-09-28 — D2 PARAMETER-SPACE TYPE ERROR

A critical type error was found in the newly written D2-A/D2-B record. The line
\[
0\ne\nu\in Q_4^*\cong H^1(G,\mathbf F_3)
\]
is false: in the fixed rank-four p=3 case, \(\dim Q_4^*=45\), whereas \(\dim H^1(G,\mathbf F_3)=4\). The variation parameter \(\nu\) in
\[
\rho_3'=\rho_3(1+9\nu)
\]
must lie in \(H^1(G,\mathbf F_3)\), not in \(Q_4^*\).

Thus the literal earlier D2 formula with \(\forall 0\ne\nu\in Q_4^*\) is **INVALID / TYPE ERROR**. The corrected load-bearing statement is the same existence-of-separating-output assertion with
\[
\forall\,0\ne\nu\in H^1(G,\mathbf F_3).
\]
For that corrected statement, the D2-A/D2-B proof remains valid: choose \(a\) by Demushkin cup nondegeneracy, lift \(a\) to \(f\), form \(\alpha_4=\nu_4\smile a_4\), and use functoriality to prove survival.

This correction does not affect the identification
\[
\ker(H^2(W_4)\to H^2(W_5))\cong Q_4^*;
\]
that is a separate output/kernel statement. It does mean that \(Q_4^*\) is the transient cohomological obstruction space, not the parameter space of coefficient-lift variations.

Classification:
- literal D2 statement with \(\nu\in Q_4^*\): **INVALID / CLOSED**;
- corrected D2-A finite representative for \(\nu\in H^1(G,\mathbf F_3)\): **PASS / CLOSED**;
- corrected D2-B W4 -> W5 survival: **PASS / CLOSED**;
- identification of \(Q_4^*\) as the one-step kernel: **PASS / CLOSED**;
- delta-family / \(Q_4^*\) direct intersection: **SUPERSEDED / NOT LOAD-BEARING**.
