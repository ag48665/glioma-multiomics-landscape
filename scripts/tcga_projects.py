from pathlib import Path
import pandas as pd

projects = pd.DataFrame({
    "project_id": ["TCGA-GBM", "TCGA-LGG"],
    "cancer_type": ["Glioblastoma", "Lower Grade Glioma"],
    "organ": ["Brain", "Brain"]
})

Path("results/tables").mkdir(parents=True, exist_ok=True)

projects.to_csv(
    "results/tables/tcga_projects.tsv",
    sep="\t",
    index=False
)