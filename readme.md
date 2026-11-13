# Completeness of the Bethe Ansatz through Intersection Numbers

LaTeX source for **Completeness of the Bethe Ansatz through Intersection Numbers in $\mathbb{P}^N$**, by **Pei Wu**.

This note studies the completeness count for the homogeneous periodic spin-$1/2$ XXX chain from an intersection-theoretic perspective. It constructs weighted auxiliary polynomial systems, uses Möbius inversion on the partition lattice to account for permutations and collisions, and introduces an alternating correction on the singular-pair locus.

## The counting construction

For a chain of length $L$ with $N$ flipped spins and $L\ge 2N$, the highest-weight counting target is

$$
d(L,N)=\binom{L}{N}-\binom{L}{N-1}.
$$

The proposed cycle is

$$
\tilde Z=\sum_{r=0}^{\lfloor N/2\rfloor}(-1)^r\binom{L}{r}Z_r^{\mathrm{dep}},
$$

where $Z_r^{\mathrm{dep}}$ is the normalized partition sum after fixing $r$ singular pairs. Its projective intersection number satisfies

$$
\deg_{\mathbb{P}^N}\tilde Z
=\sum_{r=0}^{\lfloor N/2\rfloor}(-1)^r\binom{L}{r}
\binom{L+N-2r-2}{N-2r}
=d(L,N).
$$

The central question is whether this construction assigns the desired weight to every affine root configuration and zero weight at the boundary.

## Contents and status

The manuscript covers:

- Background on the XXX Bethe ansatz, singular roots, and completeness.
- Auxiliary ideals, depermutation, and a generalized $TQ$ relation.
- Projective intersection numbers and the alternating counting identity.
- Roots at infinity and local multiplicities at a single singular pair.
- A deformation interpretation of the local index through exceptional components.
- Explicit calculations for small $N$.
- A higher-spin extension, including local comparisons with known physicality conditions for repeated roots.

This is a research note developing a proposed geometric explanation of the count. Completeness in the polynomial formulation is already established in the literature; the note's general local-weight and boundary identifications remain conjectural or conditional on the stated hypotheses. The higher-spin appendix verifies selected local examples rather than a general physicality criterion.

## Repository files

| File | Description |
| --- | --- |
| [`main.tex`](main.tex) | Complete manuscript, appendices, and bibliography. |
| [`.gitignore`](.gitignore) | Excludes generated LaTeX files, including the PDF. |

The bibliography is included directly in `main.tex`; there is no separate `.bib` file.

## Build

Use a LaTeX installation such as TeX Live or MiKTeX with PDFLaTeX. The source uses `geometry`, `amsmath`, `amssymb`, `amsthm`, `mathtools`, `booktabs`, `lmodern`, `microtype`, `xcolor`, and `hyperref`.

From the repository directory, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Alternatively, run PDFLaTeX twice to resolve citations and cross-references:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The output is `main.pdf`. No BibTeX or Biber step is required.

## Selected references

- Mukhin, Tarasov, and Varchenko, [*Bethe algebra of homogeneous XXX Heisenberg model has simple spectrum*](https://arxiv.org/abs/0706.0688).
- Hao, Nepomechie, and Sommese, [*Singular solutions, repeated roots and completeness for higher-spin chains*](https://arxiv.org/abs/1312.2982).
- Hou, Jiang, and Zhu, [*Spin-$s$ Rational $Q$-system*](https://arxiv.org/abs/2303.07640).

The full bibliography appears in the manuscript.
