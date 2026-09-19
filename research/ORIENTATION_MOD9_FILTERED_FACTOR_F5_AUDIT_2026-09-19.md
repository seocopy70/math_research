# ORIENTATION MOD-9 FILTERED FACTOR — F5-AUDIT — 2026-09-19

## Scope

This audit advances F5 without running a new finite scan. The question is whether the first q=3 information needed by the twisted mod-9 obstruction is genuinely present in the restricted/Zassenhaus graded data, rather than only in the full filtered quotient (C_3=G/G_4).

The audit separates two statements:

1. the associated graded object contains the q-sensitive degree-3 power class;
2. that graded class, together with the degree-2 Demuškin relation/pairing, already canonically determines the full twisted obstruction (B_\lambda).

The first statement is verified. The second remains the exact open point.

## 1. Existing exact q=3 versus q=infinity certificate

The repository's independent Track-B calculation gives, in restricted/Zassenhaus degree 3,

[
\operatorname{in}_3(s_3)-\operatorname{in}_3(s_\infty)=X_1^{[3]}.
]

Thus the q=3 branch contains a genuine degree-3 restricted power signal (X_1^{[3]}) which is absent from the q=infinity control.

This is important because it corrects a too-strong earlier wording: the q=3 power information is not intrinsically invisible to the restricted graded object. What is not yet shown is that the *twisted lift obstruction* can be reconstructed from that graded information alone.

The certificate is independent of the later degree-4 observable branch and uses a common ambient restricted-Lie model.

## 2. Minimal candidate datum

For the present frozen rank-4 problem, the smallest plausible datum is not merely the quadratic pairing. It is the degree-3 restricted relation jet

[
D_3=(V,R_2,P_3),
]

where

- (V=L_1=G/G_2);
- (R_2subset L_2) is the one-dimensional Demuškin quadratic relation, represented by
  [
  R_2=[X_1,X_2]+[X_3,X_4];
  ]
- (P_3) is the q-sensitive restricted-power contribution, with frozen representative (X_1^{[3]}).

This is strictly weaker than the full filtered quotient (C_3), but strictly stronger than the degree-2 quadratic datum.

The key non-tautological test is therefore:

[
D_3\stackrel{?}{\Longrightarrow}B_\lambda.
]

## 3. What the frozen formula says structurally

The verified obstruction is

[
B_\lambda(f)
=(1-a_2)f_1+a_1f_2-a_4f_3+a_3f_4.
]

Its terms split into two types.

### 3.1 The constant (f_1) term

The coefficient (1) is the contribution of the q=3 power layer (P_3=X_1^{[3]}).

### 3.2 The (a_i f_j) terms

The remaining terms are the first-order response of the degree-2 commutator relation (R_2) under the coefficient twist

[
\rho=1+3\lambda.
]

Thus the formula has exactly the schematic form

[
B_\lambda
=
\operatorname{Defect}(P_3)
+
\operatorname{Twist}_\lambda(R_2).
]

No degree-4 information is used in this first-order expression.

## 4. F5-A result

The audit establishes the following narrower result:

**PASS — q-sensitive carrier existence.**

The first q=3 information needed by the twisted orientation calculation occurs already in restricted/Zassenhaus degree 3 as the class (X_1^{[3]}). Therefore it is incorrect to say that the orientation branch necessarily requires arbitrary higher filtered extension data merely because the full proof was first formulated on (G/G_4).

However:

**OPEN — canonical obstruction reconstruction.**

It has not yet been proved that there is a presentation-free operation on (D_3=(V,R_2,P_3)) whose value is exactly (B_\lambda), with the required transformation law under all automorphisms/isomorphisms of the graded restricted object.

That is the real remaining F5 question.

## 5. Consequence for the earlier boundary statement

The previous statement

> recovery requires filtered extension/multiplication data beyond the associated graded restricted object

must be weakened.

The correct statement is:

> recovery is proved from the canonical filtered quotient (C_3), and the q-sensitive power carrier is already visible in the degree-3 restricted graded layer; what remains open is whether the *twisted obstruction construction itself* factors canonically through that degree-3 restricted datum.

This correction does not upgrade F5 to PASS.

## 6. No-scan decision

No finite scan is authorized or needed at this point.

The next hand task is purely structural:

1. define (\operatorname{Defect}(P_3)) intrinsically from the restricted relation jet;
2. define (\operatorname{Twist}_\lambda(R_2)) without a chosen presentation;
3. prove their sum is functorial and coordinate-independent;
4. prove its zero set is the unique (\lambda_\chi).

Only after these are established can F5 be closed.

## Decision

[
\boxed{F1-F4=PASS,\qquad F5-A=PASS,\qquad F5=OPEN.}
]

No claim of recovery from the associated graded object alone is made yet.
