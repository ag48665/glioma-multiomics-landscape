library(maftools)

lgg_maf <- read.maf(
  maf = "results/tables/tcga_lgg_mutations.tsv"
)

png(
  "figures/oncoplot_maftools_lgg.png",
  width = 1800,
  height = 1400,
  res = 200
)

oncoplot(
  maf = lgg_maf,
  top = 20,
  showTumorSampleBarcodes = FALSE,
  draw_titv = TRUE,
  titleText = "TCGA-LGG oncoplot"
)

dev.off()

print("LGG maftools oncoplot completed")