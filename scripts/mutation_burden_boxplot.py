import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

gbm["patient"] = gbm["Tumor_Sample_Barcode"].str[:12]
lgg["patient"] = lgg["Tumor_Sample_Barcode"].str[:12]

gbm_counts = gbm.groupby("patient").size()
lgg_counts = lgg.groupby("patient").size()

plt.figure(figsize=(8,6))

plt.boxplot(
    [gbm_counts, lgg_counts],
    tick_labels=["GBM", "LGG"]
)

plt.yscale("log")

plt.ylabel("Mutations per patient (log scale)")
plt.title("Mutation burden: GBM vs LGG")

plt.tight_layout()
plt.savefig(
    "figures/mutation_burden_boxplot.png",
    dpi=300
)

print("GBM mean:", gbm_counts.mean())
print("LGG mean:", lgg_counts.mean())

print("GBM median:", gbm_counts.median())
print("LGG median:", lgg_counts.median())