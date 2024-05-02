# Select relevant columns
data = hmis_data[['Reported_Value_for_Public_Facility', 'Reported_Value_for_Rural']].dropna()

# Calculate statistics for Reported_Value_for_Public_Facility
avg_public = np.mean(data['Reported_Value_for_Public_Facility'])
median_public = np.median(data['Reported_Value_for_Public_Facility'])
iqr_public = np.percentile(data['Reported_Value_for_Public_Facility'], 75) - np.percentile(data['Reported_Value_for_Public_Facility'], 25)
variance_public = np.var(data['Reported_Value_for_Public_Facility'])

# Print results
print("Reported_Value_for_Public_Facility:")
print(f"Average: {avg_public}")
print(f"Median: {median_public}")
print(f"IQR: {iqr_public}")
print(f"Variance: {variance_public}")

# Calculate statistics for Reported_Value_for_Rural
avg_rural = np.mean(data['Reported_Value_for_Rural'])
median_rural = np.median(data['Reported_Value_for_Rural'])
iqr_rural = np.percentile(data['Reported_Value_for_Rural'], 75) - np.percentile(data['Reported_Value_for_Rural'], 25)
variance_rural = np.var(data['Reported_Value_for_Rural'])

# Print results
print("Reported_Value_for_Rural:")
print(f"Average: {avg_rural}")
print(f"Median: {median_rural}")
print(f"IQR: {iqr_rural}")
print(f"Variance: {variance_rural}")
