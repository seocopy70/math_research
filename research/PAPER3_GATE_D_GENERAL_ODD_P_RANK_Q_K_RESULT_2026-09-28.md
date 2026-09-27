# PAPER 3 — Gate D: arbitrary odd p, rank d, q, and k

Date: 2026-09-28
Status: PASS / CLOSED at the stated Kummer-selector scope

## Target

Extend Gates A–C from the fixed rank-four, p=3, q=3 case to every torsion-free Demushkin pro-p group of even rank d>=2, odd prime p, Demushkin parameter q in {0,p,p^2,...}, and every k>=2.

The target is the declared finite Kummer selector, not an arbitrary finite carrier:
\[
W_{p^{k-1}+1}(G)=G/D_{p^{k-1}+1}(G),
\]
with the intrinsic candidate family and connecting-map selector defined below.

## D0 — finite selector definition

Put N_k=p^{k-1}. For k=2, let rho_1 be the trivial mod-p character and define
\[
\mathcal K_2(W_{p+1},rho_2):
H^1(W_{p+1},\mathbf Z/p^2(rho_2))\to H^1(W_{p+1},\mathbf F_p)
\]
to be surjective. The canonical mod-p^2 character is the unique candidate satisfying this predicate.

Inductively, after rho_{k-1} has been recovered, let
\[
L_k(rho_{k-1})=\{rho_k:W_{N_k+1}\to(\mathbf Z/p^k)^\times:\rho_k\bmod p^{k-1}=rho_{k-1}\}.
\]
For each rho_k the coefficient sequence
\[
0\to\mathbf F_p\to\mathbf Z/p^k(rho_k)\to\mathbf Z/p^{k-1}(rho_{k-1})\to0
\]
defines an intrinsic connecting map
\[
\delta_{k,rho_k}:H^1(W_{N_k+1},\mathbf Z/p^{k-1}(rho_{k-1}))\to H^2(W_{N_k+1},\mathbf F_p).
\]
The selector is the unique rho_k for which the entire map delta_{k,rho_k} is zero.

No q, presentation, relator, Fox coordinate, or pre-supplied canonical orientation enters this definition.

## D1 — factorization survives for arbitrary odd p

For A_k=Z/p^k and U_{1,k}=1+pZ/p^k, form S_k=A_k\rtimes U_{1,k}. Let U_j=1+p^jZ/p^k and
\[
T_j=p^{j-1}A_k\rtimes U_j.
\]
For odd p, the lower p-central series satisfies P_j(S_k)=T_j for 1<=j<=k and P_{k+1}(S_k)=1. The proof is the same valuation argument as U1: p-th powers raise the additive valuation by one and U_j to U_{j+1}; commutators with U_1 generate exactly p^jA_k.

The Zassenhaus identity
\[
D_m(G)=\prod_{i p^r\ge m}P_i(G)^{p^r}
\]
then gives
\[
D_{p^{k-1}+1}(G)\subseteq P_{k+1}(S_k)
\]
under every crossed action G->U_{1,k}. Hence every candidate crossed cocycle factors through W_{p^{k-1}+1}. This is the arbitrary-p version of U1-U2.

The same argument works for the predecessor N_k=p^{k-1} as far as descent of candidate actions is concerned: D_{N_k} maps trivially to U_{1,k} because D_{N_k}(U_{1,k}) is contained in 1+p^kZ/p^k.

## D2 — finite obstruction family is intrinsic

Let Q_k=W_{N_k+1} and N=P_{N_k+1}. Since N is contained in Phi(G), inflation
\[
H^1(Q_k,F_p)->H^1(G,F_p)
\]
is an isomorphism. The five-term Hochschild-Serre sequence makes
\[
H^2(Q_k,F_p)->H^2(G,F_p)
\]
injective. Q_k is a nontrivial finite p-group, hence H^2(Q_k,F_p) is nonzero; Demushkinity gives dim H^2(G,F_p)=1. Thus inflation is an isomorphism.

Together with D1, every coefficient extension and every connecting map at level k is reconstructed from Q_k itself. This is the arbitrary-p,d,k version of Gate B.

## D3 — unique selector

For p odd, any two lifts reducing to rho_{k-1} differ by
\[
rho_k'=rho_k(1+p^{k-1}nu),\qquad nu\in H^1(G,F_p).
\]
The coefficient-extension cochain calculation gives
\[
\delta_{k,rho_k'}-\delta_{k,rho_k}=\iota_*\circ(nu\smile-),
\]
where \(\iota:F_p\hookrightarrow Z/p^{k-1}(rho_{k-1})\) sends 1 to p^{k-2}.

Along the canonical branch, finite-coefficient PD^2 duality makes \iota_* injective on H^2. If two candidates have zero connecting maps, then nu cups every class in H^1(G,F_p) to zero. The Demushkin cup pairing is nondegenerate, so nu=0. Thus the zero map is unique.

The base k=2 uses the same argument with A_1=F_p, so no presentation-specific U4 calculation is needed. Classical Kummerianity supplies existence of the canonical zero map at every level.

Therefore Gates A-C generalize formally once the classical Demushkin PD^2/Kummerian inputs are admitted.

## D4 — sharp Zassenhaus depth for the selector

Let a=chi(x_2) in a standard Demushkin presentation, so a=(1-q)^(-1), with q=0 interpreted as a=1. Let N=p^{k-1} and choose f in H^1(G,F_p) with f(x_2)=1. Kummerianity gives a lift z with z(x_2) congruent 1 mod p. Then
\[
z(x_2^N)=S_Nz(x_2),\qquad S_N=\sum_{j=0}^{N-1}a^j.
\]
If q=0, S_N=N=p^{k-1}. If q is nonzero, v_p(q)=f>=1 and LTE gives
\[
v_p(S_N)=v_p(a^N-1)-v_p(a-1)=f+(k-1)-f=k-1.
\]
Thus z(x_2^N) is nonzero mod p^k. Since x_2^N lies in D_N(G), the canonical Kummer predicate fails on the preceding window G/D_N. The canonical action itself descends to G/D_N by the image filtration of the principal-unit target.

Hence, among the standard Zassenhaus windows for this selector,
\[
\boxed{n_k^{Kum}=p^{k-1}+1}
\]
for every odd p, every even rank d>=2, every allowed q, and every k>=2.

## Independent verification

The extension-difference formula is cochain-level and independent of presentation. The semidirect filtration was checked symbolically from valuation estimates; the threshold witness is reduced to the all-k LTE calculation above. No finite numerical scan is used as a proof.

## Logical boundary

This does NOT prove absolute minimality among arbitrary finite carriers. It does NOT prove that p^{k-1}+1 is the recognition depth of every possible target. It proves the exact depth of the declared finite Kummer selector. Publication novelty remains separate and conditional on literature comparison.

## Classification

- D0 definition: PASS / CLOSED
- D1 arbitrary-p factorization: PASS / CLOSED
- D2 finite delta-family factorization: PASS / CLOSED
- D3 unique finite-level selector: PASS / CLOSED, using classical Demushkin PD^2 and Kummerian existence
- D4 sharp Zassenhaus threshold: PASS / CLOSED for the declared Kummer selector
- absolute carrier minimality: OPEN / NOT CLAIMED
- publication novelty: OPEN / CONDITIONAL

## Consequence

The fixed (p,d,q) calculation is not the essential source of the finite-selector theorem. The formal mechanism is odd-p semidirect filtration + finite-group cohomology + Demushkin PD^2 + Kummerian existence. The remaining Paper 3 frontier is therefore no longer the generalization of this selector; it is the richer-carrier problem
\[
W_n(G)\to O(G)\to T(G),
\]
where O contains finite filtered relation information not reducible to the already-understood Kummer selector, and the admissible carrier category is explicit.
