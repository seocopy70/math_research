# HARD ATTACK — Proposition 2.10 restriction-surjectivity for N=P_{k+1} — 2026-09-25

## Question

The proposed follow-up problem asked whether the quotient-inheritance Proposition 2.10 of Quadrelli (2024), applied with
\[
N=P_{k+1}(G),
\]
has its extra hypothesis
\[
\operatorname{res}_{G,N}^1:
H^1(G,\mathbf F_3)\to H^1(N,\mathbf F_3)^G
\]
automatically surjective.

If yes, the finite-window theorem might risk being an immediate corollary of quotient inheritance. The question is therefore a legitimate novelty attack.

## Literature statement checked

Quadrelli, *Chasing Maximal Pro-p Galois Groups via 1-Cyclotomicity* (Mediterranean Journal of Mathematics 21 (2024), Art. 56), Proposition 2.10 states:

If $(G,\theta)$ is a finitely generated Kummerian oriented pro-p group with torsion-free orientation, $N\triangleleft G$, $N\subseteq\ker\theta$, and
\[
H^1(G,\mathbf F_p)\to H^1(N,\mathbf F_p)^G
\]
is surjective, then $(G/N,\theta_{/N})$ is Kummerian.

The proof explicitly uses the dual restriction condition. In particular, the dual map
\[
N/N^p[G,N]\longrightarrow G/\Phi(G)
\]
must be injective.

Source: Quadrelli 2024, Proposition 2.10, especially the statement and proof at lines 288--342 of the Springer article.

## Critical observation

For the Demuškin finite-window choice
\[
N=P_{k+1}(G),
\]
one has
\[
P_{k+1}(G)\subseteq\Phi(G)
\]
for every $k\ge2$.

Therefore the natural inclusion-induced map
\[
N/N^p[G,N]\longrightarrow G/\Phi(G)
\]
is the zero map.

Consequently, if
\[
N/N^p[G,N]\ne0,
\]
the dual restriction map cannot be surjective.

So the question reduces to whether the coinvariant/Frattini quotient of $P_{k+1}$ is nonzero.

## Decisive finite-window counterexample: k=2

To refute automaticity, it is enough to take $k=2$, so $N=P_3$.

For a rank-$d$ Demuškin pro-p group, Mináč–Rogelstad–Nguyễn Duy Tân compute the dimensions
\[
c_n(G)=\dim_{\mathbf F_p}P_n/P_{n+1}.
\]
Their Example 5.3 gives, for $p=3$,
\[
c_3(G)=\frac{d^3-d}{3}.
\]
For the present rank-$4$ group,
\[
\boxed{\dim_{\mathbf F_3}P_3/P_4=20.}
\]
Thus $P_3/P_4\neq0$.

On the other hand,
\[
P_3^3\subseteq P_9\subseteq P_4,
\qquad
[P_3,G]\subseteq P_4,
\]
so
\[
P_3^3[P_3,G]\subseteq P_4.
\]
Therefore
\[
\boxed{
P_3/P_3^3[P_3,G]\neq0.
}
\]

Since $P_3\subseteq\Phi(G)$, the inclusion-induced map
\[
P_3/P_3^3[P_3,G]\to G/\Phi(G)
\]
is zero. It is therefore not injective. By the duality used explicitly in the proof of Proposition 2.10, the restriction map
\[
\boxed{
H^1(G,\mathbf F_3)\to H^1(P_3,\mathbf F_3)^G
}
\]
is not surjective.

This single $k=2$ counterexample already proves that the Proposition 2.10 restriction-surjectivity hypothesis is **not automatic** for $N=P_{k+1}$.

A stronger all-$k$ statement is plausible and can be checked from the explicit Zassenhaus dimension formula, but it is not needed to close the automaticity question and is therefore not promoted here without a separate proof.

## Consequence for the proposed problem 2

The proposed statement

> “Is the Proposition 2.10 restriction-surjectivity hypothesis automatic for $N=P_{k+1}$?”

is answered negatively for the present Demuškin family.

Classification:

\[
\boxed{\textbf{FAIL / CLOSED}}
\]

for automatic surjectivity.

This is stronger and cleaner than leaving the issue OPEN.

## Consequence for novelty

This result does **not** prove publication novelty by itself. It does, however, close the most obvious route by which Proposition 2.10 could trivialize the finite-window theorem.

The logical distinction is now sharp:

- Proposition 2.10: known Kummerian $(G,\theta)$ + $N\subseteq\ker\theta$ + restriction-surjectivity $\Rightarrow$ quotient Kummerian.
- Present theorem: arbitrary finite candidate $\rho$ + direct finite-depth factorization $\Rightarrow$ intrinsic predicate on $Q_k$, followed by intrinsic uniqueness.

Already at $k=2$ with $N=P_3$, the extra restriction-surjectivity premise is false. Therefore Proposition 2.10 cannot be invoked to obtain the present finite-window theorem.

## Important non-implication

The failure of restriction-surjectivity must not be confused with failure of the finite-window theorem.

The current U1-U2 argument proves a different and stronger-looking factorization statement for the twisted coefficient module attached to an arbitrary candidate $\rho$:
\[
H^1(G,\mathbf Z/3^k(\rho))
\cong
H^1(Q_k,\mathbf Z/3^k(\rho)).
\]

The failed restriction map concerns ordinary trivial-coefficient $H^1(P_{k+1},\mathbf F_3)^G$ and is precisely the extra hypothesis used by Proposition 2.10. These are different maps.

## Status update

- Proposed Problem 2 automatic restriction-surjectivity: **FAIL / CLOSED**.
- Proposition 2.10 as direct shortcut to the finite-window theorem: **CLOSED as an available route**.
- U1-U5 finite-window theorem: remains **PASS / CLOSED**.
- Exact publication novelty: remains **OPEN / STRONG CANDIDATE / CONDITIONAL**, because absence of this shortcut is not an absolute priority proof.
- No closed mathematical branch is revived.

## Required follow-up

1. Add this as an explicit negative result to the literature audit.
2. Update N2 wording: the quotient-inheritance theorem is not merely “not directly applicable”; for $N=P_{k+1}$ its stated restriction-surjectivity hypothesis actually fails in the present family.
3. Keep the theorem's novelty statement narrow.
4. Optionally run GAP at $k=2,3$ as an independent numerical verification of the nonzero relative Frattini layer.



## 2026-09-25 — FINAL PRIMARY-SOURCE CORRECTION

Quadrelli 2024 Proposition 2.10 was checked directly. Its hypotheses include N contained in ker(theta) and surjectivity of H^1(G,F_p) -> H^1(N,F_p)^G. The proof explicitly uses the dual inclusion N/N^p[G,N] -> G/Phi(G), and later uses N contained in ker(theta) again.

The Zassenhaus dimension source was also checked directly: Minac–Rogelstad–Nguyen Duy Tan, Example 5.3 gives, for p=3 Demushkin rank d, c_3=(d^3-d)/3. Thus d=4 gives c_3=20 and P_3/P_4 is nonzero. Since P_3^3[P_3,G] is contained in P_4 and P_3 is contained in Phi(G), the dual inclusion is zero with nonzero source. Therefore H^1(G,F_3) -> H^1(P_3,F_3)^G is not surjective.

This closes automatic restriction-surjectivity for N=P_{k+1}: FAIL / CLOSED. However, it does not by itself refute Proposition 2.10 as an admissible application with N=P_3, because P_3 need not be contained in ker(chi). The previous wording that the entire Prop. 2.10 shortcut was therefore closed is superseded.

A stronger admissible kernel-contained test was examined: N=P_3 intersect ker(chi). This subgroup is normal and contained in ker(chi), but the claim that its restriction map is nonsurjective requires an additional filtration-level proof that (P_3 intersect ker(chi))/(P_3 intersect ker(chi))^3[.,G] is nonzero. That proof is NOT recorded as closed here. In particular, the tentative use of x_2^3 modulo 27 does not by itself establish the required quotient statement. This branch remains OPEN until independently proved.

Final classification: Prop. 2.10 statement/proof PASS / CLOSED; duality PASS / CLOSED; c_3=20 PASS / CLOSED; P_3 restriction nonsurjectivity PASS / CLOSED; automatic restriction-surjectivity for N=P_{k+1} FAIL / CLOSED; admissible kernel-contained counterexample OPEN; Prop. 2.10 as a complete shortcut to the finite-window theorem OPEN / CONDITIONAL; publication novelty OPEN / CONDITIONAL.
