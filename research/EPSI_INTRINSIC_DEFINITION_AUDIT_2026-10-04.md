# E_psi intrinsic-definition audit — 2026-10-04

## Status

**E_psi branch: OPEN / ACTIVE.**

This document replaces the earlier informal phrase “twisted Fox derivative vanishes” by the mathematically sharper affine test datum. The finite group is not, by itself, the invariant; the invariant is a finite affine representation together with its twisted Fox evaluation ideal.

## 1. Ambient setup

Let (p) be odd, (s\ge1), and let (F=F(x_1,\ldots,x_d)) be a free pro-(p) group. Let
[
r\in D_2(F)\setminus D_3(F),
qquad
G_s(r)=F*\langle z\rangle/\overline{\langle\!\langle z^{p^s}r^{-1}\rangle\!\rangle}.
]

Put
[
A_s=\mathbf Z/p^{s+1}\mathbf Z,
qquad
U_s=1+pA_s\subset A_s^\times.
]
Let (U_s) act on the additive group (A_s) by multiplication and define the finite affine (p)-group
[
E_s=A_s\rtimes U_s,
qquad
(a,u)(b,v)=(a+ub,uv).
]

For a continuous character
[
\psi:F\to U_s
]
and a continuous (1)-cocycle/crossed homomorphism
[
\delta:F\to A_s,
qquad
\delta(gh)=\delta(g)+\psi(g)\delta(h),
]
the map
[
\rho_{\psi,\delta}(g)=(\delta(g),\psi(g))
]
is a continuous homomorphism (F\to E_s).

Because (F) is free, (delta) is arbitrary on the free generators.

## 2. Twisted Fox evaluation

For (w\in F),
[
\delta(w)
=
\sum_{i=1}^d
\psi\!\left(\frac{\partial w}{\partial x_i}\right)
\delta(x_i),
]
where the coefficient map is the ring homomorphism
[
\mathbf Z_p[[F]]\to A_s,
qquad
g\mapsto\psi(g).
]

Define
[
J_{\psi,i}(r)
=
\psi\!\left(\frac{\partial r}{\partial x_i}\right)\in A_s,
]
and the intrinsic evaluation ideal
[
I_{\psi}(r)
=
\sum_i A_s J_{\psi,i}(r)
=
\{\delta(r):\delta\in Z^1(F,A_{s,\psi})\}.
]

This (I_\psi(r)), not an individual derivative coordinate, is the first canonical candidate.

### Critical affine test condition

The relation (z^{p^s}=r) can be represented by sending
[
z\mapsto(1,1)\in E_s
]
and (F\) through (\rho_{\psi,\delta}) exactly when
[
\psi(r)=1,
qquad
\delta(r)=p^s\pmod {p^{s+1}}.
]

Equivalently,
[
\psi(r)=1,
qquad
p^s\in I_\psi(r).
]

The condition “twisted Fox derivative (=0)” is therefore **not** the right separator. Zero is the kernel condition for a relation in an affine extension; our power relation requires the nonzero critical translation (p^s).

## 3. Gauge invariance

If (delta) is replaced by the affine-conjugate cocycle
[
\delta_c(g)=\delta(g)+c(1-\psi(g)),
]
then
[
\delta_c(r)=\delta(r)+c(1-\psi(r)).
]
Hence, whenever (\psi(r)=1),
[
\delta_c(r)=\delta(r).
]

More generally, conjugating the affine target by a unit rescales (p^s) by a unit. Thus the invariant statement is valuation-theoretic:
[
v_p(\delta(r))=s,
]
or equivalently (I_\psi(r)=p^sA_s) or a larger ideal containing (p^sA_s).

For a relator conjugate (grg^{-1}), if (\psi(r)=1),
[
\delta(grg^{-1})=\psi(g)\delta(r),
]
so the valuation/ideal is unchanged.

**Gauge: PASS.**

## 4. Functoriality / presentation change

For an admissible free-group automorphism (\alpha), transport
[
r' = \alpha(r),
qquad
\psi'=\psi\circ\alpha^{-1},
qquad
\delta'=\delta\circ\alpha^{-1}.
]
Then
[
\delta'(r')=\delta(r).
]

The Fox-Jacobian chain rule gives the corresponding coordinate transformation of the vector
[
(J_{\psi,1}(r),\ldots,J_{\psi,d}(r)),
]
while its generated (A_s)-submodule (I_\psi(r)) is unchanged.

Thus individual Fox coordinates are presentation-dependent, but the evaluation ideal and the existence of a critical affine lift are functorial.

**Functoriality: PASS in the marked free-presentation category.**

## 5. q-blindness

The finite target
[
E_s=A_s\rtimes U_s
]
is defined from the window index (s) alone. It does not contain the unknown exponent (q=p^s) as an input parameter to the relation test.

The comparison exponent is recovered from the distinguished translation:
[
(1,1)^{p^s}=(p^s,1)\ne1,
qquad
(1,1)^{p^{s+1}}=1.
]

Thus the construction is **window-indexed, not q-encoded**.

**q-blindness: PASS.**

## 6. Zassenhaus depth of the affine target

Write (A=A_s), (U=U_s). Then
[
[E_s,E_s]=pA,
]
and, for (i\ge2),
[
\gamma_i(E_s)=p^{i-1}A
]
until the right side becomes zero.

Using Lazard's formula
[
D_n(E_s)=
\prod_{ip^j\ge n}\gamma_i(E_s)^{p^j},
]
one obtains
[
D_{p^s}(E_s)=p^sA\ne0,
qquad
D_{p^s+1}(E_s)=1.
]

The second identity is the critical point: for (i\ge2), the condition (ip^j\ge p^s+1) forces enough (p)-powering that
[
\gamma_i(E_s)^{p^j}=1,
]
while the (i=1) factor requires (p^{s+1})-powering.

This makes (E_s) an exact finite detector for the (p^s\leftrightarrow p^s+1) boundary.

## 7. Critical affine lift for every nonzero quadratic initial relation

Let
[
\rho_2(r)\in D_2(F)/D_3(F)
]
be the nonzero initial form. For odd (p), the degree-two restricted Lie piece has the form
[
\rho_2(r)
=
\sum_i a_i X_i^{[p]}
+
\sum_{i<j} b_{ij}[X_i,X_j].
]

Two cases suffice.

### Case A: nonzero p-power component

If some (a_i\ne0), take the trivial character (\psi=1). Then
[
\psi(r)=1.
]
The ordinary augmentation of the Fox derivative satisfies
[
\epsilon\!\left(\frac{\partial r}{\partial x_i}\right)
\equiv p,a_i\pmod {p^2}
]
for some (i). Hence the corresponding coefficient has valuation exactly (1). Choosing
[
\delta(x_i)=p^{s-1}u,
qquad
u\in\mathbf Z_p^\times,
]
and the other generator values zero gives
[
\delta(r)=p^s u'\ne0\pmod {p^{s+1}}.
]

### Case B: pure commutator quadratic component

If all (a_i=0), the alternating matrix (B=(b_{ij})) is nonzero. Choose
[
c=(c_1,\ldots,c_d)\in\mathbf F_p^d
]
with (Bc\ne0), and define an order-(p) character
[
\psi_c(x_i)=1+p^s\tilde c_i.
]
Since (r\in D_2(F)) and (\psi_c) has image of exponent (p),
[
\psi_c(r)=1.
]

For a basic commutator,
[
J_{\psi_c,x_i}([x_i,x_j])
=
1-\psi_c(x_j)
\equiv -p^s c_j
\pmod {p^{s+1}},
]
and similarly in the other coordinate. Therefore the quadratic initial form contributes
[
p^s Bc
]
to the twisted Fox vector. Since (Bc\ne0), at least one coefficient has valuation at most (s). Any higher-order contribution cannot destroy the existence of a coefficient allowing (p^s\in I_{\psi_c}(r)); if it lowers the valuation, that only makes the affine lift easier.

Consequently, for every
[
r\in D_2(F)\setminus D_3(F)
]
there exist (\psi,\delta) such that
[
\psi(r)=1,
qquad
v_p(\delta(r))=s.
]

This is the central generalization lemma to be independently formalized.

## 8. Exact marked critical-window separation

With the affine lift above,
[
z\mapsto(1,1),
qquad
F\xrightarrow{\rho_{\psi,\delta}}E_s,
]
satisfies
[
\rho(z^{p^s})=(p^s,1)=\rho(r)\ne1.
]

Since
[
D_{p^s+1}(E_s)=1,
]
the representation factors through the marked quotient
[
W_{p^s+1}(G_s(r)).
]

But it does not factor through (W_{p^s}(G_s(r))), because (r\in D_2(F)\not\subset D_{p^s}(F)) while its affine image is nontrivial.

For (t>s),
[
\rho(z^{p^t})=(p^t,1)=1
]
in (A_s), while (\rho(r)\ne1). Therefore the same affine representation cannot satisfy
[
z^{p^t}=r.
]

Hence the critical exponent is separated in the **marked affine/representation category** exactly at
[
n=p^s+1.
]

## 9. Logical boundary — what this does NOT prove

This construction does **not yet prove**
[
W_{p^s+1}(G_s(r))\not\cong W_{p^s+1}(G_t(r))
]
as abstract unmarked finite groups.

It proves a stronger and cleaner statement in the marked category: the critical finite window carries a finite affine representation that is compatible with exponent (p^s) and incompatible with every larger (p^t).

Thus the remaining bridge is:

[
\text{abstract }W_{p^s+1}
\longrightarrow
\text{canonical affine representation / character package}.
]

If that bridge can be made intrinsic, the marked theorem upgrades to an unmarked separation theorem. If it cannot, the correct endpoint is a **PASS / CLOSED marked theorem + OPEN unmarked reconstruction**.

This is exactly the orientation-bridge gate; it must not be hidden.

## 10. Independent computational audit

Finite-word calculations were independently checked for:
- (p=3,5);
- (s=1,2,3);
- random quadratic words in three generators;
- exhaustive canonical quadratic initial forms in rank two for (p=3) (26 nonzero forms) and (p=5) (124 nonzero forms).

Every tested nonzero quadratic initial relation admitted a character/cocycle pair with
[
\psi(r)=1,
qquad
v_p(\delta(r))\le s,
]
hence (p^s\in I_\psi(r)).

These computations are **PASS / LOCAL**, not a substitute for the general lemma.

## 11. Current gate classification

| Gate | Status |
|---|---|
| Object | **PASS / CLOSED** for the affine test datum |
| Input | **PASS / CLOSED** |
| Functoriality | **PASS / CLOSED** in marked presentation category |
| Gauge | **PASS / CLOSED** when (\psi(r)=1) |
| q-blindness | **PASS / CLOSED** |
| Orientation bridge | **OPEN / LOAD-BEARING** for unmarked finite windows |
| Marked separation at (p^s+1) | **PASS / LOCAL → theorem candidate** |
| General quadratic lemma | **OPEN / LOAD-BEARING** until formalized without case gaps |
| Unmarked same-window separation | **OPEN** |
| Universal arbitrary-degree theorem | **FAIL / CLOSED** |

## 12. Stop rule

Do not enlarge the relation class yet. First close the quadratic lemma and the marked theorem formally. The next computation should attack the unmarked orientation bridge, not another random relation sweep.
