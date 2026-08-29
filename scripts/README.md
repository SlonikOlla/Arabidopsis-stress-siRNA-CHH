# Analysis scripts

This repository contains transparent analysis code for the manuscript.

## Available code

- `exact_rank_extreme_tail_reference.py` implements the final exact-rank extreme-tail statistical design: exact 1%, 5%, and 10% tails; rank-balanced baseline matching on control 24-nt abundance and control CHH methylation; within-stratum permutation; empirical enrichment P values; and Benjamini-Hochberg correction.

The final analyses used seed `20260829`. The primary analysis used 10×10 baseline strata and 1,000 permutations; a 20×20 sensitivity analysis and 10,000-draw annotation/TE analyses were also used where described in the manuscript.

## Provenance note

The accessible retained project archive contains final outputs, command logs, software/mapping parameters, and analysis summaries, but not every original workstation Python script. We therefore do **not** present reconstructed code as if it were the original historical script. Reference implementations are explicitly labelled as such.

Recovered processing parameters and output provenance are documented in `../results/retained_output_provenance.md` and `../docs/REPRODUCIBILITY.md`.

Small-RNA alignment parameters recovered from the retained analysis records were Bowtie `-f -v 0 -a -m 50 --best --strata`, with fractional treatment of multimappers and nuclear 16–27-nt mapped abundance used for normalization. Cutadapt 4.7 was used where adapter removal was required.
