import pandas as pd
import mygene

df = pd.read_csv(
    "results/tables/top20_de_genes.tsv",
    sep="\t"
)

genes = [
    x.split(".")[0]
    for x in df["gene"]
]

mg = mygene.MyGeneInfo()

res = mg.querymany(
    genes,
    scopes="ensembl.gene",
    fields="symbol",
    species="human"
)

mapping = {
    x["query"]: x.get("symbol", x["query"])
    for x in res
}

df["symbol"] = [
    mapping.get(x.split(".")[0], x)
    for x in df["gene"]
]

print(df[["gene","symbol","log2FoldChange"]])