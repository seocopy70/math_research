# Gate 0-B Q3-0 — q=∞ and `X1^[3]`

## Purpose

Before constructing the q=∞ analogue of
\[
d=[X_1^{[3]},X_2],
\]
verify first that the restricted-power class `X1^[3]` is a nonzero element modulo the q=∞ relation ideal in degree 3.

This is logically prior to the Q3 orbit/structure construction.

## Fixed criterion

In the free restricted Lie algebra over `F_3`, the degree-3 restricted power of `X1` is represented in the tensor-algebra realization by the associative word `X1 X1 X1`.

For q=∞ the quadratic relation is
\[
R_\infty=[X_1,X_2]+[X_3,X_4].
\]
The degree-3 ordinary bracket part of the relation ideal is
\[
(R_\infty)_3=[L_1,R_\infty].
\]

Q3-0 checks:
1. `X1^[3]` is nonzero in the ambient degree-3 tensor realization.
2. `X1^[3]` is not contained in `(R_inf)_3`.
3. Therefore its class survives nontrivially in the degree-3 quotient relevant to the q=∞ restricted structure.

## Decision

- `X1^[3]` nonzero modulo `(R_inf)_3` → Q3 may proceed to construct `d=[X1^[3],X2]` and compare the resulting structure.
- `X1^[3]` in `(R_inf)_3` → restricted-power class is killed; record this as a separate degeneration of the proposed q=∞ analogue, not as the generic `NO STRUCTURE` case.

## Scope

This step does **not** claim that q=∞ has the same degree-4 `d`-generated structure as q=3. It only establishes whether the input class needed to define `d` survives.
