# PAPER 4 — a=s vs a=infinity: intrinsic transfer-defect attack
## 2026-10-04

### Target

Attack the remaining boundary
\[
W_{p^s+1}(G_{s,s})\stackrel{?}{\cong}W_{p^s+1}(G_{s,\infty}),\qquad s\ge2,
\]
without choosing the marked quotient map as part of the final invariant.

### Pre-check

**Object.** Let \(W=W_{p^s+1}\). The cup-radical line in \(H^1(W,\mathbf F_p)\) is one-dimensional in the declared stress-family scope. Its kernel \(K\triangleleft W\), \([W:K]=p\), is therefore intrinsic once the radical line is identified.

**Intrinsic torsion line.** The finite abelianization has
\[
W^{ab}\cong \mathbf Z/p^s\oplus(\mathbf Z/p^{s+1})^d
\]
for both \(a=s\) and \(a=\infty\). Hence the subgroup
\[
T:=W^{ab}[p^s]
\]
(and equivalently its one-dimensional image in \((W^{ab}[p^s]+pW^{ab})/pW^{ab}\)) is canonical. A generator is only defined up to a unit, which is harmless for a zero/nonzero test.

**Functoriality.** For the intrinsic index-\(p\) subgroup \(K\), the transfer
\[
V:W^{ab}\to K^{ab}
\]
is canonical. Therefore the predicate
\[
\varepsilon(W):\quad p^{s-1}V(T)\neq0\text{ in }K^{ab}
\]
is an unmarked, isomorphism-invariant candidate. It uses neither a chosen \(z\) nor the marked map \(W\to D/D_{p^s+1}\).

### Computation

Write \(\sigma\) for conjugation by a lift of the nontrivial element of \(W/K\). For an element \(x\in K\), the transfer is the norm
\[
V(x)=N_\sigma(x),\qquad N_\sigma=1+\sigma+\cdots+\sigma^{p-1}.
\]
For the boundary cases, the canonical short torsion class is represented in abelianization by
\[
\tau_s=zx_1^{-1}\quad(a=s),\qquad \tau_\infty=z\quad(a=\infty).
\]
Thus
\[
p^{s-1}V(\tau_s)
\equiv z^{p^s}N_\sigma(x_1)^{-p^{s-1}}
\pmod{[K,K]},
\]
whereas
\[
p^{s-1}V(\tau_\infty)=z^{p^s}=x_1^{p^s}[x_1,x_2]\cdots
\equiv x_1^{p^s}\pmod{[K,K]}.
\]
Using the boundary relation in the \(a=s\) case, the same expression reduces to the norm defect
\[
 p^{s-1}\bigl(p-N_\sigma\bigr)[x_1]\in K^{ab}.
\]
In the group ring, with \(\delta=\sigma-1\),
\[
N_\sigma
=p+\binom p2\delta+\binom p3\delta^2+\cdots+\delta^{p-1}.
\]
Hence the first potentially new term is the \(\delta^{p-1}\)-term. After multiplication by \(p^{s-1}\), it lies exactly at the critical filtered degree \(p^s\). This is precisely the Jacobson/Hall–Petrescu cross term that survives the naive shear calculation and is invisible in the ordinary quadratic graded shadow.

### What the attack closes

1. The raw \(p^s\)-power of a chosen lift was not intrinsic; the transfer construction removes that gauge ambiguity.
2. The candidate is genuinely unmarked: it is built from the intrinsic radical kernel, the canonical torsion subgroup of \(W^{ab}\), and transfer.
3. The scalar/coinvariant shortcut is not being repeated. The surviving datum is the non-coinvariant \(C_p\)-module action in \(K^{ab}\).
4. The remaining boundary is reduced to one explicit lemma: whether the \(\delta^{p-1}\)-term survives in the actual \(K^{ab}\) at the critical layer.

### Decisive unresolved lemma

A separating theorem would follow if one proves
\[
p^{s-1}(p-N_\sigma)[x_1]\neq0
\]
in the \(a=s\) window, while the corresponding transfer class for \(a=\infty\) is zero after the canonical normalization of the torsion line. The \(a=\infty\) side has the relation \(z^{p^s}\in[K,K]\), so its transfer class vanishes in \(K^{ab}\).

What is **not** yet proved is the required nonvanishing on the \(a=s\) side. A quotient witness must preserve the cyclic action \(W/K=C_p\) and the defining relation simultaneously; the earlier non-equivariant class-2 witnesses cannot simply be reused. This is the exact load-bearing point.

### Classification

- intrinsic radical kernel \(K\): **PASS / LOCAL**;
- canonical torsion line \(T\): **PASS / LOCAL**;
- transfer-defect predicate \(\varepsilon(W)\): **PASS / LOCAL candidate**;
- reduction to the \(\delta^{p-1}\) critical term: **PASS / LOCAL**;
- nonvanishing for \(a=s\): **OPEN / LOAD-BEARING**;
- vanishing for \(a=\infty\) after normalization: **PASS / LOCAL**;
- general unmarked separation \(a=s\) vs \(a=\infty\): **OPEN / LOAD-BEARING**.

This attack therefore does not close the boundary, but it materially sharpens it: the remaining question is no longer “find any filtered invariant”, but an explicit transfer/norm nonvanishing statement in the intrinsic index-\(p\) kernel.
