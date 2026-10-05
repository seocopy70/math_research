# Paper 5 — intrinsic relation-jet stabilizer in W_p — 2026-10-06

## Classification

**PASS / CLOSED — intrinsic finite-window relation-package stabilizer and exact GL-image, in the declared odd-p presentation.**

The remaining Step-3 equality at the boundary window is closed intrinsically inside W_p. The correct intrinsic package is slightly more than the shorthand "(b,pi)": it includes the canonical central line
\[
L:=Z(W_p)D_2(W_p)/D_2(W_p)\subset V=W_p/D_2(W_p),
\]
together with the p-power map \(\pi:V\to D_p(W_p)\) and commutator map \(b:\wedge^2V\to D_p(W_p)\), and the defining relation tying the commutator jet to the p-power jet along an adapted generator of L.

## 1. Intrinsic finite window

Since \(D_{p+1}(W_p)=1\),
\[
D_p(W_p)=\langle X=x^p,Y=y^p,Z=z^p\rangle\cong\mathbf F_p^3,
\qquad [D_p(W_p),W_p]=1,
\qquad D_p(W_p)^p=1.
\]
The p-power map
\[
\pi:V\to D_p(W_p),\qquad \pi(\bar g)=g^p,
\]
is well-defined and \(\mathbf F_p\)-linear in this class-\(p\) finite window; the commutator map
\[
b:\wedge^2V\to D_p(W_p),\qquad b(\bar g,\bar h)=[g,h],
\]
is likewise intrinsic and bilinear.

The center gives the intrinsic line
\[
L=Z(W_p)D_2(W_p)/D_2(W_p)=\langle e_z\rangle.
\]
In an adapted basis \((e_x,e_y,e_z)\) with \(e_z\) spanning L,
\[
b(e_x,e_y)=XZ^{-1}=\pi(e_x)\pi(e_z)^{-1},
\qquad
b(e_x,e_z)=b(e_y,e_z)=1.
\]

## 2. Stabilizer calculation

Write an induced linear map as
\[
g(e_x)=me_x+ue_y+ce_z,\quad
g(e_y)=be_x+ve_y+de_z,\quad
g(e_z)=ae_z,
\]
where preservation of the intrinsic central line gives \(a\ne0\).

Preservation of the intrinsic relation package gives
\[
b(g e_x,g e_y)=\pi(g e_x)\pi(g e_z)^{-1}.
\]
The left side is
\[
(mv-bu)XZ^{-1},
\]
while the right side is
\[
X^mY^uZ^{c-a}.
\]
Independence of \(X,Y,Z\) gives
\[
u=0,\qquad v=1,\qquad c=a-m.
\]
Invertibility then forces \(m,a\ne0\), and \(b,d\in\mathbf F_p\) are free. Therefore
\[
\operatorname{Stab}(\mathcal J_p)
=
S'_{11}(p)
=
\left\{
\begin{pmatrix}
m&b&0\\
0&1&0\\
a-m&d&a
\end{pmatrix}
:m,a\in\mathbf F_p^\times,\ b,d\in\mathbf F_p
\right\},
\]
with
\[
|S'_{11}(p)|=p^2(p-1)^2.
\]

## 3. Exact realization inside Aut(W_p)

For every \(m,a\in\mathbf F_p^\times\) and \(b,d\in\mathbf F_p\),
\[
x\mapsto x^m z^{a-m},\qquad
y\mapsto x^b y z^d,\qquad
z\mapsto z^a
\]
preserves the defining relations in W_p:
\([x,z]=[y,z]=1\) and
\[
[x^m z^{a-m},x^b y z^d]
=
[x,y]^m
=
(x^m z^{a-m})^p(z^a)^{-p}.
\]
Hence every element of \(S'_{11}(p)\) is realized, giving
\[
\operatorname{Im}(\operatorname{Aut}(W_p)\to GL(V))
=
S'_{11}(p).
\]

Together with
\[
IA(W_p)\cong\operatorname{Hom}(V,D_p(W_p))\cong\mathbf F_p^9,
\]
this gives
\[
|\operatorname{Aut}(W_p)|=p^{11}(p-1)^2.
\]

## 4. Required numerical correction

The raw index in \(GL_3(\mathbf F_p)\) is
\[
\frac{|GL_3(\mathbf F_p)|}{|S'_{11}(p)|}
=
p(p-1)(p+1)(p^2+p+1).
\]
Thus the previously written expression
\[
\frac{(p^3-1)(p+1)p}{p-1}
\]
is missing a factor \(p-1\).

More importantly, \(|S'_{11}|=p^2(p-1)^2\) means that the intrinsic stabilizer retains two additive/unipotent parameters \(b,d\); it does **not by itself** prove a \(p^2\) deficit relative to all of \(GL_3\), whose p-primary order is \(p^3\). The phrase “p^2 automorphism-order deficit” is therefore not to be inferred from the GL_3 index alone.

## 5. Final gate status

- \(W_{p+1}=W_p\): **PASS / CLOSED / GENERAL**.
- Intrinsic relation package \(\mathcal J_p=(V,D_p,\pi,b,L,\text{relation})\): **PASS / CLOSED / GENERAL**.
- \(\operatorname{Stab}(\mathcal J_p)=S'_{11}(p)\): **PASS / CLOSED / GENERAL**.
- \(\operatorname{Im}(\operatorname{Aut}(W_p)\to GL(V))=S'_{11}(p)\): **PASS / CLOSED / GENERAL**.
- \(|\operatorname{Aut}(W_p)|=p^{11}(p-1)^2\): **PASS / CLOSED / GENERAL**.
- Previous \(S_{11}(p)\) target: **FAIL / CLOSED / SUPERSEDED**.
- “stabilization \(\Rightarrow\) intrinsic S'_{11} stabilizer”: **PASS / CLOSED**.
- “S'_{11} alone \(\Rightarrow\) p^2 automorphism-order deficit”: **NOT CLOSED**; the deficit must be defined relative to the exact comparison family/window whose order differs by \(p^2\).

This audit supersedes the earlier Step-3 entries that left the W_p image equality open, while preserving the numerical correction above.
