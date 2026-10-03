# PAPER 4 — B-ATTACK RECONCILIATION: THE “K_n / H^2 / FAIL” ENDPOINT IS NOT VALID
## 2026-10-03

### Trigger
A proposed continuation of the W10 Gate-B attack attempted to replace the remaining quotient-map orbit problem by a global computation of the kernel K_n, its module structure, and H^2(Q_n,K_n), and concluded “Reconstruction FAIL (high probability)” and “Separation FAIL”.

That endpoint was independently audited against the authoritative W10 audit and the research continuity protocol.

### Pre-check
- **Object:** unmarked filtered finite group W_n; target is the relative obstruction after forgetting the marked map pi_n:W_n -> Q_n.
- **Input:** abstract filtered W_n only.
- **Functoriality:** any accepted reconstruction must be Aut(W_n)-natural; quotient-map choices are gauge.
- **Orientation bridge:** must recover the relative extension class, not merely a presentation relator.
- **Separation:** requires the same underlying W with genuinely different marked quotient/obstruction data.
- **Stop rule:** unsupported kernel/module formulas or cohomology dimension statements cannot be promoted to a reconstruction/no-go theorem.

### Corrections to the proposed B endpoint

1. **The asserted exact structure of K_n was not established.**
   The displayed identification of the nonabelian kernel K_n with a simple group-ring quotient, followed by an asserted abelian decomposition
   K_n^{ab} ~= Z/p^{e_1} direct-sum Z/p^{e_2},
   was not derived from the actual relation-module sequence. Fox derivatives generate a relation-module presentation; they do not by themselves identify the kernel as the displayed abelian group.

2. **The group-ring calculation used an invalid simplification.**
   Q_n is nonabelian in general, so replacing Z_p[Q_n] by a truncated polynomial/cyclotomic calculation in independent commuting generators z,x_i is not legitimate. Moreover, the augmentation and cyclotomic factors of z^{p^n}-1 are not comaximal over Z_p, so the asserted integral CRT splitting is not available in that form.

3. **The claimed cyclic/direct-sum Q_n-module structure is therefore unproved.**
   The subsequent claims about Aut_{Q_n}(K_n), scalar/diagonal automorphisms, and the exact automorphism structure of W_n do not follow.

4. **H^2(Q_n,K_n) != 0 does not imply multiple quotient kernels.**
   Nonzero H^2 classifies extension classes with a fixed kernel module and quotient, up to the appropriate equivalence. It does not imply that a fixed W_n contains two distinct normal subgroups N_1 != N_2 with W_n/N_i ~= Q_n. The latter is exactly the quotient-map orbit problem and requires an explicit construction or a theorem.

5. **The proposed “Separation FAIL because the same W gives the same extension class” is logically false.**
   An abstract isomorphism W_1 ~= W_2 does not identify the marked quotient maps pi_1,pi_2. Even for one fixed W there may be several epimorphisms W -> Q with different kernels. This is precisely why the current Gate-B target is the Aut(W) x Aut(Q) orbit of admissible quotient maps.

6. **Therefore the claimed final classification is withdrawn.**
   The statements “Reconstruction FAIL (high probability)”, “Separation FAIL”, and “Intrinsic factorization impossible” are not theorem-level conclusions and must not enter the paper or authoritative state.

### What survives

The authoritative W10 correction remains controlling:
- cup-radical line: PASS / LOCAL;
- H^1 quotient data: PASS / LOCAL;
- explicit family pi_c(z)=c, pi_c(x)=x, pi_c(y)=y for c in D_2(Q_10): PASS / LOCAL;
- full quotient-map orbit uniqueness: OPEN / LOAD-BEARING;
- same-window separation with different obstruction: OPEN;
- unmarked reconstruction: OPEN / LOAD-BEARING.

The family pi_c is legitimate because for c in D_2(Q_10), c^9 lies in D_18(D), hence is trivial in Q_10. This shows concretely that H^1-level uniqueness is insufficient.

### Stronger reduction obtained from the graded structure

For the rank-two p=3 Demushkin quotient, the initial quadratic relation is [X,Y]=0 in the associated restricted Lie algebra. Thus the first potentially nontrivial part of D_2(Q_10) occurs one Zassenhaus step later, and the critical residual of pi_c should first be tested in the finite graded layer
D_3(Q_10)/D_4(Q_10).
For the rank-two surface/restricted-Lie model this layer is controlled by the p-powers X^[3],Y^[3]. This is the correct finite-dimensional first-order IA orbit test; it is strictly smaller and more faithful than the unsupported global K_n/H^2 calculation.

This reduction is a **LOAD-BEARING subproblem**, not a result of transitivity or separation. It must be computed before any full orbit claim.

### Classification
- proposed K_n exact decomposition: **FAIL / CLOSED as a proof route**;
- proposed H^2 => multiple quotient kernels implication: **FAIL / CLOSED**;
- proposed “same W => same obstruction” argument: **FAIL / CLOSED**;
- W10 explicit quotient family: **PASS / LOCAL**;
- first graded IA orbit test in D_3/D_4: **OPEN / LOAD-BEARING**;
- full quotient-map orbit uniqueness: **OPEN / LOAD-BEARING**;
- same-window separation: **OPEN**;
- intrinsic reconstruction: **OPEN / LOAD-BEARING**.

### Next authorized action
Do not reopen radical, critical-jet, scalar/norm, degree-5, or carrier branches.

The single next calculation is:
\[
\boxed{
\text{compute the Aut(W_{10}) x Aut(Q_{10})-orbit of the family }\pi_c
\text{ first in }D_3(Q_{10})/D_4(Q_{10}),
}
\]
including the exact image of radical-preserving IA shears from W_{10}. If this first graded orbit already separates 0 from a nonzero class invariantly, Gate-B closes negatively; if it is transitive, lift the orbit test one Zassenhaus layer and only one layer at a time, with a predeclared stop.

This replaces the unsupported “Reconstruction FAIL (high probability)” endpoint.
