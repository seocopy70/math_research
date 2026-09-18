# 03. Mathematical and Computational Conventions

This document fixes the conventions needed for independent reproduction and defines the minimum operating protocol for AI-assisted mathematical research in this repository.

## 1. Base field

All finite-field calculations in the degree-4 representation-theoretic track are over

\[
\mathbb F_3=\{0,1,2\},
\]

with arithmetic modulo 3.

## 2. Group commutator

The group convention is

\[
[a,b]=a^{-1}b^{-1}ab.
\]

This convention controls all Hall–Petrescu signs.

## 3. Free Lie algebra

Let

\[
L=\mathbb L_{\mathbb F_3}(X_1,X_2,X_3,X_4).
\]

The Lie bracket is implemented inside the free associative algebra as

\[
[A,B]=AB-BA.
\]

The code represents a word by a tuple of letters, for example
\[
X_1X_3X_4X_2\leftrightarrow(1,3,4,2).
\]

## 4. Quadratic relation

The initial quadratic relation is

\[
R=[X_1,X_2]+[X_3,X_4].
\]

In the implementation this is constructed as the sum of the first and sixth degree-2 brackets in lexicographic pair order.

## 5. Degree-4 target

The target is exactly

\[
\boxed{T=[[[X_3,X_4],X_1],X_1].}
\]

Its multidegree is \((2,0,1,1)\).

## 6. Symplectic form

Vectors are column vectors in \(\mathbb F_3^4\). We use

\[
J=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}.
\]

The symplectic pairing is \(\omega(x,y)=x^TJy\). All matrix products are modulo 3.

This J is the authoritative convention for the current repository.

## 7. Symplectic transvection

The implementation uses
\[
\boxed{t_v=I+v(Jv)^T.}
\]

Acting on a column vector x,
\[
t_vx=x+v(Jv)^Tx.
\]

Replacing v by -v gives the same matrix over \(\mathbb F_3\), so the 40 nonzero projective directions produce 40 distinct transvections. Every generated transvection is checked directly by \(t_v^TJt_v=J\).

## 8. Five generators used in Phase 2-1

The generating vectors are

\[
(1,0,0,0),\ (0,1,0,0),\ (0,0,1,0),\ (0,0,0,1),\ (1,0,1,0).
\]

Their associated transvections are constructed by the formula above. The code verifies that they are symplectic and that the subgroup they generate has order
\[
51840=|Sp_4(\mathbb F_3)|.
\]

## 9. Action on Lie words

If g is a 4x4 matrix, its j-th column gives the image of \(X_j\). The induced degree-4 action is obtained by substituting these linear combinations into the associative-word representation and reducing modulo 3.

This is the action used to generate the orbit of T.

## 10. Quotient coordinates

Degree-4 computations use
\[
Q_4=L_4/(R)_4,\qquad (R)_4=[R,L_2].
\]

The implementation embeds Lie elements into the 256-dimensional degree-4 associative word space, selects independent columns for \((R)_4\), and then represents quotient orbit modules relative to a complementary basis.

## 10A. q=3 / q=∞ baseline-relative degree-3 source

For the q=3 versus q=∞ comparison track, the reference baseline is fixed to the pure-commutator q=∞ presentation

\[
G_\infty=\langle x_1,x_2,x_3,x_4\mid [x_1,x_2][x_3,x_4]=1\rangle,
\]

while the q=3 case is

\[
G_3=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle.
\]

The comparison object is defined **relatively to this fixed baseline**, not as an absolute degree-3 term. Let \(s_q\) denote the relation-derived element used in the q=3/q=∞ comparison, and define

\[
\boxed{\Delta_3(q):=\operatorname{in}_3(s_q)-\operatorname{in}_3(s_\infty).}
\]

The corresponding bracketed q-sensitive object is

\[
\boxed{d_q:=[\Delta_3(q),X_2].}
\]

The independent truncated Magnus verification recorded that

\[
\Delta_3(3)=X_1^{[3]},
\qquad
\Delta_3(\infty)=0,
\]

so in particular

\[
d_3=[X_1^{[3]},X_2],
\qquad
\boxed{d_\infty=[0,X_2]=0}.
\]

Thus \(d_\infty=0\) is not an independently selected target value: it follows tautologically from the baseline-relative definition once the baseline is fixed. The convention that q=∞ is the baseline is itself a mathematical/conventional choice made at the presentation level; it must not be confused with a posteriori selection based on an observed orbit or invariant.

This definition also makes explicit that the common Lie/conjugation contribution in \(\operatorname{in}_3(s_3)\) is not being discarded by the downstream construction. It cancels in the baseline-relative difference \(\Delta_3(3)\) by definition. Consequently the downstream objects \(d_q\), \(W_d\), \(N\), \(\tau\), and the associated \(J\)-comparison are understood to operate on this q-sensitive difference source, not on \(\operatorname{in}_3(s_3)\) as an absolute object.

**Scope note.** This section fixes the definition of the q-sensitive comparison object. It does not by itself assert that \(d_\infty\) is a canonical whole degree-3 q=∞ analogue of \(d_3\), nor does it establish any q-detection result. Those claims require the separate Q3/Q∞ definition and invariant audit.

## 11. Coordinate consistency protocol

The authoritative Python representation uses **column action** \(v\mapsto Av\). GAP `GModuleByMats` uses **row vectors with right action**. Therefore Python action matrices, endomorphisms, and subspace bases must all be transposed when converted to GAP. This applies equally to generators and to objects such as \(N\), kernels, images, and socle bases.

Equality of subspaces must be checked in one common ambient coordinate system by span/rank, never from dimensions alone.

A structural contradiction caused by a coordinate conversion mismatch is classified as **INVALID TEST**, not as a mathematical failure.

Every new computational record must state:

1. basis order and dimension;
2. action direction;
3. matrix convention;
4. Python→GAP transpose rule, if GAP is used;
5. which coordinate system each subspace/endormorphism lives in;
6. sanity invariants checked and their outcomes.

## 11A. Complete H-orbit closure invariant

Whenever an experiment claims an (H)-submodule or (H)-span generated by vectors, the closure procedure must apply **every generator to every accumulated basis vector** and continue until no new independent vector appears.

Applying generators only to the most recently discovered vector is not an H-span computation and can produce a false dimension. Any result produced by an incomplete closure routine is **INVALID TEST** until recomputed with complete closure.

For a claimed orbit/submodule equality, record the closure dimension and, when relevant, verify it against an independent construction or known ambient dimension.

## 12. Finite-field rank protocol

All rank, kernel, image, independence, and span calculations involving \(\mathbb F_3\)-data must use exact finite-field arithmetic.

The repository's authoritative Phase 2-1 routine `rank3()` is the verified reference rank function and should be reused rather than reimplemented in new experiments whenever possible.

The following real/numerical linear-algebra calls are forbidden for the finite-field track:

- `numpy.linalg.matrix_rank`
- `numpy.linalg.det`

They compute over the real/numerical field and can produce values that are mathematically irrelevant to \(\mathbb F_3\) rank questions. Future `np.linalg` usage is surfaced by the repository-wide audit for explicit review.

The CI audit `FINITE_FIELD_RANK_AUDIT_2026-09-17.py` scans all tracked research Python files using the Python AST and fails on forbidden `matrix_rank` or `det` calls. It does not treat comments or string literals as code calls.

## 13. Sanity invariants

Before accepting a finite-field result, check relevant necessary identities such as:

- \(N^2=0\Rightarrow\operatorname{im}N\subseteq\ker N\);
- rank-nullity;
- nonzero finite-dimensional modules have nonzero socle;
- any nonzero submodule meets the socle nontrivially;
- \(\dim U+\dim V>\dim M\Rightarrow U\cap V\neq0\);
- intertwiner identities such as \(Q\rho_M(g)=\rho_N(g)Q\).

If a necessary condition fails, stop and classify the calculation as **INVALID TEST** until coordinate and field conventions have been reconciled.

## 14. Result classification

Every experiment is assigned one operational status:

- **SETUP FAILURE** — the environment/toolchain prevented the intended mathematical computation from running.
- **IMPLEMENTATION FAILURE** — the intended computation ran but the implementation is known to be wrong or inconsistent with the specification.
- **INVALID TEST** — a computation produced output, but its mathematical interpretation is invalid because of a convention, field, coordinate, stale-input, or design error.
- **MATHEMATICAL FAILURE** — the implementation and prerequisites are validated, but the stated mathematical proposition is false or the decision criterion fails.
- **PASS** — the stated decision criterion is satisfied and the computation has been executed and checked.

These are **cause/status labels**, not a forced linear progression. In particular, a setup failure is not evidence against the mathematics, and an invalid test is not a negative mathematical result.

## 15. Three-layer verification

For important claims, use three layers whenever feasible:

1. **Local mathematical sanity** — identities, dimensions, field arithmetic, and necessary module-theoretic constraints.
2. **Independent computational verification** — a second implementation, GAP/MeatAxe, exact certificate, or independently constructed check.
3. **Reproducible CI execution** — committed script/workflow and an actual GitHub Actions run/job.

A strong claim should not be promoted solely because one program printed an expected number.

## 16. Research operating protocol

The standard loop is

\[
\boxed{\text{수학적 주장}\rightarrow\text{계산 설계}\rightarrow\text{독립 검증}\rightarrow\text{CI 재현}\rightarrow\text{기록}.}
\]

For each experiment record goal/input/method/decision criterion/actual result/interpretation/open issue, together with exact commit and Actions run/job identifiers when available.

Do not pre-confirm a result before execution. If a result conflicts with basic theory, inspect implementation, coordinate conversion, field consistency, and stale inputs before calling it a mathematical discovery.

## 17. Important historical corrections

An earlier exploratory calculation used an incorrect symplectic pairing matrix. That calculation was not retained as a valid result.

An earlier B1-1 diagnostic used `numpy.linalg.matrix_rank` on \(\mathbb F_3\)-data and printed a spurious real-field rank. That number is not a valid mathematical result and is not retained. The corrected calculation reuses `rank3()` and independently checks the GAP \(\mathbb F_3\) rank.

## 18. Reproduction principle

A reader should be able to reproduce each claim from:

1. the mathematical convention in this document;
2. the cited script;
3. the recorded Git commit;
4. the GitHub Actions result where available;
5. an independent implementation or certificate for strong identification claims.

No numerical output is treated as a proof without an explicit mathematical interpretation.
