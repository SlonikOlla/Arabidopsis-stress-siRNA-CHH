#!/usr/bin/env python3
"""Single-entry workflow: preflight retained heat validation scripts, then execute on request."""
import argparse, importlib.util, shutil, subprocess, sys
from pathlib import Path
STAGES = [
 ("site-counts","build_heat_site_counts.py",["heat_consensus/methylation/bedGraph","heat_consensus/methylation/context"],[]),
 ("mappability","build_24mer_mappability.py",["genome/TAIR10.fa","results/validation_20261014/mappability/TAIR10_24mer_canonical.jf"],["jellyfish"]),
 ("siRNA-500bp","verify_heat_500bp.py",["heat_consensus/results/heat_24nt_500bp_matrix.tsv","results/validation_20261014/SRR25485472_fractional.bed.gz"],[]),
 ("siRNA-100bp","verify_heat_100bp.py",["heat_consensus/results/heat_24nt_100bp_matrix.tsv","results/validation_20261014/SRR25485472_fractional.bed.gz"],[]),
 ("heat-hierarchy","heat_common_window_context_hierarchy.py",["heat_consensus/results/heat_joint_500bp.tsv","heat_consensus/results/heat_CG_500bp_matrix.tsv","heat_consensus/results/heat_CHG_500bp_matrix.tsv","heat_consensus/results/heat_CHH_500bp_matrix.tsv","results/validation_20261014/site_counts","heat_consensus/methylation/CHH500"],[]),
 ("TE-matched","heat_TE_CHH_matched_validation.py",["heat_consensus/results/heat_24nt_500bp_matrix.tsv","heat_consensus/results/heat_CHH_500bp_matrix.tsv","results/validation_20261014/site_counts"],["bedtools"]),
 ("TE-mappability","heat_TE_CHH_mappability_validation.py",["heat_consensus/results/heat_24nt_500bp_matrix.tsv","heat_consensus/results/heat_CHH_500bp_matrix.tsv","results/validation_20261014/site_counts","results/validation_20261014/mappability/TAIR10_24mer_500bp_midpoint_mappability.tsv"],["bedtools"]),
]
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--root",type=Path,default=Path.cwd())
 p.add_argument("--stage",choices=["all"]+[s[0] for s in STAGES],default="all")
 p.add_argument("--execute",action="store_true")
 a=p.parse_args(); root=a.root.resolve()
 stages=[s for s in STAGES if a.stage in ("all",s[0])]
 blocked=[]
 for name,script,inputs,tools in stages:
  missing=[i for i in inputs if not (root/i).exists()]
  if not (root/"scripts/validation"/script).exists(): missing.append("scripts/validation/"+script)
  missing += [t+" (executable)" for t in tools if not shutil.which(t)]
  missing += [m+" (Python)" for m in ("numpy","pandas") if importlib.util.find_spec(m) is None]
  print(name+": "+("BLOCKED" if missing else "READY"))
  for item in missing: print("  missing:",item)
  if missing: blocked.append(name)
 if not a.execute:
  print("Preflight only. Use --execute to run available stages.")
  return 0
 if blocked:
  print("Refusing execution: "+", ".join(blocked),file=sys.stderr); return 2
 for name,script,_,_ in stages:
  cmd=[sys.executable,str(root/"scripts/validation"/script)]
  if name.startswith("TE-"): cmd+=["--root",str(root)]
  print("Running",name,flush=True)
  subprocess.run(cmd,cwd=root,check=True)
 return 0
if __name__=="__main__": raise SystemExit(main())
