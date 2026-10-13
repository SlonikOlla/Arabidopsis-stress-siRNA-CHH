# Statistical test provenance and verification plan

## Restored script

`scripts/recovered_original/permutation_delta24_CHH.py` is copied from the retained recovery archive. Its Python syntax was checked against the archive.

Usage:

```bash
python scripts/recovered_original/permutation_delta24_CHH.py INPUT.tsv OUTPUT_PREFIX
```

Input must contain numeric columns `delta24`, `deltaCHH`, and chromosome label `chr`. The script computes genome-wide Pearson correlation and directional concordance among windows with nonzero changes in both molecular layers. It permutes `delta24` **within each chromosome** 10,000 times (seed 12345), computes two-sided empirical P values, and saves permutation distributions.

## Important limitations

- Chromosome-wise shuffling preserves chromosome membership, but **not** local spatial autocorrelation, coverage, TE density, baseline methylation or siRNA abundance.
- The directional concordance test uses absolute deviation from **0.5**, not from its observed permutation-null mean. With unequal sign frequencies or other asymmetry, 0.5 need not be the correct null center. Compare with a permutation-centered statistic in sensitivity analyses.
- Correlation is undefined when either variable has zero variance. Concordance is undefined if there are no windows with both changes nonzero. Input validation should be added in a separately named, tested implementation, rather than silently modifying recovered historical code.
- Genomic windows are not independent biological replicates. These empirical P values characterize a spatial null and do not establish reproducibility across independently treated plants.
- The script does not implement the baseline-matched exact-rank extreme-tail test described in the README; that is a **separate** analysis.

## Outstanding exact-rank code

The recovery archive includes `exact_rank_CHH_10k_context_comparison.py` and `exact_rank_CG_CHG.py`. Both passed Python syntax parsing. They are **not yet committed** because their input/output dependencies and relationship to the existing reference implementation need to be audited first.

## Acceptance tests before release

1. Run on a small synthetic input with known chromosome groups, sign frequencies, and null distributions.
2. Compare restored-script output against an independent test implementation with the same random seed.
3. Validate against original per-stress joint matrices, including input column names and missing-data handling.
4. Recalculate permutation P values using a null-centered concordance statistic as a sensitivity analysis.
5. Distinguish window-level significance from biological replicate-level uncertainty in manuscript text.
6. Record output checksums and comparison tolerances against archived manuscript tables.

**Status:** source restored and syntax checked; **no manuscript-scale numerical reproduction claim**.
