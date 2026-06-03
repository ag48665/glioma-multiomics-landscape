library(TCGAbiolinks)

query <- GDCquery(
  project = "TCGA-GBM",
  data.category = "Transcriptome Profiling",
  data.type = "Gene Expression Quantification",
  workflow.type = "STAR - Counts"
)

GDCdownload(query)

exp <- GDCprepare(query)

dir.create(
  "results/expression",
  recursive = TRUE,
  showWarnings = FALSE
)

saveRDS(
  exp,
  file = "results/expression/tcga_gbm_expression.rds"
)

print("RNA-seq download completed")