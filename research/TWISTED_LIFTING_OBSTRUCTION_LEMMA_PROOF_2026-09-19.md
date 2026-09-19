# TWISTED LIFTING OBSTRUCTION LEMMA — PROOF ATTEMPT / 2026-09-19

This is the proof-level continuation authorized by the structural audit created immediately before this file.

## 1. The coboundary issue is resolved by the coefficient exact sequence

Let
\[
A_2=\mathbf Z/9
\]
with G-action through
\[
\rho:G\to1+3\mathbf F_3,
\]
and let A_1=\mathbf F_3 be the trivial module.

There is a G-equivariant short exact sequence
\[
0\longrightarrow 3A_2\longrightarrow A_2\longrightarrow A_1\longrightarrow0.
\]
Since rho(g) is congruent to 1 modulo 3, the kernel 3A_2 is isomorphic to the trivial module F_3.

The long exact cohomology sequence contains
\[
H^1(G,A_2)\longrightarrow H^1(G,A_1)
\xrightarrow{\delta_\rho}
H^2(G,\mathbf F_3).
\]

Hence the reduction map is surjective iff
\[
\delta_\rho=0.
\]

This automatically quotients by twisted principal derivations. No separate coboundary analysis is required.

Because the action on A_1 is trivial, H^1(G,A_1) is identified with V^* via generator values in a minimal one-relator presentation.

## 2. Relator formula for the connecting map

Let F be the free pro-3 group on the minimal generators, with G=F/<r>. Choose a lift of a mod-3 cocycle f to a crossed homomorphism on F. Under the standard one-relator transgression identification
\[
H^2(G,\mathbf F_3)\cong\mathbf F_3,
\]
the connecting class is represented by the lifted relator obstruction
\[
\widetilde f(r)/3\pmod3.
\]

Changing the lift changes only the representative in the standard coboundary fashion, so the resulting H^2 class is well-defined. Therefore
\[
\delta_\rho(f)=0
\quad\Longleftrightarrow\quad
\widetilde f(r)/3\equiv0\pmod3.
\]

This is the rigorous cohomological form of the relator-obstruction calculation.

## 3. Degree-(2,3) truncation

Write the relation expansion as
\[
r=(R,P)+O(4),
\]
where R is the degree-2 Lie component and P is the degree-3 restricted/power component relevant modulo 9.

Write
\[
\rho(x_i)=1+3a_i,
\qquad
\lambda=\sum_i a_i e_i^*.
\]

Use the crossed-homomorphism rule
\[
z(uv)=z(u)+\rho(u)z(v)
\]
and the fixed commutator convention
\[
[x,y]=x^{-1}y^{-1}xy.
\]

The first nonzero term of z(r)/3 modulo 3 has two sources:

1. the degree-3 restricted-power part, contributing f(p(P));

2. the degree-2 commutator part, where the first-order deformation of the coefficient action contributes the bilinear term (lambda wedge f)(R).

Terms of filtered degree at least 4 are expected to vanish after division by 3 modulo 3 because they contain either too many augmentation factors or an extra factor of 3.

Thus the target formula is
\[
\boxed{
\delta_\rho(f)
=
\bigl[f(p(P))+(\lambda\wedge f)(R)\bigr]\omega
}
\]
for a chosen generator omega of H^2.

## 4. Frozen rank-4 verification

For
\[
r_3=x_1^3[x_1,x_2][x_3,x_4],
\]
we have
\[
R=[X_1,X_2]+[X_3,X_4],
\qquad
p(P)=X_1^{(1)}.
\]

Hence
\[
\delta_\rho(f)/\omega
=
f_1+(\lambda\wedge f)(R)
=
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]

Therefore delta_rho is zero exactly when
\[
a_1=a_3=a_4=0,
\qquad
a_2=1.
\]

Thus the twisted-surjectivity condition recovers
\[
\rho=(1,4,1,1)\pmod9.
\]

This recovery criterion does not use the earlier Bockstein argument.

## 5. Current proof status

A. Cohomological obstruction bridge: PASS / CLOSED at the standard one-relator resolution level.

B. Degree-(2,3) truncation: STRONG PROGRESS, not yet CLOSED. The filtration estimate proving that all degree >=4 contributions vanish must be written explicitly.

C. Presentation/gauge naturality: OPEN. The coordinate-free formula is not by itself a proof that the carrier transforms naturally under every allowed change of generators and relator representative.

D. General Demushkin orientation characterization: SUPPORTED BY LITERATURE, but the exact theorem and hypotheses must be cited in the final manuscript.

## Stop rule

No broad scan. The next work is the explicit filtration estimate for B, followed by the naturality proof for C.