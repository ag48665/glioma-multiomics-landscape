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

gbm["patient_id"] = gbm["Tumor_Sample_Barcode"].str[:12]
lgg["patient_id"] = lgg["Tumor_Sample_Barcode"].str[:12]

gbm_counts = gbm.groupby("patient_id").size().reset_index(name="mutation_count")
lgg_counts = lgg.groupby("patient_id").size().reset_index(name="mutation_count")

gbm_counts["tumor"] = "GBM"
lgg_counts["tumor"] = "LGG"

df = pd.concat([gbm_counts, lgg_counts], ignore_index=True)
df = df.sort_values("mutation_count", ascending=False).reset_index(drop=True)

Path("figures").mkdir(exist_ok=True)
Path("results/tables").mkdir(parents=True, exist_ok=True)

df.to_csv(
    "results/tables/waterfall_mutation_burden.tsv",
    sep="\t",
    index=False
)

colors = df["tumor"].map({
    "GBM": "red",
    "LGG": "blue"
})

plt.figure(figsize=(16, 6))

plt.bar(
    range(len(df)),
    df["mutation_count"],
    color=colors
)

plt.yscale("log")
plt.xlabel("Patients sorted by mutation burden")
plt.ylabel("Number of mutations per patient (log scale)")
plt.title("Waterfall plot: mutation burden across GBM and LGG patients")

plt.legend(
    handles=[
        plt.Rectangle((0,0),1,1,color="red",label="GBM"),
        plt.Rectangle((0,0),1,1,color="blue",label="LGG")
    ]
)

plt.tight_layout()
plt.savefig(
    "figures/waterfall_mutation_burden.png",
    dpi=300
)

print("Waterfall mutation burden completed")