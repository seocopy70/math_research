# KUMMER 2-CELL OBSTRUCTION HARD ATTACK 28 — 2026-09-20

## 1. The first canonical 2-cell object inside the finite extension

Let
N=P_{k+1}(G), Q=G/N,
M=N/(N^{3^k}[N,N]),
E=G/(N^{3^k}[N,N]).

The extension
1 -> M -> E -> Q -> 1
has a canonical extension class
e_k(G) in H^2(Q,M).

This is intrinsic to the finite extension E and is independent of a chosen presentation of G.

For every candidate rho:Q->U_k and A=A_k(rho), a Q-equivariant map
f:M->A
pushes e_k forward:
f_*(e_k) in H^2(Q,A).

Equivalently, the extension class induces the canonical connecting/transgression map
delta_{e_k,rho}: Hom_Q(M,A) -> H^2(Q,A).

Thus there is a precise finite 2-cell obstruction object available without choosing generators.

## 2. Hard attack: does e_k reproduce the twisted one-relator obstruction?

Not automatically.

The standard-family obstruction row is a map
Obs_rho:A^4 -> A
whose vanishing characterizes the canonical rho. To recover this row from e_k, one would need a canonical identification of the relevant part of Hom_Q(M,A) with the four generator directions and a distinguished functional/class whose pushout gives the row.

The extension class e_k itself contains no distinguished four-generator basis. Any such identification in the standard presentation is presentation-dependent unless an independent intrinsic rigidification is supplied.

Therefore the implication

e_k alone => the standard Fox/Kummer obstruction row

is not established.

## 3. Why simply adding a fundamental class is dangerous

A distinguished top class in H^2, or an equivalent one-dimensional duality quotient, would provide precisely the missing 2-cell/fundamental-class rigidification. But for a Demushkin group that structure is tied to the dualizing module and hence to the orientation action.

Therefore adding H^2(G, A_k(rho)) or a distinguished duality class as an input is not an acceptable non-circular solution unless that class is itself reconstructed from the declared filtered extension data by an independent theorem.

This is the same logical boundary seen in Hard Attack 27, now sharpened: the problem is not merely missing kernel information; it is missing a canonical 2-cell evaluation functional.

## 4. What the extension class DOES give

The map delta_{e_k,rho} is a genuine q-blind finite construction. It can be used to ask finite, intrinsic questions such as:

- which coefficient twists admit an M-valued extension functional that kills e_k?
- what is the kernel/cokernel of delta_{e_k,rho}?
- how does this vary functorially under admissible group isomorphisms?

These are legitimate discovery questions.

However, a Boolean statement such as "there exists f with f_*(e_k)=0" is immediately suspect as a selector: f=0 always works. Requiring f nonzero needs a separate proof and, by Hard Attack 25, existence of nonzero crossed cocycles is already too weak in the one-relator family.

## 5. Stronger logical boundary

The finite extension has now been decomposed into two conceptually different pieces:

(A) kernel extension data:
    (Q,M,E), equivalently the extension class e_k;

(B) 2-cell evaluation data:
    a distinguished functional/evaluation on the extension class sufficient to produce the twisted top obstruction.

(A) is intrinsic and q-blind.
(B) is exactly where orientation-like information can re-enter.

Consequently the next carrier cannot be obtained by blindly enlarging (A). It must either:

1. construct (B) intrinsically from (A) and the declared filtered structure, or
2. prove that (B) is not recoverable without importing duality/orientation information.

## 6. Decision

- canonical finite extension class e_k: **PASS / LOCAL**;
- finite q-blind transgression map delta_{e_k,rho}: **PASS / LOCAL**;
- automatic recovery of the one-relator obstruction row from e_k: **FAIL / CLOSED as an inference**;
- "exists f with f_*(e_k)=0" as selector: **FAIL / CLOSED** (zero map);
- nonzero/equivariant transgression selector: **OPEN**;
- independent recovery of the distinguished 2-cell evaluation from filtered data: **OPEN / decisive**;
- adding duality/fundamental-class data directly: **CONDITIONAL / circularity risk**.

## 7. Exact next target

The next attack is not a larger quotient. It is the intrinsic reconstruction problem:

Can the Demushkin PD^2 condition, expressed only through finite filtered extension data, canonically produce the missing 2-cell evaluation without naming the dualizing character?

If yes, this is the desired orientation bridge.
If no, the failure identifies the exact logical boundary between finite filtered extension information and the canonical orientation.
