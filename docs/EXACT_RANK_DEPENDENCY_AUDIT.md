# Exact-rank analysis recovery: dependency audit

**Source examined:** retained `Arabidopsis_four_stress_GitHub_recovery_v2.zip`, paths `scripts/recovered/exact_rank_CHH_10k_context_comparison.py` and `scripts/recovered/exact_rank_CG_CHG.py`.

Both scripts parse as Python, but have **not** been numerically validated. They are distinct from the already committed `scripts/exact_rank_extreme_tail_reference.py`.

## CHH reconstruction script

- Seed `20260829`; 10,000 permutations; 10 baseline bins; exact 1%, 5%, 10% tails.
- Reads `drought_consensus/results/drought_joint_{100,500}bp.tsv`, `heat_consensus/results/heat_joint_{100,500}bp.tsv`, `pathogen_consensus/results/pathogen_joint_{100,500}bp.tsv` and phosphate-derived joint inputs.
- Reads the archived reference table `results/all_stresses_extreme_tail_EXACT_RANK_FINAL.tsv`.
- Writes `results/all_stresses_CHH_extreme_tail_EXACT_RANK_10k_CONTEXT.tsv` and `results/exact_rank_CHH_10k_vs_original_validation.tsv`.
- Compares reconstructed significance flags with the retained reference output. **This is a validation procedure, not proof of agreement until executed.**

## CG and CHG extension script

- Seed `20260829`; 10,000 permutations; 10 baseline bins; exact 1%, 5%, 10% tails.
- Uses stress-specific siRNA and methylation matrices, reusing the 24-nt siRNA tracks for the non-CHH contexts.
- Writes `results/all_stresses_CG_CHG_extreme_tail_EXACT_RANK_10k.tsv`.
- Must be assessed for equivalent coverage filtering and biological matching across methylation contexts.

## Prerequisites for executable verification

1. Obtain all four stress-specific 100-bp and 500-bp joint matrices and any auxiliary siRNA/methylation inputs referenced by these scripts.
2. Confirm their column schemas and their precise source datasets.
3. Preserve original files and checksums, execute in a clean documented environment, and compare exact row counts, statistics, empirical P values and BH FDR.
4. Report differences without modifying the original reference tables.
5. Evaluate the multiple-testing family and compare conclusions under conservative correction.
6. Treat windows as genomic observations, not independent plant-level replicates.

## Status

The scripts were found in the recovery ZIP; they have **not yet been checked into GitHub** or run against the original full-size matrices. Do not claim a successful reproduction or CHH specificity based on these recovered scripts alone.
