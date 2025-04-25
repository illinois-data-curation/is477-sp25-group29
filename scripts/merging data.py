import pandas as pd
import os

# Load and clean unemployment rate data
unemployment_rate_fred = pd.read_csv('data/Unemployment Rate.csv')
unemployment_rate_fred.rename(columns={'observation_date': 'Date', 'UNRATE': 'Unemployment Rate'}, inplace=True)
unemployment_rate_fred['Date'] = pd.to_datetime(unemployment_rate_fred['Date']).dt.strftime('%Y-%m-%d')

# Load and clean housing data
housing_data = pd.read_csv('data/US House Price and Mortgage Rate.csv')
housing_data.rename(columns={'Month': 'Date', 'Mortgage Rate (30-Year Fixed)': 'Mortgage Rate'}, inplace=True)
housing_data = housing_data.dropna().reset_index(drop=True)
housing_data['Date'] = pd.to_datetime(housing_data['Date']).dt.strftime('%Y-%m-%d')

# Merge the datasets on the 'Date' column
merged_data = pd.merge(housing_data, unemployment_rate_fred, on='Date', how='inner')

# Save merged dataset to CSV
output_dir = 'results'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'merged_data.csv')
merged_data.to_csv(output_path, index=False)

print(f'✅ Merged dataset saved to {output_path}')
