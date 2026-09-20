# B2 / k=2 — FINITE-WINDOW KUMMER RECOGNITION MOD 9

## Status

**PASS / LOCAL for the k=2 existence-and-uniqueness theorem; OPEN / DECISIVE for the general B2 finite-window theorem.**

## 1. Object and predicate

Let Q_2=G/P_3(G), where P_1=G and P_{n+1}=P_n^3[P_n,G]. Define, for a candidate character
\(\rho:Q_2\to(\mathbf Z/9)^\times\) with \(\rho\equiv1\pmod3\), the finite Kummer predicate
\[
\mathsf K_2(\rho):\quad H^1(Q_2,\mathbf Z/9(\rho))\to H^1(Q_2,\mathbf F_3)\text{ is surjective}.
\]
This predicate is stated using only the finite group Q_2, its coefficient character, and finite coefficient-extension data. It does not define rho using q or chi.

## 2. Existence at the actual finite window

For the standard rank-four Demushkin group
\[
G=\langle x_1,x_2,x_3,x_4\mid r=x_1^3[x_1,x_2][x_3,x_4]\rangle,
\]
the already established mod-9 twisted obstruction formula is
\[
\delta_{2,\rho}(f)=\bigl[f(p)+(\lambda\wedge f)(R)\bigr]\omega,
\quad \rho=1+3\lambda,
\]
with
\[
R=[X_1,X_2]+[X_3,X_4],\qquad p=X_1^{(1)}.
\]
Writing \(\lambda=(\lambda_1,\lambda_2,\lambda_3,\lambda_4)\) and \(f=(f_1,f_2,f_3,f_4)\), vanishing for every f is equivalent to
\[
1-\lambda_2=0,\quad \lambda_1=0,\quad\lambda_3=0,\quad\lambda_4=0.
\]
Hence the unique candidate is
\[
\rho_2=1+3e_2^*,\qquad \rho_2(x_1,x_2,x_3,x_4)=(1,4,1,1).
\]

The crucial finite-window existence point is that the resulting A_2-valued lifts actually kill P_3. For any such lift z, reduction gives z(P_2)=0, hence z(g)\in3\mathbf Z/9 for g\in P_2; also \rho_2(P_2)=1. Therefore
\[
z(g^3)=3z(g)=0\pmod9,
\]
and for \(g\in P_2, h\in G\), the crossed-commutator formula gives \(z([g,h])=0\pmod9\), because both contributing factors contain a product of two multiples of 3. Thus z(P_3)=0, so z factors through Q_2. This proves existence in the finite quotient itself, not merely in G.

## 3. Failure for every other candidate

For any \(\lambda\neq e_2^*\), choose f so that
\[
f(p)+(\lambda\wedge f)(R)\neq0.
\]
The corresponding obstruction is nonzero in \(H^2(G,\mathbf F_3)\). Its Q_2-origin has nonzero inflation to G, so the Q_2 obstruction cannot vanish. Hence \(\mathsf K_2(\rho)\) fails. Equivalently, no other candidate coefficient action has the universal lifting property.

## 4. What is and is not proved

This establishes the finite-window statement at k=2:
\[
\boxed{\mathsf K_2(\rho)\iff \rho=\chi\bmod9}
\]
for the declared rank-four Demushkin setting, with existence proved by direct P_3 annihilation and uniqueness by the audited obstruction formula/cup nondegeneracy.

It does **not** yet prove the general theorem for every k, nor a classification-free construction that takes an arbitrary abstract Q_2 and algorithmically outputs rho without first proving existence of a candidate satisfying the predicate. The definition of the predicate is classification-free; the identification with the canonical orientation is proved here using the audited Demushkin relation/cohomology calculation.

## Decision

- B2 Object/Input definition at k=2: **PASS / CLOSED**.
- q-blindness of the predicate: **PASS / CLOSED**.
- finite-window existence G/P_3: **PASS / LOCAL**.
- uniqueness at k=2: **PASS / LOCAL**.
- naturality of the predicate under Q_2 isomorphism: **PASS / CLOSED** at the predicate level.
- classification-free general k factorization: **OPEN / DECISIVE**.
- next target: k=3, Q_3=G/P_4, with the P_4 annihilation of the mod-27 lift as the sole existence gate before any higher interpretation.

## Boundary

The argument must not be inflated into “B2 is solved”. What is closed is the first finite-window test. The remaining theorem is the uniform statement that the Kummer finite-window predicate factors through Q_k for the required k and reconstructs chi mod 3^k without importing q, chi, the dualizing action, or classification.
