# Paper 5 — W_p corrected structure / Step 3 closure audit — 2026-10-06

## Verdict

**PASS / CLOSED / GENERAL within the declared odd-(p), (n=p) presentation scope**, subject to the intrinsic structural lemma (D_p(W_p)cong\mathbf F_p^3) being understood as part of the quotient computation.

The previous (D_p\cong\mathbf F_p^2, x^p=z^p) package is superseded. The relation
[
[x,y]=x^p z^{-p}
]
identifies the commutator with (X-Z); it does not impose (X=Z).

## 1. Correct (W_p) structure

Set
[
X=x^p,quad Y=y^p,quad Z=z^p.
]
At (n=p),
[
[D_p(W_p),W_p]=1,qquad D_p(W_p)^p=1,
]
and the quotient computation gives
[
D_p(W_p)=\langle X,Y,Z\rangle\cong\mathbf F_p^3.
]
The defining relation is
[
[x,y]=XZ^{-1}.
]
Thus (XZ^{-1}) is a nonzero central (D_p)-element in general; it is not the relation (X=Z).

## 2. IA kernel

For (g\in IA(W_p)),
[
g(x)=x\alpha,quad g(y)=y\beta,quad g(z)=z\gamma,
qquad \alpha,\beta,\gamma\in D_p.
]
Since (D_p) is central of exponent (p),
[
(x\alpha)^p=x^p,qquad
[y\beta,x\alpha]=[y,x],
]
and similarly for the defining centrality relations. Hence every linear map
[
V\to D_p
]
gives an IA automorphism, and the kernel is
[
IA(W_p)\cong\operatorname{Hom}(V,D_p)
\cong\operatorname{Hom}(\mathbf F_p^3,\mathbf F_p^3)
\cong\mathbf F_p^9.
]
In particular (z\mapsto zy^p) is present. The former (\mathbf F_p^2) and (\mathbf F_p^6) claims are superseded.

## 3. Intrinsic image upper bound

For an automorphism, the characteristic central quotient satisfies
[
g(z)\equiv z^a\pmod{D_2},
qquad a\ne0,
]
so write
[
g(x)\equiv x^m y^u z^c,qquad
g(y)\equiv x^b y^v z^d.
]
The central (D_p)-calculation gives
[
[g(x),g(y)]
=X^{mv-bu}Z^{-(mv-bu)},
]
whereas
[
g(x)^p g(z)^{-p}=X^mY^uZ^{c-a}.
]
Because (X,Y,Z) are independent in (D_p\cong\mathbf F_p^3), equality forces
[
u=0,qquad mv-bu=m,qquad c-a=-(mv-bu).
]
Since (M\in GL(V)), (m\ne0), hence
[
v=1,qquad c=a-m.
]
Thus
[
\operatorname{Im}\subseteq
S'_{11}(p)
=
\left\{
\begin{pmatrix}
m&b&0\\
0&1&0\\
a-m&d&a
\end{pmatrix}
:
m,a\in\mathbf F_p^\times, b,d\in\mathbf F_p
\right\}.
]

## 4. Lower bound / realization

For every (m,a\in\mathbf F_p^\times) and (b,d\in\mathbf F_p),
[
x\mapsto x^m z^{a-m},qquad
y\mapsto x^b y z^d,qquad
z\mapsto z^a
]
preserves
[
[x,z]=[y,z]=1,qquad [x,y]=x^p z^{-p}
]
inside (W_p). Indeed,
[
[g(x),g(y)]=X^mZ^{-m}
=g(x)^p g(z)^{-p}.
]
The induced map on (V) is invertible, so the descended endomorphism is an automorphism. Therefore
[
S'_{11}(p)\subseteq\operatorname{Im}.
]

Hence
[
\boxed{\operatorname{Im}=S'_{11}(p)},
qquad
|S'_{11}(p)|=p^2(p-1)^2.
]

## 5. Automorphism order

With
[
|IA(W_p)|=p^9,
]
the exact sequence
[
1\to IA(W_p)\to\operatorname{Aut}(W_p)
\to S'_{11}(p)\to1
]
gives
[
\boxed{|\operatorname{Aut}(W_p)|=p^{11}(p-1)^2}.
]

## Classification

- (n<p: W_n\cong\mathbf F_p^3, IA=1, \operatorname{Aut}=GL_3(\mathbf F_p)): **PASS / CLOSED**.
- (D_p(W_p)\cong\mathbf F_p^3): **PASS / CLOSED / GENERAL**, within the declared quotient computation.
- (IA(W_p)\cong\mathbf F_p^9): **PASS / CLOSED / GENERAL**.
- (m_{y,x}=0, m_{y,y}=1, c=a-m): **PASS / CLOSED / GENERAL**.
- (S_{11}) of order (p^2(p-1)): **FAIL / CLOSED / SUPERSEDED**.
- (S'_{11}\subseteq\operatorname{Im}): **PASS / CLOSED / GENERAL**.
- (\operatorname{Im}=S'_{11}(p)): **PASS / CLOSED / GENERAL**.
- ( |\operatorname{Aut}(W_p)|=p^{11}(p-1)^2): **PASS / CLOSED / GENERAL**.

The preceding boundary-consistency audit is therefore **superseded by this corrected (D_p\cong\mathbf F_p^3) computation**.
