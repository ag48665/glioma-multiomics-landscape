library(survival)

surv_data <- read.table(
  "results/tables/tcga_survival.tsv",
  sep = "\t",
  header = TRUE,
  stringsAsFactors = FALSE
)

surv_data <- surv_data[
  !is.na(surv_data$overall_survival_days),
]

fit <- survfit(
  Surv(overall_survival_days, event) ~ project_id,
  data = surv_data
)

png(
  "figures/kaplan_meier_gbm_vs_lgg.png",
  width = 1200,
  height = 900,
  res = 150
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
  legend = levels(as.factor(surv_data$project_id)),
  col = c("red", "blue"),
  lwd = 3
)

dev.off()