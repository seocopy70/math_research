# PAPER 3 — RAAG S2 ABELIANIZATION SUPPORT THEOREM — 2026-10-02

## Decision

The previously declared S2 load-bearing problem can be reduced much further for **special pro-p RAAGs**. The proposed statement that abelianization only gives a control invariant is too pessimistic.

For the modern digraph definition used by Quadrelli (2024/2025), a special vertex is the second coordinate of a special edge, hence every special vertex is a genuine sinkhole in a special digraph. In this setting, the finite-window abelianization canonically separates the special/sinkhole subspace from the ordinary subspace whenever (q=p^f<p^k).

This yields a candidate **PASS / CLOSED** theorem for the orientation bridge, subject to the precise window convention and the elementary abelianization calculation below.

## 1. Literature correction that matters

The 2024/2025 directed-graph formulation defines a special vertex as the second coordinate of a special edge. A special vertex (w) is a sinkhole when every vertex joined to (w) points to (w); a digraph is special when every special vertex is a sinkhole.

Thus, in the scope relevant to this branch, there are no isolated “special” vertices carrying the canonical nontrivial orientation. The older 2023 terminology allowed an isolated special vertex in its partition, but that case is not the current sinkhole formulation and must not be silently mixed into the present theorem.

The canonical orientation is
[
	heta_Gamma(v)=
egin{cases}
1+q,&v	ext{ is a sinkhole},\
1,&v	ext{ is not a sinkhole}.
end{cases}
]

Literature: Quadrelli, *Directed graphs, Frattini-resistance, and maximal pro-p Galois groups*, J. Pure Appl. Algebra 229 (2025), 107857; and Blumer–Quadrelli–Weigel, *Oriented right-angled Artin pro-ell groups and maximal pro-ell Galois groups*.

## 2. Exact abelianization of a special oriented pro-p RAAG

Let (G=G_{Gamma,q}), with (q=p^f), and let
[
V=V_osqcup V_s
]
be the ordinary/special vertex partition.

The defining relations are:
- ordinary edge: ([w,u]=1);
- special edge ending at (u): ([w,u]=u^q).

After abelianization, ordinary-edge relations disappear, while every special-edge relation gives
[
u^q=1.
]

Since every special vertex is the endpoint of a special edge, and no ordinary vertex is the endpoint of a special edge, the natural presentation gives
[
G^{ab}cong
mathbb Z_p^{,|V_o|}
oplus
(mathbb Z_p/qmathbb Z_p)^{,|V_s|}
=
mathbb Z_p^{,|V_o|}
oplus
(mathbb Z/p^f)^{,|V_s|}.
]

This is the crucial point omitted by the previous S2 analysis.

## 3. Finite-window abelianization

Set
[
N_k=p^{k-1}+1,qquad
W_k=G/D_{N_k+1}.
]

For (kge2), and also for (pge3,k=1), the image of (D_{N_k+1}) in an abelian pro-p group is the (p^k)-power subgroup, because
[
N_k+1=p^{k-1}+2>p^{k-1}
quad	ext{and}quad
N_k+1le p^k.
]

Hence
[
(W_k)^{ab}
cong
(mathbb Z/p^k)^{|V_o|}
oplus
(mathbb Z/p^{min(f,k)})^{|V_s|}.
]

The exceptional (p=2,k=1) case has trivial orientation modulo (2) anyway and should be treated separately rather than folded into the formula.

## 4. Canonical torsion support

Assume now
[
q=p^f<p^k.
]

Define, intrinsically from the finite abelian group
[
A_k=(W_k)^{ab},
]
the subgroup
[
T_{k}^{<k}
=
A_k[p^{k-1}]
=
{ain A_k:p^{k-1}a=0}.
]

Because the ordinary summand has exponent exactly (p^k), while the special summand has exponent (p^fle p^{k-1}),
[
T_k^{<k}
=
(mathbb Z/p^f)^{|V_s|}
]
inside (A_k).

Thus (T_k^{<k}) is exactly the special/sinkhole abelianization submodule.

This is fully intrinsic: it uses only the abstract finite group (A_k), not a generating set, presentation, graph, or relation basis.

## 5. Recovery of the sinkhole support in degree one

Let
[
overline T_k
=
T_k^{<k}/pT_k^{<k}.
]

Then
[
overline T_k
cong
mathbb F_p^{,|V_s|}.
]

Under the canonical identification
[
H_1(W_k,mathbb F_p)
cong
A_k/pA_k,
]
the subspace (overline T_k) is the image of the special/sinkhole vertices.

Equivalently, after duality, its annihilator/corresponding quotient gives an intrinsic decomposition of the degree-one character space.

Therefore the previously sought object
[
mathcal S_q(W_k)subseteq H^1(W_k,mathbb F_p)^ee
]
can be defined without commutator-depth at all:
[
oxed{
mathcal S_q(W_k)
:=
T_k^{<k}/pT_k^{<k}
subseteq H_1(W_k,mathbb F_p).
}
]

This is presentation-free.

## 6. Recovery of q

If (T_k^{<k}
eq0), its exponent is exactly
[
exp(T_k^{<k})=p^f=q.
]

Therefore (q) itself is intrinsically recovered from (W_k) whenever (q<p^k) and at least one sinkhole exists.

If (T_k^{<k}=0), the finite window sees no nontrivial special support and the canonical orientation is trivial.

If (qge p^k), the special summand has exponent (p^k), so the finite abelianization cannot distinguish special from ordinary. But this is precisely the regime where
[
1+qequiv1pmod{p^k},
]
so the target orientation is already trivial modulo (p^k).

Thus the apparent loss of q information is harmless for the orientation theorem.

## 7. Recovery of the finite orientation

For (q<p^k), define
[
ar	heta_k:W_k	o(1+pmathbb Z_p)/(1+p^kmathbb Z_p)
]
by its factorization through (A_k), sending:
- the canonical special/torsion support to (1+q);
- the complementary ordinary quotient to (1).

Because the special support is intrinsic and (q) is its exponent, this definition is invariant under every abstract isomorphism
[
W_k(G_{Gamma,q})cong W_k(G_{Delta,r}).
]

Hence, if both sides have nontrivial visible special support,
[
q=r
]
and
[
[	heta_{Gamma,q}mod p^k]
=
[	heta_{Delta,r}mod p^k]
]
after transport by the induced abelianization isomorphism.

If one or both q-values are (ge p^k), the finite orientations are trivial and equality holds automatically.

## 8. The orientation does not need the commutator-depth support

This is the major simplification.

The previous proposed route was
[
W_k
	o
	ext{degree-q commutator defect}
	o
	ext{sinkhole support}
	o
	heta.
]

For the special RAAG scope, the shorter route is
[
oxed{
W_k
	o
(W_k)^{ab}
	o
T_k^{<k}
	o
mathcal S_q(W_k)
	o
[	hetamod p^k].
}
]

The degree-q commutator defect remains a useful secondary invariant and may explain why the torsion appears, but it is not load-bearing for orientation recovery.

## 9. Important scope limitation

This result depends critically on the **special-digraph/sinkhole hypothesis**.

If the branch is enlarged to arbitrary oriented/directed RAAGs, special vertices need not be sinkholes and the clean torsion-support argument no longer identifies the canonical orientation. In fact, the literature gives non-special examples with substantially different torsion behavior.

Therefore the theorem must not be stated for arbitrary oriented RAAGs.

## 10. Consequence for S1

The orientation bridge no longer requires full finite-window graph recovery.

Even if
[
W_kRightarrowGamma
]
has not been proved, the orientation can already be recovered from the abstract finite-window abelianization within the special scope.

Thus:
- S1 remains a separate graph-reconstruction question.
- S2 orientation recovery can be closed without S1.
- The implication needed for the project's orientation bridge is stronger than the previous route suggested.

## 11. Exact gate classification

- Zassenhaus degree (q): **PASS / CLOSED**.
- Special relation ([w,u]=u^q): **PASS / CLOSED**.
- Candidate threshold (N_k=p^{k-1}+1): **PASS / LOCAL**, with the finite-window abelianization calculation supporting the threshold for the orientation bridge.
- Intrinsic q recovery from finite-window abelianization, (q<p^k): **PASS / CLOSED** for special digraphs.
- Intrinsic sinkhole/special support recovery: **PASS / CLOSED** for special digraphs.
- (W_kRightarrow[	hetamod p^k]): **PASS / LOCAL → candidate PASS / CLOSED**, pending a line-by-line formalization of the finite abelianization lemma and the (p=2,k=1) boundary case.
- S1 graph reconstruction: **PASS / LOCAL**, independent of the orientation bridge.
- Commutator-depth support: **REDUNDANT for the orientation bridge**, retained as secondary structural information.
- Full finite-window graph + orientation reconstruction: **OPEN**, because graph reconstruction remains separate.
- Presentation-level sinkhole identification: **FAIL / CLOSED**.

## 12. Next verification target

The next proof should not attack relation modules or Massey products first.

It should formally prove the lemma:

[
oxed{
(W_k(G_{Gamma,q}))^{ab}
cong
(mathbb Z/p^k)^{|V_o|}
oplus
(mathbb Z/p^{min(f,k)})^{|V_s|}
}
]

in the special-digraph scope, including the precise (p=2) boundary.

Then prove functorially:
[
T_k^{<k}=A_k[p^{k-1}]
]
is preserved by abstract isomorphisms and equals the special/sinkhole summand.

Once this is written cleanly, the S2 gate can be promoted from OPEN to PASS/CLOSED.

## 13. Research interpretation

This is a stronger result than the original S2 plan.

The finite-window orientation is not hidden in a delicate degree-q relation-module defect. It is already encoded in the **torsion-length stratification of the finite abelianization**.

So the current research frontier changes from

[
	ext{“find the intrinsic support of the q-defect”}
]

to

[
oxed{
	ext{“prove the finite-window abelianization lemma rigorously and close S2.”}
}
]

This is a materially simpler and more robust route. The commutator-depth branch should not be promoted to a theorem until it is needed for some result not already supplied by abelianization.
