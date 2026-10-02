# PAPER 4 — T1 MULTI-SINK / SCALE-FIXING AUDIT — 2026-10-02

## Decision

The critical scale objection is real, but the common-sink and multi-sink calculation gives a stronger resolution than the previous 2-generator argument.

The finite window need not normalize a projective line by an arbitrary basis choice. It can, in the local special-edge model, **select the actual vector on that line**: the unique vector whose first q-defect against an intrinsic origin q-power equals the normalized generator q-power itself. Thus the scale is fixed by the extension data, not by an external basis rescaling.

This is PASS / LOCAL only. The remaining global issue is whether this local selection is intrinsic and whether multi-sink linear combinations are excluded.

## 1. Common-sink calculation

Take
  G=<v_1,...,v_m,w | [v_i,v_j]=1, w v_i w^{-1}=v_i^{1+q}>.

At degree one:
  L_1=<bar v_1,...,bar v_m,bar w>.

The origin sector is
  O_q=<bar v_1,...,bar v_m>,

so
  U_q=L_1/O_q=<bar w>.

The first q-defect satisfies
  B_q(bar w,bar v_i)=overline{v_i^q}
for every i.

Now replace bar w by lambda bar w, lambda in F_p^*. The defect becomes
  lambda overline{v_i^q}.

Since the q-power classes overline{v_i^q} are independently determined by the restricted-power structure of the origin sector, lambda=1 is forced by equality with the normalized q-power vector. Therefore the finite extension data distinguish the canonical vector bar w from its nonzero scalar multiples.

This resolves the specific 2-generator scale objection at the local level.

## 2. What the scale argument does NOT prove

It does not prove that the origin q-power class is itself canonically normalized in an arbitrary abstract window. The argument only shows:

  **conditional local statement:** once the intrinsic restricted-power target is identified, the special direction has a unique scale.

Thus the earlier status must be corrected from "2-generator normalization PASS / LOCAL" to:

  coefficient observability: PASS / LOCAL;
  scale fixing relative to intrinsic q-power target: PASS / LOCAL;
  existence of the intrinsic q-power target in the general T1 input: OPEN.

## 3. Multiple-sink control

Consider a specially oriented graph with distinct special vertices w_1,...,w_r and ordinary origin vertices. For each sink w_j choose an ordinary origin v_{j,a} with a special edge (v_{j,a},w_j). Assume initially that there are no cross-relations connecting distinct sink components; this is the minimal multi-sink control.

Modulo O_q, write
  U_q=span_Fp{bar w_1,...,bar w_r}.

For
  u=sum_j alpha_j bar w_j
and an origin direction v_{j,a}, the first q-defect has component
  alpha_j overline{v_{j,a}^q}.

If at least two alpha_j are nonzero and the corresponding q-power targets are independent, then the defect has rank at least two across the origin sectors. Hence the local special-edge signature, which requires a rank-one target aligned with one origin q-power sector, excludes generic sums of distinct sink directions.

Therefore the candidate set P_q can, in these controls, recover the individual normalized sink vectors rather than merely their span.

## 4. The key remaining ambiguity

There is one nontrivial possibility: two sink directions could share enough origin q-power target data that a linear combination still has rank-one defect.

This is not excluded by the abstract rank argument alone. It requires the actual graph/filtered structure to show that distinct sink directions have sufficiently independent origin sectors, or else a different intrinsic invariant must separate them.

Hence:
  rank-one accidental-direction exclusion: OPEN.

## 5. Symmetry / filtered-isomorphism test

Permuting two indistinguishable sink components preserves the set
  {bar w_1,...,bar w_r}
and also preserves the functional
  omega_q(sum alpha_j bar w_j)=sum alpha_j.

Thus graph automorphism symmetry does not create a normalization ambiguity: the desired functional is symmetric under sink permutation.

A dangerous filtered automorphism would instead have to send
  bar w_1 -> bar w_1 + c bar w_2
while preserving all first-defect data. In the minimal separated multi-sink model, the defect against an origin attached only to w_1 detects c, so such a shear is not an automorphism of the filtered pair. This is a useful local obstruction to GL_r gauge freedom.

## 6. Revised T1 formal statement

The correct target is now not "normalize a projective direction" but:

  **intrinsically identify the affine set of normalized sink vectors**
  S_q subset U_q

by the finite extension data, where each s in S_q is characterized by a rank-one special-edge defect whose target is a restricted-power class of O_q.

Then define omega_q by
  omega_q(s)=1 for all s in S_q.

The logical order is:

  W_q <- W_{q+1}
    -> O_q
    -> intrinsic q-power target(s)
    -> normalized sink vectors S_q
    -> omega_q.

No arbitrary basis normalization is allowed.

## 7. New failure criterion

T1 closes if either:

1. there exists a multi-sink model with an accidental normalized vector
   u not equal to a sink direction but having the same intrinsic rank-one special-edge signature; or
2. there are two specially oriented RAAGs with isomorphic adjacent windows for which the induced normalized sink-vector sets, hence omega_q, differ; or
3. the restricted-power target required to fix scale cannot itself be recovered q-blindly from the adjacent window.

The third condition is now the cleanest possible bottleneck.

## 8. Classification

- common-sink coefficient observability: PASS / LOCAL;
- common-sink scale fixing relative to q-power target: PASS / LOCAL;
- separated multi-sink rank test: PASS / LOCAL;
- sink permutation symmetry: harmless / PASS / LOCAL;
- shear-gauge obstruction in separated control: PASS / LOCAL;
- intrinsic q-power target in general window: OPEN / LOAD-BEARING;
- rank-one accidental-direction exclusion in general: OPEN / LOAD-BEARING;
- filtered-isomorphism invariance of S_q: OPEN / LOAD-BEARING;
- T1: OPEN / LOAD-BEARING.

## Next authorized attack

Do not return to 2-generator normalization or search for a new carrier.

The next decisive calculation is to construct the smallest **overlapping multi-sink model**, where two sinkholes share one or more origin sectors, and determine whether the intrinsic q-power targets remain separable. If an accidental rank-one direction appears, T1 closes. If not, the next task is the q-blind intrinsic construction of the target set S_q itself.


## 9. INTRINSIC q-POWER TARGET RECOVERED FROM THE ADJACENT WINDOW

The load-bearing target-definition question is resolved at the level needed by the scale argument.

Let an admissible adjacent window be
\[
E:\qquad 1\to A\to Y\xrightarrow{\pi}X\to1,
\]
with \(X=W_q,\;Y=W_{q+1}\) in the target class. Define \(e(X):=\exp(X)\). This is an intrinsic invariant of the finite group \(X\), so the construction does not insert the parameter \(q\).

For the Zassenhaus window \(W_q=G/D_q\), \(D_1^q\le D_q\), hence \(\exp(W_q)\mid q\). In the declared specially oriented RAAG class the degree-one quotient contains elements of exact \(q\)-height, so at the relevant jump \(e(W_q)=q\).

Put \(L(X):=X/\Phi(X)\cong D_1/D_2\) and \(A=\ker\pi\). Define
\[
\boxed{
P_E:L(X)\longrightarrow A,\qquad
P_E(\bar x)=\tilde x^{\,e(X)}
}
\]
where \(\tilde x\in Y\) is any lift of \(x\in X\).

### 9.1 Well-definedness

If \(\tilde x'=\tilde x a\) with \(a\in A=D_q/D_{q+1}\), then \(A\) is central in \(Y\), \(A\) has exponent \(p\), and \(p\mid e(X)=q\). Hence \((\tilde x a)^q=\tilde x^q\).

If \(x'=xd\) with \(d\in\Phi(X)=D_2/D_q\), choose a lift of \(d\) in \(D_2/D_{q+1}\). The Zassenhaus restricted-Lie \(p\)-operation gives the canonical iterated map
\[
L_1=D_1/D_2\longrightarrow L_q=D_q/D_{q+1},
\qquad
\bar x\longmapsto \bar x^{[q]},
\]
and by definition \(\bar x^{[q]}=x^qD_{q+1}\). Therefore changing the representative modulo \(D_2\) does not change the class.

The underlying structural fact is standard: the Zassenhaus quotients \(D_n/D_{n+1}\) form a restricted \(\mathbf F_p\)-Lie algebra and the \(p\)-operation is induced by group \(p\)-th powers. citeturn6search12turn6search14

Hence \(P_E\) is a well-defined intrinsic map determined by the adjacent finite pair.

### 9.2 No hidden basis or generator choice

The construction uses only the finite group \(X\), its Frattini quotient, the finite central kernel \(A=\ker(Y\to X)\), the intrinsic exponent \(e(X)\), and the group power operation in \(Y\). No generator, section, presentation, basis, orientation, or displayed \(q\) occurs in the definition.

Thus the previous bottleneck has a concrete answer:
\[
\boxed{
P_E(\bar x)=\tilde x^{\,\exp(X)}\in\ker(Y\to X).
}
\]

### 9.3 Relation to the local targets

In the 2-generator special-edge model,
\[
P_E(\bar v)=\overline{v^q},\qquad
B_q(\bar w,\bar v)=\overline{v^q}.
\]

In the common-sink model,
\[
P_E(\bar v_i)=\overline{v_i^q},\qquad
B_q(\bar w,\bar v_i)=\overline{v_i^q}.
\]

Therefore the scale equation is intrinsic:
\[
B_q(u,\bar v)=P_E(\bar v).
\]
For \(u=\lambda\bar w\), whenever \(P_E(\bar v)\ne0\),
\[
\lambda=1.
\]

### 9.4 Limitation

This does **not** prove T1. It proves only that the required q-power target exists intrinsically. It does not yet prove accidental-direction exclusion, spanning/recognition of \(S_q\), or full adjacent-window naturality. Also, \(P_E\) need not be linear on arbitrary \(L_1\); it is the iterated restricted-power operation.

## 10. Revised classification

- intrinsic q-power target \(P_E\): **PASS / LOCAL**;
- q-blind definition of \(P_E\) via \(\exp(X)\): **PASS / LOCAL**;
- target equality with local extension defect: **PASS / LOCAL** in audited 2-generator/common-sink models;
- scale fixing relative to \(P_E\): **PASS / LOCAL**;
- overlapping multi-sink accidental direction: **OPEN / LOAD-BEARING**;
- filtered-isomorphism invariance of \(S_q\): **OPEN / LOAD-BEARING**;
- T1: **OPEN / LOAD-BEARING**.

## 11. Immediate consequence

The study is **not** returning to carrier hunting. The target-first chain is now
\[
W_q\leftarrow W_{q+1}
\Longrightarrow O_q
\Longrightarrow P_E
\Longrightarrow S_q
\Longrightarrow\omega_q.
\]

The next authorized attack is the smallest overlapping multi-sink configuration.
