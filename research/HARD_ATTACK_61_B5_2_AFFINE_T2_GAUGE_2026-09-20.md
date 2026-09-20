# HA61-B5-2 — DEGREE-THREE GAUGE TERM AND AFFINE t_2 SHIFT — 2026-09-20

## Status

**OPEN / LOAD-BEARING.**

The degree-three Lie/gauge sector can be computed explicitly. It is not an independent new functional, but it also cannot simply be declared zero. Under a residual relation-gauge change
\[
P_3\mapsto P_3+[v,R],
\]
the secondary /9 evaluation of the cubic bracket changes by a scalar multiple of the already-known primary obstruction.

This means the raw vector called \(t_2\) is, in general, only defined up to an affine shift by the previous power direction \(p\) unless the accompanying lift/coordinate transformation is tracked.

## 1. Triple-bracket evaluation

For the commutator convention \([a,b]=a^{-1}b^{-1}ab\), modulo 27 the first-order crossed-commutator formula implies
\[
\frac{z([x,[y,z]])}{9}
=
-\lambda(x)
\bigl(\lambda(y)f(z)-\lambda(z)f(y)\bigr)
\pmod3,
\]
where \(\rho_2=1+3\lambda\) and \(z\bmod3=f\).

By linearity, for a cubic Lie term \([v,R]\),
\[
T_{\lambda,f}([v,R])
=
-\lambda(v)(\lambda\wedge f)(R).
\]

## 2. Use of the primary-zero equation

On the primary-zero locus,
\[
\delta_2(f)=
\bigl[f(p)+(\lambda\wedge f)(R)\bigr]\omega
=0.
\]
Therefore
\[
(\lambda\wedge f)(R)=-f(p),
\]
and hence
\[
T_{\lambda,f}([v,R])
=
\lambda(v)f(p).
\]

Thus a gauge change \(P\mapsto P+[v,R]\) changes the secondary functional by
\[
f\mapsto f(\lambda(v)p).
\]

Equivalently, at the level of a raw new-power vector,
\[
\boxed{t_2\mapsto t_2+\lambda(v)p}
\]
(up to the fixed global sign convention).

## 3. Interpretation

This has two consequences.

### Not a new independent obstruction

The shift lies in the old line \(\mathbf F_3 p\). Therefore the degree-three bracket sector does not create a genuinely new independent carrier direction.

### But raw t_2 is not automatically intrinsic

Unless \(\lambda(v)=0\) for the allowed gauge group, the vector \(t_2\) itself is not presentation/gauge invariant.

The natural object may instead be:
\[
[t_2]\in V/\mathbf F_3 p,
\]
or an affine torsor modeled on \(\mathbf F_3p\), together with the coefficient-extension parameter \(\mu\).

This is a stronger and more precise statement than simply saying “the bracket term is absorbed.”

## 4. Interaction with the next selector

The secondary obstruction has schematic form
\[
\delta_3(f)
=
\bigl[f(t_2)+(\mu\wedge f)(R)\bigr]\omega
\]
after the old-action terms are collected.

Replacing
\[
t_2\mapsto t_2+ap
\]
changes the first term by \(a f(p)\).

But the primary-zero identity gives
\[
f(p)=-(\lambda\wedge f)(R).
\]
Therefore the same change can be compensated by an affine shift of \(\mu\) in the appropriate direction.

Hence the pair \((t_2,\mu)\), not the raw \(t_2\) alone, is the natural secondary object before a gauge is fixed.

## 5. Important special cases

### q=9 standard branch

Here \(\lambda=0\). Therefore
\[
t_2\mapsto t_2
\]
under the cubic \([v,R]\) shift. The raw \(t_2=X_1^{(2)}\) is stable under this particular affine ambiguity.

### q=3 standard branch

Here \(\lambda=e_2^*\) and \(p=X_1^{(1)}\). Thus
\[
t_2\mapsto t_2+v_2p.
\]
The raw statement \(t_2=0\) is therefore coordinate/gauge-sensitive unless the corresponding lift transport is included.

This explains why the q=3 branch is the more stringent test for a universal presentation-free secondary carrier.

## 6. Logical consequence for HA61-B

The claim

“all non-power degree-three terms are absorbed, so \(t_2\) is intrinsic”

is too strong.

The correct statement is:

\[
\boxed{
\text{degree-three bracket terms are old-sector/gauge directions,}
\quad
\text{but they induce an affine shift of the raw }t_2.
}
\]

Thus B5 can close only after constructing the **combined secondary quotient/torsor** in which this affine shift is identified.

## 7. Current decision

- degree-three bracket contribution computed: **PASS / LOCAL**;
- independent new functional from \([v,R]\): **FAIL / CLOSED**;
- raw vector \(t_2\) presentation-independent: **FAIL / CLOSED**;
- affine/torsor secondary carrier \((t_2,\mu)\): **OPEN / LOAD-BEARING**;
- HA61-B: **OPEN / LOAD-BEARING**;
- HA61-C: **not opened**.

## 8. Next authorized attack

Construct the combined affine action explicitly:
\[
(v,c): (t_2,\mu)\mapsto
(t_2+\lambda(v)p,\,\mu+\text{corresponding compensator}),
\]
and determine its invariant quotient.

If the quotient is canonically a single affine class in
\[
V/\mathbf F_3p
\]
(or an equivalent extension torsor), B5 can be closed at the intrinsic level.

If a second independent affine parameter survives, the current two-stage carrier is insufficient.
