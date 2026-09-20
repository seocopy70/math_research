# HARD ATTACK 42 — AMBIENT H^2 AUDIT: COEFFICIENT-EXTENSION REDUCTION

Date: 2026-09-20

## Purpose

Hard Attack 40's critical review identified a load-bearing issue: for

C_2(rho)=H^2(Q_2,A_2(rho))/im(delta_{2,rho}),

both the numerator H^2(Q_2,A_2(rho)) and the transgression image depend on rho. Hard Attack 41 closed the k=2 identification of the transgression obstruction with the intrinsic mod-9 relation-jet carrier (R,p), but did not control the ambient numerator.

The present attack asks for the strongest structural reduction available before any numerical scan.

## 1. Coefficient exact sequence

For every candidate rho modulo 9, write A=A_2(rho)=Z/9 with the scalar Q_2-action rho. Since rho is trivial modulo 3, there is a short exact sequence of Q_2-modules

0 -> F_3 -> A -> F_3 -> 0,

where both end modules have trivial Q_2-action. Its connecting maps are the twisted Bockstein operators

beta_rho^i : H^i(Q_2,F_3) -> H^{i+1}(Q_2,F_3).

The long exact sequence gives

H^1(F_3) --beta_rho^1--> H^2(F_3) -> H^2(A)
 -> H^2(F_3) --beta_rho^2--> H^3(F_3).

Therefore, writing b_i=dim_F3 H^i(Q_2,F_3) and r_i(rho)=rank(beta_rho^i),

log_3 |H^2(Q_2,A_2(rho))|
 = 2 b_2 - r_1(rho) - r_2(rho).

This is an exact reduction, not a heuristic.

## 2. Relation to the already closed mod-9 carrier

For rho(x_i)=1+3a_i mod 9 and lambda=sum a_i e_i^*, the degree-one twisted Bockstein is the same scalar obstruction already identified in the intrinsic carrier:

beta_rho^1(f) = [ f(p) + (lambda wedge f)(R) ] omega,

up to the single synchronized H^2 normalization/sign convention already isolated in the mod-9 theorem.

Thus Hard Attack 41 is strengthened conceptually: the same intrinsic relation-jet controls the first connecting map entering the ambient H^2 calculation.

The second connecting map beta_rho^2 is the next layer. By the coefficient-extension derivation rule it is the corresponding twisted Bockstein on H^2, i.e. the ordinary Bockstein contribution together with cup-product by lambda (up to the same convention). No claim about its rank is made here.

## 3. Consequence for the coker selector

At k=2,

|C_2(rho)| = |H^2(Q_2,A_2(rho))| / |im(delta_{2,rho})|.

Hence the ambient factor is controlled exactly by r_1(rho)+r_2(rho), while Hard Attack 41 identifies the transgression/extension-class scalar obstruction with beta_rho^1 on H^1.

This is a genuine structural decomposition of the two sources of rho-dependence:

(A) ambient coefficient cohomology: r_1(rho), r_2(rho);
(B) extension-class visibility: im(delta_{2,rho}), whose degree-one scalar shadow is the already closed Theta_(R,p).

No cancellation between (A) and (B) may be assumed.

## 4. What is and is not closed

PASS / CLOSED:
- exact coefficient-sequence reduction of ambient H^2 to twisted-Bockstein ranks;
- identification of beta_rho^1 with the intrinsic mod-9 obstruction already established;
- separation of ambient rho-dependence from extension-class visibility.

OPEN / LOAD-BEARING:
- actual values of b_2 and the possible ranks r_1(rho), r_2(rho) for the fixed finite group Q_2;
- whether |H^2(Q_2,A_2(rho))| is constant in rho;
- whether any variation has an intrinsic relation to the Demushkin extension class rather than ordinary finite-group coefficient cohomology;
- unique coker maximality without the external PD^2 criterion.

## 5. Gate for the next attack

The next attack is NOT a broad rho-scan. First compute/derive the cohomology of the fixed q-blind finite group Q_2 structurally, beginning with H^*(Q_2,F_3) and the two operators beta_rho^1, beta_rho^2. Only after this is controlled should the coker-size function be combined with extension-class visibility.

A particularly important possible outcome is:

- If the ambient H^2 size is rho-independent, the selector problem reduces sharply to transgression visibility.
- If it varies, the variation must be isolated as a separate finite-group effect; it cannot be silently attributed to orientation.

## 6. Negative discipline

This attack does NOT prove K_2=0, does NOT prove a unique scalar-character maximizer, and does NOT remove PD^2 dependence from the known selector. It is a reduction of the remaining problem, not its solution.

No broad numerical scan is authorized by this record.
