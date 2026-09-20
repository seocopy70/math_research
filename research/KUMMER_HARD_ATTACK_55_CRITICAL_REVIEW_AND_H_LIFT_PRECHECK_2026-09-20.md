# HARD ATTACK 55 — CRITICAL REVIEW OF HA54 AND PRE-CHECK FOR THE H-LIFT

Date: 2026-09-20

## 1. Target

Before entering the representation-theoretic branch, HA54 and the proposed \(H\)-module construction of the permanent 19-dimensional LHS piece were re-audited. The purpose is to prevent an unproved lift of the previously computed filtered \(H\)-action from being silently assumed at the finite central-extension level.

## 2. Confirmed facts

HA52–54 establish
\[
E_3^{2,1}=E_\infty^{2,1},\qquad \dim E_\infty^{2,1}=19.
\]
The corresponding quotient is
\[
\mathcal S=
\frac{\ker\bigl(H^2(V,\mathbf F_3)\otimes K\to H^4(V,\mathbf F_3)\bigr)}
{\operatorname{im}\bigl(d_2:H^2(W,\mathbf F_3)\to H^2(V,\mathbf F_3)\otimes W^*\bigr)},
\]
with \(\dim K=9\) and \(\dim\mathcal S=19\).

This is a permanent associated-graded LHS filtration piece. Permanence does not imply that \(\mathcal S\) is an orientation carrier.

## 3. Load-bearing correction: the H-lift is not automatic

The earlier filtered representation calculation gives an action on the relevant degree-one object and identifies its effective image with \(PSp_4(3)\). It does **not** automatically give an action on the finite central extension
\[
1\to W\to Q_2\to V\to1.
\]

To define \(\mathcal S\) as an \(H\)-module, one first needs an actual lift to the extension, equivalently an induced compatible action on \(W\) preserving the extension class, or an explicit construction of extension automorphisms. Only after this lift is established may one infer functorially that \(K\), \(\ker\mu\), \(\operatorname{im}d_2\), and \(\mathcal S\) are stable.

If the lift fails, that is itself a genuine structural boundary and the representation-theoretic branch must be classified accordingly.

## 4. Input-category audit

The finite objects \(V,W,Q_2\) arise from the filtered quotient and its central extension, but their admissibility as the declared intrinsic input category must remain explicit. No presentation coordinate, known \(q\), known \(\chi\), classification theorem, or PD^2 orientation datum may be silently inserted into the construction of the lift or into the interpretation of \(\mathcal S\).

This is essential because the project goal is an intrinsic filtered recognition mechanism rather than a repackaging of already-known orientation information.

## 5. q=3 locality

The number 19 is a result for the frozen \(q=3\) model. It is not a universal dimension statement for the entire Demuškin family until a general-q argument is supplied. The current role of the 19D piece is therefore local structural evidence.

## 6. Strategic alternatives remain open

The permanent sector can ultimately fall into one of three categories:

1. **Collapse:** its contribution is already controlled by the established \((R,p)\) data;
2. **Controlled Enrichment:** it supplies a finite functorial correction needed to control \(\beta_\rho^2\);
3. **Independent Layer:** it carries genuinely new \(\rho\)-visibility relevant to the selector.

No one of these outcomes is currently established.

## 7. Decisions

- permanent 19D LHS filtration piece: **PASS / CLOSED**;
- \(H\)-action lift to \(Q_2\): **OPEN / LOAD-BEARING**;
- \(H\)-module structure of \(\mathcal S\): **OPEN / LOAD-BEARING**;
- twisted \(\beta_\rho^2\) on \(\mathcal S\): **OPEN / LOAD-BEARING**;
- orientation-selector role: **OPEN / DECISIVE**;
- PD^2-free unique coker maximality: **OPEN / DECISIVE**;
- q-universality of the 19D numerical result: **OPEN**.

## 8. Next authorized attack

First search the repository for an existing proof that the filtered \(H\)-action lifts to \(Q_2\), \(W\), or the central extension class. If no such proof exists, attack extension-class invariance/lift directly. Only after this gate passes may the actual \(H\)-module structure of \(\mathcal S\) be computed.

No dimension-based identification such as \(19=10+9\), and no orientation interpretation of \(\mathcal S\), is authorized.
