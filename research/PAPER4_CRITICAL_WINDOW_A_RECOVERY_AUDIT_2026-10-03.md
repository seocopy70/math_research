# PAPER 4 — CRITICAL WINDOW RECOVERY OF a — 2026-10-03

## 1. Question

For the stress family
\[
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,
\qquad 1\le a<s,
\]
with odd p and even d>=2, and critical window
\[
W_n(G_{s,a})=G_{s,a}/D_n(G_{s,a}),\qquad n=p^s+1,
\]
does the unmarked finite group W_n determine a?

## 2. Object/Input/Functoriality/Gauge pre-check

**Object.** The abstract finite group \(W_n\), more precisely its abelianization.

**Input.** Only the unmarked filtered finite group \(W_n\); no chosen map to the reference Demushkin quotient and no explicit q/a label.

**Functoriality.** Any filtered-group isomorphism induces an isomorphism of abelianizations, hence preserves their invariant factors.

**Gauge.** Presentation changes are irrelevant after passing to the abstract abelianization.

**Orientation bridge.** Not needed: the parameter a is detected before any orientation functional is used.

**q-blindness.** The construction of the invariant does not insert q=p^a. It reads an invariant already present in W_n.

**Separation.** Distinct finite a<s give distinct abelianization invariant-factor multisets; a=infinity is also separated.

## 3. Abelianization calculation

Let A=G_{s,a}^{ab}. Since r_D has abelianization p^a x_1 in the finite-q case,
\[
A\cong \mathbb Z_p^{d+1}/\langle p^s z-p^a x_1\rangle.
\]
For the Zassenhaus filtration,
\[
\operatorname{im}(D_n(G_{s,a})\to A)=p^{\lceil\log_p n\rceil}A.
\]
At n=p^s+1,
\[
\lceil\log_p(p^s+1)\rceil=s+1.
\]
Therefore
\[
W_n^{ab}\cong A/p^{s+1}A.
\]

Equivalently, starting from \((\mathbb Z/p^{s+1})^{d+1}\), quotient by the single relation
\[
p^s z-p^a x_1=0.
\]
The Smith normal form has invariant factors
\[
\boxed{
W_{p^s+1}(G_{s,a})^{ab}
\cong
\mathbb Z/p^a
\oplus
(\mathbb Z/p^{s+1})^d.
}
\]
The key point is \(a<s\), so \(p^a<p^{s+1}\) and the exceptional invariant factor is unique.

For q=0 (written a=infinity), the relation is \(p^s z=0\), hence
\[
\boxed{
W_{p^s+1}(G_{s,\infty})^{ab}
\cong
\mathbb Z/p^s
\oplus
(\mathbb Z/p^{s+1})^d.
}
\]
Thus a=infinity is also distinguished from every finite a<s.

## 4. Recovery theorem

### Proposition
For odd p, even d>=2, s>=1, and 1<=a<s, the abstract group
\[
W_{p^s+1}(G_{s,a})
\]
determines a uniquely. More precisely, the unique cyclic direct summand of the abelianization whose exponent is strictly below s+1 has order p^a.

Hence
\[
\boxed{a=\log_p\left|T_{<p^{s+1}}\right|}
\]
where \(T_{<p^{s+1}}\) denotes the unique invariant factor of \(W_{p^s+1}^{ab}\) with exponent <s+1.

Combined with the Gate-T/U separation of s, the pair (s,a) is therefore recoverable from the unmarked critical window in the declared nonboundary stress-family range.

## 5. Independent algebra check

The presentation matrix for \(W_n^{ab}\) is the diagonal matrix \(p^{s+1}I_{d+1}\) together with the row \((p^s,-p^a,0,\ldots,0)\). Its Smith normal form is
\[
\operatorname{diag}(p^a,p^{s+1},\ldots,p^{s+1})
\]
for 1<=a<s.

Representative checks:
- (p,s,a,d)=(3,2,1,2): invariants (3,27,27);
- (3,3,2,2): (9,81,81);
- (5,2,1,4): (5,125,125,125,125);
- (3,5,2,2): (9,729,729).

These checks are only independent algebra verification; the proof is the Smith-normal-form calculation above.

## 6. Boundary and limitations

1. The argument is for the declared stress-family range \(1\le a<s\).
2. At the boundary a=s, the finite-a abelianization has exceptional factor p^s, which coincides with the a=infinity abelianization at this level; this argument therefore does **not** recover a there.
3. The proposition recovers the parameter a (equivalently q=p^a) as an invariant of the critical finite window. It does not by itself reconstruct the marked quotient map, the relative extension class, or the full orientation character.
4. It does not replace the independent audit of Gate T's relative nonsplitting proof.
5. The novelty question remains separate: the invariant may be elementary, so literature comparison is required before claiming a new theorem beyond the parameter-identifiability statement.

## 7. Classification

- critical-window recovery of a for 1<=a<s: **PASS / CLOSED**;
- a=infinity versus finite a<s: **PASS / CLOSED**;
- a=s boundary via abelianization: **OPEN**;
- simultaneous (s,a) recovery in the declared nonboundary stress family, using Gate T for s and this proposition for a: **PASS / LOCAL until Gate T is independently audited**;
- marked quotient reconstruction: **OPEN**;
- full orientation reconstruction: **OPEN**;
- coarsest intrinsic realization: **OPEN**.

## 8. Consequence for next step

The proposed “a-recovery” branch is no longer a carrier hunt. The minimal invariant is already visible in W_n^{ab}. The next legitimate task is therefore:
1. independently audit the Gate-T/U s-recovery proof and its exact hypotheses;
2. run a focused novelty/literature comparison for this finite-window abelianization parameter recovery;
3. only then package the combined (s,a)-identifiability theorem.

No degree-5 reopening, scalar/norm shortcut, carrier search, or Paper-5 compression re-opening is justified by this result.
