#!/usr/bin/env python3
import gzip
from pathlib import Path
from collections import defaultdict
import pandas as pd

ROOT = Path("heat_consensus/methylation")
OUT = Path("results/validation_20261014/site_counts")
OUT.mkdir(parents=True, exist_ok=True)

samples = sorted(
    p.name.split("_")[0]
    for p in (ROOT / "bedGraph").glob("*.bedGraph.gz")
)
samples = sorted(set(samples))

for ctx in ("CG", "CHG"):
    for sample in samples:
        files = list((ROOT / "context").glob(f"{sample}_*_{ctx}.bedGraph.gz"))
        if len(files) != 1:
            raise RuntimeError(f"{sample} {ctx}: expected one file, found {len(files)}")

        counts = {100: defaultdict(int), 500: defaultdict(int)}

        with gzip.open(files[0], "rt") as fh:
            for line in fh:
                p = line.split()
                if len(p) < 5:
                    continue

                chrom, pos = p[0], int(p[1])
                if chrom not in {"1", "2", "3", "4", "5"}:
                    continue

                for size in (100, 500):
                    start = (pos // size) * size
                    counts[size][(chrom, start)] += 1

        for size in (100, 500):
            rows = [
                (chrom, start, start + size, n)
                for (chrom, start), n in counts[size].items()
            ]
            df = pd.DataFrame(
                rows, columns=["chr", "start", "end", f"n{ctx}"]
            )
            df = df.sort_values(["chr", "start"])
            dest = OUT / f"{sample}_{ctx}_{size}bp_site_counts.tsv"
            df.to_csv(dest, sep="\t", index=False)

            print(
                f"{sample} {ctx} {size}bp: "
                f"{len(df):,} windows",
                flush=True
            )
