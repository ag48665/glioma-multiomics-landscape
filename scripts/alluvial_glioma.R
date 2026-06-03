library(ggalluvial)
library(ggplot2)
library(dplyr)
library(readr)

mut <- read_tsv("results/tables/mutation_comparison_gbm_lgg.tsv")

df <- data.frame(
  Tumor = c("GBM","GBM","GBM","GBM",
            "LGG","LGG","LGG","LGG"),
  Gene = c("EGFR","PTEN","TP53","IDH1",
           "EGFR","PTEN","TP53","IDH1"),
  Freq = c(23,33,31,6,
           6,5,48,77)
)

png(
  "figures/alluvial_gbm_lgg.png",
  width = 1400,
  height = 900,
  res = 150
)

ggplot(
  df,
  aes(axis1 = Tumor,
      axis2 = Gene,
      y = Freq)
) +
  geom_alluvium(aes(fill = Gene),
                width = 1/12) +
  geom_stratum(width = 1/8,
               fill = "grey90",
               color = "black") +
  geom_text(stat = "stratum",
            aes(label = after_stat(stratum))) +
  scale_x_discrete(
    limits = c("Tumor","Gene"),
    expand = c(.05,.05)
  ) +
  ggtitle("GBM vs LGG driver-gene landscape") +
  theme_minimal()

dev.off()

print("Alluvial plot completed")