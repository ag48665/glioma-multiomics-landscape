import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

genes = ["IDH1", "TP53", "ATRX", "EGFR", "PTEN", "NF1", "CIC", "FUBP1"]

gbm = pd.read_csv("results/tables/tcga_gbm_mutations.tsv", sep="\t", low_memory=False)
lgg = pd.read_csv("results/tables/tcga_lgg_mutations.tsv", sep="\t", low_memory=False)

gbm["patient_id"] = gbm["Tumor_Sample_Barcode"].str.slice(0, 12)
lgg["patient_id"] = lgg["Tumor_Sample_Barcode"].str.slice(0, 12)

gbm = gbm[gbm["Hugo_Symbol"].isin(genes)]
lgg = lgg[lgg["Hugo_Symbol"].isin(genes)]

gbm_matrix = pd.crosstab(gbm["patient_id"], gbm["Hugo_Symbol"])
lgg_matrix = pd.crosstab(lgg["patient_id"], lgg["Hugo_Symbol"])

gbm_matrix = (gbm_matrix > 0).astype(int).reindex(columns=genes, fill_value=0)
lgg_matrix = (lgg_matrix > 0).astype(int).reindex(columns=genes, fill_value=0)

gbm_matrix["cohort"] = "GBM"
lgg_matrix["cohort"] = "LGG"

matrix = pd.concat([gbm_matrix, lgg_matrix])

matrix["mutation_count"] = matrix[genes].sum(axis=1)
matrix = matrix.sort_values(["cohort", "mutation_count"], ascending=[True, False])

cohorts = matrix["cohort"]
plot_matrix = matrix[genes].T

Path("figures").mkdir(exist_ok=True)
Path("results/tables").mkdir(parents=True, exist_ok=True)

plot_matrix.to_csv(
    "results/tables/oncoprint_matrix_gbm_lgg.tsv",
    sep="\t"
)

plt.figure(figsize=(16, 6))
plt.imshow(plot_matrix.values, aspect="auto", interpolation="nearest")

plt.yticks(range(len(genes)), genes)
plt.xticks([])

plt.xlabel("Patients")
plt.ylabel("Driver genes")
plt.title("Oncoprint: GBM vs LGG driver gene mutations")

boundary = sum(cohorts == "GBM")
plt.axvline(boundary - 0.5, linestyle="--")

plt.text(boundary / 2, -0.8, "GBM", ha="center")
plt.text(boundary + (len(cohorts) - boundary) / 2, -0.8, "LGG", ha="center")

plt.colorbar(label="Mutation status")
plt.tight_layout()
plt.savefig("figures/oncoprint_gbm_lgg.png", dpi=200)