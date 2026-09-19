# Q3/Q9 — Gate C degree-9 source derivation

Date: 2026-09-19

## Status

**Gate C — PASS for the first baseline-relative q=9 source.**

The existing Gate-C protocol required an independent derivation of the first
nonzero homogeneous degree of the full q=9 baseline-relative control before
any new downstream invariant is designed.

Using the repository's frozen Magnus conventions over F3,

[
x_i=1+X_i,qquad [a,b]=aba^{-1}b^{-1},
]

and the existing control construction

[
C_q=x_1x_2[x_3,x_4]x_1^q x_2^{-1},
qquad
C_infty=x_1x_2[x_3,x_4]x_2^{-1},
]

followed by the frozen common-factor stripping

[
s_q=C_qx_1^{-1}[x_3,x_4]^{-1},
]

the exact truncated Magnus computation through degree 9 gives

[
Delta_d(9)=operatorname{in}_d(s_9)-operatorname{in}_d(s_infty)=0
quad(1le dle8),
]

and

[
oxed{Delta_9(9)=X_1^9}.
]

The characteristic-3 identity independently gives

[
(1+X_1)^9=1+X_1^9
]

through the truncation, so the result is consistent with the expected
first possible q=9 power contribution.

## Exact computation result

Nonzero homogeneous degrees through degree 9:

[
oxed{{9}}.
]

First nonzero component:

[
oxed{Delta_9(9)=X_1^9}.
]

No degree-3 source is being reused or inferred from q=3.

## Restricted-Lie interpretation boundary

The previously closed S9-A ambient gate established

[
X_1^9=X_1^{[9]}
]

in the one-generator enveloping realization over F3. Therefore the degree-9
Magnus source is compatible with the already established ambient restricted
element

[
oxed{S_9=X_1^{[9]}}.
]

This does **not** yet imply that (Delta_9(9)) itself is a canonical
degree-9 quotient invariant, nor does it imply H-stability.

## Consequence

Gate C's source-location question is now closed:

[
oxed{	ext{first q=9 baseline-relative source degree}=9}.
]

The next step is a **new source-map gate**, not D9 and not the old degree-3
N/J probe. One must define, from the repository's frozen construction, a
degree-9 analogue that maps the source to the appropriate comparison module,
then independently verify that definition and whether the resulting source is
nonzero.

The failed H-stability of the naive relation space remains unchanged and
must not be bypassed by treating S9 as an H-submodule.
