# Inputs needed to complete the resubmission release

The October 15 documentation update does **not** certify a complete executable pipeline. The source workspace is outside this repository and the GitHub connector cannot access its WSL filesystem.

Transfer the following *text scripts* from `~/arabidopsis_siRNA_methylation/scripts/validation/` into `scripts/validation/` in a follow-up commit:
- `fractional_bowtie_to_bed.py`
- `verify_heat_500bp.py`
- `verify_heat_100bp.py`
- `build_heat_site_counts.py`
- `build_24mer_mappability.py`
- `heat_TE_CHH_matched_validation.py`
- `heat_TE_CHH_mappability_validation.py`
- `heat_common_window_context_hierarchy.py`

Transfer compact TSV output summaries, including the complete 36-row heat hierarchy test table, its 12-row paired comparison, eligibility table, and TE/mappability null summary. Large reference genomes, Jellyfish databases, Bowtie alignments, and sequencing reads should be linked by accession/checksum rather than committed to GitHub.

Before any versioned release, run a clean-clone smoke test with declared environment and inputs. Confirm the README normalization description against the executed heat matrix reconstruction. Do not overwrite or retroactively edit archived recovery release `v1.1.0-recovery` / DOI 10.5281/zenodo.23353757.
