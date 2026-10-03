# Paper 4 — s=3 model Schreier transfer witness (2026-10-04)

## Purpose

Continue the remaining (a=s) versus (a=infty) boundary attack at the next local case
[
(p,s)=(3,3),qquad n=p^s+1=28.
]
This is a **model Schreier-lattice calculation**, not yet a theorem about the full (W_{28}), because the required truncation comparison
[
D_{28}(F)cap Ksubseteq D_{10}(K)
]
remains unproved in general.

## Intrinsic setup

Use the corrected cup-radical character
[
chi(z)=1,qquad chi(x)=chi(y)=0,
]
and (K=kerchi). With transversal ({1,z,z^2}), put
[
u=z^3,quad a_i=z^i xz^{-i},quad b_i=z^i yz^{-i}.
]
Conjugation by (z) cycles each (a_i)- and (b_i)-triple and fixes (u) in (K^{ab}).

For (a=s=3), the relator (z^{27}=x^{27}[x,y]) gives the abelianized Schreier relations
[
9u-27a_i=0,qquad i=0,1,2.
]

## Lattice calculation

On the (a)-cycle,
[
(sigma-1)^2a_0=a_0-2a_1+a_2.
]
Hence the critical integral transfer term is
[
9(sigma-1)^2a_0=9a_0-18a_1+9a_2.
]

The relation matrix on ((u,a_0,a_1,a_2)) is
[
A=
egin{pmatrix}
9&-27&0&0\
9&0&-27&0\
9&0&0&-27
end{pmatrix},
]
whose Smith invariants are
[
operatorname{diag}(9,27,27).
]
The target vector
[
(0,9,-18,9)
]
is not in the integral row lattice of (A): the rational solution requires coefficients
[
(-1/3,,2/3,,-1/3),
]
so no integral combination exists.

Therefore, in the **untruncated Schreier abelianization model**,
[
oxed{9(sigma-1)^2a_0
e0}.
]

Modulo (3),
[
(sigma-1)^2a_0equiv a_0+a_1+a_2
e0.
]

## Interpretation

This exactly matches the (s=2) pattern:
[
p^{s-1}(sigma-1)^{p-1}a_0
e0
]
in the model Schreier lattice.

It therefore strengthens the local evidence for the proposed all-(s) transfer-defect mechanism.

It does **not** prove the full finite-window statement at (W_{28}), because the only load-bearing missing step is still the effect of the (D_{28}(F))-truncation relations on (K^{ab}). In particular, no claim is made that the model class survives in the actual (K^{ab}) without a verified filtration comparison.

## Classification

- (s=3) model Schreier lattice nonvanishing: **PASS / LOCAL**.
- Pattern (p^{s-1}(sigma-1)^{p-1}a_0
e0) for (s=2,3): **PASS / LOCAL**.
- Actual (W_{28}) transfer separator: **OPEN / LOAD-BEARING**.
- General all-(s) truncation comparison ((SC_s)): **OPEN / LOAD-BEARING**.
- Paper 4 final all-(s) boundary: **OPEN**.

## Next authorized attack

Do not infer the general theorem from the two local lattices. The next proof target is the actual truncation image
[
operatorname{im}igl(D_{28}(F)cap K	o K^{ab}igr)
]
for this (p=3,s=3) case. If it is contained in (27K^{ab}), the (s=3) finite-window separator follows. If not, this is a decisive counterexample to the proposed transfer-defect mechanism.
