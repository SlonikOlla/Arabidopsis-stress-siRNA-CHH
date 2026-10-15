# Single-entry heat validation workflow (2026-10-15)

**This is a stage runner, not a complete FASTQ-to-figure pipeline.** It is designed for the retained local WSL workspace `~/arabidopsis_siRNA_methylation`.

```bash
cd ~/arabidopsis_siRNA_methylation
python3 scripts/validation/run_validation_workflow.py
# After resolving every reported missing prerequisite:
python3 scripts/validation/run_validation_workflow.py --stage heat-hierarchy --execute
# Only if all stages and their external prerequisites are available:
python3 scripts/validation/run_validation_workflow.py --execute
```

Preflight is the default; no analysis is run without `--execute`. It checks required files and directories, Python numpy/pandas, and the presence of Jellyfish/bedtools for stages requiring them. The seven stages are: site-count generation, 24-mer mappability query, 500-bp and 100-bp siRNA matrix verification, common-window heat context hierarchy, TE baseline/site-count matching, and TE/mappability matching.

**Limitations:** Original Bowtie/FASTQ processing and Jellyfish database creation are not included. TE annotation inputs are partially resolved inside the original scripts and are not all covered by preflight. The original analysis scripts may require substantial memory/time and additional software. Site counts are not bisulfite sequencing read depths.

## Tests in isolated container (2026-10-15)

- All eight uploaded validation scripts compiled: PASS.
- Independent retained-output checks on uploaded tables: PASS for 36 heat context tests, three contexts, three times, observed/expected arithmetic, eligibility counts, and both 12-row TE summary schemas.
- Preflight correctly reported absent intermediate matrices, TAIR10 FASTA, Jellyfish database, and Jellyfish/bedtools binaries. **No full scientific analysis stage was executed in the isolated container.**

**Next gate:** Run the driver on the author's WSL workspace and inspect any missing inputs, then run `--stage heat-hierarchy --execute`. Do not merge or tag a final Zenodo release until execution and documentation have been verified.


## WSL execution audit — 2026-10-15 (user-reported terminal output)

The author executed the driver in `~/arabidopsis_siRNA_methylation` under the `arabidopsis-validation` environment. All seven preflight stages reported READY. Executed stages and outcomes:

- `--stage heat-hierarchy --execute`: successful; 235,480 common windows, eligible 6h=218,849, 12h=219,570, 24h=217,696; CG/CHG/CHH median O/E and 12 direction-level CHH superiority checks agreed with retained reference.
- `--stage siRNA-500bp --execute`: successful; 238,296 windows × six samples = 1,429,776 values, all within 1e-5 CPM; maximum absolute error 4.729281e-7.
- `--stage siRNA-100bp --execute`: successful; 1,191,466 windows × six samples = 7,148,796 values, all within 1e-5 CPM; maximum absolute error 3.782034e-7.
- `--stage TE-matched --execute`: successful; 12 heat × observed-CHH-site-count thresholds; results agreed with retained stratified-null table.
- `--stage TE-mappability --execute`: successful; 12 heat × threshold tests; at 50-site threshold empirical p=0.011 (6h), 0.003 (12h), 0.006 (24h). TE minus nonTE sign concordance remains negative; do not characterize as stronger positive TE concordance.

### Methylome site-count input arrangement

The `results/validation_20261014/site_counts/` directory has **48** files, not 72: for all 12 GSM4150340–GSM4150351 samples, CG and CHG each have both 100-bp and 500-bp site-count TSVs (12 files per context/resolution). The heat hierarchy script reads **CHH 500-bp site-count input separately** from `heat_consensus/methylation/CHH500/GSM4150*_CHH_500bp.tsv`. The author confirmed exactly one matching file for each of the 12 GSM samples. The missing CHH-named files in the 48-file directory are therefore expected. This does **not** verify the existence of CHH 100-bp site-count files, which the heat hierarchy stage does not require.

The Jellyfish canonical TAIR10 24-mer database (~1.1 GB) and both 500-bp mappability TSVs (~7.5 MB each) exist locally, generated October 13; the 48 CG/CHG site-count TSVs (~608 MB total) also exist. No costly regeneration was performed. Their presence and prior successful downstream use do not constitute a fresh reference-generation rerun.

**Remaining release gates:** clean-clone execution from publicly obtainable inputs; dependency/version lock; full historical alignment-command provenance; README denominator correction (historical 16–27nt vs independently validated 18–30nt); no bisulfite read-depth reconstruction; biological cross-study heat mismatch; spatial dependence of TE null. Do not mark the complete raw-read pipeline reproducible.
