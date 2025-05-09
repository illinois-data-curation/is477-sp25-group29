rule reproduce_all:
    input:
        'results/correlation_heatmap.png',
        'results/merged_data.csv',
        'results/r2_scores.txt',
        'results/scatterplot.png',
        'results/time_series_trends.png'
rule dataacquisition:
    output:
        'data/Unemployment Rate.csv',
        'data/US House Price and Mortgage Rate.csv'
    shell:
        'python scripts/dataacquisition.py'
rule datacleaning:
    input:
        'data/Unemployment Rate.csv',
        'data/US House Price and Mortgage Rate.csv'
    output:
        'results/merged_data.csv'
    shell:
        'python scripts/datacleaning.py'
rule Analysis:
    input:
        'results/merged_data.csv'
    output:
        'results/correlation_heatmap.png',
        'results/merged_data.csv',
        'results/r2_scores.txt',
        'results/scatterplot.png',
        'results/time_series_trends.png'
    shell:
        'python scripts/Analysis.py'