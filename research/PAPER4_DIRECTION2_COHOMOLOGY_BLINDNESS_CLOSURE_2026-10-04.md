# PAPER 4 — DIRECTION 2: MOD-p COHOMOLOGY BLINDNESS — CLOSURE AUDIT — 2026-10-04

## Target

Close Direction 2 at the strongest justified level:

> For the declared odd-p stress family
> \[
> G_{s,a}=\langle z,x_1,\ldots,x_d\mid
> z^{p^s}=x_1^{p^a}[x_1,x_2][x_3,x_4]\cdots[x_{d-1},x_d]\rangle,
> \]
> with \(p\) odd, \(s\ge1\), and finite \(a\ge1\), together with the \(a=\infty\) case in which the \(x_1^{p^a}\) term is absent, the ordinary mod-p cohomology algebra \(H^\bullet(G_{s,a},\mathbf F_p)\) is independent of \(s\) and \(a\) within this declared family.

This is a blindness theorem for the ordinary graded cohomology ring. It is not a claim that the groups, finite windows, higher operations, or filtered extension data are isomorphic.

## 1. Definition / scope audit

Write the defining relator in the free pro-p group as
\[
r_{s,a}=z^{p^s}x_1^{-p^a}
([x_1,x_2][x_3,x_4]\cdots[x_{d-1},x_d])^{-1}
\]
for finite \(a\), with the \(x_1^{-p^a}\) factor omitted for \(a=\infty\).

For odd \(p\),
\[
z^{p^s}\in F^p\subseteq F_{(3)},\qquad
x_1^{p^a}\in F^p\subseteq F_{(3)}
\]
for every \(s,a\ge1\). Hence
\[
r_{s,a}\equiv
[x_1,x_2][x_3,x_4]\cdots[x_{d-1},x_d]
\pmod{F_{(3)}}
\]
up to sign/unit convention.

Thus the degree-2 Zassenhaus initial relation is independent of both \(s\) and \(a\).

Classification: PASS / CLOSED.

## 2. Literature theorem controlling the whole cohomology ring

Quadrelli, arXiv:2011.03233v3, Proposition 2.1 states that for a finitely generated one-relator pro-p group
\[
G=\langle x_1,\ldots,x_d\mid r\rangle
\]
whose relator satisfies
\[
r\equiv [x_1,x_2][x_3,x_4]\cdots[x_{n-1},x_n]
\pmod{G_{(3)}},
\]
the mod-p cohomology algebra is quadratic; the indicated degree-one cup products give the generator of \(H^2\), all other basis products vanish (apart from graded-commutativity), and
\[
H^k(G,\mathbf F_p)=0\quad(k\ge3).
\]

This theorem applies directly because the only \(s,a\)-dependent terms in \(r_{s,a}\) lie in \(F_{(3)}\).

Independent literature control is therefore stronger than a mere associated-graded calculation: it determines the entire ordinary cohomology ring.

## 3. Explicit cohomology algebra

Let
\[
V=H^1(G_{s,a},\mathbf F_p)
=\langle\chi_z,\chi_1,\ldots,\chi_d\rangle.
\]
Then
\[
H^0\cong\mathbf F_p,\qquad
H^1\cong V,\qquad
H^2\cong\mathbf F_p\omega,\qquad
H^k=0\ (k\ge3).
\]

With the dual basis to \(z,x_1,\ldots,x_d\),
\[
\chi_1\cup\chi_2
=\chi_3\cup\chi_4
=\cdots
=\chi_{d-1}\cup\chi_d
=\omega
\]
up to the global sign/unit convention for the relator, while
\[
\chi_z\cup\chi_i=0,\qquad
\chi_i\cup\chi_j=0
\]
for all other unordered pairs not appearing in the displayed commutators. Since \(p\) is odd, graded commutativity supplies the reverse-order signs.

Consequently the algebra is determined solely by the quadratic commutator form and contains no \(s\)- or \(a\)-parameter.

Classification: PASS / CLOSED.

## 4. Why this closes the "all H*" question

There is no hidden higher ordinary cohomology degree in which \(s\) or \(a\) could reappear:
\[
H^k(G_{s,a},\mathbf F_p)=0\quad(k\ge3).
\]
Therefore the full graded ring
\[
H^\bullet(G_{s,a},\mathbf F_p)
\]
is already exhausted by \(H^0,H^1,H^2\) and the degree-one cup product.

Hence, for every two allowed parameter choices,
\[
\boxed{
H^\bullet(G_{s,a},\mathbf F_p)
\cong
H^\bullet(G_{t,b},\mathbf F_p)
}
\]
as graded \(\mathbf F_p\)-algebras.

For the fixed marked presentation there is an evident parameter-independent identification sending the degree-one dual basis to the corresponding degree-one dual basis and the common degree-two generator to the common generator. As an abstract graded algebra, the conclusion is even presentation-independent.

Classification: PASS / CLOSED.

## 5. What is NOT proved by this closure

This closure does **not** imply any of the following:

1. \(G_{s,a}\cong G_{t,b}\).
2. \(W_n(G_{s,a})\cong W_n(G_{t,b})\) for all \(n\).
3. The critical finite windows at \(n=p^s+1\) are isomorphic.
4. Higher Bockstein, Massey, \(A_\infty\), integral Magnus, relation-module, or filtered extension data are equal.
5. The \(a=s\) and \(a=\infty\) groups/windows are indistinguishable by every cohomological operation.

In particular, ordinary \(H^\bullet(-,\mathbf F_p)\) is now certified as a **blind invariant**, not as a proof of group-level non-rigidity.

## 6. Independent verification / adversarial checks

### Check A — filtration degree

For odd \(p\), \(p^m\ge3\) for every \(m\ge1\), so every power term \(z^{p^s}\) and \(x_1^{p^a}\) lies in the third Zassenhaus term. Thus no parameter-dependent term survives in \(D_2/D_3\).

PASS.

### Check B — one-relator hypothesis

The family has one defining relator, and the relator lies in the Frattini subgroup because its lowest term is a commutator. Hence the presentation is minimal and \(H^2\) has dimension one.

PASS.

### Check C — higher ordinary cohomology

The cited Proposition 2.1 gives \(H^k=0\) for \(k\ge3\) under precisely the required quadratic commutator congruence.

PASS.

### Check D — no accidental use of \(q=p^a\)

The cohomology object and its identification use only the degree-two initial commutator form. No \(q\)-dependent coefficient is inserted.

PASS.

### Check E — boundary \(a=s\) versus \(a=\infty\)

Both satisfy exactly the same congruence modulo \(F_{(3)}\), so the same conclusion applies:
\[
H^\bullet(G_{s,s},\mathbf F_p)
\cong
H^\bullet(G_{s,\infty},\mathbf F_p).
\]

PASS.

## 7. Literature boundary

The cited result is stronger than the earlier internal statement "the associated graded is s-blind": it gives the full ordinary mod-p cohomology algebra and its vanishing above degree two for this one-relator quadratic-commutator family.

This also corrects the methodological wording that had suggested a separate mildness argument was required to close Direction 2. Mildness is compatible with the conclusion, and Gärtner's one-relator/mildness results provide independent background, but Proposition 2.1 already closes the exact cohomology-ring claim directly.

## 8. Final classification

\[
\boxed{\text{DIRECTION 2: PASS / CLOSED}}
\]

Precise theorem-level content:

> For odd \(p\), within the declared stress family with \(s\ge1\), finite \(a\ge1\), and \(a=\infty\), the ordinary mod-p cohomology algebra \(H^\bullet(G_{s,a},\mathbf F_p)\) is independent of \(s\) and \(a\). The common algebra is concentrated in degrees \(0,1,2\), with \(H^2\) generated by the common quadratic commutator cup class.

The route is closed. No further computation of ordinary \(H^\bullet(-,\mathbf F_p)\) is authorized as a route to the remaining \(a=s\) versus \(a=\infty\) finite-window separation.

## 9. Consequence for Paper 4

The remaining boundary is now sharply isolated:
\[
\text{ordinary }H^\bullet(-,\mathbf F_p)
\quad\text{blind}
\qquad\Longrightarrow\qquad
\text{look beyond ordinary cohomology}.
\]

The load-bearing problem, if pursued, must retain information not present in the ordinary graded cohomology ring: filtered extension/deformation data, integral p-adic relation data, or another genuinely higher structure. The closed Direction 2 route must not be reopened merely by recomputing the same \(H^1/H^2/H^\ast\) invariants.
