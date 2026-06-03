library(SummarizedExperiment)

exp <- readRDS("results/expression/tcga_lgg_expression.rds")

mat <- assay(exp, "unstranded")

cat("Genes:", nrow(mat), "\n")
cat("Samples:", ncol(mat), "\n")

vars <- apply(mat, 1, var)

top_genes <- names(sort(vars, decreasing = TRUE))[1:500]

mat_top <- mat[top_genes, ]

pca <- prcomp(
  t(log2(mat_top + 1)),
  scale. = TRUE
)

dir.create("results/pca", recursive = TRUE, showWarnings = FALSE)

write.table(
  pca$x,
  "results/pca/pca_lgg_coordinates.tsv",
  sep = "\t",
  quote = FALSE
)

png(
  "figures/pca_lgg_expression.png",
  width = 1000,
  height = 800
)

plot(
  pca$x[, 1],
  pca$x[, 2],
  pch = 19,
  xlab = "PC1",
  ylab = "PC2",
  main = "PCA of TCGA-LGG RNA-seq expression"
)

dev.off()

print("LGG PCA completed")