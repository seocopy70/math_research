# PAPER 4 — Top-Down Orientation Target Audit (2026-10-02)

## Decision

The recent (J_q) arbitrary-linear-direction counterexample does **not** reopen an unrestricted carrier hunt. The top-down strategy remains controlling.

The target-first reduction is now sharpened:
[
W_{q+1}Longrightarrow (q,O_q,omega_q)Longrightarrow chimod p^k,
]
where (q=p^f) is the first nonzero q-defect degree, (O_qsubset L_1) is the intrinsic origin/torsion sector already recovered locally by RP-3, and (omega_q) is the remaining normalized orientation functional on (L_1/O_q).

Thus the genuine Paper-4 bottleneck is **not full directed-incidence reconstruction**. It is the existence of an intrinsic finite-window normalization functional (omega_q).

## Target reduction

For a specially oriented RAAG with sinkhole set (S), under the literature convention
[
wvw^{-1}=v^{1+q}
]
for a special edge with origin (v) and sinkhole (w), the canonical orientation satisfies
[
	heta(v)=1,qquad	heta(w)=1+q.
]

Modulo (p^{f+1}=pq), write
[
1+qalongleftrightarrow ainmathbf F_p.
]
The first nontrivial orientation layer is therefore a linear functional
[
omega_q:L_1	omathbf F_p
]
with (omega_q|_{O_q}=0) and (omega_q(ar w)=1) on sinkhole generators.

For (kle f), the orientation is trivial modulo (p^k). At (k=f+1), (omega_q) is exactly the new orientation information. Once (q) and this normalized functional are known, the standard value (1+q) determines the higher reductions. Hence full graph reconstruction is stronger than the declared orientation target unless necessity is separately proved.

## Existing information

1. **q-value:** the 2-generator filtered extension defect has first nonzero degree (q) locally.
2. **origin sector:** RP-3 gives an intrinsic adjacent-window carrier whose annihilator recovers the origin/torsion sector locally.
3. **missing datum:** (O_q) determines the kernel of (omega_q), but not its normalization on the quotient (L_1/O_q).

## Abelianization lower boundary

In the rank-2 special-edge model
[
G=langle v,wmid wvw^{-1}=v^{1+q}angle,
]
abelianization alone sees the torsion/free decomposition but does not canonically normalize the sink coefficient. The full finite nonabelian extension does contain extra normalization information through
[
wvw^{-1}=v^{1+q}.
]
If (wmapsto w^c) preserves the finite semidirect structure modulo (pq), then
[
(1+q)^cequiv1+qpmod{pq},
]
forcing (cequiv1pmod p), so the first orientation coefficient is unchanged.

Classification:
- abelianization-only normalization: **FAIL / CLOSED as sufficient**;
- extension-level normalization: **OPEN / LOAD-BEARING**.

## Why the (J_q) failure is not the end

In the complete three-vertex one-sink model,
[
G=langle s,a,bmid[a,b]=1,;sas^{-1}=a^{1+q},;sbs^{-1}=b^{1+q}angle,
]
the q-layer defect is
[
B_q(u,x)=(alphagamma'-gammaalpha')overline{a^q}
+(etagamma'-gammaeta')overline{b^q}.
]
For (u=alphaar a+etaar b+gammaar s), the matrix of (B_q(u,-)) is
[
egin{pmatrix}-gamma&0&alpha\0&-gamma&etaend{pmatrix}.
]
Hence nonzero origin directions have rank (1), whereas directions with nonzero sink component have rank (2). Thus the failed predicate (J_q(u)
e0) was too coarse; the same defect contains a sharper local rank stratification recovering the origin plane.

This is only a local lemma, not a general theorem.

In the 2-generator model, by contrast, the q-defect has one-dimensional target and has rank (1) for every nonzero (u). Therefore rank-stratification alone cannot be the universal orientation functional.

## Literature boundary

Blumer–Quadrelli–Weigel prove that Kummerianity characterizes specially oriented oriented pro-(ell) RAAGs and their canonical orientation. This is a full-group uniqueness theorem. It does not by itself prove finite-window descent of that orientation to the abstract unmarked pair (W_qleftarrow W_{q+1}). citeturn0search0turn0search2

## Exact Gate T1

Given the abstract adjacent pair
[
W_qleftarrow W_{q+1},
]
construct intrinsically and q-blindly a normalized functional
[
omega_qin(L_1/O_q)^*
]
such that on every specially oriented RAAG
[
omega_q(ar w)=1
]
for every sinkhole generator (w).

Required:
1. intrinsicity under filtered-pair isomorphisms;
2. presentation/lift independence;
3. q-blind definition;
4. non-tautological construction;
5. naturality sufficient for finite-pair descent;
6. independent checks on the 2-generator, common-sink, and complete one-sink models;
7. direct reconstruction of (chimod p^{f+1});
8. reconstruction for higher (k) from the same normalized data and recovered (q).

Failure: two admissible specially oriented RAAGs with isomorphic (W_qleftarrow W_{q+1}) but different (omega_q) imply **FAIL / CLOSED** at this window.

Success: T1 makes full directed-incidence reconstruction unnecessary for the orientation theorem unless separately shown necessary.

## Strategy boundary

Not authorized as default targets:
- full directed-incidence reconstruction;
- arbitrary-linear-direction purity;
- another unrestricted sequence of Grassmannian/(J_q) variants.

The only admissible next construction is one whose stated output is (omega_q), or a theorem proving that no such finite factorization exists.

## Current classification

- Paper 3: **FROZEN / COMPLETE**.
- Paper-4 top-down reset: **PASS / ACTIVE**.
- (J_q) arbitrary-linear purity: **FAIL / CLOSED**.
- q recovery from first extension defect: **PASS / LOCAL**.
- origin sector from RP-3: **PASS / LOCAL**.
- abelianization-only normalization: **FAIL / CLOSED**.
- normalized finite-window orientation functional (omega_q): **OPEN / LOAD-BEARING**.
- finite-window orientation at (q+1): **OPEN / LOAD-BEARING**.
- categorical no-go at (q+1): **OPEN**.

## Bottom line

The research has **not** returned to square one. The bottom-up phase ruled out an overly strong carrier. The top-down reset now reduces the remaining problem to the single falsifiable question
[
oxed{W_qleftarrow W_{q+1}stackrel{?}{Longrightarrow}omega_qLongrightarrowchimod p^k.}
]
No broader carrier hunt is currently justified.
