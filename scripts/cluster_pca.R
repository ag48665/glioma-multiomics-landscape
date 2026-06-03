library(SummarizedExperiment)

exp <- readRDS(
  "results/expression/tcga_gbm_expression.rds"
)

mat <- assay(exp, "unstranded")

vars <- apply(mat, 1, var)

top_genes <- names(
  sort(vars, decreasing = TRUE)
)[1:500]

mat_top <- mat[top_genes, ]

pca <- prcomp(
  t(log2(mat_top + 1)),
  scale. = TRUE
)

clusters <- kmeans(
  pca$x[,1:2],
  centers = 2,
  nstart = 25
)

write.table(
  data.frame(
    sample = rownames(pca$x),
    cluster = clusters$cluster
  ),
  "results/pca/pca_clusters.tsv",
  sep = "\t",
  row.names = FALSE,
  quote = FALSE
)

png(
  "figures/pca_clusters.png",
  width = 1000,
  height = 800
)

plot(
  pca$x[,1],
  pca$x[,2],
  col = clusters$cluster,
  pch = 19,
  xlab = "PC1",
  ylab = "PC2",
  main = "TCGA-GBM PCA clusters"
)

dev.off()