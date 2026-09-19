# TWISTED DEGREE-(2,3) LIFTING-OBSTRUCTION THEOREM — 2026-09-19

## Status

This file records the proof-level closure of the previously open degree-truncation and presentation/gauge-naturality bridges for the first twisted mod-9 lifting obstruction.

The result is deliberately limited to the first twisted obstruction modulo 9. It does **not** prove recovery from the bare Zassenhaus restricted graded object, and it does **not** by itself recover higher 3-adic digits.

## 1. Setup

Let
\[
G=F/\overline{\langle r\rangle}
\]
be a minimal one-relator pro-3 group, with
\[
V=H^1(G,\mathbf F_3)^*.
\]
Let the Zassenhaus initial form of the relator through degree 3 be
\[
r=(R,P)+O(D_4),
\]
where
\[
R\in L_2(V),\qquad P\in L^{res}_3(V).
\]
Let
\[
p(P)\in V^{(1)}
\]
be the restricted-cubic/power projection.

For a character
\[
\rho:G\to1+3\mathbf F_3\subset(\mathbf Z/9)^\times
\]
write
\[
\rho(g)=1+3\lambda(g)\pmod 9,
\qquad \lambda\in H^1(G,\mathbf F_3).
\]
Put \(A_2=\mathbf Z/9\) with action through \rho and \(A_1=\mathbf F_3\) with trivial action.

## 2. Cohomological obstruction

There is a G-equivariant exact sequence
\[
0\to3A_2\to A_2\to A_1\to0,
\]
and \(3A_2\cong\mathbf F_3\) is trivial because
\[
(1+3\lambda(g))\,3t=3t\pmod9.
\]
Hence the connecting map
\[
\delta_\rho:H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3)
\]
is the complete obstruction to lifting a mod-3 class.

For a one-relator presentation, the standard free-resolution/transgression description identifies \(\delta_\rho(f)\) with the lifted crossed-homomorphism evaluation on \(r\), divided by 3 and reduced modulo 3. Thus the calculation is automatically on cohomology classes; twisted principal derivations do not create a separate loophole.

## 3. Exact word calculation modulo 9

Let \(z:F\to A_2\) be a crossed homomorphism lifting \(f\). For a positive word
\[
w=s_1\cdots s_m
\]
the crossed rule gives
\[
z(w)=\sum_{j=1}^m \rho(s_1\cdots s_{j-1})z(s_j).
\]
Modulo 9,
\[
\rho(s_1\cdots s_{j-1})
=1+3\lambda(s_1\cdots s_{j-1}),
\]
and only the reduction of \(z(s_j)\) modulo 3 is needed in the correction term. Therefore
\[
z(w)\equiv
\sum_j z(s_j)
+
3\sum_j\lambda(s_1\cdots s_{j-1})f(s_j)
\pmod9.
\tag{3.1}
\]
The same formula, with the usual inverse rule
\[
z(s^{-1})=-\rho(s)^{-1}z(s),
\]
handles arbitrary reduced words.

The second term in (3.1), after division by 3 and reduction modulo 3, depends only on the degree-2 Magnus initial form of \(w\). Hence it sees exactly \(R\).

For the fixed convention
\[
[x,y]=x^{-1}y^{-1}xy,
\]
a direct calculation gives
\[
z([x,y])
=
3\bigl(\lambda(x)f(y)-\lambda(y)f(x)\bigr)
\pmod9.
\tag{3.2}
\]
Thus the quadratic contribution is
\[
(\lambda\wedge f)(R).
\]

For a generator,
\[
z(x^3)=z(x)+(1+3a)z(x)+(1+3a)^2z(x)
\equiv3f(x)\pmod9,
\tag{3.3}
\]
so the restricted cubic/power contribution is \(f(p(P))\).

## 4. Why degree >=4 cannot contribute

The relevant filtration is the Zassenhaus filtration, not merely ordinary word length.

For a free pro-3 group,
\[
D_n(F)=\prod_{3^j i\ge n}\gamma_i(F)^{3^j}.
\]
Consequently an element of \(D_4(F)\) has exponent sums divisible by 9: the only possible nonzero abelian contribution comes from the \(\gamma_1^9\) factor; all commutator factors have zero exponent sum.

Therefore, if \(r'\equiv r\pmod{D_4(F)}\), then
\[
\frac{\text{(trivial-action part of }z(r))-
      \text{(trivial-action part of }z(r'))}{3}
\equiv0\pmod3.
\]
Likewise, the degree-2 Magnus coefficients of \(r\) and \(r'\) agree modulo 3, because a \(D_4\)-difference has no degree-2 initial form.

Hence the first twisted obstruction depends only on the degree-2 and degree-3 restricted initial data:
\[
(R,p(P)).
\]
The bracket component of \(P\) contributes no abelian exponent sum, so it disappears from the divided trivial-action term. Equivalently, the restricted-cubic quotient relevant to degree-one evaluation is
\[
L^{res}_3(V)/[V,L_2(V)]\cong V^{(1)}.
\]

This proves the truncation statement; no informal “higher terms vanish” assumption remains.

## 5. The obstruction formula

Combining (3.2), (3.3), and the \(D_4\) estimate gives
\[
\boxed{
\delta_\rho(f)
=
\bigl[f(p(P))+(\lambda\wedge f)(R)\bigr]\omega
}
\]
for a chosen generator \(\omega\in H^2(G,\mathbf F_3)^\times\).

Changing \(\omega\) rescales the entire expression by one common nonzero scalar. An independent sign change of \(p(P)\) is not a gauge transformation.

Thus the first twisted lifting obstruction factors through the projective degree-(2,3) carrier
\[
\boxed{\overline J_3(G)=[(R,p(P))].}
\]

## 6. Presentation/gauge naturality

The connecting map \(\delta_\rho\) is defined intrinsically by the coefficient exact sequence and therefore is independent of the chosen free presentation.

Suppose two minimal one-relator presentations describe the same \(G\). Their generator changes induce the natural identification of \(H^1(G,\mathbf F_3)\), and their choices of nonzero \(H^2\)-generator differ by one common scalar.

For every first-digit character \(\lambda\), the family
\[
B_{\lambda}(f):=\delta_\rho(f)\in H^2(G,\mathbf F_3)
\]
is therefore presentation-independent.

The map
\[
(R,p)\longmapsto
\bigl[(\lambda,f)\mapsto f(p)+(\lambda\wedge f)(R)\bigr]
\]
is injective: setting \(\lambda=0\) recovers \(p\), while varying \(\lambda,f\) recovers the alternating bilinear form \(R\). Consequently the projective carrier \([(R,p)]\) is forced by the intrinsic family of connecting maps.

This proves the required naturality without choosing a preferred IA lift. In particular, the earlier degree-3 gauge
\[
(R,P)\mapsto(uR,uP+[v,R])
\]
is compatible with the intrinsic obstruction family: the \([v,R]\) part is invisible to the degree-one evaluation, and the twisted cocycle coordinates transform through the induced \(H^1\)-identification.

## 7. Frozen rank-4 consequence

For
\[
r_3=x_1^3[x_1,x_2][x_3,x_4],
\]
\[
R=[X_1,X_2]+[X_3,X_4],
\qquad
p(P)=X_1^{(1)}.
\]
Hence
\[
\frac{\delta_\rho(f)}{\omega}
=
(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
\]
Vanishing for every \(f\) gives
\[
a_1=a_3=a_4=0,\qquad a_2=1,
\]
so
\[
\boxed{\rho(x_1,x_2,x_3,x_4)=(1,4,1,1)\pmod9.}
\]

For the power-free control
\[
r_0=[x_1,x_2][x_3,x_4],
\]
one has \(p(P)=0\), so the first twisted-surjectivity obstruction has the zero solution \(\lambda=0\).

## 8. Relation to canonical Demuškin orientation

For an infinite Demuškin pro-p group, the canonical orientation is characterized by the Kummerian/1-cyclotomic lifting condition: for every \(n\), the map
\[
H^1(G,\mathbf Z_p(\chi)/p^n)\to H^1(G,\mathbf F_p)
\]
is surjective, and this orientation is unique. Quadrelli records this explicitly and gives, for the standard Demuškin presentation,
\[
\chi(x_2)=(1-p^f)^{-1},\qquad \chi(x_i)=1\ (i\ne2).
\]
See Quadrelli, *Chasing Maximal Pro-p Galois Groups via 1-Cyclotomicity*, Example 2.6 and the surrounding definition of Kummerianity. \cite{quadrelli2024}

Thus the present mod-9 calculation is the first nontrivial finite-level shadow of the canonical orientation criterion; the literature theorem supplies the global uniqueness statement, while the present relation-jet calculation supplies the explicit degree-(2,3) obstruction for the frozen group.

## 9. Final theorem status

### CLOSED
- cohomological connecting obstruction;
- exact crossed-homomorphism formula modulo 9;
- degree-(2,3) truncation;
- disappearance of the bracket part of \(P\);
- projective presentation/gauge naturality of the first twisted carrier;
- frozen recovery \(\chi\bmod9=(1,4,1,1)\).

### STILL OPEN / SEPARATE
- recovery from the bare Zassenhaus restricted graded object;
- a claim of absolute categorical minimality without first fixing the carrier category;
- a new exact characteristic-zero compression theorem beyond the already closed fixed-q filtered carrier result;
- higher 3-adic digits unless the full compatible tower is used.

The broad computational scan remains unauthorized. The correct next work, if this branch is continued, is manuscript-level consolidation and comparison with the higher cohomological invariants in the literature.
