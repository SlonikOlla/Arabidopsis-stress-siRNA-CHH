# Retained output provenance

This file records final-analysis outputs that were recovered from retained command/output logs during preparation of the public repository. It is intended to distinguish directly recovered results from values reconstructed from manuscript prose.

## TE superfamily analysis

Recovered retained output identifies:

- output: `results/all_stresses_CHH5pct_TE_superfamily_baseline_permutation_10k.tsv`
- tests: 348
- globally significant tests at FDR < 0.05: 137
- significant CHH-gain/24-nt-gain tests: drought 6, heat 56, pathogen 2, phosphate 19
- significant CHH-loss/24-nt-loss tests: drought 5, heat 31, pathogen 6, phosphate 12

The retained log explicitly records 10,000-draw results and includes the major significant superfamily rows.

## TE family analysis

Recovered retained output identifies:

- output: `results/all_stresses_CHH5pct_TE_FAMILY_baseline_permutation_10k.tsv`
- tests: 2,702
- globally significant tests at FDR < 0.05: 675
- significant gain/loss counts: drought 14/13, heat 316/165, pathogen 3/6, phosphate 94/64

## TE element-level sensitivity

Recovered retained output identifies:

- output: `results/all_stresses_TE_ELEMENT_LEVEL_length_bias_sensitivity.tsv`
- tests: 400
- globally significant tests at FDR < 0.05: 90
- significant gain/loss counts: drought 6/3, heat 24/34, pathogen 2/3, phosphate 9/9

## Annotation threshold sensitivity

Recovered retained output identifies:

- output: `results/all_stresses_concordant_annotation_1pct_10pct_EXACT_RANK_10k.tsv`
- tests: 224
- globally significant tests at FDR < 0.05: 124

## Exact-rank extreme-tail analysis

The final manuscript analysis used exact-rank 1%, 5%, and 10% tails, 10×10 rank-balanced baseline strata, 1,000 permutations, seed 20260829, and global Benjamini-Hochberg correction. A transparent reference implementation is provided in `scripts/exact_rank_extreme_tail_reference.py`.

An earlier retained summary log contains the same four directional test definitions and records the generation of an all-stress extreme-tail permutation summary. Because the historical workstation script itself was not retained in the accessible archive, the repository does not falsely label the reference implementation as the original executed script.

## Data-processing parameters recovered from logs

Small-RNA processing parameters recovered from retained analysis records include:

- TAIR10 nuclear genome reference.
- Bowtie exact-match/all-alignment settings: `-f -v 0 -a -m 50 --best --strata`.
- multimapping abundance fractionalized across all reported alignments, including organellar hits in the denominator.
- 16–27-nt mapped nuclear abundance used as the normalization denominator for the mapping analysis.
- 24-nt alignments summarized to 100-bp and 500-bp nuclear windows.
- Cutadapt 4.7 was used where adapter removal was required; retained logs record adapter `TGGAATTCTCGGGTGCCAAGG` and length filtering `-m 18 -M 30`.

Methylation processing used coverage-weighted CHH fractions where methylated/unmethylated counts were available and condition means after independent replicate-level window summarization.

## Important distinction

This provenance document does not substitute rounded manuscript values for missing machine-readable tables. Machine-readable files should be deposited only when the exact retained output is available. The reference script is provided to make the statistical procedure transparent, not to imply preservation of the original execution environment.
