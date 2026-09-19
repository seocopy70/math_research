# Rank-4 D4 IA Quotient-Legitimacy / Equivariance Audit — 2026-09-19

## Status

**LOCAL SUB-GATE PASS / MAIN DEFINITION GATE REMAINS OPEN**

This audit tests equivariance of the first-layer IA variation space and the ordinary correction space under the frozen tensor action. It is not a rank-4 representative scan.

## 1. Frozen spaces

Degree-3 associative Magnus target:
[
A_3cong mathbf F_3^{4otimes3},qquad dim A_3=64.
]

Ordinary correction space:
[
C_3=operatorname{span}{[X_i,R_2]}_{i=1}^4,qquad dim C_3=4.
]

First IA variation space:
[
Delta_{mathrm{IA}}subset A_3,qquad dimDelta_{mathrm{IA}}=20.
]

Combined candidate gauge space:
[
G_3=C_3+Delta_{mathrm{IA}},qquad dim G_3=20.
]

Hence the candidate quotient has dimension 44.

## 2. Sp4 transvection audit

Using the frozen alternating form corresponding to
[
R_2=[X_1,X_2]+[X_3,X_4],
]
all 80 nonzero-vector symplectic transvections of (operatorname{Sp}_4(mathbf F_3)) were tested.

Results:

- every transvection preserves (C_3);
- every transvection preserves (Delta_{mathrm{IA}});
- every transvection preserves (G_3=C_3+Delta_{mathrm{IA}}).

Exact bad-counts:

[
oxed{
N_{mathrm{bad}}(C_3)=
N_{mathrm{bad}}(Delta_{mathrm{IA}})=
N_{mathrm{bad}}(G_3)=0.
}
]

Thus the 44-dimensional candidate quotient carries the frozen tensor action for this complete transvection audit.

## 3. GSp multiplier audit

A multiplier-2 similitude representative
[
M_mu=operatorname{diag}(1,2,1,2)
]
was checked and satisfies
[
M_mu^TJM_mu=2J.
]

It preserves the three relevant ranks:

[
operatorname{rank}(M_muDelta_{mathrm{IA}})=20,
]
[
operatorname{rank}(M_mu C_3)=4,
]
[
operatorname{rank}(M_mu G_3)=20.
]

Therefore the candidate quotient is also compatible with this tested GSp multiplier direction.

## 4. What this establishes

The previous sub-gate showed that the first IA gauge does not erase the q-sensitive degree-3 signal.

The present audit adds:

[
oxed{
G_3=C_3+Delta_{mathrm{IA}}
	ext{ is invariant under the tested Sp4/GSp action.}
}
]

Consequently, the quotient
[
A_3/G_3
]
is a legitimate **equivariant candidate object** under the frozen action.

This is materially stronger than merely observing a 44-dimensional quotient.

## 5. What remains unproved

This still does **not** establish coordinate-free canonicity.

Specifically, it has not yet proved:

1. that every allowed change of free-group coordinates induces the same quotient construction;
2. that the lift fibre is globally a torsor under the full relevant IA group, rather than only its first graded layer;
3. that higher IA layers cannot alter the degree-3 defect through the chosen filtration convention;
4. that the q-sensitive defect defines a canonical section/class in the quotient independently of a base lift;
5. that the quotient separates the required q=3 and q=infinity structures globally.

Therefore the main IA/filtered-extension gate remains **OPEN**.

## 6. Next authorized step

The next computation should not be a full rank-4 scan.

The remaining minimal definition audit is:

- verify the lift-fibre composition/change law at the graded level;
- prove that the first IA variation map is the derivative of that change law, not merely an empirically invariant subspace;
- test whether the q-sensitive defect descends from the lift fibre to an orbit/torsor or extension class in the 44-dimensional quotient.

Only after that definition-level audit can a small q-comparison be authorized.
