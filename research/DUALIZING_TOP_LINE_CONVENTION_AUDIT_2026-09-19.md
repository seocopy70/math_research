# DUALIZING TOP-LINE CONVENTION AUDIT — 2026-09-19

## Objective

Resolve the remaining convention issue in the MU-CHI bridge: for the repository's frozen degree-one matrix \(g\), determine whether the induced \(\operatorname{Aut}(G)\)-action on \(H^2(G,\mathbf F_3)\) is \(\mu\) or \(\mu^{-1}\), and determine what this says about recovery of the group orientation \(\chi\).

## 1. Frozen matrix is generator-side / \(H_1\)-side

The project convention is degree-one action on the generator/abelianization side:
\[
g:\;G/\Phi(G)\simeq H_1(G,\mathbf F_3)\to H_1(G,\mathbf F_3),
\]
with
\[
g^T Jg=\nu(g)J,\qquad ge_1=\mu(g)e_1.
\]

For an actual automorphism, the preceding manual gate established
\[
\nu(g)=\mu(g)\in\mathbf F_3^\times.
\]

## 2. Passage to \(H^1\)

Cohomology is contravariant. Under the natural duality
\[
H^1(G,\mathbf F_3)\simeq H_1(G,\mathbf F_3)^*,
\]
the induced matrix is
\[
g^{-T}.
\]

If \(J\) is the frozen alternating form on the \(H_1\)-side, the dual alternating form is represented (up to the fixed basis identification) by \(J^{-1}\). Therefore
\[
(g^{-T})^T J^{-1}g^{-T}
=
g^{-1}J^{-1}g^{-T}
=
\nu(g)^{-1}J^{-1}.
\]

Hence the induced similitude scalar on the cohomological pairing is
\[
\nu(g)^{-1}.
\]

For a Demushkin group the cup product
\[
H^1(G,\mathbf F_3)\times H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3)
\]
is perfect, and \(H^2(G,\mathbf F_3)\) is one-dimensional. Functoriality therefore forces the induced scalar on \(H^2\) to be
\[
\boxed{\mu_{H^2}(\phi)=\nu(g)^{-1}=\mu_{\rm int}(\phi)^{-1}}.
\]

This is the convention-corrected form of the previous statement that the top-duality line carries the same invariant: it carries the **inverse** because the repository matrix is on the \(H_1\)/generator side.

## 3. No contradiction with the intrinsic torsion-line interpretation

The torsion-line character remains
\[
\mu_{\rm int}(\phi)=\mu(g).
\]

The top-cohomology character is
\[
\mu_{H^2}(\phi)=\mu_{\rm int}(\phi)^{-1}.
\]

Since
\[
\mathbf F_3^\times=\{1,-1\},
\]
the inverse happens to equal the element itself:
\[
a^{-1}=a\qquad(a\in\mathbf F_3^\times).
\]

Therefore, specifically for \(p=3\),
\[
\boxed{\mu_{H^2}=\mu_{\rm int}}
\]
as \(\mathbf F_3^\times\)-valued characters, even though the conceptual variance is inverse.

This is important: the equality is a special \(p=3\) accident, not a reason to identify the underlying constructions in general.

## 4. What this says about \(\chi\)

The canonical orientation is still
\[
\chi:G\to\mathbf Z_3^\times,
\]
defined by the \(G\)-action on the \(\mathbf Z_3\)-dualizing module.

Its reduction is trivial:
\[
\bar\chi=1:G\to\mathbf F_3^\times.
\]

By contrast,
\[
\mu_{\rm int}:\operatorname{Aut}(G)\to\mathbf F_3^\times
\]
is an automorphism character.

Thus the top-duality realization of \(\mu\) does **not** produce a map
\[
\chi\longmapsto\mu
\]
and does not recover the higher \(3\)-adic information of \(\chi\).

In particular, any recovery theorem for \(\chi\) from filtered/graded data must retain information beyond the mod-3 top-line scalar. The present \(\mu\)-observable is therefore a genuine canonical duality shadow, but not the orientation itself.

## 5. Gate decision

### PASS
- Frozen \(g\) is \(H_1\)/generator-side.
- The induced \(H^1\) action is \(g^{-T}\).
- The top-cohomology scalar is \(\nu^{-1}\).
- Since \(p=3\), \(\nu^{-1}=\nu\), so the top-duality line realizes the same \(\mathbf F_3^\times\)-character as \(\mu_{\rm int}\).

### FAIL
- Any identification of this top-line character with the full orientation \(\chi:G\to\mathbf Z_3^\times\).
- Any claim that \(\mu\) contains the \(3\)-adic orientation data beyond mod 3.

### OPEN / NEXT
The MU-CHI bridge itself is now conceptually resolved: \(\mu\) is a canonical automorphism-of-duality-line shadow, not a reduction of \(\chi\). The next research question should return to the original target: locate a filtered/graded object retaining the \(3\)-adic orientation information (the \(1+3\mathbf Z_3\) layer), rather than continuing to refine the mod-3 \(\mu\) observable.

No finite scan is authorized by this gate.
