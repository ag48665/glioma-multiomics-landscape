library(SummarizedExperiment)
library(GenomicRanges)

gbm <- readRDS("results/expression/tcga_gbm_expression.rds")

res <- read.delim(
  "results/tables/gbm_vs_lgg_deseq2.tsv"
)

rr <- rowRanges(gbm)

annot <- data.frame(
  gene = rownames(gbm),
  chr = as.character(seqnames(rr)),
  pos = start(rr)
)

df <- merge(res, annot, by = "gene")

df <- df[!is.na(df$pvalue), ]
df <- df[!is.na(df$chr), ]

df$chr <- gsub("chr", "", df$chr)

keep_chr <- c(as.character(1:22), "X", "Y")
df <- df[df$chr %in% keep_chr, ]

df$chr <- factor(df$chr, levels = keep_chr)

df <- df[order(df$chr, df$pos), ]

df$logp <- -log10(df$pvalue)

chr_offsets <- cumsum(c(0, tapply(df$pos, df$chr, max)[-length(levels(df$chr))]))
names(chr_offsets) <- levels(df$chr)

df$pos_cum <- df$pos + chr_offsets[as.character(df$chr)]

chr_centers <- tapply(df$pos_cum, df$chr, mean)

png(
  "figures/manhattan_gbm_lgg.png",
  width = 1800,
  height = 900,
  res = 180
)

plot(
  df$pos_cum,
  df$logp,
  pch = 16,
  cex = 0.35,
  col = as.numeric(df$chr) %% 2 + 1,
  xaxt = "n",
  xlab = "Chromosome",
  ylab = "-log10(p-value)",
  main = "Manhattan plot: differential expression GBM vs LGG"
)

axis(
  1,
  at = chr_centers,
  labels = names(chr_centers),
  las = 2,
  cex.axis = 0.7
)

abline(
  h = -log10(0.05),
  col = "red",
  lty = 2
)

dev.off()

print("Manhattan plot completed")