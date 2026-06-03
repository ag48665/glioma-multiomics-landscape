library(TCGAbiolinks)

query_lgg <- GDCquery(
  project = "TCGA-LGG",
  data.category = "Simple Nucleotide Variation",
  data.type = "Masked Somatic Mutation",
  workflow.type = "Aliquot Ensemble Somatic Variant Merging and Masking"
)

GDCdownload(query_lgg)

maf_lgg <- GDCprepare(query_lgg)

dir.create(
  "results/tables",
  recursive = TRUE,
  showWarnings = FALSE
)

write.table(
  maf_lgg,
  "results/tables/tcga_lgg_mutations.tsv",
  sep = "\t",
  row.names = FALSE,
  quote = FALSE
)

print("LGG mutation download completed")