# Weak genome-wide correspondence masks stress-specific local 24-nt siRNA–CHH methylation relationships in Arabidopsis

Reproducibility repository for the manuscript examining spatial correspondence between stress-associated changes in 24-nucleotide small interfering RNAs (24-nt siRNAs) and CHH DNA methylation in *Arabidopsis thaliana*.

**Archived release DOI:** [10.5281/zenodo.22165451](https://doi.org/10.5281/zenodo.22165451)

## Study overview

The study integrates public small-RNA and DNA-methylation datasets for four environmental stresses: phosphate deprivation, drought, heat, and pathogen challenge. Analyses were performed independently at 100-bp and 500-bp genomic resolution on TAIR10 nuclear chromosomes 1–5.

The central question is whether stress-associated changes in 24-nt siRNA abundance and CHH methylation show a uniform genome-wide relationship, or whether correspondence is concentrated in strongly remodeled genomic regions.

The original manuscript reports weak genome-wide correlations and uses exact-rank extreme-tail analyses to examine local correspondence in the original exploratory analysis. Cross-study heterogeneity and incomplete biological replication prevent treating all four stress comparisons as equally confirmatory. TE-associated enrichment and TE lineage patterns are exploratory findings. An additional heat-specific TE sign-concordance sensitivity analysis finds TE-minus-nonTE effects below zero, although less negative than a mappability-stratified null; it does not establish stronger positive TE concordance.

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
- **Validated heat reconstruction:** 24-nt CPM is normalized to fractionally allocated mapped nuclear **18–30-nt** abundance; all 8,578,572 values at 100-bp and 500-bp resolutions reproduced within 1e-5 CPM. The historical README stated 16–27 nt; that denominator is inconsistent with the reconstructed retained heat matrices. Other stress datasets have not been independently revalidated for this denominator.
- Environmental comparisons are cross-dataset genomic associations, **not paired-sample responses**. Heat contrasts seven-day seedlings (37°C, 1 h) against methylomes from 21-day leaves (42°C, 6/12/24 h); drought and pathogen contrasts have limited small-RNA biological replication. The datasets are not uniformly biologically matched.
- Extreme-tail analyses use exact rank selection to avoid quantile tie inflation.
- Baseline matching accounts jointly for control CHH methylation and control 24-nt siRNA abundance.
- Multiple testing is controlled using the Benjamini–Hochberg false-discovery-rate procedure.

## Software

The manuscript analysis used Cutadapt 4.7, Bowtie, SAMtools, BEDTools, Python, pandas, NumPy, SciPy, and Matplotlib. Versions that could not be recovered from the retained environment or command logs are intentionally not guessed.

## Code provenance

The accessible retained project archive includes final outputs, command logs, software/mapping parameters, and analysis summaries, but not every original workstation script. Where an original script was unavailable, any transparent reimplementation is explicitly labelled as a reference implementation rather than being presented as the historical executed source. See `scripts/README.md` and `results/retained_output_provenance.md`.

## October 2026 validation status (draft branch; not a release)\n\nThe draft validation workflow and executed WSL results are documented in [docs/SINGLE_EXECUTION_WORKFLOW_2026-10-15.md](docs/SINGLE_EXECUTION_WORKFLOW_2026-10-15.md). The retained heat hierarchy, 500-bp/100-bp siRNA matrices, and two TE sensitivity analyses were rerun successfully. Heat-specific common-window filtering (CG≥5, CHG≥5, CHH≥50 observed cytosine sites) yielded stronger CHH O/E than CG and CHG in all 12 tested directions; the CHG-versus-CG ordering was inconsistent. Observed cytosine-site counts are **not bisulfite sequencing read depth**. The 48 CG/CHG site-count files and 12 separately stored CHH 500-bp files cover the heat hierarchy inputs. A clean-clone FASTQ-to-figures run, complete dependency lock, and historical mapping provenance remain outstanding. **Do not cite this draft branch as a finalized end-to-end reproducible release.**\n\n## Citation

For the original archive, cite the associated manuscript and v1.0.0 DOI **10.5281/zenodo.22165451**. The subsequent recovery milestone DOI **10.5281/zenodo.23353757** is not a finalized resubmission release.

## Licensing

Code is released under the MIT License. Derived documentation and summary metadata may be reused with attribution. Original public sequencing and methylation datasets remain subject to the terms of their source repositories and publications.
