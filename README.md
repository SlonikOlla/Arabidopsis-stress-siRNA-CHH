# Stress-specific local correspondence between 24-nt siRNAs and CHH methylation in Arabidopsis

Reproducibility repository for the manuscript **“Weak genome-wide correspondence masks stress-specific local 24-nt siRNA–CHH methylation relationships in Arabidopsis.”**

## Study question and novelty

RNA-directed DNA methylation (RdDM) provides a well-established mechanistic link between 24-nucleotide small interfering RNAs (24-nt siRNAs) and CHH methylation. The question addressed here is different: **do stress-associated changes in 24-nt siRNA abundance spatially correspond to stress-associated changes in CHH methylation across the genome?**

To our knowledge, this is the first systematic genome-scale comparison of this cross-layer relationship across multiple *Arabidopsis thaliana* environmental stresses. The analysis shows that near-zero genome-wide correlations can coexist with reproducible local correspondence concentrated in strongly remodeled loci. This correspondence is direction-dependent, stress-specific, and structured by genomic context and transposable-element (TE) lineage.

## Environmental stresses

The manuscript integrates public small-RNA and methylome datasets for four stresses:

- phosphate deprivation;
- drought;
- heat;
- *Pseudomonas syringae* pv. *tomato* DC3000 challenge.

Because matched small-RNA and methylome measurements from the same biological samples were generally unavailable, the environmental analyses are explicitly treated as **cross-dataset spatial correspondence**, not synchronous molecular coupling or causation.

## Main analyses

Analyses are performed independently in non-overlapping **100-bp and 500-bp TAIR10 nuclear windows**.

The workflow includes genome-wide correspondence, RdDM-related genetic positive controls, exact-rank extreme-tail analyses, baseline matching, gain-versus-loss asymmetry, genomic-context and TE-lineage analyses, sensitivity analyses, and recurrent cross-resolution locus identification.

## Principal result

Genome-wide Δ24-nt-siRNA–ΔCHH correlations are weak or essentially absent under all four environmental stresses. In contrast, extreme CHH-gain regions are reproducibly enriched for local 24-nt siRNA gains across all stresses. CHH-loss/24-nt-loss correspondence is strongly stress dependent: it is robust under heat and drought but largely absent under phosphate deprivation and pathogen treatment. Gain-associated correspondence is recurrently enriched in TE-associated sequence, with additional heterogeneity among TE superfamilies, families, and individual elements.

## Public datasets

- phosphate: small RNA **GSE17741**; methylation **GSE72770**
- drought: small RNA **GSE26356**; methylation **GSE94075**
- heat: small RNA **GSE239836**; methylation **GSE139941**
- pathogen: small RNA **GSE19694**; methylation **GSE128768**

No raw sequencing files are redistributed here. Raw and processed public data remain available from their original repositories.

## Core computational conventions

- Reference genome: TAIR10, nuclear chromosomes 1–5.
- Resolutions: 100 bp and 500 bp.
- Small-RNA reads: adapter/length preprocessing where required; exact genomic alignment; multimapping abundance fractionally allocated.
- 24-nt abundance: assigned to genomic windows by alignment midpoint.
- CHH methylation: aggregated independently into the same genomic windows.
- Condition changes: stress minus control (`Δ24nt` and `ΔCHH`).
- Missing methylation values are excluded rather than imputed.
- Extreme tails are selected by exact rank to prevent tie-induced tail inflation.
- Environmental-stress results are interpreted as spatial correspondence, not causal estimates.

## Repository organization

- `scripts/` – analysis and figure-generation scripts or workflow notes.
- `metadata/` – dataset/accession maps and metadata.
- `results/` – compact derived results suitable for version control.
- `figures/` – manuscript figures and sensitivity figures.
- `docs/` – workflow and reproducibility notes.
- `CITATION.cff` – citation metadata.
- `environment.yml` / `requirements.txt` – software-environment information.

## Reproducibility note

This repository is intended to contain the scripts and compact derived outputs needed to reproduce the analyses reported in the manuscript without redistributing large public raw sequencing datasets. Exact final executed scripts will be added only when verified against the retained analysis workflow; they will not be reconstructed or guessed.

## Citation

Please cite the associated manuscript and repository release. A manuscript-specific archival DOI will be added after the first release is archived.

## Licensing

Code: MIT License. Original sequencing data remain subject to the terms of their source repositories and publications.
