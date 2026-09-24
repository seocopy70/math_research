# U5 — Intrinsic finite-selector uniqueness from Demuškin structure — 2026-09-24

## Gate
Target:
\[
\forall k\ge2,\quad \mathsf K_k(Q_k,\rho)
\Longleftrightarrow
\rho=\chi_G\bmod 3^k,
\qquad Q_k=G/P_{k+1}(G).
\]

This attack does **not** use a new Fox expansion.

## 1. Intrinsic reduction to G
For a candidate \(\rho_k:G\to U_k\), U1–U2 give
\[
H^1(Q_k,\mathbf Z/3^k(\bar\rho_k))
\cong H^1(G,\mathbf Z/3^k(\rho_k)),
\]
naturally. Hence the finite predicate on \(Q_k\) is equivalent to the same lifting predicate on \(G\).

Moreover, if \(\rho_k\) satisfies the level-k predicate, its reduction \(\rho_{k-1}\) satisfies the level-(k-1) predicate.

## 2. Inductive uniqueness mechanism
Assume level \(k-1\) uniqueness. Then any level-k candidate must reduce to
\[
\rho_{k-1}=\chi_{k-1}.
\]
Any two lifts of \(\chi_{k-1}\) differ uniquely by
\[
\rho_k'=\rho_k(1+3^{k-1}\nu),
\qquad \nu\in H^1(G,\mathbf F_3).
\]

For each lift define the intrinsic coefficient extension
\[
0\to A_{k-1}(\chi_{k-1})
\xrightarrow{\,3\,}
A_k(\rho_k)
\to\mathbf F_3\to0.
\]
Let \(\delta_{\rho_k}:H^1(G,\mathbf F_3)\to
H^2(G,A_{k-1}(\chi_{k-1}))\) be its connecting map.

The level-k Kummer predicate is exactly
\[
\mathsf K_k(\rho_k)\iff \delta_{\rho_k}=0.
\]

## 3. Intrinsic variation lemma
The key coefficient-extension identity is
\[
\boxed{
\delta_{\rho_k'}-\delta_{\rho_k}
=
\iota_{k-1}\circ(\nu\smile -)
}
\]
where
\[
\iota_{k-1}:H^2(G,\mathbf F_3)
\to H^2(G,A_{k-1}(\chi_{k-1}))
\]
is induced by the socle inclusion \(\mathbf F_3\hookrightarrow A_{k-1}(\chi_{k-1})\),
\(1\mapsto3^{k-2}\).

This is a Yoneda/naturality statement about the difference of the two coefficient extensions; it is independent of a presentation, relator, Fox derivative, or chosen \(H^2\)-generator.

## 4. Why the socle map is injective
Because \(G\) is Demuškin and \(\chi\) is its dualizing orientation, finite-module Poincaré duality identifies the relevant \(H^2\)-groups with dual invariant modules. Under this duality, the socle inclusion is dual to the natural quotient
\[
A_{k-1}(\mathbf 1)\twoheadrightarrow\mathbf F_3,
\]
whose invariant map is surjective. Therefore \(\iota_{k-1}\) is injective.

Equivalently, the order-3 socle in the dualizing twist survives nontrivially in top cohomology.

## 5. Uniqueness
If both \(\rho_k\) and \(\rho_k'\) satisfy \(\mathsf K_k\), then
\[
0=\delta_{\rho_k'}-\delta_{\rho_k}
=\iota_{k-1}(\nu\smile-).
\]
Injectivity of \(\iota_{k-1}\) gives
\[
\nu\smile v=0\quad\forall v\in H^1(G,\mathbf F_3).
\]
The Demuškin cup pairing is nondegenerate, hence \(\nu=0\). Thus the level-k candidate is unique.

Base level \(k=1\) is trivial because every admissible orientation is \(1\bmod3\). Existence at every level is supplied by the already-known canonical orientation \(\chi\), whose Kummerian property gives the required lift; U2 then factors it through \(Q_k\).

Therefore the finite predicate has exactly one candidate:
\[
\boxed{
\mathsf K_k(Q_k,\rho)
\Longleftrightarrow
\rho=\chi_G\bmod3^k.
}
\]

## 6. What this proves / what it does not
### PASS / CLOSED (mathematical gate)
Under the standard torsion-free pro-3 Demuškin hypotheses and the intrinsic coefficient-extension variation lemma above, the finite Kummer predicate is uniquely solved by the canonical orientation at every finite level. No new Fox calculation is required.

### Remaining logical boundary
The result is **not** yet a novelty claim. The infinite statement “the canonical orientation is the unique Kummerian orientation” is classical (Labute; modern Kummerian formulations). The present theorem must therefore be positioned as a finite-window factorization/recognition result:
\[
G/P_{k+1}\quad\rightsquigarrow\quad\chi\bmod3^k.
\]
The novelty question is whether the finite factorization through \(Q_k\), together with the explicit semidirect finite-depth proof U1–U2, is absent from the literature or is an immediate corollary of an existing finite-coefficient quotient theorem.

## 7. Required final audit before claiming U5 closed in the paper
1. Write the coefficient-extension variation lemma as a standalone lemma with a complete Yoneda/cochain proof.
2. Verify the socle-to-\(H^2\) injectivity directly from PD^2 duality, including the exact coefficient duals and maps.
3. Compare this induction line-by-line with Labute Proposition 6/Theorem 4 and modern Kummerian quotient results.
4. Only then promote U5 from proof-level PASS to manuscript-ready PASS/CLOSED.

## Status
**U5 uniqueness mechanism: PASS / LOCAL → candidate PASS/CLOSED conditional on the two coefficient-duality lemmas being written out.**

**U5 intrinsic selector as a finite-window theorem: OPEN / DECISIVE until the novelty/factorization audit is completed.**
