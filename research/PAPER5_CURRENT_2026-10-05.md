# Paper 5 — Current State (2026-10-06)

## Classification
**OPEN / LOAD-BEARING.**

Paper 5 is the finite Zassenhaus-window automorphism-structure programme. The former compression/trichotomy programme is HISTORICAL / SUPERSEDED.

## 2026-10-06 decisive boundary closure

The corrected intrinsic boundary theorem at n=p is **PASS / CLOSED / GENERAL** for odd p in the declared presentation scope.

At n=p,
D_p(W_p)=<X,Y,Z> ≅ F_p^3, with X=x^p, Y=y^p, Z=z^p, D_p central of exponent p, and
[x,y]=XZ^{-1}.

For g in Aut(W_p), write modulo D_2:
g(x) ≡ x^m y^u z^c, g(y) ≡ x^b y^v z^d, g(z) ≡ z^a.
Comparison in the independent X,Y,Z basis gives
u=0, v=1, c=a-m, with m,a nonzero. Hence
Im(Aut(W_p)->GL(V)) = S'_11(p),
where
S'_11(p) = { [[m,b,0],[0,1,0],[a-m,d,a]] : m,a in F_p^*, b,d in F_p }.
Its order is p^2(p-1)^2.

The substitutions
x -> x^m z^(a-m), y -> x^b y z^d, z -> z^a
realize every element. Also
IA(W_p) ≅ Hom(F_p^3,F_p^3) ≅ F_p^9,
so
|Aut(W_p)| = p^11(p-1)^2.

The earlier D_p ≅ F_p^2, S_11, and IA ≅ F_p^6 packages are HISTORICAL / SUPERSEDED.

## Boundary n=p+1

W_{p+1}=W_p, so the same automorphism theorem holds at n=p+1:
|Aut(W_{p+1})|=p^11(p-1)^2.
Classification: PASS / CLOSED / GENERAL.

## Local computation

Run 37381098677:
- p=5,n=6=p+1,(s,a)=(0,1);
- candidate order 2000;
- actual order 2000;
- equal=true.

Classification: PASS / LOCAL only. This confirms the already-closed boundary theorem because W_6=W_5; it is not a general proof.

## 2026-10-06 stabilization-lemma audit: second repair rejected

The original stabilization proof failed at \(D_p\subseteq M_{p+1}\). The subsequent repaired route correctly established the \(D_c^p\) and lower-central absorption sublemmas, but its final equality still failed because \(D_{k+1}\subseteq M_{p+1}\) gives only \(M_{k+1}\subseteq M_{p+1}\), not the reverse inclusion.

A further proposed repair via
\[
J_aI\subseteq J_{a+1}R+J_aI^2
\]
is now FAIL / CLOSED as a general lemma. The elementary-abelian counterexample \(G=C_p^2\), \(a=1\), gives \(J_1=I,\ J_2=0\), so the claim would force \(I^2\subseteq I^3\), which is false. The group-algebra identity also leaves a \(g(x-1)\in J_a\) term that is not shown to lie in \(J_aI^2\). The proposed Lemma D additionally uses a \(J\)-versus-\(I\) inclusion not previously established, making that induction circular.

Detailed audit: research/PAPER5_ZASSENHAUS_STABILIZATION_AUDIT_2026-10-06.md.

## What remains open

The arbitrary-n extension is OPEN / LOAD-BEARING because the reverse inclusion (M_{p+1}subseteq M_{k+1}) is still unproved.
Im(Aut(W_n)->GL(V)) ?= S'_11(p), or the correct n-dependent intrinsic replacement.

The previous B,theta attempt to force a uniform flag and P=lambda_s I+N from
B(gbar x,gbar y)=gbar_U B(x,y)
is FAIL / CLOSED as submitted. The U_n-action moves simultaneously, so B-equivariance alone does not force the required flag/Jordan form.

The free-lift objection is withdrawn. For a given g in Aut(W_n), a free lift tilde-g is available; the unresolved issue is not lifting g, but extracting a uniform intrinsic constraint on gbar from relation preservation. This is distinct from lifting an arbitrary M in GL(V).

Therefore the remaining proof problem is specifically the uniform U_n-action control needed to turn the intrinsic B,theta equations into a flag constraint and then a normal form such as P=lambda_s I+N, if that statement is true.

## Result classification

| Item | Classification |
|---|---|
| n=p boundary theorem | PASS / CLOSED / GENERAL |
| D_p(W_p) ≅ F_p^3 | PASS / CLOSED / GENERAL |
| IA(W_p) ≅ F_p^9 | PASS / CLOSED / GENERAL |
| Im at n=p = S'_11(p) | PASS / CLOSED / GENERAL |
| |Aut(W_p)| = p^11(p-1)^2 | PASS / CLOSED / GENERAL |
| W_{p+1}=W_p | PASS / CLOSED / GENERAL |
| n=p+1 automorphism theorem | PASS / CLOSED / GENERAL |
| Run 37381098677 | PASS / LOCAL |
| arbitrary-n B,theta proof as submitted | FAIL / CLOSED |
| proposed Zassenhaus stabilization proof | FAIL / CLOSED |
| implication W_{p+1}=W_p => W_n=W_p for all n>=p | OPEN / LOAD-BEARING |
| arbitrary-n uniform U_n-action control | OPEN / LOAD-BEARING |
| arbitrary-n Frattini-image theorem | OPEN / LOAD-BEARING |
| Paper 5 arbitrary-n END | NOT YET |
| Paper 5 full arbitrary-n END | NOT YET |

## Authorized next action

Do not run another blind prime/numerical sweep.

The stabilization pre-Gate remains OPEN / LOAD-BEARING. Do not integrate an arbitrary-n theorem yet.

If uniform U_n-control fails, classify that route FAIL / CLOSED rather than weakening the statement silently. If it succeeds, it becomes the load-bearing arbitrary-n theorem route.

## Repository anchors

- corrected n=p closure: research/PAPER5_WP_CORRECTED_STRUCTURE_STEP3_CLOSURE_2026-10-06.md
- previous Step 3 failure audit: research/PAPER5_STEP3_EQUALITY_AUDIT_2026-10-05.md
- P5-JET correction: research/PAPER5_JET_S11_JACOBSON_CORRECTION_AUDIT_2026-10-05.md
- IA/GL gate and runtime audits: research/PAPER5_IA_GL_*.md
