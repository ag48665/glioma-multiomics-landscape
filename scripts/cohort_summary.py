from pathlib import Path
import yaml
import pandas as pd

with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

cohorts = config["cohorts"]

df = pd.DataFrame({
    "cohort": cohorts
})

Path("results/tables").mkdir(parents=True, exist_ok=True)

df.to_csv(
    "results/tables/cohort_summary.tsv",
    sep="\t",
    index=False
)