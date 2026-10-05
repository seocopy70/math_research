# Paper 4 — publication re-audit after 2026-10-05 manuscript review

## Classification

**PASS / CLOSED — mathematical core remains certified in the repository evidence.**

**Publication artifact: NOT SUBMISSION-CLOSED.**

This audit records a new manuscript-level review identifying proof-packaging and statement defects that must be corrected before a submission claim is made. These findings do not by themselves refute the certified Paper-4 theorems; they reopen the publication proof-completeness gate.

## 1. Theorem 4.1 / SC proof

The manuscript proof based on the old weighted product filtration is not valid as written. In particular, the step controlling the conjugation term
\[
\sigma(c)-c
\]
does not justify the claimed weight increase in the Schreier coordinates.

A concrete index-p example is \(c=b-1\), with \(K=\ker(F\to C_p)\), \(a\mapsto1,b\mapsto0\):
\[
\sigma(c)-c=aba^{-1}-b\in J\setminus J^2.
\]
Thus the old multiplication argument cannot support \(E_mE_\ell\subseteq E_{m+\ell}\) in that form.

The replacement proof to use is the Magnus-coordinate / finite-difference proof already independently audited in research/PAPER4_MAGNUS_PREFIX_CODE_AUDIT_2026-10-05.md. Its key coordinates are algebra coordinates
\[
w_{k,i}=(\sigma-1)^kY_{0,i},
\qquad
U=z^p-1,
\]
with ambient weights \(k+1\) and \(p\), and prefix-free initial monomials
\[
X_0^kX_i,\quad X_0^p.
\]
This avoids the defective \(\sigma(c)-c\) estimate entirely.

**Required manuscript action:** replace the old Theorem-4.1 proof in full; do not retain the defective \(E_m\)-multiplication proof.

## 2. Section 8 / critical separation proof

The current manuscript's Section 8 theorem is not publication-grade if it is presented only as “Proof architecture”. The explicit constructions and calculations must occur in the main text or in a clearly cited proof appendix.

At minimum the final proof must specify:
- the \(a\ge2\) and \(a=\infty\) metabelian/finite witness construction actually used;
- the \(a=1\) witness separately, if \(a=1\) is claimed;
- the exact group presentation/name consistently;
- the order/relations of the witness;
- the definition and provenance of the Fox derivatives \(f_x,f_y\), if the integral Fox argument is used;
- the precise quotient/filtration in which the nonvanishing or nonsplitting calculation occurs.

No “Proof architecture” label is acceptable as the final proof of the load-bearing theorem.

## 3. Proposition 9.1 / abelianization

The statement “abelianization does not see \(s\)” must be restricted to the correct parameter range.

For
\[
p^s z-p^a x_1=0
\]
the torsion factor is governed by \(\min(a,s)\). In particular, for \(a>s\), the abelianization still has an \(s\)-dependent \(p^s\)-torsion factor, and for \(a=\infty\) the abelianization still depends on \(s\).

The manuscript must not claim \(s\)-blindness of abelianization in the full \(a\ge s\) range.

## 4. Definition of \(n_{\rm sep}(s)\)

The notation must specify the pair being separated. The lower bound and upper bound previously referred to different comparison pairs.

The final definition should explicitly state that, in the certified unmarked stress-family theorem,
\[
n_{\rm sep}(s)
=
\min\{n:\,
W_n(G_{s,s})\not\cong W_n(G_{s,\infty})
\},
\]
or an equivalent precise definition, and then prove the lower bound and critical-window separation for this same pair.

## 5. Section 5 notation

The duplicate use of \(c_0\) must be removed. In particular, \(c_0=a^{p^s}\) must not coexist with \(c_0=b\) in the conjugate family.

If Schreier conjugates \(a^i b a^{-i}\) are used, their ambient Zassenhaus degree is not \(i+1\). The \(i+1\) weight belongs to the adapted \((\sigma-1)^i\)-coordinates / iterated commutator leading terms. The manuscript must use one convention consistently.

The \(r=0,q=1\) edge case for \(h_1\) must also be defined or excluded.

## 6. Minor mathematical corrections

- In the Jennings product, the condition is \(i p^j\ge n\), not \(ij\ge n\).
- Replace “\(z\in D_n(F)\) only at depth 1” with the precise filtration statement intended.
- The \(r=z^p\) counterexample can be stated more cleanly: for \(s\ge2\), the defining relation makes \(z^{p^s-p}=1\), so the comparison reduces to \(z^p=1\), and the constructed group is independent of \(s\).
- State Proposition 10.1 with \(s\ge2\) if that is its actual hypothesis; retain \(s\ge1\) only for results independently valid there.

## 7. Form and bibliography

Required before submission:
- repair the page-16 overflow/truncation;
- remove Section 14 if it contains workflow language such as PASS/CLOSED, FAIL/CLOSED, or artifact audit;
- cite references [2] and [4] where used, or remove them;
- add the Ershov–Jaikin-Zapirain source (arXiv:1007.1489) and adjust the novelty language around SC/weighted-Schreier machinery;
- strengthen the citation for the cohomological theorem (cd=2 / H^2 statement);
- align the introduction's list of main results with Theorem 4.1 and Proposition 5.1;
- distinguish the Demushkin parameter notation from the Zassenhaus filtration notation \(D_n\).

## 8. Artifact package

The final submission package should contain the actual manuscript source, dossier/evidence files, and reproduction scripts, not only references to them. The checksum manifest must be directly usable by the stated verification command, and PDF title/author metadata should be populated.

## 9. Decision

The mathematical Paper-4 core remains **PASS / CLOSED** under the repository's certified scope.

The manuscript publication gate is **OPEN / LOAD-BEARING** until:
1. Theorem 4.1 proof is replaced by the audited finite-difference Magnus proof;
2. Section 8 is converted from architecture to a complete proof, or the unsupported claim is narrowed/removed;
3. statements 9.1, n_sep, Section 5 notation, and the listed minor errors are corrected;
4. bibliography, layout, metadata, and package contents are re-audited.

No new broad mathematical branch is authorized by this audit. The next action is manuscript repair followed by an independent source-to-PDF proof/artifact audit.
