library(circlize)

edges <- read.delim(
  "results/tables/comutation_edges.tsv"
)

genes <- c(
  "IDH1", "TP53", "ATRX",
  "EGFR", "PTEN", "NF1",
  "CIC", "FUBP1"
)

edges <- edges[
  edges$gene1 %in% genes &
  edges$gene2 %in% genes,
]

edges <- edges[edges$co_mutated_patients >= 10, ]

png(
  "figures/chord_comutation.png",
  width = 1200,
  height = 1200,
  res = 180
)

chordDiagram(
  edges[, c("gene1", "gene2", "co_mutated_patients")],
  transparency = 0.3
)

title("Chord diagram: glioma co-mutated driver genes")

dev.off()

print("Chord diagram completed")