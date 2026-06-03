import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
from pathlib import Path

genes = ["IDH1", "TP53", "ATRX", "EGFR", "PTEN", "NF1", "CIC", "FUBP1"]

gbm = pd.read_csv("results/tables/tcga_gbm_mutations.tsv", sep="\t", low_memory=False)
lgg = pd.read_csv("results/tables/tcga_lgg_mutations.tsv", sep="\t", low_memory=False)

maf = pd.concat([gbm, lgg])
maf["patient_id"] = maf["Tumor_Sample_Barcode"].str[:12]

maf = maf[maf["Hugo_Symbol"].isin(genes)]

patient_genes = (
    maf.groupby("patient_id")["Hugo_Symbol"]
    .apply(lambda x: sorted(set(x)))
)

edges = {}

for gene_list in patient_genes:
    for a, b in combinations(gene_list, 2):
        pair = tuple(sorted([a, b]))
        edges[pair] = edges.get(pair, 0) + 1

G = nx.Graph()

for gene in genes:
    G.add_node(gene)

for (a, b), weight in edges.items():
    if weight >= 10:
        G.add_edge(a, b, weight=weight)

Path("figures").mkdir(exist_ok=True)
Path("results/tables").mkdir(parents=True, exist_ok=True)

edge_table = pd.DataFrame([
    {"gene1": a, "gene2": b, "co_mutated_patients": w}
    for (a, b), w in edges.items()
])

edge_table.to_csv(
    "results/tables/comutation_edges.tsv",
    sep="\t",
    index=False
)

plt.figure(figsize=(10, 8))

pos = nx.spring_layout(G, seed=42)

weights = [G[u][v]["weight"] for u, v in G.edges()]
edge_widths = [w / 10 for w in weights]

nx.draw_networkx_nodes(
    G,
    pos,
    node_size=2500
)

nx.draw_networkx_edges(
    G,
    pos,
    width=edge_widths
)

nx.draw_networkx_labels(
    G,
    pos,
    font_size=12,
    font_weight="bold"
)

edge_labels = {
    (u, v): G[u][v]["weight"]
    for u, v in G.edges()
}

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=9
)

plt.title("Gene co-mutation network: GBM + LGG")
plt.axis("off")
plt.tight_layout()

plt.savefig(
    "figures/comutation_network.png",
    dpi=300
)

print("Co-mutation network completed")