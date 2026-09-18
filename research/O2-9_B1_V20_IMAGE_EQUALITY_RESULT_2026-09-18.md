# O2-9 B1 V20 image equality — RESULT (2026-09-18)

## 1. Scope

This record closes the specific question:

\[
\text{Is the image }\operatorname{Im}D_{(1,b)}\text{ independent of }b\in\{0,1,2\}
\text{ within the verified B1 family?}
\]

It does **not** test or decide filtration-intrinsicity of the full O2 obstruction route.

Authoritative execution:
- Commit: \`721c6866fbf6ff4282f9e187c37951b1fea7eb71\`
- Actions run: \`35359895308\`
- Job: \`105648285525\`
- Diagnostic follow-up commit: \`06ff62d7ded3c5155e0962882878644bc70e1f87\`

## 2. B1 family and image ranks

The pointwise B1-admissible transports are

\[
(1,0),(1,1),(1,2).
\]

For

\[
A_b:=\operatorname{Im}D_{(1,b)}
\]

the computation gives

\[
\dim A_0=\dim A_1=\dim A_2=10.
\]

All pairwise joins have rank 20:

\[
\dim(A_i+A_j)=20\qquad(i\neq j).
\]

Therefore

\[
\dim(A_i\cap A_j)
=10+10-20
=0.
\]

Thus every pair of B1 images has trivial intersection. In particular, there is no common nonzero vector, and certainly no common 10-dimensional image.

The three-way span has rank

\[
\dim(A_0+A_1+A_2)=20.
\]

Hence the three distinct 10-dimensional images are all contained in their jointly generated 20-dimensional span, while no pair shares a nonzero vector.

## 3. Gate decision

\[
\boxed{\text{V20 image transport-independence within B1 = FAIL}}
\]

This rejects the specific proposition that the absolute image itself is a transport-independent 10-dimensional subspace within the B1 family.

It does **not** imply:
- filtration-intrinsicity as a whole fails;
- the previously verified fixed-\tau \(O\cong U\) module identification is invalid;
- the B1-generated 20-dimensional span is filtration-intrinsic;
- q=3 versus q=\infty is decided by this result;
- the orientation character \(\chi\) is or is not recoverable.

## 4. Structural observation retained

Define only for this B1 family

\[
W_{B1}:=A_0+A_1+A_2.
\]

Then

\[
\boxed{\dim W_{B1}=20}
\]

is a verified computational observation.

The important structure is therefore not a common 10-dimensional image, but three distinct 10-dimensional subspaces with pairwise-zero intersections whose total span is 20-dimensional.

The 20-dimensional span must **not** be identified with a canonical/filtration-intrinsic \(V_{20}\) without a separate construction.

## 5. Consequence for the research route

The concrete-subspace interpretation of \(V_{20}\) is **not promoted**.

The next question, if this route is pursued, is narrower:

1. keep the dimension/intersection facts above as fixed evidence;
2. determine whether the B1-generated 20-dimensional span has any transport-free definition;
3. do not introduce a new canonical \(V_{20}\) candidate before such a definition is available.

The q=3/q=\infty and \(\chi\)-recovery claims remain outside the scope of this result.
