res <- read.table(
  "results/tables/gbm_vs_lgg_deseq2.tsv",
  sep = "\t",
  header = TRUE
)

res <- res[!is.na(res$padj), ]
res <- res[order(res$padj), ]

top20 <- head(
  res[, c("gene", "log2FoldChange", "padj")],
  20
)

print(top20)

write.table(
  top20,
  "results/tables/top20_de_genes.tsv",
  sep = "\t",
  row.names = FALSE,
  quote = FALSE
)

png(
  "figures/top20_de_genes.png",
  width = 1400,
  height = 900
)

barplot(
  top20$log2FoldChange,
  names.arg = top20$gene,
  las = 2,
  cex.names = 0.7,
  main = "Top differentially expressed genes: GBM vs LGG",
  ylab = "log2 fold change"
)

dev.off()

print("Top genes completed")