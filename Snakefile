configfile: "config/config.yaml"

rule all:
    input:
        "results/tables/project_status.tsv"

rule project_status:
    output:
        "results/tables/project_status.tsv"
    shell:
        "echo step,status > {output} && echo setup,ok >> {output}"