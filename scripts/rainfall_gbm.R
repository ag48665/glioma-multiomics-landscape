library(maftools)

maf <- read.maf(
  maf = "results/tables/tcga_gbm_mutations.tsv"
)

png(
  "figures/rainfall_gbm.png",
  width = 1800,
  height = 1200
)

rainfallPlot(
  maf = maf,
  detectChangePoints = TRUE
)

dev.off()

print("Rainfall plot completed")