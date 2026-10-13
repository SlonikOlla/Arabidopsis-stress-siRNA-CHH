# Resubmission gate 2 — biological replication audit (2026-10-13)

Source: `metadata/datasets.tsv` in this repository. This is a **metadata-level preliminary audit**, not a raw-SRA accession/library verification. The editor's requirements take precedence over earlier manuscript interpretations.

| Stress | sRNA dataset / replication | Methylome dataset / replication | Cross-assay comparability | Provisional classification |
| --- | --- | --- | --- | --- |
| Heat | GSE239836; 3 per condition; 7-day seedlings, 37°C 1h | GSE139941; 3 per condition/time; 21-day leaves, 42°C 6/12/24h | Major tissue/developmental-stage/temperature/duration mismatch | Replicated within each layer, but **not yet qualified** as biologically matched primary evidence |
| Drought | GSE26356; 1 per condition; shoots, 4-week plants | GSE94075; 3 per condition; whole rosette, 4 weeks | Different protocol/genotype; sRNA unreplicated | Exploratory only; exclude from confirmatory claims |
| Pathogen | GSE19694; 2 mock and 1 infected library per time; 6/14h | GSE128768; one deposited pooled sample per condition; ~72h | Time mismatch; no independent infected sRNA replicate or methylome variance | Exploratory only; exclude from confirmatory claims |
| Phosphate | GSE17741; vague 'public libraries' label; 17-day roots, 5d ±Pi | GSE72770; 2 per condition; 7-day roots | Developmental/treatment mismatch; sRNA biological replicates unverified | Unresolved pending accession-level verification |

**Important:** Genomic windows are not biological replicates. Technical replicates and pooled biological material do not establish independent sample-level variance.

## Required accession-level inventory

For every SRR/GSM sample, record: stress, assay, GEO/SRA accession, biological replicate ID, technical replicate ID, control/treatment, genotype, tissue, developmental age, growth conditions, dose, duration, sequencing library, pooled/not pooled, and provenance/source citation. Only then decide whether both molecular layers have independent biological replication under a defensibly matched comparison.

## Primary-claim decision rule

Retain as confirmatory only contrasts with independent biological replication in **both** assays and adequate biological comparability. A replicated but mismatched heat experiment is not automatically a matched contrast. Drought and pathogen may be retained as explicitly descriptive/exploratory, with no inference from windows as biological replication. Re-evaluate TE enrichment and CHH > CHG > CG on the final qualified subset.

## Other editor gates

1. End-to-end executed, version-pinned pipeline and all test-family outputs remain outstanding.
2. TE-associated mappability/coverage-matched null or suitable library-shuffle remains outstanding.
3. Context hierarchy must be recalculated after restrictions.
4. Software versions must be reported for every executed stage.

This document does **not** claim these gates have been satisfied.
