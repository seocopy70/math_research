# Paper 4 — weighted-Schreier derivation gate — 2026-10-05

## Classification

**SC novelty: CONDITIONAL -> likely not independent novelty.**

The uploaded source \`arXiv-1007.1489v3\` is the full TeX source of *Groups of positive weighted deficiency and their applications*. Direct inspection of the relevant Section 2.4 / Section 3 material shows that its weighted-Schreier machinery is strong enough to derive the Paper-4 subgroup comparison
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K)
\]
for a free pro-p group F and an index-p subgroup K, after specializing the uniform weight to the ordinary Zassenhaus filtration.

This does **not** invalidate the Paper-4 theorem. It changes the novelty boundary: the SC statement itself should not be presented as a new standalone theorem until an independent obstruction is found.

## 1. Relevant statements in the source

The source explicitly establishes:

1. **Uniform weight = Zassenhaus order.** Its Proposition \`uniform2\` states that for a finitely generated free pro-p group with a uniform weight function W there is beta in (0,1) such that
\[
W(f)=\beta^{d_F(f)},
\]
where \(d_F(f)\) is the Zassenhaus degree.

2. **Restriction to a closed subgroup remains a weight function.** Its Corollary \`weight_preserve\` states that if W is a weight function on free pro-p F, then its restriction to any closed subgroup H is again a weight function.

3. **Index-p weighted Schreier basis.** Its Lemma \`index_p0\` gives, for an index-p subgroup H and suitable generator x,
\[
X'=\bigcup_{y\ne x}\{y,[y,x],\ldots,[y,\underbrace{x,\ldots,x}_{p-1}],x^p\},
\]
and states that X' is W-optimal when F is free and W is a weight function.

4. **Exact weights of the Schreier generators.** In the proof of its Lemma \`indexp\`, the source states
\[
W(x^p)\le W(x)^p,\qquad
W([y,\underbrace{x,\ldots,x}_{k}])\le W(y)W(x)^k,
\]
with equality in the free/weight-function case.

5. **No-cancellation property.** Its Proposition \`cor1\` characterizes weight functions by power-commutator factorization: the weight of an element is determined by the largest weight of its nonzero power-commutator terms. Thus the weighted filtration is not merely a generator-by-generator upper bound.

## 2. Specialization to the Paper-4 SC

Choose the uniform weight on F with every free generator of weight beta. By \`uniform2\`,
\[
W_F(g)=\beta^{d_F(g)}.
\]

Choose the index-p kernel K and the Schreier basis X' from \`index_p0\`, with the transversal generator z outside K.

The Schreier generators have Zassenhaus/weight exponents at most
\[
1,2,\ldots,p-1,p.
\]
Equivalently, after writing \(W_K=\left.W_F\right|_K\), every generator of X' has W_K-weight exponent at most p.

Because \(W_K\) is again a weight function, the power-series/power-commutator characterization implies that a nontrivial K-element whose ordinary K-Zassenhaus degree is \ell has some nonzero K-coordinate monomial of length \ell, and that monomial has weighted exponent at most \(p\ell\). Hence
\[
d_F(g)\le p\,d_K(g).
\]
Therefore
\[
d_F(g)\ge n\quad\Longrightarrow\quad
d_K(g)\ge\left\lceil\frac np\right\rceil,
\]
which is exactly
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
\]

The key point is that this derivation is not merely heuristic: the source's weight-function characterization supplies the required non-cancellation statement.

## 3. Consequence for the Paper-4 prefix-code proof

The Paper-4 Magnus prefix-code proof remains mathematically valid, but its role changes.

It should **not** be advertised as a new general index-p Zassenhaus comparison theorem unless a genuinely stronger statement is isolated.

Its safer role is:

- an explicit self-contained Magnus-coordinate derivation of the comparison in the precise notation needed by Paper 4;
- a transparent bridge from the free-presentation coordinates to the transfer calculation;
- an independent verification/alternative proof of a consequence already accessible from weighted-Schreier theory.

The previous wording “strongest novelty candidate = SC” should therefore be downgraded.

## 4. What remains potentially novel

The literature threat is substantially weaker for the downstream Paper-4 objects:

### (a) The finite-window transfer obstruction
\[
\varepsilon_s(W)
=p^{s-1}V(t)\pmod{p^sK^{ab}}.
\]

The uploaded weighted-Schreier source does not contain this finite-window torsion-line construction.

### (b) The exact \(a=s\) versus \(a=\infty\) separation

The source contains no theorem matching the Paper-4 stress family
\[
z^{p^s}=x_1^{p^a}r_2^{-1}
\]
and no finite-window comparison proving non-isomorphism at \(n=p^s+1\).

### (c) The exact threshold
\[
n_{\mathrm{sep}}(s)=p^s+1
\]
for the declared stress family.

The weighted-Schreier machinery explains the subgroup-filtration estimate needed for the proof, but does not by itself produce the Paper-4 torsion defect or the separation theorem.

## 5. Novelty classification after the source audit

- General index-p Zassenhaus comparison SC: **CONDITIONAL / likely standard corollary of weighted-Schreier theory**.
- Paper-4 Magnus prefix-code implementation: **PASS / mathematically valid; novelty not claimed**.
- Transfer bound TF_s: **PASS / CLOSED mathematically; novelty dependent on downstream construction**.
- Intrinsic finite-window \(\varepsilon_s\): **OPEN / strongest current novelty candidate**.
- \(a=s\) versus \(a=\infty\) separation at \(p^s+1\): **OPEN / strong theorem-level novelty candidate**.
- Exact threshold \(p^s+1\): **OPEN / strong application-level novelty candidate**.
- Paper-4 mathematical result overall: **PASS / CLOSED** in the declared scope.
- Publication novelty overall: **CONDITIONAL / OPEN**.

## 6. Governance consequence

Do not reopen the mathematical Paper-4 proof merely because SC has a close prior derivation.

The correct response is to **move the novelty center of gravity downstream**:
weighted-Schreier comparison -> transfer bound -> intrinsic \(\varepsilon_s\) -> exact finite-window separation.

The next literature search should therefore target the exact \(\varepsilon_s\), finite-window torsion-line obstruction, and the \(a=s\) versus \(a=\infty\) family, not generic index-p Schreier theory.


## 2026-10-05 — direct source recheck: SC derivation is genuinely covered by the weighted-Schreier chain

The uploaded source was decompressed and the cited statements were inspected line-by-line, rather than inferred from the earlier summary. The relevant chain is exact:

`uniform2` gives (W_F(g)=\beta^{d_F(g)}) for the uniform weight on free (F).

`weight_preserve` says the restriction (W_K=W_F|_K) is again a weight function on the closed subgroup (K).

`index_p0) gives the standard index-(p) Schreier generating set
[
X'={y,[y,z],ldots,[y,z,ldots,z],z^p}
]
and says it is (W_K)-optimal in the free case.

The proof of `indexp` gives equality of weights in the free/weight-function case:
[
W_K([y,z,ldots,z]_j)=W_F(y)W_F(z)^j=\beta^{j+1},
qquad
W_K(z^p)=W_F(z)^p=\beta^p.
]
Thus every Schreier generator has ambient Zassenhaus exponent at most (p).

Finally, `cor1`(ii) is explicitly a **global no-cancellation statement for every (fin K)** in its power-commutator factorization in (X'):
[
W_K(f)=max{W_K(c)^{p^k}:\alpha_{c,k}
e0}.
]
This is the precise missing logical step needed to turn generator weight bounds into an elementwise comparison.

Hence, if (d_K(f)=ell), a nonzero K-power-commutator term of K-degree at most (ell) has ambient exponent at most (pell), and `cor1` prevents cancellation at the maximal (W_K)-weight. Since (W_K(f)=W_F(f)=\beta^{d_F(f)}), one gets
[
d_F(f)le p,d_K(f).
]
Therefore
[
D_n(F)cap Ksubseteq D_{lceil n/pceil}(K).
]

### Review verdict

The earlier caution about “is cor1 strong enough?” is now resolved **YES**: `cor1` is stated for arbitrary (fin F), not merely for generators or selected optimal words, and its proof explicitly rules out cancellation in the relevant power-commutator factorization.

The correct novelty statement is consequently stronger than “the SC proof resembles prior work”:

- **SC itself is a derivable consequence of prior weighted-Schreier machinery under the Paper-4 hypotheses.**
- The Magnus prefix-code proof is a valid self-contained reproof/coordinate realization, but should not be presented as the novel theorem.
- The novelty audit must move downstream to the intrinsic transfer obstruction (arepsilon_s), the (a=s) versus (a=\infty) finite-window separation, and the exact threshold (p^s+1).

This is a literature-method transfer result, not a negative result about Paper 4's mathematics.


## 2026-10-05 — SC literature audit CLOSED by decision

The project now treats the SC audit as closed. The distinction is:

**Prior literature:** supplies the weighted-Schreier/Zassenhaus ingredients.

**Paper-4 deduction:** assembles those ingredients into the exact depth-comparison
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K),
\]
in the form required for the finite-window transfer argument.

No audited source was found stating this exact subgroup-depth comparison as the Paper-4 lemma, although the weighted-Schreier machinery is sufficient to derive it. Therefore the safe novelty language is **new logical deduction/assembly**, not “new underlying Zassenhaus/Schreier theory.”

Classification:
- SC mathematical validity: **PASS / CLOSED**.
- SC literature audit: **PASS / CLOSED**.
- SC as independent foundational theorem: **not claimed**.
- SC as a new Paper-4 logical step in the proof chain: **YES — claimable**.
- Further generic SC literature search: **STOPPED**.
- Novelty audit moves downstream to \(\varepsilon_s\), intrinsic finite-window separation, and the exact threshold \(p^s+1\).

The Magnus prefix-code proof remains as an independent self-contained verification and should be presented as such.
