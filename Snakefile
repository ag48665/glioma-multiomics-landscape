configfile: "config/config.yaml"

rule all:
    input:
        "results/tables/project_status.tsv",
        "results/tables/cohort_summary.tsv"

rule project_status:
    output:
        "results/tables/project_status.tsv"
    shell:
        "echo step,status > {output} && echo setup,ok >> {output}"

rule cohort_summary:
    output:
        "results/tables/cohort_summary.tsv"
    script:
        "scripts/cohort_summary.py"