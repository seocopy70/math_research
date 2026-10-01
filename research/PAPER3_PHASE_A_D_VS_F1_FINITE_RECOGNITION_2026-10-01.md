# PAPER 3 — PHASE A: D vs F1 FINITE-WINDOW RECOGNITION

Date: 2026-10-01
Status: **PASS / CLOSED at the declared fixed-pair category; novelty remains OPEN / CONDITIONAL**

## 1. Target and category

Fix an odd prime p, rank parameter d>=2, and p-power q=p^f (f>=1). Let C_{p,d,q} be the two-family test category consisting of:

- D_{d,q}: the ordinary Demushkin group
  \[
  \langle x_1,y_1,\ldots,x_d,y_d\mid x_1^q[x_1,y_1]\cdots[x_d,y_d]=1\rangle_{\hat p},
  \]
- F1_{d,q}: the Blumer–Quadrelli F1 group
  \[
  \langle x_1,y_1,\ldots,x_d,y_d\mid [x_1^q,y_1][x_2,y_2]\cdots[x_d,y_d]=1\rangle_{\hat p}.
  \]

Target:
\[
T_{\rm cyc}(G)=\begin{cases}1,&G\text{ admits a 1-cyclotomic orientation},\\0,&\text{otherwise.}\end{cases}
\]

For the concrete Phase-A instance, (p,d,q)=(3,2,3).

The finite observation is the unmarked Zassenhaus window
\[
W_n(G)=(G/D_n(G),D_1/D_n,\ldots,D_{n-1}/D_n).
\]

## 2. Pre-check

### Object
W_n as the actual truncated filtered group, not merely its graded vector spaces.

### Input
Only the intrinsic filtered quotient and its induced commutator map; q is not inserted into the detector.

### Functoriality
A filtered-group isomorphism W_n(G)\cong W_n(H) preserves the commutator map
\[
\kappa:\bigwedge^2(G/D_2)\to D_2/D_n.
\]
For n=3, its rank/type is therefore an intrinsic window invariant.

### Gauge
No presentation or chosen lift is used in the detector. The relevant invariant is the isomorphism class of the alternating commutator pairing.

### Orientation bridge
The global target is 1-cyclotomicity. The literature establishes that ordinary Demushkin groups admit the canonical 1-cyclotomic orientation, while every F1 group is not 1-cyclotomic.

### q-blindness
The degree-2 initial form used below is independent of q in both families. No q is supplied to the finite detector.

### Separation
D and F1 have the same abelianization window W_2 but different W_3 commutator-pairing rank.

### Stop test
All five mandatory structural items are defined before calculation; execution is authorized.

## 3. W_2: no separation

Both defining relators lie in the Frattini subgroup. Hence
\[
D_2(G)=\Phi(G)
\]
for these finitely generated pro-p groups, and both D_{d,q} and F1_{d,q} have the same minimal-generator rank 2d. Therefore
\[
W_2(D_{d,q})\cong W_2(F1_{d,q})\cong (\mathbf F_p)^{2d}
\]
with the abelian filtered structure.

Thus r_{T_cyc}>=3 for the two-object category.

## 4. W_3: intrinsic separation

For odd p, the degree-2 initial form of the ordinary Demushkin relation is
\[
R_D^{(2)}=[X_1,Y_1]+\cdots+[X_d,Y_d].
\]
For F1, the term [x_1^q,y_1] has Zassenhaus degree q+1>=3, so the degree-2 initial form is
\[
R_{F1}^{(2)}=[X_2,Y_2]+\cdots+[X_d,Y_d].
\]

The induced cup/commutator alternating form therefore has ranks
\[
\operatorname{rank}(B_D)=2d,
\qquad
\operatorname{rank}(B_{F1})=2d-2.
\]
Equivalently, the quadratic relation line is nondegenerate in the Demushkin case and has a 2-dimensional radical in F1.

Rank of an alternating pairing is invariant under filtered-window isomorphism. Hence
\[
W_3(D_{d,q})\not\cong W_3(F1_{d,q}).
\]
For Phase A, d=2 gives ranks 4 and 2 respectively.

An independent exact matrix check at (p,d,q)=(3,2,3) gives ranks 4 and 2 for the two 4x4 alternating matrices.

## 5. Recognition conclusion

Since the category contains only the two declared isomorphism types and W_3 separates them,
\[
\boxed{r_{T_{\rm cyc}}(C_{3,2,3};D_\bullet)=3.}
\]
Moreover the same argument gives the uniform pairwise statement
\[
\boxed{r_{T_{\rm cyc}}(C_{p,d,q};D_\bullet)=3}
\]
for odd p, d>=2 and q=p^f, provided C_{p,d,q} means exactly the two-family test category {D_{d,q},F1_{d,q}}.

The threshold is q-blind: the detector sees only the degree-2 commutator structure.

## 6. What this proves — and what it does not

It proves a genuine finite-window recognition statement for the declared two-family category: the known global 1-cyclotomic/non-1-cyclotomic distinction is already visible intrinsically at W_3, and W_2 is insufficient.

It does **not** prove that W_3 recognizes 1-cyclotomicity on a larger category of arbitrary pro-p groups, nor that W_3 detects all F1 groups internally (within F1 the target is constant false), nor that q is recognized. It also does not establish a new converse to Blumer–Quadrelli's theorem.

## 7. Novelty audit boundary

The mathematical mechanism is already implicit in the published structural data: the ordinary Demushkin degree-2 symplectic relation and the F1 degree-2 relation omitting the first pair are explicit in the literature. Therefore the numerical threshold r=3 is a derived finite-window reformulation, not presently a priority claim.

The result becomes research-significant only if the mechanism yields a nontrivial extension: a larger admissible category, a sharp threshold not visible from the presentation, a genuine obstruction/no-go theorem, or a reusable carrier that survives beyond this two-family pair.

## 8. Promotion decision

- Phase A fixed pair: **PASS / CLOSED**.
- Uniform D-vs-F1 pairwise theorem: **PASS / CLOSED** as a direct structural extension.
- New-paper novelty from this result alone: **OPEN / CONDITIONAL; currently weak**.
- Next authorized direction: test whether the same intrinsic W_3 carrier recognizes a broader class containing multiple 1-cyclotomic and non-1-cyclotomic families, without hard-coding family membership or q.
