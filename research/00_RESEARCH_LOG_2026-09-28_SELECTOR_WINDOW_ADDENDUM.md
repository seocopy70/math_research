# PAPER 3 — RESEARCH LOG ADDENDUM — 2026-09-28

## Selector-window minimality attack

After the finite cup-line compression was closed, the next target was absolute intrinsic minimality of the recognition window.

The current sharp window is
\[
W_{p^{k-1}+1}(G),
\]
while the affine crossed-cocycle theorem proves
\[
n_{\mathrm{aff}}(k)=p^{k-1}+1
\]
for the full representation category.

A critical distinction was established:
\[
\text{sharp factorization of all affine cocycles}
\not\Rightarrow
\text{sharpness of the Kummer recognition predicate}.
\]

The Kummer selector only asks for surjectivity of
\[
H^1(Q,A_k(\rho))\to H^1(Q,\mathbf F_p),
\]
so loss of an individual crossed cocycle at a shallower quotient does not by itself imply failure of orientation recognition.

The D2 variation identity
\[
\delta_{\rho_k}(f)-\delta_{\chi_k}(f)=\nu\smile\bar f
\]
does not close the gap either: to turn the global nonzero cup obstruction into a finite rejection at a shallower quotient, the relevant lifting obstruction must be represented by a cocycle that factors through that shallower quotient. The sharp affine theorem does not provide this.

The base case
\[
p=3,\quad k=2,\quad W_3\text{ versus }W_4
\]
is therefore the decisive concrete test. The existing 81-candidate computation verifies the selector at the established window but does not establish failure or success at the smaller window.

Classification after this attack:
- affine factorization threshold: PASS/CLOSED;
- affine sharpness: PASS/CLOSED;
- intrinsic 1D cup carrier at the sharp window: PASS/CLOSED;
- absolute intrinsic selector-window minimality: OPEN/LOAD-BEARING;
- next authorized computation: dedicated W3 base-case selector test.

Detailed analysis: research/PAPER3_SELECTOR_WINDOW_MINIMALITY_ATTACK_2026-09-28.md.

No prior CLOSED result was reopened or downgraded.
