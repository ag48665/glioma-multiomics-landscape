import pandas as pd

clusters = pd.read_csv(
    "results/pca/pca_clusters.tsv",
    sep="\t"
)

clusters["submitter_id"] = (
    clusters["sample"]
    .str[:12]
)

idh = pd.read_csv(
    "results/tables/idh1_status.tsv",
    sep="\t"
)

merged = clusters.merge(
    idh,
    on="submitter_id"
)

print(
    pd.crosstab(
        merged["cluster"],
        merged["IDH1_status"]
    )
)