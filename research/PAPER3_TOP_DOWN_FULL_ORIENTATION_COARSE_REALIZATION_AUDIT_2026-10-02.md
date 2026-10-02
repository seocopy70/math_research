# TOP-DOWN FULL-ORIENTATION COARSE REALIZATION AUDIT — 2026-10-02

## 0. Decision

The T−1/T0 closure changes the target from recognition to **full finite-level orientation recovery**:
\[
W_k(G)\longmapsto [\chi_G\bmod p^k].
\]

At the declared standard odd-p fixed-rank Demuškin scope, the target has exactly **k distinct finite-level values** (for k≥2), represented by
\[
1,\quad (1-p)^{-1},\quad (1-p^2)^{-1},\ldots,\quad(1-p^{k-1})^{-1}
\pmod{p^k}.
\]
All q=p^s with s≥k, and q=0, give the same value 1.

This yields an information-theoretic lower bound on any full-orientation carrier: its set of isomorphism classes must have at least k target-distinguishable classes. In particular, the previously frozen one-dimensional \(\mathbf F_p\) cup-line selector cannot itself be a full \(\chi_k\)-carrier once k>p: it has only p elements. Its established role is recognition/selection, not full orientation encoding.

## 1. Target cardinality lemma

Let
\[
\Omega_k=\{[\chi_k(G)]:G\text{ in the standard odd-p fixed-rank family}\}.
\]

For q=0 or q=p^s with s≥k,
\[
\chi_k=1.
\]
For 1≤s<k,
\[
\chi_k(x_2)=(1-p^s)^{-1}\pmod{p^k}.
\]

If s≠t<k and
\[
(1-p^s)^{-1}\equiv(1-p^t)^{-1}\pmod{p^k},
\]
then multiplying by the units \((1-p^s)(1-p^t)\) gives
\[
p^s\equiv p^t\pmod{p^k},
\]
which is impossible for distinct s,t<k. Hence the k values are pairwise distinct.

Therefore
\[
|\Omega_k|=k.
\]

## 2. Universal lower bound for any full-orientation carrier

Suppose a finite carrier \(C_k\) is determined by \(W_k\) up to isomorphism and admits a map
\[
\Phi_k:\operatorname{Iso}(C_k)\to\Omega_k
\]
with
\[
\Phi_k(C_k(G))=[\chi_k(G)].
\]

Then \(\Phi_k\) must hit all k target values. Consequently
\[
|\operatorname{Iso}(C_k)|\ge k.
\]

This bound is independent of linearity, Fox presentations, relation modules, or the choice of construction. It is therefore stronger than the old “dimension ≥1” selector-minimality statement, but it is only an information-theoretic lower bound; it does not identify a canonical algebraic carrier.

For an \(\mathbf F_p\)-vector-space carrier V_k,
\[
p^{\dim V_k}\ge k,
\qquad
\dim V_k\ge\lceil\log_p k\rceil.
\]

For the active p=3 case, a 1-dimensional carrier has only 3 values, so it cannot encode the full orientation for k≥4.

## 3. Candidate exact coarsest finite realization

The audited Demuškin reconstruction gives an intrinsic q-detection mechanism: when q=p^s<N_k, the first q-dependent Zassenhaus graded relation defect occurs in degree q; when q≥p^k or q=0, the finite window has the stable branch.

Define the **defect-index carrier** \(D_k^{\mathrm{def}}\) by the finite-window isomorphism class of:
- s=1,…,k−1 if the first q-dependent defect occurs at degree p^s;
- s=∞ for the stable branch q=0 or q≥p^k.

This definition does not insert q or χ as input; it reads an intrinsic filtered/graded defect from W_k.

Its value set has exactly k classes, and the orientation functional is
\[
s\mapsto
\begin{cases}
(1-p^s)^{-1}\pmod{p^k},&1\le s<k,\\
1,&s=\infty.
\end{cases}
\]

Thus, **conditional on the already-audited q-reconstruction lemma**, \(D_k^{\mathrm{def}}\) realizes the information-theoretic lower bound exactly.

## 4. Critical novelty boundary

The exactness above is not automatically a new mathematical contribution.

For the standard odd-p Demuškin family, Labute/modern classification already treats (d,q) as the classification invariants, and the audited finite-window reconstruction recovers exactly the q-regime needed here. Hence \(D_k^{\mathrm{def}}\) is, at present, best understood as a **q-classification re-encoding** of the finite window.

Therefore:
- exact cardinality/coarseness at the information level: **PASS / LOCAL**;
- intrinsic defect-index realization: **PASS / LOCAL**, conditional on the audited reconstruction lemma;
- full-orientation factorization through the defect-index carrier: **PASS / LOCAL**;
- genuinely new theorem/non-redundancy: **FAIL / CLOSED** at the present standard-family scope, unless an additional structural consequence beyond q-classification is obtained.

This is an important boundary: the research has now separated **coarsest information** from **new mathematics**.

## 5. Consequence for the frozen cup-line

The one-dimensional cup-line \(C_k\) remains a valid recognition carrier under its declared selector category, but it should not be described as a carrier of the entire \(\chi_k\) once k>p.

For p=3:
- k=2,3: a 1D \(\mathbf F_3\)-space has enough raw cardinality to encode the target values, but the established selector theorem is not an orientation-encoding theorem;
- k≥4: cardinality alone rules out full orientation encoding by a single \(\mathbf F_3\)-line.

Thus the earlier selector-minimality theorem and the present full-orientation coarseness problem are logically distinct.

## 6. What remains genuinely open

The only potentially new route left at the declared scope is not “find a smaller carrier.” The lower bound is already sharp at the abstract finite-set level, and the natural exact realization is classification-equivalent.

A genuinely new result would need to do at least one of:

1. construct an intrinsic algebraic carrier with exactly k classes whose definition is visibly not a disguised q-classification invariant;
2. prove a structural theorem showing that a cohomological/filtered/deformation object is canonically equivalent to the defect-index carrier for a reason stronger than Demuškin classification;
3. enlarge the admissible class so that q no longer classifies the objects, while the same finite carrier still determines \(\chi_k\);
4. derive a new sharp observability theorem for a target other than the already-classified Demuškin orientation.

No large computation is justified before one of these novelty tests survives.

## 7. Classification

- target cardinality \(|\Omega_k|=k\): **PASS / CLOSED** at standard scope;
- universal carrier lower bound \(|\operatorname{Iso}(C_k)|\ge k\): **PASS / CLOSED**;
- vector-space lower bound \(\dim\ge\lceil\log_p k\rceil\): **PASS / CLOSED**;
- exact defect-index carrier: **PASS / LOCAL**;
- full-orientation factorization through it: **PASS / LOCAL**;
- genuinely new coarsest carrier theorem: **FAIL / CLOSED — classification re-encoding**;
- new carrier search at the same standard-family target: **OPEN**, but only if it passes the novelty test above.

## 8. Stop boundary

Do not reopen:
- Mixed Fox;
- \(\mathcal O_k\) universal/minimality;
- q=N_k;
- W_{11}/W_{12};
- Paper 2;
- the frozen cup-line proof.

The next authorized research branch, if continued, is an **adjacent-class/general-target test**, not another compression of q inside the standard Demuškin classification.
