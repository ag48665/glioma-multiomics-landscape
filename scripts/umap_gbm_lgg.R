library(SummarizedExperiment)
library(umap)

gbm <- readRDS("results/expression/tcga_gbm_expression.rds")
lgg <- readRDS("results/expression/tcga_lgg_expression.rds")

gbm_mat <- assay(gbm, "unstranded")
lgg_mat <- assay(lgg, "unstranded")

common_genes <- intersect(rownames(gbm_mat), rownames(lgg_mat))

gbm_mat <- gbm_mat[common_genes, ]
lgg_mat <- lgg_mat[common_genes, ]

mat <- cbind(gbm_mat, lgg_mat)

vars <- apply(mat, 1, var)
top_genes <- names(sort(vars, decreasing = TRUE))[1:1000]

mat_top <- log2(mat[top_genes, ] + 1)

embedding <- umap(t(mat_top))

groups <- c(
  rep("GBM", ncol(gbm_mat)),
  rep("LGG", ncol(lgg_mat))
)

dir.create("results/umap", recursive = TRUE, showWarnings = FALSE)

out <- data.frame(
  sample = colnames(mat),
  group = groups,
  UMAP1 = embedding$layout[, 1],
  UMAP2 = embedding$layout[, 2]
)

write.table(
  out,
  "results/umap/umap_gbm_lgg.tsv",
  sep = "\t",
  row.names = FALSE,
  quote = FALSE
)

png(
  "figures/umap_gbm_lgg.png",
  width = 1000,
  height = 800
)

plot(
  out$UMAP1,
  out$UMAP2,
  col = ifelse(out$group == "GBM", "red", "blue"),
  pch = 19,
  xlab = "UMAP1",
  ylab = "UMAP2",
  main = "UMAP of TCGA-GBM and TCGA-LGG RNA-seq"
)

legend(
  "topright",
  legend = c("GBM", "LGG"),
  col = c("red", "blue"),
  pch = 19
)

dev.off()

print("UMAP completed")