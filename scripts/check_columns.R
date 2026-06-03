surv <- read.delim(
  "results/tables/tcga_survival.tsv"
)

idh1 <- read.delim(
  "results/tables/idh1_status.tsv"
)

cat("\nSURVIVAL:\n")
print(colnames(surv))

cat("\nIDH1:\n")
print(colnames(idh1))