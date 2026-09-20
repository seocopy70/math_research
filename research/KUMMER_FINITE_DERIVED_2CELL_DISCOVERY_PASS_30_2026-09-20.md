# DISCOVERY PASS 30 — FINITE DERIVED 2-CELL / FITTING-TORSION CANDIDATE

## 2026-09-20

### 1. Discovery target
Hard Attack 29 closed direct addition of the PD^2 top class as non-tautological input. The next legitimate possibility is to derive a 2-cell rigidifier from the finite extension itself, rather than append oriented cohomology.

Set
\[
N=P_{k+1}(G),\quad Q=G/N,\quad M=N/(N^{3^k}[N,N]),\quad E=G/(N^{3^k}[N,N]),
\]
with extension class \(e_k\in H^2(Q,M)\). For each candidate \(\rho:Q\to U_k\), let \(A=A_k(\rho)\).

### 2. Candidate T_k
Construct a finite, presentation-free chain-level complex from the extension \(1\to M\to E\to Q\to1\), together with the coefficient action \(\rho\), and retain only basis-free invariants of its low-degree homology/cohomology: Fitting ideals, annihilators, determinant lines, or a torsion-like defect of the transgression complex.

The intended selector is not a chosen scalar. It is a canonical finite module/line/ideal \(T_k(G,\rho)\) whose distinguished degeneration/nondegeneration condition is equivalent to the twisted PD^2 obstruction. In a minimal one-relator presentation this should specialize to the rank-one obstruction row \(d_\rho\), but the definition must not mention generators or \(\chi\).

### 3. Why this is genuinely new relative to Hard Attack 28
The previous object \(e_k\) supplied only
\[
\operatorname{Hom}_Q(M,A)\xrightarrow{\delta_{e_k,\rho}}H^2(Q,A),
\]
and lacked a canonical evaluation. The new proposal does not ask for a preferred element of \(\operatorname{Hom}_Q(M,A)\). Instead it asks for the intrinsic module-theoretic defect of the entire finite transgression complex. Thus a possible rigidifier could arise from a kernel/cokernel/Fitting ideal rather than a basis vector.

### 4. Mandatory attack
**Object:** finite derived/transgression complex attached to \((Q,M,E,\rho)\).

**Input:** only \((Q,M,E)\), \(\rho\), and canonical finite homological constructions; no \(q\), \(\chi\), dualizing module, or chosen presentation.

**Functoriality:** induced by isomorphisms of finite extensions and coefficient-action intertwiners.

**Gauge:** no generator basis or relator normalization may enter; any chain model must be replaced by its canonical derived object or proved chain-equivalent.

**Orientation bridge:** still OPEN. A bridge would have to identify the finite defect with the twisted PD^2 obstruction by an independent theorem, not by inserting the known orientation formula.

**q-blindness:** PASS at definition level.

**Separation:** not yet executed; no numerical scan authorized.

**Novelty:** potentially stronger than \(e_k\) because it retains secondary/module-level information rather than a single pushforward class; potentially equivalent to a repackaging of top cohomology, which must be attacked.

**Stop:** the construction cannot be promoted unless a canonical derived object and a non-circular orientation bridge are both proved.

### 5. Immediate hard attack: torsion/determinant scalarization
A scalar determinant is immediately suspect. Changing a basis of any finite free resolution multiplies a determinant by a unit, and the coefficient-module automorphisms \(A\xrightarrow{\times c}A\) (\(c\in U_k\)) also act by units. Therefore a raw scalar cannot be the intrinsic selector unless the construction descends to a basis-free ideal/line or its vanishing/Fitting filtration.

So the scalar Reidemeister-torsion route is **FAIL / CLOSED as a definition of a canonical scalar**. The basis-free Fitting/annihilator/derived-line version remains OPEN.

### 6. Stronger attack: does a Fitting invariant merely repackage H^2?
Not yet. A Fitting ideal of a finite chain-level defect is determined by the finite extension and \(\rho\), whereas \(H^2(G,A(\rho))\) is not automatically determined by \(Q\). Hence it is logically possible for the defect to contain exactly the missing deep-kernel information without directly adjoining \(H^2(N,A)\). But no theorem currently identifies such a defect with the PD^2 obstruction.

### 7. Decision
- raw scalar Reidemeister/determinant selector: **FAIL / CLOSED**;
- basis-free finite derived/Fitting/annihilator 2-cell object \(T_k\): **OPEN / decisive**;
- automatic identification \(T_k\cong H^2(G,A(\rho))\): **NOT ESTABLISHED**;
- universal orientation reconstruction: **OPEN**.

No numerical scan is authorized until \(T_k\) is defined canonically and its bridge is stated precisely.
