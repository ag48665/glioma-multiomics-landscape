library(SummarizedExperiment)

exp <- readRDS(
  "results/expression/tcga_gbm_expression.rds"
)

mat <- assay(exp, "unstranded")

vars <- apply(mat, 1, var)

top_genes <- names(
  sort(vars, decreasing = TRUE)
)[1:50]

heat <- log2(
  mat[top_genes, ] + 1
)

png(
  "figures/expression_heatmap.png",
  width = 1200,
  height = 1000
)

heatmap(
  heat,
  Colv = NA,
  scale = "row",
  main = "TCGA-GBM expression heatmap (top 50 variable genes)"
)

dev.off()

print("Expression heatmap completed")