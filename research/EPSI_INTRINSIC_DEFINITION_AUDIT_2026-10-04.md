# E_psi intrinsic-definition audit — 2026-10-04

## Status

**E_psi branch: OPEN / ACTIVE.**

### 2026-10-04 critical correction and closure
The earlier claim that (D_2/D_3) contains a p-power restricted term was **FAIL / CLOSED** and is superseded. For odd (p), (D_2/D_3congLambda^2H_1(F,mathbf F_p)). A second audit then showed that the (D_3)-tail cannot simply be declared harmless: its p-power part contributes at the same (p^s)-scale after the necessary cocycle normalization. The corrected argument separates that α-independent linear contribution from the nonzero quadratic (B)-functional and varies the order-(p) character parameter to avoid cancellation. This closes the marked quadratic affine separator.


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

## 7. Critical affine lift for every nonzero quadratic initial relation — corrected proof

The earlier Case A/Case B split was mathematically wrong because, for odd p,
[
D_2(F)/D_3(F)cong Lambda^2 H_1(F,mathbf F_p)
]
and contains **no p-power restricted terms**. In particular,
[
ho_2(r)=sum_{i<j}b_{ij}[X_i,X_j],qquad B=(b_{ij})
e0.
]

The remaining issue is not the quadratic class itself but the possible (D_3)-tail, including p-th-power factors. That tail must be controlled rather than dismissed.

Put
[
arepsilon=p^s,qquad
T_s=1+arepsilon A_ssubset U_s.
]
Use characters
[
psi_alpha:F	o T_s,qquad
psi_alpha(x_i)=1+arepsilonalpha_i,
]
with (alpha_iinmathbf F_p). Then (T_s) has exponent p, so
[
psi_alpha(D_2(F))=1.
]

### 7.1 Pure quadratic contribution

For a basic commutator,
[
delta([x_i,x_j])
=
(1-psi(x_j))delta(x_i)
+
(psi(x_i)-1)delta(x_j).
]
Hence, modulo (p^{s+1}),
[
delta([x_i,x_j])
equiv
p^sigl(-alpha_j u_i+alpha_i u_jigr),
qquad u_i=delta(x_i).
]

Therefore for
[
r_2=sum_{i<j}b_{ij}[x_i,x_j]
]
one obtains
[
delta(r_2)
equiv
p^s L_B(alpha,u)
pmod{p^{s+1}},
]
where
[
L_B(alpha,u)
=
sum_{i<j}b_{ij}
igl(-alpha_j u_i+alpha_i u_jigr).
]

If (B
e0), choose a vertex (k) incident to a nonzero coefficient of (B). For (alpha=t e_k), the functional
[
ulongmapsto L_B(t e_k,u)
]
is nonzero whenever (t
e0). Thus the quadratic contribution supplies a genuinely nonzero linear functional in (u).

### 7.2 The (D_3)-tail

Write
[
r=r_2,h,qquad hin D_3(F),
]
where (r_2) is any fixed word representative of the nonzero class (ho_2(r)).

The crucial filtration estimate is:
[
p^{s-1}delta_0(h)
equiv
p^s C_h(u)
pmod{p^{s+1}}
]
for some (mathbf F_p)-linear functional (C_h(u)) independent of (alpha), after choosing an arbitrary base crossed homomorphism (delta_0(x_i)=u_i).

The proof is by the standard generators of (D_3) for odd p:

1. **(gamma_3(F))-part.**  
   For (aingamma_2(F)), (psi_alpha(a)=1) and (delta_0(a)in p^sA_s). Hence
   [
   delta_0([a,b])
   =
   (1-psi_alpha(b))delta_0(a)
   +
   (psi_alpha(a)-1)delta_0(b)
   in p^{2s}A_s
   subseteq p^{s+1}A_s.
   ]
   Thus the (gamma_3)-part disappears modulo (p^{s+1}), even for (s=1).

2. **(p)-power part.**  
   For (gin F),
   [
   delta_0(g^p)
   =
   igl(1+psi_alpha(g)+cdots+psi_alpha(g)^{p-1}igr)delta_0(g).
   ]
   Since (psi_alpha(g)=1+p^salpha(g)),
   [
   1+psi_alpha(g)+cdots+psi_alpha(g)^{p-1}
   equiv ppmod{p^{s+1}}.
   ]
   Hence
   [
   p^{s-1}delta_0(g^p)
   equiv p^s u_gpmod{p^{s+1}},
   ]
   which is exactly an (alpha)-independent linear contribution.

Consequently the full leading evaluation has the form
[
p^{s-1}delta(r)
equiv
p^sigl(C_h(u)+L_B(alpha,u)igr)
pmod{p^{s+1}}.
]

Because (L_B(alpha,u)) is a nonzero linear functional for some (alpha), while (C_h(u)) is independent of (alpha), varying (t) in (alpha=t e_k) shows that at most one (tinmathbf F_p) can make
[
C_h+L_B(t e_k,cdot)
]
identically zero. Since (p) is odd, choose a different (t). Then choose (u) so that
[
C_h(u)+L_B(alpha,u)
e0.
]

Thus there exist ((alpha,u)) for which
[
v_p(delta(r))=s
]
after the harmless normalization by (p^{s-1}).

Since (psi_alpha(r)=1), this gives
[
p^sin I_{psi_alpha}(r).
]

### 7.3 Correct classification

The quadratic separator is therefore no longer merely a computation-backed candidate:

[
oxed{
rin D_2(F)setminus D_3(F)
Longrightarrow
exists(psi,delta):
psi(r)=1,quad
v_p(delta(r))=s.
}
]

This is a **PASS / CLOSED marked affine lemma**, subject only to routine formal polishing of the (D_3=gamma_3F^p) decomposition and the crossed-homomorphism product calculation.

Importantly, this does **not** extend the old arbitrary-degree theorem. The hypothesis
[
rin D_2setminus D_3
]
is essential.

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
| Marked separation at (p^s+1) | **PASS / CLOSED** in the marked affine category |
| General quadratic lemma | **PASS / CLOSED** under (r\in D_2\setminus D_3); routine formal polishing remains |
| Unmarked same-window separation | **OPEN** |
| Universal arbitrary-degree theorem | **FAIL / CLOSED** |

## 12. Stop / next gate

Do not enlarge the relation class to arbitrary Zassenhaus degree. The quadratic marked lemma and marked critical-window separator are now closed. The next load-bearing problem is the **unmarked orientation bridge**: determine whether the abstract finite window canonically recovers enough of the affine/character package to turn marked separation into abstract finite-group separation. If that bridge fails, record the marked theorem as the endpoint of this E_psi formulation rather than silently weakening the notion of intrinsicity.


## 2026-10-04 — critical correction: marked (s) is target-indexed, not an invariant of (r_2)

The proposed next gate “does (v_p(\delta(r))) depend only on (r_2)?” was audited against the actual marked E_\psi construction. That question was ill-posed.

In the closed marked lemma, (s) is fixed **before** constructing the affine target:
\[
A_s=\mathbf Z/p^{s+1}\mathbf Z,qquad E_s=A_s\rtimes(1+p^sA_s).
\]
The lemma then asserts that for every nonzero quadratic initial relation (r\in D_2\setminus D_3), after choosing the order-(p) character and cocycle in that (E_s), one can arrange
\[
\psi(r)=1,qquad v_p(\delta(r))=s.
\]
Thus (s) is not extracted from (r), and there is no single (\delta) whose valuation is an invariant attached to (r_2). The cocycle takes values in the (s)-dependent module (A_s).

For (r_A=[x_1,x_2]), this is explicit for every (s\ge1): take \(\psi(x_1)=1+p^s\), \(\psi(x_i)=1\) for (i>1), and choose the normalized cocycle with (u_2=1) and the other relevant coordinate zero. Then
\[
\delta([x_1,x_2])\equiv p^s\pmod{p^{s+1}},
\]
so the same fixed relation admits a critical affine lift at every target index (s).

Therefore:
- “marked (s) is determined by (r_2)” = **FAIL / CLOSED as a formulation**;
- “same (r_2) implies same marked (s)” = **FAIL / CLOSED**;
- the deduction that marked (s) is not an abstract invariant from that premise is **superseded**;
- the genuine unmarked orientation/orbit-level problem remains **OPEN / LOAD-BEARING**.

This also separates two notions previously conflated: (i) the Zassenhaus degree of a higher tail inserted into a relator, and (ii) the externally indexed critical depth of the affine detector. They are different parameters and must not be identified.

For the exploratory pair (r_A) versus (r_B=r_Ax_1^{p^m}), any separation caused by the added degree-(p^m) tail is therefore a filtered-relator/quotient statement, not evidence that the marked E_\psi exponent parameter is encoded by the quadratic initial form.
