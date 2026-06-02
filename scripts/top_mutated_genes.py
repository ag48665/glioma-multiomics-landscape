import pandas as pd

maf = pd.read_csv(
    "results/tables/tcga_gbm_mutations.tsv",
    sep="\t",
    low_memory=False
)

gene_counts = (
    maf["Hugo_Symbol"]
    .value_counts()
    .head(20)
)

gene_counts.to_csv(
    "results/tables/top_mutated_genes.tsv",
    sep="\t",
    header=["mutation_count"]
)

print(gene_counts)