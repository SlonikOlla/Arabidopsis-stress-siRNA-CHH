# Four-stress computational recovery audit (October 2026)

**Status:** Work in progress. This branch is an audit and recovery workspace, **not** a validated manuscript release. The original `main` branch and published v1.0.0/Zenodo archive remain unchanged.

## Recovered local materials
- Original analysis workspace: `~/arabidopsis_siRNA_methylation` (approximately 51 GB on the author's WSL machine).
- Recovered compact audit archive: `Arabidopsis_original_statistical_audit.tar.gz`.
- Candidate recovery bundle: `Arabidopsis_four_stress_GitHub_recovery_v2.zip` (contains 104 inventoried source/result files plus checksum manifest).
- Recovered original scripts include `exact_rank_extreme_tail_reference.py`, `exact_rank_CHH_10k_context_comparison.py`, `exact_rank_CG_CHG.py`, `permutation_delta24_CHH.py`, `bowtie_to_weighted_bed.awk`, and `bin_methylation.awk`.
- Archived results include `all_stresses_CHH5pct_TE_superfamily_baseline_permutation_10k.tsv`, `all_stresses_CHH5pct_TE_FAMILY_baseline_permutation_10k.tsv`, and `all_stresses_TE_ELEMENT_LEVEL_length_bias_sensitivity.tsv`.
- Original TAIR10 TE family/superfamily annotation and mutually exclusive 100-bp/500-bp annotations were recovered.

These materials have **not** all been checked into this branch; references here document their provenance and pending integration.

## Distinguish original code from reconstruction
A recovered source script does not prove that it generated a specific archived output. Some recovered scripts concern follow-up basal-state or TE-distant gene analyses, rather than the original four-stress study. Never present reference implementations or reconstructed scripts as historical executed code.

## Reproducibility work still required
1. Reconcile the existing repository's contents with the recovered bundle, using checksums; retain original scripts without destructive overwrites.
2. Trace sample accession, tissue, developmental stage, treatment duration and biological replicate for all four stresses.
3. Recover the 100-bp/500-bp stress-specific joint matrices and test input/output schemas.
4. Verify fractional multimapper allocation, normalization, methylation count aggregation and filtering against retained command logs.
5. Re-execute exact-rank/baseline-stratified permutation tests and compare numerical results to archived outputs.
6. Identify or explicitly reimplement the TE family, superfamily and element-level length-bias analysis. The original generating scripts have not yet been identified.
7. Audit TE nulls for chromosome, methylation/siRNA baseline, genomic opportunity, TE length, coverage and mappability.
8. Evaluate CG/CHG/CHH specificity and biological replication limits; genomic windows must not be treated as independent biological replicates.
9. Generate machine-readable numerical validation reports and manuscript-figure provenance.

## Interpretation
Most stress-related siRNA and methylation profiles originate from separate public studies or unmatched biological samples. Report spatial cross-dataset correspondence, not same-sample molecular coupling or causation.

## Publication release gate
Do not label this repository 'fully reproducible', create a v2.0.0 release, or update the manuscript's data-availability statement until the above analyses have been validated.
