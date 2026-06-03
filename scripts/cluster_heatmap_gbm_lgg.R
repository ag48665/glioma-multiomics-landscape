library(SummarizedExperiment)
library(pheatmap)

gbm <- readRDS("results/expression/tcga_gbm_expression.rds")
lgg <- readRDS("results/expression/tcga_lgg_expression.rds")

gbm_mat <- assay(gbm)
lgg_mat <- assay(lgg)

common_genes <- intersect(
  rownames(gbm_mat),
  rownames(lgg_mat)
)

gbm_mat <- gbm_mat[common_genes, ]
lgg_mat <- lgg_mat[common_genes, ]

combined <- cbind(gbm_mat, lgg_mat)

vars <- apply(combined, 1, var)

top_genes <- names(
  sort(vars, decreasing = TRUE)
)[1:100]

mat <- combined[top_genes, ]

mat <- log2(mat + 1)

mat <- t(scale(t(mat)))

annotation_col <- data.frame(
  Tumor = c(
    rep("GBM", ncol(gbm_mat)),
    rep("LGG", ncol(lgg_mat))
  )
)

rownames(annotation_col) <- colnames(mat)

png(
  "figures/cluster_heatmap_gbm_lgg.png",
  width = 2200,
  height = 1800,
  res = 220
)

pheatmap(
  mat,
  annotation_col = annotation_col,
  show_colnames = FALSE,
  show_rownames = FALSE,
  clustering_method = "complete",
  main = "Hierarchical clustering: GBM vs LGG"
)

dev.off()

print("GBM-LGG clustering heatmap completed")