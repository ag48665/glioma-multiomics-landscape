from pathlib import Path
import pandas as pd

clinical_fields = pd.DataFrame({
    "field": [
        "patient_id",
        "project_id",
        "age_at_diagnosis",
        "gender",
        "vital_status",
        "days_to_death",
        "days_to_last_follow_up"
    ],
    "why_needed": [
        "unique patient identifier",
        "GBM or LGG cohort",
        "clinical annotation for heatmap and Cox model",
        "clinical annotation",
        "survival status",
        "overall survival time if patient died",
        "follow-up time if patient is alive"
    ]
})

Path("results/tables").mkdir(parents=True, exist_ok=True)

clinical_fields.to_csv(
    "results/tables/clinical_fields.tsv",
    sep="\t",
    index=False
)