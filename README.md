# TE-distant gene networks show stress- and context-dependent 24-nt siRNA–DNA methylation correspondence in Arabidopsis thaliana

Reproducibility repository for the current manuscript analyzing stress-associated spatial correspondence between 24-nucleotide small interfering RNAs (24-nt siRNAs) and DNA methylation at **TE-distant gene-associated regions** in *Arabidopsis thaliana*.

> **Version history:** the archived `v1.0.0` release and Zenodo DOI `10.5281/zenodo.22165451` correspond to an earlier CHH-focused stage of the project. The current `main` branch is being prepared for the expanded TE-distant gene-network analysis and will be archived as a new Zenodo version.

## Study overview

The analysis integrates independent public small-RNA and whole-genome bisulfite-sequencing datasets for heat, drought, phosphate deficiency, and bacterial pathogen challenge. Analyses are performed at 100-bp and 500-bp resolution across CG, CHG, and CHH methylation contexts.

The current manuscript asks whether stress-associated 24-nt siRNA and DNA-methylation changes show reproducible functional organization at gene-associated genomic regions that are spatially separated from annotated transposable elements. Windows overlapping annotated TEs are removed, and the primary stringent analysis retains windows located at least 1 kb from the nearest annotated TE.

Because the molecular layers originate from independent studies, the analysis tests **cross-study spatial correspondence**, not paired within-sample molecular coupling, temporal ordering, or causality.

## Public datasets

| Stress | Small-RNA dataset | Methylation dataset |
|---|---|---|
| Heat | GSE239836 | GSE139941 |
| Drought | GSE26356 | GSE94075 |
| Phosphate deficiency | GSE17741 | GSE72770 |
| Pathogen challenge | GSE19694 | GSE128768 |

No raw sequencing files are redistributed in this repository.

## Current analysis framework

1. Quantification of stress-associated 24-nt siRNA and methylation changes in common 100-bp and 500-bp windows.
2. Separate analysis of CG, CHG, and CHH methylation contexts.
3. Removal of TE-overlapping windows and primary restriction to windows >=1 kb from the nearest annotated TE.
4. Separate concordant-gain and concordant-loss analyses.
5. Joint-tail discovery at 1%, with 5% and 10% sensitivity analyses.
6. Gene-level GO analysis followed by genomic-window opportunity permutation to control gene length and measurable-window opportunity.
7. Cross-context recurrence at gene and exact physical-window levels.
8. Threshold-free window-structure-preserving permutation analysis for targeted heat-response functional systems.
9. Descriptive gene-level ranking, Araport11 annotation, and cross-stress recurrence analysis.

## Repository organization

- `metadata/` — source dataset accessions and design metadata.
- `scripts/` — exact analysis scripts and provenance notes.
- `results/` — compact processed tables supporting manuscript results and figures.
- `supplement/` — supplementary data files.
- `docs/` — reproducibility and interpretation notes.

**The manuscript itself is intentionally not included in this repository.**

## Supplementary data

`Supplementary_Table_S2.xlsx` contains the complete ranked and functionally annotated TE-distant gene-body loci underlying Table 1 and the gene-level physiological interpretation, including support scores, methylation contexts, genomic resolutions, methylation direction, and cross-stress overlap information.

## Reproducibility note

The final v2 release should contain the exact scripts used for the reported analyses. Reconstructed or approximate replacement scripts should not be represented as historical executed code. Public raw sequencing files should be retrieved from their original repositories using the accessions above rather than committed to GitHub.

## Citation

Please cite the associated manuscript and the versioned Zenodo archive corresponding to the release used. The current manuscript title is:

**Kovalchuk I. TE-distant gene networks show stress- and context-dependent 24-nt siRNA–DNA methylation correspondence in Arabidopsis thaliana.**

The DOI for the new release will be added after Zenodo archives the v2.0.0 GitHub release.

## Licensing

Code is released under the MIT License. Derived documentation and summary metadata may be reused with attribution. Original public sequencing and methylation datasets remain subject to the terms of their source repositories and publications.
