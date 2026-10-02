# PAPER 4 — ORIGIN-CONDITIONED FILTERED DEFECT CANDIDATE AUDIT — 2026-10-02

## Decision

The proposed raw pairing
\[
B_q|_{O\times L_1}:O\times L_1\to A_q
\]
is **not yet a legitimate intrinsic object on the general nonabelian class**. The obstruction is not ordinary-edge contamination but lift dependence: if a degree-one class is represented by \(\tilde u\) and the lift is changed by \(d\in D_2\), then
\[
[\tilde u d,\tilde x]\,[\tilde u,\tilde x]^{-1}
\]
is controlled by \([d,\tilde x]\in D_3\), which is not contained in \(D_{q+1}\) for general \(q\ge3\). Thus a putative degree-q commutator value in \(D_q/D_{q+1}\) cannot be declared lift-independent merely from the centrality of \(D_q/D_{q+1}\). The same issue occurs for the second argument.

This closes Candidate 1 **as written**, but it identifies a stronger intrinsic replacement: condition the **entire finite central extension** on the origin-generated filtered subgroup, rather than trying to manufacture an \(O\times L_1\) pairing first.

## 1. Pre-check

### Object

For every adjacent finite window
\[
E_n:\quad 1\to A_n=D_n/D_{n+1}\to W_{n+1}\xrightarrow{\pi_n}W_n\to1,
\]
let the RP-3 q-blind adjacent-window carrier produce
\[
O_n\subseteq L_1=D_1/D_2.
\]
Define the canonical preimage
\[
H_n(O):=\pi_{1,n}^{-1}(O_n)\le W_n,
\]
where \(\pi_{1,n}:W_n\to W_n/D_2\cong L_1\).

The primary candidate is the restricted extension
\[
E_n(O):=E_n|_{H_n(O)}.
\]
Equivalently, its class is
\[
[E_n(O)]\in H^2(H_n(O),A_n)
\]
with the kernel action inherited from the extension.

This is an origin-conditioned object without choosing generators, lifts, or a complement to \(O_n\).

### Input

Only the abstract adjacent pair \((W_n,W_{n+1})\), together with the already established RP-3 intrinsic carrier \(O_n\). No presentation, generator labels, displayed \(q\), or chosen section are part of the input.

### Functoriality

A filtered isomorphism of adjacent windows transports the extension, the RP-3 carrier, its preimage \(H_n(O)\), and the restricted extension. Full functoriality for arbitrary graph morphisms is not claimed.

### Gauge / lift independence

Changing a section of \(E_n\) changes a cocycle representative by a coboundary but does not change the extension isomorphism class. Hence this object avoids the lift problem that blocks the raw pairing.

### q-blindness

The definition is made for every \(n\). The distinguished special depth is discovered as the first \(n\) for which the relevant restricted extension defect is nontrivial. No \(q\) is inserted.

### Orientation bridge

No bridge to the canonical orientation is assumed. The present object is only a candidate filtered incidence carrier.

### Separation

RP-5 already supplies a same-abelianization separation witness for the underlying extension data; the remaining question is whether the restriction to \(H_n(O)\) preserves a canonical cross-defect that separates the incidence patterns.

## 2. Why Candidate 1 fails as written

A tempting definition is
\[
B_q(u,x)=[\tilde u,\tilde x]\bmod D_{q+1}.
\]
In a nonabelian window this is not a well-defined map on \(L_1\times L_1\).

If \(\tilde u' = \tilde u d\) with \(d\in D_2\), then modulo the usual commutator identities the change contains \([d,\tilde x]\). The filtration only guarantees
\[
[D_2,D_1]\subseteq D_3.
\]
For \(q\ge3\), \(D_3\not\subseteq D_{q+1}\) in the general class. Therefore the degree-q residue can depend on the lift unless additional structure kills the lower-degree term.

This is exactly the structural distinction between:
- a genuine central extension commutator pairing on elements whose images commute in the base, and
- a fictitious pairing on arbitrary degree-one classes obtained by choosing lifts.

Hence the proposed \(B_q|_{O\times L}\) should not be promoted to a theorem.

## 3. The corrected object: restricted origin extension

The intrinsic object is instead
\[
\boxed{\mathfrak D_n(O):=[E_n|_{H_n(O)}].}
\]

The useful secondary datum is its intrinsic commutator defect on the centralizer of \(H_n(O)\) **when that centralizer is taken inside the actual finite group and not replaced by a degree-one lift construction**.

For any
\[
z\in C_{W_n}(H_n(O)),
\qquad
h\in H_n(O),
\]
their images commute in \(W_n\), so for any lifts \(\tilde z,\tilde h\in W_{n+1}\),
\[
\kappa_n^O(h,z):=[\tilde h,\tilde z]\in A_n
\]
is well-defined: changing either lift multiplies by elements of the central kernel \(A_n\), which does not alter the commutator.

This gives a genuine extension-level cross-defect
\[
\kappa_n^O:
H_n(O)\times C_{W_n}(H_n(O))\to A_n,
\]
subject to the usual commutator identities. It is not yet claimed to descend canonically to \(O_n\times L_1\).

## 4. Control calculations

### RP-5 pair

For the four-vertex pair
\[
A:(a,s),(b,s),
\qquad
B:(a,s),(b,t),
\]
the RP-3 origin sector is
\[
O=\langle\bar a,\bar b\rangle.
\]
At the first special layer, the relevant cross-defect is represented by
\[
M_A=
\begin{pmatrix}1&0\\1&0\end{pmatrix},
\qquad
M_B=
\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]
Thus the restricted extension retains the same rank-one versus rank-two separation already established by RP-5.

This is a genuine **PASS / LOCAL** separation test for the corrected object, not a proof of arbitrary incidence reconstruction.

### Mixed ordinary/special model

For
\[
G=\langle a,b,s\mid [a,b]=1,\ sas^{-1}=a^{1+q}\rangle,
\]
the origin carrier gives \(O=\langle\bar a\rangle\). At the first special layer:
- the ordinary edge \((a,b)\) contributes zero extension defect;
- the special edge \((a,s)\) contributes the nonzero class \(\overline{a^q}\).

Thus the extension-level defect is compatible with the desired ordinary-edge contamination rule.

The important point is that this is obtained from the actual finite extension, not from a presentation-dependent subtraction of the ordinary sector.

### Complete one-sink / common-sink controls

In the complete one-sink model, \(W_q\) is abelian at the relevant degree and the restricted extension commutator recovers the previously computed q-defect form. In the common-sink model, the origin plane is already recovered and the extension defect has image
\[
\langle\overline{v_1^q},\overline{v_2^q}\rangle.
\]
These are consistency checks only; they do not close the general theorem.

## 5. What is now genuinely open

The central unresolved question is:

\[
\boxed{
\text{Does }\mathfrak D_q(O)
\text{ contain a canonical cross-defect whose degree-one shadow reconstructs directed special incidence?}
}
\]

Three separate subclaims must not be conflated:

1. **Existence:** the restricted extension is intrinsic. — PASS / LOCAL.
2. **Extraction:** a canonical incidence-relevant subquotient/cross-defect can be extracted from it without a section or presentation. — OPEN / LOAD-BEARING.
3. **Reconstruction:** that extracted object recovers arbitrary directed incidence. — OPEN / LOAD-BEARING.

The raw pairing \(O\times L_1\to A_q\) is therefore not the next object to manipulate. The next target is an intrinsic **relative extension-class quotient**.

## 6. Literature boundary

The oriented pro-p RAAG literature treats the canonical orientation as an intrinsic structure of specially oriented graphs, while the Zassenhaus filtration is characteristic and its successive layers carry genuine filtered information. The literature also relates higher Zassenhaus structure to higher Massey/unipotent phenomena. These facts support the use of filtered extension data, but they do not establish the project-specific origin-conditioned incidence theorem. citeturn0search0turn0search8

No claim is made here that the restricted extension class is a known equivalent of a Massey invariant.

## 7. Classification

| Candidate / claim | Status |
|---|---|
| Raw \(B_q|_{O\times L_1}\) in general nonabelian window | **FAIL / CLOSED — not intrinsically defined as written** |
| Restricted finite extension \(E_n|_{H_n(O)}\) | **PASS / LOCAL** |
| Extension-level commutator on actual centralizer | **PASS / LOCAL** |
| Ordinary-edge contamination in audited controls | **PASS / LOCAL** |
| RP-5 separation retained | **PASS / LOCAL** |
| Canonical degree-one cross-defect extraction | **OPEN / LOAD-BEARING** |
| Arbitrary directed-incidence reconstruction | **OPEN / LOAD-BEARING** |
| Full orientation reconstruction | **OPEN** |

## 8. Stop condition

Do not attempt a large graph scan.

The next authorized attack is a **relative extension-class quotient**:
- define the canonical subgroup(s) from \(O_n\) and the degree-2 bracket data;
- quotient the restricted extension by the lower-degree/ordinary sector intrinsically;
- prove that the resulting first nonzero extension class has a well-defined degree-one cross-defect;
- test it first on the mixed ordinary/special model and RP-5.

If this quotient necessarily requires a section, basis, or presentation, close this carrier branch as **FAIL / CLOSED**.

## Final status

Paper 4 remains **OPEN / LOAD-BEARING**.

The candidate-object search has produced a sharper boundary:

\[
\boxed{
\text{raw origin-restricted pairing: CLOSED}
\quad\longrightarrow\quad
\text{origin-conditioned restricted extension class: OPEN}
}
\]

This is a narrowing of the problem, not yet a new theorem.
