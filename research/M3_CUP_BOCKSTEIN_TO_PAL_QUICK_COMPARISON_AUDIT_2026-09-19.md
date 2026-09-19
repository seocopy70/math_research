# M3 comparison audit: intrinsic cup/Bockstein carrier vs Pál–Quick canonical class — 2026-09-19

## Objective

Test whether the intrinsic mod-9 carrier
\[
\overline J_3(G)=[(R,p)]
\]
constructed from the cup product and Bockstein admits a natural comparison/factorization to the Benson–Krause–Schwede canonical class used by Pál–Quick for A_3-formality.

External source checked:
Ambrus Pál and Gereon Quick, *A_3-formality for Demushkin groups at odd primes*, arXiv:2601.07551v2. The paper proves that q=3 is not A_3-formal and q≠3 is A_3-formal in the odd-prime setting, by an explicit Hochschild canonical-class computation and Dwyer U_4 lifting. The source states that the q=3 obstruction is represented by the degree-three tensor \(\chi_1^{\otimes3}\) and a non-liftability calculation in \(U_4(\mathbf F_3)\). The project literature audit independently records the same boundary.

## 1. What can already be compared

Our intrinsic carrier contains the power-direction datum detected by the Bockstein:
\[
\beta:H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3).
\]

For the standard Demushkin family at p=3:
- q=3: \(\beta\neq0\), with the distinguished power direction represented by \(x_1^3\);
- q=9 and higher powers of 3: the first Bockstein coefficient vanishes, so \(\beta=0\) at this layer.

Pál–Quick's theorem has the parallel detection pattern:
- q=3: the canonical A_3 class is nonzero;
- q≠3 in their odd-prime Demushkin range: the canonical A_3 class vanishes.

Therefore there is a genuine **detection-level overlap**:
\[
\boxed{
\beta\neq0
\quad\Longleftrightarrow\quad
q=3
\quad\Longrightarrow\quad
\gamma_{A_3}\neq0
}
\]
for the standard p=3 Demushkin family, with the converse detection statement supplied by the Pál–Quick theorem.

This is evidence of a common q=3 power-layer source, not a proof that the two invariants are the same.

## 2. Why this is not yet a factorization theorem

The two objects have different types.

Our carrier is a projective pair
\[
[(R,p)]\in
\mathbf P(\Lambda^2V\oplus V^{(1)}),
\]
equivalently the cohomological pair (cup product, Bockstein).

The Pál–Quick invariant is a canonical Hochschild/cochain class attached to the A_3-formality problem. Its computation uses a higher tensor such as
\[
\chi_1^{\otimes3}
\]
and a Dwyer lifting obstruction to \(U_4(\mathbf F_3)\).

No natural map
\[
[(R,p)]\longrightarrow \gamma_{A_3}
\]
has been constructed in the present project.

In particular, the fact that both detect q=3 does not supply such a map. A map would have to explain how the power-direction data in \(p\) produces the specific Hochschild class, including its target, grading, and gauge/cochain equivalence.

## 3. A useful structural obstruction to the naive identification

The carrier \([(R,p)]\) contains only the quadratic pairing and the first Bockstein/power direction. The Pál–Quick class is defined in a higher cochain/Hochschild complex and is sensitive to a chosen canonical cocycle representative modulo coboundaries before its class is formed.

Thus the identification
\[
\gamma_{A_3}=F([(R,p)])
\]
cannot be justified merely from equality of q=3/q≠3 detection behavior.

At minimum, one must construct the higher cochain-level map from the intrinsic carrier to the Hochschild complex or exhibit a universal property forcing the class.

No such construction is currently present.

## 4. Strongest justified conclusion

There is a **nontrivial detection-level compatibility**:

\[
\boxed{
\text{intrinsic cup+Bockstein carrier}
\Rightarrow
\text{q=3 power-layer detected}
\Rightarrow
\text{Pál–Quick A}_3\text{ obstruction is nonzero}.
}
\]

But the stronger statement
\[
\boxed{
\text{intrinsic carrier}
\Longrightarrow
\text{Pál–Quick canonical class by natural factorization}
}
\]
remains **OPEN**.

This is not a failure of either invariant. It is a boundary between:
- first filtered/cohomological power information, and
- the higher Hochschild/unipotent lifting obstruction built from it.

## 5. Research decision

**PASS / LOCAL:** detection-level compatibility with the independent literature invariant is established for the standard p=3 Demushkin family.

**OPEN:** a natural factorization/map from \([(R,p)]\) to the full Pál–Quick canonical Hochschild class.

**STOP:** no computation of Hochschild classes or U_4 matrices is authorized merely to search for a map. A future attempt must first define the target map at the cochain/Hochschild level and prove its functoriality and gauge compatibility.

This closes the present M3 attempt at the structural boundary without claiming equivalence.
