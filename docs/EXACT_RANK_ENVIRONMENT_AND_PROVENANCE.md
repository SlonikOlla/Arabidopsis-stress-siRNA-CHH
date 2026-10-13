# Exact-rank validation environment and source provenance

Validation performed by the manuscript author on 2026-10-13 using the original processed matrices in WSL.

## Environment
- Python: **3.11.17**
- NumPy: **2.4.6**
- pandas: **3.0.6**
- Conda environment name: `arabidopsis-validation`

## Original local script SHA256 (author-reported)
```text
3f3dc7788979ff48d526b42f0deb353088d663fa798b66b1486d7075d3000f67  scripts/exact_rank_CHH_10k_context_comparison.py
8d757cda6660ef3049be0004063a2b7e6ce36d9f7040c091c15657d9b82f535e  scripts/exact_rank_CG_CHG.py
```

GitHub recovery branch contains both scripts:
- `scripts/exact_rank_CHH_10k_context_comparison.py` (Git blob SHA `bc9935147124cab23f5dc34528451dca4ffe7397`)
- `scripts/exact_rank_CG_CHG.py` (Git blob SHA `8c5df95185a8468d740d9e7624a8ae8fb5f13e46`)

**Note:** Git blob SHAs are not SHA256 hashes. The uploaded file SHA256 values must be independently computed and compared with the local hashes before asserting byte-for-byte identity.

## Reproduction from processed matrices
Run from repository project root, with expected input matrices available at the relative paths hard-coded in the original scripts:

```bash
conda create -n arabidopsis-validation -c conda-forge python=3.11.17 numpy=2.4.6 pandas=3.0.6 -y
conda activate arabidopsis-validation
python -u scripts/exact_rank_CHH_10k_context_comparison.py
python -u scripts/exact_rank_CG_CHG.py
```

**Caution:** These original scripts write directly to their default `results/` paths. For a non-destructive verification, use separate copies with output paths redirected to a validation subdirectory, as done by the author on 2026-10-13. The CHH script compares to `results/all_stresses_extreme_tail_EXACT_RANK_FINAL.tsv`. Some large source matrices are not included in GitHub.

## Results
See `docs/EXACT_RANK_NUMERICAL_VALIDATION_2026-10-13.md`. All 504 selected counts and observed statistics reproduced exactly; CG/CHG permutation statistics reproduce to floating point precision; CHH has two borderline FDR call differences.

## Limitations
This validation begins from processed matrices. It does not validate upstream alignment, multimapper handling, biological replication, or TE-enrichment null models. The original 336-test CG/CHG script FDR family is different from the archived 504-test combined table.
