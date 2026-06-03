import pandas as pd

df = pd.read_csv(
    "results/tables/gbm_vs_lgg_deseq2.tsv",
    sep="\t"
)

sig = df[df["padj"] < 0.05]

sig.to_csv(
    "results/tables/significant_genes.tsv",
    sep="\t",
    index=False
)

print("Significant genes:", len(sig))