BEGIN { OFS="\t" }

# First pass supplied externally gives number of alignments/read.
{
    id=$1
    strand=$2
    chr=$3
    start=$4
    seq=$5

    split(id,a,"_count_")
    count=a[2]+0

    end=start+length(seq)

    print chr,start,end,id,count,strand
}
