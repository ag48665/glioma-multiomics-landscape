import pandas as pd

maf = pd.read_csv(
    "results/tables/tcga_lgg_mutations.tsv",
    sep="\t",
    low_memory=False
)

top = (
    maf["Hugo_Symbol"]
    .value_counts()
    .head(20)
)

print(top)

top.to_csv(
    "results/tables/top_mutated_genes_lgg.tsv",
    sep="\t",
    header=["mutation_count"]
)