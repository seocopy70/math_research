# Q3/Q9 — S9 H-closure redesign gate (C3.1–C3.3)

Date: 2026-09-19

## Status

**C3.1 PASS, C3.2 FAIL, C3.3 PASS.**

The complete H-orbit span of (S_9=X_1^{[9]}) is the full
(L_1^{[9]}) coefficient layer, but this H-closure is **not** the
relation contribution of the fixed q=9 presentation.

## C3.1 — exact orbit closure

Using exact (mathbb F_3) arithmetic and the complete set of
nonzero-vector symplectic transvections, the complete orbit-span
calculation gives

[
oxed{dimlangle Hcdot S_9angle=4}
]

and

[
oxed{langle Hcdot S_9angle=L_1^{[9]}}.
]

No smaller generating-set assumption is used in the final computation.

## C3.2 — provenance

The fixed q=9 degree-9 relation space is already frozen as

[
(I_9)_9=(I_infty)_9opluslangle S_9angle,
]

with

[
(I_infty)_9cap L_1^{[9]}=0.
]

The fixed transvection gives

[
t_{e_2}(S_9)=S_9+X_2^{[9]}.
]

Hence (X_2^{[9]}) is an H-orbit direction but is not contained in
the fixed-presentation degree-9 relation space. Therefore the H-closure
cannot be promoted as an equivalent replacement for ((I_9)_9).

[
oxed{	ext{C3.2 = FAIL}}
]

This is a mathematical provenance failure, not an implementation
failure.

An H-closed enlargement can be defined as a different restricted ideal,
but it corresponds to adding additional p-power relations and is not
the original q=9 presentation.

## C3.3 — baseline intersection

The frozen S9-B structural lemma gives

[
(I_infty)_9cap L_1^{[9]}=0.
]

Since C3.1 gives (langle Hcdot S_9angle=L_1^{[9]}),

[
oxed{langle Hcdot S_9anglecap(I_infty)_9=0}.
]

Thus C3.3 is PASS.

## Gate consequence

The H-closure rescue route is **CLOSED / NOT PROMOTED**.

In particular, the tempting replacement

[
(I_infty)_9+langle Hcdot S_9angle
]

has dimension

[
13524+4=13528,
]

but this is a different H-stable relation enlargement, not the
degree-9 relation space of the fixed q=9 group. The number 13528 must
not be used as the original q=9 relation dimension.

## Next authorized direction

Do not proceed to (gr_9) or (D_9) using either the naive
((I_9)_9) or the artificial H-closed enlargement.

Return to the independently defined q=9 filtration comparison track:
derive the first nonzero baseline-relative degree-9 source of the
full q=9 presentation from the presentation/Magnus expansion, without
assuming H-stability.

The existing Gate-C / degree-9 derivation remains the appropriate
next controlled question.
