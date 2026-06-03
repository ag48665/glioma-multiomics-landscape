import pandas as pd

clusters = pd.read_csv(
    "results/pca/pca_clusters.tsv",
    sep="\t"
)

surv = pd.read_csv(
    "results/tables/tcga_survival.tsv",
    sep="\t"
)

clusters["submitter_id"] = (
    clusters["sample"]
    .str.slice(0, 12)
)

merged = clusters.merge(
    surv,
    on="submitter_id",
    how="inner"
)

print(merged.shape)

print(
    merged["cluster"]
    .value_counts()
)