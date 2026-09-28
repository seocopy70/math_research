# PAPER 3 — SELECTOR-WINDOW MINIMALITY ATTACK — 2026-09-28

## Status

**OPEN / LOAD-BEARING — absolute intrinsic selector-window minimality is not proved.**

The current finite recognition theorem uses the Zassenhaus window
\[
W_{N_k+1}(G),\qquad N_k=p^{k-1},
\]
and the affine factorization theorem proves the threshold
\[
n_{\mathrm{aff}}(k)=p^{k-1}+1
\]
is sharp for the full category of affine crossed-cocycle representations into
\[
S_k=A_k\rtimes U_{1,k}.
\]

The present attack asked whether that sharpness can be promoted to **minimality of the Kummer selector itself**, i.e. whether a shallower quotient
\[
W_m(G),\qquad m\le p^{k-1},
\]
can ever recognize the canonical orientation modulo \(p^k\).

It cannot be promoted by the affine sharpness argument alone.

## 1. What is proved

The affine theorem gives:

\[
\exists\,\psi=(z,\rho):G\to S_k
\quad\text{with}\quad
\psi(W_{N_k})\ne1,
\]
while every affine crossed cocycle kills
\[
W_{N_k+1}.
\]

Hence no shallower quotient preserves **all** twisted \(H^1\)-lifting data in the affine category.

This is a genuine sharp factorization statement.

It is not yet a sharp recognition statement.

## 2. The exact logical gap

The finite Kummer selector is only the predicate

\[
\mathsf K_k(Q,\rho):
H^1(Q,A_k(\rho))\to H^1(Q,\mathbf F_p)
\quad\text{is surjective}.
\]

It does **not** ask the quotient to retain every crossed cocycle.

Therefore:

\[
\boxed{
\text{loss of one crossed cocycle}
\not\Rightarrow
\text{loss of orientation recognition}.
}
\]

A shallower quotient could, in principle, lose some twisted cocycles while still retaining enough lifts to make the surjectivity predicate distinguish \(\chi_k\) from every false candidate.

This is the precise reason D4 cannot currently be upgraded from category-relative factorization sharpness to absolute selector-window minimality.

## 3. The tempting lower-bound argument and why it fails

For a false candidate on the canonical lower-level branch,

\[
\rho_k=\chi_k(1+p^{k-1}\nu),
\qquad \nu\ne0,
\]

the intrinsic variation identity gives

\[
\delta_{k,\rho_k}(f)-\delta_{k,\chi_k}(f)
=
\nu\smile \bar f.
\]

Demuškin cup nondegeneracy supplies an \(f\) with nonzero global variation.

One might try to conclude that this already forces the shallower quotient to reject \(\rho_k\).

The missing step is:

> the obstructing lifted cocycle for that \(f\) must itself factor through the shallower quotient.

At the sharp window \(W_{N_k+1}\), arbitrary-candidate affine factorization guarantees exactly this.

At \(W_{N_k}\), that guarantee fails in general: the affine sharpness witness is precisely a crossed cocycle that can remain nontrivial on \(W_{N_k}\).

Thus the global obstruction
\[
\nu\smile\bar f\ne0
\]
does not by itself imply that the **finite** connecting map for \(W_{N_k}\) is nonzero.

This is the load-bearing gap.

## 4. Why the cup-line compression does not solve minimal depth

The recently closed intrinsic cup-line result gives

\[
C_k(Q_k)
=
\operatorname{im}
\bigl(
H^1(Q_k,\mathbf F_p)^{\otimes2}
\to H^2(Q_k,\mathbf F_p)
\bigr),
\qquad
\dim C_k=1.
\]

Relation-module/cup-product duality proves this rank directly from the quadratic initial form of the Demuškin relator; the argument does not use finite-to-global \(H^2\) injectivity. The relevant pairing compatibility is recorded in Mináč–Pasini–Quadrelli–Tân, Proposition 7.1. [literature citation]

This compresses the **target carrier** at the sharp window.

It does not prove that the same obstruction is realized by a lift already living on \(W_{N_k}\).

The distinction is:

\[
\boxed{
\text{carrier dimension}
\neq
\text{depth needed for the lifting predicate to see that carrier}.
}
\]

## 5. The k=2 sanity check

For \(p=3,k=2\),

\[
N_k=3,
\qquad
N_k+1=4.
\]

The affine sharpness witness is nontrivial on the third Zassenhaus layer, so the full affine lifting category genuinely needs the fourth-stage quotient.

But the selector asks only whether every mod-3 class has **some** lift.

Consequently, even at the base case, affine non-factorization does not automatically produce a false orientation that passes the smaller selector.

The existing 81-candidate calculation verifies the canonical candidate at the proved finite window, but it is not a proof that the smaller quotient \(W_3\) fails as a selector. A dedicated \(W_3\) calculation would be needed for that claim.

## 6. What would actually prove minimal selector depth

For each \(m\le N_k\), one needs one of the following.

### Route A — explicit false candidate

Construct
\[
\rho_k\ne\chi_k
\]
such that \(\rho_k\) factors through \(W_m\) and

\[
\mathsf K_k(W_m,\rho_k)
\]
still holds.

This is the cleanest counterexample to sufficiency of \(W_m\).

### Route B — obstruction-free shallow quotient

Prove that for some false \(\rho_k\), every obstruction to surjectivity is carried entirely by cocycles nontrivial on \(W_m\), so that the finite predicate at \(W_m\) misses all global obstructions.

This would also show that the shallower quotient cannot recognize \(\chi_k\).

### Route C — universal lower-bound theorem

Prove a structural theorem of the form

\[
\mathsf K_k(W_m,\rho_k)
\Longrightarrow
\rho_k=\chi_k
\quad\Rightarrow\quad
m\ge p^{k-1}+1,
\]

using a finite relative-cohomology obstruction attached to the extension

\[
1\to W_{N_k}/W_{N_k+1}
\to W_{N_k+1}/W_{N_k+1}
\to W_{N_k}
\to1,
\]

or an equivalent relative transgression statement.

At present none of these three routes is established.

## 7. Literature check

The classical literature establishes the canonical Demuškin orientation and its Kummerian characterization, but the audited sources do not supply the missing implication from sharp affine factorization to sharp finite Kummer recognition. Labute's classical theory identifies the canonical orientation, while later Kummerian/1-cyclotomic work formulates the cohomological criterion; these are logically distinct from a minimal finite selector window. [literature citation]

The prior-art audit therefore does not close this gap.

## 8. Final classification

| Question | Status |
|---|---|
| Full affine factorization through \(W_{p^{k-1}+1}\) | **PASS / CLOSED** |
| Sharpness for the full affine category | **PASS / CLOSED** |
| 1D intrinsic cup-line at the sharp window | **PASS / CLOSED** |
| 1D linear selector-carrier minimality at the sharp window | **PASS / CLOSED** |
| Shallower quotient can/cannot recognize \(\chi_k\) | **OPEN / LOAD-BEARING** |
| Absolute selector-window minimality | **OPEN** |
| Canonical \(\mathcal O_k\to\mathbf F_p\) from \(E_k\to Q_k\) alone | **OPEN / NOT LOAD-BEARING** |

## 9. Authorized next attack

The next mathematically meaningful computation is **not** another large carrier calculation.

It is the base-case lower-window test:

\[
\boxed{
p=3,quad k=2,quad
W_3(G)\stackrel{?}{\text{ recognizes }}\chi\bmod9.
}
\]

If \(W_3\) fails, we obtain the first concrete false-candidate mechanism and can try to lift it inductively.

If \(W_3\) succeeds, then the claimed threshold \(p^{k-1}+1\) is not the selector-minimal window, even though it remains the sharp affine-factorization window.

Either outcome is decisive for the interpretation of Paper 3.

## Bottom line

The current result is stronger than “we do not know the minimal window.”

We now know **exactly why the existing sharpness theorem does not answer the selector-minimality question**, and exactly what finite calculation/theorem would settle it.

No false minimality claim should be inserted into Paper 3.
