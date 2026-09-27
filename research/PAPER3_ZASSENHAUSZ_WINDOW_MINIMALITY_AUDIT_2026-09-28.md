# Paper 3 — Zassenhaus finite-window minimality audit — 2026-09-28

## Gate

**Target:** determine whether the sufficient window
[
Q_k=G/P_{3^{k-1}+1}
]
for the finite Kummer recognition predicate is minimal in the declared fixed rank-four (q=3) Demuškin setting.

Here (P_ullet) is the 3-Zassenhaus filtration and
[
mathsf K_k(Q_n,ho):
H^1(Q_n,mathbf Z/3^k(ho))	o H^1(Q_n,mathbf F_3)
]
is the finite Kummer lifting predicate whenever the candidate (ho) descends to (Q_n).

## 1. Sufficiency

The existing U1–U3 chain proves that every crossed cocycle with coefficients
[
A_k=mathbf Z/3^k(ho)
]
factors through
[
Q_k^{mathrm{win}}=G/P_{N+1},
qquad N=3^{k-1}.
]
Equivalently,
[
P_{N+1}
]
is annihilated by the semidirect product (A_ktimes U_{1,k}), so
[
mathsf K_k(Q_{N+1},ho)
Longleftrightarrow
mathsf K_k(G,ho).
]

This is the established upper bound.

## 2. Sharpness witness at the preceding window

Let
[
chi_k(x_2)=(1-3)^{-1}pmod{3^k},
qquad
N=3^{k-1}.
]
Let (fin H^1(G,mathbf F_3)) be the class with
[
f(x_2)=1,qquad f(x_i)=0 (i
e2).
]

By the U3 criterion, the canonical candidate (chi_k) admits a crossed cocycle lift (z) with
[
z(x_2)equiv1pmod3.
]
For every such lift,
[
z(x_2^N)
=
left(sum_{j=0}^{N-1}chi_k(x_2)^jight)z(x_2).
]
Writing (a=(1-3)^{-1}), the geometric sum is
[
S_N=rac{a^N-1}{a-1}.
]
Since (a-1) has 3-adic valuation (1), while
[
v_3(a^N-1)=v_3((1-3)^N-1)=1+v_3(N)=k
]
by the LTE valuation formula, one gets
[
v_3(S_N)=k-1.
]
Hence
[
S_Nequiv u,3^{k-1}pmod{3^k}
]
for a unit (u), and therefore
[
oxed{z(x_2^N)
e0pmod{3^k}}
]
for every lift with (z(x_2)equiv1pmod3).

But
[
x_2^Nin G^{N}subseteq P_N(G)
]
for the 3-Zassenhaus filtration. Thus no such cocycle can factor through
[
G/P_N.
]

Therefore the mod-(3^k) canonical Kummer lifting predicate cannot already be realized on the preceding window (G/P_N): the class (f) has no lift there for the canonical candidate.

## 3. Minimality conclusion

The sufficient window is (P_{N+1}), while the preceding window (P_N) fails for the canonical candidate itself.

Consequently:
[
oxed{
n_k^{mathrm{Kum}}=3^{k-1}+1
}
]
for the declared finite Kummer recognition predicate on the fixed rank-four (q=3) Demuškin group, among the standard Zassenhaus windows (G/P_n).

In particular:
[
k=2:quad n_2=4,
qquad
k=3:quad n_3=10,
]
and the direct witnesses are
[
z(x_2^3)=3pmod9,
qquad
z(x_2^9)=9pmod{27}.
]

## 4. What exactly is proved

This is a **sharpness theorem for the stated Kummer selector**, not a theorem that every conceivable orientation carrier requires this depth.

It proves:

1. (P_{3^{k-1}+1}) is sufficient for arbitrary candidate factorization/U1–U3.
2. (P_{3^{k-1}}) is insufficient even for the canonical candidate and a single explicit mod-3 cohomology class.
3. Therefore the exact Zassenhaus-window threshold of this selector is (3^{k-1}+1).

It does **not** prove:
- absolute minimality among arbitrary finite invariants;
- minimality among richer relation-jet carriers;
- impossibility of a different selector using less information;
- publication novelty by itself.

## 5. Independent finite checks

For (k=2,dots,6), direct modular evaluation gives
[
sum_{j=0}^{3^{k-1}-1}(1-3)^{-j}
equiv3^{k-1}pmod{3^k}
]
for the canonical inverse (a=(1-3)^{-1}) in (mathbf Z/3^k).

Explicitly:
[
egin{array}{c|c|c}
k&N& S_Nmod 3^k\
hline
2&3&3\
3&9&9\
4&27&27\
5&81&81\
6&243&243
end{array}
]
The table is verification only; the LTE argument is the proof.

## Classification

- preceding-window obstruction: **PASS / CLOSED**
- sharp Zassenhaus threshold (3^{k-1}+1): **PASS / CLOSED**
- absolute carrier minimality: **OPEN / NOT CLAIMED**
- publication novelty of the threshold: **OPEN / CONDITIONAL**
- next Paper 3 problem: richer-carrier separation (O	o T), not another attempt to lower this selector's Zassenhaus window.


## Critical review correction — 2026-09-28

The sharpness argument is mathematically sound, but one prerequisite was implicit and must be stated explicitly: to formulate \(\mathsf K_k(G/P_N,\chi_k)\), the canonical coefficient action \(\chi_k\) must descend to \(G/P_N\). This follows by functoriality of the Zassenhaus filtration under homomorphisms together with
\[
D_N(1+3\mathbf Z_3)=1+3^k\mathbf Z_3\quad\text{for }N=3^{k-1},
\]
so \(\chi_k(P_N)=1\pmod{3^k}\). Equivalently, this can be proved directly from the Zassenhaus image filtration of the principal-unit target. The witness \(z(x_2^N)\neq0\) then shows that the lifting predicate on \(G/P_N\) fails, rather than merely that a particular cocycle fails to descend.

A second editorial correction: the independently checked modular table in this document covers \(k=2,\ldots,6\), not \(k=2,\ldots,8\). The proof itself is all-\(k\) and does not depend on the finite table.

Classification unchanged: **PASS / CLOSED** for the sharpness theorem of the stated Kummer selector; the descent lemma is now made explicit. Absolute carrier minimality and publication novelty remain **OPEN / CONDITIONAL**.
