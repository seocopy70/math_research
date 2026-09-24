# B2 / k=3 — FINITE-WINDOW KUMMER RECOGNITION MOD 27 — 2026-09-24

## Status

**PASS / LOCAL for the standard rank-four q=3 Demushkin finite window (Q_3=G/P_4).**
Uniform all-k B2 remains **OPEN / DECISIVE**.

This attack directly closes the authorized k=3 existence gate: the unique mod-27 coefficient character selected by the full relation obstruction admits all mod-3 classes as (A_3=mathbf Z/27(ho_3))-valued cocycle lifts, and every such lift annihilates (P_4), hence factors through (Q_3).

## 1. Frozen object and finite predicate

Let
[
G=langle x_1,x_2,x_3,x_4mid r=x_1^3[x_1,x_2][x_3,x_4]angle,
]
with ([x,y]=x^{-1}y^{-1}xy), and
[
P_1=G,qquad P_{n+1}=P_n^3[P_n,G],qquad Q_3=G/P_4.
]

For a candidate
[
ho_3:Q_3	o(mathbf Z/27)^	imes,qquad ho_3equiv1pmod3,
]
define
[
mathsf K_3(ho_3):
H^1(Q_3,mathbf Z/27(ho_3))
	o H^1(Q_3,mathbf F_3)
]
to be surjective.

By the k=2 result, any candidate satisfying (mathsf K_3) must reduce mod 9 to
[
ho_2(x_1,x_2,x_3,x_4)=(1,4,1,1).
]

Every mod-27 lift of this (ho_2) is therefore uniquely parametrized by
[
ho_3(x_1)=1+9a_1,quad
ho_3(x_2)=13+9a_2,quad
ho_3(x_3)=1+9a_3,quad
ho_3(x_4)=1+9a_4,
]
with (a_iinmathbf F_3).

## 2. Exact crossed-word calculation

Let (z:F	o A_3=mathbf Z/27(ho_3)) be a crossed homomorphism, with generator values (z_i=z(x_i)).

For a generator with scalar (s=ho_3(x)),
[
z(x^3)=(1+s+s^2)z(x).
]
Since (s=1+9a_1),
[
1+s+s^2equiv3pmod{27}.
]

For the commutator convention ([x,y]=x^{-1}y^{-1}xy),
[
z([x,y])
=
s_x^{-1}(s_y^{-1}-1)z(x)
+s_y^{-1}(1-s_x^{-1})z(y).
]

For the ((x_1,x_2))-commutator, writing
(s_1=1+9a_1), (s_2=13+9a_2), direct reduction mod 27 gives
[
z([x_1,x_2])
=
(-3-9a_2)z_1+9a_1z_2
pmod{27}.
]

For ((x_3,x_4)), both coefficients are already 9-divisible:
[
z([x_3,x_4])
=
-9a_4z_3+9a_3z_4
pmod{27}.
]

Therefore
[
oxed{
z(r)
=
9igl(
-a_2z_1+a_1z_2-a_4z_3+a_3z_4
igr)
pmod{27}.
}
]

After division by 9 and reduction mod 3, with (f_i=z_imod3),
[
oxed{
delta_3(f)
=
-a_2f_1+a_1f_2-a_4f_3+a_3f_4.
}
]

This is exactly the expected cup-type variation
[
(muwedge f)(R)
]
with (mu=(a_1,a_2,a_3,a_4)), while the canonical (P_4)-residual is zero in the q=3 branch.

## 3. Uniqueness of the mod-27 candidate

For (mathsf K_3(ho_3)) to hold, the obstruction must vanish for every
[
fin H^1(G,mathbf F_3)congmathbf F_3^4.
]

Taking successively (f=e_1,e_2,e_3,e_4) gives
[
a_2=a_1=a_4=a_3=0.
]

Hence the unique candidate is
[
oxed{
ho_3(x_1,x_2,x_3,x_4)=(1,13,1,1)pmod{27}.
}
]

Equivalently,
[
ho_3=ho_2(1+9mu),qquad mu=0.
]

This is independently verified by exhaustive enumeration of all (3^4=81) compatible lifts: exactly one lift makes all four obstruction coefficients zero.

## 4. The authorized existence gate: (P_4)-annihilation

This is the load-bearing step. It must not be replaced by the full-group Kummerian theorem.

Fix the unique candidate
[
ho_3=(1,13,1,1).
]

For every (fin H^1(G,mathbf F_3)), choose arbitrary lifts (z_iinmathbf Z/27) of (f_i). The exact relation calculation above gives
[
z(r)=0pmod{27}
]
for every choice of the (z_i).

Therefore every (f) has an (A_3)-valued crossed cocycle lift (z) on (G).

Now prove that (z(P_4)=0).

### Step 1: (z(P_2)subseteq3A_3)

Since (f) is the reduction of (z), every (gin P_2) has (f(g)=0), because
[
P_2subseteqker(G	o G/P_2)
]
and (H^1(G,mathbf F_3)) factors through the abelianization.

Hence
[
z(P_2)subseteq3A_3.
]

Also (ho_3(P_2)=1), because (ho_3) is abelian.

### Step 2: (z(P_3)subseteq9A_3)

Recall
[
P_3=P_2^3[P_2,G].
]

For (gin P_2),
[
z(g^3)=3z(g)in9A_3,
]
since (ho_3(g)=1).

For (gin P_2, hin G), the crossed-commutator identity gives terms of the form
[
(ho_3(h)-1)z(g)
]
and
[
(1-ho_3(g)^{-1})z(h).
]
The second term is zero because (ho_3(g)=1), while
[
ho_3(h)-1in3mathbf Z/27
]
and
[
z(g)in3A_3.
]
Therefore
[
z([g,h])in9A_3.
]

Consequently
[
oxed{z(P_3)subseteq9A_3.}
]

### Step 3: (z(P_4)=0)

Now
[
P_4=P_3^3[P_3,G].
]

For (gin P_3),
[
z(g^3)=3z(g)in27A_3=0.
]

For (gin P_3, hin G),
[
z([g,h])
]
contains the factor
[
(ho_3(h)-1)z(g),
]
which lies in
[
3cdot9A_3=27A_3=0,
]
and the term involving (ho_3(g)-1) vanishes because (ho_3(P_3)=1).

Hence
[
oxed{z(P_4)=0.}
]

Therefore every (A_3)-valued cocycle lift factors through
[
Q_3=G/P_4.
]

This is the required finite-window existence proof.

## 5. Finite predicate is therefore actually realized on (Q_3)

We have now proved both directions needed for the standard q=3 window:

1. Every (fin H^1(Q_3,mathbf F_3)) has an (A_3)-valued lift for the candidate
[
ho_3=(1,13,1,1).
]

2. Every other compatible (ho_3) has a nonzero obstruction for some (f), so (mathsf K_3(ho_3)) fails.

Thus
[
oxed{
mathsf K_3(ho_3)
iff
ho_3=chimod27
}
]
for the declared standard rank-four q=3 Demushkin finite window.

## 6. Independent verification

The obstruction coefficient vector was evaluated for all 81 tuples
[
(a_1,a_2,a_3,a_4)inmathbf F_3^4.
]

The only zero vector occurs at
[
(0,0,0,0).
]

The four coordinate perturbations give:
[
(1,0,0,0)mapsto(0,9,0,0),
]
[
(0,1,0,0)mapsto(18,0,0,0),
]
[
(0,0,1,0)mapsto(0,0,0,9),
]
[
(0,0,0,1)mapsto(0,0,18,0)
]
before division by 9, confirming rank four of the secondary selector.

This independent enumeration is verification only; the mathematical proof is the crossed-word formula plus the (P_2	o P_3	o P_4) valuation argument.

## 7. What this closes and what it does not

### Closed at k=3

- mod-27 candidate parameterization over the unique mod-9 candidate;
- exact secondary relation obstruction;
- uniqueness of the compatible mod-27 coefficient action;
- existence of all mod-3 cocycle lifts on (G);
- direct (P_4)-annihilation;
- factorization through (Q_3=G/P_4).

Therefore the authorized k=3 existence gate is **PASS / LOCAL**.

### Still open

This does NOT prove:

- the theorem for every (k);
- a presentation-free construction for arbitrary Demushkin input;
- minimality/coarseness of the finite carrier;
- an all-(n) induction;
- that the finite predicate is classification-free for arbitrary abstract (Q_k), rather than for the declared standard family.

The single-vector (t_2) route remains **FAIL / CLOSED**; this k=3 result does not resurrect it. The successful object here is the exact coefficient-extension obstruction family.

## 8. Gate classification

- k=3 exact obstruction: **PASS / CLOSED** for the standard family.
- k=3 uniqueness: **PASS / LOCAL**.
- k=3 (P_4)-annihilation: **PASS / LOCAL**.
- k=3 finite quotient factorization: **PASS / LOCAL**.
- uniform B2: **OPEN / DECISIVE**.
- all-(n) coefficient-extension induction: **OPEN / DECISIVE**.
- intrinsic minimal carrier: **OPEN / LOAD-BEARING**.

## 9. Next authorized gate

The k=3 existence gate is now closed locally.

The next question is **not** to resurrect (t_2), and not yet to claim an all-(n) theorem.

The next authorized attack is:

[
A_3	o A_4,qquad
0	omathbf F_3	omathbf Z/81(ho_4)	omathbf Z/27(ho_3)	o0,
]

and determine whether the k=4 obstruction admits the same finite-depth factorization through
[
Q_4=G/P_5
]
without importing the canonical orientation or classification.
