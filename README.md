# Glioma Multi-Omics Landscape

Topology-informed multi-omics analysis of human gliomas using TCGA data.

## Research Question

Can molecular and clinical data identify glioma subgroups associated with patient survival?

## Datasets

- TCGA-GBM (Glioblastoma)
- TCGA-LGG (Lower Grade Glioma)

## Data Types

- Clinical data
- Survival data
- Somatic mutations (MAF)
- RNA-seq (planned)

## Methods

### Clinical Survival Analysis

- Kaplan-Meier survival analysis
- GBM vs LGG comparison
- IDH1-mutant vs IDH1-wildtype comparison

### Mutation Analysis

- TCGA mutation download using TCGAbiolinks
- Driver gene analysis
- Mutation frequency analysis
- Mutation heatmap generation

### Planned Analyses

- Differential expression analysis
- Pathway enrichment
- Network analysis
- Topological data analysis

## Results

### GBM vs LGG Survival

LGG patients show substantially longer survival than GBM patients.

![GBM vs LGG](figures/kaplan_meier_gbm_vs_lgg.png)

### IDH1 Mutation Status and Survival

Patients carrying IDH1 mutations exhibit improved overall survival.

![IDH1 survival](figures/kaplan_meier_idh1.png)

### Driver Gene Mutation Landscape

Frequently altered genes in TCGA-GBM include:

| Gene | Mutation count |
|--------|--------:|
| TP53 | 175 |
| PTEN | 157 |
| EGFR | 135 |
| NF1 | 69 |
| ATRX | 52 |
| IDH1 | 26 |

### Driver Gene Heatmap

![Driver heatmap](figures/driver_gene_mutation_heatmap.png)

## Repository Structure

```text
config/
reports/
scripts/
results/
figures/
Snakefile
README.md
```
##  Results
# Results

## Mutation landscape of gliomas

Somatic mutation analysis revealed distinct genomic profiles between glioblastoma (GBM) and lower-grade glioma (LGG). In GBM, the most frequently mutated genes were **PTEN (33%)**, **TP53 (31%)**, and **EGFR (23%)**, whereas LGG was characterized by a markedly higher prevalence of **IDH1 (77%)**, **TP53 (48%)**, and **ATRX (37%)** mutations.

Oncoplot visualization demonstrated the classical molecular distinction between glioma subtypes. GBM samples showed enrichment of receptor tyrosine kinase and PI3K pathway alterations, while LGG samples were dominated by IDH1-associated molecular signatures.

## Co-occurrence and mutual exclusivity patterns

Mutual exclusivity analysis identified significant relationships between major glioma driver genes. A strong mutually exclusive pattern was observed between **EGFR** and **IDH1**, reflecting their association with distinct glioma subtypes. Conversely, significant co-occurrence was detected between **ATRX** and **TP53**, consistent with the molecular profile of IDH-mutant astrocytomas.

Chord diagram analysis further highlighted recurrent co-mutation networks involving ATRX, TP53, CIC, and FUBP1, suggesting subtype-specific genomic cooperation.

## Survival analysis

Kaplan–Meier analysis demonstrated substantial survival differences between GBM and LGG patients. LGG patients exhibited significantly prolonged overall survival compared with GBM patients, reflecting the known biological aggressiveness of glioblastoma.

Additional stratification by IDH1 mutation status revealed that patients harboring IDH1 mutations experienced markedly improved survival outcomes relative to IDH1 wild-type tumors. This finding supports the established prognostic value of IDH1 alterations in diffuse gliomas.

## Differential gene expression

Differential expression analysis between GBM and LGG identified a large set of significantly deregulated genes. Volcano plot visualization demonstrated widespread transcriptional differences between tumor types, with thousands of genes exhibiting significant fold changes.

Several highly dysregulated genes showed strong enrichment in either GBM or LGG, highlighting distinct transcriptional programs associated with tumor progression, metabolism, and cellular differentiation.

## Tumor heterogeneity and mutational processes

Rainfall plots revealed heterogeneous mutation clustering across individual GBM genomes, suggesting localized hypermutation events and variable mutational densities across chromosomes.

Transition/transversion (Ti/Tv) analysis showed characteristic nucleotide substitution patterns, with C>T transitions representing a dominant mutational class. These patterns are consistent with previously reported mutational processes in glioma genomes.

## Multi-omics integration

Integrated visualization using alluvial and comparative oncoplot analyses demonstrated clear separation between GBM and LGG molecular architectures.

LGG tumors were strongly associated with IDH1-driven genomic programs, whereas GBM samples displayed enrichment of EGFR and PTEN alterations. These findings collectively support the concept that GBM and LGG represent biologically distinct disease entities despite sharing a common glial origin.


## Technologies

- Python
- R
- TCGAbiolinks
- pandas
- matplotlib
- survival
- Snakemake

## Author

Agata Gabara
