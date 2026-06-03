library(survival)

data <- read.delim(
  "results/tables/idh1_lgg_survival.tsv"
)

fit <- survfit(
  Surv(
    overall_survival_days,
    event
  ) ~ IDH1_status,
  data = data
)

png(
  "figures/kaplan_meier_idh1_lgg.png",
  width = 1000,
  height = 800
)

plot(
  fit,
  col = c("red","blue"),
  lwd = 3,
  xlab = "Days",
  ylab = "Survival probability",
  main = "LGG: IDH1 mutant vs wildtype"
)

legend(
  "topright",
  legend = levels(
    factor(data$IDH1_status)
  ),
  col = c("red","blue"),
  lwd = 3
)

dev.off()