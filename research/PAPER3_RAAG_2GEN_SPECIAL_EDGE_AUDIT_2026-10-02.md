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


## 8. CRITICAL CORRECTION — GAUGE TEST REPAIRED BY THE LITERATURE'S ORIENTATION CONVENTION

A further literature check changes the previous gauge conclusion.

For the 2-generator special-edge model
G=<v,w | w v w^{-1}=v^{1+q},
the **special/sinkhole vertex is w**, not v. This follows directly from the standard oriented pro-p RAAG convention: for a special edge e=(v,w), the relation is w v w^{-1}=v^{lambda(1)}, while the canonical orientation assigns theta(v)=1 and theta(w)=lambda(1). The original draft had the vertex labels reversed. The source explicitly gives this 2-generator example and states that the resulting pair is theta-abelian. See Blumer–Quadrelli–Weigel, Theorem 4.9 and Example 4.3. 

Therefore the correct canonical orientation is
theta(v)=1, theta(w)=1+q,
not theta(v)=1+q, theta(w)=1.

Under the gauge automorphisms
phi_{a,c}(v)=v^a, phi_{a,c}(w)=v^c w,
one now has
(theta o phi_{a,c})(v)=1,
(theta o phi_{a,c})(w)=1+q,
because theta(v)=1. Hence this family **does not change the canonical orientation**.

This removes the previously claimed orientation no-go from this model. It also resolves the apparent contradiction with the literature's uniqueness theorem: Kummerianity is invariant under isomorphism of oriented pro-p groups, and the literature indeed states that for a specially oriented graph there is a unique torsion-free orientation making the pair Kummerian, namely the canonical orientation. The gauge family is compatible with that uniqueness precisely because it fixes theta.

Consequently:
- the earlier "gauge/shear changes theta" claim is **REJECTED / SUPERSEDED**;
- the 2-generator model does **not** currently provide a no-go for exact orientation recovery;
- any remaining obstruction must come from the finite-window carrier failing to recover the canonical oriented-pair structure, not from an automorphism of the full group changing the canonical orientation.

## 9. Relation module / H^2 correction

For the minimal pro-p presentation F=<v,w> -> G with relator
r=[w,v]v^{-q},
the relation subgroup R=ker(F->G) is normally generated by r. The standard relation-module object is the abelianization R/[R,R] with its G-action. For a minimal presentation, the mod-p relation module is dual to H^2(G,F_p) in the usual presentation-cohomology correspondence. General references define the pro-p relation module as R/[R,R] with conjugation action; see the relation-module literature.

However, the key filtration point is:
r has **initial Zassenhaus degree 2**, because [w,v] has degree 2 while v^q has degree q>=p>=2. Thus H^2(G,F_p) sees the degree-2 initial relation, not the higher q-correction. In particular, H^2 alone cannot be used as a direct carrier of the q-dependent coefficient 1+q.

The q-dependent information lives in the **higher filtered correction**
r [w,v]^{-1}=v^{-q}
(or equivalently the difference between the relator and its degree-2 initial form). This is precisely why the required object is a filtered relation-module/extension defect rather than bare H^2.

## 10. P_q status

The restricted p-operation gives a canonical map
P_q=(−)^{[p^f]}:L_1 -> L_q.
Its existence is clear. What remains unresolved is whether, in the truncated filtered group W_{q+1}, the image P_q(L_1) carries an intrinsic substructure singled out by the higher relation defect.

The naive construction
Delta_q=im(Lambda^2 L_1 -> L_q)
remains invalid. A valid replacement must use the filtered relator/extension class. No PASS is claimed here.

## 11. Revised final classifications

| Claim | Status |
|---|---|
| q-defect invisible for n<=q | PASS/LOCAL |
| first survival at n=q+1 | PASS/LOCAL |
| ordinary Lambda^2 L_1 -> L_q carrier | FAIL/CLOSED — TYPE MISMATCH |
| P_q itself | PASS/CLOSED as a restricted-power map |
| intrinsic role recognition at q+1 | OPEN/LOAD-BEARING |
| relation-module definition R/[R,R] | PASS/CLOSED |
| H^2 as direct q-defect carrier | FAIL/CLOSED |
| filtered relation/extension defect as q-carrier | OPEN |
| phi_{a,c} changes canonical theta | FAIL/CLOSED — label/orientation convention was reversed |
| gauge automorphism preserves canonical theta | PASS/CLOSED |
| exact orientation recovery from bare W_n | OPEN |
| theorem-level orientation no-go | FAIL/CLOSED as unsupported by this model |

This correction supersedes the gauge-obstruction portion of the earlier audit, while retaining the type-mismatch and filtered-extension problems.
