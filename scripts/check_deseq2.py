import pandas as pd

df = pd.read_csv(
    "results/tables/gbm_vs_lgg_deseq2.tsv",
    sep="\t"
)

print(df.columns.tolist())
print(df.head())