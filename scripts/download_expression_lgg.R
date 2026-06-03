library(TCGAbiolinks)

query <- GDCquery(
  project = "TCGA-LGG",
  data.category = "Transcriptome Profiling",
  data.type = "Gene Expression Quantification",
  workflow.type = "STAR - Counts"
)

GDCdownload(query)

exp <- GDCprepare(query)

dir.create("results/expression", recursive = TRUE, showWarnings = FALSE)

saveRDS(
  exp,
  file = "results/expression/tcga_lgg_expression.rds"
)

print("LGG RNA-seq download completed")