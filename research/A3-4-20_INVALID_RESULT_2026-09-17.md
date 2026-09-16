# A3-4-20 — INVALID RESULT / DEFINITION AUDIT

Date: 2026-09-17
Run: GitHub Actions `35115294064`
Job: `104859060091`

## Status

**A3-4-20 is INVALID as a Loewy radical/socle test. It is not a mathematical FAIL.**

The intertwiner reconstruction itself passed the expected exact checks:

- intertwiner system: `6125 x 1225`
- `rank(E) = 1224`
- `Hom_dimension = 1`
- `rank(Q) = 10`
- `dim ker(Q) = 25`
- `dim im(Q) = 10`

These agree with A3-4-17.

## Error identified

The script called

`sum_g im(g-I)`

"radical" and

`intersection_g ker(g-I)`

"socle".

The latter is the invariant-vector space `M^H`, not the module-theoretic socle in general. The former is the augmentation-generated subspace and is not automatically the Jacobson/Loewy radical of an arbitrary modular group module.

The run consequently produced dimensions 35 and 0 rather than the already established Loewy dimensions 25 and 10. This exposes a definition/implementation error in A3-4-20 rather than a contradiction in the modules.

## Corrective principle

Use the actual Q-defined invariant submodules and test them directly as modules:

- `ker(Q)` has dimension 25 and is an H-submodule of `B/A`.
- `im(Q)` has dimension 10 and is an H-submodule of `K`.
- Test whether each is simple with GAP/MeatAxe.
- Test whether the corresponding quotient is simple.

If both the submodule and quotient are simple, the exact short exact sequence is established without assuming a radical/socle formula.

The corrected experiment is A3-4-20R.

## Interpretation policy

Do not yet call the extension "flipped". First establish the actual simple submodule and simple quotient on each side. Only then identify the extension directions and proceed to split/non-split and Ext analysis.
