import pandas as pd

df = pd.read_csv(
    "results/tables/top20_de_genes.tsv",
    sep="\t"
)

genes = df["gene"].tolist()

print(genes[:10])