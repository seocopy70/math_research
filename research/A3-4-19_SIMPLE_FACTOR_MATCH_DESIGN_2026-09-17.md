# A3-4-19 Design — explicit matching of the 10- and 25-dimensional simple factors

Date: 2026-09-17

## 1. Starting point

A3-4-17 established, using exactly the A3-4-16 action matrices,

\[
\dim\operatorname{Hom}_H(B/A,K)=1,
\qquad
\max_{0\ne P}\operatorname{rank}P=10,
\]

and hence \(B/A\not\cong_H K\).

A3-4-18 then established by exact GAP MeatAxe computation that both modules are indecomposable of dimension 35 and Loewy length 2, with

\[
\dim\operatorname{soc}(B/A)=\dim\operatorname{rad}(B/A)=25,
\]

\[
\dim\operatorname{soc}(K)=\dim\operatorname{rad}(K)=10,
\]

while both have the same composition-factor dimension multiset \(\{10,25\}\).

## 2. A3-4-19 question

The remaining point is to determine whether the 10-dimensional simple factor occurring in \(B/A\) is actually isomorphic to the 10-dimensional simple factor occurring in \(K\), and likewise for the 25-dimensional factors.

This must not be inferred from dimension alone.

## 3. Exact test

Reuse the same five 35x35 generator matrices by importing
`A3-4-16_STRONG_MODULAR_FINGERPRINT_2026-09-16.py`.

Construct the GF(3) MeatAxe modules exactly as in A3-4-18. For each module compute

\[
\operatorname{MTX.CollectedFactors}(M).
\]

For each dimension \(d\in\{10,25\}\), select the unique collected simple factor of that dimension and test

\[
\operatorname{MTX.Isomorphism}(S_{B/A,d},S_{K,d}).
\]

Because these are irreducible composition factors, MeatAxe's irreducible-module isomorphism test is the appropriate exact certificate.

## 4. Required PASS conditions

A3-4-19 is PASS only if:

1. B/A has exactly one 10-dimensional and one 25-dimensional simple factor;
2. K has exactly one 10-dimensional and one 25-dimensional simple factor;
3. the 10-dimensional factors are isomorphic;
4. the 25-dimensional factors are isomorphic;
5. no dimension-mismatched factor is accidentally compared.

If any isomorphism test returns `fail`, the conclusion must be recorded as a genuine difference in the simple-factor types rather than forcing the extension interpretation.

## 5. Interpretation if PASS

If both factor-isomorphism tests succeed, then the result can be stated precisely as:

\[
\operatorname{soc}(B/A)\cong S_{25},\qquad (B/A)/\operatorname{rad}(B/A)\cong S_{10},
\]

\[
\operatorname{soc}(K)\cong S_{10},\qquad K/\operatorname{rad}(K)\cong S_{25},
\]

for the same pair of simple H-modules \(S_{10},S_{25}\).

Only after this is verified should the difference be described as an extension-orientation difference between the same simple factors.

## 6. Deliberate scope control

A3-4-19 does not yet attempt to compute Ext^1 groups or classify extension classes. Those are subsequent questions. The immediate goal is only to identify the simple factors rigorously.

## 7. Next after PASS

A3-4-20 should then connect the unique rank-10 intertwiner from A3-4-17 to the exact radical/socle maps, verifying that its image is the 10-dimensional socle of K and that its kernel is the 25-dimensional radical of B/A.

This gives a direct bridge between the Hom-space certificate and the Loewy certificate before any Ext computation is attempted.
