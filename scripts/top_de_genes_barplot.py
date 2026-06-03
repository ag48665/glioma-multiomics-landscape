import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/tables/top20_de_genes.tsv",
    sep="\t"
)

gbm = (
    df[df["log2FoldChange"] > 0]
    .sort_values("log2FoldChange", ascending=False)
    .head(10)
)

lgg = (
    df[df["log2FoldChange"] < 0]
    .sort_values("log2FoldChange")
    .head(10)
)

plot_df = pd.concat([lgg, gbm])

plt.figure(figsize=(10,8))

plt.barh(
    plot_df["gene"],
    plot_df["log2FoldChange"]
)

plt.axvline(0, color="black")

plt.xlabel("log2 Fold Change")
plt.ylabel("Gene")
plt.title("Top differentially expressed genes: GBM vs LGG")

plt.tight_layout()

plt.savefig(
    "figures/top_de_genes_barplot.png",
    dpi=300
)

print("Top DE genes plot completed")