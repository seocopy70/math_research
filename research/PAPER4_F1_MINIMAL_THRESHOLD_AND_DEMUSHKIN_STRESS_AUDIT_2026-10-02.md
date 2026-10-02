# PAPER 4 — F1 MINIMAL THRESHOLD AND STANDARD DEMUSHKIN EXTENSION TEST — 2026-10-02

## A. Exact K–Z threshold

For
\[
G_s^{ab}\simeq \mathbf Z_p^2\oplus\mathbf Z/p^s
\]
and \(Q_n=G_s/D_n(G_s)\), put \(e(n)=\lceil\log_p n\rceil\). Then
\[
Q_n^{ab}\simeq(\mathbf Z/p^{e(n)})^2\oplus
\mathbf Z/p^{\min(s,e(n))}.
\]

To recover \(\min(s,m)\) uniformly for all \(s\), one must have \(e(n)\ge m\). For \(m\ge2\), this is equivalent to
\[
n>p^{m-1}.
\]
Thus the exact smallest integer depth is
\[
\boxed{n_m^{\mathrm{KZ}}=p^{m-1}+1}.
\]

Sufficiency: at this depth \(e(n)=m\), so the finite abelianization recovers \(\min(s,m)\).

Necessity: if \(n\le p^{m-1}\), then \(e(n)\le m-1\), and the two parameters
\[
s=e(n),\qquad t=m
\]
have identical \(\min(s,e(n))=e(n)\), while \(\min(s,m)=e(n)\ne m=\min(t,m)\). Hence no invariant extracted solely from this abelianization can uniformly recover \(\min(s,m)\) at that depth. More strongly, the same-window lemma gives identical full Zassenhaus windows whenever \(p^s\ge n\), so for suitable \(s<t<m\) no full-window factorization can recover the m-truncation.

Boundary: \(m=1\) is trivial for the K–Z family with \(s\ge1\), since every \(\epsilon_s\) is divisible by \(p\).

## B. Standard higher-rank q=0 Demushkin stress model

For odd p and even \(d\ge4\), let
\[
D_d=\langle x_1,\ldots,x_d\mid
r_D=[x_1,x_2][x_3,x_4]\cdots[x_{d-1},x_d]\rangle,
\]
the standard q=0 Demushkin group. Consider the one-relator extension candidate
\[
\widetilde G_{s,d}
=
\langle z,x_1,\ldots,x_d
\mid
z^{p^s}=r_D
\rangle,
\]
with N the normal closure of z and quotient \(D_d\).

The initial Zassenhaus form of the defining relation is exactly the Demushkin quadratic relation \(r_D\). Since q=0 Demushkin groups are mild, the candidate presentation has the same quadratic initial form and is a natural mild test model; mildness gives cd_p \(\widetilde G_{s,d}=2\). However, a general theorem that this particular N is free pro-p is not being asserted here without an explicit kernel theorem. Therefore this is a **stress model for the homological mechanism, not yet a certified free-by-Demushkin example**.

Its abelianization is nevertheless immediate:
\[
\widetilde G_{s,d}^{ab}
\simeq
\mathbf Z_p^d\oplus\mathbf Z/p^s.
\]
Thus the same finite-window calculation yields
\[
(\widetilde G_{s,d}/D_{p^m})^{ab}
\simeq
(\mathbf Z/p^m)^d\oplus\mathbf Z/p^{\min(s,m)}.
\]

So the K–Z adaptive abelianization mechanism is not rank-2-specific: it persists for the standard q=0 Demushkin relation at the level of this one-relator extension model.

## C. q != 0 boundary

For a standard Demushkin quotient with finite torsion invariant \(q=p^a\), the defining relation has an abelianized \(p^a x_1\) component. Replacing it by
\[
z^{p^s}=r_D
\]
gives, at the abelianized level, one relation
\[
p^s z=p^a x_1.
\]
Smith normal form therefore produces a torsion factor of order
\[
p^{\min(a,s)}
\]
rather than \(p^s\).

Hence the simple abelianization detector saturates at the quotient's own Demushkin q-invariant. It cannot recover arbitrarily deep extension depth once \(s>a\).

This is a genuine structural warning: the K–Z/q=0 mechanism is not a universal abelianization theorem. For q>0, higher nonabelian/filtered relation data would be required to see the tail beyond the intrinsic quotient torsion.

## D. Current frontier

- exact K–Z minimal valuation threshold \(p^{m-1}+1\): **PASS / CLOSED**;
- q=0 higher-rank standard-relation stress model: **PASS / LOCAL** at abelianized homological level;
- certification that the stress model's kernel N is free: **OPEN**;
- q>0 abelianization saturation at \(\min(a,s)\): **PASS / LOCAL**;
- general free-by-Demushkin finite-window recovery of extension depth: **OPEN / LOAD-BEARING**;
- general finite scalar character beyond abelianization: **OPEN**;
- E2 -> orientation: **OPEN**.

## E. Stop / next authorized test

Do not claim a general theorem from the stress model. The next decisive test is kernel certification for \(\widetilde G_{s,d}\), or alternatively an independently sourced free-by-Demushkin family with q>0 and variable extension depth. If the kernel is certified free and q>0 still exhibits saturation, then the program obtains a genuine positive/negative dichotomy:
q=0: abelianization may detect arbitrary depth;
q>0: abelianization alone cannot.

