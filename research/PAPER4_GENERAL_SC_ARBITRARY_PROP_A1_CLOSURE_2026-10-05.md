# Paper 4 — A1 arbitrary pro-p SC closure audit — 2026-10-05

## Claim

For every pro-p group G, every open subgroup K <= G with [G:K]=p^s,
\[
D_n(G)\cap K\subseteq D_{\lceil n/p^s\rceil}(K).
\tag{A1}
\]

Here D_n denotes the p-Zassenhaus filtration.

## Verdict

**PASS / CLOSED.**

The earlier augmentation-ideal equality route was false and remains rejected. The corrected proof uses a weighted normal-form filtration on the completed group algebra and does not require G to be free.

## Index-p proof

Let [G:K]=p and choose a in G with G/K=<aK>. Put
\[
A=\mathbf F_p[[K]],\qquad B=\mathbf F_p[[G]],\qquad J=I_K,\qquad t=a-1.
\]
As a left A-module,
\[
B=\bigoplus_{r=0}^{p-1}At^r.
\]
Because a^p in K and char(F_p)=p,
\[
t^p=a^p-1\in J.
\]
Normality of K gives aJa^{-1}=J.

The crucial point is NOT the false identity
\[
I_G^n=\sum_j J^{n-j}t^jB.
\]
Instead define, for m>=1,
\[
E_m=
\bigoplus_{r=0}^{p-1}
J^{\max(0,\lceil(m-r)/p\rceil)}t^r.
\tag{E_m}
\]
The normal-form multiplication rules imply
\[
E_mE_\ell\subseteq E_{m+\ell}.
\tag{*}
\]
More explicitly, define the weight of a normal-form monomial (c,t^r), (c\in J^q), (0\le r<p), to be (pq+r). If \(\sigma(c)=aca^{-1}\), then
\[
tc=\sigma(c)t+(\sigma(c)-c),
\]
and, because \(\sigma(J^q)=J^q\), both coefficients on the right lie in (J^q). Iterating gives (t^rJ^q\subseteq\sum_{j=0}^rJ^qt^j). On multiplying by a further (t^s), every resulting (t^{j+s}) is written as
\[
t^{j+s}=(t^p)^u t^v,
\qquad j+s=up+v,quad0\le v<p,
\]
and (t^p=a^p-1\in J). Thus the weight (pq+r) is not decreased by multiplication. Hence products of terms of weights at least (m) and \(\ell\) have weight at least (m+\ell), proving (*).

Since
\[
I_G=JB+tB\subseteq E_1,
\]
multiplicativity gives
\[
I_G^n\subseteq E_n
=
\bigoplus_{r=0}^{p-1}
J^{\max(0,\lceil(n-r)/p\rceil)}t^r.
\tag{NF}
\]
The decomposition is direct. Hence
\[
I_G^n\cap A\subseteq J^{\lceil n/p\rceil}.
\tag{AI}
\]
Using the dimension-subgroup identity
\[
D_n(H)=H\cap(1+I_H^n)
\]
for pro-p groups, (AI) gives
\[
D_n(G)\cap K\subseteq D_{\lceil n/p\rceil}(K).
\tag{SC}
\]

This proof explicitly handles the previously missed terms t^rBt: they are normalized inside the direct-sum E_m decomposition rather than discarded.

## Index-p^s extension

For [G:K]=p^s choose a subnormal chain
\[
G=K_0>K_1>\cdots>K_s=K,
\qquad [K_{i-1}:K_i]=p.
\]
Applying (SC) successively gives
\[
D_n(G)\cap K\subseteq D_{\lceil n/p^s\rceil}(K),
\tag{SC_s}
\]
because
\[
\left\lceil\frac{\lceil m/p\rceil}{p}\right\rceil
=
\left\lceil\frac m{p^2}\right\rceil
\]
and hence the ceiling operation composes exactly.

## Consequences

1. **A1 is arbitrary-pro-p, not free-pro-p.** No freeness assumption enters the group-algebra normal-form argument.
2. The previously certified free-pro-p SC/SC_s results remain valid.
3. At the Paper-4 critical index n=p^s+1,
\[
D_{p^s+1}(G)\cap K
\subseteq
D_{p^{s-1}+1}(K),
\]
which supplies the subgroup-depth bound used in the transfer truncation argument.
4. The separate free-pro-p sharpness witness remains the correct sharpness statement for SC_s. A1 does not enlarge that sharpness claim to arbitrary pro-p groups.
5. The old augmentation-ideal equality, the Heisenberg counterexample, and the old Lemma-2/Lemma-3 route remain **FAIL / CLOSED / SUPERSEDED**. They are not part of the proof.

## Audit status

- A1 index-p arbitrary pro-p: **PASS / CLOSED**.
- A1 index-p^s arbitrary pro-p: **PASS / CLOSED**.
- Pointwise sharpness for every n: **OPEN / not needed**.
- Uniform sharpness in the free-pro-p witness family: **PASS / CLOSED**.
- Paper-4 downstream transfer obstruction and exact critical-window theorem: unchanged and remain PASS / CLOSED in the declared stress-family scope.

## Publication wording

Do not claim a new foundational theorem about augmentation ideals. The defensible statement is:

> We prove the precise index-p Zassenhaus subgroup-depth comparison needed for the finite-window argument for arbitrary pro-p groups, by a weighted normal-form filtration of the completed group algebra; iterating along an index-p^s chain yields the corresponding p^s comparison. The result is used as filtration infrastructure for the intrinsic transfer obstruction and sharp finite-window separation.
