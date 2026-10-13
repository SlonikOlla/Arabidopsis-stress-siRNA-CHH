BEGIN {
    OFS="\t"
}

$4 == CONTEXT {
    chr=$1
    bin=int($2/W)*W

    key=chr SUBSEP bin

    n[key]++
    m[key]+=$5
    u[key]+=$6
}

END {
    for(k in n) {
        split(k,a,SUBSEP)

        total=m[k]+u[k]
        wm=(total>0 ? m[k]/total : "NA")

        print a[1],a[2],a[2]+W,n[k],m[k],u[k],total,wm
    }
}
