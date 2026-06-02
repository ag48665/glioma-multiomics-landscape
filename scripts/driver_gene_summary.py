import pandas as pd

maf = pd.read_csv(
    "results/tables/tcga_gbm_mutations.tsv",
    sep="\t",
    low_memory=False
)

driver_genes = [
    "IDH1",
    "TP53",
    "ATRX",
    "EGFR",
    "PTEN",
    "NF1"
]

summary = (
    maf[maf["Hugo_Symbol"].isin(driver_genes)]
    .groupby("Hugo_Symbol")
    .size()
    .reset_index(name="mutation_count")
    .sort_values("mutation_count", ascending=False)
)

print(summary)

summary.to_csv(
    "results/tables/driver_gene_summary.tsv",
    sep="\t",
    index=False
)