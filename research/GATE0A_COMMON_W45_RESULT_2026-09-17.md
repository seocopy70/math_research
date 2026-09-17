# Gate 0-A — q=3 / q=∞ common W45 direct verification

## Status

**GATE 0-A: PASS**

This is recorded as a **first direct check**, not a re-confirmation of the existing Track-B prose.

## Fixed failure rule

Before execution we fixed the following rule: if any of the degree-2 relation check, the 45-dimensional construction, or the explicit H-action/isomorphism check failed, A3-4-21P would be put on hold and the mismatch would be recorded before redesigning the q=3/q=∞ comparison track.

## Direct calculation

The q=3 and q=∞ defining relators were independently expanded through degree 2 in F_3:

- q=3: `x1^3 [x1,x2] [x3,x4]`
- q=∞ control: `[x1,x2] [x3,x4]`

The degree-2 initial forms were computed directly and were identical:

`R2_q3 = R2_qinf = X1 X2 - X2 X1 + X3 X4 - X4 X3`.

Thus the common quadratic relation is

`R = [X1,X2] + [X3,X4]`.

The exact recursive degree-4 calculation then gave:

- `dim L4 = 60`
- `dim (R)_3 = 4`
- `dim (R)_4 = 15`
- `dim Q4 = 45`
- orbit-span `dim W = 45`
- `rank([R4_ind | W_basis]) = 60`

## Explicit H action

Five explicit transvection generators were used. Direct checks gave:

- all five generators preserve the symplectic form J;
- generated group order = `51840`;
- five W-action matrices are all `45 x 45`;
- stacked `(A_i - I)` has rank `45`;
- `dim W^Sp4(F3) = 0`.

For the q=3/q=∞ quadratic objects, the verified relation subspaces are literally identical and the same explicit five H generators act on the same quotient construction. Therefore the identity map is the candidate H-equivariant isomorphism. It was checked on all five generator matrices:

`W45_IDENTITY_INTERTWINER_CHECK = PASS`.

## CI certificate

Workflow run: `35197992399`

Commit: `62647d620549168fe4b2e2fb0d0b7d246c107d4d`

Final status: **success**.

Key raw outputs:

```text
DEGREE2_RELATION_MATCH = True
EXPECTED_RELATION_MATCH = True
dim Q4 = 45
dim W_q3 = 45
dim W_qinf = 45
W_DIM_MATCH = True
H_generator_count = 5
H_generator_matrices_shape = [(45, 45), (45, 45), (45, 45), (45, 45), (45, 45)]
H_generators_symplectic = True
H_generated_group_order = 51840
W45_IDENTITY_INTERTWINER_CHECK = PASS
GATE0A_PASS = True
```

## Interpretation

This directly verifies the **common quadratic W45 claim**. It does **not** establish that q=∞ has the same A3-4 `B/A` and `K` 35-dimensional structures. That remains the Gate 0-B question.

It also does **not** close or invalidate A3-4-21P. The Ext¹ comparison remains open pending the degree-3 → degree-4 structural trace and the existence/action of q=∞ analogues of `B/A` and `K`.

The already verified degree-3 q-sensitive term `X1^[3]` is not used here as a reason to abandon the degree-4/Ext track.
