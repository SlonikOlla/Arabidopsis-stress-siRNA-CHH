#!/usr/bin/env python3

from pathlib import Path
import csv
import subprocess

ROOT = Path("results/validation_20261014/mappability")
JF = ROOT / "TAIR10_24mer_canonical.jf"
GENOME = Path("genome/TAIR10.fa")
OUTPUT = ROOT / "TAIR10_24mer_500bp_midpoint_mappability.tsv"

K = 24
WINDOW = 500
BATCH = 1000
NUCLEAR = {"1", "2", "3", "4", "5"}


def read_fasta(path):
    name = None
    parts = []

    with open(path) as f:
        for line in f:
            if line.startswith(">"):
                if name is not None:
                    yield name, "".join(parts).upper()

                name = line[1:].split()[0]
                parts = []
            else:
                parts.append(line.strip())

    if name is not None:
        yield name, "".join(parts).upper()


def query_batch(proc, mers):
    if not mers:
        return []

    proc.stdin.write("\n".join(mers) + "\n")
    proc.stdin.flush()

    counts = []

    for _ in mers:
        line = proc.stdout.readline()

        if not line:
            raise RuntimeError(
                "Jellyfish stopped unexpectedly during querying"
            )

        counts.append(int(line.strip()))

    return counts


def main():
    ROOT.mkdir(parents=True, exist_ok=True)

    if not JF.exists():
        raise FileNotFoundError(JF)

    proc = subprocess.Popen(
        ["jellyfish", "query", "-L", "-i", str(JF)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    try:
        with OUTPUT.open("w", newline="") as out:
            writer = csv.writer(out, delimiter="\t")

            writer.writerow([
                "chr",
                "start",
                "end",
                "valid_24mers",
                "unique_24mers",
                "unique_fraction",
            ])

            for chrom, seq in read_fasta(GENOME):
                if chrom not in NUCLEAR:
                    continue

                print(
                    f"Processing chromosome {chrom}",
                    flush=True
                )

                n_windows = (len(seq) + WINDOW - 1) // WINDOW

                valid = [0] * n_windows
                unique = [0] * n_windows

                positions = []
                mers = []

                def flush_batch():
                    if not mers:
                        return

                    counts = query_batch(proc, mers)

                    for pos, count in zip(positions, counts):

                        # Match historical siRNA midpoint convention.
                        midpoint = pos + K // 2
                        window = midpoint // WINDOW

                        valid[window] += 1

                        if count == 1:
                            unique[window] += 1

                    positions.clear()
                    mers.clear()

                for pos in range(len(seq) - K + 1):
                    mer = seq[pos:pos + K]

                    if any(base not in "ACGT" for base in mer):
                        continue

                    positions.append(pos)
                    mers.append(mer)

                    if len(mers) >= BATCH:
                        flush_batch()

                flush_batch()

                for i in range(n_windows):
                    start = i * WINDOW
                    end = min(start + WINDOW, len(seq))

                    fraction = (
                        unique[i] / valid[i]
                        if valid[i] > 0
                        else float("nan")
                    )

                    writer.writerow([
                        chrom,
                        start,
                        end,
                        valid[i],
                        unique[i],
                        fraction,
                    ])

        print("\nCompleted successfully.")
        print("Output:", OUTPUT, flush=True)

    finally:
        if proc.poll() is None:
            proc.stdin.close()
            proc.terminate()
            proc.wait()


if __name__ == "__main__":
    main()
