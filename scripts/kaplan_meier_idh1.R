library(survival)

surv <- read.delim("results/tables/tcga_survival.tsv")
idh1 <- read.delim("results/tables/idh1_status.tsv")

dat <- merge(
  surv,
  idh1,
  by = "submitter_id"
)

fit <- survfit(
  Surv(overall_survival_days, event) ~ IDH1_status,
  data = dat
)

png(
  "figures/kaplan_meier_idh1.png",
  width = 1200,
  height = 900
)

plot(
  fit,
  col = c("darkgreen", "red"),
  lwd = 3,
  xlab = "Days",
  ylab = "Survival probability",
  main = "Kaplan-Meier: IDH1 mutant vs wildtype"
)

legend(
  "topright",
  legend = levels(factor(dat$IDH1_status)),
  col = c("darkgreen", "red"),
  lwd = 3
)

dev.off()

print("IDH1 Kaplan-Meier completed")