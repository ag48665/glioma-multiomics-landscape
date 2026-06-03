import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# wartości z Twoich analiz
categories = [
    "IDH1",
    "TP53",
    "ATRX",
    "EGFR",
    "Mutation burden",
    "Survival"
]

# przykładowe wartości (0-100)
GBM = [10, 35, 5, 90, 100, 20]
LGG = [95, 80, 75, 10, 45, 100]

N = len(categories)

angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
angles += angles[:1]

GBM += GBM[:1]
LGG += LGG[:1]

fig, ax = plt.subplots(
    figsize=(8,8),
    subplot_kw=dict(polar=True)
)

ax.plot(angles, GBM, linewidth=3, label="GBM")
ax.fill(angles, GBM, alpha=0.25)

ax.plot(angles, LGG, linewidth=3, label="LGG")
ax.fill(angles, LGG, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11)

plt.title(
    "GBM vs LGG molecular profile",
    fontsize=16,
    fontweight="bold"
)

plt.legend(loc="upper right")

plt.tight_layout()
plt.savefig(
    "figures/radar_gbm_lgg.png",
    dpi=300
)

print("Radar plot completed")