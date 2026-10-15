# Proposed GitHub release — validation checkpoint (NOT YET PUBLISHED)

**Suggested tag:** `v1.2.0-validation`  
**Suggested title:** October 2026 heat validation checkpoint  
**Prerelease:** YES  
**Target:** reviewed commit after PR #2 is reconciled, not automatically `main`.

## Scope

This checkpoint documents independent reconstruction and reruns of selected downstream analyses in the *Arabidopsis* stress siRNA–methylation study. It **does not** establish an end-to-end raw-read-to-figure reproducible workflow and should **not** be described as a final resubmission package.

### Verified in the author's retained WSL workspace on October 15, 2026

- Heat 24-nt siRNA 500-bp matrix: 1,429,776 CPM values reproduced, maximum absolute deviation 4.729281e-7 CPM.
- Heat 24-nt siRNA 100-bp matrix: 7,148,796 CPM values reproduced, maximum absolute deviation 3.782034e-7 CPM.
- Heat 500-bp common-window CG/CHG/CHH exact-rank hierarchy: 235,480 common windows; 218,849, 219,570, and 217,696 eligible windows at 6, 12, and 24 hours; CHH enrichment exceeds CG and CHG in 12 of 12 related directional comparisons. These are **not biological replicates**.
- TE/non-TE sign-concordance sensitivity analyses rerun with baseline and mappability stratification; TE-minus-nonTE effects are negative and do not establish stronger positive TE concordance.
- All seven workflow stages passed preflight; the five downstream stages listed above executed successfully.
- Confirmed 48 CG/CHG observed-cytosine-site-count tables and 12 separately stored CHH 500-bp inputs.
- Corrected heat CPM denominator to fractionally mapped nuclear **18–30-nt** small RNAs.

### Important limitations

- Heat siRNA: 7-day seedlings, 37°C, 1 h; methylome: 21-day leaves, 42°C, 6/12/24 h. These are **cross-study genomic associations**, not matched or causal heat responses.
- Drought/pathogen small-RNA contrasts have insufficient independent biological replication for confirmatory cross-layer inference; phosphate replication needs verification.
- Heat methylome per-cytosine values do not supply true bisulfite read depths. Observed cytosine-site counts are not read-depth measurements.
- TE null analyses do not fully control spatial dependence or sequencing coverage.
- Exact historical FASTQ trimming, Bowtie alignment invocation and complete dependency versions are not independently recovered.
- The 1.1-GB Jellyfish database and mappability TSVs were present locally, but reference generation was not rerun during this checkpoint.
- Clean-clone end-to-end FASTQ-to-figures reproduction remains outstanding.

## Publication gate

Before publishing, review PR #2, reconcile its branch with `main`, confirm that all intended validation scripts/results are tracked at canonical paths, run basic syntax/import tests on the checked-out branch, and inspect the final diff. Keep this release marked **prerelease**. A final journal-facing release requires the unresolved provenance and reproducibility issues to be documented and, where possible, resolved.
