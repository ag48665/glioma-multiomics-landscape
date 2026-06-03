library(SummarizedExperiment)
library(pheatmap)

expr <- readRDS("results/expression/tcga_gbm_expression.rds")

counts <- assay(expr)

samples <- colnames(counts)

groups <- rep("GBM", length(samples))

res <- read.delim(
  "results/tables/gbm_vs_lgg_deseq2.tsv"
)

res <- res[order(res$padj), ]

top_genes <- head(
  res$gene,
  50
)

gene_names <- rownames(counts)

selected <- gene_names %in% top_genes

mat <- counts[selected, ]

mat <- log2(mat + 1)

mat <- t(scale(t(mat)))

annotation_col <- data.frame(
  Group = groups
)

rownames(annotation_col) <- colnames(mat)

png(
  "figures/heatmap_top50_genes.png",
  width = 1800,
  height = 1600,
  res = 200
)

pheatmap(
  mat,
  annotation_col = annotation_col,
  show_colnames = FALSE,
  fontsize_row = 6,
  main = "Top 50 differentially expressed genes (GBM)"
)

dev.off()

print("Heatmap completed")