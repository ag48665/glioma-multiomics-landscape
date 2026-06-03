library(maftools)

maf <- read.maf(
  maf = "results/tables/tcga_gbm_mutations.tsv"
)

titv_res <- titv(maf = maf)

png(
  "figures/titv_gbm.png",
  width = 1600,
  height = 1200,
  res = 200
)

plotTiTv(
  res = titv_res
)

dev.off()

print("Ti/Tv GBM completed")