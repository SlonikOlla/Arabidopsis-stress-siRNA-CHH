# Audit of recovered preprocessing fragments

Status: **recovered original workspace files; not yet validated as a complete pipeline**. The copies in `scripts/recovered_original/` preserve the source text without silently correcting it.

## bowtie_to_weighted_bed.awk

The recovered file parses the read identifier for `_count_`, extracts the count, and writes BED-like columns: chromosome, start, end, identifier, count, strand. **It does not divide the read count by the number of genomic alignments.** The comment says a first pass supplied the number of alignments, but that quantity is never used in this AWK script. Thus the file name must not be treated as evidence of fractional multimapper assignment.

A separate upstream or downstream weighting step may exist; it must be identified and verified before asserting that the published 24-nt abundance tracks used fractional allocation.

## bin_methylation.awk

The recovered file groups rows by chromosome and integer-width bin, sums methylated and unmethylated counts, and computes methylated/(methylated+unmethylated). This implements read-weighted methylation for the supplied rows and context.

**Open questions:** whether the input position is zero-based or one-based; whether `$4` is the context in the actual input; whether `$5`/`$6` are methylated/unmethylated counts; whether cytosine counts and coverage filters were applied downstream; and whether chromosome naming and nuclear-only filters were enforced. The AWK output iteration order is unspecified and must be sorted before deterministic comparisons.

## Reproduction gate

1. Identify the executed preprocessing commands, including Bowtie alignment and any multimapper weighting stage.
2. Test on synthetic reads with 1, 2 and 4 alignments; confirm each read's total fractional count is conserved.
3. Check methylation bin boundary behavior against TAIR10 input coordinate conventions.
4. Compare recomputed 100-bp/500-bp matrices against retained matrices and record numerical differences.
5. Only after these tests, cite these scripts as reproducing published processing.

No claim of a successful end-to-end rerun is made here.
