# Mortgage Rate impace on Housing price project

## Link to archival record:
The complete archived copy of this project, including all scripts, workflows, datasets, documentation, and metadata is available on Zenodo. The project has been assigned a persistent identifier (DOI) for future reference.
- Zenodo archive link: https://zenodo.org/records/14401013?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjFhZTQzZDgxLTUyMjQtNGRmNC1iOWQxLTkwNWE2NzkyZDI0ZSIsImRhdGEiOnt9LCJyYW5kb20iOiJmZTQ0ZWQ0M2UxZGJmZmJmNjNkNTNmMWI4NjY0NzllMCJ9.Yb75sb_izdNVglLnjtWLlJLN4tXpVq1CNjk-nD8u46DcGVPKYiDz9lgX7GDf1vuciwWNjXKkx-3beHHk0T_yVg&fbclid=IwY2xjawHHMRxleHRuA2FlbQIxMAABHWdNyGAC031rR0DmQFmWJ3TSqgh32MeXe5dIiYegv7oSWstioaM5wZIFcg_aem_FP8oO6OOnhsnuFx-iDJPoQ
- DOI: 10.5281/zenodo.14401013
## Contributors:
- Han Huynh

Han Huynh was responsible for the following parts:
- Setting up the GitHub repository and handling the submission.
- Merging and integrating the datasets using Python and Pandas, including cleaning and aligning the data.
- Implementing the statistical analysis, including regression models and correlation analysis.
- Creating visualizations like heatmaps, scatter plots, and time-series graphs to illustrate the findings.
- Collaborating on data preprocessing and ensuring the datasets were accurately merged.
- Contributing to the creation of the project’s methodology and overall analysis framework.
- Assisting in generating insights from the visualizations and supporting the interpretation of results.
- Working on the Snakemake automation setup to ensure the analysis could be reproduced efficiently.

She worked throughout the project dilligently and made sure to check deadlines, ensuring that the analysis was comprehensive and well-rounded.

## Summary:
### Project Overview:
This project investigates the relationship between mortgage rates, consumer price index (CPI), and housing prices in the United States over the past decade. Housing prices are a critical economic indicator, reflecting household wealth, affordability, and broader economic conditions. Understanding the impact of mortgage rates and inflation on housing prices is vital for policimakers, investors, and consumers to make informed decisions.

The analysis leverages two datasets:
1. Historical housing prices from the Federal Housing Finance Agency (FHFA)
2. 30-year fixed mortgage rates

The goal is to assess how fluctuations in mortgage rates and inflation (proxied by CPI) influence changes in housing prices. This analysis combines statistical methods, data integration, and visualizations to offer meaningful insights

### Motivation: 
The motivation for this research arises from the significant role housing markets play in the broader economy. Housing prices are affected by numerous factors, including interest rates, inflation, and economic stability. Mortgage rates, which determine the cost of borrowing for prospective homeowners, are especially influential. Simultaneously, inflation purchasing power, potentially impacting demand for real estate. 

The project address the following key questions:
- How do mortgage rates affect housing prices in the U.S. over the past decade?
- What is the role of inflation (via CPI) in influencing housing prices?
- Can statistical analysis quantify these relationships and identify trends or patterns?

By exploring these questions, the project contributes to a deeper understanding of the housing market dynamics.

### Research questions
1. How do changes in mortgage rates affect housing prices in the United States over the last 10 years?
2. How does inflation, as measured by the Consumer Price Index (CPI), impact housing prices over the same period?
3. Are these relationships statistically significant, and can they be visualized through trends or predictive models?

### Methodology
1. Data integration: 
- Two datasets were programmatically merged using Python and Pandas. The FHFA housing price index and the 30-year mortgage rate were aligned by date.
- CPI data was incorporated to reflect inflationary effects.
- Data cleaning included handling missing values, standardizing formats, and ensuring aligment across datasets
2. Exploratory Data Analysis (EDA):
- Correlation analysis was performed to assess the relationship between variables.
- Line plots and scatter plots were used to identify trends over time.
3. Statistical Analysis:
- A linear regression model was implemented to quantify the impact of mortgage rates on housing prices.
- CPI was included as an additional explanatory variable to evaluate it influence.
4. Visualizations:
- Heatmap highlighted the strengthe and directions of correlations.
- Time-series graphs illustrated rends in housing prices, mortgage rates, and CPI.
5. Reproducible Workflow:
- The entire analysis was automated using Snakemake to ensure reproducibility. Scripts for data preprocessing, analysis, and visualization were modular and scalable.

### Findings
1. Correlation:
- A negative correlation was observed between mortgage rates and housing prices, indicating that higher borrowing costs tend to reduce demand for housing
- A positive correlation was noted between CPI and housing prices, suggesting that inflationary pressures drive up real estate values.
2. Regression Analysis:
- The regression model revealed that mortgage rates had a statistically insignificant effect on housing prices. The R^2 score was only 0.0043
- CPI exhibited a positive and significant effect, with a R^2 score of 0.98.
3. Trends:
- Housing prices showed a steady upward trend over the past decade, with periods of sharp increased corresponding to historically low mortgage rates.
- Rising inflation in recent years has coincided with accelerated growth in housing prices, emphasizing its influence.

### Conclusion

This project highlights the critical interplay between mortgage rates, inflation, and housing prices. The findings suggest that mortgage rates and inflation are significant drivers of housing prices, aligning with economic theory. When mortgage rates are low, housing becomes more affordable, driving up demand and prices. Conversely, inflation erodeds purchasing power but also increases asset values, including real estate.

The automoated workflow and reproducible framework ensure that this analysis can be extended with new data or additional variables. Future research could incorporate broader datasets, such as regional housing prices or unemployment rates, to refine these findings.

this study provides valuable insights for policy makers, financial institutions, and real estate stakeholders, enabling better decision-making in the context of housing market dynamics.

## Data Profile:
### Overview

This project utilizes two primary datasets to analyze the relationship between mortgage rates, inflation, and housing prices in the United States over the past decade. Each dataset was chosen for its relevance to the research questions and provides critical economic indicators neccessary for the analysis.

### Dataset 1: US House Price and Mortgage rate
- Source: Acquired on Kaggle
- Links on Kaggle:
    - https://www.fhfa.gov/DataTools/Downloads/Pages/House-Price-Index-Datasets.aspx
    - https://fred.stlouisfed.org/series/MORTGAGE30US
    - https://www.bls.gov/regions/mid-atlantic/data/consumerpriceindexhistorical_us_table.htm
- Description for HPI: The FHFA Housing Price Index (HPI) is a weighted, repeat-sales index measuring average price changes in repeat sales or refinancings on the same properties. It serves as a benchmark for analyzing the appreciation or depreciation trends in residential property prices across the United States.
- Key Features for HPI:
    - Date: Monthly frequency representing the observation period.
    - Housing Price Index: Reflects the relative price level of homes
- Terms of Use for HPI: The FHFA HPI is publicly available for non-comercial use and is distritbuted under the terms of the FHFA's data policy. Users must acknowledge FHFA as the source and are prohibited from using the data for unauthorized commercial purposes.
    - Full policy: https://www.fhfa.gov/
- Processing for HPI:
    - Extracted monthly data for the period 2012-2022
    - Cleaned missing values and aligned dates with other datasets
- Description for CPI: The CPI measures the average change over time in the prices paid by urban consumers for a basket of goods and services. It is widely used as an indicator of inflation.
- Key Features for CPI:
    - Date: Monthly frequency representing the observation period
    - CPI: The aggregate consumer price index for all items in the basket
- Terms of Use for CPI: The Bureau of Labor Statistics data is freely available for public use. Proper atribution is required when utilizing the data for research or publication process
    - Full policy: https://www.bls.gov/
- Processing for CPI:
    - Extracted CPI data for 2012-2022
    - Normalized CPI values and merged with other datasets on a monthly frequency.

### Dataset2: 30-year Fixed Mortgage Rate
- Source: Acquired from FRED (from Freddie Mac Primary Mortgage Market Survey)
- Description: This dataset provides weekly data on ther average 30-year fixed mortgage rates in the United States. These rates are an essential factor in determining the affordability of homes and the cost of financing.
- Key Features:
    - Date: Weekly frequency representing observation periods
    - Mortgage Rate (%): The average 30-year fixed mortgage rate for the given period
- Terms of Use: The Freddie Mac PMMS data is available under public terms for non-commercial research and educational purposes. Redistribution requires proper attribution to Freddie Mac.
    - Full policy: https://www.freddiemac.com/pmms/syndication/how_to#:~:text=Terms%20and%20Conditions,the%20possibility%20of%20such%20damages.

### Integration and Cleaning

To ensure the datasets were compatible for analysis:
1. Standardization:
- Dates across all datasets were converted into a consistent monthly format
- Missing data points were either removed or complemented by one of the two datasets
2. Merging:
- The datasets were merged on the common Date column.
- A complete dataset with columns for HPI, Mortgage Rate, and CPI was created, enabling direct analysis of their relationship

### Data Quality Assessment
- Completeness:
    - All datasets were reasonably complete. Missing values in CPI and Mortgage Rates were minor and handled using drop or interpolation.
- Consistency:
    - Formatting inconsistencies (e.g., date formats) were resolved during preprocessing.
- Accuracy:
    - The sources (FHFA, Freddie Mac, and BLS) are reputable organizations, ensuring high data reliability.

### Summary

The combined datasets offer a comprehensive view of the interplay between housing prices, mortgage rates, and inflation over the past decade. By adhering to licensing terms  and applying robust cleaning processes, the project ensures data integrity and reproducibility. This foundation enables meaningful analysis and facilitates transparent reporting of findings.

## Findings

This project examined the relationship between U.S. housing prices, mortgage rates, and inflation (measured by the CPI) over the last decade (2012-2022). Using datasets from Kaggle and FRED (source: Federal Housing Finance Agency, Freddie Mac, and the U.S. Bureau of Labor Statistics), statistical analysis and visualizations were employed to derive insights. Below is a summary of the findings.

### Key Observations
1. Trend analysis:
- Housing prices consistently rose over the decade, with an especially steep increase after 2020.
- Mortgage rates fluctuated significantly, with a prolonged period of low rates during the COVID-19 pandemic (2020-2021), followed by increases in 2022.
- The Consumer Price Index (CPI) steadily increased over the decade, reflecting persistent inflationary pressures, with a sharp rise starting in 2021.
2. Correlation Analysis:
- A very weak negative correlation (-0.07) was observed between mortgage rates and housing prices. This suggests that changes in mortgage rates alone have minimal direct impact on housing prices during the observed period.
- A strong positive corrleation (0.99) was found between CPI and housing prices, indicating a nearly linear relationship. As inflation increased, housing prices rose significantly, possibly reflecting inflation's effect on the cost of constuction and the role of real estate as an inflation hedge.

### Regression Analysis

Two separate linear regression models were built to analyze the relationship between housing prices and the independent variables (mortgage rates and CPI). The results are as follows:
1. Model 1: Housing Prices vs. Mortgage Rates
- R^2 value: 0.0043
    - The model explains less than 1% of the variance in housing prices. Mortgage rates have a negligible predictive value for housing prices.
2. Model 2: Housing Prices vs. CPI
- R^2 value: 0.9837
    - The model explains 98.37% of the variance in housing prices, indicating an extremely strong fit.

### Visualizations
1. Time-Series trends:
- Line charts of housing prices, mortgage rates, and CPI showed:
    - A weak association between mortgage rate fluctuations and housing price trends.
    - A strong alignment between CPI and housing prices, particularly during periods of high inflation.
![Time-Series trends](results/Visualizations.png)
2. Scatter plots:
- Scatter plot of mortgage rates vs. housing prices revealed a nearly flat trend line, reflecting the weak correlation.
- Scatter plot of CPI vs. housing prices showed a clear upward trend, emphasizing their strong positive relatioship
![Scatter plots](results/Relationship_scatterplot.png)
3. Heatmap:
- The correlation heatmap visually highlighted the negligible relationship between mortgage rates and housing prices and the near-perfect correlation between CPI and housing prices
![Heat map](results/Correlation_heatmap.png)
### Findings Summary
1. Mortgage Rates and Housing Prices:
Despite theoretical expectations of a negative relationship, the analysis indicates that mortgage rates had little direct impact on housing prices over the past decade. This could be attributed to other factors, such as strong housing demand, supply constraints, and low inventory, which overshadowed changes in financing costs.
2. Inflation (CPI) and Housing Prices:
The nearly linear relationship between CPI and housing prices underscore the significant influence of inflation on housing costs. Rising prices for materials, labor, and land likely contributed to the observed trends. Additionally, real estate's function as an inflation hedge likely drove demand, furhter amplifying price increases.
3. Broader Implications:
The findings suggest that inflation is a far more dominant factor in driving housing price changes than mortgage rates. Policymakers and investors should prioritize inflationary trends when assessing the housing market.

### Conclusion

This analysis demonstrates that while mortgage rates have minimal power for housing price trends, inflation (CPI) plays a critical role. The findings align with economic theory regarding inflation and its effects on asset prices. Future research could investigate additional variables, such as regional disparities, wage growth, and housing supply, to gain a deeper understanding of these dynamics.

## Future Work

This project explored the relationship between U.S. housing prices, mortgage rates, and inflation over the last decade (2012-2022). While the findings were insightful, several challenges and limitations emerged, offering valuable lessons and opportunities for future work. Below is a discussion of these lessons and potential avenues for extending the research.

### Lessons Learned
1. Data Integration Challenges

Combinding datasets from multiple source required significant preprocessing, such as aligning time intervals and resolving missing data. this step emphasized the importance of a systematic approach to data cleaning and integration. Automating this process using tools like Snakemake provided efficiency, but issues with software setup highlighted the need for robust development environments and user-friendly automation tools.

2. Complexity of Housing Market Dynamics

The weak correlation between mortgage rates and housing prices suggests that housing market trends are influenced by numerous factors beyond macroeconomic indicators. These factors may include housing supply, local market conditions, consumer behavior, and governmental policies. Simplistic models may fail to capture the intricacies of these interactions, underscoring the need for multifactorial analyses.

3. Impact of Inflation

The strong correlation between CPI and housing prices highlighted inflation's significant role in real estate markets. However, it also raised questions about causation versus correlation. While inflation likely impacts housing prices, reverse causality or mutual influences from other variables, such as wage growth or monetary policy, cannot be ruled out.

4. Model limitations

Linear regression models provided a starting point but were limited in capturing non-linear relationships and interaction effects. Additionally, the extremely high R^2 value for the CPI model suggested possible overfitting, warranting caution in interpreting results.

### Potential Future Work
1. Incorporating Additional Variables

Future studies could enhance the analysis by including more granular data:
- Regional data: Housing prices, mortgage rates, and CPI can vary significantly by state or metropolitan area. Regional analysis would allow for deeper insights into local housing market dynamics
- Supply-side Factors: Variables such as housing inventory, new construction rates, and zoning regulations could shed light on supply constraints affecting prices
- Demographic Trends: Population growth, migration patterns, and household formation rates could provide context for demand-side pressures.
- Economic Indicators: Including variables such as unemployment rates, wage growth, and monetary policy changes could improve the model's explanatory power.

2. Advanced Modeling Techniques

While linear regression provided a baseline, future research could benefit from:
- Machine learning models: Techniques like decision trees, random forests, or neural networks could capture complex, non-linear relationships between variables
- Time-Series Analysis: Models such as ARIMA, VAR, or LSTM could better account for temporal dependencies in the data.
- Causal Inference Methods: Approaches like instrumental variables or difference-in-differences could help disentagle causality from correlation.

3. Longer Time Horizons

Expanding the study period beyond a single decade could provide insights into longer-term trends and cyclical patterns in the housing market. For instance, including data from earlier housing crises or economic downturns might reveal how relationships between variables change under different market conditions.

4. Policy Impact Analysis

Investigating the role of government policies, such as interest rate changes by the Federal Reserve or housing subsidies, could add a valuable dimension to the analysis. For example:
- How do changes in mortgage interest deduction policies impact housing prices?
- What role do monetary and fiscal policies play in mitigating housing market volatility during economic crises?

5. Interactive Visualizations

Developing interactive dashboards or web-based tools to visualize the relationships between variables could make the findings more accessible to policymakers, researchers, and the general public. These tools could allow users to explore "what-if" scenarios, such as the impact of a hypothetical increase in mortgage rates or inflation on housing prices.

6. Exploring Global Comparisons

Comparing the U.S. housing market dynamics with those of other countries could offer a broader perspective. This could help identify unique aspects of the U.S. market or universal trends that apply across different economies.

### Broader Implications

This project highlighted the critical role of macroeconomic factors, particularly inflation, in shaping housing prices. However, the findings also underscored the complexity of the housing market, where numerous interdependent factors interact. Future work that integrates these elements could provide a more holistic understanding of housing market dynamics and inform better policy decisions.

### Conclusion

The lessons learned from this project and the outlined avenues for future work emphasize the importance of iterative, interdisciplinary research in understanding housing markets. By incorporating more data, employing advanced analytical methods, and addressing current limitations, future studies can build on these findings to offer deeper insights and practical recommendations for stakeholders in real estate, finance, and policymaking.

## Reproducing

Below is a detailed guide for reproducing the project’s results, including data acquisition, integration, profiling, cleaning, analysis, and workflow execution. Each section includes the necessary steps, tools, and explanations to ensure the project can be reproduced successfully.

### Data Acquisition
1. Download the datasets:
- 30-Year Mortgage Rates Dataset: Download the data from a trusted source such as the Federal Reserve Economic Data (FRED) or another reliable provider. Ensure the data covers 2012–2022.
- U.S. Housing Prices Dataset: Obtain via Kaggle (link: https://www.kaggle.com/datasets/tiffanytong0321/housepriceandmortgage?resource=download)
2. Verify integrity
3. Save files: save the dataset to folder named 'data'.

### Data Integration
1. Load Datasets: Use Python with Pandas to load the datasets into DataFrames. Drop missing values and change 'Date' column to datetime.
2. Align Timeframes: Ensure both datasets cover the same timeframe (2012-2022). 
3. Merge Datasets: Merge the datasets on the common 'Date' column
4. Save Merged Data: Save the resulting datset to a folder named 'results' for reproducibility.

### Data Analysis and Visualization
1. Correlation Analysis: Compute correlations between variables
2. Linear Regression: Fit linear regression moedels for housing price predictions based on mortgage rates and CPI
3. Visualization: Create scatterplots and trend lines to visualize relationships.
4. Save outputs: Save figures and analysis results in a folder named 'results'.

### Workflow Automation:
1. Set up Snakemake workflow: Create a Snakefile to automate the entire process
2. Run Workflow: snakemake --cores 1


#### Data Citations
- For each dataset, find the suggested citation from the source.
- Cite the software packages used (e.g., Python, Pandas, Snakemake).
  
### Metadata for Your Dataset

#### **Descriptive Metadata**
- Title: Name of your dataset (e.g., "Impact of Mortgage Rates on Housing Prices").
- Creator/Author:List the authors (e.g., Han Huynh).
- Date:The date the dataset was created or last modified.
- Keywords/Subjects: List relevant keywords (e.g., mortgage rates, housing prices, inflation, CPI).
- Description: Brief description of the dataset and its purpose.

#### Data Dictionary or Codebook
- Provide a text or PDF file describing each variable in your dataset, including:
   - Variable Name:** Name of the variable.
   - Type: Data type (e.g., float, integer, date).
   - Description: A brief description of what the variable represents.


### Archiving Your Project using Zenodo
1. Go to [Zenodo](https://zenodo.org/).
2. Create an account or log in.
3. Upload your project files (code, data, reports).
4. Fill in metadata (title, authors, description, keywords).
5. Click "Publish" to get a DOI.


### Obtaining a Persistent Identifier
- Once your project is published on Zenodo or CodeOcean, a persistent identifier (DOI) will be generated.
- Example citation for a DOI:  
  Pham, L., & Patel, N. (2024). *Impact of Mortgage Rates on Housing Prices* [Data set]. Zenodo. https://doi.org/10.1234/zenodo.1234567


## References

Below are the formatted ciations for the datasets, software, and other resources used in the project

### Datasets
1. Federal Reserve Economic Data (FRED)
- Title: "30-Year Mortgage Rates"
- Source: Federal Reserve Bank of St. Louis
- URL: https://fred.stlouisfed.org
2. Kaggle
- Title: "US House Price and Mortgage Rate"
- Source: Kaggle
- URL: https://www.kaggle.com/datasets/tiffanytong0321/housepriceandmortgage?resource=download
### Software and Libraries
1. Python
- Python Software Foundation. Python: A programming language.
    - URL: https://www.python.org/
    - Version: 3.11.9
2. Pandas
- Reback, J., McKinney, W., et al. Pandas: Powerful Python data analysis toolkit
    - URL: https://pandas.pydata.org
    - Version: 2.0.3
3. Scikit-learn
- Pedregosa, F., Varoquaux, G., et al. Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, pp. 2825-2830, 2011.
    - URL: https://scikit-learn.org
    - Version: 1.5.2
4. Matplotlib
- Hunter, J.D. Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), pp. 90-95, 2007.
    - URL: https://matplotlib.org
    - Version: 3.8.0
5. Snakemake
- Köster, J., Rahmann, S. Snakemake – a scalable bioinformatics workflow engine. Bioinformatics, 2012.
    - URL: https://snakemake.readthedocs.io
    - Version: 8.25.5
### Zenodo Archive 
- Zenodo Archive of Project
    - Title: Fed Rates and Mortgage Rates
    - DOI: 10.5281/zenodo.14401013
    - URL: https://zenodo.org/records/14401013?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjFhZTQzZDgxLTUyMjQtNGRmNC1iOWQxLTkwNWE2NzkyZDI0ZSIsImRhdGEiOnt9LCJyYW5kb20iOiJmZTQ0ZWQ0M2UxZGJmZmJmNjNkNTNmMWI4NjY0NzllMCJ9.Yb75sb_izdNVglLnjtWLlJLN4tXpVq1CNjk-nD8u46DcGVPKYiDz9lgX7GDf1vuciwWNjXKkx-3beHHk0T_yVg&fbclid=IwY2xjawHHMRxleHRuA2FlbQIxMAABHWdNyGAC031rR0DmQFmWJ3TSqgh32MeXe5dIiYegv7oSWstioaM5wZIFcg_aem_FP8oO6OOnhsnuFx-iDJPoQ
    - Description: Includes all scripts, documentation, and reproducible workflows used in the project
 
In this project, Linh Pham and Nandil Patel collaborated closely, with Linh handling the GitHub submission due to technical difficulties. Linh was primarily responsible for integrating and cleaning the datasets using Python and Pandas, conducting statistical analysis, and creating visualizations like heatmaps, scatter plots, and time-series graphs. Nandil contributed to the data preprocessing and merging process, assisted in developing the methodology and framework for the analysis, and helped interpret the results. Both team members worked together throughout the project, with Nandil also contributing to the setup of the Snakemake automation for reproducibility.
# is477-sp25-group29
