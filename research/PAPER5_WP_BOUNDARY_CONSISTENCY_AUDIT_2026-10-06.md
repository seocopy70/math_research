# Paper 5 — W_p boundary consistency audit — 2026-10-06

## Verdict

**FAIL / CLOSED as submitted.** The proposed Step 3 upper-bound proof is algebraically inconsistent with its own stated (W_p) relations.

The critical incompatible pair is
[
D_p(W_p)=\mathbf F_p^2=\langle x^{[p]},y^{[p]}\rangle,
qquad x^{[p]}=z^{[p]},
]
together with
[
[x,y]=x^p z^{-p}.
]
If (D_{p+1}(W_p)=1), then these are equalities in (W_p), hence
[
[x,y]=x^p z^{-p}=1.
]
Therefore the later calculation
[
[x^m y^u,x^b y^v]
=x^{p(mv-bu)}z^{-p(mv-bu)}
]
cannot be used as a comparison of independent (x^p,z^p) coordinates: the displayed element is already (1).

## 1. Exact point where the submitted coefficient comparison fails

The submitted proof equates
[
x^{p(mv-bu)}z^{-p(mv-bu)}
=
x^{pm}y^{pu}z^{p(c-a)}
]
and then extracts separately
[
u=0,qquad mv=m,qquad c=a-m.
]

That extraction requires (x^p,y^p,z^p) to be independent in (D_p(W_p)). It is incompatible with the simultaneously asserted relation (x^p=z^p).

If (x^p=z^p), the equality reduces instead to
[
1=x^{pm}y^{pu}z^{p(c-a)}
=y^{pu}x^{p(m+c-a)},
]
so the only coefficient conclusions available from the stated package are
[
u=0,qquad c=a-m
]
(after using the asserted independence of (x^p) and (y^p)). There is no valid route to (mv=m), hence no valid deduction (v=1).

## 2. Structural correction

For the presentation-level relation actually recorded in the Paper 5 audits,
[
[x,y]=x^p z^{-p},
]
the relation does **not** imply (x^p=z^p). Rather, it identifies the commutator with the difference of the (p)-power classes:
[
[x,y]=x^p z^{-p}.
]

At (n=p), (D_p) must therefore be re-derived from the actual finite quotient before any dimension or IA-order statement is promoted. In particular, the package
[
D_p\cong\mathbf F_p^2,quad x^p=z^p,quad IA(W_p)\cong\mathbf F_p^6
]
is not established by the current presentation and is incompatible with the coefficient comparison used for the proposed upper bound.

## 3. Consequences

The following submitted claims are **FAIL / CLOSED as submitted**:

- (D_p(W_p)=\mathbf F_p^2) with (x^p=z^p), when used together with ([x,y]=x^p z^{-p}) as the defining relation package.
- The deduction (m_{y,x}=0, m_{y,y}=1, c=a-m) from the displayed coefficient comparison.
- (operatorname{Im}=S'_{11}(p)).
- (IA(W_p)\cong\mathbf F_p^6) unless independently re-derived from the correct (D_p(W_p)).
- (|\operatorname{Aut}(W_p)|=p^8(p-1)^2).

The previously established explicit (S'_{11}) lower-bound family should also be rechecked against the **correct** (W_p) structure before retaining it as a theorem-level lower bound.

## 4. Required next gate

Recompute, from the actual quotient
[
W_p=F/(R D_{p+1}),qquad
R=\langle[x,z],[y,z],[x,y]^{-1}x^p z^{-p}\rangle^F,
]
the intrinsic structure of:

1. (D_2(W_p));
2. (D_p(W_p));
3. (Z(W_p));
4. (W_p^{ab}) and its torsion subgroup;
5. (IA(W_p)=\ker(\operatorname{Aut}(W_p)\to GL(V))).

Only after these are independently established may the (S'_{11}) upper-bound calculation be restarted.

**No equality/order theorem is promoted at this checkpoint.**
