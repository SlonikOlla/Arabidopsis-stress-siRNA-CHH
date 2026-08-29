# Derived results included for manuscript reproducibility

This directory is reserved for compact derived outputs used directly in the manuscript and sensitivity analyses. Large raw sequencing files are not redistributed.

## Final result files to include before v1.0.0

Primary statistical outputs:

- `all_stresses_extreme_tail_EXACT_RANK_FINAL.tsv` — definitive 100-bp/500-bp exact-rank extreme-tail analysis across all stresses.
- `all_stresses_CHH_to_24_EXACT_RANK_20x20_10k.tsv` — 20×20 baseline-stratification sensitivity analysis.
- `all_stresses_concordant_5pct_annotation_EXACT_RANK_FINAL.tsv` — primary genomic-context analysis.
- `all_stresses_concordant_annotation_1pct_10pct_EXACT_RANK_10k.tsv` — 1%/10% tail sensitivity analysis.
- `all_stresses_CHH5pct_TE50pct_overlap_sensitivity.tsv` — TE-overlap sensitivity analysis.
- `all_stresses_CHH5pct_TE_superfamily_baseline_permutation_10k.tsv` — TE-superfamily analysis.
- `all_stresses_CHH5pct_TE_FAMILY_baseline_permutation_10k.tsv` — TE-family analysis.
- `all_stresses_TE_ELEMENT_LEVEL_length_bias_sensitivity.tsv` — TE-element-level sensitivity analysis.

Representative-locus outputs:

- `top1pct_joint_concordant_windows.tsv`
- `recurrent_joint_concordant_clusters.tsv`
- `exact_100_500bp_recurrent_hits.tsv`
- `locus_plot_candidate_shortlist.tsv`

Dataset-specific frozen summaries, where retained:

- phosphate sentinel-filtered extreme-tail output.
- drought final consensus summary.
- heat final consensus summary.
- pathogen joint 100-bp and 500-bp summaries.

The repository release should not claim that a listed output is available until the exact retained file has been copied here and verified. Files are not reconstructed from manuscript text or rounded values.
