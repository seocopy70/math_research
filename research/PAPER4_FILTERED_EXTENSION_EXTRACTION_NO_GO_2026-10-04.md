# PAPER4_FILTERED_EXTENSION_EXTRACTION_NO_GO_2026-10-04.md

## Target

Test whether the intrinsic one-step Zassenhaus extension
\[
1\to K_n:=D_n(G)/D_{n+1}(G)\to W_{n+1}(G)\to W_n(G)\to1
\]
provides a new canonical defect that extracts the hidden \(p^s\)-power relation, without introducing a marked orientation/character.

The active boundary is the unresolved critical case \(n=p^s\), especially the \(a=s\) versus \(a=\infty\) stress comparison.

## Pre-check

### Object — PASS

The extension above is canonical and q-blind: it is determined by the Zassenhaus filtration of the finite window and contains the kernel, its filtration degree, conjugation action, and the extension itself.

Since \([D_n,G]\subseteq D_{n+1}\), the kernel \(K_n\) is central.

### Input — PASS

Allowed input is only the filtered finite extension. The hidden \(q=p^a\), a chosen character, and a chosen presentation are not inserted into the object.

### Functoriality — PASS

An isomorphism of filtered finite windows induces an isomorphism of the corresponding one-step extensions. Thus the extension is an intrinsic object over the finite-window isomorphism class.

### Gauge — PASS, with a decisive boundary

Choose a section \(s:W_n\to W_{n+1}\). Because the kernel is central, the section defines a 2-cocycle
\[
c_s(g,h)=s(g)s(h)s(gh)^{-1}\in K_n.
\]
Replacing \(s\) by another section changes \(c_s\) by a coboundary. Hence any proposed p-power/commutator defect computed from a particular lift or section is not canonical unless it descends through this gauge action.

This is standard central-extension theory. The intrinsic datum is the extension-equivalence class \([c_s]\in H^2(W_n,K_n)\), not an individual lift formula. The Zassenhaus setting additionally identifies the graded layer with restricted-Lie p-power/commutator data, but that does not remove the section gauge.

### Orientation bridge — FAIL / CLOSED for a scalar defect

The one-step extension has no distinguished generator, character, or affine direction. A p-power/commutator formula for a selected lift therefore depends on a section/lift choice unless an additional canonical orientation bridge is supplied.

The previously explored marked \(E_\psi\) construction supplies such an orientation only in the marked presentation category; the present object intentionally forgets that marking. No intrinsic map from the abstract extension to a distinguished \(\psi\) has been established.

Therefore the proposed route
\[
\text{unmarked extension}\to\text{distinguished lift defect}
\]
fails the mandatory orientation/gauge test.

### q-blindness — PASS

The extension itself contains no inserted \(q=p^a\).

### Separation — NOT A NEW TESTABLE INVARIANT

After quotienting section/lift gauge, the remaining canonical object is the extension-equivalence class itself. But this is precisely the isomorphism class of the structured map
\[
W_{n+1}\twoheadrightarrow W_n.
\]
Therefore asking whether this full package separates two cases is equivalent to the original finite-window extension-isomorphism problem; it is not a lower-complexity extraction theorem.

In particular, the filtered-extension package does not produce a new scalar/carrier automatically. Any genuine separation would require classifying the extension class (or an explicitly declared quotient of it), which is the same structural problem in different language.

This does **not** prove that the two critical windows are isomorphic. It proves that the proposed 'extension extraction' strategy does not reduce that question unless an additional intrinsic quotient/factorization theorem is supplied.

## Independent structural verification

The central-extension interpretation agrees with standard extension theory: central extensions with fixed action are classified by \(H^2\), with changes of section changing cocycles by coboundaries. The Zassenhaus filtration also has canonical restricted-Lie p-power and commutator operations on \(D_n/D_{n+1}\). These facts confirm the gauge analysis, but they do not provide the missing orientation bridge.

## Result

**Filtered-extension extraction as a new canonical defect: FAIL / CLOSED.**

More precisely:

- canonical one-step filtered extension: **PASS / CLOSED**;
- section/lift gauge analysis: **PASS / CLOSED**;
- intrinsic scalar/orientation defect from the unmarked extension alone: **FAIL / CLOSED**;
- full extension-equivalence class as a separator: **OPEN**, but it is exactly the original structured finite-window isomorphism problem, not a new extraction method;
- ordinary mod-p cohomology route: **PASS / CLOSED and STOPPED**;
- arbitrary degree-only theorem: **FAIL / CLOSED**.

## Stop decision

Do not return to carrier hunting, new \(E_\psi\) variants, ordinary cohomology, or ad hoc lift decorations.

The research branch has reached its legitimate boundary. Any further progress would require a genuinely new theorem proving a canonical quotient/factorization of the full extension-equivalence class, not another candidate invariant search.

The bounded research objective is therefore closed at the method level: **the existing one-step filtered extension is the correct next structural layer, but it does not by itself yield a new intrinsic compression/extraction map.**
