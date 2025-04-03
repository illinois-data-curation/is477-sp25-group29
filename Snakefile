rule reproduce_all:
    input:
        'results/Correlation_heatmap.png',
        'results/merged_data.csv',
        'results/r2_cpi.txt',
        'results/r2_mortgage.txt',
        'results/Relationship_scatterplot.png',
        'results/Visualizations.png'
rule dataacquisition:
    output:
        'data/30_year_mortgage_rate_2012_2022.csv',
        'data/US House Price and Mortgage Rate.csv'
    shell:
        'python scripts/dataacquisition.py'
rule datacleaning:
    input:
        'data/30_year_mortgage_rate_2012_2022.csv',
        'data/US House Price and Mortgage Rate.csv'
    output:
        'results/merged_data.csv'
    shell:
        'python scripts/datacleaning.py'
rule Analysis:
    input:
        'results/merged_data.csv'
    output:
        'results/Correlation_heatmap.png',
        'results/r2_cpi.txt',
        'results/r2_mortgage.txt',
        'results/Relationship_scatterplot.png',
        'results/Visualizations.png'
    shell:
        'python scripts/Analysis.py'