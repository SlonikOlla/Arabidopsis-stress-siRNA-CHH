# Release readiness — Arabidopsis four-stress recovery

Status: **HOLD — do not tag a release or publish a new Zenodo version yet.**

## Validated downstream analyses
See [EXACT_RANK_NUMERICAL_VALIDATION_2026-10-13.md](EXACT_RANK_NUMERICAL_VALIDATION_2026-10-13.md).

- 504/504 selected-window counts and observed statistics reproduced.
- 336/336 CG/CHG null means, observed/expected ratios and empirical P values reproduced exactly.
- 166/168 CHH significance calls match. Two borderline CHH FDR decisions differ; original and reconstructed each yield 112 significant calls.
- All analyses use original processed stress-specific matrices; these checks **do not** establish upstream read-to-matrix reproducibility.

## Blocking actions before a versioned recovery release
- [ ] Commit historical source scripts `scripts/exact_rank_CHH_10k_context_comparison.py` and `scripts/exact_rank_CG_CHG.py` to `recovery-audit-v2`, preserving original source.
- [ ] Add a tested invocation, Python/NumPy/pandas version record, input paths and output descriptions to scripts README.
- [ ] Commit compact validation summaries and logs with provenance and checksums; exclude large matrices.
- [ ] Explain CHH FDR disagreements prominently in release notes.
- [ ] Review recovered preprocessing and permutation scripts for actual implementation of multimapper weights, normalization, replicate structure, TE enrichment and null model; label unresolved items clearly.
- [ ] Check that documented commands work from a clean checkout when required inputs are supplied.
- [ ] Review diff and merge the recovery branch into main only after verification.

## Release policy
The existing published release/Zenodo record must remain intact. A new GitHub tag and Zenodo version may be created for a transparently labeled **recovery / partial-validation release** once the required files and documentation are present. Do not describe the package as an end-to-end independently reproducible pipeline until upstream processing and TE testing have been verified. Do not mint or claim a new DOI before Zenodo actually archives the new release.

## Distinct repository
This is the four-stress project `SlonikOlla/Arabidopsis-stress-siRNA-CHH`, **not** the later TE-distant analysis repository.
