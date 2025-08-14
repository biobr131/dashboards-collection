cran_packages <- c(
    "tidyverse",
    "anndata",
    "Seurat",
    "Signac",
    "WGCNA",
    "arrow",
    "data.table",
    "DBI",
    "RPostgres",
    "pool",
    "plotly",
    "reactable",
    "flexdashboard",
    "rmarkdown",
    "knitr",
    "bigrquery",
    "aws.s3",
    "AzureStor"
)
install.packages(cran_packages, dependencies = TRUE)

bioconductor_packages <- c(
    "BiocVersion",
    "BioBase",
    "BiocGenerics",
    "DESeq2",
    "edgeR",
    "monocle",
    "clusterProfiler",
    "mixOmics"
)
BiocManager::install(bioconductor_packages, dependencies = TRUE)
