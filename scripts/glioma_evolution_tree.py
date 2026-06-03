import matplotlib.pyplot as plt
from pathlib import Path

Path("figures").mkdir(exist_ok=True)

fig, ax = plt.subplots(figsize=(12,8))
ax.axis("off")

nodes = {
    "Glioma": (0.5,0.9),

    "IDH1-mutant": (0.25,0.65),
    "EGFR/PTEN": (0.75,0.65),

    "TP53": (0.15,0.40),
    "ATRX": (0.35,0.40),

    "NF1": (0.65,0.40),
    "PTEN loss": (0.85,0.40),

    "LGG": (0.25,0.15),
    "GBM": (0.75,0.15)
}

for name,(x,y) in nodes.items():

    color="lightblue"

    if name=="LGG":
        color="lightgreen"

    if name=="GBM":
        color="salmon"

    ax.text(
        x,y,name,
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.4",
                  fc=color,
                  ec="black")
    )

edges = [

    ("Glioma","IDH1-mutant"),
    ("Glioma","EGFR/PTEN"),

    ("IDH1-mutant","TP53"),
    ("IDH1-mutant","ATRX"),

    ("EGFR/PTEN","NF1"),
    ("EGFR/PTEN","PTEN loss"),

    ("TP53","LGG"),
    ("ATRX","LGG"),

    ("NF1","GBM"),
    ("PTEN loss","GBM")
]

for a,b in edges:

    x1,y1 = nodes[a]
    x2,y2 = nodes[b]

    ax.annotate(
        "",
        xy=(x2,y2),
        xytext=(x1,y1),
        arrowprops=dict(
            arrowstyle="->",
            lw=2
        )
    )

plt.title(
    "Simplified molecular evolution of diffuse gliomas",
    fontsize=18,
    fontweight="bold"
)

plt.savefig(
    "figures/glioma_evolution_tree.png",
    dpi=300,
    bbox_inches="tight"
)

print("Evolution tree completed")