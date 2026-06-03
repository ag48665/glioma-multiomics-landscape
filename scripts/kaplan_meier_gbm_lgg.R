library(survival)

surv <- read.delim(
  "results/tables/tcga_survival.tsv"
)

surv <- surv[
  surv$project_id %in% c("TCGA-GBM", "TCGA-LGG"),
]

surv$project <- ifelse(
  surv$project_id == "TCGA-GBM",
  "GBM",
  "LGG"
)

fit <- survfit(
  Surv(overall_survival_days, event) ~ project,
  data = surv
)

png(
  "figures/kaplan_meier_gbm_lgg.png",
  width = 1000,
  height = 800
)

plot(
  fit,
  col = c("red", "blue"),
  lwd = 3,
  xlab = "Days",
  ylab = "Survival probability",
  main = "Kaplan-Meier: GBM vs LGG"
)

legend(
  "topright",
  legend = levels(factor(surv$project)),
  col = c("red", "blue"),
  lwd = 3
)

dev.off()

print("GBM vs LGG Kaplan-Meier completed")