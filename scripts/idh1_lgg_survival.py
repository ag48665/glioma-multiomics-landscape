import pandas as pd

maf = pd.read_csv(
    "results/tables/tcga_lgg_mutations.tsv",
    sep="\t",
    low_memory=False
)

surv = pd.read_csv(
    "results/tables/tcga_survival.tsv",
    sep="\t"
)

maf["patient_id"] = maf["Tumor_Sample_Barcode"].str.slice(0, 12)

idh1_patients = set(
    maf.loc[
        maf["Hugo_Symbol"] == "IDH1",
        "patient_id"
    ]
)

surv_lgg = surv[
    surv["project_id"] == "TCGA-LGG"
].copy()

surv_lgg["IDH1_status"] = surv_lgg["submitter_id"].apply(
    lambda x:
        "IDH1-mutant"
        if x in idh1_patients
        else "IDH1-wildtype"
)

print(
    surv_lgg["IDH1_status"]
    .value_counts()
)

surv_lgg.to_csv(
    "results/tables/idh1_lgg_survival.tsv",
    sep="\t",
    index=False
)