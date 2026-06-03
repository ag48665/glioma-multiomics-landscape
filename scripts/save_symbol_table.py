import pandas as pd
import mygene
import time

df = pd.read_csv(
    "results/tables/gbm_vs_lgg_deseq2.tsv",
    sep="\t"
)

df = df[
    (df["padj"] < 0.05) &
    (df["log2FoldChange"].abs() > 1)
].copy()

df["ensembl_clean"] = df["gene"].str.split(".").str[0]

genes = df["ensembl_clean"].dropna().unique().tolist()

mg = mygene.MyGeneInfo()

all_results = []

for i in range(0, len(genes), 500):
    batch = genes[i:i+500]
    print("Batch", i, "to", i + len(batch))

    res = mg.querymany(
        batch,
        scopes="ensembl.gene",
        fields="symbol",
        species="human",
        verbose=False
    )

    all_results.extend(res)
    time.sleep(1)

mapping = {
    x["query"]: x.get("symbol", "")
    for x in all_results
}

df["symbol"] = df["ensembl_clean"].map(mapping)

df = df[df["symbol"].notna() & (df["symbol"] != "")]

df.to_csv(
    "results/tables/significant_genes_symbols.tsv",
    sep="\t",
    index=False
)

print("Saved genes:", len(df))
print(df[["gene", "symbol", "log2FoldChange", "padj"]].head(20))