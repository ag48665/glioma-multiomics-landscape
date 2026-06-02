library(survival)

surv <- read.delim(
  "results/tables/idh1_survival.tsv",
  sep="\t"
)

png(
  "figures/kaplan_meier_idh1.png",
  width=1000,
  height=800
)

fit <- survfit(
  Surv(overall_survival_days, event) ~ IDH1_status,
  data = surv
)

plot(
  fit,
  col=c("red","blue"),
  lwd=3,
  xlab="Days",
  ylab="Survival probability",
  main="Kaplan-Meier: IDH1 mutant vs wildtype"
)

legend(
  "topright",
  legend=levels(as.factor(surv$IDH1_status)),
  col=c("red","blue"),
  lwd=3
)

dev.off()