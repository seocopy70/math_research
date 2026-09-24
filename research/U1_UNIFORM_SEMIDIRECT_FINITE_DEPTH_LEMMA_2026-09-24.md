# U1 — Uniform finite-depth semidirect-product lemma — 2026-09-24

## Statement

Let
[
A_k=\mathbf Z/3^k
]
(additively), (U_1=1+3A_k), (U_j=1+3^jA_k) for (jge1), with (U_j=1) for (jge k). Put
[
S_k=A_k\rtimes U_1,
]
where (uin U_1) acts on (A_k) by multiplication.

Let (P_1(S_k)=S_k) and
[
P_{j+1}(S_k)=P_j(S_k)^3[P_j(S_k),S_k]
]
be the lower 3-central series. Define
[
T_j=3^{j-1}A_k\rtimes U_j.
]

## Proof

### 1. Cube

For ((a,u)in S_k),
[
(a,u)^3=((1+u+u^2)a,u^3).
]

If (uin U_j), then (u=1+3^jt), hence
[
1+u+u^2=3+3^{j+1}t+3^{2j}t^2in3A_k.
]
Therefore
[
T_j^3subseteq 3^jA_k\rtimes U_j^3.
]

For (1le j<k),
[
U_j^3=U_{j+1}.
]
The inclusion (U_j^3subseteq U_{j+1}) is immediate from the binomial expansion. Surjectivity follows by 3-adic digit lifting: for (1+3^{j+1}bin U_{j+1}), choose the successive base-3 digits of (a) in (u=1+3^ja) so that (u^3) agrees with the prescribed element modulo (3^{j+2},3^{j+3},ldots,3^k). The linear term is (3^{j+1}a), with unit coefficient on each successive digit because (3) is odd.

### 2. Commutators

A direct multiplication in (A_k\rtimes U_1) shows that the commutator of an element of (T_j) with an arbitrary element of (S_k) has trivial (U_1)-component and additive component divisible by (3^j). Indeed, the two possible valuation contributions are
[
(u-1)b,qquad (v-1)a,
]
with (u-1in3^jA_k, v-1in3A_k, ain3^{j-1}A_k). Thus
[
[T_j,S_k]subseteq3^jA_k.
]

Conversely, take (ain3^{j-1}A_k) and (v=4in U_1). With the convention ([x,y]=x^{-1}y^{-1}xy),
[
[(a,1),(0,4)]=((4^{-1}-1)a,1).
]
Since
[
4^{-1}-1=-3/4
]
is (3) times a unit modulo (3^k), these commutators generate all of (3^jA_k). Hence
[
[T_j,S_k]=3^jA_k
]
for (j<k).

### 3. Induction

Since (P_1(S_k)=S_k=T_1), suppose (P_j(S_k)=T_j). Then
[
P_{j+1}(S_k)=T_j^3[T_j,S_k]
subseteq3^jA_k\rtimes U_{j+1}=T_{j+1}.
]

The reverse inclusion follows from the two generation facts:
[
U_{j+1}=U_j^3subseteq P_{j+1}(S_k),
qquad
3^jA_k=[T_j,S_k]subseteq P_{j+1}(S_k).
]
Therefore
[
oxed{P_j(S_k)=3^{j-1}A_k\rtimes U_j}
]
for all (j).

At the boundary,
[
T_{k+1}=3^kA_k\rtimes U_{k+1}=1,
]
so
[
oxed{P_{k+1}(S_k)=1}.
]

## Consequence: finite-window factorization

Let (G) be any pro-3 group, let (ho:G	o U_1) be a character, and let
[
zin Z^1(G,A_k(\rho)).
]
Then
[
psi(g)=(z(g),ho(g))
]
is a continuous homomorphism (G	o S_k). Functoriality of the lower 3-central series gives
[
psi(P_{k+1}(G))subseteq P_{k+1}(S_k)=1.
]
Hence
[
z(P_{k+1}(G))=0,qquad ho(P_{k+1}(G))=1.
]

Thus every crossed cocycle factors through
[
Q_k=G/P_{k+1}(G).
]
The same holds for coboundaries, so inflation induces the canonical isomorphism
[
oxed{
H^1(Q_k,A_k(\bar\rho))
\cong
H^1(G,A_k(\rho)).
}
]

## Classification

**U1: PASS / CLOSED**, subject only to routine presentation cleanup.

This replaces the longer generator-by-generator valuation proof as the preferred uniform factorization proof. The valuation mechanism remains a valid corollary.

## Boundary

U1 proves finite-depth factorization of the crossed-cocycle problem. It does **not** prove:
- intrinsic/presentation-free selection of (ho_k);
- q-blindness of the selector beyond the declared input category;
- novelty of the finite-window formulation.

Next gate: U3/U4 — finite predicate equivalence and all-k uniqueness, with the corrected inverse coefficient (2+ho(x_2)^{-1}), not the erroneous (4-r_{k-1}) recurrence.
