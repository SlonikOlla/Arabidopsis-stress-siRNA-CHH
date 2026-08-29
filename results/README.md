# Derived results and provenance

This directory contains compact derived material used to document and reproduce the manuscript analysis. Large raw sequencing and methylation files are not redistributed; source data should be retrieved from their original public repositories using the accessions in `../metadata/datasets.tsv`.

## Included

- `summary/Figure1_global_summary_source.tsv` — compact global/window-level summary retained from the analysis workspace.
- `retained_output_provenance.md` — provenance record for final statistical outputs and analysis parameters recovered from retained command/output logs.

## Final statistical analyses documented in the retained archive

The retained project records document the definitive exact-rank extreme-tail analysis, the 20×20 baseline sensitivity analysis, genomic-context analyses, TE-overlap sensitivity, TE-superfamily analysis, TE-family analysis, and TE-element-level sensitivity analysis. Their output names, test counts, key parameters, and recovered summary results are recorded in `retained_output_provenance.md`.

Exact machine-readable historical output tables are not reconstructed from rounded manuscript values when the original table is unavailable in the accessible archive. This distinction is intentional. The repository therefore separates directly retained machine-readable data from provenance recovered from logs and from explicitly labelled reference implementations.
