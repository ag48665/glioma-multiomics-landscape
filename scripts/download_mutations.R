library(TCGAbiolinks)

query_gbm <- GDCquery(
  project = "TCGA-GBM",
  data.category = "Simple Nucleotide Variation",
  data.type = "Masked Somatic Mutation",
  workflow.type = "Aliquot Ensemble Somatic Variant Merging and Masking"
)

GDCdownload(query_gbm)

maf_gbm <- GDCprepare(query_gbm)

dir.create(
  "results/tables",
  recursive = TRUE,
  showWarnings = FALSE
)

write.table(
  maf_gbm,
  "results/tables/tcga_gbm_mutations.tsv",
  sep = "\t",
  row.names = FALSE,
  quote = FALSE
)