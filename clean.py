
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
import statsmodels.api as sm

# Read the CSV file and store it in a variable named hmis_data
hmis_data = pd.read_csv("/content/drive/MyDrive/DAV_Week1/HMIS-Jammu_and_Kashmir-Kathua-Apr-2021-22.csv")

"""# Replace NAs with the Mean Value"""

# Replace NaNs with mean value for 'Reported_Value_for_Public_Facility'
mean_public_facility = hmis_data['Reported_Value_for_Public_Facility'].mean()
hmis_data['Reported_Value_for_Public_Facility'].fillna(mean_public_facility, inplace=True)

# Replace NaNs with mean value for 'Reported_Value_for_Private_Facility'
mean_private_facility = hmis_data['Reported_Value_for_Private_Facility'].mean()
hmis_data['Reported_Value_for_Private_Facility'].fillna(mean_private_facility, inplace=True)

# Replace NaNs with mean value for 'Reported_Value_for_Rural'
mean_rural = hmis_data['Reported_Value_for_Rural'].mean()
hmis_data['Reported_Value_for_Rural'].fillna(mean_rural, inplace=True)

# Replace NaNs with mean value for 'Reported_Value_for_Urban'
mean_urban = hmis_data['Reported_Value_for_Urban'].mean()
hmis_data['Reported_Value_for_Urban'].fillna(mean_urban, inplace=True)

"""# Dropping the Unwanted Column"""

# Drop the specified columns
hmis_data.drop(['Reported_Value_for_Private_Facility', 'Reported_Value_for_Urban'], axis=1, inplace=True)

# Print the entire DataFrame
hmis_data
