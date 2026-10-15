#!/usr/bin/env python3
"""Heat CG/CHG/CHH hierarchy on common, site-count-filtered 500bp windows.

Preserves the exact-rank selection and baseline-stratified
hypergeometric null of scripts/exact_rank_CG_CHG.py.

Site counts are observed cytosine positions, NOT sequencing read depth.
The heat siRNA and methylation data are from independent experiments.
"""

from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path("results/validation_20261015/heat_context_hierarchy")
ROOT.mkdir(parents=True, exist_ok=True)

KEYS = ["chr", "start", "end"]
CONTEXTS = ["CG", "CHG", "CHH"]
THRESHOLDS = {"CG": 5, "CHG": 5, "CHH": 50}
TIMES = {
    "6h":  [340, 341, 342, 343, 344, 345],
    "12h": [340, 341, 342, 346, 347, 348],
    "24h": [340, 341, 342, 349, 350, 351],
}

N_PERM = 10000
NBINS = 10
TAIL = 0.05
SEED = 20260829
rng = np.random.default_rng(SEED)


def rank_bins(x):
    n = len(x)
    order = np.argsort(x, kind="mergesort")
    ranks = np.empty(n, dtype=int)
    ranks[order] = np.arange(n)
    return np.floor(ranks * NBINS / n).astype(int)


def exact_tail(x, direction):
    k = int(np.floor(len(x) * TAIL))
    order = np.argsort(x, kind="mergesort")
    return order[:k] if direction == "loss" else order[-k:]


def test(selected, counterpart, direction, strata):
    target = counterpart > 0 if direction == "gain" else counterpart < 0
    selected_mask = np.zeros(len(counterpart), dtype=bool)
    selected_mask[selected] = True

    observed = int(np.sum(target & selected_mask))
    null = np.zeros(N_PERM, dtype=np.int64)

    for st in np.unique(strata):
        idx = strata == st
        N = int(idx.sum())
        K = int(target[idx].sum())
        n = int(selected_mask[idx].sum())

        if n == 0 or K == 0:
            continue
        if K == N:
            null += n
        else:
            null += rng.hypergeometric(
                ngood=K, nbad=N-K, nsample=n, size=N_PERM
            )

    expected = float(null.mean())
    return {
        "observed": observed,
        "null_mean": expected,
        "OE": observed / expected if expected > 0 else np.nan,
        "empirical_p_enrich": (
            1 + int(np.sum(null >= observed))
        ) / (N_PERM + 1),
        "empirical_p_deplete": (
            1 + int(np.sum(null <= observed))
        ) / (N_PERM + 1),
        "null_sd": float(null.std(ddof=1)),
    }


def read_counts(ctx, num):
    gsm = f"GSM4150{num}"

    if ctx == "CHH":
        folder = Path("heat_consensus/methylation/CHH500")
        matches = sorted(folder.glob(f"{gsm}*_CHH_500bp.tsv"))
    else:
        folder = Path("results/validation_20261014/site_counts")
        matches = sorted(
            folder.glob(f"{gsm}_{ctx}_500bp_site_counts.tsv")
        )

    if len(matches) != 1:
        raise RuntimeError(
            f"Expected exactly one {ctx} file for {gsm}; "
            f"found {matches}"
        )

    col = f"n{ctx}"
    counts = pd.read_csv(
        matches[0], sep="\t", usecols=KEYS + [col]
    ).set_index(KEYS)[col]

    if counts.index.has_duplicates:
        raise RuntimeError(f"Duplicate coordinates in {matches[0]}")

    return counts


print("Loading heat matrices...", flush=True)

s = pd.read_csv(
    "heat_consensus/results/heat_joint_500bp.tsv",
    sep="\t",
    usecols=KEYS + ["CTRL24", "delta24"]
)

matrices = {}
for ctx in CONTEXTS:
    matrices[ctx] = pd.read_csv(
        f"heat_consensus/results/heat_{ctx}_500bp_matrix.tsv",
        sep="\t",
        usecols=KEYS + [
            "CTRLmean",
            "delta" + ctx + "_6h",
            "delta" + ctx + "_12h",
            "delta" + ctx + "_24h",
        ]
    ).set_index(KEYS)

common = s.set_index(KEYS)

for ctx in CONTEXTS:
    common = common.join(
        matrices[ctx][["CTRLmean"]].rename(
            columns={"CTRLmean": f"baseline_{ctx}"}
        ),
        how="inner",
        validate="one_to_one",
    )

print(f"Common windows: {len(common):,}", flush=True)

count_masks = {}
for ctx in CONTEXTS:
    for num in range(340, 352):
        count_masks[(ctx, num)] = (
            read_counts(ctx, num)
            .reindex(common.index)
            .ge(THRESHOLDS[ctx])
        )

rows = []
eligibility_rows = []

for time, ids in TIMES.items():
    eligible = pd.Series(True, index=common.index)

    for ctx in CONTEXTS:
        for num in ids:
            eligible &= count_masks[(ctx, num)]

    eligibility_rows.append({
        "time": time,
        "n_common": len(common),
        "n_eligible_site_counts": int(eligible.sum()),
    })

    print(
        f"{time}: {int(eligible.sum()):,} windows "
        "pass site-count thresholds",
        flush=True,
    )

    for ctx in CONTEXTS:
        d = common.loc[eligible, [
            "CTRL24", "delta24", f"baseline_{ctx}"
        ]].copy()

        delta_col = f"delta{ctx}_{time}"
        d["delta_methylation"] = (
            matrices[ctx][delta_col].reindex(d.index)
        )

        d = d.replace([np.inf, -np.inf], np.nan)
        d = d.dropna().reset_index(drop=True)

        b24 = d["CTRL24"].to_numpy(float)
        bm = d[f"baseline_{ctx}"].to_numpy(float)
        x = d["delta24"].to_numpy(float)
        y = d["delta_methylation"].to_numpy(float)

        strata = rank_bins(b24) * NBINS + rank_bins(bm)

        directions = [
            ("24_gain_to_CTX_gain", x, "gain", y, "gain"),
            ("24_loss_to_CTX_loss", x, "loss", y, "loss"),
            ("CTX_gain_to_24_gain", y, "gain", x, "gain"),
            ("CTX_loss_to_24_loss", y, "loss", x, "loss"),
        ]

        for label, selector, select_dir, counterpart, target_dir in directions:
            selected = exact_tail(selector, select_dir)
            result = test(selected, counterpart, target_dir, strata)

            rows.append({
                "context": ctx,
                "stress": "heat",
                "time": time,
                "resolution": 500,
                "pct": 5,
                "direction": label,
                "n_eligible": len(d),
                "n_selected": len(selected),
                **result,
            })

        print(f"  {ctx}: {len(d):,} finite windows", flush=True)

results = pd.DataFrame(rows)
results.to_csv(
    ROOT / "heat_common_window_context_exact_rank_10k.tsv",
    sep="\t", index=False
)

pd.DataFrame(eligibility_rows).to_csv(
    ROOT / "heat_common_window_eligibility.tsv",
    sep="\t", index=False
)

matched = results.pivot(
    index=["time", "resolution", "pct", "direction"],
    columns="context",
    values="OE",
).reset_index()

matched["CHH_minus_CG"] = matched["CHH"] - matched["CG"]
matched["CHH_minus_CHG"] = matched["CHH"] - matched["CHG"]
matched["CHG_minus_CG"] = matched["CHG"] - matched["CG"]

matched.to_csv(
    ROOT / "heat_common_window_context_OE_comparison.tsv",
    sep="\t", index=False
)

print("\n=== Time-specific summary ===")
for time, g in matched.groupby("time", sort=True):
    print(f"\n{time}")
    print("Median O/E:")
    print(g[CONTEXTS].median().round(4).to_string())
    print("CHH > CHG:", int((g.CHH > g.CHG).sum()), "/ 4")
    print("CHG > CG:", int((g.CHG > g.CG).sum()), "/ 4")
    print("CHH > CG:", int((g.CHH > g.CG).sum()), "/ 4")

print("\nSaved results to:", ROOT)
