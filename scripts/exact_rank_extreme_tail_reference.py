#!/usr/bin/env python3
"""Reference implementation of the final exact-rank extreme-tail test.

This script was prepared for the public reproducibility repository from the
final analysis specification documented in the manuscript and retained output
logs. It is NOT represented as the original historical workstation script.

Expected input: a tab-delimited table with columns
    stress, time, resolution, ctrl24, ctrlCHH, delta24, deltaCHH
and any additional genomic-coordinate columns desired by the user.

For each stress/time/resolution group, the script:
  * removes non-finite values and implausible CHH values;
  * forms exact-rank 1%, 5%, and 10% tails;
  * creates rank-balanced baseline strata from control 24-nt abundance and
    control CHH methylation (10 x 10 by default);
  * holds the selected tail fixed and shuffles the counterpart change values
    within baseline strata;
  * calculates observed/expected concordance and a one-sided empirical
    enrichment P value;
  * applies Benjamini-Hochberg correction across the complete output family.

Random seed used in the final analyses: 20260829.
"""

from __future__ import annotations

import argparse
import numpy as np
import pandas as pd

SEED = 20260829
TAILS = (1, 5, 10)


def exact_tail_mask(x: pd.Series, pct: int, side: str) -> np.ndarray:
    """Select exactly floor(n*pct/100) observations by stable rank."""
    a = np.asarray(x, dtype=float)
    n = len(a)
    k = max(1, int(np.floor(n * pct / 100.0)))
    order = np.argsort(a, kind="mergesort")
    idx = order[:k] if side == "low" else order[-k:]
    mask = np.zeros(n, dtype=bool)
    mask[idx] = True
    return mask


def rank_bins(x: pd.Series, n_bins: int) -> np.ndarray:
    """Equal-count rank bins, avoiding quantile-edge problems from ties."""
    a = np.asarray(x, dtype=float)
    n = len(a)
    order = np.argsort(a, kind="mergesort")
    bins = np.empty(n, dtype=int)
    bins[order] = np.minimum((np.arange(n) * n_bins) // n, n_bins - 1)
    return bins


def bh(pvals: np.ndarray) -> np.ndarray:
    p = np.asarray(pvals, dtype=float)
    n = len(p)
    order = np.argsort(p)
    ranked = p[order]
    q = ranked * n / np.arange(1, n + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    q = np.clip(q, 0, 1)
    out = np.empty(n, dtype=float)
    out[order] = q
    return out


def permutation_test(df: pd.DataFrame, selected_var: str, selected_side: str,
                     counterpart_var: str, counterpart_sign: str, pct: int,
                     n_strata: int, n_perm: int, rng: np.random.Generator):
    selected = exact_tail_mask(df[selected_var], pct, selected_side)
    y = df[counterpart_var].to_numpy(float)
    concordant = y > 0 if counterpart_sign == "gain" else y < 0
    observed = int(np.sum(selected & concordant))

    b24 = rank_bins(df["ctrl24"], n_strata)
    bchh = rank_bins(df["ctrlCHH"], n_strata)
    strata = b24 * n_strata + bchh
    members = [np.flatnonzero(strata == s) for s in np.unique(strata)]

    null = np.empty(n_perm, dtype=float)
    yp = y.copy()
    for i in range(n_perm):
        for ix in members:
            yp[ix] = y[rng.permutation(ix)]
        c = yp > 0 if counterpart_sign == "gain" else yp < 0
        null[i] = np.sum(selected & c)

    null_mean = float(null.mean())
    oe = float(observed / null_mean) if null_mean > 0 else np.nan
    p = float((1 + np.sum(null >= observed)) / (n_perm + 1))
    return selected.sum(), observed, null_mean, oe, p


def run_group(df: pd.DataFrame, n_strata: int, n_perm: int,
              rng: np.random.Generator) -> list[dict]:
    tests = [
        ("CHH_gain_to_24_gain", "deltaCHH", "high", "delta24", "gain"),
        ("CHH_loss_to_24_loss", "deltaCHH", "low", "delta24", "loss"),
        ("24_gain_to_CHH_gain", "delta24", "high", "deltaCHH", "gain"),
        ("24_loss_to_CHH_loss", "delta24", "low", "deltaCHH", "loss"),
    ]
    rows = []
    for pct in TAILS:
        for name, sv, side, cv, sign in tests:
            nsel, obs, exp, oe, p = permutation_test(
                df, sv, side, cv, sign, pct, n_strata, n_perm, rng
            )
            rows.append({
                "test": name, "pct": pct, "n_selected": int(nsel),
                "observed": obs, "null_mean": exp, "OE": oe,
                "empirical_p": p,
            })
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input_tsv")
    ap.add_argument("output_tsv")
    ap.add_argument("--strata", type=int, default=10)
    ap.add_argument("--permutations", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=SEED)
    args = ap.parse_args()

    x = pd.read_csv(args.input_tsv, sep="\t")
    required = {"stress", "time", "resolution", "ctrl24", "ctrlCHH", "delta24", "deltaCHH"}
    missing = required - set(x.columns)
    if missing:
        raise SystemExit(f"Missing columns: {sorted(missing)}")

    cols = ["ctrl24", "ctrlCHH", "delta24", "deltaCHH"]
    x = x[np.isfinite(x[cols]).all(axis=1)].copy()
    x = x[x["ctrlCHH"].between(0, 1) & x["deltaCHH"].between(-1, 1)].copy()

    rng = np.random.default_rng(args.seed)
    out = []
    for keys, g in x.groupby(["stress", "time", "resolution"], sort=True):
        for r in run_group(g.reset_index(drop=True), args.strata, args.permutations, rng):
            r.update(dict(zip(["stress", "time", "resolution"], keys)))
            out.append(r)

    res = pd.DataFrame(out)
    res["FDR_BH"] = bh(res["empirical_p"].to_numpy())
    res.to_csv(args.output_tsv, sep="\t", index=False)


if __name__ == "__main__":
    main()
