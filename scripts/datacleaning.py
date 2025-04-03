import pandas as pd
import os

#Read dataset
mortgage_rate_fred=pd.read_csv('data/30_year_mortgage_rate_2012_2022.csv')
mortgage_rate_fred=mortgage_rate_fred.reset_index(drop=True)
mortgage_and_housing_price=pd.read_csv('data/US House Price And Mortgage Rate.csv')
mortgage_and_housing_price=mortgage_and_housing_price.reset_index(drop=True)

#Data cleaning
mortgage_rate_fred['Date']=pd.to_datetime(mortgage_rate_fred['Date'])
mortgage_and_housing_price.dropna(inplace=True)
mortgage_and_housing_price.rename(columns={'Month': 'Date', 'Mortgage Rate (30-Year Fixed)': 'Mortgage Rate'}, inplace=True)
mortgage_and_housing_price['Date']=pd.to_datetime(mortgage_and_housing_price['Date'])
mortgage_and_housing_price['Date']=mortgage_and_housing_price["Date"].dt.strftime("%Y-%m-%d")

#Data integration
# Merge the datasets on the common timeframe
merged_data = pd.merge(
    mortgage_and_housing_price,
    mortgage_rate_fred,
    how='inner',
    left_on='Mortgage Rate',
    right_on='Mortgage Rate'
)
merged_data.drop(['Date_y'], axis=1, inplace=True)

folder_path='results'
os.makedirs(folder_path, exist_ok=True)
file_path=os.path.join(folder_path, 'merged_data.csv')
merged_data.to_csv(file_path, index=False)
print(f'Dataset has been saved to {file_path}')
