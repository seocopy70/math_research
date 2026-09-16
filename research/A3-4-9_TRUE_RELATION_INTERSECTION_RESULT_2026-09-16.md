# A3-4-9 — W45 and the true degree-4 relation space

Date: 2026-09-16

## 1. Purpose

The previous degree-4 quotient used the relation space `[L2,R]`, of dimension 5. The natural degree-4 relation space for the quotient under consideration is instead

\[
S=[L_1,(R)_3],\qquad (R)_3=[L_1,R].
\]

The key question is whether the previously constructed 45-dimensional space \(W_{45}\) survives injectively under

\[
\pi:L_4/[L_2,R]\longrightarrow L_4/[L_1,(R)_3].
\]

Because `[L2,R] \subset S`, the decisive calculation is

\[
\dim(W_{45}\cap S).
\]

## 2. Coordinate convention

The calculation is performed directly in the 256-dimensional degree-4 associative word space on \(X_1,X_2,X_3,X_4\). The authoritative Phase 2-1 construction already produces the 45 independent columns of \(W_{45}\) in these ambient coordinates. No comparison between quotient coordinate systems is used.

## 3. Exact computation

The verification script is:

`research/phase2_22_A3_4_9_W45_true_relation_intersection_2026-09-16.py`

It reconstructs

\[
(R)_3=[L_1,R],\qquad S=[L_1,(R)_3],
\]

in the same ambient coordinates as \(W_{45}\), and computes ranks over \(\mathbb F_3\).

The certificate is:

```text
dim (R)_3 = 4
dim [L1,(R)_3] = 15
dim W45 = 45
rank([W45 | [L1,(R)_3]]) = 60
dim(W45 intersection [L1,(R)_3]) = 0
dim pi(W45) = 45
dim [L2,R] = 5
dim ker(L4/[L2,R] -> L4/[L1,(R)_3]) = 10
[L2,R] subset [L1,(R)_3] = True
ALL CHECKS PASSED
```

## 4. Consequence

Using

\[
\dim(W_{45}\cap S)=\dim W_{45}+\dim S-\dim(W_{45}+S),
\]

we obtain

\[
0=45+15-60.
\]

Therefore

\[
\boxed{W_{45}\cap[L_1,(R)_3]=0}.
\]

Hence the induced projection is injective on \(W_{45}\):

\[
\boxed{\dim\pi(W_{45})=45}.
\]

Also,

\[
\dim S-\dim[L_2,R]=15-5=10,
\]

so the quotient map has a 10-dimensional kernel on the full degree-4 quotient, while it has zero kernel when restricted to \(W_{45}\).

## 5. Research status

This settles the specific coordinate/quotient-survival gate for \(W_{45}\): the 45-dimensional space does **not** collapse when passing from the old relation quotient by `[L2,R]` to the true quotient by `[L1,(R)_3]`.

This result alone does not establish the remaining Track A conclusions. It establishes only the injective survival of \(W_{45}\) under the corrected degree-4 quotient map.

## 6. Reproducibility

CI workflow:

`.github/workflows/phase2-23-A3-4-9-true-relation.yml`

The workflow reruns the exact certificate from a clean Python 3.11 environment with NumPy.
