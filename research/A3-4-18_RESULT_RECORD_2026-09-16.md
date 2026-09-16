# A3-4-18 Result Record — B/A vs K: exact socle/radical/Loewy structure

Date: 2026-09-16
Workflow run: 35112986819
Job: 104851178585
Commit tested: 1f76679c4351b30b1784c2d72ccbe65939492f14

## 1. Verification environment

The calculation re-imported `A3-4-16_STRONG_MODULAR_FINGERPRINT_2026-09-16.py`, so the five 35x35 generator matrices for B/A and K were the same action matrices used in A3-4-16/A3-4-17.

The matrices were transposed only to convert the existing left-column convention to GAP MeatAxe's right-row convention, and all entries were explicitly coerced into GF(3).

The workflow installed Python `numpy`, `sympy`, and GAP 4.12.1.

The run passed exactly after the GF(3) coercion fix.

## 2. Exact MeatAxe results

### B/A

- dimension: 35
- indecomposable: TRUE
- socle dimension: 25
- radical dimension: 25
- top dimension: 10
- radical filtration dimensions:

  \[
  [35,25,0]
  \]

- Loewy length from radical filtration: 2
- cumulative socle filtration dimensions:

  \[
  [0,25,35]
  \]

- Loewy length from socle filtration: 2
- composition-factor dimensions: [25,10]
- collected composition-factor dimensions/multiplicities: [ [10,1], [25,1] ]

### K

- dimension: 35
- indecomposable: TRUE
- socle dimension: 10
- radical dimension: 10
- top dimension: 25
- radical filtration dimensions:

  \[
  [35,10,0]
  \]

- Loewy length from radical filtration: 2
- cumulative socle filtration dimensions:

  \[
  [0,10,35]
  \]

- Loewy length from socle filtration: 2
- composition-factor dimensions: [10,25]
- collected composition-factor dimensions/multiplicities: [ [10,1], [25,1] ]

## 3. Direct comparison

\[
\boxed{\dim \operatorname{soc}(B/A)=25}
\]

while

\[
\boxed{\dim \operatorname{soc}(K)=10}.
\]

Likewise,

\[
\boxed{\dim \operatorname{rad}(B/A)=25}
\]

while

\[
\boxed{\dim \operatorname{rad}(K)=10}.
\]

Thus the Loewy structures differ immediately at the first layer.

Both modules are indecomposable and both have Loewy length 2, but the direction of the two composition factors is reversed:

\[
B/A:
\quad 0\subset \operatorname{rad}(B/A)=\operatorname{soc}(B/A),
\quad \dim=25,
\quad (B/A)/\operatorname{rad}(B/A)\text{ has dim }10;
\]

\[
K:
\quad 0\subset \operatorname{rad}(K)=\operatorname{soc}(K),
\quad \dim=10,
\quad K/\operatorname{rad}(K)\text{ has dim }25.
\]

The composition-factor multiset is the same (one 10-dimensional simple factor and one 25-dimensional simple factor), but their extension orientation is reversed.

Therefore the earlier A3-4-17 non-isomorphism is now explained structurally, not merely detected by Hom-space rank.

## 4. Important consequence for the unique rank-10 intertwiner

A3-4-17 found

\[
\dim \operatorname{Hom}_H(B/A,K)=1
\]

and the unique nonzero intertwiner has rank 10.

A3-4-18 now shows why rank 10 is natural: the 10-dimensional factor occurs as the **top of B/A** but as the **socle of K**. Hence a nonzero H-map from B/A to K can naturally collapse the 25-dimensional radical/socle of B/A and land in the 10-dimensional socle of K.

This is a structural interpretation of the A3-4-17 rank-10 result.

## 5. What A3-4-18 does and does not prove

It proves exactly, by an independent finite-field MeatAxe computation on the same action matrices:

1. B/A and K are both indecomposable 35-dimensional H-modules.
2. Both have Loewy length 2.
3. Their composition-factor multisets agree: one 10-dimensional and one 25-dimensional simple factor.
4. Their radical/socle dimensions are reversed (25 vs 10).
5. Therefore B/A and K are not isomorphic, with a submodule/extension-level certificate.

It does not by itself identify the actual simple modules by an abstract label beyond their dimensions. The next useful refinement is to match the 10- and 25-dimensional simple factors explicitly and then identify the corresponding extension classes.

## 6. Relation to previous results

Previously verified:

\[
\dim(B/A)=\dim(K)=35,
\]

all tested conjugacy-class fingerprints agree,

\[
\dim\operatorname{Hom}_H(B/A,K)=1,
\]

and the maximum intertwiner rank is 10.

A3-4-18 adds:

\[
\boxed{
\operatorname{soc}(B/A)=\operatorname{rad}(B/A)\text{ has dimension }25,
}
\]

\[
\boxed{
\operatorname{soc}(K)=\operatorname{rad}(K)\text{ has dimension }10.
}
\]

Thus the first genuine module-structure invariant beyond class-level fingerprints already separates the modules.

## 7. Next step

Do not immediately move to a more complicated invariant. First identify the two simple factors explicitly and verify:

- the 10-dimensional simple factor of B/A is isomorphic to the 10-dimensional simple factor of K;
- the 25-dimensional simple factor of B/A is isomorphic to the 25-dimensional simple factor of K;
- the two modules therefore represent two different extension classes between the same pair of simple factors, with opposite Loewy orientation.

Then compute the unique rank-10 intertwiner from A3-4-17 against the exact radical/socle filtrations and record:

\[
P(\operatorname{rad}(B/A)),\quad
P(B/A),\quad
P^{-1}(\operatorname{soc}(K))
\]

where defined, to connect the Hom-space certificate directly to the Loewy certificate.

## 8. CI note

The first A3-4-18 run failed only because `sympy` was not installed and subsequently exposed a GAP GF(3) matrix-coercion issue. Both were corrected. The final run 35112986819 completed successfully, with the exact MeatAxe output above. The final driver also treats GAP `Error,` output as a failure condition.
