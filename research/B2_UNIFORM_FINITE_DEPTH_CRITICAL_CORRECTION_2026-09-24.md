# B2 uniform finite-depth critical correction — 2026-09-24

## Purpose

Critical audit of the proposed all-k valuation/obstruction argument supplied on 2026-09-24. The finite-depth factorization mechanism and the proposed next-digit recurrence must be separated.

## 1. Valuation mechanism: survives

For (A_k=\mathbf Z/3^k(\rho)), (P_{j+1}=P_j^3[P_j,G]), and any crossed cocycle (z) with (\rho\equiv1\pmod3), the induction
[
z(P_j)\subset3^{j-1}A_k,qquad
\rho(P_j)\subset1+3^j\mathbf Z/3^k
]
for (2\le j<k), with (\rho(P_k)=1), is valid.

The base (j=2) follows because reduction of (z) modulo 3 is a homomorphism and kills (P_2), while (\rho(G)\subset U_1) and cubes of (U_1) lie in (U_2). The induction uses
[
z(g^3)=(1+\rho(g)+\rho(g)^2)z(g)
]
and the crossed-commutator formula. If (g\in P_j), then (\rho(g)\in U_j), so the cube coefficient has 3-adic valuation exactly 1; commutator terms gain at least one additional factor of 3. At (j=k), (\rho(P_k)=1), hence (z(P_{k+1})=0).

This is consistent with the cleaner semidirect-product proof
[
P_j(A_k\rtimes U_1)=3^{j-1}A_k\rtimes U_j,
]
which is now the preferred U1 route.

## 2. Critical error in the proposed next-digit calculation

The claimed general formula
[
z(r)=\bigl(4-r_{k-1}-3^{k-1}a_2\bigr)z_1
+3^{k-1}(a_1z_2-a_4z_3+a_3z_4)
]
is not valid for general (k). The step replacing the inverse
[
\rho(x_2)^{-1}-1
]
by a truncation linear in (r_{k-1}-1) drops higher inverse terms that are still visible modulo (3^k).

This already becomes decisive beyond (k=4): with (r_4=40), the displayed recurrence would give
[
4r_4-12=148\equiv67\pmod{81},
]
whereas the canonical residue is
[
r_5\equiv-1/2\equiv121\pmod{243}.
]
So the proposed recurrence and the assertion that it follows from (4-r_{k-1}) are **FAIL / CLOSED**.

## 3. Correct general coefficient

For the standard relation, after the previous-stage candidate has been fixed, the coefficient of (z_1) coming from (x_1^3[x_1,x_2]) is governed exactly by
[
2+\rho_k(x_2)^{-1}.
]

Write
[
\rho_k(x_2)=r+3^{k-1}a_2,qquad r=r_{k-1}.
]
Then
[
(r+3^{k-1}a_2)^{-1}
\equiv r^{-1}-r^{-2}3^{k-1}a_2\pmod{3^k},
]
so
[
2+\rho_k(x_2)^{-1}
\equiv
(2+r^{-1})-r^{-2}3^{k-1}a_2
\pmod{3^k}.
]
Because the previous-stage obstruction has already vanished,
[
2+r^{-1}\equiv0\pmod{3^{k-1}}.
]
Define, after fixing the chosen representative/lift (r),
[
c_k:=\frac{2+r^{-1}}{3^{k-1}}\pmod3.
]
Then universal vanishing forces
[
a_1=a_3=a_4=0,qquad
a_2\equiv c_k r^2\pmod3.
]
For the canonical sequence (r\equiv-1/2), one has (r\equiv1pmod3) and (c_k=1), so the next digit is (a_2=1). Thus
[
1,4,13,40,121,364,\ldots
]
is recovered by the corrected calculation.

However, this is still a standard-presentation calculation. It does **not** by itself prove presentation-free intrinsicity or q-blindness.

## 4. Classification of this audit

- valuation/factorization mechanism: **PASS / LOCAL**, pending the independent U1 semidirect-product proof;
- proposed (4-r_{k-1}) recurrence: **FAIL / CLOSED**;
- corrected inverse-based next-digit calculation: **PASS / LOCAL** for the standard presentation;
- presentation-free intrinsic selector: **OPEN**;
- q-uniformity: **OPEN**;
- novelty: **OPEN / DECISIVE**.

The earlier all-k general finite-window record must therefore not be read as validating the erroneous (4-r_{k-1}) recurrence. The factorization part and the standard-presentation Fox/Kummer uniqueness part are logically separate.

## 5. Immediate next gate

**U1 — independently prove**
[
P_j(S_k)=3^{j-1}A_k\rtimes U_j,
qquad
S_k=A_k\rtimes U_1,
quad U_j=1+3^jA_k.
]

Required checks:
1. both inclusions in the induction;
2. (U_j^3=U_{j+1});
3. commutator generation of (3^jA_k) from (3^{j-1}A_k) and (U_1);
4. boundary (j=k), giving (P_{k+1}(S_k)=1);
5. only after U1 is closed, deduce the exact (H^1) factorization (H^1(Q_k,A_k(\rho))\cong H^1(G,A_k(\rho))).

No t2 route is reopened.