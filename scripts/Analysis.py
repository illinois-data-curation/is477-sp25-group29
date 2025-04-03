import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

merged_data=pd.read_csv('results/merged_data.csv')
#Visualizations
# Set style for visualizations
sns.set(style="whitegrid")

# Plot trends of Housing Price Index, CPI, and Mortgage Rate
fig, ax = plt.subplots(3, 1, figsize=(12, 12), sharex=True)

# FHFA House Price Index
sns.lineplot(data=merged_data, x="Date_x", y="FHFA House Price Index", ax=ax[0], color="blue")
ax[0].set_title("FHFA House Price Index Over Time")
ax[0].set_ylabel("House Price Index")

# Consumer Price Index
sns.lineplot(data=merged_data, x="Date_x", y="Consumer Price Index", ax=ax[1], color="green")
ax[1].set_title("Consumer Price Index (CPI) Over Time")
ax[1].set_ylabel("CPI")

# Mortgage Rate
sns.lineplot(data=merged_data, x="Date_x", y="Mortgage Rate", ax=ax[2], color="red")
ax[2].set_title("30-Year Fixed Mortgage Rate Over Time")
ax[2].set_ylabel("Mortgage Rate (%)")
ax[2].set_xlabel("Year")
plt.xticks([])
plt.tight_layout()
folder_path='results'
os.makedirs(folder_path, exist_ok=True)
file_path=os.path.join(folder_path, 'Visualizations.png')
plt.savefig(file_path)

#Analysis
# Perform data analysis to explore how changes in mortgage rate and CPI affect housing prices

# Calculate correlation matrix to understand relationships
correlation_matrix = merged_data[['Mortgage Rate', 'Consumer Price Index', 'FHFA House Price Index']].corr()
correlation_matrix
# Visualize correlation matrix using heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Correlation Matrix of Housing Prices, Mortgage Rate, and CPI")
folder_path='results'
os.makedirs(folder_path, exist_ok=True)
file_path=os.path.join(folder_path, 'Correlation_heatmap.png')
plt.savefig(file_path)

# Plot scatter plots to visualize relationships
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Scatter plot: Housing Price Index vs Mortgage Rate
sns.scatterplot(data=merged_data, x="Mortgage Rate", y="FHFA House Price Index", ax=ax[0], color="blue")
ax[0].set_title("Housing Price Index vs Mortgage Rate")
ax[0].set_xlabel("Mortgage Rate (%)")
ax[0].set_ylabel("House Price Index")

# Scatter plot: Housing Price Index vs CPI
sns.scatterplot(data=merged_data, x="Consumer Price Index", y="FHFA House Price Index", ax=ax[1], color="green")
ax[1].set_title("Housing Price Index vs Consumer Price Index")
ax[1].set_xlabel("Consumer Price Index")
ax[1].set_ylabel("House Price Index")

plt.tight_layout()
folder_path='results'
os.makedirs(folder_path, exist_ok=True)
file_path=os.path.join(folder_path, 'Relationship_scatterplot.png')
plt.savefig(file_path)

# Fit simple regression models to quantify relationships
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Prepare data
X_mortgage = merged_data["Mortgage Rate"].values.reshape(-1, 1)
X_cpi = merged_data["Consumer Price Index"].values.reshape(-1, 1)
y = merged_data["FHFA House Price Index"]

# Fit regression models
model_mortgage = LinearRegression().fit(X_mortgage, y)
model_cpi = LinearRegression().fit(X_cpi, y)

# Predictions and R-squared values
y_pred_mortgage = model_mortgage.predict(X_mortgage)
y_pred_cpi = model_cpi.predict(X_cpi)

r2_mortgage = r2_score(y, y_pred_mortgage)
r2_cpi = r2_score(y, y_pred_cpi)

folder_path='results'
os.makedirs(folder_path, exist_ok=True)
file_path=os.path.join(folder_path, 'r2_mortgage.txt')
with open(file_path, 'w') as file:
    file.write(f'R² score: {r2_mortgage:.4f}')

folder_path='results'
os.makedirs(folder_path, exist_ok=True)
file_path=os.path.join(folder_path, 'r2_cpi.txt')
with open(file_path, 'w') as file:
    file.write(f'R² score: {r2_cpi:.4f}')