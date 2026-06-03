import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

gbm = pd.read_csv("results/tables/idh1_survival.tsv", sep="\t")
lgg = pd.read_csv("results/tables/idh1_lgg_survival.tsv", sep="\t")

df = pd.concat([gbm, lgg], ignore_index=True)

df["tumor_type"] = df["project_id"].replace({
    "TCGA-GBM": "GBM",
    "TCGA-LGG": "LGG"
})

df["survival_group"] = df["overall_survival_days"].apply(
    lambda x: "Long survival" if x >= 1000 else "Short survival"
)

labels = [
    "GBM", "LGG",
    "IDH1-mutant", "IDH1-wildtype",
    "Long survival", "Short survival"
]

label_id = {label: i for i, label in enumerate(labels)}
links = []

def add_links(source_col, target_col):
    counts = df.groupby([source_col, target_col]).size().reset_index(name="count")
    for _, row in counts.iterrows():
        links.append({
            "source": label_id[row[source_col]],
            "target": label_id[row[target_col]],
            "value": row["count"]
        })

add_links("tumor_type", "IDH1_status")
add_links("IDH1_status", "survival_group")

fig = go.Figure(data=[go.Sankey(
    node=dict(label=labels, pad=20, thickness=20),
    link=dict(
        source=[x["source"] for x in links],
        target=[x["target"] for x in links],
        value=[x["value"] for x in links]
    )
)])

fig.update_layout(
    title_text="Glioma Sankey: tumor type, IDH1 status and survival",
    font_size=14
)

Path("figures").mkdir(exist_ok=True)
fig.write_html("figures/sankey_glioma.html")

print("Sankey completed")