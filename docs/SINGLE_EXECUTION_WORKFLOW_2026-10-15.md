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
