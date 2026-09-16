# A3-4-20R — Result Record

## Status
**PASS** — GitHub Actions run `35116761852`, job `104864042643`.

## Exact computation
Using the exact 35×35 generator matrices from A3-4-16, the intertwiner equation
\[
Q\,\rho_{B/A}(g)=\rho_K(g)\,Q
\]
was solved over \(\mathbb F_3\).

- intertwiner system: \(6125\times1225\)
- \(\operatorname{rank}E=1224\)
- \(\dim\operatorname{Hom}_H(B/A,K)=1\)
- \(\operatorname{rank}Q=10\)
- \(\dim\ker Q=25\)
- \(\dim\operatorname{im}Q=10\)

## Four direct MeatAxe simplicity tests
All four returned `True`:

1. \(\ker Q\subset B/A\) is simple.
2. \((B/A)/\ker Q\) is simple.
3. \(\operatorname{im}Q\subset K\) is simple.
4. \(K/\operatorname{im}Q\) is simple.

Therefore the following short exact sequences are computationally established:
\[
0\to S_{25}\to B/A\to S_{10}\to0,
\]
\[
0\to S_{10}\to K\to S_{25}\to0.
\]

Combined with A3-4-18 indecomposability, these extensions are non-split.

## Important methodological correction
A3-4-20 was marked **INVALID**, not failed, because it used
\[
\sum_g\operatorname{im}(g-I),\qquad \bigcap_g\ker(g-I)
\]
as radical/socle definitions. The latter is the invariant space \(M^H\), not the general module socle. A3-4-20R avoids this mistake by directly testing the Q-defined submodules and quotients.

## Remaining verification before Ext
A3-4-20R did not directly compare `ker(Q)`/`im(Q)` with the actual `MTX.BasisSocle` spaces. Therefore A3-4-20S was designed as a short independent check of the exact vector-space equality:
\[
\operatorname{Soc}(B/A)=\ker Q,
\qquad
\operatorname{Soc}(K)=\operatorname{im}Q.
\]
Only after A3-4-20S will the project proceed to A3-4-21 (direct extension/Ext-direction analysis).
