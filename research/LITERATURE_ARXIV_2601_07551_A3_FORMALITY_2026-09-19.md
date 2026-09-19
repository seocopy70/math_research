# Literature audit — arXiv:2601.07551v2

## Source
Ambrus Pál and Gereon Quick, *A_3-formality for Demushkin groups at odd primes*, arXiv:2601.07551v2. Full source archive was read from the uploaded v2 tarball.

## Main result of the paper
For a pro-p Demushkin group with presentation
\[
G=\langle x_1,\ldots,x_d\mid x_1^q[x_1,x_2]\cdots[x_{d-1},x_d]=1\rangle,
\]
with p odd, the paper proves that the mod-p continuous-cochain dga is A_3-formal for q=0 or q>=5 (and q=3^f, f>=2 when p=3), while q=p=3 is not A_3-formal. The q=3 obstruction is the Benson–Krause–Schwede canonical class in Hochschild cohomology.

## Direct overlap with current orientation-reconstruction research
1. The paper independently confirms that the standard q=3 Demushkin relation contains a genuinely higher-order feature invisible in the quadratic cohomology algebra: q=3 and q=9 have the same exterior-type degree-one cohomology pattern but different A_3-formality behavior.
2. The q-dependent information enters through the higher relation x_1^q, while the quadratic relation is the commutator part. This is strongly consistent with our current information-theoretic obstruction: bounded low-degree associated-graded data cannot recover the full 3-adic orientation uniformly over q=3^s.
3. The paper gives an explicit U_3/U_4 unipotent-lifting mechanism (Dwyer) for converting relation/Massey data into cochain obstructions. This is mathematically adjacent to our use of filtered relation jets and higher unipotent/jet-level probes, but it is not the same invariant.
4. The paper's q=3 non-formality obstruction is detected by a specific degree-three tensor \chi_1^{\ot3} and failure of a lift to U_4(F_3). It does not recover the cyclotomic character \chi:G\to Z_3^\times.
5. For q=3, the paper explicitly uses the presentation relation x_1^3[x_1,x_2]\cdots=1. Thus it supplies an independent literature precedent that the first p-power relation layer can carry information not captured by the quadratic relation.

## What it does NOT establish for our project
- It does not prove that the orientation character is recoverable from the filtered/graded relation carrier.
- It does not distinguish q=3 from q=infinity by an intrinsic filtered-group invariant.
- It does not provide a universal finite bounded-degree reconstruction of full chi.
- Its canonical class lives in the mod-p cochain/Hochschild setting and therefore cannot simply be identified with our exact Z_3 relation-jet carrier.
- Its A_3-formality distinction is a property of the dga C(G,F_p), not a proof that the corresponding obstruction is intrinsic to the Zassenhaus filtration alone.

## Important methodological connection
The strongest reusable idea is the pattern
\[
\text{higher relation data}\to\text{unipotent lifting obstruction}\to\text{cohomological invariant}.
\]
For our work this is evidence for using higher relation/jet information rather than the quadratic associated graded alone. However, importing the canonical class itself would change the object of study and would require a separate intrinsicity proof.

## Current project consequence
Status: RELEVANT LITERATURE / SUPPORTING EVIDENCE, not a new theorem for the current project.

It supports the already-closed conclusion that q-sensitive information first appears beyond the common quadratic relation, and it reinforces the separation between (a) q-sensitive higher-order structure and (b) actual reconstruction of the full orientation character.

No current Gate is reopened by this paper. In particular, it does not reopen the closed universal finite-information bounded-degree route or the closed naive Z_3 restricted-Lie scalar-extension route.

## Specific technical facts worth retaining
- \(H^*(G,F_p)\) is quadratic/Koszul for Demushkin groups in the paper's setting.
- Dwyer's criterion identifies triple-Massey defining systems with homomorphisms to \(U_4(F_p)/Z_4(F_p)\), and vanishing of the selected representative with liftability to \(U_4(F_p)\).
- For q=3, the matrix \(B_+\) has \(B_+^3\neq I\) in \(U_4(F_3)\) but becomes trivial modulo the center, producing the nontrivial canonical-class obstruction.
- The paper also emphasizes that the triple Massey product itself can still contain zero; nontriviality of the particular canonical representative is not the same statement as nonvanishing of the whole Massey product.
