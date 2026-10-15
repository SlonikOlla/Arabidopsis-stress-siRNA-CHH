# Resubmission reproducibility checklist — updated 2026-10-15

## Uploaded and organized on draft branch
Eight scripts are now at `scripts/validation/`:
- `fractional_bowtie_to_bed.py`
- `verify_heat_500bp.py`
- `verify_heat_100bp.py`
- `build_heat_site_counts.py`
- `build_24mer_mappability.py`
- `heat_TE_CHH_matched_validation.py`
- `heat_TE_CHH_mappability_validation.py`
- `heat_common_window_context_hierarchy.py`

Four uploaded TSV tables are now under `results/validation_20261015/`:
- `heat_common_window_context_exact_rank_10k.tsv`
- `heat_common_window_context_OE_comparison.tsv`
- `heat_common_window_eligibility.tsv`
- `TE_CHH_concordance_stratified_null.tsv`

**These files were copied from the user's upload. No clean-clone reproduction has been performed.**

## Pending issues before merge and Zenodo release
1. Check dependencies and input paths for each script; add a runnable driver, environment file, and documented public-data acquisition steps.
2. Reconcile the README's historical 16–27-nt denominator with the validated 18–30-nt reconstruction of the retained heat matrices.
3. Provide exact software versions for stages actually reproduced; do not invent missing historical versions.
4. Ensure the full 36-test table and other compact outputs are referenced in manuscript tables/captions.
5. Verify site-count filters do not masquerade as bisulfite read-depth thresholds.
6. Treat heat as cross-study association (different ages, tissues, temperatures and exposure times), not a matched paired response.
7. Treat drought/pathogen as exploratory; phosphate sRNA replication remains unresolved.
8. Check whether TE permutation nulls address spatial dependence and read-depth differences; current analysis is not a fully read-depth-matched test.
9. Run a clean-clone smoke test before promoting this branch to a citable release.

**Do not merge or publish a new release while these gates remain open.**
