# B2 / k=4 — FINITE-WINDOW KUMMER RECOGNITION MOD 81 — 2026-09-24

## Status / gate

**Authorized next gate after the corrected k=3 audit.**

Target:
\[
A_4=\mathbf Z/81(\rho_4),\qquad Q_4=G/P_5,
\]
with
\[
G=\langle x_1,x_2,x_3,x_4\mid r=x_1^3[x_1,x_2][x_3,x_4]\rangle,
\quad P_{n+1}=P_n^3[P_n,G].
\]

The purpose is deliberately narrow: determine whether the mod-81 coefficient-extension obstruction has a unique compatible zero and whether the corresponding lift annihilates (P_5), before making any all-(k), intrinsic, or classification-free claim.

## 0. Pre-check

- **Object:** \(\mathsf K_4(\rho_4):H^1(Q_4,\mathbf Z/81(\rho_4))\to H^1(Q_4,\mathbf F_3)\) surjective.
- **Input:** finite quotient (Q_4), candidate coefficient action, coefficient-extension/crossed-cocycle structure only.
- **Functoriality:** the predicate is invariant under isomorphism of ((Q_4,\rho_4)); presentation independence of the selected character remains open.
- **Gauge:** no relator coordinate is declared intrinsic; the current calculation is in the frozen standard presentation.
- **Orientation bridge:** universal relation obstruction (=0), followed by (P_5)-annihilation.
- **q-blindness:** (q) is absent from the predicate formula, but the underlying model is fixed to (q=3); this is not yet a q-uniform theorem.
- **Separation:** failure means no finite-window lift at k=4; success means only a local k=4 result.
- **Novelty:** full-group Kummerianity is known; the candidate novelty remains finite-window factorization.
- **Stop:** no all-k induction or intrinsic selector claim is made at this gate.

## 1. Compatible mod-81 candidates

The k=3 selector gives
\[
\rho_3=(1,13,1,1)\pmod{27}.
\]

Every compatible lift to mod 81 has
\[
\rho_4(x_1)=1+27a_1,quad
\rho_4(x_2)=13+27a_2,quad
\rho_4(x_3)=1+27a_3,quad
\rho_4(x_4)=1+27a_4,
\]
with (a_i\in\mathbf F_3).

Because the target is abelian, these generator values define characters on the free group.

## 2. Exact mod-81 crossed-word obstruction

Let (z:F\to A_4=\mathbf Z/81(\rho_4)), (z_i=z(x_i)). For (s=\rho_4(x)),
\[
z(x^3)=(1+s+s^2)z(x).
\]
For ([x,y]=x^{-1}y^{-1}xy),
\[
z([x,y])
=s_x^{-1}(s_y^{-1}-1)z(x)
+s_y^{-1}(1-s_x^{-1})z(y).
\]

Direct reduction modulo 81 gives
\[
\boxed{
z(r)=27\bigl((1-a_2)z_1+a_1z_2-a_4z_3+a_3z_4\bigr)\pmod{81}.
}
\]

Thus, with (f_i=z_i\bmod3),
\[
\boxed{
\delta_4(f)=(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
}
\]

## 3. Uniqueness

Universal vanishing on (H^1(G,\mathbf F_3)\cong\mathbf F_3^4) forces, from the four basis vectors,
\[
1-a_2=0,quad a_1=0,quad a_4=0,quad a_3=0.
\]

Hence the unique candidate is
\[
\boxed{\rho_4=(1,40,1,1)\pmod{81}.}
\]

No use of the known formula ((1-3)^{-1}) is made in obtaining 40.

## 4. Independent verification

A fresh exhaustive enumeration of all (3^4=81) compatible lifts gives exactly one zero obstruction vector, at
\[
(a_1,a_2,a_3,a_4)=(0,1,0,0).
\]
This is verification only; the proof is the displayed obstruction plus basis vectors.

## 5. Finite-depth existence: (P_5)-annihilation

Fix \(\rho_4=(1,40,1,1)\).

For arbitrary lifts (z_i\in\mathbf Z/81) of (f_i), the relation formula gives (z(r)=0), so the cocycle descends from the free pro-3 group to (G).

Since (f) vanishes on (P_2),
\[
z(P_2)\subset3A_4.
\]
Also \(\rho_4(P_2)=1\).

Using (P_3=P_2^3[P_2,G]), the crossed-power and crossed-commutator formulas give
\[
z(P_3)\subset9A_4.
\]
Here (g\in P_2\Rightarrow\rho_4(g)=1), so the second commutator term vanishes, while ((\rho_4(h)-1)z(g)\in3\cdot3A_4).

Next, (P_4=P_3^3[P_3,G]) gives
\[
z(P_4)\subset27A_4,
\]
because (z(P_3)\subset9A_4) and (ho_4(P_3)=1).

Finally,
\[
P_5=P_4^3[P_4,G]
\]
gives
\[
z(P_5)=0,
\]
since cube terms lie in (81A_4) and commutator terms in (3\cdot27A_4=81A_4); also (ho_4(P_4)=1).

Therefore every mod-3 class lifts and every lift factors through
\[
Q_4=G/P_5.
\]

## 6. k=4 conclusion

For the declared standard rank-four (q=3) model,
\[
\boxed{
\mathsf K_4(\rho_4)\iff\rho_4=(1,40,1,1).
}
\]

Classification:
- k=4 exact obstruction: **PASS / CLOSED** for the standard family;
- k=4 uniqueness: **PASS / LOCAL**;
- (P_5)-annihilation: **PASS / LOCAL**;
- (Q_4)-factorization: **PASS / LOCAL**;
- presentation-free/intrinsic selector: **OPEN**;
- q-uniform theorem: **OPEN**;
- all-k theorem: **OPEN / DECISIVE**;
- minimal/coarsest carrier: **OPEN / LOAD-BEARING**.

## 7. Boundary and next gate

The repeated valuation chain is evidence for a uniform finite-depth lemma, but k=4 alone does not prove it. A uniform induction is a separate authorized gate.

The next gate, after audit, is therefore the **uniform finite-depth lemma** for
\[
A_k=\mathbf Z/3^k,qquad Q_k=G/P_{k+1},
\]
followed by a direct literature comparison of that lemma with existing Kummerian quotient machinery.

No (t_2) route is revived.

## 8. Critical audit — 2026-09-24

Independent modular recomputation over Z/81 confirms the displayed crossed-power and crossed-commutator calculation for all 81 parameter tuples. The exact obstruction formula is algebraically sound:

z(r)=27((1-a_2)z_1+a_1z_2-a_4z_3+a_3z_4) mod 81.

### 8.1 Character factorization
Because the target is abelian, every candidate kills P_2, hence also P_5. Therefore every compatible candidate character factors through Q_4=G/P_5. This should be stated explicitly.

### 8.2 Cocycle descent
The relation calculation is first on the free pro-3 group. Descent to G requires z(r)=0 and rho(r)=1. The latter holds because every candidate factors through the abelianization. These conditions imply vanishing on the closed normal closure of r.

### 8.3 Obstruction versus K_4
If K_4(rho_4) holds on Q_4, every mod-3 class has a Q_4-valued lift, so the relation obstruction vanishes universally. Conversely, the unique zero candidate gives arbitrary generator lifts whose cocycles descend to G and then factor through Q_4 by the valuation argument. Thus the local equivalence is justified.

### 8.4 Arbitrary generator lifts
For the canonical candidate, z(r)=0 for arbitrary z_i in Z/81, not merely specially chosen lifts. This is an important strength of the existence argument.

### 8.5 Valuation chain
The chain z(P_2) subset 3A_4, z(P_3) subset 9A_4, z(P_4) subset 27A_4, z(P_5)=0 is valid. At each commutator step one must explicitly use g in P_j implies rho(g)=1, while rho(h)-1 is divisible by 3. This is the mechanism producing the extra factor of 3.

This strongly suggests a uniform lemma, but k=4 alone does not prove it.

### 8.6 Novelty boundary
The full Kummerian/cyclotomic characterization and uniqueness of the Demushkin orientation are already known. The potentially new statement remains finite-depth factorization: finite-level coefficient lifting on G is already visible on Q_4. Even this remains LOCAL because the current construction is tied to the standard presentation.

### 8.7 q-blindness
The obstruction formula contains no explicit q, but the computation is on the fixed q=3 standard model. This is not yet q-uniformity.

### 8.8 Dependence on k=3
The k=4 candidate space was reduced using the established k=3 selector. Thus k=4 uniqueness is conditional on k=3 and should not be presented as independent from scratch.

### 8.9 Enumeration
The 81-case enumeration is independent verification, not proof. The proof is the obstruction formula plus the four basis-vector tests.

### 8.10 Notation cleanup
The source contains several formatting artifacts in LaTeX delimiters. They do not affect the mathematics but should be cleaned before publication use.

### Revised audit classification
- exact mod-81 obstruction: PASS / CLOSED;
- compatible candidate character and Q_4-factorization: PASS / CLOSED, with the explicit P_5 subset P_2 argument;
- unique zero obstruction: PASS / CLOSED;
- cocycle descent to G: PASS / CLOSED;
- valuation chain through P_5: PASS / LOCAL;
- Q_4-level existence/surjectivity: PASS / LOCAL;
- presentation-free selector: OPEN;
- q-uniform theorem: OPEN;
- all-k theorem: OPEN / DECISIVE;
- minimal/coarsest intrinsic carrier: OPEN / LOAD-BEARING.

**Audit decision: k=4 survives. It is not yet the uniform theorem.**