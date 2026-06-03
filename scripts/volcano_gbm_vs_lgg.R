library(DESeq2)

gbm <- readRDS("results/expression/tcga_gbm_expression.rds")
lgg <- readRDS("results/expression/tcga_lgg_expression.rds")

expr_gbm <- assay(gbm, "unstranded")
expr_lgg <- assay(lgg, "unstranded")

common_genes <- intersect(rownames(expr_gbm), rownames(expr_lgg))

expr_gbm <- expr_gbm[common_genes, ]
expr_lgg <- expr_lgg[common_genes, ]

counts <- cbind(expr_gbm, expr_lgg)

condition <- factor(c(
  rep("GBM", ncol(expr_gbm)),
  rep("LGG", ncol(expr_lgg))
))

coldata <- data.frame(
  row.names = colnames(counts),
  condition = condition
)

dds <- DESeqDataSetFromMatrix(
  countData = round(counts),
  colData = coldata,
  design = ~ condition
)

dds <- DESeq(dds)

res <- results(dds, contrast = c("condition", "GBM", "LGG"))

res_df <- as.data.frame(res)
res_df$gene <- rownames(res_df)

res_df$significant <- ifelse(
  !is.na(res_df$padj) & res_df$padj < 0.05 & abs(res_df$log2FoldChange) > 1,
  "significant",
  "not_significant"
)

dir.create("figures", recursive = TRUE, showWarnings = FALSE)
dir.create("results/tables", recursive = TRUE, showWarnings = FALSE)

write.table(
  res_df,
  "results/tables/gbm_vs_lgg_deseq2.tsv",
  sep = "\t",
  quote = FALSE,
  row.names = FALSE
)

png(
  "figures/volcano_gbm_lgg.png",
  width = 1200,
  height = 1000
)

plot(
  res_df$log2FoldChange,
  -log10(res_df$pvalue),
  pch = 16,
  cex = 0.5,
  col = ifelse(res_df$significant == "significant", "red", "grey"),
  xlab = "log2 fold change (GBM vs LGG)",
  ylab = "-log10(p-value)",
  main = "Volcano plot: GBM vs LGG"
)

abline(v = c(-1, 1), lty = 2)
abline(h = -log10(0.05), lty = 2)

dev.off()

print("Volcano plot completed")