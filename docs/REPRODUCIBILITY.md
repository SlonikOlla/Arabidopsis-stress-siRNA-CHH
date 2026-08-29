# Reproducibility notes

This repository accompanies a cross-study integration analysis. Environmental stress small-RNA and methylation profiles were not generally generated from the same biological samples. Dataset pairing therefore prioritizes species/genotype, tissue, developmental stage, stress identity, and treatment duration, while biological mismatches are retained explicitly.

Analyses are performed separately at 100-bp and 500-bp resolution. Missing methylation measurements are excluded rather than imputed. For phosphate analyses, dataset-specific missing-value sentinels are removed before statistical analysis.

The final exact-rank extreme-tail analysis selects the upper and lower 1%, 5%, and 10% of the relevant change distribution by rank, then evaluates concordant changes after matching windows on control CHH methylation and control 24-nt siRNA abundance. This design avoids inflation from tied quantile thresholds and reduces confounding by baseline molecular state.

Positive-control genetic perturbations are included to demonstrate that the analysis framework detects strong spatial correspondence when present.

Raw sequencing and source methylation files are not redistributed and should be retrieved from their original public repositories using the listed accessions. The accessible retained project archive does not contain every original workstation script. Accordingly, reconstructed code is never labelled as the historical executed script; reference implementations and recovered-output provenance are identified explicitly in `scripts/README.md` and `results/retained_output_provenance.md`.
