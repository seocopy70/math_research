# PAPER 3 — REFEREE-STYLE ADVERSARIAL AUDIT 2026-09-28

## Verdict
**MAJOR REVISION / NOT ACCEPTABLE AS CURRENTLY WRITTEN.**
The core finite-window machinery may be correct at its declared scopes, but the present paper3/main.tex contains several theorem-level gaps and scope mismatches. These are repairable; none currently forces abandonment of the program. The most serious issues concern the free-product Kummer recognition theorem, the parameter-profile proposition, and the logical separation between imported Paper 1/2 results and genuinely proved statements in Paper 3.

## 1. Critical issue: free-product Kummer predicate factorization is under-justified
The theorem claims K_k(Q_k(G),rho) iff K_k(Q_k(G_i),rho_i) for every i. The proof invokes H^1 decomposition and says the global reduction map is a direct sum. This is plausible but the coefficient modules are rho-twisted and vary with the factor. The manuscript must explicitly identify the restricted module M_rho|_{G_i}, prove the H^1 decomposition for the actual finite quotient/free pro-p coproduct, and show that the inflation/factorization isomorphisms commute with the restriction/direct-sum diagram. Without a commutative diagram, “direct sum map” is asserted rather than proved.

Status: **OPEN / LOAD-BEARING**.

## 2. Critical issue: Truncation preserves free pro-p coproducts is stated categorically but not proved at the needed level
The reflector argument is reasonable, but the manuscript silently uses a specific Zassenhaus quotient functor on pro-p groups and then identifies the quotient of a free product with the free product of quotients after another truncation. This should be written as an explicit universal-property argument. Distinguish the canonical map T_n(G_1 *_p G_2) -> T_n(T_n(G_1)*_p T_n(G_2)) from an equality before reflection. The current proof is too compressed for a load-bearing structural lemma.

Status: **LOCAL / repairable**.

## 3. Critical issue: finite-depth f-collapse proposition overstates what the quotient intrinsically records
For f>=k, the relation term dies at the selected depth, but saying “the image of the defining relation agrees with the power-free relation” needs to be interpreted in the quotient presentation; it does not mean the abstract finite quotient has forgotten all traces of f. Conversely, for f<k, the claim that the image of x_1 has order exactly p^f requires a clean argument that the Zassenhaus kernel contributes no smaller relation in that cyclic torsion direction. The abelianization argument can establish this, but the sentence about P_n contributing only p-power relations of exponent at least p^k in the free directions should be replaced by an explicit calculation of the image of P_n(G) in G_ab.

Status: **OPEN / LOCAL**.

## 4. Major issue: parameter profile is marked, not intrinsic
The manuscript itself partially admits this, but the abstract/conclusion can still be read as saying that the bare finite quotient intrinsically records the individual f_i. In a free product, factor decomposition and block labels need not be recoverable from the bare quotient without hypotheses. State this as a marked finite quotient / inherited factor decomposition result, not an intrinsic classification theorem.

Status: **PASS after wording correction**.

## 5. Major issue: heterogeneous affine example needs precise Demushkin scope
The manuscript should state the precise Demushkin convention and allowed q=p^f range once, including why all f_i>=1 are torsion-free Demushkin cases for odd p.

Status: **LOCAL**.

## 6. Critical issue: lower-bound witness for f<k is not checked against the defining relation
The proposition proposes z(x_1)=1 with canonical orientation and claims a crossed-cocycle witness. But a crossed cocycle on the quotient/free group is not automatically a crossed cocycle on the Demushkin quotient: the defining relator must map to zero under the affine representation. This must be explicitly verified. The current one-line construction is insufficient.

Status: **OPEN / LOAD-BEARING for that proposition**.

## 7. Major issue: f>=k lower-bound witness also requires relator verification
The choice rho(x_2)=1+p and z(x_2)=1 must satisfy the full defining relation. Since the relation contains [x_1,x_2] and x_1 is sent trivially, it likely works, but the manuscript must calculate it rather than assume it.

Status: **OPEN / LOCAL-to-load-bearing**.

## 8. Critical issue: imported theorem dependencies are underspecified
The manuscript must state exactly which theorem from Paper 1 is invoked, at which q/rank/k scope, and exactly which factorization theorem from Paper 2 is invoked. A referee must be able to distinguish cited preprint results from claims actually proved here.

Status: **OPEN / LOAD-BEARING**.

## 9. Major issue: manuscript is stale relative to current selector-minimality result
The current conclusion says the threshold is sharp only in the affine category, while the latest research branch has a fixed rank-4 q=3 selector-minimality theorem. Either keep this manuscript deliberately application-only and explicitly exclude the newer theorem, or upgrade the manuscript. Do not mix the two states.

Status: **OPEN / EDITORIAL-LOGICAL**.

## 10. Major issue: 1-dimensional cup-line result is absent
The current manuscript never mentions C_k or the relation-module/cup-product proof. That is acceptable only if Paper 3 is intentionally an applications paper. The project must decide whether Paper 3 is the application paper in paper3/main.tex or the finite-recognition theorem paper. They are different manuscripts with different novelty claims.

Status: **OPEN / STRATEGIC**.

## 11. Major issue: novelty is underspecified
If Paper 3 is only an application/synthesis paper, its novelty may be too weak unless the composite-group theorem is genuinely absent from the literature. If the intended novelty is the finite-selector/minimal-window theorem, it belongs in a theorem paper or must be integrated explicitly.

Status: **OPEN / LOAD-BEARING for publication**.

## 12. Wording issue: “No additional depth is required for mixed commutators” is stronger than proved
The target-filtration argument proves every affine representation kills P_n(G). It does not prove a universal lower bound for every possible presentation-dependent notion of mixed-commutator depth. Replace with the exact categorical statement: no additional truncation is needed beyond the global Zassenhaus quotient for the stated affine target.

Status: **PASS after wording correction**.

## 13. Technical issue: parameter-collapse threshold needs explicit abelianization calculation
The inequality p^f >= p^k > p^{k-1}+1 is correct for odd p and k>=2, but the converse visibility statement f<k should explicitly use n=p^{k-1}+1 and the image of D_n(G) in G_ab.

Status: **LOCAL / repairable**.

## 14. Critical issue: H^1 decomposition is not enough until the rho-dependent module is transported
The direct-sum decomposition is for a fixed G-module. Here the module depends on rho. Define M_rho and show M_rho restricted to G_i is exactly the module attached to rho_i. Then draw the commutative diagram for reduction maps.

Status: **OPEN / LOAD-BEARING**.

## 15. Scope inconsistency
The authoritative research log now records Gate D closed for torsion-free Demushkin groups of odd p, even rank, q in {0,p,p^2,...}, all k. The selector-minimality proof is fully established in the fixed q=3 rank-4 case, with a partial endpoint extension for q=p^f and f<k. The general recognition theorem and the general minimality theorem must be stated separately.

Status: **PASS if explicitly separated; otherwise FAIL**.

## 16. Strongest referee objection
A referee could reasonably say: “Your finite-window recognition theorem may be correct, but the submitted Paper 3 is unclear about what is imported, what is new, and what is intrinsic. The applications theorem is not yet sufficiently justified at the free-product cohomology step, and the manuscript's stated contribution does not match the latest claimed selector-minimality result.”
This is the central revision request.

## 17. What survives the attack
The following core claims remain credible and independently motivated after stripping vulnerable wording:
- uniform affine factorization through Q_k at depth p^{k-1}+1;
- corrected finite obstruction carrier O_k via E_k -> Q_k;
- finite Kummer recognition at the declared Demushkin scope, conditional on the imported D1/D2 theorem chain;
- fixed q=3 rank-4 selector minimality n_selector(k)=3^{k-1}+1;
- intrinsic one-dimensional cup-line compression, conditional on the relation-module/cup-duality theorem being stated with exact hypotheses;
- no need to revive the closed bare-H^2 inflation route.

## Final referee classification
**MANUSCRIPT: MAJOR REVISION.**
**CORE PROGRAM: OPEN BUT VIABLE.**
**NO FATAL MATHEMATICAL COUNTEREXAMPLE FOUND IN THIS PASS.**
**LOAD-BEARING OPEN ITEMS: free-product twisted-H^1 diagram, relator verification for lower-bound witnesses, exact dependency statements, and manuscript/novelty alignment.**

Do not label Paper 3 ready for submission until these four items are repaired and independently checked.
