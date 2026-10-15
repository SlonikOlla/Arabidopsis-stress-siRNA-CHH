#!/usr/bin/env python3
import sys
import gzip
from pathlib import Path

def process(input_file, output_file):
    current_id = None
    group = []
    n_reads = 0
    n_alignments = 0

    with open(input_file) as source, gzip.open(output_file, "wt") as out:

        def write_group():
            nonlocal n_reads, n_alignments
            if not group:
                return

            k = len(group)
            weight = 1.0 / k

            for fields in group:
                strand = fields[1]
                chrom = fields[2]
                start = int(fields[3])
                end = start + len(fields[4])

                out.write(
                    f"{chrom}\t{start}\t{end}\t"
                    f"{weight:.12g}\t{strand}\n"
                )

            n_reads += 1
            n_alignments += k

        for line in source:
            fields = line.rstrip("\n").split("\t")
            rid = fields[0]

            if current_id is not None and rid != current_id:
                write_group()
                group = []

            current_id = rid
            group.append(fields)

        write_group()

    print(
        Path(input_file).name,
        "reads=", n_reads,
        "alignments=", n_alignments,
        "weight_sum=", n_reads
    )

if __name__ == "__main__":
    process(sys.argv[1], sys.argv[2])
