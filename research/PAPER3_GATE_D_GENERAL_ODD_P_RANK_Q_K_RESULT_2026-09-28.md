# PAPER 3 — Gate D: arbitrary odd p, rank d, q, and k — CORRECTED GENERAL THEOREM

Date: 2026-09-28

## Status

**Gate D finite Kummer selector: PASS / CLOSED** for torsion-free Demushkin pro-p groups of even rank d>=2, odd prime p, Demushkin parameter q in {0,p,p^2,...}, and every k>=2, after replacing the false bare-Q_k H^2-inflation argument by the intrinsic transgression quotient carrier.

The theorem is about the declared finite Kummer selector. It does not assert absolute carrier minimality, nor minimality among all possible finite observations.

## 1. Target and notation

Let G be a torsion-free Demushkin pro-p group, p odd, with even rank d>=2 and parameter q in {0,p,p^2,...}. Let D_\bullet(G) be the Zassenhaus filtration and put
\[
N_k=p^{k-1},\qquad Q_k=W_{N_k+1}=G/D_{N_k+1}.
\]

At level k, after the lower-level candidate \rho_{k-1} has been recovered, candidates are
\[
L_k(\rho_{k-1})
=
\{\rho_k:Q_k\to(\mathbf Z/p^k)^\times:
\rho_k\bmod p^{k-1}=\rho_{k-1}\}.
\]

For \rho_k, the coefficient sequence
\[
0\to\mathbf F_p\to\mathbf Z/p^k(\rho_k)
\to\mathbf Z/p^{k-1}(\rho_{k-1})\to0
\]
defines
\[
\delta_{k,\rho_k}:
H^1(Q_k,\mathbf Z/p^{k-1}(\rho_{k-1}))
\to H^2(Q_k,\mathbf F_p).
\]

The finite selector is:
\[
\boxed{\rho_k\text{ is selected iff }\delta_{k,\rho_k}=0.}
\]

No q, presentation, relator, Fox coordinate, or pre-supplied canonical orientation is part of the selector input.

## 2. D1 — arbitrary odd-p finite-depth factorization

For
\[
A_k=\mathbf Z/p^k,\qquad U_{1,k}=1+p\mathbf Z/p^k,
\]
let
\[
S_k=A_k\rtimes U_{1,k},
\]
with the principal-unit group acting on A_k by multiplication.

For j>=1 put
\[
U_j=1+p^j\mathbf Z/p^k
\]
(with U_j=1 for j>=k) and
\[
T_j=p^{j-1}A_k\rtimes U_j.
\]

For odd p,
\[
P_j(S_k)=T_j\quad(1\le j\le k),
\qquad
P_{k+1}(S_k)=1.
\]

The proof is valuation-theoretic:
- p-th powers send the additive layer p^{j-1}A_k to p^jA_k and U_j onto U_{j+1};
- commutators with U_1 generate exactly p^jA_k;
- the reverse inclusions follow from these two generation statements.

For a crossed cocycle z in
\[
Z^1(G,A_k(\rho)),
\]
the affine map
\[
g\mapsto(z(g),\rho(g))
\]
is a continuous homomorphism G->S_k. Functoriality of the lower p-central series gives
\[
D_{p^{k-1}+1}(G)\longmapsto
P_{p^{k-1}+1}(S_k)=1.
\]
Hence z and rho factor through Q_k.

In particular,
\[
\boxed{
H^1(Q_k,A_k(\bar\rho))
\;\cong\;
H^1(G,A_k(\rho))
}
\]
for every candidate action rho occurring in the selector.

The same factorization statement applies to the lower coefficient module A_{k-1}; because its own depth is p^{k-2}+1, it certainly factors through the larger quotient Q_k.

**Classification: PASS / CLOSED.**

## 3. D2 — corrected finite obstruction carrier

The previous claim
\[
H^2(Q_k,\mathbf F_p)\hookrightarrow H^2(G,\mathbf F_p)
\]
is false and is permanently CLOSED.

Instead define
\[
E_k=W_{N_k+2}=G/D_{N_k+2},
\qquad
K_k=D_{N_k+1}/D_{N_k+2}.
\]
Then
\[
1\to K_k\to E_k\to Q_k\to1
\]
is an intrinsic finite central extension, because
\[
[D_{N_k+1},G]\subseteq D_{N_k+2}.
\]
Moreover K_k is contained in the Frattini subgroup of E_k. Hence
\[
H^1(Q_k,\mathbf F_p)\xrightarrow{\sim}
H^1(E_k,\mathbf F_p).
\]

The five-term Hochschild-Serre sequence gives
\[
\ker\!\left(
H^2(Q_k,\mathbf F_p)\to H^2(E_k,\mathbf F_p)
\right)
=
\operatorname{im}(\operatorname{tra}_k).
\]

Define the intrinsic finite carrier
\[
\boxed{
\mathcal O_k(G)
=
H^2(Q_k,\mathbf F_p)/
\operatorname{im}(\operatorname{tra}_k).
}
\]

This is the corrected carrier. It does not require H^2(Q_k) to inject into global H^2(G).

### 3.1 Canonical branch

For the canonical orientation chi, take any
\[
f\in H^1(Q_k,\mathbf Z/p^{k-1}(\chi_{k-1})).
\]
Inflate f to G. Classical Kummerianity of the canonical Demushkin orientation gives a global lift
\[
z\in H^1(G,\mathbf Z/p^k(\chi_k)).
\]
By D1, z factors through Q_k. Therefore f already lifts on Q_k, so
\[
\delta_{k,\chi_k}(f)=0
\]
in H^2(Q_k,F_p).

Thus
\[
\boxed{\bar\delta_{k,\chi_k}=0:\;
H^1(Q_k,\mathbf Z/p^{k-1}(\chi_{k-1}))
\to\mathcal O_k(G).}
\]

This argument is important: it uses finite factorization of the global lift, not injectivity of finite-to-global H^2 inflation.

### 3.2 False branch

Let
\[
\rho_k'=\chi_k(1+p^{k-1}\nu),
\qquad
0\ne\nu\in H^1(G,\mathbf F_p).
\]

The coefficient-extension calculation gives
\[
\delta_{k,\rho_k'}(f)-\delta_{k,\chi_k}(f)
=
\iota_*(\nu\smile\bar f),
\]
where
\[
\iota:\mathbf F_p\hookrightarrow
\mathbf Z/p^{k-1}(\chi_{k-1})
\]
is the standard inclusion.

Because G is Demushkin, cup product
\[
H^1(G,\mathbf F_p)\times H^1(G,\mathbf F_p)
\to H^2(G,\mathbf F_p)
\]
is a perfect pairing. Choose a with
\[
\nu\smile a\ne0.
\]

Canonical Kummerianity at level k-1 gives the required reduction-surjectivity, so choose
\[
f\in H^1(G,\mathbf Z/p^{k-1}(\chi_{k-1}))
\]
with
\[
\bar f=a.
\]
By D1, f factors through Q_k.

Let
\[
\alpha_k\in H^2(Q_k,\mathbf F_p)
\]
be the finite connecting output for f under rho_k'. Its inflation to H^2(G,F_p) is the nonzero class
\[
\iota_*(\nu\smile a)\ne0.
\]

Now suppose
\[
\alpha_k\in\operatorname{im}(\operatorname{tra}_k).
\]
Every transgression class dies under
\[
H^2(Q_k,\mathbf F_p)\to H^2(E_k,\mathbf F_p),
\]
hence also dies after further inflation to H^2(G,F_p). This contradicts the nonzero global inflation of alpha_k.

Therefore
\[
[\alpha_k]\ne0\in\mathcal O_k(G).
\]

So every false first-order lift produces a nonzero finite obstruction in the corrected carrier.

### 3.3 D2 conclusion

\[
\boxed{
\bar\delta_{k,\rho}=0
\iff
\rho=\chi_G\bmod p^k
}
\]
at the first-order level around the canonical lower-level orientation.

The parameter space is H^1(G,F_p), not Q_4^* or any transgression-dual space. The latter is an output/kernel space.

**Classification: PASS / CLOSED.**

The earlier bare-Q_k H^2-injectivity argument remains **FAIL / CLOSED**.

## 4. D3 — induction to all k

Assume the finite Kummer predicate at level k holds for a candidate rho_k.

D1 transfers the finite cocycle-lifting problem to G. Reduction/descent transfers the predicate to level k-1. By induction,
\[
\rho_{k-1}=\chi_G\bmod p^{k-1}.
\]

Therefore
\[
\rho_k=\chi_k(1+p^{k-1}\nu)
\]
for some
\[
\nu\in H^1(G,\mathbf F_p).
\]

If nu is nonzero, D2 produces a nonzero class in \mathcal O_k(G), contradicting the zero finite Kummer obstruction. Hence nu=0.

Conversely, the canonical orientation is Kummerian, so its finite connecting map is zero by the finite-lift argument in D2.

The base k=2 uses the same argument with the lower coefficient module F_p; no presentation-specific U4 calculation is required for the uniqueness mechanism.

Thus, for every k>=2,
\[
\boxed{
\mathsf K_k(Q_k,\rho)
\iff
\rho=\chi_G\bmod p^k.
}
\]

A crucial non-circularity point is retained:

D2 does NOT require arbitrary-candidate surjectivity
\[
H^1(G,A_k(\rho_k))\to H^1(G,\mathbf F_p).
\]
That would be essentially the Kummer predicate itself.

Only canonical lower-level surjectivity
\[
H^1(G,A_{k-1}(\chi_{k-1}))
\to H^1(G,\mathbf F_p)
\]
is used, and this is supplied by classical Kummerianity.

**Classification: PASS / CLOSED**, conditional only on the standard Demushkin Kummerian theorem and the cochain-level variation identity already audited in the project.

## 5. D4 — exact threshold in the declared selector category

In a standard Demushkin presentation, choose x_2 with
\[
\chi(x_2)=(1-q)^{-1}
\]
for q nonzero, and chi(x_2)=1 for q=0.

Put
\[
N=p^{k-1}.
\]
Choose f with f(x_2)=1 and let z be its canonical Kummer lift.

Then
\[
z(x_2^N)=
\left(\sum_{j=0}^{N-1}\chi(x_2)^j\right)z(x_2).
\]

If q=0,
\[
\sum_{j=0}^{N-1}1=N=p^{k-1}.
\]

If q!=0 and v_p(q)=s>=1, LTE gives
\[
v_p\!\left(
\sum_{j=0}^{N-1}\chi(x_2)^j
\right)
=
v_p(\chi(x_2)^N-1)-v_p(\chi(x_2)-1)
=
s+(k-1)-s
=
k-1.
\]

Hence the canonical Kummer predicate fails on the predecessor quotient G/D_N, while it holds on G/D_{N+1}. Therefore, within the declared standard Zassenhaus-window selector category,
\[
\boxed{
n_k^{\mathrm{Kum}}=p^{k-1}+1.
}
\]

This is uniform in odd p, even rank d>=2, allowed q, and k>=2.

**Classification: PASS / CLOSED in the declared selector category.**

It is not a theorem about arbitrary carriers or arbitrary targets.

## 6. What is now genuinely closed

The repaired general theorem has the following status:

| Component | Status |
|---|---|
| D0 finite selector definition | PASS / CLOSED |
| D1 arbitrary odd-p factorization | PASS / CLOSED |
| bare-Q_k H^2 inflation injectivity | FAIL / CLOSED |
| D2 transgression quotient O_k | PASS / CLOSED |
| D2 canonical finite zero map | PASS / CLOSED |
| D2 false-lift separation in O_k | PASS / CLOSED |
| D3 finite selector uniqueness | PASS / CLOSED |
| D4 exact selector threshold p^(k-1)+1 | PASS / CLOSED |
| absolute carrier minimality | OPEN |
| minimality among arbitrary finite carriers | OPEN |
| uniform-in-q recognition within the declared Demushkin class | PASS / CLOSED |
| publication novelty | OPEN / CONDITIONAL |

The phrase “arbitrary (p,d,q,k)” is now justified for the declared torsion-free Demushkin class with odd p. It is not a theorem for arbitrary pro-p groups.

## 7. Critical logical boundary

The corrected theorem proves a finite intrinsic selector for canonical orientation modulo p^k. It does not prove that O_k is minimal, that Q_k is the smallest possible observation, or that the selector is the only interesting orientation carrier.

Therefore the next frontier is not another generalization of Gate D and not another 45-dimensional computation.

The next frontier is:
\[
\boxed{
W_n(G)\longrightarrow O(G)\longrightarrow T(G)
}
\]
with a specified carrier category, and in particular the universal/minimality question for the transgression quotient O_k.

Publication novelty must be audited separately.

## Final classification

**Gate D: PASS / CLOSED.**

**Corrected D2 carrier mechanism: PASS / CLOSED.**

**D3 finite selector: PASS / CLOSED.**

**D4 selector threshold: PASS / CLOSED.**

**Absolute/functorial carrier minimality: OPEN.**

**Publication novelty: OPEN / CONDITIONAL.**
