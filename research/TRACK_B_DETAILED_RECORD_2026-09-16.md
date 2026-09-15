# Track B — Detailed Research Record — 2026-09-16

## 0. Independence principle

Track B is kept independent from Track A. Track A studies the representation-theoretic structure of the degree-4 quotient; Track B studies how the actual Demuškin relation produces degree-3/4 filtration classes through Hall–Petrescu and conjugation.

The guiding chain is
\[
uv\to (uv)^3\to gr_3,gr_4\to A1/A2/A3.
\]
No Track-A representation-theoretic conclusion is used as an input to the Track-B calculations.

## 1. Basic setup

\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle,
\]
with \([a,b]=a^{-1}b^{-1}ab\). Set
\[
u=x_1^{-2},\qquad v=[x_3,x_4]^{-1}.
\]
Then
\[
x_2^{-1}x_1x_2=x_1[x_1,x_2]=uv.
\]

The free graded Lie algebra is
\[
L=\mathbb L_{\mathbf F_3}(X_1,X_2,X_3,X_4),
\]
with quadratic relation
\[
R=[X_1,X_2]+[X_3,X_4],\qquad Q_4=L_4/(R)_4.
\]
The target is
\[
T=[[[X_3,X_4],X_1],X_1].
\]
An independent linear-algebra certificate established \(T\notin(R)_4\), hence \(T\neq0\) in \(Q_4\).

## 2. Hall–Petrescu baseline

For \(u\) of weight 1 and \(v\) of weight 2,
\[
(uv)^3\equiv u^3v^3[v,u]^3[v,u,u][v,u,v]\pmod{D_5}.
\]
The relevant weight-4 term is \([v,u,u]\). Since
\[
\operatorname{in}_1(u)=X_1,\qquad \operatorname{in}_2(v)=-[X_3,X_4],
\]
one gets
\[
\operatorname{in}_4([v,u,u])=-T,
\]
so its coefficient is \(2\in\mathbf F_3\).

## 3. A1 — CLOSED

Use
\[
(vu)^3=u^{-1}(uv)^3u.
\]
If \(z=z_3+z_4+\cdots\), then
\[
u^{-1}zu=z_3+(z_4+[z_3,u])+\cdots.
\]
Thus
\[
HP_4((vu)^3)=HP_4((uv)^3)+[z_3,u].
\]
Here \(z_3=X_1^{[3]}\) and \(\operatorname{in}_1(u)=X_1\). The restricted-Lie identity gives
\[
[X_1^{[3]},X_1]=0.
\]
Therefore the possible conjugation correction vanishes; A1 closes without assuming \(z_3=0\).

## 4. A2 — CLOSED

Start with
\[
(uv)^{-3}=(v^{-1}u^{-1})^3.
\]
Put \(x=v^{-1}\) (weight 2), \(y=u^{-1}\) (weight 1). Then
\[
(xy)^3\equiv x^3y^3[y,x]^3[y,x,x][y,x,y]\pmod{D_5}.
\]
Weights are respectively 6, 3, 9, 5, 4, so through degree 4,
\[
(xy)^3\equiv y^3[y,x,y].
\]
With
\[
\operatorname{in}(u^{-1})=X_1,\qquad \operatorname{in}(v^{-1})=[X_3,X_4],
\]
we obtain
\[
[y,x,y]\mapsto [[X_1,[X_3,X_4]],X_1]=-T.
\]
Hence
\[
HP_4((uv)^{-3})=2\,gr_4(x_1^3)-T.
\]
Magnus in characteristic 3 gives
\[
(1+X_1)^3=1+X_1^3,
\]
so \(gr_3(x_1^3)=X_1^{[3]}\) and \(gr_4(x_1^3)=0\). Therefore
\[
\boxed{HP_4((uv)^{-3})=-T=2T\neq0\text{ in }Q_4.}
\]

## 5. A3 — conjugation direction

From
\[
x_2^{-1}x_1x_2=uv
\]
we have
\[
x_2x_1x_2^{-1}=x_2^2(uv)x_2^{-2},
\]
and the preferred exact identity is
\[
\boxed{x_2x_1x_2^{-1}=x_1[x_1,x_2^{-1}].}
\]
The goal is to determine the degree-4 class produced by this opposite conjugation, reduce it in \(Q_4\), and determine its position relative to \(W\) (dimension 45) and \(Q_4/W\) (dimension 10).

### A3-1 — corrected degree 1/2 calculation

Define \(C(g)=x_2gx_2^{-1}\). Then
\[
gr_1(C(x_1))=X_1.
\]
A crucial correction to an earlier draft is
\[
gr_1((uv)^{-1})=-X_1,
\]
so
\[
gr_1((uv)^{-1}x_1)=-X_1+X_1=0,
\]
not \(2X_1=-X_1\). This must hold because \([x_1,x_2^{-1}]\) is a commutator and starts in degree 2.

From
\[
[x_1,x_2]=x_1^{-3}[x_3,x_4]^{-1},
\]
we get at degree 2
\[
gr_2(x_1^{-3})=0,\qquad gr_2([x_3,x_4]^{-1})=-[X_3,X_4],
\]
therefore
\[
\boxed{gr_2([x_1,x_2])=-[X_3,X_4].}
\]
After inversion and conjugation,
\[
\boxed{gr_2([x_1,x_2^{-1}])=[X_3,X_4].}
\]
Thus the currently certified filtered expansion is
\[
\boxed{C(x_1)=X_1+[X_3,X_4]+O(D_3).}
\]

### A3 caution

It is not yet justified to identify the complete degree-3 component of \([x_1,x_2]\) with only \(-X_1^{[3]}\). Degree-3 corrections from \([x_3,x_4]^{-1}\) and product/conjugation terms must be included before degree 4 is computed.

## 6. Current Track-B status

**Closed:** A1 and A2.

**In progress:** A3-1. Degree 1 is \(X_1\), degree 2 is \([X_3,X_4]\). Degree 3 and degree 4 remain to be derived rigorously.

**Next certified target:** compute the complete degree-3 and degree-4 contributions of \([x_1,x_2^{-1}]\), obtain the degree-4 class \(T'\), reduce modulo \((R)_4\), and then determine \(T'\bmod W\).

## 7. Independence rule

No A3 conclusion may be inferred merely from the representation-theoretic structure of \(W\). Conversely, A2's nonzero \(-T\) is an independent Track-B filtration result and does not depend on \(W\cong\Lambda^2(\operatorname{Sym}^2V)\).
