clinical <- read.table(
  "results/tables/tcga_clinical.tsv",
  sep = "\t",
  header = TRUE,
  quote = "",
  fill = TRUE,
  stringsAsFactors = FALSE
)

survival <- clinical[, c(
  "submitter_id",
  "project_id",
  "gender",
  "age_at_diagnosis",
  "vital_status",
  "days_to_death",
  "days_to_last_follow_up"
)]

survival$overall_survival_days <- ifelse(
  is.na(survival$days_to_death),
  survival$days_to_last_follow_up,
  survival$days_to_death
)

survival$event <- ifelse(
  survival$vital_status == "Dead",
  1,
  0
)

write.table(
  survival,
  "results/tables/tcga_survival.tsv",
  sep = "\t",
  row.names = FALSE,
  quote = FALSE
)