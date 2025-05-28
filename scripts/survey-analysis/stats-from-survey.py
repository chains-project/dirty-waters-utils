import pandas as pd
import numpy as np
import os
import sys
import openpyxl
import re
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
survey_data_dir = os.path.join(current_dir, 'survey-data')
survey_data_file = os.path.join(survey_data_dir, 'survey-data.xlsx')
if not os.path.exists(survey_data_file):
    print(f"Error: {survey_data_file} does not exist.")
    sys.exit(1)

try:
    df = pd.read_excel(survey_data_file, engine='openpyxl')
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
if df.empty:
    print("Error: The file is empty.")
    sys.exit(1)

# ignore first column
df = df.iloc[:, 1:]
# next two columns are how many years of experience, and how many years of experience with package managers
experience = df.iloc[:, 0]
package_manager_experience = df.iloc[:, 1]
# next column is which package managers have they used
package_managers = df.iloc[:, 2]
# every column until the last column, not including the last column, is a smell and its severity; they will include the strings "Low", "Medium", "High", or "Critical"
smells = df.iloc[:, 3:-1]
# drop na values
smells = smells.dropna()
suggestions = df.iloc[:, -1]

# check if the smells are in the correct format
for col in smells.columns:
    if not any(smells[col].str.contains('Low|Medium|High|Critical', na=False)):
        print(f"Error: {col} does not contain valid severity levels.")
        sys.exit(1)

# convert the severity levels to numbers
severity_map = {
    'Low': 10,
    'Medium': 20,
    'High': 30,
    'Critical': 40
}
def convert_severity_to_number(severity):
    for key in severity_map.keys():
        if key in severity:
            return severity_map[key]
    return 0

smells = smells.applymap(convert_severity_to_number)
smells_mean = smells.mean().to_dict()
smells_mean = {k: v for k, v in smells_mean.items() if not np.isnan(v)}
print("Mean of each smell:")
for k, v in smells_mean.items():
    print(f"{k}: {v}")

smells_median = smells.median().to_dict()
smells_median = {k: v for k, v in smells_median.items() if not np.isnan(v)}
print("Median of each smell:")
for k, v in smells_median.items():
    print(f"{k}: {v}")

smells_mode = smells.mode().iloc[0].to_dict()
smells_mode = {k: v for k, v in smells_mode.items() if not np.isnan(v)}
print("Mode of each smell:")
for k, v in smells_mode.items():
    print(f"{k}: {v}")