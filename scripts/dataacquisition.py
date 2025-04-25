import requests
import pandas as pd

with open('fred_apikey.txt', 'r') as f:
    apikey=f.readline().strip()
api_key = apikey

#Acquire data from FRED
url = "https://api.stlouisfed.org/fred/series/observations"
params = {
    "series_id": "MORTGAGE30US",        
    "api_key": api_key,
    "file_type": "json",                  
    "observation_start": "2012-01-01",   
    "observation_end": "2022-12-31",
    'frequency': 'm'     
}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    observations = data.get("observations", [])
    if observations:
        df = pd.DataFrame(observations)
        df = df[["date", "value"]]
        df.rename(columns={"date": "Date", "value": "Mortgage Rate"}, inplace=True)
        df["Mortgage Rate"] = pd.to_numeric(df["Mortgage Rate"], errors="coerce")
        df.dropna(inplace=True)
        print(df.head())
        df.to_csv("30_year_mortgage_rate_2012_2022.csv", index=False)
        print("Data saved to 30_year_mortgage_rate_2012_2022.csv")
    else:
        print("No observations found.")
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")

#Read datasets
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