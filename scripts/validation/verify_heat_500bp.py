import gzip
import numpy as np
import pandas as pd

base = "results/validation_20261014/"

samples = {
    "CTRL1": ("SRR25485472", 3660645.034),
    "CTRL2": ("SRR25485471", 4006770.103),
    "CTRL3": ("SRR25485470", 2397307.947),
    "HEAT1": ("SRR25485469", 5965676.605),
    "HEAT2": ("SRR25485468", 6662821.724),
    "HEAT3": ("SRR25485467", 2654259.900),
}

historical = pd.read_csv(
    "heat_consensus/results/heat_24nt_500bp_matrix.tsv",
    sep="\t"
)

keys = list(zip(
    historical["chr"].astype(int),
    historical["start"].astype(int)
))

results = []

for sample, (srr, denominator) in samples.items():
    counts = {}

    with gzip.open(base + srr + "_fractional.bed.gz", "rt") as handle:
        for line in handle:
            chrom, start, end, weight, strand = line.rstrip().split("\t")

            if chrom not in {"1", "2", "3", "4", "5"}:
                continue

            midpoint = (int(start) + int(end)) // 2
            key = (int(chrom), midpoint // 500 * 500)

            counts[key] = counts.get(key, 0.0) + float(weight)

    reconstructed = np.array([
        counts.get(key, 0.0) / denominator * 1e6
        for key in keys
    ])

    original = historical[sample].to_numpy()
    diff = np.abs(reconstructed - original)

    results.append({
        "sample": sample,
        "windows": len(diff),
        "within_1e-5": int((diff < 1e-5).sum()),
        "max_absolute_error": float(diff.max()),
        "mean_absolute_error": float(diff.mean()),
        "pearson_r": float(np.corrcoef(reconstructed, original)[0, 1])
    })

report = pd.DataFrame(results)
report.to_csv(base + "heat_500bp_reproduction_report.tsv",
              sep="\t", index=False)

print(report.to_string(index=False))
