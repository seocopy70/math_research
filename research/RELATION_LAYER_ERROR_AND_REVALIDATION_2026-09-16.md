# Relation-layer definition error and full revalidation — 2026-09-16

## 1. What was wrong

The quadratic initial relator is

R = [X1,X2] + [X3,X4] in L2(F3).

The relation layers must be generated recursively:

(R)_3 = [L1,R],
(R)_4 = [L1,(R)_3],
(R)_5 = [L1,(R)_4].

The original degree-4 computation instead used [L2,R] as if it were the complete (R)_4. That is only a proper subspace.

Correct dimensions:

- dim L4 = 60
- dim [L2,R] = 5
- dim (R)_4 = dim [L1,(R)_3] = 15
- therefore the old quotient dimension 55 was wrong; the true quotient has dimension 45.
- the difference is 10 dimensions.

This was a mathematical-definition error, not a numerical precision error.

## 2. How it was discovered

The issue was found by checking the definition of the homogeneous relation ideal rather than trusting the existing numerical dimension. The key structural question was whether degree 4 is [L2,R] or the recursive layer [L1,(R)_3]. The recursive definition forces the latter.

A direct computation then confirmed

[L2,R] subsetneq [L1,(R)_3],

with dimensions 5 and 15 respectively.

This explains why some old computations looked stable: the old space was a genuine subspace of the correct one, not an unrelated random space.

## 3. How it was corrected

The source construction was corrected to

(R)_3=[L1,R],
(R)_4=[L1,(R)_3],
(R)_5=[L1,(R)_4].

A permanent relation-recursion audit was added to CI so that future code must follow the recursive definition.

The corrected degree-4 construction generates 16 natural [L1,(R)_3] candidates and extracts a genuine 15-dimensional basis. This exact basis is then used as the sole input to the degree-5 construction.

## 4. What had to be regarded as invalid

The following old statements are superseded:

- (R)_4 = [L2,R] as the full degree-4 relation space.
- dim (R)_4 = 5.
- Q4 = L4/[L2,R] has dimension 55 as the true relation quotient.
- Any downstream module/intersection statement whose coordinates explicitly depend on that old 55-dimensional quotient.

The old quotient is not a harmless alternative description; it is a quotient by only a 5-dimensional proper subspace of the true 15-dimensional relation layer.

## 5. What survived — A3-4-9

The central W45 result was fully recomputed with the correct relation space.

Let S=[L1,(R)_3]. The corrected computation gives

- dim S = 15
- dim W45 = 45
- rank(W45 + S) = 60
- W45 intersection S = 0
- projected dim = 45
- [L2,R] subset S
- dim [L2,R] = 5

Thus the 45-dimensional W-space survives the true quotient:

W45 ∩ (R)_4 = 0,

and its projection to L4/(R)_4 still has dimension 45.

A separate determinant/reconstruction path independently confirmed this. A genuine 15-column S basis was extracted; 60 ambient rows were selected; the corresponding 60x60 maximal minor had determinant 2 mod 3; and an independent test-vector reconstruction had zero residual.

Therefore A3-4-9 is locked as a corrected result.

## 6. Why the old calculation nevertheless survived at this point

Because

[L2,R] subset (R)_4

and the corrected calculation gives

W45 ∩ (R)_4 = 0,

we automatically have W45 ∩ [L2,R] = 0 as well. The old smaller relation space therefore did not contaminate the W45 independence result.

This is a robustness fact about W45, not a validation of the old relation definition.

## 7. Revalidation of degree 5

After fixing (R)_4, the degree-5 layer was rebuilt from the corrected 15-dimensional basis.

The independent sanity script checks:

- R3 has 4 generators and dimension 4;
- the 16 raw R4 candidates reduce to exactly 15 independent vectors;
- all R4 inputs are genuinely degree 4;
- R5 uses exactly 4 x 15 = 60 brackets [Xi,rj];
- all R5 outputs are genuinely degree 5;
- the ambient free-Lie L5 dimension is independently 204;
- the 60 R5 columns have rank 60.

Thus

(dim (R)_5) = 60

is not merely the old number carried forward.

## 8. Direction-by-direction revalidation of R5

A second, separate check formed for each i the matrix

Mi = [[Xi,r1] ... [Xi,r15]].

The CI result was:

rank ad(X1)|R4 = 15, kernel = 0
rank ad(X2)|R4 = 15, kernel = 0
rank ad(X3)|R4 = 15, kernel = 0
rank ad(X4)|R4 = 15, kernel = 0
combined rank = 60
sum of individual ranks = 60

Therefore every directional map is injective and the four 15-dimensional images have no cross-direction overlap at the dimension level. Hence

[L1,(R)_4] = direct sum_i [Xi,(R)_4]

as vector spaces, and dim (R)_5 = 60.

## 9. Status after revalidation

### Locked

- R = [X1,X2]+[X3,X4]
- dim L4 = 60
- dim (R)_3 = 4
- dim (R)_4 = 15
- dim W45 = 45
- W45 ∩ (R)_4 = 0
- dim projection of W45 to L4/(R)_4 = 45
- [L2,R] subset (R)_4
- dim (R)_5 = 60
- all four ad(Xi)|(R)_4 are injective

### Must be rechecked before reuse

Any downstream result that used the old 55-dimensional quotient, the old 5-dimensional R4 space, or an inherited old R4 coordinate basis.

In particular, A3-4-10/11 must not reuse a previously constructed (R)_5^4 blindly.

## 10. Mandatory entry condition for A3-4-10/11

Before computing

Im(Phi) intersection (R)_5^4,

the canonical corrected R5 coordinate system must be frozen.

Required audit:

1. Build the same canonical 15-vector R4 basis used in the verified R5 checks.
2. Build the canonical 60-vector R5 basis from the four ad(Xi) directions.
3. Verify rank 60 and degree 5.
4. Construct four copies of exactly that same ordered R5 basis.
5. Verify identical internal ordering and coordinate convention in all four blocks.
6. Only then compute Im(Phi) intersection (R)_5^4.

This coordinate-copy check is mandatory because the principal error discovered today was a definition/basis mismatch, not an arithmetic error.

## 11. Methodological rule adopted from this incident

For every future relation layer (R)_n, record separately:

- mathematical definition;
- recursive construction implemented;
- raw candidate count;
- extracted basis dimension;
- ambient degree and ambient Lie dimension;
- coordinate convention;
- any smaller comparison subspace;
- explicit containment/equality verification before identifying two constructions.

A dimension match is not enough to prove equality of spaces.

Research protocol going forward:

**definition -> recursive construction -> basis extraction -> coordinate identity audit -> independent rank check -> downstream computation.**

## 12. Repository records

This incident is cross-linked by the following permanent records:

- research/A3-4-9_FINAL_VERIFICATION_2026-09-16.md
- research/RELATION_R5_SANITY_CHECK_2026-09-16.py
- research/RELATION_R5_DIRECTIONAL_RESULT_2026-09-16.md
- permanent relation-recursion CI audit
- R5 sanity CI workflow
- R5 directional CI workflow

This document is the authoritative incident-and-revalidation addendum for 2026-09-16.
