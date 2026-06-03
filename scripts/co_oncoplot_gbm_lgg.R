library(maftools)

gbm <- read.maf(
  maf = "results/tables/tcga_gbm_mutations.tsv"
)

lgg <- read.maf(
  maf = "results/tables/tcga_lgg_mutations.tsv"
)

png(
  "figures/co_oncoplot_gbm_lgg.png",
  width = 2200,
  height = 1600,
  res = 220
)

coOncoplot(
  m1 = gbm,
  m2 = lgg,
  m1Name = "GBM",
  m2Name = "LGG",
  genes = c(
    "IDH1",
    "TP53",
    "ATRX",
    "EGFR",
    "PTEN",
    "NF1",
    "CIC",
    "FUBP1"
  )
)

dev.off()

print("Co-oncoplot completed")