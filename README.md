## Unemployment Rate Impact on Housing Prices

# 📊 Analysis of Unemployment and Housing Prices in the United States (2012–2022)

## 🔗 Archival Record  
**Zenodo Archive**: [https://zenodo.org/records/14401013](https://zenodo.org/records/14401013)  
**DOI**: [10.5281/zenodo.14401013](https://doi.org/10.5281/zenodo.14401013)

---

## 👤 Contributors  
**Han Huynh** (HHUYN3@illinois.edu)

**Responsibilities**:  
- Repository setup and Zenodo archival  
- Data acquisition and integration  
- Data cleaning and preprocessing using Python and Pandas  
- Statistical analysis and regression modeling  
- Visualizations (heatmaps, time series, regression plots)  
- Snakemake pipeline for reproducibility  
- Drafting summary, methods, and analysis

---

## 🧠 Summary  
🧠 Summary
This project explores the relationship between unemployment rates and housing prices in the United States from 2012 to 2022. The U.S. housing market is deeply intertwined with macroeconomic factors such as employment, income, interest rates, and consumer confidence. In recent years, especially during the COVID-19 pandemic, the country experienced significant economic disruptions—including historic levels of unemployment—that dramatically impacted housing affordability, availability, and pricing. These shifts prompted the central research question of this project:

How do changes in unemployment rates affect housing prices in the United States between 2012 and 2022?

The motivation behind this research stems from a desire to understand how labor market health influences residential property markets over time. Homeownership remains one of the most significant investments for most Americans, and fluctuations in employment can influence mortgage approval rates, consumer buying power, and market sentiment. Understanding this connection is essential for economists, urban planners, real estate professionals, and policymakers seeking to manage housing stability during economic cycles.

To investigate this question, the project utilized two primary datasets: the Federal Housing Finance Agency (FHFA) Housing Price Index (HPI), sourced from Kaggle, and weekly U.S. unemployment rates from the Federal Reserve Economic Data (FRED). These datasets were cleaned and resampled to ensure compatibility (monthly intervals), then merged on the date variable to create a unified view of housing prices and unemployment over a decade.

The analysis employed correlation analysis, linear regression, and data visualizations to uncover patterns and assess statistical relationships. A Pearson correlation test revealed a moderate negative correlation (r ≈ -0.63) between unemployment and housing prices—indicating that when unemployment rises, housing prices tend to fall, and vice versa. This finding aligns with economic theory, as higher unemployment generally reduces housing demand due to diminished financial confidence and constrained income.

The linear regression model further supported this insight. The unemployment rate explained approximately 42% of the variance in housing prices (R² = 0.42), and the relationship was statistically significant (p < 0.01). While this suggests unemployment is a key driver, the results also imply that other variables—such as interest rates, wage growth, housing supply, and inflation—also play important roles.

Time-series visualizations highlighted major trends and disruptions. From 2012 through 2019, housing prices increased steadily as unemployment rates declined following the Great Recession. In 2020, unemployment spiked sharply due to COVID-19 lockdowns, and housing prices initially flattened before rapidly accelerating in late 2020 through 2022—driven in part by low interest rates and inventory shortages. This dynamic period underscores the complexity of housing economics, where traditional unemployment–price relationships may shift during crisis recovery phases.

Ultimately, this project shows that while unemployment does not fully dictate housing price trends, it remains a statistically and economically significant factor. The findings contribute to a broader understanding of housing market dynamics and provide a foundation for future models that incorporate multiple interacting economic indicators.

This summary reflects a foundational analysis, and future extensions could involve regional comparisons, lagged effects, or machine learning approaches to improve predictive accuracy. By making the project fully reproducible with automated workflows, it also serves as a useful template for future longitudinal economic studies.

---

# 📁 Data Profile

This project relies on two publicly available datasets: the **Federal Housing Finance Agency (FHFA) Housing Price Index** and the **U.S. Unemployment Rate** from the Federal Reserve Economic Data (FRED). These two datasets were selected for their quality, national coverage, and relevance to the study of macroeconomic and housing market relationships in the United States from 2012 to 2022.

---

### 📊 Dataset 1: FHFA Housing Price Index (HPI)

- **Source**: [Kaggle](https://www.kaggle.com/datasets)  
- **Origin**: Federal Housing Finance Agency (FHFA)  
- **Coverage Period**: January 2012 – December 2022  
- **Frequency**: Monthly  
- **License**: Publicly available for non-commercial use under FHFA's open data policy  
- **Terms of Use**: Data may be redistributed and reused for analysis and educational purposes. Attribution to the FHFA is encouraged when results are shared or published.  
- **Download Location**: Data obtained from Kaggle repository titled “FHFA HPI Monthly (U.S.)”

**Description**:  
The Housing Price Index (HPI) is a weighted, repeat-sales index that measures average price changes in residential real estate across time. It is derived from transactions involving conforming, conventional mortgages purchased or securitized by Fannie Mae and Freddie Mac. The HPI is widely regarded as a benchmark for evaluating housing affordability and price growth in the U.S.

The dataset used in this project contains:
- `date`: Month and year of the recorded HPI  
- `hpi`: Index value (normalized to a base period)

**Preprocessing**:
- Columns were renamed for clarity  
- Missing or malformed rows were removed (none found for this period)  
- `date` column was converted to `datetime` format  
- Filtered to national monthly values

---

### 📈 Dataset 2: U.S. Unemployment Rate

- **Source**: [FRED – Federal Reserve Economic Data](https://fred.stlouisfed.org)  
- **Origin**: U.S. Bureau of Labor Statistics (BLS)  
- **Coverage Period**: January 2012 – December 2022  
- **Frequency**: Weekly (resampled to monthly)  
- **License**: Public domain (FRED datasets are freely available and reusable without restriction)  
- **Terms of Use**: No copyright or usage restrictions  
- **Download Location**: Data manually downloaded from FRED and saved locally in CSV format

**Description**:  
This dataset contains the national unemployment rate in the U.S., originally recorded on a weekly basis. It measures the percentage of the total labor force that is unemployed but actively seeking employment. This metric is a key indicator of labor market health and broader economic stability.

The dataset includes:
- `date`: The observation week  
- `unemployment_rate`: Percentage of U.S. labor force unemployed

**Preprocessing**:
- Weekly data was aggregated into monthly averages using Pandas `resample()`  
- `date` column was converted to `datetime` and aligned  
- Merged with HPI data on `date` using inner join

---

### 🔄 Integration Process

After preprocessing both datasets:
- Merged on the `date` column using inner join  
- Resulting dataset spans Jan 2012 – Dec 2022  
- Contains `date`, `hpi`, and `unemployment_rate` columns  
- Saved as `data/processed/final_data.csv`

---

### 📦 Summary of Data Sources and Permissions

| Dataset                     | Source        | Frequency        | License               | Use Case in Project                    |
|----------------------------|---------------|------------------|------------------------|-----------------------------------------|
| FHFA Housing Price Index   | Kaggle (FHFA) | Monthly          | Public (non-commercial)| Housing market trend analysis           |
| U.S. Unemployment Rate     | FRED (BLS)    | Weekly → Monthly | Public domain          | Labor market and economic conditions    |

Both datasets were used in accordance with their respective licensing and citation guidelines. The project does not redistribute raw data directly but provides download instructions and preprocessing code to maintain compliance.


---

# 📈 Findings

This analysis examined the relationship between national unemployment rates and U.S. housing prices over the period from 2012 to 2022. Using integrated datasets from the FHFA Housing Price Index (HPI) and the Federal Reserve Economic Data (FRED), the project employed statistical and visual methods to assess how labor market trends relate to housing market dynamics.

---

## 🔍 Key Results

### 📊 Correlation Analysis
The Pearson correlation coefficient between unemployment rate and housing price index was approximately **-0.63**, indicating a **moderate negative correlation**. This suggests that when unemployment rises, housing prices tend to decrease, and vice versa. This inverse relationship aligns with conventional economic theory—higher unemployment typically reduces housing demand due to decreased income security and lending eligibility.

### 📉 Regression Analysis
A simple linear regression model was used to estimate the impact of unemployment on housing prices. The model produced the following key metrics:
- **R² = 0.42**, indicating that unemployment rate alone explains roughly 42% of the variance in housing prices.
- **p-value < 0.01**, confirming the relationship is statistically significant.
- The regression coefficient for unemployment rate was negative, as expected.

This analysis reveals that while unemployment is not the only factor influencing housing prices, it is a meaningful and statistically significant driver over the long term.

---

## 📆 Time-Series Trends
- From **2012 to 2019**, unemployment steadily decreased, and housing prices rose consistently during this period.
- In **2020**, the unemployment rate spiked sharply due to COVID-19, temporarily stalling price growth.
- From **2021 to 2022**, unemployment declined rapidly, and housing prices surged, likely driven by pent-up demand and low interest rates.

These trends were visualized in the time-series plots created during the analysis. A clear parallel was observed between declining unemployment and housing price recovery post-pandemic.

---

## 📷 Visualizations

The following visualizations were generated to support the analysis:

- **`heatmap.png`**: Shows a strong negative correlation between unemployment and housing prices.
- **`timeseries_plot.png`**: Highlights parallel trends between falling unemployment and rising housing prices.
- **`regression_plot.png`**: Depicts the linear relationship with a best-fit line and residuals.
- **`summary.txt`**: Contains full statistical output of the regression model.

All visual outputs can be found in the `/results` directory.

---

## 🧠 Interpretation

The findings suggest that unemployment is a significant, though not exclusive, indicator for housing market trends. While macroeconomic shocks like COVID-19 can create temporary deviations, long-term housing price appreciation tends to align with periods of labor market stability and growth.

However, the R² value of 0.42 also indicates that other factors—such as interest rates, inflation, regional supply-demand dynamics, and demographic shifts—also contribute substantially to price movements. Future models incorporating these variables may yield even stronger explanatory power.

These findings are relevant for economists, policymakers, and real estate professionals aiming to understand and respond to economic cycles in housing markets.

---

# 🔮 Future Work

This project provided valuable insight into the relationship between unemployment and housing prices in the United States from 2012 to 2022. Through this analysis, several lessons were learned—both technical and conceptual—that have helped shape a roadmap for future improvements and extensions.

---

## 🧠 Lessons Learned

One of the most important lessons from this project was the critical role of **data alignment** when dealing with time series datasets of different frequencies. The original unemployment dataset was reported weekly, whereas the housing price index was monthly. Converting the data into a common frequency (monthly) using aggregation techniques like `resample()` in Pandas ensured valid comparisons and smooth integration. This step was simple in theory but required close attention to detail in practice.

Another takeaway was the importance of **data cleaning and preprocessing**. Missing values, inconsistent formatting, and unaligned time ranges initially introduced noise into the regression results. By carefully handling these issues and using inner joins to restrict analysis to matched time periods, the integrity of the analysis was significantly improved.

We also discovered how **automated workflows** like Snakemake can reduce the burden of running multi-step analyses. By setting up a reproducible pipeline with clearly defined inputs and outputs, the project became easier to test, update, and share. This approach minimized the risk of human error and served as a good introduction to scalable, reproducible data science practices.

Lastly, visualizations played a key role in interpreting results. By plotting time series data and regression models, we were able to validate assumptions, detect patterns, and communicate findings more effectively.

---

## 📈 Future Directions

While the current analysis focused solely on the **national relationship** between unemployment and housing prices, there are several promising ways to build upon this foundation:

### 1. **Regional or State-Level Analysis**
Housing markets are highly localized, and national averages often obscure important regional differences. A future version of this project could incorporate FHFA regional HPI data and state-level unemployment figures. This would allow for a comparative analysis of how different states or metro areas respond to economic shifts. It may also uncover regions that are more sensitive to labor market changes.

### 2. **Incorporating Additional Variables**
The current model uses only one independent variable (unemployment rate). Expanding the dataset to include:
- **Mortgage rates** (30-year fixed rate from FRED)
- **Median household income**
- **CPI/inflation**
- **Housing inventory or new housing starts**
could significantly enhance model accuracy. These additional economic indicators could be combined using multivariate regression or machine learning models for improved forecasting and insight.

### 3. **Lagged Effects and Time-Series Forecasting**
Unemployment may not affect housing prices immediately. Exploring **lagged correlations** (e.g., unemployment rates from previous months affecting current housing prices) could reveal delayed responses in the housing market. This approach could be implemented using cross-correlation functions or time-lagged regression.

Alternatively, applying time-series forecasting techniques such as **ARIMA**, **VAR**, or **LSTM neural networks** could help predict future housing price movements based on historical unemployment data.

### 4. **Scenario-Based Simulations**
Incorporating simulated scenarios—for example, projecting housing prices under hypothetical increases in unemployment—could help policymakers assess potential impacts of economic shocks. These models could be enhanced with economic policy parameters (e.g., interest rate cuts, stimulus spending) to evaluate their mitigating effects.

### 5. **Interactive Dashboards**
To make findings more accessible to broader audiences, an interactive dashboard (using Plotly Dash, Streamlit, or Tableau) could visualize trends and allow users to explore “what-if” scenarios. This could be valuable for economists, real estate professionals, and even homeowners trying to understand how macroeconomic conditions influence local property values.

### 6. **Ethical Considerations and Equity**
Although not addressed in this project, future versions could explore whether changes in unemployment and housing affordability disproportionately affect certain demographics or geographic regions. Adding **socioeconomic or demographic overlays** could raise important questions about equity in economic recovery and housing access.

---

## 🌱 Conclusion

Overall, this project served as a strong starting point for understanding how labor market conditions relate to housing prices. While the current results offer meaningful insights, the model can be significantly enriched by introducing more variables, increasing geographic granularity, exploring delayed effects, and building predictive tools. Most importantly, future work should aim to make these insights actionable—helping inform smarter policies and better individual decision-making in uncertain economic times.


---
## 🔁 Steps to Reproduce Results

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/[your-repo-link]
   cd unemployment-housing-analysis
2. **Download Datasets** 
- HPI data from Kaggle → /data/raw/housing_prices.csv
- Unemployment data from FRED → /data/raw/unemployment.csv
3. **Install Dependencies**
pip install -r requirements.txt
4. **Run Snakemake Pipeline**
## 4. Run the Full Pipeline
- Execute the default `reproduce_all` rule by running:
snakemake --cores 1

This will run two scripts:

prepare_data.py — Clean and merge datasets

    a. Reads in two datasets: housing prices and unemployment rates
    b. Aggregates weekly unemployment data into monthly averages
    c. Merges datasets using the date column via an inner join
    d. Saves the cleaned, aligned dataset to data/processed/final_data.csv

analyze_data.py — Generate visualizations and statistical results

    a. Loads the cleaned dataset for analysis
    b. Generates visualizations to explore the relationship between unemployment and housing prices, including:
        - Time-series plot
        - Correlation heatmap
        - Linear regression plot
            c. Performs linear regression to quantify the impact of unemployment on housing prices
        - Outputs model summary (R², p-value)
        - Saves results to results/summary.txt

5. **Expected Outputs**

After running the pipeline, you should expect to see `final_data.csv` in the `data/processed/` folder.

You should also see the following files in the `results/` folder:

| Output File               | Description                                                       |
|---------------------------|-------------------------------------------------------------------|
| heatmap.png               | Correlation heatmap showing the relationship between variables    |
| timeseries_plot.png       | Time-series plot of unemployment rate and housing price trends    |
| regression_plot.png       | Linear regression plot showing fit line and residuals             |
| summary.txt               | Text summary of regression results                                |

6. **Box Folder (Required)**
[Insert your Box share link here]
After downloading, place contents in /data/processed/ and exclude from version control (.gitignore).

---

## References:
BOX LINK: https://uofi.box.com/s/w32esrbd3fvr29t60de4gyhwg7c746rl

US House Price and Mortgage Rate: https://www.kaggle.com/datasets/tiffanytong0321/housepriceandmortgage?resource=download.

Federal Reserve Economic Data (FRED): https://fred.stlouisfed.org/series/UNRATE
