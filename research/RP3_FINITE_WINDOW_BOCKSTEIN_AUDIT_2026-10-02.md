# RP-3 FINITE-WINDOW BOCKSTEIN AUDIT — 2026-10-02

## Verdict

The proposed RP-3 argument contains a valid local algebraic core, but the stated **PASS/LOCAL for finite-window factorization is not yet justified**. The correct surviving statement is a finite-window **liftability criterion for the kernel of the higher Bockstein**, not a proof that the full map
\(\beta_f:H^1(G,\mathbf F_p)\to H^2(G,\mathbf F_p)\)
is itself canonically reconstructible from \((W_q,W_{q+1})\).

## 1. What survives

For a specially oriented pro-p RAAG with sinkhole set \(S\), the minimal presentation relations imply
\[
G^{ab}\cong \mathbf Z_p^{V\setminus S}\oplus(\mathbf Z/p^f\mathbf Z)^S,
\qquad q=p^f.
\]
Thus the free/non-torsion and sinkhole/torsion decomposition of the abelianization is correct under the stated special-graph convention.

For the higher Bockstein, the cyclic model \(C_{p^f}\) has first nonzero higher Bockstein at level \(f\). More generally, the relevant \(\beta_f\) is the obstruction to lifting a mod-p character through the coefficient extension
\[
0\to \mathbf F_p\to \mathbf Z/p^{f+1}\to \mathbf Z/p^f\to0.
\]
This agrees with the standard higher-Bockstein/liftability description. See the literature check recorded below.

Consequently, in the specially oriented RAAG class,
\[
\ker\beta_f
=
\{\chi\in H^1(G,\mathbf F_p):\chi|_{(\mathbf Z/p^f)^S}=0\}.
\]
Equivalently, a mod-p character lies in \(\ker\beta_f\) exactly when it lifts to \(\mathbf Z/p^{f+1}\). This is the correct structural formulation.

## 2. Three local graph models

The complete 3-vertex, common-sink, and minimal non-complete examples all support the same abelianization-level conclusion. Their ordinary commutator structure does not alter the torsion/free decomposition of \(G^{ab}\).

So the local conclusion
\[
\ker\beta_f=\operatorname{span}\{\bar v^*:v\notin S\}
\]
is valid provided \(\beta_f\) is the standard higher Bockstein attached to the coefficient extension above.

However, this is not yet a finite-window theorem: it is an algebraic consequence of the known abelianization/presentation structure.

## 3. Critical correction: \(C_f\) is in the wrong space in the draft

If
\[
H^1(G,\mathbf F_p)=L_1^*,
\qquad L_1=G/D_2,
\]
then
\[
(\ker\beta_f)^\perp\subseteq L_1,
\]
not in \(L_1^*\).

Hence the literal statement
\[
C_f=\mathbf F_p\bar s^*
\]
is type-invalid under the declared annihilator notation. The corrected form is
\[
C_f=(\ker\beta_f)^\perp
=\operatorname{span}\{\bar s:s\in S\}\subseteq L_1.
\]
Only after choosing an auxiliary identification \(L_1\cong L_1^*\) could one write a dual-basis version, and that identification is not intrinsic.

## 4. Main gap: Step 5 overclaims what the finite window gives

The statement

> “\(\beta_f\) is determined by \(W_q\) and \(W_{q+1}\)”

is too strong as written.

The obstruction is that \(\beta_f\) lands in the global group cohomology \(H^2(G,\mathbf F_p)\), whereas \(W_{q+1}\) is only a finite filtered quotient. There is no automatic identification
\[
H^2(G,\mathbf F_p)\cong H^2(W_{q+1},\mathbf F_p),
\]
nor has the draft produced a natural map from the finite window whose value is literally \(\beta_f(\chi)\).

What can be proved directly is the weaker and exactly relevant statement:
\[
\chi\in\ker\beta_f
\iff
\chi\text{ lifts to }\mathbf Z/p^{f+1}.
\]

Moreover every homomorphism
\[
G\to\mathbf Z/p^{f+1}
\]
kills \(D_{q+1}(G)\), because the target is cyclic of order \(p^{f+1}\) and its Zassenhaus term \(D_{q+1}\) is trivial. Hence every such lift factors through
\[
W_{q+1}=G/D_{q+1}.
\]
Therefore the **liftability predicate** is visible at the adjacent finite window once the coefficient target \(\mathbf Z/p^{f+1}\) is specified.

This is the correct finite-window statement to attack.

## 5. q-blindness is not yet closed

The draft says the carrier is q-blind, but the proposed liftability formulation explicitly mentions \(p^{f+1}\), equivalently q.

That is not automatically fatal, because the window itself is indexed by \(q=p^f\). But under the project's stricter q-blindness rule, the carrier definition must not smuggle q in as a parameter.

Thus one must define a **uniform adjacent-window construction** for an arbitrary index n, and prove that at a p-power jump n=q it specializes to the desired liftability kernel without inserting q as external orientation data.

Current status: **OPEN / LOAD-BEARING**.

## 6. No Massey interference at the level actually needed

For the kernel-recognition problem, one does not need to identify the full \(H^2\)-class \(\beta_f(\chi)\). Higher Massey operations concern additional higher-order structure; they do not invalidate the elementary liftability criterion for \(\beta_f(\chi)=0\).

Therefore “Massey interference” should not be treated as a reason that the kernel calculation itself fails. It becomes relevant only if one tries to reconstruct the actual cohomology class \(\beta_f(\chi)\) or a richer carrier from finite filtered data.

## 7. Corrected target

The legitimate RP-3 target is:

> Construct a q-blind, intrinsic functor \(F\) of an adjacent finite Zassenhaus window such that
> \[
> F(W_q,W_{q+1})
> =
> (\ker\beta_f)^\perp
> \subseteq L_1,
> \]
> for every specially oriented pro-p RAAG with \(q=p^f\).

The natural candidate is the annihilator of the mod-p characters that admit a lift through the next p-power coefficient layer. The remaining theorem is to make this construction uniform, intrinsic, and q-blind.

## 8. Classification

- abelianization/free-vs-sinkhole decomposition: **PASS / LOCAL**;
- higher-Bockstein kernel characterization by liftability: **PASS / LOCAL**;
- three explicit graph models: **PASS / LOCAL**;
- \(C_f\) as written in \(L_1^*\): **FAIL / CLOSED — TYPE ERROR**;
- literal reconstruction of the full \(\beta_f\) from \((W_q,W_{q+1})\): **OPEN / NOT PROVED**;
- finite-window liftability predicate: **PASS / LOCAL**;
- q-blind uniform carrier: **OPEN / LOAD-BEARING**;
- general sinkhole-sector recovery from a q-blind adjacent-window carrier: **OPEN / LOAD-BEARING**;
- RP-3 overall: **OPEN / LOAD-BEARING**, not PASS/LOCAL.

## 9. Next authorized attack

Do not build Massey examples yet.

First prove the following uniform lemma:

For arbitrary \(n\), define an intrinsic adjacent-window liftability object from
\[
W_n=G/D_n,\qquad W_{n+1}=G/D_{n+1},
\]
without inserting q. Determine whether its specialization at \(n=p^f\) recovers
\((\ker\beta_f)^\perp\).

If this q-blind construction fails, seek a same-window counterexample. If it succeeds, then and only then test non-complete/multiple-sink configurations.

## Literature check

Higher Bockstein calculations for cyclic \(p\)-groups support the level indexing: for \(C_{p^f}\), the first nonzero higher Bockstein on the degree-one generator occurs at level f. A standard description identifies the corresponding obstruction with the failure of a mod-p character to lift to the next p-power coefficient layer. See the independent discussion of higher Bocksteins and the associated \(\mathbf Z/p^{f+1}\) central extension. citeturn0search0turn0search5

The Zassenhaus filtration is functorial and satisfies the standard power/commutator identities; in particular, maps to cyclic \(p\)-groups respect the filtration, which is the ingredient needed for the factorization of lifts through the adjacent finite quotient. citeturn1search0turn1search1

For specially oriented pro-p RAAGs, the literature gives the canonical orientation as 1+q on sinkholes and 1 on ordinary vertices, and defines special edges with the terminus at a special/sinkhole vertex. This supports the presentation convention used in the local checks. citeturn3search0turn3search2
