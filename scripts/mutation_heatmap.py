import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

maf = pd.read_csv(
    "results/tables/tcga_gbm_mutations.tsv",
    sep="\t",
    low_memory=False
)

driver_genes = ["TP53", "PTEN", "EGFR", "NF1", "ATRX", "IDH1"]

maf["patient_id"] = maf["Tumor_Sample_Barcode"].str.slice(0, 12)

driver_maf = maf[maf["Hugo_Symbol"].isin(driver_genes)]

matrix = (
    driver_maf
    .assign(mutated=1)
    .pivot_table(
        index="patient_id",
        columns="Hugo_Symbol",
        values="mutated",
        aggfunc="max",
        fill_value=0
    )
)

matrix = matrix.reindex(columns=driver_genes, fill_value=0)

matrix["mutation_count"] = matrix.sum(axis=1)
matrix = matrix.sort_values("mutation_count", ascending=False)
matrix = matrix.drop(columns="mutation_count")

Path("results/tables").mkdir(parents=True, exist_ok=True)
Path("figures").mkdir(parents=True, exist_ok=True)

matrix.to_csv(
    "results/tables/driver_gene_mutation_matrix.tsv",
    sep="\t"
)

plt.figure(figsize=(10, 8))
plt.imshow(matrix.values, aspect="auto", interpolation="nearest")
plt.xticks(range(len(matrix.columns)), matrix.columns, rotation=45, ha="right")
plt.yticks([])
plt.xlabel("Driver genes")
plt.ylabel("GBM patients")
plt.title("TCGA-GBM driver gene mutation heatmap")
plt.colorbar(label="Mutation status")
plt.tight_layout()
plt.savefig("figures/driver_gene_mutation_heatmap.png", dpi=200)