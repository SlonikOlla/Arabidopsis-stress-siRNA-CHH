# Resubmission validation status — 2026-10-15

**Status: interim, not a completed end-to-end reproduction.** This document records outputs executed in the author's local WSL analysis workspace, `~/arabidopsis_siRNA_methylation`. Those local inputs, scripts and derived tables are **not** automatically present in this GitHub repository.

## Heat siRNA reconstruction
- GSE239836, three control and three heat small-RNA libraries.
- The retained Bowtie 1 alignments reproduced the nuclear 500-bp and 100-bp siRNA matrices, with all 8,578,572 tested matrix values agreeing to <1e-5 CPM.
- Reconstructed denominator: fractional **nuclear 18–30-nt** alignments; numerator: fractional nuclear 24-nt alignment midpoints; see the workspace scripts `scripts/validation/verify_heat_500bp.py`, `verify_heat_100bp.py`, and `fractional_bowtie_to_bed.py`.
- This **differs from the older README statement** of a 16–27-nt denominator. The older description must not be treated as a verified reconstruction of the retained heat matrices.
- Original FASTQ processing, historical Bowtie invocation, and exact upstream filtering commands have not all been recovered.

## Methylation
- Reconstructed observed cytosine-site counts for CG/CHG/CHH from retained context bedGraphs.
- **Observed cytosine-site counts are not bisulfite sequencing read depth.** Per-site read depth is absent from the retained methylation fractions.

## Mappability
- TAIR10 nuclear 24-mer exact-match uniqueness quantified using Jellyfish 2.2.10, canonical 24-mers, midpoint-assigned 500-bp windows.
- 238,296 windows; 118,955,407 valid 24-mer positions; 105,925,943 unique positions; 346 windows with zero valid positions.
- Pilot 500 Bowtie exact-match queries agreed with Jellyfish uniqueness.

## Heat-only common-window CG/CHG/CHH sensitivity
- Same 500-bp genomic windows across contexts; 5% exact-rank tails; 10,000 baseline-stratified hypergeometric null draws per test.
- Eligibility thresholds in **each of six relevant methylome samples**: CG >=5 observed sites, CHG >=5, CHH >=50.
- Eligible windows: 6h 218,849; 12h 219,570; 24h 217,696.
- Median observed/expected enrichment (four related directional tests each):
  - 6h: CG 1.0358; CHG 1.0590; CHH 1.1056.
  - 12h: CG 1.0291; CHG 1.0387; CHH 1.0945.
  - 24h: CG 1.0431; CHG 1.0347; CHH 1.0970.
- CHH exceeds both CG and CHG in all 12 related analytical comparisons. CHG exceeds CG in 9/12; a universal CHH > CHG > CG hierarchy is **not established**.
- The four directional tests and three time points are not independent biological replicates.
- Local generating script: `scripts/validation/heat_common_window_context_hierarchy.py`; local output: `results/validation_20261015/heat_context_hierarchy/`.

## TE sign-concordance sensitivity
- Local scripts: `scripts/validation/heat_TE_CHH_matched_validation.py` and `heat_TE_CHH_mappability_validation.py`.
- At 500bp and CHH observed-site threshold >=50, TE-minus-nonTE sign concordance: 6h -0.04913; 12h -0.05827; 24h -0.04305.
- Adding genome-derived 24-mer mappability to baseline-siRNA, baseline-CHH, and site-count strata gave null expectations approximately -0.05806, -0.06999, -0.05303 (999 draws; nominal p=.011, .003, .006).
- **Do not interpret this as positive overall TE concordance.** It is a different statistic from original extreme-tail TE enrichment. True read-depth matching and spatial-dependence-sensitive nulls remain unresolved.

## Biological design caveat
Heat siRNA: GSE239836, Col-0 7-day seedlings, 37°C 1h. Heat methylome: GSE139941, Col-0 21-day leaves, 42°C 6/12/24h. Independent, developmentally and experimentally mismatched studies. These are cross-study genomic associations, not matched longitudinal or causal responses.

Drought/pathogen: exploratory because independent biological replication is inadequate in at least one molecular layer. Phosphate siRNA replication still unresolved.

## Environment observed locally
Python 3.11.17; Bowtie 1.3.1; Jellyfish 2.2.10. Other historical versions and an executed clean-start workflow are not yet verified.

## Outstanding publication gates
1. Obtain and deposit local validation scripts plus compact machine-readable outputs.
2. Audit original processing commands and normalization descriptions; document irrecoverable historical parameters.
3. Provide an executed, environment-pinned reproduction starting from stated downloadable inputs.
4. Decide whether any heat comparison meets the editor's biological comparability requirement; avoid confirmatory paired-response claims.
5. Reconcile all original TE-tail and context-hierarchy claims with the restricted analyses.
6. Test read-depth/mappability matching where source data permit; otherwise explicitly delimit claims.
