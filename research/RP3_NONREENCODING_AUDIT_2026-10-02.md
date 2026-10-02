# RP-3 NON-REENCODING AUDIT — 2026-10-02

## Scope

This audit tests whether the q-blind adjacent-window carrier
\[
\mathcal L(X,Y)=
\begin{cases}
\operatorname{im}\bigl(\operatorname{Hom}(Y,\mathbf Z/p^{e(Y)})\to
\operatorname{Hom}(Y,\mathbf F_p)\bigr),&e(Y)>e(X),\\
0,&e(Y)=e(X),
\end{cases}
\qquad e(Z)=\log_p\exp(Z^{ab}),
\]
is merely a re-encoding of the target, rather than an independently defined finite intrinsic object.

## 1. Object/Input

The carrier takes only an adjacent pair of finite p-groups \((X,Y)\), their abelianizations, the intrinsic exponents \(e(X),e(Y)\), Hom, and reduction modulo p. It does not take q, a presentation, a sinkhole set, a relator, or a Bockstein map as an argument.

The output is a subspace of \(H^1(Y,\mathbf F_p)\), equivalently a marked subspace of the degree-one quotient when the pair is a Zassenhaus window.

## 2. Intrinsicity and isomorphism covariance

An isomorphism of pairs \((X,Y)\cong(X',Y')\) induces an isomorphism of abelianizations, preserves exponent, and transports the Hom/reduction construction. Hence \(\mathcal L\) is invariant under finite-window isomorphism.

This is sufficient for the present intrinsicity claim. Full functoriality for arbitrary non-isomorphic pair morphisms is not claimed: the coefficient group \(\mathbf Z/p^{e(Y)}\) varies with the object, and Hom is contravariant. Thus the stronger categorical natural-transformation statement remains open/non-load-bearing.

## 3. Standard specially oriented RAAG specialization

For \(q=p^f\), with sinkhole set \(S\),
\[
G^{ab}\cong \mathbf Z_p^{V\setminus S}\oplus(\mathbf Z/q)^S.
\]
Consequently
\[
W_q^{ab}\cong(\mathbf Z/q)^V,
\qquad
W_{q+1}^{ab}\cong(\mathbf Z/pq)^{V\setminus S}\oplus(\mathbf Z/q)^S.
\]
Therefore
\[
\mathcal L(W_q,W_{q+1})
=\operatorname{span}\{\bar v^*:v\notin S\}
=\ker\beta_f,
\]
and
\[
\mathcal L(W_q,W_{q+1})^\perp
=\operatorname{span}\{\bar s:s\in S\}\subseteq L_1.
\]

The calculation uses only the abelianization structure; it is independent of the ordinary/special edge pattern beyond the induced special-vertex torsion/free decomposition.

## 4. Strong non-reencoding test

A genuine re-encoding of q would require the carrier's intrinsic isomorphism type to distinguish different q-regimes. It does not.

For fixed \(p\), fixed rank \(|V|\), and fixed number \(|S|=r\), the carrier at the jump has dimension
\[
\dim_{\mathbf F_p}\mathcal L=|V|-r,
\]
while its annihilator has dimension \(r\). These dimensions do not depend on \(f\) (hence not on q=p^f).

More strongly, after forgetting the ambient degree-one marking, all one-sink examples of the same rank give the same abstract carrier \(\mathbf F_p^{|V|-1}\), for every admissible \(q=p^f\). Thus the carrier does not itself encode the q-value or the orientation coefficient \((1-q)\bmod p^k\).

A fortiori, the carrier cannot by itself reconstruct the full \(\chi\bmod p^k\): distinct q-regimes can have isomorphic \(\mathcal L\). This is a feature, not a defect, because RP-3 now claims only recovery of the Bockstein kernel/its annihilator.

## 5. Target-relative non-redundancy

The carrier is nevertheless exactly the target subspace on the declared RAAG family:
\[
\mathcal L(W_q,W_{q+1})=\ker\beta_f.
\]
Hence it is not a new invariant independent of that target; it is a finite intrinsic realization of the target predicate. This should be described as a **recognition carrier**, not as a new independent global invariant.

The non-redundancy claim that is justified is narrower:
- the definition is not target-circular;
- the carrier is not a q-labelled presentation re-encoding;
- the carrier does not encode the full orientation coefficient;
- the carrier does exactly realize the kernel/annihilator target.

No absolute minimality or "coarsest possible" claim follows.

## 6. Smallest non-complete independent model

Take three vertices \(a,s,b\), with one special edge \((a,s)\), no edge involving \(b\), and \(s\) the special/sinkhole vertex:
\[
G=\langle a,s,b\mid sas^{-1}=a^{1+q}\rangle.
\]
Then
\[
G^{ab}\cong \mathbf Z_p\langle s\rangle
\oplus\mathbf Z_p\langle b\rangle
\oplus(\mathbf Z/q)\langle a\rangle.
\]
Hence
\[
W_q^{ab}\cong(\mathbf Z/q)^3,
\qquad
W_{q+1}^{ab}\cong(\mathbf Z/pq)^2\oplus\mathbf Z/q,
\]
and
\[
\mathcal L(W_q,W_{q+1})
=\operatorname{span}\{\bar s^*,\bar b^*\},
\qquad
\mathcal L^\perp=\mathbf F_p\bar a.
\]
Thus the carrier passes an independent non-complete graph check. The result is still local: it does not prove a graph-sensitive orientation theorem.

## 7. Multiple-sink check

If \(S=\{s_1,\ldots,s_r\}\), the same abelianization argument gives
\[
\mathcal L=\operatorname{span}\{\bar v^*:v\notin S\},
\qquad
\mathcal L^\perp=\operatorname{span}\{\bar s_1,\ldots,\bar s_r\}.
\]
No disjointness or uniqueness of special edges is needed for this abelianization statement. The carrier therefore survives the multiple-sink test at the level of the declared sinkhole sector.

The stronger question of recovering the directed incidence relation (which ordinary vertex points to which sinkhole) is not addressed by \(\mathcal L\) and remains a separate/open graph-sensitive problem.

## 8. All-sinkhole boundary

If \(V=S\), then both adjacent window abelianizations have exponent q:
\[
e(W_q)=e(W_{q+1})=f.
\]
Thus \(\mathcal L=0\), matching \(\ker\beta_f=0\). This confirms that the definition does not silently assume a nonempty free sector.

## 9. Final classification

- q-blind definition: **PASS / LOCAL**.
- finite-window isomorphism invariance: **PASS / LOCAL**.
- strong q-non-reencoding (carrier isomorphism type does not determine q): **PASS / LOCAL**.
- exact identification with \(\ker\beta_f\) on the declared specially oriented RAAG family: **PASS / LOCAL**.
- annihilator recovery of the sinkhole sector: **PASS / LOCAL**.
- smallest non-complete model: **PASS / LOCAL**.
- multiple-sink sinkhole-sector recovery: **PASS / LOCAL**.
- full categorical functoriality for arbitrary pair morphisms: **OPEN / NOT LOAD-BEARING**.
- full \(\beta_f\)-class reconstruction: **OPEN / NOT LOAD-BEARING**.
- full orientation reconstruction from \(\mathcal L\) alone: **FAIL / CLOSED**.
- absolute minimality/coarseness: **OPEN / NOT AUTHORIZED**.
- directed incidence recovery from \(\mathcal L\): **OPEN**.

## 10. Decision

RP-3 may legitimately advertise the result as an intrinsic q-blind finite-window **kernel/annihilator carrier**. It should not advertise it as a full Bockstein reconstruction, a full orientation reconstruction, a coarsest carrier, or a proof of graph-directed incidence recovery.

The next authorized research question is whether a genuinely graph-sensitive carrier can refine this abelianization carrier without re-encoding q or the presentation. This is a separate branch and must pass Object/Input/Functoriality/Gauge/Orientation-bridge/q-blindness/Separation/Novelty/Stop before substantial computation.
