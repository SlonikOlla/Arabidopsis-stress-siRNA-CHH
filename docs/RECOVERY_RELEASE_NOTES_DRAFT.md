# Recovery release notes — draft (13 October 2026)

**Scope:** code recovery and numerical verification of downstream exact-rank analysis for four stress conditions in Arabidopsis. This is **not** a claim of end-to-end raw-read reproducibility.

## Added or documented
- Historical exact-rank scripts `scripts/exact_rank_CHH_10k_context_comparison.py` and `scripts/exact_rank_CG_CHG.py`.
- Recovered AWK preprocessing utilities and permutation scripts, with provenance and caveats.
- Numerical validation against original processed matrices and archived results, detailed in `docs/EXACT_RANK_NUMERICAL_VALIDATION_2026-10-13.md`.
- Statistical, preprocessing, and dependency audits.

## Verification summary
- All 504 tests reproduce selected-window counts and observed statistics exactly.
- CG and CHG (336 tests) reproduce null means, OE ratios, empirical P values exactly; null SD differs by at most 3.55e-15.
- CHH (168 tests) reproduces deterministic statistics exactly, but two borderline significance classifications differ:
  - heat, 24h, 500bp, 1%, `24_loss_to_CHH_loss`: archived FDR 0.057416; reconstruction 0.040946.
  - pathogen, 14h, 100bp, 1%, `CHH_gain_to_24_gain`: archived FDR 0.042336; reconstruction 0.056490.
- Both CHH runs report 112 significant tests, with 166/168 identical classifications.

## Limitations
- Upstream trimming, mapping, multimapper weighting, sample/replicate structure, TE-enrichment null-model assumptions, and clean-room execution remain incompletely verified.
- Some source matrices are not hosted in GitHub because of size. The results should be interpreted as cross-dataset spatial correspondence, not paired molecular causation.
- The reconstructed CG/CHG script adjusts significance over 336 tests; historical combined-table FDR was adjusted over 504 tests. Compare only harmonized FDR families.

## Publication
Retain the historical archive DOI [10.5281/zenodo.22165451](https://doi.org/10.5281/zenodo.22165451). Do not claim a new version-specific DOI until Zenodo archives the actual GitHub release. Proposed label: `v1.1.0-recovery` (not yet created).
