# Exact-rank numerical validation (13 October 2026)

## Source and scope
Validation was performed by the manuscript author in WSL at `~/arabidopsis_siRNA_methylation` against the original stress-specific processed matrices (heat, drought, pathogen, phosphate), using Python 3.11, NumPy and pandas in conda environment `arabidopsis-validation`. Outputs were redirected into `results/validation_20261013/`; archived results were not overwritten. The figures below are transcribed from the author's terminal output, not independently executed by this repository.

## CHH (168 tests)
- 168/168 test keys and selected-window counts match archived `results/all_stresses_extreme_tail_EXACT_RANK_FINAL.tsv`.
- 168/168 observed statistics match exactly.
- Maximum absolute differences: null_mean 8.7279; OE 0.00605117; empirical_p 0.0377573; p_deplete 0.0378747; null_sd 6.80196; global FDR 0.0434467.
- Significance calls agree for 166/168; both versions have 112 significant tests.
- Discordant tests:
  1. Heat, 24 h, 500 bp, 1% tail, `24_loss_to_CHH_loss`: archived FDR 0.057416 (not significant), reconstruction 0.040946 (significant).
  2. Pathogen, 14 h, 100 bp, 1% tail, `CHH_gain_to_24_gain`: archived FDR 0.042336 (significant), reconstruction 0.056490 (not significant).
- Permutation differences remain unexplained. Do not claim exact CHH inferential reproducibility.

## CG and CHG (336 tests)
- Both contexts completed successfully, 336/336 expected tests.
- Compared with CG/CHG subset (336 rows) of archived `results/all_stresses_CG_CHG_CHH_EXACT_RANK_10k_504tests.tsv`, joined one-to-one on context, stress, time, resolution, tail percentage, and direction.
- 336/336 row matches, 336/336 selected-window counts exact, 336/336 observed statistics exact.
- Maximum absolute difference = 0 for null_mean, OE, empirical_p and p_deplete; null_sd difference ≤ 3.552713678800501e-15 (floating-point precision).
- In the reconstructed **336-test FDR family**, 97 CG and 111 CHG tests were significant. These significance totals must not be conflated with FDR from the archived **504-test family**. Archived and reconstructed FDR require harmonized correction families before comparison.
- Reconstructed significant tests by stress: CG drought 16, heat 54, pathogen 11, phosphate 16; CHG drought 17, heat 62, pathogen 20, phosphate 12.

## Remaining actions
1. Commit exact historical scripts `scripts/exact_rank_CHH_10k_context_comparison.py` and `scripts/exact_rank_CG_CHG.py` without silently changing code.
2. Preserve logs, comparison tables, software version manifests and SHA256 of source scripts/input tables; exclude large processed matrices from Git.
3. Investigate CHH permutation differences (ordering, RNG consumption, baseline bins, original code revision).
4. Independently audit upstream trimming, alignment, multimapper weighting, replicate structure and TE null models. This downstream numerical validation does not resolve these issues.
