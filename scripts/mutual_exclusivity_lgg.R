library(maftools)

lgg_maf <- read.maf(
  maf = "results/tables/tcga_lgg_mutations.tsv"
)

png(
  "figures/mutual_exclusivity_lgg.png",
  width = 1600,
  height = 1200,
  res = 200
)

somaticInteractions(
  maf = lgg_maf,
  top = 20,
  pvalue = c(0.05, 0.1)
)

dev.off()

print("LGG mutual exclusivity completed")