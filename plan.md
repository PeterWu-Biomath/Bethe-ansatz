# Revision plan for the updated Bethe ansatz note

Planning basis: `main.tex` as reviewed on November 4, 2026.

## Aim and agreed level of rigor

Prepare a readable physics-style research note explaining the weighted-counting mechanism for the periodic spin-1/2 XXX chain. The aim is a convincing derivation under stated working assumptions, with exact combinatorial factors and informative examples. A complete scheme-theoretic proof of every deformation statement is not a prerequisite.

Preserve the author's decisions:

- Keep **depermutation**, the setting L >= 2N, and the existing weighted formal sums.
- Keep the generalized TQ/depermutation correspondence heuristic. Do not require a full proof as part of this revision.
- Retain the updated Section 5 and its notation D_r and tilde D_r; refine the exposition rather than replace it with the older counting convention.
- Preserve the current author information, email, and displayed manuscript date unless asked to change them.
- This task updates the plan only. Apply manuscript revisions separately in the existing `main.tex` and commit completed changes.

## What the current draft already contains

- [x] The proposed alternating count is displayed in the introduction, with a comparison to string-based counting.
- [x] The observable-sum formula uses ordered points on the weighted side and unordered physical configurations on the physical side.
- [x] The ambient intersection-number calculation and its generating-function identity are written out.
- [x] The boundary argument locates roots at infinity on collision diagonals and distinguishes this from cancellation.
- [x] The one-pair calculation gives length L for a nonphysical simple reduced root and at least L+1 for a physical one.
- [x] Section 5 defines degree-weighted component multisets, site labels, and equality partitions of escaping coordinates.
- [x] Section 5 constructs the reduced deformation with distinct fixed sites and states the working genericity assumptions.
- [x] The formulas for w_r(p), the refinement of D_r by tilde D_s, and the binomial cancellation leaving tilde D_0(p)/N! are present.

## Priority 1: make the existing counting argument easy to follow

- [x] Standardize N as the number of roots throughout. In the local discussion, use k for the number of copies of each singular value, r for fixed pairs, and s for total site pairs. Use M for the number of free coordinates and m for the number of free blocks.
- [x] Add a compact notation guide before the component count: D_r counts configurations containing the prescribed r site pairs; tilde D_r counts configurations carrying exactly those pairs and no others. In particular, D_0 and tilde D_0 are different counts.
- [x] Explain once that a component is counted with its degree over the parameter space. The multiset convention already includes this degree; do not multiply by it again.
- [x] Distinguish ordered nearby root configurations, their permutation orbits, and irreducible components. Avoid using these interchangeably in the opening paragraph of Section 5.
- [x] Keep the calculation of the normalization explicit:

  `w_r(p) = (k!)^2 D_r(p) / [N! ((k-r)!)^2]`.

  Check the limiting cases r=0 and r=k and one small example.
- [x] Keep the refinement factors visible: choose s-r additional sites, choose their positive and negative root labels, and assign those labels to the sites. Explain that permutation symmetry makes the resulting degree counts equal.
- [ ] Summarize the cancellation in one sentence: the alternating sum removes configurations with one or more pinned site pairs and retains generically distinct configurations with no pinned pair.

## Priority 2: give the deformation assumptions a short physical explanation

- [ ] Gather the working assumptions into one paragraph: multiplicity is conserved under the chosen deformation; the relevant generic roots split simply; free roots avoid already fixed endpoints; the label/site permutations preserve the counts being compared.
- [ ] Explain finite flatness as conservation of the number of nearby solutions, including multiplicities. Formal local algebra details can be deferred.
- [ ] Explain that distinct coordinates and a simple zero are different notions. Generic simple collision solutions are allowed and are cancelled by depermutation.
- [ ] Either keep endpoint avoidance as a stated working assumption, as in the current draft, or include the short Jacobian explanation. A separate technical theorem is optional.
- [ ] Retain distinct sites for the fixed-pair deformation and division once per selected site. Do not reintroduce an average over repeated site labels as though it specialized to the same reduced ideal.
- [ ] Make clear that an exceptional component is a surviving generic branch, not an already established physical homogeneous solution.

## Priority 3: align the claims with what the note establishes

- [ ] Revise the abstract to foreground the proposed alternating count and the conditional explanation by exceptional components.
- [ ] State the remaining physical questions briefly: exact excess one at a physical single-pair root, and absence of exceptional branches at repeated balanced singular limits.
- [ ] State the distinct-root property away from +/-1 as an input, retaining the intended heuristic TQ discussion.
- [ ] Keep the weaker one-pair result accurate: h(0)=0 establishes positive excess; exact excess one needs a simple zero of the residual germ h.
- [ ] Remove the sentence promising that every boundary weight will be proved to vanish, since the current boundary section does not establish this.
- [ ] Describe the projective number as an ambient intersection count. Explain that its equality with the affine total weight needs boundary cancellation, especially when the boundary intersection is not isolated.
- [ ] Keep the BKK discussion short and explicit that it uses retained/enlarged supports. Do not identify that generic count with the specialized affine solution count without the boundary comparison.
- [ ] Use a brief concluding paragraph to separate the explained mechanism from the remaining physical and boundary identifications. Do not require those open problems to be solved before a clearly scoped conjectural note can be posted.

## Priority 4: add two useful checks

- [ ] Restore a short N=2 calculation for both parities of L, showing the singular multiplicity and its correction. This is the first normalization check.
- [ ] Choose one further example: N=3, L=6 for the affine/ambient comparison, or N=4 at (1,1,-1,-1) for the multiple-pair correction. Include whichever calculation can be checked most transparently.
- [ ] State whether each example is analytic or computational, record the parameters, and use the current normalization consistently.
- [ ] Prefer a short table or a one-page worked example to a large computation. Generic reducedness and conservation assumptions may remain working assumptions; a general proof is not needed for this stage.

## Priority 5: final presentation and submission pass

- [ ] Polish draft grammar, especially the abstract, the start of Section 2, and the description of component counts.
- [ ] Replace hard-coded section numbers with LaTeX references.
- [ ] Describe the contribution relative to MTV and Jiang–Zhang concisely: the local weighted/intersection-counting picture, rather than completeness or multiplication traces themselves being new.
- [ ] Check the references actually used for physicality and repeated-root inputs. Add a comparison with equivariant-system/resultant work only if it clarifies the method; an exhaustive survey is unnecessary.
- [ ] Review the title, abstract, conclusion, and AI-assistance disclosure for consistency with the final text.
- [ ] Compile `main.tex` with the editor's compiler, inspect the PDF for long formulas and unresolved references, and commit the completed revision.

## Optional later work

These are research directions, not requirements for the present physics-style revision:

- Prove the genericity assumptions for all relevant Bethe families.
- Supply a fully rigorous local-length proof of the generalized TQ/depermutation identity.
- Prove general boundary cancellation, including nonproper intersections.
- Prove exact physical one-pair excess and exclusion of exceptional branches at repeated singular limits.
- Develop explicit sums of observables from the weighted formal sums.

## Completion criterion

The revised note should let a reader reconstruct the coefficients and cancellation, understand what is assumed about the deformation, follow at least two checks, and identify the remaining physical questions. It need not settle every open claim, but heuristic explanations must remain distinguishable from established identities.
