# R5 directional injectivity verification — 2026-09-16

## Purpose

Before locking the degree-5 relation-space dimension
\[
\dim (R)_5=60,
\]
we separately test the four directional maps
\[
\operatorname{ad}(X_i):(R)_4\to L_5,
\qquad i=1,2,3,4.
\]

The motivation is that the previous sanity check established that the 60 candidates
\[
[X_i,r_j],\qquad i=1,\dots,4,\quad j=1,\dots,15
\]
have combined rank 60, but did not separately test whether any individual direction has a kernel.

## Exact verification performed

The check reconstructs the quadratic relator independently as
\[
R=[X_1,X_2]+[X_3,X_4],
\]
then recursively constructs
\[
(R)_3=[L_1,R],
\qquad
(R)_4=[L_1,(R)_3].
\]

The degree-4 relation space is extracted as a 15-dimensional basis. For each generator \(X_i\), the matrix
\[
M_i=\bigl[[X_i,r_1]\;\cdots\;[X_i,r_{15}]\bigr]
\]
is formed over \(\mathbb F_3\), and its rank and kernel dimension are computed independently.

Finally, the four matrices are concatenated and the combined rank is computed.

## CI result

Repository: `seocopy70/math_research`

Commit: `40c80b6f17964e09da92045f6af22ef0bc6c931a`

Workflow: `R5 directional injectivity check`

Run: `35066766293`

Job: `104698684213`

Conclusion: **SUCCESS**

## Numerical output

```text
rank ad(X1)|_(R4) = 15
kernel dimension = 0
rank ad(X2)|_(R4) = 15
kernel dimension = 0
rank ad(X3)|_(R4) = 15
kernel dimension = 0
rank ad(X4)|_(R4) = 15
kernel dimension = 0
combined rank = 60
sum of individual ranks = 60
number of directional columns = 60
ALL DIRECTIONAL R5 INJECTIVITY / COMBINED-RANK CHECKS PASSED
```

## Interpretation

All four directional maps are individually injective:
\[
\boxed{
\operatorname{rank}\bigl(\operatorname{ad}(X_i)|_{(R)_4}\bigr)=15,
\quad
\ker\bigl(\operatorname{ad}(X_i)|_{(R)_4}\bigr)=0
\quad(i=1,2,3,4).
}
\]

Moreover,
\[
\boxed{
\operatorname{rank}[L_1,(R)_4]=60.
}
\]

Since the four directional images each have dimension 15 and their combined span has dimension 60, there is no dimension loss within any individual direction and no cross-direction overlap at the level of the four 15-dimensional images.

This independently strengthens the earlier R5 sanity result. The earlier check established that the 60 candidates are genuine degree-5 vectors and that the ambient free-Lie degree-5 space has dimension 204. The present check additionally establishes directional injectivity and the exact 60-dimensional combined span.

## Status

The value
\[
\boxed{\dim (R)_5=60}
\]
is now supported by:

1. correct recursive construction of relation layers;
2. explicit 15-dimensional \((R)_4\) input basis;
3. degree checks preventing degree-4/L4 input contamination;
4. independent ambient \(\dim L_5=204\) check;
5. full 60-column rank computation;
6. four separate directional rank/kernel checks;
7. combined rank = 60;
8. CI enforcement of the directional checks.

This result is recorded as a verification checkpoint before proceeding to A3-4-10/11.
