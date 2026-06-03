import pandas as pd
import matplotlib.pyplot as plt

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

plt.figure(figsize=(10,6))

plt.hist(
    gbm_counts,
    bins=30,
    alpha=0.6,
    label="GBM"
)

plt.hist(
    lgg_counts,
    bins=30,
    alpha=0.6,
    label="LGG"
)

plt.xlabel("Number of mutations per patient")
plt.ylabel("Number of patients")
plt.title("Mutation burden distribution: GBM vs LGG")
plt.legend()

plt.tight_layout()
plt.savefig(
    "figures/mutation_burden_gbm_lgg.png",
    dpi=300
)

summary = pd.DataFrame({
    "GBM":[gbm_counts.mean(), gbm_counts.median(), gbm_counts.max()],
    "LGG":[lgg_counts.mean(), lgg_counts.median(), lgg_counts.max()]
}, index=["Mean","Median","Max"])

summary.to_csv(
    "results/tables/mutation_burden_summary.tsv",
    sep="\t"
)

print(summary)
print("Mutation burden completed")