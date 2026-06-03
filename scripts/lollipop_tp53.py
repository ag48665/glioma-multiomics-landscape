import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

gene = "IDH1"

gbm = pd.read_csv("results/tables/tcga_gbm_mutations.tsv", sep="\t", low_memory=False)
lgg = pd.read_csv("results/tables/tcga_lgg_mutations.tsv", sep="\t", low_memory=False)

maf = pd.concat([gbm, lgg], ignore_index=True)

sub = maf[
    (maf["Hugo_Symbol"] == gene) &
    (maf["Protein_position"].notna())
].copy()

sub["protein_pos"] = (
    sub["Protein_position"]
    .astype(str)
    .str.extract(r"(\d+)")
    .astype(float)
)

counts = (
    sub["protein_pos"]
    .dropna()
    .astype(int)
    .value_counts()
    .sort_index()
)

Path("figures").mkdir(exist_ok=True)
Path("results/tables").mkdir(parents=True, exist_ok=True)

counts.to_csv(
    f"results/tables/lollipop_{gene}.tsv",
    sep="\t",
    header=["mutation_count"]
)

plt.figure(figsize=(14, 5))

plt.hlines(
    y=0,
    xmin=0,
    xmax=max(counts.index) + 20,
    linewidth=4
)

plt.vlines(
    counts.index,
    0,
    counts.values,
    linewidth=2
)

plt.scatter(
    counts.index,
    counts.values,
    s=counts.values * 25
)

plt.xlabel("Protein position")
plt.ylabel("Mutation count")
plt.title(f"Lollipop plot: {gene} mutations in TCGA gliomas")

plt.tight_layout()
plt.savefig(
    f"figures/lollipop_{gene}.png",
    dpi=300
)

print(counts.sort_values(ascending=False).head(10))
print("Lollipop completed")