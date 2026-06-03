library(maftools)

gbm_maf <- read.maf(
  maf = "results/tables/tcga_gbm_mutations.tsv"
)

png(
  "figures/oncoplot_maftools_gbm.png",
  width = 1800,
  height = 1400,
  res = 200
)

oncoplot(
  maf = gbm_maf,
  top = 20,
  showTumorSampleBarcodes = FALSE,
  draw_titv = TRUE,
  titleText = "TCGA-GBM oncoplot"
)

dev.off()

print("GBM maftools oncoplot completed")