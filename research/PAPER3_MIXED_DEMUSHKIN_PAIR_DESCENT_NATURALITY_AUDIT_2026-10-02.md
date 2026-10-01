# MIXED FOX — DEMUŠKIN PAIR DESCENT / RECONSTRUCTION + NATURALITY AUDIT — 2026-10-02

## Scope

This audit closes the immediate admissibility prerequisite without conflating object-level reconstruction with a full categorical natural-transformation theorem.

Set
\[
N_k=3^{k-1}+1,
\quad
Q_k(G)=G/D_{N_k},
\quad
E_k(G)=G/D_{N_k+1},
\quad
A_k(G)=D_{N_k}/D_{N_k+1}.
\]

Let \(\mathbf{ExtWin}^{\mathrm{Dem}}_{k,d}\) be the canonical Zassenhaus extension windows arising from infinite odd-prime finite-rank Demuškin groups of fixed rank \(d\), with standard parameter
\[
q\in\{p,p^2,p^3,\ldots\}\cup\{0\}.
\]

The active project is the \(p=3\), rank-four instance, but the reconstruction argument is written for odd \(p\).

## 1. Reconstruction lemma

### Lemma (Demuškin window reconstruction)

Within the declared standard odd-p fixed-rank Demuškin family, the isomorphism class of the bare pair
\[
(Q_k(G),A_k(G))
\]
determines the isomorphism class of the extension window
\[
1\to A_k(G)\to E_k(G)\to Q_k(G)\to1.
\]

### Proof by the three q-ranges

Let \(N=N_k\).

**Case 1: \(q<N\).**

The standard Demuškin relator has the form
\[
r=x_1^q[x_1,x_2][x_3,x_4]\cdots.
\]
The commutator part begins in Zassenhaus degree 2, while the power term begins in degree \(q\). Therefore the first q-dependent relation defect occurs at degree \(q\), strictly below \(N\). The intrinsic graded dimensions
\[
d_j(G)=\dim_{\mathbf F_p}D_j(G)/D_{j+1}(G)
\]
for \(j<N\) recover this first defect, hence recover \(q\). This is filtered-intrinsic, not presentation-local. The Demuškin Zassenhaus dimension formulas provide the corresponding intrinsic graded dimensions.

**Case 2: \(q=N\).**

The q-power term is not visible in \(Q_k=G/D_N\), because it first enters at the next layer. It is visible in
\[
A_k=D_N/D_{N+1}.
\]
The degree-N relation contribution changes the intrinsic dimension of the boundary layer relative to the \(q>N\) case. Hence the pair distinguishes \(q=N\) from \(q>N\).

**Case 3: \(q>N\) (including \(q=0\)).**

The q-power term is invisible through degree \(N\), so the truncated standard presentations agree through \(D_{N+1}\). Hence the extension windows are isomorphic for all \(q>N\).

Thus distinct q-values cannot produce two non-isomorphic extension windows over the same bare pair. Therefore
\[
U^{-1}(Q_k,A_k)
\]
is a singleton up to extension-window isomorphism in the declared Demuškin category. ∎

## 2. Important logical qualification

The lemma is an **isomorphism-class reconstruction statement**.

It does not, by itself, construct a canonical section
\[
S:\mathbf{Pair}_k\to\mathbf{ExtWin}^{\mathrm{Dem}}_{k,d}
\]
on arbitrary pair morphisms. Therefore the stronger statement
\[
F_k=\bar F_k\circ U
\]
as an equality of functors still requires an explicit definition of the pair morphism category and a lift/naturality argument.

This distinction is essential. Singleton fibers on objects prove descent of any isomorphism-invariant object assignment; they do not automatically prove a fully functorial categorical factorization.

## 3. Extension-window → mixed Fox map

For a finite extension window, choose a finite free pro-p presentation of \(E_k\) compatible with the quotient map to \(Q_k\). Form the mixed group algebra over \(\mathbf Z_p\) with maximal ideal
\[
\mathfrak m=(p,I_E),
\]
truncate at the required precision, and take the stable/projective relation-module jet.

The Fox-Lyndon mechanism supplies the relation-module exact sequence; the relative relation module is intrinsic to the extension, while presentation changes act through invertible Fox Jacobians. Relation-generator changes act by an invertible change of basis. Conjugating the relator multiplies the relation row by a unit. Passing to the projective class removes these gauge factors.

Consequently an isomorphism of extension windows induces an isomorphism of the mixed Fox jet, well-defined up to the already declared projective gauge.

The weighted Magnus estimate established previously supplies the compatibility with the original Zassenhaus precision:
\[
D_{N_k}
\]
is invisible below the target mixed precision, while the first relation contribution is the boundary layer
\[
D_{N_k}/D_{N_k+1}.
\]

### Classification

- extension-window object: **PASS / CLOSED**;
- Demuškin pair → extension-window reconstruction: **PASS / CLOSED at isomorphism-class scope**;
- extension-window → projective mixed Fox jet: **PASS / LOCAL**;
- bare finite-pair → mixed Fox jet, as an isomorphism-invariant assignment: **PASS / LOCAL**;
- full natural transformation on a specified pair-morphism category: **OPEN**;
- Paper 3: **FROZEN / COMPLETE**.

## 4. Consequence

The broad arbitrary-central-extension obstruction is now cleanly separated from the Demuškin-restricted result.

The correct current theorem is not:

> every finite pair determines every extension.

It is:

> in the declared standard odd-p fixed-rank Demuškin family, the particular Zassenhaus extension window needed by the Mixed Fox construction is determined up to isomorphism by the pair \((Q_k,A_k)\).

Therefore the previous “admissibility is merely an undefined escape hatch” objection is discharged at the declared scope.

The remaining load-bearing issue is no longer fiber ambiguity. It is the exact categorical naturality statement for the mixed Fox construction, followed by the independent non-redundancy/novelty question.

## 5. No-go boundary retained

The broad category remains closed:

\[
(Q,A)\not\Rightarrow [E]
\]
for arbitrary finite central extensions.

The examples already audited (power-type versus Heisenberg-type extensions over the same forgotten pair) remain valid as the broad-category boundary. They do not contradict the Demuškin reconstruction lemma because the latter is a restricted-family statement.

## 6. Next authorized action

Do not reopen the fiber search.

The next task is to formalize the projective mixed-Fox construction as a morphism on extension windows and prove its covariance under:
1. extension-window isomorphisms;
2. generator changes / Nielsen transformations;
3. relation-generator gauge;
4. relator conjugation;
5. the mixed maximal-ideal truncation.

Then determine whether this yields a genuine functorial factorization through the declared finite-pair category.

No W_11/W_12 computation, large Fox scan, 45-dimensional computation, or Paper 2 reproof is authorized.
