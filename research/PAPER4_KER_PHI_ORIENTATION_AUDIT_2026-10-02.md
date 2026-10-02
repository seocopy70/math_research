# PAPER 4 — KER PHI ORIENTATION TEST: SMALLEST MODELS — 2026-10-02

## Decision

The proposed \\(\ker\\Phi) route does contain genuine orientation-sensitive information in some models, but it does **not** provide a universal finite-window recovery mechanism for \\(\\omega_q\\).

The decisive point is that \\(\\ker\\Phi) can be nonzero and carry nonzero \\(\\omega_q)-mass in one model, while it can be zero in another admissible model. Therefore there is no model-independent rule of the form “recover \\(\\omega_q) from the structure/restriction of \\(\\ker\\Phi)” without adding extra data that is not contained in the kernel itself.

## 1. Object and input

Retain the already intrinsic diagnostic map
\\[
\\Phi:U\\to\\operatorname{Hom}(O,A),\\qquad
u\\mapsto B_q(u,-),
\\]
where
\\(U=L_1/O_q\\) is the quotient by the intrinsic q-torsion/origin sector.

Because \\(\\Phi) is already accepted as an intrinsic finite-window diagnostic object, its kernel
\\[
K:=\\ker\\Phi
\\]
is intrinsic as a subspace of \\(U\\).

The proposed new question is whether the canonical normalized orientation functional
\\(\\omega_q:U\\to\\mathbf F_p\\)
can be reconstructed from \\(K), for example through \\(\\omega_q|_K), the quotient \\(U/K), or the annihilator \\(K^\\perp\\subseteq U^*\\).

## 2. Smallest decisive model with nonzero kernel

Use the already audited specially oriented chordal tree with ordinary vertices \\(a,b) and special vertices \\(s,t,u), with special edges
\\[
a\\to s,\\qquad b\\to t,\\qquad a\\to u,\\qquad b\\to u.
\\]

At the q-defect layer:
\\[
\\Phi(\\bar s)=P_a,\\qquad
\\Phi(\\bar t)=P_b,\\qquad
\\Phi(\\bar u)=P_a+P_b.
\\]

Hence, in the basis \\(\\bar s,\\bar t,\\bar u) of \\(U) and \\(P_a,P_b) of the relevant image,
\\[
[\\Phi]=
\\begin{pmatrix}
1&0&1\\
0&1&1
\\end{pmatrix}.
\\]

Therefore
\\[
K=\\ker\\Phi
 =\\mathbf F_p(\\bar u-\\bar s-\\bar t).
\\]

The canonical normalization is
\\[
\\omega_q(\\bar s)=\\omega_q(\\bar t)=\\omega_q(\\bar u)=1.
\\]

Consequently
\\[
\\omega_q(\\bar u-\\bar s-\\bar t)
=1-1-1=-1\\ne0
\\]
for odd p.

Thus
\\[
K\\not\\subseteq\\ker\\omega_q.
\\]

Equivalently, \\(\\omega_q) does **not** descend to a functional on \\(U/K), and it is not in the annihilator of \\(K)\\):
\\[
\\omega_q\\notin K^\\perp=\\operatorname{im}(\\Phi^*).
\\]

This is stronger than merely saying that “some information survives in the kernel.” The kernel relation itself is an obstruction to factoring the desired orientation through \\(\\Phi)\\).

## 3. Smallest complementary model: the kernel disappears

Now use the separated two-sink model already used in the T1 affine-hull counterexample:
\\[
G=\\langle a,b,s,t\\mid
sas^{-1}=a^{1+q},\\;
tbt^{-1}=b^{1+q}
\\rangle.
\\]

This model satisfies the natural orientation-rigidity restriction candidate: every special vertex is the terminus of a special edge. There are no isolated special vertices.

Here
\\[
U=\\operatorname{span}(\\bar s,\\bar t),
\\]
and
\\[
\\Phi(\\bar s)=P_a,\\qquad
\\Phi(\\bar t)=P_b.
\\]

Thus \\(\\Phi) is injective and
\\[
\\ker\\Phi=0,
\\qquad
\\omega_q(\\alpha\\bar s+\\beta\\bar t)=\\alpha+\\beta.
\\]

So the entire orientation functional survives while the proposed kernel contains no nonzero vector at all.

This is decisive against treating \\(\\ker\\Phi) as the carrier of orientation data in general.

## 4. Structural interpretation

The two models expose the exact limitation.

The kernel records **linear dependencies among the local incidence columns**. In the chordal-tree model,
\\[
P_a+P_b-P_a-P_b=0
\\]
produces the kernel vector \\(u-s-t). But the desired orientation functional measures the coefficient sum, and that sum is not zero on the dependency.

Hence the kernel is not an “orientation remainder.” It is an incidence-dependency space, and the orientation functional is generally transverse to it.

In the separated model there are no such dependencies, so \\(K=0) and the kernel has nothing to say about the normalization.

Therefore the implication
\\[
\\ker\\Phi\\Longrightarrow\\omega_q
\\]
fails at the level of structural type, not merely because a particular reconstruction formula was chosen badly.

## 5. Quotient/dual reformulation

There are two equivalent linear-algebra formulations.

1. **Descent obstruction**
\\[
\\omega_q\\text{ descends to }U/K
\\iff K\\subseteq\\ker\\omega_q.
\\]
The chordal-tree model violates this.

2. **Dual/image obstruction**
\\[
K^\\perp=\\operatorname{im}(\\Phi^*).
\\]
The chordal-tree orientation satisfies
\\[
\\omega_q\\notin\\operatorname{im}(\\Phi^*).
\\]
Thus no recovery rule that first forces \\(\\omega_q) to factor through the image of \\(\\Phi) can work.

The separated model gives the opposite extreme \\(K=0), where \\(K^\\perp=U^*\\) and the kernel imposes no normalization at all.

## 6. What survives

The negative result does **not** make \\(\\ker\\Phi) useless.

It remains an intrinsic diagnostic of incidence dependencies and may be useful for:
- detecting linear relations among local defect signatures;
- identifying when the pairing loses information;
- constructing further no-go tests for candidate orientation factorizations.

But none of these presently supplies the missing canonical normalization.

In particular, “orientation lives in the kernel” must be rejected as a general statement. The correct statement is:

> In some models the kernel contains vectors on which the canonical orientation is nonzero; in other admissible models the kernel is zero.

## Classification

- \\(\\ker\\Phi) intrinsic as a diagnostic subspace: **PASS / LOCAL**.
- Nonzero orientation mass on \\(\\ker\\Phi) in the chordal-tree model: **PASS / LOCAL**.
- Universal recovery of \\(\\omega_q) from \\(\\ker\\Phi) alone: **FAIL / CLOSED**.
- Universal descent \\(\\omega_q:U\\to U/\\ker\\Phi): **FAIL / CLOSED**.
- Recovery through \\(\\operatorname{im}\\Phi^*=\\ker(\\Phi)^\\perp): **FAIL / CLOSED** for the current pairing.
- \\(\\ker\\Phi) as a diagnostic/no-go object: **OPEN / LOCAL**.
- Paper 4 top-down program: **OPEN**, but the kernel-rescue branch is closed.

## Consequence for the natural Gate-D restriction

The separated two-sink model already satisfies the proposed restriction that every special vertex is the terminus of a special edge. Therefore this kernel obstruction survives the most immediate repair of Gate D; it is not an artifact of isolated special vertices.

No larger kernel scan is authorized. A revival would require a materially richer object than \\(\\ker\\Phi) itself and a fresh Object/Input/Functoriality/Gauge/Orientation-bridge/q-blindness/Separation/Novelty/Stop pre-check.

Detailed continuation boundary: the next target must not be “find a clever functional on \\(\\ker\\Phi)”. It must first explain what additional intrinsic datum, beyond the kernel of the global pairing, distinguishes the zero-kernel separated model from the nonzero-kernel tree model while remaining capable of fixing the global coefficient normalization.
