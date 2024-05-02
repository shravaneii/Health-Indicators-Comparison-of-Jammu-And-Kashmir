
# Create Q-Q plot for Reported_Value_for_Public_Facility
plt.figure(figsize=(8, 6))
sm.qqplot(hmis_data['Reported_Value_for_Public_Facility'], line='s')
plt.title('Q-Q Plot for Reported Value for Public Facility')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.show()