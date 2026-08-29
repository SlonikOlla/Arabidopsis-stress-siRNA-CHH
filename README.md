# Weak genome-wide correspondence masks stress-specific local 24-nt siRNA–CHH methylation relationships in Arabidopsis

Reproducibility repository for the manuscript examining spatial correspondence between stress-associated changes in 24-nucleotide small interfering RNAs (24-nt siRNAs) and CHH DNA methylation in *Arabidopsis thaliana*.

**Archived release DOI:** [10.5281/zenodo.22165451](https://doi.org/10.5281/zenodo.22165451)

## Study overview

The study integrates public small-RNA and DNA-methylation datasets for four environmental stresses: phosphate deprivation, drought, heat, and pathogen challenge. Analyses were performed independently at 100-bp and 500-bp genomic resolution on TAIR10 nuclear chromosomes 1–5.

The central question is whether stress-associated changes in 24-nt siRNA abundance and CHH methylation show a uniform genome-wide relationship, or whether correspondence is concentrated in strongly remodeled genomic regions.

The principal result is that genome-wide correlations are weak or essentially absent, whereas exact-rank extreme-tail analyses reveal reproducible local correspondence. CHH-gain regions show recurrent enrichment for concordant 24-nt siRNA gains across all four stresses, while CHH-loss correspondence is more stress dependent. Gain-associated correspondence is recurrently enriched in transposable-element-associated regions, and TE superfamily, family, and element-level analyses reveal lineage-specific structure.

Because environmental small-RNA and methylome measurements were generally obtained from different biological samples and, in some cases, different experiments, these analyses are interpreted as cross-dataset spatial correspondence rather than synchronous molecular coupling or causation.

## Public datasets

| Stress | Small-RNA dataset | Methylation dataset |
|---|---|---|
| Phosphate deprivation | GSE17741 | GSE72770 |
| Drought | GSE26356 | GSE94075 |
| Heat | GSE239836 | GSE139941 |
| Pathogen challenge | GSE19694 | GSE128768 |

Positive-control analyses use independent RdDM-related genetic perturbations, including aly1-2 and drm1 drm2 cmt3 (ddc), to verify sensitivity of the spatial analysis framework.

No raw sequencing files are redistributed in this repository.

## Analysis outline

1. Small-RNA preprocessing and alignment to TAIR10.
2. Fractional allocation of multimapping small-RNA reads.
3. Construction of normalized 24-nt siRNA abundance profiles.
4. CHH methylation summarization in 100-bp and 500-bp windows.
5. Stress-minus-control change calculation for each molecular layer.
6. Genome-wide Pearson and Spearman correspondence analyses.
7. Baseline-matched exact-rank extreme-tail enrichment analyses.
8. Positive-control analyses using RdDM-related genetic perturbations.
9. Genomic-context enrichment analysis.
10. TE superfamily, family, and element-level analyses.
11. Representative-locus and sensitivity analyses.

## Repository organization

- `metadata/` — dataset accession and design information.
- `scripts/` — transparent analysis code and execution/provenance notes.
- `results/` — compact derived summaries and retained-output provenance.
- `docs/` — reproducibility and interpretation notes.

Publication figures and the manuscript are intentionally not duplicated in this repository.

## Important reproducibility conventions

- Reference genome: TAIR10.
- Nuclear chromosomes only: chromosomes 1–5.
- Genomic resolutions: 100 bp and 500 bp.
- Small-RNA alignments: exact-match, all-alignment strategy with a maximum of 50 reported alignments; multimappers are fractionally allocated.
- 24-nt abundance is normalized to fractional mapped nuclear 16–27-nt abundance.
- Environmental comparisons are treated as spatial correspondence across biologically matched datasets rather than causal paired-sample analyses.
- Extreme-tail analyses use exact rank selection to avoid quantile tie inflation.
- Baseline matching accounts jointly for control CHH methylation and control 24-nt siRNA abundance.
- Multiple testing is controlled using the Benjamini–Hochberg false-discovery-rate procedure.

## Software

The manuscript analysis used Cutadapt 4.7, Bowtie, SAMtools, BEDTools, Python, pandas, NumPy, SciPy, and Matplotlib. Versions that could not be recovered from the retained environment or command logs are intentionally not guessed.

## Code provenance

The accessible retained project archive includes final outputs, command logs, software/mapping parameters, and analysis summaries, but not every original workstation script. Where an original script was unavailable, any transparent reimplementation is explicitly labelled as a reference implementation rather than being presented as the historical executed source. See `scripts/README.md` and `results/retained_output_provenance.md`.

## Citation

Please cite the associated manuscript and the archived v1.0.0 release. Zenodo DOI: **10.5281/zenodo.22165451**.

## Licensing

Code is released under the MIT License. Derived documentation and summary metadata may be reused with attribution. Original public sequencing and methylation datasets remain subject to the terms of their source repositories and publications.
