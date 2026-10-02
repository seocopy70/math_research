# PAPER 4 — MINIMAL COEFFICIENT-VALUED EXTENSION OBJECT: NORMALIZATION TEST — 2026-10-02

## Decision

The smallest natural coefficient-valued augmentation of D1 is the restricted-origin extension together with its intrinsic centralizer commutator defect and the restricted-power target.

This object is intrinsically legitimate, but it **does not determine the canonical orientation functional in the chordal-tree control**.

Thus the next boundary is sharper:

\[
\boxed{
\text{depth signature loses scale}
\quad\longrightarrow\quad
\text{coefficient-valued cross-defect restores scale locally}
\quad\longrightarrow\quad
\text{but still does not determine global orientation.}
}
\]

Classification: **FAIL / CLOSED as a general orientation carrier**.

## 1. Smallest candidate

For the adjacent extension
\[
E_n:1\to A_n\to W_{n+1}\to W_n\to1,
\]
use the intrinsic RP-3 origin sector $O_n$ and its canonical preimage
\[
H_n(O)\le W_n.
\]

Restrict the extension:
\[
\mathfrak D_n(O)=[E_n|_{H_n(O)}].
\]

Inside the actual finite groups, use the centralizer
\[
C_n(O)=C_{W_n}(H_n(O)).
\]

For $z\in C_n(O)$ and $h\in H_n(O)$, the commutator of lifts is a well-defined element
\[
\kappa_n^O(h,z)\in A_n.
\]

At the first nonzero special layer, compare this coefficient-valued defect with the intrinsic restricted-power target
\[
P_n:O_n\to A_n.
\]

The minimal normalized-direction candidate is therefore
\[
\mathcal N_n
=
\left\{
\bar z\in C_n(O)/\text{(lower centralizer sector)}:
\kappa_n^O(h,z)=P_n(h)
\ \forall h\in O_n
\right\}.
\]

No basis, presentation, section, displayed $q$, or orientation is inserted.

## 2. Pre-check

### Object
A restricted finite central extension plus an actual-group commutator defect.

### Input
Only the adjacent filtered window and the q-blind origin carrier already obtained from the abelianization exponent jump.

### Functoriality
Filtered isomorphisms transport $H_n(O)$, its restricted extension, its centralizer, the commutator defect, and $P_n$.

### Gauge
The extension class is section-independent. The commutator of commuting base elements is independent of lift because the kernel is central.

### q-blindness
The construction is uniform in $n$; the first nonzero defect layer is detected rather than named in advance.

### Separation
It distinguishes the RP-5 common-sink and split-sink controls.

### Novelty
This is not merely the raw presentation relation: it is an intrinsic finite-extension construction. It is therefore a legitimate object to test.

## 3. Rank-two special-edge control: PASS / LOCAL

For
\[
G=\langle v,w\mid wvw^{-1}=v^{1+q}\rangle,
\]
the origin sector is $O=\mathbf F_p\bar v$ and the special direction is $\bar w$.

The coefficient-valued defect satisfies
\[
\kappa(\bar v,\lambda\bar w)
=
\lambda P(\bar v).
\]

Hence the normalized condition
\[
\kappa(\bar v,z)=P(\bar v)
\]
forces
\[
\lambda=1.
\]

So the new object genuinely restores the scalar normalization that D1 lost.

This is the exact reason the D2 depth-signature route failed: the missing information is now explicitly present.

Classification: **PASS / LOCAL**.

## 4. Separated two-sink control: PASS / LOCAL

For
\[
G=
\langle a,b,s,t\mid
sas^{-1}=a^{1+q},\;
tbt^{-1}=b^{1+q}\rangle,
\]
the coefficient matrix relative to the intrinsic origin and defect targets is
\[
M=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
\]

The normalized condition gives
\[
\alpha=1,\qquad\beta=1
\]
for
\[
z=\alpha s+\beta t.
\]

Thus the unique normalized vector in the sink plane is
\[
s+t,
\]
and its canonical orientation value is
\[
\omega_q(s+t)=2.
\]

This already shows that “normalized defect coefficient = 1 on every origin” is **not** the same as “orientation value = 1 on the normalized vector.” The defect object recovers an incidence-normalized vector, not automatically the desired orientation functional.

Classification: **PASS / LOCAL for coefficient normalization; FAIL / CLOSED as an orientation bridge if one identifies the normalized vector with a 1-level orientation point.**

## 5. Chordal-tree control: decisive failure

Use the audited chordal tree
\[
s-a-u-b-t
\]
with special edges
\[
a\to s,\quad b\to t,\quad a\to u,\quad b\to u.
\]

The intrinsic origin sector is
\[
O=\mathbf F_p\bar a\oplus\mathbf F_p\bar b.
\]

The coefficient-valued defect columns are
\[
\delta(s)=(1,0),\qquad
\delta(t)=(0,1),\qquad
\delta(u)=(1,1).
\]

Therefore for
\[
z=\alpha s+\beta t+\gamma u,
\]
the normalized defect condition is
\[
\alpha+\gamma=1,
\qquad
\beta+\gamma=1.
\]

Hence the normalized locus is
\[
z_\gamma=(1-\gamma)s+(1-\gamma)t+\gamma u.
\]

It is an affine line, not a point.

But the canonical orientation is
\[
\omega_q(s)=\omega_q(t)=\omega_q(u)=1,
\]
so
\[
\omega_q(z_\gamma)=2-\gamma.
\]

For odd $p$, this varies with $\gamma$.

Thus the coefficient-valued restricted-extension defect does **not** determine $\omega_q$ even after scalar normalization has been restored.

Equivalently, the defect kernel contains
\[
k=u-s-t,
\]
while
\[
\omega_q(k)=-1\ne0.
\]

This reproduces the earlier kernel obstruction, now inside the minimal genuinely coefficient-valued extension object. It is not an artifact of having discarded coefficients.

Classification:
\[
\boxed{\text{coefficient-valued restricted extension as orientation carrier = FAIL / CLOSED.}}
\]

## 6. What the three controls prove together

The obstruction chain is now structurally complete:

1. **D1 depth profile:** intrinsic and q-blind, but scalar-blind.
2. **Minimal coefficient restoration:** fixes scalar normalization in the rank-two and separated controls.
3. **Global chordal-tree control:** the resulting incidence relation has a nontrivial kernel carrying orientation mass.

Therefore the desired orientation is not simply:
- a depth invariant;
- a scalar-normalized incidence vector;
- or a linear functional descending from the first coefficient-valued incidence quotient.

The missing datum, if it exists, must be genuinely nonlinear/non-incidence information in the finite extension.

## 7. Boundary of the negative result

This does **not** prove that the full adjacent finite group extension
\[
W_{q+1}\to W_q
\]
can never determine $\omega_q$ on a restricted class.

It proves that the **minimal relative-extension cross-defect** does not.

In particular, the following stronger route remains logically distinct:
- retain the full nonabelian extension class rather than only its first cross-defect;
- use higher extension identities/relations among multiple commutators;
- determine whether those nonlinear relations break the chordal-tree shear direction.

That is the next and only meaningful gate if the branch is to continue.

## 8. Next authorized gate

The next gate is therefore **D3/nonlinear extension rigidity**, not another linear carrier search.

Before any computation, the required pre-check is:

1. **Object:** the full isomorphism class of the restricted finite extension $E_q|_{H_q(O)}$, including its multiplication/extension class, not merely $\kappa$.
2. **Input:** the finite adjacent window only.
3. **Functoriality:** filtered-isomorphism covariance.
4. **Gauge:** extension equivalence, not a chosen cocycle.
5. **Orientation bridge:** prove that the nonlinear extension structure selects $\omega_q$.
6. **q-blindness:** define uniformly for arbitrary adjacent index $n$.
7. **Separation:** first chordal-tree and separated controls.
8. **Novelty:** ensure the construction is not merely a re-encoding of the full finite group.
9. **Stop:** if an orientation-changing automorphism of the full restricted extension survives, close the branch.

No new graph/carrier family is authorized before this pre-check.

## Final status

- D2 depth-signature quotient: **FAIL / CLOSED**.
- Minimal coefficient-valued restricted extension: **FAIL / CLOSED** as orientation carrier.
- Nonlinear full-extension rigidity: **OPEN / LOAD-BEARING**.
- Unrestricted Gate D: **FAIL / CLOSED**.
- Paper 4: **OPEN**, but only if the next object passes the non-reencoding pre-check.


## CORRECTION — 2026-10-02

The separated two-sink discussion must respect the corrected oriented-RAAG convention: an absent edge does **not** imply commutation. Hence a generic mixed vector (alpha s+eta t) is not automatically q-flat against both origins; a component attached to the wrong origin can create a lower-degree obstruction.

The coefficient-valued extension candidate still passes the rank-two scalar-normalization test. The decisive global failure remains the chordal-tree model, where the normalized coefficient equations have the nontrivial kernel direction (u-s-t) with nonzero orientation mass.

Thus the chordal-tree obstruction, not the earlier separated-model calculation, is the controlling failure for the coefficient-valued carrier.
