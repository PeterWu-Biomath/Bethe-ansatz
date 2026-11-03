# Rewrite plan: a physics-style note on Bethe completeness

## Aim and level of rigor

Rewrite the note as a short, readable explanation of the weighted-counting mechanism for the periodic spin-1/2 XXX chain. Physicist-level rigor is sufficient: give explicit equations, explain why each operation should work, verify the combinatorial factors, and support the picture with examples. A full scheme-theoretic treatment is not a prerequisite.

The central story is:

1. Replace the physical count by a weighted sum of polynomial-system multiplicities.
2. Use depermutation to organize collisions and permutation redundancy.
3. Compute the corresponding ambient intersection number by a short combinatorial identity.
4. Use an inhomogeneous deformation to interpret the local alternating index as the degree-weighted count of exceptional components.
5. Explain which additional physical identifications remain open.

## Author's choices to preserve

- [x] Keep the generalized TQ/depermutation explanation heuristic. Do not turn its full proof into a rewrite requirement.
- [x] Retain the term **depermutation** and the setting L >= 2N.
- [x] Preserve the corrected observable-sum normalization: ordered points on the weighted side, unordered physical configurations on the physical side.
- [x] Preserve the current author information and email. Revisit the displayed date only when preparing the rewritten version.
- [ ] Rewrite `main.tex` in place when proceeding with the manuscript; this planning task changes only `plan.md`.

## What “physicist rigorous” means here

- State the genericity assumptions together in a short paragraph, then use the picture of roots splitting under deformation.
- Explain conservation of multiplicity as the conservation of the number of nearby roots, counted appropriately.
- Count a component with its degree over the deformation parameters. Say explicitly that the multiset convention already includes this degree, so it must not be multiplied in again.
- Use a common symmetric perturbation as the explanation of the TQ/depermutation correspondence; retain a clear indication that this is heuristic.
- Keep exact normalization factors, signs, and polynomial divisions correct. Heuristic presentation does not justify a false equality.
- Separate an assumed generic behavior from an observed example and from an unresolved physical interpretation, without repeating lengthy qualifications after every equation.

## Proposed manuscript structure

### 1. The question and the proposed answer

- [ ] Introduce the XXX Bethe equations, the rescaling to singular values +/-1, and the physical target binom(L,N) - binom(L,N-1).
- [ ] Explain the three difficulties: permutations, collisions, and singular solutions.
- [ ] Display the proposed alternating sum early, before the detailed notation.
- [ ] Explain the contribution relative to existing completeness results: an intersection-counting and local-multiplicity picture, rather than a claim that completeness itself is new.
- [ ] Keep the historical discussion short and use only the references needed for the argument.

### 2. Weighted roots and depermutation

- [ ] Introduce local multiplicity, formal sums of points, and total weight in plain language.
- [ ] Define the balanced fixed-pair partition ideals and their reduced equations.
- [ ] Explain the partition-lattice Mobius formula with one small example.
- [ ] Define the normalized Z_r^dep and the candidate alternating sum once; avoid reintroducing them in later sections.
- [ ] Explain why weighted depermutation is useful at a collision even though it need not cancel every collision before the singular correction.
- [ ] Keep the observable-sum extension as a brief remark, including the multiplication-trace interpretation and the restriction on rational denominators.

### 3. Why the global number is the expected one

- [ ] Present the ambient degree D = L + N - 2r - 2 for N - 2r free roots.
- [ ] Give the partition identity that turns D^m into a binomial coefficient after depermutation.
- [ ] Give the short generating-function derivation of the final alternating binomial identity.
- [ ] Describe this as the ambient/projective intersection count, distinguished from the actual affine root count.
- [ ] Keep BKK as an optional short explanation for enlarged supports; do not let it obscure the simpler degree calculation or identify enlarged supports with the actual specialized Newton supports.
- [ ] Summarize the boundary result: roots at infinity lie on collision diagonals. State that cancellation of the boundary contributions is a further step, not a consequence of their location alone.
- [ ] Retain the elementary boundary proof if it reads naturally; defer excess-intersection formalism rather than develop it solely for submission.

### 4. The local mechanism: deformation and exceptional components

- [ ] Introduce the site parameters theta_j and the exact site pairs 1-theta_j, -1-theta_j.
- [ ] Use the current degree-weighted multiset of components near p = (1^k,-1^k,z), with the ordinary z coordinates distinct and away from +/-1.
- [ ] Define the labels f,g and the equality partitions of escaping coordinates. Explain E as “not pinned to a site endpoint”, not “already physical”.
- [ ] Define D_r and tilde D_r as in the current note, with a concrete interpretation of the fixed sites and root labels.
- [ ] State finite flatness, generic simplicity, and endpoint avoidance as the working deformation assumptions. If useful, retain the short Jacobian argument showing endpoint avoidance from full generic simplicity; a separate technical theorem is optional.
- [ ] Explain that fixing r pairs uses r distinct sites. Divide the reduced equations once for each selected site. Do not revive the L^r average over repeated labels as a deformation of the same homogeneous reduced ideal.
- [ ] Derive the normalization
      w_r(p) = (k!)^2 D_r(p) / [N! ((k-r)!)^2].
- [ ] Derive the refinement of D_r by the total number of site pairs, carefully checking the site choices, positive and negative label choices, and factorials.
- [ ] Show explicitly how the binomial identity cancels every term with at least one site pair, leaving tilde D_0(p)/N!.
- [ ] Emphasize the interpretation: the surviving count is of generically distinct configurations with no pinned site pair, even if their homogeneous limit has collisions.

### 5. Physical interpretation, examples, and remaining questions

- [ ] Give the TQ viewpoint briefly: it explains the role of depermutation and the exclusion of unbalanced singular clusters. Keep the discussion heuristic where intended.
- [ ] State the distinct-root assumption away from +/-1 explicitly as an input, with the appropriate reference and its scope.
- [ ] Explain the one-pair calculation through the local algebra C[[u]]/(u^L h(u)). Nonphysical means h(0) != 0; physical means h(0) = 0. Exact excess one additionally needs a simple zero of h.
- [ ] State the remaining physical claim precisely: repeated balanced singular limits should receive no exceptional branches, and physical one-pair limits should receive the required degree.
- [ ] Do not describe these remaining identifications as proved by inclusion-exclusion alone.
- [ ] Finish with a concise account of what the picture explains and what still needs an argument.

## Examples to prioritize

- [ ] N=2: compute the singular multiplicity for both parities of L, then show the correction gives the physical weight.
- [ ] N=3, L=6: one small global count illustrating affine versus ambient counts and the boundary cancellation in this example.
- [ ] N=4: use (1,1,-1,-1) to illustrate the parity-dependent intermediate multiplicities and parity-independent alternating cancellation, if the calculation remains verified under the current normalization.
- [ ] Prefer two clear worked examples to a long table. Label numerical checks and analytic calculations accurately.

## Final revision pass

- [ ] Use N for the number of roots consistently. Keep k for the singular multiplicity at p, r for the number of fixed pairs, and m for the number of free blocks; flag any local exceptions.
- [ ] Make the abstract match the actual scope: a proposed weighted count and a deformation explanation under working assumptions, with the physical and boundary gaps stated briefly.
- [ ] Remove promises of results not delivered in the note, and fix draft grammar and hard-coded references.
- [ ] Keep the distinction between an ordered-point weight and an unordered-orbit contribution visible where needed.
- [ ] Check the reference details and state the relation to MTV and Jiang–Zhang accurately. Consider a short comparison with symmetric-system/resultant work if it illuminates the partition method; no exhaustive literature survey is required.
- [ ] Review the AI-assistance disclosure for accuracy.
- [ ] Compile the existing source, inspect the final PDF, and commit completed changes.

## Longer-term research, not prerequisites for this rewrite

- Prove the genericity assumptions in full generality.
- Give a complete local-length proof of the generalized TQ/depermutation correspondence.
- Prove the general boundary cancellation, including nonproper intersections.
- Prove the exact one-pair excess and exclusion of exceptional branches at repeated balanced singular limits.
- Develop explicit sums of observables using the weighted formal sums.

The rewrite should explain the mechanism convincingly at physics level. These research tasks may remain open, provided the claims made in the text reflect that status.
