#!/usr/bin/env python3
"""Exploratory heat 24nt/CHH concordance vs TE overlap, site-density stratified.
Not a mappability- or sequencing-depth-matched null.
"""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2] if 'scripts' in Path(__file__).parts else Path.cwd()


def te_fraction(windows, path):
    # BED union and overlap via bedtools, avoiding assumptions about segmentation.
    import subprocess, tempfile
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        win = td / 'windows.bed'
        ann = td / 'te.bed'
        out = td / 'overlap.tsv'
        windows[['chr','start','end']].to_csv(win, sep='\t', header=False, index=False)
        with open(ann,'w') as f:
            p = subprocess.run(['bedtools','sort','-i',str(path)], capture_output=True, text=True, check=True)
            q = subprocess.run(['bedtools','merge','-i','-'], input=p.stdout, capture_output=True, text=True, check=True)
            f.write(q.stdout)
        with open(out,'w') as f:
            subprocess.run(['bedtools','intersect','-a',str(win),'-b',str(ann),'-wao'], stdout=f, check=True)
        # -wao emits one row per window since b is disjoint, except windows spanning multiple TEs.
        overlap = pd.read_csv(out,sep='\t',header=None,usecols=[0,1,2,6],names=['chr','start','end','bp'],dtype={'chr':str})
        overlap['bp'] = pd.to_numeric(overlap['bp'],errors='coerce').fillna(0)
        summed = overlap.groupby(['chr','start','end'],sort=False)['bp'].sum().reset_index()
        d = windows[['chr','start','end']].merge(summed,on=['chr','start','end'],how='left',validate='one_to_one')
        return d.bp.fillna(0).to_numpy() / (windows.end-windows.start).to_numpy()


def quantile_strata(values, bins):
    # Ranks resolve tied zeros deterministically and ensure similar-sized bins.
    ranks = pd.Series(values).rank(method='first',pct=True).to_numpy()
    return np.minimum((ranks*bins).astype(int),bins-1)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',type=Path,default=Path.cwd())
    ap.add_argument('--permutations',type=int,default=999)
    ap.add_argument('--seed',type=int,default=20261014)
    ap.add_argument('--bins',type=int,default=4)
    ap.add_argument('--thresholds',type=int,nargs='+',default=[25,50,75,100])
    args=ap.parse_args()
    root=args.root
    results=root/'heat_consensus/results'
    s=pd.read_csv(results/'heat_24nt_500bp_matrix.tsv',sep='\t',dtype={'chr':str})
    m=pd.read_csv(results/'heat_CHH_500bp_matrix.tsv',sep='\t',dtype={'chr':str})
    s=s[['chr','start','end','CTRL1','CTRL2','CTRL3','HEAT1','HEAT2','HEAT3','CTRLmean','delta24_CPM']]
    m=m[['chr','start','end','C1','C2','C3','H6_1','H6_2','H6_3','H12_1','H12_2','H12_3','H24_1','H24_2','H24_3','CTRLmean','deltaCHH_6h','deltaCHH_12h','deltaCHH_24h']]
    d=s.merge(m,on=['chr','start','end'],suffixes=('_sRNA','_CHH'),validate='one_to_one')
    print('Joint windows:',len(d),flush=True)
    d['TE_fraction']=te_fraction(d,root/'annotation/TAIR10_TEs_with_family_superfamily.bed')
    d['TE_overlap']=d.TE_fraction.gt(0)
    print('TE-overlapping windows:',int(d.TE_overlap.sum()),flush=True)
    countcols=[]
    for gsm in range(4150340,4150352):
        files=list((root/'heat_consensus/methylation/CHH500').glob(f'GSM{gsm}_*_CHH_500bp.tsv'))
        if len(files)!=1: raise RuntimeError(f'Expected one file for GSM{gsm}, found {files}')
        c=pd.read_csv(files[0],sep='\t',usecols=['chr','start','end','nCHH'],dtype={'chr':str})
        col=f'n_{gsm}'
        c=c.rename(columns={'nCHH':col})
        d=d.merge(c,on=['chr','start','end'],how='left',validate='one_to_one')
        countcols.append(col)

    mp = pd.read_csv(
        root/'results/validation_20261014/mappability/'
             'TAIR10_24mer_500bp_midpoint_mappability.tsv',
        sep='\t', dtype={'chr':str}
    )
    mp = mp[['chr','start','end','valid_24mers','unique_fraction']]
    d = d.merge(mp, on=['chr','start','end'],
                how='left', validate='one_to_one')
    print('Mappability available:',
          int(np.isfinite(d.unique_fraction).sum()), flush=True)

    outdir=root/'results/validation_20261014/TE_CHH_mappability'
    outdir.mkdir(parents=True,exist_ok=True)
    rng=np.random.default_rng(args.seed)
    rows=[]
    # Null: permute signed CHH changes within joint baseline/CHH-site strata,
    # leaving siRNA changes and TE labels fixed. This tests local concordance
    # conditional on these covariates; it is NOT a mappability-matched TE null.
    for t,idx in [('6h',[0,1,2,3,4,5]),('12h',[0,1,2,6,7,8]),('24h',[0,1,2,9,10,11])]:
        meth=f'deltaCHH_{t}'
        for threshold in args.thresholds:
            sub=d.loc[(d[[countcols[i] for i in idx]].ge(threshold).all(axis=1)) &
                      np.isfinite(d[meth]) & np.isfinite(d['delta24_CPM']) &
                      np.isfinite(d['CTRLmean_CHH']) & np.isfinite(d['CTRLmean_sRNA']) &
                      np.isfinite(d['unique_fraction'])].copy()
            if sub.empty: continue
            # Equal-size bins for each covariate; discard strata with <2 windows.
            cov=[np.log1p(sub.CTRLmean_sRNA.to_numpy().clip(min=0)),
                 sub.CTRLmean_CHH.to_numpy(),
                 sub[[countcols[i] for i in idx]].min(axis=1).to_numpy(),
                 sub.unique_fraction.to_numpy()]
            codes=[quantile_strata(v,args.bins) for v in cov]
            group=(codes[0]*args.bins**3 +
                   codes[1]*args.bins**2 +
                   codes[2]*args.bins +
                   codes[3])
            groups=[np.flatnonzero(group==g) for g in np.unique(group)]
            groups=[g for g in groups if len(g)>=2]
            valid=np.zeros(len(sub),bool)
            for g in groups: valid[g]=True
            sub=sub.iloc[np.flatnonzero(valid)].copy()
            old_to_new=np.full(len(valid),-1,dtype=int)
            old_to_new[np.flatnonzero(valid)]=np.arange(valid.sum())
            groups=[old_to_new[g] for g in groups]
            x=sub.delta24_CPM.to_numpy()
            y=sub[meth].to_numpy()
            te=sub.TE_overlap.to_numpy()
            # Concordance sign score, no effect-size selection or thresholding.
            score=lambda yy: np.sign(x)*np.sign(yy)
            obs=score(y)
            # TE vs non-TE difference in mean directional concordance.
            if not te.any() or te.all(): continue
            observed=obs[te].mean()-obs[~te].mean()
            null=np.empty(args.permutations)
            for k in range(args.permutations):
                yp=y.copy()
                for g in groups: yp[g]=y[rng.permutation(g)]
                z=score(yp)
                null[k]=z[te].mean()-z[~te].mean()
            # Two-sided empirical p centered on null expectation.
            p=(1+np.count_nonzero(np.abs(null-null.mean())>=abs(observed-null.mean())))/(args.permutations+1)
            rows.append({'time':t,'min_sites_each_replicate':threshold,'windows':len(sub),
                         'TE_windows':int(te.sum()),'nonTE_windows':int((~te).sum()),
                         'TE_concordance':float(obs[te].mean()),
                         'nonTE_concordance':float(obs[~te].mean()),
                         'observed_TE_minus_nonTE':float(observed),
                         'null_mean':float(null.mean()),
                         'null_sd':float(null.std(ddof=1)),
                         'empirical_p_two_sided':float(p),
                         'permutations':args.permutations,'bins_per_covariate':args.bins})
            print(f'{t} threshold={threshold}: N={len(sub):,} TE={te.sum():,} effect={observed:+.5f} null={null.mean():+.5f} p={p:.4g}',flush=True)
    res=pd.DataFrame(rows)
    if not res.empty:
        # BH across all tested time x threshold combinations, for exploratory reporting.
        p=res.empirical_p_two_sided.to_numpy()
        order=np.argsort(p)
        q=np.empty(len(p))
        q[order]=np.minimum.accumulate((p[order]*len(p)/np.arange(1,len(p)+1))[::-1])[::-1].clip(max=1)
        res['BH_FDR']=q
    path=outdir/'TE_CHH_concordance_stratified_null.tsv'
    res.to_csv(path,sep='\t',index=False)
    print('Saved:',path)
    print('LIMITATIONS: this is a stratified sign-concordance null, not read-depth matching, full TE/non-TE matching, or biological replication of paired layers.')

if __name__=='__main__': main()
