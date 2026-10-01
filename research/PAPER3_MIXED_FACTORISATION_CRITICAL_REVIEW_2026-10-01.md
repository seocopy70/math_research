# MIXED (3,I)-ADIC FOX CARRIER — CRITICAL FACTORIZATION REVIEW — 2026-10-01

## Purpose

This note records a correction to the interpretation of the 2026-10-01 mixed-carrier audit. The standard-family calculation is valid, but it does not by itself establish factorization from the abstract finite pair W_k.

## 1. What is established

For the standard Demushkin family
\[
r_q=x_1^q[x_1,x_2][x_3,x_4],
\]
the projective Fox equations at the mixed maximal-ideal truncation give
\[
A=C=D=1,\qquad B=(1-q)^{-1}\pmod{3^k}.
\]
This is a valid local/direct Fox computation.

Likewise, the completed projective construction has the expected covariance under relator conjugation, relation-generator gauge, and Nielsen/free-basis changes, with the mixed maximal ideal preserved. This remains PASS / LOCAL.

## 2. Critical logical correction

The statement

\[
q\equiv q'\pmod{3^k}\Longrightarrow \mathcal M_k(q)\cong\mathcal M_k(q')
\]

is only **parameter-level factorization on the standard family**.

It is not the required theorem

\[
W_k(G)\cong W_k(H)\Longrightarrow \mathcal M_k(G)\cong\mathcal M_k(H)
\]

for arbitrary admissible inputs.

Therefore the label “finite-pair factorization: PASS / LOCAL” must be read narrowly as **standard-family parameter factorization**, not as evidence that the mixed carrier descends from the abstract finite-pair functor.

## 3. Second correction: non-redundancy

The fact that the mixed scheme retains higher 3-adic coordinates while the vector-space carrier C_k has dimension one is not, by itself, a category-level non-redundancy theorem.

To establish genuine non-redundancy one must exhibit a declared carrier category and prove that the mixed carrier is not equivalent, for the target task, to an already frozen carrier in that category. Information-content language alone is insufficient.

Thus the strongest safe classification is:
- direct standard-family bridge: PASS / LOCAL;
- higher-precision distinction from the bare vector-space object: PASS / LOCAL as an information statement;
- category-level non-redundancy: OPEN.

## 4. Consequence for the global gate

The decisive question remains exactly:

> Is the finite mixed Fox obstruction scheme determined naturally by W_k?

No proof has been established, and no same-W_k counterexample has yet been constructed.

The mixed branch therefore remains **OPEN / LOAD-BEARING**.

No larger computation is authorized merely to obtain more standard-family examples.

## 5. Literature boundary

The checked Zassenhaus literature identifies the Zassenhaus filtration with the augmentation filtration of the completed F_3-group algebra. It does not identify that finite mod-3 datum with the mixed characteristic-zero (3,I)-adic quotient used here.

A 2026 independent result of Pál–Quick distinguishes Demushkin q=3 from q≠3 at the A_3-formality/cochain level, but this does not provide a finite-pair factorization theorem for the present mixed Fox carrier. It is therefore supporting background, not a solution of the present gate.

## Classification

**Mixed Fox global finite-pair descent: OPEN / LOAD-BEARING.**

The standard-family calculation is retained as local evidence only. The next authorized work is a direct A/B attack on finite-pair descent, with no upgrade of the local result into a global theorem.
