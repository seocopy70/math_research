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

## Nonvanishing

For the infinite finitely generated rank-4 Demuškin group under study, the Zassenhaus filtration is strict:
\[
P_{k+1}/P_{k+2}\ne0.
\]

Moreover
\[
P_{k+1}^3\subseteq P_{3(k+1)}\subseteq P_{k+2},
\qquad
[P_{k+1},G]\subseteq P_{k+2}.
\]
Hence
\[
P_{k+1}^3[P_{k+1},G]\subseteq P_{k+2}.
\]

Since $P_{k+1}/P_{k+2}\ne0$, it follows that
\[
\boxed{
P_{k+1}/P_{k+1}^3[P_{k+1},G]\ne0.
}
\]

Thus the dual map required by Proposition 2.10 is non-injective, and therefore
\[
\boxed{
H^1(G,\mathbf F_3)\to
H^1(P_{k+1},\mathbf F_3)^G
\text{ is not surjective.}
}
\]

This is not a computational conjecture: the obstruction comes from the fact that $P_{k+1}$ lies inside the Frattini subgroup while still possessing a nontrivial first relative Frattini layer.

For the strictness assertion, one may use the standard properties of the Zassenhaus filtration for finitely generated pro-p groups; the repository's existing Zassenhaus/Demuškin records also treat the successive graded pieces as nontrivial in the relevant family. A finite GAP check at $k=2,3$ is useful as independent verification, but it is not the logical basis of the result.

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

For $N=P_{k+1}$, the extra restriction-surjectivity premise is not available. Therefore Proposition 2.10 cannot be invoked to obtain the present finite-window theorem.

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

