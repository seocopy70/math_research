# PAPER 4 — FILTERED q-PROFILE QUOTIENT / UNIQUENESS AUDIT — 2026-10-02

## 1. Active question

The current load-bearing question is not whether lower filtration rejects the separated accidental direction; that local mechanism works. The question is whether the full filtered q-profile determines a canonical quotient
\[
U\longrightarrow U/N_q\longrightarrow \omega_q
\]
with an intrinsic subspace \(N_q\subseteq\ker\omega_q\), and whether the induced normalized q-defect determines \(\omega_q\) uniquely.

The decisive tests are the long ordinary chain and mixed ordinary/special components.

## 2. Pre-check

**Object.** The finite-window filtered commutator profile at the first nonzero special layer:
\[
[u,x]\in D_q,\qquad [u,x]\equiv c_x(u)P_E(x)\pmod{D_{q+1}},
\]
with \(x\) in the already recovered origin sector.

**Input.** Only the adjacent finite window \(W_q\leftarrow W_{q+1}\), together with the intrinsic origin sector recovered from RP-3 and the intrinsic restricted-power target \(P_E\). The displayed value of \(q\) is not part of the definition; it is recovered from the first extension jump/exponent of the finite window.

**Functoriality / gauge.** A successful theorem must be invariant under filtered-window isomorphisms and independent of lifts. This is NOT yet proved for the full profile in arbitrary nonabelian windows and remains a separate logical boundary.

**Orientation bridge.** For a genuine special terminus \(s\), every incident edge is special in a specially oriented graph, so the normalized q-defect is 1. The target orientation has \(\omega_q(s)=1\).

**q-blindness.** The intended construction uses the adjacent-window exponent/power map, not a hard-coded q.

**Separation.** The profile distinguishes a lower-degree contaminant from a genuine q-layer special defect.

**Novelty.** The literature establishes the canonical orientation and local/sinkhole structure; it does not state the finite-window quotient theorem below. This audit is therefore a project-level structural test, not a literature attribution of the theorem.

**Stop condition.** If the quotient requires a tautological definition equivalent to \(\ker\omega_q\), the branch is rejected.

## 3. Long ordinary chain: decisive calculation

Take the mixed ordinary/special chain
\[
r_1-r_2-a\longrightarrow s,
\]
where the last arrow is the special edge \(a\to s\). The special vertex \(s\) is a sinkhole, while \(r_1,r_2,a\) are ordinary.

For the origin test at \(x=a\):

- \([s,a]\) has first nonzero contribution at degree \(q\), with normalized q-defect \(P_E(a)\).
- \([r_1,a]\) has a nonzero degree-2 contribution because \(r_1\) and \(a\) are not adjacent.
- \([r_2,a]=1\) because \(r_2-a\) is an ordinary edge.

Hence
\[
[s+r_1,a]\notin D_q,
\]
so the lower-filtration profile rejects the apparent q-layer direction \(s+r_1\). This confirms the proposed mechanism: the q-layer projection alone can hide the lower obstruction, while the full filtered profile cannot.

However, this calculation also exposes a more important point. After quotienting only by the RP-3 origin sector \(O\), the ordinary directions \(r_1,r_2\) need not disappear. Thus the normalized profile need not affinely span the whole level set \(\omega_q=1\) in the ambient \(U\).

In particular, the profile sees the genuine sink direction \(s\), but it does not force any prescribed value on the transverse ordinary directions \(r_1,r_2\), which are canonically expected to lie in \(\ker\omega_q\).

Therefore the naive theorem
\[
\operatorname{Aff}(\mathcal S_q)=\omega_q^{-1}(1)\subset U
\]
is too strong in general. The quotient \(U/N_q\) is genuinely necessary.

## 4. Stronger mixed-component obstruction

Consider the disjoint union of a single special edge \(a\to s\) and an isolated ordinary vertex \(z\):
\[
\Gamma=(a\to s)\sqcup\{z\}_{\rm ord}.
\]
This is specially oriented. The literature explicitly allows disjoint unions of special graphs, and the associated group is the free pro-p product of the component groups.

Modulo the origin sector \(O=\mathbf F_p\bar a\), the relevant degree-one space contains \(\bar s\) and \(\bar z\). Against the origin \(a\),
\[
[\bar s,\bar a]\text{ has q-defect }P_E(a),
\qquad
[\bar z,\bar a]\text{ has degree-2 obstruction}.
\]
Therefore a vector \(\alpha\bar s+\beta\bar z\) is q-flat at \(a\) only when \(\beta=0\), and the normalized profile contains \(\bar s\) but no point with a nonzero \(\bar z\)-component.

Consequently every linear functional
\[
\omega_c(\alpha\bar s+\beta\bar z)=\alpha+c\beta,
\qquad c\in\mathbf F_p,
\]
agrees on the normalized filtered-profile locus \(\{\bar s\}\), although the canonical orientation has \(c=0\).

Thus **filtered q-profile alone does not uniquely determine \(\omega_q\) on all of \(U\)** once ordinary non-origin directions are present.

This is a genuine quotient-level obstruction, not a computational accident.

## 5. Isolated special vertex: boundary remains decisive

If an isolated vertex \(z\) is declared special, it has no special edge and hence no q-profile witness, but the canonical orientation still assigns \(\omega_q(z)=1\). Therefore a quotient defined merely by “profile-invisible directions” cannot satisfy
\[
N_q\subseteq\ker\omega_q
\]
on the unrestricted specially oriented class.

This is the same object-level obstruction already recorded at Gate D: the un-oriented finite window cannot distinguish isolated ordinary from isolated special status.

Hence the quotient theorem cannot be stated on the unrestricted class. A positive continuation must either:

1. restrict the admissible class so every special vertex is the terminus of at least one special edge; or
2. enrich the finite input by an orientation marking.

The first restriction is the current authorized mathematical boundary.

## 6. What survives

The dangerous long-chain mechanism does **not** produce a counterexample to the local implication
\[
[u,x]\in D_q
\quad\Longrightarrow\quad
c_x(u)=\omega_q(u)
\]
under the specially oriented sinkhole condition, provided the relevant quotient/domain and lift-independence are already legitimate.

Reason: in a specially oriented graph, a special vertex adjacent to an ordinary origin is necessarily joined to that origin by a special edge. A special vertex not adjacent to the origin contributes a degree-2/non-q obstruction. Ordinary neighbors contribute no q-defect. Thus, after lower-degree contamination is removed, the surviving q-coefficient is exactly the sum of visible special coefficients.

This is the correct structural explanation of the four local PASS/LOCAL models.

## 7. New exact boundary

The current evidence separates two statements:

### A. Local filtered-profile lemma
For a legitimate filtered profile, lower-degree vanishing forces support visibility, and the normalized q-defect equals the visible special coefficient sum.

**Classification: PASS / LOCAL.**

### B. Global quotient/uniqueness on all of U
The normalized profile does not determine \(\omega_q\) on all of \(U\) when ordinary non-origin directions are present.

**Classification: FAIL / CLOSED as stated.**

### C. Restricted quotient theorem
On the restricted class with no isolated special vertices, the remaining target is to construct an intrinsic, non-tautological \(N_q\) that removes ordinary/non-orientation directions and proves
\[
N_q=\ker\omega_q,
\qquad
U/N_q\cong\mathbf F_p,
\]
with the normalized q-profile inducing the unique nonzero functional on the quotient.

**Classification: OPEN / LOAD-BEARING.**

Importantly, \(N_q\) cannot be defined as the span of all q-invisible directions: in the separated two-sink model \(s+t\) is q-invisible under full flatness but \(\omega_q(s+t)=2\neq0\). Any valid \(N_q\) must be extracted from the *structure of lower obstructions together with their relations*, not from invisibility alone.

## 8. Immediate consequence for Gate D / T1

The filtered q-profile was not a return to an unrestricted carrier hunt. It has instead produced a sharper negative boundary:

\[
\boxed{
\text{full filtered profile}
\not\Rightarrow
\omega_q\text{ on the ambient }U
}
\]

without an additional quotient theorem.

The correct remaining theorem is therefore:

\[
\boxed{
\text{restricted finite window}
\longrightarrow
U/N_q
\xrightarrow{\;\overline\omega_q\;}
\mathbf F_p
}
\]

where \(N_q\) must be intrinsic, q-blind, functorial, non-tautological, and satisfy \(N_q\subseteq\ker\omega_q\).

## 9. Independent literature control

Blumer–Quadrelli–Weigel define specially oriented graphs by requiring the terminus of every special edge to be special, and explicitly allow isolated special vertices. They also define the canonical orientation as 1 on ordinary vertices and \(\lambda(1)\) on special vertices. Their results therefore support both parts of the boundary: the sinkhole mechanism used in the local lemma and the isolated-special Gate-D obstruction. See *Oriented Right-Angled Artin pro-ℓ Groups and Maximal Pro-ℓ Galois Groups*, Def. 2.5, Remark 2.4, and Thm. 4.9.

They also note that disjoint components give free pro-p products in the later directed-graph treatment, supporting the mixed-component test.

The literature does **not** provide the project-specific finite-window quotient theorem. No such implication is claimed here.

## 10. Authorized next attack

Do not search for another carrier.

The next single task is to define \(N_q\) from the *relations among lower-filtration obstructions*, not from q-invisibility alone, and test it first on:

1. the long ordinary chain \(r_1-r_2-a\to s\);
2. the mixed disjoint component \((a\to s)\sqcup\{z\}_{ord}\);
3. separated two-sink;
4. the chordal tree.

The test is decisive:

- if a non-tautological \(N_q\) survives all four and \(N_q\subseteq\ker\omega_q\), proceed to the quotient theorem;
- if the same construction forces an isolated/non-special direction into \(N_q\) with nonzero orientation mass, the quotient route is FAIL/CLOSED at the proposed definition.

Current classification:
- filtered lower-obstruction mechanism: **PASS / LOCAL**;
- ambient affine-hyperplane uniqueness: **FAIL / CLOSED**;
- unrestricted quotient uniqueness: **FAIL / CLOSED**;
- restricted quotient theorem: **OPEN / LOAD-BEARING**;
- Paper 4: **OPEN**.
