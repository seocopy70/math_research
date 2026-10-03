# PAPER 4 — T1-C INTRINSIC FACTORIZATION PRE-CHECK — 2026-10-03

## Purpose

After the relative threshold theorem
\[
n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1
\]
was frozen for the declared stress family, the next question is whether that result can be factored through an intrinsic finite-window object after forgetting the chosen map to the reference Demuškin quotient.

This document is a **pre-check only**. No new carrier computation is authorized from it.

## 1. Object

The current target is the relative extension-separation datum:
\[
\mathsf T(G_{s,a},D,\pi;n)
=
[\text{split/non-split of }W_n(G_{s,a})\xrightarrow{\pi}D/D_n(D)].
\]

The theorem already proved is relative to the explicit quotient map \(\pi\).

An unmarked finite-window candidate would instead have input only
\[
W_n(G)
\quad\text{or}quad
(W_n(G),W_{n+1}(G))
\]
as an abstract filtered finite group.

## 2. Input test

There is an immediate categorical mismatch.

The relative target is a property of a **map of extensions**
\[
1\to K_n\to W_n\xrightarrow{\pi}Q_n\to1,
\qquad Q_n=D/D_n(D),
\]
not of \(W_n\) alone.

If \(\pi\) is removed from the input, then neither the distinguished quotient \(Q_n\) nor the kernel \(K_n\) is part of the object by definition. Therefore the relative extension class is not automatically a function on the unmarked finite group.

To continue legitimately, one must first prove one of the following:

1. \(\pi\) is canonically reconstructible from the intrinsic finite window; or
2. a weaker relative datum is canonically reconstructible and is sufficient to evaluate the threshold obstruction.

Without one of these, constructing a “carrier” would simply re-encode the forgotten quotient map.

## 3. Functoriality

The admissible morphisms for an intrinsic object would be filtered-group isomorphisms (or the explicitly declared weaker morphisms).

The relative extension class is naturally functorial only in the category of extension diagrams:
\[
(W_n\to Q_n).
\]
It is not yet a functor on the category of unmarked \(W_n\).

Thus the functoriality gate is currently **NOT PASSED** for the unmarked target.

## 4. Gauge

At the relative level, presentation and lift changes are quotiented by the extension-class formalism. This part is now controlled.

At the unmarked level, there is a new gauge group: automorphisms of \(W_n\) that do not preserve a chosen quotient map \(\pi\). Any proposed intrinsic realization must be invariant under these automorphisms.

This is a strictly stronger requirement than the already solved Fox/lift gauge.

## 5. Orientation bridge

Gate T is currently an extension-depth problem, not an orientation-recovery theorem. Therefore no orientation functional should be inserted at this stage.

The only bridge required is
\[
\text{intrinsic finite datum}
\longrightarrow
\text{relative extension obstruction}.
\]
That bridge is presently unproved.

## 6. q-blindness

A candidate intrinsic object may not insert \(q=p^a\) by definition.

The relative theorem itself is indexed by the hidden Demuškin parameter \(a\). Hence a q-blind carrier can support the theorem only if the relevant q-depth is recovered from the finite input or if the target is reformulated without requiring the hidden reference quotient.

No such reconstruction is currently established.

## 7. Separation

The existing Gate-O/K–Z results show that fixed-depth windows can be blind to sufficiently deep extension data. They do **not** by themselves prove that the present stress-family threshold cannot be recovered adaptively.

Therefore no new no-go theorem is claimed here.

The correct separation question is narrower:

> Can two admissible extension diagrams with different relative threshold data induce isomorphic unmarked finite windows at the same proposed intrinsic depth?

This is the first legitimate negative test after the pre-check. It must be posed only after the object category is fixed.

## 8. Novelty

A construction that merely stores \((W_n\to D/D_n(D))\) is not an intrinsic compression result; it is the already-proved relative input.

A construction that canonically reconstructs the quotient map or an equivalent obstruction object from \(W_n\) would be genuinely new.

## 9. Stop

The Object/Input/Functoriality gates do not currently pass for an unmarked factorization.

Therefore:

\[
\boxed{\text{STOP — no new carrier computation is authorized yet.}}
\]

The next authorized task is a **same-window separation test at the unmarked level**, designed to decide whether the relative obstruction can even be a function of the abstract finite window.

## 10. Classification

- relative threshold theorem: **PASS / CLOSED**;
- factorization through the marked extension diagram: **PASS / CLOSED by the existing extension-class formalism**;
- factorization through the unmarked finite window: **OPEN / LOAD-BEARING**;
- unmarked same-window no-go: **OPEN**;
- coarsest intrinsic realization: **OPEN**;
- blind carrier search: **STOP / NOT AUTHORIZED**.
