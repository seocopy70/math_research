# Paper 5 Gate 1 — p^k-power/kernel audit (2026-10-06)

## Verdict

**FAIL / CLOSED as submitted.** The proposed Gate 1 identity
[
K_k:=RD_{p^{k-1}+1}/RD_{p^k+1}=W_{p^k}^{p^k}
]
is not established, and the subsequent claims (K_k\cong\mathbf F_p), centrality, and the +3 IA recursion cannot be inferred from the present hypotheses.

This is a load-bearing correction, not a rejection of the strict-denominator theorem.

## Decisive obstruction 1: the (k=1) boundary already contradicts the proposed (A_k\cong\mathbf F_p)

At (k=1), the proposed kernel is
[
RD_2/RD_{p+1}=D_2/(RD_{p+1}),
]
because (R\subseteq D_2). The already closed (n=p) theorem gives
[
D_p(W_p)\cong\mathbf F_p^3
]
with generators (x^p,y^p,z^p). Thus the first kernel in the chain to (W_1=F/D_2\cong\mathbf F_p^3) is not justified as one-dimensional; in the actual boundary model the surviving (p)-power layer is three-dimensional.

Therefore the assertion
[
A_k=RD_{p^{k-1}+1}/RD_{p^k+1}\cong\mathbf F_p
]
is already false if (k=1) is included.

## Decisive obstruction 2: (D_{p^k+1}(W_{p^k})=1) does not imply the kernel is central

The kernel lies at filtration depth (p^{k-1}+1):
[
K_k=D_{p^{k-1}+1}(W_{p^k})
]
only if the corresponding image equality is established. From (D_{p^k+1}(W_{p^k})=1) one gets that the filtration terminates at the next level, not that (D_{p^{k-1}+1}) is central.

For (u\in D_{p^{k-1}+1}) and (g\in W_{p^k}),
[
[u,g]\in D_{p^{k-1}+2},
]
and (p^{k-1}+2<p^k+1) for odd (p) and (k\ge2). Hence the commutator is not forced to vanish. The centrality step in Gate 3 is therefore invalid.

The standard Zassenhaus facts used here are that (D_n/D_{n+1}) is elementary abelian and ([D_i,D_j]\subseteq D_{i+j}), (D_i^p\subseteq D_{pi}); they do not make an arbitrary multi-layer quotient (D_m/D_N) central. citeturn0search12turn0search13

## Decisive obstruction 3: the quotient (D_{p^{k-1}+1}/D_{p^k+1}) contains many graded layers

Jennings–Lazard gives
[
D_n(F)=\prod_{ip^j\ge n}\gamma_i(F)^{p^j},
]
and the associated graded object is a restricted Lie algebra, with independent (p)-power layers as well as brackets. Thus a quotient spanning all degrees
[
p^{k-1}+1,ldots,p^k
]
cannot be identified with a single (p^k)-power line without an additional theorem killing every other layer modulo (R). No such theorem is currently available. citeturn0search12turn0search14

In particular, the statement “the (R)-contribution is deeper, so only (F^{p^k}) remains” is exactly the missing comparison; (R\subseteq D_2) by itself does not imply that (R) absorbs all commutator and restricted-power layers in the entire interval.

## What survives

The following remains valid and is independent of the rejected Gate 1 identity:

- for every (k\ge1),
[
RD_{p^k+1}\subsetneq RD_{p^{k-1}+1},
]
using the established (phi:F\to\mathbf Z_p) witness;
- hence
[
W_{p^k}\twoheadrightarrow W_{p^{k-1}}
]
is a strict canonical epimorphism;
- (W_n/\Phi(W_n)\cong\mathbf F_p^3) remains closed under (R\subseteq\Phi(F));
- the arbitrary-(n) Frattini image (G_{p^k}), descent of automorphisms, and IA growth remain independent open problems.

## Consequence for the proposed domino

Gate 1 does **not** close. Therefore do not promote:

1. characteristicity of (K_k);
2. a canonical map (operatorname{Aut}(W_{p^k})\tooperatorname{Aut}(W_{p^{k-1}}));
3. (G_{p^k}=G_p);
4. (0\to\operatorname{Hom}(V,\mathbf F_p)\to K_{p^k}\to K_{p^{k-1}}\to1);
5. (|K_{p^k}|=p^{3k+C});
6. (operatorname{Aut}(W_{p^k})=K_{p^k}\rtimes G_p).

## Authorized next question

The correct next gate is not “prove the verbal equality” but:

> Determine the actual structure of
> [
> RD_{p^{k-1}+1}/RD_{p^k+1}
> ]
> modulo the explicit relation subgroup (R): its graded dimensions, commutator structure, and (p)-power map.

Only after that calculation can one ask whether a characteristic sublayer exists. A plausible replacement target is a canonical characteristic **top (p^k)-power layer**
[
D_{p^k}(W_{p^k})
]
or its image/annihilator, rather than the entire kernel (K_k).

Classification:
- Gate 1 equality (W_{p^k}^{p^k}=K_k): **FAIL / CLOSED as submitted**;
- (K_k\cong\mathbf F_p): **FAIL / CLOSED as submitted**;
- (K_k) central: **FAIL / CLOSED as submitted**;
- strict denominator chain: **PASS / CLOSED / GENERAL**;
- arbitrary-n Frattini-image structure: **OPEN / LOAD-BEARING**.
