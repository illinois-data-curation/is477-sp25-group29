# 📊 Status Report – Housing Prices and Unemployment Analysis (2012–2022)

Project Title: Exploring the Relationship Between Unemployment Rates and Housing Prices in the United States
Project Lead: Han Huynh
Date: April 24, 2025

---

## 🔍 Project Overview

This project investigates the relationship between unemployment rates and housing prices in the United States from 2012 to 2022. Using integrated data from FRED (unemployment rates, mortgage rates) and Kaggle (housing prices, CPI), the objective is to analyze how labor market conditions influence housing market trends and affordability.

---

## ✅ Task Progress Update

Below is an update on each task outlined in the [Project Plan](link-to-project-plan.md):

### 📁 1. **Data Acquisition and Integration**

- **Status:** ✅ Completed (March 28)
- **Artifacts:**
  - `dataacquisition.py`: Contains API requests to FRED and loading Kaggle dataset.
  - `merged_data.csv`: Final cleaned dataset used for analysis.
- **Highlights:**
  - Used FRED API to fetch monthly unemployment and mortgage rate data.
  - Downloaded housing prices and CPI data from Kaggle.
  - Merged datasets on monthly timestamps for alignment.

---

### 🧹 2. **Data Profiling and Cleaning**

- **Status:** ✅ Completed (April 10)
- **Artifacts:**
  - `dataacquisition.py` (merged and cleaned raw data)
  - `results/merged_data.csv`: Final version post-cleaning
- **Actions Taken:**
  - Addressed missing values and ensured date consistency.
  - Removed structural inconsistencies and standardized naming.
  - Converted date fields to datetime objects and removed duplicates.

---

### 📊 3. **Exploratory Data Analysis (EDA)**

- **Status:** ✅ Completed (April 24)
- **Artifacts:**
- **Status:** ✅ Completed (April 24)

- **Artifacts:**  
  The following table lists all available project artifacts:

  | Artifact File                    | Description                                                                 |
  |----------------------------------|-----------------------------------------------------------------------------|
  | `dataacquisition.py`            | Script used to collect and merge unemployment, mortgage, CPI, and housing price data |
  | `results/merged_data.csv`       | Final cleaned and merged dataset spanning 2012–2022                         |
  | `Analysis.py`                   | Script that performs exploratory analysis, correlation computation, visualizations, and linear regression |
  | `results/time_series_trends.png`| Line plots showing long-term trends for housing price index, CPI, and mortgage rates |
  | `results/correlation_heatmap.png`| Heatmap visualizing correlations between mortgage rate, CPI, and housing prices |
  | `results/scatterplots.png`      | Scatter plots illustrating the relationships between housing prices and key indicators |
  | `results/r2_scores.txt`         | Text file containing R² scores from regression models on CPI and mortgage rates |
  | `ProjectPlan.md`                | Initial plan outlining the project scope, methods, and timeline             |
  | `StatusReport.md`               | This status update, detailing current progress and deviations from the original plan |
  | `README.md`                     | Overview of the project, including purpose, installation instructions, and outcomes (to be finalized) |


- ## 📊 Key Findings (Updated)
📈 Time Series Trends (time_series_trends.png)

The FHFA House Price Index shows a strong and steady upward trajectory, with a sharp increase post-2020.

Consumer Price Index (CPI) also trends consistently upward, with acceleration during 2021–2022, suggesting inflationary pressure.

Mortgage Rates were relatively stable or declining until 2021, followed by a rapid spike in 2022.

🔗 Correlation Matrix (correlation_heatmap.png)

CPI and House Price Index: Extremely strong positive correlation (r = 0.99).

Mortgage Rate and House Price Index: Almost no correlation (r = -0.01), contrary to conventional economic assumptions.

Mortgage Rate and CPI: Weak positive correlation (r = 0.09).

🟢 Scatter Plots (scatterplots.png)

The scatter plot between Mortgage Rate and Housing Price Index shows a dispersed and unclear trend—reinforcing the near-zero correlation.

In contrast, CPI vs. Housing Price Index exhibits a nearly perfect linear relationship, consistent with the high correlation coefficient.

📐 Regression Results (r2_scores.txt)

R² for CPI Model: 0.9821 – CPI explains over 98% of the variation in housing prices.

R² for Mortgage Rate Model: 0.0001 – Mortgage rate explains almost none of the variation in housing prices.

---

### 🤖 4. **Feature Engineering and Model Development**

- **Status:** 🔄 In Progress (Target Completion: April 26)
- **Current Work:**
  - Developing additional features such as lagged unemployment rates.
  - Planning to incorporate multivariate regression models using both CPI and Unemployment Rate.
- **Next Steps:**
  - Evaluate model accuracy using R², RMSE, and visual residual plots.
  - Add unemployment rate features to current regression framework.

---

### 🧾 5. **Documentation**

- **Status:** 🔄 Ongoing
- **Artifacts (so far):**
 - **Status:** ✅ Completed (April 24)

- **Artifacts:**  
  The following table lists all available project artifacts:

  | Artifact File                    | Description                                                                 |
  |----------------------------------|-----------------------------------------------------------------------------|
  | `dataacquisition.py`            | Script used to collect and merge unemployment, mortgage, CPI, and housing price data |
  | `results/merged_data.csv`       | Final cleaned and merged dataset spanning 2012–2022                         |
  | `Analysis.py`                   | Script that performs exploratory analysis, correlation computation, visualizations, and linear regression |
  | `results/time_series_trends.png`| Line plots showing long-term trends for housing price index, CPI, and mortgage rates |
  | `results/correlation_heatmap.png`| Heatmap visualizing correlations between mortgage rate, CPI, and housing prices |
  | `results/scatterplots.png`      | Scatter plots illustrating the relationships between housing prices and key indicators |
  | `results/r2_scores.txt`         | Text file containing R² scores from regression models on CPI and mortgage rates |
  | `ProjectPlan.md`                | Initial plan outlining the project scope, methods, and timeline             |
  | `StatusReport.md`               | This status update, detailing current progress and deviations from the original plan |
  | `README.md`                     | Overview of the project, including purpose, installation instructions, and outcomes (to be finalized) |

- **Next Steps:**
  - Summarize final insights in the final report (due April 30).
  - Include methodology decisions, sources, limitations, and visuals.

---

### 🔁 6. **GitHub Repository and Version Control**

- **Status:** ✅ In Progress and consistent
- **Actions Taken:**
  - All major scripts and data files are version-controlled.
  - Commits reference specific steps in the process (e.g., `eda-complete`, `regression-model-added`)
  - Status report will be tagged with `status-report` upon submission.

---

## 📅 Updated Timeline & Status

| Task                                | Date(s)               | Status         |
|-------------------------------------|------------------------|----------------|
| Scope Definition                    | March 13              | ✅ Done         |
| Data Collection                     | March 21–28           | ✅ Done         |
| Project Plan                        | March 29–April 2      | ✅ Submitted    |
| Data Cleaning & EDA                 | April 3–24            | ✅ Done         |
| Feature Engineering & Modeling      | April 11–26           | 🔄 In Progress  |
| Interim Report                      | April 24              | ✅ Submitted    |
| Final Report & Visualization        | April 26–30           | ⏳ Upcoming     |
| Final Submission                    | May 1                 | ⏳ Upcoming     |

---

## 🔁 Changes from Original Plan

| Area                    | Original Plan                | Current Adjustment                                 |
|-------------------------|------------------------------|----------------------------------------------------|
| Regression Focus        | Initially CPI & Mortgage Rate | Plan to include **Unemployment Rate** in models   |
| Tools Used              | sklearn                      | Added fallback with `numpy` for manual regression  |
| Timeline for Modeling   | April 11–14                  | Extended to April 26 to account for enhancements   |
| Repository Structure    | Final-only visuals           | Now includes all intermediate outputs in `results/`|

---

## 📌 Next Steps

- [ ] Complete multivariate model using CPI + Unemployment Rate
- [ ] Finalize project report with figures and interpretation
- [ ] Push `StatusReport.md` and all artifacts to GitHub
- [ ] Create `status-report` release and submit the GitHub release URL

---

## 📁 File Index (In Repository)

- `dataacquisition.py`: Data collection and merging script
- `merged_data.csv`: Cleaned dataset
- `Analysis.py`: EDA and regression analysis
- `results/`: Folder with all visual outputs and R² scores
- `ProjectPlan.md`: Initial project design
- `StatusReport.md`: This file

---

📌 **Reminder**: Tag your repository release with `status-report` after committing this file and all related artifacts.

Let me know if you'd like help writing the `README.md`, final analysis summary, or formatting this into HTML for a website!

 