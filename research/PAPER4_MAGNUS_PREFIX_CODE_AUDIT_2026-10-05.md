# Paper 4 — Magnus prefix-code proof audit — 2026-10-05

## Classification

**SC_s: PASS / CLOSED.**  
**TF_s: PASS / CLOSED as a consequence of SC_s.**  
**a=s versus a=∞ at the critical window: PASS / CLOSED in the declared stress-family scope, after correcting the intrinsic torsion-line formulation.**

This audit records the independent proof and verification of the remaining all-s transfer-defect gate.

## 1. Exact subgroup comparison

Let F be a finitely generated free (pro-p) group and let
\[
\chi:F\twoheadrightarrow C_p
\]
be an index-p character. Choose a free basis
\[
z,x_1,\ldots,x_d,
\qquad \chi(z)=1,\quad \chi(x_i)=0,
\]
and put K=ker(chi).

The target is
\[
D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K).
\tag{SC}
\]

The proof uses the completed Magnus algebras over F_p.

### Schreier coordinates

Use the standard index-p Schreier basis
\[
u=z^p,\qquad y_{j,i}=z^j x_i z^{-j}\quad(0\le j\le p-1),
\]
and write
\[
U=u-1,\qquad Y_{j,i}=y_{j,i}-1.
\]
Then the completed group algebra of the free group K is the completed free associative algebra in the degree-one variables U,Y_{j,i}.

Let sigma denote conjugation by z on the Schreier orbit and
\[
\delta=\sigma-1.
\]
For 0\le k<p define
\[
w_{k,i}=\delta^kY_{0,i}.
\]
The transformation from (Y_{0,i},...,Y_{p-1,i}) to (w_{0,i},...,w_{p-1,i}) is invertible over F_p. Its coefficient matrix is unitriangular in the ordered basis e_0, sigma e_0,...,sigma^{p-1}e_0; equivalently its determinant is 1.

Thus U and all w_{k,i} are again a complete free coordinate system of the completed augmentation algebra. They are **algebra coordinates**, not group generators.

## 2. Initial terms

Put
\[
X_0=z-1,\qquad X_i=x_i-1.
\]
For the convention sigma(a)=zaz^{-1},
\[
\sigma(Y)-Y
=(1+X_0)(1+Y)(1+X_0)^{-1}-(1+Y).
\]
Hence its lowest Magnus-degree part is
\[
[X_0,Y].
\]
With degree-lexicographic order in which X_0 is the largest letter,
\[
\operatorname{in}(w_{k,i})=X_0^kX_i,
\qquad
\operatorname{in}(U)=X_0^p.
\tag{I}
\]
The second identity follows from
\[
(1+X_0)^p-1=X_0^p
\]
in characteristic p.

The local symbolic checks give the coefficient determinants
\[
1\pmod p
\]
for p=3,5,7,11, and verify (I) directly for p=3,5.

## 3. Prefix-code lemma

The set of initial monomials
\[
\mathcal C_p=
\{X_0^kX_i:0\le k<p,\ i\ge1\}
\cup\{X_0^p\}
\]
is prefix-free.

Indeed, every X_0^kX_i ends with a letter X_i\ne X_0, while X_0^p consists entirely of X_0's. Two words of the first type cannot prefix one another because after the common X_0-run one encounters X_i versus either X_0 or a different X_j.

Therefore concatenations of codewords have unique parsing. In particular distinct coordinate words have distinct initial monomials.

This is not merely an experimental observation: exhaustive concatenation tests through coordinate-word length 4 for p=3,5,7 found no collisions, independently confirming the parsing argument.

## 4. Magnus-coordinate lemma

Let f be a nonzero element of the completed augmentation algebra of K, written in the U,w_{k,i} coordinates. Give each coordinate the ambient F-weight
\[
\mathrm{wt}(U)=p,
\qquad
\mathrm{wt}(w_{k,i})=k+1.
\]
For a coordinate word W define d(W) as the sum of its weights.

For every nonzero f,
\[
\operatorname{ord}_F(f)=\min_{c_W\ne0}d(W).
\tag{M}
\]

Proof:
1. The lowest homogeneous part of a product is the product of the lowest homogeneous parts because the completed free associative algebra has no zero divisors at the monomial-leading-term level.
2. By (I), the initial monomial of W is the concatenation of the codewords attached to its coordinates.
3. Prefix-freeness makes those concatenations distinct for distinct coordinate words.
4. Hence, at the minimum weighted degree, no distinct coordinate words can cancel their leading monomials.
5. In every fixed degree there are only finitely many coordinate words (the rank is finite), so completion causes no additional cancellation problem.

Thus (M) is a theorem of the completed Magnus-coordinate algebra, not a finite-degree experimental assertion.

## 5. Deduction of SC

Suppose f=g-1 with 0\ne g\in D_n(F)\cap K. If g had K-order ell<ceil(n/p), choose a nonzero lowest K-word contribution of length ell. Every coordinate has ambient weight at most p, so its weighted degree is at most p ell<n. By (M), ord_F(f)<n, contradiction.

Therefore
\[
\boxed{D_n(F)\cap K\subseteq D_{\lceil n/p\rceil}(K)}
\]
for every n and every index-p kernel K of a free group F.

At
\[
n=p^s+1
\]
this gives exactly
\[
D_{p^s+1}(F)\cap K
\subseteq D_{p^{s-1}+1}(K),
\]
which is (SC_s).

The factor p is sharp: z^{p^s} has F-order p^s, while in K the free coordinate u=z^p gives K-order p^{s-1}.

## 6. Independent computational verification

An independent sparse Magnus implementation over F_3 was used on the concrete index-3 kernel with basis z,x,y.

Verified:
- [z^9,x] has F-order 10 and K-order 4;
- the 9-fold iterated commutator ad_z^9(x) has F-order 10 and K-order 4;
- the triple iterated commutator ad_{z^3}^3(x) has F-order 10 and K-order 4;
- 30 random products/inverses of these D_10(F) witnesses all had K-order at least 4;
- the sharp witness pattern z^{3^s} has ambient/K order ratio 3 at s=1,2,3, and the analogous p=5,s=2 ratio is 5.

These computations are sanity checks; the proof of (SC) is the Magnus-coordinate lemma above.

## 7. TF_s

For
\[
m=p^{s-1}+1,
\]
the Jennings product formula gives
\[
D_m(K)=\prod_{ip^j\ge m}\gamma_i(K)^{p^j}.
\]
After abelianization all gamma_i(K), i>=2, vanish, while the first surviving pure-power exponent is p^s. Hence
\[
\operatorname{im}(D_m(K)\to K^{ab})\subseteq p^sK^{ab}.
\]
Together with (SC_s),
\[
\boxed{
\operatorname{im}(D_{p^s+1}(F)\cap K\to K^{ab})
\subseteq p^sK^{ab}.
}
\tag{TF_s}
\]
Thus TF_s is now PASS / CLOSED, not an independent open lemma.

## 8. N∩K and the stress-family relator

For
\[
G_{s,a}=F/\overline{\langle\!\langle z^{p^s}x_1^{-p^a}r_2^{-1}\rangle\!\rangle},
\]
with a>=1 and r_2 a product of commutators in the x_i, the defining relator has trivial chi-value, so its normal closure R lies in K. Since D_{p^s+1}(F)\subseteq K,
\[
N:=D_{p^s+1}(F)R\subseteq K,
\qquad
N\cap K=N.
\]
Moreover r_2\in[K,K], because all x_i lie in K. Thus r_2 contributes zero in K^{ab}. The abelianized Schreier relation is therefore
\[
p^{s-1}U-p^aA_i=0
\]
(on each conjugate orbit, with the sign depending only on the chosen relator convention). For a=s this is exactly the lattice L_s used in the previous model audits.

For a=∞ the power relation z^{p^s}=r_2 is absent; in K^{ab} the right-hand side is zero, so the U-direction is not subject to the finite p^s relation coming from the stress power.

## 9. Survival of the critical transfer witness

On the a=s side, the model Schreier class
\[
p^{s-1}(\sigma-1)^{p-1}A_0
\]
has order p^s in the untruncated lattice, hence its image modulo p^s is nonzero.

The only possible way the finite-window truncation could kill this class is through the image of D_{p^s+1}(F)\cap K in K^{ab}. But (TF_s) places that entire image inside p^sK^{ab}. Therefore the critical class survives in the finite-window quotient modulo p^s.

The a=∞ side has no corresponding power relation in the U-direction, and the normalized transfer defect is zero in the quotient.

The s=3 model calculation (p=3,s=3) remains an independent local witness and is consistent with this all-s proof.

## 10. Correct intrinsic transfer formulation

The earlier shorthand T=W^{ab}[p^s] was too coarse if interpreted as a single element. In
\[
W^{ab}\cong \mathbf Z/p^s\oplus(\mathbf Z/p^{s+1})^d,
\]
define the canonical one-dimensional subspace
\[
S_s(W):=\operatorname{im}\bigl(W^{ab}[p^s]\to W^{ab}/pW^{ab}\bigr).
\]
This is one-dimensional over F_p in the declared stress-family scope: the p^s-cyclic factor contributes one generator, while the p^{s+1}-factors contribute only p-divisible p^s-torsion and vanish modulo pW^{ab}.

Choose any t\in W^{ab}[p^s] whose image spans S_s(W). The corrected intrinsic predicate is
\[
\varepsilon_s(W):
=
p^{s-1}V(t)
\pmod{p^sK^{ab}}
\in K^{ab}/p^sK^{ab}.
\]
It is well-defined up to multiplication by a unit:
if t is replaced by another lift of the same line, the difference lies in pW^{ab}, hence after applying p^{s-1}V it lies in p^sK^{ab}.

Thus nonvanishing of epsilon_s(W) is independent of the marked lift and isomorphism-invariant, once the cup-radical line defining K is used. This fixes the only genuine gauge ambiguity in the previous transfer formulation.

## 11. Final separation gate

The stress-family cup-radical line is one-dimensional **only in the declared nondegenerate quadratic scope**: d is even and the alternating form defined by r_2 on the x-space is nondegenerate (for example, d=2 and r_2=[x_1,x_2]). In that scope the radical is exactly \(\langle z^*\rangle\), so K is intrinsic.

For W_n with n\ge3, the defining power relation lies in D_3(F), so it does not alter the degree-2 relation class. Hence the same nondegenerate quadratic cup form is visible intrinsically in H^1(W_n,\mathbf F_p) and H^2(W_n,\mathbf F_p), with radical line \(\langle z^*\rangle\).

The corrected \(\varepsilon_s\) is therefore an intrinsic finite-window invariant in this scope.

- a=s: take t=z-x_1. Then V(t)=U-\sum_jA_j, while \(p^{s-1}U=0\) modulo the a=s relation lattice and p^s. Hence
\[
\varepsilon_s(W_{s,s})=-p^{s-1}\sum_jA_j\ne0.
\]
- a=∞: take t=z. Then V(t)=U and \(p^{s-1}U\in\operatorname{im}R\), so
\[
\varepsilon_s(W_{s,\infty})=0.
\]

The separation statement is certified here for **s\ge2**; the s=1 case is intentionally not promoted by this audit.

Hence, for every odd p and s>=2 in the declared stress-family scope,
\[
\boxed{
W_{p^s+1}(G_{s,s})
\not\cong
W_{p^s+1}(G_{s,\infty}).
}
\]

Combined with the already certified lower-window blindness, the exact unmarked separation threshold is
\[
\boxed{n_{\rm sep}(s)=p^s+1}.
\]

## 12. Scope and literature boundary

The standard Magnus embedding and Jennings/Zassenhaus descriptions used here are classical. The web literature check located standard statements of the Magnus embedding and the Zassenhaus/Jennings formulas, but no directly matching index-p subgroup comparison in the form (SC). Therefore the present proof should be treated as an explicit derivation in this setting, not attributed to a previously located theorem.

This does not by itself establish publication-level novelty; a fuller literature audit can be done separately if needed.

## Final classification

- Magnus coordinate change: **PASS / CLOSED**.
- Prefix-code leading-word lemma: **PASS / CLOSED**.
- General (SC): **PASS / CLOSED** for index-p kernels of finitely generated free groups.
- (SC_s): **PASS / CLOSED**.
- (TF_s): **PASS / CLOSED**.
- a=s Schreier critical witness: **PASS / LOCAL -> promoted by TF_s to the declared finite-window conclusion**.
- corrected intrinsic transfer invariant: **PASS / CLOSED in the declared stress-family scope**.
- a=s versus a=∞: **PASS / CLOSED**.
- exact critical boundary threshold n_sep(s)=p^s+1: **PASS / CLOSED** for the declared stress-family scope.
