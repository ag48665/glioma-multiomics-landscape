import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

gbm = pd.read_csv(
    "results/tables/tcga_gbm_mutations.tsv",
    sep="\t",
    low_memory=False
)

lgg = pd.read_csv(
    "results/tables/tcga_lgg_mutations.tsv",
    sep="\t",
    low_memory=False
)

genes = ["IDH1", "TP53", "ATRX", "EGFR", "PTEN", "NF1", "CIC", "FUBP1"]

gbm_counts = gbm["Hugo_Symbol"].value_counts()
lgg_counts = lgg["Hugo_Symbol"].value_counts()

df = pd.DataFrame({
    "gene": genes,
    "GBM": [gbm_counts.get(g, 0) for g in genes],
    "LGG": [lgg_counts.get(g, 0) for g in genes]
})

Path("results/tables").mkdir(parents=True, exist_ok=True)
Path("figures").mkdir(parents=True, exist_ok=True)

df.to_csv(
    "results/tables/mutation_comparison_gbm_lgg.tsv",
    sep="\t",
    index=False
)

ax = df.plot(
    x="gene",
    y=["GBM", "LGG"],
    kind="bar",
    figsize=(10, 6)
)

ax.set_xlabel("Gene")
ax.set_ylabel("Mutation count")
ax.set_title("Driver gene mutation counts: GBM vs LGG")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("figures/mutation_comparison_gbm_lgg.png", dpi=200)