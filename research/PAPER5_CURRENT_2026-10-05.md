# Paper 5 — Current State (2026-10-06)

## Classification
**OPEN / LOAD-BEARING.**

Paper 5 is the finite Zassenhaus-window automorphism-structure programme. The former compression/trichotomy programme is HISTORICAL / SUPERSEDED.

## 2026-10-06 decisive boundary closure

The corrected intrinsic boundary theorem at n=p is **PASS / CLOSED / GENERAL** for odd p in the declared presentation scope.

At n=p,
D_p(W_p)=<X,Y,Z> ≅ F_p^3, with X=x^p, Y=y^p, Z=z^p, D_p central of exponent p, and
[x,y]=XZ^{-1}.

For g in Aut(W_p), write modulo D_2:
g(x) ≡ x^m y^u z^c, g(y) ≡ x^b y^v z^d, g(z) ≡ z^a.
Comparison in the independent X,Y,Z basis gives
u=0, v=1, c=a-m, with m,a nonzero. Hence
Im(Aut(W_p)->GL(V)) = S'_11(p),
where
S'_11(p) = { [[m,b,0],[0,1,0],[a-m,d,a]] : m,a in F_p^*, b,d in F_p }.
Its order is p^2(p-1)^2.

The substitutions
x -> x^m z^(a-m), y -> x^b y z^d, z -> z^a
realize every element. Also
IA(W_p) ≅ Hom(F_p^3,F_p^3) ≅ F_p^9,
so
|Aut(W_p)| = p^11(p-1)^2.

The earlier D_p ≅ F_p^2, S_11, and IA ≅ F_p^6 packages are HISTORICAL / SUPERSEDED.

## Boundary n=p+1

W_{p+1}=W_p, so the same automorphism theorem holds at n=p+1:
|Aut(W_{p+1})|=p^11(p-1)^2.
Classification: PASS / CLOSED / GENERAL.

## Local computation

Run 37381098677:
- p=5,n=6=p+1,(s,a)=(0,1);
- candidate order 2000;
- actual order 2000;
- equal=true.

Classification: PASS / LOCAL only. This confirms the already-closed boundary theorem because W_6=W_5; it is not a general proof.

## 2026-10-06 stabilization-lemma audit: second repair rejected

The original stabilization proof failed at \(D_p\subseteq M_{p+1}\). The subsequent repaired route correctly established the \(D_c^p\) and lower-central absorption sublemmas, but its final equality still failed because \(D_{k+1}\subseteq M_{p+1}\) gives only \(M_{k+1}\subseteq M_{p+1}\), not the reverse inclusion.

A further proposed repair via
\[
J_aI\subseteq J_{a+1}R+J_aI^2
\]
is now FAIL / CLOSED as a general lemma. The elementary-abelian counterexample \(G=C_p^2\), \(a=1\), gives \(J_1=I,\ J_2=0\), so the claim would force \(I^2\subseteq I^3\), which is false. The group-algebra identity also leaves a \(g(x-1)\in J_a\) term that is not shown to lie in \(J_aI^2\). The proposed Lemma D additionally uses a \(J\)-versus-\(I\) inclusion not previously established, making that induction circular.

Detailed audit: research/PAPER5_ZASSENHAUS_STABILIZATION_AUDIT_2026-10-06.md.

## What remains open

The arbitrary-n extension is OPEN / LOAD-BEARING because the reverse inclusion (M_{p+1}subseteq M_{k+1}) is still unproved.
Im(Aut(W_n)->GL(V)) ?= S'_11(p), or the correct n-dependent intrinsic replacement.

The previous B,theta attempt to force a uniform flag and P=lambda_s I+N from
B(gbar x,gbar y)=gbar_U B(x,y)
is FAIL / CLOSED as submitted. The U_n-action moves simultaneously, so B-equivariance alone does not force the required flag/Jordan form.

The free-lift objection is withdrawn. For a given g in Aut(W_n), a free lift tilde-g is available; the unresolved issue is not lifting g, but extracting a uniform intrinsic constraint on gbar from relation preservation. This is distinct from lifting an arbitrary M in GL(V).

Therefore the remaining proof problem is specifically the uniform U_n-action control needed to turn the intrinsic B,theta equations into a flag constraint and then a normal form such as P=lambda_s I+N, if that statement is true.

## Result classification

| Item | Classification |
|---|---|
| n=p boundary theorem | PASS / CLOSED / GENERAL |
| D_p(W_p) ≅ F_p^3 | PASS / CLOSED / GENERAL |
| IA(W_p) ≅ F_p^9 | PASS / CLOSED / GENERAL |
| Im at n=p = S'_11(p) | PASS / CLOSED / GENERAL |
| |Aut(W_p)| = p^11(p-1)^2 | PASS / CLOSED / GENERAL |
| W_{p+1}=W_p | PASS / CLOSED / GENERAL |
| n=p+1 automorphism theorem | PASS / CLOSED / GENERAL |
| Run 37381098677 | PASS / LOCAL |
| arbitrary-n B,theta proof as submitted | FAIL / CLOSED |
| proposed Zassenhaus stabilization proof | FAIL / CLOSED |
| implication W_{p+1}=W_p => W_n=W_p for all n>=p | OPEN / LOAD-BEARING |
| arbitrary-n uniform U_n-action control | OPEN / LOAD-BEARING |
| arbitrary-n Frattini-image theorem | OPEN / LOAD-BEARING |
| Paper 5 arbitrary-n END | NOT YET |
| Paper 5 full arbitrary-n END | NOT YET |

## Authorized next action

Do not run another blind prime/numerical sweep.

The stabilization pre-Gate remains OPEN / LOAD-BEARING. Do not integrate an arbitrary-n theorem yet.

If uniform U_n-control fails, classify that route FAIL / CLOSED rather than weakening the statement silently. If it succeeds, it becomes the load-bearing arbitrary-n theorem route.

## Repository anchors

- corrected n=p closure: research/PAPER5_WP_CORRECTED_STRUCTURE_STEP3_CLOSURE_2026-10-06.md
- previous Step 3 failure audit: research/PAPER5_STEP3_EQUALITY_AUDIT_2026-10-05.md
- P5-JET correction: research/PAPER5_JET_S11_JACOBSON_CORRECTION_AUDIT_2026-10-05.md
- IA/GL gate and runtime audits: research/PAPER5_IA_GL_*.md


## 2026-10-06 — Fourth stabilization audit: R-containment premise rejected

The latest proposed closure assumes that (W_p=F/(R D_{p+1})) being exponent (p) and class (p) forces (F^p,gamma_{p+1}subseteq R). This is false from the Paper 5 definition: the conclusions are only (F^p,gamma_{p+1}subseteq R D_{p+1}). The literature audit does not add the stronger containments as hypotheses. Therefore the proposed (M_{p+1}subseteq M_{k+1}) argument remains **OPEN / LOAD-BEARING**, and (W_n=W_p) for all (nge p) remains **OPEN / LOAD-BEARING**.


## 2026-10-06 — Explicit-R Lie-induction proposal rejected

The explicit relation subgroup
[
R=langle[x,z],[y,z],[x,y]^{-1}x^pz^{-p}angle^F
]
does give
[
operatorname{gr}_2(R)=operatorname{gr}_2(F)
]
and closes the one-step boundary (W_{p+1}=W_p). However, the attempted extension to all (k) via
[
operatorname{gr}_{k+1}(F)=[operatorname{gr}_k(F),operatorname{gr}_1(F)]
]
is invalid for the full Zassenhaus graded object: (operatorname{gr}(F)) is a free **restricted** Lie algebra, with independent (p)-power layers. The bracket induction controls only the ordinary Lie-bracket part and does not establish equality of all restricted layers.

The separate (D_{p+1}) calculation does not supply arbitrary-degree restricted (p)-power control. Hence the all-(n) stabilization implication remains **OPEN / LOAD-BEARING**.

This supersedes the session-level proposal to promote (W_n=W_p) from the explicit-R argument.


## 2026-10-06 — Decisive restricted-(p)-power obstruction

The proposed necessary repair
[
(*)qquad F^psubseteq R,D_{p+1}(F)
]
fails for the explicit relation subgroup
[
R=langle[x,z],[y,z],[x,y]^{-1}x^pz^{-p}angle^F.
]
Use the quotient (phi:F	omathbb Z_p) with (x,zmapsto t) and (ymapsto1). All three generators of (R) map to (1), while (x^pmapsto t^p
otin D_{p+1}(mathbb Z_p)=mathbb Z_p^{p^2}). Hence
[
x^p
otin R D_{p+1}(F).
]
Thus the degree-(p) restricted (p)-power layer is genuinely not absorbed by (R).

This closes the proposed ((*))-repair route. It does **not yet** prove strict shrinkage (W_{p^2}subsetneq W_p); that requires an explicit witness in the relevant quotient. The arbitrary-(n) stabilization theorem therefore remains **OPEN**, but its current Lie-induction route is now **FAIL / CLOSED**.


## 2026-10-06 — All-n stabilization definitively refuted by p^2 witness

The explicit relation subgroup
\[
R=\langle[x,z],[y,z],[x,y]^{-1}x^pz^{-p}\rangle^F
\]
admits a strict denominator witness:
\[
x^{p^2}\in RD_{p+1}\setminus RD_{p^2+1}.
\]
Indeed \(x^{p^2}\in F^{p^2}\subseteq D_{p+1}\), while the homomorphism
\[
\phi:F\to\mathbf Z_p,qquad x,z\mapsto t, y\mapsto1
\]
kills \(R\) and sends \(x^{p^2}\) to \(t^{p^2}\notin D_{p^2+1}(\mathbf Z_p)=\mathbf Z_p^{p^3}\).

Hence
\[
RD_{p^2+1}\subsetneq RD_{p+1}.
\]
The all-\(n\) stabilization claim is therefore **FAIL / CLOSED**, and the arbitrary-\(n\) theorem is no longer an open stabilization problem.

Important quotient-direction correction: since the denominator shrinks, the quotient grows. There is a canonical strict epimorphism
\[
W_{p^2}=F/(RD_{p^2+1})\twoheadrightarrow W_p=F/(RD_{p+1})=W_{p+1},
\]
rather than an inclusion \(W_{p^2}\subsetneq W_p\). “Strict shrinkage” is the shrinkage of the defining normal subgroup.

The earlier OPEN status and the rejected Lie-induction routes are superseded by this explicit counterexample.


## 2026-10-06 — General-n strict-shrinkage / Aut audit

The generalization of the explicit witness is closed, but the proposed complete Aut(W_n) formula is not.

**PASS / CLOSED / GENERAL (explicit R):** for every k>=1, with R=<[x,z],[y,z],[x,y]^{-1}x^p z^{-p}>^F and phi(x)=phi(z)=t, phi(y)=1,
 x^{p^k} in F^{p^k} subseteq D_{p^{k-1}+1} subseteq R D_{p^{k-1}+1},
while phi(x^{p^k})=t^{p^k} is not in D_{p^k+1}(Z_p)=Z_p^{p^{k+1}}. Hence RD_{p^k+1} is a proper subgroup of RD_{p^{k-1}+1}, giving strict canonical epimorphisms W_{p^k} ->> W_{p^{k-1}}. This is the correct general strict-shrinkage theorem.

The following upgrades are **not closed**:
- W_n/Phi(W_n) ~= F_p^3 under R subseteq Phi(F) is closed, but this does not imply constant Im(Aut(W_n)->GL(V)).
- D_{k+1}(W_n) is a Zassenhaus/Jennings term, not a standard Frattini-series term.
- The witness line <x^{p^k}> does not prove Phi(W_{p^k}) is a direct product extension of Phi(W_{p^{k-1}}), nor that the quotient kernel has order exactly p.
- G_n=G_p for all n>=p remains **OPEN / LOAD-BEARING**: higher relation/extension constraints can change which V-linear maps lift.
- IA(W_n) ~= Hom(V,Phi(W_n)) is **FAIL / CLOSED as a general identification**; only suitable central elementary-abelian layers admit such Hom/derivation descriptions.
- The proposed exact sequence K_{p^k} -> K_{p^{k-1}} is not established; an automorphism of W_{p^k} need not descend unless the quotient kernel is characteristic/preserved.
- Schur-Zassenhaus does not yield Aut(W_n)=K_n semidirect G_p because G_p may contain p-torsion (the current S'_11(p) does).

Classification: strict denominator chain = PASS/CLOSED/GENERAL; W_n non-stabilization = PASS/CLOSED/GENERAL in the witnessed sense; constant Frattini quotient = PASS/CLOSED under the stated hypothesis; constant Frattini-image = OPEN/LOAD-BEARING; exact +3 kernel-growth law = OPEN/LOAD-BEARING; Hom identification = FAIL/CLOSED; Schur-Zassenhaus split = FAIL/CLOSED.

Research consequence: stabilization is finished negatively. The next authorized problem is the independent arbitrary-n Frattini-image/IA-layer structure, without promoting G_n=G_p or K_{p^k}/K_{p^{k-1}} ~= F_p^3.

## 2026-10-06 — Gate 1 power-kernel proposal rejected

The proposed domino starting from
\[
K_k=RD_{p^{k-1}+1}/RD_{p^k+1}=W_{p^k}^{p^k}
\]
is **FAIL / CLOSED as submitted**.

The decisive checks are:

1. At (k=1), the first kernel already spans the surviving (p)-power layer \(\langle x^p,y^p,z^p\rangle\cong\mathbf F_p^3\) in the closed (W_p) boundary theorem, so the blanket claim (A_k\cong\mathbf F_p) is false if (k=1) is included.
2. (D_{p^k+1}(W_{p^k})=1) does **not** imply that (D_{p^{k-1}+1}(W_{p^k})) is central. Its commutators only move to (D_{p^{k-1}+2}), which is generally still nontrivial modulo (D_{p^k+1}).
3. The quotient (D_{p^{k-1}+1}/D_{p^k+1}) spans many Zassenhaus degrees and includes restricted (p)-power layers. The assertion that (R) kills every non-(F^{p^k}) contribution is precisely an unproved (R)-versus-Zassenhaus-layer comparison.

Therefore the following are **not promoted**: characteristicity of (K_k), the induced Aut descent, (G_{p^k}=G_p), the +3 exact sequence, the (p^{3k+C}) formula, and the semidirect-product formula.

The strict denominator chain remains **PASS / CLOSED / GENERAL**. The correct next gate is the actual graded/commutator structure of
\[
RD_{p^{k-1}+1}/RD_{p^k+1},
\]
with the possibility that a characteristic **top (p^k)-power sublayer**, rather than the whole kernel, is the right object.

Detailed audit: research/PAPER5_GATE1_POWER_KERNEL_AUDIT_2026-10-06.md.


## 2026-10-06 — Top central layer audit

Correction: characteristicity of K_k and existence of the induced Aut map are CLOSED by functoriality of the Zassenhaus filtration. The top layer C_k=D_{p^k}(W_{p^k}) is also characteristic and central.

The proposed identification C_k = <x^(p^k), y^(p^k), z^(p^k)> = F_p^3 is NOT CLOSED. The phi witness x,z -> t, y -> 1 detects only the x/z diagonal direction; a second abelian witness detects y, so independence of three directions is not proved. The proposed containment R >= gamma_2(F)^p gamma_p(F) is not available, and the non-homogeneous relation carries higher filtered information.

The +9 IA law is NOT CLOSED either: centrality gives an ambient Hom(V,C_k), but extension-class preservation can make the actual kernel smaller and lifting to the lower IA group is not automatic.

Detailed audit: research/PAPER5_GATE1_TOP_LAYER_AUDIT_2026-10-06.md.


## 2026-10-06 — Gate 1 b-unipotent lift obstruction CLOSED

The proposed next test (b:x\mapsto xy, y\mapsto y, z\mapsto z) at (W_{p^2}) has a direct abelianization obstruction for every odd (p).

Let
\[
R=\langle[x,z],[y,z],[x,y]^{-1}x^pz^{-p}\rangle^F,
\qquad W_{p^2}=F/(RD_{p^2+1}).
\]
The map (F\to\mathbf Z_p=\langle t\rangle) defined by
\[
x\mapsto1,\quad z\mapsto1,\quad y\mapsto t
\]
kills (R). Hence (y^p\notin RD_{p^2+1}), because its image is (t^p\notin D_{p^2+1}(\mathbf Z_p)=\mathbf Z_p^{p^3}).

Now apply the proposed substitution to the defining relation. In the abelianization of (W_{p^2}), the relation gives (x^p=z^p). Its image under (x\mapsto xy) is
\[
(xy)^p z^{-p}=x^py^pz^{-p}=y^p,
\]
which is nonzero. Therefore (b) does not preserve the defining relation and cannot induce an automorphism of (W_{p^2}).

Thus the specific (b)-unipotent element present in (G_p) is absent from (G_{p^2}):
\[
\boxed{b\in G_p\setminus G_{p^2}}.
\]
Consequently
\[
\boxed{G_{p^2}\subsetneq G_p},
\]
so the hypothesis (G_\infty=G_p) is **FAIL / CLOSED**. Eventual stabilization remains **PASS / CLOSED**, but its stable subgroup is strictly smaller than (G_p).

What is *not* proved: the exact identity of (G_\infty) (e.g. a diagonal torus), the fate of the other unipotent (d), and the exact (G_{p^2}) or (G_\infty) subgroup. Those remain OPEN.

A separate notation correction is required: reserve (C_k) for the characteristic descent kernel (D_{p^{k-1}+1}(W_{p^k})) only; call the top central layer (T_k:=D_{p^k}(W_{p^k})). Also, the right map \(\operatorname{Aut}(W_{p^k})\to\operatorname{Aut}(W_{p^{k-1}})\) is not asserted surjective; the displayed sequence is exact only through the kernel unless surjectivity is proved. Finally, because (C_k) is generally nonabelian, its kernel description is a nonabelian crossed-homomorphism/derivation problem; the formula \(3\dim C_k^{W}+\dim Z^1\) is not currently justified and must not be promoted.

Classification:
- (b:x\mapsto xy) lift to (W_{p^2}): **FAIL / CLOSED / GENERAL**;
- (G_{p^2}\subsetneq G_p): **PASS / CLOSED / GENERAL**;
- (G_\infty=G_p): **FAIL / CLOSED**;
- exact (G_\infty) identification: **OPEN / LOAD-BEARING**;
- exact (K_{p^k,p^{k-1}}) / crossed-derivation dimension: **OPEN / LOAD-BEARING**.


## 2026-10-06 — Post-stabilization direction correction: persistence/global-image route

The negative stabilization result is now treated as final for the explicit relation model: the denominator chain is strictly descending along (p^k), and (G_{p^2}subsetneq G_p) via the closed (b:xmapsto xy) obstruction. Therefore the former objective “prove (G_n=G_p)” is abandoned rather than repaired.

### Global image lemma

Let (G=arprojlim_n W_n) be the corresponding pro-(p) quotient, with the finite windows cofinal in the defining filtration. The inverse-limit restriction map identifies
[
operatorname{Aut}(G)congarprojlim_n operatorname{Aut}(W_n)
]
under the standard compatible-window hypotheses. Since the relevant linear image at the first window is finite, the descending sequence of finite-level images stabilizes; the stabilized image is the image induced by (operatorname{Aut}(G)). Equivalently, with
[
G_infty:=operatorname{Im}igl(operatorname{Aut}(G)	o GL(H^1(G,mathbf F_p))igr),
]
the stable finite-level image is (G_infty).

Classification: **PASS / CLOSED** as a short inverse-limit/Mittag-Leffler auxiliary lemma under the stated cofinal-window hypotheses. This is not the load-bearing theorem of Paper 5.

### Central-boundary model versus the audited ((s,a)) family

A numerical mismatch previously noticed between
[
|S'_{11}(p)|=p^2(p-1)^2
]
for the corrected central-boundary model (W_p), and the audited ((s,a)) gate values, is **not to be called an arithmetic contradiction**.

They refer to different presentation/model data unless an explicit identification is supplied. In particular, the corrected (W_p) theorem uses the central boundary relations
[
[x,z]=[y,z]=1,qquad [x,y]=x^p z^{-p},
]
whereas the audited ((s,a)=(1,1)) family uses a different presentation (for example, at (p=3,n=4),
[
G_{1,1}=langle z,x,ymid z^3=x^3[x,y]angle
]
in the recorded computation), with no prior theorem identifying (z) as central in the ambient presentation.

Therefore a dedicated **model/index correspondence table** is required before comparing gate orders.

Known audited values that must remain distinct:
- central (W_p) boundary image: (p^2(p-1)^2);
- actual ((s,a)=(1,1)) gate: (6) at (p=3), (20) at (p=5);
- p=3 additional audited gates: ((0,1)=108), ((0,2)=864), ((1,2)=48).

Classification: **OPEN** model/index correspondence. No value is to be reinterpreted by silently identifying the two models.

### Cohomological upper-bound candidate

For the global ((1,1))-type relation, the independently computed mod-(p) data are
[
omega=x^*wedge y^*,qquad
eta(lambda)=(lambda(x)-lambda(z)),eta.
]
The radical is
[
operatorname{rad}(omega)=langle zangle,
]
so the (z)-line is intrinsically characterized by the cup product. The stabilizer of the pair ((omega,eta)) has order
[
p(p-1),
]
and is isomorphic to the affine group ( mathbf F_ptimesmathbf F_p^	imes).

The correct proposed implication is therefore
[
operatorname{Im}igl(operatorname{Aut}(G)	o GL(H^1(G,mathbf F_p))igr)
subseteq
operatorname{Stab}(omega,eta),
]
not an equality with the central-boundary group (S'_{11}(p)).

The numerical match
[
p=3: 6,qquad p=5: 20
]
with the actual ((1,1)) gates is strong evidence but is **not itself a proof of equality**.

Classification:
- (operatorname{Im}(operatorname{Aut}(G)	o GL(H^1))subseteqoperatorname{Stab}(omega,eta)): **OPEN / LOAD-BEARING candidate** until the naturality/derivation argument is written and independently checked.
- (|operatorname{Stab}(omega,eta)|=p(p-1)): **PASS / LOCAL** until the full algebraic calculation is entered as a theorem-level proof.
- Equality with the stabilizer: **OPEN**.

### Window indexing correction

Because
[
W_{p+1}=W_p,
]
the first genuinely new window after the closed boundary is (n=p+2), not (p+1). Any persistence experiment must therefore distinguish (p), (p+1), and (p+2) explicitly.

### Methodological prohibitions carried forward

- Do not form (G_k/G_{k+1}) without proving normality.
- Do not use failure of one chosen free lift as a finite-level image obstruction; use the lift-independent/coset-wide relation obstruction.
- Do not assume ordinary or higher Bockstein data classify all deeper windows without an explicit bridge theorem.
- The amalgam/root-extension interpretation suggested by (z^p=[x,y]^{-1}x^p) remains **OPEN**; canonicality of such a decomposition is not established.
- No blind (p,n) sweep is authorized before the model/index table and the cohomological stabilizer gate are fixed.

### Authorized next gate

**P5-MODEL-1:** build the explicit model/index correspondence table (presentation, (s,a), (n), window, relator, gate order).

Then **P5-COH-1:** prove and independently verify the intrinsic cohomological upper bound and compute
[
operatorname{Stab}(omega,eta)congmathbf F_ptimesmathbf F_p^	imes.
]

Only after these gates pass should a targeted (p=3, n=5,ldots,8) persistence experiment be considered.


## 2026-10-07 — Gate B B4 p=3, a=2: D3–D9 full ideal audit and exact-factorization pivot

A follow-up audit corrected the previously omitted degree-3 check for the nontrivial scalar case (p=3,a=2), with (W=z^2). The degree-3 component satisfies
\[
(W^3-X_2)_3\in I_3,
\]
with Gaussian-elimination ranks
\[
\operatorname{rank}(I_3)=7,
\qquad
\operatorname{rank}(I_3+(W^3-X_2)_3)=7.
\]
The structural degree-3 cancellation is consistent with the relation component: although the isolated commutator direction is not itself in the relevant truncated ideal, the combination with the quadratic relation component is. In particular, no standalone implication such as ([z^3,x]=1\Rightarrow[z,x]=1) is used or claimed.

Together with the existing exact two-sided ideal calculations for (N=4,5,6,7,8,9), this gives the corrected finite-window statement
\[
\boxed{(W^3-X_2)_N\in I_N\quad(3\le N\le9)}.
\]
Hence the Magnus evidence yields
\[
E_2=z^6x^{-6}[x^2,y]^{-1}-1\in N D_{10}
\]
for the tested truncation. This is **PASS / LOCAL**, not an exact normal-closure proof.

The tempting implication
\[
E_2\in N
\iff
[[X,Y],X]\in N\,G^3
\]
is therefore promoted only as the **next exact algebraic target**, not as an established equivalence. Any use of Hall–Petresco must keep the distinction between a commutator lying in (G^3N) and the exact identity ( [[x,y],x]\in N); centralizing (x^3) does not by itself centralize (x).

### Classification
- (p=3,a=2,W=z^2), full two-sided ideal membership (D3\text{–}D9): **PASS / LOCAL**.
- (E_2\in N D_{10}): **PASS / LOCAL** (finite truncation consequence).
- (E_2\in N): **OPEN / LOAD-BEARING**.
- Exact normal-closure factorization of (E_2) through the defining relators (r^{w_i}): **OPEN / LOAD-BEARING**.
- Gate B: **OPEN / LOAD-BEARING**.

### Authorized next action
Do **not** spend the next step on (D_{10}) alone. Construct an exact finite product of conjugates of the defining relator (or an exact normal-closure identity) proving (E_2\in N), or derive a rigorous obstruction to such a factorization. Preserve the (D3\text{–}D9) computation as local evidence and do not promote it to a pro-(3) lifting theorem.


## 2026-10-07 — Corrected p=3,a=2 group-level D6 realization

The fixed seed W=z^2 full non-homogeneous ideal obstruction at T=4 remains valid. A new corrected construction instead parameterizes Phi(x),Phi(y),Phi(z) by actual group elements (products of basic commutators), with linear part diag(2,1,2). This automatically enforces the group-like condition and solves the coupled relation-preservation equations at the group level.

Reported finite result: D3 weight-2 candidates = 729; D4 survivors = 81; D5 survivors = 27; D6 admits explicit solutions from D5 candidates 3,4,5,8,14. An independent slower dictionary-algebra check of candidate 3 reproduces zero residual through D6.

Classification: **PASS / LOCAL** for the p=3,a=2 finite group-level realization through D6. **Gate B remains OPEN / LOAD-BEARING** because no all-degree compatible pro-3 lift has been proved. The intermediate 4,782,969-solution enumeration is excluded from evidence.

Evidence: research/PAPER5_GATE_B_P3_A2_GROUP_LEVEL_D6_AUDIT_2026-10-07.md.

The Labute/Kochloukova–Zalesskii literature check did not identify a direct prescribed-diagonal automorphism theorem. Labute's relator-equivalence theorem is relevant methodology but does not by itself close the present Gate B; the amalgam/root-extension reduction remains OPEN.

Authorized next action: compare the five D6 solutions' weight-2/weight-3 parameters before any D7/D8 expansion.
