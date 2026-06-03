import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

genes = ["IDH1", "TP53", "ATRX", "EGFR", "PTEN", "NF1", "CIC", "FUBP1"]

gbm = pd.read_csv("results/tables/tcga_gbm_mutations.tsv", sep="\t", low_memory=False)
lgg = pd.read_csv("results/tables/tcga_lgg_mutations.tsv", sep="\t", low_memory=False)

de = pd.read_csv("results/tables/gbm_vs_lgg_deseq2.tsv", sep="\t")

gbm["patient"] = gbm["Tumor_Sample_Barcode"].str[:12]
lgg["patient"] = lgg["Tumor_Sample_Barcode"].str[:12]

gbm_patients = gbm["patient"].nunique()
lgg_patients = lgg["patient"].nunique()

rows = []

for gene in genes:
    gbm_freq = gbm.loc[gbm["Hugo_Symbol"] == gene, "patient"].nunique() / gbm_patients * 100
    lgg_freq = lgg.loc[lgg["Hugo_Symbol"] == gene, "patient"].nunique() / lgg_patients * 100

    rows.append({
        "gene": gene,
        "GBM_mutation_freq": gbm_freq,
        "LGG_mutation_freq": lgg_freq,
        "mutation_difference": gbm_freq - lgg_freq
    })

df = pd.DataFrame(rows)

Path("figures").mkdir(exist_ok=True)
Path("results/tables").mkdir(parents=True, exist_ok=True)

df.to_csv(
    "results/tables/bubble_mutation_expression.tsv",
    sep="\t",
    index=False
)

plt.figure(figsize=(10, 6))

sizes = (df["GBM_mutation_freq"] + df["LGG_mutation_freq"]) * 20 + 50

plt.scatter(
    df["GBM_mutation_freq"],
    df["LGG_mutation_freq"],
    s=sizes,
    alpha=0.6
)

for _, row in df.iterrows():
    plt.text(
        row["GBM_mutation_freq"] + 0.5,
        row["LGG_mutation_freq"] + 0.5,
        row["gene"],
        fontsize=11
    )

plt.xlabel("GBM mutation frequency (%)")
plt.ylabel("LGG mutation frequency (%)")
plt.title("Bubble plot: driver mutation frequency in GBM vs LGG")

plt.tight_layout()
plt.savefig("figures/bubble_mutation_frequency.png", dpi=300)

print(df)
print("Bubble plot completed")