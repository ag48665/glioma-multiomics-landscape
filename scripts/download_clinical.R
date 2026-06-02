library(TCGAbiolinks)

gbm <- GDCquery_clinic(
  project = "TCGA-GBM",
  type = "clinical"
)

lgg <- GDCquery_clinic(
  project = "TCGA-LGG",
  type = "clinical"
)

gbm$project_id <- "TCGA-GBM"
lgg$project_id <- "TCGA-LGG"

common_cols <- intersect(colnames(gbm), colnames(lgg))

gbm <- gbm[, common_cols]
lgg <- lgg[, common_cols]

clinical <- rbind(gbm, lgg)

dir.create(
  "results/tables",
  recursive = TRUE,
  showWarnings = FALSE
)

write.table(
  clinical,
  "results/tables/tcga_clinical.tsv",
  sep = "\t",
  row.names = FALSE,
  quote = FALSE
)