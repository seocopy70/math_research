# PAPER 4 — PAIRING/KERNEL SHEAR NO-GO — 2026-10-02

## Decision

The kernel calculation strengthens to a clean categorical no-go for the entire linear pairing package
\\[
\\mathcal D=(U,O,A,P_E,\\Phi),
\\]
not merely for \\(\\ker\\Phi) alone.

In the decisive chordal-tree model, there is an automorphism of this package that fixes \\(O), \\(A), the intrinsic q-power map \\(P_E), and \\(\\Phi)\\) exactly, but changes the canonical orientation functional \\(\\omega_q)\\).

Therefore no intrinsic orientation functional can be defined from \\(\\Phi)\\), \\(\\ker\\Phi)\\), and \\(P_E)\\) alone. The missing normalization is genuinely outside this linear package.

## 1. Kernel vector

Use the audited chordal tree with
\\[
\\Phi(s)=P_a,\\qquad
\\Phi(t)=P_b,\\qquad
\\Phi(u)=P_a+P_b.
\\]

Then
\\[
k:=u-s-t\\in\\ker\\Phi,
\\qquad
\\omega_q(k)=-1\\ne0.
\\]

## 2. Invisible shear

For any
\\[
c\\in\\mathbf F_p,
\\]
define
\\[
g_c(s)=s,\\qquad
g_c(t)=t,\\qquad
g_c(u)=u+c,k.
\\]

Because \\(\\Phi(k)=0),
\\[
\\Phi\\circ g_c=\\Phi.
\\]

The map \\(g_c) is invertible: it is the identity on the quotient \\(U/\\mathbf F_p k)\\) and sends the kernel generator to
\\[
g_c(k)=u+c(u-s-t)-(s)-(t)=(1+c)k.
\\]
For \\(c\\ne-1), this is an automorphism. In particular, take \\(c=1)\\) for every odd p.

It fixes the origin sector and the q-power target because it acts only on \\(U)\\). Hence the whole package \\(\\mathcal D)\\) is unchanged.

But
\\[
\\omega_q(g_c(u))
=\\omega_q(u+c k)
=1-c.
\\]
For \\(c=1),
\\[
\\omega_q(g_1(u))=0\\ne1=\\omega_q(u).
\\]

Thus \\(\\omega_q)\\) is not invariant under an automorphism of the complete candidate package.

## 3. Strong consequence

Suppose a canonical finite-window construction
\\[
F(\\mathcal D)=\\omega_q
\\]
existed using only the linear package \\(\\mathcal D=(U,O,A,P_E,\\Phi)\\).

Naturality under automorphisms would force
\\[
F(\\mathcal D)=g_c^*F(\\mathcal D)
]
for every automorphism \\(g_c)\\) of \\(\\mathcal D).

But the canonical \\(\\omega_q)\\) is not fixed by \\(g_1)\\). Contradiction.

So the obstruction is not merely that a proposed formula on \\(\\ker\\Phi)\\) fails. The entire linear pairing package has an internal invisible shear symmetry incompatible with the desired orientation.

## 4. Relation to the separated model

The separated two-sink model has \\(\\ker\\Phi=0)\\), so it does not exhibit the shear. It supplies the complementary fact that the kernel is not even guaranteed to exist as a nonzero carrier.

The chordal-tree model shows the stronger issue: whenever a kernel exists, its invisible directions can carry nonzero orientation mass.

Together:
- separated model: \\(\\ker\\Phi=0)\\);
- chordal tree: \\(\\ker\\Phi\\ne0)\\) and \\(\\omega_q|_{\\ker\\Phi}\\ne0)\\);
- chordal-tree shear: \\(\\Phi)\\) and \\(P_E)\\) remain fixed while \\(\\omega_q)\\) changes.

This closes the entire linear-pairing/kernel normalization branch at the level of the declared package.

## Classification

- \\(\\ker\\Phi)\\) intrinsic diagnostic: **PASS / LOCAL**.
- \\(\\omega_q|_{\\ker\\Phi}\\ne0)\\) in the chordal tree: **PASS / LOCAL**.
- \\(\\omega_q)\\) descent to \\(U/\\ker\\Phi): **FAIL / CLOSED**.
- orientation from \\(\\ker\\Phi)\\) alone: **FAIL / CLOSED**.
- orientation from \\(U,O,A,P_E,\\Phi)\\) by any intrinsic/natural construction: **FAIL / CLOSED**.
- Paper 4 overall: **OPEN**.

## Boundary

This no-go is only for the declared linear package. It does not prove that the full nonabelian finite window contains no orientation normalization; it proves that such normalization cannot be recovered after compressing the window to \\(U,O,A,P_E,\\Phi)\\).

Therefore the next authorized question is not another functional on \\(\\ker\\Phi). It is:

> What non-linear/nonabelian datum of the finite extension survives the passage to \\(\\Phi)\\) and breaks the invisible kernel shear?

Any proposed datum must pass Object/Input/Functoriality/Gauge/Orientation bridge/q-blindness/Separation/Novelty/Stop before computation.
