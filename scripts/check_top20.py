import pandas as pd

df = pd.read_csv(
    "results/tables/top20_de_genes.tsv",
    sep="\t"
)

print(df.columns.tolist())
print(df.head(20))