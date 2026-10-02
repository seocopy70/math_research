# PAPER 3 FOLLOW-UP — 2-GENERATOR SPECIAL-EDGE MODEL AUDIT — 2026-10-02

## 0. Decision

The proposed 2-generator attack contains a genuine and useful boundary, but the claimed intrinsic role-recognition proof is **not yet valid as written**.

Model:
\[
G=\langle v,w\mid wvw^{-1}=v^{1+q}\rangle,qquad q=p^f.
\]

The robust conclusions are:

- For \(n\le q\), the special relation lies in the quotient kernel, so the finite window is q-blind at that level. This is a genuine **FAIL/CLOSED lower-bound mechanism** for detecting the q-dependent deformation.
- At \(n=q+1\), the element \(v^q=[w,v]\) first survives in the finite quotient. This is a **PASS/LOCAL first-survival fact**.
- The attempted formula
  \[
  \Delta_q=\operatorname{im}(\Lambda^2L_1\to L_q)
  \]
  is **type-invalid** for the ordinary associated graded restricted Lie algebra: the graded commutator of two degree-one classes lands in \(L_2\), not \(L_q\). For \(q>2\), the relation says that this degree-2 commutator vanishes in \(L_2\), while the same group element has a later class in \(L_q\). Extracting that later class requires additional filtered extension/relation-module data.
- Therefore the claimed intrinsic identity
  \[
  P_q^{-1}(\Delta_q)=\mathbf F_p\bar v
  \]
  is **not proved** by the displayed argument. The role-recognition gate remains **OPEN / LOAD-BEARING**, not PASS/LOCAL.
- Independently, the proposed automorphisms
  \[
  \phi_{a,c}(v)=v^a,\qquad \phi_{a,c}(w)=v^c w
  \]
  are genuine automorphisms of the 2-generator semidirect presentation. They exhibit a presentation/gauge freedom that changes the displayed orientation character. Thus bare abstract-group data cannot be assumed to recover a specific marked character without resolving the exact scope of the literature's orientation-uniqueness statement. This is a serious **Gauge/target-definition obstruction**.
- The exact statement "bare \(W_n\) cannot recover \(\theta\bmod p^k\)" is therefore retained as a **strong candidate no-go**, but the literature compatibility of this counterexample with the stated Kummerian uniqueness theorem must be checked before promoting it to a theorem-level global obstruction.

## 1. What survives unchanged

### 1.1 Lower bound

Since
\[
[w,v]=v^q\in D_q,
\]
for \(n\le q\) the quotient by \(D_n\) kills the q-dependent relation term. Hence the special-edge deformation is invisible at this depth.

Classification: **PASS / LOCAL** as a degree-of-first-survival statement; **FAIL / CLOSED** as a universal role-recognition theorem only if the intended conclusion is restricted to q-dependent deformation detection.

### 1.2 First survival

At \(n=q+1\),
\[
v^q\notin D_{q+1}
\]
provided its degree is exactly q in the intended model. Thus the q-dependent relation defect first appears in the finite quotient at this depth.

Classification: **PASS / LOCAL**.

## 2. Critical type correction

Let
\[
L_i=D_i/D_{i+1}.
\]
The restricted Lie bracket has type
\[
[-,-]:L_i\times L_j\to L_{i+j}.
\]
Consequently
\[
[\bar w,\bar v]\in L_2,
\]
not in \(L_q\).

For \(q>2\), the equality
\[
[w,v]=v^q
\]
implies that the class of \([w,v]\) in \(L_2\) is zero, because \(v^q\in D_q\subset D_3\). The nonzero class
\[
v^qD_{q+1}\in L_q
\]
is a **higher filtered defect** of the relation; it is not the ordinary graded bracket of \(L_1\).

Therefore the proposed map
\[
\Lambda^2L_1\longrightarrow L_q
\]
does not exist canonically from the restricted-Lie structure alone.

A correct replacement must be formulated on an intrinsic filtered relation-module/extension object of the truncated group, e.g. a canonical quotient measuring the failure of the degree-2 commutator relation to vanish one step further. The precise construction is still OPEN.

This correction is decisive because the entire line-recognition formula depended on identifying \(\Delta_q\) with an ordinary graded commutator image.

## 3. Gauge obstruction

For \(a\in\mathbf Z_p^\times\), \(c\in\mathbf Z_p\), define
\[
\phi_{a,c}(v)=v^a,\qquad \phi_{a,c}(w)=v^c w.
\]
Then
\[
(v^cw)v^a(v^cw)^{-1}=v^{a(1+q)},
\]
so the defining relation is preserved. These maps therefore give a large presentation/gauge automorphism family.

For the displayed character
\[
\theta(v)=1+q,\qquad\theta(w)=1,
\]
one has
\[
(\theta\circ\phi_{a,c})(v)=(1+q)^a,
\qquad
(\theta\circ\phi_{a,c})(w)=(1+q)^c.
\]
For \(c\not\equiv0\pmod p\), the second value differs from 1 modulo \(p^{f+1}\).

Hence a bare abstract group, and therefore a bare filtered window together with its abstract automorphisms, does not by itself fix the displayed generator-normalized orientation.

This does **not yet** settle the literature-level question of whether the relevant Kummerian/cyclotomic orientation is supposed to be unique as an abstract-group invariant or unique only relative to the oriented RAAG/digraph structure. That scope distinction must be resolved explicitly.

## 4. The p=3, q=3 stress test

For \(p=q=3\), the proposed threshold is \(4\).

At \(W_4\), the element \(v^3=[w,v]\) survives, but the ordinary graded structure only sees
\[
[\bar w,\bar v]=0\in L_2
\]
because the commutator has been pushed to degree 3.

Thus the concrete calculation does **not** by itself prove that \(\mathbf F_3\bar v\) is intrinsically recoverable from the graded object.

The automorphism
\[
v\mapsto v,\qquad w\mapsto vw
\]
does preserve the filtered group but changes the displayed character modulo 9:
\[
\theta(w)=1,qquad (\theta\circ\phi)(w)=4\pmod9.
\]
This is the cleanest gauge stress test.

## 5. Revised classifications

| Claim | Revised status |
|---|---|
| \(\deg_Z(v^q)=q\) | **PASS / CLOSED** |
| q-dependent relation invisible for \(n\le q\) | **PASS / LOCAL** |
| first survival at \(n=q+1\) | **PASS / LOCAL** |
| \(\Lambda^2L_1\to L_q\) as canonical graded map | **FAIL / CLOSED — type mismatch** |
| \(P_q^{-1}(\Delta_q)=\mathbf F_p\bar v\) | **OPEN — proof invalidated by type mismatch** |
| intrinsic sinkhole-line recognition at \(q+1\) | **OPEN / LOAD-BEARING** |
| \(\phi_{a,c}\) gauge family | **PASS / LOCAL** |
| exact marked \(\theta\bmod p^k\) from bare abstract window | **STRONG NO-GO CANDIDATE; literature-scope check required** |
| global special-RAAG orientation theorem | **OPEN** |
| threshold \(q+1\) as universal RAAG role-recognition threshold | **CONDITIONAL / OPEN** |

## 6. Consequence for the active Gate D / adjacent-class program

The branch is **not closed**, but the next step changes.

Do not claim that the 2-generator model has already proved intrinsic sinkhole recognition.

The authorized next attack is:

1. define the intrinsic filtered extension/relation-module object that contains the class of \(v^q\) at degree q;
2. determine its automorphism action;
3. test whether its preimage under the q-power operation canonically isolates the sinkhole line;
4. independently resolve whether the literature's "unique orientation" is invariant under the gauge automorphisms above;
5. only then decide whether the branch yields
   - **PASS/LOCAL** role recognition,
   - **FAIL/CLOSED** gauge no-go,
   - or **OPEN** intrinsic extension-class problem.

No larger RAAG computation is authorized before this 2-generator gate is resolved.

## 7. Global research interpretation

The useful conceptual split survives:

\[
\text{role/deformation recognition}
\neq
\text{canonical orientation recovery}.
\]

But the first half is not yet proved intrinsically. The correct boundary is now:

\[
\boxed{
\text{first q-defect survives at }q+1
\quad\text{but its intrinsic carrier is unresolved}
}
\]

and

\[
\boxed{
\text{a concrete gauge automorphism threatens exact orientation recovery from bare }W_n.
}
\]

This audit supersedes the stronger 2-generator claim that sinkhole-line recognition was already PASS/LOCAL.
