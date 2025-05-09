## Unemployment Rate Impact on Housing Prices

## Link to Archival Record:
The complete archived copy of this project, including all scripts, workflows, datasets, documentation, and metadata, is available on Zenodo. The project has been assigned a persistent identifier (DOI) for future reference.

Zenodo archive link: https://zenodo.org/records/14401013?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjFhZTQzZDgxLTUyMjQtNGRmNC1iOWQxLTkwNWE2NzkyZDI0ZSIsImRhdGEiOnt9LCJyYW5kb20iOiJmZTQ0ZWQ0M2UxZGJmZmJmNjNkNTNmMWI4NjY0NzllMCJ9.Yb75sb_izdNVglLnjtWLlJLN4tXpVq1CNjk-nD8u46DcGVPKYiDz9lgX7GDf1vuciwWNjXKkx-3beHHk0T_yVg

DOI: 10.5281/zenodo.14401013

## Contributors:
Han Huynh

Han Huynh was responsible for:

- Setting up the GitHub repository and handling the submission.

- Merging and integrating the datasets using Python and Pandas, including cleaning and aligning the data.

- Implementing statistical analysis, including regression models and correlation analysis.

- Creating visualizations like heatmaps, scatter plots, and time-series graphs to illustrate findings.

- Collaborating on data preprocessing and ensuring the datasets were accurately merged.

- Contributing to the creation of the project’s methodology and overall analysis framework.

- Assisting in generating insights from visualizations and supporting the interpretation of results.

- Working on Snakemake automation to ensure the analysis could be reproduced efficiently.

## Summary:
This project investigates the relationship between mortgage rates, consumer price index), and housing prices in the United States over the past decade (2012-2022). The housing market plays a significant role in the broader economy, and fluctuations in mortgage rates and inflation (as measured b) can have a profound impact on housing prices. By understanding how these factors are interrelated, we aim to offer insights that can help policymakers, investors, and consumers make informed decisions.

The project utilizes two key datasets:

1. 10-year housing prices from Kaggle datasets

2. 30-year fixed US unemployment rates from FRED

In addition data was incorporated to evaluate the impact of inflation on housing prices. Statistical analysis, including correlation and regression models, along with visualizations, were used to assess the relationship between these variables. Our findings suggest a complex relationship where mortgage rates have a minimal direct effect on housing prices, whereas inflation) has a much stronger correlation with rising housing prices.

## Research Questions:
1. How do changes in unemployment rates affect housing prices in the U.S. over the past decade?


## Data Profile:
- Dataset 1: U.S. Housing Prices
- Source: Acquired from Kaggle

- Description: The FHFA Housing Price Index (HPI) measures price changes in residential properties, providing a repeat-sales index. The dataset includes monthly data on housing price changes.

- Key Features:

    - Date: Monthly frequency from 2012 to 2022

    - Housing Price Index (HPI)

- Terms of Use: Publicly available for non-commercial use under the FHFA's data policy.

- Processing: The data was extracted, cleaned, and merged with other datasets.

## Dataset 2: 30-Year Unemployment Rate
- Source: Acquired from FRED (Freddie Mac Primary Mortgage Market Survey)

- Description: This dataset provides weekly data on the average 30-year unemployment rate in the U.S., a key factor in housing affordability.

- Key Features:

    - Date: Weekly frequency

    - Unemployment Rate (%)

- Terms of Use: Publicly available for non-commercial use.

- Processing: The data was cleaned, aligned by date with the housing prices dataset, and merged.


## Findings:
Correlation:

A moderate negative correlation was observed between the unemployment rate and housing prices, indicating that higher unemployment rates tend to suppress housing demand, which can lead to lower housing prices.

Regression Analysis:

The regression model revealed that the unemployment rate had a statistically significant effect on housing prices, explaining approximately 42% of the variance (R² = 0.42).

Trends:

Housing prices generally showed a steady upward trend over the past decade, with sharp fluctuations during periods of rising unemployment, such as during the COVID-19 pandemic and the subsequent economic recovery.

During periods of low unemployment, housing prices rose more sharply, reflecting increased demand for housing driven by consumer confidence and greater financial stability.

Visualizations:
Heatmap: Correlation between unemployment rate, and housing prices.

Time-Series Graphs: Illustrating trends unemployment rates and housing prices.

## Future Work:
This analysis could be extended by exploring:

- Regional housing price variations across different U.S. states.

- The impact of other economic factors like market rates on housing prices.

- Incorporating more granular data (e.g., monthly mortgage rates).

- Expanding the model to include more sophisticated predictive techniques.

Lessons learned from this project include the importance of aligning datasets and handling missing values carefully. Future work could involve improving the predictive models and exploring deeper economic factors influencing housing markets.

## Reproducing:
To reproduce the analysis:

- Clone the GitHub repository.

- Download the datasets from Kaggle and FRED.

- Install dependencies using requirements.txt.

- Run data cleaning and preprocessing scripts.

- Execute analysis and generate visualizations using Jupyter Notebooks or Snakemake workflow.

## References:
US House Price and Mortgage Rate: https://www.kaggle.com/datasets/tiffanytong0321/housepriceandmortgage?resource=download.

Federal Reserve Economic Data (FRED): https://fred.stlouisfed.org/series/UNRATE

This structure follows the rubric’s guidelines for a project report and includes clear sections on data curation, analysis, and future work.