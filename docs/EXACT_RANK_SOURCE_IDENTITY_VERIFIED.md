# Original script source identity verified — 2026-10-13

The manuscript author independently downloaded both Python scripts from the `recovery-audit-v2` GitHub raw URLs and computed SHA256 in WSL. The hashes match the corresponding scripts in the original local analysis directory byte for byte.

| File | Local SHA256 | GitHub raw SHA256 | Result |
| --- | --- | --- | --- |
| `scripts/exact_rank_CHH_10k_context_comparison.py` | `3f3dc7788979ff48d526b42f0deb353088d663fa798b66b1486d7075d3000f67` | `3f3dc7788979ff48d526b42f0deb353088d663fa798b66b1486d7075d3000f67` | MATCH |
| `scripts/exact_rank_CG_CHG.py` | `8d757cda6660ef3049be0004063a2b7e6ce36d9f7040c091c15657d9b82f535e` | `8d757cda6660ef3049be0004063a2b7e6ce36d9f7040c091c15657d9b82f535e` | MATCH |

Verification command:
```bash
for f in exact_rank_CHH_10k_context_comparison.py exact_rank_CG_CHG.py; do
  curl -fsSL "https://raw.githubusercontent.com/SlonikOlla/Arabidopsis-stress-siRNA-CHH/recovery-audit-v2/scripts/$f" | sha256sum
done
```

The author supplied the terminal output with both matching digests. This establishes source-file identity for the two exact-rank scripts, not identity of every upstream processing script or raw-read pipeline. See `EXACT_RANK_NUMERICAL_VALIDATION_2026-10-13.md` and `RELEASE_READINESS_2026-10-13.md` for remaining limitations.
