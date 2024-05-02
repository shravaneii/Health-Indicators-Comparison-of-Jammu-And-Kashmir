
# Plot box plots for remaining columns
plt.figure(figsize=(10, 6))
sns.boxplot(data=hmis_data[['Reported_Value_for_Public_Facility', 'Reported_Value_for_Rural']])
plt.title('Box Plot of Reported Values for Public Facility and Rural')
plt.ylabel('Reported Value')
plt.xlabel('Category')
plt.xticks(ticks=[0, 1], labels=['Public Facility', 'Rural'])
plt.show()
