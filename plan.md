# Plan for the Bethe ansatz note

## Scope and decisions

- Prepare a conditional/conjectural research note, rather than claim a complete new proof of completeness.
- Keep the generalized TQ/depermutation discussion heuristic, as requested by the author. Expanding its proof is not part of this revision plan.
- Preserve the assumption L >= 2n and the term **depermutation**.
- Keep the conditional component-degree formula and its endpoint-avoidance argument as the principal proved result under the stated hypotheses.
- Edit the existing `main.tex`, check it with the editor's compiler after changes, and commit completed revisions.

## Completed

- [x] Correct the observable-sum normalization: sum over physical permutation orbits on the left and all ordered points p in X on the right, with w_k(p) the ordered-point weight.
- [x] Explain this distinction next to the formula and use n consistently within that statement.

## Submission revisions

### 1. State the scope of the results accurately

- [ ] Revise the abstract to distinguish proved statements, assumptions, and open claims.
- [ ] Explicitly retain boundary cancellation, the exact physical one-pair multiplicity, and multiple balanced-pair cancellation as unfinished tasks.
- [ ] Identify the regular nonsingular simplicity/nonzero-vector input as either a justified external result or an assumption.
- [ ] Present the component-degree proposition prominently as a conditional theorem; do not imply that generic reducedness has been proved for every relevant Bethe family.

### 2. Clarify projective intersection numbers and the boundary

- [ ] Distinguish the intersection-class calculation from the affine sum of local lengths.
- [ ] Remove the promise that all boundary weights will be shown to vanish in the current note.
- [ ] Explain that locating boundary support on collision diagonals does not establish cancellation.
- [ ] Explain how positive-dimensional boundary intersections prevent a direct interpretation as a sum of ordinary isolated local lengths; use a partition such as (3,3) to illustrate the issue.
- [ ] State precisely which additional boundary comparison would identify the projective number with the affine total weight.

### 3. Clarify physical local weights

- [ ] Keep the one-pair result in its proved form: length L at a nonphysical simple reduced zero and length at least L+1 at a physical one.
- [ ] State that exact length L+1 requires the residual germ to have a simple zero.
- [ ] Keep exclusion of exceptional components at repeated balanced singular points as a separate open problem.
- [ ] Ensure all uses of the distinct-root assumption are explicitly conditional, including its use for reduced fixed-pair systems.

### 4. Add checked examples

- [ ] Include a complete n=2 example showing ordinary local length, depermutation normalization, and singular correction for both parities of L.
- [ ] Add a checked repeated-pair example, preferably (1,1,-1,-1), with the normalization used in the current note.
- [ ] Include a small global count that distinguishes affine lengths from the projective intersection number and records any boundary contribution.
- [ ] Record the parameters, assumptions, and exact computational method for any numerical or symbolic evidence.

### 5. Explain the contribution and relation to prior work

- [ ] Separate the proposed local/intersection-theoretic construction from MTV's established polynomial-kernel completeness result.
- [ ] Explain the relation to Jiang–Zhang's quotient-ring and multiplication-trace methods without presenting the trace identity itself as new.
- [ ] Compare the partition decomposition with Busé–Karasoulou's work on equivariant polynomial systems and resultants; distinguish related results from the precise local identities used here.
- [ ] Verify bibliographic details and exact theorem/lemma references for claims used as inputs.

### 6. Final presentation pass

- [ ] Standardize n versus N throughout the manuscript, including the title and abstract.
- [ ] Replace hard-coded section numbers with LaTeX references.
- [ ] Add author information and review the title against the conditional scope.
- [ ] Polish remaining draft sentences and consistent terminology for points, coordinates, roots, weights, and component degrees.
- [ ] Review the AI-assistance disclosure so it accurately describes the assistance used.
- [ ] Compile the saved source and check references, formulas, and PDF layout.

## Research tasks beyond the submission revision

- Prove the relevant generic reducedness and finite-flatness hypotheses, or establish them in stated families of examples.
- Prove exact physical one-pair multiplicity in the required generality.
- Prove cancellation of the boundary intersection contributions.
- Determine whether exceptional components can specialize to repeated balanced singular configurations.

These tasks need not all be solved before posting a clearly scoped conditional/conjectural note. They must remain identified as assumptions or open problems until resolved.
