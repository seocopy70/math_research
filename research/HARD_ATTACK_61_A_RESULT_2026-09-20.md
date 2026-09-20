# HARD ATTACK 61-A RESULT — q=3 / q=9 FULL RELATION-JET AUDIT — 2026-09-20

## Verdict
**PASS / LOCAL.** The decisive q=3 audit shows that the feared additive rho_2-dependent term does **not** survive in the secondary relation obstruction. The old rho_2 action changes the exact crossed-word coefficient, but after inserting the compatible rho_3 lift it produces exactly the same (-mu_2) secondary coefficient as q=9. Thus there is no independent additive (B_{\rho_2}(z)) in the frozen standard-family calculation.

This is a local closure of HA61-A, not yet a general theorem for arbitrary minimal one-relator Demushkin inputs.

## 1. q=3: exact crossed-word calculation

Take
[
r_3=x_1^3[x_1,x_2][x_3,x_4],
]
with
[
\rho_3(x_1)=\rho_3(x_3)=\rho_3(x_4)=1,qquad
\rho_3(x_2)=t=13+9apmod{27}.
]
Then
[
t^{-1}=25-9apmod{27}.
]

Let (z) be an arbitrary crossed cocycle into (A_3=\mathbf Z/27(\rho_3)), with generator values (z_i=z(x_i)).

Because (\rho_3(x_1)=1),
[
z(x_1^3)=3z_1.
]

For the commutator convention ([x,y]=x^{-1}y^{-1}xy),
[
z([x_1,x_2])
=(t^{-1}-1)z_1.
]
All (z_2)-terms cancel exactly:
[
-z_1-t^{-1}z_2+t^{-1}z_1+t^{-1}z_2
=(t^{-1}-1)z_1.
]

Since (\rho_3(x_3)=\rho_3(x_4)=1),
[
z([x_3,x_4])=0.
]

Hence
[
z(r_3)
=
(3+t^{-1}-1)z_1
=
(2+t^{-1})z_1
=
-9a,z_1pmod{27}.
]

After division by (9) and reduction mod (3),
[
\delta_3(z)/\omega=-a f_1.
]

Therefore the three compatible lifts (t=13,22,4) give
[
a=0:(0,0,0,0),quad
a=1:(2,0,0,0),quad
a=2:(1,0,0,0),
]
exactly as the independent HA60 computation reported.

### Critical point
There is **no residual additive term independent of (a)**. The nontrivial old action (\rho_2(x_2)=4) is fully absorbed into the exact coefficient (2+t^{-1}), and the result is precisely the same secondary slope (-a) as the q=9 case below.

## 2. q=9: exact crossed-word calculation

Take
[
r_9=x_1^9[x_1,x_2][x_3,x_4],
]
with
[
\rho_3(x_1)=\rho_3(x_3)=\rho_3(x_4)=1,qquad
\rho_3(x_2)=t=1+9a.
]
Then
[
t^{-1}=1-9apmod{27}.
]

Again
[
z(x_1^9)=9z_1,
qquad
z([x_1,x_2])=(t^{-1}-1)z_1=-9a z_1,
]
and
[
z([x_3,x_4])=0.
]

Thus
[
z(r_9)=9(1-a)z_1pmod{27},
]
so
[
\delta_3(z)/\omega=(1-a)f_1.
]

The unique obstruction-free lift is (a=1).

## 3. What happened to the feared (B_{\rho_2})?

The audit separates two notions that must not be conflated.

### Not an additive extra term
There is no term of the form
[
B_{\rho_2}(z)
]
remaining after the full relation is evaluated.

### But the old action must not be discarded
For q=3, replacing (t=13+9a) by (1+9a) before evaluating the word would be wrong. The coefficient
[
2+t^{-1}
]
contains the old mod-9 action and the power relation together. The cancellation is only visible after the complete crossed-word calculation.

Therefore HA60's compact mechanism is supported **for the audited standard family**, but only after the full q=3 calculation. It was not legitimate to assume it in advance.

## 4. Secondary obstruction interpretation

In the frozen normal forms, with the common sign convention fixed by the mod-9 transgression,
[
\delta_3(z)/\omega
=
f(t_2)-(mu\wedge f)(R)
]
for the tested (q=3,9) branches, where:
- q=3: (t_2=0);
- q=9: (t_2=X_1^{(1)}).

The minus sign is convention-dependent globally; what is invariant for this audit is that the coefficient of the new extension parameter is the same in both branches.

Thus the feared rho_2-dependent correction is **not independently present**.

## 5. What this does NOT prove

1. It does not prove the formula for arbitrary minimal one-relator Demushkin inputs.
2. It does not yet prove an intrinsic presentation-free definition of (t_2).
3. It does not prove the exact normalization of the target fundamental class beyond the transported convention.
4. It does not justify all-(n) induction.
5. It does not rule out rho_2-dependent terms in more general relator shapes whose degree-≥3 terms interact with the coefficient action.

## 6. Independent verification

The q=3 and q=9 calculations are algebraically independent frozen checks:
- q=3 has nontrivial (\rho_2) already at mod 9;
- q=9 has trivial (\rho_2) but nonzero P_4 residual.

Both yield the same secondary extension slope (-\mu_2), while only q=9 has the nonzero (t_2) constant term.

This is precisely the separation needed to distinguish a genuine (B_{\rho_2}) from the power residual.

## 7. Decision

[
\boxed{\text{HA61-A: PASS / LOCAL}}
]

**Consequence:** proceed to **HA61-B**, but HA61-B is now a narrower structural question: prove whether the q=3/q=9 cancellation mechanism is forced by the coefficient-extension algebra and the degree-(2,3) relation jet, rather than being an accident of the frozen normal forms.

Do not start all-(n) induction yet.
