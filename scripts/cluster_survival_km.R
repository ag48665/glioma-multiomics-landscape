library(survival)

clusters <- read.table(
  "results/pca/pca_clusters.tsv",
  sep="\t",
  header=TRUE
)

surv <- read.table(
  "results/tables/tcga_survival.tsv",
  sep="\t",
  header=TRUE
)

clusters$submitter_id <- substr(
  clusters$sample,
  1,
  12
)

merged <- merge(
  clusters,
  surv,
  by="submitter_id"
)

fit <- survfit(
  Surv(overall_survival_days, event) ~ cluster,
  data=merged
)

png(
  "figures/pca_cluster_survival.png",
  width=1000,
  height=800
)

plot(
  fit,
  col=c("red","blue"),
  lwd=3,
  xlab="Days",
  ylab="Survival probability",
  main="Kaplan-Meier: PCA clusters"
)

legend(
  "topright",
  legend=c("Cluster 1","Cluster 2"),
  col=c("red","blue"),
  lwd=3
)

dev.off()