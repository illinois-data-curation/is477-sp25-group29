# Project plan

## Research question: What is/are the question(s) you intend to address?

How do changes in unemployment rate affect housing prices in the United States for the past 10 years?

## Week 1: Dataset Integration and Initial Setup

Han's tasks: Acquired the U.S. unemployment rate data from FRED using an API key. The data was converted into a CSV file called unemployment_rate_2012_2022.csv. The script for this acquisition is called dataacquisition.py. As for the dataset on Kaggle, we used this link to download the dataset about U.S. housing prices from 2012 to 2022: Kaggle Housing Prices Dataset.

During this phase, an initial inspection of the datasets will help identify compatibility issues, such as misaligned data points or inconsistencies in date formats. The team will then implement automated Python scripts, using libraries like Pandas and SQLAlchemy, to load and integrate the datasets. This approach will streamline data import processes and establish a reusable codebase for future updates. The integration step will allow for joining datasets based on common fields, ensuring consistency across time intervals. For instance, matching unemployment rates with housing prices by monthly or yearly data points will lay the foundation for a cohesive analysis. Initial challenges, such as data mismatches or formatting inconsistencies

## Week 2: Data Profiling, Cleaning, and Quality Assessment

Han's tasks: Once the datasets are integrated, the focus shifts to data quality, profiling, and cleaning. This stage will involve detailed data profiling using tools like Pandas profiling, which will help summarize key statistics, identify outliers, and detect any missing or inconsistent values. This exploration is crucial for understanding the dataset’s structure and ensuring that it aligns with the analysis requirements. Quality assessment will involve evaluating the completeness and reliability of the data. For instance, any discrepancies in unemployment rate intervals or housing price entries will be flagged and assessed for further cleaning.

During the data cleaning phase, the team will handle issues such as missing values by implementing imputation methods or removing incomplete records, depending on the impact on analysis integrity. Additionally, any format inconsistencies—like differing units or date formats—will be normalized. This step will ensure the datasets are consistent and analysis-ready. Python scripts for cleaning will be created to automate this process, with detailed comments explaining each step to maintain transparency. This documentation will be updated in the README.md file and within the codebase to make the cleaning process easily understandable to future users. Any assumptions made during cleaning will be explicitly stated, ensuring the process remains transparent and reproducible.

## Week 3: Data Cleaning, Analysis, and Workflow Automation

Han's tasks: With the integrated dataset in hand, the third week will focus on cleaning the data to ensure it is analysis-ready. Missing values will be handled using appropriate imputation methods or removal, depending on the context. Format inconsistencies, such as differing date formats or units, will be normalized to maintain consistency. The cleaning process will be automated using Python scripts, with detailed comments added to the codebase to ensure clarity and reproducibility.

Following the cleaning phase, exploratory data analysis (EDA) will begin to address the research question. Summary statistics will be calculated, and visualizations such as line charts comparing unemployment rates and housing price trends over time will be created using libraries like Matplotlib and Seaborn. These visualizations will aim to uncover potential correlations or trends, providing insights into the relationship between unemployment rates and housing prices.

An end-to-end workflow will be developed during this week. The workflow will automate the entire process, from data acquisition to analysis, ensuring that the project can be easily replicated. This workflow will be documented within a Jupyter Notebook or Python script, providing a single executable pipeline for future use.

## Week 4: Documentation, Metadata, and Archiving

Han's tasks: The final week will prioritize thorough documentation and the creation of metadata to ensure the project’s transparency and reproducibility. All code modules will be documented in Markdown, explaining their purpose and functionality. The README.md file will be updated with detailed instructions on running the project, including dependencies, execution steps, and expected outputs.

Metadata describing each dataset, including variable descriptions, transformations, and assumptions made during cleaning, will be created. This metadata will enhance the project’s usability for other researchers. Citations for all data sources and Python libraries used will be included, ensuring proper attribution and adherence to licensing requirements.

The project will be archived in a publicly accessible repository, such as GitHub or Zenodo. A persistent identifier (e.g., DOI) will be generated to ensure long-term accessibility. This archive will include all scripts, documentation, and metadata, creating a comprehensive and reproducible research package.
