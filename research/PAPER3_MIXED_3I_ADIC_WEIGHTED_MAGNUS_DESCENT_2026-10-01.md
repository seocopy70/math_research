# MIXED (3,I)-ADIC FOX CARRIER — WEIGHTED MAGNUS DESCENT — 2026-10-01

## Result

The global descent attack yields a substantive positive lemma, but not yet a complete carrier theorem.

Set
\[
N_k=3^{k-1}+1,
\qquad
W_k(G)=\bigl(G/D_{N_k},D_{N_k}/D_{N_k+1}\bigr).
\]

On the free pro-3 Magnus side, define the weighted filtration
\[
\mathcal F^t
=
\left\{
\sum_w a_wX^w:
v_3(a_w)+|w|\ge t
\right\}.
\]
Under the pro-3 Magnus isomorphism, the mixed maximal-ideal filtration \((3,I)^t\) is exactly this weighted filtration.

Efrat's Proposition 5.1 for the p-Zassenhaus filtration gives, for
\(\sigma\in D_N\) and a word of length \(i\),
\[
v_3(\epsilon_w(\sigma))
\ge
\left\lceil\log_3(N/i)\right\rceil.
\]
For \(N=N_k\), one has for every \(1\le i\le N_k\)
\[
i+\left\lceil\log_3(N_k/i)\right\rceil\ge k+1.
\]
Hence
\[
D_{N_k}\subseteq 1+(3,I)^{k+1}.
\]

This is the key weighted-filtration bridge.

## 1. Consequence for the coefficient algebra

The complete integral group algebra quotient
\[
\mathbf Z_3[[G]]/(3,I)^{k+1}
\]
is therefore insensitive to the kernel D_{N_k} at the group-element level. In particular, the underlying mixed coefficient algebra factors through the finite quotient \(G/D_{N_k}\).

This is stronger than the earlier statement that the mixed and Zassenhaus filtrations are merely “different”: they are different filtrations, but the specific sharp window \(N_k=3^{k-1}+1\) is large enough to control the mixed jet to precision k.

## 2. Why the second component of W_k matters

The Fox obstruction row contains one derivative order less than the relator itself. Therefore the quotient \(G/D_{N_k}\) alone is not the complete boundary datum for the projective Fox row.

The missing boundary contribution occurs exactly at weighted order k. Its mod-3 leading piece is the degree-N_k Zassenhaus layer
\[
D_{N_k}/D_{N_k+1}.
\]

Thus the project's pair
\[
W_k=(G/D_{N_k},D_{N_k}/D_{N_k+1})
\]
is the correct candidate input: the first component controls the mixed coefficient algebra below the boundary, while the second component controls the boundary relation/power term.

Efrat's p-adic Magnus/Zassenhaus matrix formalism gives the relevant coefficient-level pairing between Zassenhaus boundary classes and p-adic Magnus coefficients. This is independent literature support for the exact role of the second component.

## 3. What is actually proved

The following is now justified:

**Weighted Magnus descent lemma.**
At precision \(k\), every integral Magnus coefficient that can contribute to the mixed \((3,I)\)-jet is controlled by the Zassenhaus data through level
\(N_k=3^{k-1}+1\), with the boundary contribution represented by
\(D_{N_k}/D_{N_k+1}\).

Classification:
\[
\boxed{\text{weighted coefficient descent = PASS / CLOSED}}
\]
under the stated free-pro-3 Magnus hypotheses.

## 4. What is NOT yet proved

The remaining step is not a numerical one. One must identify the projective Fox obstruction scheme with a construction from the weighted Magnus jet that is independent of:

- the chosen free presentation;
- the chosen lift of the relation module;
- relation-generator gauge;
- Nielsen coordinates.

The first three covariance mechanisms were already verified locally. What is missing is a single categorical statement saying that the resulting finite projective scheme is the natural image of the weighted Magnus jet determined by W_k.

Therefore the exact global statement
\[
W_k\longmapsto M_k
\]
remains:

\[
\boxed{\text{OPEN / LOAD-BEARING}}
\]

but the obstruction is now sharply narrowed from “characteristic-zero data versus mod-3 data” to **relation-module/projective descent at the weighted boundary**.

## 5. Counterexample route

The obvious counterexample mechanism—altering a presentation by a relator lying in D_{N_k}—does not immediately work.

The weighted Magnus estimate shows that such a perturbation is invisible to the mixed coefficient jet below the boundary, and its first possible contribution is exactly at the boundary controlled by
\(D_{N_k}/D_{N_k+1}\).

Thus a same-W_k/different-M_k counterexample, if it exists, must exploit a failure of projective relation-module descent not visible in the weighted Magnus coefficients. A naive “deep Zassenhaus relator changes the integral jet earlier” construction is ruled out.

This is a genuine narrowing of the B branch.

## 6. Orientation consequence on the standard Demushkin category

For the fixed rank-four p=3 Demushkin category, once the global projective descent statement is supplied, the previously verified standard-family Fox equations give
\[
B=(1-q)^{-1}\pmod{3^k}.
\]
Thus the direct orientation bridge remains valid.

However, this does not by itself create a new recognition threshold: the frozen selector already recognizes
\(\chi\bmod 3^k\) at the same
\(N_k=3^{k-1}+1\) window.

Consequently, even a successful global descent theorem would establish a **new carrier construction**, but not automatically a new recognition theorem or a stronger threshold theorem.

## 7. Non-redundancy consequence

The mixed carrier contains richer integral/Magnus information than the one-dimensional selector, but the current target is only
\(\chi\bmod3^k\), which the frozen selector already recovers at the same window.

Therefore the correct novelty gate is now:

> Does the mixed carrier yield a genuinely new factorization/separation consequence beyond the already closed selector theorem?

Without such a consequence, the branch should be classified as **HISTORICAL / SUPERSEDED or FAIL / CLOSED — REDUNDANT**, even if the descent construction itself is mathematically valid.

## 8. Literature verification

Efrat's 2021 JIMJ paper proves the p-adic Magnus coefficient divisibility for Zassenhaus terms and constructs the finite-level unitriangular/Magnus pairing. In particular, Proposition 5.1 supplies the divisibility estimate used above, while the later pairing identifies the boundary Zassenhaus layer with the corresponding p-adic Magnus coefficient residue.

Mináč–Pasini–Quadrelli–Tân independently establish the Jennings identification of Zassenhaus filtration with powers of the augmentation ideal in \(\mathbf F_3[[G]]\).

These sources support the weighted descent lemma, but neither source states the project's exact projective mixed Fox factorization theorem.

## Classification

- weighted Magnus control of the mixed jet: **PASS / CLOSED**;
- boundary role of \(D_{N_k}/D_{N_k+1}\): **PASS / LOCAL**;
- complete projective Fox descent \(W_k\to M_k\): **OPEN / LOAD-BEARING**;
- same-W_k counterexample by naive deep-relator perturbation: **FAIL / CLOSED**;
- direct \(\chi\bmod3^k\) bridge on standard Demushkin family: **PASS / LOCAL**;
- genuinely new recognition consequence: **OPEN / DECISIVE**.

No large computation is authorized. The only remaining mathematical work is the categorical projective descent statement and, if it succeeds, the non-redundancy test.
