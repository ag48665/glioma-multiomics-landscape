import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/tables/gbm_vs_lgg_deseq2.tsv",
    sep="\t"
)

df["minuslog10padj"] = -np.log10(df["padj"] + 1e-300)

plt.figure(figsize=(12,8))

up = df[
    (df["log2FoldChange"] > 1) &
    (df["padj"] < 0.05)
]

down = df[
    (df["log2FoldChange"] < -1) &
    (df["padj"] < 0.05)
]

ns = df[
    ~(
        ((df["log2FoldChange"] > 1) |
         (df["log2FoldChange"] < -1))
        &
        (df["padj"] < 0.05)
    )
]

plt.scatter(
    ns["log2FoldChange"],
    ns["minuslog10padj"],
    s=5,
    alpha=0.3
)

plt.scatter(
    up["log2FoldChange"],
    up["minuslog10padj"],
    s=10,
    label="GBM-upregulated"
)

plt.scatter(
    down["log2FoldChange"],
    down["minuslog10padj"],
    s=10,
    label="LGG-upregulated"
)

top = df.nsmallest(10, "padj")

for _, row in top.iterrows():
    plt.text(
        row["log2FoldChange"],
        row["minuslog10padj"],
        row["gene"],
        fontsize=8
    )

plt.axvline(1, linestyle="--")
plt.axvline(-1, linestyle="--")
plt.axhline(-np.log10(0.05), linestyle="--")

plt.xlabel("log2 Fold Change")
plt.ylabel("-log10 adjusted p-value")
plt.title("Volcano plot: GBM vs LGG differential expression")

plt.legend()

plt.tight_layout()

plt.savefig(
    "figures/volcano_gbm_lgg.png",
    dpi=300
)

print("Volcano plot completed")